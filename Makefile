build: 
	pip install --editable .

freeze:
	pip freeze > requriements.txt

install:
	pip install -r requirements.txt

lint:
	isort -rc src
	black src
	pyflakes src
	git add .
	git commit -m "Linting and formatting files"

test: lint
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
	rm -rf build/
	rm-rf dist/

dist: clean
	python setup.py sdist bdist_wheel

.PHONY: lint clean dist
