"""Dutch (nl) — grapheme→IPA and allophone mappings.

Sources:
- Gussenhoven, C. (1999). Dutch. *Handbook of the IPA*.
- Booij, G. (1995). *The Phonology of Dutch*.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE

GRAPHEMES = {
    # --- Vowels (short / long distinguished by open/closed syllable) ---
    "a": ["ɑ"],  # short a
    "e": ["ɛ", "ə"],  # short e / schwa
    "i": ["ɪ"],  # short i
    "o": ["ɔ"],  # short o
    "u": ["ʏ"],  # short u (rounded front)
    "aa": ["aː"],  # long a
    "ee": ["eː"],  # long e
    "ie": ["iː"],  # long i
    "oo": ["oː"],  # long o
    "oe": ["uː"],  # long u
    "uu": ["yː"],  # long ü
    "eu": ["øː"],  # front rounded

    # --- Accented (loanwords) ---
    "é": ["eː"], "è": ["ɛ"], "ê": ["ɛ"],
    "ë": ["ə"], "ï": ["i"], "ü": ["y"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "s"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɣ", "x"],  # voiced/voiceless velar depending on dialect
    "h": ["ɦ"],
    "j": ["j"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],
    "r": ["r", "ʁ"],
    "s": ["s"],
    "t": ["t"],
    "v": ["v", "f"],  # devoiced in southern/standard
    "w": ["ʋ"],
    "x": ["ks"],
    "y": ["ɛi"],  # rare
    "z": ["z", "s"],  # devoiced in southern/standard

    # --- Consonant digraphs ---
    "ch": ["x"],  # voiceless velar
    "ng": ["ŋ"],
    "nk": ["ŋk"],
    "sch": ["sx"],  # s + ch
    "sj": ["ʃ"],  # loanwords and native
    "tj": ["tʲ", "tʃ"],  # loanwords
    "th": ["t"],  # loanwords
    "ph": ["f"],

    # --- Diphthongs ---
    "ei": ["ɛi"],
    "ij": ["ɛi"],  # same phoneme as ⟨ei⟩
    "ou": ["ɑu"],
    "au": ["ɑu"],  # same phoneme as ⟨ou⟩
    "ui": ["œy"],  # uniquely Dutch
    "ai": ["aːi"],  # loanwords
    "oi": ["ɔi"],  # loanwords

    # --- Trigraphs ---
    "eau": ["oː"],  # French loanwords
    "ieu": ["iːø"],  # French loanwords
}

ALLOPHONES = {
    "p": ["p"],
    "b": ["b", "p"],  # final devoicing
    "t": ["t"],
    "d": ["d", "t"],  # final devoicing
    "k": ["k"],

    "f": ["f"],
    "v": ["v", "f"],  # devoiced in standard Dutch
    "s": ["s"],
    "z": ["z", "s"],  # devoiced
    "x": ["x"],
    "ɣ": ["ɣ", "x"],  # devoiced in standard/southern
    "ɦ": ["ɦ", "h"],

    "m": ["m"],
    "n": ["n", "ŋ"],
    "ŋ": ["ŋ"],

    "l": ["l", "ɫ"],  # dark in coda for some speakers
    "r": ["r", "ɾ", "ʁ", "ʀ", "ɹ"],  # highly variable by region
    "ʋ": ["ʋ", "w", "β̞"],
    "j": ["j"],

    "ɑ": ["ɑ"],
    "aː": ["aː"],
    "ɛ": ["ɛ"],
    "eː": ["eː"],
    "ɪ": ["ɪ"],
    "iː": ["iː"],
    "ɔ": ["ɔ"],
    "oː": ["oː"],
    "ʏ": ["ʏ"],
    "yː": ["yː"],
    "uː": ["uː"],
    "øː": ["øː"],
    "ə": ["ə"],

    "ɛi": ["ɛi", "ɛɪ"],
    "ɑu": ["ɑu", "ʌu"],
    "œy": ["œy", "œʏ"],
}

SPECS = {
    "nl": LanguageSpec(
        code="nl",
        name="Dutch",
        family="Germanic",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="gem",
        ancestors=(
            Ancestor("gem", P, 0.90,
                     "Descent from Proto-Germanic via Old Low Franconian"),
            Ancestor("la", AD, 0.04,
                     "Latin adstrate: ecclesiastical vocabulary"),
            Ancestor("fr", AD, 0.04,
                     "French adstrate: centuries of Burgundian/French influence "
                     "in S. Netherlands; cf. van der Wal (2008)"),
        ),
        notes=(
            "Standard Dutch (ABN / Algemeen Nederlands). "
            "⟨g⟩ realisation is [ɣ] in northern NL and [x] in "
            "southern NL / Flanders. /r/ is highly variable."
        ),
    ),
}
