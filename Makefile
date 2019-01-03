all: help

.PHONY: help
help: $## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

.PHONY: hello
hello: ## [example] invokes hello function
	@sls invoke local -f hello

.PHONY: hello-with-data
hello-with-data: ## [example] invokes hello, passing data from file
	@sls invoke local -f hello --path tmp/data.json

.PHONY: test
test: ## Run test suite
	@python -m unittest
