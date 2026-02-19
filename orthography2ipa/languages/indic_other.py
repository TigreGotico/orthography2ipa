"""Konkani (kok), Sinhala (si), Bhojpuri (bho) — grapheme→IPA and allophone mappings.

Sources:
- Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
- Masica, C.P. (1991). *The Indo-Aryan Languages*. CUP.
- Subrahmanyam, P.S. (1977). *Dravidian Comparative Phonology*.
- Henadeerage, K. (2002). *Topics in Sinhala Phonology*. PhD thesis, ANU.
- Gair, J.W. (1998). *Studies in South Asian Linguistics*. OUP.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
AD = AncestorRole.ADSTRATE
SUB = AncestorRole.SUBSTRATE

# ══════════════════════════════════════════════════════════════════════════════
# Konkani — Goa/Karnataka/Kerala; multiple scripts in use
# ══════════════════════════════════════════════════════════════════════════════
# Phonologically close to Marathi but with Dravidian substrate influences.
# Uses Devanagari (official Goa), Kannada, Roman, and Perso-Arabic scripts.

GRAPHEMES_KOK = {
    # Independent vowels
    "अ": ["ə"], "आ": ["aː"],
    "इ": ["i"], "ई": ["iː"],
    "उ": ["u"], "ऊ": ["uː"],
    "ए": ["eː"], "ऐ": ["əi"],
    "ओ": ["oː"], "औ": ["əu"],

    # Vowel diacritics
    "ा": ["aː"], "ि": ["i"], "ी": ["iː"],
    "ु": ["u"], "ू": ["uː"],
    "े": ["eː"], "ै": ["əi"],
    "ो": ["oː"], "ौ": ["əu"],

    # Diacritics
    "ं": ["̃"], "ः": ["h"], "ँ": ["̃"], "्": [""],

    # Velars
    "क": ["k"], "ख": ["kʰ"], "ग": ["ɡ"], "घ": ["ɡʱ"], "ङ": ["ŋ"],

    # Palatals
    "च": ["tʃ"], "छ": ["tʃʰ"], "ज": ["dʒ"], "झ": ["dʒʱ"], "ञ": ["ɲ"],

    # Retroflexes
    "ट": ["ʈ"], "ठ": ["ʈʰ"], "ड": ["ɖ"], "ढ": ["ɖʱ"], "ण": ["ɳ"],

    # Dentals
    "त": ["t̪"], "थ": ["t̪ʰ"], "द": ["d̪"], "ध": ["d̪ʱ"], "न": ["n"],

    # Labials
    "प": ["p"], "फ": ["pʰ", "f"], "ब": ["b"], "भ": ["bʱ"], "म": ["m"],

    # Semivowels
    "य": ["j"], "र": ["r"], "ल": ["l"], "व": ["ʋ"],
    "ळ": ["ɭ"], "ड़": ["ɽ"],

    # Sibilants
    "श": ["ʃ"], "ष": ["ʂ"], "स": ["s"], "ह": ["ɦ"],
}

ALLOPHONES_KOK = {
    "p": ["p"], "pʰ": ["pʰ"], "b": ["b"], "bʱ": ["bʱ"],
    "t̪": ["t̪"], "t̪ʰ": ["t̪ʰ"], "d̪": ["d̪"], "d̪ʱ": ["d̪ʱ"],
    "ʈ": ["ʈ"], "ʈʰ": ["ʈʰ"], "ɖ": ["ɖ"], "ɖʱ": ["ɖʱ"],
    "k": ["k"], "kʰ": ["kʰ"], "ɡ": ["ɡ"], "ɡʱ": ["ɡʱ"],
    "tʃ": ["tʃ"], "tʃʰ": ["tʃʰ"], "dʒ": ["dʒ"], "dʒʱ": ["dʒʱ"],
    "m": ["m"], "n": ["n"], "ɲ": ["ɲ"], "ɳ": ["ɳ"], "ŋ": ["ŋ"],
    "ʃ": ["ʃ"], "ʂ": ["ʂ"], "s": ["s"], "ɦ": ["ɦ"],
    "r": ["r"], "ɽ": ["ɽ"], "l": ["l"], "ɭ": ["ɭ"],
    "ʋ": ["ʋ"], "j": ["j"],
    "ə": ["ə"], "aː": ["aː"], "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"], "eː": ["eː"], "oː": ["oː"],
}

# ══════════════════════════════════════════════════════════════════════════════
# Sinhala — Sri Lanka; Sinhala script (Sinhalese script, Brahmic)
# ══════════════════════════════════════════════════════════════════════════════
# Distinct from other IA in: prenasalised stops /ᵐb ⁿd ⁿɖ ᵑɡ/;
# distinction between oral and prenasalised; aspirates reduced in colloquial.

GRAPHEMES_SI = {
    # --- Independent vowels ---
    "අ": ["ə"], "ආ": ["aː"],
    "ඇ": ["æ"], "ඈ": ["æː"],  # open front vowels (unique in IA)
    "ඉ": ["i"], "ඊ": ["iː"],
    "උ": ["u"], "ඌ": ["uː"],
    "එ": ["e"], "ඒ": ["eː"],
    "ඔ": ["o"], "ඕ": ["oː"],
    "ඖ": ["ou"],

    # --- Vowel diacritics ---
    "ා": ["aː"], "ැ": ["æ"], "ෑ": ["æː"],
    "ි": ["i"], "ී": ["iː"],
    "ු": ["u"], "ූ": ["uː"],
    "ෙ": ["e"], "ේ": ["eː"],
    "ො": ["o"], "ෝ": ["oː"],
    "ෞ": ["ou"],
    "ං": ["ŋ"],  # anusvāra → /ŋ/
    "ඃ": ["h"],  # visarga
    "්": [""],  # hal kirīma (virāma)

    # --- Velars ---
    "ක": ["k"], "ඛ": ["kʰ"], "ග": ["ɡ"], "ඝ": ["ɡʱ"], "ඞ": ["ŋ"],
    # Prenasalised
    "ඟ": ["ᵑɡ"],  # prenasalised velar

    # --- Palatals ---
    "ච": ["tʃ"], "ඡ": ["tʃʰ"], "ජ": ["dʒ"], "ඣ": ["dʒʱ"], "ඤ": ["ɲ"],
    "ඦ": ["ⁿdʒ"],  # prenasalised palatal affricate

    # --- Retroflexes ---
    "ට": ["ʈ"], "ඨ": ["ʈʰ"], "ඩ": ["ɖ"], "ඪ": ["ɖʱ"], "ණ": ["ɳ"],
    "ඬ": ["ⁿɖ"],  # prenasalised retroflex

    # --- Dentals ---
    "ත": ["t"], "ථ": ["tʰ"], "ද": ["d"], "ධ": ["dʱ"], "න": ["n"],
    "ඳ": ["ⁿd"],  # prenasalised dental

    # --- Labials ---
    "ප": ["p"], "ඵ": ["pʰ"], "බ": ["b"], "භ": ["bʱ"], "ම": ["m"],
    "ඹ": ["ᵐb"],  # prenasalised bilabial

    # --- Semivowels / liquids ---
    "ය": ["j"],
    "ර": ["r"],
    "ල": ["l"],
    "ළ": ["ɭ"],  # retroflex lateral
    "ව": ["ʋ"],

    # --- Sibilant / aspirate ---
    "ශ": ["ʃ"],
    "ෂ": ["ʂ"],
    "ස": ["s"],
    "හ": ["h"],

    # --- Unique Sinhala letters ---
    "ෆ": ["f"],  # fa (loans)
}

ALLOPHONES_SI = {
    "p": ["p"], "pʰ": ["pʰ"],
    "b": ["b"], "bʱ": ["bʱ"], "ᵐb": ["ᵐb"],
    "t": ["t"], "tʰ": ["tʰ"],
    "d": ["d"], "dʱ": ["dʱ"], "ⁿd": ["ⁿd"],
    "ʈ": ["ʈ"], "ʈʰ": ["ʈʰ"],
    "ɖ": ["ɖ"], "ɖʱ": ["ɖʱ"], "ⁿɖ": ["ⁿɖ"],
    "k": ["k"], "kʰ": ["kʰ"],
    "ɡ": ["ɡ"], "ɡʱ": ["ɡʱ"], "ᵑɡ": ["ᵑɡ"],
    "tʃ": ["tʃ"], "tʃʰ": ["tʃʰ"],
    "dʒ": ["dʒ"], "dʒʱ": ["dʒʱ"], "ⁿdʒ": ["ⁿdʒ"],
    "m": ["m"], "n": ["n"], "ɲ": ["ɲ"], "ɳ": ["ɳ"], "ŋ": ["ŋ"],
    "ʃ": ["ʃ"], "ʂ": ["ʂ"], "s": ["s"],
    "h": ["h"], "f": ["f"],
    "r": ["r"], "l": ["l"], "ɭ": ["ɭ"],
    "ʋ": ["ʋ", "w"], "j": ["j"],
    "ə": ["ə"], "aː": ["aː"],
    "æ": ["æ"], "æː": ["æː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "e": ["e"], "eː": ["eː"],
    "o": ["o"], "oː": ["oː"],
}

# ══════════════════════════════════════════════════════════════════════════════
# Bhojpuri — Eastern Uttar Pradesh / Bihar; Devanagari
# ══════════════════════════════════════════════════════════════════════════════

GRAPHEMES_BHO = {
    # Phonologically close to Hindi but distinct in vowel system (no schwa deletion)
    "अ": ["a"], "आ": ["aː"],  # Bhojpuri: inherent vowel = [a], not [ə]
    "इ": ["i"], "ई": ["iː"],
    "उ": ["u"], "ऊ": ["uː"],
    "ए": ["eː"], "ऐ": ["æː"],
    "ओ": ["oː"], "औ": ["ɔː"],

    "ा": ["aː"], "ि": ["i"], "ी": ["iː"],
    "ु": ["u"], "ू": ["uː"],
    "े": ["eː"], "ै": ["æː"],
    "ो": ["oː"], "ौ": ["ɔː"],

    "ं": ["̃"], "ः": ["h"], "ँ": ["̃"], "्": [""],

    "क": ["k"], "ख": ["kʰ"], "ग": ["ɡ"], "घ": ["ɡʱ"], "ङ": ["ŋ"],
    "च": ["tʃ"], "छ": ["tʃʰ"], "ज": ["dʒ"], "झ": ["dʒʱ"], "ञ": ["ɲ"],
    "ट": ["ʈ"], "ठ": ["ʈʰ"], "ड": ["ɖ"], "ढ": ["ɖʱ"], "ण": ["ɳ"],
    "त": ["t̪"], "थ": ["t̪ʰ"], "द": ["d̪"], "ध": ["d̪ʱ"], "न": ["n"],
    "प": ["p"], "फ": ["pʰ"], "ब": ["b"], "भ": ["bʱ"], "म": ["m"],
    "य": ["j"], "र": ["r"], "ल": ["l"], "व": ["ʋ"],
    "ड़": ["ɽ"], "ढ़": ["ɽʱ"],
    "श": ["ʃ"], "ष": ["ʂ"], "स": ["s"], "ह": ["ɦ"],
}

ALLOPHONES_BHO = {
    "p": ["p"], "pʰ": ["pʰ"], "b": ["b"], "bʱ": ["bʱ"],
    "t̪": ["t̪"], "t̪ʰ": ["t̪ʰ"], "d̪": ["d̪"], "d̪ʱ": ["d̪ʱ"],
    "ʈ": ["ʈ"], "ʈʰ": ["ʈʰ"], "ɖ": ["ɖ"], "ɖʱ": ["ɖʱ"],
    "k": ["k"], "kʰ": ["kʰ"], "ɡ": ["ɡ"], "ɡʱ": ["ɡʱ"],
    "tʃ": ["tʃ"], "tʃʰ": ["tʃʰ"], "dʒ": ["dʒ"], "dʒʱ": ["dʒʱ"],
    "m": ["m"], "n": ["n"], "ɲ": ["ɲ"], "ɳ": ["ɳ"],
    "ʃ": ["ʃ"], "ʂ": ["ʂ"], "s": ["s"], "ɦ": ["ɦ"],
    "r": ["r"], "ɽ": ["ɽ"], "l": ["l"],
    "ʋ": ["ʋ"], "j": ["j"],
    "a": ["a"], "aː": ["aː"], "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"], "eː": ["eː"], "oː": ["oː"],
}

SPECS = {
    "kok": LanguageSpec(
        code="kok",
        name="Konkani",
        family="Indo-Aryan",
        script="Devanagari",
        graphemes=GRAPHEMES_KOK,
        allophones=ALLOPHONES_KOK,
        parent="sa",
        ancestors=(
            Ancestor("sa", P, 0.78,
                     "Descent via Shauraseni / Maharashtri Apabhraṃśa"),
            Ancestor("mr", AD, 0.10,
                     "Strong Marathi adstrate influence"),
            Ancestor("ta", SUB, 0.05,
                     "Dravidian substrate from pre-IA population of Goa"),
        ),
        notes=(
            "Konkani, 22nd scheduled language of India (1992). "
            "Spoken in Goa (official), Karnataka, and Kerala. "
            "Multiple scripts: Devanagari (official Goa), Kannada, Roman. "
            "Strong Dravidian substrate features: retroflex ⟨ळ⟩ = [ɭ]. "
            "Close to Marathi but considered separate language by speakers."
        ),
    ),
    "si": LanguageSpec(
        code="si",
        name="Sinhala",
        family="Indo-Aryan",
        script="Sinhala",
        graphemes=GRAPHEMES_SI,
        allophones=ALLOPHONES_SI,
        parent="sa",
        ancestors=(
            Ancestor("sa", P, 0.75,
                     "Descent via Sinhala Prakrit; migrated to Sri Lanka c. 5th c. BCE"),
            Ancestor("ta", SUB, 0.12,
                     "Tamil substrate: long contact on Sri Lanka"),
            Ancestor("pa", AD, 0.05,
                     "Pali: Buddhist religious language influence"),
        ),
        notes=(
            "Sinhala (Sri Lanka). Typologically diverges from mainland IA: "
            "prenasalised stops /ᵐb ⁿd ⁿɖ ᵑɡ ⁿdʒ/ are phonemic (rare in IA); "
            "vowels /æ æː/ absent in most other IA languages; "
            "dental stops /t d/ distinct from retroflex /ʈ ɖ/ (no dental diacritic). "
            "Diglossia: formal (literary) vs. colloquial speech differ markedly."
        ),
    ),
    "bho": LanguageSpec(
        code="bho",
        name="Bhojpuri",
        family="Indo-Aryan",
        script="Devanagari",
        graphemes=GRAPHEMES_BHO,
        allophones=ALLOPHONES_BHO,
        parent="hi",
        ancestors=(
            Ancestor("hi", P, 0.82,
                     "Closely related Hindi dialect group; Eastern Hindi"),
            Ancestor("mai", AD, 0.08,
                     "Maithili adstrate in Bihar zone"),
        ),
        notes=(
            "Bhojpuri (Eastern UP and Bihar). Largest Indic diaspora language. "
            "Inherent vowel is /a/ (not /ə/ like Standard Hindi). "
            "No schwa deletion rule. "
            "Four-way laryngeal contrast. Retroflex series phonemic."
        ),
    ),
}
