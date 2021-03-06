install:
	poetry install

lint:
	poetry run flake8 gendiff

tests:
	poetry run pytest -v -s gendiff/tests/test_diff.py
	poetry run pytest --cov=gendiff --cov-report xml gendiff/tests/