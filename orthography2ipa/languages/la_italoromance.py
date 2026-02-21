"""Italo-Romance Vulgar Latin (la-x-italia) — intermediate ancestor.

The spoken Latin of the Italian peninsula (~3rd–7th c. CE),
ancestral to Tuscan/Italian, Neapolitan, Sicilian, Corsican, and
(debatably) Friulian.

Sardinian is explicitly EXCLUDED: it split from Common Latin before
the Italo-Romance innovations took hold (Lausberg 1971, Maiden 1995).

Sources:
- Maiden, M. (1995). *A Linguistic History of Italian*. Longman.
- Lausberg, H. (1971). *Romanische Sprachwissenschaft*. De Gruyter.
- Rohlfs, G. (1966–1969). *Grammatica storica della lingua italiana*.
  Einaudi. 3 vols.
- Tekavčić, P. (1972). *Grammatica storica dell'italiano*. Il Mulino.
- Loporcaro, M. (2011). 'Phonological processes.' In Maiden et al.
  (eds.), *The Cambridge History of the Romance Languages*, vol. 1. CUP.
- Ledgeway, A. & Maiden, M. (eds.) (2016). *The Oxford Guide to the
  Romance Languages*. OUP.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# ITALO-ROMANCE VULGAR LATIN (la-x-italia)
# ═══════════════════════════════════════════════════════════════════════════
#
# The spoken Latin of the Italian peninsula from late antiquity through
# the early medieval period. Transitional between Classical Latin and
# the Italo-Romance languages.
#
# KEY SOUND CHANGES (Italo-Romance innovations):
#
# 1. VOWEL SYSTEM:
#    Same 10→7 quality-based merger as Western Romance:
#    ĭ/ē → /e/, ĕ → /ɛ/, ŭ/ō → /o/, ŏ → /ɔ/
#    BUT: /u/ is PRESERVED (no fronting to /y/ like Gallo-Romance)
#    Latin MŪRUM → Italo-Rom [muːro] → It. muro (vs Fr. mur [myʁ])
#
# 2. GEMINATION:
#    Latin geminates are PRESERVED (unlike Gallo- and Ibero-Romance
#    which simplify them):
#    ANNUM → It. anno [ˈanːo] (vs Fr. an, Sp. año)
#    BELLUM → It. bello [ˈbɛlːo] (vs Fr. beau, Sp. bello)
#    This is THE hallmark of Italo-Romance.
#
# 3. LENITION (WEAKER than Western Romance):
#    Intervocalic voiceless stops undergo VOICING but less often full
#    fricativisation or deletion:
#    -p- → -b- (not → -v- → ∅ as in French)
#    -t- → -d- (not → ∅)
#    -k- → -ɡ- (not → ∅)
#    Central/Northern Italian: some lenition (la[ɡ]o < LACUM)
#    Southern Italian: less lenition overall
#
# 4. PALATALISATION:
#    /k/ before e,i → [tʃ] (like in Ibero-Romance)
#    CENTUM → [tʃento] → It. cento [ˈtʃɛnto]
#    /ɡ/ before e,i → [dʒ]
#    GELU → [dʒɛːlo] → It. gelo [ˈdʒɛːlo]
#
# 5. F- PRESERVED:
#    Like Gallo-Romance and Portuguese, F- is kept:
#    FILIUM → It. figlio (vs Sp. hijo with f→h)
#
# 6. GORGIA TOSCANA (regional):
#    Voiceless stops → fricatives intervocalically in Tuscany:
#    /p/ → [ɸ], /t/ → [θ], /k/ → [h]
#    This is a POST-Latin innovation specific to Tuscany.
#
# 7. RADDOPPIAMENTO SINTATTICO:
#    Gemination at word boundaries after certain function words.
#    A unique Italo-Romance prosodic feature.
#
# 8. -S LOSS:
#    Final -s is lost (unlike Gallo-Romance and Ibero-Romance which keep it):
#    Plural formed with -i/-e (vowel alternation) not -s
#    This distinguishes Italo- from Western Romance fundamentally.

GRAPHEMES = {
    # --- Vowels (7-vowel system, /u/ preserved) ---
    "a": ["a"],
    "e": ["e"],  # < ĭ, ē
    "ɛ": ["ɛ"],  # < ĕ (open e)
    "i": ["i"],  # < ī
    "o": ["o"],  # < ŭ, ō
    "ɔ": ["ɔ"],  # < ŏ (open o)
    "u": ["u"],  # PRESERVED (not fronted to /y/)

    # --- Consonants ---
    "p": ["p"],
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "c": ["k", "tʃ"],  # [tʃ] before e,i
    "g": ["ɡ", "dʒ"],  # [dʒ] before e,i
    "f": ["f"],  # PRESERVED
    "v": ["v"],
    "s": ["s", "z"],  # voiced between vowels in some areas
    "h": ["∅"],  # silent (lost in late Latin)

    # --- Palatals ---
    "gn": ["ɲ"],  # < -gn-, -ni-
    "gl-ES": ["ʎ"],  # < -li-, -gl- before i
    "sc": ["ʃ"],  # < SCI, SCE

    # --- Nasals ---
    "m": ["m"],
    "n": ["n"],

    # --- Liquids ---
    "l": ["l"],
    "r": ["ɾ"],
    "rr": ["r"],  # geminate trill preserved

    # --- Geminates (PRESERVED — hallmark of Italo-Romance) ---
    "pp": ["pː"],
    "bb": ["bː"],
    "tt": ["tː"],
    "dd": ["dː"],
    "cc": ["kː", "tːʃ"],
    "gg": ["ɡː", "dːʒ"],
    "ff": ["fː"],
    "ss": ["sː"],
    "ll": ["lː"],
    "mm": ["mː"],
    "nn": ["nː"],

    # --- Affricates ---
    "z": ["ts", "dz"],

    # --- Diphthongs ---
    "ie": ["je"],  # < /ɛ/ diphthongisation
    "uo": ["wo"],  # < /ɔ/ diphthongisation
    "ai": ["aj"],
    "au": ["aw"],
    "ei": ["ej"],
    "oi": ["oj"],
}

ALLOPHONES = {
    "p": ["p", "ɸ"],  # [ɸ] in gorgia toscana area
    "b": ["b", "β"],
    "t": ["t", "θ"],  # [θ] in gorgia toscana area
    "d": ["d", "ð"],
    "k": ["k", "h"],  # [h] in gorgia toscana area
    "ɡ": ["ɡ", "ɣ"],
    "tʃ": ["tʃ"],
    "dʒ": ["dʒ"],
    "ts": ["ts"],
    "dz": ["dz"],
    "f": ["f"],
    "v": ["v"],
    "s": ["s", "z"],
    "ʃ": ["ʃ"],
    "ɲ": ["ɲ"],
    "ʎ": ["ʎ"],
    "m": ["m"],
    "n": ["n", "ŋ", "ɱ"],
    "l": ["l"],
    "ɾ": ["ɾ"],
    "r": ["r"],
    "j": ["j"],
    "w": ["w"],
    # Geminates
    "pː": ["pː"], "bː": ["bː"], "tː": ["tː"], "dː": ["dː"],
    "kː": ["kː"], "ɡː": ["ɡː"], "fː": ["fː"], "sː": ["sː"],
    "lː": ["lː"], "mː": ["mː"], "nː": ["nː"],
    "tːʃ": ["tːʃ"], "dːʒ": ["dːʒ"],
    # Vowels
    "a": ["a"], "e": ["e"], "ɛ": ["ɛ"], "i": ["i"],
    "o": ["o"], "ɔ": ["ɔ"], "u": ["u"],
}

SPECS = {
    "la-x-italia": LanguageSpec(
        code="la-x-italia",
        name="Italo-Romance Vulgar Latin",
        family="Italic",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="la",
        ancestors=(
            Ancestor("la", P, 0.82,
                     "Primary descent from Classical Latin"),
            Ancestor("grc", SUB, 0.08,
                     "Magna Graecia Greek substrate: Southern Italy "
                     "Greek colonies contributed to S. Italo-Romance "
                     "features (retroflexion in Sicilian, lexicon)."),
            Ancestor("got", SUP, 0.05,
                     "Ostrogothic superstrate (5th–6th c.): "
                     "Vocabulary (guerra, guardia), limited phonological "
                     "impact compared to Frankish in Gaul."),
            Ancestor("gem", SUP, 0.05,
                     "Lombardic superstrate (6th–8th c.): "
                     "North Italian: lexicon (guancia, stinco, "
                     "schiena), possible influence on N. Italian "
                     "lenition patterns. More significant than "
                     "Ostrogothic."),
        ),
        notes=(
            "Italo-Romance Vulgar Latin (~3rd–7th c. CE). Spoken Latin "
            "of the Italian peninsula. Key innovations: (1) Gemination "
            "PRESERVED (hallmark feature: anno, bello, terra). (2) /u/ "
            "not fronted to /y/ (unlike Gallo-Romance). (3) Weaker "
            "lenition than Western Romance. (4) Final -s LOST (plurals "
            "by vowel alternation, not -s). (5) Palatalisation of "
            "k/g before e,i → [tʃ]/[dʒ]. Ancestor of Tuscan/Italian, "
            "Neapolitan, Sicilian, Corsican. Sardinian is EXCLUDED — "
            "it diverged before these innovations (Lausberg 1971)."
        ),
    ),
}
