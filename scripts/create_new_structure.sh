#!/bin/bash
# create_new_structure.sh
# Phase 1: Create new directory structure for reorganized repository

set -e
echo "=== Phase 1: Creating New Directory Structure ==="
echo ""

# Domain 00: Programming Fundamentals
echo "Creating Domain 00: Programming Fundamentals..."
mkdir -p 00-programming-fundamentals/r-programming/{presentation,code,exercises}

# Domain 01: Foundations
echo "Creating Domain 01: Foundations..."
mkdir -p 01-foundations/statistical-modeling/{presentation,code,exercises}
mkdir -p 01-foundations/feature-engineering/presentation
mkdir -p 01-foundations/feature-engineering/code/{python,r}
mkdir -p 01-foundations/feature-engineering/exercises
mkdir -p 01-foundations/pca/{presentation,code,exercises}
mkdir -p 01-foundations/optimization/{presentation,code,exercises}

# Domain 02: Deep Learning
echo "Creating Domain 02: Deep Learning..."
mkdir -p 02-deep-learning/deep-learning-fundamentals/{presentation,code,exercises}
mkdir -p 02-deep-learning/reinforcement-learning/{presentation,code,exercises}

# Domain 03: Bayesian Methods
echo "Creating Domain 03: Bayesian Methods..."
mkdir -p 03-bayesian-methods/bayesian-machine-learning/{presentation,code,exercises}
mkdir -p 03-bayesian-methods/mcmc/presentation
mkdir -p 03-bayesian-methods/mcmc/code/{python,tests}
mkdir -p 03-bayesian-methods/mcmc/exercises

# Domain 04: Causal Inference
echo "Creating Domain 04: Causal Inference..."
mkdir -p 04-causal-inference/causal-inference-fundamentals/presentation
mkdir -p 04-causal-inference/causal-inference-fundamentals/code/{python,r}
mkdir -p 04-causal-inference/causal-inference-fundamentals/exercises
mkdir -p 04-causal-inference/ab-testing/{presentation,code,exercises}

# Domain 05: Time Series
echo "Creating Domain 05: Time Series..."
mkdir -p 05-time-series/time-series-forecasting/{presentation,code,exercises}

# Domain 06: Advanced Topics
echo "Creating Domain 06: Advanced Topics..."
mkdir -p 06-advanced-topics/explainable-ai/{presentation,code,exercises}
mkdir -p 06-advanced-topics/computer-science/{presentation,code,exercises}
mkdir -p 06-advanced-topics/mlops-deployment/{presentation,code,exercises}

# Domain 07: Capstone Projects
echo "Creating Domain 07: Capstone Projects..."
mkdir -p 07-capstone-projects/project-guides
mkdir -p 07-capstone-projects/prerequisites
mkdir -p 07-capstone-projects/industry-focus

# Domain 08: Data Science Applications Course
echo "Creating Domain 08: Data Science Applications Course..."
mkdir -p 08-data-science-applications-course/presentation/sections
mkdir -p 08-data-science-applications-course/assessments
mkdir -p 08-data-science-applications-course/exercises

# Shared Resources
echo "Creating shared resources..."
mkdir -p shared/theme
mkdir -p shared/bibliographies
mkdir -p shared/utilities

# Documentation
echo "Creating documentation structure..."
mkdir -p docs/enhancement-guides
mkdir -p docs/learning-paths/competency-matrices
mkdir -p docs/architecture
mkdir -p docs/teaching-guides

# Assessments (reorganize existing)
echo "Creating assessments structure..."
mkdir -p assessments/quizzes/{foundations,deep-learning,bayesian-methods,causal-inference}
mkdir -p assessments/exams/{midterm,final}
mkdir -p assessments/rubrics
mkdir -p assessments/self-assessment

echo ""
echo "✅ Directory structure created successfully!"
echo ""
echo "Next: Create README.md files for each domain and topic"
