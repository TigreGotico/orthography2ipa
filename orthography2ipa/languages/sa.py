"""Sanskrit (sa) and Proto-Indo-Aryan (inc) — grapheme→IPA and allophone mappings.

Sources:
- Whitney, W.D. (1879). *Sanskrit Grammar*. Harvard UP.
- MacDonell, A.A. (1927). *A Sanskrit Grammar for Students* (3rd ed.). OUP.
- Allen, W.S. (1953). *Phonetics in Ancient India*. OUP.
- Cardona, G. (2003). 'Sanskrit' in Cardona & Jain (eds.), *The Indo-Aryan Languages*. Routledge.
- Misra, S.S. (1967). *The Old Indo-Aryan Language*. Varanasi.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
AD = AncestorRole.ADSTRATE

# ══════════════════════════════════════════════════════════════════════════════
# Classical Sanskrit — Devanagari script
# ══════════════════════════════════════════════════════════════════════════════

GRAPHEMES_SA = {
    # --- Independent vowels ---
    "अ": ["ə"],  # short a (schwa)
    "आ": ["aː"],  # long ā
    "इ": ["i"],  # short i
    "ई": ["iː"],  # long ī
    "उ": ["u"],  # short u
    "ऊ": ["uː"],  # long ū
    "ऋ": ["r̩"],  # vocalic r (syllabic)
    "ॠ": ["r̩ː"],  # long vocalic r
    "ऌ": ["l̩"],  # vocalic l (rare)
    "ए": ["eː"],  # long e (no short e in Sanskrit)
    "ऐ": ["əi"],  # ai diphthong
    "ओ": ["oː"],  # long o
    "औ": ["əu"],  # au diphthong

    # --- Vowel diacritics (mātrā) ---
    "ा": ["aː"], "ि": ["i"], "ी": ["iː"],
    "ु": ["u"], "ू": ["uː"], "ृ": ["r̩"],
    "ॄ": ["r̩ː"], "ॢ": ["l̩"],
    "े": ["eː"], "ै": ["əi"],
    "ो": ["oː"], "ौ": ["əu"],

    # --- Diacritics ---
    "ं": ["̃ŋ"],  # anusvāra: nasal assimilation
    "ः": ["h"],  # visarga: voiceless glottal fricative
    "ँ": ["̃"],  # candrabindu: nasalisation
    "्": [""],  # virāma (suppresses inherent schwa)

    # --- Velars (kaṇṭhya) ---
    "क": ["k"], "ख": ["kʰ"], "ग": ["ɡ"], "घ": ["ɡʱ"], "ङ": ["ŋ"],

    # --- Palatals (tālavya) —— Sanskrit: pure palatals ---
    "च": ["tɕ"], "छ": ["tɕʰ"], "ज": ["dʑ"], "झ": ["dʑʱ"], "ञ": ["ɲ"],

    # --- Retroflexes (mūrdhanya) ---
    "ट": ["ʈ"], "ठ": ["ʈʰ"], "ड": ["ɖ"], "ढ": ["ɖʱ"], "ण": ["ɳ"],

    # --- Dentals (dantya) ---
    "त": ["t̪"], "थ": ["t̪ʰ"], "द": ["d̪"], "ध": ["d̪ʱ"], "न": ["n̪"],

    # --- Labials (oṣṭhya) ---
    "प": ["p"], "फ": ["pʰ"], "ब": ["b"], "भ": ["bʱ"], "म": ["m"],

    # --- Semivowels (antastha) ---
    "य": ["j"], "र": ["r"], "ल": ["l"], "व": ["ʋ"],

    # --- Sibilants (ūṣman) ---
    "श": ["ɕ"],  # palatal sibilant
    "ष": ["ʂ"],  # retroflex sibilant
    "स": ["s"],  # dental sibilant

    # --- Aspirate ---
    "ह": ["ɦ"],  # voiced glottal fricative

    # --- Common conjuncts ---
    "क्ष": ["kʂ"],
    "ज्ञ": ["dʑɲ"],
    "त्र": ["t̪r"],
}

ALLOPHONES_SA = {
    # Stops: Sanskrit has no final devoicing (classical period)
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
    # Nasals: anusvāra assimilates to following stop
    "m": ["m"],
    "n̪": ["n̪", "n", "ŋ", "ɲ", "ɳ"],  # place assimilation
    "ɳ": ["ɳ"],
    "ɲ": ["ɲ"],
    "ŋ": ["ŋ"],
    # Fricatives
    "ɕ": ["ɕ"],
    "ʂ": ["ʂ"],
    "s": ["s"],
    "ɦ": ["ɦ"],
    "h": ["h"],  # visarga: context-dependent realisation
    # Liquids / glides
    "r": ["r"],
    "l": ["l"],
    "ʋ": ["ʋ", "w"],
    "j": ["j"],
    "r̩": ["r̩"],
    "l̩": ["l̩"],
    # Vowels
    "ə": ["ə"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "r̩ː": ["r̩ː"],
    "eː": ["eː"], "oː": ["oː"],
    "əi": ["əi"], "əu": ["əu"],
}

# ══════════════════════════════════════════════════════════════════════════════
# Vedic Sanskrit — slightly different, represents older stage
# ══════════════════════════════════════════════════════════════════════════════
# Vedic has pitch accent (udātta/anudātta/svarita) and slightly different phonology

GRAPHEMES_VEDIC = {
    **GRAPHEMES_SA,
    # Vedic has additional phoneme: voiced retroflex lateral ḷ
    "ळ": ["ɭ"],  # voiced retroflex lateral (Vedic)
    "ॾ": ["ɖ"],  # alternate form
}

ALLOPHONES_VEDIC = {
    **ALLOPHONES_SA,
    "ɭ": ["ɭ"],
}

# ══════════════════════════════════════════════════════════════════════════════
# Pali — Middle Indo-Aryan, canonical Buddhist language
# ══════════════════════════════════════════════════════════════════════════════
# Pali simplifies Sanskrit clusters and loses some distinctions

GRAPHEMES_PALI = {
    # --- Vowels ---
    "a": ["ə"], "ā": ["aː"],
    "i": ["i"], "ī": ["iː"],
    "u": ["u"], "ū": ["uː"],
    "e": ["eː"],
    "o": ["oː"],
    # --- Nasals ---
    "ṃ": ["̃ŋ"],  # niggahīta (anusvāra equivalent)
    # --- Stops ---
    "k": ["k"], "kh": ["kʰ"], "g": ["ɡ"], "gh": ["ɡʱ"], "ṅ": ["ŋ"],
    "c": ["tɕ"], "ch": ["tɕʰ"], "j": ["dʑ"], "jh": ["dʑʱ"], "ñ": ["ɲ"],
    "ṭ": ["ʈ"], "ṭh": ["ʈʰ"], "ḍ": ["ɖ"], "ḍh": ["ɖʱ"], "ṇ": ["ɳ"],
    "t": ["t̪"], "th": ["t̪ʰ"], "d": ["d̪"], "dh": ["d̪ʱ"], "n": ["n̪"],
    "p": ["p"], "ph": ["pʰ"], "b": ["b"], "bh": ["bʱ"], "m": ["m"],
    # --- Semivowels / liquids / fricatives ---
    "y": ["j"], "r": ["r"], "l": ["l"], "v": ["ʋ"],
    "s": ["s"], "h": ["ɦ"],
    "ḷ": ["ɭ"],  # retroflex l
}

ALLOPHONES_PALI = {
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
    "m": ["m"], "n̪": ["n̪", "ŋ", "ɲ", "ɳ"],
    "ɳ": ["ɳ"], "ɲ": ["ɲ"], "ŋ": ["ŋ"],
    "s": ["s"], "ɦ": ["ɦ"],
    "r": ["r"], "l": ["l"], "ɭ": ["ɭ"],
    "ʋ": ["ʋ", "w"], "j": ["j"],
    "ə": ["ə"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "eː": ["eː"], "oː": ["oː"],
}

SPECS = {
    "sa": LanguageSpec(
        code="sa",
        name="Sanskrit",
        family="Indo-Aryan",
        script="Devanagari",
        graphemes=GRAPHEMES_SA,
        allophones=ALLOPHONES_SA,
        parent="ine",
        ancestors=(
            Ancestor("ine", P, 0.95, "Direct descendant of Proto-Indo-European"),
        ),
        notes=(
            "Classical Sanskrit (Pāṇinian standard, c. 4th c. BCE onward). "
            "Five-point place-of-articulation system: velar, palatal, retroflex, "
            "dental, labial. Four-way laryngeal contrast (plain/aspirated × "
            "voiced/voiceless). No short /e/ or /o/ (only long). "
            "⟨व⟩ = [ʋ] labiodental approximant. Sandhi rules are extensive but "
            "modeled at the allophone level here."
        ),
    ),
    "sa-x-vedic": LanguageSpec(
        code="sa-x-vedic",
        name="Vedic Sanskrit",
        family="Indo-Aryan",
        script="Devanagari",
        graphemes=GRAPHEMES_VEDIC,
        allophones=ALLOPHONES_VEDIC,
        parent="ine",
        ancestors=(
            Ancestor("ine", P, 0.97, "Archaic direct descendant of PIE"),
        ),
        notes=(
            "Vedic Sanskrit (c. 1500–600 BCE), earlier than Classical Sanskrit. "
            "Retains pitch accent system (udātta/anudātta/svarita). "
            "Includes retroflex lateral ⟨ळ⟩ /ɭ/ lost in Classical Sanskrit. "
            "Source: Macdonell (1910), *Vedic Grammar*."
        ),
    ),
    "pi": LanguageSpec(
        code="pi",
        name="Pali",
        family="Indo-Aryan",
        script="Latin",  # romanization; also written in many scripts
        graphemes=GRAPHEMES_PALI,
        allophones=ALLOPHONES_PALI,
        parent="sa",
        ancestors=(
            Ancestor("sa", P, 0.85, "Middle IA descended from Vedic/Old IA"),
        ),
        notes=(
            "Pali — canonical language of Theravāda Buddhism (c. 3rd c. BCE). "
            "Middle Indo-Aryan: simplifies Sanskrit consonant clusters (geminates "
            "instead of heteroorganic clusters), loses distinction between "
            "palatal sibilant ⟨ś⟩ and retroflex ⟨ṣ⟩ (both → /s/). "
            "Romanisation follows PTS/Velthuis convention."
        ),
    ),
}
