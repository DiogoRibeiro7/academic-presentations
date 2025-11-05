"""
Pytest configuration and fixtures for Academic Presentations tests.

This file contains shared fixtures and configuration that can be used
across all test modules.
"""

import numpy as np
import pandas as pd
import pytest


# ============================================================================
# Session-level fixtures
# ============================================================================

@pytest.fixture(scope="session")
def random_seed():
    """Set random seed for reproducibility."""
    np.random.seed(42)
    return 42


# ============================================================================
# Module-level fixtures
# ============================================================================

@pytest.fixture(scope="module")
def sample_timeseries():
    """Generate sample time series data."""
    n = 1000
    t = np.arange(n)
    trend = 0.01 * t
    seasonal = 10 * np.sin(2 * np.pi * t / 365)
    noise = np.random.normal(0, 1, n)
    y = trend + seasonal + noise

    return pd.DataFrame({
        'time': pd.date_range('2020-01-01', periods=n, freq='D'),
        'value': y
    })


@pytest.fixture(scope="module")
def sample_classification_data():
    """Generate sample classification dataset."""
    np.random.seed(42)
    n = 1000
    X = np.random.randn(n, 5)
    y = (X[:, 0] + X[:, 1] > 0).astype(int)

    return {
        'X': X,
        'y': y,
        'feature_names': [f'feature_{i}' for i in range(5)]
    }


@pytest.fixture(scope="module")
def sample_regression_data():
    """Generate sample regression dataset."""
    np.random.seed(42)
    n = 500
    X = np.random.randn(n, 3)
    true_coef = np.array([2.0, -1.5, 0.5])
    y = X @ true_coef + np.random.normal(0, 0.5, n)

    return {
        'X': X,
        'y': y,
        'true_coef': true_coef
    }


@pytest.fixture(scope="module")
def sample_causal_data():
    """Generate sample data for causal inference with instrument."""
    np.random.seed(42)
    n = 1000

    # Instrument
    z = np.random.normal(0, 1, n)

    # Confounder
    u = np.random.normal(0, 1, n)

    # Treatment (affected by instrument and confounder)
    x = 0.5 * z + 0.3 * u + np.random.normal(0, 0.5, n)

    # Outcome (affected by treatment and confounder)
    true_effect = 2.0
    y = true_effect * x + 0.4 * u + np.random.normal(0, 0.5, n)

    return {
        'y': y,
        'x': x,
        'z': z,
        'true_effect': true_effect
    }


# ============================================================================
# Function-level fixtures
# ============================================================================

@pytest.fixture
def temp_data_dir(tmp_path):
    """Create temporary directory for test data."""
    data_dir = tmp_path / "test_data"
    data_dir.mkdir()
    return data_dir


@pytest.fixture
def small_dataset():
    """Generate small dataset for quick tests."""
    X = np.array([[1, 2], [3, 4], [5, 6]])
    y = np.array([0, 1, 0])
    return X, y


# ============================================================================
# Markers
# ============================================================================

def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )


# ============================================================================
# Test collection customization
# ============================================================================

def pytest_collection_modifyitems(config, items):
    """Modify test items during collection."""
    for item in items:
        # Add unit marker to all tests not marked as integration
        if "integration" not in item.keywords:
            item.add_marker(pytest.mark.unit)
