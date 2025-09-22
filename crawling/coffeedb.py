# coffeedb.py
import requests
from bs4 import BeautifulSoup

def get_data(page_num):
    url = 'https://www.hollys.co.kr/store/korea/korStore2.do?'
    form_data = {
        'pagNo': page_num,
        'sido': '',
        'gungun': '',
        'store': ''
    }
    res = requests.post(url, data=form_data)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')

    # 꼭 tr까지 선택해야 row를 가져옴
    rows = soup.select('#contents > div.content > fieldset > fieldset > '
                       'div.tableType01 > table > tbody > tr')

    stores = []
    for row in rows:
        tds = row.select('td')
        if len(tds) >= 6:  # 방어 코드
            stores.append((
                tds[0].text.strip(),  # 지역
                tds[1].text.strip(),  # 매장명
                tds[2].text.strip(),  # 현황
                tds[3].text.strip(),  # 주소
                tds[5].text.strip(),  # 전화번호
            ))
    return stores

if __name__ == "__main__":
    # 테스트 출력
    data = get_data()
    print("rows:", len(data))
    for r in data[:5]:
        print(r)
