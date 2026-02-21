"""Southern Italo-Romance languages — Neapolitan, Sicilian, Corsican.

These descend from Italo-Romance Vulgar Latin but diverge significantly
from standard Italian (which is based on Tuscan). They are often treated
as separate languages rather than Italian dialects.

Sources:
Neapolitan:
- Ledgeway, A. (2009). *Grammatica diacronica del napoletano*. Niemeyer.
- De Blasi, N. & Imperatore, L. (2000). *Il napoletano parlato e scritto*.
- Iannace, G. (2001). *La lingua napoletana*. AIHA.
- Radtke, E. (1997). *I dialetti della Campania*. Il Calamo.

Sicilian:
- Ferrante, C. (2020). *A Grammar of Sicilian*. Lincom Europa.
- Piccitto, G. et al. (1977–2002). *Vocabolario siciliano*. 5 vols.
- Rohlfs, G. (1966). *Grammatica storica della lingua italiana*. Einaudi.
- Ferrante, C. (2016). 'Sicilian.' In Ledgeway & Maiden (eds.),
  *The Oxford Guide to the Romance Languages*. OUP.

Corsican:
- Ferracci, L. (2007). *Grammaire active du corse*. Albiana.
- Marchetti, P. (1989). *Le corse sans peine*. Assimil.
- Comiti, J.-M. (2005). *La langue corse entre chien et loup*. L'Harmattan.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# NEAPOLITAN (nap)
# ═══════════════════════════════════════════════════════════════════════════
#
# Southern Italo-Romance of Campania, plus related varieties through
# much of southern mainland Italy (Abruzzi, Molise, Puglia, Basilicata,
# N. Calabria). ~5.7 million speakers.
#
# KEY FEATURES:
# 1. METAPHONY (vowel harmony): stressed mid vowels raised when final
#    vowel is /i/ or /u/: buono→buoni, but bona→bone
# 2. VOWEL REDUCTION: Unstressed final vowels → [ə] (schwa)
# 3. Voiced/voiceless gemination patterns differ from standard Italian
# 4. Richer vowel system than standard Italian (including /ə/)
# 5. Retroflexion of -LL- → [ɖː] in some areas (shared with Sicilian)

GRAPHEMES_NAP = {
    # --- Vowels ---
    "a": ["a"],
    "e": ["e", "ɛ"],
    "ë": ["ə"],  # schwa (common in unstressed positions)
    "i": ["i"],
    "o": ["o", "ɔ"],
    "u": ["u"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "tʃ"],  # [tʃ] before e,i
    "ch": ["k"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "dʒ"],
    "gh": ["ɡ"],
    "gn": ["ɲ"],
    "gl": ["ʎ"],
    "h": ["∅"],
    "j": ["j"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "qu": ["kw"],
    "r": ["r"],
    "s": ["s", "z"],
    "sc": ["ʃ"],
    "t": ["t"],
    "v": ["v"],
    "z": ["ts", "dz"],

    # --- Geminates ---
    "bb": ["bː"], "cc": ["kː", "tːʃ"], "dd": ["dː"],
    "ff": ["fː"], "gg": ["ɡː", "dːʒ"], "ll": ["lː"],
    "mm": ["mː"], "nn": ["nː"], "pp": ["pː"],
    "rr": ["rː"], "ss": ["sː"], "tt": ["tː"],
    "zz": ["tːs", "dːz"],
}

ALLOPHONES_NAP = {
    "p": ["p"], "b": ["b", "β"],
    "t": ["t"], "d": ["d", "ð"],
    "k": ["k"], "ɡ": ["ɡ", "ɣ"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ"],
    "ts": ["ts"], "dz": ["dz"],
    "f": ["f"], "v": ["v"],
    "s": ["s", "ʃ"], "z": ["z", "ʒ"],
    "ʃ": ["ʃ"],
    "m": ["m"], "n": ["n", "ŋ", "ɱ"], "ɲ": ["ɲ"],
    "l": ["l"], "ʎ": ["ʎ"],
    "r": ["r", "ɾ"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "ə": ["ə"],
    "e": ["e"], "ɛ": ["ɛ"], "i": ["i"],
    "o": ["o"], "ɔ": ["ɔ"], "u": ["u"],
    # Geminates
    "bː": ["bː"], "dː": ["dː"], "ɡː": ["ɡː"],
    "pː": ["pː"], "tː": ["tː"], "kː": ["kː"],
    "fː": ["fː"], "sː": ["sː"],
    "lː": ["lː"], "mː": ["mː"], "nː": ["nː"], "rː": ["rː"],
    "tːʃ": ["tːʃ"], "dːʒ": ["dːʒ"],
    "tːs": ["tːs"], "dːz": ["dːz"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SICILIAN (scn)
# ═══════════════════════════════════════════════════════════════════════════
#
# Southern Italo-Romance of Sicily and southern Calabria.
# ~4.7 million speakers.
#
# KEY FEATURES:
# 1. FIVE-VOWEL SYSTEM (like Sardinian!): /a, ɛ, i, ɔ, u/
#    Latin ĭ/ē → /i/ (merged), ŭ/ō → /u/ (merged)
#    This is more archaic than standard Italian's 7-vowel system.
# 2. RETROFLEX consonants: -LL- → [ɖː], -TR- → [ʈɽ]
#    (substrate influence from pre-Roman Sicels, or Greek substrate)
# 3. DD → [ɖː] (retroflex geminate, very distinctive)
# 4. Final unstressed vowels strongly reduced or deleted
# 5. B → [v] or [β] initially (Latin /b/ → /v/ innovation)

GRAPHEMES_SCN = {
    # --- Vowels (5-vowel system) ---
    "a": ["a"],
    "e": ["ɛ"],  # always open (no /e/ vs /ɛ/ contrast)
    "i": ["i"],  # < ĭ, ē, ī (all merged)
    "o": ["ɔ"],  # always open (no /o/ vs /ɔ/ contrast)
    "u": ["u"],  # < ŭ, ō, ū (all merged)

    # --- Consonants ---
    "b": ["b", "v"],  # /v/ or /b/ initially (varies)
    "c": ["k", "tʃ"],
    "ch": ["k"],
    "d": ["d"],
    "dd": ["ɖː"],  # retroflex geminate! (< Latin -LL-)
    "f": ["f"],
    "g": ["ɡ", "dʒ"],
    "gh": ["ɡ"],
    "gn": ["ɲ"],
    "gl": ["ʎ"],
    "h": ["∅"],
    "j": ["j"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "qu": ["kw"],
    "r": ["r", "ɽ"],  # retroflex tap in some positions
    "rr": ["rː"],
    "s": ["s", "z"],
    "sc": ["ʃ"],
    "str": ["ʂʈɽ"],  # retroflex cluster
    "t": ["t"],
    "tr": ["ʈɽ"],  # retroflex cluster
    "v": ["v"],
    "z": ["ts", "dz"],

    # --- Geminates ---
    "bb": ["bː"], "cc": ["kː", "tːʃ"],
    "ff": ["fː"], "gg": ["ɡː", "dːʒ"],
    "ll": ["ɖː"],  # -LL- → retroflex! (THE Sicilian feature)
    "mm": ["mː"], "nn": ["nː"], "pp": ["pː"],
    "ss": ["sː"], "tt": ["tː"], "zz": ["tːs", "dːz"],
}

ALLOPHONES_SCN = {
    "p": ["p"], "b": ["b", "v", "β"],
    "t": ["t"], "d": ["d"],
    "k": ["k"], "ɡ": ["ɡ"],
    "ʈ": ["ʈ"], "ɖ": ["ɖ"], "ɖː": ["ɖː"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ"],
    "ts": ["ts"], "dz": ["dz"],
    "f": ["f"], "v": ["v"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʂ": ["ʂ"],
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "ʎ": ["ʎ"],
    "r": ["r", "ɾ", "ɽ"],
    "rː": ["rː"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "ɛ": ["ɛ"], "i": ["i"], "ɔ": ["ɔ"], "u": ["u"],
    # Geminates
    "bː": ["bː"], "pː": ["pː"], "tː": ["tː"], "dː": ["dː"],
    "kː": ["kː"], "ɡː": ["ɡː"],
    "fː": ["fː"], "sː": ["sː"],
    "lː": ["lː"], "mː": ["mː"], "nː": ["nː"],
    "tːʃ": ["tːʃ"], "dːʒ": ["dːʒ"],
    "tːs": ["tːs"], "dːz": ["dːz"],
}

# ═══════════════════════════════════════════════════════════════════════════
# CORSICAN (co)
# ═══════════════════════════════════════════════════════════════════════════
#
# Italo-Romance of Corsica. Close to Tuscan Italian but with significant
# innovations and archaic retentions. ~100,000 speakers.
#
# KEY FEATURES:
# 1. Very close to medieval Tuscan (before Tuscan innovations)
# 2. Preservation of Latin -LL- as [lː] (not retroflex like Sardinian)
# 3. Some vowel distinctions lost (merger of /e/ and /ɛ/ in some areas)
# 4. French superstrate (official language of Corsica since 1769)

GRAPHEMES_CO = {
    # --- Vowels ---
    "a": ["a"],
    "e": ["e", "ɛ"],
    "i": ["i"],
    "o": ["o", "ɔ"],
    "u": ["u"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "tʃ"],
    "ch": ["k"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "dʒ"],
    "gh": ["ɡ"],
    "gn": ["ɲ"],
    "gl": ["ʎ"],
    "h": ["∅"],
    "j": ["j"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "qu": ["kw"],
    "r": ["r"],
    "s": ["s", "z"],
    "sc": ["ʃ"],
    "t": ["t"],
    "v": ["v"],
    "z": ["ts", "dz"],

    # --- Geminates ---
    "bb": ["bː"], "cc": ["kː", "tːʃ"], "dd": ["dː"],
    "ff": ["fː"], "gg": ["ɡː", "dːʒ"], "ll": ["lː"],
    "mm": ["mː"], "nn": ["nː"], "pp": ["pː"],
    "rr": ["rː"], "ss": ["sː"], "tt": ["tː"],
    "zz": ["tːs"],
}

ALLOPHONES_CO = {
    "p": ["p"], "b": ["b", "β"],
    "t": ["t"], "d": ["d", "ð"],
    "k": ["k", "h"],  # [h] in gorgia (Tuscan heritage)
    "ɡ": ["ɡ", "ɣ"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ"],
    "ts": ["ts"], "dz": ["dz"],
    "f": ["f"], "v": ["v"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"],
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "ʎ": ["ʎ"],
    "r": ["r", "ɾ"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "e": ["e"], "ɛ": ["ɛ"],
    "i": ["i"], "o": ["o"], "ɔ": ["ɔ"], "u": ["u"],
    # Geminates
    "bː": ["bː"], "dː": ["dː"], "ɡː": ["ɡː"],
    "pː": ["pː"], "tː": ["tː"], "kː": ["kː"],
    "fː": ["fː"], "sː": ["sː"],
    "lː": ["lː"], "mː": ["mː"], "nː": ["nː"], "rː": ["rː"],
    "tːʃ": ["tːʃ"], "dːʒ": ["dːʒ"], "tːs": ["tːs"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SPECS
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "nap": LanguageSpec(
        code="nap",
        name="Neapolitan",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_NAP,
        allophones=ALLOPHONES_NAP,
        parent="la-x-italia",
        ancestors=(
            Ancestor("la-x-italia", P, 0.78,
                     "Italo-Romance parent."),
            Ancestor("grc", SUB, 0.10,
                     "Magna Graecia Greek substrate: Southern Italy "
                     "was heavily Hellenised. Possible influence on "
                     "consonant system and prosody."),
            Ancestor("got", SUP, 0.04,
                     "Ostrogothic/Lombardic superstrate."),
            Ancestor("fr-FR", SUP, 0.05,
                     "Norman French superstrate (11th–13th c.): "
                     "Norman conquest of S. Italy and Sicily. "
                     "Lexical influence, some structural."),
        ),
        notes=(
            "Neapolitan. Southern Italo-Romance of Campania and "
            "broader S. mainland Italy. ~5.7 million speakers. "
            "Key features: (1) Metaphony (vowel harmony triggered "
            "by final vowel). (2) Unstressed vowels → [ə]. "
            "(3) Rich gemination. (4) Retroflex -DD- [ɖː] in some "
            "areas. Literary tradition from 16th c. "
            "(Ledgeway 2009, De Blasi & Imperatore 2000)."
        ),
    ),
    "scn": LanguageSpec(
        code="scn",
        name="Sicilian",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_SCN,
        allophones=ALLOPHONES_SCN,
        parent="la-x-italia",
        ancestors=(
            Ancestor("la-x-italia", P, 0.72,
                     "Italo-Romance parent."),
            Ancestor("grc", SUB, 0.12,
                     "Greek substrate: Sicily was a Greek colony for "
                     "800+ years (Magna Graecia). Strong influence "
                     "on retroflexion, possibly on 5-vowel system."),
            Ancestor("xaa", AD, 0.06,
                     "Arabic adstrate (9th–11th c.): Emirate of "
                     "Sicily. Lexical influence (~500 words), some "
                     "phonological influence."),
            Ancestor("fr-FR", SUP, 0.05,
                     "Norman French superstrate (11th–13th c.): "
                     "Norman conquest. Administrative/legal lexicon."),
        ),
        notes=(
            "Sicilian. Southern Italo-Romance of Sicily and S. "
            "Calabria. ~4.7 million speakers. Key features: "
            "(1) 5-VOWEL system /a ɛ i ɔ u/ (like Sardinian, more "
            "archaic than Italian's 7). (2) Retroflex consonants: "
            "-LL- → [ɖː] (beddu 'beautiful'), TR → [ʈɽ]. "
            "(3) Final vowel reduction. Literary tradition from "
            "13th c. Sicilian School (Ferrante 2020)."
        ),
    ),
    "co": LanguageSpec(
        code="co",
        name="Corsican",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_CO,
        allophones=ALLOPHONES_CO,
        parent="la-x-italia",
        ancestors=(
            Ancestor("la-x-italia", P, 0.80,
                     "Italo-Romance parent: closest to medieval "
                     "Tuscan."),
            Ancestor("fr-FR", SUP, 0.12,
                     "French superstrate (from 1769): official "
                     "language, educational system, media. Heavy "
                     "lexical influence increasing over time."),
        ),
        notes=(
            "Corsican. Italo-Romance of Corsica, closely related "
            "to Tuscan Italian but with its own innovations and "
            "archaic retentions. ~100,000 speakers (declining "
            "rapidly under French pressure). Key features: "
            "(1) Close to medieval Tuscan. (2) Gorgia (aspiration "
            "of voiceless stops) in some areas (Tuscan heritage). "
            "(3) French superstrate increasing since 1769 "
            "(Ferracci 2007, Marchetti 1989)."
        ),
    ),
}
