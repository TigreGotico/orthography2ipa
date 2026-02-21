"""Sardinian (sc) — grapheme→IPA and allophone mappings.

Sardinian is widely considered the MOST CONSERVATIVE Romance language,
having diverged from Common Latin BEFORE many of the innovations shared
by the other branches (Western, Eastern, Italo-Romance). It preserves
Latin /k/ and /ɡ/ before front vowels, the 5-vowel system, and other
archaic features.

The language has two main varieties:
- Logudorese (sc-x-logudorese): most archaic, "true" conservative Sardinian
- Campidanese (sc-x-campidanese): more innovative, Catalan/Spanish influence

Sources:
- Jones, M.A. (1988). *Sardinian Syntax*. Routledge.
- Blasco Ferrer, E. (1984). *Grammatica storica del sardo*. Niemeyer.
- Contini, M. (1987). *Étude de géographie phonétique et de phonétique
  instrumentale du sarde*. Edizioni dell'Orso.
- Bolognesi, R. & Heeringa, W. (2005). 'Sardinian between typology
  and contact.' In *Sprachtypologie und Universalienforschung* 58(4).
- Virdis, M. (1978). *Fonetica del dialetto sardo campidanese*. Cagliari.
- Ledgeway, A. & Maiden, M. (eds.) (2016). *The Oxford Guide to the
  Romance Languages*. OUP. [ch. on Sardinian]
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# SARDINIAN (sc)
# ═══════════════════════════════════════════════════════════════════════════
#
# Classification: Romance > Sardinian (its OWN primary branch)
#
# Sardinian preserves numerous archaic features lost in ALL other
# Romance languages:
#
# 1. VELAR STOPS BEFORE FRONT VOWELS:
#    Latin /k/ before e,i → STILL /k/ (not palatalised!)
#    CENTUM → Log. kentu (vs It. cento [tʃ], Sp. ciento [θ/s])
#    CAELUM → Log. kelu (vs It. cielo, Fr. ciel)
#    This is THE most archaic feature in all of Romance.
#
# 2. FIVE-VOWEL SYSTEM:
#    Latin 10 → Sardinian 5 (NOT 7 like all other Romance):
#    ĭ/ē/ī → /i/ (merged into one)
#    ŭ/ō/ū → /u/ (merged into one)
#    ĕ/ĭ → /e/ but NOT open /ɛ/ (no ɛ/e distinction)
#    ŏ/ŭ → /o/ but NOT open /ɔ/ (no ɔ/o distinction)
#    The most conservative vowel system in Romance.
#
# 3. NO DIPHTHONGISATION:
#    Unlike ALL other Romance: Latin ĕ,ŏ do NOT diphthongise.
#    BONUM → Log. bonu (vs Sp. bueno, It. buono, Fr. bon/bien)
#
# 4. INTERVOCALIC VOICELESS STOPS:
#    Variable: preserved in Logudorese, voiced in Campidanese.
#    Logudorese is more conservative here too.
#
# 5. LATIN -S PRESERVED:
#    Sardinian keeps final -s (like Western Romance):
#    DOMUS → domos
#
# 6. ARTICLE FROM IPSE (not ILLE):
#    Unique in Romance: su/sa from IPSUM/IPSAM (not il/el/le/o).

GRAPHEMES_SC = {
    # --- Vowels (5-vowel system — THE archaic feature) ---
    "a": ["a"],
    "e": ["e"],  # NO /ɛ/ distinction (all mid-front → /e/)
    "i": ["i"],
    "o": ["o"],  # NO /ɔ/ distinction (all mid-back → /o/)
    "u": ["u"],

    # --- Consonants ---
    "b": ["b", "β"],  # lenition in some contexts
    "c": ["k"],  # /k/ EVEN before e,i — the archaic feature!
    "ch": ["k"],  # orthographic variant for /k/ before e,i
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ"],  # /ɡ/ EVEN before e,i (archaic)
    "gh": ["ɡ"],  # orthographic variant for /ɡ/ before e,i
    "h": ["∅"],
    "j": ["dʒ"],  # in loanwords
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "qu": ["kw"],
    "r": ["r"],
    "rr": ["rː"],
    "s": ["s", "z"],  # [z] between vowels
    "t": ["t"],
    "v": ["v", "β"],
    "x": ["ʃ"],  # retroflex fricative in some areas
    "z": ["ts", "dz"],

    # --- Digraphs ---
    "sc": ["sk", "ʃ"],  # /ʃ/ before e,i in Campidanese
    "tz": ["tː s"],  # Sardinian-specific affricate
    "dd": ["ɖː"],  # retroflex stop (Sardinian hallmark)
    "ng": ["ŋɡ"],
    "gn": ["ɲ"],
    "gl": ["ʎ"],  # in some varieties
    "ll": ["lː", "ɖː"],  # can be retroflex in Campidanese

    # --- Diphthongs ---
    "ai": ["aj"],
    "au": ["aw"],
    "ei": ["ej"],
    "oi": ["oj"],
}

ALLOPHONES_SC = {
    "p": ["p"],
    "b": ["b", "β"],
    "t": ["t"],
    "d": ["d", "ð"],
    "k": ["k"],
    "ɡ": ["ɡ", "ɣ"],
    "f": ["f"],
    "v": ["v", "β"],
    "s": ["s", "z"],
    "ʃ": ["ʃ"],
    "ts": ["ts"],
    "dz": ["dz"],
    "dʒ": ["dʒ"],
    "ɖː": ["ɖː"],  # retroflex geminate (cacuminal)
    "m": ["m"],
    "n": ["n", "ŋ", "ɱ"],
    "ɲ": ["ɲ"],
    "l": ["l"],
    "ʎ": ["ʎ"],
    "r": ["r", "ɾ"],
    "rː": ["rː"],
    "j": ["j"],
    "w": ["w"],
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
}

# ═══════════════════════════════════════════════════════════════════════════
# LOGUDORESE (sc-x-logudorese) — most conservative variety
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_LOG = {
    **ALLOPHONES_SC,
    "p": ["p"],  # preserved intervocalically (more archaic)
    "t": ["t", "θ"],  # some lenition but less than Campidanese
    "k": ["k"],  # preserved
}

# ═══════════════════════════════════════════════════════════════════════════
# CAMPIDANESE (sc-x-campidanese) — more innovative, southern
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_CAMP = {
    **ALLOPHONES_SC,
    "p": ["p", "β"],  # more lenition than Logudorese
    "t": ["t", "ð"],
    "k": ["k", "ɣ"],
    "ʃ": ["ʃ"],  # palatalisation of /sk/ before e,i
    "ɖː": ["ɖː"],  # more extensive retroflex
}

SPECS = {
    "sc": LanguageSpec(
        code="sc",
        name="Sardinian",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_SC,
        allophones=ALLOPHONES_SC,
        parent="la",
        ancestors=(
            Ancestor("la", P, 0.88,
                     "Direct from Classical Latin — Sardinian diverged "
                     "BEFORE the Western/Eastern Romance split. Most "
                     "archaic Romance variety."),
            Ancestor("grc", SUB, 0.04,
                     "Greek (Punic-era contacts, Byzantine rule): "
                     "limited phonological impact."),
        ),
        notes=(
            "Sardinian. THE most conservative Romance language. "
            "Primary archaic features: (1) Velars /k, ɡ/ preserved "
            "before front vowels (kentu 'hundred', not *centu). "
            "(2) 5-vowel system (no ɛ/e or ɔ/o split). (3) No "
            "diphthongisation of Latin ĕ, ŏ. (4) Retroflex "
            "consonants [ɖː] from Latin -LL-. (5) Article from "
            "IPSE (su/sa) not ILLE. Sardinian forms its OWN primary "
            "branch of Romance, diverging before Italo-, Gallo-, "
            "Ibero-, and Eastern Romance innovations "
            "(Lausberg 1971, Blasco Ferrer 1984)."
        ),
    ),
    "sc-x-logudorese": LanguageSpec(
        code="sc-x-logudorese",
        name="Logudorese Sardinian",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_SC,
        allophones=ALLOPHONES_LOG,
        parent="sc",
        notes=(
            "Logudorese Sardinian. The MOST archaic variety, spoken "
            "in north-central Sardinia. Less lenition than Campidanese, "
            "preserves intervocalic voiceless stops more consistently. "
            "Often cited as the closest living language to Latin."
        ),
    ),
    "sc-x-campidanese": LanguageSpec(
        code="sc-x-campidanese",
        name="Campidanese Sardinian",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_SC,
        allophones=ALLOPHONES_CAMP,
        parent="sc",
        notes=(
            "Campidanese Sardinian. Southern variety, more innovative "
            "than Logudorese. Greater intervocalic lenition, more "
            "retroflex consonants, some Catalan/Spanish influence "
            "from centuries of Aragonese-Catalan rule."
        ),
    ),
}
