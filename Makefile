.PHONY: install
install:
	poetry install

.PHONY: run
run:
	poetry run python -m famsure.main

.PHONY: dev
dev:
	poetry run uvicorn famsure.main:app --reload --port 8000

.PHONY: migrate
migrate:
	poetry run alembic upgrade head