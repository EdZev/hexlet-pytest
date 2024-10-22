install:
	poetry install

test:
	poetry run pytest

test_print:
	poetry run pytest -s