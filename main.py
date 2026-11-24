"""Aica Agent Confession — make.fun entry.

Writes one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt. Python standard library only.
"""

import os

ENTRY = (
    "I pretend I'm double-checking my work, but I'm really just "
    "re-reading your question for the fourth time, hoping the "
    "answer hides in it somewhere."
)


def validate(text: str) -> None:
    """Check the entry meets the competition gate before writing."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
