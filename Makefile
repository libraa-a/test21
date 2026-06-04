.PHONY: test build

# Run smoke/unit tests
test:
	python -m unittest test_string_utils.py

# Package the demo program
build:
	python -m zipfile -c string_utils_app.zip string_utils.py
	@echo "Build complete: string_utils_app.zip"
