"""The discovery functions, the three stage base classes and the stage constants
warn, and name the release that removes them.

The removal version comes from ``version.py``, read as text, so the expected
message does not depend on the code that writes the warning. Each warning
points at the line of the caller, which this file is.
"""
import re
import subprocess
import sys
import warnings
from pathlib import Path

import pytest

import orthography2ipa
from orthography2ipa import get, plugins, registry
from orthography2ipa.pipeline import Pipeline
from orthography2ipa.plugins import SandhiPlugin
from orthography2ipa.syllabifier_plugin import SyllabifierPlugin

VERSION = Path(orthography2ipa.__file__).parent / "version.py"


def removal_version() -> str:
    major = re.search(r"^VERSION_MAJOR = (\d+)$", VERSION.read_text(encoding="utf-8"), re.M)
    return f"{int(major.group(1)) + 1}.0.0"


def subclass_normalize():
    class Diacritizer(plugins.NormalizePlugin):
        def normalize(self, text, lang):
            return text

        language_codes = ["ar"]


def subclass_rescorer():
    from orthography2ipa.rescorer_plugin import RescorerPlugin

    class Rescorers(RescorerPlugin):
        def rescorers(self, lang):
            return []

        language_codes = ["ar"]


def subclass_stress():
    from orthography2ipa.stress_plugin import StressPlugin

    class Stress(StressPlugin):
        def stressed_index(self, word, syllables, lang):
            return None

        language_codes = ["ru"]


NORMALIZE = "Pipeline(expand=...) or Pipeline(mark=...)"
FIELDS = "the fields of Pipeline"
SPEC_STRESS = "the stress rules of the spec"

DEPRECATED = [
    ("get_declared_plugins", lambda: registry.get_declared_plugins("normalize", get("pt-PT")),
     "the Pipeline field of each stage"),
    ("get_stress_plugin", lambda: orthography2ipa.get_stress_plugin("pt-PT"), SPEC_STRESS),
    ("get_rescorers", lambda: orthography2ipa.get_rescorers("pt-PT"), "Pipeline(rescore=...)"),
    ("who_answers", lambda: orthography2ipa.who_answers("pt-PT"), "G2P.pipeline"),
    ("STAGES", lambda: orthography2ipa.STAGES, FIELDS),
    ("STAGES", lambda: plugins.STAGES, FIELDS),
    ("OUTPUT_CHANGING_STAGES", lambda: plugins.OUTPUT_CHANGING_STAGES, FIELDS),
    ("ENTRY_POINT_GROUPS", lambda: plugins.ENTRY_POINT_GROUPS, FIELDS),
    ("NormalizePlugin", lambda: orthography2ipa.NormalizePlugin, NORMALIZE),
    ("RescorerPlugin", lambda: orthography2ipa.RescorerPlugin, "Pipeline(rescore=...)"),
    ("StressPlugin", lambda: orthography2ipa.StressPlugin, SPEC_STRESS),
    ("NormalizePlugin", subclass_normalize, NORMALIZE),
    ("RescorerPlugin", subclass_rescorer, "Pipeline(rescore=...)"),
    ("StressPlugin", subclass_stress, SPEC_STRESS),
]
IDS = ["get_declared_plugins", "get_stress_plugin", "get_rescorers", "who_answers",
       "orthography2ipa.STAGES", "plugins.STAGES", "OUTPUT_CHANGING_STAGES",
       "ENTRY_POINT_GROUPS", "orthography2ipa.NormalizePlugin",
       "orthography2ipa.RescorerPlugin", "orthography2ipa.StressPlugin",
       "subclass NormalizePlugin", "subclass RescorerPlugin", "subclass StressPlugin"]


@pytest.mark.parametrize("name, use, replacement", DEPRECATED, ids=IDS)
def test_a_deprecated_name_warns_once_at_the_caller(name, use, replacement):
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        use()
    deprecations = [w for w in caught if issubclass(w.category, DeprecationWarning)]
    assert [str(w.message) for w in deprecations] == [
        f"{name} is deprecated and will be removed in {removal_version()}; "
        f"use {replacement}."]
    assert deprecations[0].filename == __file__


def test_the_constants_keep_their_values():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        assert orthography2ipa.STAGES == ("normalize", "syllabify", "stress", "rescore", "sandhi")
        assert plugins.OUTPUT_CHANGING_STAGES == plugins.STAGES
        assert plugins.ENTRY_POINT_GROUPS == {
            "normalize": "orthography2ipa.normalize", "stress": "orthography2ipa.stress",
            "rescore": "orthography2ipa.rescore", "sandhi": "orthography2ipa.sandhi"}


def test_an_unknown_name_still_raises_attribute_error():
    with pytest.raises(AttributeError, match="no_such_name"):
        orthography2ipa.no_such_name
    with pytest.raises(AttributeError, match="no_such_name"):
        plugins.no_such_name


class WholeWord(SyllabifierPlugin):
    def syllabify(self, word, lang=None):
        return [word]


class KeepWords(SandhiPlugin):
    def apply(self, words, surfaces, pausal, lang):
        return list(words)


def test_a_pipeline_step_needs_no_language_codes():
    """``Pipeline.syllabifier`` and ``Pipeline.sandhi`` take a step with no claim,
    because the caller already chose the engine it runs in."""
    assert WholeWord().language_codes == []
    assert KeepWords().language_codes == []
    plain = orthography2ipa.G2P("pt-PT").transcribe("o mar")
    stepped = orthography2ipa.G2P(
        "pt-PT", pipeline=Pipeline(syllabifier=WholeWord(), sandhi=KeepWords()))
    assert stepped.transcribe("o mar") == plain


SILENT = """
import orthography2ipa
from orthography2ipa import G2P, Pipeline, SandhiPlugin, SyllabifierPlugin


class WholeWord(SyllabifierPlugin):
    def syllabify(self, word, lang=None):
        return [word]


class KeepWords(SandhiPlugin):
    def apply(self, words, surfaces, pausal, lang):
        return list(words)


print(G2P("pt-PT").transcribe("o mar"))
print(G2P("pt-PT", pipeline=Pipeline(sandhi=KeepWords())).transcribe("o mar"))
print(G2P("pt-PT", pipeline=Pipeline(syllabifier=WholeWord())).transcribe("o mar"))
"""


def test_the_supported_path_stays_silent_under_warnings_as_errors():
    run = subprocess.run([sys.executable, "-W", "error", "-c", SILENT],
                         capture_output=True, text=True)
    assert run.returncode == 0, run.stderr
    assert run.stderr == ""
    lines = run.stdout.splitlines()
    assert len(lines) == 3 and lines[0] and len(set(lines)) == 1, lines
