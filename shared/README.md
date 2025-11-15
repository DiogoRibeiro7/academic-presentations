# Shared Resources

## Overview

This directory contains resources shared across all presentations and topics in the repository.

## Contents

### 1. Theme (`theme/`)

**ESMAD Beamer Theme** - Professional LaTeX theme for all presentations

Files:
- `esmad_beamer_theme.sty` - Main theme package
- `STYLE_GUIDE.md` - Complete theme documentation
- `template_presentation.tex` - Example template

Features:
- Professional color palette
- Custom environments (theorems, definitions, examples)
- Mathematical notation helpers
- Code listing styles
- Author information with ORCID integration

Usage in presentations:
```latex
\usepackage{../../shared/theme/esmad_beamer_theme}
```

### 2. Bibliographies (`bibliographies/`)

Comprehensive BibTeX reference libraries (140+ papers with DOIs)

Files:
- `mcmc_references.bib` - MCMC methods (30+ refs)
- `causal_inference_references.bib` - Causal inference (50+ refs)
- `statistical_learning_references.bib` - ML/Stats (60+ refs)
- `deep_learning_references.bib` - Deep learning references
- `bayesian_references.bib` - Bayesian statistics
- `time_series_references.bib` - Time series methods
- `optimization_references.bib` - Optimization algorithms
- `industry_applications.bib` - Applied DS references

Usage in presentations:
```latex
\usepackage[backend=bibtex]{biblatex}
\addbibresource{../../shared/bibliographies/mcmc_references.bib}

% In document
\cite{metropolis1953}

% At end
\printbibliography
```

### 3. Utilities (`utilities/`)

Helper scripts and tools:
- `compile_all.sh` - Batch compile all presentations
- `check_references.py` - Validate bibliography entries
- Build system configurations

## Path Conventions

### From Domain-Level Topics
Topics in domain directories (e.g., `01-foundations/statistical-modeling/`) reference shared resources with:
```latex
../../shared/theme/esmad_beamer_theme
../../shared/bibliographies/statistical_learning_references.bib
```

### From Root-Level Files
Files at repository root reference shared resources with:
```latex
shared/theme/esmad_beamer_theme
shared/bibliographies/mcmc_references.bib
```

## Maintenance

### Adding New Bibliography Entries

1. Choose appropriate `.bib` file
2. Add entry with DOI
3. Run validation: `python shared/utilities/check_references.py`
4. Test compilation of affected presentations

### Updating Theme

1. Edit `esmad_beamer_theme.sty`
2. Update `STYLE_GUIDE.md` if adding new features
3. Test with template: `shared/theme/template_presentation.tex`
4. Compile sample presentations to verify changes

## Version Control

- **Theme version**: Track in `esmad_beamer_theme.sty` header
- **Bibliography**: Date references when adding bulk updates
- **Breaking changes**: Document in repository CHANGELOG.md

## Dependencies

### LaTeX Packages Required
- beamer
- tikz
- listings
- biblatex (for bibliographies)
- amsmath, amssymb (mathematics)
- See theme file for complete list

### External Tools
- Python 3.7+ (for utilities)
- Git (version control)
- LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
