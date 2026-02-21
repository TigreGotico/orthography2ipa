"""Aragonese (an) — grapheme→IPA and allophone mappings.

Aragonese (Aragonés) is a Romance language spoken in the Pyrenean valleys
of the province of Huesca, Aragon, Spain. ~10,000–25,000 speakers.
UNESCO classified as "definitely endangered."

Sources:
- Nagore Laín, F. (1986). *El aragonés de Panticosa*.
- Tomás Arias, C. (1999). *El aragonés del Biello Sobrarbe*.
- Academia de l'Aragonés (2010). *Propuesta ortográfica de l'aragonés*.
- Kuhn, A. (1935). *Der hocharagonesische Dialekt*.

Conventions:
- ISO 639-3: an (Aragonese).
- Based on central/standard Aragonese (Alto Aragonés).
- Western (an-x-occidental): transitional to Castilian.
- Eastern (an-x-oriental): transitional to Catalan (Benasquese).
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec, GraphemePosition as GP

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE

GRAPHEMES_AN = {
    # --- Vowels (5-vowel system) ---
    "a": ["a"],
    "e": ["e", "ɛ"],
    "i": ["i"],
    "o": ["o", "ɔ"],
    "u": ["u"],
    "á": ["a"], "é": ["e"], "í": ["i"], "ó": ["o"], "ú": ["u"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "θ"],  # /θ/ before e,i in many varieties; /s/ in some
    "ç": ["s", "θ"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "x"],
    "h": [""],  # silent (but h- from Lat. F- in some words)
    "j": ["x", "tʃ"],  # [tʃ] in traditional Aragonese; [x] Castilianised
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "ñ": ["ɲ"],
    "p": ["p"],
    "q": ["k"],
    "r": ["ɾ"],
    "s": ["s"],  # apico-alveolar [s̺]
    "t": ["t"],
    "v": ["b"],  # betacism in most varieties
    "x": ["ʃ"],  # postalveolar fricative (native Aragonese)
    "y": ["ʝ", "i"],
    "z": ["θ", "s"],

    # --- Digraphs ---
    "ch": ["tʃ"],
    "ll": ["ʎ"],  # conservative: palatal lateral
    "ny": ["ɲ"],  # Aragonese palatal nasal spelling
    "rr": ["r"],
    "qu": ["k"],
    "gu": ["ɡ"],
    "ix": ["ʃ"],  # after vowel

    # --- Diphthongs (Aragonese retains Lat. Ĕ/Ŏ diphthongs like Castilian) ---
    "ue": ["we"],  # Lat. Ŏ: puerta, fuent, cuerpo
    "ie": ["je"],  # Lat. Ĕ: tierra, fiero, siete
    "ua": ["wa"], "uo": ["wo"],
    "ia": ["ja"], "io": ["jo"], "iu": ["ju"],
    "ai": ["aj"], "ei": ["ej"], "oi": ["oj"],
    "au": ["aw"], "eu": ["ew"], "ou": ["ow"],
    "ui": ["wi"],
}

ALLOPHONES_AN = {
    "p": ["p"],
    "b": ["b", "β"],
    "t": ["t"],
    "d": ["d", "ð"],
    "k": ["k"],
    "ɡ": ["ɡ", "ɣ"],
    "f": ["f"],
    "θ": ["θ"],
    "s": ["s̺"],  # apico-alveolar
    "x": ["x"],
    "ʃ": ["ʃ"],
    "ʝ": ["ʝ"],
    "tʃ": ["tʃ"],
    "m": ["m"],
    "n": ["n", "ŋ"],
    "ɲ": ["ɲ"],
    "l": ["l"],
    "ʎ": ["ʎ"],
    "ɾ": ["ɾ"],
    "r": ["r"],
    "j": ["j"],
    "w": ["w"],
    "a": ["a"], "e": ["e"], "ɛ": ["ɛ"],
    "i": ["i"], "o": ["o"], "ɔ": ["ɔ"], "u": ["u"],
}

# Standard Ibero-Romance lenition plus conservative features.

POSITIONAL_AN = {
    "b": {
        GP.DEFAULT: ["b"],
        GP.INTERVOCALIC: ["β"],
    },
    "d": {
        GP.DEFAULT: ["d"],
        GP.INTERVOCALIC: ["ð"],
    },
    "g": {
        GP.DEFAULT: ["ɡ"],
        GP.INTERVOCALIC: ["ɣ"],
    },
    "r": {
        GP.WORD_INITIAL: ["r"],
        GP.INTERVOCALIC: ["ɾ"],
        GP.ONSET: ["ɾ"],
        GP.CODA: ["ɾ"],
    },
}

# Eastern (Benasquese / Ribagorçan transition)
GRAPHEMES_AN_E = {
    **GRAPHEMES_AN,
    # Catalan influence: voiced affricates, palatal features
    "ll": ["ʎ", "j"],  # some yeísmo from Catalan side
    "j": ["dʒ", "x"],  # voiced affricate in traditional forms
    "g": ["ɡ", "dʒ"],  # before e,i
}

ALLOPHONES_AN_E = {
    **ALLOPHONES_AN,
    "dʒ": ["dʒ"],  # Catalan-like voiced affricate
    "ʎ": ["ʎ", "j"],
}

SPECS = {
    "an": LanguageSpec(
        code="an",
        name="Aragonese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_AN,
        allophones=ALLOPHONES_AN,
        parent="la",
        ancestors=(
            Ancestor("la-x-hispania", P, 0.80,
                     "Primary descent from Hispanic Vulgar Latin"),
            Ancestor("xaq", SUB, 0.06,
                     "Basque substrate: Pyrenean areas; shared f→h in some "
                     "western Aragonese; cf. Saroïhandy (1913)"),
            Ancestor("xib", SUB, 0.03,
                     "Iberian substrate: eastern Aragonese territory overlaps "
                     "with ancient Iberian-speaking areas"),
            Ancestor("got", SUP, 0.03,
                     "Visigothic superstrate"),
            Ancestor("xaa", AD, 0.04,
                     "Arabic adstrate: Ebro valley under Islamic rule until "
                     "12th c.; more than Asturian, less than Castilian"),
        ),
        notes=(
            "Central/standard Aragonese (Alto Aragonés). ~10,000–25,000 "
            "speakers in Huesca Pyrenean valleys. Conservative Romance "
            "phonology: Lat. Ĕ → [je], Lat. Ŏ → [we] (shared with "
            "Castilian), apico-alveolar [s̺], palatal lateral [ʎ] "
            "(no yeísmo), voiceless postalveolar [ʃ] for ⟨x⟩. "
            "Retains Latin F- in most positions (unlike Castilian). "
            "Latin -LL- → [ʎ], -NN- → [ɲ]. UNESCO 'definitely endangered'."
        ),
    ),
    "an-x-occidental": LanguageSpec(
        code="an-x-occidental",
        name="Western Aragonese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_AN,
        allophones=ALLOPHONES_AN,
        parent="an",
        notes=(
            "Western Aragonese (Jacetania, Cinco Villas). Transitional "
            "to Castilian: strongest Castilian phonological influence, "
            "some /ʎ/ → /ʝ/ yeísmo. Latin J- → [x] (Castilian pattern) "
            "rather than [tʃ] or [dʒ]."
        ),
    ),
    "an-x-oriental": LanguageSpec(
        code="an-x-oriental",
        name="Eastern Aragonese (Ribagorçan)",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_AN_E,
        allophones=ALLOPHONES_AN_E,
        parent="an",
        notes=(
            "Eastern Aragonese / Ribagorçan / Benasquese transition zone. "
            "Catalan influence: voiced affricate [dʒ] for Latin G/J before "
            "front vowels, possible partial yeísmo. Transitional phonology "
            "between Aragonese and Catalan, debated classification."
        ),
    ),
}
