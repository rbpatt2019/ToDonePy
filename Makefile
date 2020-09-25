VERSION=$$(grep version pyproject.toml | sed -n 1p | awk '/version/ {print $$3}' | tr -d '"' | awk '{print "v"$$0}')

define requirements
poetry export --without-hashes --dev -f requirements.txt -o requirements.txt
git add requirements.txt
git commit -m 'Update requirements.txt'
endef

define tags
git add pyproject.toml
git commit -m "VERSION bump"
git tag $(VERSION)
git push origin master --tags
endef

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
	rm -rf html/
	rm -rf doctrees/

reqs:
	$(requirements)
update:
	poetry update
	git add poetry.lock
	git commit -m 'Update dependencies'
	$(requirements)

develop:
	poetry install

install: 
	poetry install --no-dev

format: clean
	poetry run isort todonepy/ tests/
	poetry run black todonepy/ tests/

lint: format
	poetry run pylint todonepy/ tests/
	poetry run mypy --ignore-missing-imports todonepy/ tests/
	poetry check

test: clean
	pytest

patch: update test
	poetry version patch
	$(tags)

minor: update test
	poetry version minor
	$(tags)

major: update test
	poetry version major
	$(tags)

dist: clean 
	poetry build

release: dist
	poetry publish

.PHONY: clean reqs update develop install format lint test patch minor major dist release
