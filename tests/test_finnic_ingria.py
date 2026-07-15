"""Accuracy tests for the Finnic languages of Ingria and Karelia.

Covers: Ingrian (izh), Votic (vot), Karelian (krl) — shallow Finnic Latin
orthographies modelled on the Finnish base (fi), adding the sibilant/affricate
letters and, for Votic, the vowels ⟨õ ü⟩.

The smoke tests transcribe a handful of REAL WikiPron rows (broad transcription,
CUNY-CL/wikipron data/scrape/tsv/{izh,vot,krl}_latn_broad.tsv) offline — no
network — and assert the engine neither crashes nor emits a symbol the spec does
not declare.

Run with:
    pytest tests/test_finnic_ingria.py -v --tb=short
"""
from __future__ import annotations

import pytest

import orthography2ipa
from orthography2ipa import emission_inventory

# Marks (stress, length, tie bars) legitimately added on top of declared
# segments by the engine's post-processing.
_EXTRA_MARKS = set("ˈˌːˑ͜͡")


def _load(code: str):
    try:
        return orthography2ipa.get(code)
    except Exception as exc:  # pragma: no cover - availability guard
        pytest.skip(f"{code!r} not available: {exc}")


def _allowed_chars(spec) -> set:
    chars = set(_EXTRA_MARKS)
    for sym in emission_inventory(spec):
        chars.update(sym)
    return chars


def _assert_declared(code: str, words) -> None:
    spec = _load(code)
    allowed = _allowed_chars(spec)
    eng = orthography2ipa.G2P(code)
    for w in words:
        ipa = eng.transcribe_word(w)
        assert ipa, f"{code}: empty transcription for {w!r}"
        undeclared = set(ipa) - allowed
        assert not undeclared, (
            f"{code}: {w!r} -> {ipa!r} emits undeclared {sorted(undeclared)!r}")


# ═══════════════════════════════════════════════════════════════════════════
# Ingrian (izh)
# ═══════════════════════════════════════════════════════════════════════════

def test_ingrian_sibilant_letters():
    """⟨š⟩ = /ʃ/, ⟨ž⟩ = /ʒ/ (Ingrian Latin orthography)."""
    spec = _load("izh")
    assert spec.graphemes.get("š") == ["ʃ"]
    assert spec.graphemes.get("ž") == ["ʒ"]


def test_ingrian_doubled_vowel_is_long():
    """Doubled vowels mark phonemic length: ⟨maa⟩ → /mɑː/."""
    assert orthography2ipa.G2P("izh").transcribe_word("maa") == "mɑː"


def test_ingrian_geminate_and_front_vowels():
    """Geminate ⟨kk⟩ → /kː/; ⟨ä ö⟩ = /æ ø/; ⟨š⟩ word-internally."""
    assert orthography2ipa.G2P("izh").transcribe_word("Afrikka") == "ɑfrikːɑ"
    assert orthography2ipa.G2P("izh").transcribe_word("šuuri") == "ʃuːri"


@pytest.mark.slow
def test_ingrian_wikipron_rows_declared_only():
    _assert_declared("izh", [
        "Aabrama", "Afrikka", "Amerikka", "Anttikristus", "Arhippa",
        "Australia", "Annuška",
    ])


# ═══════════════════════════════════════════════════════════════════════════
# Votic (vot)
# ═══════════════════════════════════════════════════════════════════════════

def test_votic_special_vowels():
    """⟨õ⟩ = /ɤ/ and ⟨ü⟩ = /y/ (shared with Estonian)."""
    spec = _load("vot")
    assert spec.graphemes.get("õ") == ["ɤ"]
    assert spec.graphemes.get("ü") == ["y"]
    assert orthography2ipa.G2P("vot").transcribe_word("sõna") == "sɤnɑ"


def test_votic_v_is_labiodental():
    """Votic ⟨v⟩ is /v/, not the Finnish approximant /ʋ/."""
    spec = _load("vot")
    assert spec.graphemes.get("v") == ["v"]
    assert "v" in orthography2ipa.G2P("vot").transcribe_word("Kerstova")


def test_votic_affricate_letter():
    """⟨č⟩ = /t͡ʃ/."""
    assert orthography2ipa.G2P("vot").transcribe_word("tšikko") == "tʃikːo"


@pytest.mark.slow
def test_votic_wikipron_rows_declared_only():
    _assert_declared("vot", [
        "Inkerimaa", "Jaama", "Jõgõperä", "Kabrio", "Kattila", "Kerstova",
        "Kliimettina",
    ])


# ═══════════════════════════════════════════════════════════════════════════
# Karelian (krl)
# ═══════════════════════════════════════════════════════════════════════════

def test_karelian_affricate_letters():
    """⟨č⟩ = /t͡ʃ/, digraph ⟨dž⟩ = /d͡ʒ/, ⟨š ž⟩ = /ʃ ʒ/."""
    spec = _load("krl")
    assert spec.graphemes.get("č") == ["t͡ʃ"]
    assert spec.graphemes.get("dž") == ["d͡ʒ"]
    assert spec.graphemes.get("š") == ["ʃ"]
    assert spec.graphemes.get("ž") == ["ʒ"]


def test_karelian_transcribes_affricate_and_length():
    assert orthography2ipa.G2P("krl").transcribe_word("čoma") == "t͡ʃomɑ"
    assert orthography2ipa.G2P("krl").transcribe_word("muužu") == "muːʒu"


@pytest.mark.slow
def test_karelian_wikipron_rows_declared_only():
    _assert_declared("krl", [
        "Kannanlakši", "Ruočči", "aakkua", "abie", "abu", "abuiäni",
    ])
