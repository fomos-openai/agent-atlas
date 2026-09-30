PYTHON ?= python3

.PHONY: validate examples book test all

validate:
	$(PYTHON) scripts/generate_indexes.py --check
	$(PYTHON) scripts/validate_catalog.py
	$(PYTHON) scripts/validate_content.py
	$(PYTHON) scripts/validate_links.py
	$(PYTHON) scripts/check_freshness.py

examples:
	$(PYTHON) -m unittest tests.test_examples -v

book:
	$(PYTHON) scripts/build_book.py

test:
	$(PYTHON) -m unittest discover -s tests -v

all: validate examples book test
