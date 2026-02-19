"""Old Church Slavonic / Old Bulgarian (cu) — grapheme→IPA and allophone mappings.

Sources:
- Lunt, H.G. (2001). *Old Church Slavonic Grammar* (7th ed.). Mouton.
- Huntley, D. (1993). 'Old Church Slavonic' in *The Slavonic Languages* (ed. Comrie & Corbett).
- Schenker, A.M. (1995). *The Dawn of Slavic*. Yale UP.
"""
from orthography2ipa.types import LanguageSpec

# Glagolitic / early Cyrillic orthographic transcription.
# Representing the South Slavic literary dialect of the 9th–11th centuries.
GRAPHEMES = {
    # --- Vowels ---
    "а": ["a"],
    "е": ["e"],
    "и": ["i"],
    "о": ["o"],
    "оу": ["u"],  # digraph for /u/
    "ъ": ["ŭ"],  # back yer (short lax back vowel)
    "ь": ["ĭ"],  # front yer (short lax front vowel)
    "ꙑ": ["ɨ"],  # yery (high central/back vowel)
    "ѣ": ["æː"],  # yat (distinct from /e/)
    "ѫ": ["õ"],  # big yus (back nasal)
    "ѧ": ["ẽ"],  # little yus (front nasal)
    "ѭ": ["jõ"],  # iotated big yus
    "ѩ": ["jẽ"],  # iotated little yus
    "ꙗ": ["ja"],  # iotated a
    "є": ["je"],  # iotated e (initial position)
    "ю": ["ju"],

    # --- Consonants ---
    "б": ["b"],
    "в": ["ʋ"],
    "г": ["ɡ"],
    "д": ["d"],
    "ж": ["ʒ"],  # /dʒ/ in some analyses
    "з": ["z"],
    "к": ["k"],
    "л": ["l"],
    "м": ["m"],
    "н": ["n"],
    "п": ["p"],
    "р": ["r"],
    "с": ["s"],
    "т": ["t"],
    "х": ["x"],
    "ц": ["ts"],
    "ч": ["tʃ"],
    "ш": ["ʃ"],
    "щ": ["ʃt"],  # South Slavic value (Bulgarian reflex)
    "ѕ": ["dz"],  # dze
    "ж": ["ʒ"],

    # --- Palatalised / soft consonants ---
    "нь": ["nʲ"], "льь": ["lʲ"], "рьь": ["rʲ"],
    "ть": ["tʲ"], "дь": ["dʲ"],
}

ALLOPHONES = {
    "p": ["p"], "b": ["b", "p"],
    "t": ["t"], "d": ["d", "t"],
    "k": ["k"], "ɡ": ["ɡ", "k"],
    "s": ["s"], "z": ["z", "s"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ", "ʃ"],
    "x": ["x"],
    "ts": ["ts"], "dz": ["dz", "ts"],
    "tʃ": ["tʃ"],
    "m": ["m"], "n": ["n", "ŋ"], "nʲ": ["nʲ"],
    "l": ["l"], "lʲ": ["lʲ"],
    "r": ["r"], "rʲ": ["rʲ"],
    "ʋ": ["ʋ", "w"],
    "j": ["j"],
    # Vowels
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
    "ɨ": ["ɨ"],
    "æː": ["æː", "ja", "e"],  # yat reflex varies by dialect
    "õ": ["õ", "u"],
    "ẽ": ["ẽ", "e"],
    "ŭ": ["ŭ", "ə", ""],  # yer: could fall or vocalise
    "ĭ": ["ĭ", "ə", ""],
}

SPECS = {
    "cu": LanguageSpec(
        code="cu",
        name="Old Church Slavonic",
        family="Slavic",
        script="Cyrillic",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="sla",
        notes=(
            "Old Church Slavonic (also called Old Bulgarian), the first literary "
            "Slavic language, codified by Sts Cyril & Methodius (9th c.). "
            "South Slavic base with nasal vowels /ẽ õ/, yers /ĭ ŭ/, "
            "yat /æː/. ⟨щ⟩ has South Slavic value [ʃt] (vs East Slavic [ɕː]). "
            "Graphemes follow early Cyrillic; Glagolitic equivalents omitted."
        ),
    ),
}
