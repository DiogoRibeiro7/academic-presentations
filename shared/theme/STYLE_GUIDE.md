# Academic Beamer Style Guide

## Purpose

All standalone Beamer presentations in this repository should use the same visual model. Presentation-specific titles, subtitles, aspect ratios, font-size class options, mathematical notation, diagrams, and domain-specific packages remain local to each deck.

The canonical model is deliberately simple: Madrid, the default Beamer color theme, a red palette, and a common `listings` style. The shared theme package exists as a compatibility/helper layer for decks that already use it; it must not introduce a competing visual identity.

## Canonical Beamer Model

Preserve any existing `\documentclass` options. For example, both of these are valid:

```latex
\documentclass{beamer}
```

```latex
\documentclass[aspectratio=169,11pt]{beamer}
```

The common presentation shell is:

```latex
\usepackage{bookmark}

\usetheme{Madrid}
\usecolortheme{default}
\usepackage{listings}
\usepackage{xcolor}

\lstdefinestyle{code}{
  language=Python,
  basicstyle=\ttfamily\small,
  keywordstyle=\color{blue},
  commentstyle=\color{gray},
  stringstyle=\color{red!60!black},
  showstringspaces=false,
  tabsize=2,
  breaklines=true
}

\setbeamercolor{palette primary}{bg=red, fg=white}
\setbeamercolor{palette secondary}{bg=red!95!black, fg=white}
\setbeamercolor{palette tertiary}{bg=red!90!black, fg=white}
\setbeamercolor{frametitle}{bg=red, fg=white}
\setbeamercolor{title}{bg=red, fg=white}
\setbeamercolor{section in toc}{fg=red}
```

Beamer loads `hyperref` itself, so a Beamer deck does not need to add a second `\usepackage{hyperref}` merely for `bookmark`.

## Metadata

Use ordinary Beamer metadata in standalone decks:

```latex
\title[Short Title]{Full Presentation Title}
\subtitle{Optional Subtitle}
\author{Diogo Ribeiro}
\institute{Faculty of Media Arts and Design, Technical University of Porto}
\date{\today}
```

The canonical author identity for this repository is:

- **Name:** Diogo Ribeiro
- **ORCID:** 0009-0001-2022-7072
- **Affiliation:** Faculty of Media Arts and Design, Technical University of Porto
- **Email:** dfr@esmad.ipp.pt
- **LinkedIn:** https://www.linkedin.com/in/diogo-ribeiro-9094604a/

Do not present MySense.ai as a current affiliation or employer.

## Shared Theme Compatibility Layer

Decks that already use the shared package may continue to load it:

```latex
\usepackage{../../../shared/theme/esmad_beamer_theme}
```

The filename is retained for compatibility. The package follows the canonical Madrid/red model and provides reusable helpers such as:

```latex
\authorname{Diogo Ribeiro}
\authoremail{dfr@esmad.ipp.pt}
\authororcid{0009-0001-2022-7072}
\authorinstitution{Faculty of Media Arts and Design, Technical University of Porto}
```

`\authorcompany{...}` remains only as a legacy no-op so older source files continue to compile. It must not be used for current metadata.

The shared package also provides mathematical helpers, contact/reference slides, and custom box environments. Those helpers do not define a separate presentation style.

## Code Listings

### Python

The canonical Python listing style is named `code`:

```latex
\begin{lstlisting}[style=code]
import numpy as np

x = np.random.normal(size=100)
print(x.mean())
\end{lstlisting}
```

A deck may use `\lstset{style=code}` when Python is its default language.

### Other Languages

R, SQL, pseudocode, or other domain-specific languages may define a language-specific style when required, but the visual treatment should inherit the same principles:

- monospaced text;
- blue keywords;
- gray comments;
- dark-red strings;
- no visible spaces in strings;
- sensible line wrapping;
- consistent tab width.

Language-specific syntax is an exception to the Python language setting, not an excuse for a different slide palette or unrelated code theme.

## Content-Specific Colors

Decks may define extra colors for diagrams, charts, or semantic annotations. For example:

```latex
\definecolor{forest}{RGB}{34,139,34}
\definecolor{crimson}{RGB}{178,34,52}
```

These colors may be used inside figures or explanatory content. They must not override the canonical Beamer title, frame-title, palette, or table-of-contents colors.

Avoid source-level overrides such as:

```latex
\setbeamercolor{title}{bg=navyblue,fg=white}
\setbeamercolor{frametitle}{bg=navyblue,fg=white}
```

## Title and Navigation

Use standard Beamer title rendering:

```latex
\begin{frame}
  \titlepage
\end{frame}
```

A normal outline slide is:

```latex
\begin{frame}{Outline}
  \tableofcontents
\end{frame}
```

Deck-specific `\AtBeginSection` outline slides may be retained when they are pedagogically useful.

Do not introduce a second custom title-page system or a deck-specific footer solely for branding. The model should remain recognizably the same across presentations.

## Custom Environments

The shared theme retains reusable boxes for decks that need them:

```latex
\begin{theorembox}{Theorem}
  Statement.
\end{theorembox}
```

```latex
\begin{definitionbox}{Definition}
  Definition text.
\end{definitionbox}
```

```latex
\begin{examplebox}{Example}
  Example text.
\end{examplebox}
```

```latex
\begin{alertbox}{Important}
  Important text.
\end{alertbox}
```

These are optional content helpers. Standard Beamer `block`, `alertblock`, `exampleblock`, `theorem`, and `definition` environments are equally valid.

## Mathematical Notation

The shared theme provides common notation helpers, including:

```latex
\Normal
\Uniform
\Bernoulli
\E
\Var
\Cov
\Prob
\argmax
\argmin
\vect{x}
\mat{A}
\indep
```

Deck-local mathematical commands may be retained when they are specific to the subject.

## Aspect Ratio and Font Size

Do not normalize physical slide dimensions by deleting existing class options.

Examples:

```latex
\documentclass[aspectratio=169]{beamer}
```

```latex
\documentclass[aspectratio=169,11pt]{beamer}
```

```latex
\documentclass{beamer}
```

All three can follow the same visual model.

## Figures, Tables, and Diagrams

Use ordinary LaTeX/Beamer conventions. Topic-specific TikZ libraries, `pgfplots`, `booktabs`, subfigures, algorithms, and other packages should remain local to decks that need them.

The consistency rule applies to the presentation shell, not to the scientific content.

## Best Practices

### Do

- preserve each deck's existing `\documentclass` options;
- use Madrid with the default color theme;
- use the canonical red Beamer palette;
- keep the `code` listing style as the Python default;
- preserve mathematical and pedagogical content;
- keep topic-specific packages and macros where required;
- use the current faculty affiliation;
- compile every changed standalone deck.

### Do Not

- use `seahorse` or another competing Beamer color theme;
- override title/frame-title colors with a deck-specific blue palette;
- present the former MySense.ai role as current metadata;
- replace the current faculty name with the old ESMAD display name;
- remove aspect-ratio or font-size class options for the sake of consistency;
- introduce source-normalization scripts or self-modifying workflows;
- change mathematical or teaching content during a visual-shell migration.

## Compilation

Use `latexmk` when possible:

```bash
latexmk -pdf presentation.tex
```

For files with BibTeX:

```bash
pdflatex presentation.tex
bibtex presentation
pdflatex presentation.tex
pdflatex presentation.tex
```

The repository CI is the authoritative regression check for supported standalone presentation entry points.

## Source of Truth

For visual consistency, use this guide together with:

- `shared/theme/esmad_beamer_theme.sty` for shared-theme consumers;
- `shared/author.json` for canonical author identity;
- the repository's LaTeX compilation workflow for regression validation.

Historical migration documents may describe older styling and should not be treated as the current presentation contract.

---

**Maintained by:** Diogo Ribeiro  
**Affiliation:** Faculty of Media Arts and Design, Technical University of Porto  
**License:** CC BY-SA 4.0 for presentation content; MIT for code
