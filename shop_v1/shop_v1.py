import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

conn = pymysql.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)
print('접속성공')

# 2. 각 테이블별 CRUD
# C - insert 
# R - select
# U - update
# D - delte
# 3 메소드
#고객-customer 
def create_customer(name):
    sql = 'insert into customer values(null,%s)'
    cur = conn.cursor()
    cur.execute(sql,'이순신')
    conn.commit()
    print('고객추가완료')

def readAll_customers(isDict = False):
    sql= 'select *from customer'

    if isDict:
        
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(sql)
        for c in cur.fetchall():
            print(f"{c['customer_id']} {c['name']}")
    else: 
        cur = conn.cursor()
        cur.execute(sql)
        for c in cur.fetchall():
            #print(f'{c[0]} {c[1]}')    
            print(f'{c[0]}  {c[1]}')
    print('조회완료')

def update_customer(customer_id,name):
    sql = '''
        update customer 
            set name = %s
        where customer_id = %s
    '''
    with conn.cursor() as cur:
        cur.execute(sql, (customer_id,name)  )    
    conn.commit()



conn.close()
#  회원가입
#  상품정보출력
#  상품구입
#  상품정보 입력
#  대쉬보드 : 고객별 상품별 구매회수 평균구매액

# 4. 기능구현과 테스트가 되면 streamlit으로 ui구성 -- 템플릿 화면을 보고 유사하 형태로 구혀