"""Two letters the Maghrib writes that every Maghrebi spec was dropping.

⟨ݣ⟩ is a borrowed-sound letter and ⟨ڢ⟩ is not one at all — it is fāʾ in the Maghribi hand
— so they are cited separately and scoped differently. ⟨ݣ⟩ goes only where Kew 2003 puts
it, Morocco and Mauritania; ⟨ڢ⟩ goes on the ar-x-maghrebi node because its sources describe
the script tradition and name the region rather than a country.

The absences matter as much as the readings. ⟨ݣ⟩ must NOT spread to the Maghrebi specs Kew
does not name, and U+06AD ARABIC LETTER NG must stay unmapped — the proposal itself warns
that the two are visually identical in initial and medial joined forms, so a reader who
assumes they are interchangeable will map the wrong one.
"""
import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.inventory import emission_inventory, phoneme_inventory, tokenize
from orthography2ipa.registry import get

GAF_READS = ["ar-MA", "ar-MR"]          # Kew 2003 §3 p.5 (Morocco), p.6 (Mauritania)
GAF_REFUSES = ["ar-DZ", "ar-TN", "ar-LY", "ar-x-maghrebi"]
FEH_READS = ["ar-MA", "ar-DZ", "ar-TN", "ar-MR", "ar-LY", "ar-x-maghrebi"]

# Sizes before this change: neither letter may introduce a phone.
SIZES = {"ar-MA": 197, "ar-DZ": 205, "ar-TN": 225, "ar-MR": 225,
         "ar-LY": 227, "ar-x-maghrebi": 193}


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
@pytest.mark.parametrize("code", GAF_READS)
def test_moroccan_gaf_reads_g(code):
    assert "ɡ" in G2P(code).transcribe("بݣب"), code


@pytest.mark.parametrize("code", GAF_REFUSES)
def test_moroccan_gaf_does_not_spread_past_its_source(code):
    """Unmapped in Algeria, Tunisia and Libya — pinning a DEFECT that has a price.

    Kew names Morocco and Mauritania; those three are not in it, and they all have /ɡ/,
    so mapping there would be free and would look harmless. That is why the absence is
    tested rather than left as a decision nobody wrote down.

    But it is not costless. ⟨ݣ⟩ occurs **3,437** times over 2,031 rows of lahgtna's
    judged tree, counted independently by two lanes over its 305 shards: ma 3,042,
    dz 328, tn 61, lb 3, ly 2, sa 1. Refusing it in the three Maghrebi specs below
    drops **391 occurrences** (328 + 61 + 2) in silence.

    An earlier version of this docstring said 3,448 with a breakdown that omitted lb and
    sa and therefore summed to 3,433 — a total that agreed with neither its own parts nor
    the tree. Occurrences are counted as written, diacritics attached, so a form and its
    diacritised variant count apart; that is the convention the ⟨ڭ⟩ entries state and it
    is the one used here. Those varieties more usually write ⟨ڨ⟩ for the same sound and #1592 maps
    that, which is why the loss is tolerable for now and not why it is acceptable
    permanently. Citation-blocked, on the defect list, not settled.
    """
    assert "ݣ" not in get(code).graphemes, code


@pytest.mark.parametrize("code", FEH_READS)
def test_maghribi_feh_reads_f(code):
    assert "f" in G2P(code).transcribe("بڢب"), code


def test_maghribi_feh_is_not_a_borrowed_consonant():
    """It is fāʾ in the Maghribi hand, so it reads what ⟨ف⟩ reads, not a foreign phone."""
    assert get("ar-x-maghrebi").graphemes["ڢ"] == get("ar-x-maghrebi").graphemes.get(
        "ف", ["f"]
    ) or get("ar-x-maghrebi").graphemes["ڢ"] == ["f"]


def test_the_confusable_ng_letter_was_licensed_separately():
    """U+06AD is visually identical to ⟨ݣ⟩ in initial and medial joined forms.

    Kew 2003 says so in the proposal that encoded ⟨ݣ⟩, and both occur in real text.
    Mapping one by assuming it is the other is the mistake that warning exists to
    prevent. This test used to pin U+06AD unmapped; it is mapped now, and what it pins
    instead is that the two were licensed SEPARATELY rather than by assuming identity.

    The evidence differs, which is the whole point. ⟨ݣ⟩ rests on Kew §3 stating the
    form-B kāf with three dots writes /ɡ/ in Morocco, and p.6 extending it to Mauritania
    — which is why ar-MR carries ⟨ݣ⟩. ⟨ڭ⟩ rests on the Moroccan WikiPron gold, where all
    13 rows read [ɡ], plus corpus rows in Morocco, Algeria and Tunisia — which is why
    ar-MR carries NO ⟨ڭ⟩: nothing licenses it there.

    So ar-MR having one and not the other is the assertion. A change that mapped both
    everywhere would look tidier and would mean the letters had been treated as
    interchangeable, which they are not.
    """
    ma = get("ar-MA").graphemes
    assert ma["ݣ"] == ["ɡ"] and ma["ڭ"] == ["ɡ"], "ar-MA should read both"
    mr = get("ar-MR").graphemes
    assert "ݣ" in mr, "ar-MR lost the letter Kew p.6 licenses for it"
    assert "ڭ" not in mr, "ar-MR gained a letter no evidence licenses there"


@pytest.mark.parametrize("code", GAF_READS)
def test_the_gaf_introduces_no_phone(code):
    if _g_rests_only_on_the_family(code):
        # Stated exemption, not a silent pass: every source of /ɡ/ here is one of
        # ⟨گ ݣ ڨ ڭ⟩, so "reachable from ⟨ق⟩" cannot be asked — ⟨ق⟩ does not yield it and
        # only siblings do. What the reading rests on is the source cited for it, which
        # the notes must carry.
        assert "LOAN GRAPHEME" in get(code).notes, code
        return
    assert _phones_of(code, "ݣ") <= _reachable_from(code, "ق"), code


@pytest.mark.parametrize("code", FEH_READS)
def test_the_feh_introduces_no_phone(code):
    """⟨ڢ⟩ is fāʾ in the Maghribi hand, so it reads what ⟨ف⟩ reads."""
    assert _phones_of(code, "ڢ") <= _reachable_from(code, "ف"), code
