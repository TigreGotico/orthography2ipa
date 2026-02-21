"""Germanic ancestral chain — Proto-Germanic through Old stages.

This module covers the reconstructed and early-attested Germanic languages
that bridge Proto-Germanic to the modern West and North Germanic languages.

Proto-Germanic is the reconstructed ancestor of all Germanic languages.
Gothic is the earliest well-attested Germanic language (Wulfila's Bible,
4th c. CE) and the language of the Visigoths who ruled Iberia 5th–8th c.

Genealogical structure:
  Proto-Germanic (gem)             ~500 BCE – 1st c. CE
       ├── East Germanic  →  Gothic (got) — already in germanic_historical.py
       └── Proto-Northwest-Germanic (gem-x-northwest)  ~1st c. CE
              ├── Proto-North-Germanic (gem-x-north)    ~200 CE
              │     ├── Old Norse / Proto-Norse (non)   ~500–1300 CE
              │     │     ├── Old West Norse  →  Icelandic, Faroese, Norwegian
              │     │     └── Old East Norse  →  Swedish, Danish
              │     └── Runic Norse (gem-x-runic)       ~200–800 CE
              └── Proto-Ingvaeonic / North Sea Germanic (gem-x-ingvaeonic)  ~400 CE
                    ├── Old English / Anglo-Saxon (ang)  ~450–1150 CE
                    │     └── Middle English (enm)       ~1100–1500 CE
                    ├── Old Frisian (ofs)                ~1200–1500 CE
                    └── Proto-High-Low split
                          ├── Old Saxon (osx)            ~800–1100 CE
                          └── Old High German (goh)      ~750–1050 CE

Sources:
- Ringe, D. (2006). *From Proto-Indo-European to Proto-Germanic*. OUP.
- Kroonen, G. (2013). *Etymological Dictionary of Proto-Germanic*. Brill.
- Fulk, R.D. (2018). *A Comparative Grammar of the Early Germanic Languages*. Benjamins.
- Nielsen, H.F. (2000). *The Early Runic Language of Scandinavia*. Winter.
- Noreen, A. (1923). *Altisländische und altnorwegische Grammatik*. Halle.
- Gordon, E.V. (1957). *An Introduction to Old Norse*. 2nd ed. OUP.
- Campbell, A. (1959). *Old English Grammar*. OUP.
- Braune, W. (2018). *Althochdeutsche Grammatik*. 16th ed. Niemeyer.
- Gallée, J.H. (1993). *Altsächsische Grammatik*. 3rd ed. VanGorcum.
- Robinson, O.W. (1992). *Old English and Its Closest Relatives*. Stanford UP.
- Hogg, R.M. ed. (1992). *Cambridge History of the English Language*, vol. 1. CUP.
- Fischer, O. et al. (2000). *The Syntax of Early English*. CUP.
- Townend, M. (2002). *Language and History in Viking Age England*. Brepols.
- Wright, J. (1910/1954). *Grammar of the Gothic Language*. OUP.
- Braune, W. & Heidermanns, F. (2018). *Gotische Grammatik*. 21st ed. Niemeyer.
- Bennett, W.H. (1980). *An Introduction to the Gothic Language*. MLA.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
AD = AncestorRole.ADSTRATE
SUP = AncestorRole.SUPERSTRATE

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
# PROTO-NORTHWEST GERMANIC (gem-x-northwest)  ~1st century CE
# ═══════════════════════════════════════════════════════════════════════════
#
# After East Germanic (Gothic branch) separated, the remaining dialects
# formed Proto-Northwest Germanic, ancestral to all North and West Germanic.
#
# SHARED INNOVATIONS distinguishing Northwest Gmc from Gothic:
#   1. *-z (Verner) → *-r (rhotacism): PGmc *-z → NW Gmc *-r word-finally
#      (Gothic retains -z: OE -r, ON -r, OHG -r)
#   2. *-ija- suffix: suffix change
#   3. Some vowel developments differ from Gothic
#   4. Gemination before *j (West Germanic gemination — affects West Gmc only)
#      This is a West, not Northwest Germanic, feature.
#
# Consonant inventory: same as Proto-Germanic plus rhotacism.

GRAPHEMES_NW_GEM = {
    **GRAPHEMES_GEM,
    # Rhotacism: *z → *r (word-finally and intervocalically)
    # We represent the outcome: z is rare; r appears in its place
    "r": ["r"],  # now includes former *z positions
    "z": ["z"],  # only in initial position and some clusters
}

ALLOPHONES_NW_GEM = {
    **ALLOPHONES_GEM,
    # Rhotacism: z → r in most environments
    "z": ["r", "z"],  # rhotacism in progress
    "r": ["r"],
}

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-INGVAEONIC / NORTH SEA GERMANIC (gem-x-ingvaeonic)  ~3rd–5th c. CE
# ═══════════════════════════════════════════════════════════════════════════
#
# Ingvaeonic (named after the Ingaevones tribes of the North Sea coast)
# = the ancestor of English, Frisian, and the coastal Low German dialects.
#
# DEFINING INGVAEONIC INNOVATIONS (vs. High German / Old High German):
#   1. INGVAEONIC NASAL SPIRANT LAW:
#      PGmc *-nf- *-nθ- *-ns- → VN compensation + fricative (nasal deleted)
#      OE: *munþaz → mūþ "mouth" (cf. OHG munt — nasal preserved)
#      OE: *fimf → fīf "five" (cf. OHG fimf/funf — nasal preserved)
#      OE: *uns → ūs "us" (cf. OHG uns — nasal preserved)
#   2. *-ij- suffix loss (distinct from High German)
#   3. Shared *ā-umlaut / back-mutation patterns
#   4. No High German Consonant Shift (Ingvaeonic preserves PGmc stops)

GRAPHEMES_INGVAEONIC = {
    **GRAPHEMES_NW_GEM,
    # Nasal spirant law outputs: nasal deleted before fricative, vowel lengthened
    # Represented by the vowel quality changes rather than new consonants
    # (the nasal is gone, compensation lengthening is a vowel feature)
    # Key consonant: þ preserved (cf. OHG where þ → d)
    "þ": ["θ"],  # preserved (OE thorn; cf. OHG where θ → d)
    # p, t, k UNCHANGED (no HG shift)
}

ALLOPHONES_INGVAEONIC = {
    **ALLOPHONES_NW_GEM,
    "θ": ["θ"],
    # Stops remain stops (no HG shift)
    "p": ["p"],
    "t": ["t"],
    "k": ["k"],
}

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-NORTH GERMANIC (gem-x-north)  ~200–700 CE
# ═══════════════════════════════════════════════════════════════════════════
#
# Proto-North Germanic is the ancestor of all Scandinavian languages.
# Attested indirectly through:
#   - Runic inscriptions in Elder Futhark (~150–800 CE)
#   - Reconstruction from Old Norse, Swedish, Danish, etc.
#
# KEY NORTH GERMANIC INNOVATIONS (vs. West Germanic):
#   1. *-az → *-r (rhotacism complete; -a lost): nom. sg. "day" = dagr
#   2. SYNCOPE: loss of unstressed syllables more aggressive than West Gmc
#   3. Breaking (fracture): i-umlaut and u-umlaut affect root vowels
#   4. Development of definite suffix *-inn, *-in (suffixed article)
#      — unique to North Germanic
#   5. *w- before back vowel: ON vindr "wind" (cf. OE wind, OHG wint)
#   6. Loss of *j- initially before i/e
#
# I-UMLAUT (most important North Germanic phonological process):
#   Back vowels fronted before *-i, *-j in following syllable:
#   *a → e (before *-i): *gastiz → gestr "guest"
#   *u → y: *fullijaną → fylla "to fill"
#   *o → ø: *dōmijaną → dœma "to judge"
#   *ā → æ: *hālidaz → hæill "whole"

GRAPHEMES_PROTO_NORTH_GEM = {
    # Vowels — the evolving North Germanic system
    "a": ["a"],
    "e": ["e"],  # from i-umlaut of *a
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],
    "y": ["y"],  # from i-umlaut of *u (FRONT ROUNDED — new!)
    "ø": ["ø"],  # from i-umlaut of *o
    "æ": ["æ"],  # from i-umlaut of *ā
    # Long vowels
    "ā": ["aː"],
    "ē": ["eː"],
    "ī": ["iː"],
    "ō": ["oː"],
    "ū": ["uː"],
    "ȳ": ["yː"],  # long front rounded (i-umlaut of ū)
    # Diphthongs
    "ei": ["ej"],
    "au": ["ɑu"],
    "øy": ["øy"],  # from i-umlaut of *au

    # Consonants — largely Proto-Germanic base
    "p": ["p"],
    "t": ["t"],
    "k": ["k"],
    "b": ["b"],
    "d": ["d"],
    "g": ["ɡ"],
    "f": ["f"],
    "þ": ["θ"],  # thorn — preserved in North Gmc
    "ð": ["ð"],  # eth — voiced allophone of þ
    "s": ["s"],
    "h": ["h"],
    "r": ["r"],  # includes rhotacism of former *z
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "w": ["w"],
    "j": ["j"],
    # New North Germanic: velar nasal phonemic
    "ŋ": ["ŋ"],  # before velars
}

ALLOPHONES_PROTO_NORTH_GEM = {
    "p": ["p"], "t": ["t"], "k": ["k"],
    "b": ["b", "β"], "d": ["d", "ð"], "ɡ": ["ɡ", "ɣ"],
    "f": ["f"], "θ": ["θ", "ð"],
    "s": ["s"],
    "h": ["h", "x"],
    "r": ["r"], "l": ["l"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "w": ["w"], "j": ["j"],
    "y": ["y"], "ø": ["ø"], "æ": ["æ"],
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
    "aː": ["aː"], "eː": ["eː"], "iː": ["iː"], "oː": ["oː"], "uː": ["uː"],
    "yː": ["yː"], "øː": ["øː"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SUEBI (xsb) — Germanic superstrate in Galicia/NW Iberia
# ═══════════════════════════════════════════════════════════════════════════
#
# The Suebi (Suevi) established a kingdom in Gallaecia (411–585 CE).
# Germanic superstrate influence on Portuguese and especially Galician.
# Not separately attested — phonology from Proto-Germanic + onomastics.
#
# Sources:
# - d'Encarnação, J. (1975). *Divindades indígenas sob o domínio romano
#   em Portugal*. FLUC.
# - Piel, J.M. (1937). 'Os nomes germânicos na toponímia portuguesa.'
#   *Boletim de Filologia* 5.

GRAPHEMES_XSB = {
    # Essentially Proto-West-Germanic inventory
    "a": ["a"], "ā": ["aː"],
    "e": ["e"], "ē": ["eː"],
    "i": ["i"], "ī": ["iː"],
    "o": ["o"], "ō": ["oː"],
    "u": ["u"], "ū": ["uː"],
    "b": ["b"], "p": ["p"],
    "d": ["d"], "t": ["t"],
    "g": ["ɡ"], "k": ["k"],
    "f": ["f"], "þ": ["θ"],
    "s": ["s"], "h": ["h", "x"],
    "w": ["w"], "j": ["j"],
    "m": ["m"], "n": ["n"],
    "l": ["l"], "r": ["r"],
}

ALLOPHONES_XSB = {
    "a": ["a"], "aː": ["aː"], "e": ["e"], "eː": ["eː"],
    "i": ["i"], "iː": ["iː"], "o": ["o"], "oː": ["oː"],
    "u": ["u"], "uː": ["uː"],
    "b": ["b", "β"], "p": ["p"],
    "d": ["d", "ð"], "t": ["t"],
    "ɡ": ["ɡ", "ɣ"], "k": ["k"],
    "f": ["f"], "θ": ["θ", "ð"],
    "s": ["s", "z"], "h": ["h", "x"],
    "m": ["m"], "n": ["n", "ŋ"],
    "l": ["l"], "r": ["r"],
    "w": ["w"], "j": ["j"],
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

# ═══════════════════════════════════════════════════════════════════════════
# OLD NORSE (non)  ~700–1300 CE
# ═══════════════════════════════════════════════════════════════════════════
#
# Old Norse (dǫnsk tunga "Danish tongue" or norrœnt mál) is the literary
# language of medieval Scandinavia, especially Iceland and Norway.
# It is the direct ancestor of:
#   Old West Norse → Icelandic (is), Faroese (fo), Norwegian (no)
#   Old East Norse → Swedish (sv), Danish (da)
#
# Two main branches emerged ~11th century:
#   OLD WEST NORSE: Norway + Iceland (Eddas, Sagas)
#   OLD EAST NORSE: Sweden + Denmark (runic inscriptions, later texts)
#
# The standard ON of grammars is based on Old West Norse (Icelandic MSS).
#
# KEY OLD NORSE PHONOLOGICAL FEATURES:
#   - Full i-umlaut system: y, ø, æ from back vowels
#   - Preserved /θ/ and /ð/ (thorn ⟨þ⟩ and eth ⟨ð⟩)
#   - Preserved labiodental /v/ from *w
#   - /kn-/ clusters word-initial (later lost in Swedish, Danish, English)
#   - /gn-/ clusters word-initial
#   - Diphthongs: ei, au, ey (< øy from umlaut of au)
#   - Long consonants (geminates) phonemic
#   - No prosthetic vowels before initial consonant clusters

GRAPHEMES_OLD_NORSE = {
    # ── Vowels ──────────────────────────────────────────────────────────
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],
    "y": ["y"],  # front rounded (i-umlaut of u)
    "ø": ["ø"],  # front rounded (i-umlaut of o)
    "œ": ["œ"],  # open front rounded (i-umlaut of ǫ)
    "ǫ": ["ɔ"],  # back rounded (from *a before nasal+C)
    "æ": ["æ"],  # from i-umlaut of ā; also ǽ
    # Long vowels (indicated by acute accent in modern editions)
    "á": ["aː"],
    "é": ["eː"],
    "í": ["iː"],
    "ó": ["oː"],
    "ú": ["uː"],
    "ý": ["yː"],
    "ǿ": ["øː"],
    # Diphthongs
    "ei": ["ej"],
    "au": ["ɑu"],
    "ey": ["øy"],  # i-umlaut of *au

    # ── Consonants ──────────────────────────────────────────────────────
    "p": ["p"],
    "t": ["t"],
    "k": ["k"],
    "b": ["b"],
    "d": ["d"],
    "g": ["ɡ"],
    "f": ["f", "v"],  # f: [f] initially; [v] between vowels
    "þ": ["θ"],  # thorn
    "ð": ["ð"],  # eth
    "s": ["s"],
    "h": ["h"],
    "r": ["r"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "v": ["v"],  # from PGmc *w
    "j": ["j"],
    "kn": ["kn"],  # kn- cluster (not deleted as in modern Swedish/Danish)
    "gn": ["ɡn"],  # gn- cluster
    "hl": ["hl"],  # voiceless lateral (archaic; by 13th c. → l)
    "hr": ["hr"],  # voiceless r
    "hn": ["hn"],  # voiceless n
    "ng": ["ŋɡ", "ŋ"],  # -ng-: [ŋɡ] medially
    "nk": ["ŋk"],
    # Geminates
    "pp": ["pː"], "tt": ["tː"], "kk": ["kː"],
    "bb": ["bː"], "dd": ["dː"], "gg": ["ɡː"],
    "ff": ["fː"], "ss": ["sː"],
    "ll": ["lː"], "mm": ["mː"], "nn": ["nː"], "rr": ["rː"],
}

ALLOPHONES_OLD_NORSE = {
    "p": ["p"], "t": ["t"], "k": ["k"],
    "b": ["b"], "d": ["d"], "ɡ": ["ɡ", "ɣ"],  # ɣ between vowels
    "f": ["f", "v"], "θ": ["θ"], "ð": ["ð"],
    "s": ["s"], "h": ["h", "x"],  # x before consonants
    "r": ["r"], "l": ["l"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "v": ["v"], "j": ["j"],
    # Vowels
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
    "y": ["y"], "ø": ["ø"], "œ": ["œ"], "ɔ": ["ɔ"], "æ": ["æ"],
    "aː": ["aː"], "eː": ["eː"], "iː": ["iː"], "oː": ["oː"], "uː": ["uː"],
    "yː": ["yː"], "øː": ["øː"],
    # Diphthongs
    "ej": ["ej"], "ɑu": ["ɑu"], "øy": ["øy"],
}

# ═══════════════════════════════════════════════════════════════════════════
# OLD ENGLISH / ANGLO-SAXON (ang)  ~450–1150 CE
# ═══════════════════════════════════════════════════════════════════════════
#
# Old English is attested in four major dialects:
#   - West Saxon (dominant literary dialect; basis for modern editions)
#   - Northumbrian (northern England)
#   - Mercian (midlands)
#   - Kentish (southeast)
#
# We model West Saxon as the standard.
#
# KEY OLD ENGLISH PHONOLOGICAL FEATURES:
#   - BREAKING (fracture): vowels before certain consonant clusters
#     e.g. *e → ea before -l+C, -r+C, -h: eald "old", ceald "cold"
#   - I-UMLAUT: same process as Old Norse but with OE outcomes
#     *a → e: mann/menn; *u → y: mus/mys
#   - Ingvaeonic Nasal Spirant Law (see above):
#     PGmc *-nθ → long vowel: mūþ "mouth"
#   - Palatalisation: *k → /tʃ/ before i/j: cild [tʃild] "child"
#     *g → /j/ or /dʒ/ before i/j: gear [jɛɑr] "year"
#   - /w/ preserved initially (cf. ON where often preserved)
#   - Preserved þ (thorn) and ð (eth) as allophones of /θ/

GRAPHEMES_OLD_ENGLISH = {
    # ── Vowels ──────────────────────────────────────────────────────────
    "a": ["a"],
    "æ": ["æ"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],
    "y": ["y"],  # front rounded (i-umlaut of u)
    # Long vowels
    "ā": ["aː"],
    "ǣ": ["æː"],
    "ē": ["eː"],
    "ī": ["iː"],
    "ō": ["oː"],
    "ū": ["uː"],
    "ȳ": ["yː"],
    # Diphthongs (OE has a complex diphthong system)
    "ea": ["æɑ"],  # short falling diphthong
    "eo": ["eo"],  # short falling diphthong
    "ie": ["ie"],  # from i-umlaut of *ea
    "ēa": ["æːɑ"],  # long falling diphthong
    "ēo": ["eːo"],
    "īe": ["iːe"],

    # ── Consonants ──────────────────────────────────────────────────────
    "p": ["p"],
    "t": ["t"],
    "k": ["k"],  # ⟨c⟩ in OE spelling
    "c": ["k", "tʃ"],  # [k] before back vowels; [tʃ] before front
    "cg": ["dʒ"],  # OE ⟨cg⟩ = /dʒ/ (ecg "edge")
    "b": ["b"],
    "d": ["d"],
    "g": ["ɡ", "j", "ɣ"],  # [ɡ] after nasal; [j] before front V; [ɣ] elsewhere
    "sc": ["ʃ"],  # OE ⟨sc⟩ = /ʃ/ (scip "ship")
    "f": ["f", "v"],  # [f] initially/finally; [v] between voiced sounds
    "þ": ["θ", "ð"],  # thorn: [θ] initially/finally; [ð] between vowels
    "ð": ["ð", "θ"],  # eth: allophone of þ (distribution same)
    "s": ["s", "z"],  # [z] between voiced sounds
    "h": ["h", "x", "ç"],  # [h] initially; [x] finally; [ç] after front V
    "r": ["r"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "ng": ["ŋɡ", "ŋ"],
    "nk": ["ŋk"],
    "w": ["w"],
    "j": ["j"],  # ⟨g⟩ before front vowels
    # Geminates
    "pp": ["pː"], "tt": ["tː"], "cc": ["kː"],
    "bb": ["bː"], "dd": ["dː"], "gg": ["ɡː"],
    "ff": ["fː"], "þþ": ["θː"], "ss": ["sː"],
    "ll": ["lː"], "mm": ["mː"], "nn": ["nː"], "rr": ["rː"],
}

ALLOPHONES_OLD_ENGLISH = {
    "p": ["p"], "t": ["t"], "k": ["k"],
    "b": ["b"], "d": ["d"], "ɡ": ["ɡ", "ɣ", "j"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ"], "ʃ": ["ʃ"],
    "f": ["f", "v"], "θ": ["θ", "ð"], "s": ["s", "z"],
    "h": ["h", "x", "ç"],
    "r": ["r"], "l": ["l"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "w": ["w"], "j": ["j"],
    # Vowels
    "a": ["a"], "æ": ["æ"], "e": ["e"],
    "i": ["i"], "o": ["o"], "u": ["u"], "y": ["y"],
    "aː": ["aː"], "æː": ["æː"], "eː": ["eː"],
    "iː": ["iː"], "oː": ["oː"], "uː": ["uː"], "yː": ["yː"],
    # Diphthongs
    "æɑ": ["æɑ"], "eo": ["eo"], "ie": ["ie"],
    "æːɑ": ["æːɑ"], "eːo": ["eːo"], "iːe": ["iːe"],
}

# ═══════════════════════════════════════════════════════════════════════════
# OLD HIGH GERMAN (goh)  ~750–1050 CE
# ═══════════════════════════════════════════════════════════════════════════
#
# Old High German is the ancestor of all High German dialects:
# Standard German, Yiddish, Luxembourgish, Alemannic (Swiss German),
# Bavarian, Austro-Bavarian.
#
# THE DEFINING FEATURE: THE HIGH GERMAN CONSONANT SHIFT (HGCS)
# (Second Germanic Consonant Shift / zweite Lautverschiebung)
# Happened ~500–800 CE; distinguishes High German from ALL other Germanic.
#
# HGCS Rules (applied to PGmc stops):
#   Geminate/post-consonantal position:
#     *p → ff/pf: OHG appul < *ap(a)laz; OHG pfad < *paþaz
#     *t → ss/tz: OHG wasser < *watōr; OHG setzen < *satjan
#     *k → hh/kch: OHG mahha < *makōn (Bavarian kch)
#   After vowel (intervocalic):
#     *p → f(f): OHG slāfan "sleep" < PGmc *slēpaną (cf. OE slǣpan)
#     *t → z: OHG herza < *hertō (cf. OE heorte "heart")
#     *k → h: OHG machen < *makōn (cf. OE macian)
#   Word-initially (partial shift — only in some dialects):
#     *p → pf (only in Upper German / Bavarian / Alemannic)
#
# Other OHG features:
#   - þ → d: OHG dag "day" (cf. OE dæg, ON dagr — all kept þ→d)
#     Actually PGmc *þ → OHG d is shared with other West Germanic
#   - *ai → ē: OHG hēr "lord", OE hearra
#   - *au → ō: OHG fōzan "to hate" (cf. ON fautr)
#   - I-umlaut: same process, OHG outcomes: *a → e, *u → i (partial)

GRAPHEMES_OLD_HIGH_GERMAN = {
    # ── Vowels ──────────────────────────────────────────────────────────
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],
    # Long vowels
    "ā": ["aː"],
    "ē": ["eː"],  # < PGmc *ai in some positions
    "ī": ["iː"],
    "ō": ["oː"],  # < PGmc *au in some positions
    "ū": ["uː"],
    # Umlauted vowels (from i-mutation)
    "i": ["i"],  # i-umlaut of *a often still spelled ⟨a⟩ in OHG
    # Diphthongs
    "ei": ["ej"],  # = PGmc *ai in some positions
    "ou": ["ou"],  # = PGmc *au in some positions
    "ie": ["ie"],
    "uo": ["uo"],
    "ia": ["iɑ"],

    # ── Consonants — THE HIGH GERMAN SHIFT ───────────────────────────────
    # PGmc *p → OHG ff/pf (shown as outcomes below)
    "pf": ["pf"],  # affricate from shifted *p (word-initial Upper German)
    "ff": ["fː"],  # from geminate/post-C *p
    "p": ["p"],  # inherited *p after nasals/liquids (not shifted in all positions)
    # PGmc *t → OHG ss/tz
    "tz": ["ts"],  # affricate from *t (word-initial, post-consonantal)
    "zz": ["tsː", "sː"],  # geminate from intervocalic *t (→ ss in Upper Gmc)
    "t": ["t"],  # *t after consonant (only partially shifted)
    # PGmc *k → OHG hh/kch (Upper German)
    "hh": ["xː"],  # geminate from *k intervocalic
    "k": ["k"],  # *k in other positions; partially shifted
    # PGmc *d → OHG t (chain shift)
    "d": ["d", "t"],  # *d → t in some positions (chain shift)
    # Stops (unchanged by HGCS)
    "b": ["b"],
    "g": ["ɡ"],
    # Fricatives
    "f": ["f"],
    "d": ["d"],  # < PGmc *þ → OHG d (West Gmc innovation shared)
    "s": ["s"],
    "sc": ["ʃ"],
    "h": ["h", "x"],  # [h] initially; [x] elsewhere
    "z": ["ts", "s"],  # OHG ⟨z⟩ = /ts/ in most positions → /s/ finally
    # Nasals
    "m": ["m"],
    "n": ["n"],
    "ng": ["ŋɡ"],
    # Liquids
    "r": ["r"],
    "l": ["l"],
    # Glides
    "w": ["w"],
    "j": ["j"],
}

ALLOPHONES_OLD_HIGH_GERMAN = {
    "pf": ["pf"], "ff": ["fː"], "p": ["p"],
    "ts": ["ts"], "sː": ["sː"], "t": ["t"],
    "xː": ["xː"], "k": ["k"],
    "b": ["b"], "d": ["d"], "ɡ": ["ɡ"],
    "f": ["f"], "s": ["s"], "ʃ": ["ʃ"],
    "h": ["h", "x"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "r": ["r"], "l": ["l"],
    "w": ["w"], "j": ["j"],
    # Vowels
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
    "aː": ["aː"], "eː": ["eː"], "iː": ["iː"], "oː": ["oː"], "uː": ["uː"],
    "ej": ["ej"], "ou": ["ou"], "ie": ["ie"], "uo": ["uo"],
}

# ═══════════════════════════════════════════════════════════════════════════
# OLD SAXON (osx)  ~800–1100 CE
# ═══════════════════════════════════════════════════════════════════════════
#
# Old Saxon is the ancestor of Low German (Plattdeutsch) and is closely
# related to Old Frisian and Old English (all Ingvaeonic).
#
# IT DID NOT UNDERGO THE HIGH GERMAN CONSONANT SHIFT.
# This is the key isogloss: OS makōn (cf. OHG mahhōn) "to make".
#
# Major texts: Heliand (Old Saxon gospel harmony, ~830 CE).
#
# KEY OLD SAXON FEATURES:
#   - p, t, k UNCHANGED (no HG shift; cf. OHG pf/ff, tz/ss, hh)
#   - þ/ð preserved (like OE, ON; cf. OHG where merged → d in most)
#   - *ai → ē (partial; like OHG)
#   - *au → ō (like OHG)
#   - I-umlaut less fully developed than OE or ON

GRAPHEMES_OLD_SAXON = {
    # ── Vowels ──────────────────────────────────────────────────────────
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],
    "ā": ["aː"],
    "ē": ["eː"],
    "ī": ["iː"],
    "ō": ["oː"],
    "ū": ["uː"],
    # Diphthongs
    "ia": ["iɑ"],
    "ie": ["ie"],
    "io": ["io"],
    "uo": ["uo"],

    # ── Consonants — NO HG SHIFT ─────────────────────────────────────────
    "p": ["p"],  # UNCHANGED (cf. OHG pf/ff)
    "t": ["t"],  # UNCHANGED (cf. OHG tz/ss)
    "k": ["k"],  # UNCHANGED (cf. OHG hh)
    "b": ["b"],
    "d": ["d"],
    "g": ["ɡ"],
    "f": ["f", "v"],
    "þ": ["θ", "ð"],  # thorn preserved (cf. OHG → d)
    "s": ["s"],
    "h": ["h", "x"],
    "sk": ["sk", "ʃ"],  # sk → ʃ in some positions
    "r": ["r"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "ng": ["ŋɡ"],
    "w": ["w"],
    "j": ["j"],
}

ALLOPHONES_OLD_SAXON = {
    "p": ["p"], "t": ["t"], "k": ["k"],  # NO HG shift
    "b": ["b"], "d": ["d"], "ɡ": ["ɡ", "ɣ"],
    "f": ["f", "v"], "θ": ["θ", "ð"], "s": ["s", "z"],
    "h": ["h", "x"], "ʃ": ["ʃ"],
    "r": ["r"], "l": ["l"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "w": ["w"], "j": ["j"],
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
    "aː": ["aː"], "eː": ["eː"], "iː": ["iː"], "oː": ["oː"], "uː": ["uː"],
    "iɑ": ["iɑ"], "ie": ["ie"], "io": ["io"], "uo": ["uo"],
}

# ═══════════════════════════════════════════════════════════════════════════
# MIDDLE ENGLISH (enm)  ~1100–1500 CE
# ═══════════════════════════════════════════════════════════════════════════
#
# Middle English follows the Norman Conquest (1066 CE).
# The Norman French superstrate had profound phonological consequences:
#
#   1. LOSS OF GRAMMATICAL GENDER (OE had 3 genders; ME → none)
#   2. LOSS OF FINAL INFLECTIONS → stress shifts
#   3. New French phonemes introduced:
#      /v/ phonemic (OE had [v] only as allophone of /f/)
#      /dʒ/ from French ⟨g, j⟩ (OE had [dʒ] but from ⟨cg⟩ only)
#      /ʒ/ from French (in words like vision, pleasure — late ME)
#      /tʃ/ already existed in OE (from palatalized *k)
#   4. GREAT VOWEL SHIFT beginning ~1400–1700 (ME → Early Modern English)
#   5. OE diphthongs simplified: ea → ɛ, eo → e
#   6. OE y → i (loss of front rounded vowel)
#   7. Schwa /ə/ develops from weakened unstressed vowels
#
# We model Late Middle English (~1350–1450), roughly Chaucer's dialect.

GRAPHEMES_MIDDLE_ENGLISH = {
    # ── Vowels (Late ME / Chaucerian) ───────────────────────────────────
    "a": ["a", "æ"],  # short; [a] before GVS
    "e": ["ɛ", "e"],
    "i": ["i"],
    "o": ["ɔ", "o"],
    "u": ["u", "ʊ"],
    # Long vowels — on the cusp of the Great Vowel Shift
    "ā": ["aː"],  # GVS → [eɪ] in Early Modern
    "ē": ["eː"],  # GVS → [iː]
    "ī": ["iː"],  # GVS → [aɪ]
    "ō": ["oː"],  # GVS → [uː] (or [oʊ])
    "ū": ["uː"],  # GVS → [aʊ]
    # Schwa
    "e": ["ə"],  # final -e often silent or [ə] by late ME
    # ME diphthongs
    "ai": ["aj"],
    "au": ["au"],
    "ei": ["ej"],
    "oi": ["oj"],
    "ou": ["ou"],
    "ew": ["ɛu", "ju"],
    "ow": ["ou", "au"],

    # ── Consonants ──────────────────────────────────────────────────────
    "p": ["p"],
    "t": ["t"],
    "k": ["k"],
    "b": ["b"],
    "d": ["d"],
    "g": ["ɡ"],
    "tʃ": ["tʃ"],  # ch: OE + French
    "dʒ": ["dʒ"],  # j, g before front V: French origin
    "f": ["f"],
    "v": ["v"],  # NOW PHONEMIC (from French)
    "θ": ["θ"],  # th voiceless (still spelled ⟨þ⟩ or ⟨th⟩)
    "ð": ["ð"],  # th voiced
    "s": ["s"],
    "z": ["z"],
    "ʃ": ["ʃ"],  # sh (OE sc + French)
    "ʒ": ["ʒ"],  # from French (vision, pleasure — late ME)
    "h": ["h"],
    "x": ["x"],  # gh: OE [x] preserved in spelling; weakening
    "r": ["r"],  # still trill/tap (rhotic)
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "ŋ": ["ŋ"],
    "w": ["w"],
    "j": ["j"],
}

ALLOPHONES_MIDDLE_ENGLISH = {
    "p": ["p"], "t": ["t"], "k": ["k"],
    "b": ["b"], "d": ["d"], "ɡ": ["ɡ"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ"],
    "f": ["f"], "v": ["v"], "θ": ["θ"], "ð": ["ð"],
    "s": ["s"], "z": ["z"], "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "h": ["h"], "x": ["x", "h", "∅"],  # ⟨gh⟩ weakening
    "r": ["r", "ɾ"], "l": ["l"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "w": ["w"], "j": ["j"],
    "a": ["a", "æ"], "ɛ": ["ɛ"], "e": ["e", "ə"],
    "i": ["i"], "ɔ": ["ɔ"], "o": ["o"], "u": ["u", "ʊ"],
    "aː": ["aː"], "eː": ["eː"], "iː": ["iː"], "oː": ["oː"], "uː": ["uː"],
    "aj": ["aj"], "au": ["au"], "ej": ["ej"], "oj": ["oj"],
    "ou": ["ou"], "ɛu": ["ɛu"], "ju": ["ju"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SPECS
# ═══════════════════════════════════════════════════════════════════════════

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
    "gem-x-northwest": LanguageSpec(
        code="gem-x-northwest",
        name="Proto-Northwest Germanic",
        family="Germanic",
        script="Latin",
        graphemes=GRAPHEMES_NW_GEM,
        allophones=ALLOPHONES_NW_GEM,
        parent="gem",
        ancestors=(
            Ancestor("gem", P, 1.0, "Descent from Proto-Germanic"),
        ),
        notes=(
            "Proto-Northwest Germanic (~1st c. CE). The common ancestor of all "
            "North and West Germanic languages, after the separation of East "
            "Germanic (Gothic branch). "
            "KEY INNOVATION: Rhotacism — PGmc *z → NW Gmc *r "
            "(word-finally and intervocalically). Gothic preserves *z; "
            "all NW Gmc descendants have r in these positions. "
            "Evidence: OE hār, ON hárr, OHG hār 'grey' (cf. Got. *hāzs). "
            "Source: Fulk (2018), Ringe (2006)."
        ),
    ),

    "gem-x-ingvaeonic": LanguageSpec(
        code="gem-x-ingvaeonic",
        name="Proto-Ingvaeonic (North Sea Germanic)",
        family="Germanic",
        script="Latin",
        graphemes=GRAPHEMES_INGVAEONIC,
        allophones=ALLOPHONES_INGVAEONIC,
        parent="gem-x-northwest",
        ancestors=(
            Ancestor("gem-x-northwest", P, 1.0,
                     "Descent from Proto-Northwest Germanic"),
        ),
        notes=(
            "Proto-Ingvaeonic / North Sea Germanic (~3rd–5th c. CE). "
            "Ancestor of Old English, Old Frisian, and Old Saxon. "
            "Named after the Ingaevones (Tacitus) — North Sea coastal tribes. "
            "DEFINING INNOVATION: Ingvaeonic Nasal Spirant Law — "
            "PGmc nasal before fricative deleted with compensatory lengthening: "
            "*-nθ → -Vː: *munþaz → OE mūþ 'mouth' (cf. OHG munt — nasal kept); "
            "*-nf → -Vː: *fimf → OE fīf 'five' (cf. OHG fimf — nasal kept); "
            "*-ns → -Vː: *uns → OE ūs 'us'. "
            "NO High German Consonant Shift. "
            "Source: Fulk (2018), Robinson (1992)."
        ),
    ),

    "gem-x-north": LanguageSpec(
        code="gem-x-north",
        name="Proto-North Germanic (Proto-Norse)",
        family="Germanic",
        script="Latin",
        graphemes=GRAPHEMES_PROTO_NORTH_GEM,
        allophones=ALLOPHONES_PROTO_NORTH_GEM,
        parent="gem-x-northwest",
        ancestors=(
            Ancestor("gem-x-northwest", P, 1.0,
                     "Descent from Proto-Northwest Germanic"),
        ),
        notes=(
            "Proto-North Germanic / Proto-Norse (~200–700 CE). "
            "Ancestor of Old Norse and all Scandinavian languages. "
            "Attested through Elder Futhark runic inscriptions (~150–800 CE). "
            "KEY INNOVATIONS vs. West Germanic: "
            "(1) I-UMLAUT: systematic front vowels y, ø, æ from back vowels; "
            "(2) SYNCOPE: aggressive loss of unstressed syllables; "
            "(3) Definite suffix *-inn/*-in (suffixed article — unique to North Gmc); "
            "(4) Loss of PGmc *-a in nominative singular: *dagaz → dagr; "
            "(5) Rhotacism complete. "
            "Source: Nielsen (2000), Gordon (1957)."
        ),
    ),

    "xsb": LanguageSpec(
        code="xsb", name="Suebi (Germanic)",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_XSB, allophones=ALLOPHONES_XSB,
        parent="gem",
        notes=(
            "Suebi/Suevi. West Germanic people who established a "
            "kingdom in Gallaecia (NW Iberia, 411–585 CE). Germanic "
            "superstrate in Galician and Portuguese: ~200 place names "
            "and personal names, vocabulary (guerra, roubar, branco). "
            "Phonology reconstructed from Proto-West-Germanic "
            "(Piel 1937, d'Encarnação 1975)."
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

    "non": LanguageSpec(
        code="non",
        name="Old Norse",
        family="Germanic",
        script="Latin",
        graphemes=GRAPHEMES_OLD_NORSE,
        allophones=ALLOPHONES_OLD_NORSE,
        parent="gem-x-north",
        ancestors=(
            Ancestor("gem-x-north", P, 1.0,
                     "Descent from Proto-North Germanic"),
        ),
        notes=(
            "Old Norse (dǫnsk tunga / norrœnt mál, ~700–1300 CE). "
            "The literary standard of the Norse world, based on Old West Norse "
            "(Iceland, Norway). Direct ancestor of: "
            "Icelandic (is), Faroese (fo), Norwegian (no) from Old West Norse; "
            "Swedish (sv), Danish (da) from Old East Norse. "
            "FULL UMLAUT SYSTEM: y [y], ø [ø], œ [œ], ǫ [ɔ], æ [æ]. "
            "PRESERVED: /θ/ (þ) and /ð/ (ð); kn-, gn- clusters; "
            "voiceless resonants hl-, hr-, hn-. "
            "DIPHTHONGS: ei, au, ey (= i-umlaut of au). "
            "Suffixed definite article: dagr-inn 'the day'. "
            "Primary texts: Prose Edda (Snorri), Poetic Edda, Family Sagas. "
            "Source: Gordon (1957), Noreen (1923)."
        ),
    ),

    "ang": LanguageSpec(
        code="ang",
        name="Old English (Anglo-Saxon)",
        family="Germanic",
        script="Latin",
        graphemes=GRAPHEMES_OLD_ENGLISH,
        allophones=ALLOPHONES_OLD_ENGLISH,
        parent="gem-x-ingvaeonic",
        ancestors=(
            Ancestor("gem-x-ingvaeonic", P, 0.95,
                     "Ingvaeonic / Anglo-Frisian base"),
            Ancestor("non", AD, 0.05,
                     "Old Norse adstrate from Danelaw (~865–1013 CE): "
                     "heavy lexical borrowing (sky, they, take, give, etc.); "
                     "phonological influence in northern dialects"),
        ),
        notes=(
            "Old English / Anglo-Saxon (~450–1150 CE). "
            "West Saxon literary standard; 4 dialects: "
            "West Saxon, Northumbrian, Mercian, Kentish. "
            "KEY FEATURES: Breaking (ea, eo diphthongs before -rC, -lC, -h); "
            "i-umlaut (mann/menn); Ingvaeonic nasal spirant law (mūþ, fīf, ūs); "
            "Palatalisation: *k→[tʃ] / ⟨c⟩ before front V (cild 'child'); "
            "*g→[j] before front V (gear 'year'); "
            "⟨sc⟩ = /ʃ/ (scip 'ship'); ⟨cg⟩ = /dʒ/ (ecg 'edge'); "
            "⟨f⟩ = [v] between voiced sounds. "
            "Primary texts: Beowulf, Anglo-Saxon Chronicle, Ælfric's Homilies. "
            "Source: Campbell (1959), Hogg (1992)."
        ),
    ),

    "goh": LanguageSpec(
        code="goh",
        name="Old High German",
        family="Germanic",
        script="Latin",
        graphemes=GRAPHEMES_OLD_HIGH_GERMAN,
        allophones=ALLOPHONES_OLD_HIGH_GERMAN,
        parent="gem-x-northwest",
        ancestors=(
            Ancestor("gem-x-northwest", P, 1.0,
                     "Descent from Proto-Northwest Germanic"),
        ),
        notes=(
            "Old High German (~750–1050 CE). Ancestor of Standard German, "
            "Yiddish, Alemannic (Swiss German), Bavarian, Luxembourgish. "
            "THE DEFINING FEATURE: HIGH GERMAN CONSONANT SHIFT (HGCS) "
            "(zweite Lautverschiebung, ~500–800 CE): "
            "PGmc *p → OHG pf/ff; *t → tz/ss; *k → kch/hh (Upper German). "
            "This separates OHG from all other Germanic languages. "
            "Examples: OHG apful vs. OE æppel 'apple'; "
            "OHG wazzer vs. OE wæter 'water'; "
            "OHG herza vs. OE heorte 'heart'. "
            "Major texts: Hildebrandslied (~820), Otfrid's Evangelienbuch (~870). "
            "Source: Braune (2018), Fulk (2018)."
        ),
    ),

    "osx": LanguageSpec(
        code="osx",
        name="Old Saxon",
        family="Germanic",
        script="Latin",
        graphemes=GRAPHEMES_OLD_SAXON,
        allophones=ALLOPHONES_OLD_SAXON,
        parent="gem-x-ingvaeonic",
        ancestors=(
            Ancestor("gem-x-ingvaeonic", P, 1.0,
                     "Ingvaeonic base; closely related to Old English"),
        ),
        notes=(
            "Old Saxon (~800–1100 CE). Ancestor of Low German (Plattdeutsch). "
            "Major text: Heliand (~830 CE) — a Saxon gospel harmony in alliterative verse. "
            "NO HIGH GERMAN CONSONANT SHIFT: "
            "OS p, t, k unchanged (cf. OHG pf/ff, tz/ss, hh). "
            "OS makōn vs. OHG mahhōn 'to make'; "
            "OS water vs. OHG wazzer 'water'. "
            "Closely related to Old English and Old Frisian (all Ingvaeonic). "
            "Preserved þ as interdental, like OE. "
            "Source: Gallée (1993), Robinson (1992)."
        ),
    ),

    "enm": LanguageSpec(
        code="enm",
        name="Middle English",
        family="Germanic",
        script="Latin",
        graphemes=GRAPHEMES_MIDDLE_ENGLISH,
        allophones=ALLOPHONES_MIDDLE_ENGLISH,
        parent="ang",
        ancestors=(
            Ancestor("ang", P, 0.80,
                     "Descent from Old English"),
            Ancestor("fr-FR", SUP, 0.15,
                     "Norman French superstrate (post-1066): "
                     "/v/ becomes phonemic; /dʒ/ and /ʒ/ extended; "
                     "massive vocabulary influx (~10,000 French words); "
                     "loss of OE inflectional endings accelerated"),
            Ancestor("non", AD, 0.05,
                     "Old Norse Danelaw adstrate: they/their/them, "
                     "sky, take, give, etc."),
        ),
        notes=(
            "Middle English (~1100–1500 CE). "
            "Post-Norman Conquest (~1066); models Chaucerian Late ME (~1380–1400). "
            "NORMAN FRENCH SUPERSTRATE: /v/ phonemicised; /dʒ/ extended via French; "
            "/ʒ/ enters (vision, pleasure) in late ME. "
            "OE diphthongs simplified: ea→ɛ, eo→e. "
            "OE front rounded /y/ → /i/ (lost). "
            "GREAT VOWEL SHIFT beginning ~1400–1700: long vowels raised/diphthongised. "
            "Dialect continuum: Northern (Scots), Midland (Chaucer), Southern. "
            "Major texts: Canterbury Tales (Chaucer), Piers Plowman, "
            "Sir Gawain and the Green Knight. "
            "Source: Hogg (1992), Fischer (2000)."
        ),
    ),
}
