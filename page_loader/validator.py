from page_loader.log import get_logger
import validators
import requests
import sys
import os

logger = get_logger(__name__)


class RedirectError(Exception):
    pass


class ClientError(Exception):
    pass


class ServerError(Exception):
    pass


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
        if 300 <= status_code < 400:
            raise RedirectError(
                "Need further action to complete the request",
                url
            )
        if 400 <= status_code < 500:
            raise ClientError(
                "the request contains bad syntax or cannot be fulfilled",
                url
            )
        if 500 <= status_code < 600:
            raise ServerError(
                "the server failed to fulfil an apparently valid request",
                url
            )

    except requests.exceptions.ConnectionError as error:
        logger.critical(f"{error.args[0]}, url: {error.args[1]}")
        sys.exit(1)

    except RedirectError as error:
        logger.warning(f"{error.args[0]}, url: {error.args[1]}")
        sys.exit(1)

    except ClientError as error:
        logger.critical(f"{error.args[0]}, url: {error.args[1]}")
        sys.exit(1)

    except ServerError as error:
        logger.critical(f"{error.args[0]}, url: {error.args[1]}")
        sys.exit(1)

    return response
