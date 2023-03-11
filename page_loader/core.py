from page_loader.naming import get_resource_filename, get_dir_name
from page_loader.validator import validate_user_input, get_valid_response
from page_loader.resources import get_resources
from progress.bar import IncrementalBar
from page_loader.log import get_logger
import requests
import os


logger = get_logger(__name__)


class AppError(Exception):
    pass


def download(url, path):
    validate_user_input(url, path)
    logger.info(f"requested url: {url}")
    logger.info(f"output path: {path}")

    response = get_valid_response(url)

    resources_dir_name = get_dir_name(url)
    resources_dir_path = os.path.join(path, resources_dir_name)

    html_name = get_resource_filename(url + '.html')
    html_path = os.path.join(path, html_name)

    html_page, resources = get_resources(
        url, response.text, resources_dir_name
    )

    with open(html_path, 'w') as file:
        file.write(html_page)

    logger.info(f"write html file: {html_path}")

    if resources:
        download_resources(resources_dir_path, resources)
    else:
        logger.info("No possible resources to download")

    return html_path


def download_resources(resources_dir_path, resources):
    if not os.path.exists(resources_dir_path):
        logger.info(f"create directory for assets: {resources_dir_path}")
        try:
            os.mkdir(resources_dir_path)
        except OSError as error:
            logger.critical(f"Error: {error}. Can't create dir for resources")
            raise AppError("Can't create dir for resources") from error

    for resource in IncrementalBar('Downloading: ').iter(resources):
        url, filename = resource['url'], resource['filename']
        path = os.path.join(resources_dir_path, filename)

        response = requests.get(url, stream=True)
        if response.ok:
            data = response.content
            with open(path, 'wb') as file:
                file.write(data)
        else:
            logger.error(f"can't download file: {url}.\n"
                         f"{response.status_code}.")
