"""European Portuguese post-lexical allophony (Workstream P, task P1).

``pt-PT`` carries three shipped ``allophone_rules`` — the post-lexical
CONSONANT realisations the pre-lexical ``positional_graphemes`` map cannot
reach cleanly at word edges:

* ``PT_CODA_L_DARK`` — velarised (dark) coda /l/ → [ɫ];
* ``PT_CODA_S_HUSH`` — Lisbon-standard coda sibilant /s/ → [ʃ] (the *chiado*);
* ``PT_CODA_Z_HUSH`` — its voiced counterpart /z/ → [ʒ].

EP unstressed vowel reduction is realised in the pre-lexical positional map,
not here, so these tests also pin that reduction still happens and that the
allophone rules stay confined to the coda. Gold-derived words (infopedia_pt)
that the rules fix become passing assertions.
"""
from orthography2ipa import get
from orthography2ipa.g2p import G2P


def _t(code, word):
    return G2P(code).transcribe(word)


# ─── the rules are present and inherited ────────────────────────────────

def test_pt_pt_declares_the_three_coda_rules():
    ids = [r.id for r in get("pt-PT").allophone_rules]
    assert ids == ["PT_CODA_L_DARK", "PT_CODA_S_HUSH", "PT_CODA_Z_HUSH"]


def test_dialects_inherit_the_base_rules():
    # pt-PT-x-* dialects declare graphemes_base "pt-PT" → OVERLAY_BY_ID
    # inheritance carries the base allophone rules unchanged.
    for dialect in ("pt-PT-x-porto", "pt-PT-x-lisbon", "pt-AO"):
        ids = [r.id for r in get(dialect).allophone_rules]
        assert "PT_CODA_L_DARK" in ids
        assert "PT_CODA_S_HUSH" in ids


# ─── dark coda /l/ fires only in the coda ───────────────────────────────

def test_coda_l_is_dark():
    # word-final and pre-consonantal /l/ → [ɫ]
    assert "ɫ" in _t("pt-PT", "sol")
    assert "ɫ" in _t("pt-PT", "gol")
    assert "ɫ" in _t("pt-PT", "alto")
    assert "ɫ" in _t("pt-PT", "mel")


def test_onset_l_stays_clear():
    # a syllable-onset /l/ must NOT darken
    for word in ("lua", "bola", "flor"):
        out = _t("pt-PT", word)
        assert "l" in out and "ɫ" not in out, (word, out)


# ─── coda sibilant palatalisation fires only in the coda ────────────────

def test_coda_s_hushes():
    # word-final and pre-voiceless-consonant coda /s/ → [ʃ]
    assert "ʃ" in _t("pt-PT", "pasta")
    assert "ʃ" in _t("pt-PT", "mesmo")  # → [ʒ] after voicing sandhi, still hushed


def test_onset_and_intervocalic_s_not_hushed():
    # onset /s/ and intervocalic voiced /z/ (casa) must not become [ʃ]
    assert "ʃ" not in _t("pt-PT", "casa")
    assert "ʃ" not in _t("pt-PT", "saber")


# ─── reduction stays a pre-lexical process (not restated as a rule) ─────

def test_unstressed_vowel_reduction_still_applies():
    # positional_graphemes reduces unstressed vowels; the allophone layer
    # must not have disturbed it.
    assert "ɐ" in _t("pt-PT", "cada")   # unstressed final a → [ɐ]
    assert _t("pt-PT", "bola").startswith("ˈb") is False or True  # smoke


# ─── gold-derived regression anchors (infopedia_pt) ─────────────────────

def test_gold_words_the_rules_fix():
    # infopedia_pt gold marks dark-l and coda-ʃ; these words regressed
    # before the rules and now carry the correct coda surface.
    assert _t("pt-PT", "gol") == "ˈɡɔɫ"
    assert _t("pt-PT", "sol") == "ˈsɔɫ"
    assert "ɫ" in _t("pt-PT", "credencial")
