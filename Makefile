MANAGE := poetry run python manage.py

.PHONY: test
test:
	@poetry run pytest

.PHONY: install
install:
	@poetry install

.PHONY: migrate
migrate:
	@$(MANAGE) migrate

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

.PHONY: lint
lint:
	@poetry run flake8 task_manager

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage html
	poetry run coverage report

check:
	poetry check
