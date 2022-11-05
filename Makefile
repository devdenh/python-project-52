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
	@$(MANAGE) shell_plus --ipython

.PHONY: lint
lint:
	@poetry run flake8 task_manager

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage html
	poetry run coverage report

selfcheck:
	poetry check

check: selfcheck lint

start:
	poetry run python manage.py runserver 0.0.0.0:8000

push: check
	git push
