"""Cited-claim tests: Dravidian, Austronesian/Papuan/other Asian, and constructed languages.

Each test isolates ONE cited claim from a spec (its ``notes`` prose or the
``notes``/``source`` field of a single rule) and proves it fires — or, where the
engine contradicts the citation, records that with a strict xfail whose
assertion still says what the citation says.

Tests assert on the AFFECTED SEGMENT, and use a minimal pair (fires / does not
fire) wherever the orthography allows one.
"""

import pytest

from orthography2ipa.g2p import G2P


# ═══════════════════════════════════════════════════════════════════════════
# Tamil (ta) — intervocalic / post-nasal voicing of the stop series
#   "Tamil has NO phonemic voicing contrast in stops: voicing is positional"
#   (Keane 2004: 111-116, Journal of the IPA 34(1); Krishnamurti 2003: 4.2;
#    Schiffman 1999: ch. 1)
# NOTE: tests/test_indic_allophony.py already asserts whole-word forms for the
# headline Tamil cases; the tests here isolate one segment per cited rule and
# add the minimal pairs and the per-consonant coverage that file does not have.
# ═══════════════════════════════════════════════════════════════════════════

def test_ta_voice_k_intervocalic():
    """TA_VOICE_k: "A single plosive between vowels ... is voiced" — மகன்
    [maɡan] (Keane 2004: 111-116; Krishnamurti 2003: 4.2)."""
    assert G2P("ta").transcribe_word("மகன்") == "maɡan"      # ⟨க⟩ → [ɡ]
    assert G2P("ta").transcribe_word("கல்").startswith("k")  # word-initial: [k]


def test_ta_voice_t_dental_intervocalic():
    """TA_VOICE_t̪: the dental stop voices between vowels — அது [ad̪u]; it stays
    voiceless word-initially — தமிழ் [t̪amiɻ] (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("அது") == "ad̪u"
    assert G2P("ta").transcribe_word("தமிழ்").startswith("t̪")


def test_ta_voice_retroflex_intervocalic():
    """TA_VOICE_ʈ: the retroflex stop voices between vowels — கடல் [kaɖal]
    (Keane 2004: 111-116; Krishnamurti 2003: 4.2)."""
    assert G2P("ta").transcribe_word("கடல்") == "kaɖal"


def test_ta_voice_p_intervocalic():
    """TA_VOICE_p: the labial stop voices between vowels — கபம் [kabam]; it stays
    voiceless word-initially — பசு [pasu] (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("கபம்") == "kabam"
    assert G2P("ta").transcribe_word("பசு").startswith("p")


def test_ta_palatal_lenites_to_s_between_vowels():
    """TA_VOICE_tɕ: "The palatal ⟨ச⟩ lenites to [s] between vowels" but is [tɕ]
    word-initially (Keane 2004: 113; Schiffman 1999)."""
    assert G2P("ta").transcribe_word("பசு") == "pasu"        # medial ⟨ச⟩ → [s]
    assert G2P("ta").transcribe_word("சொல்").startswith("tɕ")  # initial → [tɕ]


def test_ta_voice_n_k_post_nasal():
    """TA_VOICE_N_k: "a stop AFTER a nasal is voiced" — தங்கம் [t̪aŋɡam]
    (Keane 2004: 111-116; Krishnamurti 2003: 4.2)."""
    assert G2P("ta").transcribe_word("தங்கம்") == "t̪aŋɡam"


def test_ta_voice_n_t_dental_post_nasal():
    """TA_VOICE_N_t̪: post-nasal voicing of the dental — சாந்து [tɕaːnd̪u]
    (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("சாந்து") == "tɕaːnd̪u"


def test_ta_voice_n_retroflex_post_nasal():
    """TA_VOICE_N_ʈ: post-nasal voicing of the retroflex — உண்டா [uɳɖaː]
    (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("உண்டா") == "uɳɖaː"


def test_ta_voice_n_p_post_nasal():
    """TA_VOICE_N_p: post-nasal voicing of the labial — அம்பு [ambu]
    (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("அம்பு") == "ambu"


def test_ta_voice_n_palatal_voices_rather_than_lenites():
    """TA_VOICE_N_tɕ: "The palatal ⟨ச⟩ lenites to [s] between vowels but voices to
    [dʑ] after a nasal" — மஞ்சள் [maɲdʑaɭ] (Keane 2004: 113; Schiffman 1999)."""
    assert G2P("ta").transcribe_word("மஞ்சள்") == "maɲdʑaɭ"
    # same letter, intervocalic, lenites instead:
    assert "s" in G2P("ta").transcribe_word("அரசு")


def test_ta_novoice_k_after_liquid():
    """TA_NOVOICE_k: "A stop is VOICELESS ... when it follows another vowel-less
    obstruent or liquid" — கற்க [karka] (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("கற்க") == "karka"      # [rk], never *[rɡ]


def test_ta_novoice_p_after_liquid():
    """TA_NOVOICE_p: a labial stop after a liquid stays voiceless — சார்பு
    [tɕaːrpu], against intervocalic கபம் [kabam] (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("சார்பு") == "tɕaːrpu"
    assert "b" in G2P("ta").transcribe_word("கபம்")


def test_ta_novoice_p_after_obstruent():
    """TA_NOVOICE_p: a labial stop after a vowel-less obstruent stays voiceless —
    நட்பு [naʈpu] (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("நட்பு") == "naʈpu"


def test_ta_novoice_dental_after_glide():
    """TA_NOVOICE_t̪: the dental stays voiceless after a vowel-less consonant —
    செய்தல் [tɕejt̪al], வாழ்தல் [ʋaːɻt̪al] (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("செய்தல்") == "tɕejt̪al"
    assert G2P("ta").transcribe_word("வாழ்தல்") == "ʋaːɻt̪al"


# ── Tamil gemination: C + virama + C is one LONG consonant, always voiceless ──
#    (Keane 2004: 111-116; Krishnamurti 2003: ch. 4)

def test_ta_geminate_k_is_long_and_voiceless():
    """TA_GEM1_k/TA_GEM2_k: "A geminate is ALWAYS voiceless" — பக்கம் [pakːam],
    never *[paɡam] (Keane 2004: 113)."""
    assert G2P("ta").transcribe_word("பக்கம்") == "pakːam"
    assert G2P("ta").transcribe_word("மகன்") == "maɡan"   # single ⟨க⟩ voices


def test_ta_geminate_dental_is_long_and_voiceless():
    """TA_GEM1_t̪/TA_GEM2_t̪: கத்தி [kat̪ːi] — long dental, voicing blocked
    (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("கத்தி") == "kat̪ːi"
    assert G2P("ta").transcribe_word("அது") == "ad̪u"      # single ⟨த⟩ voices


def test_ta_geminate_retroflex_is_long_and_voiceless():
    """TA_GEM1_ʈ/TA_GEM2_ʈ: பாட்டி [paːʈːi] against கடல் [kaɖal]
    (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("பாட்டி") == "paːʈːi"


def test_ta_geminate_p_is_long_and_voiceless():
    """TA_GEM1_p/TA_GEM2_p: அப்பா [apːaː] — long labial, no voicing
    (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("அப்பா") == "apːaː"


def test_ta_geminate_palatal_neither_lenites_nor_voices():
    """TA_GEM1_tɕ/TA_GEM2_tɕ: the geminate rules order before the voicing rules,
    so a doubled ⟨ச⟩ is [tɕː], not the intervocalic [s] — பேச்சு [peːtɕːu]
    (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("பேச்சு") == "peːtɕːu"


def test_ta_geminate_m_is_long():
    """TA_GEM1_m/TA_GEM2_m: "the pair rewrites C+C+V to Cː+V" — அம்மா [amːaː]
    (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("அம்மா") == "amːaː"


def test_ta_geminate_n_is_long():
    """TA_GEM1_n/TA_GEM2_n: பொன்னு [ponːu] (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("பொன்னு") == "ponːu"


def test_ta_geminate_retroflex_nasal_is_long():
    """TA_GEM1_ɳ/TA_GEM2_ɳ: அண்ணா [aɳːaː] (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("அண்ணா") == "aɳːaː"


def test_ta_geminate_l_is_long():
    """TA_GEM1_l/TA_GEM2_l: பல்லி [palːi] (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("பல்லி") == "palːi"


def test_ta_geminate_retroflex_l_is_long():
    """TA_GEM1_ɭ/TA_GEM2_ɭ: வெள்ளை [ʋeɭːai] (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("வெள்ளை") == "ʋeɭːai"


def test_ta_geminate_r_is_long():
    """TA_GEM1_r/TA_GEM2_r: வெற்றி [ʋerːi] (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("வெற்றி") == "ʋerːi"


def test_ta_geminate_glide_j_is_long():
    """TA_GEM1_j/TA_GEM2_j: மெய்யாக [mejːaːɡa] (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("மெய்யாக") == "mejːaːɡa"


def test_ta_geminate_glide_v_is_long():
    """TA_GEM1_ʋ/TA_GEM2_ʋ: செவ்வாய் [tɕeʋːaːj] (Keane 2004: 111-116)."""
    assert G2P("ta").transcribe_word("செவ்வாய்") == "tɕeʋːaːj"


# ═══════════════════════════════════════════════════════════════════════════
# Proto-Dravidian (ta-x-proto-dravidian)
#   "5 vowel qualities × short/long; two stop series (initial: unaspirated;
#    medial: voiced allophones); no aspiration contrast in native vocabulary;
#    retroflex series (ʈ ɖ ɳ ɭ ɻ)" — Krishnamurti (2003)
# ═══════════════════════════════════════════════════════════════════════════

def test_proto_dravidian_retroflex_series_is_mapped():
    """"retroflex series (ʈ ɖ ɳ ɭ ɻ) — may be the source of IA retroflexes"
    (Krishnamurti 2003)."""
    g = G2P("ta-x-proto-dravidian")
    for seg in ("ʈ", "ɖ", "ɳ", "ɭ", "ɻ"):
        assert g.transcribe_word("a" + seg + "u") == "a" + seg + "u"


def test_proto_dravidian_vowel_length_contrast():
    """"5 vowel qualities × short/long" (Krishnamurti 2003): *paal keeps the long
    vowel distinct from *pal."""
    g = G2P("ta-x-proto-dravidian")
    assert g.transcribe_word("pal") == "pal"
    assert g.transcribe_word("paːl") == "paːl"


@pytest.mark.xfail(strict=True, reason="Proto-Dravidian notes claim medial stops "
                                       "have voiced allophones; the spec carries no "
                                       "allophone_rules, so *katu stays [katu]")
def test_proto_dravidian_medial_stops_are_voiced_allophones():
    """"two stop series (initial: unaspirated; medial: voiced allophones)"
    (Krishnamurti 2003) — medial *t should surface voiced."""
    assert G2P("ta-x-proto-dravidian").transcribe_word("katu") == "kadu"


# ═══════════════════════════════════════════════════════════════════════════
# Malayalam (ml) — inherits Dravidian voicing, overrides the palatal by id
#   (Asher & Kumari 1997: 405-406; Krishnamurti 2003: 4.2)
# ═══════════════════════════════════════════════════════════════════════════

def test_ml_inherits_intervocalic_voicing_of_velar():
    """"plosives are voiceless word-initially and ... voiced between vowels"
    (Asher & Kumari 1997: 405-406) — മകൻ [maɡan-]."""
    out = G2P("ml").transcribe_word("മകൻ")
    assert "ɡ" in out and out.startswith("m")


def test_ml_inherits_intervocalic_voicing_of_dental():
    """മരുതം [marud̪am] — the medial dental voices (Asher & Kumari 1997: 405-406)."""
    assert "d̪" in G2P("ml").transcribe_word("മരുതം")


def test_ml_palatal_voices_to_dz_not_s():
    """TA_VOICE_tɕ (ml override): "It differs from Tamil in ONE realisation: the
    palatal ⟨ച⟩ does not lenite to [s] between vowels, it voices to [dʑ]"
    (Asher & Kumari 1997: 405-406)."""
    out = G2P("ml").transcribe_word("വചനം")
    assert "dʑ" in out and "s" not in out
    assert "s" in G2P("ta").transcribe_word("அரசு")   # Tamil lenites instead


def test_ml_geminate_stays_voiceless():
    """The inherited geminate rules keep a doubled stop long and voiceless —
    ചട്ട [tɕaʈːa] (Keane 2004: 111-116, inherited via ta)."""
    assert G2P("ml").transcribe_word("ചട്ട") == "tɕaʈːa"


# ═══════════════════════════════════════════════════════════════════════════
# Korean (ko)
#   "Lax stops/affricate are voiced between voiced sounds ... Tense (k͈ t͈ p͈ t͈ɕ)
#    and aspirated series never voice." Sohn (1999) §6.3; Shin, Kiaer & Cha (2012) ch. 4
# ═══════════════════════════════════════════════════════════════════════════

def test_ko_lax_k_voices_between_voiced_sounds():
    """KO_LAX_VOICING_K: 한국 [hanɡuk̚] — lax ㄱ voices after a sonorant; it is
    voiceless word-initially, 기다 [kida] (Sohn 1999 §6.3)."""
    assert "nɡ" in G2P("ko").transcribe_word("한국")
    assert G2P("ko").transcribe_word("기다").startswith("k")


def test_ko_lax_t_voices_between_vowels():
    """KO_LAX_VOICING_T: 바다 [pada] — lax ㄷ voices intervocalically, while the
    word-initial lax ㅂ stays voiceless (Sohn 1999 §6.3)."""
    assert G2P("ko").transcribe_word("바다") == "pada"


def test_ko_lax_p_voices_between_vowels():
    """KO_LAX_VOICING_P: 부부 [pubu] — the same lax ㅂ is [p] initially and [b]
    between vowels (Sohn 1999 §6.3; Shin, Kiaer & Cha 2012 ch. 4)."""
    assert G2P("ko").transcribe_word("부부") == "pubu"


def test_ko_lax_affricate_voices_between_voiced_sounds():
    """KO_LAX_VOICING_Tɕ: 아버지 [abʌdʑi] — lax ㅈ voices intervocalically, while
    initial ㅈ is voiceless, 자다 [tɕada] (Sohn 1999 §6.3)."""
    assert "dʑ" in G2P("ko").transcribe_word("아버지")
    assert G2P("ko").transcribe_word("자다").startswith("tɕ")


def test_ko_tense_and_aspirated_series_never_voice():
    """"Tense (k͈ t͈ p͈ t͈ɕ) and aspirated series never voice" (Sohn 1999 §6.3):
    까치 [k͈atɕʰi] keeps the intervocalic aspirate."""
    assert G2P("ko").transcribe_word("까치") == "k͈atɕʰi"
    assert G2P("ko").transcribe_word("타다").startswith("tʰ")


def test_ko_coda_neutralization():
    """"only k̚ n t̚ l m p̚ ŋ surface in coda" (Sohn 1999 §6.2): 낮 → [nat̚],
    꽃 → [k͈ot̚], 앞 → [ap̚]."""
    g = G2P("ko")
    assert g.transcribe_word("낮") == "nat̚"
    assert g.transcribe_word("꽃") == "k͈ot̚"
    assert g.transcribe_word("앞") == "ap̚"


def test_ko_cluster_coda_keeps_pre_pause_survivor():
    """"cluster codas keep the pre-pause survivor" (ko notes; Sohn 1999 §6.2):
    닭 → [tak̚], 값 → [kap̚]."""
    g = G2P("ko")
    assert g.transcribe_word("닭") == "tak̚"
    assert g.transcribe_word("값") == "kap̚"


def test_ko_declared_gap_liaison_not_modelled():
    """Declared omission: "Cross-boundary phenomena (liaison/resyllabification
    국어→[구거] ...) are NOT yet modelled — transcriptions are per-syllable citation
    forms." Pinned as written: 국어 stays [kuk̚ʌ], not [kuɡʌ]."""
    assert G2P("ko").transcribe_word("국어") == "kuk̚ʌ"


def test_ko_declared_gap_nasalisation_not_modelled():
    """Declared omission: nasalisation is NOT yet modelled — 국물 stays [kuk̚muɭ],
    not the sandhi form [kuŋmul] (ko notes)."""
    assert G2P("ko").transcribe_word("국물").startswith("kuk̚m")


def test_ko_declared_gap_lateralisation_not_modelled():
    """Declared omission: lateralisation is NOT yet modelled — 신라 stays [sinɾa],
    not [silla] (ko notes)."""
    assert G2P("ko").transcribe_word("신라") == "sinɾa"


# ═══════════════════════════════════════════════════════════════════════════
# Austronesian: Formosan + Malayo-Polynesian
# ═══════════════════════════════════════════════════════════════════════════

# ── Sakizaya (szy), official Council of Indigenous Peoples romanisation ──

def test_szy_l_is_the_alveolar_flap():
    """"⟨l⟩ = the alveolar flap /ɾ/" (szy notes, official 2005/2017 orthography):
    lalan → [ɾaɾan]."""
    assert G2P("szy").transcribe_word("lalan") == "ɾaɾan"


def test_szy_h_is_pharyngeal_and_c_is_ts():
    """"⟨c⟩ = /ts/ ... ⟨h⟩ = the voiceless pharyngeal fricative /ħ/" (szy notes)."""
    assert G2P("szy").transcribe_word("hani").startswith("ħ")
    assert G2P("szy").transcribe_word("cacay") == "tsatsaj"


def test_szy_e_is_central_schwa():
    """"⟨e⟩ = the central /ə/" (szy notes): malebut → [maɾəbut]."""
    assert G2P("szy").transcribe_word("malebut") == "maɾəbut"


@pytest.mark.xfail(strict=True, reason="szy notes claim /ts s z/ palatalise to "
                                       "[tɕ ɕ ʑ] before /i/, but the spec has no "
                                       "allophone_rules: cimel → tsiməɾ, sipi → sipi")
def test_szy_sibilants_palatalise_before_i():
    """"/ts s z/ palatalise to [tɕ ɕ ʑ] before /i/ and /j/ (allophones)" (szy notes)."""
    assert G2P("szy").transcribe_word("cimel").startswith("tɕ")
    assert G2P("szy").transcribe_word("sipi").startswith("ɕ")


# ── Atayal (tay), 原住民族語言書寫系統 (2005) ──

def test_tay_b_is_bilabial_fricative():
    """"⟨b⟩ = /β/ (~[v])" (tay notes, official 2005 writing system): balay → [βalaj]."""
    assert G2P("tay").transcribe_word("balay").startswith("β")


def test_tay_g_is_velar_fricative():
    """"⟨g⟩ = /ɣ/" (tay notes): gaga → [ɣaɣa]."""
    assert G2P("tay").transcribe_word("gaga") == "ɣaɣa"


def test_tay_h_is_pharyngeal():
    """"⟨h⟩ = the voiceless PHARYNGEAL fricative /ħ/ (Li 1980)": hongu → [ħoŋu],
    which also shows ⟨ng⟩ = /ŋ/."""
    assert G2P("tay").transcribe_word("hongu") == "ħoŋu"


def test_tay_x_is_velar_fricative_distinct_from_h():
    """"⟨x⟩ = /x/" and is distinct from ⟨h⟩ = /ħ/ (tay notes)."""
    assert G2P("tay").transcribe_word("xal").startswith("x")


@pytest.mark.xfail(strict=True, reason="tay notes claim /s/ and /ts/ palatalise to "
                                       "[ɕ tɕ] before /i/ and /j/, but the spec has "
                                       "no allophone_rules: cyux → tsjux, siliq → siliq")
def test_tay_sibilants_palatalise_before_i_and_j():
    """"/s/ and /ts/ are palatalised to [ɕ tɕ] before /i/ and /j/ (allophones)"
    (tay notes)."""
    assert G2P("tay").transcribe_word("cyux").startswith("tɕ")
    assert G2P("tay").transcribe_word("siliq").startswith("ɕ")


# ── Seediq / Truku (trv) ──

def test_trv_c_is_ts_and_r_is_a_flap():
    """"⟨c⟩ = /ts/ ... ⟨r⟩ = the alveolar flap /ɾ/" (trv notes, 2005 official
    Seediq writing system)."""
    assert G2P("trv").transcribe_word("cyaqung").startswith("ts")
    assert G2P("trv").transcribe_word("rudan") == "ɾudan"


def test_trv_h_is_pharyngeal_and_g_is_a_stop():
    """"⟨g⟩ = /ɡ/ (Taroko /ɣ/) ... ⟨h⟩ = the voiceless PHARYNGEAL fricative /ħ/"
    (trv notes) — the primary reading is the Seediq one."""
    assert G2P("trv").transcribe_word("hiya") == "ħija"
    assert G2P("trv").transcribe_word("gaya").startswith("ɡ")


def test_trv_e_is_schwa():
    """"The vowel letter ⟨e⟩ is /ə/ in Toda and Truku" (trv notes): ge → [ɡə]."""
    assert G2P("trv").transcribe_word("ge") == "ɡə"


# ── Paiwan (pwn), official 2005 orthography, Kuljaljau values ──

def test_pwn_tj_and_dj_are_palatal_stops():
    """"⟨tj dj⟩ are the palatal stops /c ɟ/" (pwn notes): qatja → [qaca]."""
    assert G2P("pwn").transcribe_word("qatja") == "qaca"


def test_pwn_lj_is_palatal_lateral():
    """"⟨lj⟩ the palatal lateral /ʎ/" (pwn notes): ljaljak → [ʎaʎak]."""
    assert G2P("pwn").transcribe_word("ljaljak") == "ʎaʎak"


def test_pwn_dr_is_retroflex():
    """"⟨dr⟩ the retroflex /ɖ/" (pwn notes): drusa → [ɖusa]."""
    assert G2P("pwn").transcribe_word("drusa").startswith("ɖ")


def test_pwn_q_is_uvular_and_e_is_schwa():
    """"⟨q⟩ the uvular /q/ ... Four vowels /a ə i u/" (pwn notes):
    tjaucikel → [cautsikəl]."""
    assert G2P("pwn").transcribe_word("qatja").startswith("q")
    assert "ə" in G2P("pwn").transcribe_word("tjaucikel")


# ── Acehnese (ace) ──

def test_ace_eu_is_close_back_unrounded_and_e_is_schwa():
    """"Ten oral vowel qualities" in the 1980 Latin standard (ace notes):
    ⟨eu⟩ = /ɯ/, ⟨e⟩ = /ə/, ⟨o⟩ = /ɔ/ — beungoh → [bɯŋɔh]."""
    assert G2P("ace").transcribe_word("beungoh") == "bɯŋɔh"


@pytest.mark.xfail(strict=True, reason="ace notes claim word-final ⟨k⟩ is a glottal "
                                       "stop, but the spec has no positional rule: "
                                       "manok → manɔk, not manɔʔ")
def test_ace_word_final_k_is_a_glottal_stop():
    """"Word-final ⟨k⟩ is realised as a glottal stop" (ace notes)."""
    assert G2P("ace").transcribe_word("manok") == "manɔʔ"


# ── Malay (ms) and Indonesian (id) ──

def test_id_default_stress_is_penultimate():
    """"Indonesian default stress is penultimate (-2)." Lapoliwa (1981),
    Sneddon (2003): bahasa → [baˈhasa]."""
    assert G2P("id").transcribe_word("bahasa") == "baˈhasa"


def test_ms_default_stress_is_penultimate():
    """"Malay default stress is penultimate (-2)." Clynes & Deterding (2011);
    Adelaar & Himmelmann (2005): makan → [ˈmakan]."""
    assert G2P("ms").transcribe_word("makan") == "ˈmakan"


# ── Konkani (kok) ──

def test_kok_retroflex_lateral():
    """"Strong Dravidian substrate features: retroflex ⟨ळ⟩ = [ɭ]" (kok notes)."""
    assert G2P("kok").transcribe_word("ळ").startswith("ɭ")


# ═══════════════════════════════════════════════════════════════════════════
# Zhuang (za) — 1982 official Latin orthography
# ═══════════════════════════════════════════════════════════════════════════

def test_za_final_letters_are_tone_letters_not_consonants():
    """"word-final ⟨z j x q⟩ are TONE letters, not consonants — ⟨z⟩ = ˧˩ (31),
    ⟨j⟩ = ˥ (55), ⟨x⟩ = ˦˨ (42), ⟨q⟩ = ˧˥ (35)" (za notes, 1982 orthography)."""
    g = G2P("za")
    assert g.transcribe_word("miz").endswith("˧˩")
    assert g.transcribe_word("ndaej").endswith("˥")
    assert g.transcribe_word("gvaq").endswith("˧˥")


def test_za_bare_syllable_carries_no_tone_letter():
    """"an unmarked (bare) syllable is tone ˨˦ (24), which no letter spells, so it
    is not in the map" (za notes) — bak has no tone digit at all."""
    out = G2P("za").transcribe_word("bak")
    assert out == "paːk"


def test_za_plain_letters_b_d_g_are_voiceless_stops():
    """"⟨b d g⟩ are the plain voiceless onsets /p t k/" (za notes): bak → [paːk]."""
    assert G2P("za").transcribe_word("bak").startswith("p")


def test_za_mb_nd_are_implosives():
    """"⟨mb nd⟩ are the implosives /ɓ ɗ/" (za notes): mbwn → [ɓɯn]."""
    assert G2P("za").transcribe_word("mbwn").startswith("ɓ")
    assert G2P("za").transcribe_word("ndaej").startswith("ɗ")


def test_za_w_is_a_vowel_and_r_s_c_v_are_reassigned():
    """"⟨r⟩ = /ɣ/, ⟨s⟩ = /θ/, ⟨c⟩ = /ɕ/, ⟨v⟩ = /w/, ⟨w⟩ = the VOWEL /ɯ/" (za notes)."""
    g = G2P("za")
    assert g.transcribe_word("mbwn") == "ɓɯn"          # ⟨w⟩ = vowel /ɯ/
    assert g.transcribe_word("ranz").startswith("ɣ")   # ⟨r⟩ = /ɣ/
    assert g.transcribe_word("saw").startswith("θ")    # ⟨s⟩ = /θ/
    assert g.transcribe_word("cuengh").startswith("ɕ")  # ⟨c⟩ = /ɕ/
    assert g.transcribe_word("vahcuengh").startswith("w")  # ⟨v⟩ = /w/


def test_za_h_is_a_tone_letter_word_finally_but_a_consonant_in_onset():
    """"⟨h⟩ is ambiguous: it is the consonant /h/ in onset but the tone letter ˧ (33)
    word-finally, handled by a positional_graphemes override" (za notes)."""
    g = G2P("za")
    assert g.transcribe_word("cuengh").endswith("˧")      # final ⟨h⟩ = tone 33
    assert g.transcribe_word("hoz").startswith("h")        # onset ⟨h⟩ = /h/


def test_za_declared_gap_non_final_h_in_a_compound():
    """Declared limitation: "in a written compound (e.g. Vahcuengh) an ⟨h⟩ that
    closes a NON-final syllable is still a tone letter but is only resolvable
    word-finally by this spec, so it surfaces as /h/ there" (za notes)."""
    assert G2P("za").transcribe_word("vahcuengh") == "waːhɕueŋ˧"


def test_za_vowel_length_from_a_versus_ae():
    """"⟨a⟩ = long /aː/ vs ⟨ae⟩ = short /a/" (za notes): bak → [paːk]."""
    assert "aː" in G2P("za").transcribe_word("bak")
    assert "aː" not in G2P("za").transcribe_word("haemq")


# ═══════════════════════════════════════════════════════════════════════════
# Nuosu / Sichuan Yi (ii) — Modern Yi syllabary
# ═══════════════════════════════════════════════════════════════════════════

def test_ii_syllabogram_carries_initial_rime_and_tone():
    """"The script is a SYLLABARY: one glyph = one full syllable (initial + rime +
    tone)" with "-t high [˥] (55), -x high-rising [˧˦] (34), unmarked mid [˧] (33),
    -p low-falling [˨˩] (21)" (ii notes; Liangshan Standard Yi 1980)."""
    g = G2P("ii")
    assert g.transcribe_word("ꉬ").endswith("˧")     # unmarked → mid 33
    assert g.transcribe_word("ꀋ").endswith("˨˩")    # -p → low-falling 21
    assert g.transcribe_word("ꆇ").endswith("˧˦")    # -x → high-rising 34


def test_ii_two_glyph_word_yields_two_toned_syllables():
    """One glyph = one full syllable (ii notes): ꆇꉙ (Nuosu 'Yi language') gives two
    syllables, each with its own tone."""
    out = G2P("ii").transcribe_word("ꆇꉙ")
    assert out == "nɔ˧˦ho˨˩"


# ═══════════════════════════════════════════════════════════════════════════
# Constructed languages
# ═══════════════════════════════════════════════════════════════════════════

# ── Toki Pona (tok) ──

def test_tok_stress_is_always_word_initial():
    """"Stress is always on the first syllable of a word" — "Fixed word-initial
    stress (Lang 2014)"."""
    g = G2P("tok")
    assert g.transcribe_word("toki") == "ˈtoki"
    assert g.transcribe_word("lipu") == "ˈlipu"


# ── Esperanto (eo) ──

def test_eo_stress_is_penultimate():
    """"Esperanto has perfectly regular penultimate stress ... part of the
    Fundamento de Esperanto (Zamenhof 1905). No exceptions exist in native
    vocabulary." Wells (1989)."""
    g = G2P("eo")
    assert g.transcribe_word("amiko") == "aˈmiko"
    assert g.transcribe_word("esperanto") == "espeˈranto"


# ── Ido (io) ──

def test_io_stress_is_penultimate():
    """"Penultimate stress; verb infinitives in -ar/-ir/-or take final stress
    (Kompleta Gramatiko, de Beaufront 1925)": libro → [ˈlibɾo]."""
    assert G2P("io").transcribe_word("libro") == "ˈlibɾo"


def test_io_verb_infinitives_take_final_stress():
    """Same claim, other half: the infinitive amar is stressed finally [aˈmaɾ], the
    non-infinitive libro penultimately (de Beaufront 1925)."""
    g = G2P("io")
    assert g.transcribe_word("amar") == "aˈmaɾ"
    assert g.transcribe_word("vidir") == "viˈdiɾ"


# ── Interlingue (ie) ──

def test_ie_c_and_g_soften_before_front_vowels():
    """"⟨c⟩ = [ts] before e/i/y and [k] elsewhere; ⟨g⟩ = [ʒ] before e/i/y and [ɡ]
    elsewhere" (ie notes; de Wahl 1922/1949)."""
    g = G2P("ie")
    assert g.transcribe_word("ci") == "ˈtsi"
    assert g.transcribe_word("ge") == "ˈʒe"
    assert g.transcribe_word("fisic").endswith("k")   # ⟨c⟩ elsewhere = [k]


def test_ie_intervocalic_s_is_voiced():
    """"intervocalic ⟨s⟩ = [z]" (ie notes): rosa → [ˈroza]."""
    assert G2P("ie").transcribe_word("rosa") == "ˈroza"


def test_ie_z_is_dz_and_ch_is_esh():
    """"⟨ch⟩ = [ʃ], ⟨j⟩ = [ʒ], ⟨z⟩ = [dz], ⟨y⟩ = [j] as a consonant" (ie notes)."""
    g = G2P("ie")
    assert g.transcribe_word("zon").lstrip("ˈ").startswith("dz")
    assert g.transcribe_word("chef").lstrip("ˈ").startswith("ʃ")
    assert g.transcribe_word("yun").lstrip("ˈ").startswith("j")


@pytest.mark.xfail(strict=True, reason="ie notes claim -bil is ignored for stress; "
                                       "engine stresses the i of -bil: possibil → "
                                       "poˈssibil, not ˈpossibil")
def test_ie_ending_bil_is_ignored_for_stress():
    """"Stress falls on the vowel before the final consonant; the endings -bil, -ic,
    -im, -ul, -um are ignored for stress" (ie notes)."""
    assert G2P("ie").transcribe_word("possibil") == "ˈpossibil"


@pytest.mark.xfail(strict=True, reason="ie notes claim -ic is ignored for stress; "
                                       "engine gives akaˈdemik, not aˈkademik")
def test_ie_ending_ic_is_ignored_for_stress():
    """Same claim as -bil: "the endings -bil, -ic, -im, -ul, -um are ignored for
    stress" (ie notes) — academic → [aˈkademik]."""
    assert G2P("ie").transcribe_word("academic") == "aˈkademik"


# ── Interlingua (ia) ──

def test_ia_c_is_ts_before_front_vowels_and_k_elsewhere():
    """"⟨c⟩ = /k/, but /ts/ before e, i, y" (ia notes; Gode & Blair 1951)."""
    g = G2P("ia")
    assert g.transcribe_word("cine").startswith("ts")
    assert g.transcribe_word("casa").startswith("k")


def test_ia_intervocalic_s_is_voiced_and_ch_is_esh():
    """"⟨ch⟩ = /ʃ/ in French-derived words ... ⟨s⟩ is often voiced [z] between
    vowels" (ia notes): machina → [maʃina], casa → [kaza]."""
    g = G2P("ia")
    assert g.transcribe_word("machina") == "maʃina"
    assert g.transcribe_word("casa") == "kaza"


@pytest.mark.xfail(strict=True, reason="ia notes claim ⟨qu⟩ = /k/ in que/qui; engine "
                                       "gives kwe / kwi")
def test_ia_qu_is_bare_k_in_que_and_qui():
    """"⟨qu⟩ = /kw/ (but /k/ in que, qui)" (ia notes; Gode & Blair 1951)."""
    g = G2P("ia")
    assert g.transcribe_word("que") == "ke"
    assert g.transcribe_word("qui") == "ki"


# ── Lingua Franca Nova (lfn) ──

def test_lfn_c_is_always_k_and_x_is_esh_and_j_is_ezh():
    """"⟨c⟩ is always [k], ⟨x⟩ is [ʃ], ⟨j⟩ is [ʒ]" (lfn notes; Boeree 1998)."""
    g = G2P("lfn")
    assert g.transcribe_word("casa") == "ˈkasa"
    assert g.transcribe_word("xef") == "ˈʃef"
    assert g.transcribe_word("jena") == "ˈʒena"


def test_lfn_stress_falls_before_the_last_consonant():
    """"Stress falls on the vowel or diphthong before the last consonant"
    (lfn notes): elefen → [eˈlefen]."""
    assert G2P("lfn").transcribe_word("elefen") == "eˈlefen"


@pytest.mark.xfail(strict=True, reason="lfn notes claim ⟨n⟩ is [ŋ] before a velar; "
                                       "engine gives ˈtanɡo / ˈbanka")
def test_lfn_n_is_velar_before_a_velar():
    """"⟨n⟩ is [ŋ] before a velar" (lfn notes)."""
    assert "ŋ" in G2P("lfn").transcribe_word("tango")


@pytest.mark.xfail(strict=True, reason="lfn notes claim ⟨i⟩/⟨u⟩ are [j]/[w] before "
                                       "another vowel; engine keeps the vowel: lia → ˈlia")
def test_lfn_i_is_a_glide_before_another_vowel():
    """"⟨i⟩ and ⟨u⟩ are [j]/[w] before another vowel" (lfn notes)."""
    assert "j" in G2P("lfn").transcribe_word("lia")


# ── Novial (nov) ──

def test_nov_j_ch_sh_z_x_values():
    """"⟨j⟩ = /dʒ/ (or /ʒ/) ... ⟨ch⟩ = /tʃ/, ⟨sh⟩ = /ʃ/, ⟨z⟩ = /ts/ ... ⟨x⟩ = the
    cluster /ks/" (nov notes; Jespersen 1928)."""
    g = G2P("nov")
    assert g.transcribe_word("jorne").startswith("dʒ")
    assert g.transcribe_word("chef").startswith("tʃ")
    assert g.transcribe_word("shef").startswith("ʃ")
    assert g.transcribe_word("zelo").startswith("ts")
    assert g.transcribe_word("xis").startswith("ks")


@pytest.mark.xfail(strict=True, reason="nov notes claim ⟨c⟩ = /s/ before front "
                                       "vowels; engine gives [k] everywhere: cite → kite")
def test_nov_c_is_s_before_front_vowels():
    """"⟨c⟩ is /k/ except before front vowels, where it is /s/" (nov notes)."""
    g = G2P("nov")
    assert g.transcribe_word("cite").startswith("s")
    assert g.transcribe_word("casu").startswith("k")


# ── Lojban (jbo) ──

def test_jbo_apostrophe_is_an_intervocalic_h():
    """"The apostrophe ⟨'⟩ is a voiceless glide /h/ occurring only between vowels"
    (jbo notes; Logical Language Group 1997 baseline)."""
    assert G2P("jbo").transcribe_word("ba'a") == "baha"


def test_jbo_y_is_the_schwa():
    """"⟨y⟩ is the schwa /ə/ used as a buffer/hesitation vowel" (jbo notes)."""
    assert G2P("jbo").transcribe_word("cy") == "ʃə"


@pytest.mark.xfail(strict=True, reason="jbo notes claim penultimate stress; the spec "
                                       "has no stress block, so no stress mark is "
                                       "emitted: mlatu → mlatu")
def test_jbo_stress_is_penultimate():
    """"Stress falls on the penultimate syllable of Lojban words" (jbo notes)."""
    assert G2P("jbo").transcribe_word("mlatu") == "ˈmlatu"


# ── Kotava (avk) ──

def test_avk_c_j_x_y_values():
    """"⟨c⟩ = /ʃ/, ⟨j⟩ = /ʒ/, ⟨x⟩ = /x/, ⟨y⟩ = /j/" (avk notes; Staren Fetcey 1978)."""
    g = G2P("avk")
    assert g.transcribe_word("cuvel").startswith("ʃ")
    assert g.transcribe_word("jontik").startswith("ʒ")
    assert g.transcribe_word("xanto").startswith("x")
    assert g.transcribe_word("yolt").startswith("j")


@pytest.mark.xfail(strict=True, reason="avk notes claim final stress on "
                                       "consonant-final words and penultimate on "
                                       "vowel-final ones; no stress mark is emitted")
def test_avk_stress_depends_on_the_final_segment():
    """"Stress falls on the final syllable when the word ends in a consonant and on
    the penultimate when it ends in a vowel" (avk notes)."""
    assert "ˈ" in G2P("avk").transcribe_word("kotava")


# ── Volapük (vo) ──

def test_vo_c_j_z_x_values():
    """"⟨c⟩ = /tʃ/, ⟨j⟩ = /ʃ/, ⟨z⟩ = /ts/, ⟨x⟩ = the cluster /ks/, ⟨y⟩ = /j/"
    (vo notes; Volapük nulik, de Jong 1931)."""
    g = G2P("vo")
    assert g.transcribe_word("cil").startswith("tʃ")
    assert g.transcribe_word("jul").startswith("ʃ")
    assert g.transcribe_word("zif").startswith("ts")
    assert g.transcribe_word("xamon").startswith("ks")


def test_vo_u_umlaut_is_front_rounded():
    """"Phonemic one-letter-one-sound orthography over the 27-letter alphabet"
    (vo notes): ⟨ü⟩ = /y/, ⟨ö⟩ = /ø/ — löfön → [løføn]."""
    assert G2P("vo").transcribe_word("löfön") == "løføn"


@pytest.mark.xfail(strict=True, reason="vo notes claim stress is always on the final "
                                       "vowel of a polysyllable; no stress mark is "
                                       "emitted: volapük → volapyk")
def test_vo_stress_is_on_the_final_vowel():
    """"Stress is always on the final vowel of a polysyllabic word" (vo notes)."""
    assert "ˈ" in G2P("vo").transcribe_word("volapük")
