import logging.config
import sys
# import os


FORMAT = "%(levelname)s:%(message)s"
# LOG_FILE = os.path.join(
#     os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
#     f'{__name__}.log'
# )


class Handler:
    def __init__(self, stream=sys.stdout, level='INFO', formatter=FORMAT):
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

    info_handler = Handler()
    logger.addHandler(info_handler.set_handler())

    error_handler = Handler(stream=sys.stderr, level='ERROR')
    logger.addHandler(error_handler.set_handler())
    return logger
