
  
.PHONY: lock install test lint format

lock:
	poetry lock

install:
	poetry install

test:
	pytest src tests -vv

lint:
	flake8 --max-line-length 100 src tests
	isort --check-only --diff src tests
	pydocstyle --ignore=D1,D211,D203 src tests
	black --check src tests

format:
	isort src tests
	black src tests
