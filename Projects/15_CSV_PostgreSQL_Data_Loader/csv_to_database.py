import csv, os
import psycopg2
import logging
logger = logging.getLogger("project_15_logger")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
file_handler = logging.FileHandler("project_15.log",mode='a')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
from psycopg2.extras import execute_values



def csv_to_postgresql(tb_name):
    try:
        logger.info("Creating Connection With Database...")
        with psycopg2.connect(
            host=os.getenv("host"),
            dbname=os.getenv("dbname"),
            user=os.getenv("user"),
            port=os.getenv("port"),
            password=os.getenv("password")) as conn:

            logger.info("Connection Success !")

            with conn.cursor() as cur:
                logger.info("Adding rows to data...")
                with open ('final_users_data.csv', 'r') as file:
                    reader = csv.reader(file)
                    next(reader)
                    query = f"""
                    --sql
                    INSERT INTO {tb_name} (id, name, email, age, city, company) VALUES %s ON CONFLICT (id) DO NOTHING
                    ;
                    """
                    execute_values(cur, query, list(reader))
                    logger.info("Data Inserted !")
    except Exception as error:
        logger.error(error)

