"""Cited-rule tests for the Catalan / Basque / Iberian-minority / Italo-Romance cluster.

Every test here isolates ONE claim that a spec makes with a citation, on a real
word, and asserts exactly the segment the citation asserts. Where a rule can be
switched on and off by variety, the test is a minimal pair: the same word in the
variety that has the rule and in the sister variety that (per the same citation)
does not.

Claims already proven by tests/test_catalan_phonology.py,
tests/test_catalan_reduction.py, tests/test_allophone_rules.py,
tests/test_basque_dialects.py, tests/test_asturleonese_sources.py,
tests/test_aragonese_valleys.py and tests/test_ligurian.py are not repeated.

Strict xfails mark cited rules the engine does not honour. The assertion is kept
as the CITATION states it; the reason records what the engine actually produces.
"""

import pytest

from orthography2ipa.g2p import G2P


def word(code: str, w: str) -> str:
    return G2P(code).transcribe_word(w)


def bare(code: str, w: str) -> str:
    return G2P(code).transcribe_word(w).replace("ˈ", "")


def phrase(code: str, text: str) -> list:
    return G2P(code).transcribe(text).split()


# ═══════════════════════════════════════════════════════════════════════════
# Catalan — Old Catalan core (ca-x-medieval) and Central Catalan (ca)
# ═══════════════════════════════════════════════════════════════════════════

def test_ca_medieval_final_affricate_devoicing():
    """CA_DEVOICE_DZH: "Final-obstruent devoicing (Wheeler 2005 §5.3): the
    word-final affricate /dʒ/ → [tʃ] (jutge is [ˈdʒudʒə] but mig [ˈmitʃ])."

    The minimal pair is position: the same affricate is voiced word-medially
    and devoiced word-finally.
    """
    assert bare("ca-x-medieval", "jutge") == "dʒudʒe"
    assert bare("ca-x-medieval", "mig") == "mitʃ"


def test_ca_cross_word_voicing_of_final_ps_cluster():
    """CA_FINAL_PS_VOICING: "word-final obstruents ... voice before a following
    vowel or voiced consonant inside the phonological phrase (Wheeler 2005
    §5.3, §10.5; Recasens 1993): ... cops havíem [ˈkɔbz əˈβiəm]. Longer
    clusters are listed first so the whole cluster voices."
    """
    assert phrase("ca", "cops havíem")[0].endswith("bz")
    # in isolation the cluster is voiceless
    assert bare("ca", "cops").endswith("ps")


def test_ca_cross_word_voicing_of_final_ks_cluster():
    """CA_FINAL_KS_VOICING: the whole final cluster voices before a voiced
    segment — "els amics [əlz əˈmiks]" voiceless in phrase-final position,
    voiced when a voiced consonant follows (Wheeler 2005 §5.3, §10.5).
    """
    assert phrase("ca", "amics vells")[0].endswith("ɡz")
    assert bare("ca", "amics").endswith("ks")


def test_ca_cross_word_voicing_of_final_ts_cluster():
    """CA_FINAL_TS_VOICING: word-final /ts/ → [dz] before a voiced segment
    (Wheeler 2005 §5.3, §10.5; Recasens 1993)."""
    assert phrase("ca", "tots dos")[0].endswith("dz")
    assert bare("ca", "tots").endswith("ts")


def test_ca_cross_word_voicing_of_final_affricate():
    """CA_FINAL_TSH_VOICING: "vaig obrir [ˈbadʒ uˈβɾi]" — the word-final
    affricate [tʃ] voices to [dʒ] before a following vowel (Wheeler 2005
    §5.3, §10.5; Recasens 1993)."""
    assert phrase("ca", "vaig obrir")[0].endswith("dʒ")
    assert bare("ca", "vaig").endswith("tʃ")


def test_ca_cross_word_voicing_of_final_sh():
    """CA_FINAL_SH_VOICING: a word-final /ʃ/ voices to [ʒ] before a voiced
    segment inside the phonological phrase (Wheeler 2005 §5.3, §10.5)."""
    assert phrase("ca", "peix blau")[0].endswith("ʒ")
    assert bare("ca", "peix").endswith("ʃ")


def test_ca_cross_word_voicing_of_final_f():
    """CA_FINAL_F_VOICING: a word-final /f/ voices to [v] before a voiced
    consonant (Wheeler 2005 §5.3, §10.5; Recasens 1993)."""
    assert phrase("ca", "serf va")[0].endswith("v")
    assert bare("ca", "serf").endswith("f")


def test_ca_cross_word_stop_voices_before_a_voiced_consonant():
    """CA_FINAL_K_VOICING / CA_FINAL_P_VOICING: "A single word-final STOP voices
    only before a voiced CONSONANT — before a vowel it stays voiceless (poc a
    poc [ˈpɔk ə ˈpɔk])" (Wheeler 2005 §5.3, §10.5).

    The minimal pair is the following segment: consonant voices the stop, vowel
    does not.
    """
    assert phrase("ca", "poc bo")[0].endswith("ɡ")
    assert phrase("ca", "cap gran")[0].endswith("b")
    assert phrase("ca", "poc a poc")[0].endswith("k")


def test_ca_phrase_spirantization_blocked_after_a_nasal():
    """CA_EXT_SPIRANT_G: an initial /b d ɡ/ lenites "whenever the preceding word
    ends in a continuant ... and stays a stop after a pause, a nasal or another
    stop (Wheeler 2005 §5.2, §10.5; Recasens 1993): ... but un glop [uŋ ˈɡlɔp]
    keeps the stop after the nasal."

    Minimal pair against the lenition context ("es va [əz ˈβa]").
    """
    assert phrase("ca", "un glop")[1].lstrip("ˈ").startswith("ɡ")
    assert phrase("ca", "es va")[1].lstrip("ˈ").startswith("β")


def test_ca_nasal_palatal_assimilation_word_internally():
    """CA_NASAL_PALATAL: "/n/ → [ɲ] before /ʃ ʒ tʃ dʒ ʎ/ — àngel [ˈaɲʒəl]"
    (Recasens 1993; Wheeler 2005 §10.3)."""
    assert bare("ca", "àngel") == "aɲʒəl"


@pytest.mark.xfail(
    strict=True,
    reason="CA_NASAL_PALATAL cites the cross-word case un jutge [uɲ ˈdʒudʒə]; "
           "the engine applies the rule word-internally only and produces "
           "[ˈun ˈʒudʒə] — the nasal keeps its alveolar place across the "
           "word boundary",
)
def test_ca_nasal_palatal_assimilation_across_a_word_boundary():
    """CA_NASAL_PALATAL: "Nasal place assimilation to a PALATO-ALVEOLAR
    (Recasens 1993; Wheeler 2005 §10.3): /n/ → [ɲ] before /ʃ ʒ tʃ dʒ ʎ/ —
    àngel [ˈaɲʒəl], un jutge [uɲ ˈdʒudʒə], any llunyà [ˈaɲ ʎuˈɲa]."
    """
    assert phrase("ca", "un jutge")[0].endswith("ɲ")


@pytest.mark.xfail(
    strict=True,
    reason="stress notes cite següent [səˈɣwen]; the engine reads ⟨gü⟩ before "
           "a front vowel as the soft /ʒ/ and produces [səˈʒwɛn] — the "
           "diaeresis does not protect the velar",
)
def test_ca_gu_with_diaeresis_is_a_velar_plus_glide():
    """Catalan stress notes (IEC grammar ch. 3; Wheeler 2005 §3.1): "The
    diaeresis ⟨ï ü⟩ marks hiatus/pronounced ⟨u⟩ ... (següent is [səˈɣwen], not
    [səˈɣwent] with stress on ⟨ü⟩)."

    The consonant is the isolated segment: ⟨gü⟩ is a velar plus glide, not the
    soft ⟨g⟩ of ⟨gent⟩.
    """
    assert "ɣw" in word("ca", "següent")


@pytest.mark.xfail(
    strict=True,
    reason="stress notes cite avui [əˈβuj] as oxytone; ⟨ui⟩ is absent from "
           "final_stress_endings, so the engine stresses the first syllable "
           "and leaves the ⟨a⟩ unreduced: [ˈaβuj]",
)
def test_ca_word_ending_in_a_falling_diphthong_is_oxytone():
    """Catalan stress notes (Wheeler 2005 §2.5, §3.1; IEC grammar ch. 3): "A
    word ending in a falling DIPHTHONG (-ai -au -ei -eu -iu -oi -ou) is oxytone
    (remei [rəˈmɛj], correu [kuˈrɛw], avui [əˈβuj]) — the diphthong is one
    syllable, so the word does not end in a bare vowel."

    Vowel reduction is the stress diagnostic: an unstressed ⟨a⟩ must be [ə].
    ⟨remei⟩ and ⟨correu⟩ behave as cited; ⟨avui⟩ does not.
    """
    assert bare("ca", "remei").startswith("rə")
    assert bare("ca", "correu").startswith("ku")
    assert bare("ca", "avui").startswith("ə")


@pytest.mark.xfail(
    strict=True,
    reason="phrase-level spirantization matches the /d/ of the affricate /dʒ/ "
           "and yields [ðʒeˈɾmana] for la germana; the cited Valencian form is "
           "the intact affricate [dʒeɾˈma]",
)
def test_ca_valencian_affricate_survives_phrase_level_spirantization():
    """Valencian notes (Wheeler 2005 §5.1; Veny 1982 ch. 3; AVL 2006): "the
    affricate [dʒ] for ⟨j⟩ and ⟨g⟩ before a front vowel (germà [dʒeɾˈma])".

    CA_EXT_SPIRANT_D lenites a word-initial /d/ after a continuant; the
    affricate is not a /d/, so the cited affricate must survive the phrase.
    The word in isolation is [dʒeˈɾmana] — only the phrase breaks it.
    """
    assert bare("ca-x-valencia", "germana").startswith("dʒ")
    assert phrase("ca-x-valencia", "la germana")[1].lstrip("ˈ").startswith("dʒ")


# ═══════════════════════════════════════════════════════════════════════════
# Basque
# ═══════════════════════════════════════════════════════════════════════════

def test_eu_three_way_sibilant_contrast_surfaces():
    """Standard Basque notes: "Conservative Basque varieties have a three-way
    sibilant place contrast: lamino-alveolar /s̻/ (spelled z), apico-alveolar
    /s̺/ (spelled s) and postalveolar /ʃ/ (spelled x) ... fully stable in
    eastern and Navarrese varieties such as Goizueta but is neutralised further
    west (Hualde, Lujanbio & Zubiri 2010: 119)."

    Three words differing in the sibilant grapheme alone must give three
    distinct sibilants; Biscayan, where the contrast is neutralised, is the
    minimal pair (⟨z⟩ there is apical too).
    """
    assert bare("eu", "zezen").startswith("s̻")
    assert bare("eu", "sagar").startswith("s̺")
    assert bare("eu", "xarma").startswith("ʃ")
    assert bare("eu-x-bizkaiera", "zezen").startswith("s̺")


@pytest.mark.xfail(
    strict=True,
    reason="Hualde et al. (2010: 116) is cited for intervocalic [β ð ɣ]; the "
           "engine keeps the stops — alaba [alaba], ogia [oɡia]",
)
def test_eu_intervocalic_voiced_stops_are_approximants():
    """Standard Basque notes: "Voiced stops /b d ɡ/ are realised as approximants
    [β ð ɣ] intervocalically (Hualde et al. 2010: 116)."
    """
    assert "β" in word("eu", "alaba")
    assert "ɣ" in word("eu", "ogia")


@pytest.mark.xfail(
    strict=True,
    reason="Hualde et al. (2010: 120) is cited for nasal place assimilation; "
           "the engine leaves the alveolar — hanka [hanka]",
)
def test_eu_nasal_place_assimilation():
    """Standard Basque notes: "nasals assimilate in place to a following
    consonant (2010: 120)" — /n/ before the velar /k/ of ⟨hanka⟩ must be [ŋ].
    """
    assert "ŋ" in word("eu", "hanka")


def test_eu_bizkaiera_palatal_stop_merged_into_the_affricate():
    """Biscayan notes: "MERGER of the voiceless palatal stop /c/ (spelled tt)
    with the postalveolar affricate /tʃ/, in favour of /tʃ/ (Bedialauneta &
    Hualde 2023: 1098)."

    Minimal pair by variety: the same ⟨tt⟩ is the palatal stop in Batua.
    """
    assert "tʃ" in bare("eu-x-bizkaiera", "tturru")
    assert "c" in bare("eu", "ttantta")


# ═══════════════════════════════════════════════════════════════════════════
# Asturleonese
# ═══════════════════════════════════════════════════════════════════════════

def test_ast_x_is_postalveolar_not_velar():
    """Asturian notes (ALLA 2021; Cano González 2009): "⟨x⟩ = /ʃ/ (voiceless
    postalveolar), not /x/ — 'xema' [ʃema] vs. Spanish 'jema' [xema]."
    """
    assert bare("ast", "xema") == "ʃema"
    assert "x" not in bare("ast", "xema")


def test_ast_betacism_merges_v_into_b():
    """Asturian notes (ALLA 2021): "(5) Betacism: ⟨b⟩ = ⟨v⟩ = /b/."""
    assert bare("ast", "vaca").startswith("b")
    assert "v" not in bare("ast", "vaca")


def test_ast_has_no_unstressed_vowel_reduction():
    """Asturian notes (ALLA 2021; Penny 2002): "(6) No vowel reduction: 5-vowel
    system, unstressed vowels full."

    The unstressed final ⟨a⟩ of ⟨casa⟩ stays [a] — the segment Central Catalan
    and European Portuguese would reduce.
    """
    out = bare("ast", "casa")
    assert out == "kasa"
    assert "ə" not in out and "ɐ" not in out and "ɨ" not in out


def test_ast_western_raises_final_o_where_eastern_keeps_it():
    """Western notes: "(2) FINAL -u CLOSURE: word-final Latin -O → /u/ ...
    Encoded as positional rule: word-final ⟨o⟩ → [u]" (Source A p. 10; Source B
    §2.4). Eastern notes: "(2) FINAL -o (not -u): eastern varieties preserve
    Latin -O as -o rather than raising to -u" (Source B §2.4; Source A p. 8).

    Same word, sister dialects: the final vowel is the only segment that moves.
    """
    assert bare("ast-x-occidental", "poco") == "poku"
    assert bare("ast-x-oriental", "poco") == "poko"


def test_ast_rionor_tch_is_the_affricate_and_ch_is_the_fricative():
    """Rionorese notes (Macias 2003, p. 26; stated-explicitly): "(2) AFFRICATE
    /tʃ/ WRITTEN ⟨tch⟩: *tchamar* (chamar) ... ⟨ch⟩ (without t-) = /ʃ/
    (Portuguese-type, not affricate)."

    Orthographic minimal pair inside one variety.
    """
    assert bare("ast-PT-x-rionor", "tchamar").startswith("tʃ")
    assert bare("ast-PT-x-rionor", "chamar").startswith("ʃ")


def test_ast_rionor_o_diphthongs_are_wo_and_wa():
    """Rionorese notes (Macias 2003, pp. 25-26; stated-explicitly): "Latin /o/ →
    ⟨uô⟩ /wɔ/: *ruôdra* (roda) ... Latin /o/ in other environments → ⟨uâ⟩ /wɐ/
    ...: *puârta, fuârte, muârtu*", and "(4) FINAL -o → /u/: systematic".
    """
    assert bare("ast-PT-x-rionor", "ruôdra").startswith("rwɔ")
    assert bare("ast-PT-x-rionor", "puârta").startswith("pwɐ")
    assert bare("ast-PT-x-rionor", "corpo").endswith("u")


def test_ast_sanabria_o_diphthong_is_the_archaic_wo():
    """Sanabrese notes (Frías-Conde, p. 3): "Latin Ŏ → /wo/ (NOT /we/):
    *cuorpo, ruoda, puode, lluogo* — the /wo/ form is MORE ARCHAIC than
    Castilian /we/."

    The contrast is against the Castilian-type /we/ that Aragonese has.
    """
    assert bare("ast-x-sanabria", "cuorpo").startswith("kwo")
    assert bare("an", "bueno").startswith("bwe")


# ═══════════════════════════════════════════════════════════════════════════
# Aragonese
# ═══════════════════════════════════════════════════════════════════════════

def test_an_x_and_ix_are_postalveolar():
    """Aragonese notes (Nagore Laín 2001; ELA): "(5) ⟨x⟩ = /ʃ/ and ⟨ix⟩ = /ʃ/:
    as in Catalan and Galician (Aragons. 'xa' [ʃa] 'already', 'baixo' [ˈbaʃo]
    'low')."
    """
    assert bare("an", "xa") == "ʃa"
    assert bare("an", "baixo").endswith("ʃo")


def test_an_ny_digraph_is_the_palatal_nasal():
    """Aragonese notes: "(7) ⟨ny⟩ = /ɲ/ alongside ⟨ñ⟩ (Catalan orthographic
    convention)."
    """
    assert bare("an", "nyapa").startswith("ɲ")
    assert bare("an", "añada").startswith("aɲ")


def test_an_theta_for_z_and_soft_c():
    """Aragonese notes: "(2) Distinción: /θ/ preserved for c+e/i and z"
    (Nagore Laín 2001; Arnal Purroy & Enguita Utrilla 1993).
    """
    assert bare("an", "zapato").startswith("θ")
    assert bare("an", "cinco").startswith("θ")


def test_an_latin_f_initial_is_preserved():
    """Aragonese notes: "(1) F- PRESERVED: Latin initial F- retained as /f/
    (feito 'done' < FACTU, fiyo 'son' < FILIU, fablar 'to speak' < FABULARE) —
    contrast Castilian h- (hecho, hijo, hablar). This is the most salient
    isogloss separating Aragonese from Castilian."

    The isogloss pair: Castilian spells the same etymon with a silent ⟨h⟩.
    """
    assert bare("an", "feito").startswith("f")
    assert bare("an", "fillo").startswith("f")
    assert not bare("es-ES", "hecho").startswith("f")


# ═══════════════════════════════════════════════════════════════════════════
# Extremaduran
# ═══════════════════════════════════════════════════════════════════════════

def test_ext_seseo_merges_theta_into_s():
    """Extremaduran notes (González Salgado 2000; Zamora Vicente 1960): "(1)
    SESEO (complete in most areas): /θ/ = /s/ — ⟨c⟩ before e/i and ⟨z⟩ → /s/,
    merging distinción into seseo."

    Minimal pair by variety: Aragonese keeps the distinción on the same word.
    """
    assert bare("ext", "cinco").startswith("s")
    assert bare("ext", "zapato").startswith("s")
    assert bare("an", "cinco").startswith("θ")


def test_ext_word_final_s_aspirates():
    """Extremaduran notes: "(2) ASPIRATION OF WORD-FINAL AND PRE-CONSONANTAL
    /s/: coda /s/ → [h] or deleted — one of the most salient features; 'estos
    hombres' [ˈehtoh ˈõmbɾeh]."
    """
    assert bare("ext", "estos").endswith("h")
    assert phrase("ext", "estos hombres")[1].endswith("h")


@pytest.mark.xfail(
    strict=True,
    reason="the cited form [ˈehtoh] aspirates the PRE-CONSONANTAL /s/ of estos "
           "as well; the engine aspirates only the word-final one: [estoh]",
)
def test_ext_preconsonantal_s_aspirates():
    """Extremaduran notes: "(2) ASPIRATION OF WORD-FINAL AND PRE-CONSONANTAL
    /s/: coda /s/ → [h] or deleted ... 'estos hombres' [ˈehtoh ˈõmbɾeh]."

    The isolated segment is the syllable-coda /s/ of ⟨es-tos⟩, which the
    citation writes as [h].
    """
    assert bare("ext", "estos").startswith("eh")


def test_ext_word_final_d_is_deleted():
    """Extremaduran notes: "(5) WORD-FINAL /d/ → [∅]: verdad [berˈdá] (complete
    elision more frequent than standard Castilian [ð])."
    """
    assert bare("ext", "verdad") == "beɾda"


def test_ext_yeismo():
    """Extremaduran notes: "(4) YEÍSMO: ⟨ll⟩ = ⟨y⟩ = /j/ or /ʝ/ (majority of
    speakers ...)."

    Minimal pair by variety: Asturian keeps /ʎ/ on the same digraph.
    """
    assert "ʎ" not in bare("ext", "calle")
    assert "ʎ" in bare("ast", "llobu")


@pytest.mark.xfail(
    strict=True,
    reason="notes cite 'jota' [ˈhota]; the engine keeps the Castilian velar "
           "fricative: [xota]",
)
def test_ext_velar_fricative_weakens_to_h():
    """Extremaduran notes: "(7) /x/ → [h]: the velar fricative weakens to [h] in
    many Extremaduran registers — 'jota' [ˈhota]"."""
    assert bare("ext", "jota").startswith("h")


@pytest.mark.xfail(
    strict=True,
    reason="notes cite hijo [ˈhiho] (F- aspiration + /x/ → [h]); the engine "
           "gives [ixo] — the ⟨h⟩ is silent and the ⟨j⟩ stays velar",
)
def test_ext_f_aspiration_gives_an_audible_h():
    """Extremaduran notes: "(3) F- ASPIRATION (rural/archaic): Latin F- → [h] in
    many rural areas (hacer [ˈhaθeɾ], hijo [ˈhiho]) — shared with Andalusian
    and attributed to Leonese substrate."
    """
    assert bare("ext", "hijo").startswith("h")


# ═══════════════════════════════════════════════════════════════════════════
# Occitan
# ═══════════════════════════════════════════════════════════════════════════

def test_oc_infinitive_is_paroxytone_with_a_silent_final_r():
    """Occitan stress notes (Bec 1973; Alibert): "Infinitives in -ar/-er/-ir are
    paroxytone (the final -r is silent in spoken Occitan but syllabified here,
    so penult_stress_endings must list them explicitly)."

    Minimal pair against the default: ⟨occitan⟩, ending in a consonant that is
    not an infinitive ending, is oxytone.
    """
    assert word("oc", "cantar") == "ˈkanta"
    assert word("oc", "occitan") == "uksiˈta"


def test_oc_final_o_reads_as_u():
    """Occitan stress notes (Alibertine norm): "Words ending in a vowel (a e i
    u, not o which maps [u]) ... Note: o-final words are rare in Oc orthography
    since o reads [u]; nominal -or/-on are oxytone."
    """
    assert word("oc", "flor") == "ˈflu"


# ═══════════════════════════════════════════════════════════════════════════
# Franco-Provençal
# ═══════════════════════════════════════════════════════════════════════════

def test_frp_ca_palatalisation():
    """Franco-Provençal notes (Kristol 2016): "(1) CA- → [tʃ] (like French, vs
    Occitan [ka])."

    Minimal pair by language: Occitan keeps the velar in the same etymon
    (cantar).
    """
    assert bare("frp", "chantar").startswith("tʃ")
    assert bare("oc", "cantar").startswith("k")


def test_frp_final_a_is_preserved():
    """Franco-Provençal notes: "(2) Final -a preserved (unlike French)."""
    assert bare("frp", "fenna").endswith("a")


def test_frp_u_fronting():
    """Franco-Provençal notes: "(3) /u/→/y/ fronting (shared with French)."""
    assert "y" in bare("frp", "dua")


# ═══════════════════════════════════════════════════════════════════════════
# Italo-Romance minorities
# ═══════════════════════════════════════════════════════════════════════════

def test_sc_velars_are_preserved_before_a_front_vowel():
    """Sardinian notes (Lausberg 1971; Blasco Ferrer 1984): "(1) Velars /k, ɡ/
    preserved before front vowels (kentu 'hundred', not *centu)."

    Minimal pair by language: Italian palatalises the same velar.
    """
    assert bare("sc", "kentu").startswith("k")
    assert bare("sc", "chentu").startswith("k")
    assert bare("it-IT", "cento").startswith("tʃ")


def test_sc_five_vowel_system_has_no_open_mid_vowels():
    """Sardinian notes: "(2) 5-vowel system (no ɛ/e or ɔ/o split)."""
    out = bare("sc", "pane")
    assert "e" in out and "ɛ" not in out


@pytest.mark.xfail(
    strict=True,
    reason="notes claim retroflex [ɖː] from Latin -LL-; the sc spec maps ⟨ll⟩ "
           "to a plain geminate lateral — bellu [belːu]. Sicilian, which makes "
           "the same claim, does produce [ɖː]",
)
def test_sc_retroflex_from_latin_geminate_l():
    """Sardinian notes (Lausberg 1971; Blasco Ferrer 1984): "(4) Retroflex
    consonants [ɖː] from Latin -LL-."
    """
    assert "ɖ" in bare("sc", "bellu")


def test_scn_retroflex_consonants():
    """Sicilian notes (Ferrante 2020): "(2) Retroflex consonants: -LL- → [ɖː]
    (beddu 'beautiful'), TR → [ʈɽ]."
    """
    assert "ɖː" in bare("scn", "beddu")
    assert bare("scn", "tri").startswith("ʈɽ")


def test_scn_five_vowel_system_is_the_open_mid_one():
    """Sicilian notes (Ferrante 2020): "(1) 5-VOWEL system /a ɛ i ɔ u/ (like
    Sardinian, more archaic than Italian's 7)" — the mid vowels are the OPEN
    ones, so ⟨e⟩ is [ɛ] and ⟨o⟩ is [ɔ].
    """
    assert "ɛ" in bare("scn", "beddu")
    assert "ɔ" in bare("scn", "picciottu")


@pytest.mark.xfail(
    strict=True,
    reason="Ledgeway (2009) is cited for unstressed vowels → [ə]; the engine "
           "keeps full vowels — paese [paese], bello [belːo]",
)
def test_nap_unstressed_vowels_reduce_to_schwa():
    """Neapolitan notes (Ledgeway 2009; De Blasi & Imperatore 2000): "(2)
    Unstressed vowels → [ə]."
    """
    assert "ə" in bare("nap", "paese")


def test_nap_gemination_is_kept():
    """Neapolitan notes (Ledgeway 2009): "(3) Rich gemination."

    Minimal pair by language: Piedmontese, which the specs describe as
    degeminating, has no long consonant.
    """
    assert "lː" in bare("nap", "bello")


def test_fur_ca_ga_palatalisation():
    """Friulian notes (Iliescu 2016): "(2) CA-/GA- palatalisation to
    [tʃ]/[dʒ]."
    """
    assert bare("fur", "cjase").startswith("tʃ")
    assert bare("fur", "gjat").startswith("dʒ")


def test_lld_pl_cl_fl_clusters_are_preserved():
    """Ladin notes (Craffonara 1977): "(3) Preservation of Latin PL-, CL-, FL-
    clusters."

    The contrast is against Asturleonese, which palatalises the same clusters
    to [tʃ] (chamar < PLANU-type).
    """
    assert bare("lld", "plan").startswith("pl")
    assert bare("lld", "cluf").startswith("kl")
    assert bare("ast", "chover").startswith("tʃ")


@pytest.mark.xfail(
    strict=True,
    reason="notes claim CA- → [tʃ]; the engine reads ⟨ci⟩ as a velar plus "
           "vowel and gives ciasa [kiasa]",
)
def test_lld_ca_palatalisation():
    """Ladin notes (Craffonara 1977): "(1) CA- → [tʃ] palatalisation."""
    assert bare("lld", "ciasa").startswith("tʃ")


@pytest.mark.xfail(
    strict=True,
    reason="notes claim CA- palatalisation; the engine reads Romansh ⟨ch⟩ as "
           "the plain velar — chasa [kasa]",
)
def test_rm_ca_palatalisation():
    """Romansh notes (Liver 1999): "(1) CA- palatalisation" — the reflex of
    Latin CASA is written ⟨chasa⟩ in Rumantsch Grischun and is a palatal, not
    the velar [k] that would make it homophonous with an unpalatalised form.
    """
    assert not bare("rm", "chasa").startswith("k")


def test_pms_front_rounded_vowels():
    """Piedmontese notes (Berruto 1974; Loporcaro 2009): "(1) Front rounded
    vowels /y, ø/ (Gallo-Romance innovation)."
    """
    assert "ø" in bare("pms", "cheur")


def test_lmo_front_rounded_vowels():
    """Lombard notes (Sanga 1984): "(1) Front rounded vowels /y, ø/."""
    out = bare("lmo", "fioeu")
    assert "y" in out or "ø" in out


def test_egl_front_rounded_vowels_and_degemination():
    """Emilian-Romagnol notes (Hajek 1997; Loporcaro 2009): "(1) Front rounded
    vowels /y, ø/ ... (4) Degemination."

    ⟨bulåggna⟩ carries both: the ⟨u⟩ is front rounded and the written geminate
    ⟨gg⟩ is one consonant.
    """
    out = bare("egl", "bulåggna")
    assert "y" in out
    assert "ɡɡ" not in out and "ɡː" not in out


def test_vec_has_no_u_fronting():
    """Venetian notes (Ferguson 2007; Zamboni 1974): "(5) No /y/ fronting."

    Minimal pair by language: Lombard and Piedmontese front the same vowel,
    Venetian does not.
    """
    assert bare("vec", "luna") == "luna"
    assert "y" not in bare("vec", "luna")


def test_mzs_word_initial_velar_nasal():
    """Macanese notes: "(2) WORD-INITIAL NG-: Malay-derived words allow initial
    /ŋ/ (ngapi, etc.)" — a syllable onset no Portuguese word can have."""
    assert bare("mzs", "ngapi").startswith("ŋ")


def test_mzs_portuguese_palatal_series():
    """Macanese notes: "(5) PALATAL CONSONANTS: ch=[tʃ], lh=[ʎ], nh=[ɲ], j=[ʒ],
    x=[ʃ] from PT."

    ⟨ch⟩ = [tʃ] is the diagnostic one: European Portuguese has [ʃ] there, so
    Patuá keeps the older affricate.
    """
    assert bare("mzs", "chuchu").startswith("tʃ")
    assert "ʎ" in bare("mzs", "filho")
    assert "ɲ" in bare("mzs", "vinho")
    assert bare("mzs", "janela").startswith("ʒ")
    assert bare("mzs", "xá").startswith("ʃ")
