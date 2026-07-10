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
)
from orthography2ipa.weights import candidate_base_costs

from typing import TYPE_CHECKING

__all__ = [
    "TokenKind",
    "Token",
    "IPAPath",
    "GraphemeContext",
    "TokenSequence",
    "PhonetokTokenizer",
    "lower_str",
]


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
        """``(start, end)`` character offsets into the original input,
        such that ``text[start:end]`` is the surface grapheme."""
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

            # (b) Punctuation — unless the spec explicitly registers this
            # exact span as a grapheme (e.g. apostrophe as glottal stop
            # in Tetum), in which case the grapheme mapping wins.
            m = _PUNCT_RE.match(text, pos)
            if m:
                span = m.group()
                if span not in self._grapheme_ipa:
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

    # ─── IPA beam search ────────────────────────────────────────────────

    def ipa_beam(
            self,
            text: str,
            *,
            beam_width: int = 8,
            expand_allophones: bool = False,
            word_separator: str = " ",
            include_special: bool = False,
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

        Returns
        -------
        List[IPAPath]
            All paths found within beam width, sorted by score (best first).
        """
        tokens = self.tokenize(text)
        if beam_width < 0:
            beam_width = 2 ** 31

        # Each beam entry: (segments_so_far, cumulative_score)
        beam: List[Tuple[List[str], float]] = [([], 0.0)]

        allophone_map = self.spec.allophones if expand_allophones else None

        for token in tokens:
            if token.kind == TokenKind.GRAPHEME:
                branches = self._ipa_branches(
                    token, allophone_map,
                    self.weights_for(token.grapheme))
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

        # Convert to IPAPath objects
        paths = [
            IPAPath(segments=tuple(segs), score=sc)
            for segs, sc in beam
        ]
        paths.sort(key=lambda p: (p.score, p.ipa))
        return paths

    def ipa_best(
            self,
            text: str,
            *,
            expand_allophones: bool = False,
            word_separator: str = " ",
            include_special: bool = False,
    ) -> str:
        """Return the single best (most canonical) IPA transcription.

        Equivalent to ``ipa_beam(..., beam_width=1)[0].ipa``.
        """
        paths = self.ipa_beam(
            text,
            beam_width=1,
            expand_allophones=expand_allophones,
            word_separator=word_separator,
            include_special=include_special,
        )
        return paths[0].ipa if paths else ""

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
        """
        costs = candidate_base_costs(
            token.ipa, weights, grapheme=token.grapheme)
        branches: List[Tuple[str, float]] = []
        for rank, phoneme in enumerate(token.ipa):
            base_cost = costs[rank]
            if allophone_map and phoneme in allophone_map:
                allophones = allophone_map[phoneme]
                for a_rank, allophone in enumerate(allophones):
                    branches.append((allophone, base_cost + 0.5 * a_rank))
            else:
                branches.append((phoneme, base_cost))
        # Deduplicate (keep lowest cost)
        seen: Dict[str, float] = {}
        for ipa, cost in branches:
            if ipa not in seen or cost < seen[ipa]:
                seen[ipa] = cost
        return sorted(seen.items(), key=lambda x: (x[1], x[0]))

    @staticmethod
    def _expand_beam(
            beam: List[Tuple[List[str], float]],
            branches: List[Tuple[str, float]],
            beam_width: int,
    ) -> List[Tuple[List[str], float]]:
        """Expand every beam entry with every branch, then prune."""
        new_beam: List[Tuple[List[str], float]] = []
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
