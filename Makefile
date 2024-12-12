DIRS = client server

all: $(DIRS)

.PHONY: install
install:
	$(MAKE) -C client install
	$(MAKE) -C server install

.PHONY: start
start:
	$(MAKE) -C client build
	$(MAKE) -C server migrate
	$(MAKE) -C server collectstatic
	$(MAKE) -C server runserver & $(MAKE) -C server celery