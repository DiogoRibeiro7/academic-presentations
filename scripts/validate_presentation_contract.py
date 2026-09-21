"""Validate the canonical LaTeX presentation entry-point contract."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Final

ROOT: Final[Path] = Path(__file__).resolve().parents[1]

PRIMARY_ENTRY_POINTS: Final[tuple[Path, ...]] = (
    Path("00-programming-fundamentals/r-programming/presentation/main.tex"),
    Path("01-foundations/feature-engineering/presentation/main.tex"),
    Path("01-foundations/optimization/presentation/main.tex"),
    Path("01-foundations/pca/presentation/main.tex"),
    Path("01-foundations/statistical-modeling/presentation/main.tex"),
    Path("02-deep-learning/deep-learning-fundamentals/presentation/main.tex"),
    Path("02-deep-learning/reinforcement-learning/presentation/main.tex"),
    Path("03-bayesian-methods/bayesian-machine-learning/presentation/main.tex"),
    Path("03-bayesian-methods/mcmc/presentation/main.tex"),
    Path("04-causal-inference/ab-testing/presentation/main.tex"),
    Path("04-causal-inference/causal-inference-fundamentals/presentation/main.tex"),
    Path("05-time-series/time-series-forecasting/presentation/main.tex"),
    Path("06-advanced-topics/ai-agents/presentation/main.tex"),
    Path("06-advanced-topics/computer-science/presentation/main.tex"),
    Path("06-advanced-topics/explainable-ai/presentation/main.tex"),
    Path("08-data-science-applications-course/presentation/main.tex"),
)

ADDITIONAL_STANDALONE_TRACKS: Final[tuple[Path, ...]] = (
    Path("01-foundations/statistical-modeling/presentation/diogo_ribeiro_beamer_extended.tex"),
    Path("05-time-series/time-series-forecasting/presentation/ARMA_processes.tex"),
    Path("05-time-series/time-series-forecasting/presentation/stationary_ergodicity.tex"),
    Path("06-advanced-topics/computer-science/presentation/streaming_pipeline_processing.tex"),
)

INPUT_RE: Final[re.Pattern[str]] = re.compile(r"\\input\{([^}]+)\}")
SHARED_THEME_TOKEN: Final[str] = "esmad_beamer_theme"


def _read(path: Path) -> str:
    """Read one UTF-8 repository file."""

    absolute_path: Path = ROOT / path
    if not absolute_path.is_file():
        raise FileNotFoundError(f"Missing required presentation file: {path}")
    return absolute_path.read_text(encoding="utf-8")


def _resolve_primary_source(main_path: Path) -> Path:
    """Resolve the source selected by a canonical main.tex wrapper."""

    content: str = _read(main_path)
    matches: list[str] = INPUT_RE.findall(content)
    if len(matches) != 1:
        raise ValueError(
            f"{main_path} must contain exactly one input target; found {len(matches)}"
        )

    target: Path = main_path.parent / matches[0]
    return target if target.suffix else target.with_suffix(".tex")


def _assert_shared_theme(path: Path) -> None:
    """Require a standalone Beamer source to inherit the shared theme."""

    content: str = _read(path)
    if "\\documentclass" not in content or "{beamer}" not in content:
        raise ValueError(f"{path} is not a standalone Beamer source")
    if SHARED_THEME_TOKEN not in content:
        raise ValueError(f"{path} does not inherit the shared Beamer theme")


def main() -> int:
    """Validate the repository presentation contract."""

    errors: list[str] = []

    for main_path in PRIMARY_ENTRY_POINTS:
        try:
            source_path: Path = _resolve_primary_source(main_path)
            _assert_shared_theme(source_path)
        except (FileNotFoundError, ValueError) as exc:
            errors.append(str(exc))

    for source_path in ADDITIONAL_STANDALONE_TRACKS:
        try:
            _assert_shared_theme(source_path)
        except (FileNotFoundError, ValueError) as exc:
            errors.append(str(exc))

    if errors:
        print("Presentation contract validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(
        "Presentation contract valid: "
        f"{len(PRIMARY_ENTRY_POINTS)} primary main.tex entry points and "
        f"{len(ADDITIONAL_STANDALONE_TRACKS)} additional standalone tracks."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
