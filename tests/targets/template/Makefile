LN=ln -sf
ORIG_DIR=../../src
SRC=$(wildcard $(ORIG_DIR)/*.py)
OBJ=$(SRC:$(ORIG_DIR)%.py=.%.pyc)

all: $(OBJ)

.PHONY: clean

%.pyc: $(ORIG_DIR)/%.py
	python$(shell basename $$PWD) -c 'import py_compile;py_compile.compile("$<", "$@");'

clean:
	$(RM) $(OBJ)

re: clean all
