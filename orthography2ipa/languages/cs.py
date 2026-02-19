"""Czech (cs) — grapheme→IPA and allophone mappings.

Sources:
- Dankovičová, J. (1999). Czech. *Handbook of the IPA*.
- Palková, Z. (1994). *Fonetika a fonologie češtiny*.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels (short / long) ---
    "a": ["a"], "á": ["aː"],
    "e": ["ɛ"], "é": ["ɛː"],
    "ě": ["jɛ"],  # iotated e (palatalises preceding C)
    "i": ["ɪ"], "í": ["iː"],
    "o": ["o"], "ó": ["oː"],
    "u": ["u"], "ú": ["uː"],
    "ů": ["uː"],  # ring-u, same as ⟨ú⟩ phonemically
    "y": ["ɪ"], "ý": ["iː"],  # same phoneme as ⟨i⟩/⟨í⟩

    # --- Consonants ---
    "b": ["b"],
    "c": ["ts"],
    "č": ["tʃ"],
    "d": ["d"],
    "ď": ["ɟ"],
    "f": ["f"],
    "g": ["ɡ"],
    "h": ["ɦ"],  # voiced glottal fricative
    "j": ["j"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "ň": ["ɲ"],
    "p": ["p"],
    "q": ["kv"],
    "r": ["r"],
    "ř": ["r̝"],  # raised alveolar trill (unique to Czech)
    "s": ["s"],
    "š": ["ʃ"],
    "t": ["t"],
    "ť": ["c"],  # palatal stop
    "v": ["v"],
    "w": ["v"],
    "x": ["ks"],
    "z": ["z"],
    "ž": ["ʒ"],

    # --- Digraphs ---
    "ch": ["x"],  # voiceless velar fricative
    "dž": ["dʒ"],

    # --- Diphthongs ---
    "ou": ["ou"],
    "au": ["au"],  # in loanwords
    "eu": ["eu"],  # in loanwords
}

ALLOPHONES = {
    "p": ["p"], "b": ["b", "p"],
    "t": ["t"], "d": ["d", "t"],
    "c": ["c"], "ɟ": ["ɟ", "c"],
    "k": ["k"], "ɡ": ["ɡ", "k"],
    "f": ["f"], "v": ["v", "f"],
    "s": ["s"], "z": ["z", "s"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ", "ʃ"],
    "x": ["x"], "ɦ": ["ɦ", "x"],  # devoiced before voiceless
    "ts": ["ts"], "tʃ": ["tʃ"],
    "dʒ": ["dʒ", "tʃ"],
    "r": ["r"], "r̝": ["r̝", "r̝̊"],  # devoiced variant
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "j": ["j"],
    "a": ["a"], "aː": ["aː"],
    "ɛ": ["ɛ"], "ɛː": ["ɛː"],
    "ɪ": ["ɪ"], "iː": ["iː"],
    "o": ["o"], "oː": ["oː"],
    "u": ["u"], "uː": ["uː"],
}

SPECS = {
    "cs": LanguageSpec(
        code="cs",
        name="Czech",
        family="Slavic",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="ine",
        notes=(
            "Standard Czech. Notable for the unique phoneme /r̝/ (⟨ř⟩) "
            "and systematic vowel length contrast. ⟨ch⟩ is the only "
            "official digraph and sorts as a separate letter."
        ),
    ),
}
