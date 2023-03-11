import logging.config
from logging import FileHandler
import sys

FORMAT = "%(levelname)s:%(name)s:%(message)s"


class Handler:
    def __init__(self, stream=sys.stdout, level='NOTSET', formatter=FORMAT):
        self.stream = stream
        self.level = level
        self.formatter = formatter

    def set_handler(self):
        handler = logging.StreamHandler(self.stream)
        handler.setLevel(self.level)
        handler.setFormatter(logging.Formatter(self.formatter))
        return handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    info_handler = Handler(level='DEBUG')
    logger.addHandler(info_handler.set_handler())

    log_to_file_handler = FileHandler(__name__)
    log_to_file_handler.setLevel('ERROR')
    log_to_file_handler.setFormatter(logging.Formatter(FORMAT))
    logger.addHandler(log_to_file_handler)
    return logger
