from page_loader.common import get_filename, get_file_path
# import requests


def download(url, path):
    file_name = get_filename(url)
    file_path = get_file_path(path)
    full_path = file_path + file_name

    # response = requests.get(url, stream=True, timeout=10)
    try:
        print('\n' + 'All good, path: ')
        # with open(full_path, 'wb') as file:
        #     for data in response.iter_content():
        #         file.write(data)
    except PermissionError:
        return f"Path {path} does not exist"

    return full_path + '\n'
