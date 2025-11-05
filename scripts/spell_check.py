#!/usr/bin/env python3
"""
Spell checker for LaTeX files in Academic Presentations.

This script checks LaTeX files for spelling errors, with special handling
for technical terms, citations, equations, and commands.

Usage:
    python scripts/spell_check.py file.tex
    python scripts/spell_check.py --all
    python scripts/spell_check.py --directory deep_learning/
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Set, Tuple

try:
    from spellchecker import SpellChecker
except ImportError:
    print("Error: spellchecker not installed. Run: pip install pyspellchecker")
    sys.exit(1)


# ============================================================================
# Configuration
# ============================================================================

# Technical terms and acronyms to ignore
TECHNICAL_TERMS = {
    # Math/Stats
    "arima", "arma", "sarima", "garch", "lstm", "gru", "relu", "softmax",
    "sigmoid", "tanh", "pooling", "backpropagation", "autoregressive",
    "stationarity", "heteroskedasticity", "autocorrelation", "cointegration",

    # ML/AI
    "sklearn", "pytorch", "tensorflow", "numpy", "scipy", "pandas",
    "xgboost", "lightgbm", "scikit", "keras", "theano",

    # Causal
    "dag", "dags", "rdd", "did", "instrumental", "endogeneity", "exogeneity",

    # Bayesian/MCMC
    "mcmc", "mh", "hmc", "nuts", "metropolis", "hastings", "gibbs",
    "variational", "elbo", "kl",

    # RL
    "mdp", "mdps", "bellman", "sarsa", "dqn", "ppo", "trpo", "ddpg",

    # General
    "hyperparameter", "hyperparameters", "overfitting", "underfitting",
    "dataset", "datasets", "preprocessing", "minibatch", "optimizer",

    # Names
    "diogo", "ribeiro", "esmad", "mysense",

    # Abbreviations
    "etc", "eg", "ie", "vs", "http", "https", "www",
}

# LaTeX commands to ignore content within
LATEX_ENVIRONMENTS_TO_SKIP = {
    r'\\begin\{equation\}.*?\\end\{equation\}',
    r'\\begin\{align\}.*?\\end\{align\}',
    r'\\begin\{lstlisting\}.*?\\end\{lstlisting\}',
    r'\\begin\{verbatim\}.*?\\end\{verbatim\}',
    r'\$.*?\$',  # Inline math
    r'\$\$.*?\$\$',  # Display math
    r'\\cite\{.*?\}',  # Citations
    r'\\ref\{.*?\}',  # References
    r'\\label\{.*?\}',  # Labels
    r'\\includegraphics.*?\{.*?\}',  # Graphics
    r'\\url\{.*?\}',  # URLs
    r'\\href\{.*?\}\{.*?\}',  # Hyperlinks
}

# LaTeX commands to remove but keep their content
LATEX_COMMANDS_TO_STRIP = [
    r'\\textbf\{(.*?)\}',
    r'\\textit\{(.*?)\}',
    r'\\emph\{(.*?)\}',
    r'\\textrm\{(.*?)\}',
    r'\\texttt\{(.*?)\}',
]


# ============================================================================
# LaTeX Processing
# ============================================================================

def extract_text_from_latex(content: str) -> str:
    """
    Extract plain text from LaTeX content for spell checking.

    Parameters
    ----------
    content : str
        LaTeX file content

    Returns
    -------
    text : str
        Extracted plain text
    """
    text = content

    # Remove comments
    text = re.sub(r'(?<!\\)%.*$', '', text, flags=re.MULTILINE)

    # Remove math and other environments
    for pattern in LATEX_ENVIRONMENTS_TO_SKIP:
        text = re.sub(pattern, ' ', text, flags=re.DOTALL)

    # Strip LaTeX commands but keep content
    for pattern in LATEX_COMMANDS_TO_STRIP:
        text = re.sub(pattern, r'\1', text)

    # Remove remaining LaTeX commands
    text = re.sub(r'\\[a-zA-Z]+\*?(?:\[.*?\])?\{.*?\}', ' ', text)
    text = re.sub(r'\\[a-zA-Z]+\*?', ' ', text)

    # Remove special characters
    text = re.sub(r'[{}\\]', ' ', text)

    return text


def tokenize(text: str) -> List[str]:
    """
    Split text into words for spell checking.

    Parameters
    ----------
    text : str
        Plain text

    Returns
    -------
    words : List[str]
        List of words
    """
    # Split on whitespace and punctuation
    words = re.findall(r'\b[a-zA-Z]+\b', text)

    # Convert to lowercase
    words = [w.lower() for w in words]

    # Filter out very short words and numbers
    words = [w for w in words if len(w) > 2]

    return words


# ============================================================================
# Spell Checking
# ============================================================================

def check_spelling(
    file_path: Path,
    custom_dictionary: Set[str] = None
) -> List[Tuple[str, List[str]]]:
    """
    Check spelling in a LaTeX file.

    Parameters
    ----------
    file_path : Path
        Path to LaTeX file
    custom_dictionary : Set[str], optional
        Additional words to ignore

    Returns
    -------
    errors : List[Tuple[str, List[str]]]
        List of (misspelled_word, suggestions) tuples
    """
    # Read file
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

    # Extract text
    text = extract_text_from_latex(content)

    # Tokenize
    words = tokenize(text)

    # Initialize spell checker
    spell = SpellChecker()

    # Add custom dictionary
    if custom_dictionary:
        spell.word_frequency.load_words(custom_dictionary)

    # Add technical terms
    spell.word_frequency.load_words(TECHNICAL_TERMS)

    # Find misspelled words
    misspelled = spell.unknown(words)

    # Get suggestions for each misspelled word
    errors = []
    for word in sorted(misspelled):
        suggestions = spell.candidates(word)
        if suggestions:
            errors.append((word, list(suggestions)[:5]))  # Top 5 suggestions

    return errors


# ============================================================================
# Reporting
# ============================================================================

def print_report(file_path: Path, errors: List[Tuple[str, List[str]]]):
    """Print spell checking report for a file."""
    if not errors:
        print(f"✓ {file_path}: No spelling errors found")
        return

    print(f"\n✗ {file_path}: {len(errors)} potential spelling errors")
    print("=" * 70)

    for word, suggestions in errors:
        print(f"\n  {word}")
        if suggestions:
            print(f"    Suggestions: {', '.join(suggestions)}")


# ============================================================================
# Main
# ============================================================================

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Spell check LaTeX files in Academic Presentations"
    )
    parser.add_argument(
        "file",
        nargs="?",
        type=Path,
        help="LaTeX file to check"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Check all LaTeX files in repository"
    )
    parser.add_argument(
        "--directory",
        type=Path,
        help="Check all LaTeX files in directory"
    )
    parser.add_argument(
        "--dictionary",
        type=Path,
        help="Custom dictionary file (one word per line)"
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only show files with errors"
    )

    args = parser.parse_args()

    # Load custom dictionary
    custom_dict = set()
    if args.dictionary and args.dictionary.exists():
        custom_dict = set(
            args.dictionary.read_text().strip().split('\n')
        )

    # Determine files to check
    if args.all:
        files = list(Path('.').rglob('*.tex'))
    elif args.directory:
        files = list(args.directory.rglob('*.tex'))
    elif args.file:
        files = [args.file]
    else:
        parser.print_help()
        return 1

    # Check each file
    total_errors = 0
    for file_path in sorted(files):
        # Skip build directories
        if any(p in str(file_path) for p in ['build', '.git', '__pycache__']):
            continue

        errors = check_spelling(file_path, custom_dict)

        if not args.quiet or errors:
            print_report(file_path, errors)

        total_errors += len(errors)

    # Summary
    print(f"\n{'=' * 70}")
    print(f"Checked {len(files)} files")
    print(f"Found {total_errors} potential spelling errors")

    return 0 if total_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
