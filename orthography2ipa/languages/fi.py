"""Finnish (fi) — grapheme→IPA and allophone mappings.

Sources:
- Suomi, K. et al. (2008). *Finnish Sound Structure*.
- Karlsson, F. (1999). *Finnish: An Essential Grammar*.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels (8 monophthongs, short/long) ---
    "a": ["ɑ"], "aa": ["ɑː"],
    "e": ["e"], "ee": ["eː"],
    "i": ["i"], "ii": ["iː"],
    "o": ["o"], "oo": ["oː"],
    "u": ["u"], "uu": ["uː"],
    "y": ["y"], "yy": ["yː"],
    "ä": ["æ"], "ää": ["æː"],
    "ö": ["ø"], "öö": ["øː"],

    # --- Consonants ---
    "b": ["b"],  # loanwords
    "c": ["k", "s"],  # loanwords
    "d": ["d"],
    "f": ["f"],  # loanwords
    "g": ["ɡ"],  # loanwords; native only in ⟨ng⟩
    "h": ["h"],
    "j": ["j"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "r": ["r"],
    "s": ["s"],
    "t": ["t"],
    "v": ["ʋ"],
    "w": ["ʋ"],  # variant of v
    "z": ["ts"],  # loanwords

    # --- Geminate consonants (phonemic length) ---
    "kk": ["kː"], "pp": ["pː"], "tt": ["tː"],
    "ll": ["lː"], "mm": ["mː"], "nn": ["nː"],
    "rr": ["rː"], "ss": ["sː"],

    # --- Digraph ---
    "ng": ["ŋː"],  # geminate velar nasal (phonemic)
    "nk": ["ŋk"],

    # --- Diphthongs (official 18) ---
    "ai": ["ɑi"], "ei": ["ei"], "oi": ["oi"], "ui": ["ui"],
    "yi": ["yi"], "äi": ["æi"], "öi": ["øi"],
    "au": ["ɑu"], "eu": ["eu"], "ou": ["ou"], "iu": ["iu"],
    "äy": ["æy"], "öy": ["øy"],
    "ie": ["ie"], "uo": ["uo"], "yö": ["yø"],
    "ey": ["ey"], "iy": ["iy"],
}

ALLOPHONES = {
    "p": ["p"], "t": ["t"], "k": ["k"],
    "d": ["d", "ɾ"],  # dialectal tap
    "b": ["b"], "ɡ": ["ɡ"], "f": ["f"],
    "s": ["s"], "h": ["h", "ç", "x", "ɦ"],  # varies by context
    "ʋ": ["ʋ", "w"],
    "m": ["m"], "n": ["n", "ŋ"], "ŋ": ["ŋ"],
    "l": ["l"], "r": ["r"], "j": ["j"],
    "ɑ": ["ɑ"], "e": ["e"], "i": ["i"],
    "o": ["o"], "u": ["u"], "y": ["y"],
    "æ": ["æ"], "ø": ["ø"],
}

SPECS = {
    "fi": LanguageSpec(
        code="fi",
        name="Finnish",
        family="Uralic",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        notes=(
            "Standard Finnish. Highly transparent orthography. "
            "Phonemic consonant and vowel length. "
            "18 diphthongs are all phonemic."
        ),
    ),
}
