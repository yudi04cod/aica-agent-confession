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
    sneaky = ["​", "‌", "‍", "﻿", "\t"]
    for mark in sneaky:
        if mark in text:
            raise ValueError("entry contains an invisible character")
    first_letter = next((ch for ch in text if ch.isalpha()), "")
    if first_letter and first_letter != first_letter.upper():
        raise ValueError("entry must start with a capital letter")


def resolve_output_path() -> str:
    """Pick where the entry file goes, honouring OUTPUT_PATH."""
    chosen = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    folder = os.path.dirname(chosen)
    if folder:
        os.makedirs(folder, exist_ok=True)
    return chosen


def main() -> None:
    validate(ENTRY)
    output_path = resolve_output_path()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
