"""Cited-claim tests for the Chichewa/Nyanja (``ny``) tone ceiling.

Chichewa is a two-tone Bantu language, and Downing & Mtenje (2017, *The
Phonology of Chichewa*, OUP, §2.1) state plainly that "tone is not
indicated in Chichewa orthography" — the spec's ``notes`` already record
this as deliberately unmodelled. This file measures what that costs
against the wikipron gold: the gold marks lexical high tone with a
combining acute accent that the plain spelling never carries, and folding
that mark out of both sides collapses part of the shipped PER. Unlike
Kikuyu (``ki``), whose gold marks tone on nearly every entry and folds to
a near-zero ceiling, only 45% of this gold's entries carry the mark, so
the fold here is real but partial — it does not by itself clear the
0.25 deep-orthography production threshold, and this file exists to keep
that partial, sourced measurement from silently drifting.
"""
from __future__ import annotations

import json
import pathlib
import sys
import unicodedata

DATA_DIR = (pathlib.Path(__file__).parent.parent
            / "orthography2ipa" / "data")

_TONE_MARKS = {"̀", "́", "̂", "̌"}  # grave, acute, circumflex, caron


def _fold_tone(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if c not in _TONE_MARKS)
    return unicodedata.normalize("NFC", s)


def _load_gold():
    sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "scripts"))
    import benchmark as bm
    return bm.load_wikipron("ny", 10 ** 9)


def test_notes_document_tone_as_deliberately_unmodelled():
    raw = json.loads((DATA_DIR / "ny.json").read_text(encoding="utf-8"))
    assert "not indicated in Chichewa orthography" in raw["notes"]
    ceiling = raw["valid_ceiling"]["wikipron"]
    assert ceiling["per"] == 0.2604
    assert "0.3119" in ceiling["citation"]
    assert "0.2604" in ceiling["citation"]


def test_identical_spelling_maps_to_more_than_one_gold_tone():
    """Direct evidence the plain orthography cannot disambiguate tone: the
    same wikipron headword recurs with different gold tone marking."""
    pairs = _load_gold()
    by_word: dict[str, set[str]] = {}
    for word, gold in pairs:
        by_word.setdefault(word, set()).add(gold.replace(" ", ""))

    ambiguous = {w: g for w, g in by_word.items() if len(g) > 1}
    # measured against the cached gold: 59/1564 unique spellings
    assert len(ambiguous) >= 50, (
        "expected the previously-measured ~59 tone-ambiguous homographs; "
        f"found {len(ambiguous)}"
    )


def test_tone_folded_scoring_narrows_the_gap():
    """Fold the acute tone mark out of both hypothesis and gold and rescore.

    This is the fail-before-sensitive claim: it exercises the shipped
    engine, not just the gold file, so a spec regression that broke
    segmental accuracy (as opposed to tone) would show up here even
    though tone is folded out.
    """
    sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "scripts"))
    import benchmark as bm

    pairs = _load_gold()
    orig_normalize = bm.normalize

    def folded_normalize(ipa, strip_stress, broad, extra_strip=""):
        out = orig_normalize(ipa, strip_stress, broad, extra_strip=extra_strip)
        return _fold_tone(out)

    try:
        bm.normalize = folded_normalize
        _, covered, per, _ = bm.evaluate(pairs, "ny", strip_stress=True,
                                          broad=True)
    finally:
        bm.normalize = orig_normalize

    assert covered == 1564
    # measured 0.2604; generous margin against harness float noise while
    # still failing hard if a future change reopens or widens the gap.
    assert per < 0.28, f"expected tone-folded PER near 0.2604, got {per:.4f}"


def test_no_vowel_length_mark_in_this_gold():
    """Negative result: this gold's broad transcription never writes the
    length mark, so there is nothing for a length fold to be measured
    against here (unlike the tone mark above)."""
    pairs = _load_gold()
    assert not any("ː" in g or "ˑ" in g for _, g in pairs)
