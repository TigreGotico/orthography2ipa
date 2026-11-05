"""Netherlandic Dutch ⟨g ch⟩ are uvular [χ]; Belgian Dutch keeps velar [ɣ x].

Sources:

- C. Gussenhoven, "Dutch", *Journal of the International Phonetic
  Association* 22(1-2), 1992, pp. 45-47. The consonant chart on p. 45 has one
  dorsal fricative, uvular, with "χ gat 'hole'". The transcription on p. 47
  writes it for ⟨g⟩ and ⟨ch⟩: [fraːχ] vraag, [bəχɔn] begon, [zɪχ] zich,
  [dɪχtər] dichter, [slɛχs] slechts. p. 46: "Voiced obstruents and /ɦ/ do
  not occur in the coda".
- J. Verhoeven, "Belgian Standard Dutch", *JIPA* 35(2), 2005, p. 244:
  "Belgian Dutch has a voiced and voiceless velar fricative: these are absent
  in the Netherlands. The Netherlands has a voiceless uvular fricative which
  does not occur in Belgian Dutch." The word list gives "x xɛil chijl" and
  "ɣ ɣɛil geil".

The other segments keep the values the specs state elsewhere.
"""
import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def nl():
    return G2P("nl-NL")


@pytest.fixture(scope="module")
def be():
    return G2P("nl-BE")


@pytest.mark.parametrize("word, ipa", [
    ("gat", "ˈχɑt"),
    ("goed", "ˈχut"),
    ("gaf", "ˈχɑf"),
    ("dag", "ˈdɑχ"),
    ("zegt", "ˈzɛχt"),
])
def test_netherlandic_g_is_uvular(nl, word, ipa):
    assert nl.transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("zich", "ˈzɪχ"),
    ("macht", "ˈmɑχt"),
    ("slechts", "ˈslɛχts"),
    ("dichter", "ˈdɪχtər"),
])
def test_netherlandic_ch_is_uvular(nl, word, ipa):
    assert nl.transcribe(word) == ipa


def test_netherlandic_sch_is_s_and_uvular(nl):
    assert nl.transcribe("school") == "ˈsχoːl"


def test_coda_obstruent_is_voiceless_before_the_uvular(nl):
    assert nl.transcribe("zandgrond") == "ˈzɑntχrɔnt"


@pytest.mark.parametrize("word, ipa", [
    ("asgat", "ˈɑsχɑt"),
    ("bosgrond", "ˈbɔsχrɔnt"),
])
def test_s_before_g_closes_the_syllable(nl, word, ipa):
    # ⟨s⟩+⟨g⟩ meet across a compound boundary (as-gat, bos-grond), so the
    # first syllable is closed and keeps its lax vowel (Booij 1995, ch. 2).
    # Only ⟨sch⟩ spells the onset /sχ/ (school).
    assert nl.transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("geil", "ˈɣɛil"),
    ("goed", "ˈɣut"),
    ("dag", "ˈdɑx"),
    ("chijl", "ˈxɛil"),
    ("zich", "ˈzɪx"),
    ("school", "ˈsxoːl"),
])
def test_belgian_g_and_ch_are_velar(be, word, ipa):
    assert be.transcribe(word) == ipa


@pytest.mark.parametrize("code", ["nl-NL", "nl-BE"])
def test_one_dorsal_series_per_spec(code):
    out = "".join(G2P(code).transcribe(w) for w in ("gat", "zich", "school", "dag"))
    uvular = "χ" in out
    velar = "ɣ" in out or "x" in out
    assert uvular != velar
    assert uvular == (code == "nl-NL")
