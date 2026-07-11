"""Carioca / Fluminense / Mineiro post-lexical allophony (Workstream P, P4).

Three Brazilian dialects modelled as deltas on the merged ``pt-BR`` base:

* ``pt-BR-x-rj`` (Carioca) and ``pt-BR-x-fluminense`` carry the defining
  *chiado carioca* as post-lexical ``allophone_rules`` — coda /S/ → [ʃ]/[ʒ]
  (Callou 2010:135) — plus posterior coda /R/ (velar [x] pre-consonantally,
  aspiration [h] word-finally; Callou 2010:138). These override the alveolar
  coda sibilant inherited from the pt-BR base.
* ``pt-BR-x-mg`` (Mineiro) does NOT chiado: it keeps the base alveolar coda
  /S/ and declares no coda-sibilant rule; its diagnostic pretonic mid-vowel
  raising (Lemos & Viegas 2016:314) is realised in the pre-lexical positional
  map, unchanged here.

Assertions are whole-word transcriptions so the rules are exercised through
the real engine pipeline (positional selection → allophone rescorer → stress).
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, get


def _t(code: str, word: str) -> str:
    return G2P(code).transcribe_word(word)


def bare(s: str) -> str:
    return s.replace("ˈ", "").replace("ˌ", "").replace("͡", "")


# ─── base inheritance ───────────────────────────────────────────────────────

@pytest.mark.parametrize("code", [
    "pt-BR-x-rj", "pt-BR-x-fluminense", "pt-BR-x-mg",
])
def test_inherits_base_vowel_rules(code):
    """Every dialect inherits the pt-BR final-vowel-raising rules by id."""
    ids = [r.id for r in get(code).allophone_rules]
    assert "BR_RAISE_FINAL_E" in ids
    assert "BR_RAISE_FINAL_O" in ids


@pytest.mark.parametrize("code", [
    "pt-BR-x-rj", "pt-BR-x-fluminense", "pt-BR-x-mg",
])
def test_inherits_base_l_vocalisation(code):
    """Coda /l/ → [w] is inherited from the pt-BR base (sol → …w)."""
    assert bare(_t(code, "sol")).endswith("w")


@pytest.mark.parametrize("code", [
    "pt-BR-x-rj", "pt-BR-x-fluminense", "pt-BR-x-mg",
])
def test_final_vowel_raising_still_fires(code):
    """Inherited final-vowel raising: gato → …u, leite → …i."""
    assert bare(_t(code, "gato")).endswith("u")
    assert bare(_t(code, "leite")).endswith("i")


# ─── Carioca (rj): chiado via coda-conditioned allophone_rules ──────────────

class TestCariocaChiado:
    def test_declares_chiado_rules(self):
        ids = [r.id for r in get("pt-BR-x-rj").allophone_rules]
        assert "RJ_CHIADO_CODA_S" in ids
        assert "RJ_CHIADO_CODA_Z" in ids

    def test_coda_s_hushes_preconsonantal(self):
        # mesmo → [ˈmeʃmu]: coda /S/ before a consonant palatalises.
        assert "ʃ" in bare(_t("pt-BR-x-rj", "mesmo"))

    def test_coda_s_hushes_word_final(self):
        # paz → [ˈpaʃ], dois → [ˈdojʃ]: word-final coda /S/ palatalises.
        assert bare(_t("pt-BR-x-rj", "paz")).endswith("ʃ")
        assert bare(_t("pt-BR-x-rj", "dois")).endswith("ʃ")

    def test_chiado_is_coda_only_not_onset(self):
        # An onset /s/ must stay alveolar: sala → [ˈsalɐ], casa → [ˈkazɐ].
        assert bare(_t("pt-BR-x-rj", "sala")).startswith("s")
        assert "ʃ" not in bare(_t("pt-BR-x-rj", "sala"))
        # intervocalic ‹s› is voiced [z], never hushed.
        assert "z" in bare(_t("pt-BR-x-rj", "casa"))
        assert "ʃ" not in bare(_t("pt-BR-x-rj", "casa"))

    def test_dorsal_onset_r(self):
        assert _t("pt-BR-x-rj", "rio").lstrip("ˈ").startswith("χ")

    def test_coda_r_velar_preconsonantal(self):
        # porta → [ˈpoxtɐ]: non-final coda /R/ is the velar fricative [x].
        assert "x" in bare(_t("pt-BR-x-rj", "porta"))

    def test_coda_r_aspiration_word_final(self):
        # mar → [ˈmah]: word-final coda /R/ aspirates.
        assert bare(_t("pt-BR-x-rj", "mar")).endswith("h")

    def test_palatalisation_present(self):
        assert "t͡ʃ" in _t("pt-BR-x-rj", "tia")
        assert "d͡ʒ" in _t("pt-BR-x-rj", "dia")


# ─── Fluminense: Carioca-like chiado (coastal prestige default) ─────────────

class TestFluminense:
    def test_declares_chiado_rules(self):
        ids = [r.id for r in get("pt-BR-x-fluminense").allophone_rules]
        assert "FLU_CHIADO_CODA_S" in ids
        assert "FLU_CHIADO_CODA_Z" in ids

    def test_coda_s_hushes(self):
        assert "ʃ" in bare(_t("pt-BR-x-fluminense", "mesmo"))
        assert bare(_t("pt-BR-x-fluminense", "paz")).endswith("ʃ")

    def test_chiado_coda_only(self):
        assert "ʃ" not in bare(_t("pt-BR-x-fluminense", "sala"))

    def test_coda_r_posterior(self):
        assert "x" in bare(_t("pt-BR-x-fluminense", "porta"))
        assert bare(_t("pt-BR-x-fluminense", "mar")).endswith("h")


# ─── Mineiro (mg): NOT chiado; pretonic raising instead ─────────────────────

class TestMineiro:
    def test_no_chiado_rules_declared(self):
        ids = [r.id for r in get("pt-BR-x-mg").allophone_rules]
        assert not any("CHIADO" in i for i in ids)

    def test_coda_s_stays_alveolar(self):
        # mesmo → [ˈmesmu], paz → [ˈpas]: no palatal sibilant anywhere.
        for w in ("mesmo", "paz", "costas"):
            r = bare(_t("pt-BR-x-mg", w))
            assert "ʃ" not in r and "ʒ" not in r, (w, r)

    def test_pretonic_raising_e(self):
        # menino → [miˈninu]: pretonic /e/ → [i] (Lemos & Viegas 2016).
        assert bare(_t("pt-BR-x-mg", "menino")).startswith("mi")

    def test_pretonic_raising_o(self):
        # coruja → [kuˈɾuʒɐ]: pretonic /o/ → [u].
        assert bare(_t("pt-BR-x-mg", "coruja")).startswith("ku")

    def test_coda_r_stays_tap(self):
        # BH tap-rhotic: porta keeps [ɾ], no velar/aspirated coda /R/.
        r = bare(_t("pt-BR-x-mg", "porta"))
        assert "ɾ" in r and "x" not in r and "h" not in r

    def test_palatalisation_present(self):
        assert "t͡ʃ" in _t("pt-BR-x-mg", "tia")
