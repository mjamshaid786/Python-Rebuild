import psycopg2, os
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

try:
    conn = psycopg2.connect(
        host=os.getenv('host'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        port=os.getenv('port'),
        dbname=os.getenv('dbname')
    )


    with conn.cursor() as cur:
        cur.execute("""
        --sql
        CREATE TABLE IF NOT EXISTS sales (
                    order_id INT PRIMARY KEY,
                    product VARCHAR NOT NULL,
                    price INT,
                    quantity INT,
                    total INT
                    )
        ;
        """)
        conn.commit()
        print("Table Created ")
except Exception as e:
    print("Failed to Connect with Database !", e)
