# Feature Engineering Pipeline in R
# ==================================
#
# Comprehensive feature engineering examples for machine learning

# Load required packages
suppressPackageStartupMessages({
  library(dplyr)
  library(tidyr)
  library(caret)        # For preprocessing
  library(recipes)      # For feature engineering pipelines
  library(ggplot2)
  library(corrplot)
  library(mice)         # For missing data imputation
  library(randomForest)
})

# ============================================
# Missing Value Imputation
# ============================================

demonstrate_imputation <- function() {
  cat("=" * 70, "\n")
  cat("Missing Value Imputation Strategies\n")
  cat("=" * 70, "\n\n")

  set.seed(42)
  n <- 1000

  # Create data with missing values
  df <- data.frame(
    age = rnorm(n, 40, 15),
    income = rlnorm(n, 10, 1),
    score = rnorm(n, 70, 15)
  )

  # Introduce missing values (20% missing)
  missing_indices <- sample(1:n, 0.2 * n)
  df$income[missing_indices] <- NA

  cat(sprintf("Missing values: %d / %d (%.1f%%)\n",
             sum(is.na(df$income)), n, 100 * mean(is.na(df$income))))

  # Method 1: Mean imputation
  df$income_mean <- df$income
  df$income_mean[is.na(df$income_mean)] <- mean(df$income, na.rm = TRUE)

  # Method 2: Median imputation
  df$income_median <- df$income
  df$income_median[is.na(df$income_median)] <- median(df$income, na.rm = TRUE)

  # Method 3: KNN imputation (using caret)
  preproc <- preProcess(df[, "income", drop = FALSE],
                       method = "knnImpute", k = 5)
  df$income_knn <- predict(preproc, df[, "income", drop = FALSE])[[1]]

  # Method 4: MICE (Multiple Imputation)
  mice_model <- mice(df[, c("age", "income", "score")],
                    m = 1, method = "pmm", seed = 42, printFlag = FALSE)
  df$income_mice <- complete(mice_model)$income

  # Compare methods
  cat("\nImputation method comparison:\n")
  cat(sprintf("Mean:   %.2f\n", mean(df$income_mean)))
  cat(sprintf("Median: %.2f\n", mean(df$income_median)))
  cat(sprintf("KNN:    %.2f\n", mean(df$income_knn)))
  cat(sprintf("MICE:   %.2f\n", mean(df$income_mice)))
  cat(sprintf("Original (w/o NA): %.2f\n", mean(df$income, na.rm = TRUE)))

  invisible(df)
}

# ============================================
# Categorical Encoding
# ============================================

demonstrate_encoding <- function() {
  cat("\n", "=" * 70, "\n")
  cat("Categorical Encoding Strategies\n")
  cat("=" * 70, "\n\n")

  # Sample data
  df <- data.frame(
    city = rep(c("NYC", "LA", "Chicago"), length.out = 100),
    education = rep(c("HS", "BS", "MS", "PhD"), length.out = 100),
    salary = rnorm(100, 70000, 20000),
    stringsAsFactors = FALSE
  )

  cat("Original data sample:\n")
  print(head(df))

  # 1. Label Encoding (factor levels)
  df$city_label <- as.numeric(factor(df$city))

  # 2. One-Hot Encoding
  dummy_vars <- dummyVars(~ city + education, data = df, fullRank = TRUE)
  df_onehot <- predict(dummy_vars, df)
  df_encoded <- cbind(df, df_onehot)

  # 3. Ordinal Encoding (for education)
  education_order <- c("HS", "BS", "MS", "PhD")
  df$education_ordinal <- match(df$education, education_order)

  # 4. Target Encoding (mean encoding)
  city_means <- df %>%
    group_by(city) %>%
    summarise(mean_salary = mean(salary), .groups = "drop")

  df <- df %>%
    left_join(city_means, by = "city") %>%
    rename(city_target_encoded = mean_salary)

  cat("\n\nEncoding results:\n")
  cat("\nLabel encoding (first 5 rows):\n")
  print(head(df[, c("city", "city_label")], 5))

  cat("\nOrdinal encoding (first 5 rows):\n")
  print(head(df[, c("education", "education_ordinal")], 5))

  cat("\nTarget encoding (first 5 rows):\n")
  print(head(df[, c("city", "city_target_encoded")], 5))

  invisible(df)
}

# ============================================
# Feature Scaling
# ============================================

demonstrate_scaling <- function() {
  cat("\n", "=" * 70, "\n")
  cat("Feature Scaling Strategies\n")
  cat("=" * 70, "\n\n")

  set.seed(42)
  df <- data.frame(
    feature1 = rnorm(100, 50, 10),
    feature2 = rnorm(100, 1000, 500),
    feature3 = rexp(100, 0.1)
  )

  cat("Original data statistics:\n")
  print(summary(df))

  # 1. Standardization (Z-score normalization)
  df_standard <- as.data.frame(scale(df))
  names(df_standard) <- paste0(names(df), "_standard")

  # 2. Min-Max scaling
  preproc_minmax <- preProcess(df, method = "range")
  df_minmax <- predict(preproc_minmax, df)
  names(df_minmax) <- paste0(names(df), "_minmax")

  # 3. Robust scaling (median and IQR)
  robust_scale <- function(x) {
    (x - median(x)) / IQR(x)
  }
  df_robust <- as.data.frame(lapply(df, robust_scale))
  names(df_robust) <- paste0(names(df), "_robust")

  cat("\n\nStandardized data statistics:\n")
  print(summary(df_standard))

  invisible(list(standard = df_standard, minmax = df_minmax, robust = df_robust))
}

# ============================================
# Feature Creation with recipes
# ============================================

create_feature_pipeline <- function() {
  cat("\n", "=" * 70, "\n")
  cat("Feature Engineering Pipeline with recipes\n")
  cat("=" * 70, "\n\n")

  # Sample data
  set.seed(123)
  n <- 500

  df <- data.frame(
    age = rnorm(n, 40, 15),
    income = rlnorm(n, 10, 1),
    education = sample(c("HS", "BS", "MS", "PhD"), n, replace = TRUE),
    city = sample(c("NYC", "LA", "Chicago", "Houston"), n, replace = TRUE),
    outcome = rbinom(n, 1, 0.5)
  )

  # Introduce missing values
  df$income[sample(1:n, 0.1 * n)] <- NA

  # Create recipe
  rec <- recipe(outcome ~ ., data = df) %>%
    # Impute missing values
    step_impute_median(all_numeric(), -all_outcomes()) %>%
    step_impute_mode(all_nominal(), -all_outcomes()) %>%

    # Create interaction terms
    step_interact(terms = ~ age:income) %>%

    # Create polynomial features
    step_poly(age, degree = 2) %>%

    # Log transform
    step_log(income, offset = 1) %>%

    # One-hot encoding
    step_dummy(all_nominal(), -all_outcomes(), one_hot = FALSE) %>%

    # Standardize
    step_normalize(all_numeric(), -all_outcomes()) %>%

    # Remove zero-variance features
    step_zv(all_predictors())

  # Prepare recipe
  rec_prepped <- prep(rec, training = df)

  # Apply to data
  df_processed <- bake(rec_prepped, new_data = df)

  cat("Original data shape: ", dim(df), "\n")
  cat("Processed data shape:", dim(df_processed), "\n")
  cat("\nProcessed features:\n")
  print(names(df_processed))

  invisible(list(recipe = rec_prepped, data = df_processed))
}

# ============================================
# Feature Selection
# ============================================

demonstrate_feature_selection <- function() {
  cat("\n", "=" * 70, "\n")
  cat("Feature Selection Methods\n")
  cat("=" * 70, "\n\n")

  # Load sample data
  data(iris)
  df <- iris
  df$Species <- as.factor(df$Species)

  # Method 1: Correlation-based filtering
  cor_matrix <- cor(df[, 1:4])
  cat("Correlation matrix:\n")
  print(round(cor_matrix, 2))

  # Find highly correlated features (|r| > 0.8)
  high_cor <- findCorrelation(cor_matrix, cutoff = 0.8)
  if (length(high_cor) > 0) {
    cat(sprintf("\nHighly correlated features to remove: %s\n",
               paste(names(df)[high_cor], collapse = ", ")))
  }

  # Method 2: Random Forest importance
  set.seed(42)
  rf_model <- randomForest(Species ~ ., data = df, importance = TRUE, ntree = 500)

  importance_df <- data.frame(
    Feature = rownames(importance(rf_model)),
    Importance = importance(rf_model)[, "MeanDecreaseGini"]
  )
  importance_df <- importance_df[order(-importance_df$Importance), ]

  cat("\nRandom Forest Feature Importance:\n")
  print(importance_df)

  # Method 3: Recursive Feature Elimination (RFE)
  control <- rfeControl(functions = rfFuncs, method = "cv", number = 5)
  rfe_results <- rfe(df[, 1:4], df$Species,
                    sizes = c(1:4),
                    rfeControl = control)

  cat("\n\nRFE Results:\n")
  print(rfe_results)
  cat("\nOptimal features:", predictors(rfe_results), "\n")

  # Plot importance
  varImpPlot(rf_model, main = "Feature Importance from Random Forest")

  invisible(list(rf = rf_model, rfe = rfe_results))
}

# ============================================
# Dimensionality Reduction (PCA)
# ============================================

demonstrate_pca <- function() {
  cat("\n", "=" * 70, "\n")
  cat("Principal Component Analysis (PCA)\n")
  cat("=" * 70, "\n\n")

  # Load data
  data(iris)
  df_numeric <- iris[, 1:4]

  # Standardize data
  df_scaled <- scale(df_numeric)

  # Apply PCA
  pca_result <- prcomp(df_scaled, center = FALSE, scale. = FALSE)

  # Summary
  cat("PCA Summary:\n")
  print(summary(pca_result))

  # Variance explained
  var_explained <- pca_result$sdev^2 / sum(pca_result$sdev^2)
  cumvar <- cumsum(var_explained)

  cat("\n\nVariance explained by each PC:\n")
  for (i in 1:4) {
    cat(sprintf("PC%d: %.2f%% (cumulative: %.2f%%)\n",
               i, 100 * var_explained[i], 100 * cumvar[i]))
  }

  # Scree plot
  par(mfrow = c(1, 2))

  # Variance explained
  barplot(var_explained, names.arg = paste0("PC", 1:4),
         main = "Variance Explained by Each PC",
         ylab = "Proportion of Variance",
         col = "steelblue")

  # Cumulative variance
  plot(1:4, cumvar, type = "b", pch = 19,
      main = "Cumulative Variance Explained",
      xlab = "Number of Components",
      ylab = "Cumulative Proportion",
      ylim = c(0, 1))
  abline(h = 0.95, col = "red", lty = 2)
  legend("bottomright", legend = "95% threshold", col = "red", lty = 2)

  par(mfrow = c(1, 1))

  # Biplot
  biplot(pca_result, scale = 0, cex = 0.7,
        main = "PCA Biplot")

  invisible(pca_result)
}

# ============================================
# Complete End-to-End Example
# ============================================

complete_pipeline_example <- function() {
  cat("\n", "=" * 70, "\n")
  cat("Complete Feature Engineering Pipeline\n")
  cat("=" * 70, "\n\n")

  # Create synthetic data
  set.seed(456)
  n <- 1000

  df <- data.frame(
    age = rnorm(n, 40, 15),
    income = rlnorm(n, 10, 1),
    education = sample(c("HS", "BS", "MS", "PhD"), n, replace = TRUE,
                      prob = c(0.3, 0.4, 0.2, 0.1)),
    city = sample(c("NYC", "LA", "Chicago", "Houston"), n, replace = TRUE),
    experience = rnorm(n, 10, 5),
    outcome = rbinom(n, 1, 0.5)
  )

  # Introduce missing values
  df$income[sample(1:n, 0.15 * n)] <- NA
  df$experience[sample(1:n, 0.1 * n)] <- NA

  cat(sprintf("Dataset: %d rows, %d columns\n", nrow(df), ncol(df)))
  cat("\nMissing values:\n")
  print(colSums(is.na(df)))

  # Build comprehensive recipe
  rec <- recipe(outcome ~ ., data = df) %>%
    # Missing value imputation
    step_impute_median(all_numeric_predictors()) %>%
    step_impute_mode(all_nominal_predictors()) %>%

    # Feature engineering
    step_interact(terms = ~ age:experience) %>%
    step_poly(age, degree = 2, options = list(raw = TRUE)) %>%
    step_log(income, offset = 1, base = 10) %>%

    # Binning
    step_discretize(experience, num_breaks = 4) %>%

    # Encoding
    step_dummy(all_nominal_predictors(), one_hot = FALSE) %>%

    # Scaling
    step_normalize(all_numeric_predictors()) %>%

    # Remove near-zero variance features
    step_nzv(all_predictors()) %>%

    # Remove highly correlated features
    step_corr(all_numeric_predictors(), threshold = 0.9)

  # Prepare and apply recipe
  rec_prepped <- prep(rec, training = df)
  df_processed <- bake(rec_prepped, new_data = df)

  cat("\n\nProcessed data:\n")
  cat(sprintf("Shape: %d rows, %d columns\n",
             nrow(df_processed), ncol(df_processed)))
  cat("\nFeature names:\n")
  print(names(df_processed))

  # Train model
  library(randomForest)
  rf_model <- randomForest(outcome ~ ., data = df_processed,
                          ntree = 500, importance = TRUE)

  cat("\n\nRandom Forest Model Performance:\n")
  print(rf_model)

  # Feature importance
  imp <- importance(rf_model)
  imp_sorted <- imp[order(-imp[, "MeanDecreaseGini"]), , drop = FALSE]

  cat("\nTop 10 Most Important Features:\n")
  print(head(imp_sorted, 10))

  invisible(list(recipe = rec_prepped, model = rf_model, data = df_processed))
}

# ============================================
# Run all examples
# ============================================

if (sys.nframe() == 0) {
  cat("\n")
  cat("=" * 70, "\n")
  cat("Feature Engineering Pipeline Examples in R\n")
  cat("=" * 70, "\n\n")

  demonstrate_imputation()
  demonstrate_encoding()
  demonstrate_scaling()
  create_feature_pipeline()
  demonstrate_feature_selection()
  demonstrate_pca()
  complete_pipeline_example()

  cat("\n\nAll feature engineering examples completed!\n")
}
