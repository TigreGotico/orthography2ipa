"""Italian (it) — grapheme→IPA and allophone mappings.

Sources:
- Rogers, D. & d'Arcangeli, L. (2004). Italian. *JIPA* 34(1).
- Bertinetto, P.M. & Loporcaro, M. (2005). The sound pattern of Standard Italian.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels (7-vowel system in stressed position) ---
    "a": ["a"],
    "e": ["e", "ɛ"],
    "i": ["i"],
    "o": ["o", "ɔ"],
    "u": ["u"],
    "à": ["a"],
    "è": ["ɛ"],
    "é": ["e"],
    "ì": ["i"],
    "ò": ["ɔ"],
    "ó": ["o"],
    "ù": ["u"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "tʃ"],  # /k/ before a,o,u; /tʃ/ before e,i
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "dʒ"],  # /ɡ/ before a,o,u; /dʒ/ before e,i
    "h": [""],  # always silent (disambiguates c/g)
    "j": ["j"],  # rare, older orthography / loanwords
    "k": ["k"],  # loanwords
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],  # only in ⟨qu⟩
    "r": ["r"],  # alveolar trill
    "s": ["s", "z"],  # /z/ before voiced C and intervocalic (N. Italy)
    "t": ["t"],
    "v": ["v"],
    "w": ["w"],  # loanwords
    "x": ["ks"],  # loanwords
    "y": ["i"],  # loanwords
    "z": ["ts", "dz"],  # distribution partly lexical

    # --- Consonant digraphs ---
    "ch": ["k"],  # hard c before e,i: ⟨che⟩, ⟨chi⟩
    "gh": ["ɡ"],  # hard g before e,i: ⟨ghe⟩, ⟨ghi⟩
    "ci": ["tʃ"],  # soft c before a,o,u: ⟨cia⟩, ⟨cio⟩, ⟨ciu⟩
    "gi": ["dʒ"],  # soft g before a,o,u: ⟨gia⟩, ⟨gio⟩, ⟨giu⟩
    "gl": ["ʎ"],  # before i: ⟨gli⟩
    "gn": ["ɲ"],
    "qu": ["kw"],
    "sc": ["ʃ", "sk"],  # /ʃ/ before e,i; /sk/ before a,o,u
    "ss": ["s"],  # always voiceless
    "zz": ["tts", "ddz"],  # geminate affricates

    # --- Geminate consonants (orthographic doubling) ---
    "bb": ["bː"], "cc": ["kk", "ttʃ"], "dd": ["dː"], "ff": ["fː"],
    "gg": ["ɡɡ", "ddʒ"], "ll": ["lː"], "mm": ["mː"], "nn": ["nː"],
    "pp": ["pː"], "rr": ["rː"], "tt": ["tː"], "vv": ["vː"],

    # --- Diphthongs (rising, with glide) ---
    "ia": ["ja"], "ie": ["je"], "io": ["jo"], "iu": ["ju"],
    "ua": ["wa"], "ue": ["we"], "uo": ["wɔ"], "ui": ["wi"],

    # --- Trigraph ---
    "sci": ["ʃ"],  # ⟨sci⟩ before a,o,u: ⟨scia⟩ → [ʃa]
    "gli": ["ʎi", "ʎ"],  # palatal lateral
}

ALLOPHONES = {
    "p": ["p"],
    "b": ["b"],
    "t": ["t", "t̪"],  # dental before dental
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

    "m": ["m", "ɱ"],  # labiodental before /f, v/
    "n": ["n", "m", "ɱ", "ŋ", "ɲ"],  # assimilates to following place
    "ɲ": ["ɲ"],
    "ŋ": ["ŋ"],  # allophone of /n/

    "l": ["l"],
    "ʎ": ["ʎ"],
    "r": ["r", "ɾ"],  # tap in fast speech / unstressed
    "j": ["j"],
    "w": ["w"],

    "a": ["a"],
    "e": ["e"],
    "ɛ": ["ɛ"],
    "i": ["i"],
    "o": ["o"],
    "ɔ": ["ɔ"],
    "u": ["u"],
}

SPECS = {
    "it": LanguageSpec(
        code="it",
        name="Italian",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="la",
        notes=(
            "Standard Italian (based on Florentine/Tuscan). "
            "Open/close mid-vowel distinction (e/ɛ, o/ɔ) is lexically "
            "determined and varies by region."
        ),
    ),
}
