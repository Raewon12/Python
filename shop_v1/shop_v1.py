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

# C - Create
def create_customer(name: str) -> int:
    sql = 'INSERT INTO customer (name) VALUES (%s)'
    with conn.cursor() as cur:
        cur.execute(sql, (name,))          # 반드시 튜플로!
        new_id = cur.lastrowid
    conn.commit()
    print(f'고객추가완료: {name} (id={new_id})')
    return new_id

# R - Read
def read_all_customers(is_dict: bool = False):
    sql = 'SELECT customer_id, name FROM customer ORDER BY customer_id'
    cursor_cls = pymysql.cursors.DictCursor if is_dict else None
    with conn.cursor(cursor=cursor_cls) as cur:
        cur.execute(sql)
        rows = cur.fetchall()
    if not rows:
        print('조회결과 없음')
    else:
        for r in rows:
            if is_dict:
                print(f"{r['customer_id']} {r['name']}")
            else:
                print(f"{r[0]} {r[1]}")
    print('조회완료')

# U - Update
def update_customer(customer_id: int, name: str):
    sql = '''
        UPDATE customer
           SET name = %s
         WHERE customer_id = %s
    '''
    with conn.cursor() as cur:
        cur.execute(sql, (name, customer_id))  # (name, id) 순서!
    conn.commit()
    print(f'수정완료: id={customer_id} -> name={name}')

# D - Delete
def delete_customer(customer_id: int):
    sql = 'DELETE FROM customer WHERE customer_id = %s'
    with conn.cursor() as cur:
        cur.execute(sql, (customer_id,))       # 튜플로!
    conn.commit()
    print(f'삭제완료: id={customer_id}')

if __name__ == '__main__':
    try:
        # 동작 확인
        new_id = create_customer('이순신')
        read_all_customers(is_dict=True)
        # update_customer(new_id, '유관순')
        # delete_customer(new_id)
        # read_all_customers(is_dict=True)
    finally:
        conn.close()
