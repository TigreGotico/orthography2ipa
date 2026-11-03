"""Signature tests for the pt-BR base and its twelve regional dialect specs.

Each dialect asserts a small set of phonemically diagnostic, well-documented
features at the grapheme/positional level (full-word transcriptions would
overreach where lexical vowel quality is unmarked). Provenance per assertion:

    pt-BR base / sp  — Barbosa & Albano (2004, JIPA), São Paulo State variety,
                       via /tmp/extract_jipa_ptbr_real.md (DIRECT extraction).
    rj / fluminense  — coda-/S/ chiado + dorsal /r/ (Callou & Leite 2001).
    caipira          — retroflex coda /r/ (Castilho 2010; Amaral 1920).
    mg               — pretonic raising (ALiB; Castilho 2010).
    sul / pr         — conservative non-palatalisation + final-/e/ retention
                       (Noll 2008; ALiB).
    recife/norte/ce  — open pretonic vowels + coda-/S/ behaviour (ALiB,
                       Cardoso et al. 2014).
    bahia            — open pretonic + retained pre-/i/ palatalisation, plain
                       coda /S/ (ALiB resolution).

The North-Wind word pairs are the JIPA São Paulo gold, asserted against the
pt-BR base.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, get


def _g(lang: str) -> G2P:
    return G2P(lang)


def bare(s: str) -> str:
    """Strip stress marks for bare phoneme comparison."""
    return s.replace("ˈ", "").replace("ˌ", "")


ALL_BR = [
    "pt-BR", "pt-BR-x-sp", "pt-BR-x-rj", "pt-BR-x-fluminense",
    "pt-BR-x-caipira", "pt-BR-x-mg", "pt-BR-x-sul", "pt-BR-x-pr",
    "pt-BR-x-recife", "pt-BR-x-norte", "pt-BR-x-bahia", "pt-BR-x-ce",
    "pt-BR-x-brasilia",
]


# ─── infrastructure / inheritance ───────────────────────────────────────────


@pytest.mark.parametrize("code", ALL_BR)
def test_spec_resolves_with_stress(code):
    """Every BR spec resolves to content and carries an own stress block."""
    spec = get(code)
    assert spec.graphemes, f"{code} has no graphemes"
    assert spec.allophones, f"{code} has no allophones"
    assert spec.stress is not None, f"{code} lacks a stress block"


@pytest.mark.parametrize("code", [c for c in ALL_BR if c not in ("pt-BR", "pt-BR-x-caipira")])
def test_dialect_inherits_base_positional(code):
    """Dialects inherit the pt-BR coda-/l/ vocalisation (l -> w); caipira
    rhotacises it (pt-BR-x-caipira notes, Amaral 1920 §22a)."""
    assert bare(_g(code).transcribe_word("sol")).endswith("w")


# ─── pt-BR base (JIPA São Paulo) ────────────────────────────────────────────


class TestBaseJIPA:
    """North-Wind word pairs from Barbosa & Albano (2004), DIRECT extraction.

    Asserted at the segment level; lexical open-mid vowels in unmarked
    spelling (norte, forte) cannot be derived and are not asserted.
    """

    def test_final_e_reduction_norte(self):
        # norte -> [ˈnɔɾt͡ʃi] in JIPA; the grapheme-derivable part is the
        # final /e/ reduced to [ɪ] and raised to close [i] by the
        # BR_RAISE_FINAL_E allophone rule (affrication keys on the
        # orthographic ‹i›, not the reduced vowel, so it is not derived here).
        assert bare(_g("pt-BR").transcribe_word("norte")).endswith("i")

    def test_final_o_reduction_vento(self):
        # vento -> [ˈvẽntu]; final /o/ reduces to [ʊ] then raises to [u].
        assert bare(_g("pt-BR").transcribe_word("vento")).endswith("u")

    def test_final_a_reduction_capa(self):
        # capa -> [ˈkapɐ]; final /a/ -> [ɐ].
        assert bare(_g("pt-BR").transcribe_word("capa")).endswith("ɐ")

    def test_l_vocalisation_sol(self):
        # sol -> [sɔw]; coda /l/ -> [w].
        assert bare(_g("pt-BR").transcribe_word("sol")).endswith("w")

    def test_td_palatalisation(self):
        assert "t͡ʃ" in bare(_g("pt-BR").transcribe_word("tia"))
        assert "d͡ʒ" in bare(_g("pt-BR").transcribe_word("dia"))

    def test_coda_s_alveolar_not_palatal(self):
        # JIPA São Paulo keeps coda /S/ alveolar (no chiado).
        r = bare(_g("pt-BR").transcribe_word("mesmo"))
        assert "ʃ" not in r and "ʒ" not in r

    def test_onset_strong_r_dorsal(self):
        # word-initial /r/ -> dorsal [ʁ]; never a tap or alveolar trill here.
        assert _g("pt-BR").transcribe_word("rato").lstrip("ˈ").startswith("ʁ")


# ─── pt-BR-x-sp (JIPA reference) ────────────────────────────────────────────


class TestSP:
    def test_matches_base_palatalisation(self):
        assert "t͡ʃ" in bare(_g("pt-BR-x-sp").transcribe_word("tia"))

    def test_final_reduction(self):
        assert bare(_g("pt-BR-x-sp").transcribe_word("vento")).endswith("u")

    def test_coda_s_alveolar(self):
        r = bare(_g("pt-BR-x-sp").transcribe_word("mesmo"))
        assert "ʃ" not in r

    def test_coda_r_not_retroflex(self):
        r = bare(_g("pt-BR-x-sp").transcribe_word("porta"))
        assert "ɻ" not in r

    def test_strong_r_velar(self):
        """Barbosa & Albano 2004: 228: strong /r/ is velar, voiced between
        voiced sounds: carro [ˈkaɣʊ]."""
        assert bare(_g("pt-BR-x-sp").transcribe_word("rato")).startswith("x")
        assert bare(_g("pt-BR-x-sp").transcribe_word("carro")) == "kaɣu"

    def test_yod_before_final_s(self):
        """Barbosa & Albano 2004: 229: arroz [aɣoɪ̯s], mas [maɪ̯s]."""
        assert bare(_g("pt-BR-x-sp").transcribe_word("arroz")) == "aɣojs"
        assert bare(_g("pt-BR-x-sp").transcribe_word("mas")) == "majs"


# ─── pt-BR-x-rj (Carioca) ───────────────────────────────────────────────────


class TestRJ:
    def test_coda_s_palatal_mesmo(self):
        """mesmo -> [ˈmeʒmʊ]: coda /S/ -> [ʒ] before voiced consonant."""
        assert "ʃ" in bare(_g("pt-BR-x-rj").transcribe_word("mesmo"))

    def test_final_s_palatal_paz(self):
        assert bare(_g("pt-BR-x-rj").transcribe_word("paz")).endswith("ʃ")

    def test_coda_s_palatal_dois(self):
        assert bare(_g("pt-BR-x-rj").transcribe_word("dois")).endswith("ʃ")

    def test_dorsal_onset_r(self):
        assert _g("pt-BR-x-rj").transcribe_word("rio").lstrip("ˈ").startswith("χ")

    def test_palatalisation_present(self):
        assert "t͡ʃ" in bare(_g("pt-BR-x-rj").transcribe_word("tia"))


# ─── pt-BR-x-fluminense ─────────────────────────────────────────────────────


class TestFluminense:
    def test_coda_s_alveolar(self):
        """Hora 1999: 34-35: the North-Northwest of the state keeps the
        alveolar, unlike the capital."""
        r = bare(_g("pt-BR-x-fluminense").transcribe_word("mesmo"))
        assert "ʃ" not in r and "ʒ" not in r
        assert bare(_g("pt-BR-x-fluminense").transcribe_word("paz")).endswith("s")

    def test_coda_r_glottal(self):
        """Silva 2023: 68: Rio de Janeiro state coda /R/ is 80 % glottal."""
        assert bare(_g("pt-BR-x-fluminense").transcribe_word("porta")) == "pohtɐ"

    def test_palatalisation_present(self):
        assert "t͡ʃ" in bare(_g("pt-BR-x-fluminense").transcribe_word("tia"))

    def test_dorsal_onset_r(self):
        assert _g("pt-BR-x-fluminense").transcribe_word("rio").lstrip("ˈ").startswith("x")

    def test_l_vocalisation(self):
        assert bare(_g("pt-BR-x-fluminense").transcribe_word("mal")).endswith("w")


# ─── pt-BR-x-caipira ────────────────────────────────────────────────────────


class TestCaipira:
    def test_retroflex_coda_porta(self):
        """porta -> retroflex [ɻ] coda — the erre caipira."""
        assert "ɻ" in bare(_g("pt-BR-x-caipira").transcribe_word("porta"))

    def test_retroflex_coda_mar(self):
        assert bare(_g("pt-BR-x-caipira").transcribe_word("mar")).endswith("ɻ")

    def test_retroflex_before_consonant_carta(self):
        assert "ɻ" in bare(_g("pt-BR-x-caipira").transcribe_word("carta"))

    def test_coda_s_alveolar(self):
        r = bare(_g("pt-BR-x-caipira").transcribe_word("mesmo"))
        assert "ʃ" not in r

    def test_lh_vocalises(self):
        """Amaral 1920 §25: lh 'Vocaliza-se em i: [...] muié, fiio'."""
        assert bare(_g("pt-BR-x-caipira").transcribe_word("filho")) == "fiju"

    def test_coda_l_rhotacised(self):
        """Amaral 1920 §22a: coda l 'muda-se em r: [...] arma'."""
        assert bare(_g("pt-BR-x-caipira").transcribe_word("alma")) == "aɻmɐ"

    def test_intervocalic_tap_not_retroflex(self):
        # intervocalic weak /r/ stays a tap, not retroflex.
        assert "ɻ" not in bare(_g("pt-BR-x-caipira").transcribe_word("caro"))


# ─── pt-BR-x-mg ─────────────────────────────────────────────────────────────


class TestMG:
    def test_pretonic_raising_e(self):
        """Viegas & Veado 1982: 58: /e/ raises before a stressed high vowel
        (66.6 %): menino [miˈninu], pedido."""
        assert bare(_g("pt-BR-x-mg").transcribe_word("menino")).startswith("mi")
        assert bare(_g("pt-BR-x-mg").transcribe_word("pedido")).startswith("pi")

    def test_pretonic_e_kept_without_high_vowel(self):
        """Viegas & Veado 1982: 54: raising is variable, not categorical, so
        /e/ before a non-high vowel keeps [e]."""
        assert bare(_g("pt-BR-x-mg").transcribe_word("pecado")).startswith("pe")

    def test_initial_e_raised(self):
        """Viegas & Veado 1982: 58: word-initial /e/ raises in 90.7 %."""
        assert bare(_g("pt-BR-x-mg").transcribe_word("escola")).startswith("is")

    def test_coda_r_glottal(self):
        """Silva 2023: 68: Minas Gerais coda /R/ is 77 % glottal."""
        assert bare(_g("pt-BR-x-mg").transcribe_word("porta")) == "pohtɐ"

    def test_coda_s_alveolar(self):
        r = bare(_g("pt-BR-x-mg").transcribe_word("mesmo"))
        assert "ʃ" not in r

    def test_palatalisation_present(self):
        assert "t͡ʃ" in bare(_g("pt-BR-x-mg").transcribe_word("tia"))


# ─── pt-BR-x-sul (Gaúcho) ───────────────────────────────────────────────────


class TestSul:
    def test_palatalisation_tia(self):
        """Battisti & Dornelles Filho 2015: 226 (ALiB): Porto Alegre
        palatalisation is categorical."""
        assert bare(_g("pt-BR-x-sul").transcribe_word("tia")).startswith("t͡ʃ")
        assert bare(_g("pt-BR-x-sul").transcribe_word("dia")).startswith("d͡ʒ")

    def test_palatalisation_before_raised_plural(self):
        assert bare(_g("pt-BR-x-sul").transcribe_word("dentes")) == "dẽt͡ʃis"

    def test_velar_onset_r(self):
        """Corrêa 2020: 87: the trill fell to 0.4 %; Comiotto & Margotti 2019:
        the velar fricative [x] predominates in RS."""
        assert bare(_g("pt-BR-x-sul").transcribe_word("rato")).startswith("x")
        assert bare(_g("pt-BR-x-sul").transcribe_word("carro")) == "kaxu"

    def test_coda_r_tap_not_dropped(self):
        assert bare(_g("pt-BR-x-sul").transcribe_word("mar")).endswith("ɾ")


# ─── pt-BR-x-pr (Curitibano) ────────────────────────────────────────────────


class TestPR:
    def test_no_palatalisation_default(self):
        r = bare(_g("pt-BR-x-pr").transcribe_word("tia"))
        assert "t͡ʃ" not in r

    def test_final_e_retained(self):
        assert bare(_g("pt-BR-x-pr").transcribe_word("verde")).endswith("e")

    def test_coda_s_alveolar(self):
        r = bare(_g("pt-BR-x-pr").transcribe_word("costas"))
        assert "ʃ" not in r and "h" not in r

    def test_l_vocalisation(self):
        assert bare(_g("pt-BR-x-pr").transcribe_word("sal")).endswith("w")


# ─── pt-BR-x-recife (Pernambucano) ──────────────────────────────────────────


class TestRecife:
    def test_no_palatalisation_tia(self):
        """tia -> [ˈtiɐ]: the strongest north/south isogloss (no affrication)."""
        r = bare(_g("pt-BR-x-recife").transcribe_word("tia"))
        assert r.startswith("t") and "t͡ʃ" not in r

    def test_no_palatalisation_leite(self):
        r = bare(_g("pt-BR-x-recife").transcribe_word("leite"))
        assert "t͡ʃ" not in r

    def test_open_pretonic_before_low_vowel(self):
        """Mota & Lopes 2018: 215: pretonic mid vowels open before a stressed
        /a/: pedaço, bolacha."""
        assert bare(_g("pt-BR-x-recife").transcribe_word("pedaço")).startswith("pɛ")
        assert bare(_g("pt-BR-x-recife").transcribe_word("bolacha")).startswith("bɔ")

    def test_closed_pretonic_before_high_vowel(self):
        """Mota & Lopes 2018: 215 (Tab. 4): before a high stressed vowel the
        closed vowel is the majority."""
        assert bare(_g("pt-BR-x-recife").transcribe_word("menino")).startswith("me")

    def test_plural_raised(self):
        """The palatal plural raises like the base one: dentes."""
        assert bare(_g("pt-BR-x-recife").transcribe_word("dentes")) == "dẽtiʃ"

    def test_final_r_deleted(self):
        """Callou, Serra & Cunha 2015: 207: word-final /R/ deletion 98 % in
        Recife verbs."""
        assert bare(_g("pt-BR-x-recife").transcribe_word("falar")) == "fala"

    def test_coda_s_palatal(self):
        assert "ʃ" in bare(_g("pt-BR-x-recife").transcribe_word("mesmo"))


# ─── pt-BR-x-norte (Amazônico) ──────────────────────────────────────────────


class TestNorte:
    def test_closed_pretonic(self):
        """Mota & Lopes 2018: 217: the North is not an open-pretonic area."""
        assert bare(_g("pt-BR-x-norte").transcribe_word("pedaço")).startswith("pe")

    def test_affrication_before_raised_plural(self):
        """Oliveira 2013: 216: Belém palatalisation 88 %; the palatal plural
        raises."""
        assert bare(_g("pt-BR-x-norte").transcribe_word("dentes")) == "dẽt͡ʃiʃ"

    def test_palatalisation_retained(self):
        """North has high /t,d/ palatalisation (ALiB), unlike the NE proper."""
        assert "t͡ʃ" in bare(_g("pt-BR-x-norte").transcribe_word("tia"))

    def test_coda_s_palatal(self):
        assert "ʃ" in bare(_g("pt-BR-x-norte").transcribe_word("mesmo"))

    def test_l_vocalisation(self):
        assert bare(_g("pt-BR-x-norte").transcribe_word("sol")).endswith("w")


# ─── pt-BR-x-bahia (resolution) ─────────────────────────────────────────────


class TestBahia:
    def test_palatalisation_retained_before_i(self):
        """Resolved: Salvador palatalises /t,d/ before /i/ (africadas baianas)."""
        assert "t͡ʃ" in bare(_g("pt-BR-x-bahia").transcribe_word("tia"))
        assert "d͡ʒ" in bare(_g("pt-BR-x-bahia").transcribe_word("dia"))

    def test_open_pretonic_before_low_vowel(self):
        """Mota & Lopes 2018: 215, 217: Bahia patterns with the Northeast."""
        assert bare(_g("pt-BR-x-bahia").transcribe_word("pedaço")).startswith("pɛ")

    def test_final_em_diphthong(self):
        """Barbosa & Albano 2004: 230: final -em is the nasal diphthong."""
        assert bare(_g("pt-BR-x-bahia").transcribe_word("quem")) == "kẽj̃"
        assert bare(_g("pt-BR-x-bahia").transcribe_word("homem")).endswith("mẽj̃")

    def test_coda_s_alveolar_not_palatal(self):
        """Bahian interior keeps coda /S/ alveolar — NOT the Carioca chiado."""
        r = bare(_g("pt-BR-x-bahia").transcribe_word("mesmo"))
        assert "ʃ" not in r and "ʒ" not in r

    def test_lh_weakening_available(self):
        # /ʎ/ -> [j] is an allowed allophone (velho); base form also valid.
        assert "ʎ" in get("pt-BR-x-bahia").allophones


# ─── pt-BR-x-ce (Cearense, resolution) ──────────────────────────────────────


class TestCE:
    def test_palatalisation_retained(self):
        """Resolved: Fortaleza prestige norm palatalises /t,d/ before /i/."""
        assert "t͡ʃ" in bare(_g("pt-BR-x-ce").transcribe_word("tia"))

    def test_affrication_before_raised_e(self):
        """Battisti & Dornelles Filho 2015: 226: Fortaleza is categorical."""
        assert bare(_g("pt-BR-x-ce").transcribe_word("gente")) == "ʒẽt͡ʃi"

    def test_open_pretonic_before_low_vowel(self):
        assert bare(_g("pt-BR-x-ce").transcribe_word("pedaço")).startswith("pɛ")

    def test_coda_s_alveolar_before_voiceless(self):
        """Marins & Margotti 2012: 257: Fortaleza keeps the alveolar."""
        assert bare(_g("pt-BR-x-ce").transcribe_word("costas")).startswith("kost")

    def test_coda_s_aspirated_before_d(self):
        """Toledo & Cantoni 2021: 27: 52 % aspiration before /d/ (DSC)."""
        assert bare(_g("pt-BR-x-ce").transcribe_word("desde")).startswith("deh")

    def test_final_s_not_aspirated(self):
        # word-final /S/ stays [s], not aspirated.
        assert bare(_g("pt-BR-x-ce").transcribe_word("mais")).endswith("s")


# ─── pt-BR-x-brasilia (koiné) ───────────────────────────────────────────────


class TestBrasilia:
    def test_code_is_alias_of_base(self):
        """No opened source separates Brasília from the base (Hora 1999: 35,
        alveolar coda /S/), so the code reads pt-BR."""
        assert get("pt-BR-x-brasilia").code == "pt-BR"
        for w in ("tia", "mesmo", "porta", "carro"):
            assert _g("pt-BR-x-brasilia").transcribe_word(w) == _g("pt-BR").transcribe_word(w)
