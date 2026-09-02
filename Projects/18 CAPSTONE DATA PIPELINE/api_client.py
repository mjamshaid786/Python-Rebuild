import logging, requests, json
import logger_config
logger = logging.getLogger(f"project_18_logger.{__name__}")

def getting_api_data():
    API_URL = "https://dummyjson.com/users"
    reponse = requests.get(API_URL, timeout=10)
    data = json.load(reponse)
    print(data)

getting_api_data()

