"""Classical Latin (la) — grapheme→IPA and allophone mappings.

Reconstructed pronunciation of literary Latin (1st c. BCE – 2nd c. CE),
the "Golden/Silver Age" standard. NOT ecclesiastical/medieval pronunciation.

The reconstruction is well-established from: grammarian testimony (Priscian,
Quintilian, Varro), loanword evidence into Greek/Germanic/Celtic, Romance
comparative evidence, inscriptional misspellings, and metrical patterns.

Sources:
- Allen, W.S. (1965/2003). *Vox Latina: A Guide to the Pronunciation
  of Classical Latin*. CUP. [the standard reference]
- Sihler, A.L. (1995). *New Comparative Grammar of Greek and Latin*. OUP.
- Clackson, J. & Horrocks, G. (2007). *The Blackwell History of the
  Latin Language*. Blackwell.
- Weiss, M. (2020). *Outline of the Historical and Comparative Grammar
  of Latin*. 2nd ed. Beech Stave Press.

Conventions:
- ISO 639-2/3: la / lat.
- Vowel length is PHONEMIC: ⟨a⟩ = short, ⟨ā⟩ = long (macron notation).
- ⟨c⟩ is ALWAYS [k]; ⟨g⟩ is ALWAYS [ɡ].
- ⟨v⟩ represents the semivowel [w] (no labiodental [v] in Classical Latin).
- ⟨i⟩ can be vowel [ɪ] or semivowel [j].
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Short vowels ---
    "a": ["a"],
    "e": ["ɛ"],
    "i": ["ɪ"],
    "o": ["ɔ"],
    "u": ["ʊ"],
    "y": ["ʏ"],  # Greek loanwords only (< υ)

    # --- Long vowels (macron notation) ---
    "ā": ["aː"],
    "ē": ["eː"],
    "ī": ["iː"],
    "ō": ["oː"],
    "ū": ["uː"],
    "ȳ": ["yː"],  # Greek loanwords

    # --- Diphthongs ---
    "ae": ["aj"],  # monophthongised to [ɛː] only in Vulgar Latin
    "oe": ["oj"],  # monophthongised to [eː] only in Vulgar Latin
    "au": ["aw"],  # preserved even into Romance
    "ei": ["ej"],  # archaic, rare in Classical
    "eu": ["ew"],  # rare, mainly Greek loans
    "ui": ["uj"],  # rare (huic, cui)

    # --- Consonants ---
    "b": ["b"],
    "c": ["k"],  # ALWAYS [k] — no palatalisation
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ"],  # ALWAYS [ɡ] — no palatalisation
    "h": ["h"],  # weak aspirate, increasingly lost
    "k": ["k"],  # archaic spelling (Kalendae)
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],  # only in ⟨qu⟩ = [kʷ]
    "r": ["r"],  # alveolar trill
    "s": ["s"],  # always voiceless
    "t": ["t"],
    "v": ["w"],  # labial-velar approximant, NOT [v]
    "x": ["ks"],  # always [ks]
    "z": ["dz"],  # Greek loanwords (< ζ)

    # --- Digraphs ---
    "qu": ["kʷ"],  # labiovelar stop
    "gu": ["ɡʷ"],  # after n: sanguis [ˈsaŋɡʷɪs]
    "ch": ["kʰ"],  # Greek loanwords (< χ)
    "ph": ["pʰ"],  # Greek loanwords (< φ)
    "th": ["tʰ"],  # Greek loanwords (< θ)
    "rh": ["r"],  # Greek loanwords (< ῥ), = [r]
    "bs": ["ps"],  # assimilation: urbs [ʊrps]
    "bt": ["pt"],  # assimilation: obtineō [ɔptɪˈnɛoː]

    # --- Geminate consonants (phonemic in Latin) ---
    "bb": ["bː"],
    "cc": ["kː"],
    "dd": ["dː"],
    "ff": ["fː"],
    "gg": ["ɡː"],
    "ll": ["lː"],
    "mm": ["mː"],
    "nn": ["nː"],
    "pp": ["pː"],
    "rr": ["rː"],
    "ss": ["sː"],
    "tt": ["tː"],

    # --- Semivowel ⟨i⟩ before vowel ---
    "j": ["j"],  # consonantal i (iam = [jam])
    "i": ["ɪ", "j"],  # vowel or glide depending on position
}

ALLOPHONES = {
    # Stops — no allophonic lenition (unlike Romance descendants)
    "p": ["p"],
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "k": ["k"],
    "ɡ": ["ɡ"],

    # Aspirated stops (Greek loans only)
    "pʰ": ["pʰ"],
    "tʰ": ["tʰ"],
    "kʰ": ["kʰ"],

    # Labiovelars
    "kʷ": ["kʷ"],
    "ɡʷ": ["ɡʷ"],

    # Fricatives
    "f": ["f"],
    "s": ["s"],  # always voiceless in Classical
    "h": ["h", "∅"],  # increasingly lost in speech

    # Nasals
    "m": ["m", "∅"],  # word-final -m weakened (nasalised preceding V)
    "n": ["n", "ŋ", "ɱ"],  # assimilates to following C place
    "ɲ": ["ɲ"],  # gn = [ŋn] or [ɲ]

    # Liquids
    "l": ["l", "ɫ"],  # possibly velarised in coda
    "r": ["r"],  # always trilled

    # Glides
    "w": ["w"],
    "j": ["j"],

    # Short vowels
    "a": ["a"],
    "ɛ": ["ɛ"],
    "ɪ": ["ɪ"],
    "ɔ": ["ɔ"],
    "ʊ": ["ʊ"],
    "ʏ": ["ʏ"],

    # Long vowels
    "aː": ["aː"],
    "eː": ["eː"],
    "iː": ["iː"],
    "oː": ["oː"],
    "uː": ["uː"],
    "yː": ["yː"],

    # Geminates
    "bː": ["bː"], "kː": ["kː"], "dː": ["dː"], "fː": ["fː"],
    "ɡː": ["ɡː"], "lː": ["lː"], "mː": ["mː"], "nː": ["nː"],
    "pː": ["pː"], "rː": ["rː"], "sː": ["sː"], "tː": ["tː"],
}

SPECS = {
    "la": LanguageSpec(
        code="la",
        name="Classical Latin",
        family="Italic",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="ine",
        notes=(
            "Reconstructed Classical Latin pronunciation (1st c. BCE – "
            "2nd c. CE) per Allen (1965/2003). Key features: (1) ⟨c⟩ always "
            "[k], ⟨g⟩ always [ɡ] — NO palatalisation. (2) ⟨v⟩ = [w], NOT "
            "[v]. (3) Vowel length phonemic (5 short + 5 long + 2 Greek). "
            "(4) Diphthongs [aj, oj, aw] preserved. (5) Geminate consonants "
            "phonemic. (6) Aspirated stops only in Greek loans. (7) Word-"
            "final -m weakened (probably nasalised vowel). (8) /h/ weak. "
            "(9) /s/ always voiceless. (10) /r/ always trilled."
        ),
    ),
}
