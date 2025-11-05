# Difference-in-Differences (DiD) in R
# =====================================
#
# Implementation using fixest for two-way fixed effects (TWFE)
#
# References:
#   Card & Krueger (1994), Bertrand et al. (2004)

# Load required packages
suppressPackageStartupMessages({
  library(fixest)   # For fast fixed effects estimation
  library(did)      # For Callaway-Sant'Anna estimator
  library(ggplot2)
  library(dplyr)
  library(tidyr)
  library(broom)
})

# ============================================
# Simulate DiD Data
# ============================================

simulate_did_data <- function(n_units = 500, n_periods = 10,
                             treatment_time = 5, treatment_effect = 5.0,
                             seed = 42) {
  #' Simulate panel data for DiD
  #'
  #' @param n_units Number of units
  #' @param n_periods Number of time periods
  #' @param treatment_time When treatment starts
  #' @param treatment_effect True ATT
  #' @return data.frame with panel data

  set.seed(seed)

  # Unit fixed effects
  unit_fe <- rnorm(n_units, 10, 2)

  # Treatment assignment (50% treated)
  treated_units <- sample(1:n_units, n_units/2)
  treated <- rep(0, n_units)
  treated[treated_units] <- 1

  # Create panel
  data <- expand.grid(
    unit_id = 1:n_units,
    time = 1:n_periods
  )

  data$treated <- treated[data$unit_id]
  data$post <- as.integer(data$time >= treatment_time)
  data$treat_post <- data$treated * data$post

  # Outcome with unit FE, time trends, and treatment effect
  data$outcome <- unit_fe[data$unit_id] +
                 3 * data$time +  # Common time trend
                 treatment_effect * data$treat_post +  # Treatment effect
                 rnorm(nrow(data), 0, 1)

  data
}

# ============================================
# 2x2 DiD Estimation
# ============================================

estimate_did_2x2 <- function(data, outcome = "outcome",
                             treated = "treated", post = "post",
                             unit_id = "unit_id") {
  #' Estimate 2x2 DiD (two periods, two groups)
  #'
  #' @param data data.frame with panel data
  #' @param outcome Name of outcome variable
  #' @param treated Name of treatment indicator
  #' @param post Name of post-treatment indicator
  #' @param unit_id Name of unit identifier
  #' @return List with results

  # Calculate group-time means
  means <- data %>%
    group_by(!!sym(treated), !!sym(post)) %>%
    summarise(mean_outcome = mean(!!sym(outcome)), .groups = "drop")

  # Extract means
  Y_11 <- means %>% filter(!!sym(treated) == 1, !!sym(post) == 1) %>%
          pull(mean_outcome)
  Y_10 <- means %>% filter(!!sym(treated) == 1, !!sym(post) == 0) %>%
          pull(mean_outcome)
  Y_01 <- means %>% filter(!!sym(treated) == 0, !!sym(post) == 1) %>%
          pull(mean_outcome)
  Y_00 <- means %>% filter(!!sym(treated) == 0, !!sym(post) == 0) %>%
          pull(mean_outcome)

  # DiD estimator
  att <- (Y_11 - Y_10) - (Y_01 - Y_00)

  # Regression approach for inference
  data$treat_post <- data[[treated]] * data[[post]]

  # With cluster-robust SE at unit level
  did_reg <- feols(
    as.formula(paste(outcome, "~", treated, "+", post, "+ treat_post")),
    data = data,
    cluster = unit_id
  )

  list(
    att = att,
    model = did_reg,
    means = means
  )
}

# ============================================
# Two-Way Fixed Effects (TWFE) DiD
# ============================================

estimate_twfe_did <- function(data, outcome = "outcome",
                              treat_post = "treat_post",
                              unit_id = "unit_id", time = "time") {
  #' Estimate DiD using two-way fixed effects
  #'
  #' @param data Panel data
  #' @param outcome Outcome variable
  #' @param treat_post Treatment x Post interaction
  #' @param unit_id Unit identifier
  #' @param time Time variable
  #' @return feols object

  formula_str <- paste(outcome, "~", treat_post, "| ", unit_id, "+", time)

  twfe_model <- feols(
    as.formula(formula_str),
    data = data,
    cluster = unit_id
  )

  twfe_model
}

# ============================================
# Event Study (Dynamic DiD)
# ============================================

estimate_event_study <- function(data, outcome = "outcome",
                                 treated = "treated", time = "time",
                                 treatment_time = 5, unit_id = "unit_id",
                                 pre_periods = 4, post_periods = 5) {
  #' Estimate event study / dynamic DiD
  #'
  #' @param data Panel data
  #' @param outcome Outcome variable
  #' @param treated Treatment indicator
  #' @param time Time variable
  #' @param treatment_time Time when treatment starts
  #' @param unit_id Unit identifier
  #' @param pre_periods Number of pre-treatment periods
  #' @param post_periods Number of post-treatment periods
  #' @return feols object

  # Create relative time variable
  data$rel_time <- data[[time]] - treatment_time
  data$rel_time[data[[treated]] == 0] <- 0  # Set to 0 for never-treated

  # Create event time dummies (excluding -1 as base period)
  event_times <- c(-pre_periods:(-2), 0:post_periods)

  for (t in event_times) {
    data[[paste0("treat_", t)]] <- as.integer(
      data[[treated]] == 1 & data$rel_time == t
    )
  }

  # Event study formula
  treat_vars <- paste0("treat_", event_times)
  formula_str <- paste(
    outcome, "~",
    paste(treat_vars, collapse = " + "),
    "|", unit_id, "+", time
  )

  event_model <- feols(
    as.formula(formula_str),
    data = data,
    cluster = unit_id
  )

  event_model
}

# ============================================
# Visualization Functions
# ============================================

plot_did_trends <- function(data, results, outcome = "outcome",
                           treated = "treated", time = "time") {
  #' Plot parallel trends
  #'
  #' @param data Panel data
  #' @param results DiD results object
  #' @param outcome Outcome variable
  #' @param treated Treatment indicator
  #' @param time Time variable

  # Calculate time-series means by group
  trends <- data %>%
    group_by(!!sym(time), !!sym(treated)) %>%
    summarise(mean_outcome = mean(!!sym(outcome)), .groups = "drop") %>%
    mutate(group = ifelse(!!sym(treated) == 1, "Treated", "Control"))

  p <- ggplot(trends, aes(x = !!sym(time), y = mean_outcome,
                         color = group, group = group)) +
    geom_line(linewidth = 1.2) +
    geom_point(size = 3) +
    geom_vline(xintercept = 5, linetype = "dashed", alpha = 0.5) +
    annotate("text", x = 5, y = max(trends$mean_outcome),
            label = "Treatment", vjust = -0.5) +
    scale_color_manual(values = c("Control" = "blue", "Treated" = "red")) +
    labs(
      x = "Time Period",
      y = "Average Outcome",
      title = "Difference-in-Differences: Parallel Trends",
      color = "Group"
    ) +
    theme_minimal() +
    theme(
      text = element_text(size = 12),
      legend.position = "bottom"
    )

  print(p)
  invisible(p)
}

plot_event_study <- function(event_model, pre_periods = 4, post_periods = 5) {
  #' Plot event study coefficients
  #'
  #' @param event_model Event study feols object
  #' @param pre_periods Number of pre-treatment periods
  #' @param post_periods Number of post-treatment periods

  # Extract coefficients
  coefs <- tidy(event_model, conf.int = TRUE)

  # Parse relative time from variable names
  coefs$rel_time <- as.numeric(gsub("treat_", "", coefs$term))

  # Add base period (-1) at zero
  base_period <- data.frame(
    term = "treat_-1",
    estimate = 0,
    std.error = 0,
    statistic = 0,
    p.value = 1,
    conf.low = 0,
    conf.high = 0,
    rel_time = -1
  )

  coefs <- bind_rows(coefs, base_period) %>%
    arrange(rel_time)

  # Plot
  p <- ggplot(coefs, aes(x = rel_time, y = estimate)) +
    geom_line(linewidth = 1) +
    geom_point(size = 3) +
    geom_errorbar(aes(ymin = conf.low, ymax = conf.high), width = 0.2) +
    geom_hline(yintercept = 0, linetype = "dashed", color = "red") +
    geom_vline(xintercept = -0.5, linetype = "dotted", alpha = 0.5) +
    annotate("text", x = -0.5, y = max(coefs$conf.high),
            label = "Treatment", vjust = -0.5, size = 3) +
    labs(
      x = "Periods Relative to Treatment",
      y = "Estimated Effect",
      title = "Event Study Plot",
      subtitle = "Point estimates with 95% confidence intervals"
    ) +
    theme_minimal() +
    theme(text = element_text(size = 12))

  print(p)
  invisible(p)
}

# ============================================
# Example 1: Minimum Wage and Employment
# ============================================

example_minimum_wage <- function() {
  cat("Example 1: Minimum Wage and Employment (Card & Krueger)\n")
  cat("========================================================\n\n")

  set.seed(789)
  n <- 400

  # New Jersey (treated) vs Pennsylvania (control)
  state <- sample(c("NJ", "PA"), n, replace = TRUE, prob = c(0.5, 0.5))
  treated <- as.integer(state == "NJ")

  # Create panel (before and after minimum wage increase)
  data <- data.frame(
    unit_id = rep(1:n, 2),
    state = rep(state, 2),
    treated = rep(treated, 2),
    time = rep(c(0, 1), each = n)
  )

  data$post <- data$time

  # Employment (FTE employees)
  baseline <- rnorm(n, 20, 5)
  data$outcome <- rep(baseline, 2) +
                 2 * data$time +  # Time trend
                 3.0 * data$treated * data$post +  # Treatment effect
                 rnorm(nrow(data), 0, 2)

  # Estimate DiD
  cat("2x2 DiD Estimation:\n")
  cat("-" * 70, "\n")
  did_results <- estimate_did_2x2(data)

  cat(sprintf("DiD Estimate (ATT): %.3f\n", did_results$att))
  cat("\nRegression Results:\n")
  print(summary(did_results$model))

  # Plot
  p <- plot_did_trends(data, did_results)
  ggsave("did_minimum_wage_R.png", plot = p, width = 10, height = 6, dpi = 150)

  invisible(did_results)
}

# ============================================
# Example 2: Event Study
# ============================================

example_event_study <- function() {
  cat("\nExample 2: Event Study (Dynamic DiD)\n")
  cat("=====================================\n\n")

  # Simulate multi-period data
  data <- simulate_did_data(n_units = 300, n_periods = 10,
                           treatment_time = 5, treatment_effect = 5.0)

  # Estimate event study
  event_model <- estimate_event_study(data, treatment_time = 5,
                                     pre_periods = 4, post_periods = 5)

  cat("Event Study Results:\n")
  print(summary(event_model))

  # Plot
  p <- plot_event_study(event_model)
  ggsave("did_event_study_R.png", plot = p, width = 10, height = 6, dpi = 150)

  invisible(event_model)
}

# ============================================
# Example 3: TWFE with Multiple Treatment Times
# ============================================

example_staggered_adoption <- function() {
  cat("\nExample 3: Staggered Treatment Adoption\n")
  cat("========================================\n\n")

  set.seed(999)

  n_units <- 500
  n_periods <- 10

  # Staggered treatment adoption
  treatment_times <- sample(c(4, 6, 8, Inf), n_units, replace = TRUE,
                            prob = c(0.25, 0.25, 0.25, 0.25))

  # Create panel
  data <- expand.grid(
    unit_id = 1:n_units,
    time = 1:n_periods
  )

  data$treatment_time <- treatment_times[data$unit_id]
  data$treated <- as.integer(
    data$time >= data$treatment_time & is.finite(data$treatment_time)
  )

  # Outcome
  unit_fe <- rnorm(n_units, 10, 2)
  data$outcome <- unit_fe[data$unit_id] +
                 2 * data$time +
                 4.0 * data$treated +
                 rnorm(nrow(data), 0, 1)

  # TWFE estimation
  twfe_model <- feols(outcome ~ treated | unit_id + time,
                     data = data, cluster = ~ unit_id)

  cat("Two-Way Fixed Effects Results:\n")
  print(summary(twfe_model))

  cat("\nNote: With staggered treatment and heterogeneous effects,\n")
  cat("TWFE may give biased estimates. Consider Callaway-Sant'Anna\n")
  cat("or Sun-Abraham estimators instead.\n")

  invisible(twfe_model)
}

# ============================================
# Test Parallel Trends Assumption
# ============================================

test_parallel_trends <- function(data, outcome = "outcome",
                                treated = "treated", time = "time",
                                treatment_time = 5) {
  #' Test parallel trends in pre-treatment period
  #'
  #' @param data Panel data
  #' @param outcome Outcome variable
  #' @param treated Treatment indicator
  #' @param time Time variable
  #' @param treatment_time When treatment starts

  # Pre-treatment data only
  data_pre <- data %>% filter(!!sym(time) < treatment_time)

  # Test for differential trends
  data_pre$time_treat <- data_pre[[time]] * data_pre[[treated]]

  trend_test <- feols(
    as.formula(paste(outcome, "~ time * ", treated)),
    data = data_pre,
    cluster = ~ unit_id
  )

  cat("\n")
  cat("=" * 70, "\n")
  cat("Parallel Trends Test (Pre-Treatment Period)\n")
  cat("=" * 70, "\n")
  print(summary(trend_test))

  cat("\nIf the interaction coefficient (time:", treated, ") is insignificant,\n")
  cat("this supports the parallel trends assumption.\n")

  invisible(trend_test)
}

# ============================================
# Run all examples
# ============================================

if (sys.nframe() == 0) {
  cat("\n")
  cat("=" * 70, "\n")
  cat("Difference-in-Differences Examples in R\n")
  cat("=" * 70, "\n\n")

  example_minimum_wage()
  example_event_study()
  example_staggered_adoption()

  # Test parallel trends for simulated data
  data_test <- simulate_did_data(n_units = 300, n_periods = 10,
                                treatment_time = 5)
  test_parallel_trends(data_test, treatment_time = 5)

  cat("\nAll examples completed successfully!\n")
}
