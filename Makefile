test:
	black . --check
	isort -y --check-only
	env PYTHONPATH=. pytest --pylint --flake8

format:
	black .
	isort -y

dev:
	pip install -U -r requirements.txt
	pre-commit install
