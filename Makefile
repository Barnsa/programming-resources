ifeq ($(OS), Windows_NT)
	# this will always fail from inside VSCode due to how it handles venv's 
	INVENV := $(shell pip3 -V | findstr 'venv')
else 	
	INVENV := $(shell pip3 -V | grep 'venv')
endif

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
# TODO: This check fails on windows systems and will not allow prereqs to work, fix it (I think it's mostly a VSCode problem.)
# Unless you are using VSCode and then venvs are used by default, check the bottom left hand corner to see if you are inside the venv.
ifeq ($(INVENV),)
	ifeq ($(OS), Windows_NT)
		ifeq ($(SHELL), sh.exe)
			$(error You should only run this from within the venv. Use '.\venv\Scripts\Activate.ps1')
		else
			$(error You should only run this from within the venv. Use '.\venv\Scripts\activate.bat')
	else
		$(error You should only run this from within the venv. Use '. ./venv/bin/activate')
else
	@echo "venv check passed\n"
endif


FORCE:

fix:
	git clone https://github.coventry.ac.uk/csx239/mk_doc_ultra.git

test: 
	@echo "$(SHELL)"
