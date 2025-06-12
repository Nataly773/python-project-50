install:
	uv sync

lint:
	uv run ruff check

test:
	uv run pytest

test-coverage:
	uv pip install pytest-cov pyyaml
	uv run pytest --cov=gendiff --cov-report=xml

check: lint test
