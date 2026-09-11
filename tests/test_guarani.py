"""Cited claims for Paraguayan Guaraní in the achegety.

The achegety writes six oral vowels and a tilde-marked nasal counterpart for
each, spells the glottal stop with an apostrophe called the puso, and treats
⟨ch mb nd ng nt rr⟩ and the tilde letters ⟨ñ g̃⟩ as single letters. The acute
accent marks lexical stress and carries no segmental value. Every claim below
is sourced in the rule or grapheme it tests, in orthography2ipa/data/gn.json.
"""
import unicodedata

import orthography2ipa as o2i


def segments(word):
    """Transcription without the stress mark."""
    return o2i.G2P("gn").transcribe_word(word).replace("ˈ", "")


def test_y_is_the_central_vowel_not_a_glide():
    g = o2i.get("gn").graphemes
    assert g["y"] == ["ɨ"]
    assert g["ỹ"] == ["ɨ̃"]
    assert segments("ky") == "kɨ"
    assert segments("yvy") == "ɨʋɨ"


def test_the_six_oral_vowels_each_have_a_tilde_nasal_counterpart():
    g = o2i.get("gn").graphemes
    for oral, nasal in (("a", "ã"), ("e", "ẽ"), ("i", "ĩ"),
                        ("o", "õ"), ("u", "ũ"), ("y", "ỹ")):
        assert g[nasal][0] == g[oral][0] + "̃" or g[nasal][0] == \
            unicodedata.normalize("NFC", g[oral][0] + "̃")
    assert segments("añẽ") != segments("añe")


def test_the_acute_accent_is_stress_only():
    g = o2i.get("gn").graphemes
    for plain, marked in (("a", "á"), ("e", "é"), ("i", "í"),
                          ("o", "ó"), ("u", "ú"), ("y", "ý")):
        assert g[marked] == g[plain]
    assert o2i.get("gn").stress.default_position == -1


def test_the_puso_is_u0027_and_is_transcribed_as_a_glottal_stop():
    """Both gold sets spell the puso with U+0027 APOSTROPHE, so that is the
    codepoint keyed; an unmapped apostrophe would delete the letter silently."""
    assert "'" in o2i.get("gn").graphemes
    assert o2i.get("gn").graphemes["'"] == ["ʔ"]
    assert segments("mba'e") == "ᵐbaʔe"
    assert segments("ha'e") == "haʔe"


def test_the_nasal_oral_contour_stops_are_single_letters():
    assert segments("mbo") == "ᵐbo"
    assert segments("nde") == "ⁿde"
    assert segments("anga") == "aᵑɡa"
    assert segments("nt") != ""


def test_the_contour_stops_carry_the_plain_nasal_as_a_second_reading():
    """The contour stops and the plain nasals are in complementary
    distribution, so each digraph offers both."""
    g = o2i.get("gn").graphemes
    assert g["mb"] == ["ᵐb", "m"]
    assert g["nd"] == ["ⁿd", "n"]
    assert g["ng"] == ["ᵑɡ", "ŋ"]


def test_g_tilde_is_the_nasal_counterpart_of_g():
    """⟨g̃⟩ is a base ⟨g⟩ plus U+0303, with no precomposed form."""
    key = "g̃"
    assert key in o2i.get("gn").graphemes
    assert o2i.get("gn").graphemes[key][0] == "ɰ̃"
    assert o2i.get("gn").graphemes["g"] == ["ɰ"]
    assert segments("hag̃ua") == "haɰ̃ua"


def test_n_tilde_ch_v_and_j_have_their_achegety_values():
    assert segments("ñe") == "ɲe"
    assert segments("che") == "ʃe"
    assert segments("ava") == "aʋa"
    assert segments("jagua") == "dʒaɰua"


def test_every_letter_of_the_achegety_is_mapped():
    """The achegety minuscule list, letter for letter. An unmapped letter is
    deleted silently rather than raising, so this is the deletion tripwire."""
    achegety = ["a", "ã", "ch", "e", "ẽ", "g", "g̃", "h", "i",
                "ĩ", "j", "k", "l", "m", "mb", "n", "nd", "ng", "nt",
                "ñ", "o", "õ", "p", "r", "rr", "s", "t", "u",
                "ũ", "v", "y", "ỹ", "'"]
    g = o2i.get("gn").graphemes
    assert [c for c in achegety if c not in g] == []


def test_b_c_and_d_are_not_letters_on_their_own():
    """They occur only inside ⟨mb ch nd⟩, so the spec keys no bare form."""
    g = o2i.get("gn").graphemes
    assert "b" not in g and "c" not in g and "d" not in g
