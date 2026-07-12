"""phonetok — Language-agnostic grapheme tokenizer with IPA beam expansion.

Tokenises raw text into grapheme tokens using a language's grapheme table
(maximal-munch / longest-match), then expands those tokens into all
possible IPA transcription paths via beam search.

Design principles
─────────────────
1. **Language-agnostic algorithm**: the tokenizer knows nothing about any
   specific language.  All linguistic knowledge comes from LanguageSpec.
2. **Maximal munch**: at each position the longest matching grapheme wins.
   Ties are impossible because grapheme keys are unique strings.
3. **Special tokens**: whitespace, punctuation, digits, and unknown
   characters each get their own token type so downstream consumers
   can handle them uniformly.
4. **Beam search IPA expansion**: because a single grapheme can map to
   multiple IPA values (e.g. English ⟨c⟩ → /k/ or /s/), the full
   transcription of a word is a combinatorial product.  We provide
   beam-width-bounded enumeration of all paths, optionally with
   allophone expansion.

Usage
─────
    >>> from orthography2ipa import get
    >>> from orthography2ipa.phonetok import PhonetokTokenizer
    >>> tok = PhonetokTokenizer(get("pt-BR"))
    >>> tokens = tok.tokenize("chuva")
    >>> [t.grapheme for t in tokens]
    ['ch', 'u', 'v', 'a']
    >>> paths = tok.ipa_beam("chuva", beam_width=4)
    >>> paths[0]
    ['ʃ', 'u', 'v', 'a']

    >>> tok_en = PhonetokTokenizer(get("en-GB"))
    >>> tokens = tok_en.tokenize("the cat")
    >>> [(t.kind.name, t.grapheme) for t in tokens]
    [('GRAPHEME', 'th'), ('GRAPHEME', 'e'), ('WHITESPACE', ' '),
     ('GRAPHEME', 'c'), ('GRAPHEME', 'a'), ('GRAPHEME', 't')]
"""
from __future__ import annotations

import math
import re
import unicodedata
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional, Sequence, Tuple

from orthography2ipa.types import GraphemePosition, LanguageSpec
from orthography2ipa.vowels import (
    is_back_vowel,
    is_front_vowel,
    is_ipa_vowel,
    is_orthographic_vowel,
    is_palatal_consonant,
)
from orthography2ipa.positional import build_branches, resolve_branches

# ── Positional-nasalisation guard (see PhonetokTokenizer._expand_beam) ──
# The combining tilde a coda ⟨m/n⟩ slot emits to nasalise the preceding
# vowel. It is a valid segment only when it lands on an ORAL vowel or a
# glide; landing on a consonant or an already-nasalised nucleus yields
# invalid IPA, so the guard drops such a branch.
_NASAL_TILDE = "̃"
_NASAL_CARRIERS = frozenset(
    # oral IPA vowels (deliberately excludes the precomposed nasal vowels
    # ã ẽ ĩ õ ũ and every combining mark, so a second tilde never stacks)
    "aeiou"
    "ɛɔəɨʉɯæɐʌɒœøɪʊɤɵɞɑɘɚɜɝɶy"
    # glides that legitimately carry a nasal offglide (nasal diphthongs
    # ɐ̃w̃ / ɐ̃j̃ from ⟨ão ãe õe⟩)
    "wjɥɰ"
)
from orthography2ipa.rescorer import (
    LatticeRescorer, RescorerArg, apply_rescorers, normalize_rescorers,
)

from typing import TYPE_CHECKING

__all__ = [
    "TokenKind",
    "Token",
    "IPAPath",
    "Candidate",
    "SegmentSlot",
    "GraphemeContext",
    "TokenSequence",
    "flat_contexts",
    "slot_confidence",
    "lattice_confidence",
    "PhonetokTokenizer",
    "lower_str",
]


# ═══════════════════════════════════════════════════════════════════════════
# Arabic-script pre-tokenization normalization
# ═══════════════════════════════════════════════════════════════════════════
#
# Two script-scoped normalizations run *before* grapheme tokenization for
# Arabic-script specs. Both are opt-in by script/spec so no other script is
# ever touched (Latin, Devanagari, … are byte-identical).
#
# 1. Presentation-form / ligature decomposition. The Arabic Presentation
#    Forms-A (U+FB50–U+FDFF) and Forms-B (U+FE70–U+FEFF) blocks hold
#    contextual glyph variants and ligatures — most importantly the four
#    lam-alif ligatures ﻻ/ﻷ/ﻵ/ﻹ (U+FEFB/FEF7/FEF5/FEF9), which decompose to
#    ل + ا/أ/آ/إ. These are *glyphs*, not letters: the base grapheme table
#    keys them on the canonical letters, so a bare ﻻ would otherwise
#    tokenize to nothing and yield an empty transcription. We NFKC-decompose
#    only codepoints inside those two blocks (leaving every other codepoint,
#    and every other script, untouched — a plain global NFKC would also fold
#    Latin ligatures, full-width forms, etc.).
# 2. Gemination (shadda, ّ U+0651). A consonant carrying shadda is a
#    geminate — it surfaces as a doubled/long consonant, and this holds for
#    the glides ي/و, which geminate as the consonants they are (Ryding 2005,
#    *A Reference Grammar of Modern Standard Arabic*, "Phonology and script",
#    doubling of consonants and the approximants/semivowels waaw & yaa,
#    pp. 15–16; Watson 2002, *The Phonology and Morphology of Arabic*, on MSA
#    gemination via shadda). We model it as a text-level transform: double
#    the base consonant and drop the shadda,
#    so downstream per-slot resolution sees two ordinary consonant slots
#    (surface e.g. عَمَّ → [ʕamma], not a length mark stranded on the vowel).
#    Both Unicode orderings of the mark cluster are handled: the canonical
#    consonant+shadda+harakat and the equally-valid consonant+harakat+shadda
#    (they render identically and NFC does not reorder them, since shadda
#    ccc=33 and the harakat ccc=27–32 are distinct non-zero classes).

#: Arabic base letters (hamza U+0621 … yeh U+064A) that a shadda geminates.
_AR_LETTER = "ء-ي"
#: Arabic short-vowel / nunation / sukun / superscript-alef marks that may
#: sit between a consonant and its shadda (or after it).
_AR_HARAKAT = "ً-ِْٰ"
_AR_SHADDA = "ّ"

# consonant + shadda + harakat  →  consonant consonant harakat
_AR_GEM_SHADDA_FIRST = re.compile(
    f"([{_AR_LETTER}]){_AR_SHADDA}([{_AR_HARAKAT}])"
)
# consonant + harakat + shadda  →  consonant consonant harakat
_AR_GEM_HARAKAT_FIRST = re.compile(
    f"([{_AR_LETTER}])([{_AR_HARAKAT}]){_AR_SHADDA}"
)
# consonant + shadda (no adjacent harakat, e.g. before a consonant / pause)
_AR_GEM_BARE = re.compile(f"([{_AR_LETTER}]){_AR_SHADDA}")


def _decompose_arabic_presentation_forms(text: str) -> str:
    """NFKC-decompose only Arabic Presentation-Form codepoints.

    Codepoints in U+FB50–U+FDFF (Forms-A) and U+FE70–U+FEFF (Forms-B) —
    ligatures and contextual glyph variants, including the lam-alif
    ligatures — are replaced by their compatibility decomposition to the
    canonical Arabic letters. Every other codepoint is returned unchanged,
    so no other script is disturbed.
    """
    def _is_presentation_form(ch: str) -> bool:
        cp = ord(ch)
        # Forms-A: U+FB50–U+FDFF ; Forms-B: U+FE70–U+FEFF
        return 0xFB50 <= cp <= 0xFDFF or 0xFE70 <= cp <= 0xFEFF

    if not any(_is_presentation_form(ch) for ch in text):
        return text
    return "".join(
        unicodedata.normalize("NFKC", ch) if _is_presentation_form(ch) else ch
        for ch in text
    )


def _expand_arabic_gemination(text: str) -> str:
    """Expand shadda gemination: double the carrying consonant, drop shadda.

    Handles both mark orderings, then any remaining bare shadda (gemination
    with no adjacent harakat). See the module block comment for the sources.
    """
    if _AR_SHADDA not in text:
        return text
    text = _AR_GEM_SHADDA_FIRST.sub(r"\1\1\2", text)
    text = _AR_GEM_HARAKAT_FIRST.sub(r"\1\1\2", text)
    text = _AR_GEM_BARE.sub(r"\1\1", text)
    return text


# ═══════════════════════════════════════════════════════════════════════════
# Locale-aware casing
# ═══════════════════════════════════════════════════════════════════════════

# Python's `str.lower()` is locale-agnostic and mishandles Turkish
# dotted/dotless I: 'I'.lower() == 'i' (should be dotless 'ı'), and
# 'İ'.lower() == 'i̇' (a combining-dot artifact, should be plain
# 'i'). Explicit substitution tables, applied only for Turkish
# (`tr`, `tr-*`), keep every other language on plain `str.lower()`.
_TR_LOWER_MAP: Dict[str, str] = {"I": "ı", "İ": "i"}


def _is_turkish(lang: str) -> bool:
    return lang == "tr" or lang.startswith("tr-")


def _lower(ch: str, lang: str) -> str:
    """Language-aware lowercasing for a single character.

    Falls back to plain :meth:`str.lower` for every language except
    Turkish, where dotted/dotless I is handled via explicit mapping.
    """
    if lang and _is_turkish(lang):
        mapped = _TR_LOWER_MAP.get(ch)
        if mapped is not None:
            return mapped
    return ch.lower()


def lower_str(text: str, lang: str) -> str:
    """Language-aware lowercasing for a whole string.

    Same rationale as :func:`_lower`, applied character-by-character
    so it is a drop-in replacement for ``text.lower()`` at call sites
    that need Turkish-correct casing (e.g. word-exception lookups)."""
    if lang and _is_turkish(lang):
        return "".join(_lower(ch, lang) for ch in text)
    return text.lower()


# ═══════════════════════════════════════════════════════════════════════════
# Token types
# ═══════════════════════════════════════════════════════════════════════════

class TokenKind(Enum):
    """Classification of a single token produced by the tokenizer."""

    GRAPHEME = auto()
    """A linguistically meaningful grapheme from the language's table."""

    WHITESPACE = auto()
    """One or more whitespace characters (space, tab, newline, …)."""

    PUNCTUATION = auto()
    """Punctuation mark (.,;:!?…—–-/\\()[]{}⟨⟩«»""''‹›)."""

    DIGIT = auto()
    """One or more consecutive digit characters."""

    UNKNOWN = auto()
    """Character(s) not matched by any grapheme, punctuation, or digit."""

    BOS = auto()
    """Beginning-of-sequence sentinel."""

    EOS = auto()
    """End-of-sequence sentinel."""


@dataclass(frozen=True, slots=True)
class Token:
    """A single token emitted by :class:`PhonetokTokenizer`."""

    kind: TokenKind
    """What kind of token this is."""

    grapheme: str
    """The surface string exactly as it appeared in the input
    (lower-cased for GRAPHEME tokens; original case for others)."""

    ipa: Tuple[str, ...]
    """Possible IPA values for this token.  Empty for non-GRAPHEME tokens."""

    position: int
    """Character offset into the original input string."""

    length: int
    """Number of characters consumed from the input."""

    def __repr__(self) -> str:
        ipa_str = "|".join(self.ipa) if self.ipa else ""
        return (
            f"Token({self.kind.name}, {self.grapheme!r}, "
            f"[{ipa_str}], pos={self.position})"
        )


# ═══════════════════════════════════════════════════════════════════════════
# IPA path (a single candidate transcription)
# ═══════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True, slots=True)
class IPAPath:
    """One possible IPA transcription path through a token sequence."""

    segments: Tuple[str, ...]
    """IPA segment for each GRAPHEME token (whitespace etc. excluded)."""

    score: float
    """Heuristic score (lower = more canonical). By default the first IPA
    listed for each grapheme is the canonical form (cost 0) and
    alternatives receive +1 each. When a spec declares per-candidate
    weights the per-grapheme cost is ``-log(p)`` instead — see
    :mod:`orthography2ipa.weights` and ``docs/candidate_scoring.md``."""

    @property
    def ipa(self) -> str:
        """Concatenated IPA string."""
        return "".join(self.segments)

    def __repr__(self) -> str:
        return f"IPAPath({self.ipa!r}, score={self.score:.1f})"


# ═══════════════════════════════════════════════════════════════════════════
# Structured lattice (per-position ranked candidates)
# ═══════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True, slots=True)
class Candidate:
    """One ranked IPA option for a single lattice slot.

    ``cost`` is the additive beam cost of choosing this option: for a spec
    that declares per-candidate weights it is the ``-log P`` of the
    candidate's (normalised) probability; for a plain-list spec it is the
    uniform-descending *rank* cost (``0.0`` for the canonical candidate,
    ``1.0`` for the next, …). Lower cost = more likely. See
    :mod:`orthography2ipa.weights` and ``docs/lattice.md``.
    """

    ipa: str
    """The IPA string for this option (a single grapheme's realisation)."""

    cost: float
    """Additive beam cost — ``-log P`` (weighted spec) or rank cost."""

    def __repr__(self) -> str:
        return f"Candidate({self.ipa!r}, cost={self.cost:.4f})"


@dataclass(frozen=True, slots=True)
class SegmentSlot:
    """One position in the structured pronunciation lattice.

    A slot corresponds to a single GRAPHEME token of the input and carries
    the ranked IPA options that grapheme may realise as in its context.
    :meth:`PhonetokTokenizer.ipa_lattice` returns the slots in **surface
    order**, and concatenating each slot's top (lowest-cost) candidate
    reproduces :meth:`PhonetokTokenizer.ipa_best` called with default
    arguments (the lattice has no slots for whitespace, so a non-empty
    ``word_separator`` or ``include_special=True`` is not reflected). This
    is the per-position lattice — the structured object downstream engines
    consume — not a flattened list of whole-word path strings (that is
    :class:`IPAPath` / :meth:`PhonetokTokenizer.ipa_beam`).

    Extension seams (implemented in later work, noted here so the shape is
    stable): a *rescorer* (B4) hooks in by adjusting each candidate's
    ``cost`` given the surrounding slots before a path is chosen; a
    *confidence* signal (B5) is derived from the top-1 vs top-2 ``cost``
    margin within a slot. Both read this object without changing it.
    """

    grapheme: str
    """The source grapheme (lower-cased, as tokenised)."""

    span: Tuple[int, int]
    """``(start, end)`` character offsets locating the grapheme, following
    the same NFC/casefold contract as :attr:`GraphemeContext.span`::

        import unicodedata
        unicodedata.normalize("NFC", text)[start:end].lower() == grapheme
    """

    candidates: Tuple[Candidate, ...]
    """Ranked IPA options, best (lowest ``cost``) first. Never empty for a
    GRAPHEME slot; ``candidates[0]`` is the canonical realisation."""

    @property
    def top(self) -> Candidate:
        """The best (lowest-cost) candidate for this slot."""
        return self.candidates[0]

    def __repr__(self) -> str:
        return (
            f"SegmentSlot({self.grapheme!r}, span={self.span}, "
            f"candidates={self.candidates!r})"
        )


# ═══════════════════════════════════════════════════════════════════════════
# Per-word confidence / OOV signal (B5)
# ═══════════════════════════════════════════════════════════════════════════
#
# A pure, deterministic read off the lattice slots — no global state, no
# randomness, thread-safe. The signal answers one question for a downstream
# specialized phonemizer: *where should it spend its expensive lexicon/rules?*
# High confidence ⇒ trust the base engine's fallback; low confidence ⇒ the
# base engine is unsure, so the specialized engine earns its keep there.
#
# It is built entirely from costs the lattice already carries
# (``Candidate.cost`` = −log P for a weighted spec, rank cost otherwise; see
# ``docs/lattice.md``), combining three signals:
#
# 1. **Ambiguity** — the top-1 vs top-2 ``cost`` margin *within* a slot. A
#    large margin means one option dominates (confident); a margin of ``0``
#    means two options tie (maximally ambiguous). A slot with a single
#    candidate has no rival, so its margin is ``+inf`` (fully unambiguous).
#    Mapped to ``[0, 1]`` by ``1 − exp(−margin)``: ``margin=0 → 0``,
#    ``margin=+inf → 1``.
# 2. **Rarity** — the absolute cost of the *best* candidate. A slot whose
#    winner is itself high-cost (a rare mapping, large −log P) is less
#    trustworthy than one whose winner is the canonical ``cost=0`` option.
#    Mapped by ``exp(−cost1)``: ``cost1=0 → 1``, larger cost → smaller.
# 3. **Coverage / OOV** — folded in by the caller (see
#    :meth:`G2P.word_confidence`): any unmapped grapheme multiplies the
#    lattice confidence by ``coverage`` (< 1), sharply lowering it.
#
# Per slot the ambiguity and rarity factors multiply; across the word the
# **minimum** slot confidence wins ("weakest link"): a single ambiguous or
# rare position drags the whole word down, which is exactly the position a
# downstream engine should target.


def slot_confidence(slot: "SegmentSlot") -> float:
    """Confidence in ``slot.top`` being the right realisation, in ``[0, 1]``.

    Combines the intra-slot **ambiguity** margin (top-1 vs top-2 ``cost``)
    with the **rarity** of the winning candidate (its absolute ``cost``).
    Returns ``1.0`` for an unambiguous, canonical slot (single candidate, or
    a decisive margin over a zero-cost winner) and approaches ``0.0`` as the
    top two candidates tie and/or the winner is a rare (high-cost) mapping.
    A pure function of the slot — no state, deterministic.
    """
    cands = slot.candidates
    if not cands:
        return 0.0
    cost1 = cands[0].cost
    if len(cands) >= 2:
        margin = cands[1].cost - cost1
        ambiguity = 1.0 - math.exp(-margin)
    else:
        ambiguity = 1.0  # no rival candidate → unambiguous
    rarity = math.exp(-cost1) if cost1 > 0.0 else 1.0
    return ambiguity * rarity


def lattice_confidence(slots: Sequence["SegmentSlot"]) -> float:
    """Aggregate :func:`slot_confidence` across a word's lattice ``slots``.

    Uses the **minimum** ("weakest link") slot confidence: the least
    confident position bounds the word. An empty lattice (no grapheme slots)
    returns ``1.0`` — there is nothing the engine was unsure about. Does not
    fold OOV/coverage; the caller multiplies that in (see
    :meth:`G2P.word_confidence`).
    """
    if not slots:
        return 1.0
    return min(slot_confidence(s) for s in slots)


# ═══════════════════════════════════════════════════════════════════════════
# Context-aware grapheme view
# ═══════════════════════════════════════════════════════════════════════════

class GraphemeContext:
    """A context-aware view over one GRAPHEME :class:`Token`.

    Wraps a single grapheme token and exposes what phonemizers built on
    top of this library otherwise re-roll by hand: access to neighbouring
    grapheme tokens (``prev``/``next``, arbitrary ``±N`` offsets and a
    ``neighbors`` window), the grapheme's character span, and
    phonological-class predicates that delegate to
    :mod:`orthography2ipa.vowels` (the single source of truth for vowel
    classification — no vowel set is defined here).

    Neighbours are **word-local**: they are the nearest GRAPHEME tokens
    *within the same run of graphemes*, and never cross a WHITESPACE,
    PUNCTUATION, DIGIT or UNKNOWN token. The first grapheme of a word has
    ``prev is None``; the last has ``next is None``. Offsets that fall past
    a word edge return ``None`` (from :meth:`at`) or are omitted (from
    :meth:`neighbors`).

    Class predicates delegate to :mod:`orthography2ipa.vowels` on the
    grapheme's first character. For the common single-character vowel
    graphemes this is exact; for multi-character graphemes (digraphs such
    as ``ch``/``qu``/``ai``) the leading character is used, so a
    consonant digraph reports as a consonant and a vowel digraph reports
    by its leading vowel.

    Instances are cheap flyweights created once per
    :meth:`PhonetokTokenizer.tokenize_with_context` call (O(n) overall)
    and hold back-references into their :class:`TokenSequence`; they are
    not intended to be constructed directly.
    """

    __slots__ = ("token", "index", "_run", "_run_pos")

    def __init__(
            self,
            token: Token,
            index: int,
            run: List["GraphemeContext"],
            run_pos: int,
    ) -> None:
        self.token = token
        """The wrapped GRAPHEME :class:`Token`."""

        self.index = index
        """Zero-based position of this grapheme among *all* GRAPHEME tokens
        in the sequence (whitespace/punctuation excluded)."""

        self._run = run
        self._run_pos = run_pos

    # ─── Convenience passthroughs ───────────────────────────────────────

    @property
    def grapheme(self) -> str:
        """The surface grapheme string (lower-cased, as tokenised)."""
        return self.token.grapheme

    @property
    def ipa(self) -> Tuple[str, ...]:
        """Possible IPA values for this grapheme (from the token)."""
        return self.token.ipa

    @property
    def span(self) -> Tuple[int, int]:
        """``(start, end)`` character offsets locating this grapheme.

        The offsets index the **NFC-normalised** form of the input that
        :meth:`tokenize` works on, and :attr:`grapheme` is **case-folded**
        (lower-cased). The exact contract is therefore::

            import unicodedata
            unicodedata.normalize("NFC", text)[start:end].lower() == grapheme

        A raw ``text[start:end]`` round-trip against the caller's original
        string only holds when that string is already lower-case NFC — it
        breaks for upper-case input (offsets index the un-folded text) and
        for NFD input (offsets index the NFC-normalised text)."""
        start = self.token.position
        return (start, start + self.token.length)

    # ─── Word-local neighbour access ────────────────────────────────────

    def at(self, offset: int) -> Optional["GraphemeContext"]:
        """Return the grapheme *offset* positions away within the same word.

        ``at(0)`` is ``self``, ``at(1)`` the next grapheme, ``at(-2)`` two
        graphemes back. Returns ``None`` when the offset falls before the
        first or past the last grapheme of the current word (run).
        """
        j = self._run_pos + offset
        if 0 <= j < len(self._run):
            return self._run[j]
        return None

    @property
    def prev(self) -> Optional["GraphemeContext"]:
        """Nearest preceding grapheme within the same word, or ``None``."""
        return self.at(-1)

    @property
    def next(self) -> Optional["GraphemeContext"]:
        """Nearest following grapheme within the same word, or ``None``."""
        return self.at(1)

    def neighbors(self, n: int = 1) -> List["GraphemeContext"]:
        """Return up to ``2*n`` neighbouring graphemes within ``±n``.

        Ordered left-to-right (``-n … -1, +1 … +n``); ``self`` is excluded.
        Offsets past a word edge are clamped away (omitted), so a word-edge
        grapheme returns fewer than ``2*n`` neighbours.
        """
        if n < 1:
            return []
        out: List["GraphemeContext"] = []
        for k in range(-n, n + 1):
            if k == 0:
                continue
            ctx = self.at(k)
            if ctx is not None:
                out.append(ctx)
        return out

    # ─── Phonological-class predicates (delegate to vowels.py) ──────────

    @property
    def is_vowel(self) -> bool:
        """True if the grapheme's leading character is a written vowel
        letter (:func:`orthography2ipa.vowels.is_orthographic_vowel`)."""
        return bool(self.grapheme) and is_orthographic_vowel(self.grapheme[0])

    @property
    def is_consonant(self) -> bool:
        """True if this grapheme is not a vowel (its complement among
        GRAPHEME tokens)."""
        return bool(self.grapheme) and not self.is_vowel

    @property
    def is_front(self) -> bool:
        """True if the grapheme's leading character is a *front* vowel
        letter (:func:`orthography2ipa.vowels.is_front_vowel`)."""
        return bool(self.grapheme) and is_front_vowel(self.grapheme[0])

    @property
    def is_back(self) -> bool:
        """True if the grapheme's leading character is a *back* vowel
        letter (:func:`orthography2ipa.vowels.is_back_vowel`)."""
        return bool(self.grapheme) and is_back_vowel(self.grapheme[0])

    @property
    def is_palatal(self) -> bool:
        """True if this grapheme's *primary IPA* is a palatal / palato-alveolar
        consonant (:func:`orthography2ipa.vowels.is_palatal_consonant`).

        Unlike the vowel-class predicates (which read the written letter), this
        reads the sound the grapheme maps to — ``ipa[0]`` — because palatality
        is a property of the phoneme: ⟨lh⟩→/ʎ/, ⟨nh⟩→/ɲ/, ⟨ch⟩→/ʃ/ all report
        palatal regardless of their spelling. Used by the ``BEFORE_PALATAL`` /
        ``AFTER_PALATAL`` positions and the ``"palatal"`` allophone-rule class."""
        return bool(self.ipa) and is_palatal_consonant(self.ipa[0])

    def __repr__(self) -> str:
        return f"GraphemeContext({self.grapheme!r}, index={self.index})"


class TokenSequence:
    """An indexed, context-aware view over a tokenised string.

    Built once by :meth:`PhonetokTokenizer.tokenize_with_context`, it keeps
    the full token stream (``tokens``) and wraps every GRAPHEME token in a
    :class:`GraphemeContext` that can reach its word-local neighbours in
    O(1). Iterating a :class:`TokenSequence` yields the
    :class:`GraphemeContext` views in order; indexing and ``len`` operate
    on the grapheme contexts too.

    The underlying full token list (including whitespace/punctuation) stays
    available via :attr:`tokens` for callers that need it.
    """

    __slots__ = ("tokens", "_contexts")

    def __init__(self, tokens: List[Token]) -> None:
        self.tokens = tokens
        """The complete token list, exactly as :meth:`tokenize` produced it."""

        contexts: List[GraphemeContext] = []
        run: List[GraphemeContext] = []
        for tok in tokens:
            if tok.kind == TokenKind.GRAPHEME:
                ctx = GraphemeContext(tok, len(contexts), run, len(run))
                run.append(ctx)
                contexts.append(ctx)
            else:
                # Any non-grapheme token ends the current word run.
                run = []
        self._contexts = contexts

    @property
    def graphemes(self) -> List[GraphemeContext]:
        """All :class:`GraphemeContext` views, in order."""
        return self._contexts

    def __iter__(self):
        return iter(self._contexts)

    def __len__(self) -> int:
        return len(self._contexts)

    def __getitem__(self, i):
        return self._contexts[i]

    def __repr__(self) -> str:
        return f"TokenSequence(graphemes={len(self._contexts)})"


def flat_contexts(g_tokens: List[Token]) -> List["GraphemeContext"]:
    """Wrap a flat list of GRAPHEME tokens as one contiguous run.

    Unlike :class:`TokenSequence` (which starts a new word-local run at
    every non-grapheme token), this treats *all* the given tokens as a
    single neighbour run. The engine calls it after word-splitting has
    already stripped whitespace/punctuation, so the per-word grapheme
    tokens (including any that flank an in-word UNKNOWN character) stay
    adjacent — preserving the engine's established neighbour semantics.
    """
    run: List["GraphemeContext"] = []
    for i, tok in enumerate(g_tokens):
        run.append(GraphemeContext(tok, i, run, i))
    return run


# ═══════════════════════════════════════════════════════════════════════════
# Punctuation / digit detection
# ═══════════════════════════════════════════════════════════════════════════

# Broad punctuation set covering Latin, CJK, and typographic marks.
_PUNCT_RE = re.compile(
    r"["
    r"\u0021-\u002F"  # ! " # $ % & ' ( ) * + , - . /
    r"\u003A-\u0040"  # : ; < = > ? @
    r"\u005B-\u0060"  # [ \ ] ^ _ `
    r"\u007B-\u007E"  # { | } ~
    r"\u00A1-\u00BF"  # ¡ ¢ … ¿
    r"\u2010-\u2027"  # ‐ – — ― … ‧
    r"\u2030-\u205E"  # ‰ ′ ″ …
    r"\u3001-\u3003"  # 、。〃 (CJK)
    r"\uFF01-\uFF0F"  # ！ … ／ (fullwidth)
    r"\uFF1A-\uFF20"  # ： … ＠
    r"\uFF3B-\uFF40"  # ［ … ｀
    r"\uFF5B-\uFF65"  # ｛ … ･
    r"\u00AB\u00BB"  # « »
    r"\u2018-\u201F"  # ' ' ‚ ‛ " " „ ‟
    r"\u2039\u203A"  # ‹ ›
    r"]+"
)

_DIGIT_RE = re.compile(r"[0-9\u0660-\u0669\u06F0-\u06F9\u0966-\u096F]+")

_WS_RE = re.compile(r"\s+")


# ═══════════════════════════════════════════════════════════════════════════
# Trie for grapheme matching (maximal munch)
# ═══════════════════════════════════════════════════════════════════════════

class _TrieNode:
    """Simple prefix-trie node for grapheme lookup."""

    __slots__ = ("children", "grapheme_key")

    def __init__(self) -> None:
        self.children: Dict[str, _TrieNode] = {}
        self.grapheme_key: Optional[str] = None  # set at leaf


class _GraphemeTrie:
    """Prefix trie built from a grapheme table.

    Supports case-insensitive longest-match lookup.
    """

    def __init__(self, graphemes: Dict[str, List[str]], lang: str = "") -> None:
        self.lang = lang
        self.root = _TrieNode()
        self.max_len = 0
        for key in graphemes:
            lk = key.lower()
            node = self.root
            for ch in lk:
                if ch not in node.children:
                    node.children[ch] = _TrieNode()
                node = node.children[ch]
            node.grapheme_key = lk
            self.max_len = max(self.max_len, len(lk))

    def longest_match(self, text: str, start: int) -> Optional[str]:
        """Return the longest grapheme key matching at *start*, or None."""
        node = self.root
        best: Optional[str] = None
        for i in range(start, min(start + self.max_len, len(text))):
            ch = _lower(text[i], self.lang)
            if ch not in node.children:
                break
            node = node.children[ch]
            if node.grapheme_key is not None:
                best = node.grapheme_key
        return best


def _path_similarity(a: IPAPath, b: IPAPath) -> float:
    """Fraction of aligned segments two equal-length paths share (0..1).

    Paths through one word's lattice always share a segment count, so a
    positional (Hamming-style) overlap is well defined; for the rare
    differing-length case the shorter length is used as the denominator.
    """
    n = min(len(a.segments), len(b.segments))
    if n == 0:
        return 0.0
    same = sum(1 for x, y in zip(a.segments, b.segments) if x == y)
    return same / n


def _rerank_diverse(paths: List[IPAPath], diversity: float) -> List[IPAPath]:
    """Maximal-Marginal-Relevance re-ranking that demotes near-duplicates.

    The lowest-cost path is kept first; each subsequent pick minimises
    ``score + diversity × (max similarity to an already-selected path)``,
    so paths that differ from the top only in a single grapheme are pushed
    down in favour of genuinely different pronunciations. Ties fall back to
    the incoming ``(score, ipa)`` order (``paths`` is pre-sorted).
    """
    remaining = list(paths)
    selected: List[IPAPath] = []
    while remaining:
        if not selected:
            selected.append(remaining.pop(0))
            continue
        best_i = 0
        best_key: Optional[Tuple[float, str]] = None
        for i, p in enumerate(remaining):
            sim = max(_path_similarity(p, s) for s in selected)
            key = (p.score + diversity * sim, p.ipa)
            if best_key is None or key < best_key:
                best_key = key
                best_i = i
        selected.append(remaining.pop(best_i))
    return selected


# ═══════════════════════════════════════════════════════════════════════════
# Main tokenizer
# ═══════════════════════════════════════════════════════════════════════════

class PhonetokTokenizer:
    """Language-agnostic grapheme tokenizer with IPA beam expansion.

    Parameters
    ----------
    spec : LanguageSpec
        The language specification providing grapheme→IPA mappings.
    add_bos : bool
        Prepend a BOS token to every tokenize() result.
    add_eos : bool
        Append an EOS token to every tokenize() result.
    collapse_whitespace : bool
        Merge consecutive whitespace into a single WHITESPACE token.
    """

    # Special token surface strings
    BOS_STR = "<bos>"
    EOS_STR = "<eos>"
    UNK_STR = "<unk>"
    WS_STR = " "
    PUNCT_STR = "<punct>"
    DIGIT_STR = "<digit>"

    def __init__(
            self,
            spec: LanguageSpec,
            *,
            add_bos: bool = False,
            add_eos: bool = False,
            collapse_whitespace: bool = True,
    ) -> None:
        self.spec = spec
        self.add_bos = add_bos
        self.add_eos = add_eos
        self.collapse_whitespace = collapse_whitespace
        # Build normalised lookup (lowercase keys) from the base grapheme
        # table first.
        self._grapheme_ipa: Dict[str, Tuple[str, ...]] = {
            k.lower(): tuple(v) for k, v in spec.graphemes.items()
        }

        # Per-candidate weights aligned to `_grapheme_ipa` (lowercased
        # keys). Sparse — only graphemes whose spec used the weighted-object
        # form appear. Absent → `weights_for` returns None → the beam uses
        # rank cost (byte-identical to the pre-weights behaviour).
        self._grapheme_weights: Dict[str, Tuple[float, ...]] = {
            k.lower(): tuple(w)
            for k, w in (spec.grapheme_weights or {}).items()
        }

        # Grapheme keys that exist *only* as positional overrides (no entry
        # in the base `graphemes` table) must still be discoverable by the
        # maximal-munch trie, otherwise the tokenizer never recognises the
        # sequence and falls back to matching it character-by-character
        # (or as UNKNOWN tokens). Seed a fallback IPA value for those keys
        # from their positional candidates (DEFAULT position preferred,
        # else the first declared position) so tokenize() always has an
        # `ipa` value to attach; g2p.py's positional resolution logic
        # still consults `spec.positional_graphemes` afterwards to pick
        # the context-correct candidate.
        if spec.positional_graphemes:
            for grapheme, pos_map in spec.positional_graphemes.items():
                key = grapheme.lower()
                if key in self._grapheme_ipa or not pos_map:
                    continue
                candidates = pos_map.get(GraphemePosition.DEFAULT)
                if candidates is None:
                    candidates = next(iter(pos_map.values()))
                self._grapheme_ipa[key] = tuple(candidates)

        self._trie = _GraphemeTrie(self._grapheme_ipa, spec.code)

    def weights_for(self, grapheme: str) -> Optional[Tuple[float, ...]]:
        """Return the per-candidate weights for *grapheme*, or ``None``.

        ``None`` means the grapheme has no declared weights and the beam
        should fall back to uniform-descending *rank* cost. The lookup key
        is lower-cased to match the tokenizer's normalised grapheme table.
        """
        return self._grapheme_weights.get(grapheme.lower())

    # ─── Core tokenization ─────────────────────────────────────────────

    def tokenize(self, text: str) -> List[Token]:
        """Tokenize *text* into a list of :class:`Token` objects.

        Algorithm:
        1. Scan left-to-right.
        2. At each position, try (in order):
           a. Whitespace match.
           b. Punctuation match.
           c. Digit match.
           d. Longest grapheme match via trie.
           e. Single unknown character.
        3. Optionally wrap with BOS/EOS.
        """
        # NFC normalization handles combining marks (Arabic harakat,
        # Devanagari matras, accented Latin characters)
        text = unicodedata.normalize("NFC", text)

        # Arabic-script pre-tokenization normalization (script-scoped; no
        # other script is touched). See the module block comment for detail.
        if self.spec.script == "Arabic":
            text = _decompose_arabic_presentation_forms(text)
            # Gemination is only expanded for specs that actually model
            # shadda (arb and its descendants declare ّ in their grapheme
            # table); this leaves Arabic-script specs that do not — e.g.
            # Persian — byte-identical.
            if _AR_SHADDA in self._grapheme_ipa:
                text = _expand_arabic_gemination(text)

        tokens: List[Token] = []
        n = len(text)
        pos = 0

        if self.add_bos:
            tokens.append(Token(
                kind=TokenKind.BOS, grapheme=self.BOS_STR,
                ipa=(), position=0, length=0,
            ))

        while pos < n:
            # (a) Whitespace
            m = _WS_RE.match(text, pos)
            if m:
                span = m.group()
                surface = " " if self.collapse_whitespace else span
                tokens.append(Token(
                    kind=TokenKind.WHITESPACE, grapheme=surface,
                    ipa=(), position=pos, length=len(span),
                ))
                pos = m.end()
                continue

            # (b) Punctuation — unless a grapheme claims these characters, in
            # which case the grapheme wins. Two ways that happens: the spec
            # registers the punctuation span itself as a grapheme (apostrophe
            # as glottal stop in Tetum), or a LONGER grapheme starts here and
            # merely opens with punctuation (pinyin's empty rime ⟨-i⟩). The
            # second case needs the trie: matching punctuation first would bite
            # off the ⟨-⟩ and leave ⟨i⟩ behind, so ⟨-i⟩ could never be matched
            # at all. Maximal munch is the tokenizer's rule; it must hold here
            # too.
            m = _PUNCT_RE.match(text, pos)
            if m:
                span = m.group()
                claimed_by_grapheme = (
                    span in self._grapheme_ipa
                    or self._trie.longest_match(text, pos) is not None
                )
                if not claimed_by_grapheme:
                    tokens.append(Token(
                        kind=TokenKind.PUNCTUATION, grapheme=span,
                        ipa=(), position=pos, length=len(span),
                    ))
                    pos = m.end()
                    continue

            # (c) Digits
            m = _DIGIT_RE.match(text, pos)
            if m:
                span = m.group()
                tokens.append(Token(
                    kind=TokenKind.DIGIT, grapheme=span,
                    ipa=(), position=pos, length=len(span),
                ))
                pos = m.end()
                continue

            # (d) Longest grapheme match (trie)
            gkey = self._trie.longest_match(text, pos)
            if gkey is not None:
                ipa_vals = self._grapheme_ipa[gkey]
                consumed = len(gkey)
                # Inherent vowel for abugidas: after a consonant grapheme,
                # append the inherent vowel unless a virama/halant follows.
                if self.spec.inherent_vowel and ipa_vals:
                    next_pos = pos + consumed
                    next_ch = text[next_pos] if next_pos < n else ""
                    # Virama/halant characters across Brahmic scripts
                    if next_ch in ("\u094D", "\u09CD", "\u0A4D", "\u0ACD",
                                   "\u0B4D", "\u0BCD", "\u0C4D", "\u0CCD",
                                   "\u0D4D", "\u0E3A", "\u1039", "\u17D2"):
                        # Virama follows — pure consonant, consume virama
                        consumed += 1
                    else:
                        # Check if the first IPA value is consonantal
                        # (not a vowel grapheme) by checking if it's NOT
                        # in the vowel set. Simple heuristic: if the IPA
                        # value contains only consonant symbols.
                        first_ipa = ipa_vals[0]
                        if first_ipa and not is_ipa_vowel(first_ipa[0]):
                            ipa_vals = tuple(
                                v + self.spec.inherent_vowel for v in ipa_vals
                            )
                tokens.append(Token(
                    kind=TokenKind.GRAPHEME, grapheme=gkey,
                    ipa=ipa_vals, position=pos, length=consumed,
                ))
                pos += consumed
                continue

            # (e) Unknown single character
            ch = text[pos]
            tokens.append(Token(
                kind=TokenKind.UNKNOWN, grapheme=ch,
                ipa=(), position=pos, length=1,
            ))
            pos += 1

        if self.add_eos:
            tokens.append(Token(
                kind=TokenKind.EOS, grapheme=self.EOS_STR,
                ipa=(), position=n, length=0,
            ))

        return tokens

    # ─── Convenience: grapheme strings only ─────────────────────────────

    def graphemes(self, text: str) -> List[str]:
        """Return just the grapheme strings (all token types)."""
        return [t.grapheme for t in self.tokenize(text)]

    def grapheme_tokens(self, text: str) -> List[Token]:
        """Return only GRAPHEME-kind tokens (skip whitespace, punct, etc.)."""
        return [t for t in self.tokenize(text) if t.kind == TokenKind.GRAPHEME]

    # ─── Context-aware view ─────────────────────────────────────────────

    def tokenize_with_context(self, text: str) -> TokenSequence:
        """Tokenise *text* and return a context-aware :class:`TokenSequence`.

        The sequence wraps every GRAPHEME token in a
        :class:`GraphemeContext` exposing word-local neighbour access
        (``prev``/``next``/``at``/``neighbors``), character spans and
        phonological-class predicates (``is_vowel``/``is_consonant``/
        ``is_front``/``is_back``) that delegate to
        :mod:`orthography2ipa.vowels`.

        This is a purely additive convenience layer over :meth:`tokenize`;
        it does not alter tokenisation or IPA expansion.
        """
        return TokenSequence(self.tokenize(text))

    # ─── Slot resolution / rescoring helpers (shared by beam + lattice) ─

    def _grapheme_slots(
            self,
            tokens: List[Token],
            contexts: Sequence["GraphemeContext"],
            *,
            allophone_map: Optional[Dict[str, List[str]]],
    ) -> List[SegmentSlot]:
        """Fully resolved (untruncated) lattice slots, one per GRAPHEME.

        Each slot's candidates are the complete ``resolve_branches`` output
        — no per-slot truncation — so a rescorer sees every option. The
        standalone tokenizer supplies no stress context, so the
        stress-conditioned positions are omitted (matching :meth:`ipa_beam`).
        """
        slots: List[SegmentSlot] = []
        g_idx = 0
        for token in tokens:
            if token.kind != TokenKind.GRAPHEME:
                continue
            branches = resolve_branches(
                self.spec, contexts[g_idx],
                weights_for=self.weights_for,
                allophone_map=allophone_map)
            g_idx += 1
            slots.append(SegmentSlot(
                grapheme=token.grapheme,
                span=(token.position, token.position + token.length),
                candidates=tuple(
                    Candidate(ipa=ipa, cost=cost) for ipa, cost in branches),
            ))
        return slots

    def _rescored_branches(
            self,
            tokens: List[Token],
            contexts: Sequence["GraphemeContext"],
            rescorers: Sequence[LatticeRescorer],
            *,
            allophone_map: Optional[Dict[str, List[str]]],
    ) -> List[List[Tuple[str, float]]]:
        """Per-grapheme ``(ipa, cost)`` branches after rescoring.

        Resolves full slots, runs the rescorers (in order) over them, and
        flattens each slot back to the ``(ipa, cost)`` branch shape the beam
        consumes. An empty inner list marks a rescorer-deleted slot.
        """
        slots = self._grapheme_slots(
            tokens, contexts, allophone_map=allophone_map)
        rescored = apply_rescorers(slots, contexts, rescorers)
        return [
            [(c.ipa, c.cost) for c in slot.candidates]
            for slot in rescored
        ]

    # ─── IPA beam search ────────────────────────────────────────────────

    def ipa_beam(
            self,
            text: str,
            *,
            beam_width: int = 8,
            expand_allophones: bool = False,
            word_separator: str = " ",
            include_special: bool = False,
            length_norm: bool = False,
            diversity: float = 0.0,
            rescorer: RescorerArg = None,
    ) -> List[IPAPath]:
        """Expand all possible IPA transcription paths via beam search.

        For each GRAPHEME token, we branch on every possible IPA value
        from the grapheme table.  If *expand_allophones* is True, we
        further branch on every allophone of each phoneme.

        The search is bounded by *beam_width*: at each token we keep
        only the top-*beam_width* partial paths (ranked by score).

        Parameters
        ----------
        text : str
            Input text to transcribe.
        beam_width : int
            Maximum number of concurrent hypotheses (paths) to maintain.
            Set to -1 or a very large number for exhaustive enumeration.
        expand_allophones : bool
            If True, expand each phoneme into its allophonic variants
            from ``spec.allophones``, multiplying the search space.
        word_separator : str
            String to insert between words in the IPA output.  Set to
            ``""`` for no separator.
        include_special : bool
            If True, include whitespace/punct/digit tokens in the IPA
            path as literal strings instead of ignoring them.
        length_norm : bool
            Opt-in scoring quality knob (default ``False`` preserves the
            exact current ordering). When ``True`` each returned path's
            :attr:`IPAPath.score` is the **mean per-segment cost**
            (cumulative cost ÷ number of segments) instead of the raw
            cumulative cost, and paths are ranked by it. Beam *pruning* is
            unchanged (still by raw cumulative cost), so a single word's
            hypotheses — which all share the same segment count — keep
            their relative order; the normalisation only makes scores
            comparable across inputs of different length.
        diversity : float
            Opt-in diversity penalty (default ``0.0`` = off, preserving the
            exact current ordering). When ``> 0`` the returned paths are
            re-ranked with a Maximal-Marginal-Relevance pass: the top path
            is kept, and each subsequent path is penalised by
            ``diversity × (fraction of segments it shares with the nearest
            already-selected path)``. This demotes near-duplicates of the
            top path (which otherwise dominate a long word's beam, differing
            in only one grapheme) in favour of genuinely different
            pronunciations. The top-1 path never changes.
        rescorer : LatticeRescorer | Iterable[LatticeRescorer] | None
            Optional lattice rescorer(s) (Workstream B4). When given, each
            grapheme slot's resolved candidates are re-costed by the
            rescorer(s), *in order*, **before** beam path selection — the
            downstream-enablement seam by which a rule cascade (sun-letter
            assimilation, silent-``e``) refines the shared lattice instead
            of forking a tokenizer. ``None`` (default) is byte-identical to
            no rescoring. A rescorer that returns no candidates for a slot
            deletes it (the grapheme contributes no segment). See
            :mod:`orthography2ipa.rescorer`. Stress-conditioned context is
            unavailable on this standalone path (``context.is_stressed`` is
            ``None``); the full engine supplies it.

        Returns
        -------
        List[IPAPath]
            All paths found within beam width, sorted by score (best first).
        """
        tokens = self.tokenize(text)
        if beam_width < 0:
            beam_width = 2 ** 31

        # Word-local context views over the grapheme tokens: they give
        # each grapheme its neighbours so positional overrides (incl. the
        # vowel-class positions) resolve exactly as the full engine does.
        seq = TokenSequence(tokens)
        contexts = seq.graphemes

        # Each beam entry: (segments_so_far, cumulative_score)
        beam: List[Tuple[List[str], float]] = [([], 0.0)]

        allophone_map = self.spec.allophones if expand_allophones else None

        # Optional rescoring (B4): when rescorer(s) are supplied, pre-resolve
        # every grapheme slot, re-cost through the rescorers, and index the
        # resulting branches by grapheme position. Absent a rescorer this is
        # skipped entirely so the default path stays byte-identical.
        rescorers = normalize_rescorers(rescorer)
        rescored_branches: Optional[List[List[Tuple[str, float]]]] = None
        if rescorers:
            rescored_branches = self._rescored_branches(
                tokens, contexts, rescorers, allophone_map=allophone_map)

        g_idx = 0
        for token in tokens:
            if token.kind == TokenKind.GRAPHEME:
                # Stress/sandhi are engine-only (no sentence context here),
                # so the stress-conditioned nucleus positions are omitted;
                # every other position agrees with G2P per word.
                if rescored_branches is not None:
                    branches = rescored_branches[g_idx]
                    g_idx += 1
                    if not branches:
                        # Rescorer deleted this slot: it contributes no
                        # segment, leaving the running hypotheses untouched.
                        continue
                else:
                    branches = resolve_branches(
                        self.spec, contexts[g_idx],
                        weights_for=self.weights_for,
                        allophone_map=allophone_map)
                    g_idx += 1
                beam = self._expand_beam(beam, branches, beam_width)

            elif include_special:
                if token.kind == TokenKind.WHITESPACE:
                    beam = self._expand_beam(
                        beam, [(word_separator, 0.0)], beam_width,
                    )
                elif token.kind in (
                        TokenKind.PUNCTUATION, TokenKind.DIGIT, TokenKind.UNKNOWN,
                ):
                    beam = self._expand_beam(
                        beam, [(token.grapheme, 0.0)], beam_width,
                    )

        # Convert to IPAPath objects. The raw cumulative cost is the
        # canonical ranking key (byte-identical to historical behaviour);
        # length_norm/diversity are opt-in refinements applied afterwards.
        paths = [
            IPAPath(segments=tuple(segs), score=sc)
            for segs, sc in beam
        ]
        paths.sort(key=lambda p: (p.score, p.ipa))

        if length_norm:
            paths = [
                IPAPath(segments=p.segments,
                        score=(p.score / len(p.segments)) if p.segments
                        else p.score)
                for p in paths
            ]
            paths.sort(key=lambda p: (p.score, p.ipa))

        if diversity > 0.0:
            paths = _rerank_diverse(paths, diversity)

        return paths

    def ipa_best(
            self,
            text: str,
            *,
            expand_allophones: bool = False,
            word_separator: str = " ",
            include_special: bool = False,
            rescorer: RescorerArg = None,
    ) -> str:
        """Return the single best (most canonical) IPA transcription.

        Equivalent to ``ipa_beam(..., beam_width=1)[0].ipa``. Accepts the
        same optional *rescorer* (B4) as :meth:`ipa_beam`.
        """
        paths = self.ipa_beam(
            text,
            beam_width=1,
            expand_allophones=expand_allophones,
            word_separator=word_separator,
            include_special=include_special,
            rescorer=rescorer,
        )
        return paths[0].ipa if paths else ""

    # ─── Structured lattice ─────────────────────────────────────────────

    def ipa_lattice(
            self,
            text: str,
            *,
            beam_width: int = 8,
            expand_allophones: bool = False,
            rescorer: RescorerArg = None,
    ) -> List[SegmentSlot]:
        """Return the structured pronunciation lattice for *text*.

        Unlike :meth:`ipa_beam` (which flattens the search into whole-word
        :class:`IPAPath` strings), this returns one :class:`SegmentSlot`
        per GRAPHEME token, **in surface order**, each carrying its source
        grapheme, character span and the *ranked* IPA
        :class:`Candidate`\\ s available at that position. Non-grapheme
        tokens (whitespace/punctuation/digits) produce no slot.

        Each slot's candidates come from the *same* shared branch resolver
        the beam uses (:func:`orthography2ipa.positional.resolve_branches`),
        so positional overrides — including the vowel-class positions — and
        per-candidate weights apply here exactly as in
        :meth:`ipa_beam`/:class:`G2P`. Candidate ``cost`` is therefore a
        real ``-log P`` for a weighted spec and rank cost for a plain-list
        spec, and — because costs are additive and independent per slot —
        concatenating each slot's :attr:`~SegmentSlot.top` candidate
        reproduces :meth:`ipa_best` called with default arguments (the
        lattice has no whitespace slots, so a non-empty ``word_separator``
        or ``include_special=True`` is not reflected); a chosen path's
        total score is the sum of its per-slot chosen-candidate costs.

        Parameters
        ----------
        text : str
            Input text to build the lattice for.
        beam_width : int
            Maximum ranked candidates to keep *per slot*. The canonical
            candidate is always at index 0, so truncation never changes the
            top-of-slot concatenation. ``-1`` keeps every candidate.
        expand_allophones : bool
            Enumerate surface allophone variants (from ``spec.allophones``)
            as extra candidates, mirroring :meth:`ipa_beam`.
        rescorer : LatticeRescorer | Iterable[LatticeRescorer] | None
            Optional lattice rescorer(s) (Workstream B4). When given, each
            slot's candidates are re-costed by the rescorer(s), in order,
            *before truncation*, so the returned lattice reflects the
            rescored costs. A rescorer that returns no candidates for a slot
            deletes it (the slot is omitted from the returned list).
            ``None`` (default) leaves the lattice byte-identical. See
            :mod:`orthography2ipa.rescorer`.

        Notes
        -----
        This is the object downstream engines consume. A *rescorer* (B4)
        re-costs each slot's candidates given the neighbouring slots before
        a path is chosen; a per-word *confidence* (B5) is read from the
        top-1 vs top-2 ``cost`` margin across slots. Neither changes the
        slot shape returned here.
        """
        tokens = self.tokenize(text)
        contexts = TokenSequence(tokens).graphemes
        allophone_map = self.spec.allophones if expand_allophones else None
        keep = 2 ** 31 if beam_width < 0 else beam_width

        rescorers = normalize_rescorers(rescorer)
        if rescorers:
            full = self._grapheme_slots(
                tokens, contexts, allophone_map=allophone_map)
            rescored = apply_rescorers(full, contexts, rescorers)
            return [
                SegmentSlot(grapheme=s.grapheme, span=s.span,
                            candidates=s.candidates[:keep])
                for s in rescored
                if s.candidates  # a rescorer that empties a slot deletes it
            ]

        slots: List[SegmentSlot] = []
        g_idx = 0
        for token in tokens:
            if token.kind != TokenKind.GRAPHEME:
                continue
            ctx = contexts[g_idx]
            g_idx += 1
            branches = resolve_branches(
                self.spec, ctx,
                weights_for=self.weights_for,
                allophone_map=allophone_map)
            cands = tuple(
                Candidate(ipa=ipa, cost=cost)
                for ipa, cost in branches[:keep]
            )
            slots.append(SegmentSlot(
                grapheme=token.grapheme,
                span=(token.position, token.position + token.length),
                candidates=cands,
            ))
        return slots

    # ─── Vocabulary / special tokens ────────────────────────────────────

    @property
    def vocab(self) -> Dict[str, int]:
        """Return a vocabulary mapping: token_string → integer ID.

        Ordering:
        0: <pad>
        1: <bos>
        2: <eos>
        3: <unk>
        4: <ws>   (whitespace)
        5: <punct>
        6: <digit>
        7…: grapheme keys sorted alphabetically
        """
        v: Dict[str, int] = {
            "<pad>": 0,
            "<bos>": 1,
            "<eos>": 2,
            "<unk>": 3,
            "<ws>": 4,
            "<punct>": 5,
            "<digit>": 6,
        }
        idx = len(v)
        for g in sorted(self._grapheme_ipa):
            v[g] = idx
            idx += 1
        return v

    @property
    def vocab_size(self) -> int:
        """Total vocabulary size including special tokens."""
        return 7 + len(self._grapheme_ipa)

    def encode(self, text: str) -> List[int]:
        """Encode *text* into integer token IDs using :attr:`vocab`."""
        v = self.vocab
        tokens = self.tokenize(text)
        ids: List[int] = []
        for t in tokens:
            if t.kind == TokenKind.BOS:
                ids.append(v["<bos>"])
            elif t.kind == TokenKind.EOS:
                ids.append(v["<eos>"])
            elif t.kind == TokenKind.WHITESPACE:
                ids.append(v["<ws>"])
            elif t.kind == TokenKind.PUNCTUATION:
                ids.append(v["<punct>"])
            elif t.kind == TokenKind.DIGIT:
                ids.append(v["<digit>"])
            elif t.kind == TokenKind.GRAPHEME:
                ids.append(v.get(t.grapheme, v["<unk>"]))
            else:
                ids.append(v["<unk>"])
        return ids

    def decode(self, ids: Sequence[int]) -> str:
        """Decode integer token IDs back into a grapheme string."""
        inv = {v: k for k, v in self.vocab.items()}
        parts: List[str] = []
        for i in ids:
            tok = inv.get(i, "<unk>")
            if tok == "<ws>":
                parts.append(" ")
            elif tok.startswith("<"):
                continue  # skip special tokens in decode
            else:
                parts.append(tok)
        return "".join(parts)

    # ─── Internal helpers ───────────────────────────────────────────────

    @staticmethod
    def _ipa_branches(
            token: Token,
            allophone_map: Optional[Dict[str, List[str]]],
            weights: Optional[Sequence[float]] = None,
    ) -> List[Tuple[str, float]]:
        """Return (ipa_string, cost) branches for one GRAPHEME token.

        Without *weights* (plain-list grapheme): cost 0 for the first
        (canonical) IPA and +1 for each alternative — the rank ordering.
        With valid *weights* the per-candidate cost is ``-log(p)`` (see
        :func:`orthography2ipa.weights.candidate_base_costs`); the branch
        shape ``(ipa, cost)`` is unchanged so ``_expand_beam`` is agnostic.
        If allophone expansion is on, each phoneme further branches into
        its allophonic variants at +0.5 cost each beyond the first.

        This is a thin wrapper over
        :func:`orthography2ipa.positional.build_branches`, the single
        shared branch-builder used by both the tokenizer beam and the
        engine's positional beam; it does **not** apply positional
        overrides (those need context — see :func:`~orthography2ipa.
        positional.resolve_branches`).
        """
        return build_branches(
            token.ipa, weights, allophone_map, token.grapheme)

    @staticmethod
    def _expand_beam(
            beam: List[Tuple[List[str], float]],
            branches: List[Tuple[str, float]],
            beam_width: int,
    ) -> List[Tuple[List[str], float]]:
        """Expand every beam entry with every branch, then prune.

        Positional-nasalisation guard: a lone combining tilde branch
        (U+0303 emitted by a coda ⟨m/n⟩ → nasalised-vowel slot) is only a
        valid segment when it attaches to a preceding *oral vowel or glide*.
        If the phoneme it would land on is a consonant (e.g. a ⟨gu⟩→[ɡ]
        vowel-drop artefact: *algum* → [ɡ̃]) or an already-nasalised nucleus
        (double tilde: *inn* → [ĩ̃]), the tilde would produce invalid IPA, so
        that branch is dropped and the slot's oral fallback (the coda nasal
        as a plain consonant) wins instead. This suppresses only the invalid
        tilde-on-consonant / double-tilde; every branch that lands on a vowel
        is untouched, so all pre-existing behaviour is byte-identical.
        """
        new_beam: List[Tuple[List[str], float]] = []
        for segs, sc in beam:
            for ipa, cost in branches:
                if ipa == _NASAL_TILDE:
                    tail = ""
                    for seg in reversed(segs):
                        if seg:
                            tail = seg[-1]
                            break
                    if tail not in _NASAL_CARRIERS:
                        continue
                new_beam.append((segs + [ipa], sc + cost))
        if not new_beam:
            # Every branch was a guarded tilde with no valid carrier and no
            # oral alternative in this slot — keep them rather than drop the
            # slot entirely (defensive; the coda ⟨m/n⟩ slots always carry an
            # oral consonant fallback so this is not reached in practice).
            for segs, sc in beam:
                for ipa, cost in branches:
                    new_beam.append((segs + [ipa], sc + cost))
        # Sort by score, keep top beam_width
        new_beam.sort(key=lambda x: x[1])
        return new_beam[:beam_width]

    # ─── repr ───────────────────────────────────────────────────────────

    def __repr__(self) -> str:
        return (
            f"PhonetokTokenizer(lang={self.spec.code!r}, "
            f"graphemes={len(self._grapheme_ipa)}, "
            f"vocab_size={self.vocab_size})"
        )
