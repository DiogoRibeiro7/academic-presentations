#!/usr/bin/env python3
"""Normalize every standalone Beamer document to the repository shell.

The script intentionally changes only presentation infrastructure. Topic-specific
packages, macros, titles, authors, institutes, and document bodies are preserved.

Run with ``--write`` to migrate files or ``--check`` in CI to reject drift.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Final

REPO_ROOT: Final[Path] = Path(__file__).resolve().parents[1]
DOCUMENTCLASS_RE: Final[re.Pattern[str]] = re.compile(
    r"^\\documentclass(?:\[[^\]]*\])?\{beamer\}\s*$", re.MULTILINE
)
BEGIN_DOCUMENT: Final[str] = r"\begin{document}"
BLOCK_START: Final[str] = "% BEGIN CANONICAL BEAMER SHELL"
BLOCK_END: Final[str] = "% END CANONICAL BEAMER SHELL"

CANONICAL_BLOCK: Final[str] = r"""% BEGIN CANONICAL BEAMER SHELL
\usepackage{bookmark}

% Theme and color customization
\usetheme{Madrid}
\usecolortheme{default}
\usepackage{listings}
\usepackage{xcolor}

\lstdefinestyle{code}{
  language=Python,
  basicstyle=\ttfamily\small,
  keywordstyle=\color{blue},
  commentstyle=\color{gray},
  stringstyle=\color{red!60!black},
  showstringspaces=false,
  tabsize=2,
  breaklines=true
}

\setbeamercolor{palette primary}{bg=red, fg=white}
\setbeamercolor{palette secondary}{bg=red!95!black, fg=white}
\setbeamercolor{palette tertiary}{bg=red!90!black, fg=white}
\setbeamercolor{frametitle}{bg=red, fg=white}
\setbeamercolor{title}{bg=red, fg=white}
\setbeamercolor{section in toc}{fg=red}
% END CANONICAL BEAMER SHELL"""

EXACT_PACKAGE_LINES: Final[set[str]] = {
    r"\usepackage{bookmark}",
    r"\usepackage{listings}",
    r"\usepackage{xcolor}",
}

STYLE_LINE_PATTERNS: Final[tuple[re.Pattern[str], ...]] = (
    re.compile(r"^\s*\\usetheme\{[^}]+\}\s*$"),
    re.compile(r"^\s*\\usecolortheme\{[^}]+\}\s*$"),
    re.compile(r"^\s*\\setbeamercolor\{palette primary\}\{.*\}\s*$"),
    re.compile(r"^\s*\\setbeamercolor\{palette secondary\}\{.*\}\s*$"),
    re.compile(r"^\s*\\setbeamercolor\{palette tertiary\}\{.*\}\s*$"),
    re.compile(r"^\s*\\setbeamercolor\{frametitle\}\{.*\}\s*$"),
    re.compile(r"^\s*\\setbeamercolor\{title\}\{.*\}\s*$"),
    re.compile(r"^\s*\\setbeamercolor\{section in toc\}\{.*\}\s*$"),
)


def _remove_marked_block(text: str) -> str:
    """Remove a previously generated canonical shell block."""
    pattern = re.compile(
        rf"\n?{re.escape(BLOCK_START)}.*?{re.escape(BLOCK_END)}\n?",
        re.DOTALL,
    )
    return pattern.sub("\n", text)


def _remove_named_listing_style(text: str, style_name: str) -> str:
    """Remove one ``\\lstdefinestyle{name}{...}`` command using brace counting."""
    marker = rf"\lstdefinestyle{{{style_name}}}{{"
    start = text.find(marker)
    while start != -1:
        index = start + len(marker)
        depth = 1
        while index < len(text) and depth:
            char = text[index]
            if char == "{" and (index == 0 or text[index - 1] != "\\"):
                depth += 1
            elif char == "}" and (index == 0 or text[index - 1] != "\\"):
                depth -= 1
            index += 1
        if depth != 0:
            raise ValueError(f"Unbalanced listing style {style_name!r}")
        while index < len(text) and text[index] in " \t":
            index += 1
        if index < len(text) and text[index] == "\n":
            index += 1
        text = text[:start] + text[index:]
        start = text.find(marker)
    return text


def _clean_preamble(preamble: str) -> str:
    """Remove shell directives superseded by the canonical block."""
    preamble = _remove_marked_block(preamble)
    preamble = _remove_named_listing_style(preamble, "code")

    kept: list[str] = []
    for line in preamble.splitlines():
        stripped = line.strip()
        if stripped in EXACT_PACKAGE_LINES:
            continue
        if any(pattern.match(line) for pattern in STYLE_LINE_PATTERNS):
            continue
        kept.append(line)
    return "\n".join(kept).rstrip()


def normalize_text(text: str) -> str:
    """Return normalized source for one standalone Beamer document."""
    match = DOCUMENTCLASS_RE.search(text)
    if match is None:
        return text
    if BEGIN_DOCUMENT not in text:
        raise ValueError("Beamer document has no \\begin{document}")

    text = DOCUMENTCLASS_RE.sub(r"\\documentclass{beamer}", text, count=1)
    begin_index = text.index(BEGIN_DOCUMENT)
    preamble = text[:begin_index]
    body = text[begin_index:]
    preamble = _clean_preamble(preamble)

    docclass = r"\documentclass{beamer}"
    if not preamble.startswith(docclass):
        # Preserve leading whitespace/comments before the class declaration.
        class_index = preamble.index(docclass)
        before = preamble[: class_index + len(docclass)]
        after = preamble[class_index + len(docclass) :].lstrip("\n")
        preamble = f"{before}\n\n{CANONICAL_BLOCK}\n\n{after}".rstrip()
    else:
        after = preamble[len(docclass) :].lstrip("\n")
        preamble = f"{docclass}\n\n{CANONICAL_BLOCK}\n\n{after}".rstrip()

    return f"{preamble}\n\n{body}"


def find_beamer_files(root: Path) -> list[Path]:
    """Return all tracked-source candidates that are standalone Beamer documents."""
    result: list[Path] = []
    for path in sorted(root.rglob("*.tex")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if DOCUMENTCLASS_RE.search(text):
            result.append(path)
    return result


def run(*, write: bool) -> int:
    """Normalize or validate all Beamer sources and return a process status."""
    changed: list[Path] = []
    for path in find_beamer_files(REPO_ROOT):
        original = path.read_text(encoding="utf-8")
        normalized = normalize_text(original)
        if normalized != original:
            changed.append(path.relative_to(REPO_ROOT))
            if write:
                path.write_text(normalized, encoding="utf-8")

    if changed and not write:
        print("Beamer shell drift detected:")
        for path in changed:
            print(f"  - {path}")
        print("Run: python scripts/normalize_beamer_preambles.py --write")
        return 1

    action = "Normalized" if write else "Validated"
    print(f"{action} {len(find_beamer_files(REPO_ROOT))} Beamer documents.")
    if write and changed:
        print(f"Updated {len(changed)} files.")
    return 0


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="Rewrite Beamer sources in place.")
    mode.add_argument("--check", action="store_true", help="Fail if any Beamer source would change.")
    return parser.parse_args()


def main() -> int:
    """CLI entry point."""
    args = parse_args()
    return run(write=bool(args.write))


if __name__ == "__main__":
    raise SystemExit(main())
