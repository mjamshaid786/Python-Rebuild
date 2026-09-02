import logging, requests, json
import logger_config
logger = logging.getLogger(f"project_18_logger.{__name__}")

def getting_api_data():
    API_URL = "https://dummyjson.com/users"
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json
    except requests.exceptions.ConnectionError:
        print("Connection ERROR !")
    except requests.exceptions.Timeout:
        print("Timeout ERROR !")


getting_api_data()

