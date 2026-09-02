import logging
from main import data
import logger_config
logger = logging.getLogger(f"project_18_logger.{__name__}")

if data:
    logger.info("Data Received Successfully.")
    clean_user = []

