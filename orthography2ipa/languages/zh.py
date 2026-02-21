"""Mandarin Chinese (zh) — grapheme→IPA and allophone mappings.

Sources:
- Lee, W.-S. & Zee, E. (2003). Standard Chinese (Beijing). *JIPA* 33(1).
- Duanmu, S. (2007). *The Phonology of Standard Chinese*, 2nd ed.

Conventions:
- Graphemes are Pinyin romanisation units (standard PRC system).
- Hanzi (characters) require dictionary lookup and are NOT included.
- Tones are suprasegmental and not in the grapheme map.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Initials (consonants) ---
    "b": ["p"], "p": ["pʰ"], "m": ["m"], "f": ["f"],
    "d": ["t"], "t": ["tʰ"], "n": ["n"], "l": ["l"],
    "g": ["k"], "k": ["kʰ"], "h": ["x"],
    "j": ["tɕ"], "q": ["tɕʰ"], "x": ["ɕ"],
    "zh": ["ʈʂ"], "ch": ["ʈʂʰ"], "sh": ["ʂ"], "r": ["ɻ"],
    "z": ["ts"], "c": ["tsʰ"], "s": ["s"],
    "w": ["w"], "y": ["j"],

    # --- Simple finals (vowels) ---
    "a": ["a"], "o": ["o"], "e": ["ɤ"],
    "i": ["i"], "u": ["u"], "ü": ["y"],

    # --- Compound finals ---
    "ai": ["ai"], "ei": ["ei"], "ao": ["au"], "ou": ["ou"],
    "ia": ["ia"], "ie": ["ie"], "iu": ["iou"],
    "ua": ["ua"], "uo": ["uo"], "ui": ["uei"],
    "üe": ["ye"],

    # --- Nasal finals ---
    "an": ["an"], "en-GB": ["ən"], "in": ["in"],
    "un": ["uən"], "ün": ["yn"],
    "ang": ["ɑŋ"], "eng": ["əŋ"], "ing": ["iŋ"], "ong": ["uŋ"],

    # --- Compound nasal finals ---
    "ian": ["iɛn"], "uan": ["uan"], "üan": ["yan"],
    "iang": ["iɑŋ"], "uang": ["uɑŋ"], "iong": ["yŋ"],
    "ueng": ["uəŋ"],

    # --- Special ---
    "er": ["aɻ"],  # rhotacised syllable
    "-i": ["ɨ"],  # 'empty' vowel after zh/ch/sh/r and z/c/s
}

ALLOPHONES = {
    # Stops/affricates (voiceless unaspirated vs aspirated; no voicing contrast)
    "p": ["p"], "pʰ": ["pʰ"],
    "t": ["t"], "tʰ": ["tʰ"],
    "k": ["k"], "kʰ": ["kʰ"],
    "tɕ": ["tɕ"], "tɕʰ": ["tɕʰ"],
    "ʈʂ": ["ʈʂ"], "ʈʂʰ": ["ʈʂʰ"],
    "ts": ["ts"], "tsʰ": ["tsʰ"],

    # Fricatives
    "f": ["f"], "s": ["s"], "ɕ": ["ɕ"],
    "ʂ": ["ʂ"], "x": ["x"],
    "ɻ": ["ɻ", "ʐ"],  # approximant or fricative

    # Nasals
    "m": ["m"], "n": ["n"],

    # Lateral / Glides
    "l": ["l"], "w": ["w"], "j": ["j"],

    # Vowels
    "a": ["a", "ɑ", "ɛ"],  # varies by final environment
    "o": ["o", "uo"],
    "ɤ": ["ɤ", "ə"],
    "i": ["i"],
    "u": ["u"],
    "y": ["y"],
    "ɨ": ["ɨ", "ɯ"],  # apical vowel after retroflex/alveolar sibilants

    # Nasal codas
    "ŋ": ["ŋ"],
}

SPECS = {
    "zh": LanguageSpec(
        code="zh",
        name="Mandarin Chinese",
        family="Sinitic",
        script="Hanzi/Pinyin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        notes=(
            "Standard Mandarin (Pǔtōnghuà) based on Beijing pronunciation. "
            "Graphemes are Pinyin romanisation units. Hanzi→Pinyin conversion "
            "requires a separate dictionary (e.g. CC-CEDICT). Four lexical "
            "tones + neutral tone are suprasegmental and not encoded here."
        ),
    ),
}
