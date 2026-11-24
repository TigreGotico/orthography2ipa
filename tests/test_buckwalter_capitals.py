"""Buckwalter writes the emphatic and pharyngeal consonants as capitals: case is part of the letter.

A Buckwalter word reads as the Arabic-script word it transliterates.
"""
import pytest

from orthography2ipa import transcribe

CAPITALS_FOLDED = pytest.mark.xfail(
    strict=True, reason="https://github.com/TigreGotico/orthography2ipa/issues/2541")


@pytest.mark.parametrize("buckwalter, arabic", [
    pytest.param("Dar", "ضَر", marks=CAPITALS_FOLDED),
    pytest.param("Sabr", "صَبْر", marks=CAPITALS_FOLDED),
    pytest.param("Tib", "طِب", marks=CAPITALS_FOLDED),
    pytest.param("Hub", "حُب", marks=CAPITALS_FOLDED),
    ("dar", "دَر"),
    ("hub", "هُب"),
])
def test_a_capital_reads_as_its_arabic_letter(buckwalter, arabic):
    assert transcribe(buckwalter, "ar-Latn-x-buckwalt") == transcribe(arabic, "ar")
