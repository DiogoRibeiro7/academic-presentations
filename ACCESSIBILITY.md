# Accessibility Guidelines

**Making Academic Presentations Accessible to All Learners**

Last Updated: January 2025

## 📚 Overview

This document outlines accessibility standards and best practices for creating inclusive educational materials. Our goal is to ensure that all students, regardless of ability, can access and benefit from our course content.

## 🎯 Accessibility Principles

We follow **WCAG 2.1 Level AA** guidelines and aim for:

1. **Perceivable** - Information must be presentable to users in ways they can perceive
2. **Operable** - Interface components must be operable by all users
3. **Understandable** - Information and operation must be understandable
4. **Robust** - Content must be robust enough for various assistive technologies

## 📊 Visual Accessibility

### Color Contrast

**Minimum Contrast Ratios** (WCAG AA):
- **Normal text**: 4.5:1
- **Large text** (18pt+ or 14pt+ bold): 3:1
- **Graphics and UI components**: 3:1

**Check contrast with tools:**
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Contrast Ratio Calculator](https://contrast-ratio.com/)
- macOS: Digital Color Meter
- Browser extensions: WAVE, axe DevTools

**Best Practices:**
```latex
% Bad: Low contrast
\definecolor{lightgray}{RGB}{200,200,200}  % On white
\color{lightgray}Important text

% Good: High contrast
\definecolor{darkgray}{RGB}{51,51,51}  % On white (12.6:1)
\color{darkgray}Important text
```

### Color Blindness

**Never rely solely on color** to convey information.

**Guidelines:**
- Use patterns, shapes, or labels in addition to color
- Avoid red-green combinations (most common color blindness)
- Use color-blind safe palettes

**Recommended Color Palettes:**

**Okabe-Ito palette** (color-blind safe):
```latex
\definecolor{oiblue}{RGB}{0,114,178}
\definecolor{oiorange}{RGB}{230,159,0}
\definecolor{oigreen}{RGB}{0,158,115}
\definecolor{oiyellow}{RGB}{240,228,66}
\definecolor{oipurple}{RGB}{204,121,167}
\definecolor{oired}{RGB}{213,94,0}
\definecolor{oicyan}{RGB}{86,180,233}
```

**Viridis** (perceptually uniform):
- Good for heatmaps and continuous data
- Readable in grayscale
- Color-blind friendly

**Testing Tools:**
- [Coblis Color Blindness Simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/)
- [Color Oracle](https://colororacle.org/) - Desktop app
- Photoshop: View → Proof Setup → Color Blindness

### Font Considerations

**Size:**
- **Minimum body text**: 11pt (12pt recommended)
- **Minimum code/math**: 10pt
- **Headings**: At least 1.5× body text

**Font Choices:**
- **Sans-serif for slides**: Helvetica, Arial, Calibri
- **Serif for body text**: Times, Palatino
- **Monospace for code**: Courier, Consolas, Monaco

**Avoid:**
- Decorative or script fonts
- All caps (harder to read)
- Overly condensed fonts
- Light weights for body text

```latex
% Good slide font configuration
\usefonttheme{professionalfonts}
\setbeamerfont{title}{size=\Large,series=\bfseries}
\setbeamerfont{normal text}{size=\normalsize}
\setbeamerfont{footnote}{size=\scriptsize}

% Minimum 11pt for body
\documentclass[11pt]{beamer}  % or 12pt
```

### Visual Layout

**Spacing:**
- Line spacing: 1.5× for body text
- Paragraph spacing: At least 1.5× line height
- Margin: Generous whitespace

**Structure:**
- Clear visual hierarchy
- Consistent formatting
- Logical reading order
- Not overly crowded

```latex
% Good spacing
\setlength{\parskip}{1.5ex}
\setlength{\lineskip}{1.5}

% Bad: Too much on one slide
\begin{frame}
% 15 bullet points, equations, code, and figures
\end{frame}

% Good: One concept per slide
\begin{frame}{Clear Title}
% 3-5 bullet points OR one equation OR one figure
\end{frame}
```

## 🖼️ Images and Figures

### Alt Text

**Every figure must have descriptive alt text.**

```latex
% LaTeX: Use caption
\begin{figure}
  \includegraphics{figure.pdf}
  \caption{Line plot showing training loss (y-axis)
           decreasing from 2.5 to 0.1 over 100 epochs
           (x-axis), indicating successful model training.}
  \label{fig:training}
\end{figure}

% For images without captions
\pdftooltip{\includegraphics{icon.pdf}}{
  Icon showing a neural network with 3 layers
}
```

**Writing Good Alt Text:**

**Bad:**
```
"Figure 1"
"Graph"
"Training results"
```

**Good:**
```
"Scatter plot showing positive linear relationship between
study hours (x-axis, 0-10) and exam scores (y-axis, 40-100),
with R²=0.87 indicating strong correlation."
```

**Guidelines:**
- Describe the content and purpose
- Include data trends and key takeaways
- Keep it concise but informative
- Don't start with "Image of..." or "Graph showing..."

### Complex Figures

For complex visualizations:

1. **Provide textual description** in caption or text
2. **Describe key findings** in bullet points
3. **Include data table** if appropriate
4. **Link to accessible version** (SVG, interactive)

```latex
\begin{frame}{Model Performance}
\begin{columns}
\column{0.5\textwidth}
\includegraphics[width=\textwidth]{complex_viz.pdf}

\column{0.5\textwidth}
Key findings:
\begin{itemize}
  \item Model A: 95\% accuracy
  \item Model B: 92\% accuracy
  \item Significant at $p < 0.01$
\end{itemize}
\end{columns}
\end{frame}
```

## 📝 Document Structure

### Headings

**Use proper heading hierarchy:**

```latex
% Correct hierarchy
\section{Introduction}
\subsection{Background}
\subsubsection{Related Work}

% Incorrect: Skipping levels
\section{Introduction}
\subsubsection{Background}  % Skipped subsection!
```

**Benefits:**
- Screen readers navigate by headings
- Logical structure
- Better comprehension

### Lists

**Use semantic list structures:**

```latex
% Ordered list
\begin{enumerate}
  \item First step
  \item Second step
\end{enumerate}

% Unordered list
\begin{itemize}
  \item Point one
  \item Point two
\end{itemize}

% Description list
\begin{description}
  \item[MCMC] Markov Chain Monte Carlo
  \item[MLE] Maximum Likelihood Estimation
\end{description}
```

### Tables

**Make tables accessible:**

```latex
\begin{table}
\caption{Model Comparison Results}
\begin{tabular}{lrrr}
\toprule
\textbf{Model} & \textbf{Accuracy} & \textbf{Precision} & \textbf{Recall} \\
\midrule
Logistic Regression & 0.85 & 0.83 & 0.87 \\
Random Forest & 0.92 & 0.91 & 0.93 \\
Neural Network & 0.94 & 0.93 & 0.95 \\
\bottomrule
\end{tabular}
\end{table}
```

**Guidelines:**
- Use `\caption` for table title
- Use header row with `\textbf`
- Keep tables simple (avoid merging cells)
- Use `booktabs` for professional appearance
- Provide text summary of key findings

### Mathematical Content

**Make equations accessible:**

```latex
% Provide text explanation
The mean squared error is defined as:
\begin{equation}
\text{MSE} = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2
\label{eq:mse}
\end{equation}
where $y_i$ is the true value and $\hat{y}_i$ is the predicted value.
```

**Best Practices:**
- Explain notation before using
- Provide intuition alongside formulas
- Read aloud well (screen readers struggle with math)
- Use `\text{}` for text within equations
- Define all symbols

## 🎤 Presentation Delivery

### Slides

**Design Guidelines:**
- **One main point per slide**
- **6×6 rule**: Max 6 bullets, 6 words each
- **High contrast**: Dark text on light, or light on dark
- **Large fonts**: Minimum 24pt for slides
- **Sans-serif fonts**: Easier to read on screen

### Speaking

**Best Practices:**
- **Describe visuals**: "This graph shows..."
- **Read equations**: Don't just point
- **Face audience**: Don't talk to screen
- **Clear speech**: Not too fast
- **Provide context**: Don't assume prior knowledge

### Recordings

**For video content:**
- **Captions/subtitles**: Auto-generate then edit
- **Transcripts**: Full text version
- **Clear audio**: Minimize background noise
- **Visual descriptions**: Describe actions on screen

## 🔧 LaTeX Accessibility Packages

### Recommended Packages

```latex
\usepackage{hyperref}  % PDF bookmarks and links
\usepackage{axessibility}  % Accessibility support
\usepackage{tagpdf}  % Tagged PDF (PDF/UA)

% Hyperref configuration
\hypersetup{
    pdftitle={Presentation Title},
    pdfauthor={Your Name},
    pdfsubject={Topic},
    pdfkeywords={keyword1, keyword2},
    pdflang={en-US},
    pdfstartview=Fit,
    colorlinks=true,
    linkcolor=blue,
    citecolor=blue,
    urlcolor=blue
}

% Tooltips for figures
\usepackage{pdfcomment}
```

## 🌐 Alternative Formats

**Provide multiple formats:**

1. **PDF** - Standard distribution
2. **HTML** - Screen reader friendly
3. **Text** - Transcripts of slides
4. **Large print** - For visually impaired
5. **Audio** - Lecture recordings

**Tools for Conversion:**
- `pdf2htmlEX` - PDF to HTML
- `pandoc` - Universal document converter
- `make4ht` - LaTeX to HTML
- `tex2html` - Alternative converter

## ♿ Testing Accessibility

### PDF Testing

**Tools:**
- **Adobe Acrobat Pro**: Accessibility Checker
- **PAC (PDF Accessibility Checker)**: Free tool
- **NVDA/JAWS**: Screen reader testing

**Checklist:**
- [ ] PDF is tagged (has structure)
- [ ] Reading order is correct
- [ ] Alt text for all images
- [ ] Color contrast sufficient
- [ ] Text is selectable (not image)
- [ ] Bookmarks present
- [ ] Language specified

### Manual Testing

**Try these:**
1. **Zoom to 200%**: Is everything still readable?
2. **Print grayscale**: Can you distinguish colors?
3. **Navigate with keyboard**: Tab through links
4. **Screen reader**: Listen to content
5. **Color blindness simulator**: Check visibility

## 📋 Accessibility Checklist

Before publishing materials:

### Visual
- [ ] Contrast ratio ≥ 4.5:1 for text
- [ ] Color not sole means of conveying info
- [ ] Font size ≥ 11pt (12pt preferred)
- [ ] Clear visual hierarchy

### Structure
- [ ] Proper heading hierarchy
- [ ] Semantic lists used
- [ ] Tables have headers
- [ ] Logical reading order

### Content
- [ ] Alt text for all images
- [ ] Math equations explained
- [ ] Acronyms defined at first use
- [ ] Clear, simple language

### Technical
- [ ] PDF is tagged
- [ ] Hyperlinks descriptive
- [ ] Metadata complete
- [ ] Language specified

### Formats
- [ ] Multiple formats available
- [ ] Captions for videos
- [ ] Transcripts provided
- [ ] High contrast version

## 🎨 High Contrast Theme

We provide a **high contrast Beamer theme** for improved visibility.

**Using the theme:**
```latex
\documentclass{beamer}
\usetheme{ESMADHighContrast}  % Use high contrast theme

% Or manually:
\setbeamercolor{normal text}{fg=black,bg=white}
\setbeamercolor{structure}{fg=black}
\setbeamercolor{alerted text}{fg=red!80!black}
```

See `theme/esmad_beamer_theme_highcontrast.sty` for details.

## 📚 Resources

### Guidelines
- [WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM](https://webaim.org/)
- [A11Y Project](https://www.a11yproject.com/)

### Tools
- [WAVE Browser Extension](https://wave.webaim.org/extension/)
- [axe DevTools](https://www.deque.com/axe/devtools/)
- [Color Oracle](https://colororacle.org/)
- [PAC PDF Checker](https://www.access-for-all.ch/en/pdf-lab/pdf-accessibility-checker-pac.html)

### LaTeX Resources
- [LaTeX Accessibility Guide](https://www.latex-project.org/help/documentation/usrguide3.pdf)
- [axessibility Package](https://ctan.org/pkg/axessibility)

## 📧 Questions?

For accessibility concerns:
- **Email**: dfr@esmad.ipp.pt
- **Issues**: [GitHub Issues](https://github.com/diogoribeiro7/academic-presentations/issues)
- **Tag**: Use `accessibility` label

## 🙏 Acknowledgments

Thank you to all students and educators who have provided feedback on accessibility. Your input helps us improve these materials for everyone.

---

*Last Updated: January 2025*
*Part of the Academic Presentations repository*
*Committed to inclusive education*
