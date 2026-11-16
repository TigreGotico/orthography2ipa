"""Belgian Dutch ⟨w⟩ is labial-velar [w].

Source: J. Verhoeven, "Belgian Standard Dutch", *Journal of the
International Phonetic Association* 35(2), 2005, pp. 243-247.

- p. 245: "[w] has a labial-velar articulation rather than labiodental in
  many accents of Netherlandic Dutch."
- p. 244, the word list: "w waːʀ̥ waar 'true'".

Netherlandic Dutch keeps the labiodental: "ʋ wang 'cheek'" (Gussenhoven,
"Dutch", *JIPA* 22, 1992, p. 46).

Before a vowel, ⟨ieuw eeuw uw⟩ give the language's own w as the onset of
the next syllable: "voor een klinker is ew en iw normaal", "rywə naast
ryuə, dywə naast dyuə" (Paardekooper, *ABN-uitspraakgids*, 1987, p. XVIII).
In Belgian Dutch that consonant is [w].

The other segments keep the values the spec states elsewhere.
"""
import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def be():
    return G2P("nl-BE")


@pytest.mark.parametrize("word, ipa", [
    ("wang", "ˈwɑŋ"),
    ("wit", "ˈwɪt"),
    ("wel", "ˈwɛl"),
    ("kwaad", "ˈkwaːt"),
    ("zwak", "ˈzwɑk"),
])
def test_belgian_w_is_labial_velar(be, word, ipa):
    assert be.transcribe(word) == ipa


def test_waar_starts_with_the_labial_velar(be):
    ipa = be.transcribe("waar")
    assert ipa.startswith("ˈwaː")
    assert "ʋ" not in ipa


@pytest.mark.parametrize("word, ipa", [
    ("leeuwen", "ˈleːwən"),
    ("nieuwe", "ˈniwə"),
    ("duwen", "ˈdywən"),
])
def test_ieuw_eeuw_uw_before_a_vowel_give_belgian_w(be, word, ipa):
    assert be.transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("wang", "ˈʋɑŋ"),
    ("leeuwen", "ˈleːʋən"),
])
def test_netherlandic_dutch_keeps_the_labiodental(word, ipa):
    assert G2P("nl-NL").transcribe(word) == ipa
