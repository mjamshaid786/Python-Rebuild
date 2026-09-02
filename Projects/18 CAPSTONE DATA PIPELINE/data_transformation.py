import logging
from main import data
import logger_config
logger = logging.getLogger(f"project_18_logger.{__name__}")
def traforming_data(data):
    if data:
        logger.info("Data Received Successfully.")
        logger.info("Getting Required Features From Raw Data")
        clean_users = []
        for user in data['users']:
            clean_user = {
                'id' : user.get('id', 'N/A'),
                'firstName' : user.get('firstName', 'N/A'),
                'lastName' : user.get('lastName', 'N/A'),
                'email' : user.get('email', 'N/A'),
                'age' : user.get('age', 'N/A'),
                'city': user.get('address', {}).get('city', 'N/A'),
                'company': user.get('company', {}).get('city', 'N/A')
            }
            clean_users.append(clean_user)
        logger.info("Required Features Received Successfully.")
        return clean_user