"""West Sudanic Arabic phonology: the rules that separate a Chadian (ar-TD) and
a Nigerian/Shuwa (ar-NG) transcription from Mashriqi Arabic, and ar-NG from its
parent ar-TD.

Chadian and Nigerian Arabic form the western ('Lake Chad') end of the Sudanic
Arabic chain, Arabicised by Bedouin migration out of Upper Egypt from ~14th c.
ar-NG is declared as a delta on ar-TD: it completes the interdental merger that
Chad only variably applies.

Every claim below is isolated on a real (diacritized) Arabic word and cited from:

* Jonathan Owens (1993) *A Grammar of Nigerian Arabic* (Harrassowitz) — the
  primary grammar of the chain;
* Jonathan Owens (2006) *A Linguistic History of Arabic* (OUP), read in full
  text: p.25 (loss of interdentals; six phonemic emphatics /tˤ dˤ sˤ ðˤ/ +
  /lˤ rˤ mˤ/ with minimal pairs; /a/-insertion after gutturals, ahamar <
  *ʔaḥmar), p.19 (*t > [ɗˤ] from Fulfulde contact);
* Alan S. Kaye (1976) *Chadian and Sudanese Arabic…* (Mouton);
* Jullien de Pommerol (1999) *Grammaire pratique de l'arabe tchadien* (Karthala);
* Roth-Laly (1979) for Abéché Chadian and Procházka (2026, JSS, p.310, 318) for
  the gahawa syndrome.

Expectations carry the engine's default primary-stress mark; the scoreboard
strips stress from both sides so it costs no PER.
"""
import pytest

from orthography2ipa import transcribe, get


# ─── Shared metadata: both are research tier off the West Sudanic chain ─────

def test_both_specs_are_research_tier_with_the_primary_grammar_cited():
    """ar-TD and ar-NG must both declare research quality and cite Owens (1993),
    the primary grammar of the West Sudanic chain, plus the full-text Owens
    (2006) and the gahawa survey Procházka (2026)."""
    for code in ("ar-TD", "ar-NG"):
        spec = get(code)
        assert spec.quality.value == "research"
        ids = {s.id for s in spec.sources}
        assert {"owens1993", "owens2006", "prochazka2026"} <= ids


def test_nigerian_is_a_delta_on_chadian():
    """ar-NG inherits from ar-TD (the coupled inheritance chain), and ar-TD from
    the Mashriqi (eastern Bedouin) base — the migration path out of Upper Egypt
    (Owens & Hassan 2009, via Procházka 2026 p.325)."""
    assert get("ar-NG").parent == "ar-TD"
    assert get("ar-TD").parent == "ar-x-mashriqi"


# ─── qāf: the Bedouin-type voiced reflex ────────────────────────────────────

def test_qaf_is_voiced_g_with_q_in_learned_words():
    """qāf ق → /ɡ/ (gāl 'he said'), the defining Bedouin-type reflex of West
    Sudanic Arabic, with /q/ retained only in learned/Classical borrowings, so
    the grapheme lists [ɡ, q] (Owens 1993; Kaye 1976; de Pommerol 1999)."""
    for code in ("ar-TD", "ar-NG"):
        assert get(code).graphemes["ق"] == ["ɡ", "q"]
        assert transcribe("قَالَ", code) == "ˈɡaːla"


# ─── ǧīm: /dʒ/ with the areal palatal-stop variant ──────────────────────────

def test_jim_is_dzh_with_a_palatal_stop_variant():
    """ǧīm ج → /dʒ/, with a palatal-stop variant [ɟ] shared with neighbouring
    Sudanese Arabic (ar-SD, whose ج is /ɟ/); جَمَل 'camel' → [dʒamal]. Inherited
    by ar-NG from ar-TD (Owens 1993; Wikipedia consonant table after Owens 2006)."""
    assert get("ar-TD").graphemes["ج"] == ["dʒ", "ɟ"]
    for code in ("ar-TD", "ar-NG"):
        assert transcribe("جَمَل", code) == "ˈdʒamal"


# ─── Interdentals: the ar-TD → ar-NG delta ──────────────────────────────────

def test_chadian_variably_retains_the_interdentals():
    """Chadian Arabic is the conservative end of the chain and retains θ ث and
    ð ذ (and emphatic ðˤ ظ), with the stop merger only as a sedentary/urban
    (Abéché) variant — so the mainline of ثَلج 'ice/snow' keeps [θ] and ظُهر
    'noon' keeps [ðˤ] (Kaye 1976; de Pommerol 1999; Roth-Laly 1979)."""
    assert get("ar-TD").graphemes["ث"] == ["θ", "t"]
    assert transcribe("ثَلج", "ar-TD") == "ˈθaldʒ"
    assert transcribe("ظُهر", "ar-TD") == "ˈðˤuhr"


def test_nigerian_completes_the_interdental_merger():
    """Nigerian Arabic has *lost* the interdentals (Owens 2006 p.25): ث → /t/,
    ذ → /d/, ظ → /dˤ/ fall together with the plain stops — the delta that
    separates ar-NG from the more conservative ar-TD. ثَلج → [taldʒ], ظُهر →
    [dˤuhr]."""
    assert get("ar-NG").graphemes["ث"] == ["t"]
    assert get("ar-NG").graphemes["ظ"] == ["dˤ"]
    assert transcribe("ثَلج", "ar-NG") == "ˈtaldʒ"
    assert transcribe("ظُهر", "ar-NG") == "ˈdˤuhr"


# ─── Gahawa syndrome: /a/-insertion after a guttural coda ───────────────────

@pytest.mark.parametrize("code", ["ar-TD", "ar-NG"])
@pytest.mark.parametrize("word,expected", [
    ("لَحم", "ˈlaħam"),   # ḥ: 'meat'
    ("بَعد", "ˈbaʕad"),   # ʕ: 'after'
    ("نَخل", "ˈnaxal"),   # x: 'palm trees'
])
def test_gahawa_low_vowel_insertion_after_gutturals(code, word, expected):
    """A short /a/ is inserted after a guttural standing in a syllable coda,
    CaGC → CaGaC (Owens 2006 p.25, ahamar < *ʔaḥmar; Procházka 2026 p.310, 318).
    The rule fires on ḥ, ʕ and x — the robustly-attested core of Owens' fuller
    guttural set {ʔ h x q ħ ʕ}. It is declared once, on ar-TD; ar-NG inherits it
    through the OVERLAY_BY_ID allophone_rules inheritance keyed on
    graphemes_base."""
    assert transcribe(word, code) == expected


def test_nigerian_inherits_the_gahawa_rules_without_duplicates():
    """allophone_rules inherit through graphemes_base via OVERLAY_BY_ID (an
    override reuses the parent's rule IDs; a new ID appends instead of
    replacing). ar-NG must therefore carry exactly the inherited
    AR_TD_GAHAWA_* rules — no restated AR_NG_GAHAWA_* duplicates — and the
    inherited rule must still fire on a probe word."""
    ids = [r.id for r in get("ar-NG").allophone_rules]
    assert {"AR_TD_GAHAWA_H", "AR_TD_GAHAWA_AIN", "AR_TD_GAHAWA_KH"} <= set(ids)
    assert not any(i.startswith("AR_NG_GAHAWA") for i in ids)
    assert len(ids) == len(set(ids))
    assert transcribe("لَحم", "ar-NG") == "ˈlaħam"


def test_gahawa_does_not_fire_on_a_guttural_onset():
    """The rule is a coda effect: a word-initial or onset guttural leaves the
    following vowel alone — حَمرَة 'red (f.)' → [ħamra], not *[ħamara]; عَين
    'eye' → [ʕajn]."""
    for code in ("ar-TD", "ar-NG"):
        assert transcribe("حَمرَة", code) == "ˈħamra"
        assert transcribe("عَين", code) == "ˈʕajn"


# ─── Emphasis: robust and *extended*, inherited from the Mashriqi base ───────

def test_emphasis_backs_the_low_vowels():
    """Emphasis (pharyngealisation) backs /a aː/ to [ɑ ɑː] adjacent to an
    emphatic — inherited from the Mashriqi base and robust in West Sudanic
    Arabic: صَابِر 'patient' → [sˤɑːbir], بَطَل 'hero' → [bɑtˤɑl] (Watson 2002;
    Owens 2006 p.25 for the extended emphatic inventory)."""
    for code in ("ar-TD", "ar-NG"):
        assert transcribe("صَابِر", code) == "ˈsˤɑːbir"
        assert transcribe("بَطَل", code) == "ˈbɑtˤɑl"


def test_notes_record_that_emphasis_is_extended_not_lost():
    """Owens (2006 p.25) documents phonemic /lˤ rˤ mˤ/ *added* to the four
    Classical emphatics — the opposite of the widely repeated 'weakened
    emphasis' claim. The spec notes must record this correction so it cannot
    silently regress to the folk claim."""
    notes = get("ar-NG").notes.lower()
    assert "extended" in notes
    assert "lˤ" in get("ar-NG").notes and "rˤ" in get("ar-NG").notes
