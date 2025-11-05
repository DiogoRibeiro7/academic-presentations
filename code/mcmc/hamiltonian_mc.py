"""
Hamiltonian Monte Carlo (HMC) Implementation
=============================================

This module implements Hamiltonian Monte Carlo, which uses Hamiltonian dynamics
to propose distant states while maintaining high acceptance rates.

References:
    Duane et al. (1987), Neal (2011), Betancourt (2017)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from typing import Callable, Tuple
import seaborn as sns

sns.set_style("whitegrid")


class HamiltonianMC:
    """
    Hamiltonian Monte Carlo sampler.

    Uses Hamiltonian dynamics to propose new states, allowing efficient exploration
    of the target distribution.

    Parameters
    ----------
    log_density : callable
        Log of the target density function
    grad_log_density : callable
        Gradient of the log density function
    epsilon : float
        Step size for leapfrog integrator
    L : int
        Number of leapfrog steps
    """

    def __init__(self, log_density: Callable, grad_log_density: Callable,
                 epsilon: float = 0.1, L: int = 10):
        self.log_density = log_density
        self.grad_log_density = grad_log_density
        self.epsilon = epsilon
        self.L = L
        self.samples = None
        self.acceptance_rate = None

    def leapfrog(self, q: np.ndarray, p: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Leapfrog integrator for Hamiltonian dynamics.

        Parameters
        ----------
        q : np.ndarray
            Position (current state)
        p : np.ndarray
            Momentum

        Returns
        -------
        Tuple[np.ndarray, np.ndarray]
            New position and momentum after L steps
        """
        q = q.copy()
        p = p.copy()

        # Half step for momentum
        p = p + 0.5 * self.epsilon * self.grad_log_density(q)

        # L-1 full steps
        for _ in range(self.L - 1):
            # Full step for position
            q = q + self.epsilon * p

            # Full step for momentum
            p = p + self.epsilon * self.grad_log_density(q)

        # Final full step for position
        q = q + self.epsilon * p

        # Final half step for momentum
        p = p + 0.5 * self.epsilon * self.grad_log_density(q)

        # Negate momentum for reversibility
        p = -p

        return q, p

    def hamiltonian(self, q: np.ndarray, p: np.ndarray) -> float:
        """
        Compute the Hamiltonian (total energy).

        H(q, p) = -log π(q) + 0.5 * p^T p

        Parameters
        ----------
        q : np.ndarray
            Position
        p : np.ndarray
            Momentum

        Returns
        -------
        float
            Hamiltonian value
        """
        potential_energy = -self.log_density(q)
        kinetic_energy = 0.5 * np.sum(p ** 2)
        return potential_energy + kinetic_energy

    def sample(self, n_samples: int, initial_state: np.ndarray,
               burn_in: int = 1000, thin: int = 1) -> np.ndarray:
        """
        Run the HMC algorithm.

        Parameters
        ----------
        n_samples : int
            Number of samples to generate (after burn-in and thinning)
        initial_state : np.ndarray
            Initial state
        burn_in : int, optional
            Number of initial samples to discard
        thin : int, optional
            Thinning interval

        Returns
        -------
        np.ndarray
            Array of samples
        """
        dim = len(initial_state)
        total_iterations = burn_in + n_samples * thin

        all_samples = np.zeros((total_iterations, dim))
        all_samples[0] = initial_state

        accepted = 0

        for i in range(1, total_iterations):
            q_current = all_samples[i-1]

            # Sample momentum from standard normal
            p_current = np.random.randn(dim)

            # Current Hamiltonian
            H_current = self.hamiltonian(q_current, p_current)

            # Propose new state using leapfrog
            q_proposed, p_proposed = self.leapfrog(q_current, p_current)

            # Proposed Hamiltonian
            H_proposed = self.hamiltonian(q_proposed, p_proposed)

            # Metropolis acceptance step
            log_accept_ratio = -H_proposed + H_current
            accept_prob = min(1.0, np.exp(log_accept_ratio))

            if np.random.uniform() < accept_prob:
                all_samples[i] = q_proposed
                accepted += 1
            else:
                all_samples[i] = q_current

        self.acceptance_rate = accepted / total_iterations

        # Discard burn-in and apply thinning
        self.samples = all_samples[burn_in::thin]

        return self.samples

    def tune_parameters(self, initial_state: np.ndarray, n_tuning: int = 500,
                       target_accept: float = 0.65) -> Tuple[float, int]:
        """
        Simple parameter tuning for epsilon and L.

        Parameters
        ----------
        initial_state : np.ndarray
            Initial state for tuning
        n_tuning : int
            Number of iterations for tuning
        target_accept : float
            Target acceptance rate

        Returns
        -------
        Tuple[float, int]
            Tuned epsilon and L
        """
        print(f"Tuning HMC parameters (target acceptance: {target_accept:.2f})...")

        # Try different epsilon values
        epsilon_candidates = np.logspace(-2, 0, 10)
        best_epsilon = self.epsilon
        best_diff = float('inf')

        for eps in epsilon_candidates:
            self.epsilon = eps
            self.sample(n_samples=n_tuning, initial_state=initial_state,
                       burn_in=0, thin=1)
            diff = abs(self.acceptance_rate - target_accept)
            if diff < best_diff:
                best_diff = diff
                best_epsilon = eps

        self.epsilon = best_epsilon
        print(f"Selected epsilon: {self.epsilon:.4f}")
        print(f"Acceptance rate: {self.acceptance_rate:.2%}")

        return self.epsilon, self.L

    def plot_diagnostics(self, dim_to_plot: int = 0):
        """Plot diagnostic plots."""
        if self.samples is None:
            raise ValueError("No samples available. Run sample() first.")

        fig, axes = plt.subplots(2, 2, figsize=(12, 10))

        # Trace plot
        axes[0, 0].plot(self.samples[:, dim_to_plot], alpha=0.7)
        axes[0, 0].set_xlabel('Iteration')
        axes[0, 0].set_ylabel(f'Value (dim {dim_to_plot})')
        axes[0, 0].set_title('Trace Plot')

        # Histogram
        axes[0, 1].hist(self.samples[:, dim_to_plot], bins=50, density=True, alpha=0.7)
        axes[0, 1].set_xlabel(f'Value (dim {dim_to_plot})')
        axes[0, 1].set_ylabel('Density')
        axes[0, 1].set_title('Marginal Distribution')

        # Autocorrelation
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
        plt.suptitle(f'HMC Diagnostics (Acceptance Rate: {self.acceptance_rate:.2%})',
                     y=1.02, fontsize=14)
        return fig


# Example usage

def example_2d_gaussian():
    """Example: Sampling from a correlated 2D Gaussian."""
    print("HMC Example 1: Correlated 2D Gaussian")

    # Target: Bivariate normal with correlation
    mean = np.array([1.0, 2.0])
    cov = np.array([[1.0, 0.8],
                    [0.8, 1.0]])
    cov_inv = np.linalg.inv(cov)

    def log_density(x):
        diff = x - mean
        return -0.5 * diff @ cov_inv @ diff

    def grad_log_density(x):
        diff = x - mean
        return -cov_inv @ diff

    # Run HMC
    hmc = HamiltonianMC(log_density, grad_log_density, epsilon=0.2, L=20)
    samples = hmc.sample(n_samples=5000, initial_state=np.array([0.0, 0.0]),
                        burn_in=1000)

    print(f"Sample mean: {samples.mean(axis=0)}")
    print(f"True mean: {mean}")
    print(f"Sample covariance:\n{np.cov(samples.T)}")
    print(f"True covariance:\n{cov}")
    print(f"Acceptance rate: {hmc.acceptance_rate:.2%}")

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].scatter(samples[:, 0], samples[:, 1], alpha=0.3, s=1)
    axes[0].set_xlabel('x1')
    axes[0].set_ylabel('x2')
    axes[0].set_title('Joint Distribution')

    # Plot true contours
    from matplotlib.patches import Ellipse
    from scipy.stats import chi2
    ax = axes[0]
    for p in [0.5, 0.9, 0.99]:
        # Confidence ellipse
        chi2_val = chi2.ppf(p, df=2)
        eigenvalues, eigenvectors = np.linalg.eig(cov)
        angle = np.degrees(np.arctan2(eigenvectors[1, 0], eigenvectors[0, 0]))
        width, height = 2 * np.sqrt(chi2_val * eigenvalues)
        ellipse = Ellipse(mean, width, height, angle=angle,
                         facecolor='none', edgecolor='red', linewidth=2, alpha=0.5)
        ax.add_patch(ellipse)

    hmc.plot_diagnostics(dim_to_plot=0)
    plt.savefig('hmc_gaussian_diagnostics.png', dpi=150, bbox_inches='tight')
    plt.show()


def example_funnel():
    """Example: Neal's funnel - a challenging distribution."""
    print("\nHMC Example 2: Neal's Funnel")

    # Neal's funnel: challenging for standard samplers
    def log_density(x):
        if len(x.shape) == 1:
            v, x_rest = x[0], x[1:]
        else:
            v, x_rest = x[:, 0], x[:, 1:]
        log_p_v = stats.norm.logpdf(v, 0, 3)
        log_p_x = np.sum(stats.norm.logpdf(x_rest, 0, np.exp(v/2)))
        return log_p_v + log_p_x

    def grad_log_density(x):
        v = x[0]
        x_rest = x[1:]
        d = len(x)

        grad = np.zeros(d)
        # Gradient w.r.t. v
        grad[0] = -v / 9 + 0.5 * np.sum(1 - x_rest**2 * np.exp(-v))
        # Gradient w.r.t. x_i
        grad[1:] = -x_rest * np.exp(-v)

        return grad

    # Run HMC (this is challenging!)
    hmc = HamiltonianMC(log_density, grad_log_density, epsilon=0.1, L=15)
    samples = hmc.sample(n_samples=5000, initial_state=np.zeros(5),
                        burn_in=2000)

    print(f"Acceptance rate: {hmc.acceptance_rate:.2%}")
    print(f"v mean: {samples[:, 0].mean():.3f} (should be ~0)")
    print(f"v std: {samples[:, 0].std():.3f} (should be ~3)")

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].scatter(samples[:, 0], samples[:, 1], alpha=0.3, s=1)
    axes[0].set_xlabel('v')
    axes[0].set_ylabel('x1')
    axes[0].set_title("Neal's Funnel")

    axes[1].hist(samples[:, 0], bins=50, density=True, alpha=0.7, label='HMC samples')
    x_range = np.linspace(samples[:, 0].min(), samples[:, 0].max(), 1000)
    axes[1].plot(x_range, stats.norm.pdf(x_range, 0, 3), 'r-', linewidth=2, label='True density')
    axes[1].set_xlabel('v')
    axes[1].set_ylabel('Density')
    axes[1].set_title('Marginal of v')
    axes[1].legend()

    plt.tight_layout()
    plt.savefig('hmc_funnel.png', dpi=150, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    example_2d_gaussian()
    example_funnel()
