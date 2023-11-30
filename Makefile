.PHONY: hello init validate-% init-go init-python3.10 init-python3.11 init-rust

WORKSPACE_DIR := workspace
UUID := $(shell uuidgen)

hello:
	@echo "Hello, world!"

init:
	@mkdir -p $(WORKSPACE_DIR)

validate-%:
	@if [ -d "$(WORKSPACE_DIR)/${@:validate-%=%}" ]; then \
		echo "$(WORKSPACE_DIR)/${@:validate-%=%} already exists (UUID collision)! Try again."; \
		exit 1; \
	fi

init-go: init
	@make validate-go_$(UUID)
	@cp -r template/go $(WORKSPACE_DIR)/go_$(UUID)
	@echo "$(WORKSPACE_DIR)/go_$(UUID) created"

init-python3.10: init
	@make validate-python3.10_$(UUID)
	@cp -r template/python/python3.10 $(WORKSPACE_DIR)/python3.10_$(UUID)
	@echo "$(WORKSPACE_DIR)/python3.10_$(UUID) created"

init-python3.11: init
	@make validate-python3.11_$(UUID)
	@cp -r template/python/python3.11 $(WORKSPACE_DIR)/python3.11_$(UUID)
	@echo "$(WORKSPACE_DIR)/python3.11_$(UUID) created"

init-rust: init
	@make validate-rust_$(UUID)
	@cp -r template/rust $(WORKSPACE_DIR)/rust_$(UUID)
	@echo "$(WORKSPACE_DIR)/rust_$(UUID) created"
