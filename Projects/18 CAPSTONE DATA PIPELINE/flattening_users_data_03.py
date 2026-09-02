import logging
import logger_config
logger = logging.getLogger(f"project_18_logger.{__name__}")
from data_transformation_02 import transforming_data, data
users = transforming_data(data)
print(len(users))

def data_flattening(users):
    logger.info("Flattening The Users Data...")
    final_users = []
    for user in users:
        final_user = {
            'id' : user['id'],
            'fullName' : user['firstName'] + " " + user['lastName'],
            'email' : user['email'],
            'age' : user['age'],
            'city' : user['city'],
            'company' : user['company']
        }
        final_users.append(final_user)
    logger.info("Flattening Complete")
    return final_users


final_users = data_flattening(users)