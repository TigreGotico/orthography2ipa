"""Modern Greek (el) — grapheme→IPA and allophone mappings.

Sources:
- Arvaniti, A. (1999). Standard Modern Greek. *JIPA* 29(2).
- Holton, D. et al. (2012). *Greek: A Comprehensive Grammar*, 2nd ed.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels (5-vowel system) ---
    "α": ["a"],
    "ε": ["e"],
    "η": ["i"],  # ita: /i/ in Modern Greek
    "ι": ["i"],
    "ο": ["o"],
    "υ": ["i"],  # ypsilon: /i/ (not /y/)
    "ω": ["o"],  # omega: same as omicron /o/

    # --- Vowel digraphs ---
    "αι": ["e"],  # = ⟨ε⟩
    "ει": ["i"],  # = ⟨ι⟩
    "οι": ["i"],  # = ⟨ι⟩
    "ου": ["u"],
    "υι": ["i"],
    "αυ": ["av", "af"],  # [av] before voiced; [af] before voiceless
    "ευ": ["ev", "ef"],  # same pattern

    # --- Consonants ---
    "β": ["v"],
    "γ": ["ɣ", "ʝ"],  # [ɣ] before back V; [ʝ] before front V
    "δ": ["ð"],
    "ζ": ["z"],
    "θ": ["θ"],
    "κ": ["k", "c"],  # palatalised before front V
    "λ": ["l"],
    "μ": ["m"],
    "ν": ["n"],
    "ξ": ["ks"],
    "π": ["p"],
    "ρ": ["r"],
    "σ": ["s"], "ς": ["s"],  # final sigma
    "τ": ["t"],
    "φ": ["f"],
    "χ": ["x", "ç"],  # [x] before back V; [ç] before front V
    "ψ": ["ps"],

    # --- Consonant digraphs ---
    "μπ": ["b", "mb"],  # [b] initially; [mb] medially
    "ντ": ["d", "nd"],  # [d] initially; [nd] medially
    "γκ": ["ɡ", "ŋɡ"],  # [ɡ] initially; [ŋɡ] medially
    "γγ": ["ŋɡ"],
    "τσ": ["ts"],
    "τζ": ["dz"],

    # --- Accented vowels (same phoneme, stress marker) ---
    "ά": ["a"], "έ": ["e"], "ή": ["i"],
    "ί": ["i"], "ό": ["o"], "ύ": ["i"], "ώ": ["o"],
}

ALLOPHONES = {
    "p": ["p"], "b": ["b"],
    "t": ["t"], "d": ["d"],
    "k": ["k"], "c": ["c"],
    "ɡ": ["ɡ"],

    "f": ["f"], "v": ["v"],
    "θ": ["θ"], "ð": ["ð"],
    "s": ["s"], "z": ["z"],
    "x": ["x"], "ç": ["ç"],
    "ɣ": ["ɣ"], "ʝ": ["ʝ"],

    "ts": ["ts"], "dz": ["dz"],

    "m": ["m"], "n": ["n", "ŋ"],
    "l": ["l"], "r": ["r", "ɾ"],
    "j": ["j"],

    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
}

SPECS = {
    "el": LanguageSpec(
        code="el",
        name="Modern Greek",
        family="Hellenic",
        script="Greek",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="grc",
        notes=(
            "Standard Modern Greek (Demotic). 5-vowel system despite "
            "many graphemic representations. Digraphs ⟨μπ⟩, ⟨ντ⟩, ⟨γκ⟩ "
            "represent voiced stops, with prenasalisation medially."
        ),
    ),
}
