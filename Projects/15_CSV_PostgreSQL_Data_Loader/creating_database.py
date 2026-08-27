#==============================================
#           IMPORTING LIBRARIES
#==============================================

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
logger.info("Loading .env variables...")
load_dotenv(dotenv_path)
logger.info(".env loaded successfull!")
#==============================================
#           CREATING DATABASE
#==============================================
def creating_database(db_name):
    try:
        logger.info("connection PostgresSQL...")
        conn = psycopg2.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        port=os.getenv("port")) 

        conn.autocommit = True
        
        logger.info("Connection Successfull !")
        with conn.cursor() as cur:
            logger.info("Creating Database...")
            cur.execute(f"CREATE DATABASE {db_name} ;")
            logger.info("Database created successfully !")
        conn.close()
    except Exception as e:
        print(f"Exception : {e}")

