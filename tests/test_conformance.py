"""The conformance kit: what a plugin may change, and what it may not."""
import pytest

from orthography2ipa.conformance import (
    ConformanceError, assert_syllabifier_conforms,
)
from orthography2ipa.syllabifier_plugin import SyllabifierPlugin

silabificador = pytest.importorskip("silabificador")

from orthography2ipa.syllabifiers import SilabificadorSyllabifier  # noqa: E402


def test_the_shipped_plugin_conforms():
    """The one we ship must pass the kit we ship."""
    assert_syllabifier_conforms(SilabificadorSyllabifier(), lang="pt-PT-x-lisbon")


class _Rewriting(SyllabifierPlugin):
    """Splits AND strips the accent — so the word downstream is not the word in."""

    def syllabify(self, word, lang=None):
        return list(word.replace("ã", "a"))

    @property
    def language_codes(self):
        return ["pt-PT"]


class _Silent(SyllabifierPlugin):
    def syllabify(self, word, lang=None):
        return [word]

    @property
    def language_codes(self):
        return []


def test_a_rewriting_syllabifier_is_caught():
    with pytest.raises(ConformanceError, match="round-trip"):
        assert_syllabifier_conforms(_Rewriting(), words=["mãe"])


def test_a_plugin_that_claims_nothing_is_caught():
    with pytest.raises(ConformanceError, match="no language codes"):
        assert_syllabifier_conforms(_Silent())


class _MergesHiatus(SyllabifierPlugin):
    """Returns a WRONG split, one syllable short — the shape of the coelho bug.

    It round-trips, it claims a language, and it still moves the transcription,
    because the syllable count is load-bearing for stress.
    """

    def syllabify(self, word, lang=None):
        if word == "coelho":
            return ["coe", "lho"]
        return [word]

    @property
    def language_codes(self):
        return ["pt-PT"]


def test_a_plugin_that_moves_the_transcription_is_caught():
    """The rule that was missing. This is the coelho bug, as a test."""
    with pytest.raises(ConformanceError, match="downstream neutrality"):
        assert_syllabifier_conforms(
            _MergesHiatus(), words=["coelho"], lang="pt-PT-x-lisbon")


# ═══════════════════════════════════════════════════════════════════════════
# Rescorer plugins — the OPPOSITE contract
# ═══════════════════════════════════════════════════════════════════════════

from orthography2ipa.conformance import assert_rescorer_conforms  # noqa: E402
from orthography2ipa.registry import get_rescorers, who_answers  # noqa: E402
from orthography2ipa.rescorer import LatticeRescorer  # noqa: E402
from orthography2ipa.rescorer_plugin import RescorerPlugin  # noqa: E402
from orthography2ipa.phonetok import Candidate  # noqa: E402


class _Backs_a(LatticeRescorer):
    """Rewrite /a/ to [ɐ] — a symbol pt-PT declares, so this is legal phonology."""

    def rescore(self, slot, context):
        if slot.top.ipa == "a":
            return (Candidate(ipa="ɐ", cost=0.0),)
        return slot.candidates


class _Invents(LatticeRescorer):
    """Rewrite /a/ to a symbol no spec declares."""

    def rescore(self, slot, context):
        if slot.top.ipa == "a":
            return (Candidate(ipa="Q", cost=0.0),)
        return slot.candidates


class _LegalPhonology(RescorerPlugin):
    def rescorers(self, lang):
        return [_Backs_a()]

    @property
    def language_codes(self):
        return ["pt-PT"]


class _InventsASymbol(RescorerPlugin):
    def rescorers(self, lang):
        return [_Invents()]

    @property
    def language_codes(self):
        return ["pt-PT"]


def test_a_rescorer_MAY_change_the_transcription():
    """The inverse of the syllabifier rule. Changing the output is the whole job."""
    assert_rescorer_conforms(_LegalPhonology(), words=["casa"], lang="pt-PT")


def test_a_rescorer_that_invents_a_symbol_is_caught():
    """Invisible in a diff. Fatal in an embedding table."""
    with pytest.raises(ConformanceError, match="inventory"):
        assert_rescorer_conforms(_InventsASymbol(), words=["casa"], lang="pt-PT")


def test_who_answers_says_who_is_answering():
    """The first question anyone debugging a plugin asks, given an API."""
    answer = who_answers("pt-PT")
    assert "syllabify" in answer and "rescore" in answer
    assert answer["code"] == "pt-PT"
