"""features — pure-data linguistic feature export for downstream ML / CRF G2P.

`orthography2ipa` ships **no trained weights**, which makes it an ideal
*feature provider* for a downstream sequence model (a CRF or a small neural
G2P). It already computes, per grapheme, everything such a model wants —
phonological-class predicates, word-local neighbours, the ranked candidate
lattice with `-log P` costs, and a per-word confidence signal. This module
packages that structure as a clean, flat, JSON-able **feature view** so a CRF
trains on linguistically-grounded features instead of raw character n-grams,
and then plugs back in as a
:class:`~orthography2ipa.rescorer.LatticeRescorer` over the shared lattice.

The public entry point is :meth:`orthography2ipa.g2p.G2P.features`; this module
holds the record types it returns. Everything here is a **pure read** — it
never affects :meth:`~orthography2ipa.g2p.G2P.transcribe`. See
``docs/features.md`` for the CRF-as-rescorer pattern and a worked example.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence, Tuple

from orthography2ipa.phonetok import GraphemeContext, SegmentSlot

__all__ = [
    "GraphemeFeatures",
    "WordFeatures",
    "build_word_features",
]

# Scalar value types produced by ``as_dict`` — everything is directly
# ``json.dumps``-safe and accepted as a python-crfsuite / sklearn-crfsuite
# feature value.
FeatureValue = object


@dataclass(frozen=True)
class GraphemeFeatures:
    """The feature record for a single grapheme — one item of a CRF sequence.

    A flat, deterministic view combining the grapheme's phonological class
    (delegated to :class:`~orthography2ipa.phonetok.GraphemeContext`, so no
    vowel set is redefined here), its word-local neighbours, and the ranked
    IPA candidate lattice for the slot. :meth:`as_dict` renders it as a
    scalar, JSON-able feature dict for a CRF library.
    """

    grapheme: str
    """The source grapheme (lower-cased, as tokenised)."""

    span: Tuple[int, int]
    """``(start, end)`` NFC character offsets of the grapheme (same contract
    as :attr:`SegmentSlot.span` / :attr:`GraphemeContext.span`)."""

    index: int
    """Zero-based position of this grapheme **within its word**."""

    position: str
    """Word-relative position: ``"initial"``, ``"medial"`` or ``"final"``."""

    prev: Optional[str]
    """Immediately preceding grapheme within the word, or ``None`` at the
    word's left edge."""

    next: Optional[str]
    """Immediately following grapheme within the word, or ``None`` at the
    word's right edge."""

    prev2: Optional[str]
    """The grapheme two positions back within the word, or ``None``."""

    next2: Optional[str]
    """The grapheme two positions ahead within the word, or ``None``."""

    is_vowel: bool
    """Phonological-class predicate — delegates to
    :attr:`GraphemeContext.is_vowel` (single source of truth for vowels)."""

    is_consonant: bool
    """Complement of :attr:`is_vowel` (:attr:`GraphemeContext.is_consonant`)."""

    is_front: bool
    """Front-vowel predicate (:attr:`GraphemeContext.is_front`)."""

    is_back: bool
    """Back-vowel predicate (:attr:`GraphemeContext.is_back`)."""

    candidates: Tuple[Tuple[str, float], ...]
    """Ranked ``(ipa, cost)`` options for this slot, best (lowest cost)
    first — the same lattice a :class:`LatticeRescorer` re-costs. Never empty
    for a grapheme slot."""

    top1_ipa: str
    """IPA of the best (lowest-cost) candidate."""

    top1_cost: float
    """Cost of the best candidate (``0.0`` for a canonical, unweighted slot)."""

    margin: Optional[float]
    """Cost gap between the top-1 and top-2 candidates (``cost2 - cost1``).
    ``None`` when the slot has a single candidate (no rival ⇒ unambiguous).
    Kept ``None`` rather than ``+inf`` so :meth:`as_dict` stays strict-JSON
    safe. A larger margin means the winner is less ambiguous."""

    n_candidates: int
    """Number of ranked candidates for this slot."""

    confidence: float
    """Per-**word** confidence in ``[0, 1]`` (Workstream B5), denormalised
    onto every grapheme of the word so each CRF item carries it. This is the
    signal that says *where* a learned model should spend capacity: low
    confidence ⇒ the base engine is unsure at this word."""

    script: str
    """The language's primary script (e.g. ``"Latin"``)."""

    code: str
    """The resolved language code (e.g. ``"en-GB"``)."""

    def as_dict(self) -> Dict[str, FeatureValue]:
        """Flat, JSON-able, CRF-consumable feature dict for this grapheme.

        Every value is a scalar (``str`` / ``int`` / ``float`` / ``bool`` /
        ``None``) so the dict is directly a python-crfsuite item and
        ``json.dumps``-clean. The nested ranked :attr:`candidates` list is
        intentionally **omitted** here (it is not a scalar CRF feature); read
        it off the dataclass when you need the full lattice. The character
        span is emitted as ``span_start`` / ``span_end``.
        """
        return {
            "grapheme": self.grapheme,
            "index": self.index,
            "position": self.position,
            "span_start": self.span[0],
            "span_end": self.span[1],
            "prev": self.prev,
            "next": self.next,
            "prev2": self.prev2,
            "next2": self.next2,
            "is_vowel": self.is_vowel,
            "is_consonant": self.is_consonant,
            "is_front": self.is_front,
            "is_back": self.is_back,
            "top1_ipa": self.top1_ipa,
            "top1_cost": self.top1_cost,
            "margin": self.margin,
            "n_candidates": self.n_candidates,
            "confidence": self.confidence,
            "script": self.script,
            "code": self.code,
        }


@dataclass(frozen=True)
class WordFeatures:
    """The feature sequence for one word — the unit a CRF trains/predicts on."""

    word: str
    """Orthographic surface form (as it appeared after normalization)."""

    code: str
    """The resolved language code."""

    script: str
    """The language's primary script."""

    confidence: float
    """The word's per-word confidence in ``[0, 1]`` (Workstream B5)."""

    graphemes: Tuple[GraphemeFeatures, ...]
    """Per-grapheme feature records, in surface order."""

    def as_dicts(self) -> List[Dict[str, FeatureValue]]:
        """The CRF feature **sequence** for this word — ``as_dict`` per
        grapheme, in order. Pass alongside the gold IPA label sequence to a
        CRF's ``trainer.append(xseq, yseq)`` / ``CRF().fit(X, y)``.
        """
        return [g.as_dict() for g in self.graphemes]


def _position(index: int, total: int) -> str:
    if index == 0:
        return "initial"
    if index == total - 1:
        return "final"
    return "medial"


def build_word_features(
    word: str,
    slots: Sequence[SegmentSlot],
    contexts: Sequence[GraphemeContext],
    confidence: float,
    code: str,
    script: str,
) -> WordFeatures:
    """Assemble a :class:`WordFeatures` from a word's lattice and contexts.

    ``slots`` (from :meth:`G2P.ipa_lattice`) and ``contexts`` (from
    :func:`~orthography2ipa.phonetok.flat_contexts` over the same grapheme
    tokens) are aligned by character span: both are built from the identical
    ``grapheme_tokens(word)`` in surface order and share each grapheme's
    ``span``. Looking each slot up by its start offset stays correct even if a
    rescorer drops a slot. All phonological predicates and neighbours are read
    off the matched :class:`GraphemeContext` — no vowel logic is recomputed.
    """
    span_map: Dict[int, GraphemeContext] = {c.span[0]: c for c in contexts}
    total = len(slots)
    records: List[GraphemeFeatures] = []
    for index, slot in enumerate(slots):
        ctx = span_map.get(slot.span[0])
        cands = tuple((c.ipa, c.cost) for c in slot.candidates)
        margin: Optional[float] = (
            slot.candidates[1].cost - slot.candidates[0].cost
            if len(slot.candidates) >= 2 else None
        )

        def _nb(offset: int) -> Optional[str]:
            if ctx is None:
                return None
            other = ctx.at(offset)
            return other.grapheme if other is not None else None

        records.append(GraphemeFeatures(
            grapheme=slot.grapheme,
            span=slot.span,
            index=index,
            position=_position(index, total),
            prev=_nb(-1),
            next=_nb(1),
            prev2=_nb(-2),
            next2=_nb(2),
            is_vowel=bool(ctx.is_vowel) if ctx is not None else False,
            is_consonant=bool(ctx.is_consonant) if ctx is not None else False,
            is_front=bool(ctx.is_front) if ctx is not None else False,
            is_back=bool(ctx.is_back) if ctx is not None else False,
            candidates=cands,
            top1_ipa=slot.candidates[0].ipa if slot.candidates else "",
            top1_cost=slot.candidates[0].cost if slot.candidates else 0.0,
            margin=margin,
            n_candidates=len(slot.candidates),
            confidence=confidence,
            script=script,
            code=code,
        ))
    return WordFeatures(
        word=word,
        code=code,
        script=script,
        confidence=confidence,
        graphemes=tuple(records),
    )
