"""Macedonian (mk) — grapheme→IPA and allophone mappings.

Sources:
- Lunt, H.G. (1952). *A Grammar of the Macedonian Literary Language*. Skopje.
- Friedman, V. (1993). 'Macedonian' in *The Slavonic Languages* (ed. Comrie & Corbett).
- Koneski, B. (1983). *Gramatika na makedonskiot literaturen jazik*.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels ---
    "а": ["a"],
    "е": ["ɛ"],
    "и": ["i"],
    "о": ["ɔ"],
    "у": ["u"],

    # --- Consonants ---
    "б": ["b"],
    "в": ["v"],
    "г": ["ɡ"],
    "д": ["d"],
    "ѓ": ["ɟ"],  # palatal stop (between к/г and ч/ж)
    "е": ["ɛ"],
    "ж": ["ʒ"],
    "з": ["z"],
    "ѕ": ["dz"],  # dze (unique Macedonian letter)
    "и": ["i"],
    "ј": ["j"],
    "к": ["k"],
    "ќ": ["c"],  # palatal stop (voiceless)
    "л": ["l"],
    "љ": ["ʎ"],  # palatal lateral
    "м": ["m"],
    "н": ["n"],
    "њ": ["ɲ"],  # palatal nasal
    "о": ["ɔ"],
    "п": ["p"],
    "р": ["r"],  # can be syllabic: e.g. *прст* [pr̩st]
    "с": ["s"],
    "т": ["t"],
    "у": ["u"],
    "ф": ["f"],
    "х": ["x"],
    "ц": ["ts"],
    "ч": ["tʃ"],
    "џ": ["dʒ"],
    "ш": ["ʃ"],
}

ALLOPHONES = {
    "p": ["p"], "b": ["b", "p"],
    "t": ["t"], "d": ["d", "t"],
    "c": ["c"], "ɟ": ["ɟ", "c"],  # Macedonian palatal stops
    "k": ["k"], "ɡ": ["ɡ", "k"],
    "f": ["f"], "v": ["v", "f"],
    "s": ["s"], "z": ["z", "s"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ", "ʃ"],
    "x": ["x"],
    "ts": ["ts"], "dz": ["dz", "ts"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ", "tʃ"],
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "ʎ": ["ʎ"],
    "r": ["r"], "r̩": ["r̩"],
    "j": ["j"],
    # Vowels: fixed antepenultimate stress, no phonemic vowel length
    "a": ["a", "ɐ"],
    "ɛ": ["ɛ"],
    "i": ["i"],
    "ɔ": ["ɔ"],
    "u": ["u"],
}

SPECS = {
    "mk": LanguageSpec(
        code="mk",
        name="Macedonian",
        family="Slavic",
        script="Cyrillic",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="sla",
        notes=(
            "Standard Macedonian, codified 1945. South Slavic, closely related "
            "to Bulgarian. Analytic case system (lost inflection). "
            "Fixed antepenultimate stress (third-from-last syllable). "
            "Unique letters: ⟨ѕ⟩ = [dz], ⟨ѓ⟩ = [ɟ], ⟨ќ⟩ = [c]. "
            "Definite article suffixed in three forms: "
            "-от/-та/-то (definite), -ов/-ва/-во (proximal), -он/-на/-но (distal). "
            "⟨љ⟩ = [ʎ], ⟨њ⟩ = [ɲ]."
        ),
    ),
}
