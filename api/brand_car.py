# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys # enter키 등을 입력하기 위해서
# from bs4 import BeautifulSoup
# from db_chan import get_connection
# import pymysql
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# URL = 'https://stat.eseoul.go.kr/statHtml/statHtml.do?orgId=201&tblId=DT_201004_I020004&conn_path=I2&obj_var_id=&up_itm_id='

# def start_dynamic_option_setting():
#     driver.get(URL)
#     driver.maximize_window() 
#     time.sleep(1)   
#     setting_btn = driver.find_element(By.CSS_SELECTOR, "#header > div > div.titleRight > a.btnStaSet")
#     setting_btn.click()
#     time.sleep(3)
    
#     # iframe 전환
#     iframe = driver.find_element(By.ID, "ifrSearchDetail")
#     driver.switch_to.frame(iframe)

#     # 종류 삭제
#     car_variable_delete_btn = driver.find_element(By.XPATH, '//*[@id="ifr_pop_selectAll2"]/div/div/div[3]/div[1]/div[2]/ul[2]/li[2]/img[2]')
#     car_variable_delete_btn.click()
#     time.sleep(3)
    
#     # 종류 전체 선택
#     car_all_select = driver.find_element(By.ID, 'selectLeft_1')
#     car_all_selected = Select(car_all_select)
#     all = '001@1'
#     car_all_selected.select_by_value(all)
#     time.sleep(3)

#     # 종류 전체 추가
#     car_add_btn = driver.find_element(By.XPATH, '//*[@id="ifr_pop_selectAll2"]/div/div/div[3]/div[1]/div[2]/ul[2]/li[1]/img[2]')
#     car_add_btn.click()
#     time.sleep(3)

#     # 기간 전체 선택
#     period_all_add_btn = driver.find_element(By.XPATH, '//*[@id="ifr_pop_selectAll2"]/div/div/div[3]/div[3]/div/div[2]/ul[3]/li[1]/img[1]')
#     period_all_add_btn.click()
#     time.sleep(3)
    
#     # 적용 버튼
#     apply_btn = driver.find_element(By.XPATH, '//*[@id="ifr_pop_selectAll2"]/div/div/div[4]/span/a')
#     driver.execute_script("arguments[0].click();", apply_btn)
#     driver.switch_to.default_content()
#     time.sleep(3)

# def crawl_data():
#     from bs4 import BeautifulSoup
#     import re

#     html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')

#     # 표 찾기 (페이지마다 id가 다를 수 있어 두 개 다 시도)
#     table = soup.select_one('#mainTableT') or soup.select_one('#mainTable')
#     if table is None:
#         raise RuntimeError("통계 표를 찾지 못했습니다. (#mainTableT / #mainTable)")

#     # ----- 헤더 처리 -----
#     thead_rows = table.select('thead tr')
#     if not thead_rows:
#         raise RuntimeError("표 thead를 찾지 못했습니다.")

#     # 보통 2번째 tr이 연료유형 라인이므로 우선 사용
#     header_tr = thead_rows[1] if len(thead_rows) >= 2 else thead_rows[0]
#     header_cells = [th.get_text(strip=True) for th in header_tr.select('th, td')]
#     header = [(h if h else "") for h in header_cells]
#     idx_to_label = {i: header[i] for i in range(len(header))}

#     # 친환경 키워드
#     eco_keys = ['하이브리드', '전기', '수소']

#     # ----- 본문 처리 -----
#     rows = []
#     for tr in table.select('tbody tr'):
#         # 연도/시점 텍스트 추출
#         th = tr.select_one('th')
#         if th:
#             ytxt = th.get_text(strip=True)
#         else:
#             tds0 = tr.select('td')
#             if not tds0:
#                 continue
#             ytxt = tds0[0].get_text(strip=True)

#         m = re.search(r'(\d{4})', ytxt)
#         if not m:
#             # 합계/소계 같은 비연도 행은 건너뛴다
#             continue
#         year = int(m.group(1))

#         # 값 셀들 숫자 변환
#         tds = tr.select('td')
#         vals = []
#         for td in tds:
#             txt = td.get_text(strip=True).replace(',', '')
#             if txt in ('', '-'):
#                 txt = '0'
#             try:
#                 vals.append(int(float(txt)))
#             except:
#                 vals.append(0)

#         # 값 열은 보통 헤더의 인덱스 1부터 대응(0은 연도/시점 헤더 칸)
#         # 길이 안 맞으면 0 채움
#         need_len = max(0, len(header) - 1)
#         if len(vals) < need_len:
#             vals += [0] * (need_len - len(vals))

#         eco_sum = 0
#         non_eco_sum = 0
#         for i, v in enumerate(vals, start=1):
#             label = idx_to_label.get(i, "")
#             if any(k in label for k in eco_keys):
#                 eco_sum += v
#             else:
#                 # 완전 공백 라벨은 무시
#                 if label:
#                     non_eco_sum += v

#         rows.append((year, eco_sum, non_eco_sum))

#     print(f"수집 행 수: {len(rows)}")
#     if rows[:3]:
#         print("샘플:", rows[:3])
# # 해당사이트에서 크롤링 하기
# # 크롤링 할 데이터는 년도별, 친환경차(하이브리드,전기,수소)와 비환경(그 외)로 나눠서 수집
# # 크롤링 한 데이터를 mysql에 넣기
# #환경
# #mainTableT > thead > tr:nth-child(2) > th:nth-child(7) > span:nth-child(2)->하이브리드
# #mainTableT > thead > tr:nth-child(2) > th:nth-child(5) > span:nth-child(2)-> 전기
# #mainTableT > thead > tr:nth-child(2) > th:nth-child(8) > span:nth-child(2)-> 수소
# #mainTableT > thead > tr:nth-child(2) > th:nth-child(6) > cng
# # vs비환경
# ##mainTableT > thead > tr:nth-child(2) > th:nth-child(2) > span:nth-child(2)-> 휘발유
# #mainTableT > thead > tr:nth-child(2) > th:nth-child(3) > span:nth-child(2) -> 경유
# #mainTableT > thead > tr:nth-child(2) > th:nth-child(4) > LPG
# ddl = """
#     CREATE TABLE IF NOT EXISTS seoul_car_fuel_by_year (
#         year INT PRIMARY KEY,
#         eco_total BIGINT NOT NULL,
#         non_eco_total BIGINT NOT NULL,
#         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#     ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
#     """
# upsert = """
#     INSERT INTO seoul_car_fuel_by_year (year, eco_total, non_eco_total)
#     VALUES (%s, %s, %s)
#     ON DUPLICATE KEY UPDATE
#       eco_total = VALUES(eco_total),
#       non_eco_total = VALUES(non_eco_total);
#     """
# ddl = """
#     CREATE TABLE IF NOT EXISTS seoul_car_fuel_by_year (
#         year INT PRIMARY KEY,
#         eco_total BIGINT NOT NULL,
#         non_eco_total BIGINT NOT NULL,
#         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#     ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
#     """
# upsert = """
#     INSERT INTO seoul_car_fuel_by_year (year, eco_total, non_eco_total)
#     VALUES (%s, %s, %s)
#     ON DUPLICATE KEY UPDATE
#       eco_total = VALUES(eco_total),
#       non_eco_total = VALUES(non_eco_total);
#     """
# conn = get_connection()
# try:
#         with conn.cursor() as cur:
#             cur.execute(ddl)
#             cur.executemany(upsert, rows)
#         conn.commit()
#         print(f"MySQL 저장 완료: {len(rows)}건")
# except Exception as e:
#         conn.rollback()
#         print("DB 저장 실패:", e)
#         raise
# finally:
#         conn.close()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time, re
from db_chan import get_connection   # ← 같은 폴더에 db_chan.py 있어야 함!

URL = "https://stat.eseoul.go.kr/statHtml/statHtml.do?orgId=201&tblId=DT_201004_I020004&conn_path=I2&obj_var_id=&up_itm_id="

# ---------------- 1) 크롬 드라이버 생성 ----------------
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# ---------------- 2) 옵션 설정 ----------------
def start_dynamic_option_setting():
    driver.get(URL)
    driver.maximize_window()
    time.sleep(1)

    # 상단 옵션 버튼
    driver.find_element(By.CSS_SELECTOR, "#header > div > div.titleRight > a.btnStaSet").click()
    time.sleep(2)

    # iframe 전환
    iframe = driver.find_element(By.ID, "ifrSearchDetail")
    driver.switch_to.frame(iframe)

    # 종류 삭제 -> 전체 추가
    driver.find_element(By.XPATH, '//*[@id="ifr_pop_selectAll2"]/div/div/div[3]/div[1]/div[2]/ul[2]/li[2]/img[2]').click()
    time.sleep(1)

    Select(driver.find_element(By.ID, 'selectLeft_1')).select_by_value('001@1')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="ifr_pop_selectAll2"]/div/div/div[3]/div[1]/div[2]/ul[2]/li[1]/img[2]').click()
    time.sleep(1)

    # 기간 전체 선택
    driver.find_element(By.XPATH, '//*[@id="ifr_pop_selectAll2"]/div/div/div[3]/div[3]/div/div[2]/ul[3]/li[1]/img[1]').click()
    time.sleep(1)

    # 적용 버튼
    apply_btn = driver.find_element(By.XPATH, '//*[@id="ifr_pop_selectAll2"]/div/div/div[4]/span/a')
    driver.execute_script("arguments[0].click();", apply_btn)
    driver.switch_to.default_content()
    time.sleep(2)

# ---------------- 3) 행렬 전환 ----------------
def do_matrix_swap():
    steps = [
        ('//*[@id="ico_swap"]/a', 3),
        ('//*[@id="Ri0"]', 1),
        ('//*[@id="pop_pivotfunc2"]/div[2]/div[1]/div[2]/p/a[2]/img', 1),
        ('//*[@id="Le0"]', 1),
        ('//*[@id="pop_pivotfunc2"]/div[2]/div[1]/div[1]/div/span/a[2]/img', 1),
        ('//*[@id="pop_pivotfunc2"]/div[2]/div[2]/span/a', 1)
    ]
    for xpath, wait in steps:
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(wait)

# ---------------- 4) 표 로딩 대기 ----------------
def wait_for_table():
    TABLE_SELECTORS = ["#mainTableT", "#mainTable"]
    try:
        for css in TABLE_SELECTORS:
            return WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css))
            )
    except TimeoutException:
        raise RuntimeError("표 로딩 대기 시간 초과!")

# ---------------- 5) 표 파싱 및 DB 저장 ----------------
def save_monthly_to_db():
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    table = soup.select_one("#mainTableT") or soup.select_one("#mainTable")
    if table is None:
        raise RuntimeError("표를 찾지 못했습니다.")

    # 헤더 (연료명)
    header_tr = table.select("thead tr")[1]
    headers = [h.get_text(strip=True) for h in header_tr.select("th,td")]
    idx_to_label = {i: headers[i] for i in range(len(headers))}

    FUEL_MAP = {
        "휘발유": ("ice", "gasoline"),
        "경유": ("ice", "diesel"),
        "LPG": ("ice", "lpg"),
        "CNG": ("ice", "cng"),
        "하이브리드": ("eco", "hev"),
        "플러그인": ("eco", "phev"),
        "전기": ("eco", "ev"),
        "수소": ("eco", "fcev")
    }

    def to_int(txt):
        t = txt.strip().replace(",", "")
        return int(float(t)) if t not in ("", "-") else 0

    dim_rows, eco_rows, ice_rows = {}, {}, {}
    for tr in table.select("tbody tr"):
        th = tr.select_one("th")
        if not th:
            continue
        txt = th.get_text(strip=True)
        ym = re.findall(r"\d+", txt)
        if len(ym) < 2:  # 연월 아니면 패스
            continue
        year, month = int(ym[0]), int(ym[1])
        date_key = year * 100 + month
        dim_rows[date_key] = (year, month)

        vals = tr.select("td")
        for i, td in enumerate(vals, start=1):
            label = idx_to_label.get(i, "")
            val = to_int(td.get_text())
            for key, (bucket, col) in FUEL_MAP.items():
                if key in label:
                    if bucket == "eco":
                        eco_rows.setdefault(date_key, {"ev":0,"hev":0,"phev":0,"fcev":0})
                        eco_rows[date_key][col] += val
                    else:
                        ice_rows.setdefault(date_key, {"gasoline":0,"diesel":0,"lpg":0,"cng":0})
                        ice_rows[date_key][col] += val

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS dim_month(
                date_key INT PRIMARY KEY,
                year INT, month INT
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """)
            cur.execute("""
            CREATE TABLE IF NOT EXISTS eco_monthly(
                date_key INT PRIMARY KEY,
                ev INT, hev INT, phev INT, fcev INT,
                FOREIGN KEY (date_key) REFERENCES dim_month(date_key)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """)
            cur.execute("""
            CREATE TABLE IF NOT EXISTS ice_monthly(
                date_key INT PRIMARY KEY,
                gasoline INT, diesel INT, lpg INT, cng INT,
                FOREIGN KEY (date_key) REFERENCES dim_month(date_key)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """)

            cur.executemany("INSERT INTO dim_month VALUES (%s,%s,%s) ON DUPLICATE KEY UPDATE year=VALUES(year), month=VALUES(month)",
                            [(k,v[0],v[1]) for k,v in dim_rows.items()])
            cur.executemany("INSERT INTO eco_monthly VALUES (%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE ev=VALUES(ev), hev=VALUES(hev), phev=VALUES(phev), fcev=VALUES(fcev)",
                            [(k,d["ev"],d["hev"],d["phev"],d["fcev"]) for k,d in eco_rows.items()])
            cur.executemany("INSERT INTO ice_monthly VALUES (%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE gasoline=VALUES(gasoline), diesel=VALUES(diesel), lpg=VALUES(lpg), cng=VALUES(cng)",
                            [(k,d["gasoline"],d["diesel"],d["lpg"],d["cng"]) for k,d in ice_rows.items()])
        conn.commit()
        print(f"[저장완료] dim:{len(dim_rows)}, eco:{len(eco_rows)}, ice:{len(ice_rows)}")
    finally:
        conn.close()

# ---------------- 메인 실행 ----------------
start_dynamic_option_setting()
do_matrix_swap()
wait_for_table()
save_monthly_to_db()
driver.quit()
