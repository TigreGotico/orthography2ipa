"""One-time rename of the top-level ``parent`` key to ``inherits`` in every spec file.

The rewrite is textual, so each file keeps its formatting, and each result is
checked against the parsed original with the key renamed. Run it once from the
repository root, with ``--check`` to count without writing.
"""
import json
import re
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "orthography2ipa" / "data"
KEY = re.compile(r'"parent"(?=\s*:)')


def main() -> None:
    write = "--check" not in sys.argv[1:]
    files = sorted(DATA.glob("*.json"))
    changed = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        spec = json.loads(text)
        if "parent" not in spec:
            continue
        if "inherits" in spec or len(KEY.findall(text)) != 1:
            sys.exit(f"{path.name}: cannot rename safely")
        new = KEY.sub('"inherits"', text)
        expected = {("inherits" if k == "parent" else k): v for k, v in spec.items()}
        if json.loads(new) != expected or list(json.loads(new)) != list(expected):
            sys.exit(f"{path.name}: rename changed more than the key")
        if write:
            path.write_text(new, encoding="utf-8")
        changed += 1
    print(f"{len(files)} files in, {changed} changed, {len(files) - changed} unchanged")


if __name__ == "__main__":
    main()
