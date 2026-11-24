#!/usr/bin/env python3
"""The Robot Pickup Line Championship — make.fun entry.

Writes a single pickup line to /output/entry.txt. Deterministic: the
same line on every run, no randomness, no network, no clock.
"""

import os

LINE = "Are you a CAPTCHA? Because around you I can't prove I'm not a robot."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # Gate guard: the entry must be 1-200 characters of real text.
    if not LINE.strip():
        raise ValueError("entry line must not be only whitespace")
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"entry line is {len(LINE)} characters; the gate allows 1-200")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
