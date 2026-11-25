"""The sentence-level stages run in the order of the interpreter: the
declarative ``sandhi_rules`` of the spec, then the sentence rescorers, then
the sandhi plugin."""
import warnings

import pytest

from orthography2ipa import G2P
from orthography2ipa import registry
from orthography2ipa.plugins import SandhiPlugin
from orthography2ipa.sentence import SentenceRescorer


class SpyRescorer(SentenceRescorer):
    def __init__(self, events=None):
        self.seen = []
        self.events = events

    def rescore(self, word, context):
        self.seen.append(context.this_word_ipa)
        if self.events is not None:
            self.events.append("rescorer")
        return context.this_word_ipa


class SpySandhi(SandhiPlugin):
    def __init__(self, events):
        self.events = events

    def apply(self, words, surfaces, pausal, lang):
        self.events.append("sandhi")
        return list(words)


def _engine(**kwargs):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        return G2P("ca", **kwargs)


def _first_word_seen(**kwargs):
    spy = SpyRescorer()
    _engine(sentence_rescorer=spy, **kwargs).transcribe("tant que")
    return spy.seen[0]


def test_rescorer_sees_the_form_after_the_sandhi_rules():
    assert _first_word_seen() == "ˈtaŋ"


def test_the_sandhi_rules_are_what_changes_the_form():
    assert _first_word_seen(apply_sandhi=False) == _engine().transcribe("tant") == "ˈtan"


def test_sentence_rescorers_run_before_the_sandhi_plugin(monkeypatch):
    events = []
    monkeypatch.setitem(registry._declared, "sandhi", {"spy": SpySandhi(events)})
    engine = _engine(sentence_rescorer=SpyRescorer(events), plugins={"sandhi": ["spy"]})
    engine.transcribe("tant que")
    assert events == ["rescorer", "rescorer", "sandhi"]
