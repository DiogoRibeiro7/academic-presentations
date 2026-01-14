#!/bin/bash

# Script to compile all LaTeX presentations and exercises

echo "Compiling all LaTeX documents..."

# Array of presentations
presentations=(
  "05-time-series/time-series-forecasting/presentation/time_series_beamer"
  "06-advanced-topics/explainable-ai/presentation/interpretability_beamer"
  "02-deep-learning/deep-learning-fundamentals/presentation/deep_learning_beamer"
  "02-deep-learning/reinforcement-learning/presentation/rl_beamer"
  "01-foundations/optimization/presentation/optimization_beamer"
  "03-bayesian-methods/mcmc/presentation/mcmc_beamer"
  "04-causal-inference/causal-inference-fundamentals/presentation/causal_inference_beamer"
  "01-foundations/statistical-modeling/presentation/statistical_learning_beamer"
  "03-bayesian-methods/bayesian-machine-learning/presentation/bayesian_ml_beamer"
  "01-foundations/feature-engineering/presentation/feature_engineering_beamer"
  "04-causal-inference/ab-testing/presentation/a_b_testing_interview"
  "01-foundations/pca/presentation/pca"
  "00-programming-fundamentals/r-programming/presentation/R_programming"
)

# Array of exercises
exercises=(
  "03-bayesian-methods/mcmc/exercises/mcmc_exercises"
  "04-causal-inference/causal-inference-fundamentals/exercises/causal_inference_exercises"
)

# Compile presentations
for doc in "${presentations[@]}"; do
  dir=$(dirname "$doc")
  file=$(basename "$doc")
  echo "Compiling $file..."
  cd "$dir" || exit
  latexmk -pdf -interaction=nonstopmode -halt-on-error "$file.tex"
  if [ $? -eq 0 ]; then
    echo "✓ Successfully compiled $file.pdf"
  else
    echo "✗ Failed to compile $file"
  fi
  cd - > /dev/null || exit
done

# Compile exercises
for doc in "${exercises[@]}"; do
  dir=$(dirname "$doc")
  file=$(basename "$doc")
  echo "Compiling $file..."
  cd "$dir" || exit
  latexmk -pdf -interaction=nonstopmode -halt-on-error "$file.tex"
  if [ $? -eq 0 ]; then
    echo "✓ Successfully compiled $file.pdf"
  else
    echo "✗ Failed to compile $file"
  fi
  cd - > /dev/null || exit
done

echo "Compilation complete!"
