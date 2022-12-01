### Hexlet tests and linter status:
[![Actions Status](https://github.com/devdenh/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/devdenh/python-project-52/actions)
[![Python CI](https://github.com/devdenh/python-project-52/actions/workflows/pyci.yaml/badge.svg)](https://github.com/devdenh/python-project-52/actions/workflows/pyci.yaml)
[![Maintainability](https://api.codeclimate.com/v1/badges/dc9c40e2c07507c2bdff/maintainability)](https://codeclimate.com/github/devdenh/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/dc9c40e2c07507c2bdff/test_coverage)](https://codeclimate.com/github/devdenh/python-project-52/test_coverage)

## Requirements

* Python 3.8+
* Poetry
* GNU Make

## Setup

```bash
make setup
```

## Run server

```bash
make start
# Open http://127.0.0.1:8000/
```

## Check codestyle

```bash
make lint
```

## Run tests

```bash
make test
make test-coverage # run tests with coverage report
```
