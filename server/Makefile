.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate:
	poetry run ./manage.py migrate

.PHONY: runserver
runserver:
	poetry run daphne -p 8000 core.asgi:application

.PHONY: celery
celery:
	poetry run celery -A core worker --loglevel=info
