"""Cited-rule conformance: the Arabic dialects and the Semitic relatives.

Companion to ``test_cited_rules_arabic.py`` (MSA, Classical, Hejazi, Najdi).
Each test here takes ONE cited claim — from a spec's ``notes`` prose or from the
``notes`` of a single ``allophone_rules``/``stress`` entry — quotes it with its
citation, and proves the engine honours it on a real, fully-vocalised word.

Only claims NOT already exercised by the older ``test_arabic*.py`` suites are
covered here; where a spec's cited reflexes (qaf, jim, interdentals, affrication,
imāla, monophthongisation) are already pinned there, they are not restated.

Each test ISOLATES its rule: the word is chosen so the rule's presence or absence
changes exactly one segment, and a minimal pair (a sister dialect lacking the
rule, or a non-triggering environment) pins the complement wherever one exists.

Where a spec HONESTLY DOCUMENTS ITS OWN GAP, the declared omission is pinned with
a passing test so it cannot silently drift. Where the engine CONTRADICTS a
citation, the assertion is kept exactly as the citation reads and marked
``xfail(strict=True)``.

Assertions go through the public API only: ``G2P(lang).transcribe_word(w)``.
"""
import pytest

from orthography2ipa.g2p import G2P


def _t(code, word):
    return G2P(code).transcribe_word(word)


def _bare(code, word):
    """Transcription with the stress mark stripped, for segment-level claims."""
    return _t(code, word).replace("ˈ", "").replace("ˌ", "")


# ---------------------------------------------------------------------------
# ar-x-peninsular — the shared Peninsular emphasis-spreading rules
# ---------------------------------------------------------------------------


def test_pen_emph_back_a_after():
    """AR_PEN_EMPH_BACK_A_AFTER: short /a/ backs to [ɑ] after an emphatic.

    Rule notes: "Emphasis (pharyngealization) spreading: short /a/ backs to [ɑ]
    when it follows an emphatic consonant /tˤ dˤ sˤ ðˤ (zˤ)/. Watson 2002, The
    Phonology and Morphology of Arabic (OUP), ch. 'Emphasis', pp. 267-286 ...
    Shared Peninsular feature."

    صَبَاح: the /a/ right after ص backs; the /aː/ two slots away, after plain ب,
    does not — the rule is strictly adjacency-scoped.
    """
    assert _bare("ar-x-peninsular", "صَبَاح") == "sˤɑbaːħ"


def test_pen_emph_back_a_before():
    """AR_PEN_EMPH_BACK_A_BEFORE: short /a/ backs to [ɑ] BEFORE an emphatic.

    Rule notes: "Emphasis spreading (leftward): short /a/ backs to [ɑ] before an
    adjacent emphatic consonant. Watson 2002 ... pharyngealization spreads
    bidirectionally within the phonological word, backing low vowels."

    سَطْح /satˤħ/ — the /a/ precedes ط and nothing follows it; only the leftward
    rule can back it.
    """
    assert _bare("ar-x-peninsular", "سَطْح") == "sɑtˤħ"


def test_pen_emph_back_aa_after():
    """AR_PEN_EMPH_BACK_AA_AFTER: long /aː/ backs to [ɑː] after an emphatic.

    Rule notes: "Emphasis spreading: long /aː/ backs to [ɑː] after an adjacent
    emphatic. Watson 2002 ... pp. 267-286."
    """
    assert _bare("ar-x-peninsular", "طَالِب") == "tˤɑːlib"


def test_pen_emph_back_aa_before():
    """AR_PEN_EMPH_BACK_AA_BEFORE: long /aː/ backs to [ɑː] BEFORE an emphatic.

    Rule notes: "Emphasis spreading (leftward): long /aː/ backs to [ɑː] before an
    adjacent emphatic. Watson 2002 ... pp. 267-286."

    بَاطِل /baːtˤil/ — the ⟨ا⟩ precedes ط; the /i/ after it is not a low vowel and
    is untouched, so exactly one segment moves.
    """
    assert _bare("ar-x-peninsular", "بَاطِل") == "bɑːtˤil"


# --- the quantity-sensitive stress cascade, on the nodes whose ONLY cited claim
# --- it is (each restates the same Ryding 2005 §2.3 / Watson 2002 ch.3 rule).

_STRESS_ONLY_NODES = [
    "ar-x-peninsular", "ar-x-mashriqi", "ar-x-maghrebi",
    "ar-BH", "ar-DZ", "ar-MR", "ar-TD",
]


@pytest.mark.parametrize("code", _STRESS_ONLY_NODES)
def test_stress_superheavy_final_attracts(code):
    """Stress cascade, step 1: a superheavy final syllable takes the stress.

    stress notes: "a superheavy final syllable (CVːC/CVCC) takes the stress
    (kiˈtaːb) ... (Ryding, A Reference Grammar of MSA, CUP 2005, §2.3; Watson,
    The Phonology and Morphology of Arabic, OUP 2002, ch.3)."

    سَلَام /salaːm/ is used rather than kitāb so the word is stable across the
    Gulf ⟨ك⟩-affrication nodes: only the stress placement is under test.
    """
    assert _t(code, "سَلَام") == "saˈlaːm"


@pytest.mark.parametrize("code", _STRESS_ONLY_NODES)
def test_stress_heavy_penult(code):
    """Stress cascade, step 2: otherwise a heavy penult takes it.

    stress notes: "otherwise a heavy penult (CVː/CVC) does (muˈdarris) ...
    max_onset=1 because Arabic onsets are obligatory and hold exactly one
    consonant — a medial cluster splits, closing the preceding syllable, and that
    boundary is what makes the penult of mudarris heavy" (Ryding 2005 §2.3).
    """
    assert _t(code, "مُدَرِّس") == "muˈdarris"


@pytest.mark.parametrize("code", _STRESS_ONLY_NODES)
def test_stress_falls_back_to_antepenult(code):
    """Stress cascade, step 3: otherwise the antepenult.

    stress notes: "otherwise the antepenult (ˈmadrasa)" (Ryding 2005 §2.3).
    مَدْرَسَة has no superheavy final and no heavy penult, so stress retracts —
    the minimal contrast with the two steps above.
    """
    assert _t(code, "مَدْرَسَة") == "ˈmadrasa"


# ---------------------------------------------------------------------------
# ar-x-gulf — Proto-Gulf (Khaleeji)
# ---------------------------------------------------------------------------


def test_gulf_loan_p_is_integrated():
    """Gulf ⟨پ⟩ reads /p/ — an integrated loan phoneme.

    ar-x-gulf notes: "(5) integrated /p/, /v/ from loanwords (پ, ڤ)."
    """
    assert _bare("ar-x-gulf", "پَان") == "paːn"


def test_gulf_loan_v_is_integrated():
    """Gulf ⟨ڤ⟩ reads /v/ — an integrated loan phoneme.

    ar-x-gulf notes: "(5) integrated /p/, /v/ from loanwords (پ, ڤ)."
    """
    assert _bare("ar-x-gulf", "ڤَان") == "vaːn"


def test_kw_non_adjacent_g_affrication_is_not_modelled():
    """Kuwaiti: Matar's non-adjacent /ɡ/-affrication trigger is NOT modelled.

    ar-KW notes: "Matar (1969), as reported in Alshammari 2026 p.1335, describes
    /ɡ/ → [dʒ] adjacent to front vowels, sometimes across an intervening /r, l/
    (e.g. qariːb→dʒiriːb) ... — the non-adjacent trigger is NOT modelled (see
    GULF_G_AFFRICATION notes)."

    The declared omission, pinned: قَرِيب keeps [ɡ] because the front vowel is not
    adjacent — GULF_G_AFFRICATION fires only on a following /i, iː/.
    """
    assert _bare("ar-KW", "قَرِيب") == "ɡariːb"


def test_qa_ocp_blocking_of_affrication_is_not_modelled():
    """Qatari: Mustafawi's OCP/emphatic blocking of affrication is NOT modelled.

    ar-QA notes: "Mustafawi further documents that affrication is blocked by
    [-high] segments, by adjacent emphatics, and by the OCP (near an
    identical/similar coronal) ... these blocking environments are NOT modelled in
    the base rule and remain an engine limit."

    The declared over-application, pinned on a NON-geminate word: مِسْكِين has an
    /s/ in the word, so real Qatari blocks affrication by the OCP — the engine
    affricates the /k/ anyway.
    """
    assert _bare("ar-QA", "مِسْكِين") == "mistʃiːn"


def test_qa_affrication_does_not_split_a_geminate():
    """Qatari: velar affrication does not apply to a geminate /kk/.

    سِكِّين 'knife' is /sikkiːn/ with a geminate ⟨كّ⟩. Affrication is a
    single-segment process triggered by an adjacent front vowel; a geminate is
    one long segment, so the rule cannot rewrite a single half and split it
    into a heterorganic *[ktʃ] cluster. The surface [sikkiːn] also happens to
    be what Mustafawi's OCP blocking predicts, but the engine reaches it by
    geminate integrity, not by modelling the OCP.
    """
    assert _bare("ar-QA", "سِكِّين") == "sikkiːn"


def test_ae_english_loan_phonemes_are_integrated():
    """Emirati has /p/ and /v/ thoroughly integrated (the Dubai effect).

    ar-AE notes: "(c) heaviest English influence of the Gulf dialects (Dubai
    effect): /p/, /v/, /tʃ/, /ŋ/ thoroughly integrated" (Szreder & Derrick 2023).
    """
    assert _bare("ar-AE", "پِيتْزَا") == "piːtzaː"
    assert _bare("ar-AE", "ڤَان") == "vaːn"


def test_om_jim_is_the_affricate():
    """Omani ⟨ج⟩ is [dʒ] — the /ɡ/ realisation is the free variant, not primary.

    ar-OM notes: "jiim /dʒ/ is realised as [dʒ] in the (mainly Bedouin/northern)
    dialects that keep it and as [ɡ] elsewhere (Glover 1988:38, cited Al-Balushi
    p.89: 'the voiced palatal affricate /ǰ/ is a free variant of /g/ in most
    words')."

    Minimal pair against Cairene, where the same grapheme is [ɡ].
    """
    assert _bare("ar-OM", "جَمَل") == "dʒamal"
    assert _bare("ar-EG", "جَمَل") == "ɡamal"


# ---------------------------------------------------------------------------
# ar-YE — Ṣanʿānī Yemeni
# ---------------------------------------------------------------------------


def test_ye_has_no_kaf_affrication():
    """Yemeni does not affricate /k/, unlike the Gulf.

    ar-YE notes: "No k → /tʃ/ (unlike Gulf)" (Watson 2002).

    The exact minimal pair the claim names: the same word, كِيس, affricates in the
    Gulf spec (GULF_K_AFFRICATION) and must not in Ṣanʿānī.
    """
    assert _bare("ar-YE", "كِيس") == "kiːs"
    assert _bare("ar-x-gulf", "كِيس") == "tʃiːs"


# ---------------------------------------------------------------------------
# ar-x-levantine — leftward emphasis spreading
# ---------------------------------------------------------------------------


def test_lev_emph_back_a_before():
    """AR_LEV_EMPH_BACK_A_BEFORE: short /a/ backs to [ɑ] before an emphatic.

    Rule notes: "Emphasis spreading (leftward): short /a/ backs to [ɑ] before an
    adjacent emphatic. Watson 2002."
    """
    assert _bare("ar-x-levantine", "سَطْح") == "sɑtˤħ"


def test_lev_emph_back_aa_before():
    """AR_LEV_EMPH_BACK_AA_BEFORE: long /aː/ backs to [ɑː] before an emphatic.

    Rule notes: "Emphasis spreading (leftward): long /aː/ backs to [ɑː] before an
    adjacent emphatic. Watson 2002."

    بَاطِل also pins the ordering claim of AR_LEV_EMPH_BACK_AA_AFTER — "Ordered
    before the Lebanese imāla rule so an emphatic /aː/ correctly stays back rather
    than raising": in Beiruti the same /aː/ must stay [ɑː], not raise to [eː].
    """
    assert _bare("ar-x-levantine", "بَاطِل") == "bɑːtˤil"
    assert _bare("ar-LB", "بَاطِل") == "bɑːtˤil"


# ---------------------------------------------------------------------------
# ar-EG — Cairene
# ---------------------------------------------------------------------------


def test_eg_emph_back_a_before():
    """AR_EG_EMPH_BACK_A_BEFORE: short /a/ backs to [ɑ] before an emphatic.

    Rule notes: "Emphasis spreading (leftward): short /a/ backs to [ɑ] before an
    adjacent emphatic consonant. Watson 2002 (Cairene as primary case) ch.
    Emphasis; Egyptian emphatics /tˤ dˤ sˤ zˤ/ with strong bidirectional
    spreading."
    """
    assert _bare("ar-EG", "سَطْح") == "sɑtˤħ"


def test_eg_emph_back_aa_after():
    """AR_EG_EMPH_BACK_AA_AFTER: long /aː/ backs to [ɑː] after an emphatic.

    Rule notes: "Emphasis spreading: long /aː/ backs to [ɑː] after an adjacent
    emphatic. Watson 2002 (Cairene as primary case) ch. Emphasis."
    """
    assert _bare("ar-EG", "طَالِب") == "tˤɑːlib"


def test_eg_emph_back_aa_before():
    """AR_EG_EMPH_BACK_AA_BEFORE: long /aː/ backs to [ɑː] before an emphatic.

    Rule notes: "Emphasis spreading (leftward): long /aː/ backs to [ɑː] before an
    adjacent emphatic. Watson 2002 (Cairene as primary case) ch. Emphasis."
    """
    assert _bare("ar-EG", "بَاطِل") == "bɑːtˤil"


def test_eg_stress_is_weight_sensitive():
    """Cairene stress is the weight-sensitive cascade, not an ending table.

    ar-EG stress notes: "a superheavy final syllable (CVːC/CVCC) takes the stress
    (kiˈtaːb); otherwise a heavy penult (CVː/CVC) does (muˈdarris); otherwise the
    antepenult (ˈmadrasa)" (Ryding 2005 §2.3; Watson 2002 ch.3) — matching the
    Cairene algorithm the spec's prose describes ("final superheavy CVːC/CVCC →
    final; else rightmost non-final heavy syllable, capped at the antepenult").
    """
    assert _t("ar-EG", "كِتَاب") == "kiˈtaːb"
    assert _t("ar-EG", "مُدَرِّس") == "muˈdarris"
    assert _t("ar-EG", "مَدْرَسَة") == "ˈmadrasa"


# ---------------------------------------------------------------------------
# ar-IQ / ar-IQ-x-qeltu — Mesopotamian
# ---------------------------------------------------------------------------


def test_iq_lexicalised_kaf_affrication_is_not_captured():
    """Iraqi: the LEXICALISED gilit affrication is deliberately not captured.

    ar-IQ notes: "ENGINE LIMIT: the fully LEXICALISED gilit affrication (M/čalb/
    'dog', where the trigger front vowel is historical) is not orthographically
    predictable and is NOT captured" (Blanc 1964, §3.25; Jasim 2020, §2.9.2).

    The declared under-application, pinned on the very word the note names: كَلْب
    keeps [k], while the orthographically-triggered كِبِير does affricate.
    """
    assert _bare("ar-IQ", "كَلْب") == "kalb"
    assert _bare("ar-IQ", "كِبِير") == "tʃibiːr"


def test_qeltu_uvular_r_is_documented_not_applied():
    """Qəltu: the uvular [ʁ] reflex of /r/ is documented, not applied.

    ar-IQ-x-qeltu notes: "(b) In Muslawi Qəltu and in Jewish/Christian Baghdadi,
    OA /r/ is in many instances a uvular/velar [ʁ]~[ɣ] (Blanc 1964, §3.24 —
    'M/ras/, JC/ɣas/'; Jasim 2020, §2.4) ... this is lexically conditioned and not
    predictable from the orthography, so it is documented rather than applied as a
    blanket rule."

    The declared omission, pinned on Blanc's own example word: /r/ stays [r].
    """
    assert _bare("ar-IQ-x-qeltu", "رَاس") == "raːs"


# ---------------------------------------------------------------------------
# ar-TN / ar-LY / ar-NG — Maghrebi and Sahelian peripheries
# ---------------------------------------------------------------------------


@pytest.mark.xfail(
    strict=True,
    reason="ar-TN notes claim θ → /t/ in urban Tunis, but the spec re-declares ث "
           "as [θ] over the Maghrebi parent's merged [t] — engine gives θaˈlaːθa",
)
def test_tn_tha_merges_to_t():
    """Tunisian ⟨ث⟩ merges to /t/ in the urban Tunis reference variety.

    ar-TN notes: "θ → /t/ (urban Tunis); some rural varieties preserve /θ/"
    (Gibson 2002; Talmoudi 1980).

    Minimal pair with the Maghrebi parent, which does merge (ثَلْج → [talʒ]).
    """
    assert _bare("ar-TN", "ثَلَاثَة") == "talaːta"


@pytest.mark.xfail(
    strict=True,
    reason="ar-LY notes claim ق is preserved as /q/, but the spec's ق reads [ɡ] "
           "first — engine gives ˈɡalb",
)
def test_ly_qaf_is_preserved():
    """Libyan ⟨ق⟩ is preserved as /q/.

    ar-LY notes: "ق → /q/ PRESERVED in most Libyan varieties (conservative)."

    Minimal pair with Moroccan, which likewise preserves /q/ (قَلْب → [qalb]).
    """
    assert _bare("ar-LY", "قَلْب") == "qalb"


def test_ly_tha_merges_to_t():
    """Libyan ⟨ث⟩ merges to /t/ (the Western/Tripoli Maghrebi reflex).

    ar-LY notes: "Two main varieties: Western (Tripoli): Maghrebi features, θ →
    /t/; Eastern (Benghazi/Barqa): more conservative, θ preserved."

    Minimal pair against MSA, which keeps the interdental [θ].
    """
    assert _bare("ar-LY", "ثَلْج").startswith("t")
    assert _bare("ar", "ثَلْج").startswith("θ")


def test_ng_interdentals_merge_completely():
    """Nigerian Shuwa merges both voiceless and voiced interdentals to stops.

    ar-NG notes: "θ → /t/, ð → /d/ (complete merger — Hausa influence)"
    (Owens 1993, A Reference Grammar of Nigerian Arabic).
    """
    assert _bare("ar-NG", "ثَلْج").startswith("t")
    assert _bare("ar-NG", "ذَهَب").startswith("d")


# ---------------------------------------------------------------------------
# xaa — Andalusi Arabic (Corriente 2013)
# ---------------------------------------------------------------------------


@pytest.mark.xfail(
    strict=True,
    reason="xaa notes call imāla the diagnostic feature, but /aː/→[eː] is only "
           "declared as a secondary allophone variant — engine gives baːb",
)
def test_xaa_imala_raises_long_a():
    """Andalusi imāla: /aː/ → [eː], the diagnostic feature.

    xaa notes: "Per Corriente (2013): (1) IMĀLA: /aː/ → [eː] (diagnostic
    feature)."

    Beiruti Lebanese, which has the same raise, is the working minimal pair:
    بَاب → [beːb] there.
    """
    assert _bare("xaa", "بَاب") == "beːb"


@pytest.mark.xfail(
    strict=True,
    reason="xaa notes claim the interdental merger, but ث is only given [t]/[s] "
           "as secondary variants — engine gives θaldʒ",
)
def test_xaa_interdental_merges():
    """Andalusi ⟨ث⟩ merges to /t/ (or /s/).

    xaa notes: "(2) Interdental merger: /θ/ → /t/ or /s/" (Corriente 2013).
    """
    assert _bare("xaa", "ثَلْج")[0] in {"t", "s"}


@pytest.mark.xfail(
    strict=True,
    reason="xaa notes claim ḍād and ẓāʾ conflate, but ض inherits Classical [ɮˤ] "
           "while ظ is [ðˤ] — engine keeps them distinct",
)
def test_xaa_emphatic_merger():
    """Andalusi ⟨ض⟩ and ⟨ظ⟩ conflate into a single emphatic.

    xaa notes: "(3) Emphatic merger: /ḍ/ and /ḏ̣/ conflate" (Corriente 2013).

    The two graphemes must therefore open their words with the same segment.
    """
    assert _bare("xaa", "ضَرَبَ")[:2] == _bare("xaa", "ظَهْر")[:2]


@pytest.mark.xfail(
    strict=True,
    reason="xaa notes claim a Romance-origin /p/, but ⟨پ⟩ has no grapheme entry — "
           "engine drops it, giving baː",
)
def test_xaa_romance_p_is_available():
    """Andalusi has a Romance-origin /p/.

    xaa notes: "(4) Romance-origin /p/ added" (Corriente 2013) — the Ibero-Romance
    adstrate phoneme, written ⟨پ⟩.
    """
    assert "p" in _bare("xaa", "بَاپ")


# ---------------------------------------------------------------------------
# cop — Sahidic Coptic
# ---------------------------------------------------------------------------


def test_cop_aspirated_stops():
    """Coptic has an aspirated stop series.

    cop notes: "KEY DIFFERENCES FROM OLD EGYPTIAN: emphatics lost, pharyngeals
    lost, aspirated stops (pʰ tʰ kʰ)" (Loprieno 1995; Layton 2000; Peust 1999).

    ⟨ⲫ⟩ is the aspirate of ⟨ⲡ⟩ [p] — the minimal pair for the series.
    """
    assert _bare("cop", "ⲫⲱⲣ").startswith("pʰ")
    assert _bare("cop", "ⲡⲉ").startswith("p")
    assert not _bare("cop", "ⲡⲉ").startswith("pʰ")


def test_cop_tsh_affricate():
    """Coptic has the affricate /tʃ/.

    cop notes: "affricate /tʃ/ from *tj" (Loprieno 1995; Peust 1999) — the Demotic
    letter ⟨ϫ⟩.
    """
    assert _bare("cop", "ϫ") == "tʃ"


# ---------------------------------------------------------------------------
# he — Modern Israeli Hebrew
# ---------------------------------------------------------------------------


def test_he_milra_is_the_default_stress():
    """Hebrew default stress is milra — final.

    he stress notes: "Modern Israeli Hebrew default is milra (final stress, -1) ...
    This block models the milra default only. Source: Bolozky (1997)."

    יְלָדִים /jelaˈdim/ is a plain milra plural: the stress mark must not sit on the
    first syllable.
    """
    assert _t("he", "יְלָדִים").index("ˈ") > 0
