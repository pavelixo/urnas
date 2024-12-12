DIRS = client server

all: $(DIRS)

.PHONY: install
install:
	$(MAKE) -C client install
	$(MAKE) -C server install

.PHONY: start-server
start-server:
	$(MAKE) -C client build
	$(MAKE) -C server migrate
	$(MAKE) -C server collectstatic
	$(MAKE) -C server runserver

.PHONY: start-tasks
start-tasks:
	$(MAKE) -C server celery