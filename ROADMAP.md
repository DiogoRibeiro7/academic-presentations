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
- [x] Set the active affiliation to **FMAD - UTP**.
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

### Canonical presentation entry points

- [x] Add `presentation/main.tex` as the primary entry point for every presentation topic.
- [x] Keep named standalone entry points only for genuine additional presentation tracks.
- [x] Make every standalone Beamer source inherit the shared canonical theme.
- [x] Enforce the entry-point contract in CI.
- [x] Remove the obsolete `develop` branch trigger from the LaTeX workflow.

### LaTeX regression coverage

- [x] Compile presentation sources from their own source directories.
- [x] Expand the static CI matrix from 13 to all **21 standalone Beamer entry points**.
- [x] Compile both exercise sets alongside presentation sources.
- [x] Trigger the LaTeX workflow when its own workflow file changes.
- [x] Verify the complete 21-presentation matrix successfully on an exact pull-request head.

## Current State

The repository-wide presentation migration is complete:

- [x] All 20 active compiled course decks expose the canonical presentation structure.
- [x] All 4 genuine additional standalone tracks inherit the shared shell.
- [x] The complete presentation matrix compiles on CI.
- [x] Current affiliation is **FMAD - UTP** across active presentation sources.
- [x] MySense.ai is absent from current presentation metadata.
- [x] Every active compiled deck has learning goals/objectives, a synthesis, references, and the shared contact slide.
- [x] Standalone acknowledgement and “Thank you” filler slides have been removed from active compiled decks.
- [x] The academic content contract is enforced by `scripts/validate_presentation_contract.py`.

## Next

### 1. Repository structure and generated artifacts

- [x] Preserve genuine alternate sources such as the PCA proof-oriented handout and the Data Science Applications composite Beamer source.
- [x] Remove obsolete PDF-only `main_presentation.tex` aggregation wrappers that were unreferenced by CI/build workflows.
- [x] Adopt a source-only Git policy for generated PDFs: `.tex` sources remain in Git, compiled PDFs live in CI/release artifacts.
- [x] Remove historically tracked generated PDFs from presentation, exercise, and assessment directories.
- [x] Ignore future generated PDFs with `*.pdf` in `.gitignore`.

### 2. Current documentation cleanup

- [x] Correct current-facing README/build/assessment documentation that contradicted the source-only PDF and canonical-entry-point policies.
- [x] Clearly label 2025 enhancement guides as historical planning documents rather than current repository instructions.
- [x] Keep genuine migration/changelog history intact and separate from current-state documentation.
- [ ] Review remaining historical/generated summary documents for redundant or misleading current-state claims.

### 3. Public repository metadata

- [ ] Review the GitHub repository description and topics against the current FMAD - UTP identity.
- [ ] Keep README, style guide, roadmap, template, and public repository metadata aligned.

### 4. Accessibility and presentation ergonomics

- [ ] Audit dense slides, minimum font sizes, contrast, table readability, and figure legibility.
- [ ] Review alt-text or textual equivalents where figures carry essential information.
- [ ] Identify decks that should be split for teaching duration rather than compressed further.

### 5. Citation and source hygiene

- [ ] Audit bibliography coverage and citation consistency across all active decks.
- [ ] Prefer stable primary/academic references over tool documentation when a scientific claim is being supported.
- [ ] Check that current software/version claims are either evergreen or maintained deliberately.

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

The presentation-standardization phase is complete when:

1. all supported standalone Beamer entry points compile in CI;
2. every active presentation inherits the canonical Madrid/red shell;
3. current author identity is consistent across active presentation sources;
4. every active compiled deck satisfies the academic content contract;
5. the shared template creates a compliant presentation by default.

The broader repository-cleanup phase remains open until generated-artifact policy, obsolete-source review, current documentation, public repository metadata, accessibility, and citation hygiene are also complete.
