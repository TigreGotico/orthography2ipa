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


#: The interjection syllables. ⟨ê⟩ is the final ㄝ /ɛ/ spelled alone, as the
#: third note to the Scheme's table of finals directs; ⟨ng hng hm⟩ have no
#: vowel letter at all and read /ŋ xŋ xm/, the last two toneless (Lee 2023,
#: from the seventh edition of the 现代汉语词典).
INTERJECTIONS = [
    ("ê", "ɛ"),
    ("ê1", "ɛ˥"),
    ("ê2", "ɛ˧˥"),
    ("ê3", "ɛ˨˩˦"),
    ("ê4", "ɛ˥˩"),
    ("ê̄", "ɛ˥"),
    ("ế", "ɛ˧˥"),
    ("ê̌", "ɛ˨˩˦"),
    ("ề", "ɛ˥˩"),
    ("ng", "ŋ"),
    ("ńg", "ŋ˧˥"),
    ("ňg", "ŋ˨˩˦"),
    ("ǹg", "ŋ˥˩"),
    ("hng", "xŋ"),
    ("hm", "xm"),
    ("m", "m"),
    ("ḿ", "m˧˥"),
    ("m̀", "m˥˩"),
    ("n", "n"),
]


@pytest.mark.linguistic
@pytest.mark.parametrize("word,expected", INTERJECTIONS)
def test_interjection_syllables(word, expected):
    assert transcribe(word, "zh") == expected


@pytest.mark.linguistic
def test_e_circumflex_is_not_deleted():
    """⟨ê⟩ is a letter of the orthography, so it must reach the output.

    A missing grapheme entry is dropped without an error, which turns a
    whole syllable into the empty string and hides the gap.
    """
    assert transcribe("ê", "zh") != ""


@pytest.mark.linguistic
def test_syllabic_nasal_is_not_read_letter_by_letter():
    """⟨ng⟩ is one syllable, not ⟨n⟩ followed by ⟨g⟩."""
    assert "k" not in transcribe("ng", "zh")
    assert "k" not in transcribe("hng", "zh")


# `phonemes` is the inventory of single sounds. A final such as /an/ or a
# whole syllable such as /pʰou/ in it becomes one atom when the list is
# passed to the syllabifier: /ana/ turns into one syllable and /pʰou/ into a
# syllable with no nucleus. The syllable is CGVX (Duanmu 2005): a full
# syllable with a diphthong or a nasal coda is heavy.
_ZH_SYLLABLES = [
    ("ana", ["a", "na"], ["light", "light"]),
    ("pan", ["pan"], ["heavy"]),
    ("pai", ["pai"], ["heavy"]),
    ("mou", ["mou"], ["heavy"]),
    ("pʰoupʰou", ["pʰou", "pʰou"], ["heavy", "heavy"]),
    ("wanwan", ["wan", "wan"], ["heavy", "heavy"]),
    ("atsʰa", ["a", "tsʰa"], ["light", "light"]),
]


@pytest.mark.linguistic
@pytest.mark.parametrize("ipa,syllables,weights", _ZH_SYLLABLES)
def test_phonemes_as_atoms_give_cgvx_syllables(ipa, syllables, weights):
    from orthography2ipa.stress import syllabify_ipa, syllable_weight
    atoms = list(get("zh").phonemes)
    got = syllabify_ipa(ipa, 1, atoms)
    assert got == syllables
    assert [syllable_weight(s, atoms) for s in got] == weights


@pytest.mark.linguistic
@pytest.mark.parametrize("code", ["zh", "zh-Hani"])
def test_phonemes_hold_no_vowel_next_to_another_segment(code):
    from orthography2ipa.allophony import segment_ipa
    from orthography2ipa.vowels import is_ipa_vowel
    phonemes = get(code).phonemes
    atoms = sorted((p for p in phonemes if len(p) > 1), key=len, reverse=True)
    for phoneme in phonemes:
        segments = segment_ipa(phoneme, atoms)
        assert segments == [phoneme], f"{phoneme} is {segments}, not one segment"
        if any(is_ipa_vowel(c) for c in phoneme):
            assert len(phoneme.rstrip("̩")) == 1, f"{phoneme} is not one vowel"
