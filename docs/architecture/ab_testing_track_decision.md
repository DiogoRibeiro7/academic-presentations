# A/B Testing Track Decision

## Decision

Keep **two separate A/B testing decks** in the curriculum:

- `04-causal-inference/ab-testing/presentation/ab_testing_experimental_design_beamer.tex`
- `04-causal-inference/ab-testing/presentation/a_b_testing_interview.tex`

## Rationale

- The two files serve different audiences:
- `ab_testing_experimental_design_beamer.tex` targets full instructional delivery.
- `a_b_testing_interview.tex` targets interview-focused preparation.
- Forcing a merge would increase conditional logic in one deck and reduce maintainability.

## Ownership And Folder Policy

- Canonical topic ownership is `04-causal-inference/ab-testing/`.
- Both decks remain in `presentation/` under this topic boundary.
- Supporting code belongs in `code/`.
- Exercises and assessments belong in `exercises/`.

## Maintenance Policy

- Shared conceptual updates (terminology, formula corrections, statistical caveats) must be reflected in both decks.
- Audience-specific examples are allowed to diverge.
- `main_presentation.tex` may point to either deck depending on delivery context.
- If long-term drift becomes costly, refactor shared content into reusable includes and keep audience wrappers separate.
