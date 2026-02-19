"""Catalan (ca) — grapheme→IPA and allophone mappings.

Sources:
- Carbonell, J.F. & Llisterri, J. (1992). Catalan. *JIPA* 22(1-2).
- Wheeler, M.W. (2005). *The Phonology of Catalan*.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels (7 stressed, reduced unstressed) ---
    "a": ["a", "ə"],
    "e": ["e", "ɛ", "ə"],
    "i": ["i"],
    "o": ["o", "ɔ", "u"],
    "u": ["u"],
    "à": ["a"], "è": ["ɛ"], "é": ["e"],
    "í": ["i"], "ò": ["ɔ"], "ó": ["o"], "ú": ["u"],
    "ï": ["i"], "ü": ["u"],  # diaeresis = hiatus

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "s"],
    "ç": ["s"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "ʒ"],  # /ʒ/ before e,i
    "h": [""],
    "j": ["ʒ"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],
    "r": ["ɾ", "r"],  # tap / trill
    "s": ["s", "z"],
    "t": ["t"],
    "v": ["b"],  # merged with /b/ in most Central Catalan
    "w": ["w"],
    "x": ["ʃ", "ks"],  # /ʃ/ initial; /ks/ medial
    "z": ["z"],

    # --- Digraphs ---
    "ig": ["tʃ"],  # word-final: ⟨ig⟩ = [tʃ]
    "ix": ["ʃ"],  # after vowel
    "ll": ["ʎ"],
    "l·l": ["lː"],  # ela geminada
    "ny": ["ɲ"],
    "qu": ["k", "kw"],
    "gu": ["ɡ", "ɡw"],
    "rr": ["r"],
    "ss": ["s"],
    "tg": ["dʒ"],  # before e,i
    "tj": ["dʒ"],
    "tx": ["tʃ"],

    # --- Diphthongs (falling) ---
    "ai": ["aj"], "ei": ["əj"], "oi": ["ɔj"], "ui": ["uj"],
    "au": ["aw"], "eu": ["əw"], "ou": ["ɔw"], "iu": ["iw"],
    # Rising
    "ua": ["wa"], "ue": ["wɛ"], "uo": ["wɔ"],
    "ia": ["ja"], "ie": ["jɛ"], "io": ["jɔ"],
}

ALLOPHONES = {
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
    "p": ["p"], "t": ["t"], "k": ["k"],
    "f": ["f"], "v": ["v", "β"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ"],
    "m": ["m", "ɱ"],
    "n": ["n", "m", "ɱ", "ŋ", "ɲ"],
    "ɲ": ["ɲ"], "ŋ": ["ŋ"],
    "l": ["l"], "ʎ": ["ʎ"], "lː": ["lː"],
    "ɾ": ["ɾ"], "r": ["r"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "ə": ["ə"],
    "e": ["e"], "ɛ": ["ɛ"],
    "i": ["i"],
    "o": ["o"], "ɔ": ["ɔ"],
    "u": ["u"],
}

SPECS = {
    "ca": LanguageSpec(
        code="ca",
        name="Catalan",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="la",
        notes=(
            "Central Catalan (Barcelona standard). Vowel reduction "
            "(a,e→[ə], o→[u] in unstressed) is systematic. "
            "⟨l·l⟩ (ela geminada) is a unique Catalan digraph."
        ),
    ),
}
