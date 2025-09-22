import requests #데이터 불러오는 요청주소

url = 'https://www.hollys.co.kr/store/korea/korStore2.do?'
#  서버에 보낼 데이터 (1페이지를 보여달라는 의미)
from_data = {
    'page' : 1,
    'sido' :'',
    'gungun' : '',
    'store' : ''
}
response = requests.post(url,data=from_data)
print(response.text[:500])