import pytest


@pytest.fixture
def urls():
    case1 = dict(url='http://testing.com', file='testing-com.html')
    case2 = dict(url='https://ru.hexlet.io/courses', file='ru-hexlet-io-courses.html')
    return case1, case2


@pytest.fixture
def paths():
    case1 = dict(fs_path='/var/data/test-case', test_path='/var/data', end_path='/var/data/')
    case2 = dict(fs_path='/test-case2/tmp', end_path='/test-case2/tmp/')
    return case1, case2


@pytest.fixture
def file_paths():
    case1 = '/var/data/testing-com.html'
    case2 = '/test-case2/tmp/ru-hexlet-io-courses.html'
    return case1, case2
