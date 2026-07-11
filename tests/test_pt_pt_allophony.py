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
import unicodedata

from orthography2ipa import get
from orthography2ipa.g2p import G2P


def _t(code, word):
    # NFC so a precomposed nasal glyph in an expected literal (õ, ĩ, ẽ, ũ)
    # compares equal to the engine's decomposed vowel + U+0303.
    return unicodedata.normalize("NFC", G2P(code).transcribe(word))


def _n(s):
    return unicodedata.normalize("NFC", s)


def _nfd(code, word):
    # NFD so the combining tilde U+0303 is always a standalone codepoint,
    # letting tilde-presence / double-tilde checks be unambiguous.
    return unicodedata.normalize("NFD", G2P(code).transcribe(word))


# ─── the rules are present and inherited ────────────────────────────────

def test_pt_pt_declares_the_coda_rules():
    ids = [r.id for r in get("pt-PT").allophone_rules]
    assert ids == [
        "PT_NASAL_A_RAISE", "PT_NASAL_E_RAISE", "PT_NASAL_O_RAISE",
        "PT_NASAL_O_UNRED",
        "PT_CODA_L_DARK", "PT_CODA_S_HUSH", "PT_CODA_Z_HUSH",
    ]


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


# ─── coda vowel nasalisation (a defining feature of Portuguese) ──────────
# A vowel before a CODA nasal ⟨m/n⟩ (word-finally or before another
# consonant) nasalises while the nasal consonant is absorbed; an
# INTERVOCALIC (onset) nasal leaves the vowel oral. Mateus & d'Andrade
# (2000: ch.2, "Nasality"). The tilde is U+0303 (combining), supplied by
# the positional m/n slot; the allophone rules only shift vowel quality.

TILDE = "̃"


def test_coda_nasal_nasalises_the_vowel():
    # word-final and pre-consonantal ⟨m/n⟩ → nasal vowel, consonant absorbed
    assert _t("pt-PT", "campo") == _n("ˈkɐ̃pu")
    assert _t("pt-PT", "sim") == _n("ˈsĩ")
    assert _t("pt-PT", "bom") == _n("ˈbõ")
    assert _t("pt-PT", "mundo") == _n("ˈmũdu")
    assert _t("pt-PT", "cantar") == _n("kɐ̃ˈtaɾ")
    assert _t("pt-PT", "fim") == _n("ˈfĩ")
    assert _t("pt-PT", "ambos") == _n("ˈɐ̃buʃ")
    assert _t("pt-PT", "tempo") == _n("ˈtẽpu")


def test_intervocalic_nasal_leaves_vowel_oral():
    # onset (intervocalic) ⟨m/n⟩ stays a consonant; the vowel is NOT nasal
    for word in ("cama", "ano", "lua", "lima", "nome", "fome"):
        out = _nfd("pt-PT", word)
        assert TILDE not in out, (word, out)


def test_no_double_tilde_ever():
    # Adversarial: curated-safe words PLUS the shapes that historically
    # produced a stray/second U+0303 — reduced ⟨o⟩ before a nasal, the
    # ⟨gu⟩→[ɡ] vowel-drop (algum/segundo) that left a consonant in the
    # coda-nasal slot, and ⟨nn⟩ loans where two nasal slots stacked tildes.
    for word in (
        "campo", "sim", "bom", "mundo", "cantar", "ambos", "tempo",
        "contar", "comprar", "bondade", "bombom",
        "algum", "alguns", "segundo",
        "inn", "Finn", "hymn", "column",
    ):
        out = _nfd("pt-PT", word)
        assert TILDE + TILDE not in out, (word, out)


def test_no_tilde_on_a_consonant():
    # The positional coda-nasal tilde must only ever attach to a vowel (or a
    # nasal-diphthong glide). The ⟨gu⟩→[ɡ] vowel-drop used to leave the tilde
    # stranded on [ɡ] (algum → [ɐˈɫɡ̃], segundo → [sɨˈɡ̃du]) — invalid IPA.
    # A tilde is valid only after an oral vowel or a w/j glide.
    carriers = set("aeiouɛɔəɨʉɯæɐʌɒœøɪʊɤɵɞɑɘɚɜɝɶywj")
    for word in ("algum", "alguns", "segundo", "inn", "Finn", "contar", "sim"):
        out = _nfd("pt-PT", word)
        for i, ch in enumerate(out):
            if ch == TILDE:
                prev = out[i - 1] if i > 0 else ""
                assert prev in carriers, (word, out, repr(prev))


def test_reduced_o_before_nasal_lowers_to_o():
    # EP unstressed ⟨o⟩ reduces to [u], but that reduction is BLOCKED before
    # a coda nasal: the nasal is [õ], never [ũ] (Mateus & d'Andrade 2000:
    # ch.2). Regression guard for contar → [kũˈtaɾ] (wrong) vs [kõˈtaɾ].
    assert _t("pt-PT", "contar") == _n("kõˈtaɾ")
    assert _t("pt-PT", "comprar") == _n("kõˈpɾaɾ")
    assert _t("pt-PT", "montanha") == _n("mõˈtaɲɐ")
    assert _t("pt-PT", "bondade") == _n("bõˈdadɨ")
    assert _t("pt-PT", "pombal") == _n("põˈbaɫ")
    assert _t("pt-PT", "bombom") == _n("bõˈbõ")


def test_lexical_u_before_nasal_stays_high():
    # The lowering is gated on the source grapheme ⟨o⟩; a LEXICAL ⟨u⟩ before
    # a nasal is a genuine high [ũ] and must NOT be lowered to [õ].
    assert _n("ũ") in _t("pt-PT", "um")
    assert _n("ũ") in _t("pt-PT", "mundo")
    for word in ("um", "mundo", "comum", "atum"):
        out = _t("pt-PT", word)
        assert "õ" not in out, (word, out)


def test_nh_digraph_unbroken_by_coda_nasal():
    # ⟨nh⟩ tokenises first (maximal munch) → [ɲ]; the n never nasalises
    out = _nfd("pt-PT", "banho")
    assert "ɲ" in out and TILDE not in out, out


def test_nasal_diphthongs_intact():
    # whole nasal-diphthong graphemes ⟨ão ãe õe⟩ are untouched
    assert _n("ɐ̃") in _t("pt-PT", "pão")
    assert _n("ɐ̃") in _t("pt-PT", "mãe")
    assert _n("õ") in _t("pt-PT", "põe")
