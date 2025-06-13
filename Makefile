install:
	uv pip install pytest pytest-cov pyyaml ruff
	uv sync

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml

lint:
	uv run ruff check --fix

check: lint test

.PHONY: install test lint check test-coverage