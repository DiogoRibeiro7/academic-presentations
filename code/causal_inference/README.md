# Causal Inference Implementations

This directory contains implementations of key causal inference methods in both Python and R.

## Python Implementations

### Files
- **`instrumental_variables.py`**: Two-Stage Least Squares (2SLS) estimation
- **`regression_discontinuity.py`**: Sharp RDD with optimal bandwidth selection
- **`diff_in_diff.py`**: Difference-in-Differences with cluster-robust SE

### Requirements (Python)
```bash
pip install numpy pandas scipy scikit-learn matplotlib seaborn statsmodels
```

### Usage Examples

#### Instrumental Variables
```python
from instrumental_variables import InstrumentalVariables

# Y: outcome, D: endogenous treatment, Z: instrument
iv = InstrumentalVariables(Y=earnings, D=education, Z=quarter_of_birth)
results = iv.fit(robust_se=True)
print(iv.summary())
```

#### Regression Discontinuity
```python
from regression_discontinuity import RegressionDiscontinuity

rdd = RegressionDiscontinuity(running_var=test_scores,
                              outcome=graduation_rate,
                              cutoff=50)
results = rdd.estimate()  # Auto-selects bandwidth
rdd.plot_rdd(results)
```

#### Difference-in-Differences
```python
from diff_in_diff import DifferenceInDifferences

# Panel data with columns: unit_id, time, post, treated, outcome
did = DifferenceInDifferences(panel_data)
results = did.estimate_2x2(cluster_se=True)
did.plot_did(results)
```

## R Implementations

### Files
- **`instrumental_variables.R`**: IV/2SLS using ivreg
- **`regression_discontinuity.R`**: RDD using rdrobust
- **`diff_in_diff.R`**: DiD with fixest for TWFE

### Requirements (R)
```r
install.packages(c("AER", "rdrobust", "fixest", "did",
                   "ggplot2", "dplyr", "broom"))
```

## Key Features

### Instrumental Variables (IV/2SLS)
- First-stage diagnostics (F-statistic, R²)
- Weak instrument detection
- Sargan test for overidentification
- Heteroskedasticity-robust standard errors
- Multiple endogenous variables support

### Regression Discontinuity (RDD)
- Imbens-Kalyanaraman optimal bandwidth selection
- Local linear and polynomial regression
- Triangular kernel weighting
- Bandwidth sensitivity analysis
- Continuity checks (density test)
- Visual diagnostics

### Difference-in-Differences (DiD)
- 2x2 DiD estimation
- Cluster-robust standard errors
- Parallel trends testing
- Event study plots (dynamic DiD)
- Multiple time periods support

## References

1. **Instrumental Variables**
   - Angrist, Imbens & Rubin (1996). "Identification of causal effects using instrumental variables"
   - Angrist & Pischke (2008). "Mostly Harmless Econometrics"

2. **Regression Discontinuity**
   - Imbens & Lemieux (2008). "Regression discontinuity designs: A guide to practice"
   - Lee & Lemieux (2010). "Regression discontinuity designs in economics"
   - Calonico et al. (2014). "Robust nonparametric confidence intervals for RDD"

3. **Difference-in-Differences**
   - Card & Krueger (1994). "Minimum wages and employment"
   - Bertrand et al. (2004). "How much should we trust DD estimates?"
   - Abadie (2005). "Semiparametric DiD estimators"

## Examples

Each implementation includes complete working examples:

```bash
# Python
python instrumental_variables.py
python regression_discontinuity.py
python diff_in_diff.py

# R
Rscript instrumental_variables.R
Rscript regression_discontinuity.R
Rscript diff_in_diff.R
```

These generate diagnostic plots and summary statistics.
