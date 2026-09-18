"""In the Maghreb ⟨چ⟩ writes jīm, and reads exactly what ⟨ج⟩ reads.

The letter is the Persian tcheh and elsewhere in these specs it marks an affricate, so
the reading is not obvious from the shape. The corpus settles it: substituting ⟨ج⟩ into
each form finds a plain twin in the same variety two to three times as often as
substituting ⟨ك⟩, and the untwinned remainder are French and English words whose donor
sound is /ʒ/ — blocage, courage, recharge.

This follows ⟨ڢ⟩, which reads what ⟨ف⟩ reads because it is the same letter in another
hand. No phone is added.
"""
import pytest

from orthography2ipa import get
from orthography2ipa.g2p import G2P
from orthography2ipa.inventory import phoneme_inventory

READS = ["ar-TN", "ar-DZ", "ar-MA", "ar-LY"]


@pytest.mark.parametrize("code", READS)
def test_it_reads_what_jim_reads(code):
    """The claim, stated as an equality so it cannot drift from ⟨ج⟩ silently."""
    g = get(code).graphemes
    assert g.get("چ") == g.get("ج") == ["ʒ", "dʒ"], code


@pytest.mark.parametrize("code", READS)
def test_the_letter_reaches_the_output(code):
    assert "ʒ" in G2P(code).transcribe("بچب"), code


@pytest.mark.parametrize("code", READS)
def test_no_phone_is_added(code):
    """⟨ج⟩ already offers both readings, so the letter adds a spelling and not a sound."""
    g = get(code).graphemes
    from_jim = set(g.get("ج") or ())
    assert set(g["چ"]) <= from_jim, code


@pytest.mark.parametrize("code", READS)
def test_the_affricate_is_not_smuggled_in(code):
    """The honest limit. A minority of these words are cheese and challenge, whose donor
    sound is /tʃ/, and they will read [ʒ] here — wrong for those words. /tʃ/ is not in
    this inventory and no source for ⟨چ⟩ in this variety was found, so it must not be
    added as a third reading on frequency alone."""
    assert "tʃ" not in get(code).graphemes["چ"], (
        f"{code}: [tʃ] was added to ⟨چ⟩; that is an inventory claim needing a source")
    assert not any("tʃ" in a for a in phoneme_inventory(get(code))), (
        f"{code}: /tʃ/ entered the inventory")


def test_the_gulf_and_najdi_readings_are_untouched():
    """Where the letter genuinely marks an affricate, it keeps doing so."""
    assert get("ar-x-gulf").graphemes["چ"] == ["tʃ"]
    assert get("ar-SA-x-najd").graphemes["چ"] == ["ts"]
