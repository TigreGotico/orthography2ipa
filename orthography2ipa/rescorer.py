"""rescorer — the lattice rescoring seam (Workstream B4).

The structured pronunciation lattice (:mod:`orthography2ipa.phonetok`,
Workstream B3) resolves each grapheme into a slot of ranked
``(ipa, cost)`` :class:`~orthography2ipa.phonetok.Candidate`\\ s. A
*rescorer* is the extension point that lets a downstream rule cascade —
arbtok's sun-letter assimilation, tugaphone's silent-``e`` — run over the
**shared** lattice instead of forking a parallel tokenizer. It re-costs
(and may reorder, add, drop, or delete) a slot's candidates as a pure
function of that slot and its context, before the beam selects a path.

Pipeline position
-----------------
A rescorer runs **after** positional/weight branch generation
(:func:`orthography2ipa.positional.resolve_branches`, i.e. the E2.1 −log P
costing) and **before** beam path selection::

    normalize → tokenize → resolve branches (positional + weights)
                              │
                              ▼
                     ┌─ rescore (B4)  ← this module; also where B8 allophony plugs in
                     │      │
                     ▼      ▼
                 beam path selection → stress → sandhi → dialect

Because every rescorer is a pure function of ``(slot, context)`` over the
*fully resolved* lattice — it sees the pre-rescore candidates of every
neighbouring slot, not a partial beam path — rescorers **compose**: a list
is applied in order and each one sees the previous one's output. This is
the same stage where the B8 post-lexical allophone pass attaches (a
phoneme→surface rewrite is exactly a rescorer that replaces a slot's IPA
with its context-conditioned realisation).

Absent a rescorer (the default), the lattice and beam behave byte-for-byte
as before — the seam adds nothing to the default path.

Context and what is available where
-----------------------------------
:class:`RescoreContext` exposes the current slot's B1
:class:`~orthography2ipa.phonetok.GraphemeContext` (word-local ``prev``/
``next`` graphemes and phonological-class predicates), the resolved
neighbouring **slots** (``prev_slot``/``next_slot``, word-local), the
slot's position in the word, and — *where available* — syllable/stress
information.

**Stress availability differs by entry path, honestly:**

- The **engine** path (:meth:`orthography2ipa.g2p.G2P.transcribe`,
  :meth:`~orthography2ipa.g2p.G2P.ipa_lattice`) computes syllabification
  and stress, so ``context.syll_idx`` / ``context.stressed_syll_idx`` /
  ``context.is_stressed`` are populated.
- The **standalone tokenizer** path
  (:meth:`orthography2ipa.phonetok.PhonetokTokenizer.ipa_beam` /
  ``ipa_lattice``) has no sentence-level stress detection, so those fields
  are ``None`` / ``None`` / ``None``. A rescorer that needs stress must
  guard for ``None`` (and can, if it chooses, no-op when stress is
  unavailable — exactly as the stress-conditioned positional rules do).

Empty-candidate return
----------------------
A rescorer may return an **empty** sequence for a slot. This is a
*feature*, not an error: the slot is **deleted** — it contributes no
segment to any beam path and is dropped from ``ipa_lattice`` output. This
is how a silent-grapheme rule (tugaphone silent-``e``) is expressed. The
beam never crashes on it (an empty branch list is skipped, leaving the
running hypotheses untouched).
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import (
    TYPE_CHECKING, Iterable, List, Optional, Sequence, Tuple, Union,
)

if TYPE_CHECKING:  # avoid an import cycle with phonetok
    from orthography2ipa.phonetok import (
        Candidate, GraphemeContext, SegmentSlot,
    )

__all__ = [
    "LatticeRescorer",
    "RescoreContext",
    "normalize_rescorers",
    "apply_rescorers",
]


@dataclass(frozen=True, slots=True)
class RescoreContext:
    """Everything a :class:`LatticeRescorer` sees about one slot's context.

    A rescorer is a **pure function** of the slot it is handed and this
    context — it holds no global state, so it is trivially testable and
    composable. All the neighbour views describe the lattice *as resolved
    before this rescorer ran* (or, in a composed chain, as left by the
    previous rescorer); a rescorer therefore reasons over stable
    candidates rather than a half-selected beam path.
    """

    slot: "SegmentSlot"
    """The slot being rescored, with its current (pre-this-rescorer)
    candidates."""

    index: int
    """Zero-based position of this slot among the word's GRAPHEME slots."""

    slots: Sequence["SegmentSlot"]
    """All GRAPHEME slots of the current word, in surface order. Aligned
    1:1 with :attr:`grapheme`'s sequence, so ``slots[index] is slot``."""

    grapheme: "GraphemeContext"
    """The B1 context view for this grapheme: word-local ``prev``/``next``
    grapheme access and ``is_vowel``/``is_consonant``/``is_front``/
    ``is_back`` predicates (single source of truth =
    :mod:`orthography2ipa.vowels`)."""

    syll_idx: Optional[int] = None
    """Syllable index of this grapheme, or ``None`` when the entry path has
    no stress context (the standalone tokenizer)."""

    stressed_syll_idx: Optional[int] = None
    """Index of the stressed syllable of the word, or ``None`` when
    unavailable (standalone tokenizer)."""

    # ─── neighbour convenience (word-local, honouring word boundaries) ──

    @property
    def prev_slot(self) -> Optional["SegmentSlot"]:
        """The resolved slot immediately before this one *within the same
        word*, or ``None`` at a word start."""
        if self.grapheme.prev is None or self.index == 0:
            return None
        return self.slots[self.index - 1]

    @property
    def next_slot(self) -> Optional["SegmentSlot"]:
        """The resolved slot immediately after this one *within the same
        word*, or ``None`` at a word end."""
        if self.grapheme.next is None or self.index + 1 >= len(self.slots):
            return None
        return self.slots[self.index + 1]

    @property
    def is_word_initial(self) -> bool:
        """True if this is the first grapheme of its word."""
        return self.grapheme.prev is None

    @property
    def is_word_final(self) -> bool:
        """True if this is the last grapheme of its word."""
        return self.grapheme.next is None

    @property
    def is_stressed(self) -> Optional[bool]:
        """Whether this grapheme sits in the stressed syllable.

        ``None`` when stress context is unavailable (standalone tokenizer);
        a rescorer needing stress must guard for ``None``.
        """
        if self.stressed_syll_idx is None or self.syll_idx is None:
            return None
        return self.syll_idx == self.stressed_syll_idx


class LatticeRescorer(ABC):
    """A pure, composable re-costing pass over one lattice slot.

    Implement :meth:`rescore` to return the slot's new candidate list.
    Returning the slot's existing ``candidates`` unchanged is a no-op;
    returning a re-costed / reordered / filtered / extended list changes
    what the beam selects; returning an **empty** sequence deletes the slot
    (see the module docstring). The returned candidates are re-sorted by
    ``cost`` (ties broken by IPA) before the beam consumes them, so a
    rescorer expresses "promote candidate X" simply by lowering X's cost.

    A rescorer is applied identically on the standalone tokenizer beam and
    the full engine — the only difference is that ``context.is_stressed``
    and the syllable fields are ``None`` on the tokenizer path (documented
    in the module docstring). Keep :meth:`rescore` free of global state so
    a list of rescorers composes deterministically.

    Example — a mini assimilation rule (c → /s/ before a front vowel)::

        class CBeforeFront(LatticeRescorer):
            def rescore(self, slot, context):
                nxt = context.next_slot
                if slot.grapheme == "c" and nxt and context.grapheme.next \\
                        and context.grapheme.next.is_front:
                    return [Candidate("s", 0.0)] + [
                        c for c in slot.candidates if c.ipa != "s"
                    ]
                return slot.candidates
    """

    @abstractmethod
    def rescore(
        self, slot: "SegmentSlot", context: RescoreContext,
    ) -> Sequence["Candidate"]:
        """Return the re-costed candidates for *slot*.

        Must be a pure function of *slot* and *context*. Return the
        existing candidates for a no-op, a new list to re-cost/reorder/
        add/remove, or an empty sequence to delete the slot.
        """
        raise NotImplementedError


# A rescorer argument: nothing, one rescorer, or an ordered collection.
RescorerArg = Union[None, LatticeRescorer, Iterable[LatticeRescorer]]


def normalize_rescorers(rescorer: RescorerArg) -> Tuple[LatticeRescorer, ...]:
    """Coerce the public ``rescorer=`` argument to an ordered tuple.

    Accepts ``None`` (→ empty tuple, the default byte-identical path), a
    single :class:`LatticeRescorer`, or any iterable of them (applied in
    iteration order). Raises :class:`TypeError` on anything else.
    """
    if rescorer is None:
        return ()
    if isinstance(rescorer, LatticeRescorer):
        return (rescorer,)
    out: List[LatticeRescorer] = []
    for r in rescorer:
        if not isinstance(r, LatticeRescorer):
            raise TypeError(
                f"rescorer entries must be LatticeRescorer, got {type(r)!r}")
        out.append(r)
    return tuple(out)


def apply_rescorers(
    slots: Sequence["SegmentSlot"],
    contexts: Sequence["GraphemeContext"],
    rescorers: Sequence[LatticeRescorer],
    *,
    syll_for_token: Optional[Sequence[int]] = None,
    stressed_syll_idx: Optional[int] = None,
) -> List["SegmentSlot"]:
    """Apply *rescorers* in order to every slot, returning new slots.

    *slots* are the fully resolved (post positional + weight) slots of one
    word, aligned 1:1 with *contexts* (the B1 grapheme views). For each
    rescorer, in order, every slot is rebuilt from that rescorer's returned
    candidates (re-sorted by ``(cost, ipa)``); the next rescorer therefore
    sees the previous one's output. A rescorer that returns an empty
    sequence leaves a slot with empty ``candidates`` — the caller (beam or
    lattice) is responsible for treating that as a deleted slot.

    Pure: it never mutates *slots* (frozen dataclasses) and holds no state.
    """
    from orthography2ipa.phonetok import SegmentSlot

    current: List["SegmentSlot"] = list(slots)
    for rescorer in rescorers:
        rescored: List["SegmentSlot"] = []
        for i, slot in enumerate(current):
            ctx = RescoreContext(
                slot=slot,
                index=i,
                slots=current,
                grapheme=contexts[i],
                syll_idx=(syll_for_token[i]
                          if syll_for_token is not None else None),
                stressed_syll_idx=stressed_syll_idx,
            )
            new_cands = rescorer.rescore(slot, ctx)
            if new_cands is slot.candidates:
                rescored.append(slot)
                continue
            ordered = tuple(sorted(new_cands, key=lambda c: (c.cost, c.ipa)))
            rescored.append(SegmentSlot(
                grapheme=slot.grapheme,
                span=slot.span,
                candidates=ordered,
            ))
        current = rescored
    return current
