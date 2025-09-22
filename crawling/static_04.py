import os, pymysql
from dotenv import load_dotenv
import coffeedb
import tqdm

load_dotenv()

def get_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST', '127.0.0.1'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', '1234'),
        database=os.getenv('DB_NAME', 'shopinfo'),
        charset='utf8mb4',
        autocommit=False
    )

for page_num in tqdm.tqdm(range(1, 47)):
    datas = coffeedb.get_data(page_num)  # [(area, name, state, addr, phone), ...]
    if not datas:
        continue

    with get_connection() as conn:
        with conn.cursor() as cur:
            for data in datas:
                try:
                    insert_sql = """
                        INSERT INTO shop_base2_tbl
                            (shop_area, shop_name, shop_state, shop_addr, shop_phone_number)
                        VALUES (%s, %s, %s, %s, %s)
                    """
                    cur.execute(insert_sql, (data[0], data[1], data[2], data[3], data[4]))
                except pymysql.err.IntegrityError:
                    update_sql = """
                        UPDATE shop_base2_tbl
                        SET shop_state=%s, shop_addr=%s, shop_phone_number=%s
                        WHERE shop_area=%s AND shop_name=%s
                    """
                    cur.execute(update_sql, (data[2], data[3], data[4], data[0], data[1]))
            # 🔑 페이지당 한 번만 커밋
            conn.commit()
