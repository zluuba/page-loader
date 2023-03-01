from urllib.parse import urlparse
import os.path


FILE_EXTENSION = '.html'


def get_filename(url):
    parse_url = urlparse(url)
    netloc, url_path = parse_url.netloc, parse_url.path
    file_name = netloc + url_path

    while '.' in file_name or '/' in file_name:
        file_name = file_name.replace('.', '-')
        file_name = file_name.replace('/', '-')

    file_name += FILE_EXTENSION
    return file_name


def get_file_path(path):
    if path:
        if path[-1] != '/':
            path += '/'

    curr_dir = os.getcwd()
    file_path = os.path.join(curr_dir, path)

    return file_path
