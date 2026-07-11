"""Behaviour tests for the Lusophone-African Portuguese varieties.

Covers the three research-tier emerging-norm specs pt-AO (Angolan),
pt-CV (Cape Verdean Portuguese) and pt-MZ (Mozambican), all of which
inherit European Portuguese (pt-PT) and then *remove* or override some of
its unstressed-vowel reduction and coda sibilant behaviour.

These are the L2 / second-norm Portuguese varieties, NOT the creoles:
pt-CV is Cape Verdean Portuguese, distinct from Kabuverdianu (kea).

Sources for the modelled features are cited per-spec in the JSON
``sources`` and in ``docs/languages/pt-{AO,CV,MZ}.md``. The Angolan
vowel facts asserted here follow Undolo (2014:183-184).
"""
import pytest

from orthography2ipa import get, transcribe
from orthography2ipa.types import QualityTier

AFRICAN = ["pt-AO", "pt-CV", "pt-MZ"]
# pt-AO and pt-MZ have a read primary for their own variety (Undolo 2014,
# Nhatuve 2019); pt-CV has none (only the Creole, Freitas 2017), so it is
# deliberately kept at skeleton — see docs/languages/pt-CV.md.
RESEARCH_TIER = ["pt-AO", "pt-MZ"]


@pytest.mark.parametrize("code", RESEARCH_TIER)
def test_is_research_tier(code):
    assert get(code).quality is QualityTier.RESEARCH


def test_cape_verdean_kept_at_skeleton_no_read_cv_source():
    """pt-CV has no read Cape-Verdean-Portuguese primary (only the Creole),
    so it must not claim research tier — honesty per hard rule 9."""
    assert get("pt-CV").quality is QualityTier.SKELETON


@pytest.mark.parametrize("code", AFRICAN)
def test_inherits_european_portuguese(code):
    """Each variety is built on pt-PT and resolves to usable data."""
    spec = get(code)
    assert spec.parent == "pt-PT"
    assert spec.graphemes  # resolved via graphemes_base = pt-PT
    assert spec.allophones


@pytest.mark.parametrize("code", AFRICAN)
def test_has_cited_sources(code):
    """Every variety cites at least one phonological reference."""
    assert len(get(code).sources) >= 1


# --- Angolan Portuguese vowels: the spelling-closer vocalism ---------------
# Undolo (2014:183): final unstressed /a/ stays open [a], NOT EP [ɐ].

def test_angolan_final_a_not_centralised():
    ao = transcribe("casa", "pt-AO")
    pt = transcribe("casa", "pt-PT")
    assert ao.endswith("a"), ao
    assert not ao.endswith("ɐ"), ao
    # EP does centralise the same word — this is the modelled delta.
    assert pt.endswith("ɐ"), pt
    assert ao != pt


def test_angolan_pretonic_e_not_raised_to_barred_i():
    """Undolo (2014:183): pretonic /e/ stays [e], not EP [ɨ]."""
    out = transcribe("presidente", "pt-AO")
    # pretonic e is realised [e]; the barred-i survives only word-finally
    assert "e" in out
    assert not out.startswith("pɨ") and "zɨ" not in out, out


def test_angolan_pretonic_o_not_raised_to_u():
    """Undolo (2014:184): pretonic /o/ stays [o], not raised to [u]."""
    out = transcribe("morar", "pt-AO")
    assert out.startswith("mo"), out
    assert not out.startswith("mu"), out


def test_angolan_final_e_keeps_barred_i():
    """[ɨ] survives in final unstressed position (Undolo 2014:183)."""
    out = transcribe("presidente", "pt-AO")
    assert out.endswith("ɨ"), out


# --- Coda /s/ stays alveolar (no Lisbon chiado) across all three -----------

@pytest.mark.parametrize("code", AFRICAN)
def test_coda_s_stays_alveolar(code):
    """The inherited EP chiado coda-sibilant rule is overridden by id."""
    spec = get(code)
    ids = {r.id if hasattr(r, "id") else r["id"] for r in spec.allophone_rules}
    assert "PT_CODA_S_HUSH" in ids
    # a word with coda /s/ must not surface the palatal [ʃ]
    out = transcribe("mais", code)
    assert "ʃ" not in out, (code, out)
    assert out.endswith("s"), (code, out)


# --- whole-word smoke checks (never raise, produce IPA) --------------------

@pytest.mark.parametrize("code", AFRICAN)
@pytest.mark.parametrize("word", ["casa", "presidente", "mais", "beleza"])
def test_whole_words_transcribe(code, word):
    out = transcribe(word, code)
    assert isinstance(out, str) and out
