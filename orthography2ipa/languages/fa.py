"""Persian / Farsi (fa) — grapheme→IPA and allophone mappings.

Sources:
- Majidi, M.-R. & Ternes, E. (1999). Persian (Farsi). *JIPA* 29(2).
- Bijankhan, M. (2018). *Persian Phonology and Morphology*.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Consonants ---
    "ا": ["ʔ", "ɒː"],  # alef: glottal stop or long /ɒː/
    "آ": ["ʔɒː"],
    "ب": ["b"],
    "پ": ["p"],
    "ت": ["t"],
    "ث": ["s"],  # merged with /s/ in modern Persian
    "ج": ["dʒ"],
    "چ": ["tʃ"],
    "ح": ["h"],  # merged with /h/ in modern Persian
    "خ": ["x"],
    "د": ["d"],
    "ذ": ["z"],  # merged with /z/
    "ر": ["ɾ"],
    "ز": ["z"],
    "ژ": ["ʒ"],
    "س": ["s"],
    "ش": ["ʃ"],
    "ص": ["s"],  # merged with /s/
    "ض": ["z"],  # merged with /z/
    "ط": ["t"],  # merged with /t/
    "ظ": ["z"],  # merged with /z/
    "ع": ["ʔ"],  # glottal stop (pharyngeal lost)
    "غ": ["ɣ", "ɢ"],
    "ف": ["f"],
    "ق": ["ɣ", "ɢ"],  # merged with غ in most dialects
    "ک": ["k"],
    "گ": ["ɡ"],
    "ل": ["l"],
    "م": ["m"],
    "ن": ["n"],
    "و": ["v", "uː", "ow"],  # consonantal or vowel
    "ه": ["h", "e"],  # /h/ or silent (marking final /e/)
    "ی": ["j", "iː"],  # consonantal or vowel

    # --- Short vowels (diacritics, usually unwritten) ---
    "\u064E": ["æ"],  # fatḥa = /æ/ in Persian
    "\u0650": ["e"],  # kasra = /e/
    "\u064F": ["o"],  # ḍamma = /o/

    # --- Common suffixes / clitics (orthographic units) ---
    "ها": ["hɒː"],  # plural marker
}

ALLOPHONES = {
    "p": ["p", "pʰ"], "b": ["b"],
    "t": ["t", "tʰ"], "d": ["d"],
    "k": ["k", "kʰ"], "ɡ": ["ɡ"],
    "ʔ": ["ʔ"],

    "f": ["f"], "v": ["v"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "x": ["x"], "ɣ": ["ɣ", "ʁ"],
    "h": ["h"],

    "tʃ": ["tʃ"], "dʒ": ["dʒ"],

    "m": ["m"], "n": ["n", "ŋ"],
    "l": ["l"],
    "ɾ": ["ɾ", "r"],  # trill in emphatic / geminate
    "j": ["j"],

    # 6-vowel system
    "ɒː": ["ɒː"],  # long open back
    "æ": ["æ"],  # short open front
    "e": ["e"],
    "o": ["o"],
    "iː": ["iː"],
    "uː": ["uː"],
}

SPECS = {
    "fa": LanguageSpec(
        code="fa",
        name="Persian (Farsi)",
        family="Iranian",
        script="Arabic",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="ine", notes=(
            "Tehran standard. Many Arabic emphatic/pharyngeal consonants "
            "have merged with plain counterparts. 6-vowel system: "
            "/ɒː, æ, e, o, iː, uː/."
        ),
    ),
}
