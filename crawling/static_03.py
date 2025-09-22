# static_03.py
import os
import pymysql
from dotenv import load_dotenv
import coffeedb

load_dotenv()

def insert_hollys():
    conn = pymysql.connect(
        host=os.getenv('DB_HOST', '127.0.0.1'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', '1234'),
        database=os.getenv('DB_NAME', 'shopinfo'),
        charset='utf8mb4',
        autocommit=False
    )

    data = coffeedb.get_data()  # ✅ 오타 수정(getd_data -> get_data)

    if not data:
        print("크롤링 결과가 0건입니다. CSS 선택자나 요청 파라미터를 확인하세요.")
        conn.close()
        return

    try:
        with conn:
            with conn.cursor() as cur:
                sql = """
                    INSERT INTO shopinfo.shop_base_tbl
                    VALUES (NULL, %s, %s, %s, %s, %s)
                """
                cur.executemany(sql, data)
            conn.commit()
            print("INSERT 건수:", len(data))
    except Exception as e:
        print("DB 에러:", e)
        conn.rollback()
    
if __name__ == "__main__":
    insert_hollys()

