"""Catalan subdialects + Aranese — grapheme→IPA and allophone mappings.

Catalan has two major dialect blocks (Eastern/Western) with several
subvarieties. Aranese is the Gascon Occitan variety spoken in Val d'Aran.

Sources:
Conventions:
- ca = Central Catalan (already in base module).
- ca-x-valencia = Valencian.
- ca-x-balear = Balearic (Mallorquín/Menorquín/Eivissenc).
- ca-x-nord = Northern/Rossellonès.
- ca-x-occidental = Northwestern (Lleidatà).
- oc-x-aranes = Aranese (Gascon Occitan, co-official in Catalonia).
"""
from orthography2ipa.types import LanguageSpec, GraphemePosition as GP
from orthography2ipa.languages.oc import POSITIONAL_OC
GRAPHEMES = {
    # --- Vowels (7 stressed, reduced unstressed) ---
    "a": ["a", "ə"],
    "e": ["e", "ɛ", "ə"],
    "i": ["i"],
    "o": ["o", "ɔ", "u"],
    "u": ["u"],
    "à": ["a"], "è": ["ɛ"], "é": ["e"],
    "í": ["i"], "ò": ["ɔ"], "ó": ["o"], "ú": ["u"],
    "ï": ["i"], "ü": ["u"],  # diaeresis = hiatus

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "s"],
    "ç": ["s"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "ʒ"],  # /ʒ/ before e,i
    "h": [""],
    "j": ["ʒ"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],
    "r": ["ɾ", "r"],  # tap / trill
    "s": ["s", "z"],
    "t": ["t"],
    "v": ["b"],  # merged with /b/ in most Central Catalan
    "w": ["w"],
    "x": ["ʃ", "ks"],  # /ʃ/ initial; /ks/ medial
    "z": ["z"],

    # --- Digraphs ---
    "ig": ["tʃ"],  # word-final: ⟨ig⟩ = [tʃ]
    "ix": ["ʃ"],  # after vowel
    "ll": ["ʎ"],
    "l·l": ["lː"],  # ela geminada
    "ny": ["ɲ"],
    "qu": ["k", "kw"],
    "gu": ["ɡ", "ɡw"],
    "rr": ["r"],
    "ss": ["s"],
    "tg": ["dʒ"],  # before e,i
    "tj": ["dʒ"],
    "tx": ["tʃ"],

    # --- Diphthongs (falling) ---
    "ai": ["aj"], "ei": ["əj"], "oi": ["ɔj"], "ui": ["uj"],
    "au": ["aw"], "eu": ["əw"], "ou": ["ɔw"], "iu": ["iw"],
    # Rising
    "ua": ["wa"], "ue": ["wɛ"], "uo": ["wɔ"],
    "ia": ["ja"], "ie": ["jɛ"], "io": ["jɔ"],
}

ALLOPHONES = {
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
    "p": ["p"], "t": ["t"], "k": ["k"],
    "f": ["f"], "v": ["v", "β"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ"],
    "m": ["m", "ɱ"],
    "n": ["n", "m", "ɱ", "ŋ", "ɲ"],
    "ɲ": ["ɲ"], "ŋ": ["ŋ"],
    "l": ["l"], "ʎ": ["ʎ"], "lː": ["lː"],
    "ɾ": ["ɾ"], "r": ["r"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "ə": ["ə"],
    "e": ["e"], "ɛ": ["ɛ"],
    "i": ["i"],
    "o": ["o"], "ɔ": ["ɔ"],
    "u": ["u"],
}

# Wheeler (2005), Recasens (1993).
# Central Catalan has strong vowel reduction: unstressed /a,e,ɛ/ → [ə],
# unstressed /o,ɔ/ → [u].

POSITIONAL_CA = {
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
    # ── Vowel reduction (Central Catalan) ────────────────────────────────
    # Stressed: full 7-vowel system; unstressed: reduced to [ə, i, u]
    "a": {
        GP.DEFAULT: ["a"],
        GP.NUCLEUS: ["ə"],  # unstressed reduction
    },
    "e": {
        GP.DEFAULT: ["ɛ", "e"],
        GP.NUCLEUS: ["ə"],  # unstressed → [ə]
    },
    "o": {
        GP.DEFAULT: ["ɔ", "o"],
        GP.NUCLEUS: ["u"],  # unstressed → [u]
    },
    # ── Sibilant voicing ─────────────────────────────────────────────────
    "s": {
        GP.DEFAULT: ["s"],
        GP.INTERVOCALIC: ["z"],  # single ⟨s⟩ between vowels = [z]
    },
    "r": {
        GP.WORD_INITIAL: ["r"],  # trill
        GP.INTERVOCALIC: ["ɾ"],
        GP.ONSET: ["ɾ"],
        GP.CODA: ["ɾ"],
    },
    # ── ⟨l⟩: some velarisation in coda ───────────────────────────────────
    "l": {
        GP.ONSET: ["l"],
        GP.CODA: ["l", "ɫ"],  # light velarisation
    },
}

# ═══════════════════════════════════════════════════════════════════════════
# Valencian (ca-x-valencia)
# Western Catalan block; distinct vowel reduction, /v/ preservation
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_VAL = {
    **GRAPHEMES,
    "v": ["v"],  # /v/ phonemically distinct from /b/ in Valencian
    # Valencian: apicoalveolar /s̺/ (like Castilian) vs standard Catalan /s/
    "s": ["s̺", "z̺"],
    # Final -r pronounced (unlike Central Catalan)
    "r": ["ɾ", "r"],
}

ALLOPHONES_VAL = {
    **ALLOPHONES,
    # /v/ is a distinct phoneme (labiodental)
    "v": ["v"],
    "b": ["b", "β"],
    # LESS vowel reduction than Central Catalan
    # Valencian: unstressed /a/ → [a] (NOT [ə]); /e/ → [e] (NOT [ə]); /o/ → [o] (NOT [u])
    "a": ["a"],  # no reduction to schwa
    "e": ["e"],
    "ɛ": ["ɛ"],
    "o": ["o"],
    "ɔ": ["ɔ"],
    "ə": ["a", "e"],  # schwa doesn't exist in Valencian
    # Apico-alveolar sibilants
    "s": ["s̺"],
    "z": ["z̺"],
    # Voiced affricate preserved where Central has [ʒ]
    "dʒ": ["dʒ"],
    "ʒ": ["dʒ", "ʒ"],  # word-initial [dʒ] more robust
}

# ── Valencian: no unstressed vowel reduction ─────────────────────────────
POSITIONAL_CA_VALENCIA = {
    **POSITIONAL_CA,
    "a": {
        GP.DEFAULT: ["a"],
        GP.NUCLEUS: ["a"],  # NO reduction (unlike Central)
    },
    "e": {
        GP.DEFAULT: ["ɛ", "e"],
        GP.NUCLEUS: ["e"],  # preserved
    },
    "o": {
        GP.DEFAULT: ["ɔ", "o"],
        GP.NUCLEUS: ["o"],  # preserved (not → [u])
    },
}

# ═══════════════════════════════════════════════════════════════════════════
# Balearic (ca-x-balear)
# Eastern block; most archaic variety, articles salat, schwa system
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_BAL = {
    **GRAPHEMES,
    "v": ["v"],  # /v/ distinct in some Balearic varieties
}

ALLOPHONES_BAL = {
    **ALLOPHONES,
    # Vowel reduction — even more extreme than Central
    "a": ["a", "ə"],
    "e": ["e", "ə"],
    "ɛ": ["ɛ"],
    "o": ["o", "u", "ə"],  # unstressed /o/ → [u] or even [ə]
    "ɔ": ["ɔ"],
    # Dark /l/ in all positions (characteristic Balearic)
    "l": ["l", "ɫ"],
    # /v/ in some varieties
    "v": ["v", "β"],
    # Deaffrication of /tʃ/ → [ʃ] in Mallorcan
    "tʃ": ["tʃ", "ʃ"],
    # Yodization of coda laterals: /ʎ/ robust
    "ʎ": ["ʎ"],
    # Article salat (es/sa) reflected in morphology, not phonology
}

# ── Balearic: partial reduction ──────────────────────────────────────────
POSITIONAL_CA_BALEAR = {
    **POSITIONAL_CA,
    # Balearic has a fuller unstressed system than Central
    "o": {
        GP.DEFAULT: ["ɔ", "o"],
        GP.NUCLEUS: ["o"],  # less reduction than Central
    },
}

# ═══════════════════════════════════════════════════════════════════════════
# Northern Catalan / Rossellonès (ca-x-nord)
# French influence; loss of final unstressed vowels
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_NORD = {
    **ALLOPHONES,
    # French-influenced features
    "ʁ": ["ʁ"],  # uvular rhotic (French influence) alongside [r]
    "r": ["r", "ʁ"],
    "ɾ": ["ɾ", "ʁ"],
    # Loss of final unstressed vowels more extreme
    "a": ["a", "ə", "∅"],
    "e": ["e", "ə", "∅"],
    "o": ["o", "u"],
    # Voicing of intervocalic stops (French-like)
    "p": ["p", "b"],
    "t": ["t", "d"],
    "k": ["k", "ɡ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Northwestern Catalan / Lleidatà (ca-x-occidental)
# Western block; minimal vowel reduction like Valencian
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_OCCI = {
    **ALLOPHONES,
    # Western block: less vowel reduction
    "a": ["a"],
    "e": ["e"],
    "o": ["o"],
    "ə": ["a", "e"],  # no phonemic schwa
    # Otherwise close to standard in consonants
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Aranese / Aranès (oc-x-aranes)
# Gascon Occitan variety, co-official in Val d'Aran (Catalonia)
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_ARANES = {
    # Aranese follows classical Occitan orthography with Gascon features
    "a": ["a", "ɔ"],  # final -a → [ɔ] (Gascon)
    "e": ["e", "ɛ"],
    "i": ["i"],
    "o": ["u", "ɔ"],  # ⟨o⟩ → [u] in many positions
    "u": ["y"],  # front rounded (as Occitan)
    "à": ["a"], "è": ["ɛ"], "é": ["e"],
    "í": ["i"], "ò": ["ɔ"], "ó": ["o"], "ú": ["y"],

    # Consonants
    "b": ["b"],
    "c": ["k", "s"],
    "ç": ["s"],
    "d": ["d"],
    "f": ["f", "h"],  # Lat. F- → [h] in Gascon (hallmark Gascon feature)
    "g": ["ɡ", "dʒ"],
    "h": ["h"],  # aspirated (from Lat. F-)
    "j": ["dʒ"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],
    "r": ["r", "ɾ"],
    "s": ["s", "z"],
    "t": ["t"],
    "v": ["v", "b"],  # /v/ distinct in careful speech
    "x": ["ks"],
    "z": ["z"],

    # Digraphs
    "ch": ["tʃ"],
    "lh": ["ʎ"],
    "nh": ["ɲ"],
    "rr": ["r"],
    "ss": ["s"],
    "qu": ["k", "kw"],
    "gu": ["ɡ", "ɡw"],
    "sh": ["ʃ"],  # Gascon: voiced/voiceless postalveolar
    "th": ["t"],  # archaic spelling

    # Diphthongs
    "ai": ["aj"], "au": ["aw"], "ei": ["ej"], "eu": ["ew"],
    "oi": ["uj"], "ou": ["ow"], "iu": ["jy"], "ui": ["yj"],
}

ALLOPHONES_ARANES = {
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
    "p": ["p"], "t": ["t"], "k": ["k"],
    "f": ["f", "h"],  # Gascon F- → h- aspiration
    "h": ["h"],
    "v": ["v", "β"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ"],
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "ʎ": ["ʎ"],
    "ɾ": ["ɾ"], "r": ["r"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "ɔ": ["ɔ"],
    "e": ["e"], "ɛ": ["ɛ"],
    "i": ["i"],
    "o": ["o"], "u": ["u"], "y": ["y"],
}

SPECS = {
    "ca": LanguageSpec(
        code="ca",
        name="Catalan",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        positional_graphemes=POSITIONAL_CA,
        parent="la",
        notes=(
            "Central Catalan (Barcelona standard). Vowel reduction "
            "(a,e→[ə], o→[u] in unstressed) is systematic. "
            "⟨l·l⟩ (ela geminada) is a unique Catalan digraph."
        ),
    ),
    "ca-x-valencia": LanguageSpec(
        code="ca-x-valencia",
        name="Valencian",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_VAL,
        allophones=ALLOPHONES_VAL,
        positional_graphemes=POSITIONAL_CA_VALENCIA,
        parent="ca",
        notes=(
            "Valencian (Valencià). Western Catalan block, co-official in "
            "Comunitat Valenciana. Key differences from Central Catalan: "
            "/v/ vs /b/ distinction preserved, apico-alveolar sibilants "
            "[s̺, z̺], MINIMAL vowel reduction (no schwa — unstressed /a/ "
            "stays [a], /e/ stays [e], /o/ stays [o]). Word-final -r "
            "pronounced. Voiced affricate [dʒ] more robust. "
            "Regulated by Acadèmia Valenciana de la Llengua (AVL)."
        ),
    ),
    "ca-x-balear": LanguageSpec(
        code="ca-x-balear",
        name="Balearic Catalan",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_BAL,
        allophones=ALLOPHONES_BAL,
        positional_graphemes=POSITIONAL_CA_BALEAR,
        parent="ca",
        notes=(
            "Balearic (Mallorquí/Menorquí/Eivissenc). Eastern block, "
            "most archaic Catalan variety. Extreme vowel reduction "
            "(beyond Central Catalan). Article salat (es/sa instead of "
            "el/la). Partial /v/ preservation. Deaffrication of /tʃ/ → [ʃ] "
            "in Mallorcan. Dark [ɫ] in all positions. Conservative "
            "palatal lateral [ʎ]. Some varieties preserve /v/."
        ),
    ),
    "ca-x-nord": LanguageSpec(
        code="ca-x-nord",
        name="Northern Catalan (Rossellonès)",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES_NORD,
        positional_graphemes=POSITIONAL_CA,
        parent="ca",
        notes=(
            "Northern Catalan (Rossellonès/Septentrional). Spoken in "
            "Pyrénées-Orientales, France. Eastern block. French influence: "
            "uvular rhotic [ʁ] alongside traditional [r], possible "
            "intervocalic stop voicing (French pattern), extreme final "
            "vowel deletion. Declining rapidly under French pressure."
        ),
    ),
    "ca-x-occidental": LanguageSpec(
        code="ca-x-occidental",
        name="Northwestern Catalan (Lleidatà)",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES_OCCI,
        positional_graphemes=POSITIONAL_CA,
        parent="ca",
        notes=(
            "Northwestern Catalan (Lleidatà/Pallarès). Western block, "
            "spoken in Lleida and Pyrenean valleys. Like Valencian: "
            "minimal vowel reduction (no phonemic schwa), 7-vowel system "
            "maintained in all positions. Otherwise consonant system "
            "close to Central Catalan standard."
        ),
    ),
    "oc-x-aranes": LanguageSpec(
        code="oc-x-aranes",
        name="Aranese (Gascon Occitan)",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_ARANES,
        allophones=ALLOPHONES_ARANES,
        positional_graphemes=POSITIONAL_OC,
        parent="oc",
        notes=(
            "Aranese (Aranès). Gascon variety of Occitan spoken in Val "
            "d'Aran, Catalonia. ~2,800 speakers. Co-official with Catalan "
            "and Spanish in Catalonia. Hallmark Gascon features: Latin "
            "F- → [h] aspiration (fo→hòc, flor→hlòr), final -a → [ɔ], "
            "front rounded /y/ (⟨u⟩). Regulated by Conselh Generau d'Aran. "
            "Classical Occitan orthography with Gascon conventions."
        ),
    ),
}
