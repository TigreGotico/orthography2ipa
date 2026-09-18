"""⟨چ⟩ reads the affricate each spec actually has, which is not the same affricate.

The letter is Perso-Arabic and writes /tʃ/, but the varieties that spell with it do not
all have /tʃ/. Najdi and Qassimi have the DENTAL affricate [t͡s] — kaskasa — where Gulf has
[t͡ʃ]. Copying one spec's reading into the others is the mistake this file exists to catch,
and it is the mistake that flatters a change: it looks like more specs fixed while writing
the wrong affricate into two varieties whose own sources give the other one.

``ar-SA-x-hejaz`` is here for an absence that is a DEFECT, not a decision: the sources it
holds describe kaf-affrication, and a ⟨چ⟩ there is a loanword question they do not address.
The test pins today's behaviour while the citation is found.
"""
import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.inventory import emission_inventory, phoneme_inventory, tokenize
from orthography2ipa.registry import get

# Inventory sizes before this change, so a reading that introduces a phone is caught
# rather than merely believed absent.
SIZES = {"ar": 231, "ar-SA-x-najd": 229, "ar-SA-x-qassim": 229,
         "ar-SA-x-hejaz": 233, "ar-x-gulf": 239}


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
_G_FAMILY = {"گ", "ݣ", "ڨ", "ڭ", "ګ"}


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
@pytest.mark.parametrize("code, affricate", [("ar-SA-x-najd", "ts"), ("ar-x-gulf", "tʃ")])
def test_tcheh_reads_the_affricate_this_variety_has(code, affricate):
    assert affricate in G2P(code).transcribe("بچب"), code


def test_najdi_does_not_take_the_gulf_affricate():
    """The whole point: [tʃ] is not a Najdi sound and must not arrive with the letter."""
    assert "tʃ" not in _inventory("ar-SA-x-najd")
    assert get("ar-SA-x-najd").graphemes["چ"] == ["ts"]


def test_qassimi_keeps_the_loanword_reading_and_gains_the_native_one():
    """Two cited readings of one letter, and the order is the existing measured one.

    [ʃ] is Alhoody 2019's measured adaptation of English /tʃ/ (Table 9 p.66). [t͡s] is the
    native reflex of ⟨ك⟩. No source measures which dominates in WRITTEN Qassimi, so the
    native reading is appended rather than promoted — this pins that, so a later
    reordering has to arrive with a source.
    """
    assert get("ar-SA-x-qassim").graphemes["چ"] == ["ʃ", "ts"]


def test_hejazi_does_not_read_tcheh():
    """Unmapped in Hejazi, and this pins a DEFECT rather than a cited absence.

    What is cited here answers a different question. Al Mahmoud 2020 pp.62-72 has Hijazi
    keeping [k] where Najdi alternates with [ts], and the spec records "No k→[tʃ]
    Gulf/Najdi affrication" — both findings about kaf-affrication, the native reflex. A
    ⟨چ⟩ in Hijazi text is not that: it is a loanword or a foreign name, and what Hijazi
    does to a borrowed /tʃ/ is a loanword-adaptation question those sources never
    address. Reasoning from the absence of affrication to the absence of a reading
    arrives at the answer by phenomenon instead of by variety.

    Nor does this spec lack the articulation — ⟨ج⟩ reads [dʒ], so [tʃ] and [ʃ] are both
    sayable and what is missing is a source saying which. Borrowing Alhoody's Qassimi
    61.5% across varieties is the inference this file avoids elsewhere.

    So a ⟨چ⟩-spelled Hijazi word loses its consonant today. This test holds that still
    while the citation is found; it is not a statement that the letter should stay
    unmapped.
    """
    assert "چ" not in get("ar-SA-x-hejaz").graphemes
    assert "ts" not in _inventory("ar-SA-x-hejaz")
    assert "tʃ" not in _inventory("ar-SA-x-hejaz")


@pytest.mark.parametrize("code, base", [("ar-SA-x-najd", "ك"), ("ar-x-gulf", "ك")])
def test_the_letter_introduces_no_phone(code, base):
    """The affricate ⟨چ⟩ reads is one ⟨ك⟩ already yields in this spec.

    This replaces a total-inventory pin, which grew when an unrelated matres-lectionis
    key added ``ajiː`` and ``awijj`` and turned the guard red with nothing about the
    affricate changed. o2i declares those sequences as atoms, so no count separates a
    new phone from a new emission; the claim was always the narrower one.
    """
    assert _phones_of(code, "چ") <= _reachable_from(code, base), code
