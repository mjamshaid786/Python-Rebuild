#==============================================
#           IMPORTING LIBRARIES
#==============================================

#-------------- FOR LOGGING ---------------
import logging
logger = logging.getLogger("mytestlogger")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
file_handler = logging.FileHandler("my_test_data.log",mode='a')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#-------------- FOR CSV ---------------
import csv
#-------------- FOR PostgreSQL ---------------
import psycopg2

#==============================================
#           CREATING DATABASE
#==============================================
def creating_database(db_name):
    print("OK")