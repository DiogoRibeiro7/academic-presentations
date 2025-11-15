# R Programming

## Overview

Comprehensive introduction to R programming for data science and statistical computing.

## Contents

### Presentation
- `R_programming.tex` - Complete R programming course presentation

## Topics Covered

1. **R Basics**
   - Data types and structures
   - Vectors, matrices, data frames, lists
   - Control flow (if/else, loops)
   - Functions

2. **Data Manipulation**
   - Base R data manipulation
   - tidyverse ecosystem
   - dplyr for data transformation
   - tidyr for data reshaping

3. **Visualization**
   - Base R graphics
   - ggplot2 fundamentals
   - Advanced plotting techniques
   - Interactive visualizations

4. **Statistical Computing**
   - Descriptive statistics
   - Statistical tests
   - Linear models
   - Generalized linear models

5. **Reproducible Research**
   - R Markdown
   - knitr
   - Report generation

## Prerequisites

- None (beginner-friendly)
- Basic computer literacy
- Familiarity with basic statistics helpful but not required

## Learning Outcomes

After completing this module, students will be able to:
- Write functional R programs for data analysis
- Import, clean, and transform datasets
- Create publication-quality visualizations
- Perform statistical analyses
- Generate reproducible reports with R Markdown

## Duration

- **Lecture time**: 6-8 hours
- **Practice time**: 8-12 hours
- **Total**: 2-3 weeks at standard pace

## Installation

### R
Download from: https://cran.r-project.org/

### RStudio (Recommended IDE)
Download from: https://posit.co/download/rstudio-desktop/

### Required Packages
```r
install.packages(c(
  "tidyverse",  # Core tidyverse packages
  "ggplot2",    # Visualization
  "dplyr",      # Data manipulation
  "tidyr",      # Data reshaping
  "readr",      # Data import
  "knitr",      # Report generation
  "rmarkdown"   # Markdown documents
))
```

## Compilation

```bash
cd 00-programming-fundamentals/r-programming/presentation/
pdflatex R_programming.tex
pdflatex R_programming.tex  # Run twice for references
```

## Related Materials

- Exercises: TBD (add to `exercises/` directory)
- Code examples: TBD (add to `code/` directory)

## Further Learning

After completing this module, proceed to:
- 01-Foundations (Statistical Modeling, Feature Engineering)
- 03-Bayesian Methods (Bayesian Machine Learning, MCMC)
- 04-Causal Inference (uses R extensively)

## References

- R for Data Science (Wickham & Grolemund)
- Advanced R (Wickham)
- R Graphics Cookbook (Chang)
