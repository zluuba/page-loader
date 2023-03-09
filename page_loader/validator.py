from page_loader.log import get_logger
import validators
import requests
import sys
import os

logger = get_logger(__name__)


def validate_user_input(url, path):
    if not os.path.exists(path) or not os.path.isdir(path):
        logger.critical(f"path does not exist: {path}")
        sys.exit(f"Directory doesn't exist: {path}.")

    if not os.access(path, os.W_OK):
        logger.critical(f"have not access to path: {path}")
        sys.exit(f"You don't have access to write in: {path}")

    if not validators.url(url):
        logger.critical(f"invalid url: {url}")
        sys.exit(f"Incorrect url: {url}")


def get_valid_response(url):
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code != 200:
            raise ConnectionError

    except (requests.exceptions.ConnectionError, ConnectionError) as error:
        logger.critical(f"connection error: {ConnectionError}, "
                        f"url: {url}")
        sys.exit(f"Connection error: {error}. "
                 "Try again later or check that the URL is working correct.")

    return response
