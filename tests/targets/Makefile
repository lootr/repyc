TARGETS=$(wildcard *.*)

all:
	@(for t in $(TARGETS); do $(MAKE) -C $$t $@; done)

re:
	@(for t in $(TARGETS); do $(MAKE) -C $$t $@; done)

.PHONY: clean

clean:
	@(for t in $(TARGETS); do $(MAKE) -C $$t $@; done)
