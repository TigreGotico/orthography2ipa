"""Cited-rule conformance: Arabic and its varieties.

Every spec under ``orthography2ipa/data/`` makes cited linguistic claims — in
its ``notes`` prose and in the ``notes``/``source`` field of each individual
``allophone_rules``/``sandhi_rules``/``stress`` entry. Each test here takes one
such claim, quotes it with its citation, and proves the engine honours it on a
real word.

Each test ISOLATES its rule: the word is chosen so that the rule's presence or
absence changes exactly one segment, and — wherever the phonology allows one —
a minimal pair pins the complementary environment (the rule must NOT fire).

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
# ar — Modern Standard Arabic
# ---------------------------------------------------------------------------


def test_ar_dad_is_plosive_not_classical_lateral():
    """MSA ⟨ض⟩ is [dˤ], not the Classical lateral fricative [ɮˤ].

    ar notes: "ض is transcribed [dˤ] (emphatic alveolar stop), not the
    Classical lateral-fricative [ɮˤ] Sibawayhi describes and arb.json retains —
    MSA has merged ض onto the plosive series (Watson 2002)."

    Minimal pair against the Classical spec ``arb``, which retains [ɮˤ]
    (arb notes: "ض /ɮˤ/ — emphatic LATERAL fricative ... Source: Sibawayhi,
    al-Kitāb (8th c.)").
    """
    assert _bare("ar", "ضَرَبَ").startswith("dˤ")
    assert _bare("arb", "ضَرَبَ").startswith("ɮˤ")


def test_ar_emph_back_a_after_emphatic():
    """AR_EMPH_BACK_A_AFTER: short /a/ backs to [ɑ] after an emphatic.

    Rule notes: "Emphasis (pharyngealization) spreading: short /a/ backs to [ɑ]
    when it follows an emphatic consonant /tˤ dˤ sˤ ðˤ (zˤ)/. Watson 2002, The
    Phonology and Morphology of Arabic (OUP), ch. 'Emphasis', pp. 267-286."

    صَبَاح /sˤabaːħ/: the /a/ after the emphatic ص backs; the /aː/ after the
    plain ب, two slots away, does not — the rule is strictly adjacency-scoped.
    """
    assert _bare("ar", "صَبَاح") == "sˤɑbaːħ"


def test_ar_emph_back_a_not_after_plain_consonant():
    """AR_EMPH_BACK_A_AFTER does not fire without an adjacent emphatic.

    The complement of the Watson (2002) emphasis-spreading claim: with no
    emphatic in the word, every /a/ stays front. سَبَب /sabab/ is صَبَاح's
    plain-sibilant counterpart.
    """
    assert "ɑ" not in _bare("ar", "سَبَب")


def test_ar_emph_back_aa_after_emphatic():
    """AR_EMPH_BACK_AA_AFTER: long /aː/ backs to [ɑː] after an emphatic.

    Rule notes: "Emphasis spreading: long /aː/ backs to [ɑː] after an adjacent
    emphatic. Watson 2002 ... pp. 267-286."

    طَالِب /tˤaːlib/ — the ⟨ا⟩ directly follows the emphatic ط.
    """
    assert _bare("ar", "طَالِب") == "tˤɑːlib"


def test_ar_glide_ya_consonantal_in_nisba():
    """AR_GLIDE_YA_BEFORE_GEMINATE + AR_GLIDE_YA_GEMINATE_COPY: ـِيّ is /-ijj/.

    Rule notes: "A shadda doubles the yāʾ (Wright I §14) ... the pair is a
    geminate consonant, not two long vowels ... so ـِيّ ends /ijj/, never
    /ijiː/ — مِصْرِيّ /misˤrijj/ (Ryding 2005 §5.4.1)."
    """
    assert _bare("ar", "مِصْرِيّ") == "misˤrijj"


def test_ar_glide_ya_stays_long_when_quiescent():
    """AR_GLIDE_YA_* do not fire on a quiescent yāʾ — فِي stays [fiː].

    Rule notes (AR_GLIDE_YA_CONSONANTAL): "The ⟨ِي⟩ mater-lectionis digraph
    reads as long /iː/ only when the yāʾ is QUIESCENT (bears no vowel of its
    own) ... otherwise it 'retains its consonantal power' (Wright, A Grammar of
    the Arabic Language, 3rd ed., I §4)."

    The minimal pair for the nisba above: no following glide, no rewrite.
    """
    assert _bare("ar", "فِي") == "fiː"


def test_ar_glide_ya_consonantal_before_vowelled_ya():
    """AR_GLIDE_YA_CONSONANTAL: ـِيَّة is /-ijja/, not /-iːja/.

    Rule notes: "Without it حُرِّيَّة reads ħurriːja ... the nisba suffixes read
    ـِيّ /-ijj/ and ـِيَّة /-ijja/ (Ryding 2005 §5.4.1)."
    """
    assert _bare("ar", "حُرِّيَّة") == "ħurrijja"


def test_ar_glide_waw_consonantal_before_geminate():
    """AR_GLIDE_WAW_CONSONANTAL: ⟨ُو⟩ before its geminate copy is /uw/.

    Rule notes: "the ⟨ُو⟩ digraph is long /uː/ only when the wāw is quiescent.
    Before its own geminate copy or a consonantal wāw it keeps its consonantal
    power — أُبُوَّة /ʔubuwwa/ (Wright I §4, §14)."
    """
    assert _bare("ar", "أُبُوَّة") == "ʔubuwwa"


def test_ar_shadda_geminates_rather_than_lengthens():
    """Shadda doubles its consonant; it is not a stranded length mark.

    ar notes: "GEMINATION — shadda (ّ) now geminates its consonant (a doubled
    consonant, not a stranded length mark), for ALL consonants incl. the glides
    ي/و ... عَمَّ → [ʕamma], عُيِّنَ → [ʕujjina] (Ryding 2005 ch.2, pp.15–16;
    Watson 2002)."
    """
    assert _bare("ar", "عَمَّ") == "ʕamma"
    assert _bare("ar", "عُيِّنَ") == "ʕujjina"


def test_ar_hamza_carrier_is_bare_consonant_before_written_vowel():
    """⟨أ⟩/⟨إ⟩ are bare /ʔ/ before a written vowel — no doubled vowel.

    ar notes: "أ/إ are bare /ʔ/ before a written vowel with the vowel from the
    harakat (Ryding 2005 p.16 'strong hamza is a regular consonant'), so
    إِيْمَان → [ʔiːmaːn] (no ʔiiː doubling)."
    """
    assert _bare("ar", "إِيْمَان") == "ʔiːmaːn"


def test_ar_ta_marbuta_silent_at_pause():
    """⟨ة⟩ after a harakat is the pausal /a/, not /at/.

    ar notes: "ة after a harakat is the pausal /a/ (the preceding fatḥa supplies
    it) so مَدْرَسَة → [madrasa] ... the tāʾ marbūṭa is only silent at a pause
    (Ryding 2005 §2.3.2)."
    """
    assert _bare("ar", "مَدْرَسَة") == "madrasa"


def test_ar_lam_alif_ligature_normalized():
    """Arabic presentation-form ligatures decompose before tokenization.

    ar notes: "LIGATURE / PRESENTATION-FORM NORMALIZATION — the engine
    decomposes Arabic Presentation Forms-A/B (U+FB50–FDFF, U+FE70–FEFF), incl.
    the lam-alif ligatures ﻻ/ﻷ/ﻵ/ﻹ, to their canonical letters before
    tokenization, so ﻻ → [laː]."
    """
    assert _bare("ar", "ﻻ") == "laː"


# --- stress: the quantity-sensitive cascade (Ryding 2005 §2.3; Watson 2002 ch.3)


def test_ar_stress_superheavy_final_attracts():
    """Stress rule, step 1: a superheavy final syllable (CVːC) takes the stress.

    stress notes: "a superheavy final syllable (CVːC/CVCC) takes the stress
    (kiˈtaːb) ... (Ryding, A Reference Grammar of MSA, CUP 2005, §2.3; Watson,
    The Phonology and Morphology of Arabic, OUP 2002, ch.3)."
    """
    assert _t("ar", "كِتَاب") == "kiˈtaːb"


def test_ar_stress_heavy_penult():
    """Stress rule, step 2: otherwise a heavy penult (CVː/CVC) takes it.

    stress notes: "otherwise a heavy penult (CVː/CVC) does (muˈdarris)"
    (Ryding 2005 §2.3). max_onset=1 splits the /rr/ cluster, closing — and so
    making heavy — the penult.
    """
    assert _t("ar", "مُدَرِّس") == "muˈdarris"


def test_ar_stress_falls_back_to_antepenult():
    """Stress rule, step 3: otherwise the antepenult.

    stress notes: "otherwise the antepenult (ˈmadrasa)" (Ryding 2005 §2.3).
    Minimal contrast with the two tests above: no superheavy final, no heavy
    penult, so stress retracts.
    """
    assert _t("ar", "مَدْرَسَة") == "ˈmadrasa"


# ---------------------------------------------------------------------------
# arb — Classical Arabic
# ---------------------------------------------------------------------------


def test_arb_diphthongs_preserved():
    """Classical /aj/ and /aw/ are not monophthongised.

    arb notes: "(7) diphthongs /aj/ and /aw/ preserved (not monophthongised).
    Source: Sibawayhi, al-Kitāb (8th c.); Wright (1896); Watson (2002)."

    The minimal pair is the Hejazi spec below, which monophthongises both.
    """
    assert _bare("arb", "بَيْت") == "bajt"
    assert _bare("arb", "يَوْم") == "jawm"


def test_arb_hamzat_wasl_article_elides_after_vowel():
    """AR_HAMZAT_WASL_ARTICLE: the article's seat vowel elides after a vowel.

    Rule notes: "The hamzat-wasl /a/ of a word-initial definite article elides
    after a vowel-final word: fiː albajti → fiː lbajti (Ryding 2005 §2.10). Only
    the article's seat vowel is deleted."

    A sandhi rule, so it is exercised across the word boundary via transcribe().
    """
    assert G2P("arb").transcribe("فِي الْبَيْتِ") == "ˈfiː lˈbajti"


# ---------------------------------------------------------------------------
# ar-SA-x-hejaz — Hejazi Arabic
# ---------------------------------------------------------------------------


def test_hejaz_mono_ay():
    """HEJ_MONO_AY: Classical /aj/ is realised [eː].

    Rule notes: "Urban Hejazi monophthongization (Omar 1975; Abdoh 2010): the
    Classical diphthong /aj/ is realised [eː], e.g. bayt → [beːt]."
    """
    assert _bare("ar-SA-x-hejaz", "بَيْت") == "beːt"


def test_hejaz_mono_aw():
    """HEJ_MONO_AW: Classical /aw/ is realised [oː].

    Rule notes: "Urban Hejazi monophthongization (Omar 1975; Abdoh 2010): the
    Classical diphthong /aw/ is realised [oː], e.g. yawm → [joːm]."
    """
    assert _bare("ar-SA-x-hejaz", "يَوْم") == "joːm"


def test_hejaz_interdentals_merge_to_stops():
    """Hejazi urban koine merges the interdentals onto the stops.

    ar-SA-x-hejaz notes: "(3) interdentals MERGED TO STOPS in the urban koine —
    ث → /t/ (~/s/) ... References Omar (1975) and Abdoh (2010)."

    ثَلَاثَة: both ⟨ث⟩ read [t], where MSA reads [θ].
    """
    assert _bare("ar-SA-x-hejaz", "ثَلَاثَة") == "talaːta"
    assert "θ" in _bare("ar", "ثَلَاثَة")


def test_hejaz_qaf_is_voiced_velar_stop():
    """Hejazi ⟨ق⟩ is /ɡ/, not /q/ and not /ʔ/.

    ar-SA-x-hejaz notes: "(1) qaf ق → /ɡ/ (voiced velar stop) in inherited
    vocabulary — part of the early Hejazi /q/→/ɡ/ shift ... (older descriptions
    positing a /ʔ/ reflex are a misattribution of the Levantine/Egyptian
    feature)."
    """
    assert _bare("ar-SA-x-hejaz", "قَلْب").startswith("ɡ")


# ---------------------------------------------------------------------------
# ar-SA-x-najd — Najdi Arabic
# ---------------------------------------------------------------------------


def test_najd_affric_k_before_front_vowel():
    """NAJD_AFFRIC_K_BEFORE: /k/ → [ts] before an adjacent front vowel.

    Rule notes: "Najdi velar affrication (Ingham 1994, pp.13-14; Al Mahmoud
    2020, Education and Linguistics Research 6(2):62-72, exx. 1-9): /k/ → [ts]
    before an adjacent FRONT vowel — /kis/ → [tsis] 'bag' (ex. 1)."
    """
    assert _bare("ar-SA-x-najd", "كِيس") == "tsiːs"


def test_najd_affric_k_after_front_vowel():
    """NAJD_AFFRIC_K_AFTER: /k/ → [ts] after an adjacent front vowel.

    Rule notes: "Najdi velar affrication (Ingham 1994; Al Mahmoud 2020): /k/ →
    [ts] after an adjacent front vowel — /dik/ → [dits] 'rooster' (ex. 2)."
    """
    assert _bare("ar-SA-x-najd", "دِيك") == "diːts"


def test_najd_affrication_excludes_fatha_environment():
    """Najdi affrication is deliberately NOT triggered by /a/.

    Rule notes (NAJD_AFFRIC_K_BEFORE): "SCOPE — /a/ is deliberately NOT a
    trigger. Al Mahmoud (2020) §3.1 shows the fatha environment splits
    LEXICALLY: /kɛlb/ 'dog' → [tsɛlb] has a front vowel, /qʌlb/ 'heart' →
    [ɡʌlb] ... and both are written with the same fatha, so no rule reading the
    orthography can separate them ... Under-applying is the honest failure."

    The declared under-application, pinned so it cannot silently start over-
    applying: كَلْب keeps [k], and قَلْب keeps [ɡ] (not *[dz]).
    """
    assert _bare("ar-SA-x-najd", "كَلْب").startswith("k")
    assert _bare("ar-SA-x-najd", "قَلْب").startswith("ɡ")


def test_najd_gahawa_epenthesis_after_h():
    """NAJD_GAHAWA_h: epenthetic /a/ after a coda guttural /h/.

    Rule notes: "Gahawa syndrome (Ingham 1994, pp.15-16): epenthetic /a/ is
    inserted after a guttural /h/ standing in a coda after a low vowel (…aXC…),
    e.g. gahwa → gahawa."
    """
    assert _bare("ar-SA-x-najd", "قَهْوَة") == "ɡahawa"


def test_najd_gahawa_epenthesis_after_hha():
    """NAJD_GAHAWA_0127: epenthetic /a/ after a coda guttural /ħ/.

    Rule notes: "Gahawa syndrome (Ingham 1994, pp.15-16): epenthetic /a/ is
    inserted after a guttural /ħ/ standing in a coda after a low vowel (…aXC…)
    ... laħm → laħam."
    """
    assert _bare("ar-SA-x-najd", "لَحْم") == "laħam"


def test_najd_qaf_is_voiced_velar_stop():
    """Najdi ⟨ق⟩ is /ɡ/ (Bedouin/traditional reflex).

    ar-SA-x-najd notes: "(1) qaf ق → /ɡ/ (Bedouin/traditional) ... Primary
    reference Ingham (1994) Najdi Arabic: Central Arabian."
    """
    assert _bare("ar-SA-x-najd", "قَلْب").startswith("ɡ")


def test_najd_emphatic_spreading_inherited_from_peninsular():
    """Emphatic backing reaches Najdi by inheritance, not restatement.

    ar-SA-x-najd notes: "(5) emphatic (pharyngealization) spreading backs low
    vowels to [ɑ]/[ɑː] — inherited from the ar-x-peninsular parent
    (AR_PEN_EMPH_*), not restated here."

    طَيِّب: the /a/ adjacent to the emphatic ط backs, exactly as the parent's
    rule dictates — and, per NAJD_AFFRIC_K_BEFORE's "NOT EXPRESSIBLE" note, the
    /ajj/ sequence must survive segmentation intact for this to happen.
    """
    assert _bare("ar-SA-x-najd", "طَيِّب") == "tˤɑjjib"
