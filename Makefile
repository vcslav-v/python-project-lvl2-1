install:
	poetry install

lint:
	poetry run flake8 gendiff

tests:
	pytest -v -s gendiff/tests/test_diff.py