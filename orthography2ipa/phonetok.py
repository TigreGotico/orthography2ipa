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

from orthography2ipa.types import LanguageSpec

from typing import TYPE_CHECKING

__all__ = [
    "TokenKind",
    "Token",
    "IPAPath",
    "PhonetokTokenizer",
]


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
    """Heuristic score (lower = more canonical).  The first IPA listed
    for each grapheme is treated as the canonical/default form and
    receives score 0; alternatives receive +1 each."""

    @property
    def ipa(self) -> str:
        """Concatenated IPA string."""
        return "".join(self.segments)

    def __repr__(self) -> str:
        return f"IPAPath({self.ipa!r}, score={self.score:.1f})"


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

    def __init__(self, graphemes: Dict[str, List[str]]) -> None:
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
            ch = text[i].lower()
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
        self._trie = _GraphemeTrie(spec.graphemes)
        # Build normalised lookup (lowercase keys)
        self._grapheme_ipa: Dict[str, Tuple[str, ...]] = {
            k.lower(): tuple(v) for k, v in spec.graphemes.items()
        }

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
                        _vowels = set("aeiouɛɔəɨʉɯæɐʌɒœøɪʊɤɵɞɑ")
                        if first_ipa and first_ipa[0] not in _vowels:
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
                branches = self._ipa_branches(token, allophone_map)
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
    ) -> List[Tuple[str, float]]:
        """Return (ipa_string, cost) branches for one GRAPHEME token.

        Cost 0 for the first (canonical) IPA; +1 for each alternative.
        If allophone expansion is on, each phoneme further branches
        into its allophonic variants at +0.5 cost each beyond the first.
        """
        branches: List[Tuple[str, float]] = []
        for rank, phoneme in enumerate(token.ipa):
            base_cost = float(rank)
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
