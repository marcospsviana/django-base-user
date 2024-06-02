SHELL: /bin/bash
setup:
	python -m venv .venv
	.venv/bin/pip install pipenv
	.venv/bin/python -m pipenv sync -d
	git remote remove origin

check:
	.venv/bin/flake8 .

format:
	.venv/bin/isort .
	.venv/bin/blue .
	