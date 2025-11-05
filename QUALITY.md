# Code Quality Guidelines

**Maintaining high-quality code and documentation in Academic Presentations**

Last Updated: January 2025

## 📚 Overview

This document outlines the quality standards and best practices for all code and documentation in the Academic Presentations repository. Following these guidelines ensures consistency, maintainability, and reproducibility.

## 🎯 Quality Principles

1. **Correctness** - Code must be accurate and produce correct results
2. **Readability** - Code should be easy to understand
3. **Maintainability** - Code should be easy to modify and extend
4. **Performance** - Code should be reasonably efficient
5. **Documentation** - All code should be well-documented
6. **Testing** - Critical functionality should have tests
7. **Reproducibility** - Results should be reproducible

## 🐍 Python Code Standards

### Style Guide

We follow **PEP 8** with minor modifications:

- **Line length**: 88 characters (Black default)
- **Formatting**: Use Black formatter
- **Import sorting**: Use isort
- **Docstrings**: NumPy style

### Formatting Tools

#### Black (Code Formatter)
```bash
# Format single file
black code/mcmc/metropolis_hastings.py

# Format directory
black code/

# Check without modifying
black --check code/

# Show differences
black --diff code/
```

**Configuration** (in `pyproject.toml`):
```toml
[tool.black]
line-length = 88
target-version = ['py39', 'py310', 'py311']
```

#### isort (Import Sorter)
```bash
# Sort imports in file
isort code/mcmc/metropolis_hastings.py

# Sort all files
isort code/

# Check without modifying
isort --check code/
```

**Configuration** (in `pyproject.toml`):
```toml
[tool.isort]
profile = "black"
line_length = 88
```

### Linting

#### Flake8
```bash
# Lint single file
flake8 code/mcmc/metropolis_hastings.py

# Lint directory
flake8 code/

# Generate HTML report
flake8 --format=html --htmldir=flake-report code/
```

**Configuration** (in `.flake8` or `setup.cfg`):
```ini
[flake8]
max-line-length = 88
extend-ignore = E203, E501, W503
exclude = .git,__pycache__,.venv,build,dist
```

#### Pylint
```bash
# Lint single file
pylint code/mcmc/metropolis_hastings.py

# Lint directory
pylint code/

# Generate report
pylint --output-format=text code/ > pylint_report.txt
```

### Type Checking

#### MyPy
```bash
# Type check single file
mypy code/mcmc/metropolis_hastings.py

# Type check directory
mypy code/

# Strict mode
mypy --strict code/
```

**Add type hints to functions**:
```python
from typing import Optional, Tuple
import numpy as np

def metropolis_hastings(
    target: callable,
    proposal: callable,
    x0: np.ndarray,
    n_samples: int = 10000
) -> Tuple[np.ndarray, float]:
    """
    Run Metropolis-Hastings MCMC sampler.

    Parameters
    ----------
    target : callable
        Target distribution (unnormalized)
    proposal : callable
        Proposal distribution
    x0 : np.ndarray
        Initial state
    n_samples : int, optional
        Number of samples to generate

    Returns
    -------
    samples : np.ndarray
        MCMC samples
    acceptance_rate : float
        Fraction of proposals accepted
    """
    # Implementation
    pass
```

### Documentation

#### Docstring Format (NumPy Style)

```python
def function_name(param1, param2, param3=None):
    """
    Short one-line description.

    More detailed description if needed. Can span multiple
    lines and paragraphs.

    Parameters
    ----------
    param1 : type
        Description of param1
    param2 : type
        Description of param2
    param3 : type, optional
        Description of param3 (default: None)

    Returns
    -------
    output : type
        Description of return value

    Raises
    ------
    ValueError
        When parameters are invalid

    Examples
    --------
    >>> result = function_name(1, 2)
    >>> print(result)
    3

    Notes
    -----
    Additional technical details or mathematical
    formulas can go here.

    References
    ----------
    .. [1] Author et al. "Paper Title." Journal, Year.
    """
    pass
```

### Code Organization

**File Structure**:
```python
"""Module docstring describing purpose."""

# Standard library imports
import os
import sys
from pathlib import Path

# Third-party imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Local imports
from .utils import helper_function

# Module-level constants
CONSTANT_NAME = 42

# Classes and functions
class MyClass:
    """Class docstring."""
    pass

def my_function():
    """Function docstring."""
    pass

# Main execution
if __name__ == "__main__":
    main()
```

## 📊 R Code Standards

### Style Guide

We follow the **tidyverse style guide**:

- **Indentation**: 2 spaces
- **Line length**: 80 characters
- **Naming**: snake_case for functions and variables
- **Assignment**: Use `<-` not `=`

### Formatting Tools

#### styler
```r
# Format single file
styler::style_file("code/causal_inference/instrumental_variables.R")

# Format directory
styler::style_dir("code/")

# Format with tidyverse style
styler::style_file("file.R", style = tidyverse_style)
```

#### lintr
```r
# Lint single file
lintr::lint("code/causal_inference/instrumental_variables.R")

# Lint directory
lintr::lint_dir("code/")

# Lint package
lintr::lint_package()
```

### Code Example

```r
#' Instrumental Variables Regression
#'
#' Estimate causal effects using instrumental variables.
#'
#' @param formula Formula specifying model
#' @param instruments Formula specifying instruments
#' @param data Data frame containing variables
#' @param method Estimation method (default: "2SLS")
#'
#' @return List with coefficients, standard errors, diagnostics
#'
#' @examples
#' # Estimate effect of education on wages using distance as IV
#' result <- instrumental_variables(
#'   wage ~ education + experience,
#'   ~ distance + experience,
#'   data = labor_data
#' )
#'
#' @export
instrumental_variables <- function(formula, instruments, data,
                                    method = "2SLS") {
  # Validate inputs
  if (!inherits(formula, "formula")) {
    stop("formula must be a formula object")
  }

  # Estimate model
  result <- ivreg::ivreg(
    formula = formula,
    instruments = instruments,
    data = data
  )

  # Return results
  return(result)
}
```

## 🧪 Testing

### Python Testing with pytest

**Test file structure** (`tests/test_mcmc.py`):
```python
"""Tests for MCMC implementations."""

import numpy as np
import pytest
from code.mcmc.metropolis_hastings import metropolis_hastings


class TestMetropolisHastings:
    """Test suite for Metropolis-Hastings sampler."""

    def test_normal_distribution(self):
        """Test sampling from normal distribution."""
        # Define target
        def target(x):
            return np.exp(-0.5 * x**2)

        # Run sampler
        samples, acc_rate = metropolis_hastings(
            target=target,
            proposal=lambda x: np.random.normal(x, 1),
            x0=np.array([0.0]),
            n_samples=10000
        )

        # Check properties
        assert len(samples) == 10000
        assert 0.2 < acc_rate < 0.8  # Reasonable acceptance
        assert abs(np.mean(samples)) < 0.1  # Near zero mean
        assert 0.9 < np.std(samples) < 1.1  # Unit variance

    def test_invalid_inputs(self):
        """Test error handling for invalid inputs."""
        with pytest.raises(ValueError):
            metropolis_hastings(
                target=None,  # Invalid
                proposal=lambda x: x,
                x0=np.array([0.0]),
                n_samples=100
            )

    @pytest.mark.slow
    def test_convergence(self):
        """Test convergence for large number of samples."""
        # Long-running test
        pass
```

**Running tests**:
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=code --cov-report=html

# Run specific test file
pytest tests/test_mcmc.py

# Run specific test
pytest tests/test_mcmc.py::TestMetropolisHastings::test_normal_distribution

# Run tests in parallel
pytest -n auto

# Skip slow tests
pytest -m "not slow"

# Verbose output
pytest -v
```

### R Testing with testthat

**Test file structure** (`tests/testthat/test-iv.R`):
```r
test_that("instrumental variables estimation works", {
  # Generate test data
  set.seed(123)
  n <- 1000
  z <- rnorm(n)
  x <- 0.5 * z + rnorm(n, 0, 0.5)
  y <- 2 * x + rnorm(n)
  data <- data.frame(y = y, x = x, z = z)

  # Estimate IV model
  result <- instrumental_variables(
    y ~ x,
    ~ z,
    data = data
  )

  # Check results
  expect_s3_class(result, "ivreg")
  expect_equal(length(coef(result)), 2)
  expect_true(abs(coef(result)["x"] - 2) < 0.2)
})

test_that("invalid inputs raise errors", {
  expect_error(
    instrumental_variables(NULL, ~ z, data.frame()),
    "formula must be a formula object"
  )
})
```

**Running tests**:
```r
# Run all tests
testthat::test_dir("tests/")

# Run specific test file
testthat::test_file("tests/testthat/test-iv.R")

# With coverage
covr::package_coverage()

# Report
covr::report()
```

## 📄 LaTeX Quality

### Spell Checking

We provide tools for spell-checking LaTeX files.

**Using aspell** (Linux/macOS):
```bash
# Check single file
aspell check --mode=tex deep_learning/deep_learning_beamer.tex

# Check all LaTeX files
find . -name "*.tex" -exec aspell check --mode=tex {} \;
```

**Using our Python tool**:
```bash
# Check LaTeX file
python scripts/spell_check.py deep_learning/deep_learning_beamer.tex

# Check all presentations
python scripts/spell_check.py --all
```

### Common LaTeX Issues

**Avoid**:
- Inconsistent spacing
- Orphaned/widow lines
- Overfull hboxes
- Missing citations
- Undefined references

**Check with**:
```bash
# Compile and check for warnings
pdflatex -file-line-error -halt-on-error presentation.tex

# Check for undefined references
grep -i "undefined" presentation.log

# Check for overfull boxes
grep -i "overfull" presentation.log
```

## 🔄 Pre-commit Hooks

We use pre-commit hooks to automatically check code quality before commits.

**Setup**:
```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run manually on all files
pre-commit run --all-files

# Update hooks
pre-commit autoupdate
```

**Configuration** (`.pre-commit-config.yaml`):
- Black formatting
- isort import sorting
- Flake8 linting
- Trailing whitespace removal
- YAML/JSON validation
- And more...

## 📊 Continuous Integration

Our GitHub Actions workflows automatically:
1. **Lint** all code
2. **Format** check with Black/styler
3. **Type check** with MyPy
4. **Run tests** with pytest/testthat
5. **Check coverage**
6. **Build documentation**
7. **Compile LaTeX**

## 🎯 Quality Checklist

Before submitting code, ensure:

### Python
- [ ] Code formatted with Black
- [ ] Imports sorted with isort
- [ ] No linting errors (Flake8, Pylint)
- [ ] Type hints added (where appropriate)
- [ ] Docstrings present (NumPy style)
- [ ] Tests written and passing
- [ ] Coverage > 80% for new code

### R
- [ ] Code formatted with styler
- [ ] No linting errors (lintr)
- [ ] Roxygen documentation present
- [ ] Tests written and passing
- [ ] Examples work

### LaTeX
- [ ] Spell-checked
- [ ] Compiles without errors
- [ ] No undefined references
- [ ] Bibliography complete
- [ ] Figures have captions

### Documentation
- [ ] README updated
- [ ] CHANGELOG updated
- [ ] Code comments clear
- [ ] Examples provided

## 📧 Questions?

For questions about code quality:
- **Issues**: [GitHub Issues](https://github.com/diogoribeiro7/academic-presentations/issues)
- **Email**: dfr@esmad.ipp.pt

---

*Last Updated: January 2025*
*Part of the Academic Presentations repository*
