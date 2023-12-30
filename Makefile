.PHONY: default clean test build upload localenv

default:
	@echo "No target specified. Do nothing."

clean:
	@rm -rf .pytest_cache
	@rm -rf dist
	@rm -rf src/*.egg-info
	@rm -rf src/parquest/__pycache__
	@rm -rf tests/__pycache__
	@rm -rf tests/.pytest_cache

test:
	@rm -rf tests/reports/*
	@pytest -v --tb=line || true

build: test clean
	@python -m build

upload:
	@twine upload --repository testpypi dist/*.whl
	@twine upload --repository pypi dist/*.whl

localenv:
	@rm -rf env/
	@python -m venv env
	source env/Scripts/activate && pip install -r requirements.txt
