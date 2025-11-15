"""
Difference-in-Differences (DiD)
================================

Implementation of DiD estimation with various extensions.

References:
    Card & Krueger (1994), Bertrand et al. (2004), Abadie (2005)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from typing import Tuple, Optional, List
from dataclasses import dataclass

sns.set_style("whitegrid")


@dataclass
class DiDResults:
    """Results from DiD estimation."""
    att: float  # Average treatment effect on the treated
    se: float
    ci_lower: float
    ci_upper: float
    n_treat: int
    n_control: int
    parallel_trends_pvalue: Optional[float] = None


class DifferenceInDifferences:
    """
    Difference-in-Differences estimator.

    Parameters
    ----------
    data : pd.DataFrame
        Panel data with columns: unit_id, time_period, outcome, treated
    outcome_col : str
        Name of outcome variable
    treated_col : str
        Name of treatment indicator
    time_col : str
        Name of time period variable
    unit_col : str
        Name of unit identifier
    """

    def __init__(self, data: pd.DataFrame, outcome_col: str = 'outcome',
                 treated_col: str = 'treated', time_col: str = 'post',
                 unit_col: str = 'unit_id'):
        self.data = data.copy()
        self.outcome_col = outcome_col
        self.treated_col = treated_col
        self.time_col = time_col
        self.unit_col = unit_col

    def estimate_2x2(self, cluster_se: bool = True) -> DiDResults:
        """
        Estimate 2x2 DiD (two time periods, two groups).

        Parameters
        ----------
        cluster_se : bool
            Use cluster-robust standard errors

        Returns
        -------
        DiDResults
            Estimation results
        """
        df = self.data

        # Calculate group-time means
        means = df.groupby([self.treated_col, self.time_col])[self.outcome_col].mean()

        # DiD estimator
        Y_11 = means.loc[(1, 1)]  # Treated, post
        Y_10 = means.loc[(1, 0)]  # Treated, pre
        Y_01 = means.loc[(0, 1)]  # Control, post
        Y_00 = means.loc[(0, 0)]  # Control, pre

        att = (Y_11 - Y_10) - (Y_01 - Y_00)

        # Regression approach for standard errors
        df['treat_post'] = df[self.treated_col] * df[self.time_col]

        # OLS: Y = β0 + β1*Treat + β2*Post + β3*Treat*Post + ε
        X = df[[self.treated_col, self.time_col, 'treat_post']].values
        X_with_const = np.column_stack([np.ones(len(df)), X])
        y = df[self.outcome_col].values

        beta = np.linalg.lstsq(X_with_const, y, rcond=None)[0]
        att_reg = beta[3]  # Interaction coefficient

        # Standard errors
        residuals = y - X_with_const @ beta

        if cluster_se:
            # Cluster-robust standard errors at unit level
            clusters = df[self.unit_col].values
            unique_clusters = np.unique(clusters)
            n_clusters = len(unique_clusters)

            # Calculate clustered variance
            meat = np.zeros((X_with_const.shape[1], X_with_const.shape[1]))
            for cluster in unique_clusters:
                idx = clusters == cluster
                X_cluster = X_with_const[idx]
                resid_cluster = residuals[idx]
                meat += np.outer(X_cluster.T @ resid_cluster, X_cluster.T @ resid_cluster)

            bread_inv = np.linalg.inv(X_with_const.T @ X_with_const / len(df))
            var_beta = bread_inv @ meat @ bread_inv * n_clusters / (n_clusters - 1)
        else:
            # Heteroskedasticity-robust standard errors
            meat = X_with_const.T @ (residuals[:, np.newaxis]**2 * X_with_const)
            bread_inv = np.linalg.inv(X_with_const.T @ X_with_const)
            var_beta = bread_inv @ meat @ bread_inv

        se = np.sqrt(var_beta[3, 3])

        # Confidence interval
        ci_lower = att - 1.96 * se
        ci_upper = att + 1.96 * se

        n_treat = df[df[self.treated_col] == 1][self.unit_col].nunique()
        n_control = df[df[self.treated_col] == 0][self.unit_col].nunique()

        return DiDResults(
            att=att,
            se=se,
            ci_lower=ci_lower,
            ci_upper=ci_upper,
            n_treat=n_treat,
            n_control=n_control
        )

    def test_parallel_trends(self, pre_periods: List[int]) -> float:
        """
        Test parallel trends assumption using pre-treatment periods.

        Parameters
        ----------
        pre_periods : list
            List of pre-treatment time periods

        Returns
        -------
        float
            p-value for parallel trends test
        """
        df_pre = self.data[self.data[self.time_col].isin(pre_periods)]

        # Regress outcome on time trends separately for treated and control
        results_treat = []
        results_control = []

        for period in pre_periods:
            treat_mean = df_pre[(df_pre[self.time_col] == period) &
                               (df_pre[self.treated_col] == 1)][self.outcome_col].mean()
            control_mean = df_pre[(df_pre[self.time_col] == period) &
                                 (df_pre[self.treated_col] == 0)][self.outcome_col].mean()
            results_treat.append(treat_mean)
            results_control.append(control_mean)

        # Test if trends are parallel (interaction of time with treatment)
        n_periods = len(pre_periods)
        X = np.column_stack([
            np.ones(n_periods * 2),
            np.repeat([0, 1], n_periods),  # Treatment indicator
            np.tile(pre_periods, 2),  # Time
            np.repeat([0, 1], n_periods) * np.tile(pre_periods, 2)  # Interaction
        ])

        y = np.concatenate([results_control, results_treat])

        beta = np.linalg.lstsq(X, y, rcond=None)[0]
        residuals = y - X @ beta

        # F-test for interaction coefficient
        sigma2 = np.sum(residuals**2) / (len(y) - X.shape[1])
        var_beta = sigma2 * np.linalg.inv(X.T @ X)
        t_stat = beta[3] / np.sqrt(var_beta[3, 3])
        p_value = 2 * (1 - stats.t.cdf(abs(t_stat), len(y) - X.shape[1]))

        return p_value

    def event_study(self, time_periods: List[int], base_period: int = -1) -> pd.DataFrame:
        """
        Estimate event study (dynamic DiD).

        Parameters
        ----------
        time_periods : list
            List of time periods relative to treatment
        base_period : int
            Base period (normalized to 0)

        Returns
        -------
        pd.DataFrame
            Event study coefficients
        """
        df = self.data.copy()

        # Create period indicators
        estimates = []

        for t in time_periods:
            if t == base_period:
                # Normalized period
                estimates.append({'period': t, 'coef': 0, 'se': 0, 'ci_lower': 0, 'ci_upper': 0})
                continue

            # Interaction between treatment and period indicator
            df[f'period_{t}'] = (df[self.time_col] == t).astype(int)
            df[f'treat_period_{t}'] = df[self.treated_col] * df[f'period_{t}']

            # Run regression
            period_cols = [c for c in df.columns if c.startswith('period_') or c.startswith('treat_period_')]
            X = df[[self.treated_col] + period_cols].values
            X_with_const = np.column_stack([np.ones(len(df)), X])
            y = df[self.outcome_col].values

            beta = np.linalg.lstsq(X_with_const, y, rcond=None)[0]

            # Find coefficient for this period's interaction
            col_idx = period_cols.index(f'treat_period_{t}') + 1 + 1  # +1 for const, +1 for treated main effect
            coef = beta[col_idx]

            # Standard error (simplified)
            residuals = y - X_with_const @ beta
            sigma2 = np.sum(residuals**2) / (len(y) - X_with_const.shape[1])
            var_beta = sigma2 * np.linalg.inv(X_with_const.T @ X_with_const)
            se = np.sqrt(var_beta[col_idx, col_idx])

            ci_lower = coef - 1.96 * se
            ci_upper = coef + 1.96 * se

            estimates.append({'period': t, 'coef': coef, 'se': se,
                            'ci_lower': ci_lower, 'ci_upper': ci_upper})

        return pd.DataFrame(estimates)

    def plot_did(self, results: DiDResults):
        """
        Visualize DiD design.

        Parameters
        ----------
        results : DiDResults
            Estimation results
        """
        df = self.data

        # Calculate group-time means
        means = df.groupby([self.treated_col, self.time_col])[self.outcome_col].mean().unstack()

        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        # Left panel: Parallel trends plot
        ax = axes[0]
        time_points = means.columns
        ax.plot(time_points, means.loc[0], 'o-', linewidth=2, markersize=8,
               label='Control', color='blue')
        ax.plot(time_points, means.loc[1], 's-', linewidth=2, markersize=8,
               label='Treated', color='red')

        # Counterfactual (parallel trends)
        if len(time_points) == 2:
            control_change = means.loc[0, time_points[1]] - means.loc[0, time_points[0]]
            counterfactual = means.loc[1, time_points[0]] + control_change
            ax.plot([time_points[0], time_points[1]],
                   [means.loc[1, time_points[0]], counterfactual],
                   '--', linewidth=2, color='red', alpha=0.5,
                   label='Counterfactual (Treated)')

            # Show treatment effect
            ax.annotate('', xy=(time_points[1], means.loc[1, time_points[1]]),
                       xytext=(time_points[1], counterfactual),
                       arrowprops=dict(arrowstyle='<->', color='green', lw=2))
            mid_y = (means.loc[1, time_points[1]] + counterfactual) / 2
            ax.text(time_points[1] + 0.05, mid_y, f'ATT={results.att:.2f}',
                   fontsize=12, color='green')

        ax.set_xlabel('Time Period')
        ax.set_ylabel('Outcome')
        ax.set_title('Difference-in-Differences')
        ax.legend()
        ax.grid(True, alpha=0.3)

        # Right panel: Distribution of treatment effects
        ax = axes[1]

        # Individual-level treatment effects (for visualization)
        df_pre = df[df[self.time_col] == 0]
        df_post = df[df[self.time_col] == 1]

        df_merged = df_pre.merge(df_post, on=self.unit_col, suffixes=('_pre', '_post'))
        df_merged['diff'] = df_merged[f'{self.outcome_col}_post'] - df_merged[f'{self.outcome_col}_pre']

        treat_diffs = df_merged[df_merged[f'{self.treated_col}_post'] == 1]['diff']
        control_diffs = df_merged[df_merged[f'{self.treated_col}_post'] == 0]['diff']

        ax.hist(control_diffs, bins=20, alpha=0.5, label='Control', density=True, color='blue')
        ax.hist(treat_diffs, bins=20, alpha=0.5, label='Treated', density=True, color='red')
        ax.axvline(x=control_diffs.mean(), color='blue', linestyle='--', linewidth=2)
        ax.axvline(x=treat_diffs.mean(), color='red', linestyle='--', linewidth=2)
        ax.set_xlabel('Change in Outcome')
        ax.set_ylabel('Density')
        ax.set_title('Distribution of Changes')
        ax.legend()

        plt.tight_layout()
        return fig


def simulate_did_data(n_units: int = 500, n_periods: int = 2,
                     treatment_effect: float = 5.0) -> pd.DataFrame:
    """
    Simulate panel data for DiD.

    Parameters
    ----------
    n_units : int
        Number of units
    n_periods : int
        Number of time periods
    treatment_effect : float
        True ATT

    Returns
    -------
    pd.DataFrame
        Simulated panel data
    """
    np.random.seed(42)

    # Unit fixed effects
    unit_fe = np.random.normal(10, 2, n_units)

    # Treatment assignment (some units treated)
    treated = np.random.binomial(1, 0.5, n_units)

    # Create panel
    data = []
    for t in range(n_periods):
        post = int(t >= n_periods // 2)

        for i in range(n_units):
            # Outcome with unit FE, time trend, and treatment effect
            y = (unit_fe[i] +
                 3 * t +  # Common time trend
                 treatment_effect * treated[i] * post +  # Treatment effect
                 np.random.normal(0, 1))

            data.append({
                'unit_id': i,
                'time': t,
                'post': post,
                'treated': treated[i],
                'outcome': y
            })

    return pd.DataFrame(data)


def example_minimum_wage():
    """
    Example: Minimum wage effect on employment (Card & Krueger style).
    """
    print("Example: Minimum Wage and Employment")
    print("=" * 70)

    # Simulate data
    np.random.seed(789)
    n = 400

    # New Jersey (treated) vs Pennsylvania (control)
    state = np.random.choice(['NJ', 'PA'], n, p=[0.5, 0.5])
    treated = (state == 'NJ').astype(int)

    # Create panel data (before and after minimum wage increase)
    data = []
    for period, post in [(0, 0), (1, 1)]:
        for i in range(n):
            # Employment (FTE employees)
            baseline = 20 + np.random.normal(0, 5)
            time_effect = 2 * post
            treatment_effect = 3.0 * treated[i] * post  # Positive effect (contrary to theory!)

            employment = baseline + time_effect + treatment_effect + np.random.normal(0, 2)

            data.append({
                'unit_id': i,
                'state': state[i],
                'time': period,
                'post': post,
                'treated': treated[i],
                'outcome': employment
            })

    df = pd.DataFrame(data)

    # Estimate DiD
    did = DifferenceInDifferences(df)
    results = did.estimate_2x2(cluster_se=True)

    print(f"Estimated ATT: {results.att:.3f}")
    print(f"Standard error: {results.se:.3f}")
    print(f"95% CI: [{results.ci_lower:.3f}, {results.ci_upper:.3f}]")
    print(f"N (treated): {results.n_treat}")
    print(f"N (control): {results.n_control}")

    # Plot
    fig = did.plot_did(results)
    plt.savefig('did_minimum_wage.png', dpi=150, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    example_minimum_wage()
