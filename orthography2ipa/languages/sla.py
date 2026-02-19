"""Proto-Slavic (sla) — reconstructed phoneme inventory.

Sources:
- Schenker, A.M. (1995). *The Dawn of Slavic*. Yale UP.
- Sussex, R. & Cubberley, P. (2006). *The Slavic Languages*. CUP.
- Kortlandt, F. (1994). 'From Proto-Indo-European to Slavic'. *JIES* 22.
"""
from orthography2ipa.types import LanguageSpec

# Scholarly transliteration of reconstructed Proto-Slavic forms.
# Late Proto-Slavic (c. 600–800 CE) before the major dialect splits.
GRAPHEMES = {
    # --- Vowels (short) ---
    "ъ": ["ŭ"],  # short back yer
    "ь": ["ĭ"],  # short front yer
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],
    "y": ["ɨ"],  # high central/back vowel

    # --- Vowels (long / nasal) ---
    "ě": ["æː"],  # yat (front long vowel)
    "ǫ": ["õ"],  # back nasal vowel
    "ę": ["ẽ"],  # front nasal vowel
    "ā": ["aː"],
    "ē": ["eː"],
    "ī": ["iː"],
    "ō": ["oː"],
    "ū": ["uː"],

    # --- Consonants ---
    "p": ["p"],
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "k": ["k"],
    "g": ["ɡ"],
    "s": ["s"],
    "z": ["z"],
    "x": ["x"],
    "š": ["ʃ"],
    "ž": ["ʒ"],
    "c": ["ts"],
    "č": ["tʃ"],
    "dž": ["dʒ"],
    "m": ["m"],
    "n": ["n"],
    "ň": ["ɲ"],
    "l": ["l"],
    "ľ": ["lʲ"],
    "r": ["r"],
    "ŕ": ["rʲ"],
    "v": ["ʋ"],
    "j": ["j"],

    # --- Palatalised (soft) consonants ---
    "tʲ": ["tʲ"], "dʲ": ["dʲ"],
    "kʲ": ["kʲ"], "gʲ": ["ɡʲ"],
    "sʲ": ["sʲ"], "zʲ": ["zʲ"],
    "nʲ": ["nʲ"], "lʲ": ["lʲ"],
    "rʲ": ["rʲ"],
}

ALLOPHONES = {
    # Obstruents: final devoicing already established
    "p": ["p"], "b": ["b", "p"],
    "t": ["t"], "d": ["d", "t"],
    "k": ["k"], "ɡ": ["ɡ", "k"],
    "s": ["s"], "z": ["z", "s"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ", "ʃ"],
    "x": ["x"],
    "ts": ["ts"], "tʃ": ["tʃ"],
    "dʒ": ["dʒ", "tʃ"],
    # Sonorants
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "lʲ": ["lʲ"],
    "r": ["r"], "rʲ": ["rʲ"],
    "ʋ": ["ʋ", "w"],
    "j": ["j"],
    # Vowels
    "a": ["a"], "aː": ["aː"],
    "e": ["e"], "eː": ["eː"],
    "i": ["i"], "iː": ["iː"],
    "o": ["o"], "oː": ["oː"],
    "u": ["u"], "uː": ["uː"],
    "ɨ": ["ɨ"],
    "æː": ["æː", "eː"],  # yat reflexes vary by dialect
    "õ": ["õ", "ɔ̃"],
    "ẽ": ["ẽ", "ɛ̃"],
    "ŭ": ["ŭ", "ə"],
    "ĭ": ["ĭ", "ɪ"],
}

SPECS = {
    "sla": LanguageSpec(
        code="sla",
        name="Proto-Slavic",
        family="Slavic",
        script="Latin",  # scholarly transliteration
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="ine",
        notes=(
            "Reconstructed Late Proto-Slavic (c. 600–800 CE). "
            "Key features: open syllable law (no closed syllables), "
            "palatalisation alternations (three Slavic palatalisations), "
            "nasal vowels /ẽ õ/, yers /ĭ ŭ/, yat /æː/. "
            "Transcription follows standard Slavicist convention."
        ),
    ),
}
