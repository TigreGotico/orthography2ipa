"""Lusophone Asian Portuguese: East Timorese (pt-TL) and Macau (pt-MO).

These are the L2/official European-derived Portuguese varieties of Timor-Leste
and the Macau SAR — NOT the Portuguese-based creoles of the region (Bidau
Creole Portuguese in Timor; Patuá/maquista in Macau), which are separate
contact languages.

pt-TL is grounded in Albuquerque, D.B. (2010) "Peculiaridades prosódicas do
português falado em Timor Leste", ReVEL 8(15):270-285 (read in full). Its
headline modelled feature is the ABSENCE of European Portuguese unstressed
vowel reduction: the Austronesian (Tetum) substrate keeps full vowels
(Albuquerque 2010:275, fn.7 — bate [ˈba.te], roda [ˈɾɔ.da]).

pt-MO is deliberately kept at skeleton tier: no citable phonological
description of Macau Portuguese proper (vs. the Patuá creole) could be read,
so it inherits the European norm and documents the thin literature honestly.
"""
from orthography2ipa import get
from orthography2ipa.g2p import G2P


def _t(code, word):
    return G2P(code).transcribe(word)


# ─── tiers, sources, creole distinction ─────────────────────────────────

def test_pt_tl_is_research_with_primary_source():
    spec = get("pt-TL")
    assert spec.quality.value == "research"
    ids = {s.id if hasattr(s, "id") else s["id"] for s in spec.sources}
    assert "albuquerque2010" in ids


def test_pt_mo_stays_skeleton_honestly():
    # Macau Portuguese phonology is under-documented; the spec must not
    # over-claim a research tier it cannot ground in a read source.
    assert get("pt-MO").quality.value == "skeleton"


def test_both_are_por_not_creoles():
    # ISO 639-3 'por' = Portuguese, not a creole language code.
    for code in ("pt-TL", "pt-MO"):
        assert get(code).iso639_3 == "por"


# ─── pt-TL: no unstressed vowel reduction (the core feature) ────────────

def test_pt_tl_has_no_schwa_reduction():
    # Albuquerque 2010:275 fn.7 — unstressed vowels keep full quality;
    # EP's schwa [ə]/[ɐ] and [ɨ] must NOT appear.
    for word in ("bate", "roda", "mesa", "chave", "comer"):
        out = _t("pt-TL", word)
        assert "ə" not in out and "ɐ" not in out and "ɨ" not in out, (word, out)


def test_pt_tl_full_final_vowels():
    # bate [ˈbate] (final e stays [e], not [ɨ]); roda [ˈrɔda] (final a [a]).
    assert _t("pt-TL", "bate").endswith("e")
    assert _t("pt-TL", "roda").endswith("a")


def test_pt_pt_still_reduces_by_contrast():
    # The parent variety keeps EP reduction — proves pt-TL overrides it.
    assert _t("pt-PT", "bate").endswith("ɨ")
    assert "ɐ" in _t("pt-PT", "roda")


def test_pt_tl_stressed_vowels_keep_ep_quality():
    # Only unstressed reduction is removed; stressed mid vowels keep the
    # EP open/close contrast (roda [ˈrɔda], mesa [ˈmɛza]).
    assert "ɔ" in _t("pt-TL", "roda")
    assert "ɛ" in _t("pt-TL", "mesa")


# ─── pt-TL: alveolar rhotic, no uvular ──────────────────────────────────

def test_pt_tl_rhotic_is_alveolar_not_uvular():
    for word in ("roda", "comer", "mar", "carro"):
        out = _t("pt-TL", word)
        assert "ʁ" not in out and "χ" not in out, (word, out)


# ─── pt-TL: digraph simplification lh→l, nh→n ───────────────────────────

def test_pt_tl_digraph_simplification():
    # Albuquerque 2010:276 — olho [ˈo.liu], vinho [ˈbi.niu]: ⟨lh⟩→[l],
    # ⟨nh⟩→[n] as the modelled (first) variant.
    assert "l" in _t("pt-TL", "olho") and "ʎ" not in _t("pt-TL", "olho")
    assert "n" in _t("pt-TL", "vinho") and "ɲ" not in _t("pt-TL", "vinho")


# ─── pt-TL: alveolar coda /s/ (no obligatory chiado) ────────────────────

def test_pt_tl_coda_s_is_alveolar():
    # escola [isˈkɔla] ~ [iʃˈkɔla] — alveolar taken as the norm
    # (Albuquerque 2010:277). The inherited hush rules are overridden.
    out = _t("pt-TL", "escola")
    assert "s" in out and "ʃ" not in out, out
    ids = [r.id for r in get("pt-TL").allophone_rules]
    assert "PT_CODA_S_HUSH" in ids and "PT_CODA_Z_HUSH" in ids


# ─── inheritance from pt-PT ─────────────────────────────────────────────

def test_pt_tl_inherits_pt_pt_base():
    spec = get("pt-TL")
    assert spec.parent == "pt-PT"
    # coda-l darkening rule is inherited unchanged (not sourced to alter).
    assert "PT_CODA_L_DARK" in [r.id for r in spec.allophone_rules]


def test_pt_mo_follows_european_norm():
    # Macau PT "closely follows the standard European dialect" — uvular
    # rhotic and EP reduction are retained (flagged secondary source).
    assert "ʁ" in _t("pt-MO", "mar")
    assert _t("pt-MO", "bate").endswith("ɨ")


# ─── whole words transcribe without error ───────────────────────────────

def test_whole_words_transcribe():
    for code in ("pt-TL", "pt-MO"):
        g = G2P(code)
        for word in ("Timor", "português", "escola", "professor", "cidade"):
            out = g.transcribe(word)
            assert isinstance(out, str) and out, (code, word)
