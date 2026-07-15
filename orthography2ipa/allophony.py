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

import unicodedata
from dataclasses import dataclass
from typing import List, Optional, Sequence, Tuple

from orthography2ipa.phonetok import Candidate, GraphemeContext, SegmentSlot
from orthography2ipa.rescorer import LatticeRescorer, RescoreContext
from orthography2ipa.types import AllophoneRule
from orthography2ipa.vowels import is_ipa_vowel

__all__ = [
    "AllophoneRescorer",
    "compile_allophone_rescorer",
    "segment_ipa",
]


def _is_modifier(ch: str) -> bool:
    """Whether *ch* attaches to the preceding IPA base character.

    Combining marks (tense ◌͈, unreleased ◌̚, nasal ◌̃), modifier letters
    (ʰ ʲ ˠ ː) and modifier symbols never start a segment of their own.
    """
    return bool(unicodedata.combining(ch)) or \
        unicodedata.category(ch) in ("Lm", "Sk")


def segment_ipa(ipa: str, atoms: Sequence[str] = ()) -> List[str]:
    """Split an IPA candidate string into phoneme-sized segments.

    *atoms* — multi-character phonemes the caller cares about (affricates
    like ``tɕ``, rule targets/surfaces), tried longest-first so ``tɕʰ``
    is one segment, never ``t`` + ``ɕʰ``. Everything else groups as one
    base character plus its trailing modifiers. A single-phoneme string
    round-trips to itself, so single-segment slots behave exactly as the
    pre-segmentation rescorer did.
    """
    segments: List[str] = []
    i, n = 0, len(ipa)
    while i < n:
        seg = _match_atom(ipa, i, atoms)
        if seg is None:
            j = i + 1
            while j < n and _is_modifier(ipa[j]):
                j += 1
            seg = ipa[i:j]
        segments.append(seg)
        i += len(seg)
    return segments


def _match_atom(ipa: str, start: int, atoms: Sequence[str]) -> Optional[str]:
    """The longest *atom* starting at *start*, or ``None``.

    An atom only matches when not immediately followed by a modifier —
    ``k`` must not steal the base of ``k͈`` (tense) or ``kʰ`` (aspirated),
    which are different phonemes.
    """
    for atom in atoms:
        end = start + len(atom)
        if not ipa.startswith(atom, start):
            continue
        if end < len(ipa) and _is_modifier(ipa[end]):
            continue
        return atom
    return None


@dataclass(frozen=True)
class SegmentContext:
    """One segment's phonological neighbourhood inside a word.

    Neighbours look across slot boundaries: the segment before the first
    segment of a slot is the LAST segment of the previous slot's top
    candidate (and symmetrically after the last). ``None`` = word edge.
    """
    prev: Optional[str]
    next: Optional[str]
    is_word_initial: bool
    is_word_final: bool


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


#: Nasal consonants, by IPA. A vowel nasalises before one of these in coda;
#: the class is decided by the neighbour's IPA, never by the language.
_NASALS = frozenset("mnɲŋɳɴ")


def _begins_consonant_cluster(gctx: GraphemeContext, step: int) -> bool:
    """Whether *gctx* starts a consonant cluster, reading in *step* direction.

    A cluster is two or more consonant segments in a row, counted away from
    the anchor (``step`` is ``+1`` for a following neighbour, ``-1`` for a
    preceding one). Three ways to qualify, all decided phonemically:

    * the neighbour realises a long/geminate consonant (``tː``) — moraic on
      its own;
    * the neighbour is a single grapheme spelling several consonants (⟨x⟩
      → /ks/);
    * the grapheme beyond it is also a consonant (⟨s⟩⟨t⟩).

    This is what closed-syllable shortening and complementary quantity need
    (Riad 2014; Kristoffersen 2000; Basbøll 2005), and it is stated over
    phonological classes only — no language, script or code is consulted.
    """
    if not gctx.is_consonant:
        return False
    ipa = gctx.ipa[0] if gctx.ipa else ""
    if "ː" in ipa:
        return True
    if len([s for s in segment_ipa(ipa) if not is_ipa_vowel(s[0])]) >= 2:
        return True
    beyond = gctx.at(step)
    return beyond is not None and beyond.is_consonant


def _neighbor_is(
        cls: str,
        gctx: Optional[GraphemeContext],
        step: int = 1,
) -> bool:
    """Whether neighbour grapheme *gctx* matches the neighbour class *cls*.

    *step* is the direction the neighbour lies in (``+1`` = the grapheme
    after the anchor, ``-1`` = the one before); only the direction-sensitive
    classes read it.
    """
    if cls == "word_boundary":
        return gctx is None
    if gctx is None:
        return False
    if cls == "vowel":
        return gctx.is_vowel
    if cls == "consonant":
        return gctx.is_consonant
    if cls == "consonant_cluster":
        return _begins_consonant_cluster(gctx, step)
    if cls == "coda":
        return _syllable_position(gctx) == "coda"
    if cls == "coda_nasal":
        if _syllable_position(gctx) != "coda":
            return False
        ipa = gctx.ipa[0] if gctx.ipa else ""
        return bool(ipa) and ipa[0] in _NASALS
    if cls == "front_vowel":
        return gctx.is_front
    if cls == "back_vowel":
        return gctx.is_back
    if cls == "palatal":
        return gctx.is_palatal
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

    __slots__ = ("rules", "_atoms")

    def __init__(self, rules: Sequence[AllophoneRule]) -> None:
        self.rules = tuple(rules)
        self._atoms = _rule_atoms(self.rules)

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

    def _is_geminate_half(self, ipa: str, context: RescoreContext) -> bool:
        """Whether this slot is one half of a written (doubled) geminate.

        A geminate is a single long consonant that the input spells — and the
        tokenizer's shadda expansion realises — as two identical, contiguous,
        same-grapheme slots. The twin is an immediately adjacent slot whose
        source grapheme is the same (case-insensitively), whose span abuts this
        slot's, and whose pre-rescorer top candidate is the same consonant
        *ipa*. Read from the slot layer, so the comparison is on underlying
        phonemes, before any rewrite.

        The doubled phoneme must be a **bare consonant** — no vowel in it. A
        true written geminate is a doubled consonant with no vowel between its
        halves (Arabic shadda expansion gives two bare ⟨ق⟩ /ɡ/ slots). Two
        adjacent identical CV units of an abugida (Tamil ⟨கக⟩ = /kaka/, each
        slot carrying its inherent /a/) are two syllables, not a geminate, and
        must not be swept up — so a slot whose phoneme contains a vowel is
        never a geminate half.
        """
        if not ipa or any(is_ipa_vowel(seg[0]) for seg in segment_ipa(ipa)):
            return False
        own_g = (context.grapheme.grapheme or "").lower()
        for step in (1, -1):
            j = context.index + step
            neighbour = context.slots[j] if 0 <= j < len(context.slots) else None
            g_neighbour = context.grapheme.at(step)
            if neighbour is None or g_neighbour is None:
                continue
            if not neighbour.candidates or neighbour.top.ipa != ipa:
                continue
            if own_g != (g_neighbour.grapheme or "").lower():
                continue
            near, far = context.slot.span, neighbour.span
            if near[1] == far[0] or far[1] == near[0]:  # contiguous
                return True
        return False

    def _realize(self, ipa: str, context: RescoreContext) -> Optional[str]:
        """The surface form of *ipa* in *context*, or ``None`` if no rule fires.

        Two passes. The whole-candidate pass is the original semantics —
        a single-phoneme slot equal to a rule target — and stays first so
        every existing single-segment spec is byte-identical. The segment
        pass then serves slots whose one candidate carries SEVERAL
        phonemes (a Hangul syllable block, an abugida consonant with its
        inherent vowel): each segment is matched and rewritten in place,
        with neighbour context read across slot boundaries.
        """
        is_geminate = self._is_geminate_half(ipa, context)
        for rule in self.rules:
            if ipa in rule.phonemes and self._matches(rule, context):
                if is_geminate and not _is_geminate_aware(rule, ipa):
                    # A geminate is one long segment: a rule triggered purely
                    # by material OUTSIDE it must not rewrite a single half and
                    # split the unit into a heterorganic cluster (Najdi
                    # affrication does not apply to geminates — Ingham 1994,
                    # Alhoody 2020). Only a rule conditioned on the twin itself
                    # (a genuine gemination process, e.g. Tamil ⟨க்க⟩→[kː]) may.
                    continue
                return rule.surface
        segments = segment_ipa(ipa, self._atoms)
        if len(segments) <= 1:
            return None
        return self._realize_segments(segments, context)

    def _realize_segments(
        self, segments: List[str], context: RescoreContext,
    ) -> Optional[str]:
        """Apply the first matching rule to each segment; ``None`` = no-op."""
        changed = False
        out: List[str] = []
        for i, seg in enumerate(segments):
            seg_ctx = _segment_context(segments, i, context, self._atoms)
            surface = self._realize_one_segment(seg, seg_ctx, context)
            if surface is not None and surface != seg:
                changed = True
                out.append(surface)
            else:
                out.append(seg)
        return "".join(out) if changed else None

    def _realize_one_segment(
        self, seg: str, seg_ctx: SegmentContext, context: RescoreContext,
    ) -> Optional[str]:
        for rule in self.rules:
            if _is_segmental(rule) \
                    and seg in rule.phonemes \
                    and _matches_segment(rule, seg_ctx) \
                    and self._matches_slot(rule, context):
                return rule.surface
        return None

    def _matches(self, rule: AllophoneRule, ctx: RescoreContext) -> bool:
        """Whole-candidate match: word flags + slot neighbours + slot flags.

        Slot neighbours match on the ADJACENT boundary segment — the last
        segment of the previous slot's top candidate and the first segment
        of the next slot's — never the whole candidate string. A rule with
        ``followed_by_phoneme=("ʂ",)`` must fire before a slot realised as
        ``ʂɨ`` (the assimilation trigger is the adjacent consonant, not the
        vowel behind it); for single-phoneme neighbours the boundary
        segment IS the whole candidate, so those keep the original
        semantics unchanged.
        """
        if rule.word_initial is not None and \
                rule.word_initial != ctx.is_word_initial:
            return False
        if rule.word_final is not None and \
                rule.word_final != ctx.is_word_final:
            return False
        if rule.preceded_by_phoneme:
            prev = ctx.prev_slot
            if prev is None or not prev.top.ipa:
                return False
            boundary = segment_ipa(prev.top.ipa, self._atoms)[-1]
            if boundary not in rule.preceded_by_phoneme:
                return False
        if rule.followed_by_phoneme:
            nxt = ctx.next_slot
            if nxt is None or not nxt.top.ipa:
                return False
            boundary = segment_ipa(nxt.top.ipa, self._atoms)[0]
            if boundary not in rule.followed_by_phoneme:
                return False
        return self._matches_slot(rule, ctx)

    def _matches_slot(self, rule: AllophoneRule, ctx: RescoreContext) -> bool:
        """The conditions that describe the SLOT, not one of its segments:
        stress, syllable position, and grapheme-class neighbours."""
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
            if not _neighbor_is(rule.preceded_by, ctx.grapheme.prev, -1):
                return False
        if rule.followed_by is not None:
            if not _neighbor_is(rule.followed_by, ctx.grapheme.next, 1):
                return False
        if rule.preceded_by_phoneme_2 or rule.followed_by_phoneme_2:
            # The grapheme TWO away, by its first IPA candidate. Read from the
            # grapheme layer (not the slot), so it is the underlying phoneme —
            # which is the point: ⟨с⟩ of ⟨гости⟩ palatalises because the ⟨т⟩
            # after it stands before a soft vowel, and that is knowable before
            # any rule has rewritten the ⟨т⟩.
            def _phoneme_at(step: int) -> Optional[str]:
                g = ctx.grapheme.at(step)
                if g is None or not g.ipa or not g.ipa[0]:
                    return None
                return segment_ipa(g.ipa[0], self._atoms)[0]
            if rule.preceded_by_phoneme_2:
                p2 = _phoneme_at(-2)
                if p2 is None or p2 not in rule.preceded_by_phoneme_2:
                    return False
            if rule.followed_by_phoneme_2:
                n2 = _phoneme_at(2)
                if n2 is None or n2 not in rule.followed_by_phoneme_2:
                    return False
        if rule.preceded_by_2 is not None:
            if not _neighbor_is(rule.preceded_by_2, ctx.grapheme.at(-2), -1):
                return False
        if rule.followed_by_2 is not None:
            if not _neighbor_is(rule.followed_by_2, ctx.grapheme.at(2), 1):
                return False
        if rule.grapheme is not None:
            g = ctx.grapheme.grapheme
            if not g or g.lower() not in rule.grapheme:
                return False
        return True


def _is_geminate_aware(rule: AllophoneRule, ipa: str) -> bool:
    """Whether *rule* is conditioned on a geminate twin of *ipa*.

    A gemination process references the doubled phoneme in its own phoneme
    neighbourhood: Tamil's paired ``TA_GEM1``/``TA_GEM2`` fire the first half
    ``followed_by_phoneme`` its twin and the second ``preceded_by_phoneme``
    its twin, so they realise ⟨க்க⟩ as the coordinated [kː]. Such a rule is
    *about* the geminate and may rewrite a half. A rule whose neighbour
    context does not mention the twin fired on external material and would
    split the geminate, so :meth:`AllophoneRescorer._realize` blocks it on a
    geminate half. The twin is matched either as the bare phoneme (``k``) or
    as that phoneme carrying a following vowel (``ka``) — the shape the other
    half takes once its own inherent vowel is attached.
    """
    for ctx in (rule.preceded_by_phoneme, rule.followed_by_phoneme):
        if any(n == ipa or n.startswith(ipa) for n in ctx):
            return True
    return False


def _is_segmental(rule: AllophoneRule) -> bool:
    """Whether *rule* may fire on a segment INSIDE a multi-phoneme slot.

    Only rules that declare phoneme-neighbour context
    (``preceded_by_phoneme``/``followed_by_phoneme``) qualify. A rule
    without one was written under whole-slot semantics, where its target
    matched the slot's ENTIRE candidate — the spec's own phoneme unit. A
    diphthong slot like ``ow`` segments into ``o``+``w``, but it is one
    phoneme to its spec, and a neighbour-less ``[o] → [wo]``
    diphthongisation rule must not fire on the ``o`` inside it. A rule
    that states its segment adjacency, by contrast, is asking for exactly
    this granularity.
    """
    return bool(rule.preceded_by_phoneme or rule.followed_by_phoneme)


def _matches_segment(rule: AllophoneRule, seg_ctx: SegmentContext) -> bool:
    """The conditions that describe ONE SEGMENT of a multi-phoneme slot:
    word-edge flags and phoneme neighbours, read at segment granularity."""
    if rule.word_initial is not None and \
            rule.word_initial != seg_ctx.is_word_initial:
        return False
    if rule.word_final is not None and \
            rule.word_final != seg_ctx.is_word_final:
        return False
    if rule.preceded_by_phoneme:
        if seg_ctx.prev is None or \
                seg_ctx.prev not in rule.preceded_by_phoneme:
            return False
    if rule.followed_by_phoneme:
        if seg_ctx.next is None or \
                seg_ctx.next not in rule.followed_by_phoneme:
            return False
    return True


def _segment_context(
    segments: List[str], index: int,
    ctx: RescoreContext, atoms: Sequence[str],
) -> SegmentContext:
    """Build one segment's :class:`SegmentContext` within its word.

    Neighbours fall back across slot boundaries to the ADJACENT SLOT's
    top candidate (its last segment on the left, first on the right), so
    an intervocalic rule sees 바+다 the same way it would see a single
    slot carrying ``pata``.
    """
    if index > 0:
        prev = segments[index - 1]
    elif ctx.prev_slot is not None:
        prev_segs = segment_ipa(ctx.prev_slot.top.ipa, atoms)
        prev = prev_segs[-1] if prev_segs else None
    else:
        prev = None
    if index < len(segments) - 1:
        nxt = segments[index + 1]
    elif ctx.next_slot is not None:
        next_segs = segment_ipa(ctx.next_slot.top.ipa, atoms)
        nxt = next_segs[0] if next_segs else None
    else:
        nxt = None
    return SegmentContext(
        prev=prev, next=nxt,
        is_word_initial=ctx.is_word_initial and index == 0,
        is_word_final=ctx.is_word_final and index == len(segments) - 1,
    )


def _rule_atoms(rules: Sequence[AllophoneRule]) -> Tuple[str, ...]:
    """Every multi-character phoneme the rules mention, longest first.

    These are the segmentation atoms: a rule about ``tɕ`` must see ``tɕ``
    as one segment, never ``t`` + ``ɕ``. Single characters segment
    naturally and need no atom entry.
    """
    atoms = set()
    for rule in rules:
        atoms.update(rule.phonemes or ())
        atoms.update(rule.preceded_by_phoneme or ())
        atoms.update(rule.followed_by_phoneme or ())
        if rule.surface:
            atoms.add(rule.surface)
    return tuple(sorted((a for a in atoms if len(a) > 1),
                        key=len, reverse=True))


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
