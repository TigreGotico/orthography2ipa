"""French (fr) — grapheme→IPA and allophone mappings.

Sources:
- Fougeron, C. & Smith, C. (1993). French. *JIPA* 23(2).
- Tranel, B. (1987). *The Sounds of French*.
- Walker, D.C. (2001). *French Sound Structure*.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE

GRAPHEMES = {
    # --- Single vowels ---
    "a": ["a"],
    "â": ["ɑ"],
    "e": ["ə", "e", "ɛ"],
    "é": ["e"],
    "è": ["ɛ"],
    "ê": ["ɛ"],
    "ë": ["ɛ"],
    "i": ["i"],
    "î": ["i"],
    "ï": ["i"],  # diaeresis = hiatus
    "o": ["ɔ", "o"],
    "ô": ["o"],
    "u": ["y"],
    "û": ["y"],
    "ù": ["y"],
    "ü": ["y"],
    "y": ["i"],

    # --- Single consonants ---
    "b": ["b"],
    "c": ["k", "s"],  # /k/ before a,o,u; /s/ before e,i
    "ç": ["s"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "ʒ"],  # /ɡ/ before a,o,u; /ʒ/ before e,i
    "h": [""],  # always silent (aspiré blocks liaison)
    "j": ["ʒ"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],
    "r": ["ʁ"],
    "s": ["s", "z"],  # /z/ intervocalic (liaison)
    "t": ["t"],
    "v": ["v"],
    "w": ["w", "v"],  # loanwords
    "x": ["ks", "ɡz"],
    "z": ["z"],

    # --- Consonant digraphs ---
    "ch": ["ʃ"],
    "gn": ["ɲ"],
    "ph": ["f"],
    "qu": ["k"],
    "gu": ["ɡ"],  # ⟨u⟩ silent before e,i
    "th": ["t"],  # no dental fricative in French
    "ss": ["s"],  # intervocalic voiceless

    # --- Trigraphs ---
    "ill": ["ij"],  # after vowel: /j/ glide
    "sch": ["ʃ"],  # German loanwords

    # --- Vowel digraphs ---
    "ai": ["ɛ", "e"],
    "ei": ["ɛ"],
    "au": ["o"],
    "ou": ["u"],
    "oi": ["wa"],
    "eu": ["ø", "œ"],
    "œu": ["ø", "œ"],

    # --- Vowel trigraphs ---
    "eau": ["o"],
    "oui": ["wi"],

    # --- Nasal vowel digraphs ---
    "an": ["ɑ̃"],
    "am": ["ɑ̃"],
    "en": ["ɑ̃"],
    "em": ["ɑ̃"],
    "in": ["ɛ̃"],
    "im": ["ɛ̃"],
    "on": ["ɔ̃"],
    "om": ["ɔ̃"],
    "un": ["œ̃"],
    "um": ["œ̃"],

    # --- Nasal trigraphs ---
    "ain": ["ɛ̃"],
    "aim": ["ɛ̃"],
    "ein": ["ɛ̃"],
    "ien": ["jɛ̃"],
    "oin": ["wɛ̃"],

    # --- Semi-vowel digraphs ---
    "ui": ["ɥi"],
}

ALLOPHONES = {
    # Plosives
    "p": ["p"],
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "k": ["k"],
    "ɡ": ["ɡ"],

    # Fricatives
    "f": ["f"],
    "v": ["v"],
    "s": ["s"],
    "z": ["z"],
    "ʃ": ["ʃ"],
    "ʒ": ["ʒ"],
    "ʁ": ["ʁ", "ʀ", "χ", "ɣ", "r"],  # uvular; trilled in singing/emphatic

    # Nasals
    "m": ["m"],
    "n": ["n"],
    "ɲ": ["ɲ", "nj"],  # weakened to [nj] in casual speech
    "ŋ": ["ŋ"],  # loanwords only (parking)

    # Laterals / Glides
    "l": ["l"],
    "j": ["j"],
    "w": ["w"],
    "ɥ": ["ɥ"],  # labio-palatal approximant

    # Oral vowels
    "a": ["a"],
    "ɑ": ["ɑ"],  # merging with [a] in modern Parisian
    "e": ["e"],
    "ɛ": ["ɛ"],
    "ə": ["ə"],  # may delete (schwa elision)
    "i": ["i"],
    "o": ["o"],
    "ɔ": ["ɔ"],
    "u": ["u"],
    "y": ["y"],
    "ø": ["ø"],
    "œ": ["œ"],

    # Nasal vowels
    "ɑ̃": ["ɑ̃"],
    "ɛ̃": ["ɛ̃", "æ̃"],  # younger Parisian speakers fronting
    "ɔ̃": ["ɔ̃"],
    "œ̃": ["œ̃", "ɛ̃"],  # merging with /ɛ̃/ in many speakers
}

SPECS = {
    "fr-FR": LanguageSpec(
        code="fr-FR",
        name="French",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="la-x-gallia",
        ancestors=(
            Ancestor("la-x-gallia", P, 0.72,
                     "Gallo-Romance Vulgar Latin"),
            Ancestor("gem", SUP, 0.18,
                     "Frankish superstrate: /h/ restoration, "
                     "initial stress, massive vocabulary (guerre, "
                     "jardin, blanc). Strongest in Romance."),
            Ancestor("xcg", SUB, 0.05,
                     "Gaulish substrate (already in la-x-gallia, "
                     "additional direct traces)"),
            Ancestor("got", SUP, 0.03,
                     "Visigothic superstrate (pre-Frankish)"),
            Ancestor("xaa", AD, 0.02,
                     "Arabic via Iberian transmission"),
        ),
        notes=(
            "Standard Metropolitan French (Parisian). "
            "Nasal grapheme sequences (⟨an⟩, ⟨en⟩, etc.) only nasalise "
            "when NOT followed by a vowel or another ⟨n⟩/⟨m⟩; context "
            "rules needed for disambiguation."
        ),
    ),
}
