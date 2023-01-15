
  
.PHONY: lock install test lint format

lock:
	poetry lock

install:
	poetry install

test:
	pytest src tests -vv

lint:
	flake8 --max-line-length 100 src tests bin
	isort --check-only --diff src tests bin
	pydocstyle --ignore=D1,D211,D203 src tests bin
	black --check src tests bin

format:
	isort src tests bin
	black src tests bin

run:
	python src/portfolio/__main__.py
