#==============================================
#           IMPORTING LIBRARIES
#==============================================
#-------------- IMPORTING FUNCTIONS -----------
from creating_database import creating_database

#-------------- FOR LOGGING ---------------
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

#-------------- FOR CSV ---------------
import csv
#-------------- FOR PostgreSQL ---------------
import psycopg2 # --> pip install psycopg2
#-------------- FOR .ENV ---------------
import os
# import dotenv
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv() #Find the .env folder automatically

#-------------- Creating table in databse -----------

def creating_table(tb_name):
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
                logger.info("Creating Table...")
                query = f"""--sql
                CREATE TABLE IF NOT EXISTS {tb_name}(
                id      INT PRIMARY KEY,
                name    VARCHAR NOT NULL,
                email   VARCHAR,
                age     INT,
                city    VARCHAR,
                company VARCHAR );
                """
                cur.execute(query)
                logger.info("Table Created !")
                conn.commit()
    except Exception as error:
        logger.error(error)