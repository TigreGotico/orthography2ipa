"""The Perso-Arabic gaf reads [ɡ] in the specs whose ⟨ق⟩ already does.

The sources are cited in each spec's notes; this file pins the readings and the
one thing a reading like this can get wrong, which is quietly enlarging an
inventory. ``ar`` is here for its ABSENCE: Modern Standard Arabic has no /ɡ/, so
the letter must stay unmapped there, and a change that maps it everywhere would
pass every other assertion in this file.
"""
import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.inventory import emission_inventory, phoneme_inventory
from orthography2ipa.registry import get

READS_GAF = ["ar-SA-x-najd", "ar-SA-x-qassim", "ar-SA-x-hejaz", "ar-x-gulf"]

# Inventory sizes before the gaf key was added, so a reading that introduces a
# phone is caught rather than merely being believed not to.
SIZES = {"ar-SA-x-najd": 229, "ar-SA-x-qassim": 229, "ar-SA-x-hejaz": 233,
         "ar-x-gulf": 239, "ar": 231}


def _inventory(code):
    spec = get(code)
    return set(phoneme_inventory(spec)) | set(emission_inventory(spec))


@pytest.mark.parametrize("code", READS_GAF)
def test_gaf_reads_g(code):
    assert "ɡ" in G2P(code).transcribe("بگب"), code


@pytest.mark.parametrize("code", READS_GAF)
def test_gaf_is_the_reflex_qaf_already_carries(code):
    """Not a new phone: the spec reads ⟨ق⟩ as [ɡ] too, which is why this is free."""
    assert "ɡ" in get(code).graphemes.get("ق", []), code


def test_msa_does_not_read_gaf():
    """``ar`` has no /ɡ/, so the letter is not mapped here — and this pins today's
    behaviour rather than a settled position.

    What the absence costs, measured on ``ar``'s own gold: 2 of the 17,563
    ``ara_arab_broad`` rows are the bare letter ⟨گ⟩, and each transcribes to the
    **empty string**. Inside a word it goes silently — ``بگب`` returns ``ˈbb``
    against ``بفب``'s ``ˈbfb`` — with no error and no placeholder, so nothing
    downstream can tell a dropped phoneme from a shorter word.

    Mapping it would need a phone Modern Standard Arabic does not have, which is why
    this PR does not do it. But an unmapped letter that occurs in this spec's own gold
    is an open defect, not a resolved question: it sits on the o2i defect list above
    ``ar-EG``'s, whose spec has never been shown to need the letter at all. If a later
    change maps ⟨گ⟩ in ``ar``, this test is meant to fail and be revisited on its
    source, not deleted.
    """
    assert "ɡ" not in _inventory("ar")
    assert "گ" not in get("ar").graphemes


@pytest.mark.parametrize("code, size", sorted(SIZES.items()))
def test_the_inventory_did_not_grow(code, size):
    assert len(_inventory(code)) == size, code
