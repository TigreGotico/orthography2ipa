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
    "is_nucleus_only",
    "grapheme_is_vowel",
    "grapheme_vowel_axis",
    "base_vowel_letter",
    "SYLLABIC_MARKS",
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
    # Cyrillic vowel letters: East/South Slavic core (а е ё и о у ы э ю я),
    # Ukrainian і ї є, plus the grave-accented forms ѐ ѝ used to mark
    # stress in Bulgarian/Macedonian text. The glides ў (Belarusian /w/)
    # and й (/j/) are deliberately excluded, as are the vowel-less signs
    # ь and ъ.
    "аеёиоуыэюяіїєѐѝ"
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
#: Base letters classified on the front/back axis. Greek is included —
#: Modern Greek ⟨ε η ι υ⟩ are all front (υ merged into /i/ by iotacism;
#: Holton, Mackridge & Philippaki-Warburton ch. 1.1) and ⟨α ο ω⟩ back —
#: because the class positions (BEFORE_FRONT_VOWEL …) must work for
#: Greek text: the velar palatalization κ→[c]/γ→[ʝ]/χ→[ç] is conditioned
#: on exactly this axis. Accented forms (ά έ ή ί ό ύ ώ) classify through
#: the axis-preserving acute below; dialytika (ϊ ϋ ΐ ΰ) is
#: axis-preserving for the already-front ι/υ, listed explicitly since
#: the Latin diaeresis rule (back → front) does not apply.
_FRONT_BASE = frozenset("eiy" "εηιυ")
_BACK_BASE = frozenset("aou" "αοω")

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
    # Greek dialytika forms: ι/υ are already front, the mark only breaks
    # a digraph, never changes the axis
    "ϊ" "ϋ" "ΐ" "ΰ"
)

# Ring vowels (å, ẙ) genuinely straddle the axis — Scandinavian ⟨å⟩ ≈ /ɔ o/ is
# back-leaning yet spelled from ⟨a⟩. Left out of BOTH classes rather than
# forced into one.
_AXIS_AMBIGUOUS = frozenset("å" "ẙ")


def base_vowel_letter(ch: str) -> str:
    """The bare base vowel letter for *ch* once axis-preserving diacritics are
    stripped, else *ch* lowercased unchanged.

    ``é ê`` → ``e``; ``í`` → ``i``; ``ó ô`` → ``o``; ``á â ã`` → ``a``. Marks
    that change the front/back axis (diaeresis ``ü``, ring ``å``) and
    non-decomposing letters (``ø œ æ``) are preserved, so callers that key on
    the plain letter (e.g. the ``before_e``/``before_i`` softening positions)
    treat an accented front vowel like its base without misclassifying a form
    whose diacritic shifted the axis. Purely orthographic and script-neutral —
    the same rule that lets ``é è ê`` share ⟨e⟩'s front/back axis above.
    """
    if not ch:
        return ch
    c = ch.lower()
    decomposed = unicodedata.normalize("NFD", c)
    base = decomposed[0]
    marks = decomposed[1:]
    if marks and all(m in _AXIS_PRESERVING_MARKS for m in marks):
        return base
    return c


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


# ═══════════════════════════════════════════════════════════════════════════
# Script-agnostic vowel-hood: spec data first, Unicode second
# ═══════════════════════════════════════════════════════════════════════════
#
# The letter sets above enumerate written vowels for the scripts they cover.
# They cannot be extended per script — a list of "which letters are vowels" is
# language/script knowledge, and that belongs in DATA, not in the engine.
# Devanagari, Cyrillic, Arabic letters, Tamil, Hebrew, Thai and every script the
# library has never seen must still be able to answer "is this grapheme an
# orthographic vowel?", because that answer is what makes INTERVOCALIC /
# BEFORE_VOWEL / AFTER_FRONT_VOWEL and the vowel-conditioned allophone classes
# fire at all. When it silently answers "no" for a whole script, every such rule
# in that script's spec is inert.
#
# :func:`grapheme_is_vowel` answers it from three sources, in order:
#
# 1. The letter sets above — unchanged, and *authoritative* (see below).
# 2. **The spec's own data**: a grapheme whose flat-table IPA is a syllable
#    nucleus and nothing else (a vowel, or a syllabic consonant like /r̩/) IS an
#    orthographic vowel. This needs zero new tables and
#    generalises to any script: the spec already says what each grapheme sounds
#    like, and vowel-hood is derivable from that.
# 3. **Unicode**, where the spec is silent: a character whose Unicode NAME
#    marks it a vowel (``DEVANAGARI VOWEL SIGN AA``, ``TAMIL VOWEL SIGN I``,
#    ``… LETTER VOCALIC R``) is a vowel. This is a Unicode property, not a
#    per-script list.
#
# **Where the letter sets are authoritative (why Latin/Greek cannot change).**
# Sources 2 and 3 are only consulted for characters the letter sets have no
# jurisdiction over. Jurisdiction is derived from the sets themselves, not
# hardcoded: for each member we take its script (from its Unicode name) and
# whether it is a combining mark, and the resulting (script, is-mark) pairs are
# the closed inventories. The Latin and Greek members are *letters*, so the sets
# enumerate those scripts' vowel LETTERS exhaustively — a Latin letter absent
# from them (⟨y⟩, ⟨w⟩, ⟨r⟩) is a consonant letter by that closed inventory, and
# stays one no matter what IPA a spec gives it. The Arabic members are the
# harakat — *marks* — so the sets close Arabic COMBINING MARKS only; Arabic
# letters (⟨ا⟩ → /aː/, ⟨و⟩, ⟨ي⟩) fall through to the spec, as they must.
# Consequence: for Latin and Greek, :func:`grapheme_is_vowel` returns exactly
# what :func:`is_orthographic_vowel` returned before, by construction.

#: Combining marks that make the segment they attach to SYLLABIC — the IPA
#: syllabicity marks (U+0329 below, U+030D above). They are what makes /r̩/ a
#: nucleus rather than an onset. Shared with :mod:`orthography2ipa.phonetok`.
SYLLABIC_MARKS = "̩̍"


def is_nucleus_only(ipa: str) -> bool:
    """True if *ipa* is **nothing but** syllable nucleus.

    A nucleus is a vowel or a syllabic consonant (/r̩/, /l̩/). Every segment must
    be one — a grapheme is a written vowel only when its realisation carries no
    consonant. Length, nasality, tone and other diacritics ride along with their
    base (``aː``, ``ẽ``) and do not disqualify it.

    Both halves of "every" matter, in both directions:

    - an abugida consonant carrying a vowel (⟨क⟩ → /kə/) is NOT a vowel — were
      the leading segment alone inspected it would pass on its vowel tail and
      every consonant in the script would become a vowel;
    - a multigraph realised as a whole syllable (Arabic ⟨ال⟩ → /al/) is NOT a
      vowel either — it ends in a consonant, and treating it as one makes the
      grapheme after it wrongly ``AFTER_VOWEL``.

    The single exception is a **leading on-glide**: the iotated Cyrillic vowel
    letters ⟨я е ё ю⟩ realise as /ja je jo ju/ and are vowel letters all the
    same. A bare glide (⟨й⟩ → /j/, ⟨य⟩ → /j/) is not.
    """
    if not ipa:
        return False
    found = False
    i = 0
    n = len(ipa)
    if n > 1 and ipa[0] in _ONGLIDES:
        # A leading glide does not make the grapheme a consonant: the iotated
        # Cyrillic vowel letters ⟨я е ё ю⟩ → /ja je jo ju/ are vowel letters
        # whose realisation carries an on-glide. Only a LEADING one is allowed,
        # and only with a nucleus behind it, so /j/ alone (⟨й⟩, ⟨य⟩) stays a
        # consonant.
        i = 1
    while i < n:
        ch = ipa[i]
        nxt = ipa[i + 1] if i + 1 < n else ""
        if nxt and nxt in SYLLABIC_MARKS:
            # A syllabic consonant (/r̩/): base + syllabicity mark = a nucleus.
            found = True
            i += 2
            continue
        if unicodedata.combining(ch) or unicodedata.category(ch) in ("Lm", "Sk"):
            # Length mark, tone letter, nasalisation, stress mark …: a modifier
            # on the preceding segment, never a segment of its own — and never a
            # nucleus by itself. A grapheme realised as a bare mark (the
            # Devanagari anusvāra ⟨ं⟩ → nasalisation) is NOT a vowel: counting
            # it as one makes a following consonant wrongly INTERVOCALIC
            # (⟨अंडा⟩ would flap its ⟨ड⟩).
            i += 1
            continue
        if is_ipa_vowel(ch):
            found = True
            i += 1
            continue
        return False  # a consonant: this grapheme is not a written vowel
    return found


# Tokens in a Unicode character NAME that mark the character a written vowel.
# "VOWEL" covers the Brahmic/Thai/Khmer vowel signs and letters ("DEVANAGARI
# VOWEL SIGN AA", "TAMIL VOWEL SIGN I"); "VOCALIC" covers the syllabic-liquid
# vowel letters ("DEVANAGARI LETTER VOCALIC R"), whose IPA is a consonant plus
# a vowel and so is not nucleus-initial.
_UNICODE_VOWEL_NAME_TOKENS = ("VOWEL", "VOCALIC")


def _script_key(ch: str):
    """A (script, is-combining-mark) key for *ch*, derived from Unicode.

    The script is the first word of the character's Unicode name (``LATIN``,
    ``GREEK``, ``ARABIC``, ``DEVANAGARI`` …) — the stdlib exposes no script
    property, and the name prefix IS the script for letters and marks. Returns
    ``None`` for unnamed characters.
    """
    try:
        name = unicodedata.name(ch)
    except ValueError:
        return None
    return name.split()[0], unicodedata.combining(ch) != 0


#: The (script, is-mark) inventories the letter sets above enumerate
#: exhaustively — derived from their own members, never hardcoded. For these,
#: absence from the sets means "not a vowel" and no other source is consulted.
_CLOSED_INVENTORIES = frozenset(
    key for key in (_script_key(c) for c in _ORTHOGRAPHIC_VOWELS)
    if key is not None
)


def _is_letter_or_mark(ch: str) -> bool:
    """True if *ch* is a Unicode letter or combining mark — the only two
    categories a written vowel can belong to."""
    return unicodedata.category(ch)[0] in ("L", "M")


def _closed(ch: str) -> bool:
    """True if *ch* falls inside an inventory the letter sets close."""
    key = _script_key(ch)
    return key is not None and key in _CLOSED_INVENTORIES


def _unicode_says_vowel(ch: str) -> bool:
    try:
        name = unicodedata.name(ch)
    except ValueError:
        return False
    return any(tok in name for tok in _UNICODE_VOWEL_NAME_TOKENS)


def grapheme_is_vowel(grapheme: str, ipa=()) -> bool:
    """True if *grapheme* is an orthographic vowel, in any script.

    *ipa* is the grapheme's **flat-table** candidate list (``spec.graphemes``),
    never its positionally-resolved realisation — positional resolution asks
    this question, so answering it from a positional result would be circular.

    Resolution order: the Latin/Greek/harakat letter sets (authoritative for
    the inventories they close), then the spec's own IPA (nucleus-initial →
    vowel), then the character's Unicode name. See the section comment above.
    """
    if not grapheme:
        return False
    ch = grapheme[0]
    if is_orthographic_vowel(ch):
        return True
    if not _is_letter_or_mark(ch):
        # A written vowel is a letter or a mark. Symbols, digits and
        # punctuation never are — including the ASCII symbols a
        # transliteration scheme presses into service (Buckwalter ⟨>⟩, ⟨&⟩).
        return False
    if _closed(ch):
        return False
    primary = ipa[0] if ipa else ""
    if is_nucleus_only(primary):
        return True
    return _unicode_says_vowel(ch)


#: IPA vowel symbols by front/back axis, read off the IPA vowel chart (this is
#: IPA knowledge, not language knowledge). Central vowels (ɨ ʉ ə ɘ ɜ ɞ ɐ) belong
#: to neither axis and are deliberately omitted, exactly as ⟨å⟩ is omitted from
#: the orthographic classes.
#: IPA on-glides. A grapheme realised as glide + nucleus is still a vowel letter
#: (Cyrillic ⟨я⟩ → /ja/); a grapheme realised as a bare glide is not (⟨й⟩ → /j/).
_ONGLIDES = frozenset("jwɥ")

_IPA_FRONT = frozenset("iyɪʏeøɛœæaɶ")
_IPA_BACK = frozenset("uʊɯoɤɔɑɒʌ")


def _ipa_axis(ipa: str):
    if not ipa:
        return None
    for c in ipa:
        if c in _IPA_FRONT:
            return "front"
        if c in _IPA_BACK:
            return "back"
        if is_ipa_vowel(c):
            return None  # a central vowel: on neither axis
    return None


def grapheme_vowel_axis(grapheme: str, ipa=()):
    """``"front"`` / ``"back"`` / ``None`` for *grapheme*, in any script.

    Latin and Greek keep the orthographic letter classification exactly (the
    letter sets close those inventories, so ⟨å⟩ stays axis-less and ⟨y⟩ stays
    non-vowel). Everywhere else the axis is read off the IPA the spec maps the
    grapheme to — ⟨ि⟩ → /ɪ/ is front, ⟨ु⟩ → /ʊ/ is back — so
    ``before_front_vowel`` / ``before_back_vowel`` work outside Latin too.
    """
    if not grapheme:
        return None
    ch = grapheme[0]
    axis = _vowel_axis(ch)
    if axis is not None:
        return axis
    if _closed(ch) or not _is_letter_or_mark(ch):
        return None
    if not grapheme_is_vowel(grapheme, ipa):
        return None
    return _ipa_axis(ipa[0] if ipa else "")
