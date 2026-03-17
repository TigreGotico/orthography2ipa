"""Tests for Arabic G2P plugin."""
from orthography2ipa.plugins.arabic_g2p import ArabicG2PPlugin
from orthography2ipa.plugins.arabic_utils import (
    is_arabic_letter,
    is_sun_letter,
    normalize_arabic,
    strip_tashkeel,
)


class TestArabicUtils:
    def test_is_arabic_letter(self):
        assert is_arabic_letter("ب") is True
        assert is_arabic_letter("a") is False
        assert is_arabic_letter("\u064E") is False  # fatha is diacritic

    def test_strip_tashkeel(self):
        # بِسْمِ → بسم
        assert strip_tashkeel("بِسْمِ") == "بسم"

    def test_is_sun_letter(self):
        assert is_sun_letter("ش") is True
        assert is_sun_letter("ب") is False

    def test_normalize_arabic(self):
        text = "كِتَابٌ"
        result = normalize_arabic(text)
        assert isinstance(result, str)


class TestArabicG2PPlugin:
    def test_language_codes(self):
        plugin = ArabicG2PPlugin(tashkeel=False)
        assert "arb" in plugin.language_codes

    def test_transcribe_word_diacritized(self):
        plugin = ArabicG2PPlugin(tashkeel=False)
        # كِتَاب = k-i-t-a-ā-b
        result = plugin.transcribe_word("كِتَاب")
        assert "k" in result
        assert "t" in result
        assert "b" in result

    def test_transcribe_word_basic_consonants(self):
        plugin = ArabicG2PPlugin(tashkeel=False)
        # بَ = ba
        result = plugin.transcribe_word("بَ")
        assert result == "ba"

    def test_transcribe_sentence(self):
        plugin = ArabicG2PPlugin(tashkeel=False)
        result = plugin.transcribe("بَابٌ")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_has_diacritics_detection(self):
        assert ArabicG2PPlugin._has_diacritics("بِسْمِ") is True
        assert ArabicG2PPlugin._has_diacritics("بسم") is False
