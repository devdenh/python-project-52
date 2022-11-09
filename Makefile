MANAGE := poetry run python manage.py

.PHONY: test
test:
	poetry run python manage.py test

.PHONY: install
install:
	@poetry install

.PHONY: migrate
migrate:
	@$(MANAGE) migrate

.PHONY: shell
shell:
	@$(MANAGE) shell

.PHONY: lint
lint:
	@poetry run flake8 task_manager

test-coverage:
	poetry run coverage run --source='.' manage.py test
	poetry run coverage report
	poetry run coverage xml

selfcheck:
	poetry check

check: selfcheck lint

start:
	poetry run python manage.py runserver

push: check
	git push
