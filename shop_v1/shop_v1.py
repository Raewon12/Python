import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

conn = pymysql.connect(
    host=os.getenv('DB_HOST', '127.0.0.1'),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASSWORD', '1234'),
    database=os.getenv('DB_NAME', 'mydb'),
    charset='utf8mb4',
    autocommit=False
)
print('접속성공')

def create_customer(customer_id,name):
    sql = 'INSERT INTO customer (customer_id, name) VALUES (%s, %s)'
    with conn.cursor() as cur:
        cur.execute(sql, (customer_id,name))  # ✅ 튜플로 바인딩
    conn.commit()
    print('고객추가 완료')

def readAll_customers(isDict=False):
    sql = 'SELECT * FROM customer'
    result = []
    if isDict:
        with conn.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(sql)
            for c in cur.fetchall():
                print(f"{c['customer_id']}  {c['name']}")
    else:
        with conn.cursor() as cur:
            cur.execute(sql)
            for c in cur.fetchall():
                print(f'{c[0]}  {c[1]}')
                result.append({"회원아이디": c[0], "회원이름": c[1]})
    print('조회완료')
    return result

def update_customer(customer_id, name):
    sql = '''
        UPDATE customer
           SET name = %s
         WHERE customer_id = %s
    '''
    with conn.cursor() as cur:
        cur.execute(sql, (name, customer_id))  # ✅ 순서 (name, id)
    conn.commit()
    print(f'업데이트 되었습니다. id={customer_id}, name={name}')

def delete_customer(customer_id):
    sql = 'DELETE FROM customer WHERE customer_id=%s'
    with conn.cursor() as cur:
        cur.execute(sql, (customer_id,))  # ✅ 튜플로 바인딩
    conn.commit()
    print(f'삭제되었습니다. id={customer_id}')

if __name__ == "__main__":
    print("테스트 실행")
    create_customer('abc')
    readAll_customers()
    update_customer(1, 'abc')
    delete_customer(1)
