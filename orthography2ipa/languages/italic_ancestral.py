"""Extinct substrate and superstrate languages from Italian Peninsula."""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT


# ═══════════════════════════════════════════════════════════════════════════
# OSCAN (osc) — Italic, substrate in S. Italy
# ═══════════════════════════════════════════════════════════════════════════
#
# Sabellic (Osco-Umbrian) language of Samnium, Campania, Lucania.
# ~400 inscriptions. Closest relative of Latin within Italic.
#
# Sources:
# - Buck, C.D. (1928). *A Grammar of Oscan and Umbrian*. Branden Press.
# - Rix, H. (2002). *Sabellische Texte*. Winter.
# - McDonald, K. (2015). *Oscan in Southern Italy and Sicily*. CUP.

GRAPHEMES_OSC = {
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
    "í": ["iː"], "ú": ["uː"],
    "b": ["b"], "p": ["p"],
    "d": ["d"], "t": ["t"],
    "g": ["ɡ"], "k": ["k"],
    "f": ["f"], "v": ["v", "w"],
    "s": ["s"], "z": ["ts"],
    "h": ["h"],
    "m": ["m"], "n": ["n"],
    "l": ["l"], "r": ["r"],
}

ALLOPHONES_OSC = {
    "a": ["a"], "e": ["e"], "i": ["i"], "iː": ["iː"],
    "o": ["o"], "u": ["u"], "uː": ["uː"],
    "b": ["b"], "p": ["p"], "d": ["d"], "t": ["t"],
    "ɡ": ["ɡ"], "k": ["k"],
    "f": ["f"], "v": ["v", "w"],
    "s": ["s"], "ts": ["ts"],
    "h": ["h"],
    "m": ["m"], "n": ["n"],
    "l": ["l"], "r": ["r"],
}

# ═══════════════════════════════════════════════════════════════════════════
# UMBRIAN (xum) — Italic, substrate in central Italy
# ═══════════════════════════════════════════════════════════════════════════
#
# Sabellic language of Umbria. Main source: Iguvine Tablets (7 bronze
# tablets, ~3rd–1st c. BCE, longest Italic text outside Latin).
#
# Sources:
# - Rix, H. (2002). *Sabellische Texte*. Winter.
# - Bakkum, G. (2009). *The Latin Dialect of the Ager Faliscus*. Amsterdam UP.

GRAPHEMES_XUM = {
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
    "b": ["b"], "p": ["p"],
    "d": ["d"], "t": ["t"],
    "g": ["ɡ"], "k": ["k"],
    "f": ["f"], "v": ["v"],
    "s": ["s"], "ś": ["ʃ"],  # distinctive Umbrian sibilant
    "rs": ["r̝"],  # Umbrian rhotacism product
    "h": ["h"],
    "m": ["m"], "n": ["n"],
    "l": ["l"], "r": ["r"],
    "ç": ["ts"],  # palatalised stop
}

ALLOPHONES_XUM = {
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
    "b": ["b"], "p": ["p"], "d": ["d"], "t": ["t"],
    "ɡ": ["ɡ"], "k": ["k"],
    "f": ["f"], "v": ["v"],
    "s": ["s"], "ʃ": ["ʃ"],
    "ts": ["ts"], "r̝": ["r̝"],
    "h": ["h"],
    "m": ["m"], "n": ["n"],
    "l": ["l"], "r": ["r"],
}

# ═══════════════════════════════════════════════════════════════════════════
# ETRUSCAN (etr) — pre-IE substrate of Tuscany
# ═══════════════════════════════════════════════════════════════════════════
#
# Non-Indo-European language of pre-Roman Etruria. ~13,000 inscriptions.
# Language is READABLE but only partially TRANSLATED.
# Massive influence on Latin (and through it, all Romance) in
# vocabulary, onomastics, and possibly phonology.
#
# Sources:
# - Bonfante, G. & Bonfante, L. (2002). *The Etruscan Language*. 2nd ed. MUP.
# - Rix, H. (1991). *Etruskische Texte*. Narr.
# - Wallace, R. (2008). *Zikh Rasna: A Manual of the Etruscan Language
#   and Inscriptions*. Beech Stave Press.

GRAPHEMES_ETR = {
    # 4-vowel system (NO /o/ — distinctive Etruscan feature)
    "a": ["a"], "e": ["e"], "i": ["i"], "u": ["u"],
    # Stops (aspirate series prominent)
    "p": ["p"], "t": ["t"], "c": ["k"],
    "ph": ["pʰ"], "th": ["tʰ"], "ch": ["kʰ"],
    # Fricatives
    "f": ["f"], "s": ["s"], "ś": ["ʃ"],
    "h": ["h"],
    # Nasals
    "m": ["m"], "n": ["n"],
    # Liquids
    "l": ["l"], "r": ["r"],
    # Glides
    "v": ["w"],  # labiovelar glide, not /v/
}

ALLOPHONES_ETR = {
    "a": ["a"], "e": ["e"], "i": ["i"], "u": ["u"],
    "p": ["p"], "t": ["t"], "k": ["k"],
    "pʰ": ["pʰ"], "tʰ": ["tʰ"], "kʰ": ["kʰ"],
    "f": ["f"], "s": ["s"], "ʃ": ["ʃ"],
    "h": ["h"],
    "m": ["m"], "n": ["n"],
    "l": ["l"], "r": ["r"],
    "w": ["w"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SPECS
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "osc": LanguageSpec(
        code="osc", name="Oscan",
        family="Italic", script="Latin",
        graphemes=GRAPHEMES_OSC, allophones=ALLOPHONES_OSC,
        parent="ine",
        notes=(
            "Oscan (5th c. BCE – 1st c. CE). Sabellic (Osco-Umbrian) "
            "language of Samnium, Campania, Lucania, Bruttium. ~400 "
            "inscriptions. Closest Italic relative of Latin. Substrate "
            "in Southern Italo-Romance: possible influence on Neapolitan "
            "and Sicilian vowel systems. Distinct from Latin in vowel "
            "diphthongisation patterns (Buck 1928, Rix 2002)."
        ),
    ),
    "xum": LanguageSpec(
        code="xum", name="Umbrian",
        family="Italic", script="Latin",
        graphemes=GRAPHEMES_XUM, allophones=ALLOPHONES_XUM,
        parent="ine",
        notes=(
            "Umbrian (3rd–1st c. BCE). Sabellic language of Umbria. "
            "Main source: Iguvine Tablets (7 bronze tablets, longest "
            "Italic text outside Latin). Distinctive sibilant /ʃ/ and "
            "extensive rhotacism. Substrate in central Italian "
            "dialects (Rix 2002)."
        ),
    ),
    "etr": LanguageSpec(
        code="etr", name="Etruscan",
        family="Tyrrhenian", script="Latin",
        graphemes=GRAPHEMES_ETR, allophones=ALLOPHONES_ETR,
        notes=(
            "Etruscan (8th c. BCE – 1st c. CE). Non-IE language isolate "
            "(or Tyrrhenian family with Rhaetic and Lemnian). ~13,000 "
            "inscriptions, READABLE but only partially translated. "
            "4-vowel system (no /o/!), aspirate stops prominent. "
            "MASSIVE influence on Latin: alphabet, vocabulary (persona, "
            "fenestra, histrio, lanista, arena, elementum), and through "
            "Latin on ALL Romance languages. Pre-Roman substrate of "
            "Tuscany; possibly influenced gorgia toscana "
            "(Bonfante & Bonfante 2002, Wallace 2008)."
        ),
    ),
}