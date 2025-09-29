from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1) 멜론 차트 크롤링
url = "https://www.melon.com/chart/"
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(url)

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tr[id^='lst']"))
)

score_rows = driver.find_elements(By.CSS_SELECTOR, '#frm tr[id^="lst"]')

melon_songs = []
for r in score_rows[:5]:  # Top 5만 예시로
    title = r.find_element(By.CSS_SELECTOR,"div.ellipsis.rank01 a").text.strip()
    artist = ", ".join(a.text.strip() for a in r.find_elements(By.CSS_SELECTOR, "div.ellipsis.rank02 a"))
    melon_songs.append(f"{title} {artist}")

driver.quit()

print("멜론 Top 5 곡:", melon_songs)

# 2) 유튜브 검색
youtube_url = "https://www.youtube.com/"
driver = webdriver.Chrome(service=service)
driver.get(youtube_url)

for song in melon_songs:
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
    search_box.clear()
    search_box.send_keys(song)
    search_box.send_keys(Keys.ENTER)

    # 검색결과 로딩 기다림
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "video-title"))
    )

    # 상위 1~3개 영상만 추출
    videos = driver.find_elements(By.ID, "video-title")[:3]

    print(f"\n🔎 [{song}] 검색 결과")
    for v in videos:
        title = v.get_attribute("title")
        link = v.get_attribute("href")
        print(f"- {title}\n  ({link})")

driver.quit()
