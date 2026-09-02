import logging
import logger_config
logger = logging.getLogger(f"project_18_logger.{__name__}")
#----- Importing Function From Other Files -----
from api_client import getting_api_data

#==============================================
#                   MAIN
#==============================================
data = getting_api_data()
if data:
    print(type(data))