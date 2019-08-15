clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/

develop: clean
	pip install --editable .
	pip install -r dev_requirements.txt

install:
	pip install -r requirements.txt

format: 
	isort -rc src
	black src

lint: format
	pyflakes src

test: lint
	python setup.py test

docs: clean
	cd docs/; and make html

patch:
	bump2version patch
	git push origin master --tags

minor:
	bump2version minor
	git push origin master --tags

major:
	bump2version major
	git push origin master --tags


dist: clean docs
	python setup.py sdist bdist_wheel

release: dist
	twine upload dist/*

.PHONY: clean develop install format lint test docs patch minor major dist clean 
