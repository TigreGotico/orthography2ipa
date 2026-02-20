"""Norwegian (no) — grapheme→IPA and allophone mappings.

Sources:
- Kristoffersen, G. (2000). *The Phonology of Norwegian*.
- Vanvik, A. (1979). *Norsk fonetikk*.

Conventions:
- Based on Urban East Norwegian (standard Bokmål pronunciation).
"""

from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE
GRAPHEMES = {
    # --- Vowels ---
    "a": ["ɑ", "ɑː"],
    "e": ["ɛ", "eː", "ə"],
    "i": ["ɪ", "iː"],
    "o": ["ɔ", "uː"],  # ⟨o⟩ often = [uː] when long
    "u": ["ʉ", "ʉː"],
    "y": ["ʏ", "yː"],
    "æ": ["æ", "æː"],
    "ø": ["ø", "øː"],
    "å": ["ɔ", "oː"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "s"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "j"],  # /j/ before front vowels in some words
    "h": ["h"],
    "j": ["j"],
    "k": ["k", "ç"],  # /ç/ before front vowels
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],
    "r": ["ɾ"],
    "s": ["s"],
    "t": ["t"],
    "v": ["v"],
    "w": ["v"],
    "x": ["ks"],
    "z": ["s"],

    # --- Consonant digraphs ---
    "gj": ["j"],
    "hj": ["j"],
    "kj": ["ç"],
    "ng": ["ŋ"],
    "nk": ["ŋk"],
    "sj": ["ʃ"],
    "sk": ["ʃ", "sk"],  # /ʃ/ before front vowels
    "tj": ["ç"],

    # --- Trigraphs ---
    "skj": ["ʃ"],

    # --- Retroflex digraphs (r + dental) ---
    "rd": ["ɖ"],
    "rl": ["ɭ"],
    "rn": ["ɳ"],
    "rs": ["ʂ"],
    "rt": ["ʈ"],

    # --- Diphthongs ---
    "ei": ["æi"],
    "øy": ["øy"],
    "au": ["æʉ"],
    "ai": ["ɑi"],
}

ALLOPHONES = {
    "p": ["p", "pʰ"],
    "b": ["b"],
    "t": ["t", "tʰ"],
    "d": ["d"],
    "k": ["k", "kʰ"],
    "ɡ": ["ɡ"],

    "f": ["f"],
    "v": ["v"],
    "s": ["s"],
    "ʃ": ["ʃ"],
    "ç": ["ç"],
    "h": ["h"],

    "m": ["m"],
    "n": ["n"],
    "ŋ": ["ŋ"],
    "l": ["l"],
    "ɾ": ["ɾ", "r"],  # trilled emphatically

    # Retroflexes
    "ɖ": ["ɖ"], "ɭ": ["ɭ"], "ɳ": ["ɳ"], "ʂ": ["ʂ"], "ʈ": ["ʈ"],

    "j": ["j"],

    "ɑ": ["ɑ"], "ɑː": ["ɑː"],
    "ɛ": ["ɛ"], "eː": ["eː"],
    "ɪ": ["ɪ"], "iː": ["iː"],
    "ɔ": ["ɔ"], "oː": ["oː"], "uː": ["uː"],
    "ʉ": ["ʉ"], "ʉː": ["ʉː"],
    "ʏ": ["ʏ"], "yː": ["yː"],
    "æ": ["æ"], "æː": ["æː"],
    "ø": ["ø"], "øː": ["øː"],
    "ə": ["ə"],
}

SPECS = {
    "no": LanguageSpec(
        code="no",
        name="Norwegian",
        family="Germanic",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="gem",
        ancestors=(
            Ancestor("non", P, 0.92,
                     "Descent from Old Norse (West Norse branch)"),
            Ancestor("da", AD, 0.06,
                     "Danish adstrate: 400+ years of Danish rule (1380-1814); "
                     "Bokmål is essentially Norwegianised Danish"),
        ),
        notes=(
            "Urban East Norwegian (standard Bokmål pronunciation). "
            "Retroflex assimilation shared with Swedish. "
            "Western/Northern dialects may use uvular [ʁ] for /r/."
        ),
    ),
}
