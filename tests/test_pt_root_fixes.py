"""Root-cause conformance tests for the Portuguese-cluster fixes.

Each test takes ONE cited claim and proves the shared engine / base-spec now
honours it, isolating the change to a single segment and, where the phonology
allows, using a minimal pair (same word under a sibling or parent lect). The
leads these cover were surfaced while authoring the ``portuguese_tts`` gold
sets; the fixes live in the base ``roa-x-galaicopt`` / ``pt-PT-x-medieval``
specs, the per-lect override tables, and the shared positional engine — never
in per-word patches.
"""
import unicodedata

import pytest

from orthography2ipa import transcribe


def _t(code, word):
    # NFC so a precomposed nasal glyph compares equal to the engine's
    # decomposed vowel + combining tilde and vice-versa.
    return unicodedata.normalize("NFC", transcribe(word, code))


def _bare(code, word):
    return _t(code, word).replace("ˈ", "").replace("ˌ", "")


# ===========================================================================
# Soft ⟨g⟩ before front vowels — [ʒ] in every modern Portuguese variety.
# "⟨g⟩ before ⟨e i⟩ is realised as the palato-alveolar fricative [ʒ]"
# (Mateus & d'Andrade 2000, The Phonology of Portuguese, ch. 2).
# Historical affricate [d͡ʒ] in Galaico-Portuguese, deaffricated to [ʒ] by the
# Old-Portuguese period (Teyssier 1982; Williams, From Latin to Portuguese).
# ===========================================================================
@pytest.mark.parametrize("code", ["pt-PT", "pt-BR", "pt-AO", "pt-PT-x-lisbon"])
def test_soft_g_before_e_i_is_zh(code):
    assert "ʒ" in _t(code, "gente")
    assert "ʒ" in _t(code, "girafa")
    assert "ʒ" in _t(code, "longe")


def test_soft_g_deaffrication_medieval_vs_galaicopt():
    # minimal pair on the same word: the affricate survives in the older lect,
    # deaffricates in Old Portuguese and its descendants.
    assert "d͡ʒ" in _bare("roa-x-galaicopt", "gente")
    assert "ʒ" in _bare("pt-PT-x-medieval", "gente")
    assert "d͡ʒ" not in _bare("pt-PT-x-medieval", "gente")


def test_hard_gu_digraph_keeps_g_before_e_i():
    # the fix must not turn the silent-u ⟨gu⟩ digraph into [ʒ]
    assert _bare("pt-PT", "guerra").startswith("ɡ")
    assert _bare("pt-PT", "guitarra").startswith("ɡ")


# ===========================================================================
# Accented front vowels still soften a preceding ⟨c g⟩ (generic engine).
# ⟨ê é⟩ are front vowels (they only differ from ⟨e⟩ in height/marking), so
# ⟨gê cê⟩ soften exactly like ⟨ge ce⟩ — the front/back softening axis is
# diacritic-invariant (Mateus & d'Andrade 2000, ch. 2).
# ===========================================================================
def test_soft_c_g_before_circumflex_front_vowel():
    assert "ʒ" in _t("pt-BR", "gênero")   # was [ɡ] before the fix
    assert _bare("pt-PT", "cê").startswith("s")  # soft-c before ⟨ê⟩ → [s]


def test_voce_northern_betacism_not_velar():
    # Northern EP betacism v→b is real, but ⟨c⟩ before ⟨ê⟩ must be [s], never
    # [k]: você → [buˈse]-type, not the implausible [buˈke].
    out = _bare("pt-PT-x-braga", "você")
    assert "k" not in out
    assert "s" in out


# ===========================================================================
# Accented vowels are never deleted in the historical lects; a written accent
# attracts stress rather than being dropped (an accented grapheme must map to
# its plain quality — deletion is always wrong).
# ===========================================================================
@pytest.mark.parametrize("code", ["pt-PT-x-medieval", "roa-x-galaicopt"])
@pytest.mark.parametrize("word,vowel", [("está", "a"), ("café", "ɛ"), ("avô", "o")])
def test_accented_vowels_not_deleted(code, word, vowel):
    out = _t(code, word)
    assert vowel in out, f"{code} {word} -> {out!r} dropped its accented vowel"
    assert out.endswith(vowel)  # oxytone: the final accented vowel survives


def test_galaicopt_emits_stress():
    # Galaico-Portuguese was paroxytone-by-default with oxytone consonant
    # endings, like its descendants; the transcriber must mark stress.
    assert "ˈ" in _t("roa-x-galaicopt", "amigo")
    assert "ˈ" in _t("roa-x-galaicopt", "cantar")


# ===========================================================================
# Medieval nasalisation: a coda ⟨n m⟩ nasalises the preceding vowel (canto,
# campo, dente). Old Portuguese had phonemic nasal vowels and automatic
# regressive nasalisation before a tautosyllabic nasal (Williams, From Latin
# to Portuguese; Mattos e Silva, O Português Arcaico). Target quality is the
# base vowel + tilde ([ã], not the modern raised [ɐ̃]). This also fixes the
# stress artifact: with the nasal absorbed there is no stranded coda to be
# mis-parsed as an onset, so ⟨cantar⟩ syllabifies kã.ˈtar.
# ===========================================================================
def test_medieval_coda_nasalisation_and_stress():
    assert _t("pt-PT-x-medieval", "cantar") == "kãˈtaɾ"
    assert "̃" in unicodedata.normalize("NFD", _t("pt-PT-x-medieval", "campo"))
    assert "ɐ̃" not in _t("pt-PT-x-medieval", "campo")  # base-vowel quality, not raised


# ===========================================================================
# ⟨gu⟩/⟨qu⟩ are the silent-u digraph only before ⟨e i⟩; elsewhere the ⟨u⟩ is a
# pronounced [w] (before ⟨a o⟩) or a full vowel [u] (before a consonant). The
# digraph must not swallow a stressed nucleus (Cunha & Cintra, Nova Gramática,
# §Ortografia; Mateus & d'Andrade 2000).
# ===========================================================================
@pytest.mark.parametrize("code", ["pt-PT", "pt-BR"])
def test_gu_qu_digraph_only_before_front_vowels(code):
    assert "u" in _t(code, "agudo")          # a.gu.do — u is the stressed vowel
    assert "w" in _t(code, "água")           # á.gua — [ˈaɡwɐ]
    assert "u" in _t(code, "legumes")        # le.gu.mes — pretonic u survives
    assert "w" in _t(code, "quatro")         # qua → [kwa]
    assert _bare(code, "aquele").count("k") == 1  # que → [k], silent u


# ===========================================================================
# African-lect coda / rhotic overrides.
# ===========================================================================
def test_gw_final_z_is_alveolar():
    # "alveolar [s] in coda (no palatalisation)" (pt-GW notes; Couto 1994).
    # Word-final ⟨z⟩ must devoice to [s], not hush to [ʃ].
    assert _t("pt-GW", "paz").endswith("s")
    assert _t("pt-GW", "luz").endswith("s")


def test_cv_coda_z_alveolar_and_initial_r_trill():
    # Cape-Verde coda ⟨z⟩ patterns with ⟨s⟩ → [s]; strong-R is the alveolar
    # trill [r], word-initial ⟨r⟩ included (not just ⟨rr⟩).
    assert _t("pt-CV", "paz").endswith("s")
    assert _bare("pt-CV", "rato").startswith("r")
    assert "ʁ" not in _t("pt-CV", "rato")


def test_mo_intervocalic_r_is_tap():
    # Macau Portuguese (EP-based): single intervocalic ⟨r⟩ is the tap [ɾ];
    # strong-R positions (word-initial, ⟨rr⟩) stay uvular.
    assert "ɾ" in _t("pt-MO", "caro")
    assert "ʁ" not in _t("pt-MO", "caro")
    assert _bare("pt-MO", "rato").startswith("ʁ")   # word-initial strong-R


# ===========================================================================
# PALOP five-vowel systems: pretonic /e o/ stay unreduced (no [ɨ]).
# pt-ST: "FIVE-VOWEL SYSTEM: no /ɨ/; full unstressed vowels" (Ferraz 1979,
# Hagemeijer 2009). pt-GW: "/ɨ/ absent; full articulation of unstressed
# vowels" (Couto 1994, Kihm 1994).
# ===========================================================================
@pytest.mark.parametrize("code", ["pt-ST", "pt-GW"])
def test_palop_no_pretonic_reduction(code):
    assert "ɨ" not in _t(code, "menino")     # EP would give mɨˈninu
    assert "ɨ" not in _t(code, "cebola")
    assert _bare(code, "moderno").startswith("mo")  # pretonic o stays [o]
