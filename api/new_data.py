import pandas as pd
from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parent
xlsx_path = BASE_DIR / "2023_12_car.xlsx"
SHEET = "10.연료별_등록현황"

raw = pd.read_excel(xlsx_path, sheet_name=SHEET, header=None)

# 헤더 찾기
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

# 연료 열 위치(내용 기반)
targets_src = ["휘발유", "경유", "LPG", "CNG"]
fuel_col_idx, best_hits = None, -1
for c in data.columns:
    s = data[c].astype(str)
    hits = sum(s.str.contains(t, na=False).sum() for t in targets_src)
    if hits > best_hits:
        best_hits, fuel_col_idx = hits, c

# 시도/용도 열 위치(내용 기반)
sido_col_idx, best_sogye = None, -1
for c in data.columns:
    cnt = data[c].astype(str).str.fullmatch(r"\s*소계\s*").sum()
    if cnt > best_sogye:
        best_sogye, sido_col_idx = cnt, c

yongdo_col_idx, best_y = None, -1
yong_tokens = ["비사업용", "사업용", "계"]
for c in data.columns:
    s = data[c].astype(str)
    cnt = sum(s.str.contains(tok, na=False).sum() for tok in yong_tokens)
    if cnt > best_y:
        best_y, yongdo_col_idx = cnt, c

def to_num(x):
    x = str(x).replace(",", "").strip()
    return pd.to_numeric(x, errors="coerce")

# 연료명 정규화: 공백 제거, 대문자화, 엘피지→LPG
def norm_fuel(x: str):
    s = str(x).strip().upper()
    s = re.sub(r"\s+", "", s)
    if "휘발유" in x:
        return "휘발유"
    if "경유" in x:
        return "경유"
    if "엘피지" in x or "LPG" in s:
        return "LPG"
    if "CNG" in s:
        return "CNG"
    return None

fuel_norm = data[fuel_col_idx].astype(str).apply(norm_fuel)

# 기본 마스크: 시도=소계 & 용도=계 (정확일치)
sido_is_sogye = data[sido_col_idx].astype(str).str.fullmatch(r"\s*소계\s*", na=False)
yong_is_gye   = data[yongdo_col_idx].astype(str).str.fullmatch(r"\s*계\s*",   na=False)
base_mask = sido_is_sogye & yong_is_gye

# 추출
picked = []
for src, outname in [("휘발유","gasoline"), ("경유","disel"), ("LPG","lpg"), ("CNG","cng")]:
    m = (fuel_norm == src) & base_mask
    rows = data.loc[m, [fuel_col_idx, seoul_col_idx]].copy()

    # Fallback: 혹시 구조가 달라 base_mask로 못 잡히면, 해당 행의 다른 열들 어딘가에 '소계'와 '계'가 모두 포함되는지로 재검사
    if rows.empty:
        obj_cols = data.select_dtypes(include="object").columns
        tmp_m = (fuel_norm == src)
        tmp = data.loc[tmp_m, obj_cols].astype(str)
        mask_fb = tmp.apply(lambda r: ("소계" in "".join(r)) and ("계" in "".join(r)), axis=1)
        rows = data.loc[tmp_m[tmp_m.index[mask_fb]].index, [fuel_col_idx, seoul_col_idx]].copy()

    if not rows.empty:
        total = to_num(rows.iloc[0, 1])
        picked.append((outname, int(total) if pd.notna(total) else None))
    else:
        picked.append((outname, None))  # 못 찾으면 None 표시

for name, val in picked:
    if val is None:
        print(f"{name}\t(값 없음)")
    else:
        print(f"{name}\t{val}")
