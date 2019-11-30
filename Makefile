clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -rf {} +
	rm -rf .mypy_cache/
	rm -rf .pytest_cache/
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/

develop:
	poetry install

install: 
	poetry install --no-dev

format: clean
	isort -rc src
	black src

lint: format
	pyflakes src
	poetry check

test: lint
	pytest --ignore=docs --verbose --instafail --mypy --mypy-ignore-missing-imports --doctest-modules --cov=src/ --cov-report term

patch: test
	poetry version patch
	git tag (rg version pyproject.toml | sed -n 1p | awk '/version/{print $$NF}' | tr -d '"' | awk '{print "v"$$0}')
	git push --tags

minor: test
	poetry version minor
	git tag (rg version pyproject.toml | sed -n 1p | awk '/version/{print $$NF}' | tr -d '"' | awk '{print "v"$$0}')
	git push --tags

major: test
	poetry version major
	git tag (rg version pyproject.toml | sed -n 1p | awk '/version/{print $$NF}' | tr -d '"' | awk '{print "v"$$0}')
	git push --tags

dist: clean 
	poetry build

release: dist
	poetry publish

.PHONY: clean develop install format lint test patch minor major dist release
