import logging.config
from logging import FileHandler, StreamHandler
import sys

FORMAT = "%(levelname)s:%(name)s:%(message)s"


def set_handler(handler, level='DEBUG', formatter=FORMAT):
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter(formatter))


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    info_handler = StreamHandler(sys.stdout)
    set_handler(info_handler)
    logger.addHandler(info_handler)

    log_to_file_handler = FileHandler(__name__)
    set_handler(log_to_file_handler, level='ERROR')
    logger.addHandler(log_to_file_handler)
    return logger
