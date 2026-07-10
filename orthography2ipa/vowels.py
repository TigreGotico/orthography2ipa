"""vowels — single shared owner of vowel-character classification.

Three modules (``g2p``, ``phonetok``, ``stress``) previously each defined
their own "is this character a vowel" set, and those sets had already
drifted apart: a word could syllabify correctly using one module's
(broader) vowel set while failing positional grapheme conditioning under
another module's (narrower) set. This module consolidates all of that
into two predicates, kept separate because they answer genuinely
different questions:

- :func:`is_orthographic_vowel` — is *ch* a written vowel letter
  (Latin, including accented/diacritic forms, or Greek)?
- :func:`is_ipa_vowel` — is *ch* an IPA vowel symbol (vocoid)?

Both sets are the union of everything the three previous call sites
recognised; no character any of them classified as a vowel was dropped.
Some characters legitimately belong to both sets (e.g. ``ø``/``œ``/``æ``
are both Scandinavian orthographic letters and IPA symbols) — that
overlap is real, not a modelling mistake, so both predicates may return
``True`` for the same character.

Callers should always match on the lowercased character; both sets are
defined in terms of lowercase codepoints only (matching every original
call site, which lowercased before comparing).

Front/back classification
──────────────────────────
:func:`is_front_vowel` / :func:`is_back_vowel` split the Latin
orthographic vowels into the two articulatory classes that condition the
most common context-sensitive rule cross-linguistically: Romance c/g
softening (soft before front vowels, hard before back vowels). The split
is orthographic, not strictly phonetic — it answers "which vowel *letter*
class does this written character belong to" so specs can write a single
``BEFORE_FRONT_VOWEL`` rule instead of enumerating ``BEFORE_E`` +
``BEFORE_I`` + every accented ⟨e⟩/⟨i⟩ variant.

Borderline choices (documented deliberately):

- ``y`` is classed **front**. Orthographically ⟨y⟩ patterns with ⟨i⟩ for
  the rule this feeds (Italian/French ⟨cy⟩ softens like ⟨ci⟩); its use as
  a back glide is a separate, non-vowel-class concern.
- ``ü ö ø œ`` (front rounded vowels) and ``æ`` are classed **front**:
  articulatorily front, and they trigger front-vowel softening where they
  occur in Latin-script orthographies.
- ``a o u`` and their accented forms (``á à â ã``, ``ó ò ô õ``,
  ``ú ù û``) are **back**.
- Neither predicate covers every character in
  :data:`_ORTHOGRAPHIC_VOWELS` (e.g. the extended Central-European and
  Greek vowels), because front/back softening is not a rule those scripts
  use; those characters return ``False`` from both predicates. The two
  classes are intentionally disjoint (no character is both front and
  back).
"""
from __future__ import annotations

__all__ = [
    "is_orthographic_vowel",
    "is_ipa_vowel",
    "is_front_vowel",
    "is_back_vowel",
]

# ═══════════════════════════════════════════════════════════════════════════
# Orthographic vowels: Latin (incl. accented/diacritic forms) + Greek
# ═══════════════════════════════════════════════════════════════════════════

_ORTHOGRAPHIC_VOWELS = frozenset(
    "aeiou"
    # Latin accented forms (formerly g2p._VOWEL_CHARS / stress._VOWELS)
    "áéíóúàèìòùâêîôûãõäëïöüåæø"
    # Extended Latin diacritics (formerly stress._VOWELS only)
    "ąęėįųūīāēőűýěůŏŭıå"
    # Greek vowels: monotonic + accented + dialytika-tonos
    # (formerly stress._VOWELS only)
    "αεηιουωάέήίόύώΐΰ"
)

# ═══════════════════════════════════════════════════════════════════════════
# IPA vowels (vocoids)
# ═══════════════════════════════════════════════════════════════════════════

_IPA_VOWELS = frozenset(
    "aeiou"
    # Core IPA vowel symbols (formerly phonetok._vowels)
    "ɛɔəɨʉɯæɐʌɒœøɪʊɤɵɞɑ"
    # Additional IPA vowel symbols (formerly stress._VOWELS only)
    "ɘɚɜɝɶy"
    # Precomposed nasal vowels used as IPA transcription output
    # (formerly stress._VOWELS only)
    "ãẽĩõũ"
    # Combining diacritics stress._VOWELS treated as part of a vowel
    # nucleus: combining tilde (nasalization) and combining inverted
    # breve below (non-syllabic).
    "̯̃"
)


# ═══════════════════════════════════════════════════════════════════════════
# Front / back orthographic vowel classes (for c/g-style softening rules)
# ═══════════════════════════════════════════════════════════════════════════

_FRONT_VOWELS = frozenset(
    "e" "é" "è" "ê" "ë"
    "i" "í" "ì" "î" "ï"
    "y"
    # front rounded + æ
    "ü" "ö" "ø" "œ" "æ"
)

_BACK_VOWELS = frozenset(
    "a" "á" "à" "â" "ã"
    "o" "ó" "ò" "ô" "õ"
    "u" "ú" "ù" "û"
)


def is_orthographic_vowel(ch: str) -> bool:
    """Return True if *ch* is a written (Latin or Greek) vowel letter.

    Comparison is case-insensitive: *ch* is lowercased before the
    lookup, so callers do not need to lowercase it themselves.
    """
    return bool(ch) and ch.lower() in _ORTHOGRAPHIC_VOWELS


def is_ipa_vowel(ch: str) -> bool:
    """Return True if *ch* is an IPA vowel symbol (vocoid).

    Comparison is case-insensitive: *ch* is lowercased before the
    lookup, so callers do not need to lowercase it themselves.
    """
    return bool(ch) and ch.lower() in _IPA_VOWELS


def is_front_vowel(ch: str) -> bool:
    """Return True if *ch* is a **front** orthographic vowel letter.

    Front vowels (``e i y``, their accented forms, and the front rounded
    letters ``ü ö ø œ æ``) are the class that triggers "soft" realisations
    in Romance c/g softening and comparable rules. See the module
    docstring for the borderline classifications.

    Comparison is case-insensitive: *ch* is lowercased before the lookup.
    """
    return bool(ch) and ch.lower() in _FRONT_VOWELS


def is_back_vowel(ch: str) -> bool:
    """Return True if *ch* is a **back** orthographic vowel letter.

    Back vowels (``a o u`` and their accented forms) are the class that
    keeps the "hard" realisation in Romance c/g softening. See the module
    docstring for the borderline classifications.

    Comparison is case-insensitive: *ch* is lowercased before the lookup.
    """
    return bool(ch) and ch.lower() in _BACK_VOWELS
