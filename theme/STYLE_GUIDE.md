# ESMAD Beamer Theme - Style Guide

## Overview

The ESMAD Beamer Theme provides consistent, professional styling for all academic presentations in this repository. This guide explains how to use the theme and maintain visual consistency.

## Quick Start

### Basic Template

```latex
\documentclass[aspectratio=169]{beamer}

% Use the ESMAD theme
\usepackage{theme/esmad_beamer_theme}

% Set author information (optional - defaults provided)
\authorname{Diogo Ribeiro}
\authoremail{dfr@esmad.ipp.pt}
\authororcid{0009-0001-2022-7072}
\authorinstitution{ESMAD - Escola Superior de Média Arte e Design}
\authorcompany{Lead Data Scientist, Mysense.ai}

\title{Your Presentation Title}
\subtitle{Optional Subtitle}
\date{\today}

\begin{document}

\begin{frame}
  \titlepage
\end{frame}

\tocslide

% Your content here

\contactslide

\end{document}
```

## Color Palette

### Primary Colors

- **ESMADBlue** (RGB: 0, 51, 102) - Primary brand color for titles and structure
- **ESMADLightBlue** (RGB: 51, 102, 153) - Secondary elements and highlights
- **ESMADAccent** (RGB: 204, 51, 0) - Accent color for important highlights
- **ESMADGray** (RGB: 128, 128, 128) - Text and subtle elements
- **ESMADLightGray** (RGB: 240, 240, 240) - Backgrounds and boxes

### Usage Guidelines

```latex
% Use colors in text
\textcolor{ESMADBlue}{Important text}
\textcolor{ESMADAccent}{Alert/Warning}

% Use in TikZ
\draw[color=ESMADBlue, thick] ...
```

## Custom Environments

### Theorem Box

```latex
\begin{theorembox}{Theorem Name}
  Your theorem statement here.
\end{theorembox}
```

**Appearance:** Blue frame, light gray background

### Definition Box

```latex
\begin{definitionbox}{Definition: MCMC}
  A Markov Chain Monte Carlo method is...
\end{definitionbox}
```

**Appearance:** Light blue frame, light gray background

### Example Box

```latex
\begin{examplebox}{Example 1: Metropolis-Hastings}
  Consider sampling from $\pi(x) = \mathcal{N}(0,1)$...
\end{examplebox}
```

**Appearance:** Light blue frame, white background

### Alert Box

```latex
\begin{alertbox}{Important!}
  Remember to check convergence diagnostics!
\end{alertbox}
```

**Appearance:** Red/accent frame, white background, bold

## Code Listings

### Python Code

```latex
\begin{lstlisting}[language=Python, caption=Metropolis-Hastings]
def metropolis_hastings(target, proposal, x0, n_samples):
    samples = [x0]
    for i in range(n_samples):
        x_current = samples[-1]
        x_proposed = proposal(x_current)
        accept_prob = min(1, target(x_proposed) / target(x_current))
        if np.random.rand() < accept_prob:
            samples.append(x_proposed)
        else:
            samples.append(x_current)
    return np.array(samples)
\end{lstlisting}
```

### R Code

```latex
\begin{lstlisting}[language=R, caption=Linear Regression]
model <- lm(y ~ x1 + x2, data = df)
summary(model)
\end{lstlisting}
```

## Mathematical Notation

### Predefined Commands

```latex
% Distributions
\Normal(0, 1)           % N(0,1)
\Uniform(0, 1)          % U(0,1)
\Bernoulli(p)           % Bernoulli(p)

% Probability operators
\E[X]                   % Expectation
\Var(X)                 % Variance
\Cov(X, Y)             % Covariance
\Prob(A)               % Probability

% Other operators
\argmax_{x}            % argmax
\argmin_{x}            % argmin

% Vectors and matrices
\vect{x}               % Bold vector
\mat{A}                % Bold matrix

% Independence
X \indep Y             % Independence symbol
```

### Example Usage

```latex
\begin{frame}{Bayesian Inference}
  Posterior distribution:
  \begin{equation}
    p(\theta | y) = \frac{p(y | \theta) p(\theta)}{p(y)}
  \end{equation}

  where $\theta \sim \Normal(\mu_0, \sigma_0^2)$ and $\E[\theta | y]$ is the posterior mean.
\end{frame}
```

## Slide Templates

### Title Slide

```latex
\begin{frame}
  \titlepage
\end{frame}
```

Automatically includes:
- Title and subtitle
- Author name
- Institution and company
- Email and ORCID (with icons)
- Date

### Table of Contents

```latex
\tocslide
```

### Section Slide

Automatically generated at the start of each section:

```latex
\section{Introduction}
% Automatically creates a section slide
```

### Contact Slide

```latex
\contactslide
```

Includes:
- Name and affiliations
- Email
- ORCID
- GitHub
- LinkedIn
- Repository link

### Acknowledgments Slide

```latex
\acknowledgmentsslide{
  \item ESMAD for institutional support
  \item Mysense.ai for industry collaboration
  \item Students and colleagues for feedback
}
```

### References Slide

```latex
\referenceslide{../bibliographies/mcmc_references}
```

## Typography Guidelines

### Font Sizes

- **Title:** Large, bold
- **Frame titles:** Bold, colored (ESMADBlue)
- **Body text:** Normal serif
- **Code:** Monospace (ttfamily)
- **Math:** Computer Modern (default LaTeX math)

### Emphasis

```latex
\textbf{Bold for important terms}
\emph{Italic for emphasis}
\alert{Red/accent for alerts}
```

### Lists

```latex
\begin{itemize}
  \item First level (circle bullet, ESMADBlue)
  \begin{itemize}
    \item Second level (dash, ESMADLightBlue)
    \begin{itemize}
      \item Third level (dot, ESMADGray)
    \end{itemize}
  \end{itemize}
\end{itemize}

\begin{enumerate}
  \item Numbered item
  \item Another item
\end{enumerate}
```

## Figures and Images

### Basic Figure

```latex
\begin{frame}{Results}
  \begin{figure}
    \centering
    \includegraphics[width=0.8\textwidth]{figures/trace_plot.pdf}
    \caption{Trace plot showing convergence}
  \end{figure}
\end{frame}
```

### Multiple Figures

```latex
\begin{frame}{Comparison}
  \begin{columns}
    \column{0.5\textwidth}
    \centering
    \includegraphics[width=\textwidth]{fig1.pdf}
    \caption*{Method A}

    \column{0.5\textwidth}
    \centering
    \includegraphics[width=\textwidth]{fig2.pdf}
    \caption*{Method B}
  \end{columns}
\end{frame}
```

## Tables

### Professional Tables

```latex
\begin{frame}{Results Table}
  \begin{table}
    \centering
    \caption{Estimation Results}
    \begin{tabular}{lrrr}
      \toprule
      Method & Estimate & SE & 95\% CI \\
      \midrule
      OLS & 1.234 & 0.056 & [1.124, 1.344] \\
      IV & 1.456 & 0.089 & [1.281, 1.631] \\
      \bottomrule
    \end{tabular}
  \end{table}
\end{frame}
```

## TikZ Diagrams

### Simple Flowchart

```latex
\begin{frame}{MCMC Algorithm}
  \begin{center}
    \begin{tikzpicture}[
      node distance=2cm,
      box/.style={rectangle, draw=ESMADBlue, thick, fill=ESMADLightGray,
                  text width=3cm, text centered, rounded corners, minimum height=1cm}
    ]
      \node[box] (init) {Initialize $x_0$};
      \node[box, below of=init] (propose) {Propose $x'$};
      \node[box, below of=propose] (accept) {Accept/Reject};
      \node[box, below of=accept] (update) {Update chain};

      \draw[->, thick] (init) -- (propose);
      \draw[->, thick] (propose) -- (accept);
      \draw[->, thick] (accept) -- (update);
      \draw[->, thick] (update.west) -- ++(-1,0) |- (propose.west);
    \end{tikzpicture}
  \end{center}
\end{frame}
```

## Aspect Ratio

**Recommended:** 16:9 for modern displays

```latex
\documentclass[aspectratio=169]{beamer}
```

**Alternative:** 4:3 for older projectors

```latex
\documentclass[aspectratio=43]{beamer}
```

## Font Options

### For Better Screen Readability

```latex
\documentclass[aspectratio=169]{beamer}
\usefonttheme{professionalfonts}  % Use non-serif fonts for slides
```

### For Mathematical Content

```latex
\documentclass[aspectratio=169]{beamer}
% Keep default (serif) fonts for better math rendering
```

## Best Practices

### Do's

✅ Use consistent color scheme from theme
✅ Include author info on title slide
✅ Add frame numbers in footer
✅ Use section slides to break up content
✅ Include contact slide at end
✅ Use theorem/definition boxes for important concepts
✅ Keep slides uncluttered (max 6-7 bullets per slide)
✅ Use high-quality vector graphics (PDF) when possible
✅ Include references for key papers/methods

### Don'ts

❌ Don't mix multiple color schemes
❌ Don't use low-resolution images
❌ Don't overcrowd slides with text
❌ Don't use more than 3 levels of bullet points
❌ Don't forget to cite sources
❌ Don't use fancy transitions (keep it professional)
❌ Don't use multiple fonts

## Customization

### Override Author Info

```latex
\authorname{Your Name}
\authoremail{your.email@institution.edu}
\authororcid{0000-0000-0000-0000}
\authorinstitution{Your Institution}
\authorcompany{Your Company/Position}
```

### Custom Colors

```latex
% Add to preamble
\definecolor{MyColor}{RGB}{100, 150, 200}
```

## Compilation

### Recommended Workflow

```bash
# For presentations with bibliography
pdflatex presentation.tex
bibtex presentation
pdflatex presentation.tex
pdflatex presentation.tex

# Or use latexmk
latexmk -pdf presentation.tex
```

### Clean Build

```bash
latexmk -c  # Remove auxiliary files
latexmk -C  # Remove all generated files including PDF
```

## Examples

See template files:
- `theme/template_presentation.tex` - Basic template
- `mcmc/mcmc_beamer.tex` - Full MCMC presentation
- `data_science_applications/causal_inference_beamer.tex` - Causal inference

## Support

For questions or suggestions:
- Email: dfr@esmad.ipp.pt
- GitHub Issues: https://github.com/diogoribeiro7/academic-presentations/issues

## Version History

- **v1.0** (2025-01): Initial release
  - Professional color scheme
  - Custom boxes and environments
  - Contact and reference slide templates
  - Mathematical notation helpers

---

**Maintained by:** Diogo Ribeiro, ESMAD
**License:** CC BY-SA 4.0 (presentations), MIT (code)
