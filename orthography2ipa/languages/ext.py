"""Extremaduran (ext) — grapheme→IPA and allophone mappings.

Extremaduran (Estremeñu/Extremeño) is an Asturleonese-influenced Romance
variety spoken in the northern provinces of Extremadura (Cáceres) and
bordering areas of Salamanca, Spain. ~200,000+ speakers with varying
competence. UNESCO classified as "definitely endangered."

Sources:
- Montero Curiel, P. (2006). *El extremeño*.
- Viudas Camarasa, A. (1980). *Diccionario extremeño*.
- González Salgado, J.A. (2003). *La fonética de las hablas extremeñas*.

Conventions:
- ISO 639-3: ext (Extremaduran).
- Northern Extremaduran (ext-x-septentrional): strongest Leonese features.
- ext = standard/general variety.
"""
from orthography2ipa.types import LanguageSpec, GraphemePosition as GP

GRAPHEMES_EXT = {
    # --- Vowels ---
    "a": ["a"],
    "e": ["e", "ɛ"],
    "i": ["i"],
    "o": ["o", "ɔ"],
    "u": ["u"],
    "á": ["a"], "é": ["e"], "í": ["i"], "ó": ["o"], "ú": ["u"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "θ"],
    "ç": ["θ"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "h"],  # /h/ before e,i (aspiration, NOT [x])
    "h": ["h"],  # ASPIRATED — from Latin F- (hallmark feature)
    "j": ["h"],  # aspirated [h], not velar [x]
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "ñ": ["ɲ"],
    "p": ["p"],
    "q": ["k"],
    "r": ["ɾ"],
    "s": ["s", "h"],  # coda /s/ → [h] aspiration (southern influence)
    "t": ["t"],
    "v": ["b"],  # betacism
    "x": ["ʃ"],
    "y": ["ʝ", "i"],
    "z": ["θ"],

    # --- Digraphs ---
    "ch": ["tʃ"],
    "ll": ["ʎ", "ʝ"],  # conservative [ʎ] in north; yeísmo in south
    "rr": ["r"],
    "qu": ["k"],
    "gu": ["ɡ"],

    # --- Diphthongs ---
    "ue": ["we"],  # Lat. Ŏ diphthong (shared with Castilian/Leonese)
    "ie": ["je"],  # Lat. Ĕ diphthong
    "ai": ["aj"], "ei": ["ej"], "oi": ["oj"],
    "au": ["aw"], "eu": ["ew"], "ou": ["ow"],
    "ia": ["ja"], "io": ["jo"], "iu": ["ju"],
    "ua": ["wa"], "uo": ["wo"], "ui": ["wi"],
}

ALLOPHONES_EXT = {
    "p": ["p"],
    "b": ["b", "β"],
    "t": ["t"],
    "d": ["d", "ð", "∅"],  # word-final -d frequently deleted
    "k": ["k"],
    "ɡ": ["ɡ", "ɣ"],
    "f": ["f", "h"],  # F- → [h] (Leonese-type aspiration)
    "θ": ["θ"],
    "s": ["s̺", "h"],  # coda aspiration: [s] → [h] before C
    "h": ["h"],  # from Lat. F- and coda /s/
    "ʃ": ["ʃ"],
    "ʝ": ["ʝ"],
    "tʃ": ["tʃ"],
    "m": ["m"],
    "n": ["n", "ŋ"],
    "ɲ": ["ɲ"],
    "l": ["l"],
    "ʎ": ["ʎ"],
    "ɾ": ["ɾ"],
    "r": ["r"],
    "j": ["j"],
    "w": ["w"],
    "a": ["a"], "e": ["e"], "ɛ": ["ɛ"],
    "i": ["i"], "o": ["o"], "ɔ": ["ɔ"], "u": ["u"],
}

POSITIONAL_EXT = {
    "b": {
        GP.DEFAULT: ["b"],
        GP.INTERVOCALIC: ["β"],
    },
    "d": {
        GP.DEFAULT: ["d"],
        GP.INTERVOCALIC: ["ð"],
        GP.WORD_FINAL: ["∅"],  # heavy deletion
    },
    "g": {
        GP.DEFAULT: ["ɡ"],
        GP.INTERVOCALIC: ["ɣ"],
    },
    "s": {
        GP.WORD_INITIAL: ["s"],
        GP.INTERVOCALIC: ["s"],
        GP.CODA: ["h", "s"],  # aspiration (southern influence)
    },
    "r": {
        GP.WORD_INITIAL: ["r"],
        GP.INTERVOCALIC: ["ɾ"],
        GP.ONSET: ["ɾ"],
        GP.CODA: ["ɾ"],
    },
}

# Northern Extremaduran — strongest Leonese traits
ALLOPHONES_EXT_N = {
    **ALLOPHONES_EXT,
    "ʎ": ["ʎ"],  # conservative: no yeísmo
    "l": ["l", "ɾ"],  # /l/ → [ɾ] in some clusters (arma < alma)
    "s": ["s̺", "h", "∅"],  # extreme aspiration in coda
}

SPECS = {
    "ext": LanguageSpec(
        code="ext",
        name="Extremaduran",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_EXT,
        allophones=ALLOPHONES_EXT,
        parent="la",
        notes=(
            "Extremaduran (Estremeñu). ~200,000+ speakers in Cáceres and "
            "adjacent areas. Asturleonese substrate with strong Castilian "
            "overlay. Hallmark: Latin F- → [h] aspiration (horno, hifo), "
            "shared with western Asturian and Andalusian. Coda /s/ → [h] "
            "aspiration. Leonese diphthongs (Ĕ → [je], Ŏ → [we]). "
            "Betacism. Final -d deletion. Vowel system is 5-vowel "
            "Castilian-like. UNESCO 'definitely endangered'."
        ),
    ),
    "ext-x-septentrional": LanguageSpec(
        code="ext-x-septentrional",
        name="Northern Extremaduran",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_EXT,
        allophones=ALLOPHONES_EXT_N,
        parent="ext",
        notes=(
            "Northern Extremaduran (Alta Extremadura, Cáceres). Strongest "
            "Leonese features: conservative palatal lateral [ʎ] (no yeísmo), "
            "extreme coda aspiration, /l/ → [ɾ] in some clusters. "
            "Closest to Leonese proper."
        ),
    ),
}
