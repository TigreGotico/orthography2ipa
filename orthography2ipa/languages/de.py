"""German (de) — grapheme→IPA and allophone mappings.

Sources:
- Mangold, M. (2005). *Duden Aussprachewörterbuch*, 6th ed.
- Hall, T.A. (2011). *Phonologie: Eine Einführung*, 2nd ed.
- Wiese, R. (1996). *The Phonology of German*.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels ---
    "a": ["a", "aː"],
    "e": ["ɛ", "eː", "ə"],
    "i": ["ɪ", "iː"],
    "o": ["ɔ", "oː"],
    "u": ["ʊ", "uː"],
    "ä": ["ɛ", "ɛː"],
    "ö": ["œ", "øː"],
    "ü": ["ʏ", "yː"],
    "y": ["ʏ", "yː"],  # in loanwords

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "ts"],  # /k/ native; /ts/ in loanwords (Celsius)
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ"],
    "h": ["h"],  # silent after vowel (length marker)
    "j": ["j"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],  # only in ⟨qu⟩
    "r": ["ʁ"],
    "s": ["z", "s"],  # /z/ onset before vowel; /s/ coda
    "t": ["t"],
    "v": ["f", "v"],  # /f/ native words; /v/ loanwords
    "w": ["v"],
    "x": ["ks"],
    "z": ["ts"],
    "ß": ["s"],

    # --- Consonant digraphs ---
    "ch": ["ç", "x"],  # /ç/ after front V; /x/ after back V (ich/ach)
    "ck": ["k"],
    "pf": ["pf"],
    "ph": ["f"],  # Greek loanwords
    "qu": ["kv"],
    "sch": ["ʃ"],
    "sp": ["ʃp"],  # word-initial
    "st": ["ʃt"],  # word-initial
    "th": ["t"],  # Greek loanwords
    "tz": ["ts"],
    "ng": ["ŋ"],
    "nk": ["ŋk"],
    "ss": ["s"],

    # --- Trigraph ---
    "tsch": ["tʃ"],  # Tschechien, Deutsch

    # --- Vowel digraphs ---
    "aa": ["aː"],
    "ee": ["eː"],
    "oo": ["oː"],
    "ie": ["iː"],  # standard long /iː/

    # --- Diphthongs ---
    "ei": ["aɪ"],
    "ai": ["aɪ"],  # same phoneme, alternate spelling
    "au": ["aʊ"],
    "eu": ["ɔʏ"],
    "äu": ["ɔʏ"],  # same phoneme
}

ALLOPHONES = {
    # Plosives (Auslautverhärtung: final devoicing)
    "p": ["p", "pʰ"],
    "b": ["b", "p"],  # [p] word/syllable-finally
    "t": ["t", "tʰ"],
    "d": ["d", "t"],  # [t] finally
    "k": ["k", "kʰ"],
    "ɡ": ["ɡ", "k"],  # [k] finally

    # Fricatives
    "f": ["f"],
    "v": ["v"],
    "s": ["s"],
    "z": ["z"],
    "ʃ": ["ʃ"],
    "ç": ["ç"],
    "x": ["x"],
    "h": ["h"],
    "ʁ": ["ʁ", "ʀ", "r", "ɐ̯"],  # uvular; trilled (stage); vocalised coda

    # Affricates
    "pf": ["pf"],
    "ts": ["ts"],
    "tʃ": ["tʃ"],

    # Nasals
    "m": ["m"],
    "n": ["n", "ŋ"],  # [ŋ] before velars
    "ŋ": ["ŋ"],

    # Laterals / Glides
    "l": ["l"],
    "j": ["j"],

    # Short vowels
    "a": ["a"],
    "ɛ": ["ɛ"],
    "ɪ": ["ɪ"],
    "ɔ": ["ɔ"],
    "ʊ": ["ʊ"],
    "œ": ["œ"],
    "ʏ": ["ʏ"],
    "ə": ["ə"],

    # Long vowels
    "aː": ["aː"],
    "eː": ["eː"],
    "iː": ["iː"],
    "oː": ["oː"],
    "uː": ["uː"],
    "ɛː": ["ɛː"],
    "øː": ["øː"],
    "yː": ["yː"],

    # Diphthongs
    "aɪ": ["aɪ"],
    "aʊ": ["aʊ"],
    "ɔʏ": ["ɔʏ"],
}

SPECS = {
    "de": LanguageSpec(
        code="de",
        name="German",
        family="Germanic",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="gem",
        notes=(
            "Standard German (Hochdeutsch / Bühnendeutsch). "
            "Auslautverhärtung (final obstruent devoicing) is reflected "
            "in allophone map. ⟨sp⟩/⟨st⟩ → [ʃp]/[ʃt] only word-initially."
        ),
    ),
}
