# Academic Presentations
**Comprehensive Data Science & Machine Learning Course Materials**

**Diogo Ribeiro**<br>
_ESMAD - Escola Superior de Média Arte e Design_<br>
_Lead Data Scientist, Mysense.ai_

[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--2022--7072-green.svg)](https://orcid.org/0009-0001-2022-7072)
[![Email](https://img.shields.io/badge/Email-dfr%40esmad.ipp.pt-blue.svg)](mailto:dfr@esmad.ipp.pt)
[![Institution](https://img.shields.io/badge/Institution-ESMAD-orange.svg)](https://www.esmad.ipp.pt/)
[![Company](https://img.shields.io/badge/Company-Mysense.ai-purple.svg)](https://mysense.ai/)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-sa/4.0/)
[![Code License: MIT](https://img.shields.io/badge/Code%20License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Overview

This repository contains a comprehensive collection of **professional academic presentations** covering advanced topics in statistics, machine learning, deep learning, and data science. The materials are designed for:

- 🎓 **Graduate-level courses** in Data Science, Statistics, and Computer Science
- 🔬 **Research seminars** and academic conferences
- 🏢 **Professional training** programs in industry
- 📚 **Self-study** for advanced learners

### Key Features

✅ **15+ comprehensive presentations** with 100+ hours of content<br>
✅ **Production-ready code** in Python and R (27,000+ lines)<br>
✅ **140+ curated references** with DOIs<br>
✅ **Professional LaTeX theme** with consistent styling<br>
✅ **Hands-on exercises** and assessments<br>
✅ **Automated PDF generation** via GitHub Actions<br>

## 📚 Course Catalog & Learning Objectives

### 🔷 Deep Learning & Neural Networks

#### **Deep Learning Fundamentals**
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

#### **Reinforcement Learning**
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

---

### 🔷 Machine Learning Theory & Practice

#### **Statistical Learning Theory**
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

#### **Feature Engineering**
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

#### **Explainable AI & Model Interpretability**
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

---

### 🔷 Bayesian Methods & MCMC

#### **Advanced MCMC Methods**
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

#### **Bayesian Machine Learning**
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

---

### 🔷 Causal Inference & Econometrics

#### **Causal Inference**
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

### 🔷 Time Series & Forecasting

#### **Time Series Analysis**
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

---

### 🔷 Optimization & Computational Methods

#### **Optimization for Data Science**
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

---

### 🔷 Applied Data Science

#### **A/B Testing & Experimentation**
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

---

## 🏗️ Repository Structure

```
academic-presentations/
├── README.md                           # This file
├── CONTRIBUTING.md                     # Contribution guidelines
├── CHANGELOG.md                        # Version history
├── LICENSE                            # CC BY-SA 4.0 for content
│
├── .github/                           # 🤖 GitHub Actions automation
│   ├── workflows/
│   │   ├── compile-latex.yml         # Auto-compile PDFs
│   │   ├── check-links.yml           # Verify all URLs
│   │   └── generate-previews.yml     # Create PDF previews
│   ├── dependabot.yml                # Dependency updates
│   └── markdown-link-check-config.json
│
├── shared/                            # 🔄 Shared resources
│   ├── theme/                        # 🎨 Professional LaTeX theme
│   │   ├── esmad_beamer_theme.sty   # Custom Beamer theme
│   │   ├── esmad_beamer_theme_highcontrast.sty
│   │   ├── STYLE_GUIDE.md           # Theme documentation
│   │   └── template_presentation.tex # Example template
│   └── bibliographies/               # 📚 Reference libraries (140+ papers)
│       ├── mcmc_references.bib      # MCMC methods (30+ refs)
│       ├── causal_inference_references.bib # Causal inference (50+ refs)
│       └── statistical_learning_references.bib # ML/Stats (60+ refs)
│
├── 00-programming-fundamentals/      # 💻 Programming Basics
│   └── r-programming/
│       └── presentation/
│           └── R_programming.tex
│
├── 01-foundations/                   # 📊 Core Foundations
│   ├── statistical-modeling/
│   │   └── presentation/            # Statistical Learning Theory
│   ├── feature-engineering/
│   │   └── presentation/            # Feature Engineering
│   ├── pca/
│   │   └── presentation/            # Principal Component Analysis
│   └── optimization/
│       └── presentation/            # Optimization for Data Science
│
├── 02-deep-learning/                 # 🧠 Deep Learning
│   ├── deep-learning-fundamentals/
│   │   └── presentation/            # Deep Learning Fundamentals
│   └── reinforcement-learning/
│       └── presentation/            # Reinforcement Learning
│
├── 03-bayesian-methods/              # 🎲 Bayesian Statistics
│   ├── mcmc/
│   │   ├── presentation/            # MCMC Methods
│   │   └── exercises/               # MCMC Exercises
│   └── bayesian-machine-learning/
│       └── presentation/            # Bayesian ML
│
├── 04-causal-inference/              # ⚖️ Causal Methods
│   ├── causal-inference-fundamentals/
│   │   ├── presentation/            # Causal Inference Fundamentals
│   │   └── exercises/               # Causal Inference Exercises
│   └── ab-testing/
│       └── presentation/            # A/B Testing & Experimentation
│
├── 05-time-series/                   # ⏱️ Time Series
│   └── time-series-forecasting/
│       └── presentation/            # Time Series Analysis
│
├── 06-advanced-topics/               # 🔬 Advanced Topics
│   ├── explainable-ai/
│   │   └── presentation/            # Explainable AI
│   └── computer-science/
│       └── presentation/            # OOP & Streaming Pipelines
│
├── 07-capstone-projects/             # 🎓 Projects
│   ├── industry-focus/              # Industry applications
│   ├── project-guides/              # Project guidelines
│   └── prerequisites/               # Prerequisites
│
└── 08-data-science-applications-course/  # 🎯 Applied Course
    ├── presentation/                # Full course materials
    └── assessments/                 # Course assessments
```

## 🎨 Professional Theme & Styling

All presentations use the **ESMAD Beamer Theme** for consistent, professional appearance:

### Theme Features

✅ **Professional color palette** (ESMAD Blue, accents)<br>
✅ **Custom environments** (theorems, definitions, examples, alerts)<br>
✅ **Mathematical notation helpers** (`\Normal`, `\E`, `\Var`, etc.)<br>
✅ **Code listing styles** with syntax highlighting<br>
✅ **Author information** with ORCID integration<br>
✅ **Slide templates** (title, TOC, contact, references)<br>

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

See [`shared/theme/STYLE_GUIDE.md`](./shared/theme/STYLE_GUIDE.md) for complete documentation.

## 🔧 Getting Started

### Prerequisites

**LaTeX Distribution:**
```bash
# Ubuntu/Debian
sudo apt-get install texlive-full

# macOS
brew install --cask mactex

# Windows
# Download and install MiKTeX or TeX Live
```

**Python Environment (for code examples):**
```bash
pip install numpy scipy matplotlib seaborn pandas scikit-learn statsmodels
pip install torch tensorflow  # For deep learning examples
pip install shap lime  # For XAI examples
```

**R Environment (for R examples):**
```r
install.packages(c(
  "AER", "rdrobust", "fixest", "did",  # Causal inference
  "caret", "recipes", "mice",           # Feature engineering
  "forecast", "vars", "fable"           # Time series
))
```

### Compiling Presentations

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

**Automated compilation:**
- Push to GitHub → GitHub Actions automatically compiles all PDFs
- Download compiled PDFs from Actions artifacts or Releases

### Running Code Examples

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

## 📖 For Students

### Recommended Learning Paths

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

### Study Tips

- 📚 **Start with slides** to understand concepts
- 💻 **Run code examples** to see methods in action
- 📝 **Complete exercises** to test understanding
- 📖 **Read references** for deeper knowledge
- 🤝 **Join discussions** (create GitHub issues)

## 👨‍🏫 For Educators

### Course Integration

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

### Assessment Resources

Use the materials in [`assessments/`](./assessments/):
- Quizzes for each topic
- Midterm and final exams
- Grading rubrics
- Project ideas

## 🔬 For Researchers

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

### Using the Bibliographies

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

All include DOIs for easy access.

## 🤝 Contributing

We welcome contributions! See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for guidelines.

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** compilation and code
5. **Submit** a pull request

### Contribution Types

- 🐛 Fix errors in presentations
- 📚 Add new presentations
- 💡 Improve existing content
- 📖 Enhance documentation
- 🧪 Add code examples
- 📝 Create exercises
- 🎨 Improve theme/styling

## 🤖 Automation & CI/CD

### GitHub Actions Workflows

- **`compile-latex.yml`**: Auto-compiles all LaTeX on push
- **`check-links.yml`**: Verifies all URLs and DOIs weekly
- **`generate-previews.yml`**: Creates PDF preview gallery
- **`dependabot.yml`**: Keeps dependencies updated

### PDF Preview Gallery

View slide previews at: **https://diogoribeiro7.github.io/academic-presentations/**

## 📊 Repository Statistics

- 📚 **15+ comprehensive presentations**
- 💻 **27,000+ lines of code** (Python & R)
- 📖 **140+ curated references** with DOIs
- 📝 **14 pages of exercises** (2 comprehensive problem sets)
- 🎨 **1 professional LaTeX theme** with full documentation
- 🤖 **Fully automated** PDF compilation and testing

## 📄 License

### Content (Presentations & Exercises)

Licensed under [Creative Commons Attribution-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-sa/4.0/)

**You are free to:**
- ✅ Share — copy and redistribute
- ✅ Adapt — remix, transform, and build upon

**Under the terms:**
- 📝 Attribution required
- 🔄 ShareAlike for derivatives

### Code

Code examples licensed under [MIT License](https://opensource.org/licenses/MIT)

## 📞 Contact & Collaboration

### Professional Inquiries

- **Email**: dfr@esmad.ipp.pt
- **Institution**: ESMAD - Escola Superior de Média Arte e Design
- **Company**: Mysense.ai (Lead Data Scientist)
- **ORCID**: [0009-0001-2022-7072](https://orcid.org/0009-0001-2022-7072)

### Research Interests

- Markov Chain Monte Carlo and Bayesian computation
- Machine learning and deep learning
- Causal inference and econometrics
- Financial risk modeling
- Time series analysis and forecasting

### Collaboration Opportunities

- 🎓 Guest lectures and workshops
- 🏢 Corporate training programs
- 🔬 Research collaborations
- 📝 Joint publications
- 🌐 Conference presentations

## 🌟 Acknowledgments

- **ESMAD** for institutional support
- **Mysense.ai** for industry applications and insights
- **Students and colleagues** for valuable feedback
- **Open source community** for tools and inspiration
- **Academic community** for rigorous peer review

## 📈 Version History

See [`CHANGELOG.md`](./CHANGELOG.md) for detailed version history.

---

**Last Updated**: January 2025<br>
**Repository Maintainer**: Diogo Ribeiro<br>
**Status**: ✅ Actively maintained<br>
**Latest Release**: [View releases](https://github.com/diogoribeiro7/academic-presentations/releases)

![GitHub stars](https://img.shields.io/github/stars/diogoribeiro7/academic-presentations?style=social)
![GitHub forks](https://img.shields.io/github/forks/diogoribeiro7/academic-presentations?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/diogoribeiro7/academic-presentations?style=social)
