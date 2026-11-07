"""Shadda gemination reaches every Arabic-script consonant, not only U+0621–U+064A.

The Perso-Arabic letters that Arabic dialects and the Iranic/Indic specs write —
پ چ ڤ گ and the wider set behind Urdu, Pashto, Kurdish and Balochi — carry shadda
like any other consonant. ``ar-x-gulf`` declares پ and ڤ as integrated loanword
consonants in its own feature list, so a class that cannot see them contradicts
the specs it serves.
"""
import pytest

from orthography2ipa.phonetok import _expand_arabic_gemination

SHADDA = "ّ"
FATHA = "َ"


@pytest.mark.parametrize("letter, name", [
    ("پ", "peh U+067E"),
    ("چ", "tcheh U+0686"),
    ("ڤ", "veh U+06A4"),
    ("گ", "gaf U+06AF"),
    ("ٹ", "tteh U+0679, Urdu"),
    ("ی", "farsi yeh U+06CC"),
])
def test_shadda_geminates_letters_outside_the_basic_block(letter, name):
    word = "ب" + FATHA + letter + SHADDA + FATHA + "ة"
    out = _expand_arabic_gemination(word)
    assert out == word.replace(letter + SHADDA, letter + letter), name
    assert SHADDA not in out, name


@pytest.mark.parametrize("letter", ["ت", "ن", "ي", "و"])
def test_shadda_still_geminates_letters_inside_the_basic_block(letter):
    """The widened class must not lose what the old range already covered."""
    word = "ب" + FATHA + letter + SHADDA + FATHA + "ة"
    out = _expand_arabic_gemination(word)
    assert out == word.replace(letter + SHADDA, letter + letter)
    assert SHADDA not in out


@pytest.mark.parametrize("letter", ["پ", "چ", "ت"])
def test_both_mark_orderings_and_a_bare_shadda(letter):
    doubled = letter + letter
    assert _expand_arabic_gemination(letter + SHADDA + FATHA) == doubled + FATHA
    assert _expand_arabic_gemination(letter + FATHA + SHADDA) == doubled + FATHA
    assert _expand_arabic_gemination(letter + SHADDA) == doubled
