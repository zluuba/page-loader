from page_loader.common import get_resource_filename, get_dir_name
from page_loader.resources import get_resources
import validators
import requests
import logging
import sys
import os


def download(url, path=None):
    if not path:
        path = os.getcwd()

    if not os.path.exists(path) or not os.path.isdir(path):
        raise FileExistsError("Directory doesn't exist.")

    if not os.access(path, os.W_OK):
        raise PermissionError(f"You don't have access to write in: {path}")

    if not validators.url(url):
        raise ValueError(f"Incorrect url: {url}")

    logging.info(f"user input. url: {url}, path: {path}")

    try:
        response = requests.get(url, stream=True, timeout=10)
        status_code = response.status_code
        logging.info(f"response status code: {status_code}")
        if not response.ok:
            raise ConnectionError

    except (requests.exceptions.ConnectionError, ConnectionError) as error:
        sys.exit(f"Connection error: {error}. "
                 "Try again later or check that the URL is working correct.")

    resources_dir_name = get_dir_name(url)
    resources_dir_path = os.path.join(path, resources_dir_name)

    html_name = get_resource_filename(url)
    html_path = os.path.join(path, html_name)

    html_page, resources = get_resources(url, response.text, path)

    with open(html_path, 'w') as file:
        file.write(html_page)

    logging.info(f"html-page was downloaded. path: {html_path}")

    if resources:
        if not os.path.exists(resources_dir_path):
            os.mkdir(resources_dir_path)

        logging.info(f"start download resources to {resources_dir_path}")
        for resource in resources:
            url = resource['url']
            filename = resource['filename']
            resource_path = os.path.join(resources_dir_path, filename)
            download_resource(url, resource_path)
            logging.info(f"start download {filename}. url: {url}")

    return html_path


def download_resource(url, path):
    response = requests.get(url, stream=True)
    if response.ok:
        data = response.content
        with open(path, 'wb') as file:
            file.write(data)
        logging.info(f"resource was successfully downloaded: '{path}'")
    else:
        logging.error(f"response error: {response.status_code}")
