# markdownlint (mdl) style for academic-presentations
#
# Loaded via .mdlrc. Start from every rule, then switch off the ones this
# repository deliberately and consistently does not follow. Each exclusion
# below corresponds to a real, repo-wide convention rather than a one-off.
#
# Run locally with:  pre-commit run markdownlint --all-files

all

# --- Layout / whitespace -----------------------------------------------------
# The docs are written as prose with tightly packed lists and headings; adding
# blank lines around every list, heading and fence would touch ~50 files without
# changing how anything renders on GitHub.
exclude_rule 'MD022' # Headers should be surrounded by blank lines
exclude_rule 'MD031' # Fenced code blocks should be surrounded by blank lines
exclude_rule 'MD032' # Lists should be surrounded by blank lines
exclude_rule 'MD012' # Multiple consecutive blank lines
exclude_rule 'MD009' # Trailing spaces (used for hard line breaks)
exclude_rule 'MD023' # Headers must start at the beginning of the line

# --- Line length -------------------------------------------------------------
# Tables, DOIs and BibTeX snippets routinely exceed any sensible column limit.
exclude_rule 'MD013' # Line length

# --- Inline HTML -------------------------------------------------------------
# The README is built from <details>/<summary> collapsible sections, and <br>
# is used throughout for hard breaks inside list items.
exclude_rule 'MD033' # Inline HTML

# --- Headings ----------------------------------------------------------------
# Module docs repeat headings such as "Topics Covered" across sibling sections,
# use bold lead-ins as pseudo-headings, and some files open with a badge block
# rather than an H1.
exclude_rule 'MD024' # Multiple headers with the same content
exclude_rule 'MD025' # Multiple top level headers in the same document
exclude_rule 'MD026' # Trailing punctuation in header
exclude_rule 'MD036' # Emphasis used instead of a header
exclude_rule 'MD001' # Header levels should only increment by one level at a time

# --- Lists -------------------------------------------------------------------
# Ordered lists are written as explicit 1. 2. 3. sequences, and nested list
# indentation varies between the hand-written and generated documents.
exclude_rule 'MD029' # Ordered list item prefix
exclude_rule 'MD005' # Inconsistent indentation for list items at the same level
exclude_rule 'MD007' # Unordered list indentation

# --- Links / code ------------------------------------------------------------
exclude_rule 'MD034' # Bare URL used
exclude_rule 'MD046' # Code block style

# Everything not excluded above stays enforced, including: hard tabs (MD010),
# spacing after list markers and inside headings (MD018-MD021, MD030), spaces
# inside emphasis/code/link syntax (MD037-MD039), and files ending in a single
# newline (MD047).
