"""The conformance checks warn, name the release that removes them, and still run.

The removal version comes from ``version.py``, read as text, so the expected
message does not depend on the code that writes the warning.
"""
import re
import warnings
from pathlib import Path

import pytest

import orthography2ipa
from orthography2ipa.conformance import (
    ConformanceError, assert_rescorer_conforms, assert_syllabifier_conforms,
)
from orthography2ipa.syllabifier_plugin import SyllabifierPlugin

VERSION = Path(orthography2ipa.__file__).parent / "version.py"


def removal_version() -> str:
    major = re.search(r"^VERSION_MAJOR = (\d+)$", VERSION.read_text(encoding="utf-8"), re.M)
    return f"{int(major.group(1)) + 1}.0.0"


class WholeWord(SyllabifierPlugin):
    """One syllable per word. On one-syllable words it moves nothing."""

    language_codes = ["pt-PT"]

    def syllabify(self, word, lang=None):
        return [word]


class Rewrites(WholeWord):
    def syllabify(self, word, lang=None):
        return [word.upper()]


class NoRescorers:
    language_codes = ["pt-PT"]

    def rescorers(self, lang):
        return []


CHECKS = [
    ("assert_syllabifier_conforms", lambda: assert_syllabifier_conforms(WholeWord(), words=["mar", "sol"]),
     "a test of your own that compares G2P(lang) with G2P(lang, pipeline=Pipeline(syllabifier=...))"),
    ("assert_rescorer_conforms", lambda: assert_rescorer_conforms(NoRescorers(), words=["mar", "sol"]),
     "a test of your own over G2P(lang, pipeline=Pipeline(rescore=...)) and phoneme_inventory(spec)"),
]


@pytest.mark.parametrize("name, check, replacement", CHECKS, ids=[c[0] for c in CHECKS])
def test_a_check_warns_once_at_the_caller(name, check, replacement):
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        assert check() is None
    deprecations = [w for w in caught if issubclass(w.category, DeprecationWarning)]
    assert [str(w.message) for w in deprecations] == [
        f"{name} is deprecated and will be removed in {removal_version()}; use {replacement}."]
    assert deprecations[0].filename == __file__


def test_a_check_still_fails_a_broken_plugin():
    with pytest.deprecated_call(), pytest.raises(ConformanceError, match="round-trip"):
        assert_syllabifier_conforms(Rewrites(), words=["mar"])
