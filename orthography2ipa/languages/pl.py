"""Polish (pl) — grapheme→IPA and allophone mappings.

Sources:
- Jassem, W. (2003). Polish. *JIPA* 33(1).
- Gussmann, E. (2007). *The Phonology of Polish*.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels ---
    "a": ["a"],
    "ą": ["ɔ̃", "ɔw̃", "ɔm", "ɔn", "ɔŋ"],  # nasal; realisation varies by context
    "e": ["ɛ"],
    "ę": ["ɛ̃", "ɛw̃", "ɛm", "ɛn", "ɛŋ"],  # nasal
    "i": ["i"],
    "o": ["ɔ"],
    "ó": ["u"],  # same phoneme as ⟨u⟩
    "u": ["u"],
    "y": ["ɨ"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["ts"],
    "ć": ["tɕ"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ"],
    "h": ["x"],  # same as ⟨ch⟩
    "j": ["j"],
    "k": ["k"],
    "l": ["l"],
    "ł": ["w"],  # modern Polish: labio-velar approximant
    "m": ["m"],
    "n": ["n"],
    "ń": ["ɲ"],
    "p": ["p"],
    "r": ["r"],
    "s": ["s"],
    "ś": ["ɕ"],
    "t": ["t"],
    "w": ["v"],
    "z": ["z"],
    "ź": ["ʑ"],
    "ż": ["ʐ"],

    # --- Digraphs ---
    "ch": ["x"],
    "cz": ["tʂ"],
    "dz": ["dz"],
    "dź": ["dʑ"],
    "dż": ["dʐ"],
    "rz": ["ʐ"],  # same phoneme as ⟨ż⟩
    "sz": ["ʂ"],
    "ni": ["ɲi"],  # before vowel: palatalised /ɲ/
    "ci": ["tɕi"],
    "si": ["ɕi"],
    "zi": ["ʑi"],
    "dzi": ["dʑi"],

    # --- Consonant clusters (not digraphs but common) ---
    "szcz": ["ʂtʂ"],  # official trigraph
}

ALLOPHONES = {
    "p": ["p"], "b": ["b", "p"],  # final devoicing
    "t": ["t"], "d": ["d", "t"],
    "k": ["k"], "ɡ": ["ɡ", "k"],
    "f": ["f"], "v": ["v", "f"],
    "s": ["s"], "z": ["z", "s"],
    "ʂ": ["ʂ"], "ʐ": ["ʐ", "ʂ"],
    "ɕ": ["ɕ"], "ʑ": ["ʑ", "ɕ"],
    "x": ["x"],
    "ts": ["ts"], "dz": ["dz", "ts"],
    "tʂ": ["tʂ"], "dʐ": ["dʐ", "tʂ"],
    "tɕ": ["tɕ"], "dʑ": ["dʑ", "tɕ"],
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "w": ["w"],
    "r": ["r", "ɾ"],
    "j": ["j"],
    "a": ["a"], "ɛ": ["ɛ"], "ɔ": ["ɔ"],
    "i": ["i"], "u": ["u"], "ɨ": ["ɨ"],
}

SPECS = {
    "pl": LanguageSpec(
        code="pl",
        name="Polish",
        family="Slavic",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="ine",
        notes=(
            "Standard Polish. Three sibilant series: alveolar /s z ts dz/, "
            "retroflex /ʂ ʐ tʂ dʐ/, alveolo-palatal /ɕ ʑ tɕ dʑ/. "
            "Nasal vowels ⟨ą ę⟩ realise as VN sequences before stops."
        ),
    ),
}
