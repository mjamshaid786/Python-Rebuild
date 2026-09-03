import logging, requests
import logger_config
logger = logging.getLogger(f"project_18_logger.{__name__}")

def getting_api_data():
    logger.info("Getting Data From API...")
    API_URL = "https://dummyjson.com/users"
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        
        return response.json()
    except requests.exceptions.ConnectionError as c:
        logger.error(f"Connection ERROR !: {c}")
        return None
    except requests.exceptions.Timeout as t:
        logger.error(f"Timeout ERROR !: {t}")
        return None
    except requests.exceptions.HTTPError as h:
        logger.error(f"HTTP error !: {h}")
        return None
    except requests.RequestException as e:
        logger.error(f"ERROR !: {e}")
        return None


