#pip install pymysql
import pymysql
<<<<<<< HEAD
from dotenv import load_dotenv
import os 
load_dotenv()
# 1 .DB연결
conn = pymysql.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
=======
# 1 .DB연결
conn = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '1234',
    database='mydb'
>>>>>>> 3849f5e4c7bd77d97f454ec720ca5376171b3465
)
print('접속성공')
conn.close()

# 2. 각 테이블별 CRUD
# C - insert 
# R - select
# U - update
# D - delte
# 3 메소드
 #회원가입
 #상품정보출력
 #상품구입
 #상품정보 입력
 #대쉬보드 : 고객별 상품별 구매회수 평균구매액

# 4. 기능구현과 테스트가 되면 streamlit으로 ui구성 -- 템플릿 화면을 보고 유사하 형태로 구혀