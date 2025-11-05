# Optimization for Data Science

**Mathematical optimization methods for machine learning and data science**

## 📚 Overview

This presentation provides comprehensive coverage of optimization techniques essential for modern data science and machine learning. From classical convex optimization to cutting-edge methods for deep learning, the material balances theoretical foundations with practical implementation.

## 🎯 Learning Objectives

By the end of this module, students will be able to:

1. **Optimization Fundamentals**
   - Formulate real-world problems as optimization problems
   - Understand convexity and its implications
   - Derive optimality conditions (KKT conditions)
   - Recognize problem structure (LP, QP, SOCP, SDP)

2. **Gradient-Based Methods**
   - Implement gradient descent and variants
   - Apply momentum and Nesterov acceleration
   - Use adaptive learning rate methods (AdaGrad, RMSprop, Adam)
   - Understand convergence guarantees and rates

3. **Constrained Optimization**
   - Apply Lagrangian duality theory
   - Derive KKT conditions
   - Use penalty and barrier methods
   - Implement augmented Lagrangian methods

4. **Evolutionary & Derivative-Free Methods**
   - Apply genetic algorithms and evolution strategies
   - Use particle swarm optimization (PSO)
   - Implement CMA-ES for difficult landscapes
   - Understand when to use derivative-free methods

5. **Advanced Topics**
   - Apply Bayesian optimization for hyperparameter tuning
   - Solve multi-objective optimization problems
   - Optimize neural network training
   - Handle non-convex optimization in deep learning

## 📋 Topics Covered

### Part 1: Foundations

**Convex Optimization**
- Convex sets and functions
- Strong convexity and smoothness
- Optimality conditions
- Duality theory and KKT conditions

**Problem Formulations**
- Linear programming (LP)
- Quadratic programming (QP)
- Second-order cone programming (SOCP)
- Semidefinite programming (SDP)

### Part 2: Gradient Descent Methods

**Basic Gradient Descent**
- Batch gradient descent
- Stochastic gradient descent (SGD)
- Mini-batch gradient descent
- Learning rate selection
- Convergence analysis

**Momentum Methods**
- Classical momentum
- Nesterov accelerated gradient
- Heavy ball method
- Polyak momentum

**Adaptive Learning Rates**
- AdaGrad (adaptive gradient)
- RMSprop (root mean square propagation)
- Adam (adaptive moment estimation)
- AdamW (Adam with decoupled weight decay)
- AMSGrad and other variants

### Part 3: Second-Order Methods

**Newton's Method**
- Newton-Raphson algorithm
- Quasi-Newton methods (BFGS, L-BFGS)
- Trust region methods
- Cubic regularization

**Natural Gradient**
- Fisher information matrix
- Natural gradient descent
- Applications to deep learning

### Part 4: Constrained Optimization

**Lagrangian Methods**
- Lagrange multipliers
- KKT conditions derivation
- Dual problem formulation
- Strong duality

**Practical Methods**
- Penalty methods (quadratic penalty)
- Barrier methods (interior point)
- Augmented Lagrangian (ADMM)
- Projected gradient descent

### Part 5: Derivative-Free Optimization

**Evolutionary Algorithms**
- Genetic algorithms (GA)
- Evolution strategies (ES)
- Differential evolution
- CMA-ES (Covariance Matrix Adaptation)

**Swarm Intelligence**
- Particle swarm optimization (PSO)
- Ant colony optimization
- Bee colony algorithms

**Bayesian Optimization**
- Gaussian process surrogates
- Acquisition functions (EI, UCB, PI)
- Hyperparameter tuning
- Multi-fidelity optimization

### Part 6: Applications to Deep Learning

**Neural Network Training**
- Loss landscape analysis
- Batch normalization effects
- Learning rate scheduling
- Gradient clipping
- Warm restarts

**Regularization as Optimization**
- L1 and L2 regularization
- Proximal gradient methods
- Group lasso and structured sparsity

**Multi-Objective Optimization**
- Pareto optimality
- Scalarization methods
- Multi-task learning
- Neural architecture search

## 📖 Prerequisites

**Required:**
- Calculus (multivariable, gradients, Hessians)
- Linear algebra (matrices, eigenvalues, positive definite matrices)
- Python programming
- Basic probability

**Recommended:**
- Real analysis (for convergence proofs)
- Numerical methods
- Machine learning basics

## 🛠️ Technical Requirements

### Software
```bash
# Optimization libraries
pip install scipy  # scipy.optimize
pip install cvxpy  # Convex optimization
pip install pyomo  # Mathematical optimization modeling

# Bayesian optimization
pip install scikit-optimize
pip install optuna
pip install hyperopt
pip install ax-platform  # Adaptive experimentation

# Evolutionary algorithms
pip install deap  # Distributed Evolutionary Algorithms
pip install pymoo  # Multi-objective optimization

# Deep learning optimizers
pip install torch  # PyTorch with built-in optimizers
pip install tensorflow  # TensorFlow/Keras

# Visualization
pip install matplotlib seaborn plotly
pip install numpy pandas
```

## 📝 Materials

### Presentation
- **File:** `optimization_beamer.tex`
- **Compile:** `pdflatex optimization_beamer.tex` (run twice)
- **Format:** Beamer slides with aspect ratio 16:9

### Code Examples
Code implementations available in:
- `../code/optimization/` (when created)

### Exercises
Practice problems available in:
- `../exercises/optimization/` (when created)

## 📚 Recommended References

### Textbooks

1. **Convex Optimization** - Boyd & Vandenberghe (2004)
   - The definitive convex optimization text
   - Free online: https://web.stanford.edu/~boyd/cvxbook/

2. **Numerical Optimization** - Nocedal & Wright (2006)
   - Comprehensive coverage of all methods
   - Excellent for algorithms and implementation

3. **First-Order Methods in Optimization** - Beck (2017)
   - Modern perspective on gradient methods
   - Convergence analysis and acceleration

4. **Optimization for Machine Learning** - Sra, Nowozin, Wright (2012)
   - ML-specific optimization
   - Theory and practice

### Research Papers

**Gradient Methods:**
- Nesterov (1983) - "A method for solving convex programming problems"
- Kingma & Ba (2015) - "Adam: A method for stochastic optimization"
- Loshchilov & Hutter (2019) - "Decoupled weight decay regularization (AdamW)"

**Second-Order:**
- Nocedal (1980) - "Updating quasi-Newton matrices with limited storage"
- Martens (2010) - "Deep learning via Hessian-free optimization"

**Bayesian Optimization:**
- Snoek et al. (2012) - "Practical Bayesian optimization of ML algorithms"
- Shahriari et al. (2016) - "Taking the human out of the loop"

**Evolutionary:**
- Hansen & Ostermeier (2001) - "Completely derandomized self-adaptation (CMA-ES)"
- Salimans et al. (2017) - "Evolution strategies as scalable alternative to RL"

**Deep Learning:**
- Smith (2017) - "Cyclical learning rates for training neural networks"
- Loshchilov & Hutter (2017) - "SGDR: Stochastic gradient descent with warm restarts"

### Online Resources
- **CVX101** (Stanford) - Convex Optimization course
- **CS 165B** (UCSB) - Machine Learning Optimization
- **Optuna Documentation** - https://optuna.org/
- **PyTorch Optimizers** - https://pytorch.org/docs/stable/optim.html

## 🎓 Assessment

Students will be evaluated on:

1. **Problem Sets (40%)**
   - Implement gradient descent variants from scratch
   - Solve constrained optimization with KKT
   - Apply CMA-ES to black-box optimization
   - Tune hyperparameters with Bayesian optimization

2. **Quizzes (20%)**
   - Convexity and optimality conditions
   - Convergence rates
   - Algorithm selection

3. **Final Project (40%)**
   - Optimize real-world problem
   - Compare multiple methods
   - Analyze convergence behavior
   - Write technical report

See `../assessments/` for detailed rubrics and evaluation criteria.

## 💡 Study Tips

1. **Master the Theory**
   - Derive optimality conditions
   - Understand convergence proofs
   - Work through examples by hand

2. **Implement from Scratch**
   - Code gradient descent without libraries
   - Implement momentum and Adam
   - Verify convergence on test problems

3. **Visualize Optimization**
   - Plot loss landscapes
   - Animate optimization trajectories
   - Visualize convergence rates

4. **Experiment Systematically**
   - Compare optimizers on same problem
   - Vary learning rates and batch sizes
   - Keep detailed experiment logs

5. **Read Implementation Code**
   - Study PyTorch/TensorFlow optimizer source
   - Understand numerical stability tricks
   - Learn from established libraries

## 🔗 Related Topics

- **Prerequisites:** Calculus, Linear Algebra
- **Follow-up:** Deep Learning, Reinforcement Learning
- **Complementary:** Numerical Methods, Control Theory
- **Applications:** Machine Learning, Operations Research

## 📊 Common Optimization Problems in ML

### Supervised Learning
- Linear regression (least squares)
- Logistic regression (log-likelihood)
- Support vector machines (hinge loss + regularization)
- Neural networks (cross-entropy + regularization)

### Unsupervised Learning
- K-means clustering (sum of squared distances)
- PCA (eigenvalue problem)
- Matrix factorization (Frobenius norm)
- Autoencoders (reconstruction loss)

### Reinforcement Learning
- Policy optimization (policy gradient)
- Value function approximation (Bellman residual)
- Actor-critic methods (combined objective)

## 📧 Contact

For questions about this module:
- **Instructor:** Diogo Ribeiro
- **Email:** dfr@esmad.ipp.pt
- **Office Hours:** By appointment
- **Issues:** [GitHub Issues](https://github.com/diogoribeiro7/academic-presentations/issues)

## 📄 License

**Content:** Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
**Code:** MIT License

---

*Last Updated: January 2025*
*Part of the Academic Presentations series by Diogo Ribeiro, ESMAD & Mysense.ai*
