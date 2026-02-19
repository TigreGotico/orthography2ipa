"""Bulgarian (bg) — grapheme→IPA and allophone mappings.

Sources:
- Klagstad, H.L. (1958). 'The phonemic system of colloquial standard Bulgarian'. *SEEJ* 2.
- Leafgren, J. (2011). *A Concise Bulgarian Grammar*. SEELRC.
- Ternes, E. & Vladimirova-Buhtz, T. (1999). Bulgarian. *Handbook of the IPA*.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels ---
    "а": ["a"],
    "е": ["ɛ"],
    "и": ["i"],
    "о": ["ɔ"],
    "у": ["u"],
    "ъ": ["ɤ"],  # schwa-like back unrounded vowel (unique to Bulgarian)
    "ю": ["ju"],
    "я": ["ja"],

    # --- Consonants ---
    "б": ["b"],
    "в": ["v"],
    "г": ["ɡ"],
    "д": ["d"],
    "ж": ["ʒ"],
    "з": ["z"],
    "й": ["j"],
    "к": ["k"],
    "л": ["l"],
    "м": ["m"],
    "н": ["n"],
    "п": ["p"],
    "р": ["r"],
    "с": ["s"],
    "т": ["t"],
    "ф": ["f"],
    "х": ["x"],
    "ц": ["ts"],
    "ч": ["tʃ"],
    "ш": ["ʃ"],
    "щ": ["ʃt"],  # South Slavic value [ʃt]

    # --- Digraphs ---
    "дж": ["dʒ"],
    "дз": ["dz"],

    # --- Palatalised consonants (before е/и) ---
    "ль": ["lʲ"],
    "нь": ["nʲ"],
    "ть": ["tʲ"],
    "дь": ["dʲ"],
    "сь": ["sʲ"],
    "зь": ["zʲ"],
}

ALLOPHONES = {
    "p": ["p"], "b": ["b", "p"],
    "t": ["t"], "d": ["d", "t"],
    "k": ["k"], "ɡ": ["ɡ", "k"],
    "f": ["f"], "v": ["v", "f"],
    "s": ["s"], "sʲ": ["sʲ"],
    "z": ["z", "s"], "zʲ": ["zʲ", "sʲ"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ", "ʃ"],
    "x": ["x"],
    "ts": ["ts"], "dz": ["dz", "ts"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ", "tʃ"],
    "m": ["m"], "n": ["n", "ŋ"], "nʲ": ["nʲ"],
    "l": ["l"], "lʲ": ["lʲ"],
    "r": ["r"],
    "j": ["j"],
    # Vowels: Bulgarian has vowel reduction but less systematic than Russian
    "a": ["a", "ɐ"],  # unstressed reduction
    "ɔ": ["ɔ", "u"],  # unstressed /ɔ/ → [u] in some positions
    "ɛ": ["ɛ", "ɪ"],
    "i": ["i"],
    "u": ["u"],
    "ɤ": ["ɤ", "ɐ"],  # unstressed ⟨ъ⟩ reduces
}

SPECS = {
    "bg": LanguageSpec(
        code="bg",
        name="Bulgarian",
        family="Slavic",
        script="Cyrillic",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="sla",
        notes=(
            "Standard Bulgarian. Analytic Slavic language (lost case system). "
            "⟨ъ⟩ represents the unique phoneme /ɤ/ (back unrounded mid vowel). "
            "⟨щ⟩ = [ʃt] (South Slavic, contrasting with East Slavic [ɕː]). "
            "Soft consonants occur mainly before /ɛ/ and /i/. "
            "Definite article is a suffix, not a separate word."
        ),
    ),
}
