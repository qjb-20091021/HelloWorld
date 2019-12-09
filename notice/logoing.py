import logging
def log():
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler("server_log.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s- %(thread)d -%(filename)s-- %(funcName)s - %(levelname)s -[line:%(lineno)d] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

    # logger.info("Start print log")
    # logger.debug("Do something")
    # logger.warning("Something maybe fail.")
    # logger.info("Finish")