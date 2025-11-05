# Time Series Analysis Self-Assessment Checklist

**Topic:** Time Series Analysis & Forecasting
**Related Presentation:** `../../time_series/`
**Last Updated:** January 2025

## How to Use This Checklist

- Check ✅ items you understand well
- Leave unchecked ⬜ items you need to study
- Use color coding (see README) for more granular tracking
- Review before quizzes, exams, and while studying

---

## 1. Time Series Fundamentals

### Conceptual Understanding
- [ ] I understand the components of a time series (trend, seasonal, cyclical, irregular)
- [ ] I can distinguish between additive and multiplicative decomposition
- [ ] I understand weak vs strict stationarity
- [ ] I know why stationarity matters for modeling
- [ ] I can explain the difference between deterministic and stochastic trends

### Mathematical Foundations
- [ ] I can write the mathematical definition of stationarity
- [ ] I understand the autocovariance function
- [ ] I can compute mean and variance of a time series
- [ ] I know the mathematical formulation of decomposition

### Practical Skills
- [ ] I can decompose a time series in Python/R
- [ ] I can plot and identify time series components
- [ ] I can perform seasonal adjustment
- [ ] I can handle missing values in time series

---

## 2. Stationarity & Testing

### Conceptual Understanding
- [ ] I understand what makes a series non-stationary
- [ ] I know different types of non-stationarity
- [ ] I understand the concept of unit roots
- [ ] I can explain differencing and its effects
- [ ] I know when to use transformations (log, Box-Cox)

### Mathematical Foundations
- [ ] I can write the equation for a unit root process
- [ ] I understand the mathematics of differencing
- [ ] I know the hypotheses of ADF test
- [ ] I can interpret test statistics (ADF, KPSS, PP)

### Practical Skills
- [ ] I can perform unit root tests (ADF, KPSS)
- [ ] I can apply appropriate transformations
- [ ] I can difference a time series
- [ ] I can check if differencing achieved stationarity
- [ ] I know how many differences are typically needed

---

## 3. Autocorrelation Analysis

### Conceptual Understanding
- [ ] I understand autocorrelation (ACF)
- [ ] I can explain partial autocorrelation (PACF)
- [ ] I know the difference between ACF and PACF
- [ ] I understand how to use ACF/PACF for model identification
- [ ] I can explain the Ljung-Box test

### Mathematical Foundations
- [ ] I can write the equation for sample ACF
- [ ] I can write the equation for PACF
- [ ] I understand the standard errors for ACF/PACF
- [ ] I know the theoretical ACF/PACF for AR and MA processes

### Practical Skills
- [ ] I can plot and interpret ACF
- [ ] I can plot and interpret PACF
- [ ] I can identify patterns in correlograms
- [ ] I can use ACF/PACF to identify model orders
- [ ] I can perform Ljung-Box test for white noise

---

## 4. ARMA Models

### Conceptual Understanding
- [ ] I understand autoregressive (AR) processes
- [ ] I understand moving average (MA) processes
- [ ] I can explain the ARMA model
- [ ] I know the conditions for stationarity and invertibility
- [ ] I understand the ACF/PACF patterns of AR and MA

### Mathematical Foundations
- [ ] I can write AR(p) equations
- [ ] I can write MA(q) equations
- [ ] I can write ARMA(p,q) equations
- [ ] I can derive stationarity conditions for AR(1)
- [ ] I understand the backshift operator notation

### Practical Skills
- [ ] I can identify AR vs MA from ACF/PACF
- [ ] I can estimate ARMA models in Python/R
- [ ] I can determine appropriate p and q orders
- [ ] I can check residuals for white noise
- [ ] I can forecast using ARMA models

---

## 5. ARIMA & SARIMA Models

### Conceptual Understanding
- [ ] I understand the integrated (I) component of ARIMA
- [ ] I can explain the Box-Jenkins methodology
- [ ] I understand seasonal ARIMA (SARIMA)
- [ ] I know how to handle seasonality
- [ ] I can explain the airline model

### Mathematical Foundations
- [ ] I can write ARIMA(p,d,q) equations
- [ ] I can write SARIMA(p,d,q)(P,D,Q)s equations
- [ ] I understand seasonal differencing
- [ ] I can interpret ARIMA model orders

### Practical Skills
- [ ] I can fit ARIMA models
- [ ] I can use auto.arima or pmdarima
- [ ] I can fit SARIMA models
- [ ] I can select model orders using AIC/BIC
- [ ] I can perform diagnostic checking
- [ ] I can forecast with confidence intervals

---

## 6. Exponential Smoothing

### Conceptual Understanding
- [ ] I understand simple exponential smoothing
- [ ] I can explain Holt's linear trend method
- [ ] I understand Holt-Winters seasonal method
- [ ] I know the ETS framework
- [ ] I can compare exponential smoothing to ARIMA

### Mathematical Foundations
- [ ] I can write the equation for simple exponential smoothing
- [ ] I can write Holt's trend equations
- [ ] I can write Holt-Winters equations
- [ ] I understand the smoothing parameters (α, β, γ)

### Practical Skills
- [ ] I can apply simple exponential smoothing
- [ ] I can implement Holt's method
- [ ] I can use Holt-Winters for seasonal data
- [ ] I can choose smoothing parameters
- [ ] I can forecast using exponential smoothing methods

---

## 7. Multivariate Time Series

### Conceptual Understanding
- [ ] I understand Vector Autoregression (VAR)
- [ ] I can explain Granger causality
- [ ] I understand cointegration
- [ ] I know what a Vector Error Correction Model (VECM) is
- [ ] I can explain impulse response functions

### Mathematical Foundations
- [ ] I can write VAR equations in matrix form
- [ ] I can write the Granger causality test equation
- [ ] I understand the Engle-Granger cointegration test
- [ ] I can write VECM equations

### Practical Skills
- [ ] I can estimate VAR models
- [ ] I can select VAR order
- [ ] I can test for Granger causality
- [ ] I can test for cointegration (Engle-Granger, Johansen)
- [ ] I can estimate VECM models
- [ ] I can compute impulse response functions

---

## 8. State Space Models & Kalman Filter

### Conceptual Understanding
- [ ] I understand state space representation
- [ ] I can explain the Kalman filter
- [ ] I understand filtering vs smoothing vs prediction
- [ ] I know structural time series models
- [ ] I can explain unobserved components

### Mathematical Foundations
- [ ] I can write state space equations
- [ ] I understand the Kalman filter recursions
- [ ] I can write the measurement and transition equations
- [ ] I know the mathematics of the prediction and update steps

### Practical Skills
- [ ] I can formulate models in state space form
- [ ] I can implement basic Kalman filter
- [ ] I can use pykalman or similar libraries
- [ ] I can estimate structural time series models
- [ ] I can handle missing data with Kalman filter

---

## 9. Deep Learning for Time Series

### Conceptual Understanding
- [ ] I understand when to use RNNs for time series
- [ ] I can explain LSTM for forecasting
- [ ] I understand Temporal Convolutional Networks (TCN)
- [ ] I know about Transformer models for time series
- [ ] I can compare classical vs deep learning approaches

### Mathematical Foundations
- [ ] I understand the LSTM equations
- [ ] I can explain causal convolutions
- [ ] I understand attention mechanisms for sequences
- [ ] I know the architecture of Temporal Fusion Transformer

### Practical Skills
- [ ] I can build LSTM models for forecasting
- [ ] I can implement sequence-to-sequence models
- [ ] I can use pytorch-forecasting or similar
- [ ] I can train Transformers for time series
- [ ] I know when deep learning outperforms classical methods

---

## 10. Forecasting & Evaluation

### Conceptual Understanding
- [ ] I understand point vs interval forecasts
- [ ] I can explain forecast horizons (h-step ahead)
- [ ] I understand the difference between in-sample and out-of-sample
- [ ] I know proper cross-validation for time series
- [ ] I can explain probabilistic forecasting

### Mathematical Foundations
- [ ] I can compute forecast intervals
- [ ] I understand forecast error metrics (MSE, MAE, MAPE, MASE)
- [ ] I know how to calculate prediction intervals
- [ ] I understand the mathematics of forecast combination

### Practical Skills
- [ ] I can generate point forecasts
- [ ] I can compute confidence intervals
- [ ] I can evaluate forecasts with multiple metrics
- [ ] I can implement rolling window validation
- [ ] I can visualize forecasts with uncertainty
- [ ] I can combine forecasts from multiple models

---

## 11. Advanced Topics

### Conceptual Understanding
- [ ] I understand GARCH models for volatility
- [ ] I know about Facebook Prophet
- [ ] I can explain Bayesian structural time series
- [ ] I understand N-BEATS architecture
- [ ] I know about hierarchical forecasting

### Practical Skills
- [ ] I can fit GARCH models
- [ ] I can use Prophet for business time series
- [ ] I can implement Bayesian time series models
- [ ] I can use modern forecasting libraries (Darts, GluonTS)
- [ ] I can handle multiple related time series

---

## 12. Diagnostic Checking & Validation

### Conceptual Understanding
- [ ] I understand residual analysis
- [ ] I know how to check model assumptions
- [ ] I can explain overfitting in time series
- [ ] I understand how to validate time series models
- [ ] I know common pitfalls in time series analysis

### Practical Skills
- [ ] I can analyze residuals for autocorrelation
- [ ] I can test residuals for normality
- [ ] I can detect outliers and structural breaks
- [ ] I can use walk-forward validation
- [ ] I can diagnose model inadequacy
- [ ] I can compare models fairly

---

## Self-Assessment Summary

**Count your checks:**
- Total items: 105
- Items checked: _____ / 105
- Percentage: _____ %

**Readiness for Assessment:**
- 90-100%: Excellent, ready for exam
- 75-89%: Good, review weak areas
- 60-74%: Adequate, need focused study
- <60%: Need significant review

**Priority Areas to Study:**
(List topic sections with fewest checks)
1. _____________________
2. _____________________
3. _____________________

**Study Plan:**
- Date of next assessment: __________
- Study hours needed: __________
- Focus areas: __________

---

## Additional Resources

**If you need help with:**
- **Fundamentals:** Review slides 1-30, Hyndman & Athanasopoulos textbook
- **Stationarity:** Practice unit root tests, work through examples
- **ARIMA:** Box-Jenkins methodology, auto.arima documentation
- **Multivariate:** VAR tutorial, cointegration examples
- **State Space:** Kalman filter tutorial, pykalman examples
- **Deep Learning:** PyTorch Forecasting tutorials, TFT paper
- **Practical skills:** Complete coding assignments, Kaggle competitions

**Office Hours:** Schedule time if you have many unchecked items
**Study Group:** Find peers to work through difficult concepts

---

## Common Time Series Pitfalls

Watch out for:
- [ ] Using random train-test splits instead of temporal splits
- [ ] Forgetting to difference non-stationary data
- [ ] Overfitting due to too many parameters
- [ ] Not checking residuals for autocorrelation
- [ ] Using MAPE with data containing zeros
- [ ] Data leakage (using future information)
- [ ] Ignoring seasonality
- [ ] Not accounting for outliers

---

*Last Updated: January 2025*
*Part of the Academic Presentations Assessment Materials*
