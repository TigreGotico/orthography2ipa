"""Accuracy tests for Nahuatl in the traditional Hispanic orthography.

Covers: Central Nahuatl (nhn) and Classical Nahuatl (nci, inheriting nhn).
The WikiPron gold uses the 'Jesuit'/classical spelling: ⟨c⟩ = /k/ (but /s/
before a front vowel), ⟨qu⟩ /k/, ⟨cu⟩ /kʷ/, ⟨tl⟩ /t͡ɬ/, ⟨tz⟩ /t͡s/, ⟨x⟩ /ʃ/,
⟨hu⟩ /w/, ⟨h⟩ the saltillo /ʔ/.

The smoke test transcribes REAL WikiPron rows (CUNY-CL/wikipron
data/scrape/tsv/{nhn,nci}_latn_broad.tsv) offline. Phonemic vowel LENGTH is not
written in this orthography, so it is deliberately under-generated.

Run with:
    pytest tests/test_nahuatl_classical.py -v --tb=short
"""
from __future__ import annotations

import pytest

import orthography2ipa
from orthography2ipa import emission_inventory

_EXTRA_MARKS = set("ˈˌːˑ͜͡")


def _load(code: str):
    try:
        return orthography2ipa.get(code)
    except Exception as exc:  # pragma: no cover
        pytest.skip(f"{code!r} not available: {exc}")


def test_nahuatl_lateral_affricate_and_labialised_stop():
    """⟨tl⟩ = the lateral affricate /t͡ɬ/; ⟨cu⟩ = the labialised /kʷ/."""
    spec = _load("nhn")
    assert spec.graphemes.get("tl") == ["t͡ɬ"]
    assert spec.graphemes.get("cu") == ["kʷ"]
    assert orthography2ipa.G2P("nhn").transcribe_word("acatl") == "akat͡ɬ"


def test_nahuatl_c_softens_before_front_vowel():
    """⟨c⟩ = /k/ by default but /s/ before ⟨e i⟩; ⟨x⟩ = /ʃ/, ⟨z⟩ = /s/."""
    eng = orthography2ipa.G2P("nhn")
    assert eng.transcribe_word("cecec") == "sesek"      # c/e -> s, c/final-e etc
    assert eng.transcribe_word("tlaxcalli") == "t͡ɬaʃkalːi"


def test_nahuatl_saltillo_is_glottal_stop():
    """⟨h⟩ = the saltillo /ʔ/."""
    spec = _load("nhn")
    assert spec.graphemes.get("h") == ["ʔ"]


def test_classical_nahuatl_inherits_central():
    """nci inherits the nhn grapheme system wholesale."""
    nci = _load("nci")
    assert nci.graphemes.get("tl") == ["t͡ɬ"]
    assert nci.graphemes.get("cu") == ["kʷ"]
    assert orthography2ipa.G2P("nci").transcribe_word("acatl") == "akat͡ɬ"


@pytest.mark.slow
@pytest.mark.parametrize("code,words", [
    ("nhn", ["acalli", "ahtlapalli", "ahcolli", "Portugal", "acayotl"]),
    ("nci", ["Acapolco", "Ahuitzotl", "Atlacomolco", "ahcolli"]),
])
def test_nahuatl_wikipron_rows_declared_only(code, words):
    spec = _load(code)
    allowed = set(_EXTRA_MARKS)
    for sym in emission_inventory(spec):
        allowed.update(sym)
    eng = orthography2ipa.G2P(code)
    for w in words:
        ipa = eng.transcribe_word(w)
        assert ipa, f"{code}: empty transcription for {w!r}"
        assert not (set(ipa) - allowed), (
            f"{code}: {w!r} -> {ipa!r} undeclared symbol")
