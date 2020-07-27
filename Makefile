install:
	pip install -r requirements_dev.txt --upgrade
	pip install -r requirements.txt --upgrade
	pip install -e .
	pre-commit install

lint:
	flake8

test:
	pytest

test-force:
	echo 'Regenerating component metadata for regression test. Make sure there are not any unwanted regressions because this will overwrite them'
	pytest --force-regen

clean:
	rm **/**.log
	rm **/**.fsp
	rm **/**.lms
