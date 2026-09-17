"""A borrowed consonant is read, not deleted — as the phone each spec actually has.

The base table had no entry for پ چ ڤ گ ڨ ڢ ݣ ھ, so a word containing one came back
with the consonant absent: بچت read as bt. Every Arabic spec inherits graphemes from
arb, so every one of them dropped these letters, including ar-x-gulf, whose own notes
name پ and ڤ as integrated consonants.

The base reads each as the substitute MSA has, not as the foreign phone. The inventory
is DERIVED from the graphemes, so mapping پ to [p] in arb would add /p/ to Modern
Standard Arabic, and a phone outside a spec's inventory has no embedding at synthesis
time — the word carrying it is mispronounced silently. The foreign phone belongs to the
specs whose phonology has it, and those already declare it.
"""
import pytest

from orthography2ipa import G2P
from orthography2ipa.inventory import phoneme_inventory

TABLES = ["ar", "ar-SA-x-najd", "ar-SA-x-qassim", "ar-SA-x-hejaz", "ar-x-gulf"]
#: letter, the substitute MSA reads it as
NATIVE = [("پ", "b"), ("چ", "ʃ"), ("ڤ", "f"), ("گ", "k"),
          ("ڨ", "q"), ("ڢ", "f"), ("ݣ", "k"), ("ھ", "h")]
#: a spec whose phonology has the foreign phone, and what it must read
FOREIGN = [("ar-x-gulf", "پ", "p"), ("ar-x-gulf", "چ", "tʃ"),
           ("ar-x-gulf", "ڤ", "v"), ("ar-x-gulf", "گ", "ɡ"),
           ("ar-EG", "چ", "ʒ"), ("ar-MA", "گ", "ɡ")]
#: phones Modern Standard Arabic does not have and must not acquire from a grapheme
NOT_MSA = ["p", "tʃ", "v", "ɡ"]


def _inner(g2p, letter):
    """What the letter contributes between a fixed b_t frame."""
    out = g2p.transcribe("ب" + letter + "ت").lstrip("ˈ")
    assert out.startswith("b") and out.endswith("t"), out
    return out[1:-1]


def test_the_frame_itself_is_read():
    """Guards the probe: if بات stops reading, every assertion below is vacuous."""
    assert G2P("ar").transcribe("بات").lstrip("ˈ") == "baːt"


@pytest.mark.parametrize("letter, native", NATIVE)
def test_a_borrowed_consonant_is_never_silent(letter, native):
    assert _inner(G2P("ar"), letter) == native


@pytest.mark.parametrize("letter, _native", NATIVE)
@pytest.mark.parametrize("table", TABLES)
def test_no_arabic_table_deletes_it(table, letter, _native):
    assert _inner(G2P(table), letter) != "", f"{letter} is silent under {table}"


@pytest.mark.parametrize("table, letter, phone", FOREIGN)
def test_a_spec_whose_phonology_has_the_phone_still_reads_it(table, letter, phone):
    """The base substitute must not shadow a spec's own, more specific reading."""
    assert _inner(G2P(table), letter) == phone


@pytest.mark.parametrize("phone", NOT_MSA)
def test_the_msa_inventory_does_not_grow(phone):
    """The inventory is derived from the graphemes, so a foreign reading in arb would
    add the phone to MSA — which g2p refuses for forced IPA, and which would silently
    widen the phone set every downstream consumer of `ar` builds from."""
    assert phone not in phoneme_inventory(G2P("ar").spec)


@pytest.mark.parametrize("letter, _native", NATIVE)
def test_the_letter_is_not_read_as_nothing_anywhere_it_is_declared(letter, _native):
    """Catches the shape of the original defect rather than its instances."""
    for table in TABLES + ["ar-EG", "ar-MA", "xaa"]:
        assert _inner(G2P(table), letter) != "", (table, letter)
