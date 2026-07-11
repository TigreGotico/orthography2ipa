"""allophony — the post-lexical allophone rule layer (Workstream B8).

The engine models the PRE-lexical map (orthography → phoneme) richly:
``positional_graphemes``, the vowel-class positions and per-candidate
weights all condition which phoneme a grapheme selects. The POST-lexical
map (phoneme → surface allophone) is what this module makes *live*.

A spec declares an ordered list of :class:`~orthography2ipa.types.AllophoneRule`
objects — declarative, pure-data ``phoneme → surface`` rewrites keyed on
phonological context (syllable position, stress, word position, and
neighbouring grapheme/phoneme class). :func:`compile_allophone_rescorer`
compiles that list into an :class:`AllophoneRescorer`, a
:class:`~orthography2ipa.rescorer.LatticeRescorer` (the Workstream B4
seam). Because it *is* a rescorer, it runs at exactly the right pipeline
position — after positional/weight phoneme selection, composed after any
user rescorer, and before beam path selection (hence before stress-mark
insertion and cross-word sandhi, which act on the whole utterance). This
is the "second stage" of the lattice: phoneme lattice → allophone lattice.

Realisation, not search-space inflation
----------------------------------------
Unlike ``expand_allophones`` (which enumerates *every* variant of
``spec.allophones`` into the beam at a flat ``+0.5`` cost — useful for
"give me all surface variants", useless for picking the correct one), an
allophone rule is a **deterministic rewrite**: it replaces a slot's chosen
phoneme with its single context-correct surface form at the *same* beam
cost, so the winner changes but the search space does not grow.

Stress availability
-------------------
Stress- and syllable-conditioned rules need the engine's stress context.
On the standalone tokenizer path (:meth:`PhonetokTokenizer.ipa_beam`) that
context is ``None``, so a ``stress=…`` rule simply does not fire there —
identical to how the stress-conditioned positional rules behave. Word
position and neighbour conditions work on both paths.
"""
from __future__ import annotations

from typing import List, Optional, Sequence

from orthography2ipa.phonetok import Candidate, GraphemeContext, SegmentSlot
from orthography2ipa.rescorer import LatticeRescorer, RescoreContext
from orthography2ipa.types import AllophoneRule

__all__ = [
    "AllophoneRescorer",
    "compile_allophone_rescorer",
]


def _syllable_position(ctx: GraphemeContext) -> str:
    """Classify the grapheme's syllable position by a maximal-onset rule.

    A vowel grapheme is a ``"nucleus"``; a consonant grapheme followed
    (word-locally) by a vowel is an ``"onset"``, otherwise a ``"coda"``.
    This is a declarative approximation that needs no external syllabifier
    and is exact for the word-edge cases that matter to final devoicing.
    """
    if ctx.is_vowel:
        return "nucleus"
    nxt = ctx.next
    if nxt is not None and nxt.is_vowel:
        return "onset"
    return "coda"


def _neighbor_is(cls: str, gctx: Optional[GraphemeContext]) -> bool:
    """Whether neighbour grapheme *gctx* matches the neighbour class *cls*."""
    if cls == "word_boundary":
        return gctx is None
    if gctx is None:
        return False
    if cls == "vowel":
        return gctx.is_vowel
    if cls == "consonant":
        return gctx.is_consonant
    if cls == "front_vowel":
        return gctx.is_front
    if cls == "back_vowel":
        return gctx.is_back
    return False  # unreachable — AllophoneRule validates the vocabulary


class AllophoneRescorer(LatticeRescorer):
    """A :class:`LatticeRescorer` compiled from a spec's ``allophone_rules``.

    For each slot it scans the slot's candidates; a candidate whose IPA is a
    target phoneme of the first rule whose context matches is rewritten to
    that rule's surface form (same cost). The candidates' costs are otherwise
    untouched, so this is a pure realisation pass, not a re-ranking. Returns
    the slot's existing ``candidates`` object unchanged (a genuine no-op)
    when no rule fires, so :func:`~orthography2ipa.rescorer.apply_rescorers`
    can skip it cheaply.
    """

    __slots__ = ("rules",)

    def __init__(self, rules: Sequence[AllophoneRule]) -> None:
        self.rules = tuple(rules)

    def rescore(
        self, slot: "SegmentSlot", context: RescoreContext,
    ) -> Sequence["Candidate"]:
        new: Optional[List[Candidate]] = None
        for idx, cand in enumerate(slot.candidates):
            surface = self._realize(cand.ipa, context)
            if surface is not None and surface != cand.ipa:
                if new is None:
                    new = list(slot.candidates)
                new[idx] = Candidate(ipa=surface, cost=cand.cost)
        return new if new is not None else slot.candidates

    def _realize(self, ipa: str, context: RescoreContext) -> Optional[str]:
        """The surface form of *ipa* in *context*, or ``None`` if no rule fires."""
        for rule in self.rules:
            if ipa in rule.phonemes and self._matches(rule, context):
                return rule.surface
        return None

    @staticmethod
    def _matches(rule: AllophoneRule, ctx: RescoreContext) -> bool:
        if rule.word_initial is not None and \
                rule.word_initial != ctx.is_word_initial:
            return False
        if rule.word_final is not None and \
                rule.word_final != ctx.is_word_final:
            return False
        if rule.stress is not None:
            stressed = ctx.is_stressed
            if stressed is None:  # no stress context (tokenizer path)
                return False
            if (rule.stress == "stressed") != bool(stressed):
                return False
        if rule.syllable_position is not None:
            if _syllable_position(ctx.grapheme) != rule.syllable_position:
                return False
        if rule.preceded_by is not None:
            if not _neighbor_is(rule.preceded_by, ctx.grapheme.prev):
                return False
        if rule.followed_by is not None:
            if not _neighbor_is(rule.followed_by, ctx.grapheme.next):
                return False
        if rule.preceded_by_phoneme:
            prev = ctx.prev_slot
            if prev is None or prev.top.ipa not in rule.preceded_by_phoneme:
                return False
        if rule.followed_by_phoneme:
            nxt = ctx.next_slot
            if nxt is None or nxt.top.ipa not in rule.followed_by_phoneme:
                return False
        return True


def compile_allophone_rescorer(
    rules: Sequence[AllophoneRule],
) -> Optional[AllophoneRescorer]:
    """Compile ``allophone_rules`` into a rescorer, or ``None`` if empty.

    ``None`` lets a caller treat "no rules" as "no post-lexical pass" with a
    plain truthiness check, keeping the default engine path byte-identical.
    """
    rules = tuple(rules or ())
    if not rules:
        return None
    return AllophoneRescorer(rules)
