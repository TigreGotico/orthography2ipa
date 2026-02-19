"""Arabic (ar) — grapheme→IPA and allophone mappings.

Sources:
- Thelwall, R. & Sa'Adeddin, M.A. (1990). Arabic. *JIPA* 20(2).
- Watson, J.C.E. (2002). *The Phonology and Morphology of Arabic*.

Conventions:
- Modern Standard Arabic (MSA / Fuṣḥā).
- Short vowels represented by diacritics (ḥarakāt).
- Letters in isolated form as keys.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Consonants ---
    "ا": ["ʔ", "aː"],  # alif: glottal stop or long /aː/
    "أ": ["ʔa"],  # hamza above alif
    "إ": ["ʔi"],  # hamza below alif
    "آ": ["ʔaː"],  # alif madda
    "ب": ["b"],
    "ت": ["t"],
    "ث": ["θ"],
    "ج": ["dʒ"],  # MSA standard; [ɡ] Egyptian, [ʒ] Levantine
    "ح": ["ħ"],
    "خ": ["x"],
    "د": ["d"],
    "ذ": ["ð"],
    "ر": ["r"],
    "ز": ["z"],
    "س": ["s"],
    "ش": ["ʃ"],
    "ص": ["sˤ"],  # emphatic s
    "ض": ["dˤ"],  # emphatic d
    "ط": ["tˤ"],  # emphatic t
    "ظ": ["ðˤ"],  # emphatic dh
    "ع": ["ʕ"],
    "غ": ["ɣ"],
    "ف": ["f"],
    "ق": ["q"],
    "ك": ["k"],
    "ل": ["l"],
    "م": ["m"],
    "ن": ["n"],
    "ه": ["h"],
    "و": ["w"],  # consonantal
    "ي": ["j"],  # consonantal
    "ء": ["ʔ"],  # hamza (standalone)
    "ى": ["aː"],  # alif maqṣūra
    "ة": ["a", "at"],  # tāʾ marbūṭa: [a] pausal / [at] construct

    # --- Short vowel diacritics ---
    "\u064E": ["a"],  # fatḥa
    "\u064F": ["u"],  # ḍamma
    "\u0650": ["i"],  # kasra
    "\u064B": ["an"],  # tanwīn fatḥa
    "\u064C": ["un"],  # tanwīn ḍamma
    "\u064D": ["in"],  # tanwīn kasra
    "\u0651": ["ː"],  # shadda (gemination)
    "\u0652": [""],  # sukūn (no vowel)

    # --- Long vowels (consonant letter as mater lectionis) ---
    # Represented as sequences: ⟨ا⟩ after fatḥa = /aː/, etc.
    # These are handled as the consonant letters above.

    # --- Definite article ---
    "ال": ["al", "aː"],  # assimilates before sun letters
}

ALLOPHONES = {
    "b": ["b"],
    "t": ["t"], "tˤ": ["tˤ"],
    "d": ["d"], "dˤ": ["dˤ"],
    "k": ["k"],
    "q": ["q", "ɡ", "ʔ"],  # dialectal: [ɡ] Gulf/Egyptian, [ʔ] Levantine
    "ʔ": ["ʔ"],

    "θ": ["θ", "t", "s"],  # [t]/[s] in many colloquials
    "ð": ["ð", "d", "z"],  # same pattern
    "ðˤ": ["ðˤ", "dˤ", "zˤ"],

    "f": ["f"],
    "s": ["s"], "sˤ": ["sˤ"],
    "z": ["z"],
    "ʃ": ["ʃ"],
    "x": ["x", "χ"],
    "ɣ": ["ɣ", "ʁ"],
    "ħ": ["ħ"],
    "ʕ": ["ʕ", "ʔ"],  # weakened in some dialects
    "h": ["h"],

    "m": ["m"],
    "n": ["n", "m", "ŋ"],  # assimilates before labials/velars
    "l": ["l", "lˤ"],  # emphatic in الله [ɫ]
    "r": ["r", "ɾ"],

    "w": ["w"], "j": ["j"],

    # Vowels
    "a": ["a", "æ", "ɑ"],  # fronted near plain C, backed near emphatic
    "aː": ["aː", "æː", "ɑː"],
    "i": ["i", "ɪ"],
    "iː": ["iː"],
    "u": ["u", "ʊ"],
    "uː": ["uː"],
}

SPECS = {
    "ar": LanguageSpec(
        code="ar",
        name="Arabic (MSA)",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        notes=(
            "Modern Standard Arabic (Fuṣḥā). Dialectal variants noted "
            "in allophone map. Emphatic consonants trigger backing of "
            "adjacent vowels. Sun/moon letter assimilation of /l/ in "
            "definite article not encoded as separate graphemes."
        ),
    ),
}
