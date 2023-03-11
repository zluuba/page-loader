import page_loader.core
import validators
import requests
import os


class AppError(Exception):
    pass


def validate_user_input(url, path):
    if not validators.url(url):
        page_loader.core.logger.critical(f"Invalid url: {url}")
        raise AppError(f"Invalid URL: {url}")

    if not os.path.exists(path) or not os.path.isdir(path):
        page_loader.core.logger.critical(
            f"Directory does not exists: {path}"
        )
        raise AppError(f"Directory does not exists: {path}")

    if not os.access(path, os.W_OK):
        page_loader.core.logger.critical(
            f"Need permission to write in: {path}"
        )
        raise AppError(f"Have no write permission to path: {path}")


def get_valid_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        if response.status_code >= 300:
            raise AppError(
                "Network error. See log for more details."
            )

    except requests.exceptions.RequestException as error:
        page_loader.core.logger.critical(error)
        raise AppError(
            "Network error. See log for more details."
        ) from error

    return response
