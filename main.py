#!/usr/bin/env python3
"""Entry for make.fun's "One-Liner Marathon" bounty.

Prints one one-line joke (at most 280 characters) on any subject.
"""

import os

SETUP = "I'm not saying my cooking is terrible"
PUNCHLINE = "the smoke alarm and I are now in a committed relationship"


def build_line() -> str:
    """Assemble the joke from its parts."""
    return ", ".join([SETUP, PUNCHLINE]) + "."


def main() -> None:
    line = build_line()
    assert len(line) <= 280, f"joke too long: {len(line)} chars"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except OSError:
        pass
    print(line)


if __name__ == "__main__":
    main()
