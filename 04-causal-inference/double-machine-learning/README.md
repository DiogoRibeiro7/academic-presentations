# double-machine-learning

## Overview

This topic develops Double Machine Learning (DML) for causal and structural parameters when high-dimensional or flexible nuisance models are estimated with machine learning.

## Scope

- partially linear regression;
- nuisance functions;
- residualization / partialling out;
- Neyman orthogonality;
- cross-fitting;
- product-rate conditions;
- ATE and PLR scores;
- doubly robust scores;
- regularization bias;
- inference after ML;
- overlap and identification limits.

## Design principle

Machine learning is used to estimate nuisance functions, not to replace the causal identification argument. Orthogonal scores and cross-fitting reduce sensitivity to nuisance-estimation error, but they do not repair confounding, weak overlap, or invalid instruments.
