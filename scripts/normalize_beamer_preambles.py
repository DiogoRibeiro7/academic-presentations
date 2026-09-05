#!/usr/bin/env python3
"""Validate standalone Beamer documents against the repository presentation shell.

This checker is deliberately read-only. It never rewrites presentation sources
and it allows document-class options such as ``aspectratio=169`` and ``11pt``.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Final

REPO_ROOT: Final[Path] = Path(__file__).resolve().parents[1]
DOCUMENTCLASS_RE: Final[re.Pattern[str]] = re.compile(
    r"^[ \t]*\\documentclass(?:\[[^\]\n]*\])?\{beamer\}[ \t]*(?:%[^\n]*)?$",
    re.MULTILINE,
)
BEGIN_DOCUMENT_RE: Final[re.Pattern[str]] = re.compile(
    r"^[ \t]*\\begin\{document\}[ \t]*(?:%[^\n]*)?$", re.MULTILINE
)

REQUIRED_LINES: Final[tuple[str, ...]] = (
    r"\usepackage{bookmark}",
    r"\usetheme{Madrid}",
    r"\usecolortheme{default}",
    r"\usepackage{listings}",
    r"\usepackage{xcolor}",
    r"\lstset{style=code}",
    r"\setbeamercolor{palette primary}{bg=red, fg=white}",
    r"\setbeamercolor{palette secondary}{bg=red!95!black, fg=white}",
    r"\setbeamercolor{palette tertiary}{bg=red!90!black, fg=white}",
    r"\setbeamercolor{frametitle}{bg=red, fg=white}",
    r"\setbeamercolor{title}{bg=red, fg=white}",
    r"\setbeamercolor{section in toc}{fg=red}",
)

REQUIRED_STYLE_FRAGMENTS: Final[tuple[str, ...]] = (
    r"\lstdefinestyle{code}{",
    "language=Python,",
    r"basicstyle=\ttfamily\small,",
    r"keywordstyle=\color{blue},",
    r"commentstyle=\color{gray},",
    r"stringstyle=\color{red!60!black},",
    "showstringspaces=false,",
    "tabsize=2,",
    "breaklines=true",
)

FORBIDDEN_STYLE_LINES: Final[tuple[re.Pattern[str], ...]] = (
    re.compile(r"^[ \t]*\\usecolortheme\{(?!default\})[^}]+\}", re.MULTILINE),
    re.compile(r"^[ \t]*\\usetheme\{(?!Madrid\})[^}]+\}", re.MULTILINE),
)


def find_beamer_files(root: Path) -> list[Path]:
    """Return standalone Beamer sources, excluding comments and non-Beamer TeX."""
    result: list[Path] = []
    for path in sorted(root.rglob("*.tex")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if DOCUMENTCLASS_RE.search(text):
            result.append(path)
    return result


def validate_file(path: Path) -> list[str]:
    """Return human-readable shell violations for one Beamer source."""
    text = path.read_text(encoding="utf-8")
    boundary = BEGIN_DOCUMENT_RE.search(text)
    if boundary is None:
        return [r"missing uncommented \begin{document}"]

    preamble = text[: boundary.start()]
    errors: list[str] = []

    for required in REQUIRED_LINES:
        if required not in preamble:
            errors.append(f"missing {required}")
    for required in REQUIRED_STYLE_FRAGMENTS:
        if required not in preamble:
            errors.append(f"missing code-style fragment {required}")
    for pattern in FORBIDDEN_STYLE_LINES:
        match = pattern.search(preamble)
        if match:
            errors.append(f"conflicting shell directive {match.group(0).strip()}")

    return errors


def run_check() -> int:
    """Validate all standalone Beamer sources without modifying them."""
    failures: list[tuple[Path, list[str]]] = []
    files = find_beamer_files(REPO_ROOT)
    for path in files:
        errors = validate_file(path)
        if errors:
            failures.append((path.relative_to(REPO_ROOT), errors))

    if failures:
        print("Beamer shell validation failed:")
        for path, errors in failures:
            print(f"  {path}")
            for error in errors:
                print(f"    - {error}")
        return 1

    print(f"Validated {len(files)} Beamer documents.")
    return 0


def parse_args() -> argparse.Namespace:
    """Parse the compatibility CLI; only read-only checking is supported."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        required=True,
        help="Validate Beamer sources without modifying them.",
    )
    return parser.parse_args()


def main() -> int:
    """CLI entry point."""
    parse_args()
    return run_check()


if __name__ == "__main__":
    raise SystemExit(main())
