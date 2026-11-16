"""The two text roles of a Pipeline: ``expand`` writes words out, and ``mark`` adds
marks to the same words.

Expected values come from a plain engine that reads the prepared text directly, or
from a string written by hand.
"""
import unicodedata
from dataclasses import replace

import pytest

from orthography2ipa import G2P, Pipeline, get
from orthography2ipa.registry import MissingPlugin

FORCED = 'o <phoneme ph="ˈɡatu">gato</phoneme> bebe água'

# These tests check that a deprecated G2P argument still works.
OLD_ARGUMENT = pytest.mark.filterwarnings(
    r"ignore:G2P\(\w+=\.\.\.\) is deprecated:DeprecationWarning")
# These tests check that the deprecated spec field still works.
SPEC_FIELD = pytest.mark.filterwarnings(
    r"ignore:the plugins field of the [\w-]+ spec is deprecated:DeprecationWarning")


class Recorder:
    """A stage that records its input and applies *rewrite*."""

    def __init__(self, rewrite=lambda text: text):
        self.rewrite = rewrite
        self.calls = []

    def __call__(self, text):
        self.calls.append(text)
        return self.rewrite(text)


def test_expand_reads_as_the_text_it_writes():
    engine = G2P("pt-PT", pipeline=Pipeline(
        expand=lambda text: text.replace("3", "três")))

    assert engine.transcribe("tenho 3 gatos") == G2P("pt-PT").transcribe("tenho três gatos")


def test_mark_reads_as_the_marked_text():
    engine = G2P("pt-PT", pipeline=Pipeline(
        mark=lambda text: text.replace("sede", "sêde")))

    assert engine.transcribe("tenho sede") == G2P("pt-PT").transcribe("tenho sêde")
    assert engine.transcribe("tenho sede") != G2P("pt-PT").transcribe("tenho sede")


def test_expand_runs_before_mark():
    mark = Recorder(lambda text: text.replace("sede", "sêde"))
    engine = G2P("pt-PT", pipeline=Pipeline(
        expand=lambda text: text.replace("S", "sede"), mark=mark))

    ipa = engine.transcribe("tenho S")

    assert mark.calls == ["tenho sede"]
    assert ipa == G2P("pt-PT").transcribe("tenho sêde")


@OLD_ARGUMENT
def test_mark_runs_once_on_the_sentence_and_normalizer_once_per_run():
    mark, normalizer = Recorder(), Recorder()

    G2P("pt-PT", pipeline=Pipeline(mark=mark)).transcribe(FORCED)
    G2P("pt-PT", normalizer=normalizer).transcribe(FORCED)

    assert mark.calls == ["o gato bebe água"]
    assert normalizer.calls == ["o ", " bebe água"]


def test_expand_runs_on_plain_runs_only():
    expand = Recorder()

    G2P("pt-PT", pipeline=Pipeline(expand=expand)).transcribe(FORCED)

    assert expand.calls == ["o ", " bebe água"]


def test_forced_word_keeps_its_surface_and_plain_words_keep_their_marks():
    engine = G2P("pt-PT", pipeline=Pipeline(
        mark=lambda text: text.replace("gato", "gáto").replace("bebe", "bébe")))

    words = engine.transcribe_detailed(FORCED).words

    assert [w.word for w in words] == ["o", "gato", "bébe", "água"]
    assert words[1].ipa == "ˈɡatu"


def test_a_mark_stage_can_hold_its_own_engine():
    """A model that reads the lattice answers through ``mark``: it asks its own
    engine about each reading and returns the one it picks."""
    own = G2P("pt-PT")

    def mark(text):
        readings = [text.replace("sede", form) for form in ("séde", "sêde")]
        return next(r for r in readings if "e" in own.transcribe(r))

    engine = G2P("pt-PT", pipeline=Pipeline(mark=mark))

    assert engine.transcribe("muita sede") == G2P("pt-PT").transcribe("muita sêde")


@pytest.mark.parametrize("rewrite, named", [
    (lambda text: text.replace("gatos", "gatas"), "'gatos'"),
    (lambda text: text.replace("gatos", "gato"), "'gatos'"),
    (lambda text: text.replace("gatos", "gatos a"), "'pretos'"),
])
def test_a_mark_that_changes_a_word_raises_and_names_it(rewrite, named):
    engine = G2P("pt-PT", pipeline=Pipeline(mark=rewrite))

    with pytest.raises(ValueError, match=named):
        engine.transcribe("tenho gatos pretos")


def test_a_mark_that_changes_spacing_raises():
    engine = G2P("pt-PT", pipeline=Pipeline(
        mark=lambda text: text.replace(" ", "  ")))

    with pytest.raises(ValueError, match="mark stage"):
        engine.transcribe("tenho gatos")


def test_marks_stay_with_their_letters_around_a_forced_word_in_arabic():
    text = 'كتب <phoneme ph="ˈqalam">قلم</phoneme> ولد'
    vocalized = {"كتب": "كَتَبَ", "قلم": "قَلَمٌ", "ولد": "وَلَدٌ"}

    def mark(sentence):
        for bare, marked in vocalized.items():
            sentence = sentence.replace(bare, marked)
        return sentence

    words = G2P("ar", pipeline=Pipeline(mark=mark)).transcribe_detailed(text).words

    assert [w.word for w in words] == ["كَتَبَ", "قلم", "وَلَدٌ"]
    assert words[1].ipa == "ˈqalam"


def test_a_mark_on_the_last_letter_before_a_forced_word_stays_with_that_letter():
    text = 'sede<phoneme ph="a">a</phoneme> b'
    engine = G2P("pt-PT", pipeline=Pipeline(
        mark=lambda sentence: sentence.replace("sedea", "sedéá")))

    words = engine.transcribe_detailed(text).words

    assert words[0].word == "sed\u00e9"
    assert words[1].word == "a"


def test_nfd_marks_align_in_every_chunk():
    decomposed = unicodedata.normalize("NFD", "sêde")
    engine = G2P("pt-PT", pipeline=Pipeline(
        mark=lambda text: text.replace("sede", decomposed)))

    words = engine.transcribe_detailed('sede <phoneme ph="a">a</phoneme> sede').words

    assert [w.word for w in words] == ["sêde", "a", "sêde"]


def test_nfc_input_may_come_back_in_nfd():
    """NFD reads the same letters, so the check accepts it."""
    engine = G2P("pt-PT", pipeline=Pipeline(
        mark=lambda text: unicodedata.normalize("NFD", text)))

    assert engine.transcribe("água") == G2P("pt-PT").transcribe(
        unicodedata.normalize("NFD", "água"))


@pytest.mark.parametrize("call", [
    lambda engine: engine.transcribe_word("sede"),
    lambda engine: engine.word_candidates("sede"),
    lambda engine: engine.ipa_lattice("sede"),
    lambda engine: engine.candidates("sede"),
    lambda engine: engine.word_confidence("sede"),
])
def test_word_methods_run_neither_field(call):
    expand, mark = Recorder(), Recorder()

    call(G2P("pt-PT", pipeline=Pipeline(expand=expand, mark=mark)))

    assert expand.calls == []
    assert mark.calls == []


@OLD_ARGUMENT
def test_a_compound_word_keeps_normalizer_and_runs_neither_field():
    """``transcribe_word`` reads a compound's elements through the word splitter.
    That reaches the old argument, and it does not reach the fields."""
    mark, normalizer = Recorder(), Recorder()

    G2P("pt-PT", pipeline=Pipeline(mark=mark)).transcribe_word("guarda-chuva")
    G2P("pt-PT", normalizer=normalizer).transcribe_word("guarda-chuva")

    assert mark.calls == []
    assert normalizer.calls == ["guarda-chuva"]


def test_sentence_lattice_and_features_read_the_prepared_text():
    def stage():
        return Recorder(lambda text: text.replace("sede", "sêde"))

    mark = stage()
    engine = G2P("pt-PT", pipeline=Pipeline(mark=mark))
    plain = G2P("pt-PT")

    assert ([slot.surface for slot in engine.sentence_lattice("tenho sede").words]
            == [slot.surface for slot in plain.sentence_lattice("tenho sêde").words])
    assert ([w.word for w in engine.features("tenho sede")]
            == [w.word for w in plain.features("tenho sêde")])
    assert mark.calls == ["tenho sede", "tenho sede"]


@OLD_ARGUMENT
@pytest.mark.parametrize("field", ["expand", "mark"])
@pytest.mark.parametrize("old", [
    {"normalizer": str},
    {"plugins": {"normalize": "anything"}},
    {"plugins": {"normalize": ("anything",)}},
])
def test_an_old_argument_and_a_field_cannot_both_be_set(field, old):
    with pytest.raises(ValueError, match="normalizer=.*Pipeline"):
        G2P("pt-PT", pipeline=Pipeline(**{field: str}), **old)


@SPEC_FIELD
@pytest.mark.parametrize("field", ["expand", "mark"])
def test_a_field_stands_in_for_a_spec_named_normalize_plugin(field):
    spec = replace(get("pt-PT"), plugins={"normalize": ("not-installed",)})

    with pytest.raises(MissingPlugin):
        G2P("pt-PT", spec=spec).transcribe("sede")

    engine = G2P("pt-PT", spec=spec, pipeline=Pipeline(**{field: str}))

    assert engine.transcribe("sede") == G2P("pt-PT").transcribe("sede")
