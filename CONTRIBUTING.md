# Contributing to Academic Presentations

First off, thank you for considering contributing to this project! 🎉

This repository contains academic presentations and course materials for data science and machine learning. We welcome contributions from the community to help improve and expand these educational resources.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Style Guidelines](#style-guidelines)
- [Testing Your Changes](#testing-your-changes)
- [Submitting Changes](#submitting-changes)
- [Community](#community)

## 🤝 Code of Conduct

This project adheres to a code of conduct that all contributors are expected to follow:

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

**Positive behavior includes:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards others

**Unacceptable behavior includes:**
- Trolling, insulting/derogatory comments, and personal attacks
- Public or private harassment
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at [dfr@esmad.ipp.pt](mailto:dfr@esmad.ipp.pt). All complaints will be reviewed and investigated promptly and fairly.

## 🌟 How Can I Contribute?

There are many ways to contribute to this project:

### 1. Report Bugs or Errors

Found a typo, mathematical error, or broken link? Please report it!

- **Check existing issues** first to avoid duplicates
- **Create a new issue** with:
  - Clear, descriptive title
  - Exact location (file and line number if possible)
  - Description of the error
  - Suggested correction (if you have one)

**Example:**
```
Title: Mathematical error in MCMC presentation, slide 15

Description: The acceptance probability formula on slide 15 is missing
the transition probability ratio.

Location: mcmc/mcmc_beamer.tex, line 342

Suggested fix: Add q(x'|x)/q(x|x') to the formula
```

### 2. Suggest Enhancements

Have ideas for improving presentations or adding new content?

- **Open an issue** with tag `enhancement`
- Describe your suggestion clearly
- Explain why it would be valuable
- Include examples if possible

### 3. Add New Presentations

Want to contribute a new presentation on a related topic?

**Before starting:**
1. Open an issue to discuss the topic
2. Wait for approval from maintainers
3. Follow the [style guidelines](#style-guidelines)

**Good topics include:**
- Advanced statistical methods
- New machine learning techniques
- Specialized applications
- Emerging research areas

### 4. Improve Existing Presentations

Contributions to existing presentations are welcome:

- Add clarifying examples
- Improve visualizations
- Add recent references
- Enhance code examples
- Fix errors or ambiguities

### 5. Contribute Code Examples

Add or improve code implementations:

- Must be well-documented
- Include usage examples
- Follow coding standards (PEP 8 for Python, tidyverse for R)
- Add tests where appropriate

### 6. Create Exercises

Contribute problem sets or exercises:

- Align with presentation content
- Include solutions (in separate file)
- Provide clear instructions
- Indicate difficulty level

### 7. Improve Documentation

Help improve READMEs, guides, and documentation:

- Fix unclear instructions
- Add missing information
- Update outdated content
- Improve organization

## 🚀 Getting Started

### Fork and Clone

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:

```bash
git clone https://github.com/YOUR-USERNAME/academic-presentations.git
cd academic-presentations
```

3. **Add upstream** remote:

```bash
git remote add upstream https://github.com/diogoribeiro7/academic-presentations.git
```

### Set Up Development Environment

**For LaTeX:**
```bash
# Ubuntu/Debian
sudo apt-get install texlive-full

# macOS
brew install --cask mactex
```

**For Python code:**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install numpy scipy matplotlib seaborn pandas scikit-learn statsmodels
pip install torch tensorflow  # For deep learning
pip install shap lime  # For XAI
pip install black flake8 pytest  # For development
```

**For R code:**
```r
install.packages(c(
  "AER", "rdrobust", "fixest", "did",
  "caret", "recipes", "mice",
  "forecast", "vars", "fable",
  "testthat", "styler", "lintr"
))
```

## 🔄 Development Workflow

### 1. Create a Branch

Always create a new branch for your work:

```bash
git checkout -b feature/your-feature-name
```

**Branch naming conventions:**
- `feature/` - New features or presentations
- `fix/` - Bug fixes
- `docs/` - Documentation improvements
- `refactor/` - Code refactoring
- `test/` - Adding or updating tests

**Examples:**
- `feature/add-nlp-presentation`
- `fix/mcmc-convergence-formula`
- `docs/improve-installation-guide`

### 2. Make Your Changes

Follow the [style guidelines](#style-guidelines) when making changes.

### 3. Test Your Changes

Before submitting, ensure:

**For LaTeX:**
```bash
# Compile to check for errors
cd your_presentation/
pdflatex your_beamer.tex
pdflatex your_beamer.tex  # Run twice
```

**For Python code:**
```bash
# Format code
black your_script.py

# Check style
flake8 your_script.py

# Run tests
pytest tests/
```

**For R code:**
```r
# Format code
styler::style_file("your_script.R")

# Check style
lintr::lint("your_script.R")

# Run tests
testthat::test_file("tests/test_your_script.R")
```

### 4. Commit Your Changes

Write clear, descriptive commit messages:

```bash
git add .
git commit -m "Add: Brief description of changes

- Detailed point 1
- Detailed point 2
- Detailed point 3"
```

**Good commit messages:**
- `Add: Deep learning presentation with CNN architectures`
- `Fix: Correct Bellman equation in RL slides`
- `Docs: Update installation instructions for M1 Macs`
- `Refactor: Improve MCMC diagnostic plotting functions`

**Bad commit messages:**
- `Update file`
- `Fix bug`
- `Changes`

### 5. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 6. Submit a Pull Request

1. Go to your fork on GitHub
2. Click "New Pull Request"
3. Select your branch
4. Fill in the PR template:
   - Title: Clear, concise description
   - Description: What changes you made and why
   - Related issues: Link any relevant issues
   - Checklist: Complete all items

## 📐 Style Guidelines

### LaTeX Presentations

**General structure:**
```latex
\documentclass[aspectratio=169]{beamer}
\usepackage{../theme/esmad_beamer_theme}

% Author information
\authorname{Your Name}
\authoremail{your.email@institution.edu}
\authororcid{0000-0000-0000-0000}
\authorinstitution{Your Institution}

\title{Presentation Title}
\subtitle{Subtitle if needed}
\date{\today}

\begin{document}

\begin{frame}
  \titlepage
\end{frame}

\tocslide

% Content sections...

\contactslide
\end{document}
```

**Best practices:**

1. **Use theme environments:**
   ```latex
   \begin{theorembox}{Theorem Name}
     Theorem statement
   \end{theorembox}

   \begin{definitionbox}{Definition Name}
     Definition
   \end{definitionbox}

   \begin{examplebox}{Example Title}
     Example content
   \end{examplebox}

   \begin{alertbox}{Important Note}
     Important information
   \end{alertbox}
   ```

2. **Mathematical notation:**
   - Use theme helpers: `\Normal`, `\E`, `\Var`, `\Cov`, `\Prob`
   - Use `\vect{}` for vectors, `\mat{}` for matrices
   - Number important equations
   - Define custom commands for frequently used notation

3. **Code listings:**
   ```latex
   \begin{frame}[fragile]{Code Example}
     \begin{lstlisting}[language=Python]
     def function_name(param):
         """Docstring."""
         return result
     \end{lstlisting}
   \end{frame}
   ```

4. **Structure:**
   - One main idea per slide
   - Maximum 6-7 bullet points per slide
   - Use progressive disclosure (overlays) for complex content
   - Include references to key papers

5. **Figures:**
   - Use vector graphics (PDF) when possible
   - Ensure high resolution (≥300 DPI for raster images)
   - Include descriptive captions
   - Cite source if not original

### Python Code

**Follow PEP 8:**
```python
import numpy as np
import matplotlib.pyplot as plt


class MyClass:
    """Class docstring."""

    def __init__(self, param):
        """Initialize with clear docstring."""
        self.param = param

    def my_method(self, x):
        """
        Method with clear documentation.

        Parameters
        ----------
        x : array-like
            Input data

        Returns
        -------
        result : ndarray
            Processed data
        """
        result = self.param * x
        return result


def standalone_function(x, y=None):
    """
    Function with NumPy-style docstring.

    Parameters
    ----------
    x : float
        First parameter
    y : float, optional
        Second parameter (default: None)

    Returns
    -------
    float
        Result of computation

    Examples
    --------
    >>> standalone_function(1.0)
    2.0
    """
    if y is None:
        y = 1.0
    return x + y
```

**Best practices:**
- Use type hints where appropriate
- Include docstrings for all functions/classes
- Add inline comments for complex logic
- Format with `black`
- Check with `flake8`
- Maximum line length: 88 characters (black default)

### R Code

**Follow tidyverse style:**
```r
# Use descriptive names with underscores
calculate_statistics <- function(data, group_var) {
  #' Calculate summary statistics by group
  #'
  #' @param data A data frame
  #' @param group_var Character string, name of grouping variable
  #' @return A data frame with summary statistics
  #' @examples
  #' calculate_statistics(mtcars, "cyl")

  result <- data %>%
    group_by(.data[[group_var]]) %>%
    summarise(
      mean_value = mean(value, na.rm = TRUE),
      sd_value = sd(value, na.rm = TRUE),
      n = n()
    )

  return(result)
}

# Use spaces around operators
x <- 5 + 3

# Indent with 2 spaces
if (condition) {
  do_something()
} else {
  do_something_else()
}
```

**Best practices:**
- Use `roxygen2` comments for documentation
- Use `tidyverse` style (2-space indents, snake_case)
- Format with `styler`
- Check with `lintr`
- Include examples in documentation

### Bibliographies

**BibTeX format:**
```bibtex
@article{author2023,
  author  = {Last, First and Last, First},
  title   = {Article Title},
  journal = {Journal Name},
  year    = {2023},
  volume  = {10},
  number  = {2},
  pages   = {123--145},
  doi     = {10.1234/journal.2023.12345}
}

@book{author2022,
  author    = {Last, First},
  title     = {Book Title},
  publisher = {Publisher Name},
  year      = {2022},
  edition   = {2nd},
  doi       = {10.1234/book.2022.12345}
}
```

**Requirements:**
- Include DOI when available
- Use consistent naming (firstauthor + year)
- Include all relevant fields
- Verify entries compile correctly

### Exercises

**Structure:**
```latex
\section{Problem X: Topic Name}

\textbf{Problem Statement:}
Clear description of the problem.

\textbf{Tasks:}
\begin{enumerate}
  \item First task
  \item Second task
  \item Third task
\end{enumerate}

\textbf{Data:}
Description of any data provided.

\textbf{Hints:}
\begin{itemize}
  \item Helpful hint 1
  \item Helpful hint 2
\end{itemize}

\textbf{Grading Rubric:} (X points total)
\begin{itemize}
  \item Part 1: Y points
  \item Part 2: Z points
\end{itemize}
```

## ✅ Testing Your Changes

### Pre-submission Checklist

Before submitting a PR, ensure:

**For all contributions:**
- [ ] Code/LaTeX compiles without errors
- [ ] No broken links or references
- [ ] Follows style guidelines
- [ ] Clear, descriptive commit messages
- [ ] PR description is complete

**For LaTeX presentations:**
- [ ] Compiles with `pdflatex` (run twice)
- [ ] All references resolve correctly
- [ ] Figures display properly
- [ ] Mathematical notation is correct
- [ ] Uses ESMAD theme correctly
- [ ] Includes contact slide
- [ ] No overfull/underfull boxes (major ones)

**For code contributions:**
- [ ] Follows language style guide (PEP 8 / tidyverse)
- [ ] Includes comprehensive docstrings/comments
- [ ] Includes usage examples
- [ ] Tests pass (if applicable)
- [ ] No linting errors

**For exercises:**
- [ ] Clear problem statements
- [ ] Appropriate difficulty level
- [ ] Solutions provided (separate file)
- [ ] Compiles to PDF correctly

### Automated Checks

When you submit a PR, GitHub Actions will automatically:

1. **Compile all LaTeX documents**
2. **Check all links** (markdown, DOIs, URLs)
3. **Run code tests** (if applicable)
4. **Check code style**

Your PR must pass all checks before it can be merged.

## 📝 Submitting Changes

### Pull Request Process

1. **Ensure your PR:**
   - Has a clear, descriptive title
   - References any related issues
   - Includes a detailed description
   - Passes all automated checks

2. **PR Title format:**
   ```
   [Type] Brief description

   Examples:
   [Feature] Add Natural Language Processing presentation
   [Fix] Correct formula in HMC derivation
   [Docs] Improve installation guide for Windows
   [Refactor] Simplify MCMC diagnostic code
   ```

3. **PR Description should include:**
   ```markdown
   ## Description
   Brief overview of changes

   ## Motivation and Context
   Why is this change needed?

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Code refactoring

   ## Related Issues
   Fixes #123

   ## How Has This Been Tested?
   Description of testing

   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Self-review completed
   - [ ] Documentation updated
   - [ ] No new warnings
   - [ ] Tests pass
   ```

4. **Review process:**
   - Maintainers will review your PR
   - May request changes or ask questions
   - Make requested changes in your branch
   - Push updates (PR will automatically update)

5. **After approval:**
   - PR will be merged by maintainers
   - Your contribution will be credited
   - Branch can be safely deleted

### What Happens After Merging?

Once your PR is merged:

1. **Automated compilation** generates new PDFs
2. **PDF previews** are updated
3. **GitHub release** is created (if applicable)
4. **CHANGELOG** is updated
5. **Contributors** list is updated

## 🎓 First-Time Contributors

Never contributed to an open-source project before? Here's a quick guide:

1. **Find an issue** labeled `good first issue` or `help wanted`
2. **Comment** on the issue expressing interest
3. **Wait for** maintainer approval
4. **Follow** the development workflow above
5. **Ask questions** if you're stuck!

### Good First Issues

Look for issues tagged:
- `good first issue` - Perfect for beginners
- `help wanted` - Extra help needed
- `documentation` - Usually straightforward
- `typo` - Quick fixes

### Getting Help

Stuck? Here's how to get help:

- **Comment on your issue/PR** - Maintainers will respond
- **Check documentation** - `README.md`, `STYLE_GUIDE.md`
- **Search existing issues** - Someone may have had the same question
- **Email maintainer** - dfr@esmad.ipp.pt (for complex questions)

## 👥 Community

### Communication Channels

- **GitHub Issues** - Bug reports, feature requests, questions
- **Pull Requests** - Code review and discussion
- **Email** - dfr@esmad.ipp.pt

### Recognition

Contributors are recognized in:

- **CHANGELOG.md** - All contributions noted
- **Contributors section** - In README.md
- **Acknowledgments slide** - In presentations (for significant contributions)

### Attribution

By contributing, you agree that:

- Presentations/exercises are licensed under **CC BY-SA 4.0**
- Code is licensed under **MIT License**
- You have the right to submit the content
- Your contribution may be redistributed per these licenses

## 📚 Additional Resources

### Learning Resources

- [LaTeX Beamer Documentation](https://ctan.org/pkg/beamer)
- [PEP 8 Style Guide](https://pep8.org/)
- [Tidyverse Style Guide](https://style.tidyverse.org/)
- [Git Best Practices](https://git-scm.com/book/en/v2)

### Tools

- **LaTeX:** [Overleaf](https://www.overleaf.com/) (online editor)
- **Python:** [Black](https://github.com/psf/black) (formatter)
- **R:** [styler](https://styler.r-lib.org/) (formatter)
- **Git:** [GitHub Desktop](https://desktop.github.com/) (GUI client)

### Examples

See existing presentations and code for examples:

- **Presentation structure:** `deep_learning/deep_learning_beamer.tex`
- **Python code:** `code/mcmc/metropolis_hastings.py`
- **R code:** `code/causal_inference/instrumental_variables.R`
- **Exercises:** `exercises/mcmc/mcmc_exercises.tex`

## 📧 Questions?

Still have questions? Contact:

- **Email:** dfr@esmad.ipp.pt
- **GitHub Issues:** [Create an issue](https://github.com/diogoribeiro7/academic-presentations/issues/new)
- **ORCID:** [0009-0001-2022-7072](https://orcid.org/0009-0001-2022-7072)

---

**Thank you for contributing to make these educational materials better!** 🎉

Every contribution, no matter how small, is valued and appreciated. Together, we can create comprehensive, high-quality resources for the data science community.

---

*Last updated: January 2025*
*Maintainer: Diogo Ribeiro*
