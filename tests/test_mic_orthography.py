"""Mi'kmaq apostrophe and ⟨g⟩ readings.

The Mi'gmaq-Mi'kmaq Online Talking Dictionary (mikmaqonline.org) gives the
pronunciation guides ``a'pi`` -> ``aa·bi``, ``gta'n`` -> ``êk·taan``,
``p'tew`` -> ``bê·dew`` and ``put'p`` -> ``bu·dêp``: an apostrophe lengthens a
preceding vowel and stands for schwa after a consonant, and is never a glottal
stop.  The same source gives ``alug`` -> ``a·luk`` and ``agumegw`` ->
``a·gu·mekw``, and Fidelholtz, J. L. (1968), *Micmac Morphophonemics* (MIT PhD
dissertation), p. 12, states that obstruent voicing is predictable, so ⟨g⟩
and ⟨gw⟩ are the voiceless /k/ and /kʷ/ rather than voiced stops.
"""
import orthography2ipa


def test_apostrophe_lengthens_a_preceding_vowel():
    ipa = orthography2ipa.transcribe("a'pi", "mic")
    assert "aː" in ipa
    assert "ʔ" not in ipa


def test_apostrophe_after_a_consonant_is_schwa():
    ipa = orthography2ipa.transcribe("p'tew", "mic")
    assert ipa.startswith("pə")
    assert "ʔ" not in ipa


def test_final_g_is_voiceless_k():
    assert orthography2ipa.transcribe("alug", "mic").endswith("k")


def test_gw_is_labialised_k():
    assert "kʷ" in orthography2ipa.transcribe("agumegw", "mic")
