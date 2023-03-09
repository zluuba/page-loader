from page_loader.log import get_logger
import validators
import requests
import sys
import os

logger = get_logger(__name__)


def validate_user_input(url, path):
    if not os.path.exists(path) or not os.path.isdir(path):
        logger.critical("Directory not exists")
        sys.exit(f"Directory doesn't exist: {path}.")

    if not os.access(path, os.W_OK):
        logger.critical(f"Need permission to write in: {path}")
        sys.exit(f"You don't have access to write in: {path}")

    if not validators.url(url):
        logger.critical(f"Invalid url: {url}")
        sys.exit(f"Incorrect url: {url}")


def get_valid_response(url):
    try:
        response = requests.get(url, stream=True, timeout=10)
        status_code = response.status_code
        if 300 <= status_code < 400:
            raise ConnectionError(
                "Need further action to complete the request",
                url
            )
        if 400 <= status_code < 500:
            raise ConnectionError(
                "the request contains bad syntax or cannot be fulfilled",
                url
            )
        if 500 <= status_code < 600:
            raise ConnectionError(
                "the server failed to fulfil an apparently valid request",
                url
            )

    except (requests.exceptions.ConnectionError, ConnectionError) as error:
        logger.critical(f"{error.args[0]}, "
                        f"url: {error.args[1]}")
        sys.exit(1)

    return response
