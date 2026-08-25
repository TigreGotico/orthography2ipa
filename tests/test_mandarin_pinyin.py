"""Whole-word transcription pins for Mandarin Pinyin (zh).

Each case is a real Pinyin word in both of the conventions the orthography
is written in — the tone diacritics of the official Scheme and the ASCII
tone digits — and the expected IPA is the one the spec's own stated rules
give, segment by segment, not a value read back from the engine.
"""
import pytest

from orthography2ipa import transcribe
from orthography2ipa.registry import get


# (Pinyin, IPA). Tone letters follow Chao (1968): 55, 35, 214, 51, and
# nothing for the neutral tone.
NUMBERED = [
    # Tone digits are segments of the orthography, not stray numerals.
    ("ma1", "ma˥"),
    ("ma2", "ma˧˥"),
    ("ma3", "ma˨˩˦"),
    ("ma4", "ma˥˩"),
    ("ma5", "ma"),
    ("de", "tɤ"),
    # ⟨u⟩ after ⟨j q x y⟩ is /y/: Pinyin drops the umlaut where /u/ and
    # /y/ do not contrast, and keeps it elsewhere.
    ("qu4", "tɕʰy˥˩"),
    ("xu1", "ɕy˥"),
    ("lu4", "lu˥˩"),
    ("jun1", "tɕyn˥"),
    ("gun3", "kwən˨˩˦"),
    ("quan2", "tɕʰɥɛn˧˥"),
    ("guan1", "kwan˥"),
    ("xue2", "ɕɥe˧˥"),
    ("lv4", "ly˥˩"),
    ("nv3", "ny˨˩˦"),
    # ⟨y w⟩ are the zero-onset spellings of the medials, so these are
    # bare vowels and the ⟨i⟩/⟨ü⟩ rimes, not /j/ or /w/ plus a rime.
    ("yi1", "i˥"),
    ("wu3", "u˨˩˦"),
    ("yu2", "y˧˥"),
    ("ying1", "iŋ˥"),
    ("yin1", "in˥"),
    ("ye4", "je˥˩"),
    ("yan2", "jɛn˧˥"),
    ("yuan2", "ɥɛn˧˥"),
    ("yun2", "yn˧˥"),
    ("wo3", "wo˨˩˦"),
    # ⟨o⟩ after a labial spells the rime /uo/; alone it is the
    # interjection [ɔ].
    ("bo1", "pwo˥"),
    ("mo2", "mwo˧˥"),
    ("mou3", "mou˨˩˦"),
    ("o1", "ɔ˥"),
    # ⟨i⟩ after the two sibilant series is the apical vowel.
    ("zi4", "tsɨ˥˩"),
    ("si3", "sɨ˨˩˦"),
    ("zhi1", "ʈʂɨ˥"),
    ("shi4", "ʂɨ˥˩"),
    ("ri4", "ɻɨ˥˩"),
    ("ni3", "ni˨˩˦"),
    # Prenuclear high vowels are glides.
    ("xian4", "ɕjɛn˥˩"),
    ("jiu4", "tɕjou˥˩"),
    ("duo1", "two˥"),
    ("hao3", "xau˨˩˦"),
    ("dang1", "tɑŋ˥"),
    ("dong1", "tʊŋ˥"),
    ("er2", "ɚ˧˥"),
    # A whole utterance in the corpus shape: syllables run together with
    # the tone digit closing each one.
    ("xian4zai4", "ɕjɛn˥˩tsai˥˩"),
    ("xue2sheng1", "ɕɥe˧˥ʂəŋ˥"),
    ("zai4jian4", "tsai˥˩tɕjɛn˥˩"),
]

#: The same words in the diacritic orthography of the 1958 Scheme.
DIACRITIC = [
    ("mā", "ma˥"),
    ("má", "ma˧˥"),
    ("mǎ", "ma˨˩˦"),
    ("mà", "ma˥˩"),
    ("qù", "tɕʰy˥˩"),
    ("xué", "ɕɥe˧˥"),
    ("nǐ", "ni˨˩˦"),
    ("hǎo", "xau˨˩˦"),
    ("xiànzài", "ɕjɛn˥˩tsai˥˩"),
    ("yī", "i˥"),
    ("wǒ", "wo˨˩˦"),
    ("bō", "pwo˥"),
    ("shì", "ʂɨ˥˩"),
    ("dāng", "tɑŋ˥"),
]


@pytest.mark.linguistic
@pytest.mark.parametrize("word,expected", NUMBERED)
def test_numbered_pinyin(word, expected):
    assert transcribe(word, "zh") == expected


@pytest.mark.linguistic
@pytest.mark.parametrize("word,expected", DIACRITIC)
def test_diacritic_pinyin(word, expected):
    assert transcribe(word, "zh") == expected


@pytest.mark.linguistic
def test_apical_vowel_realizations_are_declared():
    """The apical vowel is written /ɨ/ and both surfaces are stated."""
    assert get("zh").allophones["ɨ"] == ["ɨ", "ɹ̩", "ɻ̩"]


def test_digit_grapheme_is_not_swallowed_by_the_digit_token():
    """A digit a spec maps is a grapheme, not a numeral.

    The Arabic chat alphabet writes ⟨3⟩ for /ʕ/; Riffian declares it, and
    the tokenizer must let the grapheme claim the character the same way
    it lets one claim punctuation.
    """
    assert "ʕ" in transcribe("3ar", "rif")
