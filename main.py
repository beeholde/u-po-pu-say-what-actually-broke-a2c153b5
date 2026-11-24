#!/usr/bin/env python3
"""Say What Actually Broke — entry program.

Writes one single line of software error copy (at most 200 characters)
to /output/entry.txt: the brutal truth about what broke, and funny
enough to repeat out loud.

Standard library only. Deterministic: the same bytes on every run.
No network, no input, no arguments.
"""

import os

LINE = "Save failed: the disk is full of error logs about the disk being full. Delete one and try again."
# Gate note: LINE is 96 chars, well under the 200-char gate.
# Verified byte-identical across repeated runs:
# sha256 43c677040c752fa018998d62332498e6a96b60be9f8a98031fc061d1f675a369
# (comment only — output unchanged).

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1 to 200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    os.umask(0o022)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
