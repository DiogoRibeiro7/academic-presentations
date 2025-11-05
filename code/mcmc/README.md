# MCMC Implementations

This directory contains Python implementations of various Markov Chain Monte Carlo (MCMC) algorithms.

## Files

- **`metropolis_hastings.py`**: Classic Metropolis-Hastings algorithm with random walk proposals
- **`hamiltonian_mc.py`**: Hamiltonian Monte Carlo using leapfrog integration
- **`nuts_sampler.py`**: No-U-Turn Sampler with adaptive step size tuning

## Requirements

```bash
pip install numpy scipy matplotlib seaborn statsmodels
```

## Usage Examples

### Metropolis-Hastings

```python
from metropolis_hastings import MetropolisHastings
import numpy as np

# Define target log-density
def log_density(x):
    return -0.5 * x**2  # Standard normal

# Create sampler
mh = MetropolisHastings(log_density, proposal_std=1.0)

# Generate samples
samples = mh.sample(n_samples=5000, initial_state=np.array([0.0]))

# Plot diagnostics
mh.plot_diagnostics()
```

### Hamiltonian Monte Carlo

```python
from hamiltonian_mc import HamiltonianMC

# Define log-density and its gradient
def log_density(x):
    return -0.5 * np.sum(x**2)

def grad_log_density(x):
    return -x

# Create sampler
hmc = HamiltonianMC(log_density, grad_log_density, epsilon=0.1, L=20)

# Generate samples
samples = hmc.sample(n_samples=5000, initial_state=np.zeros(2))
```

### NUTS

```python
from nuts_sampler import NUTS

# Same log-density and gradient as HMC
nuts = NUTS(log_density, grad_log_density, delta=0.65)

# Generate samples (epsilon is automatically tuned)
samples = nuts.sample(n_samples=3000, initial_state=np.zeros(2),
                      adapt_steps=1000)
```

## Key Features

### Metropolis-Hastings
- Symmetric random walk proposals
- Adjustable proposal standard deviation
- Diagnostic plots: trace, histogram, autocorrelation, running mean

### HMC
- Hamiltonian dynamics using leapfrog integration
- Efficient exploration of high-dimensional spaces
- Parameter tuning utilities
- Reduced correlation between samples

### NUTS
- Automatic trajectory length selection
- Dual averaging for step size adaptation
- No manual tuning of step size or number of steps
- More efficient than standard HMC

## References

1. Metropolis et al. (1953). "Equation of state calculations by fast computing machines"
2. Hastings (1970). "Monte Carlo sampling methods using Markov chains"
3. Duane et al. (1987). "Hybrid Monte Carlo"
4. Neal (2011). "MCMC using Hamiltonian dynamics"
5. Hoffman & Gelman (2014). "The No-U-Turn sampler"
6. Betancourt (2017). "A conceptual introduction to Hamiltonian Monte Carlo"

## Examples

Each file includes runnable examples at the bottom. To run:

```bash
python metropolis_hastings.py
python hamiltonian_mc.py
python nuts_sampler.py
```

These will generate diagnostic plots showing convergence and sampling quality.
