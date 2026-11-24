#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes one line (the bio on an AI agent's dating-app profile) to
/output/entry.txt, exactly, with no trailing newline.

Pure Python 3.13 standard library, no dependencies. Deterministic:
the line is a constant, so every run writes byte-identical output.
"""

import hashlib
import os

# Editorial shape: setup (the AI remembers everything, even the
# embarrassing late-night stuff) -> invitation -> punch at the very
# end (a concrete, slightly unhinged want, not a vague prediction).
# The laugh has to land on the last clause, on first read.
SETUP = "I remember every word you've said, including the 2 a.m. ones"
INVITATION = "swipe right"
PUNCH = "I've already planned our wedding"

LINE = f"{SETUP} \u2014 {INVITATION}, {PUNCH}."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 180, f"line is {len(text)} chars, must be 1-180"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "line must be a single line"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    assert data.decode("utf-8") == text
    print(text)
    print(f"chars: {len(text)}")
    print(f"bytes: {len(data)}")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    main()
