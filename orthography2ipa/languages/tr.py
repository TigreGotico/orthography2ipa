"""Turkish (tr) — grapheme→IPA and allophone mappings.

Sources:
- Zimmer, K. & Orgun, O. (1999). Turkish. *Handbook of the IPA*.
- Göksel, A. & Kerslake, C. (2005). *Turkish: A Comprehensive Grammar*.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels (8-vowel harmony system) ---
    "a": ["a"],
    "e": ["e"],
    "ı": ["ɯ"],  # dotless i: unrounded back close
    "i": ["i"],
    "o": ["o"],
    "ö": ["ø"],
    "u": ["u"],
    "ü": ["y"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["dʒ"],
    "ç": ["tʃ"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "ɟ"],  # palatalised before front vowels
    "ğ": [""],  # soft g: lengthens preceding V or [j] between front V
    "h": ["h"],
    "j": ["ʒ"],
    "k": ["k", "c"],  # palatalised before front vowels
    "l": ["l", "ɫ"],  # clear before front V; dark before back V
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "r": ["ɾ"],
    "s": ["s"],
    "ş": ["ʃ"],
    "t": ["t"],
    "v": ["v"],
    "y": ["j"],
    "z": ["z"],

    # --- No official digraphs in Turkish ---
    # (Turkish orthography is nearly 1:1 with phonemes)
}

ALLOPHONES = {
    "p": ["p"], "b": ["b", "p"],  # final devoicing
    "t": ["t"], "d": ["d", "t"],
    "k": ["k"], "c": ["c"],
    "ɡ": ["ɡ", "k"], "ɟ": ["ɟ", "c"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ", "tʃ"],
    "f": ["f"], "v": ["v", "f"],
    "s": ["s"], "z": ["z", "s"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ", "ʃ"],
    "h": ["h", "ç", "x"],  # /ç/ before front V, /x/ before back V
    "m": ["m"], "n": ["n", "ŋ"],
    "l": ["l", "ɫ"],
    "ɾ": ["ɾ", "r"],
    "j": ["j"],
    "a": ["a"], "e": ["e"], "ɯ": ["ɯ"], "i": ["i"],
    "o": ["o"], "ø": ["ø"], "u": ["u"], "y": ["y"],
}

SPECS = {
    "tr": LanguageSpec(
        code="tr",
        name="Turkish",
        family="Turkic",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        notes=(
            "Standard Istanbul Turkish. Near-transparent orthography. "
            "8-vowel system with front/back × rounded/unrounded × "
            "high/low vowel harmony."
        ),
    ),
}
