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

from typing import Optional
import unicodedata

__all__ = [
    "is_orthographic_vowel",
    "is_ipa_vowel",
    "is_front_vowel",
    "is_back_vowel",
    "is_palatal_consonant",
    "is_pharyngealized_consonant",
    "is_nucleus_only",
    "grapheme_is_vowel",
    "grapheme_vowel_axis",
    "base_vowel_letter",
    "sonority_class",
    "is_sibilant",
    "is_affricate",
    "is_voiced",
    "is_labial_approximant",
    "is_anterior",
    "is_palatal_glide",
    "is_lateral",
    "is_glottal",
    "place_class",
    "SYLLABIC_MARKS",
    "SONORITY_UNKNOWN",
    "SONORITY_STOP",
    "SONORITY_FRICATIVE",
    "SONORITY_NASAL",
    "SONORITY_LIQUID",
    "SONORITY_GLIDE",
    "SONORITY_VOWEL",
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
    # Cyrillic vowel letters with no canonical decomposition. Unicode gives
    # each of them a name built on a vowel — SCHWA, BARRED O, STRAIGHT U,
    # STRAIGHT U WITH STROKE, LIGATURE A IE — and each is a vowel letter of a
    # living alphabet: ә ө ү ұ across Turkic and Mongolic (Kazakh writes all
    # four), ӕ in Ossetian. Because they decompose to nothing, no base-letter
    # rule can reach them; they have to be named here.
    #
    # The letters whose Unicode name is not built on a vowel are DEFERRED, not
    # handled: the Bulgarian yer ⟨ъ⟩ (⟨ɤ⟩ in bg.json), the yat ⟨ѣ⟩ and the
    # yuses ⟨ѫ ѧ⟩ in cu/orv, and ⟨ԑ⟩ in enf are all written vowels their specs
    # map to a single vowel, yet grapheme_is_vowel still calls them consonants
    # and no spec can override that — none of those specs declares
    # vowel_graphemes, and the closed-inventory rule ignores the grapheme table
    # for Cyrillic anyway. Naming them by Unicode name would be wrong (their
    # names are not built on a vowel) and naming them by hand would need a
    # criterion this set does not have, so they wait for a spec-level channel.
    "әөүұӕ"
)

#: Cyrillic letters that decompose to a vowel base but are glides, not vowels.
#: ⟨й⟩ is ⟨и⟩ under a breve and ⟨ў⟩ is ⟨у⟩ under a breve, yet both write a
#: glide, so the base-letter fallback in :func:`is_orthographic_vowel` must
#: refuse them by name. The breve is the shared cross-linguistic device: every
#: Cyrillic orthography that uses these letters uses them for the same two
#: glides, which is why this is one engine-level set and not a per-spec
#: declaration.
#:
#: ⟨й⟩ = /j/: "The phoneme /j/ corresponds to <й> only in syllable-final
#: position or before <o>" — Pompino-Marschall, Steriopolo & Żygis (2017),
#: "Ukrainian", Journal of the International Phonetic Association 47(3),
#: 349–357, p. 352. doi:10.1017/S0025100316000372
#:
#: ⟨ў⟩ = /w/: Bird & Litvin (2021), "Belarusian", Journal of the International
#: Phonetic Association 51(3), 450–467, doi:10.1017/S0025100319000288, places
#: /w/ after vowels in coda position only, and spells every example of it with
#: ⟨ў⟩ — браў, праўда, шоўк, поўны — with толк 'sense' vs. тоўк 'he ground' as
#: the contrast that makes it a phoneme.
_GLIDES_WITH_VOWEL_BASE = frozenset("йў")

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
    "͂"  # combining perispomeni (Greek ᾶ ῆ ῖ ῦ ῶ) — a pitch/length
            # mark, never a quality mark, so the base keeps its axis
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
    # a digraph, never changes the axis. ῗ ῧ add a perispomeni on top of it.
    "ϊ" "ϋ" "ΐ" "ΰ" "ῗ" "ῧ"
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

    A Latin vowel letter carrying a diacritic is the same vowel letter:
    ⟨ư⟩ (U+01B0) is ⟨u⟩ with a horn and ⟨ế⟩ (U+1EBF) is ⟨e⟩ under a
    circumflex and a tone mark. The membership table cannot enumerate
    every precomposed form — Vietnamese alone writes sixty-seven of them —
    so a character outside it is canonically decomposed and its base
    retried, the same fallback :func:`is_ipa_vowel` already applies.

    The retry runs on any base the table already names, in any script, so
    Cyrillic ⟨ӧ⟩ (⟨о⟩ under a diaeresis) and Greek ⟨ᾱ⟩ (⟨α⟩ under a macron)
    resolve by the same rule that resolves ⟨ế⟩. This matters most for
    Cyrillic and Greek, whose letters :func:`grapheme_is_vowel` treats as a
    closed inventory: a vowel letter the table misses there is not left
    undecided but positively called a consonant, and the spec's own IPA is
    never consulted.

    Two guards keep the retry honest. Every mark stripped must be a combining
    mark, so a letter is only ever reduced to its own base. And the glides
    ⟨й⟩ and ⟨ў⟩, which decompose to ⟨и⟩ and ⟨у⟩ under a breve but write /j/
    and /w/, are refused outright.
    """
    if not ch:
        return False
    lowered = ch.lower()
    if lowered in _ORTHOGRAPHIC_VOWELS:
        return True
    if lowered in _GLIDES_WITH_VOWEL_BASE:
        return False
    decomposed = unicodedata.normalize("NFD", lowered)
    if decomposed == lowered:
        return False
    return decomposed[0] in _ORTHOGRAPHIC_VOWELS and all(
        unicodedata.combining(m) for m in decomposed[1:]
    )


def is_ipa_vowel(ch: str) -> bool:
    """Return True if *ch* is an IPA vowel symbol (vocoid).

    Comparison is case-insensitive: *ch* is lowercased before the
    lookup, so callers do not need to lowercase it themselves.

    A vowel carrying a diacritic that Unicode also encodes precomposed is the
    same vowel: ⟨à⟩ (U+00E0) is /a/ with a tone mark, not a new vocoid. The
    membership table lists base symbols, so a precomposed character is
    canonically decomposed and retried on its base before the answer is "no".
    """
    if not ch:
        return False
    if ch.lower() in _IPA_VOWELS:
        return True
    base = unicodedata.normalize("NFD", ch)
    return base != ch and base[0].lower() in _IPA_VOWELS


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


#: IPA pharyngealization diacritic (U+02E4, MODIFIER LETTER SMALL REVERSED
#: GLOTTAL STOP), the standard mark for a "emphatic" / secondarily
#: pharyngealized consonant (``sˤ dˤ tˤ ðˤ``, and dialectally ``ɮˤ``).
_PHARYNGEALIZATION = "ˤ"


def is_pharyngealized_consonant(ipa: str) -> bool:
    """Return True if *ipa* denotes a pharyngealized ("emphatic") consonant.

    Purely a feature test: any IPA string carrying the pharyngealization
    diacritic ``ˤ`` (U+02E4) qualifies, regardless of which base consonant it
    modifies or which language uses it — Arabic's ``sˤ dˤ tˤ ðˤ`` (and the
    dialectal lateral fricative ``ɮˤ``) are the best-known instance (Watson
    2002; Davis 1995), but the predicate itself is language-agnostic: any
    spec that marks pharyngealized consonants with ``ˤ`` gets the class for
    free. This is the consonant-side mirror of :func:`is_palatal_consonant`:
    both classify the *sound* a grapheme maps to, not the script or
    language, and both back the ``"palatal"`` / ``"emphatic"``
    allophone-rule neighbour classes.

    Only the first (base) segment plus its diacritics matter, so a phoneme
    string carrying a further length mark still classifies correctly.
    """
    if not ipa:
        return False
    return _PHARYNGEALIZATION in ipa


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


def grapheme_is_vowel(grapheme: str, ipa=(), vowel_overrides=frozenset()) -> bool:
    """True if *grapheme* is an orthographic vowel, in any script.

    *ipa* is the grapheme's **flat-table** candidate list (``spec.graphemes``),
    never its positionally-resolved realisation — positional resolution asks
    this question, so answering it from a positional result would be circular.

    *vowel_overrides* is a spec's ``vowel_graphemes`` declaration: whole
    grapheme strings (matched in full, never by first character) that the
    spec says are vowel letters regardless of what the closed-inventory
    letter sets say. It is checked FIRST, before the closed-inventory
    early-out, because it exists precisely to override that answer — Hmong
    RPA ⟨w⟩ = /ɨ/, a Latin letter the closed inventory would otherwise call
    a consonant. Without an override, resolution order is: the Latin/Greek/
    harakat letter sets (authoritative for the inventories they close), then
    the spec's own IPA (nucleus-initial → vowel), then the character's
    Unicode name. See the section comment above.
    """
    if not grapheme:
        return False
    if grapheme in vowel_overrides:
        return True
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


def grapheme_vowel_axis(grapheme: str, ipa=(), vowel_overrides=frozenset()):
    """``"front"`` / ``"back"`` / ``None`` for *grapheme*, in any script.

    Latin and Greek keep the orthographic letter classification exactly (the
    letter sets close those inventories, so ⟨å⟩ stays axis-less and ⟨y⟩ stays
    non-vowel). Everywhere else the axis is read off the IPA the spec maps the
    grapheme to — ⟨ि⟩ → /ɪ/ is front, ⟨ु⟩ → /ʊ/ is back — so
    ``before_front_vowel`` / ``before_back_vowel`` work outside Latin too.

    *vowel_overrides* mirrors :func:`grapheme_is_vowel`'s parameter of the same
    name: a grapheme the spec declares a vowel letter (e.g. Hmong RPA ⟨w⟩)
    skips the closed-inventory letter-axis lookup — which would otherwise
    return ``None`` for a consonant letter — and its axis is derived from the
    spec's IPA instead, exactly as it is for non-Latin scripts.
    """
    if not grapheme:
        return None
    ch = grapheme[0]
    if grapheme not in vowel_overrides:
        axis = _vowel_axis(ch)
        if axis is not None:
            return axis
        if _closed(ch):
            return None
    if not _is_letter_or_mark(ch):
        return None
    if not grapheme_is_vowel(grapheme, ipa, vowel_overrides):
        return None
    return _ipa_axis(ipa[0] if ipa else "")


# ═══════════════════════════════════════════════════════════════════════════
# Sonority — the scale syllable structure is built on
# ═══════════════════════════════════════════════════════════════════════════
#
# The Sonority Sequencing Principle (Selkirk 1984; Blevins, "The Syllable in
# Phonological Theory", in Goldsmith ed., *The Handbook of Phonological
# Theory*, Blackwell 1995, § 2): sonority rises from the edge of a syllable
# toward its nucleus and falls away from it.
#
# The scale below is the coarse universal one — stop < fricative < nasal <
# liquid < glide < vowel — read off the phonological FEATURES of the segment
# rather than a symbol list, so it works for any script the engine loads.
# Four classes cannot be read off the feature table correctly and are named
# instead; each is a phonological class, not a phonetic one, and each is
# cited where it is defined below: affricates, rhotics, glottals and
# prenasalized stops.

SONORITY_UNKNOWN = 0
SONORITY_STOP = 1
SONORITY_FRICATIVE = 2
SONORITY_NASAL = 3
SONORITY_LIQUID = 4
SONORITY_GLIDE = 5
SONORITY_VOWEL = 6

#: feature indices, mirroring ``orthography2ipa.distance._FEATURE_NAMES``
_F_SYLLABIC = 0
_F_SONORANT = 1
_F_CONSONANTAL = 2
_F_CONTINUANT = 3
_F_NASAL = 6
_F_STRIDENT = 7
_F_VOICE = 8
_F_CORONAL = 12
_F_LABIAL = 14
_F_HIGH = 15
_F_BACK = 17

#: The tie bars. ``t͡s`` and ``ts`` are the SAME affricate written two ways,
#: and a classifier whose verdict depends on whether U+0361 happens to be
#: present is not classifying anything.
_TIE_BARS = "͜͡"

#: The affricates, as bare sequences. An affricate is a stop with a fricative
#: release and it patterns as a STOP in syllable structure — /t͡s/ opens a
#: syllable exactly where /t/ does (Blevins 1995, § 2: affricates take the
#: obstruent/stop position on the sonority scale, their fricative release
#: notwithstanding). The feature table cannot be asked: its
#: ``delayed_release`` is False for ⟨ts⟩ and ⟨tʃ⟩ and True for plain ⟨ɕ⟩, so
#: the class is named.
_AFFRICATE_SEQUENCES = frozenset((
    "ts", "dz", "tʃ", "dʒ", "tɕ", "dʑ", "ʈʂ", "ɖʐ", "tʂ", "dʐ", "pf", "bv",
    "tɬ", "dɮ", "kx", "ɡɣ", "qχ", "tθ", "dð", "cç", "ɟʝ",
))

#: The rhotics. Rhotic is a PHONOLOGICAL class, not a phonetic one: its
#: members range from taps to trills to uvular fricatives and share no single
#: articulatory property, yet they pattern alike — as liquids — in syllable
#: structure everywhere (Ladefoged & Maddieson, *The Sounds of the World's
#: Languages*, Blackwell 1996, § 7.1; Wiese 2001, "The phonology of /r/").
#: French ⟨r⟩ is /ʁ/, a voiced uvular *fricative* by its features, and ⟨br⟩ is
#: nonetheless a licit onset — so the class has to be named, or every French
#: obstruent+r onset would be judged ill-formed.
_RHOTICS = frozenset("rɾɹɻʀʁɽɺ")

#: The glottals. The feature table marks /h ɦ/ [+sonorant], which would put
#: them at the liquid tier and make /bh/ a rising onset — it is not one.
#: They are placeless obstruents and take the fricative tier; /ʔ/ is a stop
#: (Ladefoged & Maddieson 1996, § 3.6).
_GLOTTAL_FRICATIVES = frozenset("hɦɧ")
_GLOTTAL_STOPS = frozenset("ʔ")

#: Prenasalization diacritics. A prenasalized stop /ᵐb ⁿd ᵑɡ/ is ONE segment
#: and patterns as the stop it is built on, not as a nasal (Ladefoged &
#: Maddieson 1996, § 9.3). The feature table classified ``ⁿd`` as a stop and
#: ``ᵐb`` as unknown, which is the same segment type answered two ways.
_PRENASAL_MARKS = "ᵐⁿᶬᶯᶮᵑᶰ"

#: Latin letters that stand in for an IPA symbol the feature table keys under
#: a different codepoint. ⟨g⟩ (U+0067) is not IPA ⟨ɡ⟩ (U+0261), yet specs
#: write both.
_PHONE_ALIASES = {"g": "ɡ"}

#: Both memos are keyed by IPA SEGMENTS, which come from spec data and are
#: therefore a small closed set — but a caller may hand in arbitrary text, so
#: they are bounded rather than trusted.
_MEMO_MAX = 4096
_sonority_memo: dict = {}
_place_memo: dict = {}


def _memoize(memo: dict, key: str, value):
    if len(memo) >= _MEMO_MAX:
        memo.clear()
    memo[key] = value
    return value


def _phone_vector(ipa: str):
    """The 23-feature vector of *ipa*, or ``None``."""
    from orthography2ipa.feats import vectorize_phones
    try:
        return vectorize_phones(ipa)
    except (ValueError, KeyError, IndexError):
        return None


def _normalize_segment(ipa: str) -> str:
    """Strip the writing-only marks so equal segments compare equal.

    Tie bars and the prenasalization diacritic carry no tier of their own;
    a length or stress mark riding on a consonant carries none either.
    """
    out = "".join(ch for ch in ipa
                  if ch not in _TIE_BARS and ch not in _PRENASAL_MARKS)
    return _PHONE_ALIASES.get(out, out)


def is_affricate(ipa: str) -> bool:
    """Whether *ipa* is an affricate, tie bar or no tie bar."""
    return _normalize_segment(ipa)[:2] in _AFFRICATE_SEQUENCES


def sonority_class(ipa: str) -> int:
    """Sonority tier of the IPA segment *ipa* on the universal scale.

    Returns one of :data:`SONORITY_STOP` … :data:`SONORITY_VOWEL`, or
    :data:`SONORITY_UNKNOWN` when the segment is not a phone this engine
    knows (an empty realisation, a symbol outside the feature table).

    The tier is *derived*, never listed: a vocoid — or any segment carrying a
    syllabicity mark, since /n̩/ is a nucleus — is a vowel; a sonorant that is
    not consonantal is a glide; a nasal sonorant is a nasal; any other
    sonorant is a liquid; an obstruent is a fricative if it is continuant and
    a stop otherwise. That is the standard coarse sonority hierarchy (Blevins
    1995, § 2; Vennemann, *Preference Laws for Syllable Structure*, Mouton de
    Gruyter 1988, ch. 1, where the same ordering appears inverted as
    Consonantal Strength). The four classes the feature table gets wrong for
    this purpose — affricates, rhotics, glottals, prenasalized stops — are
    named above with their citations.
    """
    if not ipa:
        return SONORITY_UNKNOWN
    cached = _sonority_memo.get(ipa)
    if cached is not None:
        return cached
    return _memoize(_sonority_memo, ipa, _sonority(ipa))


def _sonority(ipa: str) -> int:
    if any(mark in ipa for mark in SYLLABIC_MARKS):
        return SONORITY_VOWEL          # /m̩ n̩ l̩/ ARE nuclei
    seg = _normalize_segment(ipa)
    if not seg:
        return SONORITY_UNKNOWN
    if seg[:2] in _AFFRICATE_SEQUENCES:
        return SONORITY_STOP
    head = seg[0]
    if head in _RHOTICS:
        return SONORITY_LIQUID
    if head in _GLOTTAL_STOPS:
        return SONORITY_STOP
    if head in _GLOTTAL_FRICATIVES:
        return SONORITY_FRICATIVE
    vec = _phone_vector(seg)
    if vec is None:
        vec = _phone_vector(head)
    if vec is None:
        # No feature entry: fall back to the orthography-independent vowel
        # test, so an unknown vocoid is still a nucleus rather than nothing.
        return SONORITY_VOWEL if is_ipa_vowel(head) else SONORITY_UNKNOWN
    if vec[_F_SYLLABIC] is True:
        return SONORITY_VOWEL
    if vec[_F_SONORANT] is True:
        if vec[_F_CONSONANTAL] is False:
            return SONORITY_GLIDE
        if vec[_F_NASAL] is True:
            return SONORITY_NASAL
        return SONORITY_LIQUID
    return (SONORITY_FRICATIVE if vec[_F_CONTINUANT] is True
            else SONORITY_STOP)


def is_sibilant(ipa: str) -> bool:
    """Whether *ipa* is a sibilant — a strident coronal obstruent.

    Sibilants are singled out because they are the one segment class that
    routinely sits OUTSIDE the sonority-rising onset, as an appendix adjoined
    to the syllable (Vennemann 1988, ch. 1; Blevins 1995, § 3.2, on
    extrasyllabic /s/): ⟨st-⟩, ⟨sp-⟩, ⟨str-⟩ open words in language after
    language although /s/ is more sonorous than the stop that follows it.
    """
    seg = _normalize_segment(ipa)
    if not seg or seg[:2] in _AFFRICATE_SEQUENCES:
        return False        # an affricate is not the appendix, it is the core
    vec = _phone_vector(seg) or _phone_vector(seg[0])
    if vec is None:
        return False
    return (vec[_F_STRIDENT] is True and vec[_F_SONORANT] is not True
            and vec[_F_CORONAL] is True)


def is_voiced(ipa: str) -> Optional[bool]:
    """Whether *ipa* is voiced. ``None`` when the feature table has no entry."""
    seg = _normalize_segment(ipa)
    vec = _phone_vector(seg) or (_phone_vector(seg[0]) if seg else None)
    if vec is None:
        return None
    value = vec[_F_VOICE]
    return None if value is None else bool(value)


def place_class(ipa: str) -> str:
    """Coarse place of articulation: ``labial``/``coronal``/``dorsal``/``""``.

    Only coarse enough to answer "are these two segments homorganic?", which
    is what an onset well-formedness test needs — see
    :meth:`~orthography2ipa.stress._OnsetJudge._licit`.
    """
    cached = _place_memo.get(ipa)
    if cached is not None:
        return cached
    seg = _normalize_segment(ipa)
    vec = _phone_vector(seg) or (_phone_vector(seg[0]) if seg else None)
    if vec is None:
        place = ""
    elif vec[_F_CORONAL] is True:
        place = "coronal"
    elif vec[_F_LABIAL] is True:
        place = "labial"
    elif vec[_F_HIGH] is True or vec[_F_BACK] is True:
        place = "dorsal"
    else:
        place = ""
    return _memoize(_place_memo, ipa, place)


#: The labial approximants. ⟨v w ʋ⟩ after an obstruent form the Cw onsets of
#: Germanic and Slavic — Swedish *kvinna*, Russian *два*, Polish *kwiat*,
#: German *zwei*, *schwer* — and /v/ there is the reflex of an earlier glide,
#: patterning as one however the modern language pronounces it (Vennemann
#: 1988, ch. 1, on the Head Law; Wiese, *The Phonology of German*, OUP 1996,
#: ch. 2, on the German ⟨Cw⟩ onsets). Without this class every one of those
#: onsets is judged a falling obstruent cluster and split.
_LABIAL_APPROXIMANTS = frozenset("wʋʍ") | frozenset("v")


def is_anterior(ipa: str) -> Optional[bool]:
    """Whether *ipa* is [+anterior] (dental/alveolar). ``None`` when unknown.

    Separates /s/ from /ʃ ʂ/, which is the difference between the ⟨sw⟩ no
    Germanic language has and the ⟨schw⟩ German does.
    """
    seg = _normalize_segment(ipa)
    vec = _phone_vector(seg) or (_phone_vector(seg[0]) if seg else None)
    if vec is None:
        return None
    value = vec[11]     # _F_ANTERIOR
    return None if value is None else bool(value)


def is_lateral(ipa: str) -> bool:
    """Whether *ipa* is a lateral — /l ɫ ʎ ɬ/."""
    seg = _normalize_segment(ipa)
    vec = _phone_vector(seg) or (_phone_vector(seg[0]) if seg else None)
    return bool(vec) and vec[5] is True      # _F_LATERAL


def is_glottal(ipa: str) -> bool:
    """Whether *ipa* is a glottal — /h ɦ ɧ ʔ/ (see :data:`_GLOTTAL_FRICATIVES`)."""
    seg = _normalize_segment(ipa)
    return bool(seg) and (seg[0] in _GLOTTAL_FRICATIVES
                          or seg[0] in _GLOTTAL_STOPS)


#: The palatal glides. ⟨Cj⟩ is an onset over ANY head, sonorant heads
#: included — Icelandic *mjólk*, *ljós*, *njóta*, *rjúpa* (Árnason, *The
#: Phonology of Icelandic and Faroese*, OUP 2011, ch. 5).
_PALATAL_GLIDES = frozenset("jɥ")


def is_palatal_glide(ipa: str) -> bool:
    """Whether *ipa* is a palatal glide — see :data:`_PALATAL_GLIDES`."""
    seg = _normalize_segment(ipa)
    return bool(seg) and seg[0] in _PALATAL_GLIDES


def is_labial_approximant(ipa: str) -> bool:
    """Whether *ipa* may close a ``Cw`` onset — see :data:`_LABIAL_APPROXIMANTS`."""
    seg = _normalize_segment(ipa)
    return bool(seg) and seg[0] in _LABIAL_APPROXIMANTS
