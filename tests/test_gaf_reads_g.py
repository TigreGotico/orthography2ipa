"""The Perso-Arabic gaf reads [ɡ] in the specs whose ⟨ق⟩ already does.

The sources are cited in each spec's notes; this file pins the readings and the
one thing a reading like this can get wrong, which is quietly enlarging an
inventory. ``ar`` is here for its ABSENCE: Modern Standard Arabic has no /ɡ/, so
the letter must stay unmapped there, and a change that maps it everywhere would
pass every other assertion in this file.
"""
import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.inventory import emission_inventory, phoneme_inventory, tokenize
from orthography2ipa.registry import get

READS_GAF = ["ar-SA-x-najd", "ar-SA-x-qassim", "ar-SA-x-hejaz", "ar-x-gulf"]

# Inventory sizes before the gaf key was added, so a reading that introduces a
# phone is caught rather than merely being believed not to.
SIZES = {"ar-SA-x-najd": 229, "ar-SA-x-qassim": 229, "ar-SA-x-hejaz": 233,
         "ar-x-gulf": 239, "ar": 231}


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


@pytest.mark.parametrize("code", READS_GAF)
def test_the_letter_introduces_no_phone(code):
    """What the size pins were standing in for, said directly.

    They asserted a TOTAL, which grows whenever any unrelated grapheme key adds a
    multi-segment reading — ``ajiː`` and ``awijj`` arrived from a matres-lectionis PR
    and turned these red while nothing about gaf had changed. o2i declares such
    sequences as atoms, so no count can separate "a new phone" from "a new emission".
    The claim was always narrower: this letter reads what ⟨ق⟩ already reads here.
    """
    if _g_rests_only_on_the_family(code):
        # Stated exemption, not a silent pass: every source of /ɡ/ here is one of
        # ⟨گ ݣ ڨ ڭ⟩, so "reachable from ⟨ق⟩" cannot be asked — ⟨ق⟩ does not yield it and
        # only siblings do. What the reading rests on is the source cited for it, which
        # the notes must carry.
        assert "LOAN GRAPHEME" in get(code).notes, code
        return
    assert _phones_of(code, "گ") <= _reachable_from(code, "ق"), code
