"""The host hooks of the IR interpreter.

Each runtime step a caller passes runs around the interpreter: a normalize
plugin, a rescorer, a syllabifier, a sandhi plugin, a sentence rescorer, a
forced word, a caller spec and ``expose_ambiguous_endings=False``. Each test
checks that the engine has an interpreter, that the output equals the rules
engine's recorded output (``tests/frozen_rules.py``), and that the hook
changed the output the way an independent computation says it should.
"""
import warnings
from dataclasses import replace

import pytest

from orthography2ipa import G2P, Pipeline, registry
from orthography2ipa.ir import cache
from orthography2ipa.ir.interpreter import Interpreter
from orthography2ipa.phonetok import Candidate
from orthography2ipa.plugins import SandhiPlugin
from orthography2ipa.rescorer import LatticeRescorer
from orthography2ipa.sentence import SentenceRescorer
from tests.frozen_rules import FrozenRules

TEXT = "O rapaz comeu as maçãs, e a avó dormiu."


def ir(code, **kw):
    """An engine on the IR route."""
    g = G2P(code, **kw)
    assert isinstance(g._interpreter, Interpreter)
    return g


def both(code, text, **kw):
    """The IR output of *text*, checked against the rules engine, with warnings off."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        got = ir(code, **kw).transcribe_detailed(text, search="beam")
        want = FrozenRules(code, **kw).transcribe_detailed(text, search="beam")
    assert got.ipa == want.ipa
    assert [(w.word, w.ipa, w.confidence) for w in got.words] == \
        [(w.word, w.ipa, w.confidence) for w in want.words]
    assert [[c.ipa for c in w.candidates] for w in got.words] == \
        [[c.ipa for c in w.candidates] for w in want.words]
    return got.ipa


class _Theta(LatticeRescorer):
    """Every ⟨t⟩ reads [θ]."""

    def rescore(self, slot, context):
        if slot.grapheme == "t":
            return [Candidate("θ", 0.0)]
        return slot.candidates


class _DropFinalO(LatticeRescorer):
    """A word-final ⟨o⟩ is silent."""

    def rescore(self, slot, context):
        if slot.grapheme == "o" and context.index == len(context.slots) - 1:
            return []
        return slot.candidates


def test_rescorer_runs_on_the_ir_route():
    out = both("pt-PT", "o gato do Tomás", pipeline=Pipeline(rescore=(_Theta(),)))
    assert out == G2P("pt-PT").transcribe("o gato do Tomás").replace("t", "θ")


def test_rescorer_deletes_a_slot():
    out = both("pt-PT", "gato", pipeline=Pipeline(rescore=(_DropFinalO(),)))
    assert not out.endswith("u")


def test_rescorer_cost_round_trips_through_micro_units():
    class Promote(LatticeRescorer):
        def rescore(self, slot, context):
            return [Candidate(c.ipa, c.cost + 0.25) for c in slot.candidates]

    out = both("es-ES", "el perro de Ramón", pipeline=Pipeline(rescore=(Promote(),)))
    assert out == G2P("es-ES").transcribe("el perro de Ramón")


class _CaMelo:
    """Splits ``camelo`` as ca|melo, every other word as the bundled splitter.
    The stressed syllable is then ``ca``, and the ⟨e⟩ of ``melo`` is an
    unstressed vowel."""

    def syllabify(self, word, lang):
        return ["ca", "melo"] if word == "camelo" else None


def test_syllabifier_runs_on_the_ir_route():
    out = both("pt-PT", "o camelo", pipeline=Pipeline(syllabifier=_CaMelo()))
    assert G2P("pt-PT").transcribe("o camelo").split()[1] == "kɐˈmɛlu"
    assert out.split()[1] == "kɐˈmɨlu"


class _Tag(SandhiPlugin):
    """Appends ``|`` to every word that is not before a pause."""

    def apply(self, words, surfaces, pausal, lang):
        return [w + ("" if p else "|") for w, p in zip(words, pausal)]

    @property
    def language_codes(self):
        return ["pt-PT"]


def test_sandhi_plugin_runs_after_the_ir_sandhi():
    out = both("pt-PT", TEXT, pipeline=Pipeline(sandhi=_Tag()))
    plain = G2P("pt-PT").transcribe(TEXT).split()
    tagged = out.split()
    assert [w.rstrip("|") for w in tagged] == plain
    pausal = {4, len(plain) - 1}  # "maçãs," and the last word
    assert [w.endswith("|") for w in tagged] == [i not in pausal for i in range(len(plain))]


def test_sandhi_plugin_that_changes_the_word_count_raises():
    class Drop(SandhiPlugin):
        def apply(self, words, surfaces, pausal, lang):
            return words[1:]

        @property
        def language_codes(self):
            return ["pt-PT"]

    with pytest.raises(ValueError):
        ir("pt-PT", pipeline=Pipeline(sandhi=Drop())).transcribe("o gato")


class _Upper(SentenceRescorer):
    def rescore(self, word, context):
        return context.this_word_ipa.upper() if word.index == 0 else context.this_word_ipa


def test_sentence_rescorer_runs_on_the_ir_route():
    out = both("es-ES", "el perro de Ramón", sentence_rescorer=_Upper())
    assert out.split()[0] == G2P("es-ES").transcribe("el").upper()


def test_normalize_plugin_runs_on_the_ir_route(monkeypatch):
    class Swap:
        def normalize(self, text, lang):
            return text.replace("rapaz", "menino")

    monkeypatch.setitem(registry._declared, "normalize", {"swap": Swap()})
    out = both("pt-PT", "o rapaz", plugins={"normalize": "swap"})
    assert out == G2P("pt-PT").transcribe("o menino")


def test_normalizer_does_not_see_a_forced_word():
    forced = 'o rapaz e o <phoneme ph="ʁɐˈpaʃ">rapaz</phoneme>'
    out = both("pt-PT", forced, normalizer=lambda t: t.replace("rapaz", "menino"))
    words = out.split()
    assert words[-1] == "ʁɐˈpaʃ"
    assert words[1] == G2P("pt-PT").transcribe("menino")


@pytest.mark.parametrize("text", [
    'o <phoneme ph="ʁɐˈpaʃ">rapaz</phoneme> comeu',
    '<phoneme ph="ɡatu">gato</phoneme>, e o cão.',
    'as amarelas <phoneme ph="kazɐʃ">casas</phoneme>',
])
def test_forced_word_is_a_pre_resolved_override(text):
    """A forced word before a pause, where no sandhi rewrites it."""
    out = both("pt-PT", text)
    forced = text.split('ph="')[1].split('"')[0]
    assert forced in out.split()


def test_forced_word_with_expand_and_mark():
    pipeline = Pipeline(expand=lambda t: t.replace("2", "dois"), mark=lambda t: t.replace("dois", "dóis"))
    out = both("pt-PT", '2 <phoneme ph="ɡatu">gatos</phoneme>', pipeline=pipeline)
    assert out.split() == [G2P("pt-PT").transcribe("dóis gatos").split()[0], "ɡatu"]


def test_caller_spec_is_compiled_without_the_disk_cache(tmp_path, monkeypatch):
    monkeypatch.setenv("O2I_IR_CACHE", str(tmp_path))
    spec = registry.get("pt-PT")
    spec = replace(spec, word_exceptions={**(spec.word_exceptions or {}), "gato": "ɡaˈtɔ"})
    out = both("pt-PT", "o gato", spec=spec)
    assert out.split()[1] == G2P("pt-PT", pipeline=Pipeline(lexicon={"gato": "ɡaˈtɔ"})).transcribe("gato")
    assert not list(tmp_path.iterdir())


def test_unambiguous_endings_compile_option():
    text = "ils parlent et elles mangent"
    with_alts = G2P("fr-FR").transcribe_detailed(text, search="beam")
    out = both("fr-FR", text, expose_ambiguous_endings=False)
    assert out == with_alts.ipa
    got = G2P("fr-FR", expose_ambiguous_endings=False).transcribe_detailed(text, search="beam")
    assert sum(len(w.candidates) for w in got.words) < sum(len(w.candidates) for w in with_alts.words)


def test_hooks_keep_the_shared_interpreter_clean():
    hooked = ir("pt-PT", pipeline=Pipeline(rescore=(_Theta(),)))
    plain = G2P("pt-PT")
    assert hooked._interpreter is not plain._interpreter
    assert "θ" not in plain.transcribe("gato")
    assert cache.interpreter("pt-PT", **cache.DEFAULT_OPTIONS).hooks.rescore is None
