"""
Instrumental Variables (IV) Estimation
=======================================

Implementation of Two-Stage Least Squares (2SLS) and related IV methods.

References:
    Angrist, Imbens & Rubin (1996), Angrist & Pischke (2008)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from typing import Tuple, Optional
from dataclasses import dataclass

sns.set_style("whitegrid")


@dataclass
class IVResults:
    """Results from IV estimation."""
    beta_iv: np.ndarray
    se_iv: np.ndarray
    first_stage_f: float
    first_stage_r2: float
    sargan_stat: Optional[float] = None
    sargan_pvalue: Optional[float] = None


class InstrumentalVariables:
    """
    Two-Stage Least Squares (2SLS) estimator.

    Parameters
    ----------
    Y : array-like
        Outcome variable
    D : array-like
        Treatment/endogenous variable(s)
    Z : array-like
        Instrument(s)
    X : array-like, optional
        Exogenous controls
    """

    def __init__(self, Y: np.ndarray, D: np.ndarray, Z: np.ndarray,
                 X: Optional[np.ndarray] = None):
        self.Y = np.asarray(Y).reshape(-1, 1)
        self.D = np.asarray(D).reshape(-1, 1) if D.ndim == 1 else np.asarray(D)
        self.Z = np.asarray(Z).reshape(-1, 1) if Z.ndim == 1 else np.asarray(Z)
        self.X = X if X is None else np.asarray(X)

        self.n = len(Y)
        self.results = None

    def fit(self, robust_se: bool = True) -> IVResults:
        """
        Estimate IV model using 2SLS.

        Parameters
        ----------
        robust_se : bool
            Use heteroskedasticity-robust standard errors

        Returns
        -------
        IVResults
            Estimation results
        """
        # Prepare design matrices
        if self.X is not None:
            # Include controls in both stages
            Z_full = np.hstack([np.ones((self.n, 1)), self.X, self.Z])
            X_with_const = np.hstack([np.ones((self.n, 1)), self.X])
        else:
            Z_full = np.hstack([np.ones((self.n, 1)), self.Z])
            X_with_const = np.ones((self.n, 1))

        # First stage: regress D on Z (and X if present)
        D_hat = Z_full @ np.linalg.lstsq(Z_full, self.D, rcond=None)[0]

        # First stage diagnostics
        residuals_first = self.D - D_hat
        ss_res_first = np.sum(residuals_first**2)
        ss_tot_first = np.sum((self.D - self.D.mean())**2)
        r2_first = 1 - ss_res_first / ss_tot_first

        # F-statistic for first stage
        k_instruments = self.Z.shape[1]
        k_controls = 0 if self.X is None else self.X.shape[1]
        k_total = k_instruments + k_controls + 1  # +1 for intercept

        f_stat = (r2_first / k_instruments) / ((1 - r2_first) / (self.n - k_total))

        # Second stage: regress Y on D_hat (and X if present)
        if self.X is not None:
            D_hat_full = np.hstack([np.ones((self.n, 1)), self.X, D_hat])
        else:
            D_hat_full = np.hstack([np.ones((self.n, 1)), D_hat])

        beta_iv = np.linalg.lstsq(D_hat_full, self.Y, rcond=None)[0]

        # Calculate standard errors
        residuals = self.Y - D_hat_full @ beta_iv

        if robust_se:
            # Heteroskedasticity-robust standard errors
            meat = np.zeros((D_hat_full.shape[1], D_hat_full.shape[1]))
            for i in range(self.n):
                meat += residuals[i]**2 * np.outer(D_hat_full[i], D_hat_full[i])

            bread_inv = np.linalg.inv(D_hat_full.T @ D_hat_full / self.n)
            var_beta = bread_inv @ meat @ bread_inv / self.n
        else:
            # Homoskedastic standard errors
            sigma2 = np.sum(residuals**2) / (self.n - D_hat_full.shape[1])
            var_beta = sigma2 * np.linalg.inv(D_hat_full.T @ D_hat_full)

        se_iv = np.sqrt(np.diag(var_beta))

        # Sargan test for overidentification (if we have more instruments than endogenous vars)
        if k_instruments > self.D.shape[1]:
            # Regress 2SLS residuals on all instruments
            sargan_resid = residuals
            proj = Z_full @ np.linalg.lstsq(Z_full, sargan_resid, rcond=None)[0]
            sargan_stat = (sargan_resid.T @ proj).item() / (residuals.T @ residuals / self.n).item()
            df = k_instruments - self.D.shape[1]
            sargan_pvalue = 1 - stats.chi2.cdf(sargan_stat, df)
        else:
            sargan_stat = None
            sargan_pvalue = None

        self.results = IVResults(
            beta_iv=beta_iv,
            se_iv=se_iv,
            first_stage_f=f_stat,
            first_stage_r2=r2_first,
            sargan_stat=sargan_stat,
            sargan_pvalue=sargan_pvalue
        )

        return self.results

    def summary(self) -> str:
        """Print estimation summary."""
        if self.results is None:
            return "Model not fitted. Call fit() first."

        output = ["=" * 70]
        output.append("Two-Stage Least Squares (2SLS) Results")
        output.append("=" * 70)
        output.append(f"Number of observations: {self.n}")
        output.append(f"Number of instruments: {self.Z.shape[1]}")
        output.append("")
        output.append("First Stage Diagnostics:")
        output.append(f"  F-statistic: {self.results.first_stage_f:.3f}")
        output.append(f"  R-squared: {self.results.first_stage_r2:.3f}")

        if self.results.first_stage_f < 10:
            output.append("  WARNING: Weak instruments (F < 10)!")

        output.append("")
        output.append("Second Stage Results:")
        output.append("-" * 70)
        output.append(f"{'Variable':<20} {'Coefficient':>12} {'Std. Error':>12} {'t-stat':>10} {'p-value':>10}")
        output.append("-" * 70)

        var_names = ['Intercept'] + \
                   ([f'Control_{i+1}' for i in range(self.X.shape[1])] if self.X is not None else []) + \
                   ['Treatment']

        for i, (name, coef, se) in enumerate(zip(var_names, self.results.beta_iv.flatten(),
                                                   self.results.se_iv)):
            t_stat = coef / se
            p_value = 2 * (1 - stats.t.cdf(abs(t_stat), self.n - len(var_names)))
            output.append(f"{name:<20} {coef:>12.4f} {se:>12.4f} {t_stat:>10.3f} {p_value:>10.4f}")

        if self.results.sargan_stat is not None:
            output.append("")
            output.append("Overidentification Test (Sargan):")
            output.append(f"  Chi-square statistic: {self.results.sargan_stat:.3f}")
            output.append(f"  p-value: {self.results.sargan_pvalue:.4f}")

        output.append("=" * 70)

        return "\n".join(output)


def simulate_iv_data(n: int = 1000, instrument_strength: float = 0.5,
                     confounding: float = 0.3) -> pd.DataFrame:
    """
    Simulate data for IV example.

    Parameters
    ----------
    n : int
        Sample size
    instrument_strength : float
        Strength of instrument-treatment relationship
    confounding : float
        Degree of confounding

    Returns
    -------
    pd.DataFrame
        Simulated data
    """
    np.random.seed(42)

    # Confounder (unobserved)
    U = np.random.normal(0, 1, n)

    # Instrument (e.g., randomized encouragement)
    Z = np.random.binomial(1, 0.5, n)

    # Treatment (endogenous because of U)
    D = instrument_strength * Z + confounding * U + np.random.normal(0, 0.5, n)

    # Outcome
    true_effect = 1.5
    Y = true_effect * D + confounding * U + np.random.normal(0, 1, n)

    return pd.DataFrame({'Y': Y, 'D': D, 'Z': Z, 'U': U})


def example_returns_to_schooling():
    """
    Example: Returns to schooling using quarter of birth as instrument.

    This replicates the Angrist & Krueger (1991) approach.
    """
    print("Example: Returns to Schooling (Simulated)")
    print("=" * 70)

    # Simulate data
    n = 5000
    np.random.seed(123)

    # Quarter of birth (instrument)
    quarter = np.random.randint(1, 5, n)
    Z = (quarter == 1).astype(int)  # Born in Q1

    # Unobserved ability
    ability = np.random.normal(0, 1, n)

    # Years of education (endogenous)
    education = 12 + 0.3 * Z - 0.4 * ability + np.random.normal(0, 2, n)

    # Log earnings
    true_return = 0.08  # 8% return per year of education
    log_earnings = 2.0 + true_return * education + 0.3 * ability + np.random.normal(0, 0.5, n)

    # OLS (biased due to ability confounding)
    from sklearn.linear_model import LinearRegression
    ols = LinearRegression()
    ols.fit(education.reshape(-1, 1), log_earnings)
    ols_coef = ols.coef_[0]

    print(f"OLS estimate: {ols_coef:.4f}")
    print(f"True effect: {true_return:.4f}")
    print(f"OLS bias: {ols_coef - true_return:.4f}")
    print()

    # IV estimation
    iv = InstrumentalVariables(Y=log_earnings, D=education, Z=Z)
    results = iv.fit()
    print(iv.summary())

    # Visualize first stage
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # First stage
    df_plot = pd.DataFrame({'Education': education, 'Quarter_1': Z})
    df_plot.groupby('Quarter_1')['Education'].mean().plot(kind='bar', ax=axes[0])
    axes[0].set_xlabel('Born in Q1')
    axes[0].set_ylabel('Average Years of Education')
    axes[0].set_title('First Stage: Instrument → Treatment')
    axes[0].set_xticklabels(['No', 'Yes'], rotation=0)

    # Reduced form
    df_plot['Earnings'] = log_earnings
    df_plot.groupby('Quarter_1')['Earnings'].mean().plot(kind='bar', ax=axes[1])
    axes[1].set_xlabel('Born in Q1')
    axes[1].set_ylabel('Average Log Earnings')
    axes[1].set_title('Reduced Form: Instrument → Outcome')
    axes[1].set_xticklabels(['No', 'Yes'], rotation=0)

    plt.tight_layout()
    plt.savefig('iv_schooling_example.png', dpi=150, bbox_inches='tight')
    plt.show()


def example_weak_instruments():
    """Demonstrate the weak instruments problem."""
    print("\nExample: Weak Instruments Problem")
    print("=" * 70)

    # Simulate with weak instrument
    df_weak = simulate_iv_data(n=1000, instrument_strength=0.1, confounding=0.5)

    iv_weak = InstrumentalVariables(Y=df_weak['Y'].values,
                                    D=df_weak['D'].values,
                                    Z=df_weak['Z'].values)
    results_weak = iv_weak.fit()

    print("WEAK INSTRUMENT:")
    print(iv_weak.summary())

    # Simulate with strong instrument
    df_strong = simulate_iv_data(n=1000, instrument_strength=0.8, confounding=0.5)

    iv_strong = InstrumentalVariables(Y=df_strong['Y'].values,
                                      D=df_strong['D'].values,
                                      Z=df_strong['Z'].values)
    results_strong = iv_strong.fit()

    print("\nSTRONG INSTRUMENT:")
    print(iv_strong.summary())


if __name__ == "__main__":
    example_returns_to_schooling()
    example_weak_instruments()
