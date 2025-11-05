# Regression Discontinuity Design (RDD) in R
# ===========================================
#
# Implementation using rdrobust package for robust RDD inference
#
# References:
#   Imbens & Lemieux (2008), Calonico et al. (2014, 2020)

# Load required packages
suppressPackageStartupMessages({
  library(rdrobust)  # For robust RDD inference
  library(rddensity) # For density continuity tests
  library(ggplot2)
  library(dplyr)
  library(tidyr)
})

# ============================================
# Simulate RDD Data
# ============================================

simulate_rdd_data <- function(n = 1000, effect = 5.0, cutoff = 0,
                             polynomial_order = 2, seed = 42) {
  #' Simulate sharp RDD data
  #'
  #' @param n Sample size
  #' @param effect True treatment effect
  #' @param cutoff Cutoff for treatment assignment
  #' @param polynomial_order Order of baseline polynomial
  #' @return data.frame with running variable, outcome, treatment

  set.seed(seed)

  # Running variable
  x <- runif(n, -2, 2)

  # Treatment assignment (sharp RDD)
  D <- as.integer(x >= cutoff)

  # Outcome with polynomial baseline
  y_baseline <- 10 + 2*x + 0.5*x^2

  if (polynomial_order >= 3) {
    y_baseline <- y_baseline + 0.1*x^3
  }

  # Add treatment effect
  y <- y_baseline + effect * D + rnorm(n, 0, 1)

  data.frame(
    running_var = x,
    outcome = y,
    treatment = D
  )
}

# ============================================
# RDD Estimation using rdrobust
# ============================================

estimate_rdd <- function(data, running_var = "running_var",
                        outcome = "outcome", cutoff = 0,
                        bandwidth = NULL, kernel = "triangular") {
  #' Estimate RDD using rdrobust
  #'
  #' @param data data.frame
  #' @param running_var Name of running variable column
  #' @param outcome Name of outcome column
  #' @param cutoff Cutoff value
  #' @param bandwidth Bandwidth (NULL for optimal)
  #' @param kernel Kernel type
  #' @return rdrobust object

  x <- data[[running_var]]
  y <- data[[outcome]]

  # Estimate RDD with robust inference
  if (is.null(bandwidth)) {
    # Use MSE-optimal bandwidth
    rdd_result <- rdrobust(y, x, c = cutoff, kernel = kernel)
  } else {
    rdd_result <- rdrobust(y, x, c = cutoff, h = bandwidth, kernel = kernel)
  }

  rdd_result
}

# ============================================
# RDD Visualization
# ============================================

plot_rdd <- function(data, rdd_result, running_var = "running_var",
                    outcome = "outcome", cutoff = 0, n_bins = 20) {
  #' Create RDD visualization with binned scatter plot
  #'
  #' @param data data.frame
  #' @param rdd_result rdrobust object
  #' @param running_var Running variable name
  #' @param outcome Outcome variable name
  #' @param cutoff Cutoff value
  #' @param n_bins Number of bins

  x <- data[[running_var]]
  y <- data[[outcome]]

  # Create bins
  x_left <- x[x < cutoff]
  x_right <- x[x >= cutoff]
  y_left <- y[x < cutoff]
  y_right <- y[x >= cutoff]

  # Bin means
  bins_left <- cut(x_left, breaks = n_bins/2)
  bins_right <- cut(x_right, breaks = n_bins/2)

  binned_left <- data.frame(x = x_left, y = y_left, bin = bins_left) %>%
    group_by(bin) %>%
    summarise(x_mean = mean(x), y_mean = mean(y), .groups = "drop")

  binned_right <- data.frame(x = x_right, y = y_right, bin = bins_right) %>%
    group_by(bin) %>%
    summarise(x_mean = mean(x), y_mean = mean(y), .groups = "drop")

  # Get bandwidth
  h <- rdd_result$bws[1]

  # Fit polynomials within bandwidth
  mask_left <- (x < cutoff) & (abs(x - cutoff) <= h)
  mask_right <- (x >= cutoff) & (abs(x - cutoff) <= h)

  if (sum(mask_left) > 0) {
    fit_left <- lm(y[mask_left] ~ x[mask_left])
    x_plot_left <- seq(min(x[mask_left]), cutoff, length.out = 100)
    y_plot_left <- predict(fit_left, newdata = data.frame(x = x_plot_left))
  }

  if (sum(mask_right) > 0) {
    fit_right <- lm(y[mask_right] ~ x[mask_right])
    x_plot_right <- seq(cutoff, max(x[mask_right]), length.out = 100)
    y_plot_right <- predict(fit_right, newdata = data.frame(x = x_plot_right))
  }

  # Create plot
  p <- ggplot() +
    # Binned scatter
    geom_point(data = binned_left, aes(x = x_mean, y = y_mean),
              color = "blue", size = 3, alpha = 0.6) +
    geom_point(data = binned_right, aes(x = x_mean, y = y_mean),
              color = "red", size = 3, alpha = 0.6) +
    # Fitted lines
    geom_line(data = data.frame(x = x_plot_left, y = y_plot_left),
             aes(x = x, y = y), color = "blue", linewidth = 1.5) +
    geom_line(data = data.frame(x = x_plot_right, y = y_plot_right),
             aes(x = x, y = y), color = "red", linewidth = 1.5) +
    # Cutoff line
    geom_vline(xintercept = cutoff, linetype = "dashed",
              linewidth = 1, alpha = 0.7) +
    labs(
      x = "Running Variable (centered at cutoff)",
      y = "Outcome",
      title = sprintf("RDD Plot (Bandwidth = %.3f)", h),
      subtitle = sprintf("Treatment Effect = %.3f (SE = %.3f)",
                        rdd_result$coef[1], rdd_result$se[1])
    ) +
    theme_minimal() +
    theme(
      text = element_text(size = 12),
      plot.title = element_text(size = 14, face = "bold"),
      plot.subtitle = element_text(size = 11)
    )

  print(p)
  invisible(p)
}

# ============================================
# Bandwidth Sensitivity Analysis
# ============================================

bandwidth_sensitivity <- function(data, running_var = "running_var",
                                  outcome = "outcome", cutoff = 0,
                                  h_range = NULL, n_points = 20) {
  #' Test sensitivity to bandwidth choice
  #'
  #' @param data data.frame
  #' @param running_var Running variable name
  #' @param outcome Outcome variable name
  #' @param cutoff Cutoff value
  #' @param h_range Vector of min and max bandwidth
  #' @param n_points Number of bandwidth values to try

  x <- data[[running_var]]
  y <- data[[outcome]]

  # Default bandwidth range
  if (is.null(h_range)) {
    h_range <- c(0.3, 2.0)
  }

  bandwidths <- seq(h_range[1], h_range[2], length.out = n_points)

  results <- data.frame(
    bandwidth = numeric(n_points),
    estimate = numeric(n_points),
    se = numeric(n_points),
    ci_lower = numeric(n_points),
    ci_upper = numeric(n_points)
  )

  for (i in seq_along(bandwidths)) {
    h <- bandwidths[i]
    rdd <- rdrobust(y, x, c = cutoff, h = h)

    results$bandwidth[i] <- h
    results$estimate[i] <- rdd$coef[1]
    results$se[i] <- rdd$se[1]
    results$ci_lower[i] <- rdd$ci[1, 1]
    results$ci_upper[i] <- rdd$ci[1, 2]
  }

  # Plot sensitivity
  p <- ggplot(results, aes(x = bandwidth, y = estimate)) +
    geom_line(linewidth = 1) +
    geom_point(size = 2) +
    geom_ribbon(aes(ymin = ci_lower, ymax = ci_upper),
               alpha = 0.3, fill = "blue") +
    geom_hline(yintercept = 5.0, linetype = "dashed",
              color = "red", linewidth = 1) +
    annotate("text", x = mean(h_range), y = 5.0,
            label = "True Effect", vjust = -0.5, color = "red") +
    labs(
      x = "Bandwidth",
      y = "Estimated Treatment Effect",
      title = "RDD Sensitivity to Bandwidth Choice",
      subtitle = "Shaded area shows 95% confidence interval"
    ) +
    theme_minimal() +
    theme(text = element_text(size = 12))

  print(p)
  invisible(results)
}

# ============================================
# Density Continuity Test (Manipulation Check)
# ============================================

test_manipulation <- function(data, running_var = "running_var", cutoff = 0) {
  #' Test for manipulation of running variable (McCrary density test)
  #'
  #' @param data data.frame
  #' @param running_var Running variable name
  #' @param cutoff Cutoff value

  x <- data[[running_var]]

  # Density test
  density_test <- rddensity(x, c = cutoff)

  cat("\n")
  cat("=" * 70, "\n")
  cat("Manipulation Test (Density Continuity)\n")
  cat("=" * 70, "\n")
  print(summary(density_test))
  cat("\n")

  # Plot density
  p <- rdplotdensity(density_test, x)

  invisible(density_test)
}

# ============================================
# Example 1: Remedial Education Program
# ============================================

example_education_rdd <- function() {
  cat("Example 1: Remedial Education Program\n")
  cat("======================================\n\n")

  set.seed(456)
  n <- 2000

  # Test score (running variable)
  test_score <- rnorm(n, 50, 15)

  # Treatment: remedial program if score < 50
  treatment <- as.integer(test_score < 50)

  # Outcome: next year's test score
  x_centered <- test_score - 50
  true_effect <- 8.0
  next_score <- 55 + 0.5*x_centered + 0.02*x_centered^2 +
               true_effect * treatment + rnorm(n, 0, 5)

  df <- data.frame(
    test_score = test_score,
    next_score = next_score,
    treatment = treatment
  )

  # Estimate RDD
  cat("Estimating RDD with MSE-optimal bandwidth...\n\n")
  rdd <- rdrobust(df$next_score, df$test_score, c = 50)

  # Print results
  print(summary(rdd))

  cat("\n")
  cat(sprintf("True effect: %.2f\n", true_effect))
  cat(sprintf("Estimated effect: %.3f (SE = %.3f)\n",
             rdd$coef[1], rdd$se[1]))
  cat(sprintf("95%% CI: [%.3f, %.3f]\n", rdd$ci[1,1], rdd$ci[1,2]))
  cat(sprintf("Bandwidth: %.3f\n", rdd$bws[1]))
  cat(sprintf("N (left): %d, N (right): %d\n",
             rdd$N_h[1], rdd$N_h[2]))

  # Plot
  df$running_var <- df$test_score
  df$outcome <- df$next_score
  p <- plot_rdd(df, rdd, cutoff = 50)
  ggsave("rdd_education_R.png", plot = p, width = 10, height = 6, dpi = 150)

  # Manipulation test
  test_manipulation(df, cutoff = 50)

  invisible(rdd)
}

# ============================================
# Example 2: Bandwidth Sensitivity
# ============================================

example_bandwidth_sensitivity <- function() {
  cat("\nExample 2: Bandwidth Sensitivity Analysis\n")
  cat("==========================================\n\n")

  # Simulate data
  df <- simulate_rdd_data(n = 1500, effect = 5.0)

  # Sensitivity analysis
  sensitivity_results <- bandwidth_sensitivity(df)
  ggsave("rdd_bandwidth_sensitivity_R.png", width = 10, height = 6, dpi = 150)

  invisible(sensitivity_results)
}

# ============================================
# Example 3: Fuzzy RDD
# ============================================

example_fuzzy_rdd <- function() {
  cat("\nExample 3: Fuzzy RDD (Imperfect Compliance)\n")
  cat("===========================================\n\n")

  set.seed(789)
  n <- 1500

  # Running variable
  x <- runif(n, -2, 2)

  # Treatment eligibility
  eligible <- as.integer(x >= 0)

  # Actual treatment (fuzzy: not everyone complies)
  # Compliance rate: 80% above cutoff, 20% below
  compliance_prob <- ifelse(eligible == 1, 0.8, 0.2)
  treatment <- rbinom(n, 1, compliance_prob)

  # Outcome
  true_effect <- 6.0
  y <- 10 + 2*x + 0.5*x^2 + true_effect * treatment + rnorm(n, 0, 1)

  # Fuzzy RDD (uses eligibility as instrument for treatment)
  fuzzy_rdd <- rdrobust(y, x, c = 0, fuzzy = treatment)

  cat("Fuzzy RDD Results:\n")
  print(summary(fuzzy_rdd))

  cat("\n")
  cat(sprintf("True effect: %.2f\n", true_effect))
  cat(sprintf("Estimated LATE: %.3f (SE = %.3f)\n",
             fuzzy_rdd$coef[1], fuzzy_rdd$se[1]))

  # First stage (effect on treatment uptake)
  first_stage <- rdrobust(treatment, x, c = 0)
  cat(sprintf("\nFirst stage (jump in treatment): %.3f\n",
             first_stage$coef[1]))

  invisible(fuzzy_rdd)
}

# ============================================
# Run all examples
# ============================================

if (sys.nframe() == 0) {
  cat("\n")
  cat("=" * 70, "\n")
  cat("Regression Discontinuity Design Examples in R\n")
  cat("=" * 70, "\n\n")

  example_education_rdd()
  example_bandwidth_sensitivity()
  example_fuzzy_rdd()

  cat("\nAll examples completed successfully!\n")
}
