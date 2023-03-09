from page_loader.log import get_logger
import page_loader.core
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
        response = requests.get(url)
        response.raise_for_status()

        status_code = response.status_code
        logger.info(f'got a {response} from {url}')

        if 300 <= status_code < 600:
            raise ConnectionError

    except (requests.exceptions.RequestException, ConnectionError) as error:
        logger.critical(f"{error}, url: {url}")
        raise page_loader.core.AppError(
            "Network error! See log for more details."
        ) from error

    return response
