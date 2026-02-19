"""Munda languages: Santali (sat), Mundari (unr) — grapheme→IPA and allophone mappings.
Tibeto-Burman: Meitei/Manipuri (mni), Bodo (brx) — grapheme→IPA and allophone mappings.

Sources (Munda):
- Zide, N. (1965). *A Munda Bibliographical List*. Univ. Chicago.
- Neukom, L. (1995). *Santali*. LINCOM Europa.
- Pinnow, H.-J. (1959). *Versuch einer historischen Lautlehre der Kharia-Sprache*.
- Anderson, G.D.S. (2008). *The Munda Languages*. Routledge.

Sources (Tibeto-Burman):
- Chelliah, S.L. (1997). *A Grammar of Meithei*. Mouton.
- Bhat, D.N.S. (1968). *Boro (Bodo): A Descriptive Analysis*. Poona.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
AD = AncestorRole.ADSTRATE
SUB = AncestorRole.SUBSTRATE

# ══════════════════════════════════════════════════════════════════════════════
# Santali — Jharkhand/West Bengal/Odisha; Ol Chiki script (official) + Latin/Devanagari
# ══════════════════════════════════════════════════════════════════════════════
# Santali is Austroasiatic (Munda branch), completely unrelated to Indo-Aryan or Dravidian.
# Key features: consonant clusters; aspirates phonemic; glottalized stops;
# phonemic distinction between plain /n/ and apical-alveolar; no retroflex stops.

GRAPHEMES_SAT = {
    # Romanisation following Bodding/Zide convention
    # --- Vowels ---
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "e": ["e"], "eː": ["eː"],
    "o": ["o"], "oː": ["oː"],
    "ɔ": ["ɔ"],
    # Glottalized vowels (checked syllables)
    "aʔ": ["aˀ"], "iʔ": ["iˀ"], "uʔ": ["uˀ"],

    # --- Stops ---
    "p": ["p"], "pʰ": ["pʰ"], "b": ["b"],
    "t": ["t"], "tʰ": ["tʰ"], "d": ["d"],
    "k": ["k"], "kʰ": ["kʰ"], "g": ["ɡ"],
    "ʔ": ["ʔ"],  # glottal stop

    # --- Affricates ---
    "c": ["tʃ"], "ch": ["tʃʰ"], "j": ["dʒ"],

    # --- Nasals ---
    "m": ["m"],
    "n": ["n"],
    "ŋ": ["ŋ"],

    # --- Fricatives ---
    "s": ["s"],
    "h": ["h"],

    # --- Liquids / glides ---
    "l": ["l"],
    "r": ["r"],
    "y": ["j"],
    "w": ["w"],
}

ALLOPHONES_SAT = {
    "p": ["p"], "pʰ": ["pʰ"], "b": ["b"],
    "t": ["t"], "tʰ": ["tʰ"], "d": ["d"],
    "k": ["k"], "kʰ": ["kʰ"], "ɡ": ["ɡ"],
    "ʔ": ["ʔ"],
    "tʃ": ["tʃ"], "tʃʰ": ["tʃʰ"], "dʒ": ["dʒ"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "s": ["s"], "h": ["h"],
    "l": ["l"], "r": ["r"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "e": ["e"], "eː": ["eː"],
    "o": ["o"], "oː": ["oː"],
    "ɔ": ["ɔ"],
}

# ══════════════════════════════════════════════════════════════════════════════
# Mundari — Jharkhand; Latin/Devanagari scripts
# ══════════════════════════════════════════════════════════════════════════════

GRAPHEMES_UNR = {
    **GRAPHEMES_SAT,
    # Mundari has some additional distinctions from Santali
    "ɖ": ["ɖ"],  # retroflex d (borrowed/contact)
    "ɳ": ["ɳ"],  # retroflex n
}

ALLOPHONES_UNR = {
    **ALLOPHONES_SAT,
    "ɖ": ["ɖ", "d"],
    "ɳ": ["ɳ", "n"],
}

# ══════════════════════════════════════════════════════════════════════════════
# Meitei / Manipuri — Manipur; Meitei Mayek script (official) + Bengali
# ══════════════════════════════════════════════════════════════════════════════
# Tibeto-Burman; tonal; no aspiration/voice distinction in native words.

GRAPHEMES_MNI = {
    # Romanisation following Chelliah 1997
    # --- Vowels ---
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "e": ["e"], "eː": ["eː"],
    "o": ["o"], "oː": ["oː"],
    "ə": ["ə"],

    # --- Tone markers (for reference; phonemic) ---
    # Meitei has falling, level, rising tones on stressed syllables

    # --- Stops (4 series in loanwords; native: tenuis only) ---
    "p": ["p"], "ph": ["pʰ"], "b": ["b"],
    "t": ["t"], "th": ["tʰ"], "d": ["d"],
    "k": ["k"], "kh": ["kʰ"], "g": ["ɡ"],
    "ʔ": ["ʔ"],  # glottal stop (syllable-final allophone)

    # --- Affricates ---
    "c": ["tʃ"], "ch": ["tʃʰ"], "j": ["dʒ"],

    # --- Nasals ---
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],

    # --- Fricatives ---
    "s": ["s"], "z": ["z"],
    "h": ["h"],

    # --- Liquids / glides ---
    "l": ["l"],
    "r": ["r"],
    "y": ["j"],
    "w": ["w"],
}

ALLOPHONES_MNI = {
    "p": ["p", "pʰ"],  # Meitei: aspiration in onset
    "t": ["t", "tʰ"],
    "k": ["k", "kʰ", "ʔ"],  # [ʔ] in coda
    "b": ["b"], "d": ["d"], "ɡ": ["ɡ"],
    "tʃ": ["tʃ", "tʃʰ"], "dʒ": ["dʒ"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "s": ["s"], "z": ["z"], "h": ["h"],
    "l": ["l"], "r": ["r"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "e": ["e"], "eː": ["eː"],
    "o": ["o"], "oː": ["oː"],
    "ə": ["ə"],
}

# ══════════════════════════════════════════════════════════════════════════════
# Bodo — Assam; Devanagari script
# ══════════════════════════════════════════════════════════════════════════════
# Tibeto-Burman; tonal (falling vs. non-falling); aspirated vs. non-aspirated.

GRAPHEMES_BRX = {
    # Romanisation / Devanagari transcription

    # --- Vowels ---
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "e": ["e"], "eː": ["eː"],
    "o": ["o"], "oː": ["oː"],
    "ə": ["ə"],

    # --- Stops ---
    "p": ["p"], "pʰ": ["pʰ"],
    "b": ["b"], "bʱ": ["bʱ"],
    "t": ["t"], "tʰ": ["tʰ"],
    "d": ["d"], "dʱ": ["dʱ"],
    "k": ["k"], "kʰ": ["kʰ"],
    "ɡ": ["ɡ"], "ɡʱ": ["ɡʱ"],
    "ʔ": ["ʔ"],

    # --- Affricates ---
    "ts": ["ts"], "tʃ": ["tʃ"], "tʃʰ": ["tʃʰ"],
    "dʒ": ["dʒ"],

    # --- Nasals ---
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],

    # --- Fricatives ---
    "s": ["s"], "ʃ": ["ʃ"], "h": ["h"],

    # --- Liquids / glides ---
    "l": ["l"], "r": ["r"],
    "j": ["j"], "w": ["w"],
}

ALLOPHONES_BRX = {
    "p": ["p"], "pʰ": ["pʰ"], "b": ["b"],
    "t": ["t"], "tʰ": ["tʰ"], "d": ["d"],
    "k": ["k"], "kʰ": ["kʰ"], "ɡ": ["ɡ"], "ʔ": ["ʔ"],
    "ts": ["ts"], "tʃ": ["tʃ"], "tʃʰ": ["tʃʰ"], "dʒ": ["dʒ"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "s": ["s"], "ʃ": ["ʃ"], "h": ["h"],
    "l": ["l"], "r": ["r"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "e": ["e"], "eː": ["eː"],
    "o": ["o"], "oː": ["oː"],
    "ə": ["ə"],
}

SPECS = {
    "sat": LanguageSpec(
        code="sat",
        name="Santali",
        family="Austroasiatic",
        script="Ol Chiki",
        graphemes=GRAPHEMES_SAT,
        allophones=ALLOPHONES_SAT,
        parent=None,
        ancestors=(
            Ancestor("sat-x-proto-munda", P, 0.90,
                     "Descent from Proto-Munda (Austroasiatic)"),
        ),
        notes=(
            "Santali (Jharkhand, West Bengal, Odisha, Bihar). "
            "Austroasiatic, Munda branch — unrelated to IA or Dravidian. "
            "Written officially in Ol Chiki script (invented 1925 by Raghunath Murmu); "
            "also Latin and Devanagari. "
            "Phonemic aspiration in stops; glottalized vowels in checked syllables. "
            "No retroflex consonants (unlike IA neighbours)."
        ),
    ),
    "unr": LanguageSpec(
        code="unr",
        name="Mundari",
        family="Austroasiatic",
        script="Latin",
        graphemes=GRAPHEMES_UNR,
        allophones=ALLOPHONES_UNR,
        parent=None,
        ancestors=(
            Ancestor("sat-x-proto-munda", P, 0.88,
                     "Descent from Proto-Munda; sister language to Santali"),
        ),
        notes=(
            "Mundari (Jharkhand). Closely related to Santali. "
            "Written in Latin (linguistic convention) or Devanagari. "
            "Has some retroflex consonants from IA contact."
        ),
    ),
    "mni": LanguageSpec(
        code="mni",
        name="Meitei",
        family="Tibeto-Burman",
        script="Meitei Mayek",
        graphemes=GRAPHEMES_MNI,
        allophones=ALLOPHONES_MNI,
        parent=None,
        ancestors=(
            Ancestor("mni-x-proto-kuki-chin", P, 0.85,
                     "Tibeto-Burman, Kuki-Chin branch"),
            Ancestor("bn", AD, 0.08,
                     "Bengali adstrate through administrative contact"),
        ),
        notes=(
            "Meitei/Manipuri (Manipur, India). "
            "Tibeto-Burman, Kuki-Chin-Mizo branch. "
            "Phonemic tone (falling vs. non-falling in stressed syllable). "
            "Meitei Mayek script (traditional, restored 2013 as official). "
            "Also written in Bengali script officially."
        ),
    ),
    "brx": LanguageSpec(
        code="brx",
        name="Bodo",
        family="Tibeto-Burman",
        script="Devanagari",
        graphemes=GRAPHEMES_BRX,
        allophones=ALLOPHONES_BRX,
        parent=None,
        ancestors=(
            Ancestor("brx-x-proto-boro-garo", P, 0.88,
                     "Tibeto-Burman, Boro-Garo branch"),
            Ancestor("as", AD, 0.07,
                     "Assamese adstrate: long administrative contact"),
        ),
        notes=(
            "Bodo (Assam, India). "
            "Tibeto-Burman, Boro-Garo branch. "
            "Phonemic tonal distinction (falling vs. level). "
            "Written in Devanagari (official since 2003). "
            "Aspirated and plain stops both phonemic."
        ),
    ),
}
