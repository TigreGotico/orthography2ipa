"""Asturian / Leonese (ast) — grapheme→IPA and allophone mappings.

Asturian (Asturianu/Bable) is an Asturleonese language spoken in the
Principality of Asturias and parts of León, Zamora, and Salamanca (Spain).
~100,000+ speakers. Not yet officially recognised at state level despite
decades of normativization by the Academia de la Llingua Asturiana (ALLA).

Three main dialectal blocks plus Leonese (eastern continuation).

Sources:
- ALLA (2021). *Normes Ortográfiques* (8ª ed. revisada). Uviéu.
- ALLA (2001). *Gramática de la Llingua Asturiana* (GrALLA, 3ª ed.).
- Arias Cabal, Á. (2002). El asturiano. In: Estudios filolóxicos asturianos.
- Cano González, A.M. (2009). Asturianu. In: Atlas Lingüístico de la
  Península Ibérica.
- García Arias, X.L. (2003). *Gramática histórica de la lengua asturiana*.
- Muñiz Cachón, C. (2002). Rasgos fónicos del asturiano.

Conventions:
- ISO 639-3: ast. Central Asturian = standard (ALLA norms).
- Western: ast-x-occidental. Eastern: ast-x-oriental.
- Leonese (Spain): ast-ES-x-leon.

Phoneme inventory per ALLA Normes §1.7:
  Vowels: /a, e, i, o, u/
  Consonants: /p, t, tʃ, k, b, d, ɡ, ʝ, f, θ, s, ʃ, m, n, ɲ, l, ʎ, ɾ, r/

Key distinctions from Castilian:
- ⟨x⟩ = /ʃ/ (postalveolar fricative), NOT Castilian /x/ (velar)
- ⟨j⟩ is foreign-word only (§1.1.6); no native /x/ phoneme
- ⟨g⟩ before e,i = /ɡ/ via digraph ⟨gu⟩, never /x/
- ⟨ḥ⟩ or ⟨h.⟩ = aspiration in eastern varieties (§1.1.2)
- ⟨ḷḷ⟩ or ⟨l.l⟩ = "che vaqueira" western sound (§1.1.3)
- ⟨ts⟩ = western dialectal [ts] for /tʃ/ (§1.1.4)
- ⟨yy⟩ = western dialectal [ky] for /ʝ/ (§1.1.5)
- /s/ = apico-alveolar [s̺] (not Castilian laminal)
- Palatal lateral /ʎ/ preserved (no yeísmo in standard)
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec, GraphemePosition as GP

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# Central Asturian (standard — ALLA norms)
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_AST = {
    # --- Vowels (5-vowel system, §1.2) ---
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],
    # Accented forms (same phonemic value, §1.9.1)
    "á": ["a"], "é": ["e"], "í": ["i"], "ó": ["o"], "ú": ["u"],

    # --- Consonants (§1.7) ---
    "b": ["b"],            # /b/ (§1.7.5); betacism — same phoneme as ⟨v⟩
    "c": ["k", "θ"],       # /k/ before a,o,u,l,r; /θ/ before e,i (§1.7.4, §1.7.10)
    "d": ["d"],            # /d/ (§1.7.6)
    "f": ["f"],            # /f/ (§1.7.9)
    "g": ["ɡ"],            # /ɡ/ before a,o,u,l,r (§1.7.8); before e,i use ⟨gu⟩
    "h": [""],             # silent (§1.7.20); h muda
    "k": ["k"],            # /k/ in foreign words (§1.1.6)
    "l": ["l"],            # /l/ (§1.7.16)
    "m": ["m"],            # /m/ (§1.7.13)
    "n": ["n"],            # /n/ (§1.7.14)
    "ñ": ["ɲ"],            # /ɲ/ (§1.7.15)
    "p": ["p"],            # /p/ (§1.7.1)
    "q": ["k"],            # only in ⟨qu⟩ + e,i → /k/ (§1.7.4.2)
    "r": ["ɾ"],            # /ɾ/ tap (§1.7.18); trill /r/ word-initial (§1.7.19.1a)
    "s": ["s"],            # /s/ apico-alveolar (§1.7.11)
    "t": ["t"],            # /t/ (§1.7.2)
    "v": ["b"],            # /b/ betacism (§1.7.5)
    "w": ["w"],            # in foreign words (§1.1.6)
    "x": ["ʃ"],            # /ʃ/ voiceless postalveolar fricative (§1.7.12)
    "y": ["ʝ", "i"],       # /ʝ/ consonantal; /i/ as vowel/glide (§1.7.7, §1.2.1)
    "z": ["θ"],            # /θ/ (§1.7.10.2)

    # --- Digraphs (§1.1.1) ---
    "ch": ["tʃ"],          # /tʃ/ (§1.7.3)
    "ll": ["ʎ"],           # /ʎ/ palatal lateral — no yeísmo in standard (§1.7.17)
    "rr": ["r"],           # /r/ alveolar trill between vowels (§1.7.19)
    "qu": ["k"],           # /k/ before e,i (§1.7.4.2)
    "gu": ["ɡ"],           # /ɡ/ before e,i (§1.7.8.2)

    # --- Diaeresis digraphs (§1.9.3) ---
    "güe": ["ɡwe"],        # /ɡ/ + /we/: güesu, güevu
    "güi": ["ɡwi"],        # /ɡ/ + /wi/: güisqui

    # --- Aspiration grapheme (§1.1.2) ---
    "ḥ": ["h"],            # aspiration in eastern varieties / orientalisms
    "h.": ["h"],           # alternative notation for aspiration

    # --- Dialectal graphemes accepted in standard orthography ---
    "ts": ["ts"],          # western dialectal [ts] for /tʃ/ (§1.1.4)
    "yy": ["ky"],          # western dialectal [ky] for /ʝ/ (§1.1.5)

    # --- Asturleonese diphthongs (from Lat. Ĕ and Ŏ, §1.6.1) ---
    "ue": ["we"],          # Lat. Ŏ → ue: puerta, fueru, rueda
    "ie": ["je"],          # Lat. Ĕ → ie: piedra, tierra, siete

    # --- Falling diphthongs (§1.6.1b) ---
    "ai": ["aj"], "ei": ["ej"], "oi": ["oj"],
    "au": ["aw"], "eu": ["ew"], "ou": ["ow"],

    # --- Rising diphthongs (§1.6.1a) ---
    "ia": ["ja"], "io": ["jo"], "iu": ["ju"],
    "ua": ["wa"], "uo": ["wo"], "ui": ["wi"],
}

ALLOPHONES_AST = {
    # Plosives — standard Iberian lenition
    "p": ["p"],
    "b": ["b", "β"],       # [b] post-pause/nasal; [β] elsewhere
    "t": ["t"],
    "d": ["d", "ð"],       # [d] post-pause/nasal; [ð] elsewhere
    "k": ["k"],
    "ɡ": ["ɡ", "ɣ"],       # [ɡ] post-pause/nasal; [ɣ] elsewhere

    # Fricatives
    "f": ["f"],
    "θ": ["θ"],
    "s": ["s̺"],            # apico-alveolar (distinct from Castilian laminal)
    "ʃ": ["ʃ"],            # ⟨x⟩ = /ʃ/
    "ʝ": ["ʝ", "ɟʝ"],     # palatal: fricative ~ affricate

    # Affricates
    "tʃ": ["tʃ"],
    "ts": ["ts"],           # in western/archaic forms (§1.1.4)

    # Nasals
    "m": ["m"],
    "n": ["n", "ŋ"],       # [ŋ] before velars; nasal place assimilation
    "ɲ": ["ɲ"],

    # Laterals
    "l": ["l"],
    "ʎ": ["ʎ"],            # preserved in standard — no yeísmo

    # Rhotics
    "ɾ": ["ɾ"],            # tap
    "r": ["r"],             # trill

    # Glides
    "j": ["j"],
    "w": ["w"],

    # Aspiration (§1.1.2: ⟨ḥ⟩/⟨h.⟩ for eastern/orientalism)
    "h": ["h"],

    # Vowels (no reduction in standard Asturian)
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],
}

# Cano González (2009). Asturian shares Ibero-Romance lenition.
# ALLA Normes §1.7.19.1: ⟨r⟩ word-initial = trill [r];
# after n, l, s = trill; intervocalic = tap [ɾ].

POSITIONAL_AST = {
    "b": {
        GP.DEFAULT: ["b"],
        GP.INTERVOCALIC: ["β"],
    },
    "d": {
        GP.DEFAULT: ["d"],
        GP.INTERVOCALIC: ["ð"],
    },
    "g": {
        GP.DEFAULT: ["ɡ"],
        GP.INTERVOCALIC: ["ɣ"],
    },
    "r": {
        GP.WORD_INITIAL: ["r"],       # §1.7.19.1a: strong at word start
        GP.INTERVOCALIC: ["ɾ"],       # tap between vowels (single ⟨r⟩)
        GP.ONSET: ["ɾ"],             # in clusters: pr, tr, cr, etc. (§1.7.19.1c)
        GP.CODA: ["ɾ"],             # word-final / syllable-final (§1.7.19.1d)
    },
    "n": {
        GP.DEFAULT: ["n"],
        GP.CODA: ["n", "ŋ"],         # velar assimilation before velars
    },
}

# ═══════════════════════════════════════════════════════════════════════════
# Western Asturian (asturianu oucidental)
# Strongest archaic features: aspirated f-, -ḷḷ- che vaqueira, etc.
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_AST_W = {
    **GRAPHEMES_AST,
    # Western hallmark: Lat. F- → aspiration (§1.1.2.1)
    "h": ["h"],            # aspirated h- from Latin F- (hallmark western feature)
    # "Che vaqueira" — western lateral realisation (§1.1.3)
    # ALLA approves both ⟨ḷḷ⟩ and ⟨l.l⟩ notations
    "ḷḷ": ["ɖ"],           # che vaqueira: retroflex / affricate realisation
    "l.l": ["ɖ"],          # alternative ALLA notation for che vaqueira
    "uo": ["wo"],          # diphthong variant (cf. central ue)
}

ALLOPHONES_AST_W = {
    **ALLOPHONES_AST,
    "h": ["h"],            # aspiration from Lat. F-: forno→hornu, filu→hilu
    "ɖ": ["ɖ", "ʈʂ", "ts̺"],  # che vaqueira variants across western subdialects
    "f": ["f", "h"],       # F- → h- is the western hallmark
}

# ── Western Asturian: f→h aspiration ─────────────────────────────────────
POSITIONAL_AST_W = {
    **POSITIONAL_AST,
    "f": {
        GP.WORD_INITIAL: ["h", "f"],  # Latin F- → [h] (forno → hornu)
        GP.INTERVOCALIC: ["f"],       # retained intervocalically
    },
}

# ═══════════════════════════════════════════════════════════════════════════
# Eastern Asturian (asturianu oriental)
# Transitional to Cantabrian; mass diphthongs, Castilian influence
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_AST_E = {
    **ALLOPHONES_AST,
    "s": ["s̺", "s"],      # mixed apical/laminal due to Castilian contact
    "ʎ": ["ʎ", "ʝ"],      # yeísmo creeping in from Castilian contact
}

# ═══════════════════════════════════════════════════════════════════════════
# Leonese (ast-ES-x-leon) — spoken in León, Zamora, Salamanca
# Continuation of Asturleonese south of the Cantabrian mountains
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_LEON = {
    **GRAPHEMES_AST,
    # Leonese preserves some features shared with Mirandese
    "ll": ["ʎ"],           # palatalization of -LL- consistent
}

ALLOPHONES_LEON = {
    **ALLOPHONES_AST,
    "ʎ": ["ʎ"],           # conservative — no yeísmo
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
        positional_graphemes=POSITIONAL_AST,
        parent="la",
        ancestors=(
            Ancestor("la-x-hispania", P, 0.80,
                     "Primary descent from Hispanic Vulgar Latin"),
            Ancestor("cel", SUB, 0.06,
                     "Celtic (Astures) substrate: tribal name itself is Celtic; "
                     "strong NW Iberian Celtic presence; cf. "
                     "García Arias (2003)"),
            Ancestor("got", SUP, 0.04,
                     "Visigothic superstrate: Kingdom of Asturias (718-924 CE) "
                     "was the first Christian successor state"),
            Ancestor("xaa", AD, 0.02,
                     "Arabic adstrate: minimal — Asturias never fully conquered"),
        ),
        notes=(
            "Central Asturian per ALLA (Academia de la Llingua Asturiana) "
            "norms (8th ed., 2021). ~100,000+ speakers. 5-vowel system, "
            "apico-alveolar [s̺], Leonese diphthongs (Ĕ → [je], Ŏ → [we]). "
            "Palatal lateral [ʎ] from Latin -LL-. Neuter gender "
            "(lo: mass/uncountable). 3sg copula ye. "
            "Native phoneme inventory per §1.7: "
            "/p, t, tʃ, k, b, d, ɡ, ʝ, f, θ, s, ʃ, m, n, ɲ, l, ʎ, ɾ, r/. "
            "Note: /x/ (velar fricative) is NOT a native phoneme — Asturian "
            "uses /ʃ/ where Castilian uses /x/. ⟨j⟩ appears only in "
            "foreign words. Pending official recognition in Spain."
        ),
    ),
    "ast-x-occidental": LanguageSpec(
        code="ast-x-occidental",
        name="Western Asturian",
        family="Asturleonese",
        script="Latin",
        graphemes=GRAPHEMES_AST_W,
        allophones=ALLOPHONES_AST_W,
        positional_graphemes=POSITIONAL_AST_W,
        parent="ast",
        notes=(
            "Western Asturian (asturianu oucidental). Most archaic variety. "
            "Hallmark: Latin F- → [h] aspiration (forno→hornu). "
            "Latin -LL- → 'che vaqueira' [ɖ~ʈʂ~ts̺] instead of palatal [ʎ] "
            "(written ⟨ḷḷ⟩ or ⟨l.l⟩ per ALLA §1.1.3). "
            "Closest to Galician-Portuguese in several phonological traits. "
            "Diphthongs may show -uo- alongside -ue-. "
            "§1.1.4: ⟨ts⟩ for /tʃ/ in some zones. "
            "§1.1.5: ⟨yy⟩ for [ky] in some zones."
        ),
    ),
    "ast-x-oriental": LanguageSpec(
        code="ast-x-oriental",
        name="Eastern Asturian",
        family="Asturleonese",
        script="Latin",
        graphemes=GRAPHEMES_AST,
        allophones=ALLOPHONES_AST_E,
        positional_graphemes=POSITIONAL_AST,
        parent="ast",
        notes=(
            "Eastern Asturian, transitional to Cantabrian/Castilian. "
            "Strongest Castilian influence: incipient yeísmo ([ʎ]→[ʝ]), "
            "mixed apical/laminal sibilants. Diphthong system retained "
            "but vowel-reduction patterns approaching Castilian. "
            "§1.1.2: ⟨ḥ⟩ aspiration in orientalisms (ḥou, ḥue)."
        ),
    ),
    "ast-ES-x-leon": LanguageSpec(
        code="ast-ES-x-leon",
        name="Leonese",
        family="Asturleonese",
        script="Latin",
        graphemes=GRAPHEMES_LEON,
        allophones=ALLOPHONES_LEON,
        positional_graphemes=POSITIONAL_AST,
        parent="ast",
        notes=(
            "Leonese (Llionés), spoken in the provinces of León, Zamora, "
            "and Salamanca. Southern continuation of Asturleonese. Shares "
            "core features with Asturian (diphthongs, betacism, palatal [ʎ], "
            "ye copula) but under heavier Castilian pressure. Some Zamoran "
            "varieties show aspiration of velar fricatives. Related to "
            "Mirandese (Portugal) which descends from the same Leonese branch."
        ),
    ),
}