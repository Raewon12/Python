# update_fuel_monthly.py
import re
import os
import pandas as pd
import pymysql
from pathlib import Path
from dotenv import load_dotenv

# ------------------ 1) 엑셀에서 202312 값 추출 ------------------
BASE_DIR = Path(__file__).resolve().parent
XLSX = BASE_DIR / "2023_12_car.xlsx"     # 파일명 맞게
SHEET = "10.연료별_등록현황"
DATE_KEY = 202312

raw = pd.read_excel(XLSX, sheet_name=SHEET, header=None)

# 헤더 줄 찾기(‘연료’와 ‘서울’이 같이 있는 줄)
header_idx = None
for i in range(min(40, len(raw))):
    row = raw.iloc[i].astype(str).fillna("")
    if ("연료" in "".join(row)) and ("서울" in "".join(row)):
        header_idx = i
        break
if header_idx is None:
    raise RuntimeError("헤더 행을 찾지 못했습니다.")

data = raw.iloc[header_idx+1:].reset_index(drop=True).copy()

# '서울' 열 위치
seoul_col_idx = int((raw.iloc[header_idx].astype(str).fillna("").str.contains("서울")).idxmax())

# 연료/시도/용도 열 위치(내용 기반 추정)
keys_for_fuel_locate = ["휘발유","경유","LPG","CNG","전기","하이브리드","플러그","수소"]
fuel_col_idx, best_hits = None, -1
for c in data.columns:
    s = data[c].astype(str)
    hits = sum(s.str.contains(k, na=False).sum() for k in keys_for_fuel_locate)
    if hits > best_hits:
        best_hits, fuel_col_idx = hits, c

# 시도: '소계' 정확히 많이 나오는 열
sido_col_idx, best_sogye = None, -1
for c in data.columns:
    cnt = data[c].astype(str).str.fullmatch(r"\s*소계\s*").sum()
    if cnt > best_sogye:
        best_sogye, sido_col_idx = cnt, c

# 용도: '비사업용/사업용/계'가 자주 나오는 열
yongdo_col_idx, best_y = None, -1
for c in data.columns:
    s = data[c].astype(str)
    cnt = s.str.contains("비사업용|사업용|계", na=False).sum()
    if cnt > best_y:
        best_y, yongdo_col_idx = cnt, c

def to_num(x):
    x = str(x).replace(",", "").strip()
    return pd.to_numeric(x, errors="coerce")

# 연료명 정규화 → 테이블 컬럼명으로
def norm_conv_fuel(x: str):
    s_raw = str(x)
    s = s_raw.upper().replace(" ", "")
    if "휘발유" in s_raw:
        return "gasoline"
    if "경유" in s_raw:
        return "diesel"
    if "엘피지" in s_raw or "LPG" in s or "액화석유" in s_raw:
        return "lpg"
    if "CNG" in s:
        return "cng"
    return None

fuel_norm = data[fuel_col_idx].astype(str).apply(norm_conv_fuel)

# 정확 매칭: 시도=소계 & 용도=계
sido_is_sogye = data[sido_col_idx].astype(str).str.fullmatch(r"\s*소계\s*", na=False)
yong_is_gye   = data[yongdo_col_idx].astype(str).str.fullmatch(r"\s*계\s*",   na=False)
base_mask = sido_is_sogye & yong_is_gye

needed = ["gasoline","diesel","lpg","cng"]
picked = {}

for key in needed:
    m = (fuel_norm == key) & base_mask
    rows = data.loc[m, [fuel_col_idx, seoul_col_idx]].copy()
    # Fallback: 같은 행의 다른 열 문자열 합쳐서 '소계'와 '계' 동시 포함이면 채택
    if rows.empty:
        obj_cols = data.select_dtypes(include="object").columns
        tmp_idx = (fuel_norm == key)
        tmp = data.loc[tmp_idx, obj_cols].astype(str)
        mask_fb = tmp.apply(lambda r: ("소계" in "".join(r)) and ("계" in "".join(r)), axis=1)
        idx = mask_fb[mask_fb].index
        rows = data.loc[idx, [fuel_col_idx, seoul_col_idx]].copy()

    picked[key] = int(to_num(rows.iloc[0, 1])) if not rows.empty else 0

print("\n[PREVIEW] 202312 서울 연료별:", picked)  # 예: {'gasoline': 1658706, 'diesel': 1008457, 'lpg': 203451, 'cng': 7799}

# ------------------ 2) MySQL 업서트 ------------------

# ... (위에서 엑셀 -> picked 딕셔너리까지는 그대로)
# picked 예: {'gasoline': 1658706, 'diesel': 1008457, 'lpg': 222468, 'cng': 7799}

import os, pymysql
from dotenv import load_dotenv

DATE_KEY = 202312  # 이번 달 키

load_dotenv()
conn = pymysql.connect(
    host=os.getenv("DB_HOST", "127.0.0.1"),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", "1234"),
    database="1st_project",          # ✅ 스키마 고정
    charset="utf8mb4",
    autocommit=False,
)

try:
    with conn.cursor() as cur:
        # 1) dim_month 선삽입 (FK 대비) — 컬럼이 date_key 하나만 있다고 가정
        cur.execute("INSERT IGNORE INTO `1st_project`.`dim_month` (date_key) VALUES (%s)", (DATE_KEY,))

        # 2) ice_monthly 업서트
        sql = """
        INSERT INTO `1st_project`.`ice_monthly` (date_key, gasoline, diesel, lpg, cng)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
          gasoline = VALUES(gasoline),
          diesel   = VALUES(diesel),
          lpg      = VALUES(lpg),
          cng      = VALUES(cng)
        """
        cur.execute(sql, (
            DATE_KEY,
            int(picked.get("gasoline", 0)),
            int(picked.get("diesel", 0)),
            int(picked.get("lpg", 0)),
            int(picked.get("cng", 0)),
        ))

    conn.commit()
    print(f"[OK] 1st_project.ice_monthly 업서트 완료: {DATE_KEY} -> {picked}")
except Exception as e:
    conn.rollback()
    raise
finally:
    conn.close()
