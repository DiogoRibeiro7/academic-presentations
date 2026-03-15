# feature-engineering

## Overview

This directory is the canonical home for Feature Engineering materials.

## Scope

- Keep Feature Engineering content in this topic boundary.
- Preserve separation between slides, runnable code, and exercises.
- Use this folder for all future migrations and updates.

## Current Assets

- `presentation/feature_engineering_beamer.tex`
- `code/python/feature_engineering_pipeline.py`
- `code/r/feature_engineering_pipeline.R`
- `exercises/` (reserved for topic-specific exercise files)

## Structure

- `presentation/` - lecture slides
- `code/` - executable examples (Python and R)
- `exercises/` - problem sets and assessment material for this topic

## Build And Validation

Compile slides:

```bash
cd 01-foundations/feature-engineering/presentation
latexmk -pdf -interaction=nonstopmode feature_engineering_beamer.tex
```

Validate Python example syntax:

```bash
python -m py_compile 01-foundations/feature-engineering/code/python/feature_engineering_pipeline.py
```

Validate R example syntax (if R is installed):

```bash
Rscript -e "parse(file='01-foundations/feature-engineering/code/r/feature_engineering_pipeline.R')"
```

## Migration Status

- Presentation assets are consolidated under `presentation/`.
- Code assets are consolidated under `code/`.
- Exercises location is consolidated under `exercises/` and ready for topic exercise files.

