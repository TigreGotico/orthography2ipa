"""Slovenian (sl) — grapheme→IPA and allophone mappings.

Sources:
- Šuštaršič, R., Komar, S. & Petek, B. (1999). Slovene. *Handbook of the IPA*.
- Priestly, T. (1993). 'Slovene' in *The Slavonic Languages* (ed. Comrie & Corbett).
- Toporišič, J. (2000). *Slovenska slovnica* (4th ed.).
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels ---
    "a": ["a"],
    "e": ["ɛ", "e"],  # open [ɛ] in stressed; mid [e] in unstressed/long
    "é": ["eː"],  # long mid
    "è": ["ɛ"],  # short open
    "i": ["i"],
    "o": ["ɔ", "o"],
    "ó": ["oː"],
    "ò": ["ɔ"],
    "u": ["u"],
    "ə": ["ə"],  # schwa (unstressed)

    # --- Consonants ---
    "b": ["b"],
    "c": ["ts"],
    "č": ["tʃ"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ"],
    "h": ["x"],  # /x/ (not voiced glottal like Czech)
    "j": ["j"],
    "k": ["k"],
    "l": ["l", "w"],  # /l/ → [w] finally and before consonant
    "lj": ["ʎ"],
    "m": ["m"],
    "n": ["n"],
    "nj": ["ɲ"],
    "p": ["p"],
    "r": ["r"],
    "s": ["s"],
    "š": ["ʃ"],
    "t": ["t"],
    "v": ["v", "ʋ", "w"],  # realisation varies by position
    "z": ["z"],
    "ž": ["ʒ"],

    # --- Digraphs ---
    "dž": ["dʒ"],
}

ALLOPHONES = {
    "p": ["p"], "b": ["b", "p"],
    "t": ["t"], "d": ["d", "t"],
    "k": ["k"], "ɡ": ["ɡ", "k"],
    "f": ["f"], "v": ["v", "ʋ", "w", "f"],  # v devoices finally
    "s": ["s"], "z": ["z", "s"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ", "ʃ"],
    "x": ["x"],
    "ts": ["ts"], "tʃ": ["tʃ"], "dʒ": ["dʒ", "tʃ"],
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l", "w"], "ʎ": ["ʎ"],  # l → w in coda
    "r": ["r"],
    "j": ["j"],
    # Vowels: Slovenian has pitch accent in standard language
    "a": ["a"],
    "e": ["e"], "eː": ["eː"], "ɛ": ["ɛ"],
    "i": ["i"],
    "o": ["o"], "oː": ["oː"], "ɔ": ["ɔ"],
    "u": ["u"],
    "ə": ["ə"],
}

SPECS = {
    "sl": LanguageSpec(
        code="sl",
        name="Slovenian",
        family="Slavic",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="sla",
        notes=(
            "Standard Slovenian. Unique among Slavic languages: "
            "retains a dual number in grammar. "
            "⟨l⟩ → [w] in syllable coda (e.g. *delal* [dɛˈlaw]). "
            "⟨v⟩ is variable [v ~ ʋ ~ w ~ f] depending on context. "
            "Standard language has phonemic pitch accent (tone); "
            "many dialects are toneless. "
            "No palatal stops (unlike Czech/Slovak), but ⟨lj nj⟩ = [ʎ ɲ]."
        ),
    ),
}
