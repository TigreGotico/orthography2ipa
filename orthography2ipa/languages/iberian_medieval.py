"""Medieval Iberian languages — Hispanic Latin, Mozarabic, Andalusi Arabic.

These bridge the gap between the pre-Roman/Roman period and the modern
Ibero-Romance languages.

Sources:
- Penny, R. (2002). *A History of the Spanish Language*. 2nd ed. CUP.
- Lloyd, P.M. (1987). *From Latin to Spanish*. American Philosophical Soc.
- Herman, J. (2000). *Vulgar Latin*. Penn State UP.
- Galmés de Fuentes, Á. (1983). *Dialectología mozárabe*. Gredos.
- Corriente, F. (2013). *A Descriptive and Comparative Grammar of
  Andalusi Arabic*. 2nd ed. Brill.
- Corriente, F. (1977). *A Grammatical Sketch of the Spanish Arabic
  Dialect Bundle*. IHAC.
- Griffin, D.A. (1961). *Los mozarabismos del «Vocabulista» atribuido
  a Ramón Martí*. CSIC.
"""
from orthography2ipa.types import LanguageSpec

# ═══════════════════════════════════════════════════════════════════════════
# HISPANIC VULGAR LATIN (la-x-hispania)
# ═══════════════════════════════════════════════════════════════════════════
#
# This is NOT a single attested language but a RECONSTRUCTION of the
# spoken Latin of Hispania (~3rd–7th c. CE), the transitional stage
# between Classical Latin and Proto-Ibero-Romance.
#
# Evidence: inscriptional errors, grammarian complaints, early Romance
# outcomes, loanwords into Basque and Arabic, comparative Romance.
#
# KEY SOUND CHANGES (Hispania-specific or general Vulgar Latin):
#
# 1. VOWEL SYSTEM RESTRUCTURING:
#    Classical 10-vowel (5 long + 5 short) → 7-vowel by quality:
#    ĭ/ē → /e/,  ĕ → /ɛ/,  ŭ/ō → /o/,  ŏ → /ɔ/
#    (The Romance "vowel collapse" — shared across Western Romance)
#
# 2. CONSONANT LENITION (Western Romance, incl. Hispania):
#    Intervocalic voiceless stops → voiced → fricatives:
#    -p- → -b- → -β-;  -t- → -d- → -ð-;  -k- → -g- → -ɣ-
#
# 3. PALATALISATION:
#    /k/ before /e,i/ → [tʃ] → eventual /θ/ or /s/ in Ibero-Romance
#    /g/ before /e,i/ → [dʒ] → eventual /x/ or ∅
#    -li-, -cl-, -gl- → [ʎ]
#    -ni-, -gn- → [ɲ]
#
# 4. /f/ → /h/ (HISPANIC SPECIFIC):
#    Latin F- → [h] in Castilian (but NOT in Portuguese, Catalan, etc.)
#    filium → Sp. hijo, Pt. filho (retains [f])
#    This is either substrate (Basque lacks /f/) or internal innovation.
#
# 5. LOSS OF FINAL -M, -T:
#    Already underway in Classical period (Appendix Probi evidence)
#
# 6. DIPHTHONGISATION:
#    /ɛ/ → [je], /ɔ/ → [we] (in stressed open syllables — Castilian)
#    Not in Portuguese, Catalan (they keep [ɛ, ɔ])

GRAPHEMES_VL_HISP = {
    # --- Vowels (7-vowel system, post-merger) ---
    "a": ["a"],
    "e": ["e"],  # < ĭ, ē
    "ɛ": ["ɛ"],  # < ĕ (open e; diphthongises in Castilian)
    "i": ["i"],  # < ī
    "o": ["o"],  # < ŭ, ō
    "ɔ": ["ɔ"],  # < ŏ (open o; diphthongises in Castilian)
    "u": ["u"],  # < ū

    # --- Consonants (showing lenition stages) ---
    "p": ["p"],
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "c": ["k", "tʃ"],  # [k] before a/o/u; [tʃ] before e/i (palatalised)
    "g": ["ɡ", "dʒ"],  # [ɡ] before a/o/u; [dʒ] before e/i
    "f": ["f", "h"],  # [f] > [h] (Hispanic specific, variable)
    "s": ["s"],
    "v": ["β"],  # merged with /b/
    "j": ["dʒ", "ʒ"],  # < Latin I before vowel
    "h": ["∅", "h"],  # silent in most positions

    # --- Nasals ---
    "m": ["m"],
    "n": ["n"],
    "ñ": ["ɲ"],  # < -ni-, -gn- palatalisation

    # --- Liquids ---
    "l": ["l"],
    "r": ["ɾ"],
    "rr": ["r"],
    "ll": ["ʎ"],  # < -li-, -cl-, -gl- palatalisation

    # --- Palatalised digraphs (emerging) ---
    "ch": ["tʃ"],  # < Latin -ct- (factum > hecho)
    "gn": ["ɲ"],
    "li": ["ʎ"],

    # --- Diphthongs (from VL open-syllable diphthongisation) ---
    "ie": ["je"],  # < /ɛ/ in Castilian area
    "ue": ["we"],  # < /ɔ/ in Castilian area
    "ai": ["aj"],
    "au": ["aw"],
    "ei": ["ej"],
    "ou": ["ow"],
}

ALLOPHONES_VL_HISP = {
    "p": ["p"],
    "b": ["b", "β"],  # lenition: [β] intervocalic
    "t": ["t"],
    "d": ["d", "ð"],  # lenition: [ð] intervocalic
    "k": ["k"],
    "ɡ": ["ɡ", "ɣ"],  # lenition: [ɣ] intervocalic
    "tʃ": ["tʃ"],
    "dʒ": ["dʒ", "ʒ"],
    "f": ["f", "h"],
    "s": ["s", "z"],  # [z] before voiced C
    "m": ["m"],
    "n": ["n", "ŋ"],
    "ɲ": ["ɲ"],
    "l": ["l"],
    "ʎ": ["ʎ"],
    "ɾ": ["ɾ"],
    "r": ["r"],
    "a": ["a"], "e": ["e"], "ɛ": ["ɛ"], "i": ["i"],
    "o": ["o"], "ɔ": ["ɔ"], "u": ["u"],
}

# ═══════════════════════════════════════════════════════════════════════════
# MOZARABIC (mxi)
# ═══════════════════════════════════════════════════════════════════════════
#
# Classification: Romance > Western > Ibero-Romance
# The Romance variety spoken by Christians (and some Muslims/Jews)
# in Al-Andalus (Muslim-ruled Iberia), ~8th–13th century.
#
# Attestation:
#   - Kharjas (خرجة): final stanzas of Arabic/Hebrew muwashshaḥ poems,
#     written in Arabic or Hebrew script but in Romance language
#     (~40 kharjas, 11th–12th c.)
#   - Ibn Quzmān's zajal fragments
#   - Botanical/medical terminology (in Arabic translations)
#   - Pedro de Alcalá (1505) — late Granadan Arabic with Romance elements
#   - Place names, loanwords in Andalusi Arabic
#
# PHONOLOGICAL FEATURES (Galmés de Fuentes 1983):
#   - ARCHAIC: preserves Latin features lost in Castilian:
#     * No diphthongisation of /ɛ/ and /ɔ/ (night = noite, not noche)
#     * Latin F- preserved as [f] (not [h] like Castilian)
#     * Latin -CT- → [jt] (not [tʃ] like Castilian)
#     * Initial PL-, CL-, FL- preserved (not → [ʎ] like Castilian)
#   - INNOVATIVE in other ways:
#     * Heavy Arabic phonological influence on later Mozarabic
#     * Possible pharyngealisation in some speakers
#     * Arabic loanwords abundant
#
# Mozarabic is written in ARABIC SCRIPT, so the phonological
# interpretation depends on understanding Arabic orthographic conventions
# applied to Romance sounds.  There is inherent uncertainty.

GRAPHEMES_MXI = {
    # --- Vowels (7-vowel Romance system, archaic) ---
    "a": ["a"],
    "e": ["e"],
    "ɛ": ["ɛ"],  # NOT diphthongised (unlike Castilian)
    "i": ["i"],
    "o": ["o"],
    "ɔ": ["ɔ"],  # NOT diphthongised (unlike Castilian)
    "u": ["u"],

    # --- Consonants ---
    "b": ["b"],
    "p": ["p"],
    "t": ["t"],
    "d": ["d"],
    "c": ["k", "tʃ"],  # [tʃ] before front vowels (palatalised)
    "g": ["ɡ", "dʒ"],
    "f": ["f"],  # PRESERVED (not > [h] — archaic feature)
    "s": ["s"],
    "z": ["z"],  # voiced sibilant (preserved longer than Castilian)
    "š": ["ʃ"],  # from palatalisation
    "ž": ["ʒ"],  # voiced postalveolar (from palatalisations)
    "v": ["v"],  # /v/ possibly preserved (not merged with /b/)

    # --- Palatalised consonants ---
    "ch": ["tʃ"],
    "ñ": ["ɲ"],
    "ll": ["ʎ"],
    "yt": ["jt"],  # < Latin -CT- (noctis > noyte, not noche)
    "yš": ["jʃ"],  # variant of -CT- outcome

    # --- Clusters (preserved, unlike Castilian) ---
    "pl": ["pl"],  # preserved (Castilian → [ʎ])
    "cl": ["kl"],  # preserved (Castilian → [ʎ])
    "fl": ["fl"],  # preserved (Castilian → [ʎ])

    # --- Nasals ---
    "m": ["m"],
    "n": ["n"],

    # --- Liquids ---
    "l": ["l"],
    "r": ["ɾ"],
    "rr": ["r"],

    # --- Diphthongs (limited, archaic) ---
    "ai": ["aj"],
    "ei": ["ej"],
    "au": ["aw"],
    "ou": ["ow"],
}

ALLOPHONES_MXI = {
    "p": ["p"],
    "b": ["b", "β"],
    "t": ["t"],
    "d": ["d", "ð"],
    "k": ["k"],
    "ɡ": ["ɡ", "ɣ"],
    "f": ["f"],
    "v": ["v"],
    "tʃ": ["tʃ"],
    "dʒ": ["dʒ", "ʒ"],
    "s": ["s"],
    "z": ["z"],
    "ʃ": ["ʃ"],
    "ʒ": ["ʒ"],
    "ɲ": ["ɲ"],
    "ʎ": ["ʎ"],
    "m": ["m"],
    "n": ["n", "ŋ"],
    "l": ["l"],
    "ɾ": ["ɾ"],
    "r": ["r"],
    "a": ["a"], "e": ["e"], "ɛ": ["ɛ"], "i": ["i"],
    "o": ["o"], "ɔ": ["ɔ"], "u": ["u"],
}

# ═══════════════════════════════════════════════════════════════════════════
# ANDALUSI ARABIC (xaa)
# ═══════════════════════════════════════════════════════════════════════════
#
# Classification: Semitic > Arabic > Western Arabic (Maghrebi type)
# The Arabic dialect spoken in Al-Andalus (~8th–17th c. CE)
#
# Attestation: EXCELLENT —
#   - Ibn Quzmān's dīwān (12th c.) — colloquial Andalusi
#   - Kharjas (some in Arabic colloquial)
#   - Agricultural treatises (Ibn al-ʿAwwām)
#   - Vocabulista in Arabico (13th c.)
#   - Pedro de Alcalá (1505) — invaluable late source (Latin transcription!)
#   - Legal documents, letters, hisba manuals
#
# PHONOLOGICAL FEATURES (Corriente 2013):
#   - IMĀLA: raising of /aː/ → [eː] (shared with some Maghrebi)
#   - MERGER of emphatics: /ḍ/ and /ḏ̣/ merge (interdental emphatic lost)
#   - LOSS of interdentals: /θ/ → /s/ or /t/, /ð/ → /d/ (like Maghrebi)
#   - Preservation of /p/ (from Romance loans; not in Classical Arabic)
#   - Final short vowel loss (apocopation)
#   - Partial retention of case vowels in early period
#   - Heavy Romance substrate influence (phonological and lexical)
#
# THIS IS THE BEST-DOCUMENTED PRE-MODERN IBERIAN LANGUAGE after Latin,
# thanks to Corriente's extensive reconstruction from multiple sources.

GRAPHEMES_XAA = {
    # --- Consonants (Arabic inventory, with Andalusi modifications) ---
    "ʾ": ["ʔ"],  # hamza (weakening in Andalusi)
    "b": ["b"],
    "t": ["t"],
    "ṯ": ["θ", "t"],  # < CA /θ/; merges with /t/ in late Andalusi
    "j": ["dʒ"],  # /ɡ/ in some analyses (like Maghrebi)
    "ḥ": ["ħ"],
    "ḫ": ["x"],  # ḫāʾ
    "d": ["d"],
    "ḏ": ["ð", "d"],  # merges with /d/ in late Andalusi
    "r": ["r"],
    "z": ["z"],
    "s": ["s"],
    "š": ["ʃ"],
    "ṣ": ["sˤ"],
    "ḍ": ["dˤ"],
    "ṭ": ["tˤ"],
    "ẓ": ["ðˤ", "dˤ"],  # merges with /ḍ/ in Andalusi
    "ʿ": ["ʕ"],
    "ġ": ["ɣ"],
    "f": ["f"],
    "q": ["q"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "h": ["h"],
    "w": ["w"],
    "y": ["j"],

    # --- ROMANCE ADDITION: /p/ ---
    # Classical Arabic has no /p/; Andalusi developed it from Romance loans
    "p": ["p"],

    # --- Vowels ---
    # Short (3 in Classical; modified in Andalusi)
    "a": ["a", "e"],  # imāla: /a/ → [e] in many contexts
    "i": ["i"],
    "u": ["u"],

    # Long
    "ā": ["aː", "eː"],  # IMĀLA: /aː/ → [eː] — distinctive Andalusi
    "ī": ["iː"],
    "ū": ["uː"],

    # Diphthongs
    "ay": ["aj"],
    "aw": ["aw"],

    # --- Digraphs/emphatic combinations ---
    "ll": ["lː"],
    "mm": ["mː"],
    "nn": ["nː"],
    "rr": ["rː"],
    "ss": ["sː"],
    "šš": ["ʃː"],
}

ALLOPHONES_XAA = {
    # Stops
    "ʔ": ["ʔ", "∅"],  # weakened in many positions
    "b": ["b", "β"],  # spirantisation (Arabic + Romance influence)
    "t": ["t"],
    "d": ["d", "ð"],
    "k": ["k"],
    "ɡ": ["ɡ", "ɣ"],
    "q": ["q", "ʔ"],  # /q/ → [ʔ] in some late Andalusi
    "p": ["p"],  # from Romance

    # Emphatics
    "tˤ": ["tˤ"],
    "dˤ": ["dˤ"],
    "sˤ": ["sˤ"],
    "ðˤ": ["ðˤ", "dˤ"],  # merger

    # Fricatives
    "f": ["f"],
    "θ": ["θ", "t", "s"],  # merging with /t/ or /s/ in late Andalusi
    "ð": ["ð", "d"],
    "s": ["s"],
    "z": ["z"],
    "ʃ": ["ʃ"],
    "x": ["x"],
    "ɣ": ["ɣ"],
    "ħ": ["ħ"],
    "ʕ": ["ʕ"],
    "h": ["h", "∅"],

    # Affricates
    "dʒ": ["dʒ", "ɡ", "ʒ"],  # variable: [dʒ] early; [ɡ] Maghrebi-like

    # Nasals
    "m": ["m"],
    "n": ["n", "ŋ"],

    # Liquids
    "l": ["l"],
    "r": ["r", "ɾ"],

    # Glides
    "w": ["w"],
    "j": ["j"],

    # Vowels
    "a": ["a", "e"],  # imāla
    "i": ["i"], "u": ["u"],
    "aː": ["aː", "eː"],  # imāla
    "iː": ["iː"], "uː": ["uː"],
    "eː": ["eː"],  # from imāla

    # Geminates
    "lː": ["lː"], "mː": ["mː"], "nː": ["nː"], "rː": ["rː"],
    "sː": ["sː"], "ʃː": ["ʃː"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SPECS
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "la-x-hispania": LanguageSpec(
        code="la-x-hispania", name="Hispanic Vulgar Latin",
        family="Italic", script="Latin",
        graphemes=GRAPHEMES_VL_HISP, allophones=ALLOPHONES_VL_HISP,
        parent="la",
        notes=(
            "Hispanic Vulgar Latin (~3rd–7th c. CE). Reconstructed spoken "
            "Latin of Roman Hispania, transitional to Ibero-Romance. Key "
            "changes from Classical Latin: (1) 10-vowel → 7-vowel merger "
            "(by quality not quantity). (2) Intervocalic lenition (-p- → "
            "-b- → -β-). (3) Palatalisation (CE/CI → [tʃ], GE/GI → [dʒ]). "
            "(4) F- → [h] (Hispanic specific; Basque substrate?). "
            "(5) -CT- → [jt] (→ [tʃ] in Castilian). (6) Diphthongisation "
            "of /ɛ/ → [je], /ɔ/ → [we] in Castilian area. The ancestor "
            "of ALL Ibero-Romance languages."
        ),
    ),
    "mxi": LanguageSpec(
        code="mxi", name="Mozarabic",
        family="Romance", script="Latin",
        graphemes=GRAPHEMES_MXI, allophones=ALLOPHONES_MXI,
        parent="la",
        notes=(
            "Mozarabic (8th–13th c. CE). Romance language of Al-Andalus, "
            "spoken by Christians, some Jews/Muslims under Islamic rule. "
            "Attested in kharjas (Arabic/Hebrew-script Romance stanzas) "
            "and botanical/medical texts. ARCHAIC features: no ĕ/ŏ "
            "diphthongisation (noite not noche), F- preserved as [f] "
            "(not [h]), Latin PL-/CL-/FL- preserved, -CT- → [jt] not [tʃ]. "
            "Extinct by ~13th century, replaced by advancing Castilian, "
            "Portuguese, and Catalan. Written in Arabic/Hebrew scripts."
        ),
    ),
    "xaa": LanguageSpec(
        code="xaa", name="Andalusi Arabic",
        family="Semitic", script="Latin",
        graphemes=GRAPHEMES_XAA, allophones=ALLOPHONES_XAA,
        parent="ar",
        notes=(
            "Andalusi Arabic (8th–17th c. CE). Western Arabic dialect of "
            "Al-Andalus. Best-documented through Ibn Quzmān, kharjas, Pedro "
            "de Alcalá (1505), Vocabulista. Per Corriente (2013): "
            "(1) IMĀLA: /aː/ → [eː] (diagnostic feature). (2) Interdental "
            "merger: /θ/ → /t/ or /s/. (3) Emphatic merger: /ḍ/ and /ḏ̣/ "
            "conflate. (4) Romance-origin /p/ added. (5) Heavy Romance "
            "substrate/adstrate. ~4000 Andalusi Arabic loanwords survive "
            "in Ibero-Romance (alcalde, algodón, azúcar, alfombra...)."
        ),
    ),
}
