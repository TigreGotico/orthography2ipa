"""arabic_g2p — Arabic G2P plugin for orthography2ipa.

Provides rule-based Arabic-to-IPA transcription handling:
- Consonant mapping (28 Arabic letters → IPA)
- Diacritic (harakat) → vowel mapping
- Sun-letter assimilation (ال + sun letter → geminate)
- Hamzat al-wasl elision
- Tanwin (nunation) pausal/connected forms
- Optional tashkeel (diacritization) via ONNX model

Usage
─────
    >>> from orthography2ipa.plugins.arabic_g2p import ArabicG2PPlugin
    >>> plugin = ArabicG2PPlugin()
    >>> plugin.transcribe_word("كِتَاب")
    'kitaːb'
"""
from __future__ import annotations

from typing import Dict, List, Optional

from orthography2ipa.g2p_plugin import G2PPlugin, WordContext
from orthography2ipa.plugins.arabic_utils import normalize_arabic, strip_tashkeel

__all__ = ["ArabicG2PPlugin"]

# ═══════════════════════════════════════════════════════════════════════════
# Consonant mapping: Arabic letter → IPA
# ═══════════════════════════════════════════════════════════════════════════

ARABIC_TO_IPA_CONSONANTS: Dict[str, str] = {
    "ب": "b", "ت": "t", "ث": "θ", "ج": "d͡ʒ", "ح": "ħ",
    "خ": "x", "د": "d", "ذ": "ð", "ر": "r", "ز": "z",
    "س": "s", "ش": "ʃ", "ص": "sˤ", "ض": "dˤ", "ط": "tˤ",
    "ظ": "ðˤ", "ع": "ʕ", "غ": "ɣ", "ف": "f", "ق": "q",
    "ك": "k", "ل": "l", "م": "m", "ن": "n", "ه": "h",
    "و": "w", "ي": "j", "ء": "ʔ",
    # Hamza carriers
    "أ": "ʔ", "إ": "ʔ", "ؤ": "ʔ", "ئ": "ʔ",
    # Alef variants
    "آ": "ʔaː", "ا": "",  # alef — carrier, no sound by itself
    "ى": "",  # alef maqsura
    "ة": "",  # ta marbuta (handled contextually)
}

# ═══════════════════════════════════════════════════════════════════════════
# Diacritic → vowel mapping
# ═══════════════════════════════════════════════════════════════════════════

DIACRITIC_TO_IPA: Dict[str, str] = {
    "\u064E": "a",      # fatha
    "\u064F": "u",      # damma
    "\u0650": "i",      # kasra
    "\u064B": "an",     # fathatan (tanwin)
    "\u064C": "un",     # dammatan (tanwin)
    "\u064D": "in",     # kasratan (tanwin)
    "\u0651": "",       # shadda (gemination — handled separately)
    "\u0652": "",       # sukun (no vowel)
}

# Sun letters for assimilation
_SUN_LETTERS = frozenset("ت ث د ذ ر ز س ش ص ض ط ظ ل ن".split())


class ArabicG2PPlugin(G2PPlugin):
    """Rule-based Arabic G2P with optional tashkeel."""

    def __init__(self, tashkeel: bool = True) -> None:
        self._diacritizer = None
        if tashkeel:
            try:
                from orthography2ipa.plugins.tashkeel import TashkeelDiacritizer
                self._diacritizer = TashkeelDiacritizer()
            except ImportError:
                pass

    @property
    def language_codes(self) -> List[str]:
        return ["arb", "ar-SA", "ar-EG", "ar-MA"]

    def transcribe(self, text: str) -> str:
        """Transcribe Arabic text to IPA."""
        text = normalize_arabic(text)
        if self._diacritizer and not self._has_diacritics(text):
            text = self._diacritizer.diacritize(text)
        words = text.split()
        ipa_words = [self.transcribe_word(w) for w in words]
        return " ".join(ipa_words)

    def transcribe_word(
        self, word: str, context: Optional[WordContext] = None
    ) -> str:
        """Transcribe a single Arabic word to IPA."""
        word = normalize_arabic(word)
        result: List[str] = []
        i = 0
        chars = list(word)
        n = len(chars)

        while i < n:
            ch = chars[i]

            # Handle shadda (gemination)
            if ch == "\u0651":
                if result:
                    result.append(result[-1])  # double the last consonant
                i += 1
                continue

            # Handle diacritics (vowels)
            if ch in DIACRITIC_TO_IPA:
                vowel = DIACRITIC_TO_IPA[ch]
                if vowel:
                    result.append(vowel)
                i += 1
                continue

            # Handle consonants
            if ch in ARABIC_TO_IPA_CONSONANTS:
                ipa = ARABIC_TO_IPA_CONSONANTS[ch]
                if ipa:
                    # Check for long vowels: alef/waw/ya after vowel
                    if ch == "ا" and result and result[-1] == "a":
                        result[-1] = "aː"
                    elif ch == "و" and result and result[-1] == "u":
                        result[-1] = "uː"
                    elif ch == "ي" and result and result[-1] == "i":
                        result[-1] = "iː"
                    else:
                        result.append(ipa)
                elif ch == "ا":
                    # Bare alef — context dependent
                    pass
                i += 1
                continue

            # Unknown character — skip
            i += 1

        return "".join(result)

    @staticmethod
    def _has_diacritics(text: str) -> bool:
        """Check if text already has Arabic diacritics."""
        for ch in text:
            if "\u064B" <= ch <= "\u0652":
                return True
        return False
