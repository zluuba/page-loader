import pytest
import os


def get_fixture_path(filename):
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(parent_dir, 'fixtures/', filename)


def read_file(filename, mode='rb'):
    return open(get_fixture_path(filename), mode).read()


@pytest.fixture
def main_page():
    return {
        'url': 'https://page-loader.hexlet.repl.co',
        'filename': 'page-loader-hexlet-repl-co.html',
        'content': read_file(get_fixture_path('page.html'), mode='r'),
        'content_after': read_file(get_fixture_path('prettify_page.html'), mode='r')
    }


@pytest.fixture
def urls():
    return {
        'js': 'https://page-loader.hexlet.repl.co/script.js',
        'css': 'https://page-loader.hexlet.repl.co/assets/application.css',
        'html': 'https://page-loader.hexlet.repl.co/courses',
        'image': 'https://page-loader.hexlet.repl.co/assets/professions/nodejs.png'
    }


@pytest.fixture
def names():
    return {
        'js': 'page-loader-hexlet-repl-co-script.js',
        'css': 'page-loader-hexlet-repl-co-assets-application.css',
        'html': 'page-loader-hexlet-repl-co-courses.html',
        'image': 'page-loader-hexlet-repl-co-assets-professions-nodejs.png'
    }


@pytest.fixture
def contents():
    return {
        'js': read_file(get_fixture_path('script.js')),
        'css': read_file(get_fixture_path('style.css')),
        'html': read_file(get_fixture_path('page.html')),
        'image': read_file(get_fixture_path('image.png'))
    }


@pytest.fixture
def resources(urls, names):
    return [
        {'url': urls['image'], 'filename': names['image']},
        {'url': urls['css'], 'filename': names['css']},
        {'url': urls['html'], 'filename': names['html']},
        {'url': urls['js'], 'filename': names['js']}
    ]


@pytest.fixture
def dir_name():
    return {
        'url': 'https://page-loader.hexlet.repl.co',
        'dir_name': 'page-loader-hexlet-repl_files'
    }


@pytest.fixture
def user_inputs():
    return {
        'wrong': {'url': 'htpppp://wrong.com', 'path': 'this/path/doesn\'t/exist/'},
        'correct': {'url': 'https://correct.com', 'path': os.getcwd()}
    }
