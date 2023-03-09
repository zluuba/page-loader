import validators
import requests
import sys
import os


def validate_user_input(url, path):
    if not os.path.exists(path) or not os.path.isdir(path):
        sys.exit(f"Directory doesn't exist: {path}.")

    if not os.access(path, os.W_OK):
        sys.exit(f"You don't have access to write in: {path}")

    if not validators.url(url):
        sys.exit(f"Incorrect url: {url}")


def get_valid_response(url):
    try:
        response = requests.get(url, stream=True, timeout=10)
        if not response.ok:
            raise ConnectionError

    except (requests.exceptions.ConnectionError, ConnectionError) as error:
        sys.exit(f"Connection error: {error}. "
                 "Try again later or check that the URL is working correct.")

    return response
