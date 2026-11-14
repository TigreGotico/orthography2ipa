"""Wiyot (`wiy`) grapheme-table regression tests.

Teeter's practical orthography (the alphabet the WikiPron wiy_latn_broad gold
is transcribed in) uses several single letters for values a naive Latin-script
reading would get wrong: b/d/g/r are approximants or flaps, not the stops or
trill an English reader expects, e is a true mid vowel rather than [ɛ], and o
is a low back vowel [ɑ]. The digraph series ph/th/kh/kwh/čh (and ch, which is
itself the aspirated affricate) mark aspiration and must win over decomposing
into the plain consonant plus a bare h. A standalone ⟨h⟩ is [h] word-initially
and [ʔ] everywhere else, so the same letter is a fricative at the front of a
word and a glottal stop inside one.

Every pair below is drawn verbatim from the upstream WikiPron gold
(CUNY-CL/wikipron, data/scrape/tsv/wiy_latn_broad.tsv) and cross-checked
against Teeter's chart as reproduced in Wikipedia's Wiyot language phonology
section (see orthography2ipa/data/wiy.json for the full provenance note).
"""
from orthography2ipa import transcribe


def test_b_lenites_to_bilabial_fricative():
    assert transcribe("bás", "wiy") == "βás"


def test_d_is_an_alveolar_flap():
    assert transcribe("balìd", "wiy") == "βalìɾ"


def test_g_is_a_velar_fricative():
    assert transcribe("toyagáhla", "wiy") == "tɑjaɣáʔla"


def test_r_is_an_alveolar_approximant():
    assert transcribe("rakhùy", "wiy") == "ɹakʰùj"


def test_e_is_a_true_mid_vowel_not_open_mid():
    out = transcribe("dihrétoruy", "wiy")
    assert out == "ɾiʔɹétɑɹuj"
    assert "ɛ" not in out


def test_o_is_a_low_back_vowel():
    out = transcribe("dihrétoruy", "wiy")
    # the orthographic 'o' surfaces as [ɑ], not [o]
    assert out.count("ɑ") == 1
    assert "o" not in out


def test_aspirated_ph_th_kh_digraphs_win_over_plain_consonant_plus_h():
    assert transcribe("khápt", "wiy") == "kʰápt"
    assert transcribe("thígadił", "wiy") == "tʰíɣaɾiɬ"
    assert transcribe("phicúhlokš", "wiy") == "pʰitsúʔlɑkʃ"


def test_kwh_and_ch_digraphs_are_aspirated():
    assert transcribe("bíkwhal", "wiy") == "βíkʷʰal"
    # ch itself is the aspirated affricate [tsʰ], not [tʃ]
    assert transcribe("bacadàk", "wiy") == "βatsaɾàk"


def test_ch_is_aspirated_tsh_not_tsh_unaspirated_or_tsh_palatal():
    out = transcribe("bacadàk", "wiy")
    assert "ts" in out
    assert "tʃ" not in out


def test_standalone_h_is_a_glottal_stop_inside_a_word():
    assert transcribe("báhlawal", "wiy") == "βáʔlawal"
    assert transcribe("bóhn", "wiy") == "βɑ́ʔn"
    assert transcribe("bíwih", "wiy") == "βíwiʔ"


def test_word_initial_h_stays_a_fricative():
    assert transcribe("hałkàn", "wiy") == "haɬkàn"
    assert transcribe("hutwùy", "wiy") == "hutwùj"
    # both values of the letter in one word: [h] at the front, [ʔ] inside
    assert transcribe("híh", "wiy") == "híʔ"
    assert transcribe("hihłòkw", "wiy") == "hiʔɬɑ̀kʷ"


def test_aspiration_digraphs_are_not_touched_by_the_positional_h():
    assert transcribe("bakhàs", "wiy") == "βakʰàs"
    assert transcribe("bíkwhal", "wiy") == "βíkʷʰal"


def test_the_apostrophe_still_spells_a_glottal_stop():
    assert transcribe("ba'", "wiy") == "βaʔ"
