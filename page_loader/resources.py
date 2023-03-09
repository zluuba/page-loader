from page_loader.naming import get_resource_filename
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
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
