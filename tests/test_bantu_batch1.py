"""Behaviour tests for the "bantu1" batch of Southern/Central Bantu specs:

nd (Northern Ndebele), lu (Luba-Katanga/Kiluba), lua (Luba-Kasai/Tshiluba),
bem (Bemba), umb (Umbundu), seh (Sena), yao (Yao/Chiyao).

Each is parented directly to the Bantu clade node (x-clade-narr1281). Test
words and citations follow the sources listed in each spec's ``sources``.
"""
import pytest

from orthography2ipa import get, transcribe
from orthography2ipa.types import QualityTier

CODES = ["nd", "lu", "lua", "bem", "umb", "seh", "yao"]


@pytest.mark.parametrize("code", CODES)
def test_is_research_tier(code):
    assert get(code).quality is QualityTier.RESEARCH


@pytest.mark.parametrize("code", CODES)
def test_has_cited_sources_and_wikipedia(code):
    spec = get(code)
    assert len(spec.sources) >= 1
    assert spec.wikipedia and len(spec.wikipedia) >= 1


@pytest.mark.parametrize("code", CODES)
def test_parents_into_bantu_clade(code):
    """Every batch spec resolves its ancestry to the Bantu clade node."""
    spec = get(code)
    assert spec.parent in ("x-clade-narr1281", "lu")
    assert "Bantu" in spec.family


# --- Northern Ndebele (isiNdebele) -----------------------------------------
# Nguni click system shared with Zulu (Hachipola 1998).

def test_ndebele_click_c():
    out = transcribe("icici", "nd")
    assert "ǀ" in out, out


def test_ndebele_prenasalized_nd():
    out = transcribe("indoda", "nd")
    assert "nd" in out, out


# --- Luba-Katanga (Kiluba) --------------------------------------------------
# Van Avermaet & Mbuya (1954): five vowels, prenasalized nasal+stop clusters.

def test_luba_katanga_prenasalized_mb():
    out = transcribe("mbuya", "lu")
    assert out.startswith("mb"), out


def test_luba_katanga_ny_palatal():
    out = transcribe("nyoka", "lu")
    assert out.startswith("ɲ"), out


# --- Luba-Kasai (Tshiluba) ---------------------------------------------------

def test_tshiluba_affricate_tsh():
    out = transcribe("tshiluba", "lua")
    assert out.startswith("tʃ"), out


def test_tshiluba_prenasalized_nd():
    out = transcribe("ndaya", "lua")
    assert out.startswith("nd"), out


# --- Bemba (Chibemba) --------------------------------------------------------
# Givón (1972): bare velar nasal ng' vs prenasalized ng.

def test_bemba_bare_velar_nasal():
    out = transcribe("ng'anda", "bem")
    assert out.startswith("ŋ"), out
    assert not out.startswith("ᵑɡ"), out


def test_bemba_palatal_affricate_ch():
    out = transcribe("chibemba", "bem")
    assert out.startswith("tʃ"), out


# --- Umbundu ------------------------------------------------------------------
# Schadeberg (1990): prenasalized stop series.

def test_umbundu_prenasalized_ng():
    out = transcribe("ngola", "umb")
    assert out.startswith("ᵑɡ"), out


def test_umbundu_five_vowels():
    spec = get("umb")
    for v in "aeiou":
        assert v in spec.graphemes


# --- Sena (Chisena) ------------------------------------------------------------
# Ngunga (2000) conventions for aspirate/affricate-rich Zambezi Bantu.

def test_sena_aspirated_th():
    out = transcribe("thumba", "seh")
    assert out.startswith("tʰ"), out


def test_sena_affricate_dz():
    out = transcribe("dzuwa", "seh")
    assert out.startswith("d͡z"), out


# --- Yao (Chiyao) ----------------------------------------------------------------
# Ngunga (2000): aspirated voiceless stops, retroflex s, labiodental ŵ.

def test_yao_aspirated_t():
    out = transcribe("tuwa", "yao")
    assert out.startswith("tʰ"), out


def test_yao_labiodental_w_circumflex():
    out = transcribe("ŵanga", "yao")
    assert out.startswith("ʋ"), out
