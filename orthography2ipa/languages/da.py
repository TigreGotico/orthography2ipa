"""Danish (da) — grapheme→IPA and allophone mappings.

Sources:
- Grønnum, N. (1998). Danish. *JIPA* 28(1-2).
- Basbøll, H. (2005). *The Phonology of Danish*.
"""

from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE

GRAPHEMES = {
    # --- Vowels ---
    "a": ["a", "æ", "ɑː"],
    "e": ["e", "ɛ", "ə"],
    "i": ["i", "ɪ"],
    "o": ["o", "ɔ"],
    "u": ["u", "ʊ"],
    "y": ["y", "ʏ"],
    "æ": ["ɛ", "ɛː"],
    "ø": ["ø", "œ"],
    "å": ["ɔ", "ɔː"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "s"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ"],
    "h": ["h"],
    "j": ["j"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],
    "r": ["ʁ"],
    "s": ["s"],
    "t": ["t"],
    "v": ["v"],
    "w": ["v"],
    "x": ["ks"],
    "z": ["s"],

    # --- Consonant digraphs ---
    "ch": ["ɕ", "k"],
    "ng": ["ŋ"],
    "nk": ["ŋk"],
    "sj": ["ɕ"],
    "sk": ["ɕ", "sk"],  # /ɕ/ before front vowels
    "kj": ["ɕ"],
    "tj": ["ɕ"],

    # --- Vowel digraphs ---
    "aa": ["ɔː"],  # older spelling of ⟨å⟩
    "aj": ["aj"],
    "ej": ["aj"],
    "øj": ["ɔj"],

    # --- Diphthongs ---
    "au": ["ɑw"],
    "av": ["ɑw"],  # v → [w] in diphthong
    "eu": ["ew"],
    "eg": ["aj"],  # word-final ⟨eg⟩
    "øg": ["ɔj"],  # word-final ⟨øg⟩
    "ig": ["iː"],  # word-final ⟨ig⟩
}

ALLOPHONES = {
    "p": ["p", "pʰ", "b̥"],  # aspirated initially; unaspirated after /s/
    "b": ["b", "b̥"],
    "t": ["t", "tʰ", "d̥"],
    "d": ["d", "ð", "d̥"],  # soft d [ð] is pervasive intervocalic
    "k": ["k", "kʰ", "ɡ̊"],
    "ɡ": ["ɡ", "ɡ̊"],

    "f": ["f"],
    "v": ["v", "w"],  # [w] in diphthong context
    "s": ["s"],
    "ɕ": ["ɕ"],
    "h": ["h"],
    "ð": ["ð"],  # soft d (not a fricative but approximant [ð̞])

    "ʁ": ["ʁ", "ɐ̯"],  # vocalised in coda

    "m": ["m"],
    "n": ["n", "ŋ"],
    "ŋ": ["ŋ"],
    "l": ["l"],
    "j": ["j"],

    "a": ["a", "æ"],
    "ɑː": ["ɑː"],
    "ɛ": ["ɛ"], "ɛː": ["ɛː"],
    "e": ["e"], "eː": ["eː"],
    "ə": ["ə"],
    "i": ["i"], "iː": ["iː"],
    "ɪ": ["ɪ"],
    "o": ["o"], "oː": ["oː"],
    "ɔ": ["ɔ"], "ɔː": ["ɔː"],
    "u": ["u"], "uː": ["uː"],
    "ʊ": ["ʊ"],
    "y": ["y"], "yː": ["yː"],
    "ʏ": ["ʏ"],
    "ø": ["ø"], "øː": ["øː"],
    "œ": ["œ"],
}

SPECS = {
    "da": LanguageSpec(
        code="da",
        name="Danish",
        family="Germanic",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="gem",
        ancestors=(
            Ancestor("non", P, 0.90,
                     "Descent from Old Norse (East Norse branch)"),
            Ancestor("de-DE", AD, 0.07,
                     "Low German / Hanseatic adstrate: even stronger than Swedish "
                     "due to geographic proximity and political union"),
        ),
        notes=(
            "Standard Danish (rigsdansk). The 'soft d' [ð̞] is an "
            "approximant unique to Danish. Stød (glottal prosody) not "
            "encoded in grapheme map as it is suprasegmental."
        ),
    ),
}
