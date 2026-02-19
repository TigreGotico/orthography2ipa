"""Hindi (hi) — grapheme→IPA and allophone mappings.

Sources:
- Ohala, M. (1999). Hindi. *Handbook of the IPA*.
- Shapiro, M.C. (2003). Hindi. In G. Cardona & D. Jain (Eds.), *The Indo-Aryan Languages*.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Independent vowels ---
    "अ": ["ə"], "आ": ["aː"], "इ": ["ɪ"],
    "ई": ["iː"], "उ": ["ʊ"], "ऊ": ["uː"],
    "ऋ": ["ɾɪ"],
    "ए": ["eː"], "ऐ": ["ɛː"],
    "ओ": ["oː"], "औ": ["ɔː"],

    # --- Vowel diacritics (mātrā) ---
    "ा": ["aː"], "ि": ["ɪ"], "ी": ["iː"],
    "ु": ["ʊ"], "ू": ["uː"], "ृ": ["ɾɪ"],
    "े": ["eː"], "ै": ["ɛː"],
    "ो": ["oː"], "ौ": ["ɔː"],

    # --- Nasalisation ---
    "ं": ["̃"],  # anusvāra (nasal)
    "ँ": ["̃"],  # candrabindu (nasalisation)
    "ः": ["h"],  # visarga

    # --- Halant ---
    "्": [""],  # virāma (suppresses inherent /ə/)

    # --- Velar stops ---
    "क": ["k"], "ख": ["kʰ"], "ग": ["ɡ"], "घ": ["ɡʱ"], "ङ": ["ŋ"],
    # --- Palatal affricates ---
    "च": ["tʃ"], "छ": ["tʃʰ"], "ज": ["dʒ"], "झ": ["dʒʱ"], "ञ": ["ɲ"],
    # --- Retroflex stops ---
    "ट": ["ʈ"], "ठ": ["ʈʰ"], "ड": ["ɖ"], "ढ": ["ɖʱ"], "ण": ["ɳ"],
    # --- Dental stops ---
    "त": ["t̪"], "थ": ["t̪ʰ"], "द": ["d̪"], "ध": ["d̪ʱ"], "न": ["n"],
    # --- Labial stops ---
    "प": ["p"], "फ": ["pʰ"], "ब": ["b"], "भ": ["bʱ"], "म": ["m"],
    # --- Approximants / fricatives ---
    "य": ["j"], "र": ["ɾ"], "ल": ["l"], "व": ["ʋ"],
    "श": ["ʃ"], "ष": ["ʂ"], "स": ["s"], "ह": ["ɦ"],

    # --- Perso-Arabic loans (nukta consonants) ---
    "क़": ["q"], "ख़": ["x"], "ग़": ["ɣ"],
    "ज़": ["z"], "फ़": ["f"],

    # --- Common conjuncts ---
    "क्ष": ["kʃ"],
    "त्र": ["t̪ɾ"],
    "ज्ञ": ["ɡj", "dʒɲ"],  # varies by dialect
    "श्र": ["ʃɾ"],
}

ALLOPHONES = {
    "k": ["k"], "kʰ": ["kʰ"],
    "ɡ": ["ɡ"], "ɡʱ": ["ɡʱ"],
    "tʃ": ["tʃ"], "tʃʰ": ["tʃʰ"],
    "dʒ": ["dʒ"], "dʒʱ": ["dʒʱ"],
    "ʈ": ["ʈ"], "ʈʰ": ["ʈʰ"],
    "ɖ": ["ɖ", "ɽ"], "ɖʱ": ["ɖʱ", "ɽʱ"],  # flapped allophones
    "t̪": ["t̪"], "t̪ʰ": ["t̪ʰ"],
    "d̪": ["d̪"], "d̪ʱ": ["d̪ʱ"],
    "p": ["p"], "pʰ": ["pʰ"],
    "b": ["b"], "bʱ": ["bʱ"],

    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʂ": ["ʂ"],
    "ɦ": ["ɦ", "h"],
    "f": ["f", "pʰ"],  # [pʰ] for speakers without /f/
    "x": ["x", "kʰ"],  # similarly
    "ɣ": ["ɣ", "ɡ"],
    "q": ["q", "k"],

    "m": ["m"], "n": ["n", "n̪"], "ɲ": ["ɲ"], "ɳ": ["ɳ"], "ŋ": ["ŋ"],
    "l": ["l"], "ɾ": ["ɾ"], "ɽ": ["ɽ"],
    "ʋ": ["ʋ", "w", "v"],  # [w] before back vowels; [v] emphatic
    "j": ["j"],

    "ə": ["ə", "æ"],
    "aː": ["aː"],
    "ɪ": ["ɪ"], "iː": ["iː"],
    "ʊ": ["ʊ"], "uː": ["uː"],
    "eː": ["eː"], "ɛː": ["ɛː", "æː"],
    "oː": ["oː"], "ɔː": ["ɔː"],
}

SPECS = {
    "hi": LanguageSpec(
        code="hi",
        name="Hindi",
        family="Indo-Aryan",
        script="Devanagari",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="ine",
        notes=(
            "Standard Hindi (Khaṛī Bolī). 4-way laryngeal contrast: "
            "voiceless, aspirated, voiced, breathy-voiced. "
            "Nukta letters for Perso-Arabic loans may not be distinguished "
            "by all speakers."
        ),
    ),
}
