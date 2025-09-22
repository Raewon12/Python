#데이터 베이스 연결
# 환경변수를 읽어와야함
#os를 이용해서 환경변수의 값을 읽어서 connection 객체를 생성
# 커넥션 객체의 cursor객체를 생성
#커서 객체의 callproc('프로시저이름',[,,,,])
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

conn = pymysql.connect(
    host=os.getenv('DB_HOST', '127.0.0.1'),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASSWORD', '1234'),
    database=os.getenv('DB_NAME', 'sqldb'),
    charset='utf8mb4',
    autocommit=False
)
print('DB접속성공')

try:
    with conn.cursor() as cursor:
        cursor.callproc('AddCodeWithTransaction',['PRODUCT','P1001','소보루빵',0,'Y'])
        for row in cursor.fetchall():
            print(row)
    conn.commit()

except Exception as e:
    print(f"에러 발생: {e}")
    conn.rollback()

finally:
    conn.close()

#프로시저 호출