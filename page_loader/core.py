from page_loader.naming import get_resource_filename, get_dir_name
from page_loader.validator import validate_user_input, get_valid_response
from page_loader.resources import get_resources, download_resources
from page_loader.log import get_logger
import os

logger = get_logger(__name__)


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

    return html_path
