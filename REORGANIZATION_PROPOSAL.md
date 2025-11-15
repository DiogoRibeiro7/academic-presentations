# Repository Reorganization Proposal

**Date**: 2025-11-15
**Current Branch**: `claude/repo-reorganization-suggestions-01BFTRP73rpUCz1QKpLYqikn`
**Status**: Proposal for Review

---

## Executive Summary

This document proposes a reorganization of the `academic-presentations` repository to improve navigability, maintainability, and pedagogical clarity. The current structure has 24+ top-level directories with inconsistent organization patterns. The proposed reorganization reduces cognitive overhead, clarifies relationships between materials, and better aligns with the three defined learning paths.

**Key Benefits:**
- **Improved Navigation**: Clear hierarchy with 5 main categories instead of 24 directories
- **Better Discoverability**: Related materials (presentations, code, exercises) grouped together
- **Learning Path Alignment**: Structure mirrors the three pedagogical paths
- **Scalability**: Easy to add new topics without cluttering root directory
- **Consistency**: Uniform naming and organizational patterns

---

## Current Structure: Analysis

### Strengths ✅
1. **Good Documentation**: Comprehensive READMEs, style guides, contributing guidelines
2. **Code Quality**: Production-ready Python/R implementations with tests
3. **Automation**: GitHub Actions for CI/CD (LaTeX compilation, link checking)
4. **Custom Theme**: Professional Beamer theme with consistent styling
5. **Academic Rigor**: 140+ curated references across 8 BibTeX files

### Problems ⚠️

#### 1. **Overwhelming Root Directory**
- 24+ top-level directories create decision paralysis
- No clear hierarchy between courses, topics, and supporting materials
- Difficult to understand repository scope at a glance

#### 2. **Inconsistent Organization Patterns**
```
✗ Separated: /code/ vs /presentations/ (breaks topic cohesion)
✗ Catch-all: /data_science_applications/ contains too much diverse content
✗ Disconnected: Exercises/assessments separated from their topics
✗ Mixed levels: Some directories are topics, others are infrastructure
```

#### 3. **Naming Inconsistencies**
- Mix of `snake_case` (most), `camelCase` (none), and compound words
- Topic names don't clearly indicate content type (presentation vs code vs docs)

#### 4. **Unclear Relationships**
- Code in `/code/mcmc/` related to presentations in `/mcmc/` (non-obvious)
- Exercises in `/exercises/mcmc/` related to both code and presentations
- Assessments cover multiple topics but organized by type, not topic

#### 5. **Data Science Applications Hub**
The `/data_science_applications/` directory contains:
- Feature engineering materials
- Statistical learning content
- Causal inference presentations
- Interview materials (A/B testing)
- Assessment frameworks

**Issue**: This is a conceptual grab-bag without clear organizational principle.

---

## Proposed Reorganization: Option 1 (Recommended)

### **Structure by Learning Domain + Material Type**

This approach groups content by major learning domains while keeping related materials together.

```
academic-presentations/
│
├── README.md                          # Main overview (updated)
├── QUICK_START.md                     # Getting started guide
├── LICENSE
├── CHANGELOG.md
├── pyproject.toml
├── environment.yml
├── requirements.txt
├── requirements-dev.txt
│
├── 01-foundations/                    # Foundational ML & Stats
│   ├── README.md                      # Overview of foundational topics
│   ├── statistical-modeling/
│   │   ├── presentation/
│   │   │   └── statistical_modeling_beamer.tex
│   │   ├── code/
│   │   ├── exercises/
│   │   └── README.md
│   ├── feature-engineering/
│   │   ├── presentation/
│   │   │   ├── feature_engineering_beamer.tex
│   │   │   └── feature_engineering_enhancements.tex
│   │   ├── code/
│   │   │   ├── python/
│   │   │   │   ├── feature_engineering_pipeline.py
│   │   │   │   └── README.md
│   │   │   └── r/
│   │   │       ├── feature_engineering_pipeline.R
│   │   │       └── README.md
│   │   ├── exercises/
│   │   └── README.md
│   ├── pca/
│   │   ├── presentation/
│   │   ├── code/
│   │   └── README.md
│   └── optimization/
│       ├── presentation/
│       │   ├── optimization_beamer.tex
│       │   └── optimization_enhancements.tex
│       ├── code/
│       ├── exercises/
│       └── README.md
│
├── 02-deep-learning/                  # Deep Learning & RL
│   ├── README.md
│   ├── deep-learning-fundamentals/
│   │   ├── presentation/
│   │   │   ├── deep_learning_beamer.tex
│   │   │   └── deep_learning_enhancements.tex
│   │   ├── code/
│   │   ├── exercises/
│   │   └── README.md
│   └── reinforcement-learning/
│       ├── presentation/
│       │   ├── reinforcement_learning_beamer.tex
│       │   └── reinforcement_learning_enhancements.tex
│       ├── code/
│       ├── exercises/
│       └── README.md
│
├── 03-bayesian-methods/               # Bayesian Statistics & MCMC
│   ├── README.md
│   ├── bayesian-machine-learning/
│   │   ├── presentation/
│   │   │   ├── bayesian_ml_beamer.tex
│   │   │   └── bayesian_ml_enhancements.tex
│   │   ├── code/
│   │   ├── exercises/
│   │   └── README.md
│   └── mcmc/
│       ├── presentation/
│       │   ├── mcmc_beamer.tex
│       │   └── mcmc_enhancements.tex
│       ├── code/
│       │   ├── python/
│       │   │   ├── metropolis_hastings.py
│       │   │   ├── hamiltonian_mc.py
│       │   │   ├── nuts_sampler.py
│       │   │   └── README.md
│       │   └── tests/
│       │       ├── test_mcmc.py
│       │       ├── test_metropolis.py
│       │       └── conftest.py
│       ├── exercises/
│       │   ├── mcmc_exercises.tex
│       │   └── mcmc_exercises.pdf
│       └── README.md
│
├── 04-causal-inference/               # Causal Methods & Econometrics
│   ├── README.md
│   ├── causal-inference-fundamentals/
│   │   ├── presentation/
│   │   │   ├── causal_inference_beamer.tex
│   │   │   └── causal_inference_enhancements.tex
│   │   ├── code/
│   │   │   ├── python/
│   │   │   │   ├── instrumental_variables.py
│   │   │   │   ├── regression_discontinuity.py
│   │   │   │   ├── diff_in_diff.py
│   │   │   │   └── README.md
│   │   │   └── r/
│   │   │       ├── instrumental_variables.R
│   │   │       ├── regression_discontinuity.R
│   │   │       ├── diff_in_diff.R
│   │   │       └── README.md
│   │   ├── exercises/
│   │   │   ├── causal_inference_exercises.tex
│   │   │   └── causal_inference_exercises.pdf
│   │   └── README.md
│   └── ab-testing/                    # Practical application of causal inference
│       ├── presentation/
│       ├── code/
│       └── README.md
│
├── 05-time-series/                    # Temporal Data Analysis
│   ├── README.md
│   └── time-series-forecasting/
│       ├── presentation/
│       │   ├── time_series_beamer.tex
│       │   └── time_series_enhancements.tex
│       ├── code/
│       ├── exercises/
│       └── README.md
│
├── 06-advanced-topics/                # Specialized Topics
│   ├── README.md
│   ├── explainable-ai/
│   │   ├── presentation/
│   │   │   ├── explainable_ai_beamer.tex
│   │   │   └── explainable_ai_enhancements.tex
│   │   ├── code/
│   │   ├── exercises/
│   │   └── README.md
│   └── computer-science/              # OOP, Streaming, etc.
│       ├── presentation/
│       ├── code/
│       └── README.md
│
├── assessments/                       # Cross-topic assessments
│   ├── README.md
│   ├── quizzes/
│   │   ├── foundations/
│   │   ├── deep-learning/
│   │   ├── bayesian-methods/
│   │   └── causal-inference/
│   ├── exams/
│   │   ├── midterm/
│   │   └── final/
│   ├── rubrics/
│   │   ├── presentation_rubric.md
│   │   └── project_rubric.md
│   └── self-assessment/
│       └── competency_checklist.md
│
├── learning-paths/                    # Structured course sequences
│   ├── README.md
│   ├── ml-fundamentals.md             # Path 1: 11 weeks
│   ├── deep-learning-track.md         # Path 2: 14+ weeks
│   ├── causal-bayesian-track.md       # Path 3: 14+ weeks
│   └── competency-matrices/
│       ├── foundations_matrix.md
│       ├── deep_learning_matrix.md
│       └── bayesian_causal_matrix.md
│
├── shared/                            # Shared resources
│   ├── theme/
│   │   ├── esmad_beamer_theme.sty
│   │   ├── STYLE_GUIDE.md
│   │   └── template_presentation.tex
│   ├── bibliographies/
│   │   ├── mcmc_references.bib
│   │   ├── causal_inference_references.bib
│   │   ├── statistical_learning_references.bib
│   │   ├── deep_learning_references.bib
│   │   ├── bayesian_references.bib
│   │   ├── time_series_references.bib
│   │   ├── optimization_references.bib
│   │   └── industry_applications.bib
│   └── utilities/
│       ├── compile_all.sh
│       └── check_references.py
│
├── docs/                              # Project documentation
│   ├── CONTRIBUTING.md
│   ├── ACCESSIBILITY.md
│   ├── QUALITY.md
│   ├── COMPLETION_SUMMARY.md
│   ├── architecture/
│   │   └── repository_structure.md
│   └── teaching-guides/
│       ├── facilitator_guide.md
│       └── student_guide.md
│
├── scripts/                           # Utility scripts
│   ├── spell_check.py
│   ├── compile_all_presentations.sh
│   └── generate_toc.py
│
└── .github/                           # CI/CD automation
    ├── workflows/
    │   ├── compile-latex.yml
    │   ├── check-links.yml
    │   └── generate-previews.yml
    └── markdown-link-check-config.json
```

### **Key Design Principles**

1. **Domain-First Organization**: Group by learning domain (6 major areas)
2. **Topic Cohesion**: Each topic contains ALL related materials (presentation + code + exercises)
3. **Consistent Structure**: Every topic follows same pattern
4. **Clear Hierarchy**: 3 levels max (domain → topic → material type)
5. **Hyphenated Naming**: Use `kebab-case` for directories for readability

### **Standard Topic Structure**

Every topic follows this template:
```
topic-name/
├── presentation/               # LaTeX Beamer files
│   ├── topic_beamer.tex
│   └── topic_enhancements.tex (optional)
├── code/                       # Implementations
│   ├── python/                 # Python code (if applicable)
│   ├── r/                      # R code (if applicable)
│   └── tests/                  # Unit tests (if applicable)
├── exercises/                  # Problem sets
│   ├── topic_exercises.tex
│   └── topic_exercises.pdf
└── README.md                   # Topic overview
```

---

## Proposed Reorganization: Option 2 (Alternative)

### **Structure by Learning Path**

This approach organizes content by the three defined learning paths, making it easier for students to follow a course.

```
academic-presentations/
│
├── paths/
│   ├── 01-ml-fundamentals/        # Path 1: 11 weeks
│   │   ├── week-01-statistical-modeling/
│   │   ├── week-02-feature-engineering/
│   │   ├── week-03-optimization/
│   │   └── week-04-explainable-ai/
│   │
│   ├── 02-deep-learning-track/    # Path 2: 14+ weeks
│   │   ├── week-01-deep-learning-intro/
│   │   ├── week-05-reinforcement-learning/
│   │   └── week-10-time-series-deep/
│   │
│   └── 03-causal-bayesian/        # Path 3: 14+ weeks
│       ├── week-01-causal-inference/
│       ├── week-05-bayesian-ml/
│       └── week-09-mcmc/
│
├── topics/                        # Topic library (referenced by paths)
│   ├── statistical-modeling/
│   ├── deep-learning/
│   ├── mcmc/
│   └── ...
│
└── [shared/, assessments/, docs/, etc.]
```

**Pros:**
- Clear pedagogical progression
- Week-by-week structure for instructors
- Easy to follow for students

**Cons:**
- Duplication if topics appear in multiple paths
- Harder to maintain (changes must update multiple paths)
- Less flexible for self-learners who cherry-pick topics

**Recommendation**: Use Option 1 for main structure, create Option 2 as symbolic links or reference documents in `/learning-paths/`.

---

## Proposed Reorganization: Option 3 (Hybrid)

### **Structure by Format with Topic Cross-Reference**

```
academic-presentations/
│
├── presentations/                 # All presentation materials
│   ├── foundations/
│   ├── deep-learning/
│   ├── bayesian-methods/
│   └── causal-inference/
│
├── code/                          # All code implementations
│   ├── python/
│   └── r/
│
├── exercises/                     # All exercises
│   ├── foundations/
│   └── bayesian-methods/
│
└── courses/                       # Course assemblies (cross-reference)
    ├── ml-fundamentals/
    └── deep-learning-track/
```

**Pros:**
- Clear separation by artifact type
- Easy to find all presentations, all code, etc.

**Cons:**
- **Breaks topic cohesion** (same as current structure)
- Requires mental mapping between related materials
- Not recommended for educational repositories

---

## Comparison Matrix

| Criterion | Current | Option 1 (Recommended) | Option 2 (Path-First) | Option 3 (Format) |
|-----------|---------|------------------------|----------------------|-------------------|
| **Navigability** | ⚠️ Poor (24 dirs) | ✅ Excellent (6 domains) | ✅ Good (3 paths) | ⚠️ Fair (format silos) |
| **Topic Cohesion** | ⚠️ Broken (code separated) | ✅ Strong (all together) | ✅ Strong | ❌ Broken |
| **Scalability** | ❌ Poor (root clutter) | ✅ Excellent | ⚠️ Fair (duplication risk) | ✅ Good |
| **Learning Path Support** | ⚠️ Fair (docs only) | ✅ Explicit (learning-paths/) | ✅ Native | ⚠️ Fair |
| **Maintenance** | ⚠️ Moderate | ✅ Easy (consistent structure) | ⚠️ Complex (multi-path updates) | ✅ Easy |
| **Discoverability** | ❌ Difficult | ✅ Intuitive | ✅ Guided | ⚠️ Requires cross-reference |
| **For Instructors** | ⚠️ Fair | ✅ Excellent | ✅ Excellent | ⚠️ Fair |
| **For Self-Learners** | ⚠️ Fair | ✅ Excellent | ⚠️ Rigid | ⚠️ Fair |
| **Consistency** | ⚠️ Mixed patterns | ✅ Uniform | ✅ Uniform | ✅ Uniform |

**Verdict**: **Option 1 (Domain + Material Type)** is recommended.

---

## Migration Plan

### Phase 1: Preparation (Low Risk)
1. **Create reorganization branch** (already done: `claude/repo-reorganization-suggestions-01BFTRP73rpUCz1QKpLYqikn`)
2. **Backup current state**: Tag current commit as `pre-reorganization`
3. **Document current paths**: Generate file manifest for reference
4. **Test automation**: Ensure GitHub Actions work with new paths

### Phase 2: Structure Creation (Low Risk)
1. Create new directory structure (empty)
2. Add README.md files to each new domain/topic directory
3. Update main README.md with new structure overview
4. Create migration script to automate file moves

### Phase 3: Content Migration (Medium Risk)
1. **Migrate shared resources first**:
   - Move `/theme/` → `/shared/theme/`
   - Move `/bibliographies/` → `/shared/bibliographies/`
   - Move `/scripts/` → `/scripts/` (no change)

2. **Migrate by domain** (one at a time):
   - Start with smallest domain (Time Series)
   - Test LaTeX compilation after each migration
   - Update relative paths in `.tex` files
   - Move related code, exercises, assessments

3. **Update cross-references**:
   - Fix LaTeX `\input{}` and `\bibliography{}` paths
   - Update Python/R import statements if needed
   - Fix links in README files

### Phase 4: Automation Updates (Medium Risk)
1. Update `.github/workflows/compile-latex.yml` with new paths
2. Update `.github/workflows/check-links.yml`
3. Test all workflows on reorganization branch

### Phase 5: Documentation (Low Risk)
1. Update main README.md
2. Create QUICK_START.md
3. Update CONTRIBUTING.md with new structure
4. Generate new architecture diagrams

### Phase 6: Testing & Validation (Critical)
1. **Compile all presentations**: Ensure all `.tex` files compile
2. **Run all tests**: Python unit tests, link checks
3. **Manual review**: Check all READMEs render correctly
4. **Path verification**: Ensure no broken links

### Phase 7: Deployment
1. Merge reorganization branch to main
2. Create release tag: `v2.0.0-reorganized`
3. Update GitHub repository description
4. Notify users of structure changes

---

## Detailed Migration Script

### Automated Migration (Bash Script)

```bash
#!/bin/bash
# migrate_to_new_structure.sh

set -e  # Exit on error

echo "=== Academic Presentations Repository Reorganization ==="
echo "Starting migration to new structure..."

# Create new directory structure
echo "Creating new directory structure..."

# 01-foundations
mkdir -p 01-foundations/{statistical-modeling,feature-engineering,pca,optimization}/{presentation,code,exercises}
mkdir -p 01-foundations/feature-engineering/code/{python,r}

# 02-deep-learning
mkdir -p 02-deep-learning/{deep-learning-fundamentals,reinforcement-learning}/{presentation,code,exercises}

# 03-bayesian-methods
mkdir -p 03-bayesian-methods/{bayesian-machine-learning,mcmc}/{presentation,code,exercises}
mkdir -p 03-bayesian-methods/mcmc/code/{python,tests}

# 04-causal-inference
mkdir -p 04-causal-inference/{causal-inference-fundamentals,ab-testing}/{presentation,code,exercises}
mkdir -p 04-causal-inference/causal-inference-fundamentals/code/{python,r}

# 05-time-series
mkdir -p 05-time-series/time-series-forecasting/{presentation,code,exercises}

# 06-advanced-topics
mkdir -p 06-advanced-topics/{explainable-ai,computer-science}/{presentation,code,exercises}

# Shared resources
mkdir -p shared/{theme,bibliographies,utilities}

# Other top-level
mkdir -p assessments/{quizzes,exams,rubrics,self-assessment}
mkdir -p learning-paths/competency-matrices
mkdir -p docs/{architecture,teaching-guides}

echo "Directory structure created."

# Move shared resources
echo "Migrating shared resources..."
mv theme/* shared/theme/ 2>/dev/null || true
mv bibliographies/* shared/bibliographies/ 2>/dev/null || true

# Move MCMC materials
echo "Migrating MCMC materials..."
mv mcmc/*_beamer.tex 03-bayesian-methods/mcmc/presentation/ 2>/dev/null || true
mv mcmc/*_enhancements.tex 03-bayesian-methods/mcmc/presentation/ 2>/dev/null || true
mv code/mcmc/*.py 03-bayesian-methods/mcmc/code/python/ 2>/dev/null || true
mv code/mcmc/README.md 03-bayesian-methods/mcmc/code/python/ 2>/dev/null || true
mv tests/unit/test_mcmc.py 03-bayesian-methods/mcmc/code/tests/ 2>/dev/null || true
mv exercises/mcmc/* 03-bayesian-methods/mcmc/exercises/ 2>/dev/null || true

# Move Causal Inference materials
echo "Migrating Causal Inference materials..."
mv causal_inference/*_beamer.tex 04-causal-inference/causal-inference-fundamentals/presentation/ 2>/dev/null || true
mv code/causal_inference/*.py 04-causal-inference/causal-inference-fundamentals/code/python/ 2>/dev/null || true
mv code/causal_inference/*.R 04-causal-inference/causal-inference-fundamentals/code/r/ 2>/dev/null || true
mv exercises/causal_inference/* 04-causal-inference/causal-inference-fundamentals/exercises/ 2>/dev/null || true

# Move Feature Engineering materials
echo "Migrating Feature Engineering materials..."
# (Assuming they're in data_science_applications/)
mv code/feature_engineering/*.py 01-foundations/feature-engineering/code/python/ 2>/dev/null || true
mv code/feature_engineering/*.R 01-foundations/feature-engineering/code/r/ 2>/dev/null || true

# Move Deep Learning materials
echo "Migrating Deep Learning materials..."
mv deep_learning/*_beamer.tex 02-deep-learning/deep-learning-fundamentals/presentation/ 2>/dev/null || true

# Move Reinforcement Learning materials
echo "Migrating Reinforcement Learning materials..."
mv reinforcement_learning/*_beamer.tex 02-deep-learning/reinforcement-learning/presentation/ 2>/dev/null || true

# Move Time Series materials
echo "Migrating Time Series materials..."
mv time_series/*_beamer.tex 05-time-series/time-series-forecasting/presentation/ 2>/dev/null || true

# Move Optimization materials
echo "Migrating Optimization materials..."
mv optimization/*_beamer.tex 01-foundations/optimization/presentation/ 2>/dev/null || true

# Move Bayesian ML materials
echo "Migrating Bayesian ML materials..."
mv bayes/*_beamer.tex 03-bayesian-methods/bayesian-machine-learning/presentation/ 2>/dev/null || true

# Move Explainable AI materials
echo "Migrating Explainable AI materials..."
mv explainable_ai/*_beamer.tex 06-advanced-topics/explainable-ai/presentation/ 2>/dev/null || true

# Move Computer Science materials
echo "Migrating Computer Science materials..."
mv computer_science/*_beamer.tex 06-advanced-topics/computer-science/presentation/ 2>/dev/null || true

# Move assessments
echo "Migrating assessments..."
mv assessments/quizzes/* assessments/quizzes/ 2>/dev/null || true
mv assessments/exams/* assessments/exams/ 2>/dev/null || true
mv assessments/rubrics/* assessments/rubrics/ 2>/dev/null || true

# Move documentation
echo "Migrating documentation..."
mv CONTRIBUTING.md docs/ 2>/dev/null || true
mv ACCESSIBILITY.md docs/ 2>/dev/null || true
mv QUALITY.md docs/ 2>/dev/null || true
mv COMPLETION_SUMMARY.md docs/ 2>/dev/null || true

echo "Migration complete!"
echo "Next steps:"
echo "1. Update LaTeX paths (run update_latex_paths.sh)"
echo "2. Update README files"
echo "3. Test all presentations compile"
echo "4. Update GitHub Actions workflows"
```

### LaTeX Path Update Script

```bash
#!/bin/bash
# update_latex_paths.sh

echo "Updating LaTeX file paths..."

# Update theme path references
find . -name "*.tex" -type f -exec sed -i 's|\\usepackage{../theme/esmad_beamer_theme}|\\usepackage{../../../shared/theme/esmad_beamer_theme}|g' {} \;

# Update bibliography paths (domain-specific)
find 01-foundations -name "*.tex" -type f -exec sed -i 's|\\bibliography{../bibliographies/|\\bibliography{../../shared/bibliographies/|g' {} \;
find 02-deep-learning -name "*.tex" -type f -exec sed -i 's|\\bibliography{../bibliographies/|\\bibliography{../../shared/bibliographies/|g' {} \;
find 03-bayesian-methods -name "*.tex" -type f -exec sed -i 's|\\bibliography{../bibliographies/|\\bibliography{../../shared/bibliographies/|g' {} \;
find 04-causal-inference -name "*.tex" -type f -exec sed -i 's|\\bibliography{../bibliographies/|\\bibliography{../../shared/bibliographies/|g' {} \;
find 05-time-series -name "*.tex" -type f -exec sed -i 's|\\bibliography{../bibliographies/|\\bibliography{../../shared/bibliographies/|g' {} \;
find 06-advanced-topics -name "*.tex" -type f -exec sed -i 's|\\bibliography{../bibliographies/|\\bibliography{../../shared/bibliographies/|g' {} \;

echo "LaTeX paths updated."
```

---

## Impact Analysis

### Breaking Changes
1. **LaTeX paths**: All `\usepackage{}` and `\bibliography{}` need updates
2. **Python imports**: If code cross-references other modules
3. **GitHub Actions**: Workflow paths need updates
4. **Documentation links**: All internal links need updates
5. **Git history**: File move may obscure history (use `git log --follow`)

### Non-Breaking Changes
1. **PDF outputs**: Will work after path updates
2. **Code functionality**: Code logic unchanged
3. **Bibliography content**: BibTeX files unchanged
4. **CI/CD logic**: Same workflows, just different paths

### Rollback Plan
If issues arise:
1. **Git reset**: Return to `pre-reorganization` tag
2. **Selective rollback**: Use `git checkout pre-reorganization -- path/to/file`
3. **Merge conflicts**: Documented resolution strategies

---

## Timeline Estimate

| Phase | Duration | Effort | Risk |
|-------|----------|--------|------|
| Preparation | 1 hour | Low | Low |
| Structure Creation | 1 hour | Low | Low |
| Content Migration | 4-6 hours | Medium | Medium |
| Automation Updates | 2 hours | Low | Medium |
| Documentation | 2 hours | Low | Low |
| Testing & Validation | 3-4 hours | High | High |
| **Total** | **13-16 hours** | **Medium** | **Medium** |

**Recommended approach**: Execute over 2-3 days with testing checkpoints.

---

## Post-Migration Checklist

### Immediate Validation
- [ ] All `.tex` files compile without errors
- [ ] All code examples run successfully
- [ ] All unit tests pass
- [ ] No broken internal links in README files
- [ ] GitHub Actions workflows complete successfully
- [ ] PDF previews generated correctly

### Documentation Updates
- [ ] Main README.md updated with new structure
- [ ] QUICK_START.md created
- [ ] Learning path documents updated
- [ ] Contributing guidelines reflect new structure
- [ ] Architecture documentation updated

### Quality Checks
- [ ] Spell check passes on all files
- [ ] Link validation passes
- [ ] Pre-commit hooks work with new structure
- [ ] Accessibility guidelines still met

### User Communication
- [ ] Changelog entry created
- [ ] Migration guide published
- [ ] GitHub release notes written
- [ ] Example paths updated in documentation

---

## Alternative: Incremental Migration

If full migration is too risky, consider **incremental approach**:

### Iteration 1: Shared Resources (Week 1)
- Move `/theme/` → `/shared/theme/`
- Move `/bibliographies/` → `/shared/bibliographies/`
- Update all LaTeX files to reference new paths
- Test compilation

### Iteration 2: One Domain (Week 2)
- Migrate smallest domain (e.g., Time Series)
- Create domain structure
- Move all related materials
- Test thoroughly

### Iteration 3: Expand (Weeks 3-6)
- Migrate one domain per week
- Validate after each migration
- Build confidence incrementally

### Iteration 4: Cleanup (Week 7)
- Remove old empty directories
- Update all documentation
- Final validation

---

## Recommendations

### ✅ DO THIS
1. **Implement Option 1 (Domain + Material Type)**
   - Best balance of all criteria
   - Scalable and maintainable
   - Pedagogically sound

2. **Use incremental migration**
   - Lower risk
   - Easier to validate
   - Can pause/rollback if needed

3. **Automate path updates**
   - Use scripts for LaTeX path fixes
   - Reduces manual errors
   - Reproducible process

4. **Maintain backward compatibility temporarily**
   - Create symbolic links from old paths to new (if needed)
   - Add deprecation notices to old READMEs
   - Remove after 1-2 months

### ❌ DON'T DO THIS
1. **Don't migrate everything at once**
   - Too risky
   - Hard to troubleshoot
   - High chance of errors

2. **Don't use Option 3 (Format-First)**
   - Repeats current problems
   - Breaks topic cohesion
   - Not recommended for educational repos

3. **Don't skip testing**
   - Every LaTeX file must compile
   - Every code example must run
   - Every link must resolve

---

## Success Metrics

After migration, the repository should demonstrate:

1. **Improved Navigability**
   - Users find topics in ≤3 clicks from root
   - Clear hierarchy (no more than 3 levels deep)
   - Intuitive directory names

2. **Better Discoverability**
   - Related materials (presentation + code + exercises) together
   - Domain-based browsing
   - Clear entry points for learning paths

3. **Maintainability**
   - Adding new topic follows clear template
   - Consistent structure across all topics
   - Easy to update cross-cutting concerns

4. **User Satisfaction**
   - Positive feedback from instructors
   - Reduced "where is X?" questions
   - Easier onboarding for contributors

---

## Questions for Review

Before proceeding, please consider:

1. **Which option do you prefer?**
   - Option 1 (Recommended): Domain + Material Type
   - Option 2: Learning Path First
   - Option 3: Format-First (not recommended)
   - Other variation?

2. **Migration approach?**
   - Full migration at once
   - Incremental by domain
   - Hybrid (shared resources first, then incremental)

3. **Naming conventions?**
   - `kebab-case` (recommended: `feature-engineering`)
   - `snake_case` (current: `feature_engineering`)
   - Mixed case (not recommended)

4. **Backward compatibility?**
   - Symbolic links for transition period
   - Hard break with deprecation notice
   - No backward compatibility

5. **Timeline?**
   - Immediate (1-2 days intensive work)
   - Gradual (1-2 months incremental)
   - Deferred (plan now, execute later)

---

## Conclusion

The current repository structure has served well but has outgrown its organization. The proposed reorganization (Option 1) will:

- **Reduce cognitive load**: 6 domains instead of 24 root directories
- **Improve cohesion**: Related materials grouped together
- **Scale gracefully**: Easy to add new topics
- **Support pedagogy**: Clear alignment with learning paths
- **Maintain quality**: All existing content preserved and enhanced

**Next Steps**:
1. Review this proposal
2. Select preferred option
3. Approve migration plan
4. Execute migration (with testing checkpoints)
5. Validate and deploy

**Estimated Effort**: 13-16 hours over 2-3 days
**Risk Level**: Medium (mitigated by incremental approach and testing)
**Impact**: High positive (significantly improved usability)

---

**Author**: Claude (AI Assistant)
**Review Requested**: Diogo Ribeiro
**Date**: 2025-11-15
**Version**: 1.0
