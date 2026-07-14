"""sentence — the cross-word (utterance-scope) seam (Workstream C4).

The per-word lattice (:mod:`orthography2ipa.phonetok`) and its
:class:`~orthography2ipa.rescorer.LatticeRescorer` are, by design, strictly
**word-local**: a rescorer sees one slot and its immediate neighbours
*within a word*, and never crosses a word boundary. That is the right scope
for word-internal phonology (assimilation, silent graphemes, reduction), but
it cannot express the genuinely non-local processes that motivate the
downstream engines:

- **Arabic** ``waṣl`` (elision of a following word's initial
  *hamzat al-waṣl* across a boundary) and **pausal** forms (a phrase-final
  word realises differently — ``tanwīn`` suppression, ``tāʾ marbūṭa`` → [h]);
- **French liaison** (a latent word-final consonant resyllabifies as the
  *next* word's onset before a vowel);
- **Portuguese** external ``/s/``-sandhi across a word boundary.

Each needs two things the word lattice does not provide: **visibility into
the adjacent word's edge** (its final / initial candidates) and the word's
**phrase / utterance position** (is it phrase-final? utterance-initial?).
Today a downstream engine that needs those forks a private sentence
orchestrator. This module is the shared seam so it does not have to.

What it adds
------------
:class:`SentenceLattice` — the whole utterance as an *ordered* list of
:class:`WordSlot` objects, each carrying that word's per-grapheme lattice
(:class:`~orthography2ipa.phonetok.SegmentSlot`), its chosen IPA, and its
phrase / utterance position. A consumer sees the ranked candidates of every
word in order, not a flattened string.

:class:`SentenceRescorer` — the ABC mirroring
:class:`~orthography2ipa.rescorer.LatticeRescorer`, but at **sentence
scope**. It is invoked once per word with a :class:`SentenceRescoreContext`
that exposes the adjacent words (and their edge slots) plus phrase /
utterance position, and returns that word's (possibly rewritten) IPA. Because
it is invoked *per word*, a boundary rewrite that must change **both** words
(liaison resyllabification, ``waṣl`` elision on the right word) is expressed
naturally: the left word's invocation rewrites the left, the right word's
invocation rewrites the right, both seeing the same boundary context. This is
the bidirectionality the old :class:`~orthography2ipa.sandhi.SandhiEngine`
lacks (it can only rewrite the left word of a pair).

Opt-in and byte-identical when unused
-------------------------------------
Nothing here runs unless a caller passes ``sentence_rescorer=`` to
:class:`~orthography2ipa.g2p.G2P` (or calls
:meth:`~orthography2ipa.g2p.G2P.sentence_lattice` explicitly). With no
sentence rescorer, :meth:`~orthography2ipa.g2p.G2P.transcribe` is byte-for-byte
what it was — including the spec's declarative ``sandhi_rules`` via
:class:`~orthography2ipa.sandhi.SandhiEngine`, which keep working exactly as
now and **coexist** with this seam (sentence rescorers run first, then the
spec's sandhi pass).

Composition and determinism
---------------------------
A *list* of sentence rescorers composes like lattice rescorers: they apply in
order, and each pass sees the previous pass's rewritten IPA (via
:attr:`SentenceRescoreContext.prev_word_ipa` /
:attr:`~SentenceRescoreContext.next_word_ipa`), while *within* a single pass
every word reads the pre-pass snapshot so the pass is order-independent and
deterministic. A rescorer that returns ``word.ipa`` unchanged is a no-op.

What is still downstream (C5)
-----------------------------
This seam supplies **position and cross-word adjacency**, not **meaning**.
Homograph disambiguation that needs part-of-speech or semantics (English
*read* /riːd/ vs /rɛd/, Portuguese *sede* 'thirst' vs 'headquarters') is not
expressible here and remains a downstream concern — the context carries no
POS or sense field, deliberately.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import (
    TYPE_CHECKING, Iterable, List, Optional, Sequence, Tuple, Union,
)

if TYPE_CHECKING:  # avoid an import cycle with phonetok / g2p
    from orthography2ipa.phonetok import SegmentSlot

__all__ = [
    "Position",
    "WordSlot",
    "SentenceLattice",
    "SentenceRescoreContext",
    "SentenceRescorer",
    "SentenceRescorerArg",
    "normalize_sentence_rescorers",
    "apply_sentence_rescorers",
]


class Position(str, Enum):
    """Where a word sits inside a bounded span (a phrase, or the utterance).

    A *phrase* is a run of words bounded by pause punctuation
    (``.,;:!?…``) or the utterance edges — the same boundary the engine
    already marks as *pausal*. Position is computed for both the phrase span
    and the whole-utterance span (see :attr:`WordSlot.phrase_position` and
    :attr:`WordSlot.utterance_position`).

    :attr:`SOLE` is the degenerate span of length one — the word is at once
    initial and final (a one-word phrase, or a one-word utterance), so both
    :meth:`is_initial` and :meth:`is_final` are true.
    """

    INITIAL = "initial"
    """First of at least two words in the span (not the last)."""

    MEDIAL = "medial"
    """Neither first nor last — the span has ≥ 3 words and this is interior."""

    FINAL = "final"
    """Last of at least two words in the span (not the first)."""

    SOLE = "sole"
    """The only word in the span — both initial and final."""

    def is_initial(self) -> bool:
        """True at the start of the span (``INITIAL`` or ``SOLE``)."""
        return self in (Position.INITIAL, Position.SOLE)

    def is_final(self) -> bool:
        """True at the end of the span (``FINAL`` or ``SOLE``)."""
        return self in (Position.FINAL, Position.SOLE)


def span_position(index: int, start: int, end: int) -> Position:
    """The :class:`Position` of word *index* in the half-open span
    ``[start, end)``.

    ``start``/``end`` bound a phrase (or the utterance) in word indices.
    A length-one span yields :attr:`Position.SOLE`.
    """
    first = index == start
    last = index == end - 1
    if first and last:
        return Position.SOLE
    if first:
        return Position.INITIAL
    if last:
        return Position.FINAL
    return Position.MEDIAL


@dataclass(frozen=True)
class WordSlot:
    """One word's place in a :class:`SentenceLattice`.

    Carries the word's per-grapheme lattice (so a consumer sees its ranked
    candidates, not just the flattened string) alongside the position
    metadata that a cross-word rule needs.
    """

    surface: str
    """Orthographic surface form (after normalization), as split from input."""

    ipa: str
    """The word's chosen IPA in isolation — the per-word engine output
    (after stress, before any sentence rescorer or the spec's sandhi pass).
    A :class:`SentenceRescorer` reads this and returns a rewrite of it."""

    slots: Tuple["SegmentSlot", ...]
    """The word's pronunciation lattice — one
    :class:`~orthography2ipa.phonetok.SegmentSlot` per GRAPHEME, in surface
    order, with ranked ``(ipa, cost)`` candidates (the engine-context
    lattice, identical to :meth:`~orthography2ipa.g2p.G2P.ipa_lattice`). Empty
    for a lexicon-``word_exceptions`` override or an all-unmapped word."""

    index: int
    """Zero-based position of this word in the utterance."""

    phrase_position: Position
    """This word's :class:`Position` within its punctuation-bounded phrase."""

    utterance_position: Position
    """This word's :class:`Position` within the whole utterance."""

    pausal: bool = False
    """The word stands immediately before a pause (pause punctuation or the
    end of input) — i.e. it is phrase-final. Conditions e.g. Arabic pausal
    realisation. Equivalent to ``phrase_position.is_final()``."""

    @property
    def initial_slot(self) -> Optional["SegmentSlot"]:
        """The word's first lattice slot (its *onset* edge), or ``None`` when
        the word has no lattice. A cross-word rule reads this to inspect the
        next word's initial candidates from the boundary."""
        return self.slots[0] if self.slots else None

    @property
    def final_slot(self) -> Optional["SegmentSlot"]:
        """The word's last lattice slot (its *coda* edge), or ``None`` when
        the word has no lattice. A cross-word rule reads this to inspect the
        previous word's final candidates from the boundary."""
        return self.slots[-1] if self.slots else None


@dataclass(frozen=True)
class SentenceLattice:
    """The whole utterance as an ordered list of :class:`WordSlot`.

    The sentence-scope analogue of the per-word lattice: it exposes every
    word's ranked candidates **in order** with word boundaries and phrase /
    utterance position, so a consumer can reason over the entire utterance's
    search space rather than a flattened IPA string. Read via
    :meth:`~orthography2ipa.g2p.G2P.sentence_lattice`.
    """

    words: Tuple[WordSlot, ...]
    """The utterance's words, in surface order."""

    lang: str = ""
    """The resolved canonical language code used."""

    @property
    def ipa(self) -> str:
        """The utterance IPA — each word's :attr:`WordSlot.ipa` joined with
        spaces (skipping empties). This is the *pre-sentence-rescore*,
        *pre-sandhi* reading; it matches
        :meth:`~orthography2ipa.g2p.G2P.transcribe` only when no sentence
        rescorer and no spec ``sandhi_rules`` apply."""
        return " ".join(w.ipa for w in self.words if w.ipa)

    def __len__(self) -> int:
        return len(self.words)

    def __iter__(self):
        return iter(self.words)

    def __getitem__(self, i: int) -> WordSlot:
        return self.words[i]


@dataclass(frozen=True)
class SentenceRescoreContext:
    """Everything a :class:`SentenceRescorer` sees about one word's place in
    the utterance.

    Like :class:`~orthography2ipa.rescorer.RescoreContext` for a slot, this is
    a pure, immutable view. It gives a cross-word rule the two things the
    word-local lattice cannot: the **adjacent words** (with their edge slots,
    via :attr:`WordSlot.initial_slot` / :attr:`~WordSlot.final_slot`) and this
    word's **phrase / utterance position**.
    """

    word: WordSlot
    """The word being rescored."""

    index: int
    """Zero-based position of :attr:`word` in the utterance
    (``== word.index``; ``words[index] is word``)."""

    words: Sequence[WordSlot]
    """All words of the utterance, in surface order."""

    lang: str = ""
    """The resolved canonical language code."""

    _ipas: Sequence[str] = ()
    """Chain snapshot of every word's current IPA (as left by earlier
    rescorers in the chain). Read via :attr:`prev_word_ipa` /
    :attr:`next_word_ipa` / :attr:`this_word_ipa`; internal otherwise."""

    # ─── adjacency (honouring utterance edges) ──────────────────────────

    @property
    def prev_word(self) -> Optional[WordSlot]:
        """The preceding word, or ``None`` at the utterance start. Its final
        candidates are ``context.prev_word.final_slot``."""
        return self.words[self.index - 1] if self.index > 0 else None

    @property
    def next_word(self) -> Optional[WordSlot]:
        """The following word, or ``None`` at the utterance end. Its initial
        candidates are ``context.next_word.initial_slot``."""
        return (self.words[self.index + 1]
                if self.index + 1 < len(self.words) else None)

    @property
    def this_word_ipa(self) -> str:
        """This word's current IPA in the chain (== the ``ipa`` a no-op
        should return). Equals :attr:`WordSlot.ipa` on the first pass; a later
        pass sees an earlier pass's rewrite."""
        return self._ipas[self.index] if self._ipas else self.word.ipa

    @property
    def prev_word_ipa(self) -> Optional[str]:
        """The preceding word's current IPA in the chain, or ``None`` at the
        utterance start. Reflects earlier rescorers' rewrites."""
        if self.index == 0:
            return None
        return (self._ipas[self.index - 1] if self._ipas
                else self.words[self.index - 1].ipa)

    @property
    def next_word_ipa(self) -> Optional[str]:
        """The following word's current IPA in the chain, or ``None`` at the
        utterance end. Reflects earlier rescorers' rewrites."""
        if self.index + 1 >= len(self.words):
            return None
        return (self._ipas[self.index + 1] if self._ipas
                else self.words[self.index + 1].ipa)

    # ─── position convenience ───────────────────────────────────────────

    @property
    def phrase_position(self) -> Position:
        """This word's :class:`Position` within its punctuation-bounded
        phrase."""
        return self.word.phrase_position

    @property
    def utterance_position(self) -> Position:
        """This word's :class:`Position` within the whole utterance."""
        return self.word.utterance_position

    @property
    def is_phrase_initial(self) -> bool:
        """True if this word opens its phrase (conditions e.g. Arabic
        *hamzat al-waṣl* only at an utterance start — combine with
        :attr:`is_utterance_initial`)."""
        return self.word.phrase_position.is_initial()

    @property
    def is_phrase_final(self) -> bool:
        """True if this word closes its phrase (conditions e.g. Arabic pausal
        forms). Equivalent to ``word.pausal``."""
        return self.word.phrase_position.is_final()

    @property
    def is_utterance_initial(self) -> bool:
        """True if this word opens the utterance."""
        return self.word.utterance_position.is_initial()

    @property
    def is_utterance_final(self) -> bool:
        """True if this word closes the utterance."""
        return self.word.utterance_position.is_final()


class SentenceRescorer(ABC):
    """A pure, composable rewrite pass over one word, with cross-word context.

    The sentence-scope analogue of
    :class:`~orthography2ipa.rescorer.LatticeRescorer`. Implement
    :meth:`rescore` to return the word's new IPA string given its
    :class:`SentenceRescoreContext`. Returning ``word.ipa`` (or
    ``context.this_word_ipa``) unchanged is a no-op; returning a different
    string rewrites that word.

    **Bidirectional by construction.** Because :meth:`rescore` is invoked once
    per word, a boundary process that must change *both* words is expressed by
    having each word's invocation rewrite its own side while reading the shared
    boundary. French liaison, for instance: the left word's invocation strips
    its latent final consonant (or marks the tie), the right word's invocation
    prepends that consonant as its onset — both keyed off the same
    ``context.prev_word`` / ``context.next_word`` edge slots. The legacy
    :class:`~orthography2ipa.sandhi.SandhiEngine` could only rewrite the left
    word of a pair; this seam lifts that restriction.

    Keep :meth:`rescore` free of global state so a list of rescorers composes
    deterministically (see :func:`apply_sentence_rescorers`).
    """

    @abstractmethod
    def rescore(
        self, word: WordSlot, context: SentenceRescoreContext,
    ) -> str:
        """Return the (possibly rewritten) IPA for *word*.

        Must be a pure function of *word* and *context*. Return
        ``context.this_word_ipa`` for a no-op, or a new IPA string to rewrite
        this word.
        """
        raise NotImplementedError


# A sentence-rescorer argument: nothing, one, or an ordered collection.
SentenceRescorerArg = Union[
    None, SentenceRescorer, Iterable[SentenceRescorer]]


def normalize_sentence_rescorers(
    rescorer: SentenceRescorerArg,
) -> Tuple[SentenceRescorer, ...]:
    """Coerce the public ``sentence_rescorer=`` argument to an ordered tuple.

    Accepts ``None`` (→ empty tuple, the default byte-identical path), a
    single :class:`SentenceRescorer`, or any iterable of them (applied in
    iteration order). Raises :class:`TypeError` on anything else.
    """
    if rescorer is None:
        return ()
    if isinstance(rescorer, SentenceRescorer):
        return (rescorer,)
    out: List[SentenceRescorer] = []
    for r in rescorer:
        if not isinstance(r, SentenceRescorer):
            raise TypeError(
                "sentence_rescorer entries must be SentenceRescorer, "
                f"got {type(r)!r}")
        out.append(r)
    return tuple(out)


def apply_sentence_rescorers(
    lattice: SentenceLattice,
    rescorers: Sequence[SentenceRescorer],
) -> List[str]:
    """Apply *rescorers* in order to *lattice*, returning the per-word IPAs.

    For each rescorer, in order, every word's IPA is recomputed from the
    *current* chain snapshot; the whole pass is then committed at once, so a
    single pass reads a stable pre-pass snapshot (order-independent and
    deterministic) while the next pass sees this pass's output. A rescorer that
    returns a word's unchanged IPA leaves it untouched.

    Pure: it never mutates *lattice* (frozen) and holds no state. Returns a
    list aligned 1:1 with ``lattice.words``.
    """
    ipas: List[str] = [w.ipa for w in lattice.words]
    words = lattice.words
    for rescorer in rescorers:
        snapshot = tuple(ipas)
        for i, word in enumerate(words):
            ctx = SentenceRescoreContext(
                word=word,
                index=i,
                words=words,
                lang=lattice.lang,
                _ipas=snapshot,
            )
            ipas[i] = rescorer.rescore(word, ctx)
    return ipas


# ═══════════════════════════════════════════════════════════════════════════
# WordContext — what a word can see of its neighbours
# ═══════════════════════════════════════════════════════════════════════════
#
# Lives here because this is where cross-word context lives. It used to sit in a
# module called `g2p_plugin`, beside an abstract base class for a plugin system
# that did not exist: nothing in orthography2ipa ever discovered or called a
# `G2PPlugin`. The engines that implemented it — arbtok, tugaphone — are not
# plugins TO this library, they are engines built ON it, which is the opposite
# direction. The base class is gone; the TYPE is real, and it is shared
# vocabulary for exactly the thing this module is about.

@dataclass(frozen=True)
class WordContext:
    """Context for a word in a sentence, enabling sandhi/liaison.

    All fields default so existing call sites keep working; engines
    populate as much as they know.
    """

    prev_word_ipa: Optional[str] = None
    """IPA of the preceding word, if already transcribed."""

    next_word_ipa: Optional[str] = None
    """IPA of the following word, if already transcribed."""

    is_pausal: bool = False
    """The word stands before a pause — punctuation or end of input.

    Pausal position conditions e.g. Arabic tanwīn suppression and
    tāʾ marbūṭa realisation."""

    is_sentence_initial: bool = False
    """The word opens the sentence (conditions e.g. hamzat al-waṣl)."""

    prev_word: Optional[str] = None
    """Orthographic form of the preceding word."""

    next_word: Optional[str] = None
    """Orthographic form of the following word."""

    is_sentence_final: bool = False
    """The word closes the sentence."""

    word_index: int = 0
    """Zero-based position of the word in the sentence."""

    word_count: int = 1
    """Total number of words in the sentence."""

    lang: Optional[str] = None
    """Resolved BCP-47 code the transcription was requested for —
    lets a multi-dialect plugin pick the right variety."""
