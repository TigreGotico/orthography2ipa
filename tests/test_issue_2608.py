"""The sentence-level stages run in the order of the interpreter: the
declarative ``sandhi_rules`` of the spec, then the sentence rescorers, then
the sandhi plugin."""
import warnings

from orthography2ipa import G2P
from orthography2ipa import registry
from orthography2ipa.plugins import SandhiPlugin
from orthography2ipa.sentence import SentenceRescorer


class SpyRescorer(SentenceRescorer):
    def __init__(self):
        self.seen = []

    def rescore(self, word, context):
        self.seen.append(context.this_word_ipa)
        return context.this_word_ipa + "!"


class SpySandhi(SandhiPlugin):
    def __init__(self):
        self.received = []

    def apply(self, words, surfaces, pausal, lang):
        self.received.append(list(words))
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


def test_the_sandhi_plugin_receives_the_words_the_rescorers_wrote(monkeypatch):
    plugin = SpySandhi()
    monkeypatch.setitem(registry._declared, "sandhi", {"spy": plugin})
    engine = _engine(sentence_rescorer=SpyRescorer(), plugins={"sandhi": ["spy"]})
    ipa = engine.transcribe("tant que")
    expected = [w + "!" for w in _engine().transcribe("tant que").split()]
    assert plugin.received == [expected]
    assert ipa.split() == expected
