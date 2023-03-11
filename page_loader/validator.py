from page_loader.log import get_logger
import page_loader.core
import validators
import requests
import os


logger = get_logger(__name__)


def validate_user_input(url, path):
    if not os.path.exists(path) or not os.path.isdir(path):
        logger.critical("Directory not exists")
        raise page_loader.core.AppError(
            "Directory not exists"
        )

    if not os.access(path, os.W_OK):
        logger.critical(f"Need permission to write in: {path}")
        raise page_loader.core.AppError(
            "No access to path"
        )

    if not validators.url(url):
        logger.critical(f"Invalid url: {url}")
        raise page_loader.core.AppError(
            "Invalid URL"
        )


def get_valid_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        status_code = response.status_code
        logger.info(f'got a {response} from {url}')

        if 300 <= status_code < 600:
            raise ConnectionError

    except (requests.exceptions.RequestException, ConnectionError) as error:
        logger.critical(error)
        raise page_loader.core.AppError(
            "Network error! See log for more details."
        ) from error

    return response
