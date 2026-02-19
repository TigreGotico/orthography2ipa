"""Galician (gl) — grapheme→IPA and allophone mappings.

Sources:
- Regueira, X.L. (1996). Galician. *JIPA* 26(2).
- RAG (2003). *Normas ortográficas e morfolóxicas do idioma galego*.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels (7-vowel system) ---
    "a": ["a", "ɐ"],
    "e": ["e", "ɛ"],
    "i": ["i"],
    "o": ["o", "ɔ"],
    "u": ["u"],
    "á": ["a"], "é": ["ɛ"], "ê": ["e"], "í": ["i"],
    "ó": ["ɔ"], "ô": ["o"], "ú": ["u"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "θ"],  # /θ/ before e,i (seseo/ceceo varies)
    "ç": ["s"],  # historical
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "ʃ"],  # /ʃ/ before e,i (gheada variant: /h/)
    "h": [""],  # silent
    "j": ["ʃ"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "ñ": ["ɲ"],
    "p": ["p"],
    "q": ["k"],
    "r": ["ɾ"],
    "s": ["s"],
    "t": ["t"],
    "v": ["b"],  # merged with /b/ in standard
    "x": ["ʃ"],
    "z": ["θ"],

    # --- Digraphs ---
    "ch": ["tʃ"],
    "ll": ["ʎ"],  # no yeísmo in standard Galician
    "nh": ["ɲ"],  # alternative spelling
    "rr": ["r"],  # alveolar trill
    "qu": ["k"],
    "gu": ["ɡ"],
    "ss": ["s"],

    # --- Diphthongs ---
    "ai": ["aj"], "au": ["aw"], "ei": ["ej"], "eu": ["ew"],
    "oi": ["oj"], "ou": ["ow"], "ui": ["uj"], "iu": ["iw"],
    "ia": ["ja"], "ie": ["je"], "io": ["jo"],
    "ua": ["wa"], "ue": ["we"], "uo": ["wo"],

    # --- Nasal sequences ---
    "ão": ["ɐ̃w̃"],  # in some traditional spellings
}

ALLOPHONES = {
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
    "p": ["p"], "t": ["t"], "k": ["k"],
    "f": ["f"], "v": ["β"], "s": ["s", "z"],
    "θ": ["θ"], "ʃ": ["ʃ"],
    "tʃ": ["tʃ"],
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "ʎ": ["ʎ"],
    "ɾ": ["ɾ"], "r": ["r"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "ɐ": ["ɐ"],
    "e": ["e"], "ɛ": ["ɛ"],
    "i": ["i"],
    "o": ["o"], "ɔ": ["ɔ"],
    "u": ["u"],
}

SPECS = {
    "gl": LanguageSpec(
        code="gl",
        name="Galician",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="la",
        notes="Standard Galician per RAG norms. Gheada not reflected in standard.",
    ),
}
