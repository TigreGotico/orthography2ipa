"""⟨ڨ⟩ reads [ɡ] in the Maghrebi specs, and deliberately nowhere else.

The letter is a qāf with three dots. Unlike ⟨گ⟩, whose Unicode name (GAF) states its
function, this character's name describes only its shape and its annotation names only a
variety — so the Unicode chart alone cannot license a reading. Saadane & Habash 2015 §4.1
p.70 supplies the missing half, listing it among the realisations of the MSA ⟨ق⟩ consonant
as *"palatal sound ⟨ڨ⟩ [g]"* for Algerian, Moroccan and Tunisian.

The Saudi and Gulf specs are here for an absence that is a DEFECT, not a decision. The
letter occurs in genuinely Saudi-labelled rows spelling the [ɡ] reflex of ⟨ق⟩, but no source
in this repository documents ⟨ڨ⟩ in Saudi or Gulf writing — and a reading on corpus
frequency alone is the error these specs avoid elsewhere. The test pins today's behaviour
while the citation is found.
"""
import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.inventory import emission_inventory, phoneme_inventory
from orthography2ipa.registry import get

READS = ["ar-DZ", "ar-TN", "ar-MA"]
REFUSES = ["ar-SA-x-najd", "ar-SA-x-qassim", "ar-SA-x-hejaz", "ar-x-gulf", "ar", "ar-EG"]

# Sizes before this change: the letter must add no phone anywhere.
SIZES = {"ar-DZ": 205, "ar-TN": 225, "ar-MA": 197}


def _inventory(code):
    spec = get(code)
    return set(phoneme_inventory(spec)) | set(emission_inventory(spec))


@pytest.mark.parametrize("code", READS)
def test_qaf_with_three_dots_reads_g(code):
    assert "ɡ" in G2P(code).transcribe("بڨب"), code


@pytest.mark.parametrize("code", READS)
def test_g_was_already_this_specs_qaf_reflex(code):
    """Not a new phone — which is why the reading is free."""
    assert "ɡ" in _inventory(code), code


@pytest.mark.parametrize("code", REFUSES)
def test_the_letter_is_not_read_outside_the_maghreb(code):
    """Unmapped outside the Maghreb — pinning a DEFECT, not a settled absence.

    Saadane & Habash names Algerian, Moroccan and Tunisian and no variety beyond the
    Maghreb, so there is no source here for a Saudi or Gulf reading. That is a statement
    about this repository's sources, not about the world: the letter DOES occur in
    genuinely Saudi-labelled rows — ڨَال، حيوَڨف، هاڨي، وفاڨد، نيڨ، شفڨن, ordinary Saudi
    words in which it spells the [ɡ] reflex of ⟨ق⟩, exactly what ⟨گ⟩ is licensed for in
    those specs. Six such rows were counted by the data lane over 52,406.

    So najd and qassim are citation-blocked, not settled, and a ⟨ڨ⟩ in a Saudi row loses
    its consonant today. This test holds that still while the citation is found; it is
    not a statement that the letter should stay unmapped. What it does prevent is the
    mapping arriving on corpus frequency alone, which would be frequency standing in for
    a source and invisible once done.
    """
    assert "ڨ" not in get(code).graphemes, code


@pytest.mark.parametrize("code, size", sorted(SIZES.items()))
def test_the_inventory_did_not_grow(code, size):
    assert len(_inventory(code)) == size, code
