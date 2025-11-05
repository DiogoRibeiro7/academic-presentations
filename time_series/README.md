# Time Series Analysis & Forecasting

**From classical ARIMA to modern deep learning approaches**

## 📚 Overview

This presentation provides comprehensive coverage of time series analysis and forecasting, spanning classical statistical methods to cutting-edge deep learning approaches. The material is designed for graduate students and practitioners who need to analyze and forecast time-dependent data.

## 🎯 Learning Objectives

By the end of this module, students will be able to:

1. **Time Series Fundamentals**
   - Analyze time series components (trend, seasonality, cyclical, irregular)
   - Test for and achieve stationarity
   - Perform time series decomposition
   - Identify autocorrelation and partial autocorrelation patterns

2. **Classical Statistical Methods**
   - Build and diagnose ARMA models
   - Fit ARIMA models for non-stationary data
   - Apply SARIMA for seasonal time series
   - Implement exponential smoothing methods
   - Use Box-Jenkins methodology

3. **Multivariate Methods**
   - Estimate Vector Autoregression (VAR) models
   - Test for Granger causality
   - Apply cointegration analysis
   - Build Vector Error Correction Models (VECM)

4. **State Space Methods**
   - Formulate state space models
   - Apply Kalman filter for estimation
   - Use structural time series models
   - Handle missing data and irregularly-spaced observations

5. **Modern Deep Learning Approaches**
   - Build LSTM networks for forecasting
   - Apply GRU for sequential modeling
   - Implement Temporal Convolutional Networks (TCN)
   - Use Transformer models (Temporal Fusion Transformer, Autoformer, Informer)
   - Apply N-BEATS for interpretable forecasting

6. **Hybrid & Advanced Methods**
   - Combine statistical and ML approaches (ES-RNN)
   - Use Facebook Prophet for business time series
   - Apply Bayesian structural time series
   - Implement probabilistic forecasting
   - Evaluate forecast accuracy and uncertainty

## 📋 Topics Covered

### Part 1: Fundamentals

**Time Series Components**
- Trend (deterministic vs stochastic)
- Seasonality (additive vs multiplicative)
- Cyclical patterns
- Irregular/noise component

**Stationarity**
- Weak/covariance stationarity
- Strict stationarity
- Unit root tests (ADF, KPSS, PP)
- Differencing and transformations

**Autocorrelation**
- ACF (Autocorrelation Function)
- PACF (Partial Autocorrelation Function)
- Ljung-Box test
- Correlogram interpretation

### Part 2: Univariate Models

**ARMA Models**
- Autoregressive (AR) processes
- Moving Average (MA) processes
- ARMA(p,q) models
- Identification and estimation
- Diagnostic checking

**ARIMA Models**
- Integrated processes
- ARIMA(p,d,q) specification
- Model selection (AIC, BIC)
- Residual diagnostics
- Forecasting with ARIMA

**Seasonal Models**
- SARIMA(p,d,q)(P,D,Q)s
- Seasonal differencing
- Airline model
- Forecasting seasonality

**Exponential Smoothing**
- Simple exponential smoothing
- Holt's linear trend method
- Holt-Winters seasonal method
- ETS framework

### Part 3: Multivariate Models

**Vector Autoregression (VAR)**
- VAR specification and estimation
- Order selection
- Impulse response functions
- Forecast error variance decomposition

**Granger Causality**
- Testing for causality
- Instantaneous causality
- Block exogeneity tests

**Cointegration**
- Engle-Granger two-step method
- Johansen test
- Vector Error Correction Model (VECM)
- Long-run relationships

### Part 4: State Space Models

**Kalman Filter**
- State space representation
- Prediction and update equations
- Filtering, smoothing, prediction
- Maximum likelihood estimation

**Structural Models**
- Local level model
- Local linear trend
- Seasonal components
- Unobserved components models

**Dynamic Linear Models**
- Time-varying coefficients
- Bayesian estimation
- DLM framework

### Part 5: Deep Learning for Time Series

**Recurrent Architectures**
- Vanilla RNNs
- Long Short-Term Memory (LSTM)
- Gated Recurrent Units (GRU)
- Bidirectional RNNs
- Encoder-decoder architectures
- Sequence-to-sequence models

**Convolutional Approaches**
- 1D CNNs for time series
- Temporal Convolutional Networks (TCN)
- WaveNet architecture
- Dilated causal convolutions

**Attention-Based Models**
- Attention mechanisms for sequences
- Temporal Fusion Transformer (TFT)
- Autoformer (autocorrelation mechanism)
- Informer (ProbSparse attention)
- Temporal Attention Augmented Bilinear Network

**Specialized Architectures**
- N-BEATS (interpretable forecasting)
- DeepAR (probabilistic forecasting)
- Prophet-like neural architectures

### Part 6: Hybrid & Advanced Methods

**Hybrid Approaches**
- ES-RNN (combining exponential smoothing and RNN)
- Statistical + ML ensembles
- Residual modeling with ML

**Prophet**
- Additive model formulation
- Trend detection and changepoints
- Seasonality modeling
- Holiday effects
- Uncertainty quantification

**Bayesian Methods**
- Bayesian structural time series (bsts)
- MCMC for time series
- Hierarchical time series models
- Dynamic factor models

**Probabilistic Forecasting**
- Point vs interval forecasting
- Quantile regression
- Conformal prediction
- Forecast combination

### Part 7: Evaluation & Diagnostics

**Accuracy Metrics**
- MSE, RMSE, MAE
- MAPE, sMAPE
- MASE (Mean Absolute Scaled Error)
- Forecast skill scores

**Diagnostic Tests**
- Residual analysis
- Heteroskedasticity tests (ARCH, GARCH)
- Normality tests
- Outlier detection

**Backtesting**
- Rolling window validation
- Expanding window validation
- Cross-validation for time series
- Walk-forward analysis

## 📖 Prerequisites

**Required:**
- Statistics (hypothesis testing, regression)
- Linear algebra (matrices, eigenvalues)
- Python or R programming
- Basic probability

**Recommended:**
- Stochastic processes
- Maximum likelihood estimation
- Bayesian inference
- Deep learning basics (for neural methods)

## 🛠️ Technical Requirements

### Software - Python
```bash
# Classical time series
pip install statsmodels  # ARIMA, SARIMA, VAR
pip install pmdarima  # Auto-ARIMA
pip install prophet  # Facebook Prophet

# State space
pip install pykalman
pip install pydlm  # Bayesian DLM
pip install pymc  # Bayesian modeling

# Deep learning
pip install torch  # PyTorch
pip install pytorch-forecasting  # Deep learning forecasting
pip install darts  # Time series forecasting library
pip install neuralforecast  # Nixtla's neural forecasting

# Utilities
pip install numpy pandas matplotlib seaborn
pip install scikit-learn scipy
```

### Software - R
```r
# Classical methods
install.packages(c(
  "forecast",    # ARIMA, ETS, auto.arima
  "vars",        # VAR, VECM
  "urca",        # Unit root and cointegration tests
  "tseries"      # Time series utilities
))

# State space
install.packages(c(
  "dlm",         # Dynamic linear models
  "KFAS",        # Kalman filter and smoother
  "bsts"         # Bayesian structural time series
))

# Modern methods
install.packages(c(
  "fable",       # Tidy forecasting framework
  "prophet",     # Facebook Prophet
  "modeltime"    # Unified modeling interface
))
```

## 📝 Materials

### Presentation
- **File:** `time_series_beamer.tex`
- **Compile:** `pdflatex time_series_beamer.tex` (run twice)
- **Format:** Beamer slides with aspect ratio 16:9

### Code Examples
Code implementations available in:
- `../code/time_series/` (when created)

### Exercises
Practice problems available in:
- `../exercises/time_series/` (when created)

## 📚 Recommended References

### Textbooks

1. **Time Series Analysis** - Hamilton (1994)
   - Comprehensive theoretical treatment
   - Gold standard for understanding

2. **Forecasting: Principles and Practice** - Hyndman & Athanasopoulos (2021)
   - Practical forecasting guide
   - Free online: https://otexts.com/fpp3/

3. **Time Series Analysis and Its Applications** - Shumway & Stoffer (2017)
   - R-based with examples
   - State space methods

4. **Analysis of Financial Time Series** - Tsay (2010)
   - Financial applications
   - GARCH and volatility models

### Research Papers

**Classical:**
- Box & Jenkins (1970) - "Time Series Analysis: Forecasting and Control"
- Akaike (1974) - "A new look at the statistical model identification (AIC)"
- Engle & Granger (1987) - "Co-integration and error correction"

**Deep Learning:**
- Hochreiter & Schmidhuber (1997) - "Long short-term memory (LSTM)"
- Bai et al. (2018) - "An empirical evaluation of generic convolutional and recurrent networks (TCN)"
- Oreshkin et al. (2020) - "N-BEATS: Neural basis expansion analysis"
- Lim et al. (2021) - "Temporal Fusion Transformers"
- Wu et al. (2021) - "Autoformer: Decomposition Transformers with auto-correlation"
- Zhou et al. (2021) - "Informer: Beyond efficient transformer"

**Hybrid:**
- Smyl (2020) - "A hybrid method of exponential smoothing and RNNs (ES-RNN)"
- Taylor & Letham (2018) - "Forecasting at scale (Prophet)"

**Bayesian:**
- Scott & Varian (2014) - "Bayesian structural time series (bsts)"
- Salinas et al. (2020) - "DeepAR: Probabilistic forecasting"

### Online Resources
- **Forecasting Principles** - https://otexts.com/fpp3/
- **statsmodels Documentation** - https://www.statsmodels.org/
- **PyTorch Forecasting** - https://pytorch-forecasting.readthedocs.io/
- **Darts Tutorial** - https://unit8co.github.io/darts/

## 🎓 Assessment

Students will be evaluated on:

1. **Problem Sets (40%)**
   - Fit ARIMA model to real data
   - Build VAR model for multivariate series
   - Implement LSTM forecaster
   - Compare classical vs deep learning methods

2. **Quizzes (20%)**
   - Stationarity and unit roots
   - Model identification
   - Evaluation metrics

3. **Final Project (40%)**
   - Forecast real-world time series
   - Compare multiple methods
   - Evaluate forecast accuracy
   - Present findings with visualizations

See `../assessments/` for detailed rubrics and evaluation criteria.

## 💡 Study Tips

1. **Understand the Data**
   - Always plot your time series first
   - Identify patterns visually
   - Check for outliers and missing data
   - Understand the domain context

2. **Start with Classical Methods**
   - Master ARIMA before deep learning
   - Understand ACF/PACF interpretation
   - Practice model diagnostics
   - Use as baseline for comparison

3. **Visualize Everything**
   - Plot ACF and PACF
   - Show fitted vs actual values
   - Display forecast intervals
   - Compare multiple forecasts

4. **Test Rigorously**
   - Use proper train-test splits
   - Implement walk-forward validation
   - Report multiple metrics
   - Check residual assumptions

5. **Learn from Competitions**
   - Study Kaggle time series competitions
   - Read winning solutions
   - Implement ensemble methods
   - Practice feature engineering

## 🔗 Related Topics

- **Prerequisites:** Statistics, Regression Analysis
- **Follow-up:** Financial Econometrics, Forecasting Systems
- **Complementary:** Deep Learning, Bayesian ML, Causal Inference
- **Applications:** Finance, Economics, Energy, Demand Forecasting

## 📊 Common Time Series Applications

### Finance
- Stock price forecasting
- Volatility modeling (GARCH)
- Risk management
- Algorithmic trading

### Economics
- GDP forecasting
- Inflation modeling
- Unemployment prediction
- Policy analysis

### Business
- Demand forecasting
- Sales prediction
- Inventory optimization
- Customer behavior

### Energy
- Load forecasting
- Renewable energy prediction
- Price forecasting

### Other
- Weather forecasting
- Traffic prediction
- Epidemiology (disease spread)
- IoT sensor data

## ⚠️ Common Pitfalls

1. **Data Leakage** - Using future information in features
2. **Wrong Metrics** - MAPE fails with zeros, RMSE sensitive to outliers
3. **Ignoring Stationarity** - Spurious regressions with non-stationary data
4. **Overfitting** - Too many parameters relative to data
5. **Poor Validation** - Using random splits instead of time-based
6. **Missing Uncertainty** - Point forecasts without intervals

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
