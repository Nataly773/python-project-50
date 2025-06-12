install:
	uv sync

run:
	uv run gendiff

test:
	uv run pytest

test-coverage:
	uv pip install pytest-cov pyyaml
	uv run pytest --cov=gendiff --cov-report=xml

lint:
	uv run ruff check

check: 
	test lint

build:
	uv build

.PHONY: install test lint selfcheck check build