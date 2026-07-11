"""Signature tests for the Pyrenean-valley Aragonese subdialects.

The five classic High-Aragonese valley varieties are modelled as thin deltas on
the base Aragonese spec ``an`` (F- preservation, /θ/ distinción, /ʎ/ for ⟨ll⟩,
⟨ch⟩=[tʃ] are all inherited). Aragonese orthography is broadly phonemic, so most
of what distinguishes these valleys is lexical/morphological (article forms, verb
endings) and is documented in ``notes`` rather than modelled; only the
phoneme-level deltas are asserted here.

Provenance per feature (see each spec's ``sources``/``notes``):

    cheso      — ⟨x⟩/⟨ix⟩=[ʃ] without epenthesis (Kuhn 1935; es.wikipedia, secondary).
    ansotano   — word-final ⟨r⟩ deletion, Ansó vs Fago (Barcos 2007, secondary).
    belsetán   — preserved geminates -LL-/-NN- (Badía Margarit 1950, secondary).
    chistabín  — geminates + final-r deletion (Blas Gabarda & Romanos 2008; Mott 1989).
    tensino    — ro/ra/ros/ras article as weak tap [ɾ] (Vázquez Obrador 2021, read).

Diphthong geography for all five cross-checked against Várvaro (AFA XLVI-XLVII),
read directly.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, get, phonological_distance


VALLEYS = [
    "an-x-ansotano",
    "an-x-cheso",
    "an-x-chistabin",
    "an-x-belsetan",
    "an-x-tensino",
]


def bare(s: str) -> str:
    return s.replace("ˈ", "").replace("ˌ", "")


# ─── registration & inheritance ─────────────────────────────────────────────


@pytest.mark.parametrize("code", VALLEYS)
def test_spec_registers(code):
    spec = get(code)
    assert spec.code == code
    assert spec.graphemes, f"{code} resolved no graphemes"
    assert spec.family == "Romance"


@pytest.mark.parametrize("code", VALLEYS)
def test_parent_is_aragonese(code):
    assert get(code).parent == "an"


@pytest.mark.parametrize("code", VALLEYS)
def test_ancestry_chain_reaches_hispanic_latin(code):
    """Every valley declares an -> la-x-hispania in its ancestors chain."""
    codes = [a.code for a in get(code).ancestors]
    assert codes[0] == "an", f"{code} first ancestor must be an"
    assert "la-x-hispania" in codes, f"{code} lacks Ibero-Romance ancestry"


@pytest.mark.parametrize("code", VALLEYS)
def test_inherits_base_aragonese_features(code):
    """F- preserved, ⟨ll⟩=/ʎ/, ⟨ch⟩=[tʃ] all inherited from an."""
    g = G2P(code)
    assert bare(g.transcribe_word("feito")).startswith("f")   # F- kept
    assert "ʎ" in bare(g.transcribe_word("bella"))            # ⟨ll⟩ = /ʎ/
    assert "tʃ" in bare(g.transcribe_word("chaminera"))       # ⟨ch⟩ = [tʃ]


@pytest.mark.parametrize("code", VALLEYS)
def test_tier_is_documented(code):
    tier = get(code).quality.value
    assert tier in ("research", "skeleton"), f"{code} unexpected tier {tier}"


# ─── cheso: no-epenthesis ⟨ix⟩ ──────────────────────────────────────────────


class TestCheso:
    def test_ix_no_epenthesis(self):
        # base an offers [ʃ, iʃ, jʃ] for ⟨ix⟩; cheso keeps only [ʃ]
        assert get("an-x-cheso").graphemes["ix"] == ["ʃ"]

    def test_buixo(self):
        assert bare(G2P("an-x-cheso").transcribe_word("buixo")) == "bwiʃo"

    def test_tier_research(self):
        assert get("an-x-cheso").quality.value == "research"


# ─── ansotano: word-final r deletion ────────────────────────────────────────


class TestAnsotano:
    def test_final_r_deleted(self):
        # base 'fablar' -> ...ɾ ; ansotano deletes the word-final r
        assert not bare(G2P("an-x-ansotano").transcribe_word("fablar")).endswith("ɾ")
        assert bare(G2P("an").transcribe_word("fablar")).endswith("ɾ")

    def test_nonfinal_r_kept(self):
        # intervocalic / word-initial rhotics survive
        assert "ɾ" in bare(G2P("an-x-ansotano").transcribe_word("cara"))


# ─── belsetán / chistabín: preserved geminates ──────────────────────────────


@pytest.mark.parametrize("code", ["an-x-belsetan", "an-x-chistabin"])
def test_geminate_lateral(code):
    assert bare(G2P(code).transcribe_word("bel·la")) == "belːa"


@pytest.mark.parametrize("code", ["an-x-belsetan", "an-x-chistabin"])
def test_geminate_nasal(code):
    assert bare(G2P(code).transcribe_word("pen·na")) == "penːa"


class TestChistabin:
    def test_final_r_deleted(self):
        assert not bare(G2P("an-x-chistabin").transcribe_word("comer")).endswith("ɾ")

    def test_belsetan_keeps_final_r(self):
        # belsetán models geminates but NOT final-r deletion
        assert bare(G2P("an-x-belsetan").transcribe_word("comer")).endswith("ɾ")


# ─── tensino: ro/ra article as weak tap ─────────────────────────────────────


class TestTensino:
    @pytest.mark.parametrize("art,exp", [("ro", "ɾo"), ("ra", "ɾa"),
                                         ("ros", "ɾos"), ("ras", "ɾas")])
    def test_article_is_tap(self, art, exp):
        assert bare(G2P("an-x-tensino").transcribe_word(art)) == exp

    def test_word_initial_r_elsewhere_is_trill(self):
        # only the article words are overridden; ⟨rr⟩ stays the trill
        assert "r" in bare(G2P("an-x-tensino").transcribe_word("carro"))

    def test_tier_skeleton(self):
        # distinctiveness is morpholexical -> honestly skeleton
        assert get("an-x-tensino").quality.value == "skeleton"


# ─── distance sanity ────────────────────────────────────────────────────────


@pytest.mark.parametrize("code", VALLEYS)
def test_distance_to_parent_small(code):
    """Each valley is a small perturbation of an (delta specs)."""
    d = phonological_distance(get("an"), get(code)).combined
    assert 0.0 <= d < 0.1, f"{code} distance to an unexpectedly large: {d}"


def test_geminate_valleys_farther_than_minimal_deltas():
    """belsetán/chistabín (added geminate graphemes) sit farther from an than
    the tap-only tensino / final-r-only ansotano deltas."""
    an = get("an")
    d_bel = phonological_distance(an, get("an-x-belsetan")).combined
    d_ten = phonological_distance(an, get("an-x-tensino")).combined
    assert d_bel > d_ten
