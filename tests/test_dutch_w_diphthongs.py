"""Dutch diphthongs spelt with ⟨w⟩.

Main source: P.C. Paardekooper, *ABN-uitspraakgids*, 2nd rev. ed.,
Antwerpen: Heideland-Orbis, 1987 (first edition 1978).

- The key gives one diphthong for "nou, nauw" (p. VIII): the ⟨w⟩ of ⟨auw⟩
  and ⟨ouw⟩ has no sound of its own. Before a vowel a transitional w is
  heard in nauwe, blauwe, and the guide does not transcribe it (p. XVIII).
- "De lettergroep eeuw/ieuw aan het eind van een woord of van een morfeem
  voor een medeklinker (eeuwfeest, kieuwbreedte) spreek je uit als eu, resp.
  iu. Maar voor een klinker is ew en iw normaal" (p. XVIII).
- Stressed ⟨uw⟩ word-finally or before a consonant is [yu]: "dyu, ryu,
  slyu, sxyu, dyubot". Before a vowel "heeft yw de voorkeur": "rywə naast
  ryuə, dywə naast dyuə" (p. XVIII).
- The w of the guide is labiodental, [ʋ]: "De w is in het ABN een
  liptandklank" (p. XVIII).

Zonneveld & Trommelen, "Egg, onion, ouch! On the representation of Dutch
diphthongs", *Studies in Dutch Phonology*, The Hague: Nijhoff, 1980,
agree: "ou has the spelling variants ouw, au, and auw" (p. 267, note 1),
and the older ⟨aau⟩ merged with them: "first 'aau' and 'au' then 'au' and
'ou'" (p. 267). They give ieuw [iu], eeuw [eu], uw [yu] (p. 268), and
before a vowel nieuw-e ni-wə, leeuw-en le-wə (pp. 276-277).

The vowel letters keep the values the spec states elsewhere: ⟨ou⟩ [ɑu],
⟨ee⟩ [eː], ⟨ie⟩ [i].
"""
import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def nl():
    return G2P("nl-NL")


@pytest.mark.parametrize("word, ipa", [
    ("blauw", "ˈblɑu"),
    ("nauw", "ˈnɑu"),
    ("trouwde", "ˈtrɑudə"),
    ("bouwen", "ˈbɑuən"),
    ("blauwe", "ˈblɑuə"),
    ("blaauw", "ˈblɑu"),
])
def test_the_w_of_ouw_and_auw_has_no_sound(nl, word, ipa):
    assert nl.transcribe(word) == ipa


def test_vrouw_ends_in_the_diphthong(nl):
    ipa = nl.transcribe("vrouw")
    assert ipa.endswith("rɑu")
    assert "ʋ" not in ipa


@pytest.mark.parametrize("word, ipa", [
    ("nieuw", "ˈniu"),
    ("kieuw", "ˈkiu"),
    ("leeuw", "ˈleːu"),
    ("eeuw", "ˈeːu"),
    ("eeuws", "ˈeːus"),
    ("duw", "ˈdyu"),
    ("ruw", "ˈryu"),
    ("duwt", "ˈdyut"),
    ("uw", "ˈyu"),
])
def test_ieuw_eeuw_uw_end_in_a_u_offglide_in_their_syllable(nl, word, ipa):
    assert nl.transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("nieuwe", "ˈniʋə"),
    ("leeuwen", "ˈleːʋən"),
    ("eeuwen", "ˈeːʋən"),
    ("duwen", "ˈdyʋən"),
])
def test_ieuw_eeuw_uw_give_a_consonant_onset_before_a_vowel(nl, word, ipa):
    assert nl.transcribe(word) == ipa
