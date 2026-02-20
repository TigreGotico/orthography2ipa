"""Galician subdialects — grapheme→IPA and allophone mappings.

Three main dialectal blocks plus Fala (Extremaduran Galician).

Sources:
- Fernández Rei, F. (1990). *Dialectoloxía da lingua galega*.
- Regueira, X.L. (1996). Galician. *JIPA* 26(2).
- RAG (2003). *Normas ortográficas e morfolóxicas do idioma galego*.
- Frías Conde, X. (1997). "As falas de Xálima."

Conventions:
- Western: gl-x-occidental (gheada, seseo zones).
- Central: gl-x-central.
- Eastern: gl-x-oriental (closest to Portuguese).
- Fala: fax (ISO 639-3: fax) — Galician-Portuguese in Extremadura.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE


GRAPHEMES = {
    # --- Vowels (7-vowel system) ---
    "a": ["a", "ɐ"],
    "e": ["e", "ɛ"],
    "i": ["i"],
    "o": ["o", "ɔ"],
    "u": ["u"],
    "á": ["a"], "é": ["ɛ"], "ê": ["e"], "í": ["i"],
    "ó": ["ɔ"], "ô": ["o"], "ú": ["u"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "θ"],  # /θ/ before e,i (seseo/ceceo varies)
    "ç": ["s"],  # historical
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "ʃ"],  # /ʃ/ before e,i (gheada variant: /h/)
    "h": [""],  # silent
    "j": ["ʃ"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "ñ": ["ɲ"],
    "p": ["p"],
    "q": ["k"],
    "r": ["ɾ"],
    "s": ["s"],
    "t": ["t"],
    "v": ["b"],  # merged with /b/ in standard
    "x": ["ʃ"],
    "z": ["θ"],

    # --- Digraphs ---
    "ch": ["tʃ"],
    "ll": ["ʎ"],  # no yeísmo in standard Galician
    "nh": ["ɲ"],  # alternative spelling
    "rr": ["r"],  # alveolar trill
    "qu": ["k"],
    "gu": ["ɡ"],
    "ss": ["s"],

    # --- Diphthongs ---
    "ai": ["aj"], "au": ["aw"], "ei": ["ej"], "eu": ["ew"],
    "oi": ["oj"], "ou": ["ow"], "ui": ["uj"], "iu": ["iw"],
    "ia": ["ja"], "ie": ["je"], "io": ["jo"],
    "ua": ["wa"], "ue": ["we"], "uo": ["wo"],

    # --- Nasal sequences ---
    "ão": ["ɐ̃w̃"],  # in some traditional spellings
}

ALLOPHONES = {
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
    "p": ["p"], "t": ["t"], "k": ["k"],
    "f": ["f"], "v": ["β"], "s": ["s", "z"],
    "θ": ["θ"], "ʃ": ["ʃ"],
    "tʃ": ["tʃ"],
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "ʎ": ["ʎ"],
    "ɾ": ["ɾ"], "r": ["r"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "ɐ": ["ɐ"],
    "e": ["e"], "ɛ": ["ɛ"],
    "i": ["i"],
    "o": ["o"], "ɔ": ["ɔ"],
    "u": ["u"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Western Galician — gheada and seseo
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_GL_W = {
    **ALLOPHONES,
    # Gheada: /ɡ/ → [h] / [ħ] (the defining western feature)
    "ɡ": ["ɡ", "h", "ħ", "ɣ"],
    # Seseo: /θ/ → [s] (merger of c/z with s)
    "θ": ["s"],  # no interdental in seseo zones
    "s": ["s", "z"],
    # Betacism
    "b": ["b", "β"],
    "d": ["d", "ð"],
}

GRAPHEMES_GL_W = {
    **GRAPHEMES,
    "g": ["ɡ", "h", "ʃ"],  # gheada: [h] before a,o,u
    "z": ["s"],  # seseo
    "c": ["k", "s"],  # before e,i: seseo
}

# ═══════════════════════════════════════════════════════════════════════════
# Central Galician — standard-closest
# ═══════════════════════════════════════════════════════════════════════════

# Central is essentially the base standard — use GRAPHEMES/ALLOPHONES directly.

# ═══════════════════════════════════════════════════════════════════════════
# Eastern Galician — closest to Portuguese
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_GL_E = {
    **ALLOPHONES,
    # Nasalisation more Portuguese-like in some zones
    "n": ["n", "ŋ", "ɲ"],
    # Some preservation of medieval nasal vowels
    # More conservative vowel system
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# A Fala (fax) — Galician-Portuguese isolate in Extremadura
# Spoken in Valverde del Fresno, Eljas, San Martín de Trevejo (Cáceres)
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_FALA = {
    **GRAPHEMES,
    # Fala preserves archaic Galician-Portuguese features
    "v": ["b"],  # betacism universal
    "ch": ["tʃ"],
    "x": ["ʃ"],
    "ll": ["ʎ"],
    # Nasal vowels (more Portuguese-like)
    "ão": ["ɐ̃w̃"],
    "ã": ["ɐ̃"],
    "õ": ["õ"],
}

ALLOPHONES_FALA = {
    **ALLOPHONES,
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
    "f": ["f", "h"],  # Lat. F- → [h] in some words (Leonese influence)
    "s": ["s", "z"],
    "ʃ": ["ʃ"],
    "ʎ": ["ʎ"],  # conservative
    "ɾ": ["ɾ"],
    "r": ["r"],
}

SPECS = {
    "gl": LanguageSpec(
        code="gl",
        name="Galician",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="la",
        ancestors=(
            Ancestor("la-x-hispania", P, 0.78,
                     "Primary descent from Hispanic Vulgar Latin"),
            Ancestor("cel", SUB, 0.06,
                     "Gallaecian Celtic substrate: strongest in NW Iberia; "
                     "castros, toponyms; cf. Moralejo Lasso (1977)"),
            Ancestor("xlg", SUB, 0.04,
                     "Lusitanian substrate: southern Gallaecia overlap"),
            Ancestor("xsb", SUP, 0.06,
                     "Suebi superstrate: STRONGEST in Galicia — capital at Braga; "
                     "Suevic kingdom 411-585 CE; cf. Piel (1937)"),
            Ancestor("got", SUP, 0.03,
                     "Visigothic superstrate (post-585 CE conquest of Suebi)"),
            Ancestor("xaa", AD, 0.03,
                     "Arabic adstrate: minimal in NW (reconquered by ~11th c.)"),
        ),
        notes="Standard Galician per RAG norms. Gheada not reflected in standard.",
    ),

    "gl-x-occidental": LanguageSpec(
        code="gl-x-occidental",
        name="Western Galician",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_GL_W,
        allophones=ALLOPHONES_GL_W,
        parent="gl",
        notes=(
            "Western Galician (Pontevedra, western A Coruña). Diagnostic "
            "features: gheada (/ɡ/ → [h]/[ħ]) and seseo (/θ/ → [s]). "
            "Gheada is the most socially marked Galician feature — "
            "stigmatised but widespread. Seseo merges /θ/ and /s/. "
            "Otherwise phonologically close to standard."
        ),
    ),
    "gl-x-central": LanguageSpec(
        code="gl-x-central",
        name="Central Galician",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="gl",
        notes=(
            "Central Galician (Lugo, eastern A Coruña, Ourense). Closest "
            "to RAG standard norms. No gheada, no seseo. 7-vowel system "
            "with /ɛ, ɔ/ phonemic. Palatal lateral [ʎ] preserved. "
            "This is the prestige norm base."
        ),
    ),
    "gl-x-oriental": LanguageSpec(
        code="gl-x-oriental",
        name="Eastern Galician",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES_GL_E,
        parent="gl",
        notes=(
            "Eastern Galician (eastern Ourense, eastern Lugo, into León). "
            "Transitional toward Portuguese and Asturleonese. More "
            "conservative vowel system, some nasalisation patterns "
            "resembling Portuguese. No gheada. Shares some features "
            "with eonaviego (Galician-Asturian)."
        ),
    ),
    "fax": LanguageSpec(
        code="fax",
        name="A Fala (Xalimego)",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_FALA,
        allophones=ALLOPHONES_FALA,
        parent="gl",
        notes=(
            "A Fala (Xalimego/Fala de Xálima). Galician-Portuguese "
            "linguistic island in Cáceres, Extremadura. Three local "
            "varieties: Valverdeiru (Valverde del Fresno), Lagarteiro "
            "(Eljas), Mañegu (San Martín de Trevejo). ~5,000–10,000 "
            "speakers. Preserves medieval Galician-Portuguese features "
            "with Leonese/Extremaduran influence (F- → [h] aspiration "
            "in some words). Betacism. Nasal vowels. Palatal [ʎ]. "
            "ISO 639-3: fax."
        ),
    ),
}
