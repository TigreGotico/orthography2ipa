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
from orthography2ipa.inventory import emission_inventory, phoneme_inventory, tokenize
from orthography2ipa.registry import get

PAIRS = [("ھ", "ه"), ("ڪ", "ك"), ("ٲ", "أ")]
ARABIC = ["arb", "ar", "ar-SA-x-najd", "ar-SA-x-qassim", "ar-SA-x-hejaz",
          "ar-x-gulf", "ar-EG", "ar-MA"]
# Sizes before this change: a variant that reads its own base can add nothing.
SIZES = {"arb": 226, "ar": 231, "ar-SA-x-najd": 229, "ar-SA-x-qassim": 229,
         "ar-SA-x-hejaz": 233, "ar-x-gulf": 239, "ar-EG": 205, "ar-MA": 197}
# Where these are letters in their own right, with values of their own.
ELSEWHERE = [("ھ", "ckb", "h"), ("ھ", "ur", "ʰ"), ("ٲ", "kas", "əː"), ("ڭ", "ota", "ŋ")]


def _inventory(code):
    spec = get(code)
    return set(phoneme_inventory(spec)) | set(emission_inventory(spec))


def _phones_of(code, grapheme):
    """The segments a spec's reading of one grapheme is built from."""
    spec = get(code)
    out = set()
    for reading in spec.graphemes.get(grapheme, []):
        out.update(tokenize(reading, spec))
    return out


def _reachable_from(code, base):
    """Every phone the spec derives from ONE named letter: its readings, plus the surfaces
    of allophone rules that take those readings as input.

    Naming the base matters. An earlier version asked whether the phone was reachable
    ANYWHERE in the spec, which a planted ⟨چ⟩ → [ʘ] passed because an unrelated /b/ rule
    happened to emit it. The claim each of these PRs makes is narrower: this letter reads
    what THAT letter already yields, directly or through its own allophony — the Najdi
    affricate is a rule on /k/ rather than a reading of ⟨ك⟩, so the rules have to be
    followed to find it.
    """
    spec = get(code)
    direct = _phones_of(code, base)
    out = set(direct)
    for rule in (spec.allophone_rules or ()):
        if rule.surface and set(getattr(rule, "phonemes", ()) or ()) & direct:
            out.update(tokenize(rule.surface, spec))
    return out


#: The letters that exist to write /ɡ/ in Arabic script.
_G_FAMILY = {"گ", "ݣ", "ڨ", "ڭ"}


def _g_rests_only_on_the_family(code):
    """True when every source of /ɡ/ in this spec is one of those letters.

    There the "reachable from ⟨ق⟩" question cannot be asked honestly: ⟨ق⟩ does not yield
    /ɡ/ and the only things that do are the family itself, so any member passes because a
    sibling exists. The family cannot vouch for itself, and the tests exempt such a spec by
    name with the reason rather than let it pass silently.
    """
    spec = get(code)
    sources = {k for k, v in spec.graphemes.items()
               if any("ɡ" in tokenize(r, spec) for r in v)}
    rules = [r for r in (spec.allophone_rules or ())
             if r.surface and "ɡ" in tokenize(r.surface, spec)]
    return bool(sources) and sources <= _G_FAMILY and not rules
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


@pytest.mark.parametrize("variant, base", PAIRS)
def test_the_variant_introduces_no_phone(variant, base):
    """Mirroring already guarantees this; asserted separately so the reason is visible.

    This replaces a total-inventory pin. The total grows whenever any unrelated
    grapheme key adds a multi-segment reading, which o2i declares as an atom, so the
    count could not distinguish a new phone from a new emission and went red on a
    matres-lectionis change that touched none of these letters.
    """
    assert _phones_of("arb", variant) == _phones_of("arb", base)


@pytest.mark.parametrize("letter, code, expected", ELSEWHERE)
def test_the_arabic_reading_does_not_leak_into_specs_that_own_these_letters(letter, code, expected):
    """These are real letters elsewhere, with values Arabic must not overwrite.

    ⟨ھ⟩ forms aspirate digraphs in Urdu and is the plain glottal fricative in Kurdish;
    ⟨ٲ⟩ is a Kashmiri vowel; ⟨ڭ⟩ is the velar nasal its name describes. Mapping them on
    the Arabic base node is only safe while those specs do not inherit from it, and
    nothing in the change itself would tell us if they started to.
    """
    assert expected in get(code).graphemes[letter], f"{code} lost its own {letter}"
