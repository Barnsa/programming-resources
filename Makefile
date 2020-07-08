INVENV = $(shell pip3 -V | grep 'venv')
current_dir = $(shell pwd)

build:
	mkdocs build --clean

serve:
	mkdocs serve

publish:
	mkdocs gh-deploy --config-file ./mkdocs.yml --remote-branch gh-pages

clean:
	rm -rf ./site


prereqs: venvcheck FORCE
	pip install -r requirements.txt

venv: FORCE
	python3 -m venv venv

venvcheck:
ifeq ($(INVENV),)
	$(error You should only run this from within the venv. Use '. ./venv/bin/activate')
else
	@echo "venv check passed\n"
endif


FORCE:
