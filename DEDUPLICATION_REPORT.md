# Deduplication Report - Phase 0

**Generated**: 2025-11-15
**Purpose**: Identify duplicate content and determine authoritative versions

## Summary

Found **6 topics** with potential duplicates between topic-specific directories and `/data_science_applications/`.

### **KEY FINDING**: Two Types of Files in data_science_applications/

**Type A: Standalone Presentations** (complete LaTeX documents with `\documentclass`)
- `causal_inference_beamer.tex` ✓ Complete document

**Type B: Modular Sections** (LaTeX sections meant for inclusion, start with `\section{}`)
- `deep_learning_beamer.tex` → Section only
- `time_series_beamer.tex` → Section only
- `explainable_ai_beamer.tex` → Section only

**Implication**: Type B files are NOT duplicates - they're modular components for building combined presentations. Type A files may be true duplicates.

## Detailed Analysis

### 1. Deep Learning

| Location | File | Size | Date Modified | Status |
|----------|------|------|---------------|--------|
| `/deep_learning/` | `deep_learning_beamer.tex` | 26K | Nov 5 (18:15) | **Older timestamp** |
| `/data_science_applications/` | `deep_learning_beamer.tex` | 25K | Nov 5 (22:28) | **Newer timestamp** |

**File Comparison**: Files **differ** in content
**Decision**: Need to review both - data_science_applications version is newer but smaller
**Recommended Action**: Manual review to determine which has more complete content

---

### 2. Time Series

| Location | File | Size | Date Modified | Status |
|----------|------|------|---------------|--------|
| `/time_series/` | `time_series_beamer.tex` | 24K | **Nov 11** | **NEWEST - Keep this** |
| `/data_science_applications/` | `time_series_beamer.tex` | 16K | Nov 5 | Older, smaller |

**Decision**: **Use `/time_series/time_series_beamer.tex`** (most recent, larger)
**Action**: Archive or delete data_science_applications version

---

### 3. Explainable AI / Interpretability

| Location | File | Size | Date Modified | Status |
|----------|------|------|---------------|--------|
| `/explainable_ai/` | `interpretability_beamer.tex` | 24K | Nov 5 (18:13) | Older, larger |
| `/data_science_applications/` | `explainable_ai_beamer.tex` | 21K | Nov 5 (22:30) | **Newer**, smaller |

**Note**: Different filenames suggest these may be intentionally different presentations
**Decision**: Need manual review - could be:
  - Same content, renamed
  - Different perspectives on same topic
  - One is summary, one is detailed

**Recommended Action**: Manual review required

---

### 4. Causal Inference

| Location | File | Size | Date Modified | Status |
|----------|------|------|---------------|--------|
| `/causal_inference/` | **Directory may be empty or not exist** | - | - | - |
| `/data_science_applications/` | `causal_inference_beamer.tex` | 55K | Oct 29 | Primary version |
| `/data_science_applications/` | `causal_inference_enhancements.tex` | 64K | Nov 5 | Enhancement version |

**Decision**: Use data_science_applications versions as authoritative
**Action**: These will move to new `/04-causal-inference/` structure

---

### 5. Feature Engineering

| Location | File | Size | Date Modified | Status |
|----------|------|------|---------------|--------|
| `/data_science_applications/` | `feature_engineering_beamer.tex` | 52K | Oct 29 | Has compiled PDFs |
| `/code/feature_engineering/` | Code only | - | - | Implementation |
| `/exercises/feature_engineering/` | Exercises | - | - | Practice problems |

**Decision**: Content is **distributed** across locations, not duplicated
**Action**: Consolidate all into `/01-foundations/feature-engineering/`

---

### 6. Statistical Learning/Modeling

| Location | File | Size | Date Modified | Status |
|----------|------|------|---------------|--------|
| `/statistical_modeling/` | `diogo_ribeiro_beamer_extended.tex` | ? | ? | Different name |
| `/data_science_applications/` | `statistical_learning_beamer.tex` | 35K | Oct 29 | - |
| `/data_science_applications/` | `statistical_learning_enhancements.tex` | 61K | Nov 5 | Enhancement |

**Decision**: Need to check if `diogo_ribeiro_beamer_extended.tex` relates to statistical learning
**Action**: Manual review required

---

## Additional Content in data_science_applications/

### Unique Content (No Duplicates)

1. **MLOps & Deployment**
   - File: `mlops_deployment_beamer.tex` (22K)
   - Destination: `/06-advanced-topics/mlops-deployment/`

2. **A/B Testing**
   - File: `ab_testing_experimental_design_beamer.tex` (34K)
   - Note: Also `a_b_testing.tex` in `/interview/` (16K) - potential duplicate
   - Destination: `/04-causal-inference/ab-testing/`

3. **Capstone Projects**
   - `capstone_projects_enhancements.tex` (73K)
   - `capstone_prerequisites_appendix.tex` (22K)
   - `CAPSTONE_PROJECTS_ENHANCEMENT_GUIDE.md` (30K)
   - Destination: `/07-capstone-projects/`

4. **Industry Focus**
   - `industry_focus_enhancements.tex` (66K)
   - `INDUSTRY_FOCUS_ENHANCEMENT_GUIDE.md` (27KB)
   - Destination: `/07-capstone-projects/industry-focus/`

5. **Enhancement Guides**
   - `STATISTICAL_LEARNING_ENHANCEMENT_GUIDE.md`
   - `CAUSAL_ENHANCEMENT_GUIDE.md`
   - `INDUSTRY_FOCUS_ENHANCEMENT_GUIDE.md`
   - `CAPSTONE_PROJECTS_ENHANCEMENT_GUIDE.md`
   - Decision: Move to `/docs/enhancement-guides/`

6. **Competency Matrices**
   - `COMPETENCY_MATRICES.md` (26K)
   - Destination: `/learning-paths/competency-matrices/`

7. **Assessments**
   - Subdirectory: `/data_science_applications/assessments/`
   - Action: Merge with root `/assessments/`

---

## Deduplication Strategy

### Phase 1: Low-Risk Moves (Unique Content)
Move content that has no duplicates:
- MLOps presentation
- Capstone materials
- Industry focus materials
- Competency matrices
- Enhancement guides

### Phase 2: Manual Review Required
Review and decide on:
1. Deep Learning - which version is more complete?
2. Explainable AI - are these intentionally different?
3. Statistical Learning - relationship to statistical_modeling?

### Phase 3: Clear Winners
Use newer/larger versions:
- Time Series: Use `/time_series/time_series_beamer.tex` (Nov 11, 24K)

### Phase 4: Distributed Content
Consolidate distributed materials:
- Feature Engineering (presentation + code + exercises)
- Causal Inference (presentation + enhancements + code + exercises)

---

## Recommendations

### Immediate Actions

1. **Create backup before any moves**:
   ```bash
   git tag pre-deduplication-backup
   ```

2. **Manual Review Queue** (requires human decision):
   - [ ] Compare `deep_learning/deep_learning_beamer.tex` vs `data_science_applications/deep_learning_beamer.tex`
   - [ ] Compare `explainable_ai/interpretability_beamer.tex` vs `data_science_applications/explainable_ai_beamer.tex`
   - [ ] Check relationship between `statistical_modeling/` and `statistical_learning`
   - [ ] Compare `interview/a_b_testing.tex` vs `data_science_applications/ab_testing_experimental_design_beamer.tex`

3. **Automated Moves** (safe - no conflicts):
   - [ ] Move MLOps content
   - [ ] Move Capstone materials
   - [ ] Move Industry Focus materials
   - [ ] Move Competency Matrices
   - [ ] Move Enhancement Guides to `/docs/`

### Decision Matrix

| Content | Current Location | Recommended Destination | Conflict? | Action |
|---------|-----------------|------------------------|-----------|---------|
| Time Series | `/time_series/` | `/05-time-series/time-series-forecasting/` | No (use this version) | ✅ Auto-move |
| Deep Learning | **BOTH** locations | `/02-deep-learning/deep-learning-fundamentals/` | ⚠️ Yes | 🔍 Manual review |
| Explainable AI | **BOTH** locations | `/06-advanced-topics/explainable-ai/` | ⚠️ Maybe | 🔍 Manual review |
| Causal Inference | data_science_app | `/04-causal-inference/causal-inference-fundamentals/` | No | ✅ Auto-move |
| Feature Engineering | Distributed | `/01-foundations/feature-engineering/` | No | ✅ Consolidate |
| MLOps | data_science_app | `/06-advanced-topics/mlops-deployment/` | No | ✅ Auto-move |
| A/B Testing | data_science_app + interview | `/04-causal-inference/ab-testing/` | ⚠️ Maybe | 🔍 Manual review |
| Capstone | data_science_app | `/07-capstone-projects/` | No | ✅ Auto-move |

---

## Files Requiring Manual Review

Create these comparison tasks:

### Task 1: Deep Learning Comparison
```bash
diff deep_learning/deep_learning_beamer.tex data_science_applications/deep_learning_beamer.tex | less
```
**Question**: Which version is authoritative? Or should we merge?

### Task 2: Explainable AI Comparison
```bash
diff explainable_ai/interpretability_beamer.tex data_science_applications/explainable_ai_beamer.tex | less
```
**Question**: Are these different presentations or duplicates with different names?

### Task 3: A/B Testing Comparison
```bash
diff interview/a_b_testing.tex data_science_applications/ab_testing_experimental_design_beamer.tex | less
```
**Question**: Interview version vs full presentation - keep both or merge?

---

## Next Steps After Deduplication

1. Complete manual reviews
2. Tag repository: `git tag post-deduplication`
3. Proceed to Phase 1: Create new directory structure
4. Begin incremental migration

---

**Status**: Phase 0 - Deduplication analysis complete
**Action Required**: Manual review of 3-4 file pairs
**Estimated Time**: 30-45 minutes for manual reviews
