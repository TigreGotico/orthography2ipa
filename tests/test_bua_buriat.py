"""Cited-rule conformance for Buriat (bua) in Cyrillic script.

Every claim below is stated by Skribnik (2003), "Buryat", in Janhunen (ed.)
*The Mongolic Languages*, pp. 102-108 — the spec's primary source.

The wikipron ``bua_cyrl_broad`` gold is a narrow Wiktionary transcription
whose notation differs from both this spec and the independent NorthEuraLex
gold (see the spec's notes for the counts). The tests below state the
phonology, never either gold's notation.
"""
import pytest

from orthography2ipa.g2p import G2P


def _t(word):
    return G2P("bua").transcribe_word(word).replace("ˈ", "")


# --- the three extra letters of the Buriat alphabet -----------------------
# "Since 1939, the Buryat literary language has employed a Cyrillic
# orthography with three extra letters (for h ö ü)." (Skribnik 2003:105)

@pytest.mark.parametrize("letter,ipa", [
    ("ү", "y"),   # ү — the high front rounded vowel of Skribnik's table 5.1
    ("ө", "o"),   # ө
    ("һ", "h"),   # һ — the reflex of prevocalic *s, not Mongol proper's /s/
])
def test_the_three_extra_letters(letter, ipa):
    assert G2P("bua").spec.graphemes[letter][0] == ipa


def test_h_is_not_mongol_proper_s():
    """"the weakening (desibilization) of the sibilant *s > h before vowels
    other than *i" is the isogloss that separates Buriat from Mongol proper,
    so a table copied from ⟨mn⟩ would read ⟨һ⟩ as /s/ or not at all."""
    assert _t("һахал").startswith("h")  # һахал 'beard'


# --- long vowels are written as doubled letters ---------------------------
# Skribnik (2003:105) gives ээ [ɛː], оо [ɔː], өө [oː].

@pytest.mark.parametrize("word,expected", [
    ("хэлэн", "xɛlɛŋ"),        # хэлэн 'tongue'
    ("хөөхэн", "xoːxɛŋ"),  # хөөхэн
])
def test_doubled_vowel_letters_and_qualities(word, expected):
    assert _t(word) == expected


def test_oo_umlaut_is_not_front_rounded():
    """⟨өө⟩ is Skribnik's [oː]; front-rounded [øː] is Kalmyk's value, and a
    Mongolic spec that carries a sibling's vowel chart gets it from there."""
    assert G2P("bua").spec.graphemes["өө"][0] == "oː"


# --- the palatalized consonant series is phonemic -------------------------
# "All categories of consonants, with the exception of the glides, are
# characterized by an opposition between unpalatalized (plain) and
# palatalized segments." (Skribnik 2003:105-106, table 5.2)

def test_soft_sign_writes_palatalization_not_silence():
    """⟨ь⟩ is not a silent sign in Buriat: it spells the palatalized member
    of a phonemic opposition, so mapping it to nothing deletes a segment."""
    assert G2P("bua").spec.graphemes["ь"] == ["ʲ"]


def test_palatalized_lateral_survives_the_soft_sign():
    assert "lʲ" in _t("альган")  # альган 'palm'


# --- iotated letters agree with the plain vowel they are built on ---------

def test_yo_is_j_plus_the_value_of_o():
    """⟨ё⟩ is /j/ plus ⟨о⟩, and this spec reads ⟨о⟩ as [ɔ]; [jo] would leave
    the two letters disagreeing about the same vowel."""
    g = G2P("bua").spec.graphemes
    assert g["ё"][0] == "j" + g["о"][0]


def test_hoyor_keeps_one_vowel_quality():
    assert _t("хоёр") == "xɔjɔr"  # хоёр 'two'


# --- word-final ⟨н⟩ ------------------------------------------------------
# *ng "has almost completely lost its distinctive status, merging with *n in
# most positions ... In the standard orthography, n and ng are not
# distinguished." (Skribnik 2003:106)

@pytest.mark.parametrize("word", [
    "шэхэн",   # шэхэн 'ear'
    "аман",         # аман 'mouth'
])
def test_word_final_n_is_velar(word):
    assert _t(word).endswith("ŋ")


def test_medial_n_is_not_velar():
    assert _t("хана") == "xana"  # хана 'wall' (Skribnik's own example)
