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

Classification rule (not a hand-list):

The base letters ``e i y`` are **front** and ``a o u`` are **back**. A
character carrying diacritics is NFD-decomposed to its base letter and
classified by that base **only when every combining mark preserves the
front/back axis** — acute, grave, circumflex, caron, macron, breve,
ogonek, dot-above/below and tilde all preserve it, so ``é è ê ě ē ę ĕ``
are front and ``á à â ã ā ą ā`` are back with no per-form listing. This is
why the "``e/i/y`` plus accented forms" claim holds for caron/macron/
ogonek/breve/dotless variants (``ě ī į ŭ ı``), not only acute/grave/
circumflex.

Marks that CHANGE the axis are never stripped and are handled explicitly:

- **Diaeresis / umlaut** (U+0308) fronts a back vowel: ``ä ö ü`` (and the
  already-front ``ë ï ÿ``) are **front**.
- **Dotless ``ı``** does not decompose to a base ⟨i⟩; it is classed
  **front** (patterns with ⟨i⟩ — Italian/French ⟨cy⟩ softens like ⟨ci⟩,
  and dotless i behaves the same).
- **Non-decomposing** ``ø œ æ`` are classed **front** (front / front
  rounded).
- **Ring** ``å`` (U+030A) genuinely straddles the axis — Scandinavian ⟨å⟩
  ≈ /ɔ o/ is back-leaning yet spelled from ⟨a⟩ — so it is left out of
  **both** classes rather than forced into one.

Characters neither rule reaches (e.g. Greek and other non-Latin vowels)
return ``False`` from both predicates; front/back softening is not a rule
those scripts use. The two classes are intentionally disjoint — no
character is both front and back.
"""
from __future__ import annotations

import unicodedata

__all__ = [
    "is_orthographic_vowel",
    "is_ipa_vowel",
    "is_front_vowel",
    "is_back_vowel",
    "is_palatal_consonant",
]

# ═══════════════════════════════════════════════════════════════════════════
# Orthographic vowels: Latin (incl. accented/diacritic forms) + Greek
# ═══════════════════════════════════════════════════════════════════════════

_ORTHOGRAPHIC_VOWELS = frozenset(
    "aeiou"
    # Latin accented forms (formerly g2p._VOWEL_CHARS / stress._VOWELS)
    "áéíóúàèìòùâêîôûãõäëïöüåæø"
    # Precomposed nasal vowels: ã and õ arrived with the accented forms
    # above; ẽ (U+1EBD), ĩ (U+0129) and ũ (U+0169) complete the set so the
    # written nasal vowels are recognised uniformly (Portuguese family and
    # downstream). Their front/back axis is handled by _vowel_axis, where
    # the combining tilde is axis-preserving (ẽ ĩ front; ũ back).
    "ẽĩũ"
    # Extended Latin diacritics (formerly stress._VOWELS only)
    "ąęėįųūīāēőűýěůŏŭıå"
    # Greek vowels: monotonic + accented + dialytika-tonos
    # (formerly stress._VOWELS only)
    "αεηιουωάέήίόύώΐΰ"
    # Arabic short-vowel diacritics (harakat) and their nunation forms,
    # plus the superscript (dagger) alif. These combining marks ARE the
    # written vowels of fully-diacritized Arabic, so grapheme-context
    # reasoning (BEFORE_VOWEL / AFTER_VOWEL positional resolution) must
    # treat a consonant followed by a harakat as standing before a vowel.
    # sukūn (U+0652, vowel *absence*) is deliberately excluded.
    "ًٌٍَُِٰ"
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

# A character not covered by an explicit rule below is NFD-decomposed to its
# base letter and classified by that base — but ONLY when every combining mark
# preserves the front/back axis. Marks that CHANGE the axis (diaeresis/umlaut
# U+0308 fronts a back vowel; ring U+030A) are never stripped; those forms are
# handled explicitly or left unclassified. This is why "e/i/y plus accents"
# holds for caron, macron, ogonek, breve and dotless variants too (ě ī ą ŭ ı)
# without hand-listing each one.

# Base vowel letters once axis-preserving diacritics are removed.
_FRONT_BASE = frozenset("eiy")
_BACK_BASE = frozenset("aou")

# Combining diacritics that keep the base vowel's front/back axis: acute,
# grave, circumflex, caron/háček, macron, breve, ogonek, dot-above, dot-below,
# tilde. (Written as \u escapes; these are zero-width combining codepoints.)
_AXIS_PRESERVING_MARKS = frozenset(
    "́"  # combining acute       (á é í ó ú ý …)
    "̀"  # combining grave       (à è ì ò ù …)
    "̂"  # combining circumflex  (â ê î ô û …)
    "̌"  # combining caron       (ě ǐ ǒ ǔ …)
    "̄"  # combining macron      (ā ē ī ō ū …)
    "̆"  # combining breve       (ă ĕ ĭ ŏ ŭ …)
    "̨"  # combining ogonek      (ą ę į ų …)
    "̇"  # combining dot above   (ė ; İ → i̇ under lowercasing)
    "̣"  # combining dot below
    "̃"  # combining tilde       (ã ẽ ĩ õ ũ)
)

# Characters whose class does NOT come from stripping an axis-preserving mark —
# the mark changes the axis (diaeresis → front rounded) or the letter does not
# decompose. These are the only hand-maintained members.
_FRONT_EXPLICIT = frozenset(
    # diaeresis / umlaut → front (rounded, or already-front base)
    "ä" "ö" "ü" "ë" "ï" "ÿ"
    # dotless i does not decompose to base ⟨i⟩; patterns with ⟨i⟩
    "ı"
    # non-decomposing front / front-rounded letters
    "ø" "œ" "æ"
)

# Ring vowels (å, ẙ) genuinely straddle the axis — Scandinavian ⟨å⟩ ≈ /ɔ o/ is
# back-leaning yet spelled from ⟨a⟩. Left out of BOTH classes rather than
# forced into one.
_AXIS_AMBIGUOUS = frozenset("å" "ẙ")


def _vowel_axis(ch: str):
    """Return ``"front"``, ``"back"`` or ``None`` for a single character.

    Explicit sets win first (axis-changing diacritics and non-decomposing
    letters); otherwise the character is NFD-decomposed and, when every
    combining mark preserves the axis, classified by its base letter.
    Case-insensitive.
    """
    if not ch:
        return None
    c = ch.lower()
    if c in _AXIS_AMBIGUOUS:
        return None
    if c in _FRONT_EXPLICIT:
        return "front"
    decomposed = unicodedata.normalize("NFD", c)
    base = decomposed[0]
    marks = decomposed[1:]
    if marks and not all(m in _AXIS_PRESERVING_MARKS for m in marks):
        # An axis-changing or unrecognised mark is present — do not guess.
        return None
    if base in _FRONT_BASE:
        return "front"
    if base in _BACK_BASE:
        return "back"
    return None


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


# ═══════════════════════════════════════════════════════════════════════════
# Palatal / palato-alveolar consonants (for "before/after a palatal" rules)
# ═══════════════════════════════════════════════════════════════════════════
#
# The mirror of the front/back vowel classes on the *consonant* side: a class
# predicate that answers "does this IPA symbol denote a palatal or
# palato-alveolar consonant?" so a spec can condition a grapheme's realisation
# (or an allophone rule) on being adjacent to one — e.g. European Portuguese
# stressed /e/ → [ɐ] before ⟨lh⟩ (/ʎ/), or nasalisation before a palatal.
#
# Unlike the vowel classes (which read the written *letter*), the palatal test
# reads the *IPA* a grapheme maps to — palatality is a property of the sound,
# and the same letter maps to a palatal in one language and not another. The
# single-symbol members are the palatal and palato-alveolar / alveolo-palatal
# obstruents, nasal, lateral and glide; the two-symbol members are the
# palato-alveolar and alveolo-palatal affricates, whose leading segment (⟨t⟩ /
# ⟨d⟩) is *not* itself palatal, so they must be matched as a prefix. A tie-bar
# (U+0361, ``t͡ʃ``) is stripped before matching so both ``tʃ`` and ``t͡ʃ`` count.

# Single palatal / palato-alveolar / alveolo-palatal IPA symbols.
_PALATAL_SINGLE = frozenset(
    "ʎ"   # palatal lateral approximant   (pt/gl ⟨lh⟩)
    "ɲ"   # palatal nasal                 (pt/gl ⟨nh⟩, es ⟨ñ⟩)
    "ʃ"   # voiceless palato-alveolar fric (⟨ch⟩/⟨x⟩)
    "ʒ"   # voiced palato-alveolar fric    (⟨j⟩/⟨g⟩)
    "j"   # palatal approximant           (⟨y⟩/⟨i⟩ glide)
    "c"   # voiceless palatal stop
    "ɟ"   # voiced palatal stop
    "ç"   # voiceless palatal fricative
    "ʝ"   # voiced palatal fricative
    "ɕ"   # voiceless alveolo-palatal fric
    "ʑ"   # voiced alveolo-palatal fric
    "ɥ"   # labial-palatal approximant
)

# Affricates whose *first* segment is a coronal stop, not a palatal — matched
# as a prefix of the (tie-bar-stripped) IPA string.
_PALATAL_AFFRICATES = ("tʃ", "dʒ", "tɕ", "dʑ")

# Combining tie bar (U+0361) joining an affricate's two symbols.
_TIE_BAR = "͡"


def is_palatal_consonant(ipa: str) -> bool:
    """Return True if *ipa* denotes a palatal / palato-alveolar consonant.

    The consonant-side mirror of :func:`is_front_vowel` / :func:`is_back_vowel`:
    it classifies an *IPA* string (a grapheme's realisation), not a written
    letter. ``True`` for the palatal and palato-alveolar / alveolo-palatal
    obstruents, nasal, lateral and glide — ``ʎ ɲ ʃ ʒ j c ɟ ç ʝ ɕ ʑ ɥ`` — and
    the affricates ``tʃ dʒ tɕ dʑ`` (with or without a tie bar, ``t͡ʃ``).
    ``False`` for every non-palatal segment (``s t k`` …) and for vowels.

    Only the leading segment is inspected, so a phoneme string carrying a
    following length mark or diacritic (``ʃː``, ``ɲʲ``) still classifies by its
    palatal head. The argument is the IPA a grapheme maps to; membership
    delegates here so ``BEFORE_PALATAL`` / ``AFTER_PALATAL`` positions and the
    ``"palatal"`` allophone-rule class share one definition.
    """
    if not ipa:
        return False
    s = ipa.replace(_TIE_BAR, "")
    for aff in _PALATAL_AFFRICATES:
        if s.startswith(aff):
            return True
    return s[0] in _PALATAL_SINGLE


def is_front_vowel(ch: str) -> bool:
    """Return True if *ch* is a **front** orthographic vowel letter.

    Front vowels are ``e i y`` and any letter that decomposes to them under
    an axis-preserving diacritic (``é ě ī į ý …``), plus the front rounded /
    diaeresis letters ``ä ë ï ö ü ÿ ø œ æ`` and dotless ``ı``. They trigger
    "soft" realisations in Romance c/g softening and comparable rules. See
    the module docstring for the borderline classifications.

    Comparison is case-insensitive: *ch* is lowercased before the lookup.
    """
    return _vowel_axis(ch) == "front"


def is_back_vowel(ch: str) -> bool:
    """Return True if *ch* is a **back** orthographic vowel letter.

    Back vowels are ``a o u`` and any letter that decomposes to them under an
    axis-preserving diacritic (``á â ã ā ą ō ú …``). They keep the "hard"
    realisation in Romance c/g softening. Ring ``å`` is deliberately excluded
    (see the module docstring). Comparison is case-insensitive.
    """
    return _vowel_axis(ch) == "back"
