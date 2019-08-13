develop: 
	pip install --editable .
	pip install -r dev_requirements.txt

install:
	pip install -r requirements.txt

lint:
	pyflakes src

format: 
	isort -rc src
	black src
	git add .
	git commit -m "Formatting files with black and isort"

test: format lint
	python setup.py test

patch:
	bump2version patch
	git push origin master --tags

minor:
	bump2version minor
	git push origin master --tags

major:
	bump2version major
	git push origin master --tags

# docs

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/


dist: clean
	python setup.py sdist bdist_wheel

release: dist
	twine upload dist/*

.PHONY: develop install lint format test patch minor major clean dist
