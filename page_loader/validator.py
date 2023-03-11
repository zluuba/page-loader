from page_loader.log import get_logger
import page_loader.core
import validators
import requests
import os


logger = get_logger(__name__)


def validate_user_input(url, path):
    if not os.path.exists(path) or not os.path.isdir(path):
        logger.critical("Directory not exists")
        raise page_loader.core.AppError("Directory not exists")

    if not os.access(path, os.W_OK):
        logger.critical(f"Need permission to write in: {path}")
        raise page_loader.core.AppError("No access to path")

    if not validators.url(url):
        logger.critical(f"Invalid url: {url}")
        raise page_loader.core.AppError("Invalid URL")


def get_valid_response(url):
    try:
        response = requests.get(url)
        logger.info(f'got a response: {response}, url: {url}')

        response.raise_for_status()

    except (requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
            requests.exceptions.MissingSchema,
            requests.exceptions.InvalidSchema) as error:
        logger.critical(error)
        raise page_loader.core.AppError(
            "Network error. See log for more details."
        ) from error

    return response
