PYTHON=python$(shell basename $$PWD)
LN=ln -sf
ORIG_DIR=../../src
SRC=$(wildcard $(ORIG_DIR)/*.py)
OBJ=$(SRC:$(ORIG_DIR)%.py=.%.pyc)

all: $(OBJ)

.PHONY: clean magic

%.pyc: $(ORIG_DIR)/%.py
	$(PYTHON) -c 'import py_compile;py_compile.compile("$<", "$@");'

magic:
	$(PYTHON) -c 'import imp,struct;print struct.unpack("<H", imp.get_magic()[:2])[0]' > magic

clean:
	$(RM) $(OBJ)

re: clean all
