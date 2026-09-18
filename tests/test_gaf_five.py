"""Five more varieties read ⟨گ⟩, and none of them gains a phone for it.

An unmapped letter is deleted without an error, and when it carries a haraka the vowel
survives, so the word comes out well-formed and wrong. These five specs were doing that
to a letter their own judged corpus attests: Yemeni in 1,234 rows, Sudanese in 874,
Algerian 246, Tunisian 57, Palestinian 37.

What the letter writes differs by variety and the phone does not. In Yemeni, Sudanese
and Palestinian it is the qāf reflex — around half the distinct forms have a plain ⟨ق⟩
twin in the same variety and the rest are qāf words whose plain spelling does not happen
to occur. In Algerian and Tunisian it is /ɡ/ in European loans: grimage, gratuit,
négociation, exemple. Either way the reading is [ɡ].
"""
import pytest

from orthography2ipa import get
from orthography2ipa.g2p import G2P
from orthography2ipa.inventory import phoneme_inventory, tokenize

READS = ["ar-YE", "ar-SD", "ar-DZ", "ar-TN", "ar-PS"]


@pytest.mark.parametrize("code", READS)
def test_the_letter_is_declared(code):
    assert get(code).graphemes.get("گ") == ["ɡ"], code


@pytest.mark.parametrize("code", READS)
def test_the_letter_reaches_the_output(code):
    assert "ɡ" in G2P(code).transcribe("بگب"), code


@pytest.mark.parametrize("code", READS)
def test_no_phone_is_added(code):
    """The whole argument. ⟨ق⟩ already offers [ɡ] in each of these, so the letter
    writes a sound the variety already makes; a spec that gained /ɡ/ here would be
    making an inventory claim and would need its own source."""
    spec = get(code)
    from_qaf = {p for reading in (spec.graphemes.get("ق") or ())
                for p in tokenize(reading, spec)}
    assert "ɡ" in from_qaf, (
        f"{code}: ⟨ق⟩ reads {spec.graphemes.get('ق')}, which does not offer [ɡ] — "
        "declaring ⟨گ⟩ here would add a phone and needs an inventory citation")


@pytest.mark.parametrize("code", READS)
def test_the_vowel_is_no_longer_orphaned(code):
    """The damage this repairs: the consonant was dropped and its haraka kept, so
    تگُول came out as a real word with the /ɡ/ missing."""
    out = G2P(code).transcribe("تگُول")
    assert "ɡ" in out, f"{code}: {out!r} still drops the letter"


def test_the_varieties_that_already_read_it_are_untouched():
    """ar-MA and ar-LB declared it before this and must still."""
    for code in ("ar-MA", "ar-LB"):
        assert get(code).graphemes.get("گ") == ["ɡ"], code


def test_a_variety_with_no_evidence_does_not_gain_it():
    """The negative control: this is not a blanket addition to every Arabic spec."""
    assert "گ" not in (get("ar").graphemes or {}), (
        "MSA gained the letter; that is a separate claim with its own source")
