"""Cited claims for the Northern Iroquoian specs (Cayuga, Oneida).

Both languages put a spelling trap in front of a reader who assumes Latin
letter values: Cayuga writes one stop phoneme with two letters (⟨d⟩ and
⟨t⟩ are both /t/), and Oneida's ⟨u⟩ is the nasal vowel /ũ/, not [u].
"""
import orthography2ipa as o2i


def test_cayuga_voiced_looking_letters_are_the_same_phoneme():
    """Wikipedia's Cayuga consonant table pairs the letters: /t/ ⟨d, t⟩,
    /k/ ⟨g, k⟩, /ts/ ⟨j, ts⟩. They are spelling variants, not a voicing
    contrast, so ⟨gayogo⟩ has no [ɡ] in it."""
    g = o2i.get("cay").graphemes
    assert g["d"] == g["t"] == ["t"]
    assert g["g"] == g["k"] == ["k"]
    assert g["j"] == g["ts"] == ["ts"]
    assert o2i.G2P("cay").transcribe_word("gayogo") == "kajoko"


def test_cayuga_palatalizes_before_front_vowels_and_before_i_j_r():
    """/ts/ → [tʃ] before a front vowel; /s/ → [ʃ] before /i/, /j/, /ɹ/."""
    cay = o2i.G2P("cay")
    assert cay.transcribe_word("tsiˀ") == "tʃiʔ"
    assert cay.transcribe_word("sirih") == "ʃiɹih"


def test_cayuga_nasal_vowel_letters_are_single_nuclei():
    """⟨ę⟩ /ɛ̃/ and ⟨ǫ⟩ /õ/ are dedicated ogonek letters — the nasal vowel
    is not spelled as a vowel+n digraph."""
    g = o2i.get("cay").graphemes
    assert g["ę"] == ["ɛ̃"] and g["ǫ"] == ["õ"]
    assert o2i.G2P("cay").transcribe_word("ǫgweˀowe") == "õkweʔowe"


def test_oneida_has_no_bilabial_consonants():
    """Wikipedia states Oneida lacks bilabial stops and labiodental
    fricatives — the absence of these letters is the language, not a
    hole in the spec."""
    g = o2i.get("one").graphemes
    for absent in ("p", "b", "f", "v", "m"):
        assert absent not in g


def test_oneida_u_is_a_nasal_vowel_not_latin_u():
    """⟨u⟩ spells /ũ/ and ⟨ʌ⟩ spells /ə̃/."""
    g = o2i.get("one").graphemes
    assert g["u"] == ["ũ"] and g["ʌ"] == ["ə̃"]
    one = o2i.G2P("one")
    assert one.transcribe_word("luwa") == "lũwa"
    assert one.transcribe_word("onʌyoteʔa") == "onə̃joteʔa"


def test_oneida_kw_is_one_labialized_segment():
    """⟨kw⟩ is /kʷ/, a single dorsal phoneme in the consonant table, not a
    k+w cluster."""
    assert o2i.get("one").graphemes["kw"] == ["kʷ"]
    assert o2i.G2P("one").transcribe_word("kwah") == "kʷah"


def test_oneida_does_not_inherit_cayuga_palatalization():
    """The palatalization rules are Cayuga's, cited from Cayuga's own
    source; Oneida keeps plain /ts/ before /i/."""
    assert o2i.G2P("one").transcribe_word("tsi") == "tsi"
