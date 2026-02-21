"""Rionorês (ast-PT-x-rionor) — grapheme→IPA and allophone mappings.

Rionorês is a moribund Leonese dialect spoken in Rio de Onor, a twin village
straddling the Portuguese–Spanish border in Bragança district. ~0–5 active
speakers (2003). No standardised orthography.

Sources:
- Macias, D.R. (2003). *Dialecto Rionorês: Contributo para o seu estudo*.
  IPB, Bragança (Série Estudos, 64).
- Carvalho, J.H. & Dias, J. (1955). *O Falar de Rio de Onor*.
- Dias, J. (1984). *Rio de Onor: Comunitarismo Agro-Pastoril*. Ed. Presença.

Conventions:
- Code ast-PT-x-rionor: ast = Asturleonese macro-language (ISO 639-3),
  PT = Portugal, x-rionor = private-use subtag for Rio de Onor.
- Orthography follows Portuguese-based transcription conventions from
  Macias (2003) — no standardised system exists.
- IPA transcriptions are reconstructed from comparative Leonese phonology.
- Key features: betacism, affricate [tʃ] for Pt. [ʃ], Leonese diphthongs
  (Ĕ → [je], Ŏ → [wo]/[wa]), article ⟨al⟩, x- for j- [ʃ].
"""
from orthography2ipa.languages.ast import POSITIONAL_AST
from orthography2ipa.types import LanguageSpec

GRAPHEMES_RION = {
    # --- Single vowels ---
    "a": ["a", "ɐ"],
    "e": ["e", "ɛ"],
    "i": ["i"],
    "o": ["o", "ɔ"],
    "u": ["u"],

    # --- Accented vowels ---
    "á": ["a"],
    "é": ["ɛ"],
    "ê": ["e"],
    "í": ["i"],
    "ó": ["ɔ"],
    "ô": ["o"],
    "ú": ["u"],

    # --- Single consonants ---
    "b": ["b"],  # covers all /b/ and /v/ (betacism)
    "c": ["k", "s"],
    "ç": ["s"],
    "d": ["d"],  # intervocalic -d- frequently syncopated
    "f": ["f"],
    "g": ["ɡ", "ʒ"],
    "h": [""],  # silent
    "j": ["ʒ"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],
    "r": ["r", "ɾ"],  # trill initial; tap intervocalic
    "s": ["s", "z"],
    "t": ["t"],
    "v": ["b"],  # betacism
    "x": ["ʃ"],  # x- replaces j- [ʃ]: xusticia, xardineiro
    "z": ["z", "ʃ"],

    # --- Consonant digraphs ---
    "ch": ["ʃ"],
    "lh": ["ʎ"],  # palatal lateral (L-palatalization unclear in Rionorês)
    "nh": ["ɲ"],
    "rr": ["r"],
    "ss": ["s"],
    "qu": ["k", "kw"],
    "gu": ["ɡ", "ɡw"],
    "tch": ["tʃ"],  # affricate — hallmark Rionorês: tchamar, otcho, matchada

    # --- Leonese diphthongs ---
    # Ĕ → ie [je]
    "ie": ["je"],  # piedra, pierna, baliente, iera
    "iê": ["je"],  # iêl, iêla
    # Ŏ → uô [wo] / uâ [wa]
    "uô": ["wo"],  # puonte, fuôra, ruôdra
    "uâ": ["wa"],  # puârta, fuarça, muartu

    # --- Falling diphthongs ---
    "ai": ["aj"],  # mai, hai, bai
    "au": ["aw"],  # irmau, pasmau, mau
    "ei": ["ej"],  # beio
    "iu": ["ju"],  # riu, tiu, friu
    "ou": ["ow"],  # dou, bou, cousa

    # --- Nasal patterns ---
    # Rionorês uses oral vowel + nasal consonant rather than nasal diphthongs:
    # pan /pan/ (not /pɐ̃w̃/), man /man/, fonun /fonun/
    "ão": ["aw"],  # denasalised: irmau (irmão)
    "ãe": ["aj"],  # denasalised: mai (mãe)
}

ALLOPHONES_RION = {
    # Plosives
    "p": ["p"],
    "b": ["b", "β"],  # intervocalic lenition
    "t": ["t"],
    "d": ["d", "ð", "∅"],  # intervocalic lenition; syncope common
    "k": ["k"],
    "ɡ": ["ɡ", "ɣ"],

    # Fricatives
    "f": ["f"],
    "s": ["s"],
    "z": ["z"],
    "ʃ": ["ʃ"],  # from x- series (dixu, xusticia) and coda
    "ʒ": ["ʒ"],

    # Affricate
    "tʃ": ["tʃ"],  # hallmark: tchamar, escatchar, matchada, martchar, otcho

    # Rhotics
    "r": ["r"],  # alveolar trill
    "ɾ": ["ɾ"],  # alveolar tap

    # Nasals
    "m": ["m"],
    "n": ["n"],
    "ɲ": ["ɲ"],

    # Laterals
    "l": ["l"],
    "ʎ": ["ʎ"],  # status unclear in Rionorês (L-palatalization uncertain)

    # Glides
    "w": ["w"],
    "j": ["j"],

    # Oral vowels
    "a": ["a"],
    "ɐ": ["ɐ"],
    "e": ["e"],
    "ɛ": ["ɛ"],
    "i": ["i"],
    "o": ["o"],
    "ɔ": ["ɔ"],
    "u": ["u"],

    # Nasal vowels (less systematic than Portuguese)
    "ɐ̃": ["ɐ̃"],
    "ẽ": ["ẽ"],
    "ĩ": ["ĩ"],
    "õ": ["õ"],
    "ũ": ["ũ"],
}

POSITIONAL_RIONORESE = {**POSITIONAL_AST}

SPECS = {
    "ast-PT-x-rionor": LanguageSpec(
        code="ast-PT-x-rionor",
        name="Rionorês",
        family="Asturleonese",
        script="Latin",
        graphemes=GRAPHEMES_RION,
        allophones=ALLOPHONES_RION,
        positional_graphemes=POSITIONAL_RIONORESE,
        parent="ast",
        notes=(
            "Moribund Leonese dialect of Rio de Onor, Bragança. ~0–5 active "
            "speakers (2003). Key features: betacism (/v/→[b]), voiceless "
            "postalveolar affricate [tʃ] replacing Pt. [ʃ] (tchamar, otcho, "
            "matchada), x- for j- [ʃ] (xusticia, dixu — Leonese sibilant "
            "merger), Leonese diphthongs (Ĕ → [je] piedra, Ŏ → [wo]/[wa] "
            "puonte/puârta), masculine definite article ⟨al⟩ (most archaic "
            "in Asturleonese continuum), 3pl preterite in -nun (matanun, "
            "fonum), imperfect -aba (not -ava), Leonese negator ⟨nun⟩, "
            "denasalised -ão → -au (irmau, mau), intervocalic -d- syncope "
            "(pasmau, tchamau), 2sg preterite palatalization (matêste). "
            "Stronger Castilian influence than Guadramilês due to border "
            "position. No standardised orthography; IPA is reconstructed."
        ),
    ),
}
