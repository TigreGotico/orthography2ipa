"""Classical Greek / Ancient Attic (grc) — grapheme→IPA and allophone mappings.

Reconstructed pronunciation of Attic Greek (5th–4th c. BCE Athens),
the prestige dialect underlying the literary canon (Plato, Thucydides,
the tragedians). Koine developments noted where relevant.

Sources:
- Allen, W.S. (1968/1987). *Vox Graeca: A Guide to the Pronunciation
  of Classical Greek*. CUP.
- Sihler, A.L. (1995). *New Comparative Grammar of Greek and Latin*. OUP.
- Smyth, H.W. (1920). *A Greek Grammar for Colleges*. American Book Co.
- Probert, P. (2019). *Latin Grammarians on the Latin Accent*. OUP.

Conventions:
- ISO 639-2/3: grc (Ancient Greek), distinct from el (Modern Greek).
- Polytonic orthography (breathing marks, accents) included.
- ⟨φ θ χ⟩ are ASPIRATED STOPS [pʰ tʰ kʰ] in Classical Attic,
  NOT fricatives [f θ x] (that's post-Classical/Modern).
- Pitch accent system (not fully captured in segmental IPA).
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Vowels: short ---
    "α": ["a"],
    "ε": ["e"],
    "ι": ["i"],
    "ο": ["o"],
    "υ": ["y"],  # front rounded [y], NOT [u]

    # --- Vowels: long ---
    "η": ["ɛː"],  # open-mid long e
    "ω": ["ɔː"],  # open-mid long o
    "ᾱ": ["aː"],  # long alpha (macron, rare in texts)
    "ῑ": ["iː"],
    "ῡ": ["yː"],

    # --- Diphthongs ---
    "αι": ["aj"],
    "ει": ["eː"],  # by Classical period, monophthongised to [eː]
    "οι": ["oj"],
    "αυ": ["aw"],
    "ευ": ["ew"],
    "ου": ["oː"],  # by Classical period, monophthongised to [oː]
    "υι": ["yj"],
    "ηυ": ["ɛːw"],

    # --- Long diphthongs (with iota subscript) ---
    "ᾳ": ["aːj"],  # ᾱι → subscript
    "ῃ": ["ɛːj"],  # ηι → subscript
    "ῳ": ["ɔːj"],  # ωι → subscript

    # --- Consonants: voiceless stops ---
    "π": ["p"],
    "τ": ["t"],
    "κ": ["k"],

    # --- Consonants: voiced stops ---
    "β": ["b"],  # [b] in Classical, NOT [v]
    "δ": ["d"],  # [d] in Classical, NOT [ð]
    "γ": ["ɡ"],  # [ɡ] in Classical, NOT [ɣ]

    # --- Consonants: aspirated stops ---
    "φ": ["pʰ"],  # aspirated bilabial, NOT [f]
    "θ": ["tʰ"],  # aspirated dental, NOT [θ]
    "χ": ["kʰ"],  # aspirated velar, NOT [x]

    # --- Consonants: nasals ---
    "μ": ["m"],
    "ν": ["n"],

    # --- Consonants: liquids ---
    "λ": ["l"],
    "ρ": ["r"],  # probably trilled; initial ρ aspirated [r̥]

    # --- Consonants: fricative ---
    "σ": ["s"],  # voiceless alveolar (also ς final)
    "ς": ["s"],  # final sigma

    # --- Consonants: double letters ---
    "ζ": ["zd"],  # [zd] in early Attic; later [dz] or [zː]
    "ξ": ["ks"],
    "ψ": ["ps"],

    # --- Breathing marks ---
    # Rough breathing (spiritus asper) before vowels/rho
    "ἁ": ["ha"], "ἑ": ["he"], "ἱ": ["hi"], "ὁ": ["ho"], "ὑ": ["hy"],
    "ἡ": ["hɛː"], "ὡ": ["hɔː"],
    # Smooth breathing = no [h]
    "ἀ": ["a"], "ἐ": ["e"], "ἰ": ["i"], "ὀ": ["o"], "ὐ": ["y"],
    "ἠ": ["ɛː"], "ὠ": ["ɔː"],

    # --- Gamma nasals (γ before velars) ---
    "γγ": ["ŋɡ"],
    "γκ": ["ŋk"],
    "γχ": ["ŋkʰ"],
    "γξ": ["ŋks"],

    # --- Geminate stops ---
    "ππ": ["pː"],
    "ττ": ["tː"],
    "κκ": ["kː"],
    "ββ": ["bː"],
    "δδ": ["dː"],
    "γγ": ["ŋɡ"],  # NOT geminate [ɡː] — always nasal + stop
    "λλ": ["lː"],
    "μμ": ["mː"],
    "νν": ["nː"],
    "ρρ": ["rː"],  # or [r̥r] (deaspirated + voiced)
    "σσ": ["sː"],
}

ALLOPHONES = {
    # Voiceless stops
    "p": ["p"],
    "t": ["t"],
    "k": ["k"],

    # Voiced stops (NO fricative allophones in Classical — that's Koine+)
    "b": ["b"],
    "d": ["d"],
    "ɡ": ["ɡ"],

    # Aspirated stops
    "pʰ": ["pʰ"],
    "tʰ": ["tʰ"],
    "kʰ": ["kʰ"],

    # Fricative
    "s": ["s", "z"],  # [z] before voiced consonants only

    # Nasals
    "m": ["m"],
    "n": ["n", "ŋ", "ɱ"],  # assimilates to following C
    "ŋ": ["ŋ"],  # gamma-nasal before velars

    # Liquids
    "l": ["l"],
    "r": ["r", "r̥"],  # [r̥] word-initial (rough breathing on ρ)

    # Glides
    "j": ["j"],  # offglide in diphthongs
    "w": ["w"],  # lost in Attic but present in dialects (digamma)

    # Laryngeal
    "h": ["h"],  # from rough breathing

    # Short vowels
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "y": ["y"],  # front rounded

    # Long vowels
    "aː": ["aː"],
    "eː": ["eː"],
    "ɛː": ["ɛː"],
    "iː": ["iː"],
    "oː": ["oː"],
    "ɔː": ["ɔː"],
    "yː": ["yː"],

    # Geminates
    "pː": ["pː"], "tː": ["tː"], "kː": ["kː"],
    "bː": ["bː"], "dː": ["dː"],
    "lː": ["lː"], "mː": ["mː"], "nː": ["nː"],
    "rː": ["rː"], "sː": ["sː"],
}

SPECS = {
    "grc": LanguageSpec(
        code="grc",
        name="Classical Greek (Attic)",
        family="Hellenic",
        script="Greek",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="ine",
        notes=(
            "Reconstructed Classical Attic Greek (5th–4th c. BCE) per "
            "Allen (1968). Key features: (1) ⟨φ θ χ⟩ = aspirated stops "
            "[pʰ tʰ kʰ], NOT fricatives. (2) ⟨β δ γ⟩ = voiced stops "
            "[b d ɡ], NOT fricatives. (3) ⟨υ⟩ = front rounded [y]. "
            "(4) ⟨ζ⟩ = [zd]. (5) ⟨ει ου⟩ already monophthongised to "
            "[eː oː]. (6) Pitch accent (not captured segmentally). "
            "(7) Rough breathing = [h]. (8) ⟨γ⟩ before velars = [ŋ]. "
            "(9) Geminate consonants phonemic. (10) /r/ probably trilled, "
            "voiceless word-initially [r̥]."
        ),
    ),
}
