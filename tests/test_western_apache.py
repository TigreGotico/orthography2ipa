"""Per-language accuracy tests for Western Apache (apw), a Southern
Athabaskan (Apachean) language of east-central Arizona written in the
practical orthography used for San Carlos and White Mountain Apache.

Every expectation below is a claim about the language, taken from the
citations carried in ``data/apw.json``. The words and their IPA are the
worked examples the cited alphabet and phonology tables print, or values
those tables predict directly; nothing here is read back from any engine.

Run with:
    pytest tests/test_western_apache.py -v --tb=short
"""
from __future__ import annotations

import unicodedata

import pytest

import orthography2ipa


def _spec():
    try:
        return orthography2ipa.get("apw")
    except Exception as exc:  # pragma: no cover - registry failure
        pytest.skip(f"apw not available: {exc}")


def _ipa(word: str) -> str:
    # Composed form on both sides: ṍ has a precomposed codepoint and ɪ̃́
    # does not, so an uncomposed literal would fail for a typographic
    # reason rather than a phonological one.
    return unicodedata.normalize("NFC", orthography2ipa.transcribe(word, "apw"))


def _n(s: str) -> str:
    return unicodedata.normalize("NFC", s)


class TestLaryngealSeries:
    """The Athabaskan three-way contrast. The voiced-looking letters write
    the PLAIN (voiceless unaspirated) series, not voiced stops."""

    @pytest.mark.parametrize("grapheme,expected", [
        ("b", "p"), ("d", "t"), ("g", "k"), ("dz", "ts"), ("dl", "tɬ"),
    ])
    def test_plain_series_is_voiceless_unaspirated(self, grapheme, expected):
        assert _spec().graphemes[grapheme] == [expected]

    @pytest.mark.parametrize("grapheme,expected", [
        ("t", "tʰ"), ("k", "kʰ"), ("ts", "tsʰ"),
        ("ch", "tʃʰ"), ("tł", "tɬʰ"), ("p", "pʰ"),
    ])
    def test_aspirated_series(self, grapheme, expected):
        assert _spec().graphemes[grapheme] == [expected]

    @pytest.mark.parametrize("grapheme,expected", [
        ("tʼ", "tʼ"), ("kʼ", "kʼ"), ("tsʼ", "tsʼ"),
        ("chʼ", "tʃʼ"), ("tłʼ", "tɬʼ"),
    ])
    def test_ejectives_take_every_apostrophe(self, grapheme, expected):
        graphemes = _spec().graphemes
        # The scraped Wiktionary headwords use U+02BC (68 times) and U+2019
        # (8 times) and no ASCII apostrophe at all; ASCII is accepted as the
        # common typing substitute for the modifier letter.
        for apostrophe in ("ʼ", "’", "'"):
            key = grapheme.replace("ʼ", apostrophe)
            assert graphemes[key] == [expected], key

    def test_j_is_the_one_voiced_affricate(self):
        # The alphabet table draws ⟨j⟩ /dʒ/ against plain ⟨dz⟩ /ts/.
        assert _spec().graphemes["j"] == ["dʒ"]

    @pytest.mark.parametrize("word,expected", [
        ("bésh", "pɛ́ʃ"),          # knife
        ("dził", "tsɪɬ"),          # mountain
        ("chizh", "tʃʰɪʒ"),        # wood
        ("chʼah", "tʃʼax"),        # hat
        ("kʼaa", "kʼaː"),          # bullets
        ("tsʼaał", "tsʼaːɬ"),      # cradleboard
        ("itʼoh", "ɪtʼox"),        # nest
        ("tłád", "tɬʰát"),         # oil
        ("tłʼoh", "tɬʼox"),        # plants
        ("piishi", "pʰɪːʃɪ"),      # swallow
    ])
    def test_worked_examples(self, word, expected):
        assert _ipa(word) == _n(expected)


class TestLateralsAndFricatives:
    """⟨ł⟩ is the voiceless lateral fricative; ⟨l⟩ is a plain approximant,
    NOT the voiced lateral fricative of the Northern Athabaskan languages."""

    def test_barred_l_is_voiceless_lateral_fricative(self):
        assert _spec().graphemes["ł"] == ["ɬ"]

    def test_plain_l_is_an_approximant(self):
        assert _spec().graphemes["l"] == ["l"]

    def test_lateral_pair_in_words(self):
        assert _ipa("łóg") == _n("ɬók")     # fish
        assert _ipa("iloh") == _n("ɪlox")   # thread

    def test_h_is_the_velar_fricative(self):
        # The alphabet table gives H = /x/ with ⟨hashbidí⟩ [xaʃpɪtɪ́];
        # the consonant chart lists /h/ too, kept as the second candidate.
        assert _spec().graphemes["h"][0] == "x"
        assert "h" in _spec().graphemes["h"]
        assert _ipa("hashbidí") == _n("xaʃpɪtɪ́")   # quail

    def test_voiced_velar_fricative(self):
        assert _ipa("ighál") == _n("ɪɣál")   # bells


class TestVowelQualities:
    """Four qualities. Short ⟨i⟩ is lax /ɪ/ and short ⟨e⟩ is /ɛ/."""

    @pytest.mark.parametrize("grapheme,expected", [
        ("a", "a"), ("e", "ɛ"), ("i", "ɪ"), ("o", "o"), ("u", "u"),
    ])
    def test_short_vowels(self, grapheme, expected):
        assert _spec().graphemes[grapheme] == [expected]

    def test_short_i_is_lax(self):
        assert _ipa("izee") == _n("ɪzɛː")   # medicine

    @pytest.mark.parametrize("word,expected", [
        ("shash", "ʃaʃ"),          # bear
        ("zas", "zas"),            # snow
        ("acha", "atʃʰa"),         # ax
        ("eʼilzaa", "ɛʔɪlzaː"),    # picture
        ("silaada", "sɪlaːta"),    # soldier
    ])
    def test_worked_examples(self, word, expected):
        assert _ipa(word) == _n(expected)


class TestVowelLength:
    """Length is written by doubling the letter."""

    @pytest.mark.parametrize("grapheme,expected", [
        ("aa", "aː"), ("ee", "ɛː"), ("ii", "ɪː"), ("oo", "oː"),
        ("ąą", "ãː"), ("ęę", "ɛ̃ː"), ("įį", "ɪ̃ː"), ("ǫǫ", "õː"),
    ])
    def test_doubled_letter_is_one_long_nucleus(self, grapheme, expected):
        assert _spec().graphemes[_n(grapheme)] == [_n(expected)]

    def test_long_close_vowel_is_lax(self):
        # The article's ⟨įį⟩ = /ɪ̃ː/ row and its ⟨piishi⟩ [pʰɪːʃɪ] example
        # both give the lax quality; only its vowel CHART prints /iː/.
        assert _spec().graphemes["ii"] == ["ɪː"]

    @pytest.mark.parametrize("word,expected", [
        ("kee", "kʰɛː"),           # shoe
        ("iwoo", "ɪwoː"),          # teeth
        ("yoo", "joː"),            # beads
        ("oyeeł", "ojɛːɬ"),        # carry
        ("zhaali", "ʒaːlɪ"),       # money
    ])
    def test_worked_examples(self, word, expected):
        assert _ipa(word) == _n(expected)


class TestNasalVowels:
    """The ogonek writes nasalization and combines with the tone acute."""

    @pytest.mark.parametrize("grapheme,expected", [
        ("ą", "ã"), ("ę", "ɛ̃"), ("į", "ɪ̃"), ("ǫ", "õ"),
        ("ą́", "ã́"), ("ę́", "ɛ̃́"), ("į́", "ɪ̃́"), ("ǫ́", "ṍ"),
    ])
    def test_ogonek_vowels(self, grapheme, expected):
        assert _spec().graphemes[_n(grapheme)] == [_n(expected)]

    def test_nasal_in_words(self):
        # The source prints ⟨nadą́ʼ⟩ "corn" as [natã́], dropping the final
        # glottal stop its own ⟨ʼ⟩ = /ʔ/ row requires; the ⟨dlǫ́ʼ⟩ "bird"
        # row on the same table keeps it. The rule wins over the typo.
        assert _ipa("nadą́ʼ") == _n("natã́ʔ")
        assert _ipa("dlǫ́ʼ") == _n("tɬṍʔ")

    def test_hook_below_is_the_same_letter_as_the_ogonek(self):
        # Some scraped headwords write the hook with U+031C instead of the
        # U+0328 ogonek.
        assert _ipa("kowa̜") == _ipa("kową")


class TestTone:
    """Two tones. The acute writes high; low tone is unmarked on BOTH
    sides, because the source leaves low-toned vowels bare."""

    @pytest.mark.parametrize("grapheme,expected", [
        ("á", "á"), ("é", "ɛ́"), ("í", "ɪ́"), ("ó", "ó"), ("ú", "ú"),
    ])
    def test_acute_is_high_tone(self, grapheme, expected):
        assert _spec().graphemes[_n(grapheme)] == [_n(expected)]

    def test_low_tone_carries_no_mark(self):
        # Unlike South Slavey, whose descriptions write the low tone out.
        assert _ipa("shash") == _n("ʃaʃ")
        assert _ipa("zas") == _n("zas")

    def test_high_and_low_in_one_word(self):
        assert _ipa("gaagé") == _n("kaːkɛ́")            # crow
        assert _ipa("jaasíláhá") == _n("dʒaːsɪ́láxá")   # earrings

    @pytest.mark.parametrize("spelling", ["áá", "áa", "aá"])
    def test_acute_on_either_half_of_a_long_vowel(self, spelling):
        assert _spec().graphemes[_n(spelling)] == ["áː"]

    def test_long_high_in_a_word(self):
        assert _ipa("yáá") == _n("jáː")
        assert _ipa("tú") == _n("tʰú")   # water


class TestGlottalStop:
    """⟨ʼ⟩ alone is /ʔ/, in all three apostrophe characters."""

    @pytest.mark.parametrize("apostrophe", ["ʼ", "’", "'"])
    def test_glottal_stop(self, apostrophe):
        assert _spec().graphemes[apostrophe] == ["ʔ"]

    def test_glottal_stop_in_a_word(self):
        assert _ipa("oʼiʼán") == _n("oʔɪʔán")   # hole


class TestMaximalMunch:
    """Digraphs must win over their first letter."""

    def test_ejective_beats_the_plain_stop(self):
        assert _ipa("kʼaa") != _ipa("kaa")

    def test_dz_is_not_d_plus_z(self):
        assert _ipa("dził") == _n("tsɪɬ")

    def test_tl_ejective_is_the_lateral_affricate(self):
        # A barred ⟨ł⟩ typed as plain ⟨l⟩ is unambiguous before the
        # ejective apostrophe.
        assert _ipa("tlʼoh") == _ipa("tłʼoh")

    def test_bare_tl_stays_two_segments(self):
        # ⟨biditlid⟩: a bare ⟨tl⟩ also arises across a morpheme boundary,
        # so it is not read as the lateral affricate.
        assert _ipa("biditlid") == _n("pɪtɪtʰlɪt")


class TestNotInTheOrthography:
    """Letters the 31-consonant chart and the alphabet table do not have."""

    @pytest.mark.parametrize("grapheme", ["kw", "x"])
    def test_absent(self, grapheme):
        assert grapheme not in _spec().graphemes


class TestCoverage:
    """No spelling in the practical orthography may transcribe to nothing."""

    @pytest.mark.parametrize("word", [
        "ę́ʼ", "ǫ́ʼáá", "túnálį́į́ʼ", "bį́", "ííchoʼ", "tʼąązhįʼ",
    ])
    def test_accented_and_nasal_words_are_not_dropped(self, word):
        assert _ipa(word) != ""
