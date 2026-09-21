#!/bin/bash

# Script to compile all LaTeX presentations and exercises

echo "Compiling all LaTeX documents..."

# Array of presentations
presentations=(
  # Canonical primary entry points
  "00-programming-fundamentals/r-programming/presentation/main"
  "01-foundations/feature-engineering/presentation/main"
  "01-foundations/optimization/presentation/main"
  "01-foundations/pca/presentation/main"
  "01-foundations/statistical-modeling/presentation/main"
  "02-deep-learning/deep-learning-fundamentals/presentation/main"
  "02-deep-learning/reinforcement-learning/presentation/main"
  "03-bayesian-methods/bayesian-machine-learning/presentation/main"
  "03-bayesian-methods/mcmc/presentation/main"
  "04-causal-inference/ab-testing/presentation/main"
  "04-causal-inference/causal-inference-fundamentals/presentation/main"
  "05-time-series/time-series-forecasting/presentation/main"
  "06-advanced-topics/ai-agents/presentation/main"
  "06-advanced-topics/computer-science/presentation/main"
  "06-advanced-topics/explainable-ai/presentation/main"
  "08-data-science-applications-course/presentation/main"

  # Additional standalone tracks
  "01-foundations/statistical-modeling/presentation/diogo_ribeiro_beamer_extended"
  "05-time-series/time-series-forecasting/presentation/ARMA_processes"
  "05-time-series/time-series-forecasting/presentation/stationary_ergodicity"
  "06-advanced-topics/computer-science/presentation/streaming_pipeline_processing"
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

