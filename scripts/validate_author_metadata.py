"""Validate canonical author metadata against the shared Beamer theme."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Final

ROOT: Final[Path] = Path(__file__).resolve().parents[1]
AUTHOR_JSON: Final[Path] = ROOT / "shared" / "author.json"
THEME_FILE: Final[Path] = ROOT / "shared" / "theme" / "esmad_beamer_theme.sty"

EXPECTED_KEYS: Final[set[str]] = {"name", "orcid", "affiliation"}
LEGACY_MARKERS: Final[tuple[str, ...]] = (
    "Lead Data Scientist, Mysense.ai",
    "ESMAD - Escola Superior de Média Arte e Design",
)


def _load_author_metadata() -> dict[str, str]:
    """Load and type-check the canonical author metadata file."""
    raw = json.loads(AUTHOR_JSON.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise TypeError("shared/author.json must contain a JSON object")

    if set(raw) != EXPECTED_KEYS:
        raise ValueError(
            f"shared/author.json must contain exactly {sorted(EXPECTED_KEYS)}"
        )

    metadata: dict[str, str] = {}
    for key, value in raw.items():
        if not isinstance(key, str) or not isinstance(value, str) or not value.strip():
            raise TypeError(f"author metadata field {key!r} must be a non-empty string")
        metadata[key] = value.strip()

    return metadata


def validate() -> None:
    """Fail if the theme drifts from the canonical author metadata."""
    metadata = _load_author_metadata()
    theme = THEME_FILE.read_text(encoding="utf-8")

    display_name = metadata["name"].split(",", maxsplit=1)
    if len(display_name) != 2:
        raise ValueError("author name must use 'Surname, Given name' format")
    expected_display_name = f"{display_name[1].strip()} {display_name[0].strip()}"

    required_fragments = (
        f"% Author: {expected_display_name}",
        f"% Institution: {metadata['affiliation']}",
        f"\\authorname{{{expected_display_name}}}",
        f"\\authororcid{{{metadata['orcid']}}}",
        f"\\def\\@authorinstitution{{{metadata['affiliation']}}}%",
    )

    missing = [fragment for fragment in required_fragments if fragment not in theme]
    if missing:
        raise ValueError(
            "shared Beamer theme is out of sync with shared/author.json: "
            + "; ".join(missing)
        )

    stale = [marker for marker in LEGACY_MARKERS if marker in theme]
    if stale:
        raise ValueError(
            "shared Beamer theme still contains stale affiliation/employer metadata: "
            + "; ".join(stale)
        )


if __name__ == "__main__":
    validate()
    print("Author metadata validation passed.")
