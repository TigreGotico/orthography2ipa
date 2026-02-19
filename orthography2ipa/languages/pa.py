"""Punjabi (pa) — grapheme→IPA and allophone mappings.
Covers both Gurmukhi (Eastern/Indian Punjabi) and Shahmukhi (Western/Pakistani Punjabi).

Sources:
- Shackle, C. (1972). *Punjabi*. Teach Yourself Languages. Hodder.
- Gill, H.S. & Gleason, H.A. (1963). *A Reference Grammar of Punjabi*. Patiala.
- Bhatia, T. (1993). *Punjabi: A Cognitive-Descriptive Grammar*. Routledge.
- Mastrangelo, M.P. (2006). *Tone in Punjabi*. IULC.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
AD = AncestorRole.ADSTRATE

# ══════════════════════════════════════════════════════════════════════════════
# Punjabi Gurmukhi (Eastern / Indian Punjabi)
# ══════════════════════════════════════════════════════════════════════════════
# Critical feature: Punjabi has lost aspirates and breathy stops in most
# environments, replacing them with TONAL CONTRASTS (low/high/mid tone).
# This is unusual for an Indo-Aryan language.

GRAPHEMES_PA = {
    # --- Independent vowels ---
    "ਅ": ["ə"],
    "ਆ": ["aː"],
    "ਇ": ["i"],
    "ਈ": ["iː"],
    "ਉ": ["u"],
    "ਊ": ["uː"],
    "ਏ": ["eː"],
    "ਐ": ["ɛː"],
    "ਓ": ["oː"],
    "ਔ": ["ɔː"],

    # --- Vowel diacritics ---
    "ਾ": ["aː"], "ਿ": ["i"], "ੀ": ["iː"],
    "ੁ": ["u"], "ੂ": ["uː"],
    "ੇ": ["eː"], "ੈ": ["ɛː"],
    "ੋ": ["oː"], "ੌ": ["ɔː"],

    # --- Tonal/nasalisation markers ---
    "ੰ": ["̃"],  # tippi: nasalisation
    "ਂ": ["̃"],  # bindi: nasalisation
    "ੱ": [""],  # addhak: gemination marker

    # --- Velars ---
    "ਕ": ["k"], "ਖ": ["kʰ"], "ਗ": ["ɡ"], "ਘ": ["ɡ˩"], "ਙ": ["ŋ"],
    # ਘ: historically /ɡʱ/, now realized as /ɡ/ with low tone in Punjabi

    # --- Palatals ---
    "ਚ": ["tʃ"], "ਛ": ["tʃʰ"], "ਜ": ["dʒ"], "ਝ": ["dʒ˩"], "ਞ": ["ɲ"],

    # --- Retroflexes ---
    "ਟ": ["ʈ"], "ਠ": ["ʈʰ"], "ਡ": ["ɖ"], "ਢ": ["ɖ˩"], "ਣ": ["ɳ"],

    # --- Dentals ---
    "ਤ": ["t̪"], "ਥ": ["t̪ʰ"], "ਦ": ["d̪"], "ਧ": ["d̪˩"], "ਨ": ["n"],

    # --- Labials ---
    "ਪ": ["p"], "ਫ": ["pʰ"], "ਬ": ["b"], "ਭ": ["b˩"], "ਮ": ["m"],

    # --- Semivowels / liquids ---
    "ਯ": ["j"],
    "ਰ": ["r"],
    "ਲ": ["l"],
    "ਲ਼": ["ɭ"],  # retroflex l (in some dialects)
    "ਵ": ["ʋ"],
    "ੜ": ["ɽ"],  # retroflex flap

    # --- Sibilants ---
    "ਸ": ["s"],
    "ਸ਼": ["ʃ"],  # sha (Persian loan)
    "ਹ": ["ɦ"],  # he: voiced glottal fricative (tone trigger)

    # --- Persian/Arabic loan consonants ---
    "ਖ਼": ["x"], "ਗ਼": ["ɣ"],
    "ਜ਼": ["z"], "ਫ਼": ["f"],
    "ਲ਼": ["ɭ"], "ਕ਼": ["q"],
}

ALLOPHONES_PA = {
    "p": ["p"], "pʰ": ["pʰ"],
    "b": ["b"],
    "t̪": ["t̪"], "t̪ʰ": ["t̪ʰ"],
    "d̪": ["d̪"],
    "ʈ": ["ʈ"], "ʈʰ": ["ʈʰ"],
    "ɖ": ["ɖ"],
    "k": ["k"], "kʰ": ["kʰ"],
    "ɡ": ["ɡ"],
    "tʃ": ["tʃ"], "tʃʰ": ["tʃʰ"],
    "dʒ": ["dʒ"],
    "m": ["m"], "n": ["n", "ŋ", "ɲ", "ɳ"],
    "ɳ": ["ɳ"], "ɲ": ["ɲ"], "ŋ": ["ŋ"],
    "s": ["s"], "ʃ": ["ʃ"],
    "x": ["x"], "ɣ": ["ɣ"],
    "f": ["f"], "z": ["z"],
    "ɦ": ["ɦ", "h"],
    "r": ["r"], "ɽ": ["ɽ"],
    "l": ["l"], "ɭ": ["ɭ"],
    "ʋ": ["ʋ", "w"],
    "j": ["j"],
    "ə": ["ə"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "eː": ["eː"], "ɛː": ["ɛː"],
    "oː": ["oː"], "ɔː": ["ɔː"],
}

SPECS = {
    "pa": LanguageSpec(
        code="pa",
        name="Punjabi",
        family="Indo-Aryan",
        script="Gurmukhi",
        graphemes=GRAPHEMES_PA,
        allophones=ALLOPHONES_PA,
        parent="sa",
        ancestors=(
            Ancestor("sa", P, 0.82,
                     "Descent via Shauraseni Apabhraṃśa"),
            Ancestor("fa", AD, 0.10,
                     "Persian adstrate through Mughal period and Lahore cultural sphere"),
            Ancestor("ar", AD, 0.05,
                     "Arabic adstrate: religious vocabulary"),
        ),
        notes=(
            "Eastern Punjabi (Gurmukhi script, India). "
            "Typologically remarkable: phonemic tone system (low/mid/high) "
            "developed from former breathy/aspirate contrasts. "
            "⟨ਘ ਝ ਢ ਧ ਭ⟩ historically breathy-voiced, now trigger low tone. "
            "⟨ਹ⟩ triggers low tone on preceding/following vowel when not initial. "
            "Western Punjabi (Shahmukhi, Pakistan) written in Perso-Arabic script."
        ),
    ),
    "pa-PK": LanguageSpec(
        code="pa-PK",
        name="Western Punjabi (Shahmukhi)",
        family="Indo-Aryan",
        script="Arabic",
        graphemes=GRAPHEMES_PA,  # phonological system similar
        allophones=ALLOPHONES_PA,
        parent="pa",
        notes=(
            "Western Punjabi as spoken in Pakistan, written in Shahmukhi "
            "(Perso-Arabic) script. Phonological system closely parallel to "
            "Eastern Punjabi but with stronger Persian/Arabic lexical influence."
        ),
    ),
}
