"""Gulf Arabic dialects — research-grounded phonology (ar-x-gulf + AE/BH/KW/QA/OM).

The Gulf specs model, on the proto-parent ``ar-x-gulf`` and inherited by the
four Gulf country specs via ``graphemes_base`` / OVERLAY_BY_ID:

* Old Arabic *q → [ɡ] (grapheme ق → [ɡ] first);
* velar affrication — /k/ → [tʃ] (``GULF_K_AFFRICATION``) and /ɡ/(<*q) →
  [dʒ] (``GULF_G_AFFRICATION``) adjacent to a high front vowel /i, iː/;
* interdentals /θ ð ðˤ/ RETAINED (Bedouin-type), not merged to stops.

Omani (``ar-OM``) is genetically Peninsular (inherits ``ar-x-peninsular``
directly), keeps *q as [q], and carries only /k/-affrication
(``OM_K_AFFRICATION``) as a Bedouin/interior feature.

Sources actually read: Alshammari 2026 (JLTR 17(4):1333-1341), Al-Balushi
2016 (Macrolinguistics 4(1):80-125), Szreder & Derrick 2023 (JIPA).

Input contract: fully diacritised (tashkeel) Arabic.
"""
from orthography2ipa import get
from orthography2ipa.g2p import G2P

GULF = ("ar-AE", "ar-BH", "ar-KW", "ar-QA")


def _t(code, word):
    return G2P(code).transcribe(word)


# ─── the affrication rules exist and are inherited ──────────────────────

def test_proto_gulf_declares_the_two_affrication_rules():
    ids = [r.id for r in get("ar-x-gulf").allophone_rules]
    assert "GULF_K_AFFRICATION" in ids
    assert "GULF_G_AFFRICATION" in ids


def test_gulf_countries_inherit_affrication_rules():
    for code in GULF:
        ids = [r.id for r in get(code).allophone_rules]
        assert "GULF_K_AFFRICATION" in ids, code
        assert "GULF_G_AFFRICATION" in ids, code


def test_gulf_countries_inherit_peninsular_emphatic_spreading():
    # AR_PEN_EMPH_* comes from ar-x-peninsular, two nodes up.
    for code in GULF:
        ids = [r.id for r in get(code).allophone_rules]
        assert any(i.startswith("AR_PEN_EMPH") for i in ids), code


# ─── /q/ → [ɡ] in the Gulf (Bedouin/sedentary reflex) ───────────────────

def test_qaf_is_g_in_gulf():
    # قَلَم 'pen' — *q → [ɡ], /a/ does not trigger g-affrication
    for code in GULF:
        assert _t(code, "قَلَم") == "ˈɡalam", code


# ─── /k/ affrication before a high front vowel, and only there ──────────

def test_k_affricates_before_front_vowel():
    # كِتَاب 'book' — /k/ before /i/ → [tʃ]
    for code in GULF:
        out = _t(code, "كِتَاب")
        assert out.lstrip("ˈˌ").startswith("tʃ"), (code, out)


def test_k_does_not_affricate_before_back_or_low_vowel():
    # كَلْب 'dog' — /k/ before /a/ stays [k] (Mustafawi: blocked by [-high])
    for code in GULF:
        out = _t(code, "كَلْب")
        assert out.lstrip("ˈˌ").startswith("k") and "tʃ" not in out, (code, out)


# ─── /ɡ/ (< *q) affrication before a high front vowel ───────────────────

def test_g_affricates_before_front_vowel():
    # قِرْد 'monkey' — *q→[ɡ], then [ɡ] before /i/ → [dʒ]
    for code in GULF:
        out = _t(code, "قِرْد")
        assert out.lstrip("ˈˌ").startswith("dʒ"), (code, out)


# ─── interdental retention (Bedouin-type) ───────────────────────────────

def test_interdentals_retained():
    # ثَلاثَة 'three' keeps /θ/ (not merged to /t/ or /s/)
    for code in GULF + ("ar-OM",):
        assert "θ" in _t(code, "ثَلاثَة"), code
    # ذَهَب 'gold' keeps /ð/
    for code in GULF + ("ar-OM",):
        assert "ð" in _t(code, "ذَهَب"), code


# ─── per-country / per-node deltas ──────────────────────────────────────

def test_omani_is_peninsular_not_gulf():
    om = get("ar-OM")
    assert om.parent == "ar-x-peninsular"
    ids = [r.id for r in om.allophone_rules]
    # Omani carries only /k/-affrication, NOT the Gulf *q→[ɡ] g-affrication.
    assert "OM_K_AFFRICATION" in ids
    assert "GULF_G_AFFRICATION" not in ids


def test_omani_retains_qaf():
    # قَلَم and قِرْد keep [q] in sedentary Omani (no *q→[ɡ], no g-affrication)
    assert _t("ar-OM", "قَلَم") == "ˈqalam"
    assert _t("ar-OM", "قِرْد") == "ˈqird"


def test_omani_still_affricates_k_before_front_vowel():
    # Bedouin/interior feature present: كِتَاب → tʃitaːb
    assert _t("ar-OM", "كِتَاب").lstrip("ˈˌ").startswith("tʃ")


def test_emirati_has_english_loan_phonemes():
    # Heaviest English influence: /p/, /v/, /ŋ/ integrated (allophones delta)
    allo = get("ar-AE").allophones
    assert "ŋ" in allo


def test_bahraini_documents_the_communal_split():
    notes = get("ar-BH").notes.lower()
    assert "baḥārna" in notes or "baharna" in notes or "split" in notes


# ─── tier + provenance ──────────────────────────────────────────────────

def test_all_gulf_specs_are_research_tier_with_read_sources():
    from orthography2ipa.types import QualityTier
    for code in ("ar-x-gulf",) + GULF + ("ar-OM",):
        sp = get(code)
        assert sp.quality == QualityTier.RESEARCH, code
        ids = {s.id for s in sp.sources}
        # every Gulf spec cites at least one of the actually-read sources
        assert ids & {"alshammari2026", "albalushi2016", "szreder_derrick2023"}, code


# ─── Emirati lexical / function-word fixes (blind-verification round) ────

def test_emirati_law_resists_monophthongisation():
    """لَو 'if' keeps the /aw/ diphthong — a function word does not undergo the
    Gulf aw→oː monophthongisation (Holes 2016)."""
    assert _t("ar-AE", "لَو") == "ˈlaw"


def test_emirati_eesh_value():
    """عِيش 'rice/living' → [ʕeːʃ] — the Gulf lexeme has /eː/ (Holes 2016)."""
    assert _t("ar-AE", "عِيش") == "ˈʕeːʃ"


def test_emirati_il_yawm_lexical_article():
    """الْيَوم 'today' → [iljoːm] — the frozen adverb carries the /il/ article."""
    assert _t("ar-AE", "الْيَوم") == "ilˈjoːm"


# ─── ض/ظ merger, uvular fricatives, waṣl and the article ────────────────

def test_gulf_dad_merges_with_zah_to_emphatic_interdental():
    """‹ض› surfaces as the emphatic interdental [ðˤ], not the stop [dˤ].

    The wikipron afb gold writes ‹ض› as [ðˤ] in all 15 of its tokens and never
    as [dˤ]; Al Taisan 2019 transcribes ضغط 'pressure' as /ðˤɑʁtˤ/. The stop
    stays as a rank-2 MSA/formal candidate.
    """
    assert get("ar-x-gulf").graphemes["ض"][0] == "ðˤ"
    assert "dˤ" in get("ar-x-gulf").graphemes["ض"]
    assert _t("ar-x-gulf", "ضَرَب") == "ˈðˤɑrab"


def test_gulf_dad_sun_letter_keys_follow_the_merger():
    """The ‹الضض› assimilation keys carry the merged [ðˤðˤ] first, so the
    definite article does not re-introduce the lost stop."""
    g = get("ar-x-gulf").graphemes
    for key in ("الضض", "اَلضض", "لِلضض", "وَالضض", "اِلضض"):
        assert g[key][0].endswith("ðˤðˤ"), key


def test_gulf_dorsal_fricatives_are_uvular():
    """‹خ› → [χ] and ‹غ› → [ʁ]: the Gulf dorsal fricatives are uvular, against
    the MSA velars [x ɣ] inherited from ``arb``. Al Taisan 2019 transcribes ‹غ›
    as [ʁ] throughout its Hasawi data and names /χ/ the dialect's voiceless
    uvular fricative; the afb gold has [χ] in 35 of 36 ‹خ› tokens and [ʁ] in 17
    of 20 ‹غ› tokens."""
    g = get("ar-x-gulf").graphemes
    assert g["خ"] == ["χ"] and g["غ"] == ["ʁ"]
    assert _t("ar-x-gulf", "خُبُز") == "ˈχubuz"
    assert _t("ar-x-gulf", "غَالِي") == "ˈʁaːliː"


def test_gulf_wasl_alif_has_no_glottal_onset():
    """Word-initial bare ‹ا› spells a prosthetic vowel, not a consonant, so it
    gives [i…] and never [ʔi…]. Hamzat al-qaṭʿ ‹أ إ› keeps its [ʔ]. Of the 55
    bare-alif-initial rows in the afb gold exactly one carries an initial [ʔ] —
    the bare article ‹ال›, written without it elsewhere in the same gold."""
    assert _t("ar-x-gulf", "اِسْم") == "ˈism"
    assert _t("ar-x-gulf", "اِخْتَرَع") == "ˈiχtaraʕ"
    assert _t("ar-x-gulf", "اُكْتُب") == "ˈuktub"
    assert _t("ar-x-gulf", "إِثْم") == "ˈʔiθm"


def test_gulf_definite_article_is_il_word_initially_only():
    """The Gulf article is /il-/ (Holes 1990; Qafisheh 1977 — the afb gold has
    an [ɪ] article vowel in 10 of its 15 ‹ال›-initial rows), but the inherited
    ‹ال› key also matches word-internal alif+lam, so the article reading is
    restricted to word-initial position."""
    pg = get("ar-x-gulf").positional_graphemes["ال"]
    from orthography2ipa.types import GraphemePosition
    assert pg[GraphemePosition.WORD_INITIAL][0] == "il"
    for code in ("ar-x-gulf",) + GULF + ("ar-SA-x-sharqiyya", "ar-SA-x-dawasir"):
        assert _t(code, "الْحِين") == "ilˈħiːn", code
        assert _t(code, "غَالِي") == "ˈʁaːliː", code  # internal ال is not the article
        # a leaf lexicon override must not silently shadow the /il-/ rule
        assert _t(code, "الْعِيش")[0] == "i", code


def test_gulf_article_vowel_is_written_where_the_spelling_writes_one():
    """The /i/ belongs to the unwritten waṣl vowel. A written fatḥa on the
    seat — ‹اَل› and the proclitics ‹وَال فَال كَال› — is read as spelled."""
    assert _t("ar-x-gulf", "اَلْبَيت") == "alˈbeːt"
    assert _t("ar-x-gulf", "وَالْبَيت") == "walˈbeːt"
    assert _t("ar-x-gulf", "فَالْبَيت") == "falˈbeːt"
    assert _t("ar-x-gulf", "كَالْبَيت") == "kalˈbeːt"


def test_gulf_article_vowel_elides_after_a_vowel_final_word():
    """فِي الْمَدِينَة → [fiː lmaˈdiːna]: the article's /i/ drops after a
    vowel-final word, as the MSA /a/ does. The inherited ``arb`` rule only
    matches an /a/ seat, so the Gulf /il-/ needs AR_GULF_WASL_IL_ARTICLE."""
    assert "AR_GULF_WASL_IL_ARTICLE" in {r.id for r in get("ar-x-gulf").sandhi_rules}
    for code in ("ar-x-gulf",) + GULF + ("ar-SA-x-sharqiyya", "ar-SA-x-dawasir"):
        assert G2P(code).transcribe("فِي الْمَدِينَة") == "fiː lmaˈdiːna", code
    # only the article's /i/ elides — an i-initial word keeps its vowel
    assert _t("ar-x-gulf", "فِي اِسْم") == "fiː ˈism"


def test_dawasir_inherits_the_gulf_reflexes():
    """Dawāsir Arabic is a Najdi-Bedouin core with a Gulf overlay and takes the
    Gulf reflexes through ``ar-SA-x-sharqiyya``: the ض/ظ merger (independently
    documented for the variety), the uvular fricatives, and the /il-/ article
    with /al-/ kept as the rank-2 candidate."""
    assert _t("ar-SA-x-dawasir", "ضَرَب") == "ˈðˤɑrab"
    assert _t("ar-SA-x-dawasir", "خُبُز") == "ˈχubuz"
    assert _t("ar-SA-x-dawasir", "الْمَدِينَة") == "ilmaˈdiːna"


def test_gulf_cites_the_eastern_arabian_uvular_source():
    ids = {s.id for s in get("ar-x-gulf").sources}
    assert {"altaisan2019", "holes1990", "qafisheh1977"} <= ids
