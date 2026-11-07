"""Cited-claim tests for ``nup`` — Nupe, a Nupoid (Volta-Niger,
Atlantic-Congo) language of Niger and Kwara States, central Nigeria.

Nupe is tonal (three level tones plus falling and rising contours), and
the modern Latin orthography this spec transcribes routinely omits tone
diacritics in running text. The spec transcribes segments only. This file
establishes, from the shipped wikipron/nup gold itself, that tone really
is unrecoverable from the plain spelling for a measured share of the
gold, and records the honest floor once tone is folded out of both sides
-- the same convention used for the zom/Zou tone ceiling.

The board's headline PER for nup/wikipron (0.3979) is flattered: WikiPron
scrapes Wiktionary headwords, and for Nupe roughly a sixth of the gold set
is alphabet-chart entries (single letters, digraph names) that score
almost perfectly and mask a much worse real-word number. Excluding those,
the real-word PER is 0.4679, and only 0.0353 of that survives once tone
diacritics are folded out of both the hypothesis and the gold -- most of
the apparent segmental error is in fact the same tone the plain
orthography never wrote down.
"""
from __future__ import annotations

import json
import pathlib
import sys
import unicodedata

import pytest

DATA_DIR = (pathlib.Path(__file__).parent.parent
            / "orthography2ipa" / "data")
SCRIPTS_DIR = pathlib.Path(__file__).parent.parent / "scripts"

_TONE_MARKS = {"̀", "́", "̄", "̌", "̂"}  # grave, acute, macron, caron, circumflex


def _defold(s: str) -> str:
    """Strip tone diacritics only; nasalisation (combining tilde) and the
    tie bar over affricates are left untouched -- those are phonemic, not
    tonal, and folding them out would hide real segmental errors."""
    d = unicodedata.normalize("NFD", s)
    return unicodedata.normalize(
        "NFC", "".join(c for c in d if c not in _TONE_MARKS))


def _load_gold():
    sys.path.insert(0, str(SCRIPTS_DIR))
    import benchmark as bm
    return bm.load_wikipron("nup", 10 ** 9)


# ═══════════════════════════════════════════════════════════════════════════
# The documented tone ceiling
# ═══════════════════════════════════════════════════════════════════════════

def test_notes_document_the_measured_tone_ceiling():
    raw = json.loads((DATA_DIR / "nup.json").read_text(encoding="utf-8"))
    notes = raw["notes"]
    assert "NOT RECOVERABLE from the orthography" in notes
    assert "0.4679" in notes
    assert "0.0353" in notes
    assert "48 distinct Latin spellings" in notes


def test_identical_spelling_maps_to_more_than_one_gold_tone():
    """Direct evidence, independent of any literature claim, that the plain
    Latin orthography cannot disambiguate tone: the same wikipron headword
    recurs with different gold transcriptions for the identical input
    string, differing only in tone/nasalisation diacritics."""
    pairs = _load_gold()
    by_word: dict[str, set[str]] = {}
    for word, gold in pairs:
        by_word.setdefault(word, set()).add(gold)

    homographs = {w: g for w, g in by_word.items() if len(g) > 1}
    # measured against the cached gold: 48 spellings carry >=2 distinct
    # gold transcriptions, all differing only in tone/nasalisation marks
    assert len(homographs) >= 40, (
        "expected the previously-measured ~48 tone-ambiguous homographs; "
        f"found {len(homographs)}"
    )
    assert "ebe" in homographs
    assert "elo" in homographs


def test_folding_tone_out_of_both_sides_collapses_most_of_the_real_word_error():
    """Reproduces the measured ceiling cited in the spec notes: score the
    real-word subset of the gold (the alphabet-chart headwords excluded)
    with and without tone diacritics folded out of both the hypothesis and
    the gold. If this ever regresses badly it means either the segmental
    rules broke or the tone-ceiling claim in the notes is stale."""
    sys.path.insert(0, str(SCRIPTS_DIR))
    import benchmark as bm
    from gold_composition import classify_gold
    from orthography2ipa import G2P

    pairs = _load_gold()
    _trivial, real, _stats = classify_gold("nup", pairs)

    def score(fold: bool) -> float:
        engine = G2P("nup")
        refs: dict[str, list[str]] = {}
        for w, g in real:
            refs.setdefault(w, []).append(g)
        pers = []
        for word, golds in refs.items():
            transcribe = (engine.transcribe if bm._is_multiword(word)
                          else engine.transcribe_word)
            try:
                raw_hyp = transcribe(word)
            except Exception:
                continue
            hyp = bm.normalize(raw_hyp, True, True)
            if fold:
                hyp = _defold(hyp)
            if not hyp:
                continue
            golds_norm = []
            for x in golds:
                gx = bm.normalize(x, True, True)
                if fold:
                    gx = _defold(gx)
                golds_norm.append(gx)
            pers.append(min(
                bm.levenshtein(hyp, g) / max(len(g), 1) for g in golds_norm))
        return sum(pers) / len(pers)

    baseline = score(fold=False)
    folded = score(fold=True)

    # the real-word (non-alphabet-chart) baseline the board's headline PER
    # hides behind its trivial-entry share
    assert baseline == pytest.approx(0.4679, abs=0.01)
    # most of that error is tone the plain orthography never wrote down
    assert folded == pytest.approx(0.0353, abs=0.01)
    assert folded < baseline - 0.35
