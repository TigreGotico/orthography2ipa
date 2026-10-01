"""⟨ڨ⟩ reads [ɡ] in the Maghrebi specs, and deliberately nowhere else.

The letter is a qāf with three dots. Unlike ⟨گ⟩, whose Unicode name (GAF) states its
function, this character's name describes only its shape and its annotation names only a
variety — so the Unicode chart alone cannot license a reading. Saadane & Habash 2015 §4.1
p.70 supplies the missing half, listing it among the realisations of the MSA ⟨ق⟩ consonant
as *"palatal sound ⟨ڨ⟩ [g]"* for Algerian, Moroccan and Tunisian.

The Saudi and Gulf specs are here for their ABSENCE. The letter does occur in Saudi-labelled
corpus rows, but no source cited anywhere in this repository documents it in Saudi or Gulf
writing, and a reading on corpus frequency alone is the error these specs avoid elsewhere.
"""
import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.inventory import emission_inventory, phoneme_inventory, tokenize
from orthography2ipa.registry import get

READS = ["ar-DZ", "ar-TN", "ar-MA"]
REFUSES = ["ar-SA-x-najd", "ar-SA-x-qassim", "ar-SA-x-hejaz", "ar-x-gulf", "ar", "ar-EG"]

# Sizes before this change: the letter must add no phone anywhere.
SIZES = {"ar-DZ": 205, "ar-TN": 225, "ar-MA": 197}


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
@pytest.mark.parametrize("code", READS)
def test_qaf_with_three_dots_reads_g(code):
    assert "ɡ" in G2P(code).transcribe("بڨب"), code


@pytest.mark.parametrize("code", READS)
def test_g_was_already_this_specs_qaf_reflex(code):
    """Not a new phone — which is why the reading is free."""
    assert "ɡ" in _inventory(code), code


@pytest.mark.parametrize("code", REFUSES)
def test_the_letter_is_not_read_outside_the_maghreb(code):
    """The absence is the claim, and it is the claim most at risk of quiet erosion.

    Saadane & Habash names Algerian, Moroccan and Tunisian and no variety beyond the
    Maghreb. The letter nevertheless occurs in Saudi-labelled rows of our own corpus,
    all of them qāf words — which is exactly the evidence that is NOT sufficient here.
    Mapping it in a Saudi or Gulf spec on that basis would be corpus frequency standing
    in for a source, and it would be invisible once done. It stays unmapped until an
    orthographic source for Saudi or Gulf writing exists, and the letter is therefore
    dropped in those specs: a known defect, not a settled question.
    """
    assert "ڨ" not in get(code).graphemes, code


@pytest.mark.parametrize("code", READS)
def test_the_letter_introduces_no_phone(code):
    """⟨ڨ⟩ reads what ⟨ق⟩ already reads here — the claim the size pins stood in for."""
    if _g_rests_only_on_the_family(code):
        # Stated exemption, not a silent pass: every source of /ɡ/ here is one of
        # ⟨گ ݣ ڨ ڭ⟩, so "reachable from ⟨ق⟩" cannot be asked — ⟨ق⟩ does not yield it and
        # only siblings do. What the reading rests on is the source cited for it, which
        # the notes must carry.
        assert "LOAN GRAPHEME" in get(code).notes, code
        return
    assert _phones_of(code, "ڨ") <= _reachable_from(code, "ق"), code
