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
import dotenv
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv() #Find the .env folder automatically
load_dotenv(dotenv_path)
db_config = os.getenv("db_config")








#==============================================
#           CREATING DATABASE
#==============================================
def creating_database(db_name):
    print("OK")

creating_database("db")