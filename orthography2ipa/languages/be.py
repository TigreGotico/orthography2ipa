"""Belarusian (be) — grapheme→IPA and allophone mappings.

Sources:
- Padluzhny, A. (1985). *Fanetyka belaruskai litaraturnai movy*. Minsk.
- Mayo, P. (1993). 'Belorussian' in *The Slavonic Languages* (ed. Comrie & Corbett).
- Swan, O.E. (2002). *A Grammar of Contemporary Belarusian*.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels ---
    "а": ["a"],
    "е": ["jɛ"],  # iotated е; [ɛ] after consonant
    "ё": ["jɔ"],  # always iotated
    "і": ["i"],  # distinct letter (unlike Russian ⟨и⟩)
    "і": ["i"],
    "й": ["j"],
    "о": ["ɔ"],
    "у": ["u"],
    "ы": ["ɨ"],
    "э": ["ɛ"],
    "ю": ["ju"],
    "я": ["ja"],

    # --- Consonants ---
    "б": ["b"],
    "в": ["v"],
    "г": ["ɣ"],  # voiced velar fricative (key Belarusian feature)
    "ґ": ["ɡ"],  # rare plosive (loanwords)
    "д": ["d"],
    "дж": ["dʒ"],
    "дз": ["dz"],
    "ж": ["ʒ"],
    "з": ["z"],
    "к": ["k"],
    "л": ["l"],
    "м": ["m"],
    "н": ["n"],
    "п": ["p"],
    "р": ["r"],
    "с": ["s"],
    "т": ["t"],
    "ў": ["w"],  # non-syllabic /w/ (unique Belarusian letter)
    "ф": ["f"],
    "х": ["x"],
    "ц": ["ts"],
    "ч": ["tʃ"],
    "ш": ["ʃ"],
    "шч": ["ʃtʃ"],
    "'": [""],  # apostrophe (hardening sign)

    # --- Soft sign + palatalised digraphs ---
    "ь": ["ʲ"],
    "дзь": ["dzʲ"], "ць": ["tsʲ"],
    "ль": ["lʲ"], "нь": ["nʲ"], "сь": ["sʲ"],
    "зь": ["zʲ"], "дь": ["dʲ"], "ть": ["tʲ"],
    "рь": ["rʲ"],
}

ALLOPHONES = {
    "p": ["p"], "b": ["b", "p"],
    "t": ["t"], "d": ["d", "t"],
    "k": ["k"], "ɡ": ["ɡ", "k"],
    "ɣ": ["ɣ", "x"],  # devoiced finally and before voiceless
    "f": ["f"], "v": ["v", "f"],
    "s": ["s"], "sʲ": ["sʲ"],
    "z": ["z", "s"], "zʲ": ["zʲ", "sʲ"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ", "ʃ"],
    "x": ["x"],
    "ts": ["ts"], "tsʲ": ["tsʲ"],
    "dz": ["dz", "ts"], "dzʲ": ["dzʲ", "tsʲ"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ", "tʃ"],
    "m": ["m"], "n": ["n", "ŋ"], "nʲ": ["nʲ"],
    "l": ["l"], "lʲ": ["lʲ"],
    "r": ["r"], "rʲ": ["rʲ"],
    "w": ["w"], "j": ["j"],
    # Vowels — Belarusian has аканне (unstressed /o a/ merge to [a])
    "a": ["a", "ɐ"],
    "ɔ": ["ɔ", "a"],  # unstressed → [a] (аканне)
    "ɛ": ["ɛ", "ɪ"],  # яканне: unstressed /ɛ/ → [ɪ] after soft C
    "i": ["i"],
    "ɨ": ["ɨ"],
    "u": ["u", "ʊ"],
}

SPECS = {
    "be": LanguageSpec(
        code="be",
        name="Belarusian",
        family="Slavic",
        script="Cyrillic",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="sla",
        notes=(
            "Standard Belarusian (Tarashkevitsa/Narkamaŭka). "
            "Distinctive features: ⟨г⟩ = [ɣ] (voiced velar fricative, not plosive), "
            "⟨ў⟩ = [w] (unique letter for non-syllabic /w/), "
            "pervasive аканне (unstressed /ɔ/ → [a]), яканне "
            "(unstressed /ɛ/ → [i] after soft consonants), "
            "full affricate writing: ⟨дз⟩ = [dz], ⟨дж⟩ = [dʒ]."
        ),
    ),
}
