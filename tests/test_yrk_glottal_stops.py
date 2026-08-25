"""Tundra Nenets (`yrk`) — the apostrophe letters that spell the glottal stops.

Tundra Nenets Cyrillic uses two dedicated apostrophe letters for its glottal-
stop phonemes (Salminen 1997): the single ⟨ʼ⟩ (U+02BC MODIFIER LETTER
APOSTROPHE) and the doubled ⟨ˮ⟩ (U+02EE MODIFIER LETTER DOUBLE APOSTROPHE),
both realised as /ʔ/ in this spec (the voiced/nasalised vs. voiceless glottal
distinction is not separated). The WikiPron gold source also renders the
single glottal-stop letter with the typographic right single quotation mark
⟨’⟩ (U+2019) in a minority of entries; the engine's tokenizer classifies an
undeclared apostrophe-like character as PUNCTUATION rather than UNKNOWN, so a
spec that only maps U+02BC silently drops the phoneme for those words instead
of surfacing a visible error.

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
    "’",   # ’ RIGHT SINGLE QUOTATION MARK — WikiPron's typographic variant
])
def test_single_glottal_stop_letter_survives(yrk, letter):
    word = "вы" + letter
    result = strip_stress(yrk.transcribe_word(word))
    assert result.endswith("ʔ"), (
        f"glottal-stop letter {letter!r} (U+{ord(letter):04X}) was dropped: "
        f"got {result!r}"
    )


def test_double_glottal_stop_letter_survives(yrk):
    result = strip_stress(yrk.transcribe_word("выˮ"))
    assert result.endswith("ʔ")


@pytest.mark.parametrize("word,expected_tail", [
    ("пыдари’", "riʔ"),
    ("пыди’", "diʔ"),
    ("пыдо’", "doʔ"),
])
def test_wikipron_gold_words_keep_final_glottal_stop(yrk, word, expected_tail):
    result = strip_stress(yrk.transcribe_word(word))
    assert result.endswith(expected_tail)
