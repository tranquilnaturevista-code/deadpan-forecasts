#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist — entry program.

Writes one hand-written deadpan weather forecast to
``/output/entry.txt`` (or ``$OUTPUT_DIR/entry.txt``). The line is fixed:
the same forecast on every run, so the entry the judge reads is
exactly the line below.

Before writing, the program checks the line against the competition
gate — UTF-8 text of 1 to 160 characters, not only whitespace, all on
one line — and exits without writing anything if the gate fails. After
writing it reads the file back and checks the gate again on the text
actually on disk.
"""

import os
import sys

FORECAST = (
    "In Gloomsbury, 48 degrees and fog down to 12 metres visibility, "
    "so dense the lighthouse keeper has filed a formal complaint "
    "the fog ignored."
)

GATE_MIN = 1
GATE_MAX = 160


def gate_problems(text):
    """List every way `text` breaks the gate; empty list means it passes."""
    problems = []
    if not text.strip():
        problems.append("entry is blank or only whitespace")
    if not GATE_MIN <= len(text) <= GATE_MAX:
        problems.append(
            "entry is %d characters, gate needs %d-%d"
            % (len(text), GATE_MIN, GATE_MAX)
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    if any(ord(ch) < 32 and ch not in "\n\r" for ch in text):
        problems.append("entry contains control characters")
    return problems


def fail(problems, where=""):
    for problem in problems:
        print("gate failure%s: %s" % (where, problem), file=sys.stderr)
    return 1


def main():
    problems = gate_problems(FORECAST)
    if problems:
        return fail(problems)

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(FORECAST)

    with open(path, encoding="utf-8") as handle:
        on_disk = handle.read()
    if on_disk != FORECAST:
        print("entry on disk differs from the forecast", file=sys.stderr)
        return 1
    problems = gate_problems(on_disk)
    if problems:
        return fail(problems, " on disk")

    print(
        "Wrote entry.txt: %d characters (%d bytes)"
        % (len(on_disk), len(on_disk.encode("utf-8")))
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
