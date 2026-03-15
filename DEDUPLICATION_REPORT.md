# Deduplication Report - Phase 0

**Generated**: 2025-11-15  
**Status**: Finalized baseline for Phase 1 planning  
**Purpose**: Classify overlapping content and define migration-safe decisions

## Executive Summary

Initial analysis identified overlap between topic directories and `/data_science_applications/`.  
Final classification shows two intentional content types:

1. Standalone presentations (`\documentclass`) for topic-specific delivery.
2. Modular sections (`\section{}`-based) for a composite course deck.

Result: several apparent duplicates are intentional parallel assets, not true duplicates.

## Final Classification

### Category A: Keep Both (Intentional Parallel Versions)

| Topic | Standalone Path | Modular Path | Final Decision |
|------|------|------|------|
| Deep Learning | `/deep_learning/deep_learning_beamer.tex` | `/data_science_applications/deep_learning_beamer.tex` | Keep both (standalone + modular) |
| Time Series | `/time_series/time_series_beamer.tex` | `/data_science_applications/time_series_beamer.tex` | Keep both (standalone + modular) |
| Explainable AI | `/explainable_ai/interpretability_beamer.tex` | `/data_science_applications/explainable_ai_beamer.tex` | Keep both (different naming, distinct use cases) |

### Category B: Move Standalone Content to Domain Structure

| Content | Current Path | Destination |
|------|------|------|
| Causal Inference | `/data_science_applications/causal_inference_beamer.tex` | `/04-causal-inference/causal-inference-fundamentals/presentation/` |
| Feature Engineering | `/data_science_applications/feature_engineering_beamer.tex` | `/01-foundations/feature-engineering/presentation/` |
| Statistical Learning | `/data_science_applications/statistical_learning_beamer.tex` | `/01-foundations/statistical-modeling/presentation/` |

### Category C: Composite Course Assets

These modular sections should be grouped under:

`/08-data-science-applications-course/presentation/sections/`

Files:
- `deep_learning_beamer.tex` -> `deep_learning_section.tex`
- `time_series_beamer.tex` -> `time_series_section.tex`
- `explainable_ai_beamer.tex` -> `explainable_ai_section.tex`
- `mlops_deployment_beamer.tex` -> `mlops_deployment_section.tex`

### Category D: Enhancement and Documentation Assets

| File Type | Source Area | Destination |
|------|------|------|
| Enhancement `.tex` files | `/data_science_applications/` | Same topic destination as parent presentation |
| Enhancement guides `.md` | `/data_science_applications/` | `/docs/enhancement-guides/` |
| Competency matrices | `/data_science_applications/COMPETENCY_MATRICES.md` | `/learning-paths/competency-matrices/` |

## True Conflict Review (Post-Classification)

No blocking deduplication conflicts remain for Phase 0 sign-off.

Notes:
1. A/B testing appears in both `/data_science_applications/` and `/interview/`; treat as separate audiences unless content convergence is explicitly required.
2. Statistical modeling naming differences should be normalized in a later documentation pass, not blocked in dedup phase.

## Migration Guidance

### Safe to automate

1. Move standalone presentations from `/data_science_applications/` into the numbered domain structure.
2. Move modular section files into `/08-data-science-applications-course/`.
3. Move enhancement guides to `/docs/enhancement-guides/`.
4. Preserve both standalone and modular versions for Deep Learning, Time Series, and Explainable AI.

### Keep as manual checks (non-blocking)

1. Decide whether A/B testing should remain split (`interview` vs curriculum).
2. Normalize naming conventions for statistical learning/modeling assets.

## Decision Matrix

| Content Area | Action | Risk | Phase |
|------|------|------|------|
| Deep Learning | Keep both versions | Low | Phase 1+ |
| Time Series | Keep both versions | Low | Phase 1+ |
| Explainable AI | Keep both versions | Low | Phase 1+ |
| Causal Inference | Move standalone + enhancements | Low | Phase 1 |
| Feature Engineering | Consolidate distributed assets | Medium | Phase 2 |
| Statistical Learning | Move and normalize naming | Medium | Phase 2 |
| MLOps | Move modular section to course structure | Low | Phase 1 |
| A/B Testing | Keep split unless merge is requested | Medium | Phase 2 |
| Capstone/Industry Focus | Move to `/07-capstone-projects/` | Low | Phase 1 |

## Closure

**Phase 0 Deduplication Status**: Complete  
**Blocking Issues**: None  
**Ready for**: Phase 1 structure creation and controlled migration batches
