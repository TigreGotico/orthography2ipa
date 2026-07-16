"""Minho, Alfena, Beira and Aveiro European Portuguese dialects.

These four specs sit in Cintra's (1971) *Baixo-Minhoto-Duriense-Beirão* group,
which Álvarez Pérez (2014, pp.37-38) describes as having "kept only the
apico-alveolar branch" of the archaic four-sibilant system. Modelled as
grapheme / positional deltas over the standard pt-PT parent:

  * APICO-ALVEOLAR-ONLY sibilant system — ⟨s⟩/⟨ss⟩ AND ⟨c⟩(before e/i)/⟨ç⟩/⟨z⟩
    all realise as apico-alveolar [s̺] (voiceless) / [z̺] (voiced). This is the
    two-sibilant *apical-only* system, DISTINCT from the conservative
    four-sibilant Transmontano/Alto-Minhoto system (which keeps apical
    ⟨s/ss⟩ = [s̺] opposed to laminal ⟨c/ç/z⟩ = [s]). Cintra 1971 p.93; Pérez
    2014 pp.37-38.
  * Northern BETACISM — /v/–/b/ merger realised [b] ~ [β]. Cintra 1971 p.88;
    Pérez 2014 pp.35-37 (extent covers the northern coast beyond Coimbra and
    the eastern Guarda/Castelo-Branco districts).
  * Coda ⟨s/z⟩ keep the pan-EP chiado neutralisation to [ʃ]/[ʒ] inherited from
    the pt-PT base.

The apico-alveolar quality is a distinct IPA segment ([s̺ z̺]) and is modelled
actively, not deleted. Porto's tonic-close-vowel diphthongisation
([e]>[je], [o]>[wo]) is NOT applied here (it is a Porto-specific subdivision
marker kept in pt-PT-x-porto).
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, transcribe

APICAL_S = "s̺"   # [s̺] apico-alveolar voiceless
APICAL_Z = "z̺"   # [z̺] apico-alveolar voiced

DIALECTS = ["pt-PT-x-minho", "pt-PT-x-alfena", "pt-PT-x-beira", "pt-PT-x-aveiro"]


def _bare(s: str) -> str:
    return s.replace("ˈ", "").replace("ˌ", "")


# ─── Apico-alveolar-only sibilant merger ────────────────────────────────────

class TestApicoAlveolarMerger:
    """Both the ⟨s/ss⟩ branch AND the ⟨c/ç/z⟩ branch surface apical."""

    @pytest.mark.parametrize("code", DIALECTS)
    def test_s_grapheme_is_apical(self, code):
        # ⟨s⟩ onset → apico-alveolar [s̺]
        assert _bare(G2P(code).transcribe_word("sol")).startswith(APICAL_S)

    @pytest.mark.parametrize("code", DIALECTS)
    def test_intervocalic_s_is_apical_voiced(self, code):
        # ⟨-s-⟩ intervocalic → apico-alveolar voiced [z̺]
        assert APICAL_Z in G2P(code).transcribe_word("casa")

    @pytest.mark.parametrize("code", DIALECTS)
    def test_soft_c_is_apical(self, code):
        # ⟨c⟩ before e/i → apical (the branch that stays laminal in the
        # four-sibilant system)
        assert APICAL_S in G2P(code).transcribe_word("cedo")
        assert APICAL_S in G2P(code).transcribe_word("cinco")

    @pytest.mark.parametrize("code", DIALECTS)
    def test_cedilha_is_apical(self, code):
        # ⟨ç⟩ → apical
        assert APICAL_S in G2P(code).transcribe_word("praça")
        assert APICAL_S in G2P(code).transcribe_word("faço")

    @pytest.mark.parametrize("code", DIALECTS)
    def test_z_grapheme_is_apical(self, code):
        # ⟨z⟩ onset → apico-alveolar voiced [z̺]
        assert APICAL_Z in G2P(code).transcribe_word("zebra")

    @pytest.mark.parametrize("code", DIALECTS)
    def test_both_branches_share_one_apical_realisation(self, code):
        # The defining merger: ⟨ç⟩ (historic laminal branch) and ⟨ss⟩ (historic
        # apical branch) realise IDENTICALLY — a single apical sibilant.
        eng = G2P(code)
        c_from_cedilha = eng.transcribe_word("praça")     # ç
        s_from_ss = eng.transcribe_word("massa")          # ss
        assert APICAL_S in c_from_cedilha and APICAL_S in s_from_ss


class TestDistinctFromFourSibilant:
    """The apical-only system differs from the four-sibilant Transmontano:
    there ⟨ç⟩ would stay laminal [s]; here it is apical [s̺]."""

    @pytest.mark.parametrize("code", DIALECTS)
    def test_soft_c_not_plain_laminal(self, code):
        # A plain laminal [s] (no apical diacritic) would signal the
        # four-sibilant split; these dialects must show the apical mark.
        out = G2P(code).transcribe_word("cedo")
        assert APICAL_S in out
        # the sibilant is not a bare laminal 's' followed by a vowel
        assert "̺" in out


# ─── Betacism (Cintra feature 1) ────────────────────────────────────────────

class TestBetacism:
    @pytest.mark.parametrize("code", DIALECTS)
    def test_v_onset_merges_to_b(self, code):
        assert G2P(code).transcribe_word("vaca").startswith("ˈb")
        assert "v" not in _bare(G2P(code).transcribe_word("vinho"))

    @pytest.mark.parametrize("code", DIALECTS)
    def test_v_intervocalic_merges(self, code):
        out = _bare(G2P(code).transcribe_word("uva"))
        assert "v" not in out
        assert "b" in out or "β" in out


# ─── Inheritance of the pt-PT base ──────────────────────────────────────────

class TestInheritsBase:
    @pytest.mark.parametrize("code", DIALECTS)
    def test_base_edges_declared(self, code):
        eng = G2P(code)
        # coda chiado inherited: ⟨-s⟩ / ⟨-z⟩ word-final → [ʃ]
        assert G2P(code).transcribe_word("dez").endswith("ʃ")

    @pytest.mark.parametrize("code", DIALECTS)
    def test_unstressed_a_reduces_like_base(self, code):
        # pt-PT unstressed final /a/ → [ɐ] is inherited, not overridden
        assert G2P(code).transcribe_word("casa").endswith("ɐ")

    def test_no_porto_diphthongisation(self):
        # [e]>[je] / [o]>[wo] must NOT leak in from Porto
        for code in DIALECTS:
            out = transcribe("medo", code)
            assert "je" not in out and "wo" not in out


# ─── Beira-Baixa: stressed /u/ → [y] palatalisation ─────────────────────────

class TestBeiraBaixaUFronting:
    """pt-PT-x-beira models the Beira-Baixa (Castelo Branco) stressed-/u/ → [y]
    palatalisation. Cintra (1971, p.14 of the CVC reflow) delimits the
    Beira-Baixa / Alto-Alentejo zone — núcleos Castelo-Branco e Portalegre — by
    exactly this isogloss: 'a palatalização, em maior ou menor grau, da vogal
    tónica u', part of 'uma profunda alteração de timbre de todo o sistema
    vocálico, principalmente do tónico'; the explicit [y] value is written in
    the adjacent Barlavento-Algarvio passage of the same 'reacção em cadeia'
    ('a palatalização da lábio-velar [u] em [y]'). Being a whole-tonic-system
    mainland chain shift, it fronts even before a tautosyllabic coda liquid —
    unlike the insular São Miguel open-nucleus process (pt-PT-x-acores) which
    blocks it. Modelled to mirror the sister mainland zone pt-PT-x-alentejo."""

    def test_stressed_u_fronts_to_y(self):
        assert transcribe("tudo", "pt-PT-x-beira") == "ˈtydu"
        assert transcribe("lume", "pt-PT-x-beira") == "ˈlymɨ"
        assert transcribe("número", "pt-PT-x-beira") == "ˈnymɨɾu"

    def test_fronts_before_coda_l_like_mainland(self):
        # mainland chain shift fronts even before coda /l/ (unlike insular Açores
        # azul → [ɐˈzuɫ]); matches pt-PT-x-alentejo / pt-PT-x-algarve sul → [ˈsyɫ]
        assert transcribe("sul", "pt-PT-x-beira") == "ˈs̺yɫ"

    def test_lexical_tu_fronts(self):
        assert transcribe("tu", "pt-PT-x-beira") == "ˈty"

    def test_unstressed_u_is_not_fronted(self):
        out = transcribe("turistas", "pt-PT-x-beira")
        assert "y" not in out
        assert "u" in out

    def test_proclitics_keep_u_never_front(self):
        # proclitics take no word stress (stress.cliticless_words), and the
        # word_exceptions guard keeps their /u/ nucleus (do → [du], never [dy]);
        # the indefinite article um/uns is a prosodic word and keeps its stress
        for word, expected in [
            ("do", "du"), ("no", "nu"), ("um", "ˈum"), ("uns", "ˈunʃ"),
        ]:
            out = transcribe(word, "pt-PT-x-beira")
            assert out == expected
            assert "y" not in out

    def test_sister_beira_group_specs_do_not_front(self):
        # minho/alfena/aveiro are the Baixo-Minhoto-Duriense-Beirão sibilant
        # group, NOT the Beira-Baixa/Alto-Alentejo chain-shift zone: no fronting
        for code in ("pt-PT-x-minho", "pt-PT-x-alfena", "pt-PT-x-aveiro"):
            assert "y" not in transcribe("tudo", code)
