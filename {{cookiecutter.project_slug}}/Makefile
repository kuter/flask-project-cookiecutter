.PHONY: check flake8 isort pydocstyle bandit

run:
	FLASK_APP=run.py flask run

flake8:
	@echo 'Check flake8 ..'
	flake8 --output-file=flake8.log

isort:
	@echo 'Check isort ..'
	isort -rc -c

pydocstyle:
	@echo 'Check docstring style ..'
	pydocstyle

bandit:
	@echo 'Check bandit ..'
	bandit -r .

check: flake8 isort pydocstyle bandit
