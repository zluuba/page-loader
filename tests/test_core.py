from page_loader.core import download, download_resources
import os


def read_downloaded(path, filename):
    return open(os.path.join(path, filename), 'rb').read()


def test_download(requests_mock, tmp_path, main_page):
    requests_mock.get(main_page['url'], text='resp')

    expected = os.path.join(tmp_path, main_page['filename'])
    received = download(main_page['url'], tmp_path)

    assert expected == received


def test_download_resources(requests_mock, tmp_path, resources, contents):
    requests_mock.get(resources[0]['url'], content=contents['js'])
    requests_mock.get(resources[1]['url'], content=contents['css'])
    requests_mock.get(resources[2]['url'], content=contents['html'])
    requests_mock.get(resources[3]['url'], content=contents['image'])
    download_resources(tmp_path, resources)

    assert os.path.exists(os.path.join(tmp_path, resources[0]['filename']))

    js_file = read_downloaded(tmp_path, resources[0]['filename'])
    assert js_file == contents['js']

    css_file = read_downloaded(tmp_path, resources[1]['filename'])
    assert css_file == contents['css']

    html_file = read_downloaded(tmp_path, resources[2]['filename'])
    assert html_file == contents['html']

    image = read_downloaded(tmp_path, resources[3]['filename'])
    assert image == contents['image']
