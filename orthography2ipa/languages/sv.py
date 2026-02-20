"""Swedish (sv) — grapheme→IPA and allophone mappings.

Sources:
- Engstrand, O. (1999). Swedish. *Handbook of the IPA*.
- Riad, T. (2014). *The Phonology of Swedish*.
"""

from orthography2ipa.types import Ancestor, AncestorRole

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels (9 qualities, short/long) ---
    "a": ["a", "ɑː"],
    "e": ["ɛ", "eː"],
    "i": ["ɪ", "iː"],
    "o": ["ɔ", "uː"],  # ⟨o⟩ = [uː] when long in many words
    "u": ["ɵ", "ʉː"],
    "y": ["ʏ", "yː"],
    "å": ["ɔ", "oː"],
    "ä": ["ɛ", "ɛː"],
    "ö": ["œ", "øː"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "s"],  # /s/ before e,i,y,ä,ö
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "j"],  # /j/ before front vowels
    "h": ["h"],
    "j": ["j"],
    "k": ["k", "ɕ"],  # /ɕ/ before front vowels
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],
    "r": ["r", "ɾ"],
    "s": ["s"],
    "t": ["t"],
    "v": ["v"],
    "w": ["v"],
    "x": ["ks"],
    "z": ["s"],

    # --- Consonant digraphs ---
    "ch": ["ɕ", "ʃ"],
    "ck": ["k"],
    "dj": ["j"],
    "gj": ["j"],
    "gn": ["ɡn"],  # not palatal in Swedish
    "lj": ["j"],
    "ng": ["ŋ"],
    "nk": ["ŋk"],
    "sj": ["ɧ"],  # sj-sound
    "sk": ["ɧ", "sk"],  # /ɧ/ before front V; /sk/ elsewhere
    "tj": ["ɕ"],

    # --- Trigraphs ---
    "skj": ["ɧ"],
    "stj": ["ɧ"],
    "sch": ["ʃ"],  # loanwords

    # --- Retroflexes (r + dental → retroflex) ---
    "rd": ["ɖ"],
    "rl": ["ɭ"],
    "rn": ["ɳ"],
    "rs": ["ʂ"],
    "rt": ["ʈ"],
}

ALLOPHONES = {
    "p": ["p", "pʰ"],
    "b": ["b"],
    "t": ["t", "tʰ"],
    "d": ["d"],
    "k": ["k", "kʰ"],
    "ɡ": ["ɡ"],

    "f": ["f"],
    "v": ["v"],
    "s": ["s"],
    "ɕ": ["ɕ"],
    "ɧ": ["ɧ", "ʂ", "x"],  # highly variable across dialects
    "h": ["h"],

    "m": ["m"],
    "n": ["n", "ŋ"],
    "ŋ": ["ŋ"],

    "l": ["l"],
    "r": ["r", "ɾ", "ʁ"],  # uvular in Malmö/southern dialects
    "j": ["j"],

    # Retroflexes
    "ɖ": ["ɖ"], "ɭ": ["ɭ"], "ɳ": ["ɳ"], "ʂ": ["ʂ"], "ʈ": ["ʈ"],

    "a": ["a"], "ɑː": ["ɑː"],
    "ɛ": ["ɛ"], "eː": ["eː"],
    "ɪ": ["ɪ"], "iː": ["iː"],
    "ɔ": ["ɔ"], "oː": ["oː"], "uː": ["uː"],
    "ɵ": ["ɵ"], "ʉː": ["ʉː"],
    "ʏ": ["ʏ"], "yː": ["yː"],
    "œ": ["œ"], "øː": ["øː"],
    "ɛː": ["ɛː"],
}

SPECS = {
    "sv": LanguageSpec(
        code="sv",
        name="Swedish",
        family="Germanic",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="gem",
        ancestors=(
            Ancestor("non", P, 0.90,
                     "Descent from Old Norse (East Norse branch)"),
            Ancestor("de", AD, 0.06,
                     "Low German / Hanseatic adstrate: massive vocabulary "
                     "borrowing in late medieval period"),
            Ancestor("fi", AD, 0.02,
                     "Finnish adstrate: minor, in border areas"),
        ),
        notes=(
            "Central Standard Swedish. Retroflex assimilation "
            "(⟨rd⟩→[ɖ] etc.) is characteristic of Central/Northern "
            "dialects; absent in Southern/Finland Swedish."
        ),
    ),
}
