from page_loader.common import get_filename, get_file_path


def test_get_filename(urls):
    case1, case2 = urls
    assert get_filename(case1['url']) == case1['file']
    assert get_filename(case2['url']) == case2['file']


def test_get_file_path(fs, paths):
    case1, case2 = paths
    assert get_file_path('') == '/'

    fs.create_file(case1['fs_path'])
    assert get_file_path(case1['test_path']) == case1['end_path']

    fs.create_file(case2['fs_path'])
    assert get_file_path(case2['fs_path']) == case2['end_path']
