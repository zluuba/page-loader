from page_loader.validator import validate_user_input, get_valid_response
import responses
import pytest


def test_validate_user_input(user_inputs):
    wrong, correct = user_inputs['wrong'], user_inputs['correct']

    with pytest.raises(SystemExit) as invalid_url:
        validate_user_input(wrong['url'], correct['path'])
        assert f"Incorrect url: {wrong['url']}" in str(invalid_url.value)

    with pytest.raises(SystemExit) as invalid_path:
        validate_user_input(correct['url'], wrong['path'])
        assert f"Directory doesn't exist: {wrong['path']}." in str(invalid_path.value)


@responses.activate
def test_get_valid_response(main_page):
    with pytest.raises(SystemExit):
        responses.add(responses.GET, main_page['url'], status=404)
        get_valid_response(main_page['url'])

    responses.add(responses.GET, main_page['url'], status=200)
    get_valid_response(main_page['url'])
