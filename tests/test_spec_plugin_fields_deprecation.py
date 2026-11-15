"""A spec that names a plugin, or asks for a stress plugin, warns when ``G2P``
builds an engine on it: once per engine, at the caller's line.

The removal version comes from ``version.py``, read as text, so the expected
message does not depend on the code that writes the warning. No shipped spec
sets either field: ``test_plugin_stages.py::test_no_shipped_spec_names_a_plugin``
and ``test_stress_plugin.py::test_every_shipped_spec_uses_the_declarative_rules``
pin that.
"""
import re
import warnings
from dataclasses import replace
from pathlib import Path

import pytest

import orthography2ipa
from orthography2ipa import G2P, get, registry
from orthography2ipa.plugins import SandhiPlugin

VERSION = Path(orthography2ipa.__file__).parent / "version.py"
FIELDS = ("Pipeline(expand=...) or Pipeline(mark=...) for 'normalize', "
          "Pipeline(rescore=...) for 'rescore', Pipeline(sandhi=...) for 'sandhi'")


def removal_version() -> str:
    major = re.search(r"^VERSION_MAJOR = (\d+)$", VERSION.read_text(encoding="utf-8"), re.M)
    return f"{int(major.group(1)) + 1}.0.0"


class KeepWords(SandhiPlugin):
    language_codes = ["pt-PT"]

    def apply(self, words, surfaces, pausal, lang):
        return list(words)


def naming_a_plugin():
    return replace(get("pt-PT"), plugins={"sandhi": ("keep",)})


def asking_for_a_stress_plugin():
    spec = get("pt-PT")
    return replace(spec, stress=replace(spec.stress, source="plugin"))


def deprecations(build):
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        engine = build()
    return engine, [w for w in caught if issubclass(w.category, DeprecationWarning)]


@pytest.mark.parametrize("spec, name, replacement", [
    (naming_a_plugin, "the plugins field of the pt-PT spec", FIELDS),
    (asking_for_a_stress_plugin, 'stress.source = "plugin" in the pt-PT spec',
     "the stress rules of the spec"),
], ids=["plugins", "stress.source"])
def test_a_spec_field_warns_once_at_the_caller(spec, name, replacement):
    _, caught = deprecations(lambda: G2P("pt-PT", spec=spec()))
    assert [str(w.message) for w in caught] == [
        f"{name} is deprecated and will be removed in {removal_version()}; use {replacement}."]
    assert caught[0].filename == __file__


def test_the_warning_comes_once_per_engine(monkeypatch):
    """Transcribing does not warn again. A second engine warns again."""
    monkeypatch.setitem(registry._declared, "sandhi", {"keep": KeepWords()})
    engine, caught = deprecations(lambda: G2P("pt-PT", spec=naming_a_plugin()))
    assert len(caught) == 1
    plain = G2P("pt-PT")
    with warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)
        for text in ("o gato", "a casa do mar", "três gatos"):
            assert engine.transcribe(text) == plain.transcribe(text)
    _, again = deprecations(lambda: G2P("pt-PT", spec=naming_a_plugin()))
    assert len(again) == 1


@pytest.mark.parametrize("code", ["pt-PT", "ar"])
def test_a_shipped_spec_stays_silent(code):
    with warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)
        G2P(code)


def test_an_empty_plugins_field_stays_silent():
    with warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)
        G2P("pt-PT", spec=replace(get("pt-PT"), plugins={}))
