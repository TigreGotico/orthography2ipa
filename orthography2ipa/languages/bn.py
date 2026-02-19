"""Bengali (bn) and Assamese (as) — grapheme→IPA and allophone mappings.

Sources:
- Masica, C.P. (1991). *The Indo-Aryan Languages*. CUP.
- Chatterji, S.K. (1926). *The Origin and Development of the Bengali Language*. Calcutta UP.
- Khan, S. (2010). Bengali (Dhaka Standard). *JIPA* 40(2).
- Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
- Goswami, G.C. (1982). *Structure of Assamese*. Gauhati UP.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
AD = AncestorRole.ADSTRATE

# ══════════════════════════════════════════════════════════════════════════════
# Bengali — West Bengal / Bangladesh standard
# ══════════════════════════════════════════════════════════════════════════════
# Key features: no /ə/ vs /a/ distinction in modern Bengali (both → [a/ɔ]);
# dental/retroflex distinction retained; aspirates phonemic;
# no voiced aspirates for many speakers (merging with plain voiced).

GRAPHEMES_BN = {
    # --- Independent vowels ---
    "অ": ["ɔ"],  # inherent vowel (not /a/ like Hindi)
    "আ": ["a"],  # long ā → [a]
    "ই": ["i"],
    "ঈ": ["i"],  # same phoneme as ই
    "উ": ["u"],
    "ঊ": ["u"],
    "ঋ": ["ri"],  # vocalic ṛ → [ri] in Bengali
    "এ": ["e", "æ"],  # e: [e] before /i/; [æ] elsewhere
    "ঐ": ["oi"],  # oi diphthong
    "ও": ["o"],
    "ঔ": ["ou"],  # ou diphthong

    # --- Vowel diacritics ---
    "া": ["a"], "ি": ["i"], "ী": ["i"],
    "ু": ["u"], "ূ": ["u"], "ৃ": ["ri"],
    "ে": ["e", "æ"], "ৈ": ["oi"],
    "ো": ["o"], "ৌ": ["ou"],

    # --- Diacritics ---
    "ং": ["ŋ"],  # anusvāra
    "ঃ": ["h"],  # visarga
    "ঁ": ["̃"],  # candrabindu
    "্": [""],  # hasanta (virāma)

    # --- Velars ---
    "ক": ["k"], "খ": ["kʰ"], "গ": ["ɡ"], "ঘ": ["ɡʱ"], "ঙ": ["ŋ"],

    # --- Palatals ---
    "চ": ["tɕ"], "ছ": ["tɕʰ"], "জ": ["dʑ"], "ঝ": ["dʑʱ"], "ঞ": ["n"],

    # --- Retroflexes ---
    "ট": ["ʈ"], "ঠ": ["ʈʰ"], "ড": ["ɖ"], "ঢ": ["ɖʱ"], "ণ": ["n"],

    # --- Dentals ---
    "ত": ["t"], "থ": ["tʰ"], "দ": ["d"], "ধ": ["dʱ"], "ন": ["n"],

    # --- Labials ---
    "প": ["p"], "ফ": ["pʰ", "f"], "ব": ["b"], "ভ": ["bʱ", "v"], "ম": ["m"],

    # --- Semivowels / liquids ---
    "য": ["dʑ", "j"],  # ya = /dʑ/ word-initially; /j/ otherwise
    "য়": ["j"],  # antastha ya = [j] approximant
    "র": ["r"],
    "ড়": ["ɽ"],  # retroflex flap
    "ঢ়": ["ɽʱ"],  # aspirated retroflex flap
    "ল": ["l"],
    "ব": ["b", "w"],

    # --- Sibilants ---
    "শ": ["ʃ"],
    "ষ": ["ʃ"],  # Bengali merges ṣ and ś into [ʃ]
    "স": ["s", "ʃ"],  # [s] before front vowels; [ʃ] elsewhere in some dialects

    # --- Aspirate ---
    "হ": ["h"],
}

ALLOPHONES_BN = {
    "p": ["p"], "pʰ": ["pʰ"],
    "b": ["b"], "bʱ": ["bʱ"],
    "t": ["t"], "tʰ": ["tʰ"],
    "d": ["d"], "dʱ": ["dʱ"],
    "ʈ": ["ʈ"], "ʈʰ": ["ʈʰ"],
    "ɖ": ["ɖ"], "ɖʱ": ["ɖʱ"],
    "k": ["k"], "kʰ": ["kʰ"],
    "ɡ": ["ɡ"], "ɡʱ": ["ɡʱ"],
    "tɕ": ["tɕ"], "tɕʰ": ["tɕʰ"],
    "dʑ": ["dʑ"], "dʑʱ": ["dʑʱ"],
    "m": ["m"], "n": ["n", "ŋ", "ɲ"],
    "ŋ": ["ŋ"],
    "ʃ": ["ʃ"], "s": ["s", "ʃ"],
    "h": ["h"],
    "r": ["r"], "ɽ": ["ɽ"],
    "l": ["l"],
    "j": ["j"], "w": ["w"],
    # Vowels: Bengali has /ɔ/ vs /a/ as key contrast
    "ɔ": ["ɔ", "o"],  # inherent vowel
    "a": ["a"],
    "i": ["i"], "u": ["u"],
    "e": ["e", "æ"],  # contextual realisation
    "o": ["o"],
}

# ══════════════════════════════════════════════════════════════════════════════
# Assamese — closely related to Bengali; different vowel system
# ══════════════════════════════════════════════════════════════════════════════
# Key differences from Bengali:
# - /w/ phonemic (from old /v/)
# - No retroflex sibilant /ʂ/ (merged with /x/)
# - Central vowel /ɘ/ (unique)
# - /x/ fricative phonemic

GRAPHEMES_AS = {
    **GRAPHEMES_BN,
    # Assamese-specific changes:
    "ৱ": ["w"],  # wa (unique Assamese letter)
    "ক্ষ": ["kʰ"],  # Assamese merger
    "ষ": ["x"],  # Assamese: ṣ → [x] not [ʃ]
    "স": ["x"],  # Assamese: sa → [x]
    "শ": ["x"],  # Assamese: śa → [x] (three sibilants merged)
    "অ": ["ɔ", "o"],
    "ও": ["u"],  # Assamese o → [u] in certain contexts
}

ALLOPHONES_AS = {
    **ALLOPHONES_BN,
    "x": ["x"],  # Assamese fricative from three Sanskrit sibilants
    "w": ["w"],
}

SPECS = {
    "bn": LanguageSpec(
        code="bn",
        name="Bengali",
        family="Indo-Aryan",
        script="Bengali",
        graphemes=GRAPHEMES_BN,
        allophones=ALLOPHONES_BN,
        parent="sa",
        ancestors=(
            Ancestor("sa", P, 0.80,
                     "Descent via Magadhi Apabhraṃśa through Middle Indo-Aryan"),
            Ancestor("hi", AD, 0.05,
                     "Contact with Hindi belt"),
        ),
        notes=(
            "Standard Bengali (Dhaka/Kolkata). Key features: "
            "inherent vowel is /ɔ/ (not /ə/ like Hindi); "
            "⟨য⟩ = [dʑ] word-initially, [j] elsewhere; "
            "⟨শ⟩ and ⟨ষ⟩ both → [ʃ] (two Sanskrit sibilants merged); "
            "dental/retroflex contrast maintained; "
            "breathy stops phonemic but weakening in Bangladesh speech."
        ),
    ),
    "as": LanguageSpec(
        code="as",
        name="Assamese",
        family="Indo-Aryan",
        script="Bengali",  # Assamese uses a modified Bengali script
        graphemes=GRAPHEMES_AS,
        allophones=ALLOPHONES_AS,
        parent="sa",
        ancestors=(
            Ancestor("sa", P, 0.80,
                     "Descent via Magadhi Apabhraṃśa"),
            Ancestor("bn", AD, 0.08,
                     "Close contact with Bengali"),
        ),
        notes=(
            "Standard Assamese. Diverges from Bengali in: "
            "all three Sanskrit sibilants (ś ṣ s) merge to /x/; "
            "/w/ phonemic (⟨ৱ⟩); central vowel shift. "
            "Uses Assamese variant of Bengali script."
        ),
    ),
}
