"""Tests for G2P plugin architecture."""
from typing import List, Optional

from orthography2ipa.g2p_plugin import G2PPlugin, WordContext
from orthography2ipa.phonetok import PhonetokTokenizer
from orthography2ipa.types import LanguageSpec


class DummyPlugin(G2PPlugin):
    """Test plugin that returns fixed IPA."""

    def transcribe(self, text: str) -> str:
        return "tɛst"

    def transcribe_word(self, word: str, context: Optional[WordContext] = None) -> str:
        return "tɛst"

    @property
    def language_codes(self) -> List[str]:
        return ["xx-test"]


class TestWordContext:
    def test_frozen(self):
        ctx = WordContext(prev_word_ipa="ab", is_pausal=True)
        assert ctx.prev_word_ipa == "ab"
        assert ctx.is_pausal is True
        assert ctx.next_word_ipa is None
        assert ctx.is_sentence_initial is False


class TestG2PPlugin:
    def test_subclassable(self):
        plugin = DummyPlugin()
        assert plugin.transcribe("anything") == "tɛst"
        assert plugin.transcribe_word("anything") == "tɛst"
        assert "xx-test" in plugin.language_codes


class TestPhonetokPluginDelegation:
    def test_ipa_best_delegates_to_plugin(self):
        spec = LanguageSpec(
            code="xx", name="Test", family="Test", script="Latin",
            graphemes={"t": ["t"], "e": ["e"]}, allophones={},
        )
        plugin = DummyPlugin()
        tok = PhonetokTokenizer(spec, plugin=plugin)
        assert tok.ipa_best("te") == "tɛst"

    def test_ipa_beam_ignores_plugin(self):
        """ipa_beam always uses declarative beam search."""
        spec = LanguageSpec(
            code="xx", name="Test", family="Test", script="Latin",
            graphemes={"t": ["t"], "e": ["e"]}, allophones={},
        )
        plugin = DummyPlugin()
        tok = PhonetokTokenizer(spec, plugin=plugin)
        paths = tok.ipa_beam("te")
        assert paths[0].ipa == "te"  # not "tɛst"

    def test_no_plugin_fallback(self):
        """Without plugin, ipa_best uses beam search."""
        spec = LanguageSpec(
            code="xx", name="Test", family="Test", script="Latin",
            graphemes={"t": ["t"], "e": ["e"]}, allophones={},
        )
        tok = PhonetokTokenizer(spec)
        assert tok.ipa_best("te") == "te"


class ContextEchoPlugin(G2PPlugin):
    """Test plugin that records every context field it receives."""

    def __init__(self):
        self.seen_contexts = []
        self.normalized = []
        self.post_processed = []

    def transcribe(self, text: str) -> str:
        return text

    def transcribe_word(self, word: str, context: Optional[WordContext] = None) -> str:
        self.seen_contexts.append(context)
        return word

    @property
    def language_codes(self) -> List[str]:
        return ["xx-echo"]

    def normalize(self, text: str) -> str:
        self.normalized.append(text)
        return text.lower()

    def post_process(self, ipa: str, context: Optional[WordContext] = None) -> str:
        self.post_processed.append((ipa, context))
        return ipa + "!"

    @property
    def priority(self) -> int:
        return 80


class TestWordContextFields:
    def test_new_fields_default(self):
        ctx = WordContext()
        assert ctx.prev_word is None
        assert ctx.next_word is None
        assert ctx.is_sentence_final is False
        assert ctx.word_index == 0
        assert ctx.word_count == 1
        assert ctx.lang is None

    def test_positional_construction_unchanged(self):
        """Original four fields keep their positional order."""
        ctx = WordContext("a", "b", True, True)
        assert ctx.prev_word_ipa == "a"
        assert ctx.next_word_ipa == "b"
        assert ctx.is_pausal is True
        assert ctx.is_sentence_initial is True

    def test_all_fields_settable(self):
        ctx = WordContext(
            prev_word_ipa="a", next_word_ipa="b", is_pausal=True,
            is_sentence_initial=True, prev_word="um", next_word="dois",
            is_sentence_final=True, word_index=2, word_count=5, lang="pt-PT",
        )
        assert ctx.prev_word == "um"
        assert ctx.next_word == "dois"
        assert ctx.is_sentence_final is True
        assert ctx.word_index == 2
        assert ctx.word_count == 5
        assert ctx.lang == "pt-PT"


class TestPluginHooks:
    def test_default_hooks_are_identity(self):
        plugin = DummyPlugin()
        assert plugin.normalize("Some TEXT 123") == "Some TEXT 123"
        assert plugin.post_process("ipa", WordContext()) == "ipa"
        assert plugin.priority == 50

    def test_overridden_hooks(self):
        plugin = ContextEchoPlugin()
        assert plugin.normalize("ABC") == "abc"
        assert plugin.normalized == ["ABC"]
        ctx = WordContext(is_pausal=True)
        assert plugin.post_process("ipa", ctx) == "ipa!"
        assert plugin.post_processed == [("ipa", ctx)]
        assert plugin.priority == 80


class TestPluginPriorityDispatch:
    def test_higher_priority_wins(self, monkeypatch):
        from orthography2ipa import registry

        class _EP:
            def __init__(self, name, cls):
                self.name = name
                self._cls = cls

            def load(self):
                return self._cls

        class LowPlugin(DummyPlugin):
            @property
            def language_codes(self):
                return ["xx-prio"]

        class HighPlugin(ContextEchoPlugin):
            @property
            def language_codes(self):
                return ["xx-prio"]

        def _fake_entry_points(*args, **kwargs):
            return [_EP("low", LowPlugin), _EP("high", HighPlugin)]

        monkeypatch.setattr("importlib.metadata.entry_points",
                            _fake_entry_points)
        plugins = registry._discover_plugins()
        assert isinstance(plugins["xx-prio"], HighPlugin)

        # registration order must not matter
        def _fake_entry_points_reversed(*args, **kwargs):
            return [_EP("high", HighPlugin), _EP("low", LowPlugin)]

        monkeypatch.setattr("importlib.metadata.entry_points",
                            _fake_entry_points_reversed)
        plugins = registry._discover_plugins()
        assert isinstance(plugins["xx-prio"], HighPlugin)
