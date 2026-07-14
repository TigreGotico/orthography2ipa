"""Stress plugins — and the one rule that makes any output-changing plugin safe.

    The transcription is a function of the SPEC and the INPUT.
    Never of the environment.

A stress plugin is the case that forces the rule. It *changes* the
transcription — it places a mark, and it moves the vowel reduction that stress
conditions — so "may a plugin change the output?" cannot be answered yes or no.
It has to be answered: **only if the spec asked**.
"""
import dataclasses

import pytest

from orthography2ipa import get
from orthography2ipa import registry
from orthography2ipa.registry import MissingStressPlugin
from orthography2ipa.stress import detect_stress
from orthography2ipa.stress_plugin import StressPlugin


class _AlwaysFirst(StressPlugin):
    """Stresses the first syllable, always. Deliberately WRONG for Portuguese, so
    a test can see whether it was consulted at all."""

    def stressed_index(self, word, syllables, lang):
        return 0

    @property
    def language_codes(self):
        return ["pt-PT"]


class _Abstains(StressPlugin):
    """Never sure. The declarative rules should take over."""

    def stressed_index(self, word, syllables, lang):
        return None

    @property
    def language_codes(self):
        return ["pt-PT"]


@pytest.fixture
def rules_source():
    return get("pt-PT").stress


def _as_plugin(rules):
    return dataclasses.replace(rules, source="plugin")


# ─── the default: the spec decides, and it says "rules" ─────────────────

def test_a_plugin_is_ignored_unless_the_spec_asks(monkeypatch, rules_source):
    """This is the whole safeguard. Installing something must not move the answer."""
    monkeypatch.setattr(registry, "_stress_plugins", {"pt-PT": _AlwaysFirst()})

    # `falar` is oxytone — the rules say the LAST syllable. The plugin says the
    # first. The spec did not ask, so the plugin does not get a vote.
    assert detect_stress("falar", rules_source, lang="pt-PT") == 1


def test_every_shipped_spec_uses_the_declarative_rules():
    """No spec opts in yet, so nothing moves."""
    from orthography2ipa import available_codes
    opted_in = [
        code for code in available_codes()
        if (get(code).stress and get(code).stress.source != "rules")
    ]
    assert opted_in == []


# ─── the opt-in: the spec asks, so the plugin decides ───────────────────

def test_a_spec_that_asks_gets_the_plugin(monkeypatch, rules_source):
    monkeypatch.setattr(registry, "_stress_plugins", {"pt-PT": _AlwaysFirst()})
    assert detect_stress("falar", _as_plugin(rules_source), lang="pt-PT") == 0


def test_an_abstaining_plugin_falls_back_to_the_rules(monkeypatch, rules_source):
    """`None` means *I do not know* — not *unstressed*. Guessing would be worse
    than abstaining, because a wrong stress moves every reduction it conditions."""
    monkeypatch.setattr(registry, "_stress_plugins", {"pt-PT": _Abstains()})
    assert detect_stress("falar", _as_plugin(rules_source), lang="pt-PT") == 1


# ─── and the missing plugin fails LOUDLY ────────────────────────────────

def test_a_missing_plugin_is_fatal(monkeypatch, rules_source):
    """Fatal on purpose.

    The spec is saying its stress cannot be expressed by the declarative rules.
    Falling back to them would not be a graceful degradation — it would be a
    DIFFERENT ANSWER, silently, and the caller would have no way to know which one
    they got. That is precisely the failure this rule exists to prevent.
    """
    monkeypatch.setattr(registry, "_stress_plugins", {})
    with pytest.raises(MissingStressPlugin, match="no stress plugin"):
        detect_stress("falar", _as_plugin(rules_source), lang="pt-PT")
