# Install R Packages for Academic Presentations
# Last Updated: January 2025
#
# Usage:
#   Rscript install_r_packages.R
#   or source this file in R: source("install_r_packages.R")

# ============================================================================
# Package Installation Helper
# ============================================================================

# Function to install packages if not already installed
install_if_missing <- function(packages) {
  new_packages <- packages[!(packages %in% installed.packages()[, "Package"])]
  if (length(new_packages) > 0) {
    cat("Installing packages:", paste(new_packages, collapse = ", "), "\n")
    install.packages(new_packages, dependencies = TRUE, repos = "https://cloud.r-project.org/")
  } else {
    cat("All packages already installed.\n")
  }
}

# ============================================================================
# Core Packages
# ============================================================================

core_packages <- c(
  "tidyverse",      # Data manipulation and visualization
  "data.table",     # Fast data manipulation
  "ggplot2",        # Visualization
  "dplyr",          # Data manipulation
  "tidyr",          # Data tidying
  "readr",          # Data reading
  "purrr",          # Functional programming
  "stringr",        # String manipulation
  "lubridate"       # Date/time handling
)

cat("\n=== Installing Core Packages ===\n")
install_if_missing(core_packages)

# ============================================================================
# Statistical Modeling
# ============================================================================

stats_packages <- c(
  "lmtest",         # Linear model testing
  "sandwich",       # Robust standard errors
  "car",            # Regression diagnostics
  "MASS",           # Statistical functions
  "survival",       # Survival analysis
  "nlme",           # Mixed effects models
  "lme4"            # Linear mixed effects models
)

cat("\n=== Installing Statistical Packages ===\n")
install_if_missing(stats_packages)

# ============================================================================
# Causal Inference
# ============================================================================

causal_packages <- c(
  "AER",            # Applied Econometrics with R
  "ivreg",          # Instrumental variables regression
  "rdrobust",       # Regression discontinuity
  "rddensity",      # RDD density tests
  "rdd",            # Regression discontinuity designs
  "fixest",         # Fast fixed effects estimation
  "plm",            # Panel linear models
  "did",            # Difference-in-Differences
  "DidDid",         # Alternative DiD package
  "Synth",          # Synthetic control methods
  "gsynth",         # Generalized synthetic control
  "CausalImpact",   # Bayesian causal impact
  "MatchIt",        # Matching methods
  "Matching"        # Propensity score matching
)

cat("\n=== Installing Causal Inference Packages ===\n")
install_if_missing(causal_packages)

# ============================================================================
# Time Series
# ============================================================================

timeseries_packages <- c(
  "forecast",       # Time series forecasting
  "tseries",        # Time series analysis
  "zoo",            # Time series objects
  "xts",            # Extensible time series
  "vars",           # Vector autoregression
  "urca",           # Unit root and cointegration tests
  "fable",          # Tidy forecasting framework
  "feasts",         # Feature extraction from time series
  "tsibble",        # Tidy temporal data frames
  "prophet",        # Facebook Prophet
  "lubridate"       # Date/time handling
)

cat("\n=== Installing Time Series Packages ===\n")
install_if_missing(timeseries_packages)

# ============================================================================
# Machine Learning
# ============================================================================

ml_packages <- c(
  "caret",          # Classification and regression training
  "mlr3",           # Machine learning in R
  "randomForest",   # Random forests
  "xgboost",        # Gradient boosting
  "glmnet",         # Elastic net regression
  "e1071",          # SVM and other methods
  "rpart",          # Decision trees
  "rpart.plot",     # Decision tree plotting
  "recipes",        # Feature engineering
  "rsample"         # Resampling
)

cat("\n=== Installing Machine Learning Packages ===\n")
install_if_missing(ml_packages)

# ============================================================================
# Bayesian Statistics
# ============================================================================

bayesian_packages <- c(
  "rstan",          # Stan interface
  "brms",           # Bayesian regression models with Stan
  "rstanarm",       # Applied regression modeling via Stan
  "bayesplot",      # Bayesian visualization
  "bsts",           # Bayesian structural time series
  "MCMCpack",       # MCMC utilities
  "coda"            # MCMC diagnostics
)

cat("\n=== Installing Bayesian Packages ===\n")
install_if_missing(bayesian_packages)

# ============================================================================
# Visualization
# ============================================================================

viz_packages <- c(
  "ggplot2",        # Grammar of graphics
  "lattice",        # Trellis graphics
  "plotly",         # Interactive plots
  "patchwork",      # Combining plots
  "ggpubr",         # Publication-ready plots
  "ggthemes",       # Extra themes
  "RColorBrewer",   # Color palettes
  "viridis",        # Color scales
  "scales"          # Scale functions
)

cat("\n=== Installing Visualization Packages ===\n")
install_if_missing(viz_packages)

# ============================================================================
# Development & Quality
# ============================================================================

dev_packages <- c(
  "testthat",       # Unit testing
  "devtools",       # Development tools
  "roxygen2",       # Documentation
  "lintr",          # Code linting
  "styler",         # Code formatting
  "covr",           # Code coverage
  "profvis",        # Profiling
  "microbenchmark"  # Benchmarking
)

cat("\n=== Installing Development Packages ===\n")
install_if_missing(dev_packages)

# ============================================================================
# Utilities
# ============================================================================

utility_packages <- c(
  "here",           # Project-relative paths
  "janitor",        # Data cleaning
  "skimr",          # Data summaries
  "broom",          # Tidy model outputs
  "knitr",          # Dynamic reports
  "rmarkdown",      # R Markdown
  "DT",             # Interactive tables
  "gt",             # Grammar of tables
  "parallel",       # Parallel computing
  "doParallel"      # Parallel backend
)

cat("\n=== Installing Utility Packages ===\n")
install_if_missing(utility_packages)

# ============================================================================
# Verify Installation
# ============================================================================

cat("\n=== Verifying Installation ===\n")

all_packages <- c(
  core_packages,
  stats_packages,
  causal_packages,
  timeseries_packages,
  ml_packages,
  bayesian_packages,
  viz_packages,
  dev_packages,
  utility_packages
)

installed <- all_packages %in% installed.packages()[, "Package"]
success_rate <- sum(installed) / length(all_packages) * 100

cat("\nInstallation Summary:\n")
cat(sprintf("  Successfully installed: %d/%d packages (%.1f%%)\n",
            sum(installed), length(all_packages), success_rate))

if (any(!installed)) {
  cat("\nFailed to install:\n")
  cat(paste("  -", all_packages[!installed], collapse = "\n"), "\n")
  cat("\nTry installing failed packages manually:\n")
  cat("  install.packages(c(\"",
      paste(all_packages[!installed], collapse = "\", \""),
      "\"))\n", sep = "")
}

cat("\n=== Installation Complete ===\n")
cat("\nTo load all tidyverse packages:\n")
cat("  library(tidyverse)\n")
cat("\nFor individual packages, use:\n")
cat("  library(package_name)\n")

# ============================================================================
# Session Information
# ============================================================================

cat("\n=== R Session Information ===\n")
print(sessionInfo())

cat("\n=== Package Versions ===\n")
if (length(all_packages[installed]) > 0) {
  pkg_versions <- installed.packages()[all_packages[installed], "Version"]
  version_df <- data.frame(
    Package = all_packages[installed],
    Version = pkg_versions,
    stringsAsFactors = FALSE
  )
  print(version_df, row.names = FALSE)
}
