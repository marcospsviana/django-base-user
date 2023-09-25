SHELL: /bin/bash
setup:
	python -m venv .venv
	.venv/bin/pip install pipenv
	.venv/bin/python -m pipenv install

check:
	.venv/bin/flake8 --check

format:
	.venv/bin/isort .
	.venv/bin/blue .
	