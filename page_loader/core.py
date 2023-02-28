from urllib.parse import urlparse
import requests
import os.path


def download(url, path):
    if path:
        if path[-1] != '/':
            path += '/'
    file_extension = '.html'

    parse_url = urlparse(url)
    netloc, url_path = parse_url.netloc, parse_url.path
    file_name = netloc + url_path

    while '.' in file_name or '/' in file_name:
        file_name = file_name.replace('.', '-')
        file_name = file_name.replace('/', '-')

    file_name = file_name + file_extension

    curr_dir = os.path.dirname(os.path.abspath(__file__))
    dir = os.path.abspath(os.path.join(curr_dir, os.pardir))
    file_path = os.path.join(dir, path)

    full_path = file_path + file_name

    response = requests.get(url, stream=True, timeout=10)
    try:
        with open(full_path, 'wb') as file:
            for data in response.iter_content():
                file.write(data)
    except PermissionError:
        return f"Path {path} does not exist"

    return full_path


# u = 'http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm'
# print(download(u, '/var/tmp'))
