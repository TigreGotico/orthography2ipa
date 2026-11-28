"""The Unicode table the IR compiler reads in place of the host :mod:`unicodedata`.

The table pins one Unicode version, so every Python compiles the same IR bytes.
It holds the general category of every codepoint, and so tells which codepoints
the pinned version assigns; the compiler admits only those.
Regenerate it with scripts/build_unidata.py.
"""
import json
from bisect import bisect_right
from pathlib import Path

__all__ = ["VERSION", "category", "assigned"]

with (Path(__file__).resolve().parent / "unidata.json").open(encoding="utf-8") as _f:
    _table = json.load(_f)

VERSION: str = _table["version"]
_starts = [start for start, _ in _table["category"]]
_categories = [cat for _, cat in _table["category"]]


def category(c: str) -> str:
    """The general category of *c* in the pinned version."""
    return _categories[bisect_right(_starts, ord(c)) - 1]


def assigned(c: str) -> bool:
    """True if the pinned version assigns *c*."""
    return category(c) != "Cn"
