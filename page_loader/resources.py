from urllib.parse import urlparse, urljoin
from common import get_resource_filename, get_dir_name
from bs4 import BeautifulSoup
import requests
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
            outpath = os.path.join(out_folder, filename)
            content[attr] = outpath

    folder = os.path.join(out_folder, get_dir_name(url))
    [download_resource(resource, folder) for resource in resources]
    html_page = bs.prettify()
    return html_page


def download_resource(resource, folder):
    # update folder path for downloading
    url, filename = resource['url'], resource['filename']
    response = requests.get(url, stream=True)
    if response.ok:
        img_data = response.content
        # change filename to folder
        with open(filename, 'wb') as handler:
            handler.write(img_data)
            # print("Successfully downloaded: ", filename)
    else:
        print("Image Couldn't be retrieved")
