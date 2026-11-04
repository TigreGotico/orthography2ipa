"""Limburgish (``li``) spelling-to-sound cases the grapheme table is pinned to.

The sources are cited in the ``li`` spec notes; this file only pins the readings.
"""
import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.vowels import is_ipa_vowel

LI = G2P("li")


@pytest.mark.parametrize("word", ["Amboss", "Begenn", "Jannewaar", "Blitterswik"])
def test_doubled_consonant_letter_is_not_a_geminate(word):
    out = LI.transcribe(word)
    assert not any(c * 2 in out for c in "bdfklmnprst"), out


@pytest.mark.parametrize("word", ["Baasch", "Aïsch"])
def test_sch_is_the_postalveolar_fricative(word):
    out = LI.transcribe(word)
    assert "ʃ" in out and "sç" not in out, out


def test_g_before_a_back_vowel_is_the_velar_fricative():
    assert LI.transcribe("Gott").lstrip("ˈ").startswith("ɣ")


def test_g_before_a_front_vowel_is_the_palatal_fricative():
    assert LI.transcribe("gitaar").lstrip("ˈ").startswith("ʝ")


# Tone accent. Spelling 2003, printed p. 27, §8 h-i: ⟨~⟩ after the vowel
# writes sleeptoon and ⟨\⟩ writes stoottoon, with the pairs haa~s
# 'handschoen' / haa\s 'haas' and be~rg 'berg' / be\rg 'bergen'. Hermans
# 2008, p. 40, gives the Roermond pair as Accent1 [ha:s] 'haas' and Accent2
# [ha:s] 'handschoen', so ⟨\⟩ is Accent 1 and ⟨~⟩ is Accent 2. Gussenhoven
# & Peters 2019, p. 498, write the classes ¹ and ²; Peters 2006, p. 119,
# writes the digit at the end of its syllable (/boːt²/, /ˈpoː²kər/).

def _segments(ipa):
    return "".join(c for c in ipa if c not in "ˈˌ¹²")


@pytest.mark.parametrize("sleeptoon, stoottoon, unmarked", [
    ("haa~s", "haa\\s", "haas"),
    ("be~rg", "be\\rg", "berg"),
    ("ze~ve", "ze\\ve", "zeve"),
    ("vae~r", "vae\\r", "vaer"),
])
def test_tone_signs_write_the_accent_class(sleeptoon, stoottoon, unmarked):
    accent2, accent1, bare = (LI.transcribe_word(w)
                              for w in (sleeptoon, stoottoon, unmarked))
    assert accent2.count("²") == 1 and "¹" not in accent2, accent2
    assert accent1.count("¹") == 1 and "²" not in accent1, accent1
    assert "¹" not in bare and "²" not in bare, bare
    assert _segments(accent2) == _segments(accent1) == _segments(bare)


@pytest.mark.parametrize("word, next_onset", [
    ("haa~s", ""),
    ("be\\rg", ""),
    ("vae~r", ""),
    ("ze~ve", "v"),
])
def test_accent_digit_closes_its_syllable(word, next_onset):
    out = LI.transcribe_word(word)
    digit = next(i for i, c in enumerate(out) if c in "¹²")
    assert out[digit + 1:digit + 2] == next_onset, out
    if next_onset:
        assert is_ipa_vowel(out[:digit].rstrip("ː")[-1]), out


# Stress. Peters 2006, p. 119: Hasselt 'Stress location is as in Standard
# Belgian Dutch'; Gussenhoven & Peters 2019, p. 497: the syllable with main
# stress is 'typically the final or penultimate'; Köhnlein 2015
# (Taalportaal): 'A syllable headed by a schwa never receives stress';
# Spelling 2003, p. 10: "e of ' = onbeklemtoonde klinker". The words are
# from Spelling 2003: sjoon p. 11, kómme p. 17, verlange p. 26.

def test_a_monosyllable_is_stressed():
    assert LI.transcribe_word("sjoon").startswith("ˈʃ")


def test_stress_falls_before_a_final_schwa_syllable():
    out = LI.transcribe_word("kómme")
    assert out.startswith("ˈk") and out.count("ˈ") == 1, out


def test_a_schwa_prefix_is_not_stressed():
    out = LI.transcribe_word("verlange")
    assert out.count("ˈ") == 1, out
    assert out.split("ˈ")[1].startswith("l"), out


# Unstressed prefixes. Peters 2006, p. 119, and Heijmans & Gussenhoven 1998,
# p. 111: the stress follows the standard language. Schultink 1976, p. 475:
# 'be-, er-, ge-, ont- en ver-' are 'altijd accentloos'. Spelling 2003,
# printed p. 27, §8 i: the tone signs are 'de middele óm de
# lettergreepbetoning aan te gaeve', and the marked sentence writes
# 'gebroe~k'. The words are from Spelling 2003: gebroek p. 27, gevatj p. 23,
# gesjpeld p. 27, gesjtump p. 19, besjteit p. 26, versjtandj p. 26,
# verplich p. 27.

@pytest.mark.parametrize("word", [
    "gebroek", "gebroe~k", "gevatj", "gesjpeld", "gesjtump",
    "besjteit", "versjtandj", "verplich",
])
def test_the_stress_skips_an_unstressed_prefix(word):
    out = LI.transcribe_word(word)
    assert out.count("ˈ") == 1, out
    assert _vowels(out.split("ˈ")[0]) == ["ə"], out


# Peters 2006, p. 119: 'In stressed syllables, short vowels are followed by a
# coda consonant', so Gen-nep and Bel-vend start with a closed syllable, not
# with a prefix syllable, and keep the default penult. The place names are
# wikipron headwords.

@pytest.mark.parametrize("word", ["Gennep", "Belvend"])
def test_a_closed_first_syllable_is_not_a_prefix(word):
    assert LI.transcribe_word(word).startswith("ˈ"), LI.transcribe_word(word)


# The vowel of ⟨e⟩. Spelling 2003, printed p. 10: short ⟨e⟩ beside 'àè (de e
# van Ned. pet maar dan lang)', the long 'e (Limb. sjpele)' in the row of
# 'ee (Ned. beest)', and "e of ' = onbeklemtoonde klinker". Printed p. 16,
# §14 b: at the end of a syllable 'maar één a, e, u, o'. Printed p. 14, §8 f:
# a sign of two letters for one sound after a short vowel 'werkt als twee
# aparte tekens'. Printed p. 13, §8 a: a short word-final vowel is written
# with ⟨h⟩ (deh, meh). Peters 2006, p. 118, gives the symbols: short 'æ mæs²
# ‘knife’' below 'ɛ dɛk ‘often’', long 'eː', and ə 'restricted to unstressed
# syllables'; Spelling 2003, p. 11, puts ⟨è⟩ above ⟨e⟩, so ⟨e⟩ is [æ].
# The words are from Spelling 2003: pp. 10, 13, 24 and 27.

def _vowels(ipa):
    out = []
    for c in ipa:
        if is_ipa_vowel(c):
            out.append(c)
        elif c == "ː" and out:
            out[-1] += c
    return out


@pytest.mark.parametrize("word", [
    "berg", "be~rg", "be\\rg", "det", "we~rk", "me~r",
    "bed", "vet", "mes", "wet", "Wessem",
])
def test_stressed_e_in_a_closed_syllable_is_short(word):
    out = LI.transcribe_word(word)
    assert _vowels(out)[0] == "æ", out


def test_a_doubled_consonant_letter_closes_the_syllable():
    out = LI.transcribe_word("oplette")
    assert _vowels(out) == ["ɔ", "æ", "ə"], out


def test_a_consonant_digraph_closes_the_syllable():
    out = LI.transcribe_word("henjig")
    assert _vowels(out)[0] == "æ", out


@pytest.mark.parametrize("word", ["zeve", "ze~ve", "ze\\ve", "sjpele"])
def test_stressed_e_that_ends_its_syllable_is_long(word):
    out = LI.transcribe_word(word)
    assert _vowels(out) == ["eː", "ə"], out


@pytest.mark.parametrize("word", ["deh", "meh"])
def test_word_final_h_keeps_the_e_short(word):
    out = LI.transcribe_word(word)
    assert _vowels(out) == ["æ"], out


# A word-final full vowel is written with two signs: ⟨eh⟩ for the short one
# (p. 13, §8 a) and ⟨ee⟩ for the long one (p. 16, §14 b: 'het basiswoord
# eindigt op die noodzakelijke dubbele ee'). A final single ⟨e⟩ is [ə]: p. 10
# gives 'de' for the unstressed vowel, and p. 27 writes 'mót me ze'. The dev
# table already reads these as [ə]; the test keeps nucleus_stressed off them.

@pytest.mark.parametrize("word", ["de", "me", "ze"])
def test_word_final_e_is_schwa(word):
    out = LI.transcribe_word(word)
    assert _vowels(out) == ["ə"], out


# ⟨ew⟩ before a vowel. Spelling 2003, printed p. 10, lists ⟨ew⟩ as a vowel +
# glide sign ('met naslag (ë, è, j of w)'). Printed p. 12, §6 g: these signs
# stay 'binnen de lettergreepgrens', and two syllables take a glide letter
# ('–ieje'). Printed p. 13, §6 h, puts that ⟨j⟩ at a syllable edge between two
# vowels. The quotes name ⟨j⟩; reading ⟨w⟩ the same way is an analogy. Printed
# p. 27 writes geweu\n with the tone sign after ⟨eu⟩, the stressed nucleus.
# The words: geweu\n p. 27, bewaar p. 29, eweg p. 30.

@pytest.mark.parametrize("word, tokens", [
    ("geweu\\n", ["g", "e", "w", "eu", "\\", "n"]),
    ("bewaar", ["b", "e", "w", "aa", "r"]),
    ("eweg", ["e", "w", "e", "g"]),
])
def test_ew_before_a_vowel_gives_its_glide_to_the_next_syllable(word, tokens):
    assert LI._tokenizer.graphemes(word) == tokens


def test_ew_alone_stays_one_sign():
    assert LI._tokenizer.graphemes("ew") == ["ew"]


@pytest.mark.parametrize("word", ["geweu\\n", "bewaar"])
def test_the_prefix_before_a_glide_is_schwa(word):
    out = LI.transcribe_word(word)
    assert out.split("ˈ")[0] in ("ʝə", "bə") and out.split("ˈ")[1][0] == "w", out


# ⟨àè⟩. Spelling 2003, printed p. 10, gives the long partner of short ⟨e⟩ as
# 'àè (de e van Ned. pet maar dan lang)', with the after-glide signs ⟨àèë⟩ and
# ⟨àèw⟩. The Dutch vowel of pet is [ɛ] (Wells, SAMPA for Dutch, 'E pet pEt';
# Gussenhoven 1992, p. 46, 'ɛ bed'). No source word uses the sign, so the
# words are test strings.

@pytest.mark.parametrize("word, tokens", [
    ("zàèle", ["z", "àè", "l", "e"]),
    ("vàèl", ["v", "àè", "l"]),
    ("vàèë", ["v", "àèë"]),
    ("zàèw", ["z", "àèw"]),
])
def test_ae_grave_is_one_sign(word, tokens):
    assert LI._tokenizer.graphemes(word) == tokens


@pytest.mark.parametrize("word, segments", [
    ("zàèle", "zɛːlə"),
    ("vàèl", "vɛːl"),
    ("vàèë", "vɛːə"),
    ("zàèw", "zɛːw"),
])
def test_ae_grave_is_the_long_vowel_of_dutch_pet(word, segments):
    strict = G2P("li", on_unmapped="raise")
    assert strict.transcribe_word(word).replace("ˈ", "") == segments
