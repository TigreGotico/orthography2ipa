"""Asturian / Leonese (ast) — grapheme→IPA and allophone mappings.

Asturian (Asturianu/Bable) is an Asturleonese language spoken in the
Principality of Asturias and parts of León, Zamora, and Salamanca (Spain).
~100,000+ speakers. Not yet officially recognised at state level despite
decades of normativization by the Academia de la Llingua Asturiana (ALLA).

Three main dialectal blocks plus Leonese (eastern continuation).

Sources:
- ALLA (2001). *Gramática de la Llingua Asturiana*.
- Arias Cabal, Á. (2002). El asturiano. In: Estudios filolóxicos asturianos.
- Cano González, A.M. (2009). Asturianu. In: Atlas Lingüístico de la
  Península Ibérica.
- García Arias, X.L. (2003). *Gramática histórica de la lengua asturiana*.
- Muñiz Cachón, C. (2002). Rasgos fónicos del asturiano.

Conventions:
- ISO 639-3: ast. Central Asturian = standard (ALLA norms).
- Western: ast-x-occidental. Eastern: ast-x-oriental.
- Leonese (Spain): ast-ES-x-leon.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# Central Asturian (standard — ALLA norms)
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_AST = {
    # --- Vowels (5-vowel system) ---
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],
    "á": ["a"], "é": ["e"], "í": ["i"], "ó": ["o"], "ú": ["u"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "θ"],  # /θ/ before e,i (Castilian-influenced)
    "ç": ["θ"],  # archaic
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "x"],  # /x/ before e,i
    "h": [""],  # silent (h- aspirée in some western areas)
    "j": ["x"],  # velar fricative
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "ñ": ["ɲ"],
    "p": ["p"],
    "q": ["k"],
    "r": ["ɾ"],
    "s": ["s"],  # apico-alveolar [s̺] (not laminal)
    "t": ["t"],
    "v": ["b"],  # betacism
    "w": ["w"],
    "x": ["ʃ"],  # voiceless postalveolar fricative
    "y": ["ʝ", "i"],
    "z": ["θ"],

    # --- Digraphs ---
    "ch": ["tʃ"],
    "ll": ["ʎ"],  # palatal lateral (no yeísmo in standard)
    "rr": ["r"],  # alveolar trill
    "qu": ["k"],
    "gu": ["ɡ"],
    "ts": ["ts"],  # voiceless alveolar affricate (dialectal)

    # --- Asturleonese diphthongs (from Lat. Ĕ and Ŏ) ---
    "ue": ["we"],  # Lat. Ŏ → ue: puerta, fueru, rueda
    "ie": ["je"],  # Lat. Ĕ → ie: piedra, tierra, siete

    # --- Other diphthongs ---
    "ai": ["aj"], "ei": ["ej"], "oi": ["oj"],
    "au": ["aw"], "eu": ["ew"], "ou": ["ow"],
    "ia": ["ja"], "io": ["jo"], "iu": ["ju"],
    "ua": ["wa"], "uo": ["wo"], "ui": ["wi"],
}

ALLOPHONES_AST = {
    # Plosives — standard Iberian lenition
    "p": ["p"],
    "b": ["b", "β"],
    "t": ["t"],
    "d": ["d", "ð"],
    "k": ["k"],
    "ɡ": ["ɡ", "ɣ"],

    # Fricatives
    "f": ["f"],
    "θ": ["θ"],
    "s": ["s̺"],  # apico-alveolar (distinct from Castilian laminal)
    "x": ["x"],
    "ʃ": ["ʃ"],
    "ʝ": ["ʝ", "ɟʝ"],

    # Affricates
    "tʃ": ["tʃ"],
    "ts": ["ts"],  # in western/archaic forms

    # Nasals
    "m": ["m"],
    "n": ["n", "ŋ"],
    "ɲ": ["ɲ"],

    # Laterals
    "l": ["l"],
    "ʎ": ["ʎ"],

    # Rhotics
    "ɾ": ["ɾ"],
    "r": ["r"],

    # Glides
    "j": ["j"],
    "w": ["w"],

    # Vowels
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Western Asturian (asturianu oucidental)
# Strongest archaic features: aspirated f-, -l.l- geminate, etc.
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_AST_W = {
    **GRAPHEMES_AST,
    "h": ["h"],  # aspirated h- from Latin F- (hallmark western feature)
    "l·l": ["lː"],  # geminate lateral from Latin -LL- (not palatalised)
    "uo": ["wo"],  # diphthong variant (cf. central ue)
}

ALLOPHONES_AST_W = {
    **ALLOPHONES_AST,
    "h": ["h"],  # aspiration from Lat. F-: forno→hornu, filu→hilu
    "lː": ["lː"],  # geminate: -LL- → [lː] not [ʎ]
    "f": ["f", "h"],  # F- → h- is the western hallmark
}

# ═══════════════════════════════════════════════════════════════════════════
# Eastern Asturian (asturianu oriental)
# Transitional to Cantabrian; mass diphthongs, Castilian influence
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_AST_E = {
    **ALLOPHONES_AST,
    "s": ["s̺", "s"],  # mixed apical/laminal
    "ʎ": ["ʎ", "ʝ"],  # yeísmo creeping in from Castilian contact
}

# ═══════════════════════════════════════════════════════════════════════════
# Leonese (ast-ES-x-leon) — spoken in León, Zamora, Salamanca
# Continuation of Asturleonese south of the Cantabrian mountains
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_LEON = {
    **GRAPHEMES_AST,
    # Leonese preserves some features shared with Mirandese
    "ll": ["ʎ"],  # palatalization of -LL- consistent
}

ALLOPHONES_LEON = {
    **ALLOPHONES_AST,
    "x": ["x", "h"],  # aspiration tendency in some Zamoran varieties
    "ʎ": ["ʎ"],  # conservative — no yeísmo
}

# ═══════════════════════════════════════════════════════════════════════════
# Specs
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "ast": LanguageSpec(
        code="ast",
        name="Asturian (Central)",
        family="Asturleonese",
        script="Latin",
        graphemes=GRAPHEMES_AST,
        allophones=ALLOPHONES_AST,
        parent="la",
        ancestors=(
            Ancestor("la-x-hispania", P, 0.80,
                     "Primary descent from Hispanic Vulgar Latin"),
            Ancestor("cel", SUB, 0.06,
                     "Celtic (Astures) substrate: tribal name itself is Celtic; "
                     "strong NW Iberian Celtic presence; cf. García Arias (2003)"),
            Ancestor("got", SUP, 0.04,
                     "Visigothic superstrate: Kingdom of Asturias (718-924 CE) "
                     "was the first Christian successor state"),
            Ancestor("xaa", AD, 0.02,
                     "Arabic adstrate: minimal — Asturias never fully conquered"),
        ),
        notes=(
            "Central Asturian per ALLA (Academia de la Llingua Asturiana) "
            "norms. ~100,000+ speakers. 5-vowel system, apico-alveolar [s̺], "
            "Leonese diphthongs (Ĕ → [je], Ŏ → [we]). Palatal lateral [ʎ] "
            "from Latin -LL-. Neuter gender (lo: mass/uncountable). "
            "3sg copula ye. Pending official recognition in Spain."
        ),
    ),
    "ast-x-occidental": LanguageSpec(
        code="ast-x-occidental",
        name="Western Asturian",
        family="Asturleonese",
        script="Latin",
        graphemes=GRAPHEMES_AST_W,
        allophones=ALLOPHONES_AST_W,
        parent="ast",
        notes=(
            "Western Asturian (asturianu oucidental). Most archaic variety. "
            "Hallmark: Latin F- → [h] aspiration (forno→hornu). "
            "Latin -LL- → geminate [lː] (l·l) instead of palatal [ʎ]. "
            "Closest to Galician-Portuguese in several phonological traits. "
            "Diphthongs may show -uo- alongside -ue-."
        ),
    ),
    "ast-x-oriental": LanguageSpec(
        code="ast-x-oriental",
        name="Eastern Asturian",
        family="Asturleonese",
        script="Latin",
        graphemes=GRAPHEMES_AST,
        allophones=ALLOPHONES_AST_E,
        parent="ast",
        notes=(
            "Eastern Asturian, transitional to Cantabrian/Castilian. "
            "Strongest Castilian influence: incipient yeísmo ([ʎ]→[ʝ]), "
            "mixed apical/laminal sibilants. Diphthong system retained "
            "but vowel-reduction patterns approaching Castilian."
        ),
    ),
    "ast-ES-x-leon": LanguageSpec(
        code="ast-ES-x-leon",
        name="Leonese",
        family="Asturleonese",
        script="Latin",
        graphemes=GRAPHEMES_LEON,
        allophones=ALLOPHONES_LEON,
        parent="ast",
        notes=(
            "Leonese (Llionés), spoken in the provinces of León, Zamora, "
            "and Salamanca. Southern continuation of Asturleonese. Shares "
            "core features with Asturian (diphthongs, betacism, palatal [ʎ], "
            "ye copula) but under heavier Castilian pressure. Some Zamoran "
            "varieties show aspiration of /x/ → [h]. Related to Mirandese "
            "(Portugal) which descends from the same Leonese branch."
        ),
    ),
}
