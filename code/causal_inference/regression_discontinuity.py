"""
Regression Discontinuity Design (RDD)
======================================

Implementation of sharp and fuzzy RDD with various estimation methods.

References:
    Imbens & Lemieux (2008), Lee & Lemieux (2010), Calonico et al. (2014)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from typing import Tuple, Optional
from dataclasses import dataclass

sns.set_style("whitegrid")


@dataclass
class RDDResults:
    """Results from RDD estimation."""
    treatment_effect: float
    standard_error: float
    ci_lower: float
    ci_upper: float
    bandwidth: float
    n_left: int
    n_right: int


class RegressionDiscontinuity:
    """
    Regression Discontinuity Design estimator.

    Parameters
    ----------
    running_var : array-like
        Running variable (forcing variable)
    outcome : array-like
        Outcome variable
    treatment : array-like, optional
        Treatment indicator (for fuzzy RDD)
    cutoff : float
        Cutoff value for treatment assignment
    """

    def __init__(self, running_var: np.ndarray, outcome: np.ndarray,
                 treatment: Optional[np.ndarray] = None, cutoff: float = 0.0):
        self.running_var = np.asarray(running_var)
        self.outcome = np.asarray(outcome)
        self.treatment = treatment if treatment is None else np.asarray(treatment)
        self.cutoff = cutoff
        self.n = len(running_var)

        # Center running variable at cutoff
        self.x_centered = self.running_var - self.cutoff

    def imbens_kalyanaraman_bandwidth(self) -> float:
        """
        Calculate optimal bandwidth using Imbens-Kalyanaraman method.

        Returns
        -------
        float
            Optimal bandwidth
        """
        # Pilot bandwidth using rule of thumb
        h_pilot = 1.84 * np.std(self.x_centered) * self.n ** (-1/5)

        # Estimate derivatives on both sides
        mask_left = (self.x_centered < 0) & (abs(self.x_centered) < h_pilot)
        mask_right = (self.x_centered >= 0) & (abs(self.x_centered) < h_pilot)

        # Fit cubic polynomials
        poly = PolynomialFeatures(degree=3)

        # Left side
        if mask_left.sum() > 10:
            X_left = poly.fit_transform(self.x_centered[mask_left].reshape(-1, 1))
            y_left = self.outcome[mask_left]
            model_left = LinearRegression().fit(X_left, y_left)
            m2_left = 2 * model_left.coef_[2]  # Second derivative
        else:
            m2_left = 0

        # Right side
        if mask_right.sum() > 10:
            X_right = poly.fit_transform(self.x_centered[mask_right].reshape(-1, 1))
            y_right = self.outcome[mask_right]
            model_right = LinearRegression().fit(X_right, y_right)
            m2_right = 2 * model_right.coef_[2]
        else:
            m2_right = 0

        # Estimate variance
        sigma2_left = np.var(y_left) if mask_left.sum() > 0 else 1
        sigma2_right = np.var(y_right) if mask_right.sum() > 0 else 1

        # IK bandwidth formula
        N = self.n
        C_k = 3.4375  # Constant for rectangular kernel
        m2 = abs(m2_left) + abs(m2_right)

        if m2 > 0:
            h_ik = C_k * (sigma2_left + sigma2_right) / (N * m2**2)
            h_ik = h_ik ** (1/5)
        else:
            h_ik = h_pilot

        return h_ik

    def local_linear_regression(self, bandwidth: float, polynomial_order: int = 1) -> RDDResults:
        """
        Estimate treatment effect using local linear regression.

        Parameters
        ----------
        bandwidth : float
            Bandwidth for local regression
        polynomial_order : int
            Order of polynomial (1 for local linear, 2 for local quadratic)

        Returns
        -------
        RDDResults
            Estimation results
        """
        # Select observations within bandwidth
        mask = abs(self.x_centered) <= bandwidth
        x_local = self.x_centered[mask]
        y_local = self.outcome[mask]

        # Create treatment indicator
        treated = (x_local >= 0).astype(float)

        # Create polynomial features
        poly = PolynomialFeatures(degree=polynomial_order, include_bias=False)
        x_poly = poly.fit_transform(x_local.reshape(-1, 1))

        # Interaction terms: treatment * polynomial features
        X = np.column_stack([
            np.ones(len(x_local)),  # Intercept
            treated,  # Treatment indicator
            x_poly,  # Polynomial of running variable
            treated.reshape(-1, 1) * x_poly  # Interactions
        ])

        # Triangular kernel weights
        weights = (1 - abs(x_local / bandwidth)) * mask[mask]

        # Weighted least squares
        W = np.diag(weights)
        X_weighted = np.sqrt(W) @ X
        y_weighted = np.sqrt(W) @ y_local

        # Estimate
        beta = np.linalg.lstsq(X_weighted, y_weighted, rcond=None)[0]
        treatment_effect = beta[1]

        # Standard error (heteroskedasticity-robust)
        residuals = y_local - X @ beta
        meat = X.T @ (W * (residuals**2)[:, np.newaxis] * X)
        bread_inv = np.linalg.inv(X.T @ W @ X)
        var_beta = bread_inv @ meat @ bread_inv
        se = np.sqrt(var_beta[1, 1])

        # Confidence interval
        ci_lower = treatment_effect - 1.96 * se
        ci_upper = treatment_effect + 1.96 * se

        n_left = (x_local < 0).sum()
        n_right = (x_local >= 0).sum()

        return RDDResults(
            treatment_effect=treatment_effect,
            standard_error=se,
            ci_lower=ci_lower,
            ci_upper=ci_upper,
            bandwidth=bandwidth,
            n_left=n_left,
            n_right=n_right
        )

    def estimate(self, bandwidth: Optional[float] = None,
                 polynomial_order: int = 1) -> RDDResults:
        """
        Estimate RDD effect.

        Parameters
        ----------
        bandwidth : float, optional
            Bandwidth (if None, uses Imbens-Kalyanaraman)
        polynomial_order : int
            Polynomial order for local regression

        Returns
        -------
        RDDResults
            Estimation results
        """
        if bandwidth is None:
            bandwidth = self.imbens_kalyanaraman_bandwidth()
            print(f"Using IK bandwidth: {bandwidth:.3f}")

        return self.local_linear_regression(bandwidth, polynomial_order)

    def plot_rdd(self, results: RDDResults, bins: int = 20):
        """
        Create RDD visualization.

        Parameters
        ----------
        results : RDDResults
            Estimation results
        bins : int
            Number of bins for binned scatter plot
        """
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        # Left panel: Binned scatter plot
        ax = axes[0]

        # Create bins
        bins_left = pd.cut(self.x_centered[self.x_centered < 0], bins=bins//2)
        bins_right = pd.cut(self.x_centered[self.x_centered >= 0], bins=bins//2)

        # Calculate bin means
        df_left = pd.DataFrame({'x': self.x_centered[self.x_centered < 0],
                               'y': self.outcome[self.x_centered < 0],
                               'bin': bins_left})
        df_right = pd.DataFrame({'x': self.x_centered[self.x_centered >= 0],
                                'y': self.outcome[self.x_centered >= 0],
                                'bin': bins_right})

        bin_means_left = df_left.groupby('bin')[['x', 'y']].mean()
        bin_means_right = df_right.groupby('bin')[['x', 'y']].mean()

        # Plot binned means
        ax.scatter(bin_means_left['x'], bin_means_left['y'],
                  color='blue', s=50, alpha=0.6, label='Control')
        ax.scatter(bin_means_right['x'], bin_means_right['y'],
                  color='red', s=50, alpha=0.6, label='Treatment')

        # Fit lines within bandwidth
        mask_left = (self.x_centered < 0) & (abs(self.x_centered) <= results.bandwidth)
        mask_right = (self.x_centered >= 0) & (abs(self.x_centered) <= results.bandwidth)

        # Left polynomial
        if mask_left.sum() > 0:
            x_plot_left = np.linspace(self.x_centered[mask_left].min(), 0, 100)
            poly_left = np.polyfit(self.x_centered[mask_left], self.outcome[mask_left], 1)
            y_plot_left = np.polyval(poly_left, x_plot_left)
            ax.plot(x_plot_left, y_plot_left, 'b-', linewidth=2, label='Fit (Control)')

        # Right polynomial
        if mask_right.sum() > 0:
            x_plot_right = np.linspace(0, self.x_centered[mask_right].max(), 100)
            poly_right = np.polyfit(self.x_centered[mask_right], self.outcome[mask_right], 1)
            y_plot_right = np.polyval(poly_right, x_plot_right)
            ax.plot(x_plot_right, y_plot_right, 'r-', linewidth=2, label='Fit (Treatment)')

        # Vertical line at cutoff
        ax.axvline(x=0, color='black', linestyle='--', linewidth=1.5, alpha=0.7)

        ax.set_xlabel('Running Variable (centered at cutoff)')
        ax.set_ylabel('Outcome')
        ax.set_title(f'RDD Plot (Bandwidth = {results.bandwidth:.3f})')
        ax.legend()

        # Right panel: Density of running variable (continuity check)
        ax = axes[1]
        ax.hist(self.x_centered[self.x_centered < 0], bins=30, alpha=0.5,
               label='Control', density=True, color='blue')
        ax.hist(self.x_centered[self.x_centered >= 0], bins=30, alpha=0.5,
               label='Treatment', density=True, color='red')
        ax.axvline(x=0, color='black', linestyle='--', linewidth=1.5, alpha=0.7)
        ax.set_xlabel('Running Variable (centered at cutoff)')
        ax.set_ylabel('Density')
        ax.set_title('Density of Running Variable\n(Continuity Check)')
        ax.legend()

        plt.tight_layout()
        return fig


def simulate_rdd_data(n: int = 1000, effect: float = 5.0,
                     polynomial_order: int = 2) -> pd.DataFrame:
    """
    Simulate RDD data.

    Parameters
    ----------
    n : int
        Sample size
    effect : float
        True treatment effect
    polynomial_order : int
        Polynomial order for baseline relationship

    Returns
    -------
    pd.DataFrame
        Simulated data
    """
    np.random.seed(42)

    # Running variable
    x = np.random.uniform(-2, 2, n)

    # Treatment assignment (sharp RDD)
    D = (x >= 0).astype(float)

    # Outcome with polynomial trend
    y_baseline = 10 + 2*x + 0.5*x**2
    if polynomial_order >= 3:
        y_baseline += 0.1*x**3

    # Add treatment effect
    y = y_baseline + effect * D + np.random.normal(0, 1, n)

    return pd.DataFrame({'x': x, 'y': y, 'D': D})


def example_education_rdd():
    """
    Example: Effect of remedial education program.

    Students below cutoff score are assigned to remedial program.
    """
    print("Example: Remedial Education Program RDD")
    print("=" * 70)

    # Simulate data
    np.random.seed(456)
    n = 2000

    # Test score (running variable, centered at cutoff of 50)
    test_score = np.random.normal(50, 15, n)
    x_centered = test_score - 50

    # Treatment: remedial program if score < 50
    treatment = (test_score < 50).astype(float)

    # Outcome: next year's test score
    # Baseline relationship + treatment effect
    true_effect = 8.0
    next_score = 55 + 0.5*x_centered + 0.02*x_centered**2 + \
                 true_effect * treatment + np.random.normal(0, 5, n)

    # Estimate RDD
    rdd = RegressionDiscontinuity(running_var=test_score, outcome=next_score, cutoff=50)
    results = rdd.estimate()

    print(f"Estimated treatment effect: {results.treatment_effect:.3f}")
    print(f"Standard error: {results.standard_error:.3f}")
    print(f"95% CI: [{results.ci_lower:.3f}, {results.ci_upper:.3f}]")
    print(f"True effect: {true_effect:.3f}")
    print(f"Bandwidth: {results.bandwidth:.3f}")
    print(f"N (control): {results.n_left}")
    print(f"N (treatment): {results.n_right}")

    # Plot
    fig = rdd.plot_rdd(results)
    plt.savefig('rdd_education_example.png', dpi=150, bbox_inches='tight')
    plt.show()


def example_bandwidth_sensitivity():
    """Test sensitivity to bandwidth choice."""
    print("\n" + "=" * 70)
    print("Bandwidth Sensitivity Analysis")
    print("=" * 70)

    # Simulate data
    df = simulate_rdd_data(n=1500, effect=5.0)

    rdd = RegressionDiscontinuity(running_var=df['x'].values,
                                  outcome=df['y'].values,
                                  cutoff=0)

    # Try different bandwidths
    bandwidths = np.linspace(0.3, 2.0, 20)
    effects = []
    ci_lower = []
    ci_upper = []

    for bw in bandwidths:
        results = rdd.local_linear_regression(bandwidth=bw)
        effects.append(results.treatment_effect)
        ci_lower.append(results.ci_lower)
        ci_upper.append(results.ci_upper)

    # Plot sensitivity
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(bandwidths, effects, 'o-', linewidth=2, markersize=6, label='Point estimate')
    ax.fill_between(bandwidths, ci_lower, ci_upper, alpha=0.3, label='95% CI')
    ax.axhline(y=5.0, color='red', linestyle='--', linewidth=2, label='True effect')
    ax.set_xlabel('Bandwidth')
    ax.set_ylabel('Estimated Treatment Effect')
    ax.set_title('RDD Sensitivity to Bandwidth Choice')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('rdd_bandwidth_sensitivity.png', dpi=150, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    example_education_rdd()
    example_bandwidth_sensitivity()
