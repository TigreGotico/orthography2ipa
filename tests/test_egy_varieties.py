"""Sa'idi and Bedawi are not Cairene, and the specs say how.

Speech labelled as these two was being transcribed as Cairene, which gets the two most
diagnostic consonants of Arabic dialectology wrong in both, and the interdentals wrong
in one. Each claim below carries a page-cited source in the spec's notes.
"""
import pytest

from orthography2ipa import get
from orthography2ipa.g2p import G2P

SAIDI, BEDAWI, CAIRENE = "ar-EG-x-saidi", "ar-EG-x-bedawi", "ar-EG"


@pytest.mark.parametrize("code", [SAIDI, BEDAWI])
def test_the_spec_loads_and_hangs_off_cairene(code):
    s = get(code)
    assert s.parent == CAIRENE
    assert s.iso639_3 and s.glottolog_code
    assert s.sources, f"{code} has no sources"


@pytest.mark.parametrize("code", [SAIDI, BEDAWI])
def test_qaf_is_g_not_the_cairene_glottal(code):
    """The firmest claim in either spec; every source agrees."""
    assert get(code).graphemes["ق"] == ["ɡ"], code
    assert "ʔ" not in G2P(code).transcribe("قال"), code
    assert "ɡ" in G2P(code).transcribe("قال"), code


@pytest.mark.parametrize("code", [SAIDI, BEDAWI])
def test_jim_is_an_affricate_not_the_cairene_g(code):
    """Cairene reads ⟨ج⟩ as [ɡ], which is what makes it unusual among Arabic dialects.
    Neither of these does."""
    assert get(code).graphemes["ج"][0] == "dʒ", code
    assert get(CAIRENE).graphemes["ج"] == ["ɡ"], "the Cairene contrast moved"


def test_saidi_keeps_the_cairene_interdental_merger():
    """Khalafallah's chart has no interdental row and the lexicon shows the merger, so
    there is no delta to declare and the parent's reading stands."""
    assert get(SAIDI).graphemes["ث"] == get(CAIRENE).graphemes["ث"]


def test_bedawi_retains_the_interdentals():
    """The structural difference, and the reason this cannot be transcribed as
    Egyptian. de Jong 2004:155, with both CA *ḍ and *ẓ falling together as [ðˤ]."""
    g = get(BEDAWI).graphemes
    assert g["ث"] == ["θ"] and g["ذ"] == ["ð"]
    assert g["ظ"] == ["ðˤ"] and g["ض"] == ["ðˤ"], "the *ḍ/*ẓ merger is the cited claim"
    assert "θ" in G2P(BEDAWI).transcribe("ثلاثة")
    assert "t" in G2P(CAIRENE).transcribe("ثلاثة"), "the Cairene contrast moved"


def test_the_palatal_stop_is_not_smuggled_into_saidi():
    """[ɟ] for southern Upper Egyptian is reported by Watson 2002:16 citing Fischer &
    Jastrow, and by Nishio 1994 — neither of which was obtainable. It stays out: adding
    a phone to an inventory on a source nobody has opened is the thing the notes refuse.
    """
    assert "ɟ" not in get(SAIDI).graphemes["ج"]
    assert "Nishio" in get(SAIDI).notes, "the unresolved claim must stay recorded"


def test_cairene_itself_is_untouched():
    c = get(CAIRENE).graphemes
    assert c["ق"] == ["ʔ", "ɡ", "q"] and c["ج"] == ["ɡ"]
