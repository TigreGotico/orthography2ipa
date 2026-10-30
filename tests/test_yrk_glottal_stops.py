"""Tundra Nenets (`yrk`) — the apostrophe letters that spell the glottal stops.

Tundra Nenets Cyrillic uses two dedicated apostrophe letters for its glottal-
stop phonemes. The contrast is nasalizability, not voicing: the single letter
writes the nasalizable glottal stop and the double letter the non-nasalizable
one (Salminen, *An introduction to the Nenets languages*, Helsinki 2023,
pp. 23, 25-26). This spec renders both as /ʔ/, since the two are told apart
only by sandhi across a word boundary.

Each letter reaches text under several codepoints. Salminen (p. 43) states
that they are properly RIGHT SINGLE QUOTATION MARK (U+2019) and RIGHT DOUBLE
QUOTATION MARK (U+201D) rather than the modifier-letter apostrophes U+02BC /
U+02EE, and names ASCII ' and " among the shapes they are confused with; a
smart-quote substitution adds U+2018 and U+201C at the opening end of a pair.
The engine's tokenizer classifies an undeclared apostrophe-like character as
PUNCTUATION rather than UNKNOWN, so any codepoint the spec omits loses the
phoneme in silence instead of raising a visible error. Every member of the
confusable set is therefore mapped.

Expected values are the /ʔ/ Salminen assigns to the letter, not read back
from the engine.
"""
import pytest

import orthography2ipa as o2i


@pytest.fixture(scope="module")
def yrk():
    return o2i.G2P("yrk")


def strip_stress(s):
    return s.replace("ˈ", "").replace("ˌ", "")


@pytest.mark.parametrize("letter", [
    "ʼ",   # ʼ MODIFIER LETTER APOSTROPHE — the declared glottal-stop letter
    "’",   # ’ RIGHT SINGLE QUOTATION MARK — Salminen's preferred codepoint
    "'",   # ' APOSTROPHE — what a plain keyboard produces
    "‘",   # ‘ LEFT SINGLE QUOTATION MARK — smart quotes, opening end
])
def test_single_glottal_stop_letter_survives(yrk, letter):
    word = "вы" + letter
    result = strip_stress(yrk.transcribe_word(word))
    assert result.endswith("ʔ"), (
        f"glottal-stop letter {letter!r} (U+{ord(letter):04X}) was dropped: "
        f"got {result!r}"
    )


@pytest.mark.parametrize("letter", [
    "ˮ",   # ˮ MODIFIER LETTER DOUBLE APOSTROPHE — the declared letter
    "”",   # ” RIGHT DOUBLE QUOTATION MARK — Salminen's preferred codepoint
    '"',   # " QUOTATION MARK — what a plain keyboard produces
    "“",   # “ LEFT DOUBLE QUOTATION MARK — smart quotes, opening end
])
def test_double_glottal_stop_letter_survives(yrk, letter):
    result = strip_stress(yrk.transcribe_word("вы" + letter))
    assert result.endswith("ʔ"), (
        f"glottal-stop letter {letter!r} (U+{ord(letter):04X}) was dropped: "
        f"got {result!r}"
    )


@pytest.mark.parametrize("word,expected_tail", [
    ("пыдари’", "riʔ"),
    ("пыди’", "diʔ"),
    ("пыдо’", "doʔ"),
])
def test_wikipron_gold_words_keep_final_glottal_stop(yrk, word, expected_tail):
    result = strip_stress(yrk.transcribe_word(word))
    assert result.endswith(expected_tail)
