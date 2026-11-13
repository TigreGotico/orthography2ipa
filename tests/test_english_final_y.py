"""A word-final ⟨y⟩ that is the word's only vowel letter, and the word menu.

Every expected value comes from a source, never from the engine:

* Wikipedia, "English orthography", section "Spelling-to-sound
  correspondences", revision 1383244083 (WP below). The vowel table assumes
  a stressed syllable where it gives no other information. Row ⟨y⟩, condition
  "word-final", gives /aɪ/ with the examples "awry, by, deny, sky, supply".
  The row "unstressed", condition "word-final", gives /i/ with the examples
  "any, city, happy, only, supply (adv)".
* Wiktionary entries, English section, revision in brackets: by (95577075)
  /baɪ/; my (95489720) stressed /maɪ/; fly (95586506) RP, GA /flaɪ/; why
  (95589259) /waɪ̯/; cry (93687487) RP, GA /kɹaɪ/; sky (93742195) /skaɪ/; try
  (95603390) /tɹaɪ/; dry (94602073) RP, GA, CA /ˈdɹaɪ̯/; shy (93722341)
  /ʃaɪ/; spy (95587957) /spaɪ/; sly (93604654) /slaɪ/; toy (94176516)
  /tɔɪ/; boy (95530370) RP, GA /bɔɪ/; day (95491099) RP, GA /deɪ̯/; key
  (95608628) RP /kiː/, GA /ki/; menu (95547329) RP /ˈmɛn.juː/, GA and CA
  /ˈmɛn.ju/.

The non-syllabic mark of /aɪ̯/ and the syllable dot of /ˈmɛn.juː/ are
notation, so the spec writes them aɪ and ˈmɛnjuː. en-US writes no length
marks, so a GA value is the source's value in that notation. The children of
en-GB write the PRICE vowel with the symbol of en-GB, aɪ.
"""
import pytest

from orthography2ipa import G2P

_EN_GB_CHILDREN = ["en-AU", "en-CA", "en-IE", "en-ZA", "en-GB-x-scotland"]

# word, value of the stressed vowel /aɪ/ (WP row ⟨y⟩ word-final, Wiktionary)
_FINAL_Y = [
    ("by", "baɪ"),
    ("my", "maɪ"),
    ("fly", "flaɪ"),
    ("why", "waɪ"),
    ("cry", "kɹaɪ"),
    ("sky", "skaɪ"),
    ("try", "tɹaɪ"),
    ("dry", "dɹaɪ"),
    ("shy", "ʃaɪ"),
    ("spy", "spaɪ"),
    ("sly", "slaɪ"),
]


def _t(code, word):
    return G2P(code).transcribe_word(word).lstrip("ˈ")


# ─── stressed word-final ⟨y⟩ ──────────────────────────────────────────────

@pytest.mark.parametrize("word, expected", _FINAL_Y)
@pytest.mark.parametrize("code", ["en-GB", "en-US", *_EN_GB_CHILDREN])
def test_final_y_of_a_monosyllable_is_the_price_vowel(code, word, expected):
    assert _t(code, word) == expected


@pytest.mark.parametrize("word", ["by", "my", "sky"])
def test_final_y_keeps_its_place_in_a_sentence(word):
    words = G2P("en-GB").transcribe(f"look {word} now").split()
    assert words[1].lstrip("ˈ") == dict(_FINAL_Y)[word]


# ─── unstressed word-final ⟨y⟩ ────────────────────────────────────────────

@pytest.mark.parametrize("word", ["happy", "city", "very", "baby", "any", "many"])
@pytest.mark.parametrize("code", ["en-GB", "en-US", *_EN_GB_CHILDREN])
def test_final_y_after_another_syllable_is_i(code, word):
    """WP: unstressed word-final ⟨y⟩ is /i/ (any, city, happy). Only the
    final vowel is compared: the vowels before it are a separate fact."""
    ipa = _t(code, word)
    assert ipa.endswith("i") and not ipa.endswith("aɪ")


# ─── ⟨y⟩ in a vowel digraph ───────────────────────────────────────────────

@pytest.mark.parametrize("word, gb, us", [
    ("toy", "tɔɪ", "tɔɪ"),
    ("boy", "bɔɪ", "bɔɪ"),
    ("day", "deɪ", "deɪ"),
    ("key", "kiː", "ki"),
])
def test_y_after_another_vowel_letter_is_part_of_the_digraph(word, gb, us):
    assert _t("en-GB", word) == gb
    assert _t("en-US", word) == us


@pytest.mark.parametrize("word", ["they", "grey"])
@pytest.mark.parametrize("code", ["en-GB", "en-US"])
def test_final_y_rule_skips_a_word_with_another_vowel_letter(code, word):
    """WP lists ⟨ey⟩ in they among the spellings of /eɪ/. The spec does not
    give that value, so the comparison is only that the ⟨y⟩ of the digraph
    does not become the PRICE vowel."""
    assert "aɪ" not in _t(code, word)


def test_the_takes_its_whole_word_exception():
    assert _t("en-GB", "the") == "ðə"


# ─── menu ─────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("code, expected", [
    ("en-GB", "ˈmɛnjuː"),
    ("en-US", "ˈmɛnju"),
])
def test_menu_has_the_yod(code, expected):
    assert G2P(code).transcribe_word("menu") == expected


@pytest.mark.parametrize("word", ["emu", "impromptu", "gnu"])
@pytest.mark.parametrize("code", ["en-GB", "en-US"])
def test_the_other_yod_loans_are_left_to_a_lexicon(code, word):
    assert word not in G2P(code).spec.word_exceptions
