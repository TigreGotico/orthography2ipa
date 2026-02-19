"""Serbian (sr) — grapheme→IPA and allophone mappings.

Sources:
- Browne, W. & Alt, T. (2004). *A Handbook of Bosnian, Serbian, and Croatian*. SEELRC.
- Landau, E. et al. (1999). Serbian/Croatian. *Handbook of the IPA*.
- Corbett, G. & Browne, W. (1993). 'Serbo-Croat' in *The Slavonic Languages*.
"""
from orthography2ipa.types import LanguageSpec

# Serbian uses both Cyrillic (primary) and Latin (Gaj) scripts.
# Entries cover Cyrillic; Latin equivalents noted where needed.
CYRILLIC_GRAPHEMES = {
    # --- Vowels ---
    "а": ["a"],
    "е": ["ɛ"],
    "и": ["i"],
    "о": ["ɔ"],
    "у": ["u"],

    # --- Syllabic r ---
    "р": ["r", "r̩"],  # can be syllabic nucleus (трг, прст)

    # --- Consonants ---
    "б": ["b"],
    "в": ["v"],
    "г": ["ɡ"],
    "д": ["d"],
    "ђ": ["dʑ"],  # palatal affricate (softer than dž)
    "ж": ["ʒ"],
    "з": ["z"],
    "ј": ["j"],
    "к": ["k"],
    "л": ["l"],
    "љ": ["ʎ"],  # palatal lateral
    "м": ["m"],
    "н": ["n"],
    "њ": ["ɲ"],  # palatal nasal
    "п": ["p"],
    "р": ["r"],
    "с": ["s"],
    "т": ["t"],
    "ћ": ["tɕ"],  # palatal affricate (softer than č)
    "ф": ["f"],
    "х": ["x"],
    "ц": ["ts"],
    "ч": ["tʃ"],
    "џ": ["dʒ"],
    "ш": ["ʃ"],
}

# Latin/Gaj script equivalents
LATIN_GRAPHEMES = {
    "a": ["a"], "e": ["ɛ"], "i": ["i"], "o": ["ɔ"], "u": ["u"],
    "b": ["b"], "v": ["v"], "g": ["ɡ"], "d": ["d"],
    "đ": ["dʑ"],
    "ž": ["ʒ"], "z": ["z"], "j": ["j"], "k": ["k"], "l": ["l"],
    "lj": ["ʎ"], "m": ["m"], "n": ["n"], "nj": ["ɲ"],
    "p": ["p"], "r": ["r"], "s": ["s"], "t": ["t"],
    "ć": ["tɕ"],
    "f": ["f"], "h": ["x"], "c": ["ts"], "č": ["tʃ"],
    "dž": ["dʒ"], "š": ["ʃ"],
}

GRAPHEMES = {**CYRILLIC_GRAPHEMES, **LATIN_GRAPHEMES}

ALLOPHONES = {
    "p": ["p"], "b": ["b", "p"],
    "t": ["t"], "d": ["d", "t"],
    "k": ["k"], "ɡ": ["ɡ", "k"],
    "f": ["f"], "v": ["v", "f"],
    "s": ["s"], "z": ["z", "s"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ", "ʃ"],
    "x": ["x"],
    "ts": ["ts"], "tʃ": ["tʃ"], "tɕ": ["tɕ"],
    "dʒ": ["dʒ", "tʃ"], "dʑ": ["dʑ", "tɕ"],
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "ʎ": ["ʎ"],
    "r": ["r"], "r̩": ["r̩"],  # syllabic r
    "j": ["j"],
    # Vowels: Serbian has phonemic pitch accent (rising/falling) but
    # no qualitative reduction (unlike Russian)
    "a": ["a"],
    "ɛ": ["ɛ"],
    "i": ["i"],
    "ɔ": ["ɔ"],
    "u": ["u"],
}

SPECS = {
    "sr": LanguageSpec(
        code="sr",
        name="Serbian",
        family="Slavic",
        script="Cyrillic",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="sla",
        notes=(
            "Standard Serbian (Štokavian dialect, Ekavian variant in Serbia). "
            "Written in Cyrillic (primary) and Latin (Gaj) scripts. "
            "Four-accent system: short/long × falling/rising pitch accent. "
            "Two palatal affricate pairs: ⟨ћ/ć⟩ = [tɕ], ⟨ч/č⟩ = [tʃ]; "
            "⟨ђ/đ⟩ = [dʑ], ⟨џ/dž⟩ = [dʒ]. "
            "No vowel reduction (unlike Russian). Syllabic /r̩/."
        ),
    ),
}
