"""Romanian (ro) — grapheme→IPA and allophone mappings.

Sources:
- Chițoran, I. (2001). *The Phonology of Romanian*.
- Sarlin, M. (2014). Romanian. *JIPA* 44(1).
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels ---
    "a": ["a"],
    "ă": ["ə"],
    "â": ["ɨ"],
    "e": ["e", "ɛ"],
    "i": ["i"],
    "î": ["ɨ"],  # same phoneme as ⟨â⟩
    "o": ["o"],
    "u": ["u"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "tʃ"],  # /tʃ/ before e,i
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "dʒ"],  # /dʒ/ before e,i
    "h": ["h"],
    "j": ["ʒ"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],
    "r": ["r"],
    "s": ["s"],
    "ș": ["ʃ"],
    "t": ["t"],
    "ț": ["ts"],
    "v": ["v"],
    "w": ["v", "w"],
    "x": ["ks", "ɡz"],
    "y": ["i", "j"],
    "z": ["z"],

    # --- Digraphs ---
    "ch": ["k"],  # before e,i: ⟨che⟩ = [ke]
    "gh": ["ɡ"],  # before e,i: ⟨ghe⟩ = [ɡe]
    "ce": ["tʃe"], "ci": ["tʃi"],
    "ge": ["dʒe"], "gi": ["dʒi"],

    # --- Diphthongs ---
    "ea": ["e̯a"], "oa": ["o̯a"],
    "ai": ["aj"], "ei": ["ej"], "oi": ["oj"], "ui": ["uj"],
    "au": ["aw"], "eu": ["ew"], "ou": ["ow"],
    "ia": ["ja"], "ie": ["je"], "io": ["jo"], "iu": ["ju"],
    "ua": ["wa"], "ue": ["we"],

    # --- Triphthongs ---
    "eau": ["e̯aw"],
    "eai": ["e̯aj"],
    "oai": ["o̯aj"],
    "iai": ["jaj"],
}

ALLOPHONES = {
    "b": ["b"], "d": ["d"], "ɡ": ["ɡ"],
    "p": ["p"], "t": ["t"], "k": ["k"],
    "f": ["f"], "v": ["v"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "ts": ["ts"], "tʃ": ["tʃ"], "dʒ": ["dʒ"],
    "h": ["h", "x"],
    "m": ["m"], "n": ["n", "ŋ"],
    "l": ["l"], "r": ["r", "ɾ"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "ə": ["ə"], "ɨ": ["ɨ"],
    "e": ["e"], "ɛ": ["ɛ"], "i": ["i"],
    "o": ["o"], "u": ["u"],
}

SPECS = {
    "ro": LanguageSpec(
        code="ro",
        name="Romanian",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="la",
        notes=(
            "Standard Romanian. Notable for central vowels /ə, ɨ/, "
            "and rich diphthong/triphthong system."
        ),
    ),
}
