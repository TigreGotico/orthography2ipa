"""Germanic historical languages — Proto-Germanic and Gothic.

Proto-Germanic is the reconstructed ancestor of all Germanic languages.
Gothic is the earliest well-attested Germanic language (Wulfila's Bible,
4th c. CE) and the language of the Visigoths who ruled Iberia 5th–8th c.

Sources:
- Ringe, D. (2006). *From Proto-Indo-European to Proto-Germanic*. OUP.
- Kroonen, G. (2013). *Etymological Dictionary of Proto-Germanic*. Brill.
- Wright, J. (1910/1954). *Grammar of the Gothic Language*. OUP.
- Braune, W. & Heidermanns, F. (2018). *Gotische Grammatik*. 21st ed. Niemeyer.
- Bennett, W.H. (1980). *An Introduction to the Gothic Language*. MLA.
"""
from orthography2ipa.types import LanguageSpec

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-GERMANIC (gem)
# ═══════════════════════════════════════════════════════════════════════════
#
# Time: ~500 BCE – 1st c. CE (approximate)
# Reconstruction: Very well-established from comparison of Gothic,
#   Old Norse, Old English, Old High German, Old Saxon, Old Frisian.
#
# DEFINING SOUND CHANGES from PIE (Grimm's and Verner's Laws):
#
# GRIMM'S LAW (Germanic Consonant Shift):
#   PIE *p t k kʷ → PGmc *f θ x xʷ (voiceless stops → fricatives)
#   PIE *b d g gʷ → PGmc *p t k kʷ (voiced stops → voiceless stops)
#   PIE *bʰ dʰ gʰ gʷʰ → PGmc *β ð ɣ ɣʷ (breathy → voiced fricatives)
#     These *β *ð *ɣ later → *b *d *g word-initially.
#
# VERNER'S LAW (applies after Grimm's):
#   *f θ x xʷ s → *β ð ɣ ɣʷ z (when PIE accent was not on immediately
#     preceding syllable)
#
# Other major changes:
#   - Fixed initial stress accent (replacing PIE mobile pitch accent)
#   - PIE *ē → *ā (ē₁-lowering)
#   - PIE *o → *a (merger of short *a and *o)
#   - Development of *ē₂ (a new long ē, origin debated)

GRAPHEMES_GEM = {
    # --- Short vowels ---
    "a": ["ɑ"],  # < PIE *a AND *o (merged)
    "e": ["e"],
    "i": ["i"],
    "u": ["u"],

    # --- Long vowels ---
    "ā": ["ɑː"],  # < PIE *ā and *ō (merged) and PIE *ē (Grimm)
    "ē": ["eː"],  # ē₂ — origin debated; rare
    "ī": ["iː"],
    "ō": ["oː"],  # < PIE *ōw and various sources
    "ū": ["uː"],

    # --- Diphthongs ---
    "ai": ["ɑj"],
    "au": ["ɑw"],
    "eu": ["ew"],
    "iu": ["iw"],

    # --- Stops (AFTER Grimm's Law) ---
    "p": ["p"],  # < PIE *b (rare) / Grimm's *d > *t > hardened
    "t": ["t"],
    "k": ["k"],
    "kʷ": ["kʷ"],
    "b": ["b"],  # < PIE *bʰ (word-initial hardening of *β)
    "d": ["d"],  # < PIE *dʰ (word-initial hardening of *ð)
    "g": ["ɡ"],  # < PIE *gʰ (word-initial hardening of *ɣ)
    "gʷ": ["ɡʷ"],

    # --- Fricatives (THE Grimm's Law outputs) ---
    "f": ["ɸ"],  # < PIE *p (Grimm's Law); bilabial [ɸ] at this stage
    "þ": ["θ"],  # < PIE *t (Grimm's Law)
    "h": ["x"],  # < PIE *k (Grimm's Law); velar [x], glottal [h] allophone
    "hʷ": ["xʷ"],  # < PIE *kʷ (Grimm's Law)
    "s": ["s"],
    "z": ["z"],  # < Verner's Law *s → *z

    # --- Nasals ---
    "m": ["m"],
    "n": ["n"],

    # --- Liquids ---
    "l": ["l"],
    "r": ["r"],  # probably alveolar trill

    # --- Glides ---
    "w": ["w"],
    "j": ["j"],

    # --- Geminates ---
    "pp": ["pː"], "tt": ["tː"], "kk": ["kː"],
    "ff": ["ɸː"], "ss": ["sː"],
    "ll": ["lː"], "mm": ["mː"], "nn": ["nː"], "rr": ["rː"],
}

ALLOPHONES_GEM = {
    # Stops
    "p": ["p"],
    "t": ["t"],
    "k": ["k"],
    "kʷ": ["kʷ"],
    "b": ["b", "β"],  # [β] medially (Grimm's *bʰ > *β; hardened initially)
    "d": ["d", "ð"],  # [ð] medially
    "ɡ": ["ɡ", "ɣ"],  # [ɣ] medially
    "ɡʷ": ["ɡʷ"],

    # Fricatives
    "ɸ": ["ɸ", "f"],  # → [f] labiodental in later stages
    "θ": ["θ"],
    "x": ["x", "h"],  # [h] word-initially (still [x] elsewhere)
    "xʷ": ["xʷ", "hʷ"],
    "s": ["s"],
    "z": ["z"],

    # Nasals
    "m": ["m"],
    "n": ["n", "ŋ"],

    # Liquids
    "l": ["l"],
    "r": ["r"],

    # Glides
    "w": ["w"],
    "j": ["j"],

    # Vowels
    "ɑ": ["ɑ"], "e": ["e"], "i": ["i"], "u": ["u"],
    "ɑː": ["ɑː"], "eː": ["eː"], "iː": ["iː"], "oː": ["oː"], "uː": ["uː"],

    # Geminates
    "pː": ["pː"], "tː": ["tː"], "kː": ["kː"],
    "ɸː": ["ɸː"], "sː": ["sː"],
    "lː": ["lː"], "mː": ["mː"], "nː": ["nː"], "rː": ["rː"],
}

# ═══════════════════════════════════════════════════════════════════════════
# GOTHIC (got)
# ═══════════════════════════════════════════════════════════════════════════
#
# Classification: Germanic > East Germanic
# Attestation: EXCELLENT — Wulfila's Bible translation (4th c. CE)
#   - Codex Argenteus (most complete, Uppsala)
#   - Codex Carolinus, Codex Ambrosianus, etc.
#   - Skeireins (commentary on John)
#   - Some deeds and calendar fragments
# Script: Gothic alphabet (created by Wulfila from Greek + Latin + runic)
# Time: 4th century CE text; spoken in Iberia 5th–8th c.
# Geography: Originally Balkans; Visigoths in Iberia 5th–8th c.
#   The Visigoths ruled Iberia from ~470 to 711 (Arab conquest).
#   Gothic loanwords in Ibero-Romance: guerra, guardar, ropa, etc.
#
# PHONOLOGICAL SYSTEM (well-established from the writing system):
#   - 5 short vowels + 2 long + diphthongs
#   - Grimm's Law outputs fully developed
#   - Voiced fricatives [β ð ɣ] as allophones of /b d g/
#   - No High German consonant shift (Gothic is conservative)
#   - /w/ from PIE *w and Grimm's *gʷ

GRAPHEMES_GOT = {
    # --- Short vowels ---
    "a": ["ɑ"],
    "i": ["ɪ"],
    "u": ["ʊ"],

    # --- Long vowels ---
    # Gothic spelling: ⟨ei⟩ = /iː/, ⟨o⟩ = /oː/ (always long)
    "e": ["eː"],  # ⟨e⟩ is always long in Gothic
    "o": ["oː"],  # ⟨o⟩ is always long in Gothic
    "ei": ["iː"],  # digraph for long /iː/
    "iu": ["iw"],  # diphthong

    # --- Diphthongs ---
    "ai": ["ɛ", "ɑj"],  # [ɛ] before r/h/ƕ; [ɑj] elsewhere
    "au": ["ɔ", "ɑw"],  # [ɔ] before r/h/ƕ; [ɑw] elsewhere

    # --- Stops ---
    "p": ["p"],
    "t": ["t"],
    "k": ["k"],
    "q": ["kʷ"],  # labiovelar (from ⟨𐌵⟩ = qairþra)
    "b": ["b"],
    "d": ["d"],
    "g": ["ɡ"],

    # --- Fricatives ---
    "f": ["f"],  # < PGmc *ɸ → [f]
    "þ": ["θ"],  # thorn (from Gothic alphabet)
    "s": ["s"],
    "z": ["z"],
    "h": ["h", "x"],  # [h] initially; [x] medially/finally
    "ƕ": ["xʷ"],  # ⟨𐍈⟩ hwair — labiovelar fricative

    # --- Nasals ---
    "m": ["m"],
    "n": ["n"],

    # --- Liquids ---
    "l": ["l"],
    "r": ["r"],

    # --- Glides ---
    "w": ["w"],
    "j": ["j"],

    # --- Geminates ---
    "gg": ["ŋɡ"],  # ⟨gg⟩ = [ŋɡ] (nasal + stop)
    "kk": ["kː"],
    "ll": ["lː"],
    "mm": ["mː"],
    "nn": ["nː"],
    "rr": ["rː"],
    "ss": ["sː"],
    "tt": ["tː"],
}

ALLOPHONES_GOT = {
    # Stops — spirantisation medially (like all early Germanic)
    "p": ["p"],
    "t": ["t"],
    "k": ["k"],
    "kʷ": ["kʷ"],
    "b": ["b", "β"],  # [β] between vowels
    "d": ["d", "ð"],  # [ð] between vowels
    "ɡ": ["ɡ", "ɣ"],  # [ɣ] between vowels; [ŋ] before nasals

    # Fricatives
    "f": ["f", "v"],  # [v] between voiced sounds (some analyses)
    "θ": ["θ"],  # probably no voiced allophone
    "s": ["s", "z"],  # [z] before voiced C (assimilation)
    "z": ["z"],
    "h": ["h", "x"],
    "xʷ": ["xʷ", "hʷ"],

    # Nasals
    "m": ["m"],
    "n": ["n", "ŋ"],  # [ŋ] before velars

    # Liquids
    "l": ["l"],
    "r": ["r"],

    # Glides
    "w": ["w"],
    "j": ["j"],

    # Vowels
    "ɑ": ["ɑ"], "ɪ": ["ɪ"], "ʊ": ["ʊ"],
    "eː": ["eː"], "oː": ["oː"], "iː": ["iː"],
    "ɛ": ["ɛ"], "ɔ": ["ɔ"],

    # Geminates
    "kː": ["kː"], "lː": ["lː"], "mː": ["mː"], "nː": ["nː"],
    "rː": ["rː"], "sː": ["sː"], "tː": ["tː"],
}

SPECS = {
    "gem": LanguageSpec(
        code="gem", name="Proto-Germanic (reconstructed)",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_GEM, allophones=ALLOPHONES_GEM,
        parent="ine",
        notes=(
            "Proto-Germanic (~500 BCE – 1st c. CE). Reconstructed common "
            "ancestor of all Germanic languages. Defining innovation: "
            "Grimm's Law (*p→*f, *t→*θ, *k→*x; *b→*p, *d→*t, *g→*k; "
            "*bʰ→*β, *dʰ→*ð, *gʰ→*ɣ) + Verner's Law. Fixed initial "
            "stress accent. PIE *o→*a merger. *ɸ (bilabial) at this "
            "stage, not yet [f]. Source: Ringe (2006), Kroonen (2013)."
        ),
    ),
    "got": LanguageSpec(
        code="got", name="Gothic",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_GOT, allophones=ALLOPHONES_GOT,
        parent="gem",
        notes=(
            "Gothic (4th c. CE text; spoken in Iberia 5th–8th c.). "
            "East Germanic, earliest well-attested Germanic language. "
            "Wulfila's Bible (Codex Argenteus). VISIGOTHIC kingdom in "
            "Iberia ~470–711 CE; Gothic substrate loanwords in Ibero-"
            "Romance: guerra, guardar, ropa, yelmo. Gothic alphabet "
            "from Greek/Latin/runic. Conservative Germanic: no HG "
            "consonant shift. Labiovelar fricative /xʷ/ (ƕ). Voiced "
            "fricatives [β ð ɣ] as allophones of /b d g/."
        ),
    ),
}
