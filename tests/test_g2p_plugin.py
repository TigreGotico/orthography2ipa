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
