# db_chan.py
import pymysql
import os
from dotenv import load_dotenv

# .env 파일에서 DB 설정 읽어오기
load_dotenv()

def get_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST', '127.0.0.1'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', '1234'),
        database=os.getenv('DB_NAME', 'sqldb'),
        charset='utf8mb4',
        autocommit=False
    )
