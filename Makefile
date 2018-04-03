test:
	py.test

install:
	pip install dissonant

install_dev:
	pip install -e .

uninstall:
	pip uninstall dissonant

clean:
	rm -r build/ dist/ dissonant.egg-info/

# twine - a tool for uploading packages to PyPI
install_twine:
	pip install twine

build:
	python setup.py sdist
	python setup.py bdist_wheel --universal

publish:
	twine upload dist/*

test_publish:
	python setup.py sdist upload -r pypitest

test_install:
	pip install --verbose --index-url https://testpypi.python.org/pypi/ dissonant
