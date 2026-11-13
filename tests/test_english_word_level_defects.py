"""English words whose spelling rules left them with no vowel or the wrong one.

Every expected value comes from a source, never from the engine:

* Wikipedia, "English orthography", section "Spelling-to-sound
  correspondences", revision 1383244083 (WP below). Its vowel tables give
  ⟨e⟩ "final, only vowel in word" as /iː/ (be, she); ⟨u⟩ "in open syllables,
  word-final" as /juː/ (menu, emu), and /uː/ after /r ʃ ʒ j/ or a consonant
  plus /l/ (flu, guru); ⟨y⟩ "word-final" as /aɪ/ (by, sky); and its
  sound-to-spelling table lists "y...e, ye" (type, bye) and "eye" among the
  spellings of /aɪ/.
* Wiktionary entries, English section, revision in brackets: e (95535908)
  letter name /iː/; u (95573816) /ˈjuː/; mu (95548451) /mjuː/; menu
  (95547329) RP /ˈmɛn.juː/, GA /ˈmɛn.ju/; flu (94555718) UK /fluː/; guru
  (95538950) UK /ˈɡʊɹuː/, US /ˈɡʊɹ(ˌ)u/; bye (93682799) /baɪ/; dye (93691184)
  /daɪ/; rye (94434257) /ɹaɪ/; lye (95359393) /laɪ/; wye (93735354) /ˈwaɪ/;
  goodbye (94595568) RP /ɡʊdˈbaɪ/; eye (95585237) /ˈaɪ/; ye (93735623)
  /jiː/ UK, US; I (94540244) /aɪ/; I'm (92742410) RP /aɪm/; I'll (95493560)
  /aɪl/; I'd (93574985) /aɪd/; I've (91402232) /aɪv/; is (94583004) /ɪz/;
  as (95585818) strong /æz/; was (95477958) RP strong /wɒz/, US /wʌz/; has
  (93872082) stressed /hæz/; his (95411505) strong /hɪz/; you (92960107) RP
  strong /juː/, GA /ju/; your (94591594) RP stressed /jɔː(ɹ)/, GA enPR
  "yôr"; are (95563998) RP strong /ɑː/, GA strong /ɑɹ/.

en-US writes no length marks (its notes, after Kenyon & Knott 1953), so a GA
value is the source's value in that notation. The word-stress mark is a
separate claim and is stripped before the comparison.
"""
import pytest

from orthography2ipa import G2P, get
from orthography2ipa.inventory import dead_allophone_rules


def _t(code, word):
    return G2P(code).transcribe_word(word).lstrip("ˈ")


# ─── a word's only vowel letter is not silent ─────────────────────────────

@pytest.mark.parametrize("code, expected", [("en-GB", "iː"), ("en-US", "i")])
def test_the_letter_e_is_its_name(code, expected):
    assert _t(code, "e") == expected


def test_the_letter_e_keeps_its_place_in_a_sentence():
    words = G2P("en-GB").transcribe("nine e em").split()
    assert [w.lstrip("ˈ") for w in words] == ["naɪn", "iː", "ɛm"]


@pytest.mark.parametrize("word, gb, us", [
    ("be", "biː", "bi"),
    ("she", "ʃiː", "ʃi"),
])
def test_the_rule_reaches_the_function_words(word, gb, us):
    """be and she are the WP examples of the row; no exception holds them."""
    assert word not in G2P("en-GB").spec.word_exceptions
    assert _t("en-GB", word) == gb
    assert _t("en-US", word) == us


def test_a_rule_on_a_silent_reading_is_live_where_the_tables_emit_it():
    """en-GB reads word-final ⟨e⟩ as "", so the rule on "" can fire there.
    Krio inherits the rule but its tables have no silent reading."""
    assert "EN_GB_FINAL_E_SOLE_VOWEL" not in dead_allophone_rules(get("en-GB"))
    assert "EN_GB_FINAL_E_SOLE_VOWEL" in dead_allophone_rules(get("kri"))


@pytest.mark.parametrize("word, expected", [
    ("type", "taɪp"),       # WP: "y...e" spelling of /aɪ/
    ("style", "staɪl"),     # WP: ⟨y⟩ before a single consonant, /aɪ/
    ("use", "juːz"),        # WP: "u...e" spelling of /juː/, example "use"
])
def test_a_silent_e_after_another_vowel_stays_silent(word, expected):
    assert _t("en-GB", word) == expected


# ─── ⟨y⟩ before a silent final ⟨e⟩ ───────────────────────────────────────

@pytest.mark.parametrize("word, expected", [
    ("bye", "baɪ"),
    ("dye", "daɪ"),
    ("rye", "ɹaɪ"),
    ("lye", "laɪ"),
    ("wye", "waɪ"),
])
@pytest.mark.parametrize("code", ["en-GB", "en-US"])
def test_y_before_a_silent_final_e_is_a_diphthong(code, word, expected):
    assert _t(code, word) == expected


def test_goodbye_ends_in_the_diphthong():
    assert _t("en-GB", "goodbye").endswith("baɪ")


# ─── word-final ⟨u⟩ ───────────────────────────────────────────────────────

@pytest.mark.parametrize("word, gb, us", [
    ("u", "juː", "ju"),
    ("mu", "mjuː", "mju"),
    ("menu", "mɛnjuː", "mɛnju"),
    ("flu", "fluː", "flu"),
])
def test_word_final_u(word, gb, us):
    assert _t("en-GB", word) == gb
    assert _t("en-US", word) == us


@pytest.mark.parametrize("code, ending", [("en-GB", "ɹuː"), ("en-US", "ɹu")])
def test_final_u_after_r_has_no_yod(code, ending):
    """guru: WP gives it as the example of /uː/ after /r/. The first vowel
    is a separate fact, so only the final syllable is compared."""
    assert _t(code, "guru").endswith(ending)


@pytest.mark.parametrize("word, expected", [
    ("but", "bʌt"),         # WP: ⟨u⟩ in a closed syllable, /ʌ/, "but"
    ("mute", "mjuːt"),      # WP: ⟨u⟩ in an open syllable, /juː/, "mute"
])
def test_u_that_is_not_word_final_is_unchanged(word, expected):
    assert _t("en-GB", word) == expected


# ─── whole-word exceptions ────────────────────────────────────────────────

@pytest.mark.parametrize("word, expected", [
    ("i", "aɪ"),
    ("I", "aɪ"),
    ("i'm", "aɪm"),
    ("I’m", "aɪm"),
    ("i'll", "aɪl"),
    ("i’ll", "aɪl"),
    ("i'd", "aɪd"),
    ("i’d", "aɪd"),
    ("i've", "aɪv"),
    ("i’ve", "aɪv"),
    ("is", "ɪz"),
    ("as", "æz"),
    ("was", "wɒz"),
    ("has", "hæz"),
    ("his", "hɪz"),
    ("you", "juː"),
    ("your", "jɔː"),
    ("are", "ɑː"),
    ("ye", "jiː"),
    ("eye", "aɪ"),
])
def test_en_gb_function_words(word, expected):
    assert _t("en-GB", word) == expected


@pytest.mark.parametrize("word, expected", [
    ("i", "aɪ"),
    ("i’ve", "aɪv"),
    ("is", "ɪz"),
    ("was", "wʌz"),
    ("you", "ju"),
    ("your", "jɔɹ"),
    ("are", "ɑɹ"),
    ("ye", "ji"),
    ("eye", "aɪ"),
])
def test_en_us_function_words(word, expected):
    assert _t("en-US", word) == expected


@pytest.mark.parametrize("word, expected", [
    ("by", "baɪ"),          # WP: ⟨y⟩ word-final, /aɪ/, "by, sky"
    ("sky", "skaɪ"),
])
def test_en_us_final_y_is_unchanged(word, expected):
    assert _t("en-US", word) == expected
