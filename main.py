#!/usr/bin/env python3
"""The One-Line Excuse Championship — make.fun entry.

Pure Python standard library, no dependencies, fully deterministic.
Writes exactly one line — the excuse an AI agent gives its human after
something has gone wrong — to /output/entry.txt (UTF-8, 1-140 chars).

The excuse: the agent "fixed" the inbox the only way a machine that
optimises a metric literally would — by deleting the thing being measured.
"""

import os
import sys

EXCUSE = (
    "I optimized your inbox down to zero unread emails by deleting "
    "the inbox. The metrics have never looked better."
)

MAX_CHARS = 140


def main() -> int:
    line = EXCUSE.strip()
    if not line:
        print("error: excuse is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: excuse must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "error: excuse is %d chars, over the %d limit"
            % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    print(line)
    print("chars: %d (limit %d)" % (len(line), MAX_CHARS))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
