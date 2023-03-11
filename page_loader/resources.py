from page_loader.naming import get_resource_filename
import page_loader.validator
from urllib.parse import urlparse, urljoin
from progress.bar import IncrementalBar
from bs4 import BeautifulSoup
import page_loader.core
import requests
import errno
import os


TAGS = {'img': 'src', 'link': 'href', 'script': 'src'}


def get_resources(url, html_page, out_folder):
    bs = BeautifulSoup(html_page, 'html.parser')
    resources = []

    for tag, attr in TAGS.items():
        for content in bs.find_all(tag):
            raw_link = content.get(attr)
            if not raw_link:
                continue

            link = urljoin(urljoin(url, '/'), raw_link)
            if urlparse(url).netloc != urlparse(link).netloc:
                continue

            filename = get_resource_filename(link)
            resources.append({'url': link, 'filename': filename})
            output_path = os.path.join(out_folder, filename)
            content[attr] = output_path

    html_page = bs.prettify()
    return html_page, resources


def download_resources(resources_dir_path, resources):
    if not os.path.exists(resources_dir_path):
        try:
            os.mkdir(resources_dir_path)
            page_loader.core.logger.info(
                f"create directory for assets: {resources_dir_path}"
            )
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise page_loader.validator.AppError() from exc
            pass

    for resource in IncrementalBar('Downloading: ').iter(resources):
        url, filename = resource['url'], resource['filename']
        path = os.path.join(resources_dir_path, filename)

        response = requests.get(url, stream=True)
        if response.ok:
            data = response.content
            with open(path, 'wb') as file:
                file.write(data)
