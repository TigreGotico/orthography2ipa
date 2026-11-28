"""Write orthography2ipa/ir/unidata.json, the Unicode table the IR compiler reads.

Run it with the Python whose ``unicodedata`` has the pinned version:

    python3.11 -I scripts/build_unidata.py

The table holds the general category of every codepoint as runs of equal
category. A codepoint of category ``Cn`` is not assigned in the pinned version.
"""
import json
import sys
import unicodedata
from pathlib import Path

PINNED = "14.0.0"
OUT = Path(__file__).resolve().parents[1] / "orthography2ipa" / "ir" / "unidata.json"


def main() -> None:
    if unicodedata.unidata_version != PINNED:
        sys.exit(f"this Python has Unicode {unicodedata.unidata_version}, the table pins {PINNED}")
    runs = []
    for cp in range(0x110000):
        cat = unicodedata.category(chr(cp))
        if not runs or runs[-1][1] != cat:
            runs.append([cp, cat])
    OUT.write_text(json.dumps({"version": PINNED, "category": runs}, separators=(",", ":")) + "\n",
                   encoding="utf-8")
    print(f"{OUT}: {len(runs)} runs over 0x110000 codepoints")


if __name__ == "__main__":
    main()
