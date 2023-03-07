import logging
import sys


logger = logging.getLogger('logger_name')
FORMAT = '[%(asctime)s:%(levelname)s] %(message)s'
logging.basicConfig(format=FORMAT)

handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.INFO)
logger.addHandler(handler)

handler.setLevel(logging.WARNING)
logger.addHandler(handler)
