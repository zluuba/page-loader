import page_loader.core
import validators
import requests
import os


class AppError(Exception):
    pass


def validate_user_input(url, path):
    if not os.path.exists(path) or not os.path.isdir(path):
        page_loader.core.logger.critical("Directory not exists")
        raise AppError("Directory not exists")

    if not os.access(path, os.W_OK):
        page_loader.core.logger.critical(
            f"Need permission to write in: {path}"
        )
        raise AppError("No access to path")

    if not validators.url(url):
        page_loader.core.logger.critical(f"Invalid url: {url}")
        raise AppError("Invalid URL")


def get_valid_response(url):
    try:
        response = requests.get(url)
        page_loader.core.logger.info(
            f'got a response: {response}, url: {url}'
        )

        response.raise_for_status()

    except requests.exceptions.RequestException as error:
        page_loader.core.logger.critical(error)
        raise AppError(
            "Network error. See log for more details."
        ) from error

    return response
