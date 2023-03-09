from page_loader.resources import get_resources


def test_get_resources(tmp_path, main_page, dir_name, resources):
    expected = main_page['content_after'], resources

    assert get_resources(
        main_page['url'], main_page['content'], dir_name['dir_name']
    ) == expected
