"""Aragonese (an) — grapheme→IPA and allophone mappings.

Aragonese (Aragonés) is a Romance language spoken in the Pyrenean valleys
of the province of Huesca, Aragon, Spain. ~10,000–25,000 speakers.
UNESCO classified as "definitely endangered."

Sources:
- Academia de l'Aragonés (2017). *Ortografía de l'Aragonés*.
  Edicions Publicacions d'o Consello d'a Fabla Aragonesa. ISBN 978-84-8127-285-5.
  [PRIMARY SOURCE for grapheme→phoneme mappings in this module]
- Nagore Laín, F. (1986). *El aragonés de Panticosa*.
- Tomás Arias, C. (1999). *El aragonés del Biello Sobrarbe*.
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

# ═══════════════════════════════════════════════════════════════════════════
# Standard / Central Aragonese
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_AN = {
    # --- Vowels (5-vowel system, §1.1) ---
    # Standard Aragonese has a 5-vowel system /a e i o u/.
    # Eastern (Benasquese) adds /ɛ/ and /ɔ/ (7-vowel, like Catalan).
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],
    # Accented vowels — same phonemes, stress marking only (§3)
    "á": ["a"], "é": ["e"], "í": ["i"], "ó": ["o"], "ú": ["u"],

    # --- Consonants (§1.2) ---

    # §1.2.1 B — /b/ (occlusive [b] or approximant [β])
    "b": ["b"],

    # §1.2.2 C — /k/ before a,o,u,r,l,ll; /θ/ before e,i
    "c": ["k", "θ"],

    # §1.2.2 CH — palatal affricate /tʃ/
    "ch": ["tʃ"],

    # §1.2.3 D — /d/ (occlusive [d] or approximant [ð])
    "d": ["d"],

    # §1.2.4 F — labiodental fricative /f/
    "f": ["f"],

    # §1.2.5 G — velar stop /ɡ/ before a,o,u,r,l,ll
    # <gu> before e,i also represents /ɡ/
    "g": ["ɡ"],

    # §1.2.6 H — silent (etymological)
    "h": [""],

    # §1.2.7 J — velar fricative /x/
    # NOTE: In traditional Aragonese the reflex of Latin J- was /tʃ/ or /ʃ/,
    # but the orthography prescribes <j> for the Castilianised /x/ sound.
    # Traditional /tʃ/ is written <ch> and /ʃ/ is written <x>/<ix>.
    "j": ["x"],

    # §1.2.8 K — /k/ (only in foreign/technical terms)
    "k": ["k"],

    # §1.2.9 L — alveolar lateral /l/
    "l": ["l"],

    # §1.2.9 LL — palatal lateral /ʎ/ (conservative, no yeísmo)
    "ll": ["ʎ"],

    # §1.2.10 M — bilabial nasal /m/
    "m": ["m"],

    # §1.2.11 N — alveolar nasal /n/
    "n": ["n"],

    # §1.2.11 NN — geminate nasal [nː] (Belsetán, some toponyms)
    "nn": ["nː"],

    # §1.2.12 NY/Ñ — palatal nasal /ɲ/
    "ny": ["ɲ"],
    "ñ": ["ɲ"],

    # §1.2.13 P — bilabial stop /p/
    "p": ["p"],

    # §1.2.14 QU — /k/ before e,i
    "qu": ["k"],

    # §1.2.15 R — simple vibrant /ɾ/ intervocalically, after/before consonant
    "r": ["ɾ"],

    # §1.2.15 RR — multiple vibrant /r/ intervocalically
    "rr": ["r"],

    # §1.2.16 S — alveolar fricative /s/ (apico-alveolar [s̺])
    "s": ["s"],

    # §1.2.17 T — dental stop /t/
    "t": ["t"],

    # §1.2.18 V — /b/ (betacism, etymological distribution only)
    "v": ["b"],

    # §1.2.19 W — only in foreign words
    "w": ["w"],

    # §1.2.20 X, IX — prepalatal fricative /ʃ/
    # <x> in initial position or after consonant/semivowel/i
    # <ix> after vowels a,e,o,u
    "x": ["ʃ"],
    "ix": ["ʃ"],

    # §1.2.21 Y — palatal fricative /ʝ/
    "y": ["ʝ"],

    # §1.2.22 Z — interdental fricative /θ/ before a,o,u, before liquids,
    # and in coda position
    "z": ["θ"],

    # §1.2.5 GU — /ɡ/ before e,i
    "gu": ["ɡ"],

    # §1.2.5 GÜ — /ɡw/ before e,i (dieresis marks pronounced u)
    "gü": ["ɡw"],

    # §1.2.9 L·L — geminate lateral [lː] (Belsetán)
    "l·l": ["lː"],

    # --- Diphthongs (Aragonese retains Lat. Ĕ/Ŏ diphthongs) ---
    # Rising diphthongs
    "ue": ["we"],   # Lat. Ŏ: puerta, fuent, cuerpo
    "ie": ["je"],   # Lat. Ĕ: tierra, fiero, siete
    "ua": ["wa"], "uo": ["wo"],
    "ia": ["ja"], "io": ["jo"], "iu": ["ju"],
    # Falling diphthongs
    "ai": ["aj"], "ei": ["ej"], "oi": ["oj"],
    "au": ["aw"], "eu": ["ew"], "ou": ["ow"],
    "ui": ["wi"],
}

ALLOPHONES_AN = {
    # Stops with lenition allophones (standard Ibero-Romance pattern)
    "p": ["p"],
    "b": ["b", "β"],       # [β] approximant in lenition contexts
    "t": ["t"],
    "d": ["d", "ð", "∅"],  # [ð] approximant, [∅] in some intervocalic dialects
    "k": ["k"],
    "ɡ": ["ɡ", "ɣ"],       # [ɣ] approximant in lenition contexts

    # Fricatives
    "f": ["f"],
    "θ": ["θ"],
    "s": ["s̺"],             # apico-alveolar (§1.2.16)
    "x": ["x"],             # velar fricative for <j>
    "ʃ": ["ʃ"],             # prepalatal for <x>/<ix>
    "ʝ": ["ʝ"],             # palatal fricative for <y>

    # Affricate
    "tʃ": ["tʃ"],

    # Nasals
    "m": ["m"],
    "n": ["n", "ŋ", "ɱ"],  # assimilation: [ŋ] before velars, [ɱ] before f
    "nː": ["nː"],          # geminate (Belsetán)
    "ɲ": ["ɲ"],

    # Laterals
    "l": ["l"],
    "lː": ["lː"],          # geminate (Belsetán)
    "ʎ": ["ʎ"],             # conservative: palatal lateral (no yeísmo)

    # Rhotics
    "ɾ": ["ɾ", "∅"],       # [∅] in some coda/final positions (§1.2.15)
    "r": ["r"],

    # Glides
    "j": ["j"],
    "w": ["w"],

    # Vowels (5-vowel system for central/standard)
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Positional graphemes — Aragonese
# ═══════════════════════════════════════════════════════════════════════════
#
# Standard Ibero-Romance lenition for voiced stops plus:
# - R: trill word-initially, tap elsewhere
# - D: weakening/deletion in intervocalic and word-final positions
# - T: variable realisation word-finally [t]~[ð]~[ɾ]~[∅] (§1.2.17)

POSITIONAL_AN = {
    "b": {
        GP.DEFAULT: ["b"],
        GP.INTERVOCALIC: ["β"],
    },
    "d": {
        GP.DEFAULT: ["d"],
        GP.INTERVOCALIC: ["ð"],
        GP.WORD_FINAL: ["∅"],     # §1.2.3: muda in gerunds -nd, many dialects
    },
    "g": {
        GP.DEFAULT: ["ɡ"],
        GP.INTERVOCALIC: ["ɣ"],
    },
    "r": {
        GP.WORD_INITIAL: ["r"],   # §1.2.15: word-initial <r> = trill /r/
        GP.INTERVOCALIC: ["ɾ"],
        GP.ONSET: ["ɾ"],          # after/before consonants
        GP.CODA: ["ɾ"],
        GP.WORD_FINAL: ["ɾ", "∅"],  # §1.2.15: final -r may be silent
    },
    "t": {
        GP.DEFAULT: ["t"],
        GP.WORD_FINAL: ["t", "ð", "ɾ", "∅"],  # §1.2.17: variable final -t
    },
}

# ═══════════════════════════════════════════════════════════════════════════
# Eastern Aragonese (Benasquese / Ribagorçan)
# ═══════════════════════════════════════════════════════════════════════════
#
# Key differences from central:
# - 7-vowel system: /ɛ/ and /ɔ/ (Catalan influence)
# - <z> and <ce>/<ci> → /s/ (not /θ/) — seseo (§1.2.2, §1.2.22)
# - Voiced affricate [dʒ] for Latin G/J before front vowels
# - Some yeísmo: /ʎ/ → [j] in some speakers
# - Palatalised [ʎ] realisations of <l> in clusters (§1.2.9)
# - Plurals in -ts instead of -z (§1.2.22)

GRAPHEMES_AN_E = {
    **GRAPHEMES_AN,
    # 7-vowel system
    "e": ["e", "ɛ"],
    "o": ["o", "ɔ"],
    # Catalan-influenced affricate
    "j": ["dʒ", "x"],          # [dʒ] traditional, [x] Castilianised
    "g": ["ɡ", "dʒ"],          # [dʒ] before e,i (Catalan pattern)
    # Seseo: <z>, <ce>, <ci> → /s/
    "z": ["s"],
    "c": ["k", "s"],            # /s/ before e,i instead of /θ/
    # Possible yeísmo
    "ll": ["ʎ", "j"],
}

ALLOPHONES_AN_E = {
    **ALLOPHONES_AN,
    "dʒ": ["dʒ"],              # Catalan-like voiced affricate
    "ʎ": ["ʎ", "j"],           # partial yeísmo
    "ɛ": ["ɛ"],
    "ɔ": ["ɔ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SPECS
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "an": LanguageSpec(
        code="an",
        name="Aragonese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_AN,
        allophones=ALLOPHONES_AN,
        positional_graphemes=POSITIONAL_AN,
        parent="la-x-hispania",
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
            "(no yeísmo), voiceless prepalatal [ʃ] for ⟨x⟩/⟨ix⟩. "
            "Retains Latin F- in most positions (unlike Castilian). "
            "Latin -LL- → [ʎ], -NN- → [ɲ]. <j> = /x/ (Castilian "
            "influence); traditional Aragonese reflexes use <ch> [tʃ] "
            "and <x> [ʃ]. UNESCO 'definitely endangered'."
        ),
    ),
    "an-x-occidental": LanguageSpec(
        code="an-x-occidental",
        name="Western Aragonese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_AN,
        allophones=ALLOPHONES_AN,
        positional_graphemes=POSITIONAL_AN,
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
        positional_graphemes=POSITIONAL_AN,
        parent="an",
        notes=(
            "Eastern Aragonese / Ribagorçan / Benasquese transition zone. "
            "Catalan influence: voiced affricate [dʒ] for Latin G/J before "
            "front vowels, possible partial yeísmo. 7-vowel system with "
            "/ɛ/ and /ɔ/. Seseo: /θ/ → /s/. Transitional phonology "
            "between Aragonese and Catalan, debated classification."
        ),
    ),
}