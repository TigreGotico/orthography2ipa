"""Croatian (hr) — grapheme→IPA and allophone mappings.

Sources:
- Browne, W. & Alt, T. (2004). *A Handbook of Bosnian, Serbian, and Croatian*. SEELRC.
- Škarić, I. (1991). *Fonetika hrvatskoga književnog jezika*.
- Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*.
"""
from orthography2ipa.types import LanguageSpec

# Croatian uses exclusively the Latin/Gaj script.
GRAPHEMES = {
    # --- Vowels ---
    "a": ["a"],
    "e": ["ɛ"],  # phonemically /e/ but realised [ɛ]
    "i": ["i"],
    "o": ["ɔ"],
    "u": ["u"],

    # --- Syllabic r ---
    "r": ["r", "r̩"],  # syllabic in certain clusters (e.g. prst, trg)

    # --- Consonants ---
    "b": ["b"],
    "c": ["ts"],
    "č": ["tʃ"],
    "ć": ["tɕ"],  # distinct from č (softer, palatal)
    "d": ["d"],
    "dž": ["dʒ"],  # distinct from đ
    "đ": ["dʑ"],  # softer palatal affricate
    "f": ["f"],
    "g": ["ɡ"],
    "h": ["x"],
    "j": ["j"],
    "k": ["k"],
    "l": ["l"],
    "lj": ["ʎ"],
    "m": ["m"],
    "n": ["n"],
    "nj": ["ɲ"],
    "p": ["p"],
    "s": ["s"],
    "š": ["ʃ"],
    "t": ["t"],
    "v": ["v"],
    "z": ["z"],
    "ž": ["ʒ"],
}

ALLOPHONES = {
    "p": ["p"], "b": ["b", "p"],
    "t": ["t"], "d": ["d", "t"],
    "k": ["k"], "ɡ": ["ɡ", "k"],
    "f": ["f"], "v": ["v", "f"],
    "s": ["s"], "z": ["z", "s"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ", "ʃ"],
    "x": ["x"],
    "ts": ["ts"],
    "tʃ": ["tʃ"], "tɕ": ["tɕ"],
    "dʒ": ["dʒ", "tʃ"], "dʑ": ["dʑ", "tɕ"],
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "ʎ": ["ʎ"],
    "r": ["r"], "r̩": ["r̩"],
    "j": ["j"],
    "a": ["a"], "ɛ": ["ɛ"], "i": ["i"], "ɔ": ["ɔ"], "u": ["u"],
}

SPECS = {
    "hr": LanguageSpec(
        code="hr",
        name="Croatian",
        family="Slavic",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="sla",
        notes=(
            "Standard Croatian (Štokavian Ijekavian dialect basis). "
            "Latin script only (unlike Serbian). "
            "Shares the two palatal affricate pairs with Serbian: "
            "⟨ć⟩ = [tɕ] (softer), ⟨č⟩ = [tʃ] (harder); "
            "⟨đ⟩ = [dʑ], ⟨dž⟩ = [dʒ]. "
            "Four-pitch-accent system. Syllabic /r̩/ (e.g. *prst* 'finger'). "
            "Ijekavian: Proto-Slavic yat /æː/ → ije/je (vs Serbian Ekavian e)."
        ),
    ),
}
