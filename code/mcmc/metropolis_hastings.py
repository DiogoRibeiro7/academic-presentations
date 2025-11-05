"""
Metropolis-Hastings MCMC Implementation
========================================

This module implements the Metropolis-Hastings algorithm for sampling from
arbitrary probability distributions.

References:
    Metropolis et al. (1953), Hastings (1970)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from typing import Callable, Tuple, Optional
import seaborn as sns

sns.set_style("whitegrid")


class MetropolisHastings:
    """
    Metropolis-Hastings MCMC sampler.

    Parameters
    ----------
    target_log_density : callable
        Log of the target density function (up to a normalizing constant)
    proposal_std : float
        Standard deviation for the Gaussian random walk proposal
    """

    def __init__(self, target_log_density: Callable, proposal_std: float = 1.0):
        self.target_log_density = target_log_density
        self.proposal_std = proposal_std
        self.samples = None
        self.acceptance_rate = None

    def propose(self, current_state: np.ndarray) -> np.ndarray:
        """
        Generate proposal using Gaussian random walk.

        Parameters
        ----------
        current_state : np.ndarray
            Current state of the chain

        Returns
        -------
        np.ndarray
            Proposed next state
        """
        return current_state + np.random.normal(0, self.proposal_std,
                                                 size=current_state.shape)

    def acceptance_probability(self, current_state: np.ndarray,
                               proposed_state: np.ndarray) -> float:
        """
        Calculate Metropolis-Hastings acceptance probability.

        For symmetric proposals, this simplifies to min(1, π(x')/π(x))

        Parameters
        ----------
        current_state : np.ndarray
            Current state
        proposed_state : np.ndarray
            Proposed state

        Returns
        -------
        float
            Acceptance probability
        """
        log_ratio = (self.target_log_density(proposed_state) -
                     self.target_log_density(current_state))
        return min(1.0, np.exp(log_ratio))

    def sample(self, n_samples: int, initial_state: np.ndarray,
               burn_in: int = 1000, thin: int = 1) -> np.ndarray:
        """
        Run the Metropolis-Hastings algorithm.

        Parameters
        ----------
        n_samples : int
            Number of samples to generate (after burn-in and thinning)
        initial_state : np.ndarray
            Initial state of the chain
        burn_in : int, optional
            Number of initial samples to discard
        thin : int, optional
            Thinning interval (keep every thin-th sample)

        Returns
        -------
        np.ndarray
            Array of samples (n_samples, dim)
        """
        dim = len(initial_state)
        total_iterations = burn_in + n_samples * thin

        # Storage for all samples (including burn-in)
        all_samples = np.zeros((total_iterations, dim))
        all_samples[0] = initial_state

        accepted = 0

        for i in range(1, total_iterations):
            current = all_samples[i-1]
            proposed = self.propose(current)

            # Metropolis-Hastings acceptance step
            alpha = self.acceptance_probability(current, proposed)

            if np.random.uniform() < alpha:
                all_samples[i] = proposed
                accepted += 1
            else:
                all_samples[i] = current

        # Calculate acceptance rate
        self.acceptance_rate = accepted / total_iterations

        # Discard burn-in and apply thinning
        self.samples = all_samples[burn_in::thin]

        return self.samples

    def plot_diagnostics(self, true_density: Optional[Callable] = None,
                        dim_to_plot: int = 0):
        """
        Plot diagnostic plots for MCMC convergence.

        Parameters
        ----------
        true_density : callable, optional
            True density function for comparison
        dim_to_plot : int
            Which dimension to plot (for multivariate case)
        """
        if self.samples is None:
            raise ValueError("No samples available. Run sample() first.")

        fig, axes = plt.subplots(2, 2, figsize=(12, 10))

        # Trace plot
        axes[0, 0].plot(self.samples[:, dim_to_plot], alpha=0.7)
        axes[0, 0].set_xlabel('Iteration')
        axes[0, 0].set_ylabel(f'Value (dim {dim_to_plot})')
        axes[0, 0].set_title('Trace Plot')

        # Histogram with true density overlay
        axes[0, 1].hist(self.samples[:, dim_to_plot], bins=50, density=True,
                       alpha=0.7, label='MCMC samples')
        if true_density is not None:
            x_range = np.linspace(self.samples[:, dim_to_plot].min(),
                                 self.samples[:, dim_to_plot].max(), 1000)
            axes[0, 1].plot(x_range, true_density(x_range), 'r-',
                          linewidth=2, label='True density')
        axes[0, 1].set_xlabel(f'Value (dim {dim_to_plot})')
        axes[0, 1].set_ylabel('Density')
        axes[0, 1].set_title('Marginal Distribution')
        axes[0, 1].legend()

        # Autocorrelation plot
        from statsmodels.graphics.tsaplots import plot_acf
        plot_acf(self.samples[:, dim_to_plot], lags=50, ax=axes[1, 0])
        axes[1, 0].set_title('Autocorrelation Function')

        # Running mean
        running_mean = np.cumsum(self.samples[:, dim_to_plot]) / np.arange(1, len(self.samples) + 1)
        axes[1, 1].plot(running_mean)
        axes[1, 1].set_xlabel('Iteration')
        axes[1, 1].set_ylabel('Running Mean')
        axes[1, 1].set_title('Running Mean Convergence')

        plt.tight_layout()
        plt.suptitle(f'MCMC Diagnostics (Acceptance Rate: {self.acceptance_rate:.2%})',
                     y=1.02, fontsize=14)
        return fig


# Example usage and demonstrations

def example_1d_gaussian():
    """Example: Sampling from a 1D Gaussian distribution."""
    print("Example 1: Sampling from N(3, 2^2)")

    # Target: N(3, 4)
    target_mean = 3.0
    target_std = 2.0

    def log_density(x):
        return -0.5 * ((x - target_mean) / target_std) ** 2

    # Run Metropolis-Hastings
    mh = MetropolisHastings(log_density, proposal_std=2.5)
    samples = mh.sample(n_samples=5000, initial_state=np.array([0.0]),
                       burn_in=1000)

    print(f"Sample mean: {samples.mean():.3f} (true: {target_mean})")
    print(f"Sample std: {samples.std():.3f} (true: {target_std})")
    print(f"Acceptance rate: {mh.acceptance_rate:.2%}")

    # Plot diagnostics
    true_density = lambda x: stats.norm.pdf(x, target_mean, target_std)
    mh.plot_diagnostics(true_density)
    plt.savefig('mh_gaussian_diagnostics.png', dpi=150, bbox_inches='tight')
    plt.show()


def example_2d_banana():
    """Example: Sampling from a 2D banana-shaped distribution."""
    print("\nExample 2: Sampling from 2D Banana distribution")

    # Rosenbrock's banana-shaped density
    def log_density(x):
        if len(x.shape) == 1:
            x1, x2 = x[0], x[1]
        else:
            x1, x2 = x[:, 0], x[:, 1]
        return -0.5 * (x1**2 / 100 + (x2 - x1**2)**2)

    # Run Metropolis-Hastings
    mh = MetropolisHastings(log_density, proposal_std=5.0)
    samples = mh.sample(n_samples=10000, initial_state=np.array([0.0, 0.0]),
                       burn_in=2000)

    print(f"Acceptance rate: {mh.acceptance_rate:.2%}")

    # Plot 2D distribution
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Scatter plot
    axes[0].scatter(samples[:, 0], samples[:, 1], alpha=0.3, s=1)
    axes[0].set_xlabel('x1')
    axes[0].set_ylabel('x2')
    axes[0].set_title('Joint Distribution (Scatter)')

    # Density plot
    axes[1].hexbin(samples[:, 0], samples[:, 1], gridsize=50, cmap='Blues')
    axes[1].set_xlabel('x1')
    axes[1].set_ylabel('x2')
    axes[1].set_title('Joint Distribution (Density)')

    plt.tight_layout()
    plt.savefig('mh_banana_distribution.png', dpi=150, bbox_inches='tight')
    plt.show()


def example_mixture_model():
    """Example: Sampling from a mixture of Gaussians."""
    print("\nExample 3: Sampling from Mixture of Gaussians")

    # Mixture of two Gaussians: 0.3*N(-3,1) + 0.7*N(2,1.5)
    def log_density(x):
        comp1 = 0.3 * stats.norm.pdf(x, -3, 1)
        comp2 = 0.7 * stats.norm.pdf(x, 2, 1.5)
        return np.log(comp1 + comp2)

    # Run Metropolis-Hastings
    mh = MetropolisHastings(log_density, proposal_std=3.0)
    samples = mh.sample(n_samples=10000, initial_state=np.array([0.0]),
                       burn_in=2000)

    print(f"Acceptance rate: {mh.acceptance_rate:.2%}")

    # Plot results
    true_density = lambda x: 0.3 * stats.norm.pdf(x, -3, 1) + 0.7 * stats.norm.pdf(x, 2, 1.5)
    mh.plot_diagnostics(true_density)
    plt.savefig('mh_mixture_diagnostics.png', dpi=150, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    # Run examples
    example_1d_gaussian()
    example_2d_banana()
    example_mixture_model()
