"""Cited-claim tests for the Indic / Indo-Iranian / South-Asian-minority specs.

Every spec in this cluster makes linguistic claims with a citation attached —
in its ``notes`` prose and in the ``notes`` of individual rules. Each test here
takes ONE such claim, quotes it, and proves it on a real word, isolating the
single segment the claim is about.

Hindi's three schwa-deletion rule families (``HI_SCHWA_FINAL_*``,
``HI_SCHWA_MEDIAL_*``, ``HI_SCHWA_KEEP_*``, 138 rules, Ohala 1983 / Ohala 1999 /
Narasimhan, Sproat & Kiraz 2004) and Malayalam's ``TA_VOICE_tɕ*`` overrides
(Asher & Kumari 1997) are already proven in ``tests/test_indic_allophony.py``
and are not repeated here; this file covers the claims that file does not.
"""
from __future__ import annotations

import pytest

from orthography2ipa.g2p import G2P


# ═══════════════════════════════════════════════════════════════════════════
# hi — Standard Hindi (Khaṛī Bolī)
# Sources declared by the spec: Ohala (1983), Pandey (2014), Masica (1991),
# Shapiro (2003).
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.xfail(strict=True, reason=(
    "hi notes: 'ड/ढ FLAPPING: retroflex stops [ɖ/ɖʱ] become flaps [ɽ/ɽʱ] "
    "intervocalically' — no such allophone rule exists; बडा (plain ⟨ड⟩ between "
    "vowels) is transcribed [bəɖaː], the stop is never flapped"
))
def test_hi_retroflex_stop_flaps_intervocalically():
    """'ड/ढ FLAPPING: retroflex stops [ɖ/ɖʱ] become flaps [ɽ/ɽʱ]
    intervocalically.' (hi notes; Ohala 1983, Masica 1991)

    ⟨बडा⟩ has plain ⟨ड⟩ between two vowels, so the claim makes it [ɽ].
    """
    assert "ɽ" in G2P("hi").transcribe_word("बडा")


@pytest.mark.xfail(strict=True, reason=(
    "hi notes: 'ड/ढ FLAPPING: retroflex stops [ɖ/ɖʱ] become flaps [ɽ/ɽʱ] "
    "intervocalically' — बुढा (plain ⟨ढ⟩ between vowels) is [bʊɖʱaː], not [bʊɽʱaː]"
))
def test_hi_breathy_retroflex_stop_flaps_intervocalically():
    """The breathy half of the same claim: intervocalic ⟨ढ⟩ [ɖʱ] → [ɽʱ].
    (hi notes; Ohala 1983, Masica 1991)
    """
    assert "ɽʱ" in G2P("hi").transcribe_word("बुढा")


def test_hi_nukta_flap_letters_are_flaps():
    """The written flaps ⟨ड़⟩/⟨ढ़⟩ — the counterpart of the flapping claim: the
    flap surfaces only where the nukta letter spells it.
    ('Nukta letters for Perso-Arabic loans…', hi notes; Ohala 1983)
    """
    g2p = G2P("hi")
    assert "ɽ" in g2p.transcribe_word("लड़का")      # laṛkā
    assert "ɽʱ" in g2p.transcribe_word("पढ़ना")     # paṛhnā
    assert "ɽ" not in g2p.transcribe_word("लडका")  # same word, plain ⟨ड⟩


def test_hi_four_way_laryngeal_contrast():
    """'4-WAY LARYNGEAL: voiceless unaspirated, voiceless aspirated, voiced,
    breathy-voiced stops.' (hi notes; Ohala 1983, Shapiro 2003)

    Velar quadruple ⟨क ख ग घ⟩ in an otherwise identical frame.
    """
    g2p = G2P("hi")
    onsets = [g2p.transcribe_word(w)[: -len("əl")] for w in ("कल", "खल", "गल", "घल")]
    assert onsets == ["k", "kʰ", "ɡ", "ɡʱ"]
    assert len(set(onsets)) == 4


def test_hi_dental_vs_retroflex_contrast():
    """'DENTALS vs RETROFLEXES: dental series (त/थ/द/ध) vs. retroflex
    (ट/ठ/ड/ढ) fully contrastive.' (hi notes; Masica 1991)
    """
    g2p = G2P("hi")
    assert g2p.transcribe_word("तल").startswith("t̪")   # dental
    assert g2p.transcribe_word("टल").startswith("ʈ")    # retroflex
    assert g2p.transcribe_word("थल").startswith("t̪ʰ")
    assert g2p.transcribe_word("ठल").startswith("ʈʰ")
    assert g2p.transcribe_word("दल").startswith("d̪")
    assert g2p.transcribe_word("डल").startswith("ɖ")


# ═══════════════════════════════════════════════════════════════════════════
# sa-x-vedic — Vedic Sanskrit (Macdonell 1910, *Vedic Grammar*)
# ═══════════════════════════════════════════════════════════════════════════

def test_sa_x_vedic_retains_the_retroflex_lateral():
    """'Includes retroflex lateral ⟨ळ⟩ /ɭ/ lost in Classical Sanskrit.'
    (sa-x-vedic notes; Macdonell 1910)

    Minimal pair against the Classical parent: the same spelling, the same
    engine, one letter's worth of difference.
    """
    assert "ɭ" in G2P("sa-x-vedic").transcribe_word("देवळ")
    assert "ɭ" not in G2P("sa").transcribe_word("देवळ")


@pytest.mark.xfail(strict=True, reason=(
    "sa-x-vedic notes: 'Retains pitch accent system (udātta/anudātta/svarita)' "
    "— the accent marks ॑ (U+0951) and ॒ (U+0952) are not graphemes; अ॒ग्नि॑ "
    "transcribes to [əɡn̪i], identical to the unaccented spelling"
))
def test_sa_x_vedic_pitch_accent_is_realised():
    """'Retains pitch accent system (udātta/anudātta/svarita).'
    (sa-x-vedic notes; Macdonell 1910, *Vedic Grammar*)

    An accented and an unaccented spelling of the same word must not
    transcribe alike if the accent is realised.
    """
    g2p = G2P("sa-x-vedic")
    assert g2p.transcribe_word("अ॒ग्नि॑") != g2p.transcribe_word("अग्नि")


# ═══════════════════════════════════════════════════════════════════════════
# kok — Konkani
# ═══════════════════════════════════════════════════════════════════════════

def test_kok_dravidian_substrate_retroflex_lateral():
    """'Strong Dravidian substrate features: retroflex ⟨ळ⟩ = [ɭ].' (kok notes)"""
    assert "ɭ" in G2P("kok").transcribe_word("खेळ")   # khell


# ═══════════════════════════════════════════════════════════════════════════
# brx — Bodo, and its reconstructed ancestor
# ═══════════════════════════════════════════════════════════════════════════

def test_brx_aspirated_and_plain_stops_both_phonemic():
    """'Aspirated and plain stops both phonemic.' (brx notes)"""
    g2p = G2P("brx")
    assert g2p.transcribe_word("pʰa") == "pʰa"
    assert g2p.transcribe_word("pa") == "pa"


@pytest.mark.xfail(strict=True, reason=(
    "brx notes: 'Written in Devanagari (official since 2003)' — the spec's "
    "script is Latin and its graphemes are romanised; Devanagari input "
    "transcribes to the empty string"
))
def test_brx_devanagari_input_is_transcribed():
    """'Written in Devanagari (official since 2003).' (brx notes)"""
    assert G2P("brx").transcribe_word("बर")


def test_proto_boro_garo_aspirated_plain_stop_contrast():
    """'Aspirated/plain stop contrast.' (brx-x-proto-boro-garo notes; Matisoff
    2003, Burling 2003, Benedict 1972)
    """
    g2p = G2P("brx-x-proto-boro-garo")
    assert g2p.transcribe_word("pʰ") == "pʰ"
    assert g2p.transcribe_word("p") == "p"


# ═══════════════════════════════════════════════════════════════════════════
# mni — Meitei/Manipuri, and Proto-Kuki-Chin
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.xfail(strict=True, reason=(
    "mni notes: 'Meitei Mayek script (traditional, restored 2013 as official)' "
    "— the spec's script is Latin; Meitei Mayek input transcribes to the empty "
    "string"
))
def test_mni_meitei_mayek_input_is_transcribed():
    """'Meitei Mayek script (traditional, restored 2013 as official).'
    (mni notes)
    """
    assert G2P("mni").transcribe_word("ꯃꯤꯇꯩ")   # ⟨mitei⟩ in Meitei Mayek


@pytest.mark.xfail(strict=True, reason=(
    "mni notes: 'Also written in Bengali script officially' — the spec's script "
    "is Latin; Bengali-script input transcribes to the empty string"
))
def test_mni_bengali_script_input_is_transcribed():
    """'Also written in Bengali script officially.' (mni notes)"""
    assert G2P("mni").transcribe_word("মৈতৈ")


def test_proto_kuki_chin_aspirated_plain_stop_contrast():
    """'Aspirated/plain stop contrast' is reconstructed for the branch.
    (mni-x-proto-kuki-chin notes; VanBik 2009, Matisoff 2003)
    """
    g2p = G2P("mni-x-proto-kuki-chin")
    assert g2p.transcribe_word("pʰ") == "pʰ"
    assert g2p.transcribe_word("p") == "p"


# ═══════════════════════════════════════════════════════════════════════════
# sat — Santali (Munda), and Proto-Munda
# ═══════════════════════════════════════════════════════════════════════════

def test_sat_phonemic_aspiration_in_stops():
    """'Phonemic aspiration in stops.' (sat notes)"""
    g2p = G2P("sat")
    assert g2p.transcribe_word("kʰa") == "kʰa"
    assert g2p.transcribe_word("ka") == "ka"


def test_sat_glottalized_vowels_in_checked_syllables():
    """'Glottalized vowels in checked syllables.' (sat notes)

    The checked ⟨aʔ⟩ carries the modifier glottal stop ⟨ˀ⟩; the plain ⟨a⟩ does
    not.
    """
    g2p = G2P("sat")
    assert g2p.transcribe_word("aʔ") == "aˀ"
    assert "ˀ" not in g2p.transcribe_word("a")


def test_sat_has_no_retroflex_consonants():
    """'No retroflex consonants (unlike IA neighbours).' (sat notes)

    A declared absence: the retroflex letters are not in the inventory, so
    they transcribe to nothing.
    """
    g2p = G2P("sat")
    assert g2p.transcribe_word("ʈ") == ""
    assert g2p.transcribe_word("ɖ") == ""
    assert g2p.transcribe_word("t") == "t"    # the dental IS there


@pytest.mark.xfail(strict=True, reason=(
    "sat notes: 'Written officially in Ol Chiki script (invented 1925 by "
    "Raghunath Murmu)' — the spec's script is Latin; Ol Chiki input transcribes "
    "to the empty string"
))
def test_sat_ol_chiki_input_is_transcribed():
    """'Written officially in Ol Chiki script (invented 1925 by Raghunath
    Murmu); also Latin and Devanagari.' (sat notes)
    """
    assert G2P("sat").transcribe_word("ᱥᱟᱱᱛᱟᱲᱤ")   # ⟨Santali⟩ in Ol Chiki


def test_proto_munda_has_no_retroflexes():
    """'No retroflexes at proto-stage.' (sat-x-proto-munda notes; Pinnow 1959,
    Anderson 2008, Donegan & Stampe 2004)
    """
    g2p = G2P("sat-x-proto-munda")
    assert g2p.transcribe_word("ʈ") == ""
    assert g2p.transcribe_word("ɖ") == ""
    assert g2p.transcribe_word("ɳ") == ""
    assert g2p.transcribe_word("t") == "t"


# ═══════════════════════════════════════════════════════════════════════════
# kha — Khasi (Mon-Khmer), and Proto-Mon-Khmer
# ═══════════════════════════════════════════════════════════════════════════

def test_kha_is_written_in_latin_script():
    """'Written in Latin script since Welsh/British missionary period (1840s).'
    (kha notes)
    """
    assert G2P("kha").transcribe_word("phi") == "pʰi"   # ⟨phi⟩ 'you'


def test_proto_mon_khmer_palatal_stops():
    """'Palatal stops *c/*ɟ.' (kha-x-proto-mon-khmer notes; Shorto 2006,
    Diffloth 2005)
    """
    g2p = G2P("kha-x-proto-mon-khmer")
    assert g2p.transcribe_word("c") == "c"
    assert g2p.transcribe_word("ɟ") == "ɟ"


def test_proto_mon_khmer_vowel_length_contrast():
    """'Rich vowels with length.' (kha-x-proto-mon-khmer notes; Shorto 2006)"""
    g2p = G2P("kha-x-proto-mon-khmer")
    assert g2p.transcribe_word("aː") == "aː"
    assert g2p.transcribe_word("a") == "a"


# ═══════════════════════════════════════════════════════════════════════════
# ii — Nuosu / Sichuan Yi (Liangshan Standard Yi, ratified 1980)
# ═══════════════════════════════════════════════════════════════════════════

def test_ii_tone_letter_t_is_high():
    """'the tone letters: -t high [˥] (55)' (ii notes)

    ⟨ꀀ⟩ U+A000 YI SYLLABLE IT — Yi-Pinyin ⟨it⟩.
    """
    assert G2P("ii").transcribe_word("ꀀ").endswith("˥")


def test_ii_tone_letter_x_is_high_rising():
    """'-x high-rising [˧˦] (34)' (ii notes)

    ⟨ꀁ⟩ U+A001 YI SYLLABLE IX — Yi-Pinyin ⟨ix⟩.
    """
    assert G2P("ii").transcribe_word("ꀁ").endswith("˧˦")


def test_ii_unmarked_tone_is_mid():
    """'unmarked mid [˧] (33)' (ii notes)

    ⟨ꀂ⟩ U+A002 YI SYLLABLE I — Yi-Pinyin ⟨i⟩, no tone letter.
    """
    assert G2P("ii").transcribe_word("ꀂ").endswith("˧")


def test_ii_tone_letter_p_is_low_falling():
    """'-p low-falling [˨˩] (21)' (ii notes)

    ⟨ꀃ⟩ U+A003 YI SYLLABLE IP — Yi-Pinyin ⟨ip⟩.
    """
    assert G2P("ii").transcribe_word("ꀃ").endswith("˨˩")


def test_ii_initials_b_p_bb_nb():
    """'43 initials (b [p], p [pʰ], bb [b], nb [ᵐb] …)' (ii notes)

    The ⟨-it⟩ rime series: ꀖ BIT, ꀸ PIT, ꁖ BBIT, ꁶ NBIT.
    """
    g2p = G2P("ii")
    assert g2p.transcribe_word("ꀖ").startswith("p")
    assert g2p.transcribe_word("ꀸ").startswith("pʰ")
    assert g2p.transcribe_word("ꁖ").startswith("b")
    assert g2p.transcribe_word("ꁶ").startswith("ᵐb")


def test_ii_buzzing_vowels_ur_and_yr():
    """'⟨ur⟩/⟨yr⟩ are the two "buzzing" (retracted, fricativised) vowels.'
    (ii notes)

    ꀱ BUR and ꀷ BYR — both carry the retracted diacritic ◌̠ that the plain
    rimes do not.
    """
    g2p = G2P("ii")
    assert "̠" in g2p.transcribe_word("ꀱ")     # ⟨bur⟩
    assert "̠" in g2p.transcribe_word("ꀷ")     # ⟨byr⟩
    assert "̠" not in g2p.transcribe_word("ꀖ")  # ⟨bit⟩, a plain rime


def test_ii_yi_pinyin_romanisation_is_not_accepted():
    """'INPUT CONTRACT: native Yi-syllabary text …; the official Yi Pinyin
    romanisation is NOT accepted as input.' (ii notes)
    """
    g2p = G2P("ii")
    assert g2p.transcribe_word("it") == ""
    assert g2p.transcribe_word("bit") == ""


@pytest.mark.xfail(strict=True, reason=(
    "ii notes: 'LEFT OUT: the syllable iteration mark ꀕ (U+A015) … has no fixed "
    "segmental value' — U+A015 is nevertheless in the syllabogram map and "
    "transcribes to [ɣu˧]"
))
def test_ii_iteration_mark_is_left_out():
    """'LEFT OUT: the syllable iteration mark ꀕ (U+A015), which reduplicates the
    preceding syllable and has no fixed segmental value.' (ii notes)

    A declared omission: the character must carry no segmental value.
    """
    assert G2P("ii").transcribe_word("ꀕ") == ""


# ═══════════════════════════════════════════════════════════════════════════
# dv — Maldivian / Dhivehi (Thaana)
# ═══════════════════════════════════════════════════════════════════════════

def test_dv_sukun_marks_the_absence_of_a_vowel():
    """'or by the sukun ް, which marks the absence of a vowel and maps to the
    empty string.' (dv notes)

    ⟨ބަސް⟩ 'word' — the final ⟨ސް⟩ is s + sukun, so no vowel follows the [s].
    """
    assert G2P("dv").transcribe_word("ބަސް") == "bas"


def test_dv_alifu_is_a_silent_null_carrier():
    """'އ ALIFU is a null carrier: it is silent when it merely bears a fili
    (word-initial vowels).' (dv notes)
    """
    assert G2P("dv").transcribe_word("އަ") == "a"


def test_dv_alifu_plus_sukun_is_a_glottal_stop():
    """'the sequence އް (alifu + sukun) marks a glottal stop / the gemination of
    the following consonant, so it is keyed as a multigraph.' (dv notes)
    """
    assert G2P("dv").transcribe_word("އް") == "ʔ"


def test_dv_naaviyani_and_gnaviyani_are_both_mapped():
    """'ޱ NAAVIYANI /ɳ/ was abolished from official orthography in 1953
    (replaced by ޏ GNAVIYANI /ɲ/) but survives in Addu and Fuvahmulah writing,
    so both are mapped.' (dv notes)
    """
    g2p = G2P("dv")
    assert g2p.transcribe_word("ޱ") == "ɳ"
    assert g2p.transcribe_word("ޏ") == "ɲ"


def test_dv_thikijehi_letters_carry_arabic_values():
    """'The thikijehi thaana ޘ..ޥ appear only in Arabic loanwords and are given
    their Arabic values.' (dv notes)

    ޘ is the Thaana counterpart of Arabic ⟨ث⟩ /θ/.
    """
    assert G2P("dv").transcribe_word("ޘ") == "θ"


# ═══════════════════════════════════════════════════════════════════════════
# ps — Pashto (Standard Afghan, Kandahari base)
# Refs: Penzl (1955), David (2014), Tegey & Robson (1996).
# ═══════════════════════════════════════════════════════════════════════════

def test_ps_retroflex_series():
    """'DEFINING FEATURES vs. Persian: (1) Retroflex consonants ʈ, ɖ, ɳ, ɻ, ʂ, ʐ
    … Modified Arabic script with extra letters for retroflexes and affricates
    (ټ ډ ڼ ړ څ ځ ښ ږ).' (ps notes; Penzl 1955, Tegey & Robson 1996)
    """
    g2p = G2P("ps")
    assert g2p.transcribe_word("ټ") == "ʈ"
    assert g2p.transcribe_word("ډ") == "ɖ"
    assert g2p.transcribe_word("ڼ") == "ɳ"
    assert g2p.transcribe_word("ړ") == "ɻ"


def test_ps_retroflex_fricatives():
    """'(5) Retroflex fricatives ʂ, ʐ in Southern dialect' — the Kandahari base
    the spec models. (ps notes; Penzl 1955)

    ⟨ښ⟩ and ⟨ږ⟩; ⟨پښتو⟩ itself has the [ʂ].
    """
    g2p = G2P("ps")
    assert g2p.transcribe_word("ښ") == "ʂ"
    assert g2p.transcribe_word("ږ") == "ʐ"
    assert "ʂ" in g2p.transcribe_word("پښتو")


def test_ps_pashto_shift_c_to_ts():
    """'(2) Pashto shift: Proto-Iranian *č → ts.' (ps notes; Penzl 1955)

    ⟨څ⟩, the letter the shift created.
    """
    assert G2P("ps").transcribe_word("څ") == "ts"


def test_ps_pashto_shift_j_to_dz():
    """'(2) Pashto shift: … *ǰ → dz.' (ps notes; Penzl 1955)

    ⟨ځ⟩, the voiced counterpart.
    """
    assert G2P("ps").transcribe_word("ځ") == "dz"


def test_ps_has_no_pharyngeals():
    """'(3) No pharyngeals (ħ ʕ absent, unlike Arabic).' (ps notes; Penzl 1955)

    A declared absence: the Arabic-loan letters ⟨ح⟩ and ⟨ع⟩ are given
    non-pharyngeal values.
    """
    g2p = G2P("ps")
    assert g2p.transcribe_word("ح") == "h"
    assert g2p.transcribe_word("ع") == "ʔ"
    assert "ħ" not in g2p.transcribe_word("حال")


# ═══════════════════════════════════════════════════════════════════════════
# ku — Northern Kurdish / Kurmanji (Hawar Latin, Bedirxan 1932)
# ═══════════════════════════════════════════════════════════════════════════

def test_ku_hawar_latin_letter_values():
    """'The mapping above is the 31-letter Hawar Latin alphabet (Celadet Alî
    Bedirxan, 1932).' (ku notes)

    ⟨pênc⟩ 'five' isolates the three Hawar-specific values: ⟨ê⟩ = [eː],
    ⟨c⟩ = [dʒ]; ⟨ş⟩ = [ʃ] in ⟨tişt⟩.
    """
    g2p = G2P("ku")
    assert g2p.transcribe_word("pênc") == "peːndʒ"
    assert g2p.transcribe_word("tişt") == "tɪʃt"


def test_ku_aspiration_is_not_written():
    """'Aspiration of /p t k/ is contrastive but unwritten.' (ku notes)

    A declared gap: because the Hawar orthography does not mark it, no
    aspiration can surface.
    """
    g2p = G2P("ku")
    for word in ("kar", "pênc", "tişt"):
        assert "ʰ" not in g2p.transcribe_word(word)


def test_ku_kurdo_arabic_script_is_not_modelled():
    """'The Kurdo-Arabic (Sorani-style) alphabet and the former Soviet Cyrillic
    alphabet are also used for Kurdish and are NOT modelled here — Hawar Latin
    input is assumed.' (ku notes)
    """
    assert G2P("ku").transcribe_word("کوردی") == ""


# ═══════════════════════════════════════════════════════════════════════════
# os — Ossetian, Iron literary standard
# ═══════════════════════════════════════════════════════════════════════════

def test_os_iron_s_is_esh():
    """'⟨с⟩ is [ʃ] … in Iron (the Digor dialect keeps the sibilant/affricate
    values).' (os notes)
    """
    assert G2P("os").transcribe_word("сӕ").startswith("ʃ")


def test_os_iron_z_is_ezh():
    """'⟨з⟩ is [ʒ] … in Iron.' (os notes)"""
    assert G2P("os").transcribe_word("зӕ").startswith("ʒ")


def test_os_iron_ts_is_s():
    """'⟨ц⟩ is [s] … in Iron.' (os notes)

    The pair ⟨сӕ⟩ / ⟨цӕ⟩ is the whole shift in one minimal pair: the letter
    that looks like [s] is [ʃ], and the letter that looks like [ts] is [s].
    """
    assert G2P("os").transcribe_word("цӕ").startswith("s")


def test_os_iron_dz_is_z():
    """'⟨дз⟩ is [z] in Iron.' (os notes)"""
    assert G2P("os").transcribe_word("дзырд").startswith("z")


def test_os_ae_is_the_open_schwa():
    """'The alphabet extends Russian Cyrillic with ⟨ӕ⟩ /ɐ/.' (os notes)"""
    assert G2P("os").transcribe_word("ӕвзаг").startswith("ɐ")


def test_os_uvular_digraphs():
    """'the uvulars ⟨хъ⟩ /q/ and ⟨гъ⟩ /ʁ/.' (os notes)"""
    g2p = G2P("os")
    assert g2p.transcribe_word("хъ") == "q"
    assert g2p.transcribe_word("гъ") == "ʁ"


def test_os_ejective_digraphs():
    """'the ejective digraphs ⟨къ пъ тъ цъ чъ⟩.' (os notes)"""
    g2p = G2P("os")
    assert g2p.transcribe_word("къ") == "kʼ"
    assert g2p.transcribe_word("пъ") == "pʼ"
    assert g2p.transcribe_word("цъ") == "tsʼ"
    assert g2p.transcribe_word("чъ") == "tʃʼ"
    assert "tʼ" in g2p.transcribe_word("стъол")


def test_os_labialised_series_written_with_following_u():
    """'the labialised series written with a following ⟨у⟩ (гу, ку, хъу, …).'
    (os notes)
    """
    g2p = G2P("os")
    assert g2p.transcribe_word("гуыр").startswith("ɡʷ")
    assert g2p.transcribe_word("куыд").startswith("kʷ")
    assert g2p.transcribe_word("хъуыддаг").startswith("qʷ")


def test_os_russian_loan_letters_are_not_mapped():
    """'Letters used only in Russian loanwords (ё, ш, щ, ъ, ь, э, ю, я) are not
    mapped.' (os notes)

    A declared omission: ⟨ш⟩ and ⟨ё⟩ contribute nothing.
    """
    g2p = G2P("os")
    assert "ʃ" not in g2p.transcribe_word("шы")
    assert g2p.transcribe_word("ёлка") == "ɫka"


@pytest.mark.xfail(strict=True, reason=(
    "os notes: 'Stress falls on the first or second syllable depending on vowel "
    "strength' — no stress is placed; ⟨ирон⟩ transcribes to [iron] with no "
    "stress mark"
))
def test_os_stress_falls_on_the_first_or_second_syllable():
    """'Stress falls on the first or second syllable depending on vowel
    strength.' (os notes)
    """
    assert "ˈ" in G2P("os").transcribe_word("ирон")


# ═══════════════════════════════════════════════════════════════════════════
# inh — Ingush (Nakh), Cyrillic since 1938. Source: Nichols.
# ═══════════════════════════════════════════════════════════════════════════

def test_inh_palochka_must_be_the_cyrillic_letter():
    """'the palochka must be U+04CF ⟨ӏ⟩ (lowercase) / U+04C0 ⟨Ӏ⟩ — Latin "I",
    "l" and the digit "1" are NOT accepted, since no consulted source documents
    them for Ingush.' (inh notes)

    With the real palochka ⟨гӏ⟩ is [ʁ]; with a Latin ⟨I⟩ or a digit ⟨1⟩ the
    digraph does not form and ⟨г⟩ is a plain [ɡ].
    """
    g2p = G2P("inh")
    assert g2p.transcribe_word("гӏалгӏай").startswith("ʁ")
    assert g2p.transcribe_word("гIалгIай").startswith("ɡ")
    assert g2p.transcribe_word("г1алг1ай").startswith("ɡ")


def test_inh_uvular_digraphs():
    """'uvular кх /q/ and къ /qʼ/.' (inh notes; Nichols)"""
    g2p = G2P("inh")
    assert g2p.transcribe_word("кх") == "q"
    assert g2p.transcribe_word("къ") == "qʼ"


def test_inh_pharyngeal_and_laryngeal():
    """'pharyngeal хь /ħ/, laryngeal хӏ /h/.' (inh notes; Nichols)"""
    g2p = G2P("inh")
    assert g2p.transcribe_word("хь") == "ħ"
    assert g2p.transcribe_word("хӏ") == "h"


def test_inh_uvular_fricative():
    """'uvular fricative гӏ /ʁ/.' (inh notes; Nichols)"""
    assert G2P("inh").transcribe_word("гӏ") == "ʁ"


def test_inh_epiglottal_stop():
    """'the epiglottal stop ӏ /ʡ/.' (inh notes; Nichols)"""
    assert G2P("inh").transcribe_word("ӏ") == "ʡ"


def test_inh_voiceless_trill_trigraph_wins_by_maximal_munch():
    """'рхӏ for the voiceless trill /r̥/; the engine matches these by maximal
    munch, so multigraphs win over their component letters.' (inh notes;
    Nichols)

    ⟨рхӏ⟩ is one segment [r̥], not [r] + [h].
    """
    assert G2P("inh").transcribe_word("рхӏ") == "r̥"


def test_inh_russian_only_letters_are_left_out():
    """'The letters щ, ы and ь occur only in Russian loanwords and are LEFT OUT:
    no source consulted gives them an Ingush IPA value.' (inh notes)

    A declared omission.
    """
    g2p = G2P("inh")
    assert g2p.transcribe_word("щ") == ""
    assert g2p.transcribe_word("ы") == ""
    assert g2p.transcribe_word("ь") == ""


def test_inh_written_diphthongs_are_mapped_as_units():
    """'The written diphthongs listed by Nichols (иэ, уо, оа, ий, эи, ои, уи,
    ов, ув) are mapped as units.' (inh notes; Nichols)
    """
    g2p = G2P("inh")
    assert g2p.transcribe_word("иэ") == "ie"
    assert g2p.transcribe_word("уо") == "uo"
    assert g2p.transcribe_word("оа") == "oɑ"


def test_inh_e_is_e_before_je():
    """'Е is given as [e] first (its value after a consonant) with [je] as the
    second candidate (word-initial / post-vocalic), since the source lists both
    without positional detail.' (inh notes)
    """
    assert G2P("inh").transcribe_word("е") == "e"


def test_inh_gemination_and_reduced_schwa_are_not_modelled():
    """'Consonant gemination and the ultra-short unstressed schwa are
    morphophonemic and not written, so they are not modelled.' (inh notes)

    A declared gap: ⟨мотт⟩ keeps two written ⟨т⟩ as a plain sequence — no
    length mark, and no epenthetic schwa.
    """
    ipa = G2P("inh").transcribe_word("мотт")
    assert "ː" not in ipa
    assert "ə" not in ipa


# ═══════════════════════════════════════════════════════════════════════════
# iir — Proto-Indo-Iranian
# ═══════════════════════════════════════════════════════════════════════════

def test_iir_a_merger():
    """'(1) The "a-merger": PIE *e, *a, *o → PII *a (three vowel qualities
    collapse to one).' (iir notes)

    The merger is in the inventory: ⟨a⟩ is a grapheme, ⟨e⟩ and ⟨o⟩ are not.
    """
    g2p = G2P("iir")
    assert g2p.transcribe_word("a") == "a"
    assert g2p.transcribe_word("e") == ""
    assert g2p.transcribe_word("o") == ""


def test_iir_satem_palatal_sibilants():
    """'(2) Satem shift: PIE palatovelars *ḱ, *ĝ → PII palatal sibilants *ś,
    *ź.' (iir notes)

    The output of the shift is written; its PIE input ⟨ḱ⟩ is not a PII
    grapheme.
    """
    g2p = G2P("iir")
    assert g2p.transcribe_word("ś") == "ɕ"
    assert g2p.transcribe_word("ź") == "ʑ"
    assert g2p.transcribe_word("ḱ") == ""


def test_iir_voiced_aspirates_preserved():
    """'(3) Voiced aspirates *bʱ, *dʱ, *gʱ preserved (distinct from Greek which
    lost aspiration, and Germanic which shifted to fricatives).' (iir notes)
    """
    g2p = G2P("iir")
    assert g2p.transcribe_word("bʱ") == "bʱ"
    assert g2p.transcribe_word("dʱ") == "dʱ"
    assert g2p.transcribe_word("gʱ") == "ɡʱ"
