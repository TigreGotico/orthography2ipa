"""Cited-rule tests for the African, Caucasus/Siberian, Pacific and
reconstructed-language specs.

Every test below pins ONE claim that a spec makes with a citation, on a real
word of the language, isolating the segment the claim is about.  Where the
engine contradicts the citation the test is an ``xfail(strict=True)`` that
keeps the assertion the citation demands.  Where a spec explicitly documents
its own limit, that limit is pinned with a passing test.

Kabyle (kab) is not re-tested here: its cited spirantization rules are already
covered by ``tests/test_kabyle.py``.
"""

import unicodedata

import pytest

from orthography2ipa.g2p import G2P


# ---------------------------------------------------------------------------
# zgh — Standard Moroccan Amazigh (Neo-Tifinagh, IRCAM)
# ---------------------------------------------------------------------------

def test_zgh_tifinagh_is_a_true_alphabet_with_written_vowels():
    """"Written in Neo-Tifinagh (IRCAM variant) ... which is a true alphabet:
    vowels are written with their own letters, not diacritics."  ⵜⴰⵎⴰⵣⵉⵖⵜ
    'Tamazight' spells each of its vowels and yields them in the output."""
    assert G2P("zgh").transcribe_word("ⵜⴰⵎⴰⵣⵉⵖⵜ") == "tamaziɣt"


def test_zgh_labialisation_mark_yields_labiovelar():
    """"Labiovelars ⴳⵯ /ɡʷ/ and ⴽⵯ /kʷ/ are written with the labialisation
    mark ⵯ."  agʷmar 'horse': ⴳ + ⵯ is one labiovelar segment, not /ɡ/ + /w/."""
    assert G2P("zgh").transcribe_word("ⴰⴳⵯⵎⴰⵔ") == "aɡʷmar"


def test_zgh_emphatics_are_distinct_letters():
    """"Emphatic (pharyngealised) consonants ⴹ ⵕ ⵚ ⵟ ⵥ are distinct letters."
    adˤarˤ 'foot': ⴹ = /dˤ/ and ⵕ = /rˤ/, each carrying its own pharyngealisation."""
    assert G2P("zgh").transcribe_word("ⴰⴹⴰⵕ") == "adˤarˤ"


# ---------------------------------------------------------------------------
# kcg — Tyap (Tyap Literacy Committee alphabet; Follingstad 1992)
# ---------------------------------------------------------------------------

def test_kcg_z_is_a_voiced_affricate():
    """"Gotchas: ⟨z⟩ is /d͡z/, NOT [z]" (Tyap Literacy Committee alphabet,
    Follingstad 1992).  Zwunzwuo 'writing' has ⟨z⟩ twice and both are /d͡z/."""
    assert G2P("kcg").transcribe_word("Zwunzwuo") == "d͡zwund͡zwuo"


def test_kcg_a_with_macron_below_is_schwa():
    """"a̱ /ə/ ... ⟨a̱⟩ and ⟨i̱⟩ are the base letter plus COMBINING MACRON BELOW
    (U+0331)."  a̱lyem 'language' begins with the schwa, not with /a/."""
    assert G2P("kcg").transcribe_word("a̱lyem") == "əljem"


def test_kcg_y_is_the_palatal_glide():
    """"y /j/" in the Tyap Literacy Committee chart.  Tyap, the language's own
    name, has ⟨ty⟩ = /t/ + /j/."""
    assert G2P("kcg").transcribe_word("Tyap") == "tjap"


def test_kcg_tone_is_not_emitted():
    """Declared limit: "the literacy-committee alphabet marks no tone ... This
    spec transcribes SEGMENTS ONLY; unwritten tone is NOT RECOVERABLE."  No
    tone letter or accent appears in the output."""
    out = G2P("kcg").transcribe_word("a̱lyem")
    assert not any(c in out for c in "˥˦˧˨˩́̀")


# ---------------------------------------------------------------------------
# kus — Kusaal (unified orthography, Eddyshaw's 'B3')
# ---------------------------------------------------------------------------

def test_kus_hooked_v_is_near_close_back():
    """"The reformed orthography writes ⟨ʋ⟩ for /ʊ/."  Kʋsaal, the language's
    own name, has ⟨ʋ⟩ = [ʊ] in the first syllable."""
    assert G2P("kus").transcribe_word("Kʋsaal") == "kʊsaal"


def test_kus_apostrophe_is_vowel_glottalisation_not_a_consonant_letter():
    """"The apostrophe ⟨'⟩ marks vowel GLOTTALISATION ... it is mapped to [ʔ]
    as the closest segmental approximation."  nu'ug 'hand' → [nuʔuɡ]."""
    assert G2P("kus").transcribe_word("nu'ug") == "nuʔuɡ"


def test_kus_labial_velar_kp_is_one_segment():
    """"LABIAL-VELARS ⟨kp gb⟩ = /k͡p ɡ͡b/."  kpiim 'the dead' → a single
    doubly-articulated /k͡p/, not a /k/ + /p/ cluster."""
    assert G2P("kus").transcribe_word("kpiim") == "k͡piim"


def test_kus_tone_is_not_emitted():
    """Declared limit: "The standard orthography DOES NOT MARK TONE ... so tone
    is NOT RECOVERABLE from orthographic input and is not modelled here"."""
    out = G2P("kus").transcribe_word("Kʋsaal")
    assert not any(c in out for c in "˥˦˧˨˩")


# ---------------------------------------------------------------------------
# gor — Gorontalo
# ---------------------------------------------------------------------------

def test_gor_apostrophe_is_the_glottal_stop():
    """"⟨q⟩ = the glottal stop /ʔ/ (also written with an apostrophe in some
    texts, e.g. wala'o 'child')" (Omniglot; Little 1995)."""
    assert G2P("gor").transcribe_word("wala'o") == "walaʔo"


def test_gor_five_vowels_and_plain_h():
    """"Five vowels ⟨a e i o u⟩ = /a e i o u/."  Hulontalo, the language's own
    name, comes out with the cardinal five-vowel values."""
    assert G2P("gor").transcribe_word("Hulontalo") == "hulontalo"


# ---------------------------------------------------------------------------
# fon — Fon (Höftmann & Ahohounkpanzon, Dictionnaire fon-français, pp.19-20)
# ---------------------------------------------------------------------------

def test_fon_h_is_a_velar_fricative_not_glottal():
    """"⟨h⟩ = /ɣ/ (NOT [h])" (Höftmann & Ahohounkpanzon, pp.19-20).  hun
    'blood' → [ɣun]."""
    assert G2P("fon").transcribe_word("hun") == "ɣun"


def test_fon_hw_is_a_labialised_velar_fricative():
    """"⟨xw⟩ = /xʷ/" (ibid.).  xwe 'house' → [xʷe]: ⟨xw⟩ is one labialised
    fricative, not /x/ + /w/."""
    assert G2P("fon").transcribe_word("xwe") == "xʷe"


def test_fon_c_is_a_palatal_affricate():
    """"⟨c⟩ = /t͡ɕ/ (commonly transcribed /t͡ʃ/)" (ibid.).  cè 'my' → [t͡ɕe]."""
    assert G2P("fon").transcribe_word("ce") == "t͡ɕe"


def test_fon_gb_is_a_labial_velar_stop():
    """"⟨gb⟩ = /ɡ͡b/" (ibid.).  fɔngbe, the language's own name, ends in the
    single doubly-articulated /ɡ͡b/."""
    assert G2P("fon").transcribe_word("fongbe") == "fonɡ͡be"


def test_fon_nasal_vowels_are_under_generated():
    """Declared limit: "in the orthography a nasal vowel is written vowel + ⟨n⟩
    (e.g. ⟨linkpɔn⟩) ... so ⟨n⟩ always maps to /n/ and nasal vowels are
    under-generated"."""
    out = G2P("fon").transcribe_word("linkpɔn")
    assert "n" in out and "̃" not in out


# ---------------------------------------------------------------------------
# bm — Bambara (Bamako 1967 alphabet, rev. 1982)
# ---------------------------------------------------------------------------

def test_bm_c_is_a_postalveolar_affricate():
    """"⟨c⟩ = /t͡ʃ/" in the official Bambara orthography.  cɛ 'man', here in
    its bare-vowel spelling ce, opens with the affricate."""
    assert G2P("bm").transcribe_word("ce") == "tʃe"


def test_bm_j_is_a_voiced_affricate():
    """"⟨j⟩ = /d͡ʒ/" (ibid.).  ji 'water' → [dʒi]."""
    assert G2P("bm").transcribe_word("ji") == "dʒi"


def test_bm_no_tone_is_emitted():
    """"Bambara is a two-tone language (high vs low/mid) but tone is NOT written
    in the standard orthography, so no tone is emitted here"."""
    out = G2P("bm").transcribe_word("bamanankan")
    assert not any(c in out for c in "˥˦˧˨˩")


# ---------------------------------------------------------------------------
# wo — Wolof (official Latin orthography, 2005 revision)
# ---------------------------------------------------------------------------

def test_wo_c_is_a_plain_palatal_stop():
    """"⟨c⟩ = palatal /c/" (Senegalese orthography decree).  ceeb 'rice' opens
    with the stop /c/, not with an affricate."""
    assert G2P("wo").transcribe_word("ceeb") == "cɛɛb"


def test_wo_j_is_a_voiced_palatal_stop():
    """"⟨j⟩ = /ɟ/" (ibid.).  jigéen 'woman' opens with the palatal stop."""
    assert G2P("wo").transcribe_word("jigéen").startswith("ɟ")


def test_wo_n_tilde_is_a_palatal_nasal():
    """"⟨ñ⟩ = /ɲ/" (ibid.).  ñuul 'to be black' → [ɲuul]."""
    assert G2P("wo").transcribe_word("ñuul") == "ɲuul"


def test_wo_bare_a_is_lowered_to_schwa_like_central_vowel():
    """"⟨a⟩ [ɐ] vs ⟨à⟩ [a]" (ibid.): the bare vowel letter is the centralised
    quality.  xam 'to know' → [xɐm], with ⟨x⟩ = /x/ in the same word."""
    assert G2P("wo").transcribe_word("xam") == "xɐm"


def test_wo_word_initial_prenasalised_cluster_is_written_mb():
    """"Word-initial prenasalised consonants are written ⟨mb nd nj ng⟩."
    mbër 'wrestler' keeps the nasal + stop onset, and ⟨ë⟩ = [ə]."""
    assert G2P("wo").transcribe_word("mbër") == "mbər"


# ---------------------------------------------------------------------------
# sn — Shona (1955/1967 standard orthography)
# ---------------------------------------------------------------------------

def test_sn_plain_b_is_an_implosive():
    """"the implosives ⟨b⟩ /ɓ/ and ⟨d⟩ /ɗ/" as against the breathy series.
    baba 'father' → [ɓaɓa]."""
    assert G2P("sn").transcribe_word("baba") == "ɓaɓa"


def test_sn_bh_is_breathy_voiced_not_implosive():
    """"breathy-voiced obstruents written with ⟨h⟩ (bh, dh, mh, nh, vh ...) as
    against the implosives ⟨b⟩ /ɓ/".  Minimal contrast with baba: bhuku 'book'
    opens with the breathy [b̤], not the implosive [ɓ]."""
    assert G2P("sn").transcribe_word("bhuku") == "b̤uku"


def test_sn_mh_is_a_breathy_nasal():
    """"breathy-voiced obstruents written with ⟨h⟩ (bh, dh, mh, nh, vh ...)".
    mhuka 'animal' → [m̤uka]."""
    assert G2P("sn").transcribe_word("mhuka") == "m̤uka"


def test_sn_sv_is_a_whistled_sibilant():
    """"the whistled sibilants written with ⟨v⟩ (sv, zv, tsv, dzv, nzv)".
    svika 'to arrive' → the whistled [sᶲ], not /s/ + /v/."""
    assert G2P("sn").transcribe_word("svika") == "sᶲika"


def test_sn_no_tone_is_emitted():
    """"Tone is phonemic but not written" — so no tone appears in the output."""
    out = G2P("sn").transcribe_word("imba")
    assert not any(c in out for c in "˥˦˧˨˩")


# ---------------------------------------------------------------------------
# so — Somali (official Latin orthography, 1972)
# ---------------------------------------------------------------------------

def test_so_c_is_the_voiced_pharyngeal():
    """"C = pharyngeal /ʕ/" (Somali Latin orthography, 1972).  caano 'milk'
    → [ʕaːno]."""
    assert G2P("so").transcribe_word("caano") == "ʕaːno"


def test_so_x_is_the_voiceless_pharyngeal():
    """"X = pharyngeal /ħ/" (ibid.).  xaas 'family' → [ħaːs]."""
    assert G2P("so").transcribe_word("xaas") == "ħaːs"


def test_so_dh_is_retroflex_and_x_is_pharyngeal():
    """"DH = retroflex /ɖ/; X = pharyngeal /ħ/" (ibid.).  dhagax 'stone'
    exercises both in one word: [ɖaɡaħ]."""
    assert G2P("so").transcribe_word("dhagax") == "ɖaɡaħ"


def test_so_kh_is_the_velar_fricative():
    """"KH = velar fricative /x/" (ibid.).  khudaar 'vegetables' → [xudaːr]."""
    assert G2P("so").transcribe_word("khudaar") == "xudaːr"


def test_so_vowel_length_is_written_double():
    """"Vowel length is phonemic (doubled letters)."  Soomaali → [soːmaːli]."""
    assert G2P("so").transcribe_word("soomaali") == "soːmaːli"


# ---------------------------------------------------------------------------
# om — Oromo (Qubee, official since 1991)
# ---------------------------------------------------------------------------

def test_om_dh_is_an_implosive():
    """"DH = implosive /ɗ/" (Qubee orthography).  dhugaa 'truth' → [ɗuɡaː]."""
    assert G2P("om").transcribe_word("dhugaa") == "ɗuɡaː"


def test_om_q_is_an_ejective():
    """"Q = ejective /qʼ/" (ibid.).  Qubee, the name of the alphabet itself,
    opens with the ejective."""
    assert G2P("om").transcribe_word("qubee").startswith("qʼ")


def test_om_ny_is_a_palatal_nasal():
    """"NY = /ɲ/" (ibid.).  nyaata 'food' → [ɲaːta], which also shows that
    "vowel length is phonemic (doubled letters)"."""
    assert G2P("om").transcribe_word("nyaata") == "ɲaːta"


# ---------------------------------------------------------------------------
# ts — Tsonga (Baumbach 1987)
# ---------------------------------------------------------------------------

def test_ts_rh_is_a_breathy_trill():
    """"BREATHY RHOTIC: <rh> = [r̤] (breathy-voiced trill), contrastive with
    plain <r> = [r]" (Baumbach 1987).  rhula 'be calm' → [r̤ula]."""
    assert G2P("ts").transcribe_word("rhula") == "r̤ula"


def test_ts_plain_r_is_a_modal_trill():
    """The other half of the same cited contrast: plain ⟨r⟩ = [r].  rula
    keeps the modal trill, so the ⟨rh⟩/⟨r⟩ opposition is real in the output."""
    assert G2P("ts").transcribe_word("rula") == "rula"


def test_ts_tl_is_a_lateral_affricate():
    """"LATERAL AFFRICATE: tl=[tɬ] (lateral affricate), phonemic" (ibid.).
    tlanga 'to play' → [tɬaŋa]."""
    assert G2P("ts").transcribe_word("tlanga") == "tɬaŋa"


def test_ts_bv_is_a_labiodental_affricate():
    """"LABIODENTAL AFFRICATE: bv=[bv], phonemic" (ibid.).  bvula 'to remove'
    keeps the affricate onset."""
    assert G2P("ts").transcribe_word("bvula") == "bvula"


def test_ts_x_is_a_postalveolar_fricative():
    """"SIBILANT COMPLEX: x/xi=[ʃ]" (ibid.).  xikolo 'school' → [ʃikɔlɔ],
    which also shows the cited five-vowel realisations e=[ɛ], o=[ɔ]."""
    assert G2P("ts").transcribe_word("xikolo") == "ʃikɔlɔ"


def test_ts_kh_is_aspirated():
    """"ASPIRATED STOPS: kh/ph/th = [kʰ/pʰ/tʰ], phonemic" (ibid.).  khale
    'long ago' → [kʰalɛ]."""
    assert G2P("ts").transcribe_word("khale") == "kʰalɛ"


# ---------------------------------------------------------------------------
# ng — Ndonga (Oshindonga Orthography 3, 2004, NIED)
# ---------------------------------------------------------------------------

def test_ng_dh_is_a_voiced_dental_fricative():
    """"<dh> = /ð/" (Oshindonga Orthography 3).  ondjila is not the vehicle
    here — dhingi keeps ⟨dh⟩ = [ð], not a stop."""
    assert G2P("ng").transcribe_word("dhingi") == "ðiŋi"


def test_ng_th_is_a_voiceless_dental_fricative():
    """"<th> = /θ/" (ibid.).  ethano 'picture' → [eθano]."""
    assert G2P("ng").transcribe_word("ethano") == "eθano"


def test_ng_g_is_a_fricative_not_a_stop():
    """"<g> = /ɣ/ (voiced velar fricative, not a stop)" (ibid.).  gwana
    → [ɣwana]."""
    assert G2P("ng").transcribe_word("gwana") == "ɣwana"


def test_ng_ndj_is_a_prenasalised_affricate():
    """"<ndj> = /ndʒ/" (ibid.).  ondjila 'road' → [ondʒila]."""
    assert G2P("ng").transcribe_word("ondjila") == "ondʒila"


def test_ng_sh_and_ng_digraphs():
    """"<sh> = /ʃ/, <ng> = /ŋ/" (ibid.).  Oshindonga, the language's own name,
    exercises both."""
    assert G2P("ng").transcribe_word("oshindonga") == "oʃindoŋa"


def test_ng_vowel_length_is_written_double():
    """"VOWEL LENGTH is written by doubling: <aa ee ii oo uu>" (ibid.).
    aandu → [aːndu]."""
    assert G2P("ng").transcribe_word("aandu") == "aːndu"


# ---------------------------------------------------------------------------
# sg — Sango (1984 official orthography)
# ---------------------------------------------------------------------------

def test_sg_tone_diacritics_carry_the_same_vowel_quality_and_no_tone():
    """"Three tones are written on the vowel: low unmarked (a), mid with a
    diaeresis (ä), high with a circumflex (â) — so the accented vowel letters
    here map to the same vowel quality as the bare letter, and tone itself is
    not emitted by this spec."  Sängö therefore transcribes exactly as sango."""
    g = G2P("sg")
    assert g.transcribe_word("sängö") == g.transcribe_word("sango") == "saᵑɡo"


def test_sg_ngb_is_a_prenasalised_labial_velar():
    """"the digraphs kp, gb, mb, mv, nd, ng, ngb, nz for the labial-velar and
    prenasalised consonants" (1984 decree).  ngbanga 'judgement' opens with the
    trigraph ⟨ngb⟩ = one prenasalised labial-velar."""
    assert G2P("sg").transcribe_word("ngbanga") == "ᵑɡ͡baᵑɡa"


def test_sg_mb_is_prenasalised():
    """Same cited digraph list: ⟨mb⟩ is a prenasalised stop.  mbi 'I' →
    [ᵐbi], not /m/ + /b/."""
    assert G2P("sg").transcribe_word("mbi") == "ᵐbi"


# ---------------------------------------------------------------------------
# din — Dinka (Rejaf 1928 / Rek standard orthography)
# ---------------------------------------------------------------------------

def test_din_th_is_a_dental_stop_not_a_fricative():
    """"a following ⟨h⟩ marks the dental series — ⟨th⟩ = /t̪/ ... These are
    STOPS, not fricatives: Dinka has no fricatives other than /ɣ/."
    Thuɔŋjäŋ, the language's own name, opens with the dental stop [t̪]."""
    assert G2P("din").transcribe_word("thuɔŋjäŋ").startswith("t̪")


def test_din_diaeresis_marks_breathy_voice():
    """"the DIAERESIS marks the breathy-voice series ... (⟨ä⟩ = /a̤/)".
    Thuɔŋjäŋ carries the breathy [a̤] in its final syllable."""
    assert G2P("din").transcribe_word("thuɔŋjäŋ") == "t̪uɔŋɟa̤ŋ"


def test_din_length_is_written_by_doubling():
    """"LENGTH: written by DOUBLING the vowel letter (⟨aa⟩ = /aː/, e.g. baai
    'home')"."""
    assert G2P("din").transcribe_word("baai") == "baːi"


def test_din_gamma_is_the_only_fricative():
    """"⟨ŋ⟩ = /ŋ/, ⟨ɣ⟩ = /ɣ/" — the sole fricative of the language.
    ɣɔk 'cattle' → [ɣɔk]."""
    assert G2P("din").transcribe_word("ɣɔk") == "ɣɔk"


def test_din_tone_is_not_emitted():
    """Declared limit: "LEXICAL TONE ... is NOT written in the standard
    orthography and is therefore NOT recoverable; no tone is emitted"."""
    out = G2P("din").transcribe_word("thuɔŋjäŋ")
    assert not any(c in out for c in "˥˦˧˨˩")


# ---------------------------------------------------------------------------
# aa — Afar (Qafar Feera, 1976)
# ---------------------------------------------------------------------------

def test_aa_q_is_the_voiced_pharyngeal():
    """"<q> = /ʕ/" (Qafar Feera, 1976).  Qafar, the people's own name, opens
    with the pharyngeal, and ⟨r⟩ = /ɾ/ closes it."""
    assert G2P("aa").transcribe_word("qafar") == "ʕʌfʌɾ"


def test_aa_x_is_a_retroflex_stop():
    """"<x> = /ɖ/ (retroflex stop)" (ibid.).  baxa 'son' → the retroflex, not
    a fricative."""
    assert G2P("aa").transcribe_word("baxa") == "bʌɖʌ"


def test_aa_c_is_the_voiceless_pharyngeal_and_length_is_doubled():
    """"<c> = /ħ/ ... long vowels are written double (aa, ee, ii, oo, uu)".
    caado 'custom' → [ħaːdo]."""
    assert G2P("aa").transcribe_word("caado") == "ħaːdo"


# ---------------------------------------------------------------------------
# ak — Akan / Asante Twi (unified Akan orthography)
# ---------------------------------------------------------------------------

def test_ak_tw_is_a_labialised_velar_not_t_plus_w():
    """"⟨tw dw⟩ are orthographic variants of the same labialised velars (not
    /t/ or /d/ + w)" (Akan Orthography Committee).  Twi, the name of the
    language itself, is therefore [kʷi]."""
    assert G2P("ak").transcribe_word("twi") == "kʷi"


def test_ak_ky_is_a_palatal_affricate():
    """"⟨ky gy hy⟩ are the palatal(ised) realisations of underlying /k ɡ h/
    before front vowels, phonetically [tɕ dʑ ɕ]."  kyerɛ 'to show' → [tɕerɛ]."""
    assert G2P("ak").transcribe_word("kyerɛ") == "tɕerɛ"


def test_ak_hy_is_a_palatal_fricative():
    """Same cited rule: ⟨hy⟩ = [ɕ].  hyɛ 'to wear' → [ɕɛ]."""
    assert G2P("ak").transcribe_word("hyɛ") == "ɕɛ"


def test_ak_kw_is_a_labialised_velar():
    """"⟨kw gw hw nw⟩ ... spell the labialised velars /kʷ ɡʷ hʷ ŋʷ/".
    kwan 'road' → [kʷan]."""
    assert G2P("ak").transcribe_word("kwan") == "kʷan"


def test_ak_ny_is_a_palatal_nasal():
    """The unified orthography's ⟨ny⟩ digraph.  Nyame 'God' → [ɲame]."""
    assert G2P("ak").transcribe_word("nyame") == "ɲame"


def test_ak_tone_is_not_emitted():
    """Declared limit: "The standard orthography DOES NOT MARK TONE, so tone is
    NOT RECOVERABLE from orthographic input and is not modelled here"."""
    out = G2P("ak").transcribe_word("akan")
    assert not any(c in out for c in "˥˦˧˨˩")


# ---------------------------------------------------------------------------
# kr — Kanuri (Standard Kanuri Orthography, 1975; Hutchison)
# ---------------------------------------------------------------------------

def test_kr_schwa_letter():
    """"<ǝ> is the central mid vowel /ə/ (encoded U+01DD in Kanuri practice,
    not U+0259; both code points are accepted as input keys here)" (Hutchison).
    kǝla 'head' → [kəla]."""
    assert G2P("kr").transcribe_word("kǝla") == "kəla"


def test_kr_schwa_accepts_both_code_points():
    """Same claim, its second half: both U+01DD ⟨ǝ⟩ and U+0259 ⟨ə⟩ are accepted
    as input keys and give the same result."""
    g = G2P("kr")
    assert g.transcribe_word("kǝla") == g.transcribe_word("kəla") == "kəla"


def test_kr_tone_is_not_emitted():
    """Declared limit: "TONE IS NOT WRITTEN in the SKO (Hutchison states this
    explicitly) ... tone is NOT recoverable ... and is not emitted here"."""
    out = G2P("kr").transcribe_word("kanuri")
    assert not any(c in out for c in "˥˦˧˨˩")


# ---------------------------------------------------------------------------
# sw — Swahili (stress; Nurse & Hinnebusch 1993)
# ---------------------------------------------------------------------------

def test_sw_penultimate_stress():
    """Stress rule: "Swahili (Standard ...) has regular penultimate stress in
    native vocabulary.  Source: Nurse & Hinnebusch (1993), Swahili and Sabaki."
    nyumba 'house' and habari 'news' both take stress on the penult."""
    g = G2P("sw")
    assert g.transcribe_word("nyumba") == "ˈɲumba"
    assert g.transcribe_word("habari") == "haˈbari"


# ---------------------------------------------------------------------------
# id / ms — Indonesian and Malay stress
# ---------------------------------------------------------------------------

def test_id_penultimate_stress():
    """Stress rule: "Indonesian default stress is penultimate (-2).  Source:
    Lapoliwa (1981), Sneddon (2003)."  makan 'to eat' → [ˈmakan]."""
    assert G2P("id").transcribe_word("makan") == "ˈmakan"


def test_ms_penultimate_stress():
    """Stress rule: "Malay default stress is penultimate (-2).  Source: Clynes
    & Deterding (2011), Adelaar & Himmelmann (2005)."  makan 'to eat' should be
    [ˈmakan]."""
    assert G2P("ms").transcribe_word("makan") == "ˈmakan"


# ---------------------------------------------------------------------------
# ab — Abkhaz (1954 Cyrillic orthography)
# ---------------------------------------------------------------------------

def test_ab_labialisation_modifier_forms_one_grapheme():
    """"the modifier letters ⟨ь⟩ (palatalisation) and ⟨ә⟩ U+04D9
    (labialisation) combine with a base consonant to spell a distinct phoneme
    (... шә /ʃʷ/ ...), so every such digraph is ... matched by maximal munch
    ahead of the bare letter."  аԥсшәа 'Abkhaz (language)' ends in [ʃʷɑ]."""
    assert G2P("ab").transcribe_word("аԥсшәа") == "ɑpʰsʃʷɑ"


def test_ab_bare_a_is_the_open_vowel():
    """"Only two vowels are phonemic, /ɑ/ and /ɨ/."  аԥсуа 'Abkhaz (person)'
    shows ⟨а⟩ = /ɑ/, with ⟨у⟩ taking its surface glide value."""
    assert G2P("ab").transcribe_word("аԥсуа") == "ɑpʰswɑ"


# ---------------------------------------------------------------------------
# av — Avar (1938 Cyrillic alphabet)
# ---------------------------------------------------------------------------

def test_av_lambda_digraph_is_a_lateral():
    """"digraphs with ⟨ъ⟩, ⟨ь⟩ and the palochka ⟨ӏ⟩ mark uvulars, laterals and
    ejectives."  лъин 'water' → the lateral fricative [ɬ], not /l/ + /ʔ/."""
    assert G2P("av").transcribe_word("лъин") == "ɬin"


def test_av_palochka_marks_an_ejective():
    """Same cited claim, the ejective half: цӏар 'name' → [t͡sʼar]."""
    assert G2P("av").transcribe_word("цӏар") == "t͡sʼar"


def test_av_doubled_letter_is_the_fortis_series():
    """"doubled letters mark the fortis (geminate) series."  A doubled ⟨чч⟩
    yields the long affricate [t͡ʃː], not two separate affricates."""
    assert G2P("av").transcribe_word("чча") == "t͡ʃːa"


# ---------------------------------------------------------------------------
# bxr — Buryat (1939 Cyrillic)
# ---------------------------------------------------------------------------

def test_bxr_ha_is_the_glottal_fricative():
    """"written since 1939 in the Russian Cyrillic alphabet plus Өө, Үү and
    Һһ /h/."  һайн 'good' opens with [h]."""
    assert G2P("bxr").transcribe_word("һайн").startswith("h")


def test_bxr_ai_digraph_is_a_long_front_vowel():
    """"the sequences ⟨ай ой үй⟩ are realised as the long vowels [ɛː œː yː]"
    (Wikipedia 'Cyrillic alphabets', Buryat row).  һайн → [hɛːn]: ⟨ай⟩ is one
    long vowel, not /a/ + /j/."""
    assert G2P("bxr").transcribe_word("һайн") == "hɛːn"


def test_bxr_length_is_written_by_doubling():
    """"long vowels are written by DOUBLING the vowel letter (аа ээ ии оо өө уу
    үү)".  буряад 'Buryat' has the long [aː] of ⟨аа⟩."""
    assert G2P("bxr").transcribe_word("буряад") == "burjaad"


# ---------------------------------------------------------------------------
# kv / koi — Komi-Zyrian and Komi-Permyak
# ---------------------------------------------------------------------------

def test_kv_consonant_palatalises_before_front_vowel_and_soft_sign():
    """"⟨д з л н с т⟩ are realised as /ɟ ʑ ʎ ɲ ɕ c/ before ⟨е ё и ю я⟩ and
    before the soft sign ⟨ь⟩, so those sequences are entered here as multigraph
    keys."  нянь 'bread' → [ɲaɲ]: both ⟨ня⟩ and ⟨нь⟩ palatalise."""
    assert G2P("kv").transcribe_word("нянь") == "ɲaɲ"


def test_kv_tsh_digraph_is_a_postalveolar_affricate():
    """"The affricates /dʒ dʑ tʃ/ are written with the digraphs ⟨дж дз тш⟩."
    тшак 'mushroom' → [tʃak], not /t/ + /ʃ/."""
    assert G2P("kv").transcribe_word("тшак") == "tʃak"


def test_kv_dz_digraph_is_an_alveolo_palatal_affricate():
    """Same cited digraph set: ⟨дз⟩ = /dʑ/.  дзоридз 'flower' has it twice."""
    assert G2P("kv").transcribe_word("дзоридз") == "dʑoridʑ"


def test_kv_o_with_diaeresis_is_the_mid_central_vowel():
    """"the Russian alphabet plus ⟨І і⟩ ('hard i') and ⟨Ӧ ӧ⟩ /ɘ/."  сьӧм
    'money' → [ɕɘm], which also shows ⟨сь⟩ = /ɕ/."""
    assert G2P("kv").transcribe_word("сьӧм") == "ɕɘm"


def test_koi_shares_the_komi_zyrian_grapheme_map():
    """"The grapheme map is therefore the Komi-Zyrian one" — Komi-Permyak and
    Komi-Zyrian are described as sharing the same 26 consonants and 7 vowels,
    so the same word transcribes identically in both."""
    assert G2P("koi").transcribe_word("нянь") == G2P("kv").transcribe_word("нянь") == "ɲaɲ"


def test_koi_hard_i_does_not_palatalise():
    """"⟨і⟩ = 'hard i' /i/ leaving the preceding consonant hard" — it is
    "deliberately NOT part of any digraph"."""
    assert G2P("koi").transcribe_word("іи") == "ii"


# ---------------------------------------------------------------------------
# sah — Yakut / Sakha (1939 Cyrillic)
# ---------------------------------------------------------------------------

def test_sah_dj_digraph_is_a_voiced_affricate():
    """"the digraphs ⟨дь⟩ /d͡ʒ/ and ⟨нь⟩ /ɲ/."  Дьокуускай 'Yakutsk' opens
    with the affricate, not with /d/ + a soft sign."""
    assert G2P("sah").transcribe_word("дьокуускай") == "d͡ʒɔkuːskaj"


def test_sah_nj_digraph_is_a_palatal_nasal():
    """Same cited pair: ⟨нь⟩ = /ɲ/.  ньуучча 'Russian' → [ɲuːt͡ʃt͡ʃa]."""
    assert G2P("sah").transcribe_word("ньуучча") == "ɲuːt͡ʃt͡ʃa"


def test_sah_ya_is_a_rising_diphthong():
    """"the four diphthongs are written ⟨ыа иэ уо үө⟩ — all of these are listed
    as multigraph keys so that maximal-munch matching prefers them over the
    single letters."  ыал 'household' → [ɯal]."""
    assert G2P("sah").transcribe_word("ыал") == "ɯal"


# ---------------------------------------------------------------------------
# xal — Kalmyk Oirat (1938 Cyrillic)
# ---------------------------------------------------------------------------

def test_xal_ha_is_a_voiced_velar_fricative():
    """"the Russian letters plus Әә /æ/, Өө /ø/, Үү /y/, Җҗ /d͡ʒ/, Ңң /ŋ/ and
    Һһ /ɣ/."  һал 'fire' → [ɣal]."""
    assert G2P("xal").transcribe_word("һал") == "ɣal"


def test_xal_zhe_is_a_voiced_affricate():
    """Same cited letter list: ⟨җ⟩ = /d͡ʒ/.  җирһл 'life' opens with the
    affricate and keeps ⟨һ⟩ = /ɣ/."""
    assert G2P("xal").transcribe_word("җирһл") == "d͡ʒirɣl"


def test_xal_length_is_written_by_doubling():
    """"the Cyrillic orthography denotes long vowels by DOUBLING the vowel
    letter, so the doubled digraphs (аа әә ээ ии оо өө уу үү) are given as their
    own keys."  өөрд 'Oirat' → [øːrd]."""
    assert G2P("xal").transcribe_word("өөрд") == "øːrd"


# ---------------------------------------------------------------------------
# inh — Ingush (1938 Cyrillic; Nichols)
# ---------------------------------------------------------------------------

def test_inh_gh_digraph_is_a_uvular_fricative():
    """"uvular fricative гӏ /ʁ/ ... the engine matches these by maximal munch,
    so multigraphs win over their component letters."  гӏалгӏай, the Ingush
    people's own name, has ⟨гӏ⟩ twice."""
    assert G2P("inh").transcribe_word("гӏалгӏай") == "ʁɑːlʁɑːj"


def test_inh_latin_i_is_not_accepted_as_a_palochka():
    """Input contract: "the palochka must be U+04CF ⟨ӏ⟩ (lowercase) / U+04C0
    ⟨Ӏ⟩ — Latin 'I', 'l' and the digit '1' are NOT accepted, since no consulted
    source documents them for Ingush."  A Latin-I spelling therefore does NOT
    produce the uvular fricative of ⟨гӏ⟩."""
    assert "ʁ" not in G2P("inh").transcribe_word("гIалгIай")


def test_inh_kh_digraph_is_a_uvular_stop():
    """"uvular кх /q/ and къ /qʼ/" (Nichols).  къам 'people' takes the ejective
    uvular, къ winning over the bare ⟨к⟩."""
    assert G2P("inh").transcribe_word("къам") == "qʼɑːm"


# ---------------------------------------------------------------------------
# kbd — Kabardian (1936 Cyrillic)
# ---------------------------------------------------------------------------

def test_kbd_maximal_munch_prefers_the_longest_trigraph():
    """"each is a grapheme key of its own, matched by maximal munch (longest key
    wins, so кхъу beats кхъ beats къ)."  кхъуэ 'pig' → [q͡χʷa]: the four-letter
    key wins, and ⟨э⟩ = /a/."""
    assert G2P("kbd").transcribe_word("кхъуэ") == "q͡χʷa"


def test_kbd_e_is_the_short_open_vowel():
    """"Phonemic vowels are ⟨э⟩ /a/, ⟨а⟩ /aː/, ⟨ы⟩ /ə/."  адыгэбзэ 'the
    Circassian language' shows all three: [aːdəɣabza]."""
    assert G2P("kbd").transcribe_word("адыгэбзэ") == "aːdəɣabza"


def test_kbd_l_palochka_is_an_ejective_lateral():
    """"⟨ъ⟩ (uvular/back series), ⟨ӏ⟩ (ejective/glottal) and ⟨у⟩ (labialisation)
    combine with a base letter to spell single phonemes — ... лъ, лӏ ..."
    лӏы 'man' → the ejective lateral [ɬʼ]."""
    assert G2P("kbd").transcribe_word("лӏы") == "ɬʼə"


def test_kbd_lh_digraph_is_a_plain_lateral_fricative():
    """The minimal partner of лӏ in the same cited digraph list: лъ = /ɬ/,
    without the ejection.  лъэ 'leg' → [ɬa]."""
    assert G2P("kbd").transcribe_word("лъэ") == "ɬa"


# ---------------------------------------------------------------------------
# lez — Lezgian (1938 Cyrillic, 41 letters)
# ---------------------------------------------------------------------------

def test_lez_palochka_marks_an_ejective():
    """"Multigraphs carry the ejective, uvular and front-vowel series — кӏ пӏ
    тӏ цӏ чӏ (ejectives)".  чӏал 'language' → [t͡ʃʼal]."""
    assert G2P("lez").transcribe_word("чӏал") == "t͡ʃʼal"


def test_lez_soft_sign_digraph_is_a_uvular_ejective():
    """"къ /q/, кь /qʼ/" (Lezgian Cyrillic).  кьил 'head' takes the uvular
    ejective — the soft sign never occurs alone."""
    assert G2P("lez").transcribe_word("кьил") == "qʼil"


def test_lez_plain_stop_is_aspirated_first():
    """"Aspiration is phonemic but NOT written, so к п т ц ч are given
    aspirated-first with the unaspirated variant as a second candidate."
    кар 'matter' therefore surfaces as [kʰar]."""
    assert G2P("lez").transcribe_word("кар") == "kʰar"


# ---------------------------------------------------------------------------
# krc — Karachay-Balkar (1937 Cyrillic)
# ---------------------------------------------------------------------------

def test_krc_qh_digraph_is_a_uvular_stop():
    """"Digraphs: <гъ> = /ʁ/, <къ> = /q/".  Къарачай-малкъар, the language's
    own name, has ⟨къ⟩ twice."""
    assert G2P("krc").transcribe_word("къарачай") == "qaratʃaj"


def test_krc_dzh_digraph_is_a_voiced_affricate():
    """"<дж> = /dʒ/ (Karachay; the Balkar varieties have /ʒ/ or /z/ here)."
    джал → [dʒal]."""
    assert G2P("krc").transcribe_word("джал") == "dʒal"


def test_krc_yu_is_a_front_rounded_vowel():
    """"Front-rounded vowels are written with the Russian iotated letters:
    <ю> = /y/, <ё> = /ø/."  юй 'house' → [yj], not /ju/."""
    assert G2P("krc").transcribe_word("юй") == "yj"


# ---------------------------------------------------------------------------
# dv — Maldivian / Dhivehi (Thaana)
# ---------------------------------------------------------------------------

def test_dv_consonant_plus_fili_transcribes_in_sequence():
    """"its consonant letters carry NO inherent vowel, and each consonant is
    obligatorily followed by a fili ... Because vowels are always written, the
    letter and the following fili can simply be transcribed in sequence."
    ދިވެހި 'Dhivehi' → [d̪iʋehi]."""
    assert G2P("dv").transcribe_word("ދިވެހި") == "d̪iʋehi"


def test_dv_alifu_plus_sukun_is_a_glottal_stop():
    """"the sequence އް (alifu + sukun) marks a glottal stop / the gemination of
    the following consonant, so it is keyed as a multigraph."  ރާއްޖެ 'Maldives'
    → [ɾaːʔdʒe]."""
    assert G2P("dv").transcribe_word("ރާއްޖެ") == "ɾaːʔdʒe"


# ---------------------------------------------------------------------------
# ii — Nuosu / Sichuan Yi (Modern Yi syllabary)
# ---------------------------------------------------------------------------

def test_ii_syllabogram_carries_initial_final_and_tone():
    """"The script is a SYLLABARY: one glyph = one full syllable (initial + rime
    + tone) ... the tone letters: -t high [˥], -x high-rising [˧˦], unmarked mid
    [˧], -p low-falling [˨˩]."  ꆇꉙ (nuo-x hxo-p), the language's own name,
    yields the -x and -p tones."""
    assert G2P("ii").transcribe_word("ꆇꉙ") == "nɔ˧˦ho˨˩"


# ---------------------------------------------------------------------------
# fj — Fijian (Cargill orthography)
# ---------------------------------------------------------------------------

def test_fj_b_is_a_prenasalised_stop():
    """"⟨b d q⟩ are the prenasalised stops /ᵐb ⁿd ᵑɡ/" (Cargill's 1830s
    orthography).  bula 'life/hello' → [ᵐbula]."""
    assert G2P("fj").transcribe_word("bula") == "ᵐbula"


def test_fj_d_is_a_prenasalised_stop():
    """Same cited set: ⟨d⟩ = /ⁿd/.  dina 'true' → [ⁿdina]."""
    assert G2P("fj").transcribe_word("dina") == "ⁿdina"


def test_fj_q_is_a_prenasalised_velar():
    """Same cited set: ⟨q⟩ = /ᵑɡ/.  qito 'game' → [ᵑɡito]."""
    assert G2P("fj").transcribe_word("qito") == "ᵑɡito"


def test_fj_g_is_a_velar_nasal():
    """"⟨g⟩ is /ŋ/" (ibid.).  gone 'child' → [ŋone] — the minimal partner of
    ⟨q⟩ = /ᵑɡ/."""
    assert G2P("fj").transcribe_word("gone") == "ŋone"


def test_fj_c_is_a_dental_fricative():
    """"⟨c⟩ is /ð/ and ⟨v⟩ is /β/" (ibid.).  cava 'what' exercises both:
    [ðaβa]."""
    assert G2P("fj").transcribe_word("cava") == "ðaβa"


def test_fj_v_is_a_bilabial_fricative():
    """"⟨v⟩ is /β/" (ibid.).  Viti 'Fiji' → [βiti], not [viti]."""
    assert G2P("fj").transcribe_word("viti") == "βiti"


# ---------------------------------------------------------------------------
# mh — Marshallese (MED / MOD orthography, Abo et al. 1976)
# ---------------------------------------------------------------------------

def test_mh_every_consonant_carries_a_secondary_articulation():
    """"Every consonant carries a secondary articulation: ... ⟨m ṃ⟩ = /mʲ mˠ/,
    ⟨l ḷ⟩ = /lʲ lˠ/, ⟨j t⟩ = /tʲ tˠ/" (Abo, Bender, Capelle & DeBrum 1976).
    Ṃajeḷ 'Marshall (Islands)' → [mˠɑtʲɛlˠ]."""
    assert G2P("mh").transcribe_word("ṃajeḷ") == "mˠɑtʲɛlˠ"


def test_mh_j_is_a_palatalised_coronal_stop():
    """Same cited series: ⟨j⟩ = /tʲ/, not an affricate or fricative.  Kajin
    'language (of)' → [kɑtʲinʲ], with ⟨n⟩ = /nʲ/."""
    assert G2P("mh").transcribe_word("kajin") == "kɑtʲinʲ"


def test_mh_bw_is_merely_the_velarised_bilabial():
    """"after ⟨b ṃ⟩ [⟨w⟩] merely marks the already-velarised bilabial (⟨bw ṃw⟩
    = /pˠ mˠ/)" — so ⟨bw⟩ is one segment, not /pˠ/ + /w/.  bwebwenato 'story'
    → [pˠɛpˠɛnʲɑtˠo]."""
    assert G2P("mh").transcribe_word("bwebwenato") == "pˠɛpˠɛnʲɑtˠo"


# ---------------------------------------------------------------------------
# bi — Bislama (post-1995 standard orthography)
# ---------------------------------------------------------------------------

def test_bi_ng_is_a_velar_nasal():
    """"Post-1995 standard orthography: 5 vowels, the digraphs ⟨ae⟩ and ⟨ao⟩ for
    diphthongs, ⟨ng⟩ /ŋ/."  blong 'of' → [bloŋ]."""
    assert G2P("bi").transcribe_word("blong") == "bloŋ"


def test_bi_labialisation_is_not_modelled():
    """Declared limit: "labialised consonants are now written with a following
    ⟨w⟩ (mw, pw) — labialisation is not modelled here."  ⟨mw⟩ therefore comes
    out as /m/ + /w/, not /mʷ/."""
    assert G2P("bi").transcribe_word("mwala") == "mwala"


# ---------------------------------------------------------------------------
# ht — Haitian Creole (IPN orthography, 1979)
# ---------------------------------------------------------------------------

def test_ht_r_is_a_velar_fricative():
    """"⟨r⟩ = /ɣ/" (IPN 1979).  Kreyòl → [kɣejɔl], which also shows ⟨ò⟩ = /ɔ/."""
    assert G2P("ht").transcribe_word("kreyòl") == "kɣejɔl"


def test_ht_an_is_a_nasal_vowel():
    """"⟨an en on⟩ are the nasal vowels /ã ɛ̃ ɔ̃/" (ibid.).  manje 'to eat'
    → [mãʒe]: ⟨an⟩ is one nasal vowel, not /a/ + /n/."""
    assert G2P("ht").transcribe_word("manje") == "mãʒe"


def test_ht_on_is_a_nasal_vowel_and_ou_is_u():
    """"⟨an en on⟩ are the nasal vowels /ã ɛ̃ ɔ̃/ ... ⟨ou⟩ = /u/" (ibid.).
    bonjou 'hello' → [bɔ̃ʒu]."""
    assert G2P("ht").transcribe_word("bonjou") == "bɔ̃ʒu"


@pytest.mark.xfail(
    strict=True,
    reason="IPN 1979: an ⟨n⟩+vowel sequence blocks the nasal reading — engine "
           "still nasalises and produces [kãaval] for kanaval",
)
def test_ht_n_plus_vowel_blocks_the_nasal_reading():
    """"⟨an en on⟩ are the nasal vowels /ã ɛ̃ ɔ̃/ (a following hyphen or an
    ⟨n⟩+vowel sequence blocks the nasal reading)" (IPN 1979).  In kanaval
    'carnival' the ⟨n⟩ is followed by a vowel, so the ⟨an⟩ is NOT a nasal
    vowel: [kanaval]."""
    assert G2P("ht").transcribe_word("kanaval") == "kanaval"


# ---------------------------------------------------------------------------
# jam — Jamaican Patois (Cassidy/JLU orthography)
# ---------------------------------------------------------------------------

def test_jam_ch_is_a_postalveolar_affricate_and_doubling_is_length():
    """"<ch>=/tʃ/ ... long vowels doubled (ii, aa, uu)" (Cassidy 1961; JLU
    2002).  chuu 'through' → [tʃuː]."""
    assert G2P("jam").transcribe_word("chuu") == "tʃuː"


def test_jam_j_is_a_voiced_affricate_and_ie_is_a_diphthong():
    """"<j>=/dʒ/ ... diphthongs <ie> <uo> <ai> <ou>" (ibid.).  Jumiekan
    'Jamaican' → [dʒumiekan]."""
    assert G2P("jam").transcribe_word("jumiekan") == "dʒumiekan"


def test_jam_zh_is_a_voiced_postalveolar_fricative():
    """"<zh>=/ʒ/" (ibid.)."""
    assert G2P("jam").transcribe_word("zhaan") == "ʒaːn"


def test_jam_palatalised_onsets_are_not_modelled():
    """Declared limit: "the palatalised <ky>/<gy> onsets are not modelled here."
    kyaan 'can't' therefore yields a plain /k/ + /j/ sequence, not [kʲ]."""
    assert G2P("jam").transcribe_word("kyaan") == "kjaːn"


# ---------------------------------------------------------------------------
# kea — Kabuverdianu (ALUPEC, 1998/2009)
# ---------------------------------------------------------------------------

def _kea(word):
    return unicodedata.normalize("NFC", G2P("kea").transcribe_word(word)).replace(
        "ˈ", ""
    ).replace("ˌ", "")


def test_kea_tx_is_a_voiceless_affricate():
    """"AFFRICATES: tx=[tʃ], dj=[dʒ] — innovations relative to PT" (ALUPEC).
    txeu 'much' → [tʃeu]."""
    assert _kea("txeu").startswith("tʃ")


def test_kea_dj_is_a_voiced_affricate():
    """Same cited pair: dj=[dʒ].  djunta 'to join' → [dʒ…]."""
    assert _kea("djunta").startswith("dʒ")


def test_kea_x_is_a_postalveolar_fricative():
    """"SIBILANT: x=[ʃ], j=[ʒ], s=[s]" (ALUPEC).  xinti 'to feel' → [ʃinti]."""
    assert _kea("xinti").startswith("ʃ")


def test_kea_nasal_vowels_are_phonemic():
    """"NASAL VOWELS: ã/ẽ/ĩ/õ/ũ are phonemic, from African substrate influence
    and retention of archaic PT nasality."  mãi 'mother' keeps the nasal vowel."""
    assert "ã" in _kea("mãi")


def test_kea_h_is_silent():
    """"SILENT H: <h> has no phonetic value" (ALUPEC).  hora → the ⟨h⟩ adds no
    segment, so the transcription opens on the vowel."""
    assert _kea("hora").startswith("o")


# ---------------------------------------------------------------------------
# srn — Sranan Tongo (official 1986 spelling)
# ---------------------------------------------------------------------------

def test_srn_ty_is_a_voiceless_affricate():
    """"⟨ty dy⟩ = /t͡ʃ d͡ʒ/" (official 1986 phonology-based spelling).
    tyari 'to carry' → [t͡ʃaɾi]."""
    assert G2P("srn").transcribe_word("tyari") == "t͡ʃaɾi"


def test_srn_dy_is_a_voiced_affricate():
    """Same cited pair: ⟨dy⟩ = /d͡ʒ/.  dyari 'yard' → [d͡ʒaɾi]."""
    assert G2P("srn").transcribe_word("dyari") == "d͡ʒaɾi"


def test_srn_sy_is_a_postalveolar_fricative():
    """"⟨sy⟩ = /ʃ/" (ibid.).  syen 'shame' → [ʃen]."""
    assert G2P("srn").transcribe_word("syen") == "ʃen"


def test_srn_o_grave_is_open_o():
    """"⟨ò⟩ = /ɔ/" (ibid.).  òdo 'proverb' contrasts the two ⟨o⟩ letters in one
    word: [ɔdo]."""
    assert G2P("srn").transcribe_word("òdo") == "ɔdo"


def test_srn_aw_is_a_diphthong():
    """"⟨aw ow⟩ = the diphthongs /au̯ ou̯/" (ibid.).  kaw 'cow' → [kau̯]."""
    assert G2P("srn").transcribe_word("kaw") == "kau̯"


# ---------------------------------------------------------------------------
# ace — Acehnese (1980 Latin standard)
# ---------------------------------------------------------------------------

@pytest.mark.xfail(
    strict=True,
    reason="1980 Acehnese standard: word-final ⟨k⟩ is a glottal stop — engine "
           "emits a plain [k] in bak",
)
def test_ace_word_final_k_is_a_glottal_stop():
    """"Word-final ⟨k⟩ is realised as a glottal stop" (Acehnese 1980 Latin
    orthography).  bak 'at, tree' should therefore end in [ʔ]."""
    assert G2P("ace").transcribe_word("bak") == "baʔ"


def test_ace_eu_digraph_is_a_close_central_vowel():
    """"Ten oral vowel qualities" of the 1980 standard: ⟨eu⟩ spells the close
    central /ɯ/.  beudoh 'to rise' → [bɯdɔh]."""
    assert G2P("ace").transcribe_word("beudoh") == "bɯdɔh"


# ---------------------------------------------------------------------------
# za — Zhuang (official 1982 Latin orthography)
# ---------------------------------------------------------------------------

def test_za_final_z_is_a_tone_letter():
    """"word-final ⟨z j x q⟩ are TONE letters, not consonants — ⟨z⟩ = ˧˩ (31)"
    (1982 Standard Zhuang orthography).  vunz 'person' → [wun˧˩], with ⟨v⟩ =
    /w/ and no final consonant."""
    assert G2P("za").transcribe_word("vunz") == "wun˧˩"


def test_za_final_x_is_a_tone_letter_and_r_is_a_velar_fricative():
    """"⟨x⟩ = ˦˨ (42) ... ⟨r⟩ = /ɣ/" (ibid.).  raemx 'water' → [ɣam˦˨]:
    ⟨ae⟩ is the short /a/ and the ⟨x⟩ is tone, not a fricative."""
    assert G2P("za").transcribe_word("raemx") == "ɣam˦˨"


def test_za_mb_is_an_implosive_and_w_is_a_vowel():
    """"⟨mb nd⟩ are the implosives /ɓ ɗ/ ... ⟨w⟩ = the VOWEL /ɯ/" (ibid.).
    mbwn 'sky' → [ɓɯn]."""
    assert G2P("za").transcribe_word("mbwn") == "ɓɯn"


def test_za_b_d_g_are_voiceless_onsets():
    """"⟨b d g⟩ are the plain voiceless onsets /p t k/ ... ⟨gv⟩ [is] /kʷ/"
    (ibid.).  Gvangjsae 'Guangxi' opens with [kʷ] and carries the ⟨j⟩ = ˥ tone."""
    assert G2P("za").transcribe_word("gvangjsae") == "kʷaːŋ˥θa"


def test_za_non_final_h_surfaces_as_a_consonant():
    """Declared limit: "in a written compound (e.g. Vahcuengh) an ⟨h⟩ that
    closes a NON-final syllable is still a tone letter but is only resolvable
    word-finally by this spec, so it surfaces as /h/ there."  Vahcuengh, the
    language's own name, shows exactly that: the medial ⟨h⟩ is /h/ while the
    final ⟨h⟩ is the ˧ tone."""
    assert G2P("za").transcribe_word("vahcuengh") == "waːhɕueŋ˧"


# ---------------------------------------------------------------------------
# bdr — West Coast Bajau (2004 Kota Belud community orthography)
# ---------------------------------------------------------------------------

def test_bdr_apostrophe_is_a_contrastive_final_glottal_stop():
    """"the apostrophe ⟨'⟩ = the glottal stop /ʔ/, which occurs only
    word-finally in this dialect and is contrastive (paʔ 'uncle' vs pak
    'frog')" (2004 Bajau orthography workshop).  The cited minimal pair:
    pa' 'uncle' ends in [ʔ]."""
    assert G2P("bdr").transcribe_word("pa'") == "paʔ"


def test_bdr_final_k_is_a_plain_stop():
    """The other half of the cited minimal pair: pak 'frog' ends in a plain
    [k], so the ⟨'⟩/⟨k⟩ contrast survives transcription."""
    assert G2P("bdr").transcribe_word("pak") == "pak"


def test_bdr_long_vowels_are_written_double():
    """"Long vowels are written by DOUBLING the vowel letter (laan /laːn/,
    siin /siːn/)" (ibid.)."""
    g = G2P("bdr")
    assert g.transcribe_word("laan") == "laːn"
    assert g.transcribe_word("siin") == "siːn"


def test_bdr_j_is_a_voiced_palatal_affricate():
    """"⟨j⟩ = the voiced palatal affricate (the source writes it /j/ in
    Americanist notation, parallel to Malay ⟨j⟩)".  Bajau → [badʒau]."""
    assert G2P("bdr").transcribe_word("bajau") == "badʒau"


def test_bdr_prothetic_e_is_realised_as_schwa():
    """Declared limit: "Word-initial nasal or /l/ clusters are spelled with a
    prothetic ⟨e⟩ (emberen, emma', ellum) that is usually not pronounced —
    this map will realise it as /ə/"."""
    assert G2P("bdr").transcribe_word("emberen") == "əmbəɾən"


# ---------------------------------------------------------------------------
# pwn — Paiwan (2005 official romanisation, Kuljaljau dialect)
# ---------------------------------------------------------------------------

def test_pwn_tj_is_a_palatal_stop():
    """"⟨tj dj⟩ are the palatal stops /c ɟ/" (2005 official orthography,
    Kuljaljau values).  tjagaraus 'the highest heaven' → [caɡaraus]."""
    assert G2P("pwn").transcribe_word("tjagaraus") == "caɡaraus"


def test_pwn_q_is_a_uvular_stop():
    """"⟨q⟩ the uvular /q/" (ibid.).  qadaw 'sun' → [qadaw]."""
    assert G2P("pwn").transcribe_word("qadaw") == "qadaw"


def test_pwn_c_is_an_affricate():
    """"⟨c⟩ /ts~tʃ/" (ibid.).  caucau 'person' → [tsautsau]."""
    assert G2P("pwn").transcribe_word("caucau") == "tsautsau"


# ---------------------------------------------------------------------------
# tay — Atayal (2005 official romanisation)
# ---------------------------------------------------------------------------

def test_tay_b_is_a_bilabial_fricative():
    """"⟨b⟩ = /β/ (~[v])" (Council of Indigenous Peoples 2005).  balay 'true'
    → [βalaj], with ⟨y⟩ = /j/."""
    assert G2P("tay").transcribe_word("balay") == "βalaj"


def test_tay_g_is_a_velar_fricative():
    """"⟨g⟩ = /ɣ/" (ibid.).  gaga 'customary law' → [ɣaɣa], not [ɡaɡa]."""
    assert G2P("tay").transcribe_word("gaga") == "ɣaɣa"


def test_tay_h_is_a_pharyngeal_fricative():
    """"⟨h⟩ = the voiceless PHARYNGEAL fricative /ħ/ (Li 1980; realised [h] by
    some speakers)".  hozil 'dog' → [ħozil]."""
    assert G2P("tay").transcribe_word("hozil") == "ħozil"


def test_tay_q_and_x_are_distinct_dorsals():
    """"⟨x⟩ = /x/" beside the uvular ⟨q⟩ (ibid.).  qutux 'one' has both:
    [qutux]."""
    assert G2P("tay").transcribe_word("qutux") == "qutux"


def test_tay_unwritten_schwa_is_not_recoverable():
    """Declared limit: "in several dialects the schwa is simply not written,
    producing long surface consonant clusters (e.g. pspngun /pəsəpəŋun/) — such
    omitted vowels are NOT recoverable from the spelling"."""
    assert G2P("tay").transcribe_word("pspngun") == "pspŋun"


# ---------------------------------------------------------------------------
# trv — Seediq / Truku (2005 official romanisation)
# ---------------------------------------------------------------------------

def test_trv_h_is_a_pharyngeal_fricative():
    """"⟨h⟩ = the voiceless PHARYNGEAL fricative /ħ/" (Council of Indigenous
    Peoples 2005, Seediq writing system).  hakaw 'bridge' → [ħakaw]."""
    assert G2P("trv").transcribe_word("hakaw") == "ħakaw"


def test_trv_r_is_a_flap():
    """"⟨r⟩ = the alveolar flap /ɾ/" (ibid.).  rudan 'elders' → [ɾudan]."""
    assert G2P("trv").transcribe_word("rudan") == "ɾudan"


def test_trv_g_is_a_velar_stop_in_the_seediq_system():
    """"⟨g⟩ = /ɡ/ (Taroko /ɣ/)" — the Seediq table is primary, the Taroko value
    secondary.  gaya 'custom' → [ɡaja]."""
    assert G2P("trv").transcribe_word("gaya") == "ɡaja"


def test_trv_e_is_a_schwa():
    """"The vowel letter ⟨e⟩ is /ə/ in Toda and Truku but /e/ in Tgdaya"
    (ibid.).  Seediq, the language's own name, takes the schwa reading."""
    assert G2P("trv").transcribe_word("seediq") == "səədiq"


# ---------------------------------------------------------------------------
# szy — Sakizaya (official Council of Indigenous Peoples romanisation)
# ---------------------------------------------------------------------------

def test_szy_y_is_the_palatal_glide():
    """"Letters whose value departs from the IPA: ... ⟨y⟩ = /j/" (原住民族語言
    書寫系統, Sakizaya).  Sakizaya, the language's own name, ends in [ja]."""
    assert G2P("szy").transcribe_word("sakizaya") == "sakizaja"


# ---------------------------------------------------------------------------
# nqo — N'Ko (Solomana Kanté, 1949)
# ---------------------------------------------------------------------------

def test_nqo_dagbasinna_is_silent():
    """"ߑ DAGBASINNA is a silent letter marking the absence of a vowel in a
    consonant cluster and maps to the empty string."  ߛߑ = [s] alone."""
    assert G2P("nqo").transcribe_word("ߛߑ") == "s"


def test_nqo_tone_marks_become_tone_letters_not_segments():
    """"Tone and vowel length are written with seven combining marks
    (U+07EB..U+07F1): they are mapped to IPA tone letters (and ː for the long
    series) rather than to segments."  ߊ߯ (alif + the long-high mark) → [aː˥]."""
    assert G2P("nqo").transcribe_word("ߊ߯") == "aː˥"


def test_nqo_nasalisation_mark_becomes_a_tilde():
    """"U+07F2 (nasalisation) maps to a combining tilde."  ߞߊߣߊ߲ ends in a
    nasalised vowel, not in a consonant.  The tilde is the COMBINING mark
    U+0303, not a precomposed character."""
    assert G2P("nqo").transcribe_word("ߞߊߣߊ߲") == "kanã"


# ---------------------------------------------------------------------------
# peo / pal — Old and Middle Persian
# ---------------------------------------------------------------------------

def test_peo_three_stop_and_spirant_series():
    """"THREE-STOP + SPIRANT SERIES: p/b/f, t/d/θ, k/g/x" (Schmitt 2014; Kent
    1953).  xšāyaθiya 'king' (DNa) carries both the velar spirant ⟨x⟩ and the
    dental spirant ⟨θ⟩ as distinct segments."""
    assert G2P("peo").transcribe_word("xšāyaθiya") == "xʃaːjaθija"


def test_pal_xw_cluster_is_a_labialised_velar_fricative():
    """"xw- cluster preserved as /xʷ/ (later → x in New Persian)" (Mackenzie
    1971).  xwadāy 'lord' → [xʷadaːj]."""
    assert G2P("pal").transcribe_word("xwadāy") == "xʷadaːj"


# ---------------------------------------------------------------------------
# ine / iir — Proto-Indo-European and Proto-Indo-Iranian
# ---------------------------------------------------------------------------

def test_ine_breathy_voiced_series_is_distinct_from_plain_voiced():
    """"Three-way stop contrast: voiceless / voiced / breathy-voiced (the
    'voiced aspirates')" (Fortson 2010; Ringe 2006).  The literature's notation
    *bʰer- 'carry' keeps the breathy stop distinct from plain *b."""
    g = G2P("ine")
    assert g.transcribe_word("bʰer") == "bʱer"
    assert g.transcribe_word("bʰer") != g.transcribe_word("ber")


def test_ine_three_laryngeals_are_three_distinct_segments():
    """"Three laryngeals (h₁ h₂ h₃) with debated phonetic values — h₁ neutral,
    h₂ a-colouring, h₃ o-colouring" (ibid.).  The three notational symbols map
    to three different segments."""
    g = G2P("ine")
    out = {g.transcribe_word(h) for h in ("h₁", "h₂", "h₃")}
    assert len(out) == 3


def test_iir_satem_shift_gives_a_palatal_sibilant():
    """"Satem shift: PIE palatovelars *ḱ, *ĝ → PII palatal sibilants *ś, *ź."
    The reconstruction *śatam 'hundred' has a palatal sibilant, not a velar."""
    assert G2P("iir").transcribe_word("śatam") == "ɕatam"
