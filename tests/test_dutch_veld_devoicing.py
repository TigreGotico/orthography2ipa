"""The coda obstruent of the one-slot graphemes ⟨veld⟩ and ⟨berg⟩ devoices.

Sources:

- C. Gussenhoven, "Dutch", *Journal of the International Phonetic
  Association* 22(1-2), 1992, p. 46: "Voiced obstruents and /ɦ/ do not
  occur in the coda", and "obstruents may be voiced before /b, d/".
- P.C. Paardekooper, *ABN-uitspraakgids*, 1987, the guide for the Belgian
  norm: bergketen bɛr ə xketə, bergplaats bɛr ə xplats (p. 21), gebergte
  gə'bɛr ə xtə (p. 69), veldpost vɛltpɔst, veldslag vɛltslɑx (p. 218).

⟨veld⟩ and ⟨berg⟩ are one grapheme slot each, so NL_CODA_DEVOICE_D and
NL_CODA_DEVOICE_G cannot reach the obstruent. NL_CODA_DEVOICE_VELD and the
nl-BE NL_BE_CODA_DEVOICE_BERG devoice the last segment of the slot. A rule
that named the whole slot value would make that value one segmentation atom,
and the nl-BE-x-antwerp r rules would then no longer see the [v] or [b] that
follows a coda r (Aarveld, Turfberg).
"""
import pytest

from orthography2ipa import G2P


@pytest.mark.parametrize("lang, word, ipa", [
    ("nl-NL", "veldkeuken", "ˈvɛltkøykən"),
    ("nl-NL", "veldslag", "ˈvɛltslɑχ"),
    ("nl-NL", "veldpost", "ˈvɛltpɔst"),
    ("nl-NL", "veldtocht", "ˈvɛltɔχt"),
    ("nl-NL-x-polder", "veldslag", "ˈvɛltslɑχ"),
    ("nl-NL-x-groninge", "veldkeuken", "ˈvɛltkøykən"),
    ("nl-NL-x-limburg", "veldslag", "ˈvɛltslɑx"),
])
def test_veld_devoices_before_a_voiceless_obstruent(lang, word, ipa):
    assert G2P(lang).transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("velden", "ˈvɛldən"),
    ("veldbed", "ˈvɛldbət"),
    ("slagveld", "ˈslaːχvɛlt"),
])
def test_veld_keeps_its_other_values(word, ipa):
    assert G2P("nl-NL").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("veldslag", "ˈvɛltslɑx"),
    ("veldpost", "ˈvɛltpɔst"),
    ("bergtop", "ˈbɛrxtɔp"),
    ("bergketen", "ˈbɛrxkətən"),
    ("gebergte", "ɣəˈbɛrxtə"),
])
def test_belgian_dutch_devoices_veld_and_berg(word, ipa):
    assert G2P("nl-BE").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("velden", "ˈvɛldən"),
    ("veldbed", "ˈvɛldbət"),
    ("bergen", "ˈbɛrɣən"),
    ("berg", "ˈbɛrx"),
])
def test_belgian_dutch_keeps_the_other_values(word, ipa):
    assert G2P("nl-BE").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("veldslag", "ˈvɛltslɑx"),
    ("bergtop", "ˈbɛɾəxtɔp"),
    ("bergketen", "ˈbɛɾəxkətən"),
    ("gebergte", "ɣəˈbɛɾəxtə"),
])
def test_antwerp_devoices_veld_and_berg(word, ipa):
    assert G2P("nl-BE-x-antwerp").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("Aarveld", "ˈaːɾəvɛlt"),
    ("werkveld", "ˈwɛɾəkvɛlt"),
    ("Markvelde", "ˈmɑɾəkvɛldə"),
    ("Turfberg", "ˈtʏɾəfbɛɾəx"),
    ("bergen", "ˈbɛrɣən"),
    ("velden", "ˈvɛldən"),
])
def test_antwerp_keeps_the_r_schwa_before_veld_and_berg(word, ipa):
    assert G2P("nl-BE-x-antwerp").transcribe(word) == ipa
