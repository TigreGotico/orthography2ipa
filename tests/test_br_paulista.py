"""Provenance-grounded tests for the Paulistano / Caipira / Paranaense triad.

These three specs model the São Paulo–southern Brazilian dialect cluster as
deltas on the merged pt-BR base. The diagnostic features asserted here are
page-cited to Amadeu Amaral, *O Dialeto Caipira* (1920) — the foundational
description — read directly from the full text:

    Caipira retroflex coda /r/  — Amaral (1920) §6b ('r ... linguo-palatal e
                                  guturalizado ... vira a extremidade para cima
                                  ... assemelha-se ... ao r inglês post-vocálico').
    Caipira laminodental coda /s/, no chiado — Amaral (1920) §6a.
    Caipira coda /l/ rhotacism (traditional [ɻ] variant) — Amaral (1920) §22a.
    Paulistano capital: plain tap coda /r/ (NOT retroflex) — contrast, §6b;
                        coda /s/ alveolar, no chiado — Barbosa & Albano (2004).
    Paranaense (Curitibano/Sulista): conservative non-palatalisation, final
                        /e/ retention, alveolar tap coda /r/ — Noll (2008), ALiB.

Vowel quality that is lexical and unmarked in the orthography (the open-mid
/ɔ/ of *porta*) is not derivable and is not asserted; only the grapheme- and
position-derivable segments are checked.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, get


def _g(lang: str) -> G2P:
    return G2P(lang)


def bare(s: str) -> str:
    """Strip stress marks for bare phoneme comparison."""
    return s.replace("ˈ", "").replace("ˌ", "")


# ─── caipira: the defining retroflex coda /r/ (Amaral 1920 §6b) ──────────────


class TestCaipiraRetroflex:
    def test_porta_retroflex_coda(self):
        # porta -> [ˈpoɻtɐ]; the erre caipira before a consonant.
        assert bare(_g("pt-BR-x-caipira").transcribe_word("porta")) == "poɻtɐ"

    def test_mar_retroflex_word_final(self):
        assert bare(_g("pt-BR-x-caipira").transcribe_word("mar")).endswith("ɻ")

    def test_carta_retroflex_before_consonant(self):
        assert "ɻ" in bare(_g("pt-BR-x-caipira").transcribe_word("carta"))

    def test_intervocalic_r_stays_tap(self):
        # §6b applies to inter/post-vocalic weak /r/, realised as a tap
        # intervocalically here — not the strong onset rhotic and not [ɻ].
        r = bare(_g("pt-BR-x-caipira").transcribe_word("caro"))
        assert "ɻ" not in r and "ɾ" in r

    def test_coda_l_default_vocalised_traditional_retroflex_available(self):
        # Modern caipira vocalises coda /l/ to [w] (sol -> [ˈsow]); the
        # traditional Amaral §22a rhotacised realisation [ɻ] is retained as a
        # declared secondary candidate.
        assert bare(_g("pt-BR-x-caipira").transcribe_word("sol")).endswith("w")
        assert "ɻ" in get("pt-BR-x-caipira").positional_graphemes["l"]["before_consonant"]


# ─── caipira: coda /s/ laminodental, no chiado (Amaral 1920 §6a) ─────────────


class TestCaipiraSibilant:
    def test_coda_s_not_palatal(self):
        r = bare(_g("pt-BR-x-caipira").transcribe_word("mesmo"))
        assert "ʃ" not in r and "ʒ" not in r

    def test_final_s_not_palatal(self):
        assert bare(_g("pt-BR-x-caipira").transcribe_word("costas")).endswith("s")


# ─── sp (Paulistano capital): non-chiado coda /s/, plain tap /r/ ─────────────


class TestPaulistano:
    def test_coda_s_alveolar_no_chiado(self):
        r = bare(_g("pt-BR-x-sp").transcribe_word("mesmo"))
        assert "ʃ" not in r and "ʒ" not in r

    def test_final_s_alveolar(self):
        assert bare(_g("pt-BR-x-sp").transcribe_word("dois")).endswith("s")

    def test_coda_r_tap_not_retroflex(self):
        r = bare(_g("pt-BR-x-sp").transcribe_word("porta"))
        assert "ɻ" not in r and "ɾ" in r

    def test_td_palatalisation_inherited(self):
        assert "t͡ʃ" in bare(_g("pt-BR-x-sp").transcribe_word("tia"))
        assert "d͡ʒ" in bare(_g("pt-BR-x-sp").transcribe_word("dia"))


# ─── pr (Paranaense/Curitibano): conservative sulista features ───────────────


class TestParanaense:
    def test_no_palatalisation(self):
        assert "t͡ʃ" not in bare(_g("pt-BR-x-pr").transcribe_word("tia"))
        assert "d͡ʒ" not in bare(_g("pt-BR-x-pr").transcribe_word("dia"))

    def test_final_e_retained(self):
        assert bare(_g("pt-BR-x-pr").transcribe_word("verde")).endswith("e")

    def test_coda_r_alveolar_tap_not_retroflex(self):
        r = bare(_g("pt-BR-x-pr").transcribe_word("porta"))
        assert "ɻ" not in r and "ɾ" in r

    def test_coda_s_alveolar(self):
        r = bare(_g("pt-BR-x-pr").transcribe_word("costas"))
        assert "ʃ" not in r and "h" not in r


# ─── base inheritance: all three inherit the pt-BR coda-/l/ vocalisation ─────


@pytest.mark.parametrize("code", ["pt-BR-x-sp", "pt-BR-x-caipira", "pt-BR-x-pr"])
class TestBaseInheritance:
    def test_coda_l_vocalisation(self, code):
        assert bare(_g(code).transcribe_word("sol")).endswith("w")

    def test_a_final_reduction(self, code):
        assert bare(_g(code).transcribe_word("capa")).endswith("ɐ")

    def test_resolves_with_stress_block(self, code):
        spec = get(code)
        assert spec.graphemes and spec.allophones and spec.stress is not None

    def test_amaral_source_present(self, code):
        assert any(s.id == "amaral1920" for s in get(code).sources)
