from urllib.parse import urlparse
import os


def get_normalize_filename(url):
    parse_url = urlparse(url)
    netloc, url_path = parse_url.netloc, parse_url.path
    filename, _ = os.path.splitext(netloc + url_path)

    normalize_filename = ''
    for char in filename:
        if not char.isalnum():
            char = '-'
        normalize_filename += char

    return normalize_filename


def get_resource_filename(url):
    file_extension = os.path.splitext(url)[-1]
    if not file_extension:
        file_extension = '.html'

    filename = get_normalize_filename(url)
    return f'{filename}{file_extension}'


def get_dir_name(url):
    filename = get_normalize_filename(url)
    return f'{filename}_files'
