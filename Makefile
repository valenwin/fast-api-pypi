.PHONY: all \
		setup \
		run

PROJECT=fast-api-pypi

venv/bin/activate: ## alias for virtual environment
	python -m venv venv

setup: venv/bin/activate ## project setup
	. venv/bin/activate; pip install pip wheel setuptools
	. venv/bin/activate; pip install -r requirements.txt

run: venv/bin/activate ## Run
	. venv/bin/activate; uvicorn main:app

flake:
	-flake8 *.py --max-line-length 100

black:
	-black *.py

mypy:
	-mypy *.py