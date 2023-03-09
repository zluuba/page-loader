# from page_loader.core import download
# import responses


# @responses.activate
# def test_core(urls, paths, file_paths):
#     url1, url2 = urls
#     path1, path2 = paths
    # file_path1, file_path2 = file_paths

    # responses.add(responses.GET, url1['url'], status=200)
    # assert download(url1['url'], path1['test_path']) == file_path1
    #
    # responses.add(responses.GET, url2['url'], status=200)
    # assert download(url2['url'], path2['fs_path']) == file_path2

    # responses.add(responses.GET, url2['url'], status=404)
    # assert not download(url2['url'], path2['fs_path'])
