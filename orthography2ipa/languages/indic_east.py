"""Odia (or), Maithili (mai), Sindhi (sd), Kashmiri (ks) — grapheme→IPA and allophone mappings.

Sources:
- Masica, C.P. (1991). *The Indo-Aryan Languages*. CUP.
- Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
- Neukom, L. (1995). *Sindhi*. LINCOM Europa.
- Hook, P.E. (2003). 'Kashmiri'. In Cardona & Jain (eds.).
- Grierson, G.A. (1905). *Linguistic Survey of India*, Vol. V–VIII.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
AD = AncestorRole.ADSTRATE
SUB = AncestorRole.SUBSTRATE

# ══════════════════════════════════════════════════════════════════════════════
# Odia (Oriya) — Odisha; Odia script
# ══════════════════════════════════════════════════════════════════════════════

GRAPHEMES_OR = {
    # --- Independent vowels ---
    "ଅ": ["ɔ"], "ଆ": ["aː"],
    "ଇ": ["i"], "ଈ": ["iː"],
    "ଉ": ["u"], "ଊ": ["uː"],
    "ଋ": ["r̩"],
    "ଏ": ["e"], "ଐ": ["oi"],
    "ଓ": ["o"], "ଔ": ["ou"],

    # --- Vowel diacritics ---
    "ା": ["aː"], "ି": ["i"], "ୀ": ["iː"],
    "ୁ": ["u"], "ୂ": ["uː"], "ୃ": ["r̩"],
    "େ": ["e"], "ୈ": ["oi"],
    "ୋ": ["o"], "ୌ": ["ou"],

    # --- Diacritics ---
    "ଂ": ["̃"], "ଃ": ["h"], "ଁ": ["̃"], "୍": [""],

    # --- Velars ---
    "କ": ["k"], "ଖ": ["kʰ"], "ଗ": ["ɡ"], "ଘ": ["ɡʱ"], "ଙ": ["ŋ"],

    # --- Palatals ---
    "ଚ": ["tɕ"], "ଛ": ["tɕʰ"], "ଜ": ["dʑ"], "ଝ": ["dʑʱ"], "ଞ": ["ɲ"],

    # --- Retroflexes ---
    "ଟ": ["ʈ"], "ଠ": ["ʈʰ"], "ଡ": ["ɖ"], "ଢ": ["ɖʱ"], "ଣ": ["ɳ"],

    # --- Dentals ---
    "ତ": ["t̪"], "ଥ": ["t̪ʰ"], "ଦ": ["d̪"], "ଧ": ["d̪ʱ"], "ନ": ["n"],

    # --- Labials ---
    "ପ": ["p"], "ଫ": ["pʰ"], "ବ": ["b"], "ଭ": ["bʱ"], "ମ": ["m"],

    # --- Semivowels / liquids ---
    "ଯ": ["dʑ", "j"], "ୟ": ["j"],
    "ର": ["r"], "ଡ଼": ["ɽ"],
    "ଳ": ["ɭ"], "ଲ": ["l"],
    "ୱ": ["w"], "ବ": ["b", "ʋ"],

    # --- Sibilants / aspirate ---
    "ଶ": ["ʃ"], "ଷ": ["ʂ"], "ସ": ["s"], "ହ": ["ɦ"],
}

ALLOPHONES_OR = {
    "p": ["p"], "pʰ": ["pʰ"],
    "b": ["b"], "bʱ": ["bʱ"],
    "t̪": ["t̪"], "t̪ʰ": ["t̪ʰ"],
    "d̪": ["d̪"], "d̪ʱ": ["d̪ʱ"],
    "ʈ": ["ʈ"], "ʈʰ": ["ʈʰ"],
    "ɖ": ["ɖ"], "ɖʱ": ["ɖʱ"],
    "k": ["k"], "kʰ": ["kʰ"],
    "ɡ": ["ɡ"], "ɡʱ": ["ɡʱ"],
    "tɕ": ["tɕ"], "tɕʰ": ["tɕʰ"],
    "dʑ": ["dʑ"], "dʑʱ": ["dʑʱ"],
    "m": ["m"], "n": ["n", "ɳ", "ŋ"],
    "ʃ": ["ʃ"], "ʂ": ["ʂ"], "s": ["s"],
    "ɦ": ["ɦ", "h"],
    "r": ["r"], "ɽ": ["ɽ"],
    "l": ["l"], "ɭ": ["ɭ"],
    "ʋ": ["ʋ", "w"], "j": ["j"],
    "ɔ": ["ɔ"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "e": ["e"], "o": ["o"],
}

# ══════════════════════════════════════════════════════════════════════════════
# Maithili — Bihar/Nepal; Devanagari + Tirhuta script
# ══════════════════════════════════════════════════════════════════════════════

GRAPHEMES_MAI = {
    # Maithili uses Devanagari (official) and traditional Tirhuta script.
    # Phonology close to Bengali but with some distinct features.
    # --- Independent vowels ---
    "अ": ["ə"], "आ": ["aː"],
    "इ": ["i"], "ई": ["iː"],
    "उ": ["u"], "ऊ": ["uː"],
    "ए": ["e"], "ऐ": ["əi"],
    "ओ": ["o"], "औ": ["əu"],

    # --- Vowel diacritics ---
    "ा": ["aː"], "ि": ["i"], "ी": ["iː"],
    "ु": ["u"], "ू": ["uː"],
    "े": ["e"], "ै": ["əi"],
    "ो": ["o"], "ौ": ["əu"],

    # --- Diacritics ---
    "ं": ["̃"], "ः": ["h"], "ँ": ["̃"], "्": [""],

    # --- Velars ---
    "क": ["k"], "ख": ["kʰ"], "ग": ["ɡ"], "घ": ["ɡʱ"], "ङ": ["ŋ"],

    # --- Palatals ---
    "च": ["tɕ"], "छ": ["tɕʰ"], "ज": ["dʑ"], "झ": ["dʑʱ"], "ञ": ["ɲ"],

    # --- Retroflexes ---
    "ट": ["ʈ"], "ठ": ["ʈʰ"], "ड": ["ɖ"], "ढ": ["ɖʱ"], "ण": ["ɳ"],

    # --- Dentals ---
    "त": ["t̪"], "थ": ["t̪ʰ"], "द": ["d̪"], "ध": ["d̪ʱ"], "न": ["n"],

    # --- Labials ---
    "प": ["p"], "फ": ["pʰ"], "ब": ["b"], "भ": ["bʱ"], "म": ["m"],

    # --- Semivowels / liquids ---
    "य": ["j"], "र": ["r"], "ल": ["l"], "व": ["ʋ"],
    "ड़": ["ɽ"],

    # --- Sibilants ---
    "श": ["ʃ"], "ष": ["ʂ"], "स": ["s"], "ह": ["ɦ"],
}

ALLOPHONES_MAI = {
    "p": ["p"], "pʰ": ["pʰ"], "b": ["b"], "bʱ": ["bʱ"],
    "t̪": ["t̪"], "t̪ʰ": ["t̪ʰ"], "d̪": ["d̪"], "d̪ʱ": ["d̪ʱ"],
    "ʈ": ["ʈ"], "ʈʰ": ["ʈʰ"], "ɖ": ["ɖ"], "ɖʱ": ["ɖʱ"],
    "k": ["k"], "kʰ": ["kʰ"], "ɡ": ["ɡ"], "ɡʱ": ["ɡʱ"],
    "tɕ": ["tɕ"], "tɕʰ": ["tɕʰ"], "dʑ": ["dʑ"], "dʑʱ": ["dʑʱ"],
    "m": ["m"], "n": ["n"], "ɲ": ["ɲ"], "ɳ": ["ɳ"], "ŋ": ["ŋ"],
    "s": ["s"], "ʃ": ["ʃ"], "ʂ": ["ʂ"], "ɦ": ["ɦ"],
    "r": ["r"], "ɽ": ["ɽ"], "l": ["l"], "ʋ": ["ʋ"], "j": ["j"],
    "ə": ["ə"], "aː": ["aː"], "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"], "e": ["e"], "o": ["o"],
}

# ══════════════════════════════════════════════════════════════════════════════
# Sindhi — Pakistan/India; Perso-Arabic (official) and Devanagari scripts
# ══════════════════════════════════════════════════════════════════════════════
# Remarkable features: implosives /ɓ ɗ ʄ ɠ/ (rare in IA); retroflex series.

GRAPHEMES_SD = {
    # Romanisation following Grierson/standard Sindhi phonemic transcription
    # Independent vowels
    "a": ["a"], "ā": ["aː"],
    "i": ["i"], "ī": ["iː"],
    "u": ["u"], "ū": ["uː"],
    "e": ["eː"], "o": ["oː"],
    "ai": ["əi"], "au": ["əu"],

    # Velars
    "k": ["k"], "kh": ["kʰ"], "g": ["ɡ"], "gh": ["ɡʱ"],
    "ḡ": ["ɠ"],  # velar implosive (unique Sindhi feature)

    # Palatals
    "c": ["tɕ"], "ch": ["tɕʰ"], "j": ["dʑ"], "jh": ["dʑʱ"],
    "ǰ": ["ʄ"],  # palatal implosive

    # Retroflexes
    "ṭ": ["ʈ"], "ṭh": ["ʈʰ"], "ḍ": ["ɖ"], "ḍh": ["ɖʱ"],
    "ḍ̈": ["ɗ"],  # retroflex implosive (archaic symbol; see notes)

    # Dentals
    "t": ["t̪"], "th": ["t̪ʰ"], "d": ["d̪"], "dh": ["d̪ʱ"],
    "b̈": ["ɓ"],  # bilabial implosive (often written ƀ)

    # Labials
    "p": ["p"], "ph": ["pʰ"], "b": ["b"], "bh": ["bʱ"], "m": ["m"],

    # Semivowels / liquids
    "y": ["j"], "r": ["r"], "l": ["l"], "v": ["ʋ"],
    "ṛ": ["ɽ"],  # retroflex flap

    # Sibilants / aspirate
    "ś": ["ʃ"], "ṣ": ["ʂ"], "s": ["s"],
    "z": ["z"], "h": ["ɦ"],
    "x": ["x"], "ġ": ["ɣ"], "f": ["f"], "q": ["q"],
}

ALLOPHONES_SD = {
    "p": ["p"], "pʰ": ["pʰ"],
    "b": ["b"], "bʱ": ["bʱ"], "ɓ": ["ɓ"],  # bilabial implosive
    "t̪": ["t̪"], "t̪ʰ": ["t̪ʰ"],
    "d̪": ["d̪"], "d̪ʱ": ["d̪ʱ"],
    "ʈ": ["ʈ"], "ʈʰ": ["ʈʰ"],
    "ɖ": ["ɖ"], "ɖʱ": ["ɖʱ"], "ɗ": ["ɗ"],  # retroflex implosive
    "k": ["k"], "kʰ": ["kʰ"],
    "ɡ": ["ɡ"], "ɡʱ": ["ɡʱ"], "ɠ": ["ɠ"],  # velar implosive
    "tɕ": ["tɕ"], "tɕʰ": ["tɕʰ"],
    "dʑ": ["dʑ"], "dʑʱ": ["dʑʱ"], "ʄ": ["ʄ"],  # palatal implosive
    "m": ["m"], "n": ["n", "ɳ", "ŋ"],
    "ʃ": ["ʃ"], "ʂ": ["ʂ"], "s": ["s"], "z": ["z"],
    "x": ["x"], "ɣ": ["ɣ"], "f": ["f"], "q": ["q"],
    "ɦ": ["ɦ", "h"],
    "r": ["r"], "ɽ": ["ɽ"],
    "l": ["l"],
    "ʋ": ["ʋ", "w"], "j": ["j"],
    "a": ["a"], "aː": ["aː"], "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"], "eː": ["eː"], "oː": ["oː"],
}

# ══════════════════════════════════════════════════════════════════════════════
# Kashmiri — Jammu & Kashmir; Sharada, Perso-Arabic (Nastaliq), Devanagari
# ══════════════════════════════════════════════════════════════════════════════
# Dardic branch; tone/pitch accent; unusual vowel system with /ə̃/ nasal schwa.

GRAPHEMES_KS = {
    # Romanisation following Grierson/Kachru convention
    # --- Vowels (Kashmiri has a rich vowel inventory) ---
    "a": ["a"], "ā": ["aː"],
    "i": ["i"], "ī": ["iː"],
    "u": ["u"], "ū": ["uː"],
    "e": ["eː"], "ē": ["eː"],
    "o": ["oː"], "ō": ["oː"],
    "ə": ["ə"], "ə̄": ["əː"],
    "ä": ["æ"], "ö": ["ø"],  # front rounded (loanwords / specific dialects)
    # Nasal vowels
    "ã": ["ã"], "ĩ": ["ĩ"], "ũ": ["ũ"],

    # --- Velars ---
    "k": ["k"], "kh": ["kʰ"], "g": ["ɡ"], "gh": ["ɡʱ"],
    "x": ["x"], "ġ": ["ɣ"],

    # --- Palatals ---
    "c": ["tʃ"], "ch": ["tʃʰ"], "j": ["dʒ"], "jh": ["dʒʱ"],

    # --- Retroflexes ---
    "ṭ": ["ʈ"], "ṭh": ["ʈʰ"], "ḍ": ["ɖ"], "ḍh": ["ɖʱ"],

    # --- Dentals ---
    "t": ["t̪"], "th": ["t̪ʰ"], "d": ["d̪"], "dh": ["d̪ʱ"],

    # --- Labials ---
    "p": ["p"], "ph": ["pʰ"], "b": ["b"], "bh": ["bʱ"], "m": ["m"],

    # --- Semivowels / liquids ---
    "y": ["j"], "r": ["r"], "l": ["l"], "v": ["ʋ"],
    "ṛ": ["ɽ"],

    # --- Sibilants / aspirate ---
    "ś": ["ɕ"], "ṣ": ["ʂ"], "s": ["s"], "z": ["z"],
    "h": ["h"],

    # --- Nasals ---
    "n": ["n"], "ṇ": ["ɳ"], "ñ": ["ɲ"], "ṅ": ["ŋ"], "m": ["m"],
}

ALLOPHONES_KS = {
    "p": ["p"], "pʰ": ["pʰ"], "b": ["b"], "bʱ": ["bʱ"],
    "t̪": ["t̪"], "t̪ʰ": ["t̪ʰ"], "d̪": ["d̪"], "d̪ʱ": ["d̪ʱ"],
    "ʈ": ["ʈ"], "ʈʰ": ["ʈʰ"], "ɖ": ["ɖ"], "ɖʱ": ["ɖʱ"],
    "k": ["k"], "kʰ": ["kʰ"], "ɡ": ["ɡ"], "ɡʱ": ["ɡʱ"],
    "tʃ": ["tʃ"], "tʃʰ": ["tʃʰ"], "dʒ": ["dʒ"], "dʒʱ": ["dʒʱ"],
    "x": ["x"], "ɣ": ["ɣ"],
    "m": ["m"], "n": ["n"], "ɲ": ["ɲ"], "ɳ": ["ɳ"], "ŋ": ["ŋ"],
    "ɕ": ["ɕ"], "ʂ": ["ʂ"], "s": ["s"], "z": ["z"],
    "h": ["h"],
    "r": ["r"], "ɽ": ["ɽ"], "l": ["l"],
    "ʋ": ["ʋ"], "j": ["j"],
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "eː": ["eː"], "oː": ["oː"],
    "ə": ["ə"], "əː": ["əː"],
    "ã": ["ã"], "ĩ": ["ĩ"], "ũ": ["ũ"],
}

SPECS = {
    "or": LanguageSpec(
        code="or",
        name="Odia",
        family="Indo-Aryan",
        script="Odia",
        graphemes=GRAPHEMES_OR,
        allophones=ALLOPHONES_OR,
        parent="sa",
        ancestors=(
            Ancestor("sa", P, 0.82,
                     "Descent via Ardha-Māgadhī Apabhraṃśa"),
        ),
        notes=(
            "Standard Odia (Odisha). Distinct Odia script. "
            "Inherent vowel is /ɔ/ (like Bengali). "
            "Retroflex lateral ⟨ଳ⟩ = [ɭ] phonemic. "
            "Four-way laryngeal contrast."
        ),
    ),
    "mai": LanguageSpec(
        code="mai",
        name="Maithili",
        family="Indo-Aryan",
        script="Devanagari",
        graphemes=GRAPHEMES_MAI,
        allophones=ALLOPHONES_MAI,
        parent="sa",
        ancestors=(
            Ancestor("sa", P, 0.82,
                     "Descent via Magadhi/Ardha-Māgadhī"),
        ),
        notes=(
            "Standard Maithili (Bihar / Nepal Terai). "
            "One of 22 scheduled languages of India (added 2003). "
            "Traditional Tirhuta script; Devanagari used officially. "
            "Phonologically close to Bengali and Nepali."
        ),
    ),
    "sd": LanguageSpec(
        code="sd",
        name="Sindhi",
        family="Indo-Aryan",
        script="Arabic",  # Perso-Arabic (primary in Pakistan)
        graphemes=GRAPHEMES_SD,
        allophones=ALLOPHONES_SD,
        parent="sa",
        ancestors=(
            Ancestor("sa", P, 0.78,
                     "Descent via Vrāchada Apabhraṃśa / Old Sindhi"),
            Ancestor("ar", AD, 0.12,
                     "Arabic adstrate: religious vocabulary, phonemes /q x/"),
            Ancestor("fa", AD, 0.07,
                     "Persian adstrate through Islamic cultural sphere"),
        ),
        notes=(
            "Standard Sindhi (Pakistan/India). "
            "Typologically remarkable: four implosives /ɓ ɗ ʄ ɠ/ — "
            "rare in Indo-Aryan. "
            "Full four-way laryngeal contrast plus implosives. "
            "Written in Perso-Arabic (Pakistan), Devanagari (India), "
            "and the Khudabadi script (traditional)."
        ),
    ),
    "ks": LanguageSpec(
        code="ks",
        name="Kashmiri",
        family="Indo-Aryan",
        script="Arabic",  # Nastaliq (official); also Sharada and Devanagari
        graphemes=GRAPHEMES_KS,
        allophones=ALLOPHONES_KS,
        parent="sa",
        ancestors=(
            Ancestor("sa", P, 0.75,
                     "Dardic branch of Indo-Aryan; pre-Proto-IA substratum"),
            Ancestor("ar", AD, 0.10,
                     "Arabic adstrate: religious vocabulary"),
            Ancestor("fa", AD, 0.10,
                     "Persian adstrate: heavy cultural/literary influence"),
        ),
        notes=(
            "Kashmiri (Kāśmīrī), a Dardic language of Jammu & Kashmir. "
            "Rich vowel inventory including front rounded and central vowels. "
            "Tonal/pitch-accent distinctions reported in some analyses. "
            "Three scripts: Sharada (ancient), Nastaliq (modern official), "
            "Devanagari (India official). "
            "Retroflex, dental, palatal, and velar distinctions maintained."
        ),
    ),
}
