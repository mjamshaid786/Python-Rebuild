import psycopg2
import os
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
with psycopg2.connect(
            host=os.getenv("host"),
            dbname=os.getenv("dbname"),
            user=os.getenv("user"),
            port=os.getenv("port"),
            password=os.getenv("password")) as conn:
    with conn.cursor() as cur:
        query = """
        --sql
        SELECT * FROM users WHERE city = 'Columbus'
        ;
        """
        cur.execute(query)
        user = cur.fetchall()
        print(user)
    
