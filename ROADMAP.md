# Academic Presentations Roadmap

This roadmap tracks the repository cleanup and standardization work from the current 2026 baseline. It is intentionally implementation-focused: completed work is recorded briefly, active work is explicit, and future work is ordered by repository risk rather than by cosmetic priority.

## Current Objective

Bring the repository to one coherent presentation system without rewriting teaching content.

The canonical Beamer model is:

- Madrid theme;
- default Beamer color theme;
- red presentation palette;
- canonical `code` listing style for Python;
- current author identity and affiliation;
- preservation of existing `\documentclass` options such as `aspectratio=169` and `11pt`;
- topic-specific packages, mathematical notation, diagrams, and language-specific listing definitions retained where needed.

The repository should favor direct source edits, ordinary compile CI, and small reviewable pull requests. It should not depend on source normalizers, generated preambles, or self-modifying workflows.

## Completed

### Canonical author identity

- [x] Add `shared/author.json` as the canonical author metadata record.
- [x] Set the active affiliation to **Faculty of Media Arts and Design, Technical University of Porto**.
- [x] Keep ORCID `0009-0001-2022-7072` and the active `dfr@esmad.ipp.pt` contact address.
- [x] Remove MySense.ai as a current affiliation from the shared theme and public README identity.
- [x] Add the canonical LinkedIn profile.
- [x] Validate active author metadata in CI.

### Bibliography integrity

- [x] Repair invalid or mismatched DOI metadata identified during the repository audit.
- [x] Keep bibliography validation and link checking in CI.

### Canonical Beamer model

- [x] Convert the existing shared theme into a compatibility/helper layer around the Madrid/default red model.
- [x] Remove the competing custom title-page and footline visual system from the shared theme.
- [x] Standardize the canonical Python `code` listing style.
- [x] Preserve compatibility helpers and mathematical commands used by existing decks.
- [x] Update the public Beamer style guide to document the actual canonical model.

### Standalone presentation migration

The following standalone decks have been migrated with reviewable shell-level changes while preserving their teaching content:

- [x] Feature Engineering
- [x] Principal Component Analysis
- [x] Statistical Modeling
- [x] Extended Statistical Modeling
- [x] MCMC
- [x] Bayesian Machine Learning
- [x] ARMA Processes
- [x] Stationarity and Ergodicity
- [x] Object-Oriented Programming
- [x] Streaming Pipeline Processing

Existing decks that consume the shared theme now inherit the canonical visual model through that theme.

### LaTeX regression coverage

- [x] Compile presentation sources from their own source directories.
- [x] Expand the static CI matrix from 13 to all **21 standalone Beamer entry points**.
- [x] Compile both exercise sets alongside presentation sources.
- [x] Trigger the LaTeX workflow when its own workflow file changes.
- [x] Verify the complete 21-presentation matrix successfully on an exact pull-request head.

## In Progress

### Shared presentation template

- [ ] Merge the standardized shared template after exact-head CI and review.

The template update removes stale ESMAD/MySense current metadata, describes the canonical red model, and keeps the existing mathematical and helper demonstrations intact.

### Remaining long standalone decks

These three files still require direct shell migration:

- [ ] `00-programming-fundamentals/r-programming/presentation/R_programming.tex`
- [ ] `04-causal-inference/ab-testing/presentation/a_b_testing_interview.tex`
- [ ] `04-causal-inference/causal-inference-fundamentals/presentation/causal_inference_beamer.tex`

They are intentionally deferred because previous full-file rewrites produced unacceptable teaching-content churn. Their migration must preserve the complete existing lecture body and modify only presentation shell, listing style where appropriate, and active identity metadata.

## Next

### 1. Finish visual-shell consistency

- [ ] Migrate R Programming with its existing R-specific listing definitions preserved.
- [ ] Migrate A/B Testing without changing its broader experimentation, causal inference, modeling, drift, MLOps, SQL, survival, or visualization content.
- [ ] Migrate Causal Inference without changing its teaching body.
- [ ] Run the full 21-presentation matrix after each migration slice.
- [ ] Audit final source diffs for unexpected content churn before merge.

### 2. Remove stale active identity from source files

The shared theme already prevents stale affiliation from rendering in many decks, but copied source metadata should also become honest and consistent.

- [ ] Replace active `ESMAD - Escola Superior de Média Arte e Design` affiliation strings with the current faculty name where they describe Diogo's current affiliation.
- [ ] Remove active `Lead Data Scientist, Mysense.ai` / MySense.ai metadata from presentation sources, templates, and current documentation.
- [ ] Preserve genuine historical references in changelog/history material.
- [ ] Keep technical compatibility names such as `esmad_beamer_theme.sty`, legacy color aliases, and the active `dfr@esmad.ipp.pt` email where renaming would add risk without user value.

### 3. Clean current documentation

Priority files identified during the audit include:

- [ ] `COMPLETION_SUMMARY.md`
- [ ] `assessments/README.md`
- [ ] `docs/enhancement-guides/INDUSTRY_FOCUS_ENHANCEMENT_GUIDE.md`
- [ ] other current documentation that still presents old ESMAD/MySense identity as active.

The `CHANGELOG.md` should remain historical. Only statements that claim to describe the current repository state should be corrected there.

### 4. Establish a consistent repository contract

- [ ] Define the expected directory layout for each presentation topic.
- [ ] Distinguish source files, figures, references, exercises, and generated artifacts consistently.
- [ ] Audit duplicate or obsolete presentation sources before deleting anything.
- [ ] Remove stale implementation-summary/generated report files that no longer describe the repository accurately.

### 5. Generated artifact policy

PDFs are currently ignored by `.gitignore` but some generated PDFs remain tracked historically.

- [ ] Decide whether generated PDFs belong in Git history or only in CI/release artifacts.
- [ ] Apply that policy consistently across presentation and exercise directories.
- [ ] Avoid mixing source-cleanup changes with mass binary deletion in the same PR.

### 6. Public repository metadata

- [ ] Update the GitHub repository description, which still references the former ESMAD/MySense identity.
- [ ] Review repository topics and public-facing metadata for current terminology.
- [ ] Ensure README, style guide, roadmap, template, and GitHub repository description tell the same story.

## Later Improvements

These are useful only after source identity, visual consistency, and compile coverage are stable.

- [ ] Audit accessibility of figures, contrast, font sizes, and dense slides.
- [ ] Add presentation-specific content quality checks where they can be objective and low-maintenance.
- [ ] Review bibliography coverage and citation consistency across all decks.
- [ ] Consolidate genuinely duplicated helpers only when duplication creates maintenance cost.
- [ ] Consider automated discovery of presentation entry points only if the static 21-entry matrix becomes burdensome to maintain.

## Explicit Non-Goals

The cleanup should **not**:

- rewrite lectures merely to make source files look alike;
- remove `aspectratio`, font-size, or other valid `\documentclass` options;
- force Python listing syntax onto R, SQL, or pseudocode examples;
- replace the existing theme with another generated abstraction;
- introduce a source normalizer or a workflow that rewrites repository files;
- rewrite genuine historical affiliations in changelog/history material;
- rename compatibility files or commands without a concrete maintenance benefit.

## Definition of Done

The repository cleanup is complete when:

1. all 21 standalone Beamer entry points compile in CI;
2. every active presentation uses or inherits the same canonical Madrid/red visual shell;
3. current author identity is consistent across active presentation sources and documentation;
4. no active material presents MySense.ai as a current affiliation;
5. the old ESMAD display name is used only where historically or technically necessary;
6. the shared template creates a compliant presentation by default;
7. repository structure and generated-artifact policy are documented and consistently applied;
8. final changes are reviewable without unexplained teaching-content churn.
