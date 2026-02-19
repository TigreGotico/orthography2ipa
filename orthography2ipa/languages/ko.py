"""Korean (ko) — grapheme→IPA and allophone mappings.

Sources:
- Lee, H.B. (1999). Korean. *Handbook of the IPA*.
- Shin, J. et al. (2012). *The Sounds of Korean*.
- Sohn, H.-M. (1999). *The Korean Language*.

Conventions:
- Jamo (individual letters) as primary keys.
- Three-way laryngeal contrast: lax, tense, aspirated.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Consonants (Choseong / initial) ---
    "ㄱ": ["k"],  # lax velar
    "ㄲ": ["k͈"],  # tense
    "ㄴ": ["n"],
    "ㄷ": ["t"],  # lax alveolar
    "ㄸ": ["t͈"],  # tense
    "ㄹ": ["ɾ", "l"],  # onset tap, coda lateral
    "ㅁ": ["m"],
    "ㅂ": ["p"],  # lax bilabial
    "ㅃ": ["p͈"],  # tense
    "ㅅ": ["s"],
    "ㅆ": ["s͈"],  # tense
    "ㅇ": ["", "ŋ"],  # silent in onset, [ŋ] in coda
    "ㅈ": ["tɕ"],
    "ㅉ": ["tɕ͈"],  # tense
    "ㅊ": ["tɕʰ"],
    "ㅋ": ["kʰ"],
    "ㅌ": ["tʰ"],
    "ㅍ": ["pʰ"],
    "ㅎ": ["h"],

    # --- Vowels (Jungseong / medial) ---
    "ㅏ": ["a"],
    "ㅐ": ["ɛ"],
    "ㅑ": ["ja"],
    "ㅒ": ["jɛ"],
    "ㅓ": ["ʌ"],
    "ㅔ": ["e"],
    "ㅕ": ["jʌ"],
    "ㅖ": ["je"],
    "ㅗ": ["o"],
    "ㅛ": ["jo"],
    "ㅜ": ["u"],
    "ㅠ": ["ju"],
    "ㅡ": ["ɯ"],
    "ㅣ": ["i"],

    # --- Complex vowels (official diphthongs) ---
    "ㅘ": ["wa"],
    "ㅙ": ["wɛ"],
    "ㅚ": ["we"],  # historically [ø], now [we] for most speakers
    "ㅝ": ["wʌ"],
    "ㅞ": ["we"],
    "ㅟ": ["wi"],  # historically [y], now [wi]
    "ㅢ": ["ɰi"],

    # --- Double consonants (Jongseong / final clusters) ---
    "ㄳ": ["k"],  # ⟨ㄱㅅ⟩ → [k] in isolation
    "ㄵ": ["n"],  # ⟨ㄴㅈ⟩ → [n]
    "ㄶ": ["n"],  # ⟨ㄴㅎ⟩ → [n]
    "ㄺ": ["l"],  # ⟨ㄹㄱ⟩ → [l] or [k]
    "ㄻ": ["m"],  # ⟨ㄹㅁ⟩ → [m]
    "ㄼ": ["l"],  # ⟨ㄹㅂ⟩ → [l]
    "ㄽ": ["l"],  # ⟨ㄹㅅ⟩ → [l]
    "ㄾ": ["l"],  # ⟨ㄹㅌ⟩ → [l]
    "ㄿ": ["l"],  # ⟨ㄹㅍ⟩ → [l]
    "ㅀ": ["l"],  # ⟨ㄹㅎ⟩ → [l]
    "ㅄ": ["p"],  # ⟨ㅂㅅ⟩ → [p]
}

ALLOPHONES = {
    # Lax stops (voicing between voiced segments)
    "k": ["k", "ɡ", "k̚"],  # [ɡ] intervocalic; [k̚] unreleased coda
    "t": ["t", "d", "t̚"],
    "p": ["p", "b", "p̚"],

    # Tense stops
    "k͈": ["k͈"], "t͈": ["t͈"], "p͈": ["p͈"],

    # Aspirated stops
    "kʰ": ["kʰ"], "tʰ": ["tʰ"], "pʰ": ["pʰ"],

    # Affricates
    "tɕ": ["tɕ", "dʑ"],  # [dʑ] intervocalic
    "tɕ͈": ["tɕ͈"],
    "tɕʰ": ["tɕʰ"],

    # Fricatives
    "s": ["s", "ɕ"],  # [ɕ] before /i, j/
    "s͈": ["s͈", "ɕ͈"],
    "h": ["h", "ɦ", "ç", "ɸ"],  # varies by following vowel

    # Nasals
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],

    # Liquid
    "ɾ": ["ɾ"],  # onset
    "l": ["l"],  # coda

    # Vowels
    "a": ["a"], "ɛ": ["ɛ"], "e": ["e"],
    "ʌ": ["ʌ"], "o": ["o"], "u": ["u"],
    "ɯ": ["ɯ"], "i": ["i"],
}

SPECS = {
    "ko": LanguageSpec(
        code="ko",
        name="Korean",
        family="Koreanic",
        script="Hangul",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        notes=(
            "Seoul standard. Three-way laryngeal contrast (lax/tense/aspirated). "
            "Extensive sandhi rules (nasalisation, lateralisation, tensification) "
            "apply at morpheme/word boundaries."
        ),
    ),
}
