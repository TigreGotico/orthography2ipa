"""Ukrainian (uk) — grapheme→IPA and allophone mappings.

Sources:
- Danyenko, A. & Vakulenko, S. (1995). *Ukrainian*.
- Pugh, S.M. & Press, I. (1999). *Ukrainian: A Comprehensive Grammar*.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels ---
    "а": ["ɑ"],
    "е": ["ɛ"],
    "є": ["jɛ"],
    "и": ["ɪ"],
    "і": ["i"],
    "ї": ["ji"],
    "о": ["ɔ"],
    "у": ["u"],
    "ю": ["ju"],
    "я": ["jɑ"],

    # --- Consonants ---
    "б": ["b"],
    "в": ["ʋ"],
    "г": ["ɦ"],  # voiced glottal fricative
    "ґ": ["ɡ"],  # plosive (distinct letter)
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
    "щ": ["ʃtʃ"],

    # --- Soft sign ---
    "ь": ["ʲ"],

    # --- Palatalised digraphs ---
    "дь": ["dʲ"], "ть": ["tʲ"], "нь": ["nʲ"], "ль": ["lʲ"],
    "сь": ["sʲ"], "зь": ["zʲ"], "ць": ["tsʲ"],

    # --- Apostrophe (separator before iotated vowels) ---
    "'": [""],
}

ALLOPHONES = {
    "b": ["b", "p"],
    "d": ["d", "t"], "dʲ": ["dʲ", "tʲ"],
    "ɡ": ["ɡ", "k"],
    "p": ["p"], "t": ["t"], "tʲ": ["tʲ"], "k": ["k"],
    "ɦ": ["ɦ", "x"],  # devoiced in clusters
    "ʋ": ["ʋ", "w", "u̯"],  # [w] before consonant/word-finally
    "f": ["f"],
    "s": ["s"], "sʲ": ["sʲ"],
    "z": ["z", "s"], "zʲ": ["zʲ", "sʲ"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ", "ʃ"],
    "x": ["x"],
    "ts": ["ts"], "tsʲ": ["tsʲ"],
    "tʃ": ["tʃ"],
    "m": ["m"], "n": ["n", "ŋ"], "nʲ": ["nʲ"],
    "l": ["l", "ɫ"], "lʲ": ["lʲ"],
    "r": ["r"], "j": ["j"],
    "ɑ": ["ɑ"], "ɛ": ["ɛ"], "ɪ": ["ɪ"],
    "i": ["i"], "ɔ": ["ɔ"], "u": ["u"],
}

SPECS = {
    "uk": LanguageSpec(
        code="uk",
        name="Ukrainian",
        family="Slavic",
        script="Cyrillic",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="ine",
        notes=(
            "Standard Ukrainian. Key differences from Russian: "
            "⟨г⟩ = [ɦ] (not [ɡ]), ⟨ґ⟩ = [ɡ] as separate letter, "
            "⟨в⟩ = [ʋ] approximant, no vowel reduction (no аканье)."
        ),
    ),
}
