"""Dhofari carries three sociolects' jīm rather than choosing one.

Davey 2013 table 2.34 documents three coexisting communities on the Dhofar coast that
disagree about ⟨ج⟩: the monolingual coastal group reads [ɡ], the Sheḥri/Mehri-bilingual
mountain-origin group [dʒ], and the Nejd-origin migrants [dʒ] or [j]. Which community a
recording belongs to is a fact about the speaker and not visible in the text, so the
lattice carries all three and audio decides. That is what an allophone list is for.
"""
import pytest

from orthography2ipa import get
from orthography2ipa.g2p import G2P

DHOFARI, OMANI = "ar-OM-x-dhofari", "ar-OM"


def test_it_hangs_off_omani_with_the_right_codes():
    s = get(DHOFARI)
    assert s.parent == OMANI
    assert s.iso639_3 == "adf", "acw is Hejazi, not Dhofari"
    assert s.glottolog_code == "dhof1235"


def test_all_three_sociolect_readings_are_carried():
    """Group 1 first because it is the variety Davey actually describes."""
    assert get(DHOFARI).graphemes["ج"] == ["ɡ", "dʒ", "j"]


def test_the_parent_reading_is_not_silently_dropped():
    """ar-OM reads ⟨ج⟩ as [dʒ]; that is Davey's Group 2 and must survive."""
    assert get(OMANI).graphemes["ج"] == ["dʒ"]
    assert "dʒ" in get(DHOFARI).graphemes["ج"]


def test_qaf_is_inherited_because_the_range_already_matches():
    """Groups 1 and 2 read [q], Group 3 reads [ɡ], and the parent already offers both
    in that order — so declaring it again would add nothing and could drift."""
    assert "ق" not in json_keys(), "⟨ق⟩ was declared on the leaf; the parent already covers it"
    assert get(DHOFARI).graphemes["ق"] == ["q", "ɡ"]


def json_keys():
    import json
    from pathlib import Path
    import orthography2ipa
    p = Path(orthography2ipa.__file__).parent / "data" / "ar-OM-x-dhofari.json"
    return json.loads(p.read_text(encoding="utf-8"))["graphemes"]


def test_the_interdentals_are_inherited_not_restated():
    """Davey p.38 names their retention; the parent already retains them."""
    assert "ث" not in json_keys()
    assert get(DHOFARI).graphemes["ث"] == get(OMANI).graphemes["ث"]


def test_no_phone_is_added():
    """[ɡ] and [j] are both already in the parent, from ⟨ق⟩ and ⟨ي⟩."""
    parent = {p for v in get(OMANI).graphemes.values() for p in v}
    assert set(get(DHOFARI).graphemes["ج"]) <= parent


@pytest.mark.parametrize("word", ["جمل", "جبل"])
def test_the_letter_reaches_the_output(word):
    assert "ɡ" in G2P(DHOFARI).transcribe(word), word


def test_the_iso_code_reaches_the_spec_and_not_a_stub():
    """``adf.json`` was a zero-grapheme ancestry placeholder, and a placeholder wins
    resolution over a spec that merely declares the code. The registry's answer to that
    is an alias plus removing the shadowed file, as it did for ``acm``."""
    s = get("adf")
    assert s.code == DHOFARI
    assert len(s.graphemes) > 100, "resolved to something with no phonology"
