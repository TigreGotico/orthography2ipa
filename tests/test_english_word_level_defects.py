"""English words whose spelling rules left them with no vowel or the wrong one.

Every expected value comes from a source, never from the engine:

* Wikipedia, "English orthography", section "Spelling-to-sound
  correspondences", revision 1383244083 (WP below). Its vowel tables give
  ⟨e⟩ "final, only vowel in word" as /iː/ (be, she); ⟨u⟩ "in open syllables,
  word-final" with /juː/ in "menu, emu, impromptu" and /uː/ in "hindu,
  tutu, tofu", and /uː/ after /r ʃ ʒ j/ or a consonant plus /l/ (flu, guru);
  ⟨y⟩ "word-final" as /aɪ/ (by, sky); and its sound-to-spelling table lists
  "y...e, ye" (type, bye) and "eye" among the spellings of /aɪ/.
* WikiPron decides the word-final ⟨u⟩ default: in eng_latn_uk_broad.tsv,
  257 of the 283 words that end in a consonant letter and ⟨u⟩ have /uː/
  only and 13 have /juː/ only (eng_latn_us_broad.tsv: 250 and 6 of 273).
* Wikipedia, "English auxiliary verbs", section "Unstressed and contracted
  forms of individual verbs", revision 1380541835: are → /ɹ/ ('re), have →
  /v/ ('ve).
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
  "yôr", CA /jʊəɹ/, rhotic /jo(ː)ɹ/; are (95563998) RP strong /ɑː/, GA and
  Standard Canadian strong /ɑɹ/, Ireland /aɹ/ or /ɑɹ/, Scotland /aɾ/, AU
  /ɐː/; was (95477958) Canada strong /wʌz/, AusE /wɔz/.

en-US writes no length marks (its notes, after Kenyon & Knott 1953), so a GA
value is the source's value in that notation. A rhotic spec writes the
source's /ɑɹ/ or /aɾ/ with the symbols of its own car (ɑːɹ), and its FORCE
vowel as in for (ɔː). The word-stress mark is a separate claim and is
stripped before the comparison.
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
    ("u", "juː", "ju"),         # the letter name, a whole-word exception
    ("flu", "fluː", "flu"),
])
def test_word_final_u(word, gb, us):
    assert _t("en-GB", word) == gb
    assert _t("en-US", word) == us


@pytest.mark.parametrize("word, ending", [
    ("guru", "ɹuː"),            # WP: /uː/ after /r/
    ("tofu", "fuː"),            # WP: /uː/ in "hindu, tutu, tofu"
    ("tutu", "tuː"),
    ("shu", "ʃuː"),             # after /ʃ/, the yod is never there
    ("chu", "tʃuː"),
    ("Zhu", "huː"),
])
@pytest.mark.parametrize("code", ["en-GB", "en-US"])
def test_word_final_u_has_no_yod(code, word, ending):
    """Only the final syllable is compared: the vowel before it is a
    separate fact."""
    if code == "en-US":
        ending = ending.replace("ː", "")
    assert _t(code, word).endswith(ending)


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
    ("i've", "aɪv"),            # the rules give it; no exception holds it
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


def test_i_ve_is_left_to_the_rules():
    assert "i've" not in G2P("en-GB").spec.word_exceptions


# ─── detached clitics ─────────────────────────────────────────────────────

@pytest.mark.parametrize("text, clitic", [
    ("they 're here", "ɹ"),     # are → /ɹ/ ('re)
    ("we 've gone", "v"),       # have → /v/ ('ve)
    ("they ’re here", "ɹ"),
])
@pytest.mark.parametrize("code", ["en-GB", "en-US"])
def test_a_detached_clitic_has_no_vowel(code, text, clitic):
    words = G2P(code).transcribe(text).split()
    assert words[1].lstrip("ˈ") == clitic


def test_a_word_in_single_quotes_keeps_its_vowel():
    words = G2P("en-GB").transcribe("he said 'we will'").split()
    assert words[2].lstrip("ˈ") == "wiː"


@pytest.mark.parametrize("word, expected", [
    ("i", "aɪ"),
    ("i’ve", "aɪv"),
    ("is", "ɪz"),
    ("u", "ju"),
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


# ─── rhotic specs ─────────────────────────────────────────────────────────

@pytest.mark.parametrize("code, word, expected", [
    ("en-CA", "are", "ɑːɹ"),
    ("en-CA", "your", "jʊəɹ"),
    ("en-CA", "was", "wʌz"),
    ("en-IE", "are", "ɑːɹ"),
    ("en-IE", "your", "jɔːɹ"),
    ("en-GB-x-scotland", "are", "ɑːɹ"),
    ("en-GB-x-scotland", "your", "jɔːɹ"),
])
def test_a_rhotic_spec_keeps_the_r_of_its_function_words(code, word, expected):
    assert _t(code, word) == expected


@pytest.mark.parametrize("word", ["car", "far"])
@pytest.mark.parametrize("code", ["en-CA", "en-IE", "en-GB-x-scotland"])
def test_the_rhotic_are_is_spelled_like_car(code, word):
    """are takes the vowel and the /r/ the spec writes in car and far."""
    assert _t(code, word).endswith("ɑːɹ")


@pytest.mark.parametrize("word, expected", [
    ("are", "ɑː"),   # AU /ɐː/ is the START vowel, which en-AU writes ɑː (car)
    ("was", "wɒz"),  # AusE /wɔz/ is the LOT vowel, which en-AU writes ɒ (hot)
])
def test_en_au_writes_the_au_values_in_its_own_symbols(word, expected):
    assert _t("en-AU", word) == expected
    assert _t("en-AU", "car") == "kɑː"
    assert _t("en-AU", "hot") == "hɒt"
