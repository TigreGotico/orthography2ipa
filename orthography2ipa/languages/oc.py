"""Occitan (oc) — grapheme→IPA and allophone mappings.

Sources:
- Sumien, D. (2006). *La standardisation pluricentrique de l'occitan*.
- Bec, P. (1973). *Manuel pratique d'occitan moderne*.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels ---
    "a": ["a", "ɔ"],  # [ɔ] in unstressed final (Languedocien)
    "e": ["e", "ɛ"],
    "i": ["i"],
    "o": ["u", "ɔ"],  # [u] in many dialects
    "u": ["y"],  # front rounded, as in French
    "à": ["a"], "è": ["ɛ"], "é": ["e"],
    "í": ["i"], "ò": ["ɔ"], "ó": ["o"], "ú": ["y"],
    "ü": ["y"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "s"],
    "ç": ["s"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "dʒ"],  # /dʒ/ before e,i
    "h": [""],
    "j": ["dʒ"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],
    "r": ["r", "ɾ"],
    "s": ["s", "z"],
    "t": ["t"],
    "v": ["v", "b"],
    "x": ["ks", "s"],
    "z": ["z"],

    # --- Digraphs ---
    "ch": ["tʃ"],
    "lh": ["ʎ"],
    "nh": ["ɲ"],
    "qu": ["k", "kw"],
    "gu": ["ɡ", "ɡw"],
    "rr": ["r"],
    "ss": ["s"],
    "gn": ["ɲ"],
    "th": ["t"],
    "ph": ["f"],

    # --- Diphthongs ---
    "ai": ["aj"], "au": ["aw"], "ei": ["ej"], "eu": ["ew"],
    "oi": ["uj"], "ou": ["ow"], "iu": ["jy"], "ui": ["yj"],
}

ALLOPHONES = {
    "b": ["b", "β"], "d": ["d", "ð"], "ɡ": ["ɡ", "ɣ"],
    "p": ["p"], "t": ["t"], "k": ["k"],
    "f": ["f"], "v": ["v"], "s": ["s"], "z": ["z"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ"],
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "ʎ": ["ʎ"],
    "ɾ": ["ɾ"], "r": ["r"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "e": ["e"], "ɛ": ["ɛ"],
    "i": ["i"], "o": ["o"], "ɔ": ["ɔ"],
    "u": ["u"], "y": ["y"],
}

SPECS = {
    "oc": LanguageSpec(
        code="oc",
        name="Occitan",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="la",
        notes=(
            "Based on Languedocien/general Occitan norms. "
            "Substantial dialectal variation across Gascon, Provençal, "
            "Limousin, Auvergnat, and Vivaro-Alpine."
        ),
    ),
}
