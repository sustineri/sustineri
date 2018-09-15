# -----------------------------------------------------------------------------
# BUILD
# -----------------------------------------------------------------------------
.PHONY: all
all: clean build

.PHONY: build
build:
	@docker-compose build
	@echo Build done.

.PHONY: start
start:
	@docker-compose up -d
	@echo Start done.

.PHONY: stop
stop:
	@docker-compose stop
	@echo Stop done.

.PHONY: stop_deps
stop_deps:
	@docker-compose kill sustineri-database
	@docker-compose rm -f

.PHONY: start_deps
start_deps:
	@docker-compose up -d sustineri-database

.PHONY: clean
clean:
	@rm -rf .cache
	@rm -rf target
	@rm -f .coverage
	@rm -f .version
	@find . -iname __pycache__ | xargs rm -rf
	@find . -iname "*.pyc" | xargs rm -f
	@find . -iname "mb*.log" | xargs rm -f
