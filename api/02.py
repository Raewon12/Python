from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from db_chan import get_connection
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
URL = 'https://www.melon.com/chart/'

def start_dynamic_option():
    driver.get(URL)
    driver.maximize_window()
    time.sleep(1)
    museic_num= driver.find_element(By.CSS_SELECTOR,'lst50 > td:nth-child(2) > div > span.rank : 순위')
    #lst50 > td:nth-child(2) > div > span.rank : 순위
    