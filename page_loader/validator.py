from page_loader.log import get_logger
import validators
import requests
import sys
import os

logger = get_logger(__name__)


def validate_user_input(url, path):
    if not os.path.exists(path) or not os.path.isdir(path):
        logger.critical("Directory not exists")
        sys.exit(1)

    if not os.access(path, os.W_OK):
        logger.critical(f"Need permission to write in: {path}")
        sys.exit(1)

    if not validators.url(url):
        logger.critical(f"Invalid url: {url}")
        sys.exit(1)


def get_valid_response(url):
    try:
        response = requests.get(url, stream=True, timeout=10)
        status_code = response.status_code
        if 300 <= status_code < 600:
            logger.debug(f'connection error: {status_code}')
            raise ConnectionError(
                "Bad request",
                url
            )

    except (requests.exceptions.ConnectionError, ConnectionError) as error:
        # logger.critical(f"{error.args[0]}, url: {error.args[1]}")
        sys.exit(1)

    return response
