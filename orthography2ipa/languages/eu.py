"""Basque / Euskara (eu) — grapheme→IPA and allophone mappings.

Sources:
- Hualde, J.I. (1991). *Basque Phonology*.
- Hualde, J.I. & Ortiz de Urbina, J. (2003). *A Grammar of Basque*.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels (5-vowel system) ---
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],

    # --- Consonants ---
    "b": ["b"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ"],
    "h": ["h"],  # aspirated in some dialects; silent in others
    "j": ["j", "x"],  # /j/ standard; /x/ in some dialects
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "ñ": ["ɲ"],
    "p": ["p"],
    "r": ["ɾ"],  # single tap
    "s": ["s̺"],  # apico-alveolar
    "t": ["t"],
    "x": ["ʃ"],
    "z": ["s̻"],  # lamino-alveolar

    # --- Digraphs ---
    "dd": ["ɟ"],  # palatal stop
    "ll": ["ʎ"],  # palatal lateral
    "rr": ["r"],  # alveolar trill
    "ts": ["ts̻"],  # lamino-alveolar affricate
    "tz": ["ts̻"],  # alternate spelling
    "tx": ["tʃ"],  # post-alveolar affricate
    "tt": ["c"],  # palatal stop (voiceless)

    # --- Diphthongs ---
    "ai": ["ai"], "ei": ["ei"], "oi": ["oi"],
    "au": ["au"], "eu": ["eu"],
    "ui": ["ui"],
}

ALLOPHONES = {
    "b": ["b", "β"],  # [β] intervocalic
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
    "p": ["p"], "t": ["t"], "k": ["k"],
    "c": ["c"], "ɟ": ["ɟ"],
    "f": ["f"],
    "s̺": ["s̺"],  # apical
    "s̻": ["s̻"],  # laminal
    "ʃ": ["ʃ"],
    "ts̻": ["ts̻"], "tʃ": ["tʃ"],
    "x": ["x"], "h": ["h"],
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "ʎ": ["ʎ"],
    "ɾ": ["ɾ"], "r": ["r"],
    "j": ["j"],

    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
}

SPECS = {
    "eu": LanguageSpec(
        code="eu",
        name="Basque (Euskara)",
        family="Isolate",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="xaq",
        notes=("Standard Basque (Euskara Batua). Notable for apical/laminal "
               "sibilant contrast (/s̺/ vs /s̻/) and three affricate series. "
               "Dialectal variation is extensive."
               ),
    ),
}
