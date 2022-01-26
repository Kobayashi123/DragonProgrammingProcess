PYTHON	= python
PYDOC	= pydoc
PYCS	= $(shell find . -name "*.pyc")
PYCACHE	= $(shell find . -name "__pycache__")
MODULE	= Example
TARGET	= $(MODULE).py
PACKAGE	= jp.ac.kyoto_su.cse.ap.python
PKGPATH	= $(shell echo $(PACKAGE) | sed -e 's/\./\//g')
PKGTDIR	= $(shell echo $(PACKAGE) | cut -d '.' -f1)
INSTDIR	= Example.app/Contents/Resources/Python/
ARCHIVE	= $(shell basename `pwd`)
WORKDIR	= ./
PYLINT	= pylint
LINTRCF	= pylintrc.txt
LINTRST	= pylintresult.txt
ARGS	= 
TARGZ	= OpenGLMVC-1.0.0.tar.gz
ARVER	= $(shell basename $(TARGZ) .tar.gz)

all:
	@:

wipe: clean
	@find . -name ".DS_Store" -exec rm {} ";" -exec echo rm -f {} ";"
	(cd ../ ; rm -f ./$(ARCHIVE).zip)

clean:
	@for each in ${PYCS} ; do echo "rm -f $${each}" ; rm -f $${each} ; done
	@for each in ${PYCACHE} ; do echo "rm -f $${each}" ; rm -rf $${each} ; done
	@if [ -e $(INSTDIR) ] ; then echo "rm -f -r $(INSTDIR)" ; rm -f -r $(INSTDIR) ; fi
	@if [ -e $(LINTRST) ] ; then echo "rm -f $(LINTRST)" ; rm -f $(LINTRST) ; fi
	@if [ -e MANIFEST ] ; then echo "rm -f MANIFEST" ; rm -f MANIFEST ; fi
	@find . -name ".DS_Store" -exec rm {} ";" -exec echo rm -f {} ";"

test: all
	$(PYTHON) $(TARGET) ${ARGS}

install: all
	@if [ ! -e $(INSTDIR) ] ; then echo "mkdir $(INSTDIR)" ; mkdir $(INSTDIR) ; fi
	cp -p -r $(TARGET) $(PKGTDIR) ./images $(INSTDIR)
#	echo 3.7.3 > $(INSTDIR).python-version

doc:
	$(PYDOC) ./$(TARGET) `find ./$(PKGPATH) -name "*.py" -not -name "__init__.py"`

zip: wipe
	(cd ../ ; zip -r ./$(ARCHIVE).zip ./$(ARCHIVE)/ --exclude='*/.svn/*')

sdist: clean
	$(PYTHON) setup.py sdist

pydoc:
	(sleep 3 ; open http://localhost:9999/$(MODULE).html) & $(PYDOC) -p 9999

unittest:
	@echo '*** [./$(TARGET)] ***' ; $(PYTHON) ./$(TARGET)  ./images/AOKI_Atsushi.gif 100,100 -v 
	@find ./$(PKGTDIR) -name "[A-Za-z]*.py" -exec echo '*** ['{}'] ***' ";" -exec $(PYTHON) {} -v ";"

lint:
	@if [ ! -e $(LINTRCF) ] ; then $(PYLINT) --generate-rcfile > $(LINTRCF) 2> /dev/null ; fi
	$(PYLINT) --rcfile=$(LINTRCF) --extension-pkg-whitelist=PyQt5 ./$(TARGET) `find ./$(PKGPATH) -name "*.py" -not -name "__init__.py"` > $(LINTRST) ; less $(LINTRST)

# 
# pip is the PyPA recommended tool for installing Python packages.
# 
pip:
	@if [ -z `which pip` ]; \
	then \
		(cd $(WORKDIR); curl -O https://bootstrap.pypa.io/get-pip.py); \
		(cd $(WORKDIR); sudo -H python get-pip.py); \
		(cd $(WORKDIR); rm -r get-pip.py); \
	else \
		(cd $(WORKDIR); sudo -H pip install -U pip); \
	fi

# 
# Pylint is a tool that checks for errors in Python code,
# tries to enforce a coding standard and looks for code smells.
# 
pylint:
	@if [ -z `pip list --format=freeze | grep pylint` ]; \
	then \
		(cd $(WORKDIR); sudo -H pip install pylint); \
	else \
		(cd $(WORKDIR); sudo -H pip install pylint -U); \
	fi

# 
# PyQt5 is a comprehensive set of Python bindings for Qt v5.
# 
PyQt5:
	@if [ -z `pip list --format=freeze | grep PyQt5=` ]; \
	then \
		(cd $(WORKDIR); sudo -H pip install sip); \
		(cd $(WORKDIR); sudo -H pip install PyQt5); \
	else \
		(cd $(WORKDIR); sudo -H pip install sip -U); \
		(cd $(WORKDIR); sudo -H pip install PyQt5 -U); \
	fi

# 
# List of the required packages
# 
list: pip
	@(pip list --format=freeze | grep ^pip)
	@(pip list --format=freeze | grep ^pylint)
	@(pip list --format=freeze | grep ^sip)
	@(pip list --format=freeze | grep ^PyQt5)

prepare: pip pylint PyQt5

update: pip pylint PyQt5

# 
# Utilities for Development Process
# 
edit:
	@find . -name "*.py" -not -name "__init__.py" | sort | xargs open -a /Applications/Jedit\ Ω.app 

version:
	@find . -name "*.py" -not -name "__init__.py" | sort | xargs -n 1 grep -Hn '__version__ =' 

date:
	@find . -name "*.py" -not -name "__init__.py" | sort | xargs -n 1 grep -Hn '__date__ =' 
