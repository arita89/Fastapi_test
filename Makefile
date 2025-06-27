# Variables
VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip

# Default target: setup env and install requirements
.PHONY: install
install:
	@if [ ! -d "$(VENV_DIR)" ]; then \
		python3 -m venv $(VENV_DIR); \
	fi
	@. $(VENV_DIR)/bin/activate && $(PIP) install --upgrade pip && $(PIP) install -r requirements.txt

# Activate environment (prints activation command for user)
.PHONY: activate
activate:
	@echo "Run: source $(VENV_DIR)/bin/activate"

# Run the app
.PHONY: run
run:
	@. $(VENV_DIR)/bin/activate && uvicorn main:app --reload

# Clean up environment
.PHONY: clean
clean:
	rm -rf $(VENV_DIR)
