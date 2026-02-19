"""Slovak (sk) — grapheme→IPA and allophone mappings.

Sources:
- Hanulíková, A. & Hamann, S. (2010). Slovak. *JIPA* 40(3).
- Rubach, J. (1993). *The Lexical Phonology of Slovak*. OUP.
- Pauliny, E. (1979). *Slovenská fonológia*. SPN.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Short vowels ---
    "a": ["a"], "e": ["ɛ"], "i": ["i"], "o": ["ɔ"], "u": ["u"],
    "y": ["i"],  # same phoneme as ⟨i⟩

    # --- Long vowels ---
    "á": ["aː"], "é": ["ɛː"], "í": ["iː"], "ó": ["ɔː"], "ú": ["uː"],
    "ý": ["iː"],

    # --- Diphthongs ---
    "ia": ["iɐ"],  # falling diphthong
    "ie": ["iɛ"],
    "iu": ["iu"],
    "ô": ["uɔ"],  # round diphthong

    # --- Syllabic consonants ---
    "ŕ": ["r̩ː"],  # long syllabic r
    "ĺ": ["l̩ː"],  # long syllabic l

    # --- Consonants ---
    "b": ["b"],
    "c": ["ts"],
    "č": ["tʃ"],
    "d": ["d"],
    "ď": ["ɟ"],  # palatal stop
    "dz": ["dz"],
    "dž": ["dʒ"],
    "f": ["f"],
    "g": ["ɡ"],
    "h": ["ɦ"],  # voiced glottal fricative
    "ch": ["x"],
    "j": ["j"],
    "k": ["k"],
    "l": ["l"],
    "ľ": ["lʲ"],  # palatalised l
    "m": ["m"],
    "n": ["n"],
    "ň": ["ɲ"],
    "p": ["p"],
    "q": ["kv"],
    "r": ["r"],
    "s": ["s"],
    "š": ["ʃ"],
    "t": ["t"],
    "ť": ["c"],  # palatal stop
    "v": ["v"],
    "w": ["v"],
    "x": ["ks"],
    "z": ["z"],
    "ž": ["ʒ"],
}

ALLOPHONES = {
    "p": ["p"], "b": ["b", "p"],
    "t": ["t"], "d": ["d", "t"],
    "c": ["c"], "ɟ": ["ɟ", "c"],  # palatal stops
    "k": ["k"], "ɡ": ["ɡ", "k"],
    "f": ["f"], "v": ["v", "f"],
    "s": ["s"], "z": ["z", "s"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ", "ʃ"],
    "ɦ": ["ɦ", "x"],
    "x": ["x"],
    "ts": ["ts"], "dz": ["dz", "ts"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ", "tʃ"],
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "lʲ": ["lʲ"], "l̩": ["l̩"], "l̩ː": ["l̩ː"],
    "r": ["r"], "r̩": ["r̩"], "r̩ː": ["r̩ː"],
    "j": ["j"],
    # Vowels: Slovak has rhythmic lengthening law
    "a": ["a"], "aː": ["aː"],
    "ɛ": ["ɛ"], "ɛː": ["ɛː"],
    "i": ["i"], "iː": ["iː"],
    "ɔ": ["ɔ"], "ɔː": ["ɔː"],
    "u": ["u"], "uː": ["uː"],
    "iɐ": ["iɐ"], "iɛ": ["iɛ"], "iu": ["iu"], "uɔ": ["uɔ"],
}

SPECS = {
    "sk": LanguageSpec(
        code="sk",
        name="Slovak",
        family="Slavic",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="sla",
        notes=(
            "Standard Slovak. Close to Czech but distinct in several ways: "
            "⟨h⟩ = [ɦ] (like Czech, not [h]); "
            "diphthongs ⟨ia ie iu ô⟩; "
            "syllabic liquids ⟨r l⟩ and their long counterparts ⟨ŕ ĺ⟩; "
            "rhythmic law: two consecutive long syllables not permitted "
            "(second long vowel shortens). "
            "Palatal consonant pair: ⟨ď ť⟩ = [ɟ c]."
        ),
    ),
}
