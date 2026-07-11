"""Archaic Northern European Portuguese — Transmontano (pt-PT-x-trasosmontes)
and Alto-Minhoto (pt-PT-x-viana).

Cintra's (1971, Boletim de Filologia 22:81-116) conservative
'grupo transmontano-alto-minhoto' — the only EP varieties that retain the
medieval FOUR-SIBILANT system — modelled as grapheme / positional deltas over
the standard pt-PT parent, corroborated by Álvarez Pérez (2014, JPL 13-1:29-62):

  * Four-sibilant system (Cintra trait 2) — apico-alveolar [s̺ z̺] for the
    ⟨s⟩/⟨ss⟩ series vs laminal [s z] for ⟨c,ç⟩/⟨z⟩; the minimal pairs
    passo/paço and coser/cozer stay distinct.
  * Northern betacism — /v/ ~ /b/ merger into [b] (Cintra trait 1): vinho -> ˈbiɲu.
  * Archaic ⟨ch⟩ affricate — onset ⟨ch⟩ preserved as [tʃ] (Cintra trait 3):
    chave -> ˈtʃabɨ.

Porto's tonic-close-vowel diphthongisation ([e]->[je], [o]->[wo]) is a
baixo-minhoto-duriense feature and must NOT surface here.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P


def _bare(s: str) -> str:
    return s.replace("ˈ", "").replace("ˌ", "")


NORTH = ["pt-PT-x-trasosmontes", "pt-PT-x-viana"]


@pytest.fixture(params=NORTH)
def eng(request):
    return G2P(request.param)


# ─── Four-sibilant system (Cintra trait 2 / Álvarez Pérez 2014 §4) ───────────

class TestFourSibilants:
    def test_apico_ss_passo(self, eng):
        # ⟨ss⟩ -> voiceless apico-alveolar [s̺]
        assert eng.transcribe_word("passo") == "ˈpas̺u"

    def test_laminal_c_paco(self, eng):
        # ⟨ç⟩ -> laminal [s]; passo != paço is the diagnostic minimal pair
        assert eng.transcribe_word("paço") == "ˈpasu"
        assert eng.transcribe_word("passo") != eng.transcribe_word("paço")

    def test_apico_intervocalic_s_casa(self, eng):
        # intervocalic ⟨-s-⟩ -> voiced apico-alveolar [z̺]
        assert eng.transcribe_word("casa") == "ˈkaz̺ɐ"

    def test_voiced_minimal_pair_coser_cozer(self, eng):
        # coser (apico [z̺]) != cozer (laminal [z])
        assert "z̺" in eng.transcribe_word("coser")
        assert "z̺" not in eng.transcribe_word("cozer")
        assert eng.transcribe_word("coser") != eng.transcribe_word("cozer")

    def test_laminal_c_cinco(self, eng):
        # ⟨c⟩ before i -> laminal [s], never apico
        assert eng.transcribe_word("cinco") == "ˈsinku"

    def test_apico_word_initial_sal(self, eng):
        assert eng.transcribe_word("sal") == "ˈs̺aɫ"

    def test_apico_word_final_anos(self, eng):
        assert eng.transcribe_word("anos").endswith("s̺")

    def test_preconsonantal_coda_keeps_chiado(self, eng):
        # note-29 limit: preconsonantal coda ⟨s⟩ keeps the inherited chiado [ʃ]
        assert "ʃ" in eng.transcribe_word("festa")


# ─── Betacism (Cintra trait 1) ──────────────────────────────────────────────

class TestBetacism:
    def test_vinho(self, eng):
        assert eng.transcribe_word("vinho") == "ˈbiɲu"

    def test_vaca(self, eng):
        assert eng.transcribe_word("vaca") == "ˈbakɐ"

    def test_v_intervocalic_estava(self, eng):
        out = _bare(eng.transcribe_word("estava"))
        assert "b" in out and "v" not in out


# ─── Archaic ⟨ch⟩ affricate (Cintra trait 3, onset) ──────────────────────────

class TestChAffricate:
    def test_chave(self, eng):
        # ch -> [tʃ] AND intervocalic v -> [b]
        assert eng.transcribe_word("chave") == "ˈtʃabɨ"

    def test_ch_is_affricate_not_fricative(self, eng):
        assert _bare(eng.transcribe_word("chave")).startswith("tʃ")


# ─── Inheritance from the pt-PT base ────────────────────────────────────────

class TestInheritsBase:
    def test_dark_coda_l(self, eng):
        # dark coda /l/ inherited; onset s is now apico [s̺]
        assert eng.transcribe_word("sal") == "ˈs̺aɫ"

    def test_unstressed_reduction_inherited(self, eng):
        # final unstressed <e> -> [ɨ], as in the pt-PT parent
        assert eng.transcribe_word("este") == "ˈeʃtɨ"


# ─── No Porto diphthongisation (this is the ARCHAIC, not the coastal, north) ─

class TestNoPortoDiphthongisation:
    def test_no_je_diphthong(self, eng):
        assert "je" not in _bare(eng.transcribe_word("mês"))

    def test_no_wo_diphthong(self, eng):
        assert "wo" not in _bare(eng.transcribe_word("avô"))
