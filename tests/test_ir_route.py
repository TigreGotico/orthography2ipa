"""The public transcription path runs the compiled IR.

``G2P(code).transcribe`` runs compile + interpret for a language the compiler
accepts. The steps a caller passes at runtime stay host features: a lexicon,
``expand``, ``mark`` and the normalizer run around the interpreter, and so
do the hooks of ``tests/test_ir_hooks.py``. Each expected value is the
rules engine's recorded output (``tests/frozen_rules.py``).
"""
import warnings

import pytest

from orthography2ipa import G2P, Pipeline
from orthography2ipa.exceptions import UnmappedScriptError
from orthography2ipa.ir import cache
from orthography2ipa.ir.interpreter import Interpreter
from orthography2ipa.rescorer import LatticeRescorer
from tests.frozen_rules import FrozenRules

TEXT = "O rapaz comeu as maçãs, e a avó dormiu."


def test_accepted_language_runs_the_interpreter():
    g = G2P("pt-PT")
    assert isinstance(g._interpreter, Interpreter)
    assert g.transcribe(TEXT) == FrozenRules("pt-PT").transcribe(TEXT)


def test_refused_language_raises(monkeypatch):
    from orthography2ipa.ir.compiler import IRUnsupportedFeature

    def refuse(code, **options):
        raise IRUnsupportedFeature(code, "a feature")

    monkeypatch.setenv("O2I_IR_CACHE", "off")
    monkeypatch.setattr(cache, "compile_spec", refuse)
    monkeypatch.setattr(cache, "_interpreters", {})
    with pytest.raises(IRUnsupportedFeature):
        G2P("nl-NL").transcribe("de bewoners")


@pytest.mark.parametrize("search", ["greedy", "beam"])
def test_detailed_matches_the_rules_path(search):
    got = G2P("es-ES").transcribe_detailed("el perro de Ramón", search=search)
    want = FrozenRules("es-ES").transcribe_detailed("el perro de Ramón", search=search)
    assert got.ipa == want.ipa
    assert [(w.word, w.ipa, w.unmapped, w.coverage, w.confidence) for w in got.words] == \
        [(w.word, w.ipa, w.unmapped, w.coverage, w.confidence) for w in want.words]
    assert [[c.ipa for c in w.candidates] for w in got.words] == \
        [[c.ipa for c in w.candidates] for w in want.words]


def test_pipeline_lexicon_is_read_on_the_ir_route():
    lexicon = {"rapaz": "XYZ"}
    g = G2P("pt-PT", pipeline=Pipeline(lexicon=lexicon))
    out = g.transcribe("o rapaz")
    assert "XYZ" in out
    assert out == FrozenRules("pt-PT", pipeline=Pipeline(lexicon=lexicon)).transcribe("o rapaz")


def test_expand_and_mark_run_before_the_interpreter():
    def expand(text):
        return text.replace("2", "dois")

    def mark(text):
        return text.replace("dois", "dóis")

    pipeline = Pipeline(expand=expand, mark=mark)
    g = G2P("pt-PT", pipeline=pipeline)
    assert g.transcribe("2 gatos") == FrozenRules("pt-PT", pipeline=pipeline).transcribe("2 gatos")
    assert g.transcribe("2 gatos") == G2P("pt-PT").transcribe("dóis gatos")


def test_mark_that_changes_the_words_still_raises():
    g = G2P("pt-PT", pipeline=Pipeline(mark=lambda t: t + " extra"))
    with pytest.raises(ValueError):
        g.transcribe("gato")


def test_normalizer_runs_before_the_interpreter():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        g = G2P("pt-PT", normalizer=str.upper)
        want = FrozenRules("pt-PT", normalizer=str.upper).transcribe("gato")
    assert g.transcribe("gato") == want


class _Swap(LatticeRescorer):
    def rescore(self, slot, context):
        return slot.candidates


def test_rescorer_runs_on_the_ir_route():
    g = G2P("pt-PT", pipeline=Pipeline(rescore=(_Swap(),)))
    assert g.transcribe(TEXT) == FrozenRules("pt-PT").transcribe(TEXT)


def test_forced_pronunciation_is_honoured():
    g = G2P("pt-PT")
    out = g.transcribe('o <phoneme ph="ʁɐˈpaʃ">rapaz</phoneme> comeu')
    assert "ʁɐˈpaʃ" in out


def test_unmapped_policy_applies_on_the_ir_route():
    g = G2P("pt-PT", on_unmapped="raise")
    with pytest.raises(UnmappedScriptError):
        g.transcribe("gato 猫")


def test_disk_cache_serves_a_later_process(tmp_path, monkeypatch):
    monkeypatch.setenv("O2I_IR_CACHE", str(tmp_path))
    options = dict(cache.DEFAULT_OPTIONS, apply_sandhi=False)
    first = cache.document("es-ES", **options)
    files = list(tmp_path.glob("es-ES-*.json.xz"))
    assert len(files) == 1

    def refuse(*a, **kw):
        raise AssertionError("compiled again")

    monkeypatch.setattr(cache, "compile_spec", refuse)
    assert cache.document("es-ES", **options) == first
