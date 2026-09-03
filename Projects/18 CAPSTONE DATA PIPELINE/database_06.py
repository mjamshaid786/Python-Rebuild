import logging
import logger_config
logger = logging.getLogger(f"project_18_logger.{__name__}")

import psycopg2, os
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
logger.info("Creating Connection With Database")
try:
    conn = psycopg2.connect(
        host=os.getenv('host'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        port=os.getenv('port')
    )
    logger.info("Database Connected.")
    conn.autocommit = True

    with conn.cursor() as cur:
        try:
            cur.execute("CREATE DATABASE capstone_pipeline ;")
            logger.info("Database Created")
        except Exception as e:
            logger.error(f"ERROR: {e}")

except Exception as e:
    logger.error(f"Failed to Connect with Database ! {e}")


#------- table -------
try:
    conn = psycopg2.connect(
        host=os.getenv('host'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        port=os.getenv('port'),
        dbname=os.getenv('dbname')
    )
    logger.info("Database Connected.")
    with conn.cursor() as cur:
        try:
            cur.execute("""
            --sql
            CREATE TABLE IF NOT EXISTS users(
                    id INT PRIMARY KEY, 
                    full_name VARCHAR NOT NULL, 
                    email VARCHAR, 
                    age INT, 
                    city VARCHAR, 
                    company VARCHAR, 
                    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
            ;
            """)
            conn.commit()
            logger.info("Table Created.")
        except Exception as e:
            logger.error(f"ERROR: {e}")


except Exception as e:
    logger.error(f"Failed to Connect with Database ! {e}")