# from page_loader.core import download
# import os
#
#
# def test_download(requests_mock, tmp_path, main_page):
#     requests_mock.get(main_page['url'], text='resp')
#
#     expected = os.path.join(tmp_path, main_page['filename'])
#     received = download(main_page['url'], tmp_path)
#
#     assert expected == received
