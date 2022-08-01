import logging

'''
logging.info("First informational message!")
logging.critical("This is serious!")

logger = logging.getLogger()
logger = logging.Logger("MYLOGGER")

logger.info("Logger successfully created!")
logger.log(logging.INFO, "Successful!")
logger.critical("Critical Message!")
logger.log(logging.CRITICAL, "Critical!")

for handler in logging.root.handlers:
    logging.root.removeHandler(handler)
logging.basicConfig(level=logging.INFO)
'''


logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logfile.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s: %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.info("This will get into the file!")
