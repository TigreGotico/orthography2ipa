"""A plural keeps the stress of its singular, whichever syllabifier runs.

The expected place of the mark is the first sound of the stressed syllable.
It comes from these sources:

* Infopédia marks distribuidor and atribuidor [ˈdor], distribuidora [ˈdorɐ] and
  bueiro [ˈbwɐjru]. A plural in ⟨-s⟩ has the stress of the singular.
* Acordo Ortográfico 1990, Base IX, 1.º: a paroxytone has no written accent.
  This covers construidoras and osteointegradas, which Infopédia does not list.

The written accent of Catalan lingüístics and aqüífers names the stressed vowel,
and ⟨ü⟩ reads as a glide before it, so the same loss stands before the stress.

The tests read the mark only. The vowels and the glides have their own tests.

A shorter transcription that lost its syllable after the stress keeps the count
from the start. Infopédia marks diabo [ˈdjabu], and Base IX, 1.º makes teatro,
havaiano and coiote paroxytones. So the stressed vowel of these words follows
the hiatus or the glide, and pt-PT-x-alentejo drops the final vowel of each.
Schultink (1976: 475) gives ver- and be- as prefixes with
no stress, so Dutch vertrouwen and betrouwen stress [trɑu].

The silabificador division dis-tri-bu-i-do-ras counts more syllables than the
transcription has. The bundled splitter gives dis-tri-bui-do-ras, which matches.
So one word exercises two paths through `apply_stress_mark`, and the
syllabifier plugin contract requires the two paths to agree. Each path reaches
the engine through `Pipeline`, so discovery never picks the syllabifier.

Infopédia has jérsei [ˈʒɛrsɐj], the Portuguese spelling of jersey: stress on the
first syllable and a falling diphthong in the last. pt-PT has [ej] for ⟨ei⟩, and
the library writes [ɾ], so the value is [ˈʒɛɾsej]. The ⟨y⟩ of jersey reads as a
nucleus, so both paths are wrong, in different ways. A strict xfail holds the
right value.
"""
from typing import List, Optional

import pytest

from orthography2ipa import G2P, Pipeline
from orthography2ipa.stress import _lost_after_stress
from orthography2ipa.syllabifier_plugin import SyllabifierPlugin
from orthography2ipa.syllabifiers import SilabificadorSyllabifier

LANGS = ["pt-BR", "pt-PT"]


class BundledSplitter(SyllabifierPlugin):
    """Refuses every word, so the engine falls to the bundled splitter."""

    def syllabify(self, word: str, lang: Optional[str] = None) -> List[str]:
        raise ValueError("cannot split")

    @property
    def language_codes(self) -> List[str]:
        return []


@pytest.fixture(params=[BundledSplitter, SilabificadorSyllabifier],
                ids=["bundled_splitter", "silabificador_plugin"])
def pipeline(request) -> Pipeline:
    return Pipeline(syllabifier=request.param())


def reading(word: str, lang: str, pipeline: Optional[Pipeline] = None) -> str:
    engine = G2P(lang, expose_ambiguous_endings=False, pipeline=pipeline)
    return engine.transcribe_word(word)


def stressed_syllable(word: str, lang: str, pipeline: Optional[Pipeline] = None) -> str:
    return reading(word, lang, pipeline).partition("ˈ")[2]


@pytest.mark.parametrize("lang", LANGS)
@pytest.mark.parametrize("word, onset", [
    ("distribuidoras", "d"),
    ("distribuidores", "d"),
    ("construidoras", "d"),
    ("atribuidores", "d"),
    ("bueiros", "bw"),
    ("osteointegradas", "ɡ"),
])
def test_a_plural_stays_paroxytone(pipeline, word, onset, lang):
    assert stressed_syllable(word, lang, pipeline).startswith(onset)


@pytest.mark.parametrize("word, onset", [
    ("lingüístics", "ʒw"),
    ("aqüífers", "kw"),
])
def test_a_catalan_written_accent_keeps_the_mark(word, onset):
    assert stressed_syllable(word, "ca").startswith(onset)


@pytest.mark.parametrize("word, onset", [
    ("teatro", "a"),
    ("diabo", "a"),
    ("havaiano", "j"),
    ("coiote", "j"),
])
def test_an_apocope_keeps_the_mark(pipeline, word, onset):
    assert stressed_syllable(word, "pt-PT-x-alentejo", pipeline).startswith(onset)


@pytest.mark.parametrize("word", ["vertrouwen", "betrouwen"])
def test_a_dutch_apocope_keeps_the_mark(word):
    assert stressed_syllable(word, "nl-BE").startswith("tr")


@pytest.mark.parametrize("ipa, syllables, ipa_syllables, stress_index, lost_after", [
    # The site u|e stands at the stress of bu-ei-ros.
    ("bwejɾus", ["bu", "ei", "ros"], ["bwej", "ɾus"], 1, False),
    # The site a|in stands after the stress of ca-ba-in.
    ("kabajn", ["ca", "ba", "in"], ["ka", "bajn"], 1, True),
    # Two syllables are gone and one site can explain only one of them.
    ("abks", ["a", "ba", "i", "kes"], ["abks"], 3, True),
    # bu|i merged and do|u did not, so the mark on do counts from the end.
    ("bujdoutas", ["bu", "i", "do", "u", "tas"], ["buj", "do", "u", "tas"], 2, False),
    # The final vowel of te-a-tro is gone and the hiatus e|a stays.
    ("tɨatɾ", ["te", "a", "tro"], ["tɨ", "atɾ"], 1, True),
    # The hiatus u|e of re-du-ei-xin stays: [ə] opens a syllable.
    ("rəðuəʃjn", ["re", "du", "ei", "xin"], ["rə", "ðu", "əʃjn"], 2, True),
    # [j] opens the syllable of ⟨a⟩, so vai|a did not merge and the final vowel
    # of ha-vai-a-no is what is gone.
    ("ɐvajan", ["ha", "vai", "a", "no"], ["ɐ", "va", "jan"], 2, True),
    # Two sites merged and one syllable is missing: the count does not add up.
    ("bwejɾutus", ["bu", "e", "i", "ros"], ["bwej", "ɾu", "tus"], 3, True),
    # No site at all: ver-trou-wen.
    ("vərtrɑuən", ["ver", "trou", "wen"], ["vər", "trɑuən"], 1, True),
])
def test_where_the_transcription_lost_a_syllable(
        ipa, syllables, ipa_syllables, stress_index, lost_after):
    assert _lost_after_stress(ipa, syllables, ipa_syllables, stress_index) is lost_after


@pytest.mark.xfail(strict=True, reason="⟨y⟩ reads as a nucleus, not as the "
                   "glide of jérsei [ˈʒɛrsɐj]")
def test_jersey_reads_as_jersei(pipeline):
    assert reading("jersey", "pt-PT", pipeline) == "ˈʒɛɾsej"
