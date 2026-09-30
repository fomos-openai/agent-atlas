PYTHON ?= python3
NODE ?= node
QUARTO ?= quarto
ARTIFACT_DIR ?= artifacts
BOOK_PATH := $(ARTIFACT_DIR)/agent-atlas-book.zh-CN.pdf
SOURCE_DATE_EPOCH ?= 1790812800
export SOURCE_DATE_EPOCH

.PHONY: validate labs figures site book visual-check test all release-check clean

validate:
	$(PYTHON) scripts/validate_catalog.py
	$(PYTHON) scripts/validate_content.py
	$(PYTHON) scripts/validate_links.py
	$(PYTHON) scripts/check_freshness.py

labs:
	PYTHONPATH=labs/python/src $(PYTHON) -m unittest discover -s labs/python/tests -v
	$(NODE) --test labs/typescript/tests/*.test.ts

figures:
	$(PYTHON) scripts/build_figures.py
	$(PYTHON) scripts/validate_figures.py

site:
	$(QUARTO) render --to html

book:
	$(QUARTO) render --to typst
	$(PYTHON) scripts/finalize_typst.py index.typ
	$(QUARTO) typst compile index.typ _site/agent-atlas-book.zh-CN.pdf
	mkdir -p $(ARTIFACT_DIR)
	cp _site/agent-atlas-book.zh-CN.pdf $(BOOK_PATH)

visual-check:
	$(PYTHON) scripts/validate_pdf.py $(BOOK_PATH)

test:
	$(PYTHON) -m unittest discover -s tests -v

all: validate labs figures site book visual-check test

release-check: all
	$(PYTHON) scripts/release_check.py

clean:
	rm -rf _site tmp/pdfs
