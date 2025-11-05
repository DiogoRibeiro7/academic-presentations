# Explainable AI & Model Interpretability

**Understanding and explaining black-box machine learning models**

## 📚 Overview

This presentation explores the critical field of Explainable AI (XAI), addressing the interpretability-accuracy tradeoff and providing practical tools for explaining complex machine learning models. The material covers both model-agnostic and model-specific methods, with emphasis on real-world applications and fairness considerations.

## 🎯 Learning Objectives

By the end of this module, students will be able to:

1. **Interpretability Fundamentals**
   - Distinguish between interpretability and explainability
   - Understand the interpretability-accuracy tradeoff
   - Identify when interpretability is critical (healthcare, finance, legal)

2. **Model-Agnostic Methods**
   - Compute and interpret SHAP (SHapley Additive exPlanations) values
   - Apply LIME (Local Interpretable Model-agnostic Explanations)
   - Calculate permutation feature importance
   - Create and interpret Partial Dependence Plots (PDPs)
   - Generate Individual Conditional Expectation (ICE) plots

3. **Model-Specific Interpretability**
   - Interpret linear model coefficients correctly
   - Understand decision tree paths and feature splits
   - Visualize attention weights in neural networks
   - Apply gradient-based explanations (saliency maps, GradCAM)

4. **Fairness & Bias**
   - Detect algorithmic bias in ML models
   - Implement fairness metrics (demographic parity, equalized odds)
   - Understand fairness impossibility results
   - Apply bias mitigation techniques

5. **Practical Implementation**
   - Use SHAP, LIME, and InterpretML libraries
   - Create effective visualizations for stakeholders
   - Build interpretable ML pipelines
   - Communicate model behavior to non-technical audiences

## 📋 Topics Covered

### Part 1: Introduction to XAI
- Why interpretability matters
- Interpretability vs explainability
- Interpretability-accuracy tradeoff
- Regulatory requirements (GDPR, ECOA)
- Use cases: healthcare, finance, criminal justice

### Part 2: Global vs Local Explanations
- Global interpretability (entire model behavior)
- Local interpretability (individual predictions)
- When to use each approach
- Trade-offs and limitations

### Part 3: Model-Agnostic Methods

**SHAP (SHapley Additive exPlanations)**
- Shapley values from game theory
- KernelSHAP and TreeSHAP
- SHAP summary plots and dependence plots
- SHAP force plots and waterfall charts

**LIME**
- Local linear approximations
- Perturbation-based explanations
- Text, image, and tabular LIME
- Stability and reliability considerations

**Permutation Importance**
- Feature importance via permutation
- Comparison with built-in importances
- Handling correlated features

**Partial Dependence**
- PDP computation and interpretation
- ICE plots for heterogeneity
- 2D PDPs for feature interactions
- Accumulated Local Effects (ALE)

### Part 4: Model-Specific Methods

**Linear Models**
- Coefficient interpretation
- Standardization for comparison
- Interaction terms

**Tree-Based Models**
- Feature importance (Gini, split)
- Tree visualization
- Rule extraction

**Neural Networks**
- Attention mechanisms
- Saliency maps
- GradCAM and Grad-CAM++
- Layer-wise Relevance Propagation (LRP)
- Integrated Gradients

### Part 5: Algorithmic Fairness

**Fairness Definitions**
- Demographic parity
- Equalized odds
- Predictive parity
- Individual fairness
- Impossibility results

**Bias Detection**
- Disparate impact analysis
- Subgroup performance evaluation
- Intersectional fairness

**Bias Mitigation**
- Pre-processing (reweighting, resampling)
- In-processing (fairness constraints)
- Post-processing (threshold adjustment)

## 📖 Prerequisites

**Required:**
- Machine learning fundamentals
- Python programming
- Basic statistics and probability
- Experience with scikit-learn

**Recommended:**
- Deep learning basics (for neural network explanations)
- Game theory (for Shapley values)
- Causal inference (for counterfactual explanations)

## 🛠️ Technical Requirements

### Software
```bash
# Core XAI libraries
pip install shap lime
pip install interpret  # InterpretML
pip install alibi  # Algorithmic fairness

# ML frameworks
pip install scikit-learn xgboost lightgbm
pip install torch torchvision  # For neural network explanations

# Visualization
pip install matplotlib seaborn plotly
pip install pandas numpy

# Fairness
pip install fairlearn aif360
```

### Datasets
Common datasets for XAI practice:
- **Adult Income** (fairness analysis)
- **COMPAS** (criminal justice bias)
- **German Credit** (interpretability)
- **ImageNet** (vision model explanations)

## 📝 Materials

### Presentation
- **File:** `interpretability_beamer.tex`
- **Compile:** `pdflatex interpretability_beamer.tex` (run twice)
- **Format:** Beamer slides with aspect ratio 16:9

### Code Examples
Code implementations available in:
- `../code/explainable_ai/` (when created)

### Exercises
Practice problems available in:
- `../exercises/explainable_ai/` (when created)

## 📚 Recommended References

### Textbooks
1. **Interpretable Machine Learning** - Molnar (2022)
   - Comprehensive XAI guide
   - Free online: https://christophm.github.io/interpretable-ml-book/

2. **Fairness and Machine Learning** - Barocas, Hardt, Narayanan (2023)
   - Algorithmic fairness
   - Free online: https://fairmlbook.org/

### Research Papers

**SHAP:**
- Lundberg & Lee (2017) - "A unified approach to interpreting model predictions"
- Lundberg et al. (2020) - "From local explanations to global understanding"

**LIME:**
- Ribeiro et al. (2016) - "Why should I trust you?"
- Ribeiro et al. (2018) - "Anchors: High-precision model-agnostic explanations"

**Neural Network Explanations:**
- Selvaraju et al. (2017) - "Grad-CAM: Visual explanations from deep networks"
- Sundararajan et al. (2017) - "Axiomatic attribution for deep networks"
- Vaswani et al. (2017) - "Attention is all you need"

**Fairness:**
- Hardt et al. (2016) - "Equality of opportunity in supervised learning"
- Chouldechova (2017) - "Fair prediction with disparate impact"
- Kleinberg et al. (2017) - "Inherent trade-offs in algorithmic fairness"

**Surveys:**
- Guidotti et al. (2018) - "A survey of methods for explaining black box models"
- Arrieta et al. (2020) - "Explainable AI: A review of machine learning interpretability"

### Online Resources
- **InterpretML** - https://interpret.ml/
- **SHAP Documentation** - https://shap.readthedocs.io/
- **Fairlearn** - https://fairlearn.org/
- **AI Fairness 360** - https://aif360.mybluemix.net/

## 🎓 Assessment

Students will be evaluated on:

1. **Problem Sets (40%)**
   - Compute SHAP values for complex models
   - Apply LIME to text and image data
   - Conduct fairness audit on ML model
   - Create interpretability dashboard

2. **Quizzes (20%)**
   - XAI concepts and methods
   - Fairness definitions
   - Tool selection and application

3. **Final Project (40%)**
   - Explain black-box model on real data
   - Analyze fairness across subgroups
   - Create stakeholder presentation
   - Write interpretability report

See `../assessments/` for detailed rubrics and evaluation criteria.

## 💡 Study Tips

1. **Understand the Math**
   - Derive Shapley values for simple examples
   - Understand LIME's local linear approximation
   - Work through fairness metric calculations

2. **Practice with Real Models**
   - Train complex models (XGBoost, neural networks)
   - Apply multiple explanation methods
   - Compare and contrast explanations

3. **Visualize Effectively**
   - Create clear, informative plots
   - Tailor visualizations to audience
   - Use interactive tools (Plotly, Streamlit)

4. **Consider Context**
   - Think about when interpretability is critical
   - Understand domain-specific requirements
   - Balance accuracy with interpretability

5. **Read Case Studies**
   - Healthcare AI explanations
   - Financial model interpretability
   - Criminal justice fairness analysis

## 🔗 Related Topics

- **Prerequisites:** Machine Learning, Statistical Learning
- **Complementary:** Deep Learning, Causal Inference, Bayesian ML
- **Applications:** Healthcare AI, Financial ML, Computer Vision

## ⚠️ Important Considerations

### When XAI is Critical
- **Healthcare:** Diagnosis and treatment recommendations
- **Finance:** Credit decisions and fraud detection
- **Legal:** Parole and sentencing systems
- **Hiring:** Resume screening and candidate selection

### Limitations of XAI
- Explanations may not reflect true model behavior
- Local explanations may not generalize
- Multiple valid explanations may exist
- Explanations can be manipulated

### Ethical Guidelines
- Be transparent about model limitations
- Consider fairness across protected groups
- Validate explanations with domain experts
- Document explanation methodology

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
