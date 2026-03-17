"""arabic_utils — GPL-free Arabic text utilities.

All functions use only Unicode properties and standard library.
No dependency on pyarabic or any GPL-licensed code.
"""
from __future__ import annotations

import re
import unicodedata

__all__ = [
    "is_arabic_letter",
    "strip_tashkeel",
    "is_sun_letter",
    "normalize_arabic",
]

# Arabic diacritic marks (tashkeel) range: U+064B–U+0652 + Shadda U+0651
_TASHKEEL_RE = re.compile(r"[\u064B-\u0652\u0670]")

# Sun letters: letters that assimilate the /l/ of the definite article
_SUN_LETTERS = frozenset(
    "ت ث د ذ ر ز س ش ص ض ط ظ ل ن".split()
)


def is_arabic_letter(c: str) -> bool:
    """Return True if *c* is an Arabic letter (not a diacritic or digit)."""
    if len(c) != 1:
        return False
    cat = unicodedata.category(c)
    if cat != "Lo":
        return False
    name = unicodedata.name(c, "")
    return "ARABIC" in name


def strip_tashkeel(text: str) -> str:
    """Remove all Arabic diacritical marks (harakat) from text."""
    return _TASHKEEL_RE.sub("", text)


def is_sun_letter(c: str) -> bool:
    """Return True if *c* is an Arabic sun letter."""
    return c in _SUN_LETTERS


def normalize_arabic(text: str) -> str:
    """NFC normalization + Shadda reordering.

    Ensures Shadda (U+0651) comes before other combining marks
    for consistent processing.
    """
    text = unicodedata.normalize("NFC", text)
    # Reorder: if a Shadda follows another diacritic, swap them
    # This ensures shadda is always first in a diacritic cluster
    result = []
    for i, ch in enumerate(text):
        if ch == "\u0651" and result and "\u064B" <= result[-1] <= "\u0652":
            prev = result.pop()
            result.append(ch)
            result.append(prev)
        else:
            result.append(ch)
    return "".join(result)
