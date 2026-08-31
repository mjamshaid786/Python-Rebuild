import psycopg2, os
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

try:
    conn = psycopg2.connect(
        host=os.getenv('host'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        port=os.getenv('port')
    )

    conn.autocommit = True

    with conn.cursor() as cur:
        cur.execute("CREATE DATABASE realtime_sales ;")
        print("Database Created")
    conn.close()
except Exception as e:
    print("Failed to Connect with Database !", e)
