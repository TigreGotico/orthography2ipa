"""positional — Shared positional grapheme→IPA resolution.

The engine (:mod:`orthography2ipa.g2p`) and the standalone tokenizer
beam (:mod:`orthography2ipa.phonetok`) must agree, per word, on which
IPA candidate a grapheme takes in context. Both consult a spec's
``positional_graphemes`` overrides (context-sensitive grapheme→IPA
mappings, including the vowel-class positions from the
``GraphemePosition`` redesign). This module is the **single** home for
that resolution so the two beams cannot drift apart.

Three concerns live here:

1. :func:`grapheme_positions` — given a grapheme's context (a
   :class:`~orthography2ipa.phonetok.GraphemeContext`, duck-typed: it
   only needs ``grapheme``/``prev``/``next``/``is_vowel``/``is_front``/
   ``is_back``/``is_palatal``), return the ordered list of :class:`GraphemePosition`
   values to try, **most specific first**. Exact-letter positions
   (``BEFORE_E``) precede their vowel *class* (``BEFORE_FRONT_VOWEL``),
   which precede the generic (``BEFORE_VOWEL``) and finally
   ``DEFAULT`` — this ordering is the exact>class>default precedence.

2. :func:`positional_candidates` — consult ``spec.positional_graphemes``
   for a grapheme with a pre-computed position list, returning the first
   matching position's candidates (or ``None`` when the grapheme has no
   positional override at all, so the caller falls back to the flat
   ``graphemes`` table where per-candidate weights apply).

3. :func:`build_branches` / :func:`resolve_branches` — turn candidates
   into ``(ipa, cost)`` beam branches (weights → ``-log p`` cost,
   allophone expansion, dedup), and the top-level
   :func:`resolve_branches` that wires 1→2→3 together for one grapheme
   context. Both beams call :func:`resolve_branches`.

Stress/syllable-conditioned positions (``NUCLEUS_STRESSED`` etc.) need
sentence-level stress detection that only the engine computes; callers
pass ``syll_idx``/``stressed_syll_idx`` when they have them and ``None``
otherwise. With ``stressed_syll_idx is None`` the stress-conditioned
positions are simply omitted — which is why the standalone tokenizer
(no stress context) still agrees with the engine on every
non-stress-conditioned position.
"""
from __future__ import annotations

from typing import Callable, Dict, List, Optional, Sequence, Tuple

from orthography2ipa.types import GraphemePosition, LanguageSpec
from orthography2ipa.vowels import (
    base_vowel_letter,
    is_back_vowel,
    is_front_vowel,
    is_ipa_vowel,
)
from orthography2ipa.weights import candidate_base_costs

__all__ = [
    "grapheme_positions",
    "positional_candidates",
    "build_branches",
    "resolve_branches",
]


def _carries_nucleus(ctx) -> bool:
    """True when a non-vowel grapheme's primary IPA candidate contains a
    vowel — a CV unit (Cyrillic ⟨дя⟩ → dʲa, soft-consonant + nucleus)
    whose realisation is stress-conditioned like a plain vowel letter's.
    Reads the flat-table candidates (``ctx.ipa``), never a positional
    result, so the answer cannot be circular."""
    primary = next(iter(getattr(ctx, "ipa", ()) or ()), "")
    return any(is_ipa_vowel(ch) for ch in primary)

# Map an exact next/prev vowel letter to its BEFORE_*/AFTER_* position.
_BEFORE_EXACT: Dict[str, GraphemePosition] = {
    "a": GraphemePosition.BEFORE_A,
    "e": GraphemePosition.BEFORE_E,
    "i": GraphemePosition.BEFORE_I,
    "o": GraphemePosition.BEFORE_O,
    "u": GraphemePosition.BEFORE_U,
    # Cyrillic plain vowel letters map onto the same exact-letter axes so
    # positional keys like before_o work for Cyrillic-script specs
    # (Ukrainian ⟨в⟩ → [w] before rounded vowels). The iotated letters
    # (е ё ю я) are deliberately absent: they open with a glide, which is
    # the neighbour that matters.
    "а": GraphemePosition.BEFORE_A,
    "э": GraphemePosition.BEFORE_E,
    "и": GraphemePosition.BEFORE_I,
    "і": GraphemePosition.BEFORE_I,
    "о": GraphemePosition.BEFORE_O,
    "у": GraphemePosition.BEFORE_U,
}
_AFTER_EXACT: Dict[str, GraphemePosition] = {
    "a": GraphemePosition.AFTER_A,
    "e": GraphemePosition.AFTER_E,
    "i": GraphemePosition.AFTER_I,
    "o": GraphemePosition.AFTER_O,
    "u": GraphemePosition.AFTER_U,
}


def grapheme_positions(
    ctx,
    *,
    syll_idx: Optional[int] = None,
    stressed_syll_idx: Optional[int] = None,
) -> List[GraphemePosition]:
    """Ordered positions to try for the grapheme wrapped by *ctx*.

    Most-specific first, so a caller consulting ``positional_graphemes``
    in this order gets exact>class>default precedence for free.

    *ctx* is any object exposing ``grapheme``, ``prev``/``next`` (each a
    context or ``None``) and ``is_vowel``/``is_front``/``is_back``/
    ``is_palatal`` predicates — i.e. a
    :class:`~orthography2ipa.phonetok.GraphemeContext`. Neighbours are
    word-local for the standalone tokenizer and word-flat for the engine
    (which strips punctuation before this stage); either way ``prev is
    None`` marks the word-initial grapheme and ``next is None`` the
    word-final one.

    ``syll_idx``/``stressed_syll_idx`` add the stress-conditioned
    nucleus positions; when ``stressed_syll_idx is None`` (no stress
    context, e.g. the standalone tokenizer) those are omitted.
    """
    pos: List[GraphemePosition] = []
    grapheme = ctx.grapheme
    is_vowel = ctx.is_vowel
    prev_ctx = ctx.prev
    next_ctx = ctx.next
    prev_is_v = prev_ctx is not None and prev_ctx.is_vowel
    next_is_v = next_ctx is not None and next_ctx.is_vowel

    # 1. before_X (exact letter) then the front/back vowel *class*.
    if next_ctx is not None:
        nc = base_vowel_letter(next_ctx.grapheme[0])
        exact = _BEFORE_EXACT.get(nc)
        if exact is not None:
            pos.append(exact)
        if next_ctx.is_front:
            pos.append(GraphemePosition.BEFORE_FRONT_VOWEL)
        elif next_ctx.is_back:
            pos.append(GraphemePosition.BEFORE_BACK_VOWEL)
        # Palatal is a consonant class (decided by the neighbour's IPA), so it
        # never collides with the front/back vowel classes above; it sits at
        # the same class tier — after any exact-letter position, before the
        # generic BEFORE_CONSONANT and DEFAULT.
        if next_ctx.is_palatal:
            pos.append(GraphemePosition.BEFORE_PALATAL)

    # 2. word boundary
    if prev_ctx is None:
        pos.append(GraphemePosition.WORD_INITIAL)
    if next_ctx is None:
        pos.append(GraphemePosition.WORD_FINAL)

    # 3. intervocalic (consonants between two vowels)
    if prev_is_v and next_is_v:
        pos.append(GraphemePosition.INTERVOCALIC)

    # 4. nucleus_stressed / nucleus_unstressed for graphemes carrying a
    # nucleus. Besides plain vowel letters this covers CV units whose IPA
    # contains a vowel — e.g. the Cyrillic iotated-vowel digraphs (⟨дя⟩ →
    # dʲa) — whose reduction is conditioned on the same stress geometry.
    # Emitting the extra positions is inert unless the spec defines them
    # for that grapheme, so vowel-less digraphs are unaffected.
    if stressed_syll_idx is not None and syll_idx is not None and (
            is_vowel or _carries_nucleus(ctx)):
        if syll_idx == stressed_syll_idx:
            pos.append(GraphemePosition.NUCLEUS_STRESSED)
        else:
            pos.append(GraphemePosition.NUCLEUS_UNSTRESSED)
            if syll_idx < stressed_syll_idx:
                if syll_idx == stressed_syll_idx - 1:
                    pos.append(GraphemePosition.FIRST_PRETONIC)
                pos.append(GraphemePosition.PRETONIC)
            else:
                pos.append(GraphemePosition.POSTTONIC)

    # 5. after/before vowel / consonant context
    if prev_is_v:
        pc = base_vowel_letter(prev_ctx.grapheme[0])
        exact = _AFTER_EXACT.get(pc)
        if exact is not None:
            pos.append(exact)
        if prev_ctx.is_front:
            pos.append(GraphemePosition.AFTER_FRONT_VOWEL)
        elif prev_ctx.is_back:
            pos.append(GraphemePosition.AFTER_BACK_VOWEL)
        # Palatal is decided by the neighbour's IPA, so a vowel *letter*
        # realised as a palatal glide (⟨i⟩/⟨y⟩ → /j/) is palatal too — mirror
        # the unconditional BEFORE_PALATAL emission so the two sides agree.
        if prev_ctx.is_palatal:
            pos.append(GraphemePosition.AFTER_PALATAL)
        pos.append(GraphemePosition.AFTER_VOWEL)
    elif prev_ctx is not None:
        # Preceding grapheme is a consonant: the palatal class (decided by
        # its IPA) is more specific than the generic AFTER_CONSONANT.
        if prev_ctx.is_palatal:
            pos.append(GraphemePosition.AFTER_PALATAL)
        pos.append(GraphemePosition.AFTER_CONSONANT)
    if next_is_v:
        pos.append(GraphemePosition.BEFORE_VOWEL)
    elif next_ctx is not None:
        pos.append(GraphemePosition.BEFORE_CONSONANT)

    # 6. nucleus fallback for vowels
    if is_vowel:
        pos.append(GraphemePosition.NUCLEUS)

    pos.append(GraphemePosition.DEFAULT)
    return pos


def positional_candidates(
    spec: LanguageSpec,
    grapheme: str,
    positions: Sequence[GraphemePosition],
) -> Optional[List[str]]:
    """First positional override matching *grapheme* over *positions*.

    Returns ``None`` when the grapheme has no ``positional_graphemes``
    entry at all (caller falls back to the flat table), or when it has an
    entry but none of *positions* is declared for it.
    """
    pg = spec.positional_graphemes.get(grapheme)
    if not pg:
        return None
    for position in positions:
        if position in pg:
            return pg[position]
    return None


def build_branches(
    candidates: Sequence[str],
    weights: Optional[Sequence[float]],
    allophone_map: Optional[Dict[str, List[str]]],
    grapheme: str,
) -> List[Tuple[str, float]]:
    """Turn ordered *candidates* into deduped ``(ipa, cost)`` beam branches.

    ``weights`` (or ``None``) feed
    :func:`~orthography2ipa.weights.candidate_base_costs` — ``None`` gives
    the uniform-descending rank cost, byte-identical to the pre-weights
    behaviour. When *allophone_map* is given each phoneme further branches
    into its allophonic variants at ``+0.5`` per rank beyond the first.
    Duplicate IPA strings collapse to their lowest cost; the result is
    sorted ``(cost, ipa)``.
    """
    costs = candidate_base_costs(candidates, weights, grapheme=grapheme)
    branches: List[Tuple[str, float]] = []
    for rank, phoneme in enumerate(candidates):
        base_cost = costs[rank]
        if allophone_map and phoneme in allophone_map:
            for a_rank, allophone in enumerate(allophone_map[phoneme]):
                branches.append((allophone, base_cost + 0.5 * a_rank))
        else:
            branches.append((phoneme, base_cost))
    seen: Dict[str, float] = {}
    for ipa, cost in branches:
        if ipa not in seen or cost < seen[ipa]:
            seen[ipa] = cost
    return sorted(seen.items(), key=lambda x: (x[1], x[0]))


def resolve_branches(
    spec: LanguageSpec,
    ctx,
    *,
    weights_for: Callable[[str], Optional[Sequence[float]]],
    allophone_map: Optional[Dict[str, List[str]]] = None,
    syll_idx: Optional[int] = None,
    stressed_syll_idx: Optional[int] = None,
) -> List[Tuple[str, float]]:
    """The full per-grapheme branch resolution both beams share.

    Consults ``positional_graphemes`` in most-specific-first order; when a
    positional override fires its candidates are ranked first and the flat
    table's remaining candidates are appended (so the beam space is
    preserved). When no override fires the flat table is used with its
    per-candidate weights.

    Parameters
    ----------
    spec
        The language spec.
    ctx
        The grapheme's :class:`~orthography2ipa.phonetok.GraphemeContext`.
        Its ``ipa`` tuple is the flat-table base candidate list.
    weights_for
        Callable mapping a grapheme string to its per-candidate weights or
        ``None`` (typically ``PhonetokTokenizer.weights_for``).
    allophone_map
        Optional phoneme→allophones map for allophone expansion.
    syll_idx, stressed_syll_idx
        Stress context for nucleus positions; ``None`` when unavailable.
    """
    grapheme = ctx.grapheme
    base_candidates = list(ctx.ipa)

    positions = grapheme_positions(
        ctx, syll_idx=syll_idx, stressed_syll_idx=stressed_syll_idx)
    pos_candidates = positional_candidates(spec, grapheme, positions)

    if pos_candidates is None:
        # Flat table: per-candidate weights (if any) apply.
        candidates = base_candidates
        weights = weights_for(grapheme)
    else:
        # Positional winner first, then flat alternatives not already
        # covered. Positional overrides carry their own ordering; flat
        # weights do not apply to them.
        seen = set(pos_candidates)
        extra = [c for c in base_candidates if c not in seen]
        candidates = list(pos_candidates) + extra
        weights = None

    return build_branches(candidates, weights, allophone_map, grapheme)
