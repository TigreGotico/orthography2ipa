"""Italian (it) — grapheme→IPA and allophone mappings.

Standard Italian based on Florentine/Tuscan.

Sources:
- Krämer, M. (2009). *The Phonology of Italian*. OUP.
- Bertinetto, P.M. & Loporcaro, M. (2005). 'The sound pattern of
  Standard Italian.' *JIPA* 35(2).
- Canepari, L. (2005). *A Handbook of Pronunciation*. Lincom Europa.
- Rohlfs, G. (1966–1969). *Grammatica storica della lingua italiana*.
  Einaudi. 3 vols.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE

GRAPHEMES = {
    # --- Vowels (7-vowel system) ---
    "a": ["a"],
    "e": ["e", "ɛ"],    # open/close lexically determined
    "i": ["i"],
    "o": ["o", "ɔ"],    # open/close lexically determined
    "u": ["u"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "tʃ"],   # [tʃ] before e,i
    "ch": ["k"],         # before e,i: ⟨che⟩ = [ke]
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "dʒ"],   # [dʒ] before e,i
    "gh": ["ɡ"],         # before e,i: ⟨ghe⟩ = [ɡe]
    "h": ["∅"],          # always silent
    "j": ["j"],
    "k": ["k"],          # foreign words
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "qu": ["kw"],
    "r": ["r"],
    "s": ["s", "z"],     # [z] between vowels
    "t": ["t"],
    "v": ["v"],
    "w": ["v", "w"],     # foreign words
    "x": ["ks"],         # foreign words
    "y": ["i", "j"],     # foreign words
    "z": ["ts", "dz"],   # lexically determined

    # --- Digraphs / trigraphs ---
    "ci": ["tʃ"],        # before a,o,u: ⟨cia⟩ = [tʃa]
    "gi": ["dʒ"],        # before a,o,u: ⟨gia⟩ = [dʒa]
    "sc": ["ʃ", "sk"],   # [ʃ] before e,i; [sk] before a,o,u
    "sci": ["ʃ"],        # before a,o,u: ⟨scia⟩ = [ʃa]
    "gl": ["ʎ", "ɡl"],   # [ʎ] before i; [ɡl] elsewhere
    "gli": ["ʎ"],        # palatal lateral
    "gn": ["ɲ"],         # palatal nasal

    # --- Geminates ---
    "bb": ["bː"], "cc": ["kː", "tːʃ"], "dd": ["dː"],
    "ff": ["fː"], "gg": ["ɡː", "dːʒ"], "ll": ["lː"],
    "mm": ["mː"], "nn": ["nː"], "pp": ["pː"],
    "rr": ["rː"], "ss": ["sː"], "tt": ["tː"],
    "zz": ["tːs", "dːz"],

    # --- Diphthongs ---
    "ai": ["aj"], "ei": ["ej"], "oi": ["oj"], "ui": ["uj"],
    "au": ["aw"], "eu": ["ew"],
    "ia": ["ja"], "ie": ["je"], "io": ["jo"], "iu": ["ju"],
    "ua": ["wa"], "ue": ["we"], "uo": ["wo"],
}

ALLOPHONES = {
    "p": ["p"],
    "b": ["b"],
    "t": ["t", "t̪"],     # dental before dental
    "d": ["d", "d̪"],
    "k": ["k"],
    "ɡ": ["ɡ"],

    "f": ["f"],
    "v": ["v"],
    "s": ["s"],
    "z": ["z"],
    "ʃ": ["ʃ"],

    "ts": ["ts"],
    "dz": ["dz"],
    "tʃ": ["tʃ"],
    "dʒ": ["dʒ"],

    "m": ["m", "ɱ"],     # labiodental before /f, v/
    "n": ["n", "m", "ɱ", "ŋ", "ɲ"],  # assimilates to following place
    "ɲ": ["ɲ"],
    "ŋ": ["ŋ"],          # allophone of /n/

    "l": ["l"],
    "ʎ": ["ʎ"],
    "r": ["r", "ɾ"],     # tap in fast speech / unstressed
    "j": ["j"],
    "w": ["w"],

    "a": ["a"],
    "e": ["e"],
    "ɛ": ["ɛ"],
    "i": ["i"],
    "o": ["o"],
    "ɔ": ["ɔ"],
    "u": ["u"],

    # Geminates
    "bː": ["bː"], "dː": ["dː"], "ɡː": ["ɡː"],
    "pː": ["pː"], "tː": ["tː"], "kː": ["kː"],
    "fː": ["fː"], "sː": ["sː"],
    "lː": ["lː"], "mː": ["mː"], "nː": ["nː"], "rː": ["rː"],
    "tːʃ": ["tːʃ"], "dːʒ": ["dːʒ"],
    "tːs": ["tːs"], "dːz": ["dːz"],
}

SPECS = {
    "it": LanguageSpec(
        code="it",
        name="Italian",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="la-x-italia",
        ancestors=(
            Ancestor("la-x-italia", P, 0.85,
                     "Italo-Romance Vulgar Latin: gemination preserved, "
                     "7-vowel system, -s lost, standard based on Tuscan."),
            Ancestor("gem", SUP, 0.05,
                     "Lombardic superstrate (6th–8th c.): vocabulary "
                     "(guancia, stinco, schiena), some N. Italian "
                     "phonological influence."),
            Ancestor("got", SUP, 0.03,
                     "Ostrogothic superstrate (5th–6th c.): limited "
                     "phonological impact, some vocabulary."),
            Ancestor("grc", SUB, 0.04,
                     "Greek substrate (Magna Graecia): mainly affects "
                     "southern dialects; limited in Tuscan standard."),
        ),
        notes=(
            "Standard Italian (based on Florentine/Tuscan). "
            "Open/close mid-vowel distinction (e/ɛ, o/ɔ) is lexically "
            "determined and varies by region. Gemination is phonemic "
            "(fato/fatto). Gorgia toscana (intervocalic stop aspiration) "
            "is a regional Tuscan feature, not standard."
        ),
    ),
}
