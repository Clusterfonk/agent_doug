from logging.handlers import RotatingFileHandler
import logging


def set_up_logger(log_path):
    logging.basicConfig(
        handlers=[RotatingFileHandler(filename=log_path, backupCount=10)],
        format="[%(asctime)s] [%(levelname)s] [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.INFO
    )
