"""Per-spec candidate weights → probabilistic beam costs.

This module is the single, shared home for two concerns that would
otherwise be duplicated between :mod:`orthography2ipa.phonetok` (the
standalone tokenizer beam) and :mod:`orthography2ipa.g2p` (the full
engine's positional beam):

1. **Normalisation** of the two accepted JSON shapes for a grapheme's
   value into one internal representation (:func:`normalize_grapheme_value`
   / :func:`split_weighted_graphemes`).
2. **Cost derivation** for beam branches (:func:`candidate_base_costs`):
   the mapping from a candidate's rank/weight to the additive beam cost
   used by ``_expand_beam``.

The two JSON shapes
───────────────────
A grapheme's value in a language spec may be either

* the **plain list** form (today's shape)::

      "c": ["k", "s"]

* the **weighted object** form::

      "c": {"ipa": ["k", "s"], "weights": [0.9, 0.1]}

:func:`normalize_grapheme_value` collapses both to
``(ipa_list, weights_or_None)``. The plain list yields
``weights=None``, which :func:`candidate_base_costs` renders as the
*uniform-descending rank* cost (candidate[0] → 0.0, candidate[1] → 1.0,
…) — i.e. byte-identical to the behaviour that predates weights. No
existing spec (all plain lists) changes any score.

Cost ↔ weight
─────────────
When weights are present, a candidate's beam cost is ``-log(p)`` where
``p`` is that candidate's weight normalised over the entry's weight sum
(the weights become a probability distribution). Lower weight → higher
cost → later in the beam. Because cost is additive over a word's
graphemes, ``-log`` makes a path's total cost the negative log of the
product of its candidate probabilities — a proper (unnormalised)
sequence log-probability, which is what turns the rank-sum beam into a
probabilistic lattice.

Malformed weights (documented rule)
───────────────────────────────────
Weights are validated *defensively*; any of the following makes the
whole entry fall back to plain rank behaviour (with a warning), so a bad
weight can never crash transcription or silently drop a candidate:

* ``weights`` length ≠ ``ipa`` length,
* any weight is negative or non-numeric,
* the weight sum is ``0`` (no usable distribution).

A single **zero** weight (with a positive sum elsewhere) is *kept*: its
probability is floored to :data:`WEIGHT_FLOOR` so its cost is large but
finite — the candidate is strongly disfavoured yet still reachable,
never dropped from the beam.
"""
from __future__ import annotations

import math
import warnings
from typing import Dict, List, Optional, Sequence, Tuple

__all__ = [
    "WEIGHT_FLOOR",
    "normalize_grapheme_value",
    "split_weighted_graphemes",
    "candidate_base_costs",
]

# Probability floor for a zero (or vanishing) weight so ``-log(p)`` stays
# finite. Chosen well below any plausible real candidate frequency.
WEIGHT_FLOOR: float = 1e-6


def normalize_grapheme_value(
    value: object,
) -> Tuple[List[str], Optional[List[float]]]:
    """Normalise one grapheme's JSON value to ``(ipa, weights_or_None)``.

    Accepts either the plain-list form ``["k", "s"]`` (→ ``weights`` is
    ``None``) or the weighted-object form
    ``{"ipa": ["k", "s"], "weights": [0.9, 0.1]}`` (→ ``weights`` is the
    list). The returned ``ipa`` is always a plain ``list[str]`` so the
    rest of the package can keep treating ``spec.graphemes`` values as
    plain lists.

    A ``None`` value (used by the inheritance layer to null a grapheme)
    is passed through unchanged as ``(None, None)`` so callers can honour
    the existing "explicitly nulled" semantics.
    """
    if value is None:
        return None, None  # type: ignore[return-value]
    if isinstance(value, dict):
        ipa = list(value.get("ipa", []))
        raw_weights = value.get("weights")
        weights = list(raw_weights) if raw_weights is not None else None
        return ipa, weights
    # Plain list (or any other sequence of strings) → no weights.
    return list(value), None  # type: ignore[arg-type]


def split_weighted_graphemes(
    raw_graphemes: Dict[str, object],
) -> Tuple[Dict[str, List[str]], Dict[str, List[float]]]:
    """Split a raw grapheme table into parallel ``(graphemes, weights)`` dicts.

    ``graphemes`` maps each key to its plain IPA list (the shape every
    existing consumer expects); ``weights`` contains an entry **only** for
    keys whose JSON used the weighted-object form, mapping the key to its
    weight list. Keys without weights are simply absent from ``weights``
    (equivalent to rank behaviour), keeping the weight table sparse.

    ``None`` grapheme values (inheritance nulls) are preserved in
    ``graphemes`` so downstream ``__post_init__`` filtering still works.
    """
    graphemes: Dict[str, List[str]] = {}
    weights: Dict[str, List[float]] = {}
    for key, value in raw_graphemes.items():
        ipa, w = normalize_grapheme_value(value)
        graphemes[key] = ipa
        if w is not None:
            weights[key] = w
    return graphemes, weights


def _valid_weights(weights: Optional[Sequence[float]], n: int) -> bool:
    """Return ``True`` when *weights* is a usable distribution for *n* candidates."""
    if not weights:
        return False
    if len(weights) != n:
        return False
    total = 0.0
    for w in weights:
        if not isinstance(w, (int, float)) or isinstance(w, bool):
            return False
        if w < 0:
            return False
        total += w
    return total > 0.0


def candidate_base_costs(
    ipa: Sequence[str],
    weights: Optional[Sequence[float]] = None,
    *,
    grapheme: str = "",
) -> List[float]:
    """Return the additive beam cost for each candidate in *ipa*.

    With ``weights is None`` (or malformed weights) the result is the
    *rank* cost ``[0.0, 1.0, 2.0, …]`` — byte-identical to the behaviour
    that predates candidate weights, so plain-list specs never change.

    With valid weights the result is ``[-log(p_i), …]`` where ``p_i`` is
    candidate *i*'s weight normalised over the weight sum, with a
    :data:`WEIGHT_FLOOR` applied so a zero weight stays finite.

    Parameters
    ----------
    ipa
        The candidate IPA strings, in declared order.
    weights
        Optional per-candidate weights (candidate frequencies). ``None``
        for plain-list graphemes.
    grapheme
        Only used to make a malformed-weights warning actionable.
    """
    n = len(ipa)
    if not _valid_weights(weights, n):
        if weights:
            warnings.warn(
                f"ignoring malformed weights for grapheme {grapheme!r}: "
                f"expected {n} non-negative weights summing to >0, "
                f"got {list(weights)!r}; falling back to rank ordering",
                stacklevel=2,
            )
        return [float(rank) for rank in range(n)]

    total = float(sum(weights))  # type: ignore[arg-type]
    costs: List[float] = []
    for w in weights:  # type: ignore[union-attr]
        p = max(w / total, WEIGHT_FLOOR)
        costs.append(-math.log(p))
    return costs
