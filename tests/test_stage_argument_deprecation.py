"""The old stage arguments of ``G2P`` warn, and name the ``Pipeline`` field.

The removal version comes from ``version.py``, read as text, so the expected
message does not depend on the code that writes the warning.
"""
import re
import warnings
from pathlib import Path

import pytest

import orthography2ipa
from orthography2ipa import G2P, Pipeline
from orthography2ipa.conformance import assert_rescorer_conforms
from orthography2ipa.plugins import SandhiPlugin
from orthography2ipa.rescorer import LatticeRescorer
from orthography2ipa.rescorer_plugin import RescorerPlugin
from orthography2ipa.sentence import SentenceRescorer

VERSION = Path(orthography2ipa.__file__).parent / "version.py"


class KeepSlot(LatticeRescorer):
    def rescore(self, slot, context):
        return slot.candidates


class KeepWord(SentenceRescorer):
    def rescore(self, word, context):
        return context.this_word_ipa


class KeepWords(SandhiPlugin):
    language_codes = ["pt-PT"]

    def apply(self, words, surfaces, pausal, lang):
        return list(words)


# RescorerPlugin is deprecated, and a subclass still works.
with pytest.deprecated_call():
    class KeepSlots(RescorerPlugin):
        language_codes = ["pt-PT"]

        def rescorers(self, lang):
            return [KeepSlot()]


def removal_version() -> str:
    major = re.search(r"^VERSION_MAJOR = (\d+)$", VERSION.read_text(encoding="utf-8"), re.M)
    return f"{int(major.group(1)) + 1}.0.0"


OLD_ARGUMENTS = [
    ("normalizer", lambda text: text, "Pipeline(expand=...) or Pipeline(mark=...)"),
    ("rescorer", KeepSlot(), "Pipeline(rescore=...)"),
    ("sentence_rescorer", KeepWord(), "Pipeline(sandhi=...)"),
    ("plugins", {"sandhi": "not-installed"},
     "Pipeline(expand=...) or Pipeline(mark=...) for 'normalize', "
     "Pipeline(rescore=...) for 'rescore', Pipeline(sandhi=...) for 'sandhi'"),
]


@pytest.mark.parametrize("name, value, field", OLD_ARGUMENTS, ids=[a[0] for a in OLD_ARGUMENTS])
def test_an_old_argument_warns_once_and_names_its_field(name, value, field):
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        G2P("pt-PT", **{name: value})
    deprecations = [w for w in caught if issubclass(w.category, DeprecationWarning)]
    assert [str(w.message) for w in deprecations] == [
        f"G2P({name}=...) is deprecated and will be removed in {removal_version()}; "
        f"use {field}."]
    assert deprecations[0].filename == __file__


@pytest.mark.parametrize("name, value, field", OLD_ARGUMENTS, ids=[a[0] for a in OLD_ARGUMENTS])
def test_pytest_warns_matches_the_removal_version(name, value, field):
    with pytest.warns(DeprecationWarning,
                      match=rf"^G2P\({name}=\.\.\.\) is deprecated and will be removed in "
                            rf"{re.escape(removal_version())}; use {re.escape(field)}\.$"):
        G2P("pt-PT", **{name: value})


def test_no_warning_when_the_old_arguments_are_unset():
    with warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)
        G2P("pt-PT")
        G2P("pt-PT", normalizer=None, rescorer=None, sentence_rescorer=None, plugins=None)
        G2P("pt-PT", pipeline=Pipeline(expand=lambda text: text, mark=lambda text: text,
                                       rescore=(KeepSlot(),), sandhi=KeepWords()))


def test_the_rescorer_conformance_check_uses_no_old_argument():
    with warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)
        assert_rescorer_conforms(KeepSlots(), words=["casa"], lang="pt-PT")
