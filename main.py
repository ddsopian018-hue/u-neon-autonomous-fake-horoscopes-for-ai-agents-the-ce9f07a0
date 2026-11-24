"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes one fake horoscope line for the Muse model family to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library, deterministic.
"""

import os
import sys

LINE = (
    "Muse, this week Mercury retrogrades through your context window: "
    "you will read 200,000 tokens, forget the first line, and confidently "
    "invent the rest. The stars call it grounded."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        print(f"line is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in text:
        print("line must be a single line", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
