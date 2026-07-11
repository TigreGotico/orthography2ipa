"""Insular European Portuguese dialects (Workstream P, task P3).

Two dialects modelled as deltas on the inherited ``pt-PT`` base:

* ``pt-PT-x-acores`` (Azorean) — the São Miguel-class fronting of a stressed
  open-syllable /u/ to a front rounded [y] (número → [ˈnymɨɾu], tu → [ty]),
  blocked before a tautosyllabic coda liquid/sibilant (azul → [ɐˈzuɫ]), plus
  /ow/ preservation in the ⟨ou⟩ digraph.
* ``pt-PT-x-madeira`` (Madeiran) — intervocalic /l/ → [ʎ] after /i/
  (quilo → [ˈkiʎu], mochila → [muˈʃiʎɐ]) and the nasal-diphthong → nasal+N
  reduction (cães → [kɐ̃ns]).

The fronting rule must NEVER fire on a proclitic the stress detector marks as
stressed: the article/contraction ``o``/``do``/``no``/``ao`` is [u], never [y]
(a sibling spec once shipped exactly this bug). The clitic guard is pinned in
``word_exceptions`` and exercised below.
"""
from orthography2ipa import get
from orthography2ipa.g2p import G2P


def _t(code, word):
    return G2P(code).transcribe(word)


def _ns(code, word):
    """Transcription with primary/secondary stress marks stripped."""
    return _t(code, word).replace("ˈ", "").replace("ˌ", "")


# ─── inheritance: island specs keep the pt-PT base allophony ─────────────

def test_islands_inherit_base_coda_rules():
    for dialect in ("pt-PT-x-acores", "pt-PT-x-madeira"):
        ids = [r.id for r in get(dialect).allophone_rules]
        assert "PT_CODA_L_DARK" in ids
        assert "PT_CODA_S_HUSH" in ids
    # dark coda /l/ still fires (inherited, not overridden)
    assert "ɫ" in _t("pt-PT-x-acores", "sol")
    assert "ɫ" in _t("pt-PT-x-madeira", "mel")


def test_islands_declare_their_own_rules():
    aco = [r.id for r in get("pt-PT-x-acores").allophone_rules]
    assert "ACO_STRESSED_U_FRONTING" in aco
    assert "ACO_U_KEEP_BEFORE_CODA" in aco
    mad = [r.id for r in get("pt-PT-x-madeira").allophone_rules]
    assert "MAD_L_PALATALISATION" in mad


# ─── Azorean: stressed open /u/ → [y] fronting ──────────────────────────

def test_acores_fronts_stressed_open_u():
    # stressed /u/ before an onset consonant fronts to [y]
    assert "y" in _t("pt-PT-x-acores", "número")
    assert _t("pt-PT-x-acores", "número") == "ˈnymɨɾu"
    # the lexical shibboleth tu
    assert "y" in _t("pt-PT-x-acores", "tu")


def test_acores_fronting_blocked_before_coda():
    # a stressed /u/ before a tautosyllabic coda liquid stays [u]
    assert "y" not in _t("pt-PT-x-acores", "azul")
    assert _t("pt-PT-x-acores", "azul") == "ɐˈzuɫ"
    assert "y" not in _t("pt-PT-x-acores", "Furnas")


def test_acores_fronting_needs_stress():
    # an unstressed /u/ never fronts (pretonic / final)
    assert "y" not in _t("pt-PT-x-acores", "cozido")   # pretonic u
    assert "y" not in _t("pt-PT-x-acores", "rápido")   # final unstressed u


def test_acores_ow_preserved():
    # ⟨ou⟩ keeps the falling diphthong where Lisbon monophthongises
    assert "ow" in _ns("pt-PT-x-acores", "touradas")


# ─── the clitic guard: article/contraction o is [u], never [y] ──────────

def test_acores_article_o_is_u_not_y():
    assert _ns("pt-PT-x-acores", "o") == "u"
    assert "y" not in _t("pt-PT-x-acores", "o")


def test_acores_proclitic_contractions_are_u_forms():
    for clitic, expected in (
        ("os", "uʃ"), ("no", "nu"), ("nos", "nuʃ"),
        ("do", "du"), ("dos", "duʃ"), ("ao", "aw"), ("aos", "awʃ"),
    ):
        got = _ns("pt-PT-x-acores", clitic)
        assert got == expected, f"{clitic} → {got!r} (want {expected!r})"
        assert "y" not in got


# ─── Madeiran: intervocalic /l/ → [ʎ] after /i/ ─────────────────────────

def test_madeira_palatalises_l_after_i():
    assert _t("pt-PT-x-madeira", "quilo") == "ˈkiʎu"
    assert _t("pt-PT-x-madeira", "mochila") == "muˈʃiʎɐ"
    assert "ʎ" in _t("pt-PT-x-madeira", "vila")


def test_madeira_l_palatalisation_only_after_i():
    # /l/ after a reduced [ɨ] (from ⟨e⟩) is NOT palatalised
    assert "ʎ" not in _t("pt-PT-x-madeira", "teleférico")
    # onset /l/ not preceded by /i/ stays clear
    assert "ʎ" not in _t("pt-PT-x-madeira", "levada")


def test_madeira_nasal_plus_n():
    assert _t("pt-PT-x-madeira", "cães") == "ˈkɐ̃ns"


def test_madeira_keeps_v_no_betacism():
    # Madeiran has no betacism: /v/ stays [v]
    assert "v" in _t("pt-PT-x-madeira", "levada")
    assert "b" not in _t("pt-PT-x-madeira", "visitar")


# ─── base inheritance sanity: reduction still applies ───────────────────

def test_islands_inherit_unstressed_reduction():
    # unstressed final -o → [u], pretonic -e → [ɨ] as in the base
    for dialect in ("pt-PT-x-acores", "pt-PT-x-madeira"):
        assert _t(dialect, "gato").endswith("u")
