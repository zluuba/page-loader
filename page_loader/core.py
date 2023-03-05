from page_loader.common import get_html_filename
from page_loader.resources import get_resources
import validators
import requests
import os


def download(url, path=None):
    if not path:
        path = os.getcwd()
    if not validators.url(url):
        # print('Incorrect URL')
        return None

    try:
        response = requests.get(url, stream=True, timeout=10)
        if not response.ok:
            raise ConnectionError
    except (requests.exceptions.ConnectionError, ConnectionError):
        # print("Bad connection")
        return None

    html_name = get_html_filename(url)
    html_path = os.path.join(path, html_name)
    html_page = get_resources(url, response.text, path)

    with open(html_path, 'w') as file:
        file.write(html_page)

    return html_path
