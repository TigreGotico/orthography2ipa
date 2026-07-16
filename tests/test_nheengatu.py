"""Accuracy tests for Nheengatu (yrl), the Amazonian General Language (Tupian).

Shallow, broadly phonemic orthography: oral vowels ⟨a e i o u⟩ with nasal
counterparts ⟨ã ẽ ĩ õ ũ⟩, acute accents marking stress, and one-to-one
consonants with ⟨x⟩ = /ʃ/, ⟨j⟩ = /ʒ/, ⟨y⟩ = /j/ and ⟨nh⟩ = /ɲ/.

The smoke test transcribes REAL WikiPron rows (CUNY-CL/wikipron
data/scrape/tsv/yrl_latn_broad.tsv) offline.

Run with:
    pytest tests/test_nheengatu.py -v --tb=short
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


def test_nheengatu_sibilant_and_glides():
    """⟨x⟩ = /ʃ/, ⟨j⟩ = /ʒ/, ⟨y⟩ = the palatal glide /j/."""
    spec = _load("yrl")
    assert spec.graphemes.get("x") == ["ʃ"]
    assert spec.graphemes.get("j") == ["ʒ"]
    assert spec.graphemes.get("y") == ["j"]
    eng = orthography2ipa.G2P("yrl")
    assert eng.transcribe_word("ixé") == "iʃe"
    assert eng.transcribe_word("jí") == "ʒi"


def test_nheengatu_nh_is_palatal_nasal():
    """The digraph ⟨nh⟩ = /ɲ/."""
    spec = _load("yrl")
    assert spec.graphemes.get("nh") == ["ɲ"]
    assert orthography2ipa.G2P("yrl").transcribe_word("kastanha") == "kastaɲa"


def test_nheengatu_nasal_vowels():
    """Nasal vowels ⟨ã ĩ ũ⟩ are phonemic and map to nasalised vowels."""
    spec = _load("yrl")
    assert spec.graphemes.get("ã") == ["ã"]
    assert spec.graphemes.get("ĩ") == ["ĩ"]
    assert spec.graphemes.get("ũ") == ["ũ"]


@pytest.mark.slow
def test_nheengatu_wikipron_rows_declared_only():
    spec = _load("yrl")
    allowed = set(_EXTRA_MARKS)
    for sym in emission_inventory(spec):
        allowed.update(sym)
    eng = orthography2ipa.G2P("yrl")
    for w in ["Kurupira", "Tupana", "kamarara", "igara", "kastanha",
              "nheenga", "kamixá"]:
        ipa = eng.transcribe_word(w)
        assert ipa, f"empty transcription for {w!r}"
        assert not (set(ipa) - allowed), f"{w!r} -> {ipa!r} undeclared symbol"
