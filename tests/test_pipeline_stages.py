"""The two stage roles of a Pipeline: ``rescore`` inside the word paths, and
``sandhi`` between the words.

Expected values come from the old argument on a second engine, or from a plain
engine that runs without the field.
"""
from dataclasses import replace

import pytest

from orthography2ipa import G2P, Pipeline, get
from orthography2ipa.phonetok import Candidate
from orthography2ipa.plugins import SandhiPlugin
from orthography2ipa.registry import MissingPlugin
from orthography2ipa.rescorer import LatticeRescorer
from orthography2ipa.sentence import SentenceRescorer
from orthography2ipa.types import AllophoneRule, LanguageSpec

CATALAN = "els amics, de casa"

# These tests check that a deprecated G2P argument still works.
OLD_ARGUMENT = pytest.mark.filterwarnings(
    r"ignore:G2P\(\w+=\.\.\.\) is deprecated:DeprecationWarning")


class Promote(LatticeRescorer):
    """Make *grapheme* read as *ipa*."""

    def __init__(self, grapheme, ipa):
        self.grapheme, self.ipa = grapheme, ipa

    def rescore(self, slot, context):
        if slot.grapheme != self.grapheme:
            return slot.candidates
        best = min(c.cost for c in slot.candidates)
        return [Candidate(self.ipa, best - 1.0)] + [
            c for c in slot.candidates if c.ipa != self.ipa]


class Recording(SandhiPlugin):
    """Records what it gets. *rewrite* answers, and the default keeps the words."""

    language_codes = ["ca-x-nord"]

    def __init__(self, rewrite=list):
        self.rewrite = rewrite
        self.calls = []

    def apply(self, words, surfaces, pausal, lang):
        self.calls.append((list(words), list(surfaces), list(pausal), lang))
        return self.rewrite(words)


def plain_beam_spec(*rules):
    return LanguageSpec(code="yy-test", name="Test", family="Test", script="Latin",
                        graphemes={"a": ["a"], "c": ["s", "k"]}, allophones={},
                        allophone_rules=tuple(rules))


@OLD_ARGUMENT
def test_rescore_equals_rescorer_on_the_plain_beam():
    spec = plain_beam_spec()
    rescorer = Promote("c", "k")
    field = G2P("es-ES", spec=spec, pipeline=Pipeline(rescore=(rescorer,)))
    old = G2P("es-ES", spec=spec, rescorer=rescorer)

    assert not field._needs_context_beam
    assert field.transcribe_word("ac") == old.transcribe_word("ac")
    assert field.transcribe_word("ac") != G2P("es-ES", spec=spec).transcribe_word("ac")


@OLD_ARGUMENT
def test_rescore_equals_rescorer_on_the_positional_beam():
    rescorer = Promote("s", "ʃ")
    field = G2P("es-ES", pipeline=Pipeline(rescore=(rescorer,)))
    old = G2P("es-ES", rescorer=rescorer)
    sentence = "las casas"

    assert field._needs_context_beam
    assert field.transcribe(sentence) == old.transcribe(sentence)
    assert field.transcribe(sentence) != G2P("es-ES").transcribe(sentence)
    assert field.word_candidates("casa") == old.word_candidates("casa")


@pytest.mark.parametrize("value", [
    Promote("c", "k"),
    [Promote("c", "k")],
])
def test_rescore_takes_what_rescorer_takes(value):
    spec = plain_beam_spec()
    engine = G2P("es-ES", spec=spec, pipeline=Pipeline(rescore=value))

    assert "k" in engine.transcribe_word("ac")


def test_rescore_refuses_what_is_not_a_rescorer():
    with pytest.raises(TypeError, match="LatticeRescorer"):
        G2P("es-ES", pipeline=Pipeline(rescore=("not a rescorer",)))


def test_rescore_runs_before_the_allophone_rules():
    """The promoted /k/ reaches the rule, and the rule rewrites it to /q/."""
    rule = AllophoneRule(id="KFINAL", phonemes=("k",), surface="q", word_final=True)
    engine = G2P("es-ES", spec=plain_beam_spec(rule),
                 pipeline=Pipeline(rescore=(Promote("c", "k"),)))

    assert engine.transcribe_word("ac") == "aq"


def test_sandhi_runs_after_the_spec_rules_with_spelling_and_pauses():
    plugin = Recording()
    engine = G2P("ca-x-nord", pipeline=Pipeline(sandhi=plugin))

    ipa = engine.transcribe(CATALAN)

    assert plugin.calls == [(G2P("ca-x-nord").transcribe(CATALAN).split(),
                             ["els", "amics", "de", "casa"],
                             [False, True, False, True],
                             "ca-x-nord")]
    assert ipa == G2P("ca-x-nord").transcribe(CATALAN)


def test_sandhi_output_is_the_transcription():
    plugin = Recording(lambda words: [w.upper() for w in words])
    engine = G2P("ca-x-nord", pipeline=Pipeline(sandhi=plugin))

    assert engine.transcribe(CATALAN) == G2P("ca-x-nord").transcribe(CATALAN).upper()


def test_sandhi_runs_when_apply_sandhi_is_false():
    plugin = Recording()
    engine = G2P("ca-x-nord", apply_sandhi=False, pipeline=Pipeline(sandhi=plugin))

    engine.transcribe(CATALAN)

    expected = G2P("ca-x-nord", apply_sandhi=False).transcribe(CATALAN).split()
    assert plugin.calls[0][0] == expected
    assert expected != G2P("ca-x-nord").transcribe(CATALAN).split()


def test_word_methods_do_not_run_sandhi():
    plugin = Recording()

    G2P("ca-x-nord", pipeline=Pipeline(sandhi=plugin)).transcribe_word("casa")

    assert plugin.calls == []


def test_a_sandhi_that_returns_another_length_raises():
    engine = G2P("ca-x-nord", pipeline=Pipeline(
        sandhi=Recording(lambda words: list(words)[:-1])))

    with pytest.raises(ValueError, match="returned 3 words for 4"):
        engine.transcribe(CATALAN)


class Sentence(SentenceRescorer):
    def rescore(self, word, context):
        return word.ipa


@OLD_ARGUMENT
@pytest.mark.parametrize("field, old", [
    ({"rescore": (Promote("c", "k"),)}, {"rescorer": Promote("c", "k")}),
    ({"rescore": (Promote("c", "k"),)}, {"plugins": {"rescore": "anything"}}),
    ({"sandhi": Recording()}, {"sentence_rescorer": Sentence()}),
    ({"sandhi": Recording()}, {"plugins": {"sandhi": "anything"}}),
])
def test_an_old_argument_and_a_field_cannot_both_be_set(field, old):
    with pytest.raises(ValueError, match="pass the field"):
        G2P("es-ES", pipeline=Pipeline(**field), **old)


@pytest.mark.parametrize("stage, field", [
    ("rescore", {"rescore": (Promote("c", "k"),)}),
    ("sandhi", {"sandhi": Recording()}),
])
def test_a_field_stands_in_for_a_spec_named_plugin(stage, field):
    spec = replace(get("es-ES"), plugins={stage: ("not-installed",)})

    with pytest.raises(MissingPlugin):
        G2P("es-ES", spec=spec).transcribe("casa")

    assert G2P("es-ES", spec=spec, pipeline=Pipeline(**field)).transcribe("casa")
