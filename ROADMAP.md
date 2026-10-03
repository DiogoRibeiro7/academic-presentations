# Academic Presentations Roadmap

This roadmap is the active planning document for the repository. It exists to keep development finite, ordered, and reviewable.

The repository is source-first: LaTeX sources are canonical, PDFs are build artifacts, presentations share the FMAD - UTP Beamer system, and active decks must satisfy the presentation contract enforced in CI.

## Current Status

The repository-wide presentation infrastructure is mature:

- [x] shared canonical Beamer theme;
- [x] canonical author metadata;
- [x] `presentation/main.tex` entry points;
- [x] CI compilation and presentation-contract validation;
- [x] source-only policy for generated PDFs;
- [x] current-facing documentation separated from historical migration material;
- [x] causal-inference core and advanced specialist lecture series substantially expanded.

The current priority is to **finish the causal-inference domain deliberately rather than continue adding decks indefinitely**.

## Phase 1 — Presentation Infrastructure

**Status: complete.**

- [x] Standardize the shared Beamer shell.
- [x] Standardize active author identity and affiliation.
- [x] Add canonical presentation entry points.
- [x] Validate learning goals, synthesis, references, and contact slides.
- [x] Compile active decks in GitHub Actions.
- [x] Remove generated PDFs from source control.
- [x] Keep historical planning documents for provenance while marking them as historical.

## Phase 2 — Causal Inference Closeout

**Status: active.**

### Completed causal-inference expansion

- [x] Causal Econometrics
- [x] Panel Data and Fixed Effects
- [x] Difference-in-Differences and Event Studies
- [x] Instrumental Variables and 2SLS
- [x] Counterfactual Time-Series Methods
- [x] Selection on Observables
- [x] Dynamic Treatment Effects
- [x] Robustness and Sensitivity Analysis
- [x] Regression Discontinuity Designs
- [x] Heterogeneous Treatment Effects and Causal Forests
- [x] Causal Mediation Analysis
- [x] Policy Learning and Treatment Targeting
- [x] Double Machine Learning and Orthogonal Scores
- [x] Causal Discovery
- [x] Interference, Spillovers, and Network Causal Inference
- [x] Transportability and External Validity
- [x] Missing Data, Attrition, and Selection Bias
- [x] Measurement Error and Misclassification

### Remaining work

- [ ] **Partial Identification and Bounds** — current PR #125.
- [ ] **Principal Stratification and Post-Treatment Variables**
- [ ] **Time-Varying Treatments and Marginal Structural Models**
- [ ] **Causal-inference consolidation**
  - organize the domain into a coherent learning path;
  - update the domain README and supporting documentation;
  - review references and terminology across the causal decks;
  - verify every causal deck is registered in validation and CI;
  - remove duplicate or obsolete guidance;
  - declare the causal-inference domain complete.

### Hard stop

After the consolidation step, **no new causal-inference lecture topics are added as part of this expansion**.

The domain then enters maintenance mode:

- corrections;
- reference updates;
- accessibility fixes;
- teaching improvements;
- CI/build fixes.

New causal-inference decks should require a new roadmap decision rather than being appended opportunistically.

## Phase 3 — Repository-Wide Quality Pass

**Status: later.**

Once causal inference is closed:

- [ ] audit accessibility, contrast, font sizes, tables, and figure readability;
- [ ] review bibliography coverage and citation consistency across active decks;
- [ ] review dense decks that may need splitting for teaching duration;
- [ ] improve learning-path documentation across domains;
- [ ] review public slide previews and navigation;
- [ ] consolidate genuinely duplicated helpers only where duplication creates maintenance cost.

## Phase 4 — Next Domain Expansion

**Status: not started.**

Before adding another large batch of lectures:

1. choose the target domain;
2. create a finite issue/roadmap batch;
3. define its stop condition;
4. implement the batch in reviewable PRs;
5. consolidate the domain before moving again.

The next domain should be chosen deliberately rather than by continuing whichever topic happens to be convenient.

## Working Rules

- Use small, reviewable pull requests.
- Do not merge automatically.
- Keep `main` as the canonical integration branch.
- Prefer mathematically grounded and transparent teaching material.
- Do not add a method merely because it is fashionable.
- Preserve source-first reproducibility and CI compilation.
- Keep historical documents as history, not current instructions.
- Avoid endless topic expansion without a defined completion criterion.

## Definition of Done

The current roadmap cycle is complete when:

1. PR #125 is resolved;
2. Principal Stratification is added;
3. Time-Varying Treatments / Marginal Structural Models is added;
4. the causal-inference domain is consolidated and documented;
5. the causal-inference expansion is explicitly frozen;
6. repository-wide accessibility and citation work is moved to the next roadmap cycle.

At that point, the causal-inference domain is considered **complete for this expansion**.
