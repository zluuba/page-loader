install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

reinstall:
	pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 page_loader

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml

#load:
#	page-loader https://page-loader.hexlet.repl.co
