"""The unstressed Dutch suffix ⟨-(e)lijk⟩ has a schwa: [ələk].

Source: M. Trommelen & W. Zonneveld, "Schappelijke woorden", *De Nieuwe
Taalgids* 85, 1992, p. 115: "zoals bekend is dit suffix fonetisch -ələk".

Each expected form below agrees with its WikiPron row in the vowel of
⟨lijk⟩: vriendelijk [vrindələk], eigenlijk [ɛi̯ɣənlək], gelijk [ɣəlɛi̯k],
lijk [lɛi̯k], blijk [blɛi̯k]. The rest of each form is the spec's own reading.
"""
import pytest

from orthography2ipa import G2P


@pytest.mark.parametrize("lang, word, ipa", [
    ("nl-NL", "vriendelijk", "ˈvrindələk"),
    ("nl-NL", "eigenlijk", "ˈɛiχənlək"),
    ("nl-NL", "mogelijke", "ˈmouχələkə"),
    ("nl-BE", "vriendelijk", "ˈvrindələk"),
    ("nl-BE", "eigenlijk", "ˈɛiɣənlək"),
    ("nl-NL-x-polder", "eigenlijk", "ˈaːiχənlək"),
])
def test_unstressed_lijk_has_a_schwa(lang, word, ipa):
    assert G2P(lang).transcribe(word) == ipa


@pytest.mark.parametrize("lang, word, ipa", [
    ("nl-NL", "gelijk", "χəˈlɛik"),
    ("nl-NL", "lijk", "ˈlɛik"),
    ("nl-NL", "blijk", "ˈblɛik"),
    ("nl-NL-x-polder", "gelijk", "χəˈlaːik"),
])
def test_stressed_lijk_keeps_its_diphthong(lang, word, ipa):
    assert G2P(lang).transcribe(word) == ipa
