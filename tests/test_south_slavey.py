"""Per-language accuracy tests for South Slavey (xsl), a Northern Athabaskan
(Dene) language of the Dehcho region written in a practical Roman orthography.

Every expectation below is a claim about the language, sourced from the
citations carried in ``data/xsl.json``. Words are drawn from published South
Slavey vocabulary; the IPA is the value the cited descriptions predict, not a
value read back from any engine.

Run with:
    pytest tests/test_south_slavey.py -v --tb=short
"""
from __future__ import annotations

import unicodedata

import pytest

import orthography2ipa


def _spec():
    try:
        return orthography2ipa.get("xsl")
    except Exception as exc:  # pragma: no cover - registry failure
        pytest.skip(f"xsl not available: {exc}")


def _ipa(word: str) -> str:
    # Composed form on both sides: ṹ has a precomposed codepoint and ɛ̃́ does
    # not, so an uncomposed literal in a test would fail for a typographic
    # reason rather than a phonological one.
    return unicodedata.normalize("NFC", orthography2ipa.transcribe(word, "xsl"))


def _eq(word: str, expected: str) -> bool:
    return _ipa(word) == unicodedata.normalize("NFC", expected)


class TestLaryngealSeries:
    """The Athabaskan three-way contrast: plain, aspirated, ejective."""

    @pytest.mark.parametrize("grapheme,expected", [
        ("b", "p"), ("d", "t"), ("g", "k"),
        ("dz", "ts"), ("j", "tʃ"), ("dl", "tɬ"),
    ])
    def test_plain_series_is_voiceless_unaspirated(self, grapheme, expected):
        # Unaspirated obstruents are voiceless or only weakly voiced, so the
        # voiceless value leads and the voiced one stays as an alternative.
        assert _spec().graphemes[grapheme][0] == expected

    @pytest.mark.parametrize("grapheme,expected", [
        ("t", "tʰ"), ("k", "kʰ"), ("ts", "tsʰ"),
        ("ch", "tʃʰ"), ("tl", "tɬʰ"), ("tł", "tɬʰ"), ("tth", "tθʰ"),
    ])
    def test_aspirated_series(self, grapheme, expected):
        assert _spec().graphemes[grapheme] == [expected]

    @pytest.mark.parametrize("grapheme,expected", [
        ("tʼ", "tʼ"), ("kʼ", "kʼ"), ("tsʼ", "tsʼ"),
        ("chʼ", "tʃʼ"), ("tlʼ", "tɬʼ"), ("tthʼ", "tθʼ"),
    ])
    def test_ejectives_both_apostrophes(self, grapheme, expected):
        graphemes = _spec().graphemes
        assert graphemes[grapheme] == [expected]
        # Published materials use the ASCII apostrophe as well as U+02BC.
        assert graphemes[grapheme.replace("ʼ", "'")] == [expected]

    def test_ejective_words(self):
        assert _ipa("kʼoh") == "kʼòh"
        assert _ipa("tsʼu") == "tsʼù"
        assert _ipa("tthʼéh") == "tθʼɛ́h"


class TestLaterals:
    """⟨ł⟩ is voiceless [ɬ] against ⟨l⟩ voiced [ɮ] — a fricative, not [l]."""

    def test_voiceless_lateral_fricative(self):
        assert _spec().graphemes["ł"] == ["ɬ"]

    def test_voiced_lateral_fricative_leads(self):
        assert _spec().graphemes["l"][0] == "ɮ"

    def test_lateral_pair_in_words(self):
        assert _ipa("łeh") == "ɬɛ̀h"
        assert _ipa("ɂelá") == "ʔɛ̀ɮá"


class TestInterdentals:
    """⟨th⟩/⟨dh⟩ are the interdental fricatives and ⟨tth⟩ the affricate."""

    def test_fricatives(self):
        assert _ipa("tha") == "θà"
        assert _ipa("ɂedhéh") == "ʔɛ̀ðɛ́h"

    def test_interdental_affricate_beats_th(self):
        # Maximal munch must take ⟨tth⟩ whole; t + th would give [tʰθ].
        assert _ipa("tthe") == "tθʰɛ̀"


class TestTone:
    """Two tones. The acute writes high; the unmarked vowel is low, and low is
    a tone rather than the absence of one, so it is spelled out with a grave."""

    @pytest.mark.parametrize("word,expected", [
        ("sa", "sà"),
        ("tsá", "tsʰá"),
        ("hé", "hɛ́"),
        ("tu", "tʰù"),
    ])
    def test_tone_written_on_every_vowel(self, word, expected):
        assert _ipa(word) == expected

    def test_high_and_low_in_one_word(self):
        assert _ipa("ɂetá") == "ʔɛ̀tʰá"


class TestNasalVowels:
    """The ogonek writes nasalization and combines with the tone acute."""

    def test_low_nasal(self):
        assert _eq("shį", "ʃĩ̀")
        assert _eq("tę", "tʰɛ̃̀")

    def test_high_nasal(self):
        assert _eq("kų́", "kʷʰṹ")
        assert _eq("gotsʼę́", "kʷòtsʼɛ̃́")


class TestVowelQualityAndLength:
    """⟨e⟩ is [ɛ] and ⟨o⟩ is [o]; a doubled vowel letter is one long nucleus."""

    def test_e_is_open_mid(self):
        assert _ipa("dene") == "tɛ̀nɛ̀"

    def test_long_vowel_is_one_nucleus(self):
        assert _ipa("sadzee") == "sàtsɛ̀ː"
        assert _ipa("nódayaa") == "nótàjàː"

    def test_long_vowel_carries_its_tone_mark(self):
        assert _ipa("tsáah") == "tsʰáːh"


class TestVelarAllophony:
    """Velar obstruents front to a palatal before front vowels and labialize
    before round vowels."""

    def test_fronting_before_front_vowel(self):
        assert _ipa("deneke") == "tɛ̀nɛ̀cʰɛ̀"
        assert _ipa("xeníh") == "çɛ̀níh"

    def test_labialization_before_round_vowel(self):
        assert _eq("golǫ", "kʷòɮõ̀")
        assert _ipa("xóo") == "xʷóː"
        assert _ipa("ɂeghú") == "ʔɛ̀ɣʷú"

    def test_plain_velar_before_low_vowel(self):
        assert _ipa("gah") == "kàh"
        assert _ipa("xah") == "xàh"
        assert _ipa("gha") == "ɣà"

    def test_ejective_velar_does_not_shift(self):
        assert _eq("kʼų́", "kʼṹ")
        assert _ipa("kʼoh") == "kʼòh"


class TestLaxI:
    """The source gives ⟨i⟩ as [i] with a lax [ɪ] alternant. Its stated
    environment is not applicable as written, so the split encoded here is the
    one the narrow transcriptions draw: the word's last nucleus keeps [i] and
    every earlier one laxes."""

    def test_last_nucleus_keeps_tense_i(self):
        assert _ipa("medzih") == "mɛ̀tsìh"
        assert _ipa("yati") == "jàtʰì"
        assert _ipa("xeníh") == "çɛ̀níh"

    def test_earlier_nuclei_lax(self):
        assert _ipa("ɂejide") == "ʔɛ̀tʃɪ̀tɛ̀"
        assert _ipa("bebíah") == "pɛ̀pɪ́àh"

    def test_tone_survives_the_laxing(self):
        assert _ipa("lidí") == "ɮɪ̀tí"
        assert _ipa("jíye") == "tʃɪ́jɛ̀"


class TestBorrowedR:
    """⟨r⟩ is outside the South Slavey letter inventory and appears only in
    borrowings. The flap the sources describe belongs to Hare, so it is not
    read in here."""

    def test_r_is_a_plain_rhotic(self):
        assert _spec().graphemes["r"] == ["r"]


class TestCodaH:
    """A coda ⟨h⟩ before a consonant is preaspiration on the preceding vowel;
    elsewhere ⟨h⟩ stays [h]."""

    def test_preaspiration_before_consonant(self):
        assert _ipa("dihcho") == "tɪ̀ʰtʃʰò"
        assert _ipa("máhsi") == "máʰsì"

    def test_intervocalic_h_survives(self):
        assert _ipa("mbehah") == "ᵐbɛ̀hàh"

    def test_word_final_h_survives(self):
        assert _ipa("shah") == "ʃàh"


class TestGlottalStopAndLabialization:
    """⟨ɂ⟩ writes the glottal stop, and ⟨kw⟩ is /k/ + /w/ — labialization is
    allophonic, so the sequence gets no grapheme key of its own."""

    def test_glottal_stop_letter(self):
        assert _ipa("ɂah") == "ʔàh"
        assert _spec().graphemes["ɂ"] == ["ʔ"]

    def test_kw_is_two_segments(self):
        assert "kw" not in _spec().graphemes
        assert _eq("ɂekwǫjire", "ʔɛ̀kʰwõ̀tʃɪ̀rɛ̀")


class TestPrenasalized:
    """⟨mb⟩ and ⟨nd⟩ are single prenasalized segments, listed by the Dene
    Speech Atlas among the sonorants as alternants of ⟨m⟩ and ⟨n⟩."""

    def test_prenasalized_units(self):
        assert _ipa("mbeh") == "ᵐbɛ̀h"
        assert _ipa("ndu") == "ⁿdù"

    def test_both_carry_the_voicing_alternation(self):
        # Same two-way listing as every other unaspirated obstruent.
        assert _spec().graphemes["mb"] == ["ᵐb", "ᵐp"]
        assert _spec().graphemes["nd"] == ["ⁿd", "ⁿt"]

    def test_prenasalized_after_vowel(self):
        assert _ipa("samba") == "sàᵐbà"
