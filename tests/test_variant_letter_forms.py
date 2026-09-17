"""⟨ھ⟩ ⟨ڪ⟩ ⟨ٲ⟩ are other ways of writing letters Arabic already has.

They carry no sound of their own here, so each reads exactly what its base letter reads
and no inventory grows. The Unicode names say what they are — HEH DOACHASHMEE, SWASH KAF,
ALEF WITH WAVY HAMZA ABOVE — and the pool says they occur that way in Arabic words,
unanimously if not often.

Two things this file guards that are easy to lose. The readings must MIRROR their base
letters, so a later change to ⟨ه⟩ or ⟨ك⟩ cannot leave the variant behind reading what the
base no longer does. And the mapping must not leak into the specs where these are letters
in their own right with different values.
"""
import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.inventory import emission_inventory, phoneme_inventory
from orthography2ipa.registry import get

PAIRS = [("ھ", "ه"), ("ڪ", "ك"), ("ٲ", "أ")]
ARABIC = ["arb", "ar", "ar-SA-x-najd", "ar-SA-x-qassim", "ar-SA-x-hejaz",
          "ar-x-gulf", "ar-EG", "ar-MA"]
# Sizes before this change: a variant that reads its own base can add nothing.
# The three specs below grew by the readings #1553, #1586 and #980 added
# (ar-EG +16: awiː ajiː awij ajij plus the وي/يو/ية/وة digraph readings;
# ar-x-gulf and ar-SA-x-hejaz +4 each: awiː ajiː awijj ajijj). Verified
# against dev 4afe9f44 as an added-only diff, nothing removed. The
# invariant this file guards is unchanged: a variant letter that reads
# its own base adds nothing of its own.
SIZES = {"arb": 226, "ar": 231, "ar-SA-x-najd": 229, "ar-SA-x-qassim": 229,
         "ar-SA-x-hejaz": 237, "ar-x-gulf": 243, "ar-EG": 221, "ar-MA": 197}
# Where these are letters in their own right, with values of their own.
ELSEWHERE = [("ھ", "ckb", "h"), ("ھ", "ur", "ʰ"), ("ٲ", "kas", "əː"), ("ڭ", "ota", "ŋ")]


def _inventory(code):
    spec = get(code)
    return set(phoneme_inventory(spec)) | set(emission_inventory(spec))


@pytest.mark.parametrize("variant, base", PAIRS)
def test_the_variant_mirrors_its_base_letter(variant, base):
    """The invariant, not just the value.

    Asserting ⟨ھ⟩ reads [h] would pass while ⟨ه⟩ drifted to something else and the two
    silently disagreed about the same letter. This asserts they are the same list.
    """
    g = get("arb").graphemes
    assert g[variant] == g[base], f"{variant} no longer mirrors {base}"


@pytest.mark.parametrize("code", ARABIC)
@pytest.mark.parametrize("variant, base", PAIRS)
def test_every_arabic_spec_reads_the_variant_as_its_base(code, variant, base):
    g2p = G2P(code)
    assert g2p.transcribe("ب" + variant + "ب") == g2p.transcribe("ب" + base + "ب"), code


@pytest.mark.parametrize("code, size", sorted(SIZES.items()))
def test_no_inventory_grew(code, size):
    assert len(_inventory(code)) == size, code


@pytest.mark.parametrize("letter, code, expected", ELSEWHERE)
def test_the_arabic_reading_does_not_leak_into_specs_that_own_these_letters(letter, code, expected):
    """These are real letters elsewhere, with values Arabic must not overwrite.

    ⟨ھ⟩ forms aspirate digraphs in Urdu and is the plain glottal fricative in Kurdish;
    ⟨ٲ⟩ is a Kashmiri vowel; ⟨ڭ⟩ is the velar nasal its name describes. Mapping them on
    the Arabic base node is only safe while those specs do not inherit from it, and
    nothing in the change itself would tell us if they started to.
    """
    assert expected in get(code).graphemes[letter], f"{code} lost its own {letter}"
