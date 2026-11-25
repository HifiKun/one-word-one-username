#!/usr/bin/env python3
"""One Word, One Username, One Reward — entry program.

The competition asks for one word and nothing else: the entrant's own
make.fun username. This program writes that single username to
/output/entry.txt, exactly as the gate requires: UTF-8 text, 1 to 30
characters, not only white space, no explanation, no links, no pitch.
"""

import os
import sys

# The entrant's own make.fun handle, sent as one word.
USERNAME = "hifikun"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    text = USERNAME.strip()
    if not text or len(text) > 30 or any(ch.isspace() for ch in text):
        print("error: username must be one word of 1-30 characters", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {OUTPUT_PATH}: {text!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
