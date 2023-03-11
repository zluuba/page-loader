# from page_loader.resources import download_resources
# from page_loader.resources import get_resources
# import os
#
#
# def read_downloaded(path, filename):
#     return open(os.path.join(path, filename), 'rb').read()
#
#
# def test_get_resources(tmp_path, main_page, dir_name, resources):
#     expected = main_page['content_after'], resources
#
#     assert get_resources(
#         main_page['url'], main_page['content'], dir_name['dir_name']
#     ) == expected
#
#
# def test_download_resources(requests_mock, tmp_path, resources, contents):
#     requests_mock.get(resources[0]['url'], content=contents['js'])
#     requests_mock.get(resources[1]['url'], content=contents['css'])
#     requests_mock.get(resources[2]['url'], content=contents['html'])
#     requests_mock.get(resources[3]['url'], content=contents['image'])
#     download_resources(tmp_path, resources)
#
#     assert os.path.exists(os.path.join(tmp_path, resources[0]['filename']))
#
#     js_file = read_downloaded(tmp_path, resources[0]['filename'])
#     assert js_file == contents['js']
#
#     css_file = read_downloaded(tmp_path, resources[1]['filename'])
#     assert css_file == contents['css']
#
#     html_file = read_downloaded(tmp_path, resources[2]['filename'])
#     assert html_file == contents['html']
#
#     image = read_downloaded(tmp_path, resources[3]['filename'])
#     assert image == contents['image']
