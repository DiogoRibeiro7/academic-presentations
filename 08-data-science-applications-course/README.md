# Domain 08: Data Science Applications Course

## Overview

This is a **composite course** that combines modular sections from multiple domains into a unified "Data Science Applications" presentation. This course is designed for industry-focused training or executive education where a broad survey of data science topics is more appropriate than deep dives into individual subjects.

## Purpose

The materials in this domain are **modular LaTeX sections** that can be combined to create custom presentations tailored to specific audiences or time constraints.

## Architecture

### Modular Sections

This course is built from reusable LaTeX sections (NOT standalone documents):

```latex
% Each section starts with \section{} not \documentclass{}
\section{Deep Learning Fundamentals}
% ... content ...
```

### Available Sections

| Section | Source | Slides | Topics Covered |
|---------|--------|--------|----------------|
| Deep Learning | `sections/deep_learning_section.tex` | ~45 | Neural networks, CNNs, RNNs, Transformers |
| Time Series | `sections/time_series_section.tex` | ~40 | ARIMA, ML methods, deep learning for TS |
| Explainable AI | `sections/explainable_ai_section.tex` | ~40 | SHAP, LIME, interpretability |
| MLOps & Deployment | `sections/mlops_deployment_section.tex` | ~35 | Production ML, monitoring, DevOps |

## Usage

### Master Presentation

The `main_presentation.tex` file includes selected sections:

```latex
\documentclass[aspectratio=169]{beamer}
\usepackage{../../shared/theme/esmad_beamer_theme}

\title{Data Science in Practice}
\subtitle{Industry Applications}

\begin{document}

\begin{frame}
  \titlepage
\end{frame}

% Include desired sections
\input{sections/deep_learning_section.tex}
\input{sections/mlops_deployment_section.tex}
\input{sections/explainable_ai_section.tex}

\end{document}
```

### Customization Options

**Option 1: Full Course** (~160 slides, 2-3 days workshop)
- Include all 4 sections

**Option 2: ML Deployment Focus** (~80 slides, 1-day workshop)
- Deep Learning section
- MLOps section

**Option 3: Advanced Topics** (~80 slides, 1-day)
- Time Series section
- Explainable AI section

## Relationship to Standalone Topics

### Key Distinction

The sections in this domain are **SHORTER** versions designed for overview presentations. For in-depth coverage, use the standalone topic presentations in their respective domains:

| Section (This Domain) | Standalone Version (Other Domains) |
|-----------------------|-----------------------------------|
| `deep_learning_section.tex` (25K, ~45 slides) | `/02-deep-learning/deep-learning-fundamentals/` (26K, more depth) |
| `time_series_section.tex` (16K, ~40 slides) | `/05-time-series/time-series-forecasting/` (24K, comprehensive) |
| `explainable_ai_section.tex` (21K, ~40 slides) | `/06-advanced-topics/explainable-ai/` (24K, more examples) |

**Use this domain for**: Industry training, executive briefings, survey courses
**Use standalone domains for**: Academic courses, professional certifications, deep learning

## Materials

```
08-data-science-applications-course/
├── presentation/
│   ├── main_presentation.tex      # Master file for composing sections
│   ├── sections/                  # Modular LaTeX sections
│   │   ├── deep_learning_section.tex
│   │   ├── time_series_section.tex
│   │   ├── explainable_ai_section.tex
│   │   └── mlops_deployment_section.tex
│   └── README.md
├── assessments/                   # Industry-focused assessments
│   ├── case_studies/
│   └── project_templates/
├── exercises/                     # Applied exercises
└── README.md                      # This file
```

## Target Audiences

1. **Corporate Training**: 1-3 day workshops for practitioners
2. **Executive Education**: High-level overview for decision-makers
3. **Bootcamps**: Intensive short-form courses
4. **Conference Workshops**: Half-day or full-day tutorials

## Compilation

### Compile Full Course
```bash
cd presentation/
pdflatex main_presentation.tex
```

### Compile Custom Selection
Edit `main_presentation.tex` to include only desired sections:
```latex
\input{sections/deep_learning_section.tex}
% \input{sections/time_series_section.tex}    % Commented out
\input{sections/mlops_deployment_section.tex}
```

## Maintenance

When updating content:
1. **Section updates**: Edit files in `presentation/sections/`
2. **Synchronization**: If changes should propagate to standalone versions, update those separately
3. **Independence**: Sections are self-contained (no cross-references between sections)

## Prerequisites

Varies by sections included:
- Programming (Python/R)
- Basic ML knowledge
- Statistics fundamentals

See individual section comments for specific prerequisites.
