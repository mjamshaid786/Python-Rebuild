import logging
logger = logging.getLogger("project_12_logger")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
file_handler = logging.FileHandler("project_12.log",mode='a')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

import csv
def load_file():
    try:
        with open ("sales.csv", "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)
            return data
    except FileNotFoundError:
        logger.warning("File not found !")
        return False

#================================
#       SALES PROCESSING
#================================
def sales_processing(data):
    revenue = 0
    invalid_records = 0
    for sale in data:
        try:
            price  = int(sale['price'])
            quantity = int(sale['quantity'])
            revenue_by_row = price * quantity
            logger.info(f"{sale['order_id']} Processed Successfully !")
            revenue += revenue_by_row
        except ValueError:
            logger.error("Invalid Value found. Skipped")
            invalid_records += 1
    return revenue, invalid_records






#========================================
#       FUNCTIONS CALLINGS
#========================================
logger.info("Sales Processing Started...")  
data = load_file()
if data == False:
    logger.info("Ensure file path or file existance")
logger.info("File Successfully Loaded !")

logger.info("Getting Sales Revenue")
total, invalid_records = sales_processing(data)
logger.info("Revenue Generated Successfully !")
print(total)
logger.info("Processing Completed Successfully !")

#=====================================
#           FINAL REPORT
#=====================================

print("=" * 30)
print("         SALES PROCESSOR         ")
print(f"{'=' * 30}\n")
print(f"Records Processed: {len(data)}")
print(f"Invalid Records : {invalid_records}")
print(f"Total Sales :  Rs. {total}\n")
print("Processing Completed Successfully !")
