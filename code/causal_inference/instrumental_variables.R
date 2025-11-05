# Instrumental Variables (IV) Estimation in R
# ============================================
#
# Implementation using AER package for 2SLS
#
# References:
#   Angrist, Imbens & Rubin (1996), Angrist & Pischke (2008)

# Load required packages
suppressPackageStartupMessages({
  library(AER)      # For ivreg (IV regression)
  library(lmtest)   # For coeftest
  library(sandwich) # For robust SE
  library(ggplot2)
  library(dplyr)
  library(broom)
})

# ============================================
# Simulate IV Data
# ============================================

simulate_iv_data <- function(n = 1000, instrument_strength = 0.5,
                             confounding = 0.3, seed = 42) {
  #' Simulate data for IV example
  #'
  #' @param n Sample size
  #' @param instrument_strength Strength of Z -> D relationship
  #' @param confounding Degree of confounding
  #' @return data.frame with Y, D, Z, U

  set.seed(seed)

  # Unobserved confounder
  U <- rnorm(n, 0, 1)

  # Instrument (e.g., randomized encouragement)
  Z <- rbinom(n, 1, 0.5)

  # Treatment (endogenous because of U)
  D <- instrument_strength * Z + confounding * U + rnorm(n, 0, 0.5)

  # Outcome
  true_effect <- 1.5
  Y <- true_effect * D + confounding * U + rnorm(n, 0, 1)

  data.frame(Y = Y, D = D, Z = Z, U = U)
}

# ============================================
# IV Estimation Function
# ============================================

estimate_iv <- function(data, formula_str = "Y ~ D | Z", robust_se = TRUE) {
  #' Estimate IV model using 2SLS
  #'
  #' @param data data.frame containing variables
  #' @param formula_str IV formula: outcome ~ treatment | instruments
  #' @param robust_se Use heteroskedasticity-robust SE
  #' @return List with results

  # Parse formula
  formula <- as.formula(formula_str)

  # Fit IV model
  iv_model <- ivreg(formula, data = data)

  # Get coefficients
  if (robust_se) {
    coef_summary <- coeftest(iv_model, vcov = vcovHC(iv_model, type = "HC1"))
  } else {
    coef_summary <- summary(iv_model)$coefficients
  }

  # First stage diagnostics
  first_stage <- summary(iv_model, diagnostics = TRUE)

  # Extract diagnostics
  weak_instruments <- first_stage$diagnostics["Weak instruments", ]

  list(
    model = iv_model,
    coefficients = coef_summary,
    first_stage_f = weak_instruments["statistic"],
    first_stage_p = weak_instruments["p-value"],
    summary = summary(iv_model, diagnostics = TRUE)
  )
}

# ============================================
# Compare OLS vs IV
# ============================================

compare_ols_iv <- function(data) {
  #' Compare OLS (biased) with IV (consistent)

  # OLS (biased due to endogeneity)
  ols_model <- lm(Y ~ D, data = data)
  ols_coef <- coef(ols_model)["D"]

  # IV (consistent)
  iv_model <- ivreg(Y ~ D | Z, data = data)
  iv_coef <- coef(iv_model)["D"]

  cat("=" * 70, "\n")
  cat("OLS vs IV Comparison\n")
  cat("=" * 70, "\n")
  cat(sprintf("OLS estimate:  %.4f (BIASED due to endogeneity)\n", ols_coef))
  cat(sprintf("IV estimate:   %.4f (CONSISTENT)\n", iv_coef))
  cat(sprintf("True effect:   1.5000\n"))
  cat(sprintf("OLS bias:      %.4f\n", ols_coef - 1.5))
  cat("\n")

  list(ols = ols_coef, iv = iv_coef)
}

# ============================================
# Example 1: Returns to Schooling
# ============================================

example_returns_to_schooling <- function() {
  cat("Example 1: Returns to Schooling\n")
  cat("================================\n\n")

  set.seed(123)
  n <- 5000

  # Quarter of birth (instrument)
  quarter <- sample(1:4, n, replace = TRUE)
  Z <- as.integer(quarter == 1)  # Born in Q1

  # Unobserved ability
  ability <- rnorm(n, 0, 1)

  # Years of education (endogenous)
  education <- 12 + 0.3 * Z - 0.4 * ability + rnorm(n, 0, 2)

  # Log earnings
  true_return <- 0.08  # 8% return per year
  log_earnings <- 2.0 + true_return * education +
                 0.3 * ability + rnorm(n, 0, 0.5)

  df <- data.frame(
    earnings = log_earnings,
    education = education,
    quarter_1 = Z,
    ability = ability
  )

  # OLS
  ols <- lm(earnings ~ education, data = df)
  cat("OLS Results (Biased):\n")
  print(summary(ols)$coefficients)
  cat("\n")

  # IV
  iv <- ivreg(earnings ~ education | quarter_1, data = df)
  cat("IV Results (Consistent):\n")
  print(summary(iv, diagnostics = TRUE))
  cat("\n")

  # Visualize first stage
  first_stage_plot <- df %>%
    group_by(quarter_1) %>%
    summarise(mean_education = mean(education),
             se = sd(education) / sqrt(n())) %>%
    ggplot(aes(x = factor(quarter_1), y = mean_education)) +
    geom_bar(stat = "identity", fill = "steelblue", alpha = 0.7) +
    geom_errorbar(aes(ymin = mean_education - 1.96*se,
                     ymax = mean_education + 1.96*se), width = 0.2) +
    labs(x = "Born in Q1", y = "Average Years of Education",
         title = "First Stage: Instrument → Treatment") +
    scale_x_discrete(labels = c("No", "Yes")) +
    theme_minimal()

  print(first_stage_plot)
  ggsave("iv_first_stage_R.png", width = 6, height = 4, dpi = 150)

  invisible(list(ols = ols, iv = iv))
}

# ============================================
# Example 2: Weak Instruments Problem
# ============================================

example_weak_instruments <- function() {
  cat("\nExample 2: Weak Instruments Problem\n")
  cat("====================================\n\n")

  # Weak instrument
  cat("WEAK INSTRUMENT (strength = 0.1):\n")
  cat("-" * 70, "\n")
  df_weak <- simulate_iv_data(n = 1000, instrument_strength = 0.1,
                              confounding = 0.5)
  iv_weak <- estimate_iv(df_weak)
  print(iv_weak$summary)
  cat(sprintf("First-stage F-statistic: %.2f\n", iv_weak$first_stage_f))
  if (iv_weak$first_stage_f < 10) {
    cat("WARNING: Weak instruments (F < 10)!\n")
  }
  cat("\n")

  # Strong instrument
  cat("STRONG INSTRUMENT (strength = 0.8):\n")
  cat("-" * 70, "\n")
  df_strong <- simulate_iv_data(n = 1000, instrument_strength = 0.8,
                                confounding = 0.5)
  iv_strong <- estimate_iv(df_strong)
  print(iv_strong$summary)
  cat(sprintf("First-stage F-statistic: %.2f\n", iv_strong$first_stage_f))
  cat("\n")

  # Comparison plot
  results_df <- data.frame(
    Instrument = c("Weak", "Strong"),
    Estimate = c(coef(iv_weak$model)["D"], coef(iv_strong$model)["D"]),
    SE = c(iv_weak$coefficients["D", "Std. Error"],
          iv_strong$coefficients["D", "Std. Error"])
  )

  results_df$CI_lower <- results_df$Estimate - 1.96 * results_df$SE
  results_df$CI_upper <- results_df$Estimate + 1.96 * results_df$SE

  p <- ggplot(results_df, aes(x = Instrument, y = Estimate)) +
    geom_point(size = 4) +
    geom_errorbar(aes(ymin = CI_lower, ymax = CI_upper), width = 0.2) +
    geom_hline(yintercept = 1.5, linetype = "dashed", color = "red",
              linewidth = 1) +
    annotate("text", x = 1.5, y = 1.5, label = "True Effect",
            vjust = -0.5, color = "red") +
    labs(y = "Estimated Treatment Effect", x = "Instrument Strength",
         title = "Weak vs Strong Instruments") +
    theme_minimal() +
    theme(text = element_text(size = 12))

  print(p)
  ggsave("iv_weak_strong_comparison_R.png", width = 7, height = 5, dpi = 150)
}

# ============================================
# Example 3: Multiple Instruments
# ============================================

example_multiple_instruments <- function() {
  cat("\nExample 3: Multiple Instruments (Overidentification)\n")
  cat("===================================================\n\n")

  set.seed(456)
  n <- 1000

  # Two instruments
  Z1 <- rbinom(n, 1, 0.5)
  Z2 <- rbinom(n, 1, 0.5)

  # Unobserved confounder
  U <- rnorm(n, 0, 1)

  # Treatment
  D <- 0.5 * Z1 + 0.4 * Z2 + 0.3 * U + rnorm(n, 0, 0.5)

  # Outcome
  Y <- 1.5 * D + 0.3 * U + rnorm(n, 0, 1)

  df <- data.frame(Y = Y, D = D, Z1 = Z1, Z2 = Z2)

  # IV with two instruments
  iv_model <- ivreg(Y ~ D | Z1 + Z2, data = df)

  cat("IV with Multiple Instruments:\n")
  print(summary(iv_model, diagnostics = TRUE))

  # Sargan test automatically included in diagnostics
}

# ============================================
# Run all examples
# ============================================

if (sys.nframe() == 0) {
  # Only run if script is executed directly (not sourced)

  cat("\n")
  cat("=" * 70, "\n")
  cat("Instrumental Variables Examples in R\n")
  cat("=" * 70, "\n\n")

  example_returns_to_schooling()
  example_weak_instruments()
  example_multiple_instruments()

  cat("\nAll examples completed successfully!\n")
}
