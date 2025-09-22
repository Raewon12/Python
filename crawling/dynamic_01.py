from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #enter키 등을 입력하기위해서 
import time 

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.saramin.co.kr/')
print('브라우저가 성공적으로 열렸습니다.')
#driver.quit()
#검색창 요소 찾기(id 가 'ipt_keyword_recruit'인 input태그를 찾음)
search_input = driver.find_element(By.ID,'ipt_keyword_recruit')
#검색창에 파이썬 입력 
search_input.send_keys("파이썬")
time.sleep(3)
#enter키 누르기
search_input.send_keys(Keys.Enter)
 #대략 3초정도 페이지 로드 될떄까지 기다림..
#driver.quit()