MANAGE := poetry run python manage.py

.PHONY: test
test:
	poetry run python manage.py test

.PHONY: install
install:
	@poetry install

.PHONY: migrate
migrate:
	@$(MANAGE) makemigrations
	@$(MANAGE) migrate

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

.PHONY: lint
lint:
	@poetry run flake8 task_manager

test-coverage:
	poetry run coverage run --source='.' manage.py test
	poetry run coverage report
	poetry run coverage xml

selfcheck:
	poetry check

check: selfcheck lint test

start:
	poetry run python manage.py runserver

push: check
	git push
