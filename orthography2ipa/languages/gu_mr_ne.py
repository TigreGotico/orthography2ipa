"""Gujarati (gu), Marathi (mr), and Nepali (ne) — grapheme→IPA and allophone mappings.

Sources:
- Mistry, P.J. (1997). 'Gujarati writing'. In Bright, W. (ed.), *The World's Writing Systems*.
- Masica, C.P. (1991). *The Indo-Aryan Languages*. CUP.
- Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
- Naik, P. (2003). 'Marathi'. In Cardona & Jain (eds.).
- Pokharel, M.P. (2001). *Nepali Swarsastra*. Ratna Pustak Bhandar.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
AD = AncestorRole.ADSTRATE
SUB = AncestorRole.SUBSTRATE

# ══════════════════════════════════════════════════════════════════════════════
# Gujarati — Devanagari-derived Gujarati script
# ══════════════════════════════════════════════════════════════════════════════

GRAPHEMES_GU = {
    # --- Independent vowels ---
    "અ": ["ə"], "આ": ["aː"],
    "ઇ": ["i"], "ઈ": ["iː"],
    "ઉ": ["u"], "ઊ": ["uː"],
    "ઋ": ["ri"],
    "એ": ["e"], "ઐ": ["əi"],
    "ઓ": ["o"], "ઔ": ["əu"],

    # --- Vowel diacritics ---
    "ા": ["aː"], "િ": ["i"], "ી": ["iː"],
    "ુ": ["u"], "ૂ": ["uː"], "ૃ": ["ri"],
    "ે": ["e"], "ૈ": ["əi"],
    "ો": ["o"], "ૌ": ["əu"],

    # --- Diacritics ---
    "ં": ["̃"],  # anusvāra
    "ઃ": ["h"],  # visarga
    "ઁ": ["̃"],
    "્": [""],  # virāma

    # --- Velars ---
    "ક": ["k"], "ખ": ["kʰ"], "ગ": ["ɡ"], "ઘ": ["ɡʱ"], "ઙ": ["ŋ"],

    # --- Palatals ---
    "ચ": ["tɕ"], "છ": ["tɕʰ"], "જ": ["dʑ"], "ઝ": ["dʑʱ"], "ઞ": ["ɲ"],

    # --- Retroflexes ---
    "ટ": ["ʈ"], "ઠ": ["ʈʰ"], "ડ": ["ɖ"], "ઢ": ["ɖʱ"], "ણ": ["ɳ"],

    # --- Dentals ---
    "ત": ["t̪"], "થ": ["t̪ʰ"], "દ": ["d̪"], "ધ": ["d̪ʱ"], "ન": ["n"],

    # --- Labials ---
    "પ": ["p"], "ફ": ["pʰ", "f"], "બ": ["b"], "ભ": ["bʱ"], "મ": ["m"],

    # --- Semivowels / liquids ---
    "ય": ["j"],
    "ર": ["r"],
    "ળ": ["ɭ"],  # retroflex lateral (distinct grapheme in Gujarati)
    "ળ": ["ɭ"],
    "લ": ["l"],
    "વ": ["ʋ"],
    "ઋ": ["r̩"],

    # --- Sibilants ---
    "શ": ["ʃ"],
    "ષ": ["ʂ"],
    "સ": ["s"],
    "હ": ["ɦ"],

    # --- Nukta (loans) ---
    "ઝ઼": ["z"], "ફ઼": ["f"],
}

ALLOPHONES_GU = {
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
    "ɲ": ["ɲ"], "ɳ": ["ɳ"],
    "ʃ": ["ʃ"], "ʂ": ["ʂ"], "s": ["s"],
    "ɦ": ["ɦ", "h"],
    "r": ["r"], "ɭ": ["ɭ"],
    "l": ["l"],
    "ʋ": ["ʋ", "w"], "j": ["j"],
    "ə": ["ə"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "e": ["e"], "o": ["o"],
    "əi": ["əi"], "əu": ["əu"],
}

# ══════════════════════════════════════════════════════════════════════════════
# Marathi — Maharashtra; Devanagari script
# ══════════════════════════════════════════════════════════════════════════════
# Key features: dental/retroflex contrast; ⟨ळ⟩ = [ɭ] phonemic;
# nasal vowels; /ɛ ɔ/ as distinct phonemes.

GRAPHEMES_MR = {
    # --- Independent vowels ---
    "अ": ["ə"], "आ": ["aː"],
    "इ": ["i"], "ई": ["iː"],
    "उ": ["u"], "ऊ": ["uː"],
    "ऋ": ["r̩"],
    "ए": ["eː"], "ऐ": ["əi"],
    "ओ": ["oː"], "औ": ["əu"],
    "ऍ": ["ɛ"],  # Marathi-specific: open e
    "ऑ": ["ɔ"],  # Marathi-specific: open o

    # --- Vowel diacritics ---
    "ा": ["aː"], "ि": ["i"], "ी": ["iː"],
    "ु": ["u"], "ू": ["uː"], "ृ": ["r̩"],
    "े": ["eː"], "ै": ["əi"],
    "ो": ["oː"], "ौ": ["əu"],
    "ॅ": ["ɛ"], "ॉ": ["ɔ"],

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
    "य": ["j"],
    "र": ["r"],
    "ळ": ["ɭ"],  # Marathi retroflex lateral (phonemic, cf. Gujarati)
    "ल": ["l"],
    "व": ["ʋ"],

    # --- Sibilants ---
    "श": ["ʃ"],
    "ष": ["ʂ"],
    "स": ["s"],
    "ह": ["ɦ"],

    # --- Additional Marathi letters ---
    "ड़": ["ɽ"],  # retroflex flap
    "ढ़": ["ɽʱ"],
}

ALLOPHONES_MR = {
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
    "ɲ": ["ɲ"], "ɳ": ["ɳ"],
    "ʃ": ["ʃ"], "ʂ": ["ʂ"], "s": ["s"],
    "ɦ": ["ɦ", "h"],
    "r": ["r"], "ɽ": ["ɽ"],
    "ɭ": ["ɭ"], "l": ["l"],
    "ʋ": ["ʋ", "w"], "j": ["j"],
    "ə": ["ə"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "eː": ["eː"], "oː": ["oː"],
    "ɛ": ["ɛ"], "ɔ": ["ɔ"],
    "əi": ["əi"], "əu": ["əu"],
    "r̩": ["r̩"],
}

# ══════════════════════════════════════════════════════════════════════════════
# Nepali — Nepal's national language; Devanagari script
# ══════════════════════════════════════════════════════════════════════════════
# Very similar to Hindi but: no /q x ɣ/ from Arabic/Persian;
# /ɦ/ is [h]; some dialectal variation.

GRAPHEMES_NE = {
    # Same consonant inventory as Hindi, without Arabic/Persian loans
    # --- Independent vowels ---
    "अ": ["ə"], "आ": ["aː"],
    "इ": ["i"], "ई": ["iː"],
    "उ": ["u"], "ऊ": ["uː"],
    "ऋ": ["ri"],
    "ए": ["eː"], "ऐ": ["əi"],
    "ओ": ["oː"], "औ": ["əu"],

    # --- Vowel diacritics ---
    "ा": ["aː"], "ि": ["i"], "ी": ["iː"],
    "ु": ["u"], "ू": ["uː"], "ृ": ["ri"],
    "े": ["eː"], "ै": ["əi"],
    "ो": ["oː"], "ौ": ["əu"],

    # --- Diacritics ---
    "ं": ["̃"], "ः": ["h"], "ँ": ["̃"], "्": [""],

    # --- Velars ---
    "क": ["k"], "ख": ["kʰ"], "ग": ["ɡ"], "घ": ["ɡʱ"], "ङ": ["ŋ"],

    # --- Palatals ---
    "च": ["tʃ"], "छ": ["tʃʰ"], "ज": ["dʒ"], "झ": ["dʒʱ"], "ञ": ["ɲ"],

    # --- Retroflexes ---
    "ट": ["ʈ"], "ठ": ["ʈʰ"], "ड": ["ɖ"], "ढ": ["ɖʱ"], "ण": ["ɳ"],

    # --- Dentals ---
    "त": ["t̪"], "थ": ["t̪ʰ"], "द": ["d̪"], "ध": ["d̪ʱ"], "न": ["n"],

    # --- Labials ---
    "प": ["p"], "फ": ["pʰ"], "ब": ["b"], "भ": ["bʱ"], "म": ["m"],

    # --- Semivowels / liquids ---
    "य": ["j"], "र": ["r"], "ल": ["l"], "व": ["ʋ"],
    "ड़": ["ɽ"], "ढ़": ["ɽʱ"],

    # --- Sibilants ---
    "श": ["ʃ"], "ष": ["ʂ"], "स": ["s"], "ह": ["h"],  # Nepali: /h/ not /ɦ/
}

ALLOPHONES_NE = {
    "p": ["p"], "pʰ": ["pʰ"],
    "b": ["b"], "bʱ": ["bʱ"],
    "t̪": ["t̪"], "t̪ʰ": ["t̪ʰ"],
    "d̪": ["d̪"], "d̪ʱ": ["d̪ʱ"],
    "ʈ": ["ʈ"], "ʈʰ": ["ʈʰ"],
    "ɖ": ["ɖ"], "ɖʱ": ["ɖʱ"],
    "k": ["k"], "kʰ": ["kʰ"],
    "ɡ": ["ɡ"], "ɡʱ": ["ɡʱ"],
    "tʃ": ["tʃ"], "tʃʰ": ["tʃʰ"],
    "dʒ": ["dʒ"], "dʒʱ": ["dʒʱ"],
    "m": ["m"], "n": ["n", "ɳ", "ŋ"],
    "ɲ": ["ɲ"], "ɳ": ["ɳ"],
    "ʃ": ["ʃ"], "ʂ": ["ʂ"], "s": ["s"],
    "h": ["h"],
    "r": ["r"], "ɽ": ["ɽ"],
    "l": ["l"],
    "ʋ": ["ʋ", "w"], "j": ["j"],
    "ə": ["ə"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "eː": ["eː"], "oː": ["oː"],
}

SPECS = {
    "gu": LanguageSpec(
        code="gu",
        name="Gujarati",
        family="Indo-Aryan",
        script="Gujarati",
        graphemes=GRAPHEMES_GU,
        allophones=ALLOPHONES_GU,
        parent="sa",
        ancestors=(
            Ancestor("sa", P, 0.82,
                     "Descent via Shauraseni Apabhraṃśa / Old Gujarati"),
            Ancestor("fa", AD, 0.08,
                     "Persian influence through Mughal period and Parsi community"),
        ),
        notes=(
            "Standard Gujarati (Gujarat, India). "
            "Distinct Gujarati script derived from Devanagari. "
            "⟨ળ⟩ = [ɭ] retroflex lateral is a phoneme (unlike most IA). "
            "Four-way laryngeal contrast retained. "
            "Short /ə/ deleted in word-final position (schwa deletion)."
        ),
    ),
    "mr": LanguageSpec(
        code="mr",
        name="Marathi",
        family="Indo-Aryan",
        script="Devanagari",
        graphemes=GRAPHEMES_MR,
        allophones=ALLOPHONES_MR,
        parent="sa",
        ancestors=(
            Ancestor("sa", P, 0.80,
                     "Descent via Maharashtri Apabhraṃśa"),
            Ancestor("hi", AD, 0.05,
                     "Contact with Hindi"),
        ),
        notes=(
            "Standard Marathi (Maharashtra). "
            "⟨ळ⟩ = [ɭ] retroflex lateral phonemic. "
            "Has ⟨ऍ⟩ = [ɛ] and ⟨ऑ⟩ = [ɔ] (loanword phonemes). "
            "Four-way laryngeal contrast. "
            "Schwa deletion applies systematically."
        ),
    ),
    "ne": LanguageSpec(
        code="ne",
        name="Nepali",
        family="Indo-Aryan",
        script="Devanagari",
        graphemes=GRAPHEMES_NE,
        allophones=ALLOPHONES_NE,
        parent="sa",
        ancestors=(
            Ancestor("sa", P, 0.83,
                     "Descent via Shauraseni through Khas language"),
        ),
        notes=(
            "Standard Nepali (Nepal's national language). "
            "Closely related to Hindi; ⟨ह⟩ = [h] (voiceless, not [ɦ]). "
            "No Perso-Arabic loan phonemes /q x ɣ/. "
            "Four-way laryngeal contrast; retroflex series phonemic."
        ),
    ),
}
