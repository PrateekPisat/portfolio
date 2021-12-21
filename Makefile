
  
.PHONY: lock install-base install test lint format
.DEFAULT_GOAL := help

# Install
lock:
	poetry lock

install:
	poetry install

test:
	pytest src tests -vv

lint:
	flake8 src tests
	isort --check-only --diff src tests
	pydocstyle src tests
	black --check src tests
	mypy src tests

format:
	isort --recursive src tests
	black src tests