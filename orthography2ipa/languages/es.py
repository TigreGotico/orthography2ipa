"""Spanish (es, es-419, es-AR) — grapheme→IPA and allophone mappings.

Sources:
- Hualde, J.I. (2005). *The Sounds of Spanish*.
- RAE (2011). *Nueva gramática de la lengua española: Fonética y fonología*.
- Quilis, A. (1993). *Tratado de fonología y fonética españolas*.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# Castilian Spanish (Peninsular)
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_ES = {
    # --- Vowels (5-vowel system, transparent orthography) ---
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],
    "á": ["a"],
    "é": ["e"],
    "í": ["i"],
    "ó": ["o"],
    "ú": ["u"],
    "ü": ["w"],  # diaeresis: pronounced /w/ in ⟨güe⟩, ⟨güi⟩

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "θ"],  # /k/ before a,o,u; /θ/ before e,i (Castilian)
    "ç": ["s"],  # historical, rare
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "x"],  # /ɡ/ before a,o,u; /x/ before e,i
    "h": [""],  # always silent
    "j": ["x"],
    "k": ["k"],  # loanwords
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "ñ": ["ɲ"],
    "p": ["p"],
    "q": ["k"],  # only in ⟨qu⟩
    "r": ["ɾ"],  # tap (single ⟨r⟩ intervocalic)
    "s": ["s"],
    "t": ["t"],
    "v": ["b"],  # merged with /b/ in standard Spanish
    "w": ["w"],  # loanwords
    "x": ["ks", "s"],  # /ks/ standard; /s/ in some words (México)
    "y": ["ʝ", "i"],  # consonantal /ʝ/; vowel /i/ (word-final)
    "z": ["θ"],  # Castilian

    # --- Consonant digraphs ---
    "ch": ["tʃ"],
    "ll": ["ʎ", "ʝ"],  # /ʎ/ traditional; /ʝ/ yeísmo
    "rr": ["r"],  # alveolar trill
    "qu": ["k"],  # ⟨u⟩ silent before e,i
    "gu": ["ɡ"],  # ⟨u⟩ silent before e,i

    # --- Diphthongs (official rising and falling) ---
    # Rising (semivowel + vowel)
    "ia": ["ja"], "ie": ["je"], "io": ["jo"], "iu": ["ju"],
    "ua": ["wa"], "ue": ["we"], "uo": ["wo"], "ui": ["wi"],
    # Falling (vowel + semivowel)
    "ai": ["aj"], "ei": ["ej"], "oi": ["oj"],
    "au": ["aw"], "eu": ["ew"], "ou": ["ow"],
    # ⟨ay⟩, ⟨ey⟩, ⟨oy⟩ word-final variants
    "ay": ["aj"], "ey": ["ej"], "oy": ["oj"],

    # --- Triphthongs ---
    "iai": ["jaj"], "iei": ["jej"], "uai": ["waj"], "uei": ["wej"],
    "ioi": ["joj"],
}

ALLOPHONES_ES = {
    # Plosives → spirants (lenition)
    "b": ["b", "β"],  # [β] intervocalic / after continuant
    "d": ["d", "ð"],  # [ð] intervocalic / after continuant
    "ɡ": ["ɡ", "ɣ"],  # [ɣ] intervocalic / after continuant

    "p": ["p"],
    "t": ["t", "t̪"],  # dental before /θ/
    "k": ["k"],

    # Fricatives
    "f": ["f"],
    "θ": ["θ"],  # Castilian only
    "s": ["s", "z"],  # [z] before voiced consonant
    "x": ["x", "h"],  # [h] in Caribbean/Andalusian dialects
    "ʝ": ["ʝ", "ɟʝ", "ʃ"],  # affricated post-pausal; [ʃ] in Rioplatense

    # Affricates
    "tʃ": ["tʃ"],

    # Nasals
    "m": ["m"],
    "n": ["n", "m", "ɱ", "n̪", "ŋ", "ɲ"],  # assimilates to following C place
    "ɲ": ["ɲ"],

    # Laterals
    "l": ["l", "l̪", "ɫ"],  # dental before /t,d/; dark in coda (dialectal)
    "ʎ": ["ʎ"],  # only in lleísta dialects

    # Rhotics
    "ɾ": ["ɾ"],  # tap
    "r": ["r"],  # trill

    # Glides
    "j": ["j"],
    "w": ["w", "ɣʷ"],  # [ɣʷ] after consonant in some analyses

    # Vowels (no significant allophony — transparent system)
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Latin American Spanish (es-419)
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_ES_LA = {
    **GRAPHEMES_ES,
    "c": ["k", "s"],  # seseo: /s/ before e,i (no /θ/)
    "z": ["s"],  # seseo
    "ll": ["ʝ"],  # yeísmo universal
    "y": ["ʝ", "i"],
}

ALLOPHONES_ES_LA = {
    **ALLOPHONES_ES,
    # no /θ/ phoneme
    "s": ["s", "z", "h"],  # aspiration in Caribbean, coda weakening
}

# ═══════════════════════════════════════════════════════════════════════════
# Rioplatense Spanish (es-AR)
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_ES_AR = {
    **GRAPHEMES_ES_LA,
    "ll": ["ʃ", "ʒ"],  # žeísmo / šeísmo
    "y": ["ʃ", "ʒ", "i"],
}

ALLOPHONES_ES_AR = {
    **ALLOPHONES_ES_LA,
    "ʝ": ["ʃ", "ʒ"],  # devoiced in younger Buenos Aires speakers
}

# ── Specs ──────────────────────────────────────────────────────────────────
SPECS = {
    "es": LanguageSpec(
        code="es",
        name="Spanish (Castilian)",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_ES,
        allophones=ALLOPHONES_ES,
        parent="la-x-hispania",
        ancestors=(
            Ancestor("la-x-hispania", P, 0.80,
                     "Primary descent from Hispanic Vulgar Latin"),
            Ancestor("xaq", SUB, 0.08,
                     "Basque substrate: f->h, 5-vowel reinforcement"),
            Ancestor("xaa", AD, 0.07,
                     "Andalusi Arabic adstrate: ~4000 loanwords"),
            Ancestor("got", SUP, 0.05,
                     "Visigothic superstrate: guerra, guardar, ropa"),
        ),
        notes="Peninsular Castilian with distinción (θ/s contrast).",
    ),
    "es-419": LanguageSpec(
        code="es-419",
        name="Latin American Spanish",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_ES_LA,
        allophones=ALLOPHONES_ES_LA,
        parent="es",
        notes="Seseo, yeísmo. Coda /s/ aspiration noted in allophone map.",
    ),
    "es-AR": LanguageSpec(
        code="es-AR",
        name="Rioplatense Spanish",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_ES_AR,
        allophones=ALLOPHONES_ES_AR,
        parent="es",
        notes="Buenos Aires / Rioplatense: žeísmo/šeísmo for ⟨ll⟩/⟨y⟩.",
    ),
}
