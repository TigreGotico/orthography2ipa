"""lattice_per — pronunciation-fair phoneme error rate against the lattice.

Scoring an ASR hypothesis (or any phone sequence) against a *single*
reference transcription punishes the model for every legitimate
pronunciation variant the reference happens not to use: optional sandhi
fired or not, dialectal allophone choices, cliticization variants. The
candidate lattice already encodes the set of pronunciations a speaker of
the lect could validly have produced for the reference text, so the fair
score is the **oracle edit distance** — the minimum, over all lattice
paths, of the segment-level edit distance to the hypothesis. A hypothesis
is only charged for segments that are wrong on *every* valid reading.

Two readings are always admissible:

1. every path through the sentence lattice
   (:meth:`~orthography2ipa.g2p.G2P.sentence_lattice` — each grapheme
   slot's ranked candidates, per word, pre-sandhi), and
2. the engine's final reading (:func:`~orthography2ipa.transcribe`),
   which includes cross-word sandhi and sentence rescorers that the raw
   lattice deliberately does not apply.

The oracle distance is the minimum over both, computed without path
enumeration: a Levenshtein frontier is pushed through the lattice slot by
slot (each slot contributes the elementwise-minimum frontier over its
candidates), which is the edit-distance transducer composed with the
acyclic lattice.

Costs are unit by default. With ``weighted=True`` substitutions cost the
articulatory feature distance between the two segments
(:func:`orthography2ipa.feats.phonetic_distance`, in ``[0, 1]``) instead
of ``1`` — a laminal/apical sibilant confusion then costs a fraction of a
stop/vowel confusion, turning PER into a graded phonological error rate.
Insertions and deletions stay at ``1``.

Normalization: PER = oracle distance / segment count of the engine's
final reading of the reference. The oracle *path* length is not tracked
(different paths have different lengths); the final reading is the single
deterministic denominator, stated here so scores are comparable across
runs.

Honesty caveat: the metric inherits the lect spec's correctness. A spec
that is too permissive makes every hypothesis look good; scoring against
a lect whose spec is thin under-reports errors. Report the lect and the
engine version next to any number.

Usage::

    >>> from orthography2ipa.lattice_per import lattice_per
    >>> r = lattice_per("es̻ pada", "ez bada", "eu")
    >>> r.distance, r.per          # sandhi reading is admissible
    (0.0, 0.0)
    >>> lattice_per("es baða", "ez bada", "eu").distance   # genuinely wrong segments
    2.0
"""
from __future__ import annotations

import unicodedata
from dataclasses import dataclass
from typing import List, Sequence, Tuple

from orthography2ipa.allophony import segment_ipa

#: Marks stripped before scoring: stress and syllable boundaries are
#: suprasegmental and ASR phone output rarely carries them consistently.
_STRIPPED = {"ˈ", "ˌ", ".", "‿", "|", "‖"}


def _segments(ipa: str) -> List[str]:
    """Phoneme-sized segments of *ipa*, NFC, stress/boundary marks and
    whitespace removed."""
    ipa = unicodedata.normalize("NFC", ipa)
    for mark in _STRIPPED:
        ipa = ipa.replace(mark, "")
    return [s for word in ipa.split() for s in segment_ipa(word)]


def _sub_cost_unit(a: str, b: str) -> float:
    return 0.0 if a == b else 1.0


#: Featural cost of a diacritic-only difference between two segments whose
#: base characters match — priced as a single binary feature flip.
_DIACRITIC_FLIP = 1.0 / 16.0


def _strip_marks(segment: str) -> str:
    return "".join(ch for ch in unicodedata.normalize("NFD", segment)
                   if not unicodedata.combining(ch))


def _sub_cost_featural(a: str, b: str) -> float:
    if a == b:
        return 0.0
    from orthography2ipa.feats import phonetic_distance
    d = phonetic_distance(a, b)
    if d > 1.0:
        # phonetic_distance exceeds 1 when a segment is outside its feature
        # table (e.g. the laminal/apical sibilant diacritics). Fall back to
        # the base characters and charge the diacritic difference as one
        # binary feature flip — s̻/s is then a near-match, not a full
        # substitution. A substitution must never cost more than a deletion
        # plus an insertion, so the result is clamped to unit either way.
        base_a = _strip_marks(a)
        base_b = _strip_marks(b)
        d = _DIACRITIC_FLIP if base_a == base_b else \
            phonetic_distance(base_a, base_b) + _DIACRITIC_FLIP
    return min(1.0, d)


def _advance(frontier: List[float], segment: str, hyp: Sequence[str],
             sub_cost) -> List[float]:
    """One Levenshtein row: extend every frontier state by *segment*."""
    out = [frontier[0] + 1.0]
    for j in range(1, len(hyp) + 1):
        out.append(min(
            frontier[j] + 1.0,                            # delete segment
            out[j - 1] + 1.0,                             # insert hyp[j-1]
            frontier[j - 1] + sub_cost(segment, hyp[j - 1]),
        ))
    return out


def _oracle_frontier(slot_candidates: Sequence[Sequence[str]],
                     hyp: Sequence[str], sub_cost) -> float:
    """Min edit distance from any concatenation of one candidate per slot
    (each candidate pre-segmented) to *hyp*."""
    frontier = [float(j) for j in range(len(hyp) + 1)]
    for candidates in slot_candidates:
        best = None
        for cand_segments in candidates:
            f = frontier
            for seg in cand_segments:
                f = _advance(f, seg, hyp, sub_cost)
            best = f if best is None else [min(a, b) for a, b in zip(best, f)]
        if best is not None:
            frontier = best
    return frontier[-1]


@dataclass(frozen=True)
class LatticePER:
    """Result of :func:`lattice_per`."""

    distance: float
    """Oracle edit distance: min over admissible readings (all lattice
    paths, plus the engine's final sandhi-applied reading)."""

    per: float
    """``distance / ref_segments`` — the headline phoneme error rate."""

    top_distance: float
    """Edit distance against the engine's final reading only — what a
    single-reference PER would have scored."""

    top_per: float
    """``top_distance / ref_segments``."""

    ref_segments: int
    """Segment count of the engine's final reading of the reference text
    (the denominator)."""

    hyp_segments: int
    """Segment count of the hypothesis after mark stripping."""

    lang: str
    """The lect the reference was scored under."""

    @property
    def variant_credit(self) -> float:
        """``top_per - per`` — error mass the single-reference score would
        have charged that some valid pronunciation variant explains. The
        pronunciation-unfairness of the naive metric on this pair."""
        return self.top_per - self.per


def lattice_per(hyp_ipa: str, ref_text: str, lang: str, *,
                weighted: bool = False,
                beam_width: int = 8) -> LatticePER:
    """Pronunciation-fair phoneme error rate of *hyp_ipa* against the
    pronunciations the *lang* lect admits for *ref_text*.

    Parameters:
        hyp_ipa: Hypothesis phone string (IPA; whitespace and stress
            marks are ignored). Typically ASR phone output, or the
            phonemized form of an ASR word hypothesis.
        ref_text: Reference **orthographic** text; its pronunciation
            lattice is built with the *lang* lect spec.
        lang: Lect code the reference is transcribed under.
        weighted: When true, substitution costs are articulatory feature
            distances in ``[0, 1]`` instead of ``1`` (insertions and
            deletions stay ``1``), yielding a graded phonological error
            rate.
        beam_width: Candidate beam per grapheme slot, as in
            :meth:`~orthography2ipa.g2p.G2P.sentence_lattice`.

    Returns:
        A :class:`LatticePER`. ``per`` is the headline figure;
        ``top_per`` is what naive single-reference PER would have said;
        ``variant_credit`` is the difference.
    """
    from orthography2ipa import G2P

    g2p = G2P(lang)
    top = g2p.transcribe(ref_text)
    top_segments = _segments(top)
    hyp = _segments(hyp_ipa)
    sub_cost = _sub_cost_featural if weighted else _sub_cost_unit

    # Reading 2: the final engine output (sandhi, sentence rescorers).
    f = [float(j) for j in range(len(hyp) + 1)]
    for seg in top_segments:
        f = _advance(f, seg, hyp, sub_cost)
    top_distance = f[-1]

    # Reading 1: every path through the pre-sandhi sentence lattice.
    lattice = g2p.sentence_lattice(ref_text, beam_width=beam_width)
    slot_candidates: List[List[List[str]]] = []
    for word in lattice:
        if not word.slots:
            # Lexicon override / unmapped word: its single reading is the
            # word's flattened IPA.
            slot_candidates.append([_segments(word.ipa)])
            continue
        for slot in word.slots:
            slot_candidates.append(
                [_segments(c.ipa) for c in slot.candidates])
    lattice_distance = _oracle_frontier(slot_candidates, hyp, sub_cost)

    distance = min(lattice_distance, top_distance)
    denom = max(len(top_segments), 1)
    return LatticePER(
        distance=distance,
        per=distance / denom,
        top_distance=top_distance,
        top_per=top_distance / denom,
        ref_segments=len(top_segments),
        hyp_segments=len(hyp),
        lang=g2p.lang,
    )
