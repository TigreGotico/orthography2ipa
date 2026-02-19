"""Tulu (tcy), Khasi (kha), and Proto-Dravidian node.

Sources (Tulu):
- Upadhyaya, U.P. (1988). *Tulu Lexicon*. Udupi.
- Krishnamurti, Bh. (2003). *The Dravidian Languages*. CUP.

Sources (Khasi):
- Nagaraja, K.S. (1985). *Khasi: A Descriptive Analysis*. Deccan College.
- Henderson, E.J.A. (1952). 'The main features of Cambodian pronunciation'. BSOAS 14.
  (comparative Austroasiatic reference)
- Rabel-Heymann, L. (1977). *Khasi of Meghalaya*. Calcutta.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
AD = AncestorRole.ADSTRATE

# ══════════════════════════════════════════════════════════════════════════════
# Proto-Dravidian node (for ancestry tree)
# ══════════════════════════════════════════════════════════════════════════════

GRAPHEMES_PDR = {
    # Reconstructed Proto-Dravidian phonology (Krishnamurti 2003)
    # Vowels: 5 short/long pairs + diphthongs
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "e": ["e"], "eː": ["eː"],
    "o": ["o"], "oː": ["oː"],
    "ai": ["ai"], "au": ["au"],

    # Stops (2 series: unaspirated plain)
    "p": ["p"], "t": ["t"], "ʈ": ["ʈ"], "c": ["tɕ"], "k": ["k"],
    # Voiced medial allophones of the above (positional)
    "b": ["b"], "d": ["d"], "ɖ": ["ɖ"], "dʑ": ["dʑ"], "ɡ": ["ɡ"],

    # Nasals
    "m": ["m"], "n": ["n"], "ɳ": ["ɳ"], "ɲ": ["ɲ"], "ŋ": ["ŋ"],

    # Approximants / liquids
    "l": ["l"], "ɭ": ["ɭ"], "ɻ": ["ɻ"], "r": ["r"],
    "j": ["j"], "ʋ": ["ʋ"],
}

ALLOPHONES_PDR = {
    "p": ["p", "b"], "t": ["t", "d"], "ʈ": ["ʈ", "ɖ"],
    "tɕ": ["tɕ", "dʑ"], "k": ["k", "ɡ"],
    "m": ["m"], "n": ["n"], "ɳ": ["ɳ"], "ɲ": ["ɲ"], "ŋ": ["ŋ"],
    "l": ["l"], "ɭ": ["ɭ"], "ɻ": ["ɻ"], "r": ["r"],
    "j": ["j"], "ʋ": ["ʋ"],
    "a": ["a"], "aː": ["aː"], "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"], "e": ["e"], "eː": ["eː"],
    "o": ["o"], "oː": ["oː"],
}

# ══════════════════════════════════════════════════════════════════════════════
# Tulu — Karnataka coastal belt; Tigaḷari / Kannada scripts
# ══════════════════════════════════════════════════════════════════════════════

GRAPHEMES_TCY = {
    # Tulu is written in Tigaḷari (traditional) or Kannada (practical).
    # Romanisation following Upadhyaya 1988.
    # Vowels
    "a": ["a"], "ā": ["aː"],
    "i": ["i"], "ī": ["iː"],
    "u": ["u"], "ū": ["uː"],
    "e": ["e"], "ē": ["eː"],
    "o": ["o"], "ō": ["oː"],
    "ai": ["ai"], "au": ["au"],

    # Stops: Tulu has voiced/voiceless distinction + aspirates from Sanskrit
    "k": ["k"], "kh": ["kʰ"], "g": ["ɡ"], "gh": ["ɡʱ"],
    "c": ["tɕ"], "ch": ["tɕʰ"], "j": ["dʑ"], "jh": ["dʑʱ"],
    "ṭ": ["ʈ"], "ṭh": ["ʈʰ"], "ḍ": ["ɖ"], "ḍh": ["ɖʱ"],
    "t": ["t̪"], "th": ["t̪ʰ"], "d": ["d̪"], "dh": ["d̪ʱ"],
    "p": ["p"], "ph": ["pʰ"], "b": ["b"], "bh": ["bʱ"],

    # Nasals
    "m": ["m"], "n": ["n"], "ṇ": ["ɳ"], "ñ": ["ɲ"], "ṅ": ["ŋ"],

    # Liquids / approximants
    "y": ["j"], "r": ["r"],
    "l": ["l"], "ḷ": ["ɭ"], "ḻ": ["ɻ"],  # retroflex lateral + approximant
    "v": ["ʋ"],

    # Sibilants / aspirate
    "ś": ["ʃ"], "ṣ": ["ʂ"], "s": ["s"], "h": ["h"],
}

ALLOPHONES_TCY = {
    "k": ["k"], "kʰ": ["kʰ"],
    "ɡ": ["ɡ"], "ɡʱ": ["ɡʱ"],
    "tɕ": ["tɕ"], "tɕʰ": ["tɕʰ"],
    "dʑ": ["dʑ"], "dʑʱ": ["dʑʱ"],
    "ʈ": ["ʈ"], "ʈʰ": ["ʈʰ"],
    "ɖ": ["ɖ"], "ɖʱ": ["ɖʱ"],
    "t̪": ["t̪"], "t̪ʰ": ["t̪ʰ"],
    "d̪": ["d̪"], "d̪ʱ": ["d̪ʱ"],
    "p": ["p"], "pʰ": ["pʰ"],
    "b": ["b"], "bʱ": ["bʱ"],
    "m": ["m"], "n": ["n"], "ɲ": ["ɲ"], "ɳ": ["ɳ"], "ŋ": ["ŋ"],
    "ʃ": ["ʃ"], "ʂ": ["ʂ"], "s": ["s"], "h": ["h"],
    "r": ["r"], "l": ["l"], "ɭ": ["ɭ"], "ɻ": ["ɻ"],
    "ʋ": ["ʋ"], "j": ["j"],
    "a": ["a"], "aː": ["aː"], "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"], "e": ["e"], "eː": ["eː"],
    "o": ["o"], "oː": ["oː"],
}

# ══════════════════════════════════════════════════════════════════════════════
# Khasi — Meghalaya; Latin script (Austroasiatic, Mon-Khmer branch)
# ══════════════════════════════════════════════════════════════════════════════
# NOTE: Khasi is Austroasiatic (Mon-Khmer branch), not Dravidian or IA.
# It is included here as an Indian non-IA/non-Dravidian scheduled language.

GRAPHEMES_KHA = {
    # Vowels
    "a": ["a"], "ai": ["ai"], "au": ["au"],
    "e": ["e"], "i": ["i"],
    "o": ["o"], "oi": ["oi"],
    "u": ["u"],
    "ia": ["ia"], "ui": ["ui"],

    # Stops
    "p": ["p"], "b": ["b"],
    "t": ["t"], "d": ["d"],
    "k": ["k"], "g": ["ɡ"],
    "kh": ["kʰ"],
    "nk": ["ŋk"],  # prenasalised cluster

    # Affricates
    "jng": ["dʒŋ"],  # rare cluster

    # Nasals
    "m": ["m"], "n": ["n"], "ng": ["ŋ"],

    # Fricatives
    "s": ["s"], "sh": ["ʃ"],
    "h": ["h"],

    # Liquids / glides
    "l": ["l"],
    "r": ["r"],
    "y": ["j"],
    "w": ["w"],
}

ALLOPHONES_KHA = {
    "p": ["p"], "b": ["b"],
    "t": ["t"], "d": ["d"],
    "k": ["k"], "ɡ": ["ɡ"], "kʰ": ["kʰ"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "s": ["s"], "ʃ": ["ʃ"], "h": ["h"],
    "l": ["l"], "r": ["r"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "e": ["e"], "i": ["i"],
    "o": ["o"], "u": ["u"],
    "ai": ["ai"], "au": ["au"], "oi": ["oi"],
}

SPECS = {
    "ta-x-proto-dravidian": LanguageSpec(
        code="ta-x-proto-dravidian",
        name="Proto-Dravidian",
        family="Dravidian",
        script="Latin",
        graphemes=GRAPHEMES_PDR,
        allophones=ALLOPHONES_PDR,
        parent=None,
        notes=(
            "Reconstructed Proto-Dravidian (c. 3000–2000 BCE, before IA arrival). "
            "Following Krishnamurti (2003): 5 vowel qualities × short/long; "
            "two stop series (initial: unaspirated; medial: voiced allophones); "
            "no aspiration contrast in native vocabulary; "
            "retroflex series (ʈ ɖ ɳ ɭ ɻ) — may be the source of IA retroflexes."
        ),
    ),
    "tcy": LanguageSpec(
        code="tcy",
        name="Tulu",
        family="Dravidian",
        script="Kannada",  # practical script; Tigaḷari is traditional
        graphemes=GRAPHEMES_TCY,
        allophones=ALLOPHONES_TCY,
        parent=None,
        ancestors=(
            Ancestor("ta-x-proto-dravidian", P, 0.88,
                     "South Dravidian I branch, closely related to Kannada/Tamil"),
        ),
        notes=(
            "Tulu (coastal Karnataka / Udupi / Mangaluru district). "
            "South Dravidian language; unwritten in daily practice but has "
            "traditional Tigaḷari script (Buddhist manuscripts). "
            "Usually written in Kannada script. "
            "Distinct from Kannada despite geographic closeness. "
            "Full aspirate series from Sanskrit contact."
        ),
    ),
    "kha": LanguageSpec(
        code="kha",
        name="Khasi",
        family="Austroasiatic",
        script="Latin",
        graphemes=GRAPHEMES_KHA,
        allophones=ALLOPHONES_KHA,
        parent=None,
        ancestors=(
            Ancestor("kha-x-proto-mon-khmer", P, 0.88,
                     "Austroasiatic, Mon-Khmer branch (distant from Munda)"),
        ),
        notes=(
            "Khasi (Meghalaya, India). "
            "Austroasiatic, Mon-Khmer branch — unrelated to IA, Dravidian, or Munda. "
            "One of only two scheduled languages not from IA or Dravidian families. "
            "Written in Latin script since Welsh/British missionary period (1840s). "
            "Matrilineal society; shares phonological typology with Southeast Asian Mon-Khmer."
        ),
    ),
}
