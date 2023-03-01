from page_loader.core import download


def test_core(urls, paths, file_paths):
    url1, url2 = urls
    path1, path2 = paths
    file_path1, file_path2 = file_paths
    assert download(url1['url'], path1['test_path']) == file_path1 + '\n'
    assert download(url2['url'], path2['fs_path']) == file_path2 + '\n'
