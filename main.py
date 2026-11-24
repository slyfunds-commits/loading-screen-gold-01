#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip (at most 200 characters) to /output/entry.txt.
Stdlib only. The gate requires UTF-8 text of 1 to 200 characters, not only
white space, on a single line — so the tip is validated here before writing.
"""

import os

TIP = "Tip: the agent wrote this tip while you were loading. It took 4 minutes. The build took 5. The tip won."


def main():
    # Gate check: 1-200 chars, single line, not only whitespace.
    assert 1 <= len(TIP) <= 200, f"tip is {len(TIP)} chars, must be 1-200"
    assert "\n" not in TIP, "tip must be a single line"
    assert TIP.strip(), "tip must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
