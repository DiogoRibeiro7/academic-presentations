# Academic Presentations

**Comprehensive Data Science & Machine Learning Course Materials**

**Diogo Ribeiro** — _ESMAD, Escola Superior de Média Arte e Design_ · _Lead Data Scientist, Mysense.ai_

[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--2022--7072-green.svg)](https://orcid.org/0009-0001-2022-7072)
[![Email](https://img.shields.io/badge/Email-dfr%40esmad.ipp.pt-blue.svg)](mailto:dfr@esmad.ipp.pt)
[![Institution](https://img.shields.io/badge/Institution-ESMAD-orange.svg)](https://www.esmad.ipp.pt/)
[![Company](https://img.shields.io/badge/Company-Mysense.ai-purple.svg)](https://mysense.ai/)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-sa/4.0/)
[![Code License: MIT](https://img.shields.io/badge/Code%20License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A collection of professional academic presentations covering advanced topics in statistics, machine
learning, deep learning, and data science — built for graduate courses, research seminars,
professional training, and self-study.

**[📊 Browse slide previews](https://diogoribeiro7.github.io/academic-presentations/)** ·
[Course catalog](#-course-catalog) ·
[Getting started](#-getting-started) ·
[Contributing](./CONTRIBUTING.md) ·
[Changelog](./CHANGELOG.md)

> **Sections below are collapsible.** Click any ▸ heading to expand just the part you need.

---

## 🧭 Contents

| Section | What's inside |
| --- | --- |
| [📚 Course catalog](#-course-catalog) | All modules, learning objectives, topics, prerequisites |
| [📁 Repository structure](#-repository-structure) | Directory layout and conventions |
| [🚀 Getting started](#-getting-started) | Install LaTeX/Python/R, compile slides, run exercises |
| [🎨 Theme & styling](#-theme--styling) | ESMAD Beamer theme and usage template |
| [🎯 Pick your path](#-pick-your-path) | Guides for students, educators, and researchers |
| [🤖 Automation & contributing](#-automation--contributing) | CI/CD workflows and how to contribute |
| [📄 License, citation & contact](#-license-citation--contact) | Licensing, BibTeX, and how to reach out |

### At a glance

| | |
| --- | --- |
| 📚 Presentations | 15+ comprehensive decks, 100+ hours of content |
| 💻 Code | 27,000+ lines of production-ready Python & R |
| 📖 References | 140+ curated papers with DOIs |
| 🎨 Theme | One professional LaTeX theme, fully documented |
| 📝 Assessments | Exercises, quizzes, exams, and grading rubrics |
| 🤖 Build | Automated PDF compilation via GitHub Actions |

---

## 📚 Course catalog

Every module lives in its own directory with a `presentation/`, and most also ship `code/` and
`exercises/`. Expand a domain below for learning objectives and topic lists.

| Module | Domain | Level | Duration |
| --- | --- | --- | --- |
| [R Programming](./00-programming-fundamentals/r-programming/) | Programming | Beginner | 2–3 weeks |
| [Statistical Learning Theory](./01-foundations/statistical-modeling/) | ML theory | Intermediate | 4–5 weeks |
| [Feature Engineering](./01-foundations/feature-engineering/) | ML practice | Beginner–Intermediate | 2–3 weeks |
| [Principal Component Analysis](./01-foundations/pca/) | Foundations | Intermediate | 1–2 weeks |
| [Optimization for Data Science](./01-foundations/optimization/) | Optimization | Intermediate–Advanced | 3–4 weeks |
| [Deep Learning Fundamentals](./02-deep-learning/deep-learning-fundamentals/) | Deep learning | Intermediate–Advanced | 3–4 weeks |
| [Reinforcement Learning](./02-deep-learning/reinforcement-learning/) | Deep learning | Advanced | 4–5 weeks |
| [Advanced MCMC Methods](./03-bayesian-methods/mcmc/) | Bayesian | Advanced | 3–4 weeks |
| [Bayesian Machine Learning](./03-bayesian-methods/bayesian-machine-learning/) | Bayesian | Advanced | 3–4 weeks |
| [Causal Inference](./04-causal-inference/causal-inference-fundamentals/) | Causal | Advanced | 4–5 weeks |
| [A/B Testing & Experimentation](./04-causal-inference/ab-testing/) | Applied | Intermediate | 1–2 weeks |
| [Time Series Analysis](./05-time-series/time-series-forecasting/) | Forecasting | Intermediate–Advanced | 3–4 weeks |
| [Explainable AI & Interpretability](./06-advanced-topics/explainable-ai/) | Advanced topics | Intermediate–Advanced | 2–3 weeks |
| [Building AI Agents](./06-advanced-topics/ai-agents/) | Advanced topics | Advanced | 90-minute deck |
| [OOP & Streaming Pipelines](./06-advanced-topics/computer-science/) | Computer science | Intermediate | 2 weeks |
| [Capstone Projects](./07-capstone-projects/) | Projects | Advanced | Course-length |
| [Data Science Applications](./08-data-science-applications-course/) | Applied course | Intermediate | Full course |
| [Testing Suites Guide](./09-unit-tests/) | Engineering | Intermediate | 1 week |

<details>
<summary><b>🔷 Deep Learning &amp; Neural Networks</b> — deep learning fundamentals, reinforcement learning</summary>

### Deep Learning Fundamentals

📂 [`02-deep-learning/deep-learning-fundamentals/`](./02-deep-learning/deep-learning-fundamentals/)

**Learning Objectives:**
- Understand the mathematical foundations of neural networks
- Implement backpropagation and gradient descent from scratch
- Master modern optimization techniques (SGD, Adam, AdamW)
- Design and train CNN architectures for computer vision
- Build RNN/LSTM models for sequential data
- Understand Transformer architecture and attention mechanisms
- Apply regularization techniques (dropout, batch normalization)

**Topics Covered:**
- Perceptron and multilayer networks
- Activation functions (ReLU, sigmoid, tanh, Swish)
- Loss functions and optimization
- Convolutional Neural Networks (LeNet, AlexNet, VGG, ResNet)
- Recurrent Neural Networks and LSTM
- Transformers and self-attention
- Training best practices

**Prerequisites:** Linear algebra, calculus, Python programming<br>
**Level:** Intermediate to Advanced<br>
**Duration:** 3-4 weeks (graduate course)

---

### Reinforcement Learning

📂 [`02-deep-learning/reinforcement-learning/`](./02-deep-learning/reinforcement-learning/)

**Learning Objectives:**
- Formulate problems as Markov Decision Processes
- Derive and apply Bellman equations
- Implement value iteration and policy iteration
- Understand Monte Carlo and TD learning methods
- Build Q-learning and SARSA agents
- Apply function approximation with neural networks
- Implement modern deep RL algorithms (DQN, PPO, A3C)
- Design multi-agent systems

**Topics Covered:**
- Markov Decision Processes and dynamic programming
- Monte Carlo methods
- Temporal Difference learning (SARSA, Q-learning)
- Function approximation and deep Q-networks
- Policy gradient methods (REINFORCE, Actor-Critic, PPO)
- Multi-agent reinforcement learning
- Applications (games, robotics, resource allocation)

**Prerequisites:** Probability, linear algebra, Python<br>
**Level:** Advanced<br>
**Duration:** 4-5 weeks (graduate course)

</details>

<details>
<summary><b>🔷 Machine Learning Theory &amp; Practice</b> — statistical learning, feature engineering, explainable AI</summary>

### Statistical Learning Theory

📂 [`01-foundations/statistical-modeling/`](./01-foundations/statistical-modeling/)

**Learning Objectives:**
- Understand bias-variance tradeoff
- Master regularization techniques (Ridge, Lasso, Elastic Net)
- Apply cross-validation and model selection
- Implement ensemble methods (bagging, boosting, stacking)
- Understand kernel methods and SVMs
- Perform dimensionality reduction (PCA, t-SNE, UMAP)
- Evaluate models using appropriate metrics

**Topics Covered:**
- Supervised learning fundamentals
- Linear and logistic regression
- Regularization and model selection
- Tree-based methods (CART, Random Forests, XGBoost)
- Support Vector Machines
- Gaussian Processes
- Model evaluation and validation

**Prerequisites:** Statistics, linear algebra, programming<br>
**Level:** Intermediate<br>
**Duration:** 4-5 weeks

---

### Feature Engineering

📂 [`01-foundations/feature-engineering/`](./01-foundations/feature-engineering/)

**Learning Objectives:**
- Design effective feature engineering pipelines
- Handle missing data with advanced imputation techniques
- Encode categorical variables appropriately
- Create polynomial and interaction features
- Apply feature scaling and normalization
- Perform feature selection using multiple methods
- Build end-to-end ML pipelines with scikit-learn

**Topics Covered:**
- Missing value imputation (mean, median, KNN, MICE)
- Categorical encoding (one-hot, ordinal, target, entity embeddings)
- Feature scaling (standard, min-max, robust)
- Polynomial features and interactions
- Feature selection (filter, wrapper, embedded methods)
- Dimensionality reduction
- Pipeline construction

**Prerequisites:** Basic Python, pandas, scikit-learn<br>
**Level:** Beginner to Intermediate<br>
**Duration:** 2-3 weeks

---

### Explainable AI & Model Interpretability

📂 [`06-advanced-topics/explainable-ai/`](./06-advanced-topics/explainable-ai/)

**Learning Objectives:**
- Understand the interpretability-accuracy tradeoff
- Explain model predictions using SHAP values
- Apply LIME for local explanations
- Compute and interpret permutation importance
- Visualize partial dependence and ICE plots
- Detect and mitigate algorithmic bias
- Implement fairness metrics and constraints
- Use modern XAI tools (SHAP, LIME, InterpretML)

**Topics Covered:**
- Global vs local explanations
- Model-agnostic methods (SHAP, LIME, permutation importance)
- Model-specific interpretability (linear models, trees, neural networks)
- Attention mechanisms and gradient-based explanations
- Algorithmic fairness and bias detection
- Fairness definitions and impossibility results
- Practical implementation with Python tools

**Prerequisites:** Machine learning basics, Python<br>
**Level:** Intermediate to Advanced<br>
**Duration:** 2-3 weeks

</details>

<details>
<summary><b>🔷 Bayesian Methods &amp; MCMC</b> — advanced MCMC, Bayesian machine learning</summary>

### Advanced MCMC Methods

📂 [`03-bayesian-methods/mcmc/`](./03-bayesian-methods/mcmc/)

**Learning Objectives:**
- Understand Bayesian inference and posterior distributions
- Derive Metropolis-Hastings acceptance probability
- Implement MCMC algorithms from scratch
- Apply Hamiltonian Monte Carlo for efficient sampling
- Use No-U-Turn Sampler (NUTS) for automatic tuning
- Diagnose convergence using R-hat and ESS
- Apply MCMC to real Bayesian models

**Topics Covered:**
- Bayesian inference fundamentals
- Metropolis-Hastings algorithm
- Hamiltonian Monte Carlo and leapfrog integration
- No-U-Turn Sampler (NUTS)
- Convergence diagnostics (trace plots, R-hat, ESS)
- Applications (Bayesian regression, hierarchical models)

**Prerequisites:** Probability theory, calculus, Python<br>
**Level:** Advanced<br>
**Duration:** 3-4 weeks<br>
**Code:** Complete Python implementations (8,000+ lines)

---

### Bayesian Machine Learning

📂 [`03-bayesian-methods/bayesian-machine-learning/`](./03-bayesian-methods/bayesian-machine-learning/)

**Learning Objectives:**
- Apply Bayesian inference to machine learning problems
- Build Bayesian linear and logistic regression models
- Implement Gaussian Processes for regression
- Understand Bayesian neural networks
- Perform approximate inference (VI, EP)
- Apply Bayesian optimization for hyperparameter tuning
- Quantify predictive uncertainty

**Topics Covered:**
- Bayesian linear regression
- Gaussian Processes
- Bayesian neural networks
- Variational inference
- Bayesian optimization
- Uncertainty quantification

**Prerequisites:** Bayesian statistics, machine learning, Python<br>
**Level:** Advanced<br>
**Duration:** 3-4 weeks

</details>

<details>
<summary><b>🔷 Causal Inference &amp; Experimentation</b> — causal inference, A/B testing</summary>

### Causal Inference

📂 [`04-causal-inference/causal-inference-fundamentals/`](./04-causal-inference/causal-inference-fundamentals/)

**Learning Objectives:**
- Understand potential outcomes framework
- Draw and interpret causal DAGs
- Implement Instrumental Variables (IV/2SLS)
- Apply Regression Discontinuity Design
- Use Difference-in-Differences methods
- Estimate propensity scores and perform matching
- Apply synthetic control methods
- Identify and address confounding

**Topics Covered:**
- Potential outcomes and causal graphs
- Instrumental Variables and weak instruments
- Regression Discontinuity (sharp and fuzzy)
- Difference-in-Differences and event studies
- Propensity score methods
- Synthetic controls
- Modern methods (Callaway-Sant'Anna, Sun-Abraham)

**Prerequisites:** Statistics, econometrics, R or Python<br>
**Level:** Advanced<br>
**Duration:** 4-5 weeks<br>
**Code:** Python & R implementations (11,000+ lines)

---

### A/B Testing & Experimentation

📂 [`04-causal-inference/ab-testing/`](./04-causal-inference/ab-testing/)

**Learning Objectives:**
- Design statistically rigorous A/B tests
- Calculate required sample sizes
- Perform hypothesis testing correctly
- Control for multiple comparisons
- Understand statistical power and effect sizes
- Apply sequential testing methods
- Analyze experimental results
- Avoid common pitfalls (peeking, p-hacking)

**Topics Covered:**
- Experimental design
- Hypothesis testing and p-values
- Sample size calculations
- Multiple testing corrections
- Bayesian A/B testing
- Sequential analysis
- Common pitfalls and best practices

**Prerequisites:** Statistics, probability<br>
**Level:** Intermediate<br>
**Duration:** 1-2 weeks

</details>

<details>
<summary><b>🔷 Time Series &amp; Forecasting</b> — classical and deep forecasting methods</summary>

### Time Series Analysis

📂 [`05-time-series/time-series-forecasting/`](./05-time-series/time-series-forecasting/)

**Learning Objectives:**
- Analyze time series components (trend, seasonality)
- Test for and achieve stationarity
- Build ARIMA and SARIMA models
- Implement VAR models for multivariate series
- Apply state space models and Kalman filter
- Use LSTM and Transformers for forecasting
- Evaluate forecasting accuracy
- Apply hybrid methods (Prophet, N-BEATS)

**Topics Covered:**
- Stationarity and unit root tests
- ARMA, ARIMA, SARIMA models
- Vector Autoregression (VAR)
- State space models and Kalman filter
- Forecasting and evaluation
- Deep learning for time series (LSTM, GRU)
- Transformer models (TFT, Autoformer, Informer)
- Hybrid approaches (ES-RNN, N-BEATS, Prophet)

**Prerequisites:** Statistics, linear algebra, Python<br>
**Level:** Intermediate to Advanced<br>
**Duration:** 3-4 weeks

</details>

<details>
<summary><b>🔷 Optimization &amp; Computational Methods</b> — convex optimization through evolutionary search</summary>

### Optimization for Data Science

📂 [`01-foundations/optimization/`](./01-foundations/optimization/)

**Learning Objectives:**
- Formulate optimization problems
- Understand convexity and its implications
- Derive and apply KKT conditions
- Implement gradient descent variants
- Apply momentum and adaptive methods (Adam, AdamW)
- Solve constrained optimization problems
- Use evolutionary algorithms for black-box optimization
- Apply Bayesian optimization for hyperparameter tuning
- Optimize neural network training

**Topics Covered:**
- Convex optimization fundamentals
- Gradient descent (batch, SGD, mini-batch)
- Momentum methods and Nesterov acceleration
- Adaptive learning rates (AdaGrad, RMSProp, Adam)
- Constrained optimization (Lagrangian, KKT, penalties)
- Evolutionary algorithms (GA, ES, PSO, CMA-ES)
- Bayesian optimization
- Multi-objective optimization

**Prerequisites:** Calculus, linear algebra, Python<br>
**Level:** Intermediate to Advanced<br>
**Duration:** 3-4 weeks

</details>

<details>
<summary><b>🔷 Programming, Engineering &amp; Applied Modules</b> — R, PCA, OOP &amp; streaming, AI agents, capstones</summary>

| Module | Directory | Focus |
| --- | --- | --- |
| **R Programming** | [`00-programming-fundamentals/r-programming/`](./00-programming-fundamentals/r-programming/) | R from basics to data science workflows |
| **Principal Component Analysis** | [`01-foundations/pca/`](./01-foundations/pca/) | PCA theory, geometry, and applied dimensionality reduction |
| **OOP & Streaming Pipelines** | [`06-advanced-topics/computer-science/`](./06-advanced-topics/computer-science/) | Object-oriented design principles and streaming pipeline processing |
| **Building AI Agents** | [`06-advanced-topics/ai-agents/`](./06-advanced-topics/ai-agents/) | Agent architecture, reliability, and production operations (90-minute deck) |
| **Capstone Projects** | [`07-capstone-projects/`](./07-capstone-projects/) | Project guides, prerequisites appendix, and industry-focused briefs |
| **Data Science Applications** | [`08-data-science-applications-course/`](./08-data-science-applications-course/) | Full applied course: "Data Science in Practice — Industry Applications" |
| **Testing Suites Guide** | [`09-unit-tests/`](./09-unit-tests/) | Writing and structuring test suites for data science code |
| **MLOps & Deployment** | [`06-advanced-topics/mlops-deployment/`](./06-advanced-topics/mlops-deployment/) | Planned module — directory scaffolded, slides in progress |

</details>

---

## 📁 Repository structure

<details>
<summary><b>Full directory tree</b></summary>

```
academic-presentations/
├── README.md                            # This file
├── CONTRIBUTING.md                      # Contribution guidelines
├── CHANGELOG.md                         # Version history
├── ACCESSIBILITY.md                     # Accessibility guidance
├── QUALITY.md                           # Quality standards
├── compile_all.sh                       # Build every presentation
│
├── .github/                             # 🤖 GitHub Actions automation
│   ├── workflows/
│   │   ├── compile-latex.yml            # Auto-compile PDFs
│   │   ├── check-links.yml              # Verify all URLs
│   │   └── generate-previews.yml        # Create PDF previews
│   ├── dependabot.yml                   # Dependency updates
│   └── markdown-link-check-config.json
│
├── shared/                              # 🔄 Shared resources
│   ├── theme/                           # 🎨 Professional LaTeX theme
│   │   ├── esmad_beamer_theme.sty       # Custom Beamer theme
│   │   ├── esmad_beamer_theme_highcontrast.sty
│   │   ├── STYLE_GUIDE.md               # Theme documentation
│   │   └── template_presentation.tex    # Example template
│   ├── bibliographies/                  # 📚 Reference libraries (140+ papers)
│   │   ├── mcmc_references.bib
│   │   ├── causal_inference_references.bib
│   │   ├── statistical_learning_references.bib
│   │   ├── capstone_projects_references.bib
│   │   ├── industry_focus_references.bib
│   │   └── *_enhancements_references.bib
│   └── utilities/                       # Shared LaTeX/helper utilities
│
├── 00-programming-fundamentals/         # 💻 Programming basics
│   └── r-programming/                   # R: A Comprehensive Introduction
│
├── 01-foundations/                      # 📊 Core foundations
│   ├── statistical-modeling/            # Statistical Learning Theory
│   ├── feature-engineering/             # Feature Engineering
│   ├── pca/                             # Principal Component Analysis
│   └── optimization/                    # Optimization for Data Science
│
├── 02-deep-learning/                    # 🧠 Deep learning
│   ├── deep-learning-fundamentals/
│   └── reinforcement-learning/
│
├── 03-bayesian-methods/                 # 🎲 Bayesian statistics
│   ├── mcmc/                            # MCMC methods
│   └── bayesian-machine-learning/       # Bayesian ML
│
├── 04-causal-inference/                 # ⚖️ Causal methods
│   ├── causal-inference-fundamentals/
│   └── ab-testing/                      # A/B Testing & Experimentation
│
├── 05-time-series/                      # ⏱️ Time series
│   └── time-series-forecasting/
│
├── 06-advanced-topics/                  # 🔬 Advanced topics
│   ├── explainable-ai/                  # Explainable AI
│   ├── ai-agents/                       # Building AI Agents
│   ├── computer-science/                # OOP & streaming pipelines
│   └── mlops-deployment/                # Planned module
│
├── 07-capstone-projects/                # 🎓 Projects
│   ├── industry-focus/                  # Industry applications
│   ├── project-guides/                  # Project guidelines
│   └── prerequisites/                   # Prerequisites appendix
│
├── 08-data-science-applications-course/ # 🎯 Applied course
│   ├── presentation/                    # Full course materials
│   ├── exercises/
│   └── assessments/                     # Course assessments
│
├── 09-unit-tests/                       # 🧪 Testing suites guide
│
├── assessments/                         # 📝 Quizzes, exams, rubrics
├── datasets/                            # 📦 Example datasets
├── docs/                                # 📖 Guides and architecture notes
├── scripts/                             # 🔧 Maintenance scripts
└── tests/                               # ✅ Repository test suite
```

**Per-module convention:** each module directory contains `presentation/` (Beamer slides), and where
applicable `code/` (Python/R implementations) and `exercises/` (problem sets).

</details>

---

## 🚀 Getting started

<details>
<summary><b>1. Prerequisites</b> — LaTeX, Python, R</summary>

**LaTeX distribution:**
```bash
# Ubuntu/Debian
sudo apt-get install texlive-full

# macOS
brew install --cask mactex

# Windows
# Download and install MiKTeX or TeX Live
```

**Python environment (for code examples):**
```bash
pip install -r requirements.txt

# Or install the core set directly:
pip install numpy scipy matplotlib seaborn pandas scikit-learn statsmodels
pip install torch tensorflow  # For deep learning examples
pip install shap lime         # For XAI examples
```

A conda environment is also provided in [`environment.yml`](./environment.yml).

**R environment (for R examples):**
```r
install.packages(c(
  "AER", "rdrobust", "fixest", "did",  # Causal inference
  "caret", "recipes", "mice",           # Feature engineering
  "forecast", "vars", "fable"           # Time series
))
```

Or run the bundled installer: [`install_r_packages.R`](./install_r_packages.R).

</details>

<details>
<summary><b>2. Compiling presentations</b> — manual, latexmk, or CI</summary>

**Manual compilation:**
```bash
cd 02-deep-learning/deep-learning-fundamentals/presentation/
pdflatex deep_learning_beamer.tex
pdflatex deep_learning_beamer.tex  # Run twice for references
```

**Using latexmk (recommended):**
```bash
cd 02-deep-learning/reinforcement-learning/presentation/
latexmk -pdf rl_beamer.tex
```

**Compile everything:**
```bash
./compile_all.sh
```

**Automated compilation:**
- Push to GitHub → GitHub Actions automatically compiles all PDFs
- Download compiled PDFs from Actions artifacts or Releases

**Build artifact policy:**
- LaTeX auxiliary files and presentation PDFs are generated outputs and are ignored by git.
- Exercise and assessment outputs may be tracked when explicitly required for coursework delivery.

</details>

<details>
<summary><b>3. Running code and exercises</b></summary>

**Python:**
```bash
# MCMC examples (if code/ directory exists with implementations)
# Example references are embedded in presentation materials

# Exercises and assessments
cd 03-bayesian-methods/mcmc/exercises/
pdflatex mcmc_exercises.tex
```

**Exercises:**
```bash
# MCMC exercises
cd 03-bayesian-methods/mcmc/exercises/
pdflatex mcmc_exercises.tex

# Causal inference exercises
cd 04-causal-inference/causal-inference-fundamentals/exercises/
pdflatex causal_inference_exercises.tex
```

</details>

---

## 🎨 Theme & styling

All presentations use the **ESMAD Beamer Theme** for a consistent, professional appearance.

<details>
<summary><b>Theme features and usage template</b></summary>

### Features

✅ **Professional color palette** (ESMAD Blue, accents)<br>
✅ **Custom environments** (theorems, definitions, examples, alerts)<br>
✅ **Mathematical notation helpers** (`\Normal`, `\E`, `\Var`, etc.)<br>
✅ **Code listing styles** with syntax highlighting<br>
✅ **Author information** with ORCID integration<br>
✅ **Slide templates** (title, TOC, contact, references)<br>
✅ **High-contrast variant** for accessibility<br>

### Usage

```latex
\documentclass[aspectratio=169]{beamer}
\usepackage{../../../shared/theme/esmad_beamer_theme}

% Author info
\authorname{Your Name}
\authoremail{your.email@university.edu}
\authororcid{0000-0000-0000-0000}

\title{Your Presentation}
\date{\today}

\begin{document}
\begin{frame}
  \titlepage
\end{frame}

% Your content...

\contactslide
\end{document}
```

See [`shared/theme/STYLE_GUIDE.md`](./shared/theme/STYLE_GUIDE.md) for complete documentation, and
[`ACCESSIBILITY.md`](./ACCESSIBILITY.md) for accessibility guidance.

</details>

---

## 🎯 Pick your path

<details>
<summary><b>📖 For students</b> — learning paths and study tips</summary>

### Recommended learning paths

**Path 1: Machine Learning Fundamentals**
1. Statistical Learning (4 weeks)
2. Feature Engineering (2 weeks)
3. Optimization (3 weeks)
4. Explainable AI (2 weeks)

**Path 2: Deep Learning Specialization**
1. Deep Learning Fundamentals (4 weeks)
2. Optimization (focus on neural networks)
3. Reinforcement Learning (4 weeks)
4. Time Series Analysis (focus on deep methods)

**Path 3: Causal & Bayesian Methods**
1. Causal Inference (5 weeks)
2. Bayesian ML (4 weeks)
3. MCMC Methods (3 weeks)
4. A/B Testing (2 weeks)

Competency matrices and additional paths live in [`docs/learning-paths/`](./docs/learning-paths/).

### Study tips

- 📚 **Start with slides** to understand concepts
- 💻 **Run code examples** to see methods in action
- 📝 **Complete exercises** to test understanding
- 📖 **Read references** for deeper knowledge
- 🤝 **Join discussions** (create GitHub issues)

</details>

<details>
<summary><b>👨‍🏫 For educators</b> — course integration, customization, assessments</summary>

### Course integration

These materials can be integrated into:
- Graduate courses in Data Science/Statistics/CS
- Professional training programs
- Workshop series
- Seminar courses

### Customization

1. **Fork** this repository
2. **Customize** presentations for your needs
3. **Add** your own examples and exercises
4. **Maintain** attribution (CC BY-SA 4.0)

### Assessment resources

Use the materials in [`assessments/`](./assessments/):
- Quizzes for each topic
- Midterm and final exams
- Grading rubrics
- Project ideas

Teaching and enhancement guides are in [`docs/teaching-guides/`](./docs/teaching-guides/) and
[`docs/enhancement-guides/`](./docs/enhancement-guides/).

</details>

<details>
<summary><b>🔬 For researchers</b> — citation and bibliographies</summary>

### Citation

If you use these materials in your research or teaching, please cite:

```bibtex
@misc{ribeiro2025academic,
  author = {Ribeiro, Diogo},
  title = {Academic Presentations: Comprehensive Data Science Course Materials},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/diogoribeiro7/academic-presentations},
  note = {ESMAD \& Mysense.ai}
}
```

### Using the bibliographies

All presentations reference comprehensive BibTeX files:

```latex
\usepackage[backend=bibtex]{biblatex}
\addbibresource{../../../shared/bibliographies/mcmc_references.bib}

% In document
\cite{metropolis1953}
\cite{hoffman2014}

% At end
\printbibliography
```

**Available:**
- `shared/bibliographies/mcmc_references.bib`: 30+ MCMC papers
- `shared/bibliographies/causal_inference_references.bib`: 50+ causal inference papers
- `shared/bibliographies/statistical_learning_references.bib`: 60+ ML/stats papers
- Plus capstone, industry-focus, and per-topic enhancement bibliographies

All include DOIs for easy access.

</details>

---

## 🤖 Automation & contributing

<details>
<summary><b>CI/CD workflows</b></summary>

- **`compile-latex.yml`**: Auto-compiles all LaTeX on push
- **`check-links.yml`**: Verifies all URLs and DOIs weekly
- **`generate-previews.yml`**: Creates PDF preview gallery
- **`dependabot.yml`**: Keeps dependencies updated

Pre-commit hooks (formatting, spell check, LaTeX lint) are configured in
[`.pre-commit-config.yaml`](./.pre-commit-config.yaml).

**PDF preview gallery:** https://diogoribeiro7.github.io/academic-presentations/

</details>

<details>
<summary><b>How to contribute</b></summary>

Contributions are welcome — see [`CONTRIBUTING.md`](./CONTRIBUTING.md) for full guidelines.

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** compilation and code
5. **Submit** a pull request

**Contribution types:**

- 🐛 Fix errors in presentations
- 📚 Add new presentations
- 💡 Improve existing content
- 📖 Enhance documentation
- 🧪 Add code examples
- 📝 Create exercises
- 🎨 Improve theme/styling

Quality standards are documented in [`QUALITY.md`](./QUALITY.md).

</details>

---

## 📄 License, citation & contact

<details>
<summary><b>License</b> — CC BY-SA 4.0 for content, MIT for code</summary>

### Content (presentations & exercises)

Licensed under [Creative Commons Attribution-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-sa/4.0/)

**You are free to:**
- ✅ Share — copy and redistribute
- ✅ Adapt — remix, transform, and build upon

**Under the terms:**
- 📝 Attribution required
- 🔄 ShareAlike for derivatives

### Code

Code examples licensed under [MIT License](https://opensource.org/licenses/MIT)

</details>

<details>
<summary><b>Contact &amp; collaboration</b></summary>

### Professional inquiries

- **Email**: dfr@esmad.ipp.pt
- **Institution**: ESMAD - Escola Superior de Média Arte e Design
- **Company**: Mysense.ai (Lead Data Scientist)
- **ORCID**: [0009-0001-2022-7072](https://orcid.org/0009-0001-2022-7072)

### Research interests

- Markov Chain Monte Carlo and Bayesian computation
- Machine learning and deep learning
- Causal inference and econometrics
- Financial risk modeling
- Time series analysis and forecasting

### Collaboration opportunities

- 🎓 Guest lectures and workshops
- 🏢 Corporate training programs
- 🔬 Research collaborations
- 📝 Joint publications
- 🌐 Conference presentations

</details>

<details>
<summary><b>Acknowledgments</b></summary>

- **ESMAD** for institutional support
- **Mysense.ai** for industry applications and insights
- **Students and colleagues** for valuable feedback
- **Open source community** for tools and inspiration
- **Academic community** for rigorous peer review

</details>

---

**Repository maintainer**: Diogo Ribeiro ·
**Status**: ✅ Actively maintained ·
**History**: [CHANGELOG.md](./CHANGELOG.md) ·
[View releases](https://github.com/diogoribeiro7/academic-presentations/releases)

![GitHub stars](https://img.shields.io/github/stars/diogoribeiro7/academic-presentations?style=social)
![GitHub forks](https://img.shields.io/github/forks/diogoribeiro7/academic-presentations?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/diogoribeiro7/academic-presentations?style=social)
