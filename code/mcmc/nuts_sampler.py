"""
No-U-Turn Sampler (NUTS) Implementation
========================================

This module implements the No-U-Turn Sampler, an extension of HMC that
automatically tunes the trajectory length.

References:
    Hoffman & Gelman (2014)
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, Tuple
import seaborn as sns

sns.set_style("whitegrid")


class NUTS:
    """
    No-U-Turn Sampler (NUTS).

    Automatically adapts the number of leapfrog steps to avoid random walks
    while maintaining detailed balance.

    Parameters
    ----------
    log_density : callable
        Log of the target density function
    grad_log_density : callable
        Gradient of the log density function
    epsilon : float
        Step size for leapfrog integrator (will be adapted)
    delta : float
        Target acceptance probability for dual averaging
    """

    def __init__(self, log_density: Callable, grad_log_density: Callable,
                 epsilon: float = 0.1, delta: float = 0.6):
        self.log_density = log_density
        self.grad_log_density = grad_log_density
        self.epsilon = epsilon
        self.delta = delta  # Target acceptance probability
        self.samples = None
        self.acceptance_rate = None
        self.epsilon_history = []

    def leapfrog(self, q: np.ndarray, p: np.ndarray, epsilon: float) -> Tuple[np.ndarray, np.ndarray]:
        """Single leapfrog step."""
        p = p + 0.5 * epsilon * self.grad_log_density(q)
        q = q + epsilon * p
        p = p + 0.5 * epsilon * self.grad_log_density(q)
        return q, p

    def hamiltonian(self, q: np.ndarray, p: np.ndarray) -> float:
        """Compute Hamiltonian."""
        return -self.log_density(q) + 0.5 * np.sum(p ** 2)

    def find_reasonable_epsilon(self, q: np.ndarray) -> float:
        """
        Heuristic for finding a reasonable initial epsilon.

        Algorithm 4 from Hoffman & Gelman (2014)
        """
        epsilon = 1.0
        p = np.random.randn(len(q))

        _, p_new = self.leapfrog(q, p, epsilon)

        # Check if moving in right direction
        log_ratio = -self.hamiltonian(q, p_new) + self.hamiltonian(q, p)
        a = 1.0 if log_ratio > np.log(0.5) else -1.0

        # Keep doubling/halving until we cross the acceptance threshold
        while a * log_ratio > -a * np.log(2):
            epsilon = epsilon * (2.0 ** a)
            _, p_new = self.leapfrog(q, p, epsilon)
            log_ratio = -self.hamiltonian(q, p_new) + self.hamiltonian(q, p)

        return epsilon

    def build_tree(self, q, p, u, v, j, epsilon, q0, p0):
        """
        Build a balanced binary tree for candidate states.

        Recursively builds a tree of depth j using leapfrog steps.

        Returns
        -------
        q_new, p_new : Next position and momentum
        q_fwd, p_fwd : Forward-most position and momentum
        q_bwd, p_bwd : Backward-most position and momentum
        q_prime : Proposal from this subtree
        p_prime : Momentum for proposal
        n_prime : Number of valid states in subtree
        s_prime : Stop criterion (1 if should continue, 0 otherwise)
        alpha : Sum of metropolis acceptance probabilities
        n_alpha : Number of acceptance probability computations
        """
        if j == 0:
            # Base case: single leapfrog step
            q_new, p_new = self.leapfrog(q, p, v * epsilon)
            H = self.hamiltonian(q_new, p_new)
            H0 = self.hamiltonian(q0, p0)

            # Check if valid state (slice sampling condition)
            n_prime = int(u < np.exp(-H))

            # Check U-turn condition (inner product)
            s_prime = int((u < np.exp(1000 - H)))  # Avoid numerical issues

            # Metropolis acceptance probability
            alpha_prime = min(1.0, np.exp(-H + H0))
            n_alpha_prime = 1

            return (q_new, p_new, q_new, p_new, q_new, p_new, q_new, p_new,
                    n_prime, s_prime, alpha_prime, n_alpha_prime)
        else:
            # Recursion: build left and right subtrees
            (q_new, p_new, q_fwd, p_fwd, q_bwd, p_bwd, q_prime, p_prime,
             n_prime, s_prime, alpha_prime, n_alpha_prime) = self.build_tree(
                q, p, u, v, j-1, epsilon, q0, p0)

            if s_prime == 1:
                if v == -1:
                    (q_bwd, p_bwd, _, _, _, _, q_prime2, p_prime2,
                     n_prime2, s_prime2, alpha_prime2, n_alpha_prime2) = self.build_tree(
                        q_bwd, p_bwd, u, v, j-1, epsilon, q0, p0)
                else:
                    (_, _, q_fwd, p_fwd, _, _, q_prime2, p_prime2,
                     n_prime2, s_prime2, alpha_prime2, n_alpha_prime2) = self.build_tree(
                        q_fwd, p_fwd, u, v, j-1, epsilon, q0, p0)

                # Choose proposal from second subtree with probability n_prime2 / (n_prime + n_prime2)
                if np.random.rand() < n_prime2 / max(n_prime + n_prime2, 1):
                    q_prime = q_prime2
                    p_prime = p_prime2

                # Update acceptance probability statistics
                alpha_prime += alpha_prime2
                n_alpha_prime += n_alpha_prime2

                # Check U-turn condition
                delta_fwd = q_fwd - q_bwd
                s_prime = s_prime2 * int(np.dot(delta_fwd, p_bwd) >= 0) * int(np.dot(delta_fwd, p_fwd) >= 0)

                n_prime = n_prime + n_prime2

            return (q_new, p_new, q_fwd, p_fwd, q_bwd, p_bwd, q_prime, p_prime,
                    n_prime, s_prime, alpha_prime, n_alpha_prime)

    def sample(self, n_samples: int, initial_state: np.ndarray,
               burn_in: int = 1000, adapt_steps: int = 1000) -> np.ndarray:
        """
        Run NUTS with dual averaging for step size adaptation.

        Parameters
        ----------
        n_samples : int
            Number of samples to generate
        initial_state : np.ndarray
            Initial state
        burn_in : int
            Number of burn-in iterations
        adapt_steps : int
            Number of steps for epsilon adaptation

        Returns
        -------
        np.ndarray
            Array of samples
        """
        dim = len(initial_state)
        total_iterations = burn_in + n_samples

        # Find reasonable initial epsilon
        epsilon = self.find_reasonable_epsilon(initial_state)
        print(f"Initial epsilon: {epsilon:.4f}")

        # Dual averaging parameters
        gamma = 0.05
        t0 = 10
        kappa = 0.75
        mu = np.log(10 * epsilon)

        epsilon_bar = 1.0
        H_bar = 0.0

        all_samples = np.zeros((total_iterations, dim))
        all_samples[0] = initial_state
        self.epsilon_history = [epsilon]

        accepted = 0
        max_tree_depth = 10

        for m in range(1, total_iterations):
            q = all_samples[m-1]
            p = np.random.randn(dim)

            # Initial slice variable
            u = np.random.uniform(0, np.exp(-self.hamiltonian(q, p)))

            # Initialize tree
            q_fwd = q_bwd = q_new = q
            p_fwd = p_bwd = p_new = p
            j = 0  # Tree depth
            n = 1  # Number of valid states
            s = 1  # Stop criterion

            while s == 1 and j < max_tree_depth:
                # Choose direction
                v = int(2 * (np.random.rand() < 0.5) - 1)

                if v == -1:
                    (q_bwd, p_bwd, _, _, _, _, q_prime, p_prime,
                     n_prime, s_prime, alpha, n_alpha) = self.build_tree(
                        q_bwd, p_bwd, u, v, j, epsilon, q, p)
                else:
                    (_, _, q_fwd, p_fwd, _, _, q_prime, p_prime,
                     n_prime, s_prime, alpha, n_alpha) = self.build_tree(
                        q_fwd, p_fwd, u, v, j, epsilon, q, p)

                if s_prime == 1:
                    # Accept proposal with probability n_prime / n
                    if np.random.rand() < min(1, n_prime / n):
                        q_new = q_prime
                        accepted += 1

                # Update number of valid states
                n = n + n_prime

                # Check U-turn condition
                delta = q_fwd - q_bwd
                s = s_prime * int(np.dot(delta, p_bwd) >= 0) * int(np.dot(delta, p_fwd) >= 0)

                j += 1

            all_samples[m] = q_new

            # Adapt epsilon during burn-in
            if m <= adapt_steps:
                # Dual averaging
                H_bar = (1 - 1/(m + t0)) * H_bar + (1/(m + t0)) * (self.delta - alpha/n_alpha)
                log_epsilon = mu - (np.sqrt(m) / gamma) * H_bar
                epsilon = np.exp(log_epsilon)

                epsilon_bar = np.exp(m**(-kappa) * log_epsilon + (1 - m**(-kappa)) * np.log(epsilon_bar))
                self.epsilon_history.append(epsilon)
            else:
                epsilon = epsilon_bar

        self.acceptance_rate = accepted / total_iterations
        self.samples = all_samples[burn_in:]
        self.epsilon = epsilon_bar

        print(f"Final epsilon: {self.epsilon:.4f}")
        print(f"Acceptance rate: {self.acceptance_rate:.2%}")

        return self.samples


def example_2d_gaussian():
    """Example: NUTS on a 2D Gaussian."""
    print("NUTS Example: Correlated 2D Gaussian")

    mean = np.array([1.0, 2.0])
    cov = np.array([[1.0, 0.9], [0.9, 1.0]])
    cov_inv = np.linalg.inv(cov)

    def log_density(x):
        diff = x - mean
        return -0.5 * diff @ cov_inv @ diff

    def grad_log_density(x):
        return -cov_inv @ (x - mean)

    # Run NUTS
    nuts = NUTS(log_density, grad_log_density, delta=0.65)
    samples = nuts.sample(n_samples=3000, initial_state=np.array([0.0, 0.0]),
                         burn_in=1000, adapt_steps=1000)

    print(f"Sample mean: {samples.mean(axis=0)}")
    print(f"True mean: {mean}")

    # Plot samples
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].scatter(samples[:, 0], samples[:, 1], alpha=0.3, s=1)
    axes[0].set_xlabel('x1')
    axes[0].set_ylabel('x2')
    axes[0].set_title('NUTS Samples')

    # Plot epsilon adaptation
    axes[1].plot(nuts.epsilon_history)
    axes[1].set_xlabel('Iteration')
    axes[1].set_ylabel('Epsilon')
    axes[1].set_title('Step Size Adaptation')
    axes[1].axhline(y=nuts.epsilon, color='r', linestyle='--', label='Final epsilon')
    axes[1].legend()

    plt.tight_layout()
    plt.savefig('nuts_gaussian.png', dpi=150, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    example_2d_gaussian()
