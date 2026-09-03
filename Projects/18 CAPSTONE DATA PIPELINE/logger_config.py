import logging
logger = logging.getLogger("project_18_logger")
logger.setLevel(logging.DEBUG)

#------------- OUTPUT IN TERMINAL ----------------
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

#------------- OUTPUT IN LOG FILE ------------------
file_handler = logging.FileHandler("project_18.log",mode='a')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
