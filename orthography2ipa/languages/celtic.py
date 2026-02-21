"""Celtic languages — Proto-Celtic and Continental Celtic varieties.

Proto-Celtic (cel) is the reconstructed common ancestor of all Celtic.
Continental Celtic varieties are critical substrates and historical
comparanda for Iberian (xce), Gallo-Romance (French, Occitan), and
Anatolian languages.

ISO 639-5 / Linguist List codes used:
  cel — Proto-Celtic (collective code)
  xtg — Transalpine Gaulish (= "Gaulish" of France/Belgium/Switzerland)
  xga — Galatian (= Celtic of Anatolia)
  xlp — Lepontic (= Cisalpine Celtic, northern Italy)
  xbr — Common Brythonic / Proto-Brythonic (Insular Celtic ancestor)


Sources:
- Matasović, R. (2009). *Etymological Dictionary of Proto-Celtic*. Brill.
- Lambert, P.-Y. (2003). *La langue gauloise*. 2nd ed. Errance.
- Delamarre, X. (2003). *Dictionnaire de la langue gauloise*. Errance.
- Stifter, D. (2006). *Sengoídelc*. Syracuse UP.
- McCone, K. (1996). *Towards a Relative Chronology of Ancient and
  Medieval Celtic Sound Change*. Maynooth.
- Eska, J.F. (2006). "The genitive singular in Continental Celtic."
- Jackson, K.H. (1953). *Language and History in Early Britain*. Edinburgh UP.
- Schrijver, P. (1995). *Studies in British Celtic Historical Phonology*. Rodopi.
- Lejeune, M. (1971). *Lepontica*. Paris.
- Freeman, P.M. (2001). *The Galatian Language*. Edwin Mellen.
- Mitchell, S. (1993). *Anatolia: Land, Men, and Gods in Asia Minor* I.
  Clarendon. [Ch. 3: Galatians]
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
AD = AncestorRole.ADSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-CELTIC (cel)
# ═══════════════════════════════════════════════════════════════════════════
#
# Classification: Indo-European > Celtic (common ancestor)
# Time: ~1200–800 BCE (approximate; pre-attestation)
# Reconstruction: well-established through comparison of:
#   - Goidelic (Old Irish, etc.)
#   - Brythonic (Welsh, Breton, Cornish)
#   - Continental Celtic (Gaulish, Celtiberian, Lepontic, Galatian)
#
# DEFINING SOUND CHANGES from PIE:
#   1. PIE *p → ∅ (complete loss of /p/)
#      This is THE hallmark Celtic feature.
#      PIE *ph₂tēr "father" → PC *ɸatīr → OIr. athir (no /p/)
#      Actually: *p → *ɸ → ∅ (through a bilabial fricative stage)
#   2. PIE *kʷ → *kʷ (preserved; later split: Goidelic → /k/, Brythonic → /p/)
#   3. PIE *gʷ → *b  (labialised to labial)
#   4. PIE *gʷʰ → *b (with aspiration loss)
#   5. PIE *ew → *ow (vowel shift)
#   6. PIE *ē → *ī (long e-raising)
#   7. Lenition of intervocalic stops (incipient)
#
# We include *ɸ (bilabial fricative) as the intermediate stage of p-loss.

GRAPHEMES_CEL = {
    # --- Vowels ---
    "a": ["a"], "ā": ["aː"],
    "e": ["e"], "ē": ["eː"],  # rare; PIE *ē → *ī in most positions
    "i": ["i"], "ī": ["iː"],  # < PIE *ī AND *ē
    "o": ["o"], "ō": ["oː"],
    "u": ["u"], "ū": ["uː"],

    # --- Diphthongs ---
    "ai": ["aj"], "oi": ["oj"], "ei": ["ej"],
    "au": ["aw"], "ou": ["ow"],

    # --- Stops ---
    # NO /p/ in native vocabulary (the defining feature)
    "b": ["b"],  # < PIE *b (rare) and *gʷ, *gʷʰ
    "t": ["t"],
    "d": ["d"],
    "k": ["k"],
    "g": ["ɡ"],
    "kʷ": ["kʷ"],  # < PIE *kʷ (preserved at this stage)
    "gʷ": ["ɡʷ"],  # already → /b/ in most positions

    # --- Fricatives ---
    "ɸ": ["ɸ"],  # < PIE *p → *ɸ (intermediate; → ∅ later)
    "s": ["s"],
    # NO /f/ at this stage (develops later in Goidelic from *sw-, loans)

    # --- Nasals ---
    "m": ["m"],
    "n": ["n"],

    # --- Liquids ---
    "l": ["l"],
    "r": ["r"],

    # --- Glides ---
    "w": ["w"],
    "y": ["j"],

    # --- Geminates ---
    "ss": ["sː"],
    "ll": ["lː"],
    "nn": ["nː"],
    "rr": ["rː"],
}

ALLOPHONES_CEL = {
    "b": ["b", "β"],  # lenition incipient
    "t": ["t", "θ"],  # lenition incipient
    "d": ["d", "ð"],
    "k": ["k", "x"],
    "ɡ": ["ɡ", "ɣ"],
    "kʷ": ["kʷ"],
    "ɸ": ["ɸ"],  # bilabial fricative → ∅
    "s": ["s", "z"],  # [z] before voiced C
    "m": ["m"],
    "n": ["n", "ŋ"],
    "l": ["l"],
    "r": ["r"],
    "w": ["w"],
    "j": ["j"],
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
    "aː": ["aː"], "eː": ["eː"], "iː": ["iː"], "oː": ["oː"], "uː": ["uː"],
    "sː": ["sː"], "lː": ["lː"], "nː": ["nː"], "rː": ["rː"],
}


# ═══════════════════════════════════════════════════════════════════════════
# TRANSALPINE GAULISH (xtg) — THE "Gaulish" of France
# ═══════════════════════════════════════════════════════════════════════════
#
# ISO 639-3: xtg (Transalpine Gaulish)
# Classification: Celtic > Continental Celtic
# Attestation: ~800+ inscriptions
#   - Larzac lead tablet (~1000 chars, magical/juridical)
#   - Chamalières lead tablet (magical)
#   - Coligny calendar (astronomical/ritual, ~2nd c. CE)
#   - Lezoux graffiti, La Graufesenque accounts
#   - Coin legends, potters' marks, votive inscriptions
# Scripts: Greek alphabet (south), Latin alphabet (north), Lepontic (Cisalpine)
# Geography: Gaul (modern France, Belgium, Switzerland)
# Time: ~6th century BCE to ~5th century CE
#
# This is THE Gaulish substrate of French and Gallo-Romance.
#
# KEY PHONOLOGICAL FEATURES:
#   - /p/ absent in native words (Celtic p-loss)
#   - Tau Gallicum /ts/ < *t before certain vowels
#   - Nasal vowels (attested in spelling)
#   - /x/ from lenited /k/
#   - Long vowels from Greek-alphabet evidence
#   - Lenition well-developed

GRAPHEMES_XTG = {
    # --- Vowels ---
    "a": ["a"], "ā": ["aː"],
    "e": ["e"], "ē": ["eː"],
    "ī": ["iː"],
    "o": ["o"], "ō": ["oː"],
    "ū": ["uː"],

    # --- Glides ---
    "u": ["u", "w"],
    "i": ["i", "j"],

    # --- Nasal vowels (attested through spelling) ---
    "an": ["ã"],  # word-final nasalisation
    "en": ["ẽ"],
    "on": ["õ"],

    # --- Diphthongs ---
    "ai": ["aj"],
    "ei": ["ej"],
    "oi": ["oj"],
    "ou": ["ow"],
    "au": ["aw"],
    "eu": ["ew"],

    # --- Stops ---
    # NO /p/ in native words
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "c": ["k"],  # Latin/Greek alphabet convention
    "g": ["ɡ"],

    # --- Fricatives ---
    "s": ["s"],
    "x": ["x"],  # from lenited /k/

    # --- Tau Gallicum (distinctive Gaulish) ---
    # Written ⟨θ⟩ in Greek-alphabet texts, ⟨Θ⟩ or ⟨ts⟩ in Latin texts.
    # Phonetic value debated: [ts], [θ], or [ð].
    # Arises from *t before certain vowels (fronting + affrication).
    "θ": ["ts"],  # "tau gallicum" — the standard interpretation

    # --- Nasals ---
    "m": ["m"],
    "n": ["n"],

    # --- Liquids ---
    "l": ["l"],
    "r": ["r"],

    # --- Geminates ---
    "ss": ["sː"],
    "ll": ["lː"],
    "nn": ["nː"],
    "rr": ["rː"],
    "dd": ["dː"],
    "cc": ["kː"],
    "tt": ["tː"],
}

ALLOPHONES_XTG = {
    "b": ["b", "β"],  # lenition
    "t": ["t", "θ"],
    "d": ["d", "ð"],
    "k": ["k", "x"],  # lenition → [x] (well-attested)
    "ɡ": ["ɡ", "ɣ"],
    "s": ["s", "z"],
    "x": ["x"],
    "ts": ["ts"],  # tau gallicum
    "m": ["m"],
    "n": ["n", "ŋ"],
    "l": ["l"],
    "r": ["r"],
    "w": ["w"],
    "j": ["j"],
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
    "aː": ["aː"], "eː": ["eː"], "iː": ["iː"], "oː": ["oː"], "uː": ["uː"],
    "ã": ["ã"], "ẽ": ["ẽ"], "õ": ["õ"],
    "sː": ["sː"], "lː": ["lː"], "nː": ["nː"], "rː": ["rː"],
    "dː": ["dː"], "kː": ["kː"], "tː": ["tː"],
}

# ═══════════════════════════════════════════════════════════════════════════════
# CISALPINE GAULISH (xcg) — Celtic of N. Italy, distinct from Lepontic
# ═══════════════════════════════════════════════════════════════════════════════
# Attested from ~4th c. BCE; the "Gaulish" brought by La Tène Gauls
# into the Po valley, overlaying the earlier Lepontic.
# Shares most features with Transalpine but in Cisalpine epigraphic context.
# Written in both Lugano and Latin alphabets.

GRAPHEMES_XCG = {
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
    "ā": ["aː"], "ē": ["eː"], "ī": ["iː"], "ō": ["oː"], "ū": ["uː"],
    "b": ["b"], "t": ["t"], "d": ["d"], "c": ["k"], "g": ["ɡ"],
    "s": ["s"], "x": ["x"], "θ": ["ts"],
    "m": ["m"], "n": ["n"], "l": ["l"], "r": ["r"],
    "u": ["u", "w"], "i": ["i", "j"],
    "ss": ["sː"], "ll": ["lː"], "nn": ["nː"], "rr": ["rː"],
}
ALLOPHONES_XCG = {
    "b": ["b", "β"], "t": ["t", "θ"], "d": ["d", "ð"],
    "k": ["k", "x"], "ɡ": ["ɡ", "ɣ"],
    "s": ["s", "z"], "x": ["x"], "ts": ["ts"],
    "m": ["m"], "n": ["n", "ŋ"], "l": ["l"], "r": ["r"],
    "w": ["w"], "j": ["j"],
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
    "aː": ["aː"], "eː": ["eː"], "iː": ["iː"], "oː": ["oː"], "uː": ["uː"],
    "sː": ["sː"], "lː": ["lː"], "nː": ["nː"], "rː": ["rː"],
}

# ═══════════════════════════════════════════════════════════════════════════
# LEPONTIC (xlp) — earliest attested Celtic (~575 BCE)
# ═══════════════════════════════════════════════════════════════════════════
#
# ISO 639-3: xlp (Lepontic)
# Classification: Celtic > Continental Celtic (earliest attested)
# Attestation: ~140 inscriptions (6th–3rd c. BCE)
#   - Prestino (Como) stone — oldest Celtic text (~575 BCE)
#   - Vergiate bronze, Ornavasso inscriptions
#   - Cisalpine coin legends
# Script: Lepontic/Lugano alphabet (derived from Etruscan)
# Geography: Cisalpine Gaul (Lombardy, Piedmont, Ticino, Trentino)
# Time: ~6th–3rd century BCE (absorbed by Transalpine Gaulish influence,
#        then by Latin after 191 BCE Roman conquest)
#
# RELATIONSHIP TO GAULISH:
# Debated. Two positions:
#   (a) Lepontic = Cisalpine Gaulish, dialect of same language (Lejeune)
#   (b) Lepontic = separate Continental Celtic language (Eska, Stifter)
# We treat it as a separate code (xlp) per ISO 639-3 assignment,
# with parent=cel (both descend from Proto-Celtic).
#
# KEY PHONOLOGICAL FEATURES:
# - Celtic p-loss: no /p/ in native words
# - Tau Gallicum /ts/ present (shared with Transalpine)
# - Distinctive: /u/ > /o/ shift in some contexts (Lejeune 1971)
# - Etruscan-derived script only distinguishes 4 vowels (a,e,i,u)
#   so /o/ often written ⟨u⟩
# - Minimal nasal vowel evidence (unlike Transalpine)

GRAPHEMES_XLP = {
    # --- Vowels (Lugano alphabet has limited vowel notation) ---
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],

    # --- Stops ---
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "k": ["k"],
    "g": ["ɡ"],

    # --- Fricatives ---
    "s": ["s"],
    "x": ["x"],
    "θ": ["ts"],  # tau gallicum, shared with Transalpine

    # --- Nasals ---
    "m": ["m"],
    "n": ["n"],

    # --- Liquids ---
    "l": ["l"],
    "r": ["r"],

    # --- Glides ---
    "u": ["u", "w"],
    "i": ["i", "j"],
}

ALLOPHONES_XLP = {
    "b": ["b", "β"],
    "t": ["t"],
    "d": ["d", "ð"],
    "k": ["k", "x"],
    "ɡ": ["ɡ", "ɣ"],
    "s": ["s", "z"],
    "x": ["x"],
    "ts": ["ts"],
    "m": ["m"],
    "n": ["n", "ŋ"],
    "l": ["l"],
    "r": ["r"],
    "w": ["w"],
    "j": ["j"],
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
}


# ═══════════════════════════════════════════════════════════════════════════
# GALATIAN (xga)) — Anatolian Celtic, very fragmentary
# ═══════════════════════════════════════════════════════════════════════════
#
# ISO 639-3: xga (Galatian)
# Classification: Celtic > Continental Celtic
# Attestation: very sparse — ~120 glosses, personal names, tribal names
#   - Jerome (347–420 CE) compared it to Gaulish he heard in Trier
#   - Strabo, Pausanias, and church fathers mention Galatian words
#   - No continuous texts survive
# Script: none (attested only through Greek/Latin transcription)
# Geography: central Anatolia (modern Ankara region, Galatia)
# Time: ~3rd century BCE to ~5th century CE (language death)
# Speakers: Galatians — Celts who migrated to Anatolia in 278 BCE
#
# PHONOLOGICAL RECONSTRUCTION:
# Extremely fragmentary. What we can infer:
#   - Celtic p-loss maintained (personal names show no /p/)
#   - Shared features with Transalpine Gaulish (Jerome's testimony)
#   - Greek script of attestation gives limited phonological detail
#   - Lenition likely present (but impossible to confirm from names alone)
#
# We model this as a thin spec with speculative phonetics, included
# because it is a real attested language (ISO code) and closes the
# Continental Celtic subtree. The inventory is deliberately conservative
# and mirrors Transalpine Gaulish with reduced confidence.

GRAPHEMES_XGA = {
    # Very fragmentary; based on comparison with Transalpine Gaulish
    # and Greek transcriptions of Galatian names/words.
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],

    # --- Stops ---
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "k": ["k"],
    "g": ["ɡ"],

    # --- Fricatives ---
    "s": ["s"],
    "x": ["x"],

    # --- Nasals ---
    "m": ["m"],
    "n": ["n"],

    # --- Liquids ---
    "l": ["l"],
    "r": ["r"],

    # --- Glides ---
    "w": ["w"],
    "j": ["j"],
}

ALLOPHONES_XGA = {
    "b": ["b", "β"],
    "t": ["t", "θ"],
    "d": ["d", "ð"],
    "k": ["k", "x"],
    "ɡ": ["ɡ", "ɣ"],
    "s": ["s", "z"],
    "x": ["x"],
    "m": ["m"],
    "n": ["n", "ŋ"],
    "l": ["l"],
    "r": ["r"],
    "w": ["w"],
    "j": ["j"],
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
}


# ═══════════════════════════════════════════════════════════════════════════
# BRYTHONIC (xbr) — Common Brythonic / Proto-Brythonic
# ═══════════════════════════════════════════════════════════════════════════
#
# Classification: Celtic > Insular Celtic > Brythonic
# Ancestor of Welsh, Cornish, Breton.
# Substrate language of Roman and post-Roman Britain before Anglo-Saxon.
#
# Sources:
# - Jackson, K.H. (1953). *Language and History in Early Britain*. Edinburgh UP.
# - Schrijver, P. (1995). *Studies in British Celtic Historical Phonology*.

GRAPHEMES_XBR = {
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
    "ā": ["aː"], "ē": ["eː"], "ī": ["iː"], "ō": ["oː"], "ū": ["uː"],
    "y": ["ɨ"],  # from Common Celtic *ū in some environments
    "b": ["b"], "p": ["p"],
    "d": ["d"], "t": ["t"],
    "g": ["ɡ"], "c": ["k"],
    "s": ["s"], "h": ["h"],
    "m": ["m"], "n": ["n"],
    "l": ["l"], "r": ["r"],
    "w": ["w"], "j": ["j"],
    "ll": ["ɬ"],  # voiceless lateral (shared with Welsh)
    "rh": ["r̥"],  # voiceless rhotic
}

ALLOPHONES_XBR = {
    "a": ["a"], "aː": ["aː"], "e": ["e"], "eː": ["eː"],
    "i": ["i"], "iː": ["iː"], "o": ["o"], "oː": ["oː"],
    "u": ["u"], "uː": ["uː"], "ɨ": ["ɨ"],
    "b": ["b", "β"], "p": ["p"],
    "d": ["d", "ð"], "t": ["t"],
    "ɡ": ["ɡ", "ɣ"], "k": ["k"],
    "s": ["s"], "h": ["h"],
    "m": ["m"], "n": ["n", "ŋ"],
    "l": ["l"], "ɬ": ["ɬ"],
    "r": ["r"], "r̥": ["r̥"],
    "w": ["w"], "j": ["j"],
}


# ═══════════════════════════════════════════════════════════════════════════════
# WELSH (cy) — modern Brythonic
# ═══════════════════════════════════════════════════════════════════════════════
# Sources: Ball & Müller (2009), Thomas (1996), Jones (1984)

GRAPHEMES_CY = {
    "a": ["a"], "e": ["ɛ"], "i": ["ɪ"], "o": ["ɔ"], "u": ["ɨ", "i"],
    "w": ["ʊ", "w"], "y": ["ə", "ɨ"],
    "â": ["aː"], "ê": ["eː"], "î": ["iː"], "ô": ["oː"],
    "û": ["ɨː"], "ŵ": ["uː"], "ŷ": ["əː"],
    "b": ["b"], "c": ["k"], "d": ["d"],
    "f": ["v"], "ff": ["f"], "g": ["ɡ"],
    "ng": ["ŋ"], "h": ["h"],
    "l": ["l"], "ll": ["ɬ"],
    "m": ["m"], "n": ["n"],
    "p": ["p"], "ph": ["f"],
    "r": ["r"], "rh": ["r̥"],
    "s": ["s"], "t": ["t"], "th": ["θ"],
    "ch": ["x"],
    "dd": ["ð"],
    "j": ["dʒ"],  # loanwords
    "si": ["ʃ"],  # before vowels
    "mh": ["m̥"], "nh": ["n̥"],
}
ALLOPHONES_CY = {
    "p": ["p", "pʰ"], "b": ["b"],
    "t": ["t", "tʰ"], "d": ["d"],
    "k": ["k", "kʰ"], "ɡ": ["ɡ"],
    "f": ["f"], "v": ["v"],
    "θ": ["θ"], "ð": ["ð"],
    "s": ["s"], "ʃ": ["ʃ"],
    "x": ["x"], "h": ["h"],
    "ɬ": ["ɬ"],
    "m": ["m"], "m̥": ["m̥"],
    "n": ["n"], "n̥": ["n̥"], "ŋ": ["ŋ"],
    "l": ["l"], "r": ["r"], "r̥": ["r̥"],
    "w": ["w"], "j": ["j"],
    "dʒ": ["dʒ"],
    "a": ["a"], "aː": ["aː"],
    "ɛ": ["ɛ"], "eː": ["eː"],
    "ɪ": ["ɪ"], "iː": ["iː"],
    "ɔ": ["ɔ"], "oː": ["oː"],
    "ɨ": ["ɨ"], "ɨː": ["ɨː"],
    "ʊ": ["ʊ"], "uː": ["uː"],
    "ə": ["ə"], "əː": ["əː"],
}

# ═══════════════════════════════════════════════════════════════════════════════
# BRETON (br) — modern Brythonic, spoken in Brittany
# ═══════════════════════════════════════════════════════════════════════════════
# Sources: Hemon (1975), Press (1986), Ball & Müller (2009)

GRAPHEMES_BR = {
    "a": ["a"], "e": ["e", "ɛ"], "i": ["i"], "o": ["o", "ɔ"], "u": ["y"],
    "ou": ["u"],
    "â": ["aː"], "ê": ["eː"], "ô": ["oː"],
    "b": ["b"], "d": ["d"], "g": ["ɡ"],
    "p": ["p"], "t": ["t"], "k": ["k"],
    "f": ["f"], "v": ["v"],
    "s": ["s"], "z": ["z"],
    "ch": ["ʃ"], "j": ["ʒ"],
    "c'h": ["x", "h"],
    "gn": ["ɲ"],
    "lh": ["ʎ"],  # some dialects
    "m": ["m"], "n": ["n"],
    "l": ["l"], "r": ["ʁ", "r"],
    "w": ["w"],
    "zh": ["z", "h"],  # varies by dialect: KLT [z], Vannetais [h]
    "h": ["h"],
    "nn": ["n"], "mm": ["m"],
}
ALLOPHONES_BR = {
    "p": ["p"], "b": ["b"],
    "t": ["t"], "d": ["d"],
    "k": ["k"], "ɡ": ["ɡ"],
    "f": ["f"], "v": ["v"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "x": ["x"], "h": ["h"],
    "ɲ": ["ɲ"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "l": ["l"], "ʎ": ["ʎ"],
    "ʁ": ["ʁ", "r"], "r": ["r"],
    "w": ["w"], "j": ["j"],
    "a": ["a"], "aː": ["aː"],
    "e": ["e"], "ɛ": ["ɛ"], "eː": ["eː"],
    "i": ["i"], "o": ["o"], "ɔ": ["ɔ"], "oː": ["oː"],
    "y": ["y"], "u": ["u"],
}

# ═══════════════════════════════════════════════════════════════════════════════
# CORNISH (kw) — revived Brythonic
# ═══════════════════════════════════════════════════════════════════════════════
# Sources: George (1993), Brown (2001) *A Grammar of Modern Cornish*

GRAPHEMES_KW = {
    "a": ["a", "æ"], "e": ["ɛ"], "i": ["ɪ"], "o": ["ɔ"], "u": ["ʊ"],
    "y": ["ɪ", "ə"],
    "b": ["b"], "d": ["d"], "g": ["ɡ"],
    "p": ["p"], "t": ["t"], "k": ["k"],
    "f": ["f"], "v": ["v"],
    "s": ["s"], "z": ["z"],
    "th": ["θ"], "dh": ["ð"],
    "ch": ["tʃ"], "j": ["dʒ"],
    "gh": ["x", "h"],
    "m": ["m"], "n": ["n"],
    "l": ["l"], "r": ["r"],
    "w": ["w"], "h": ["h"],
    "hw": ["ʍ"],
}
ALLOPHONES_KW = {
    "p": ["p"], "b": ["b"],
    "t": ["t"], "d": ["d"],
    "k": ["k"], "ɡ": ["ɡ"],
    "f": ["f"], "v": ["v"],
    "θ": ["θ"], "ð": ["ð"],
    "s": ["s"], "z": ["z"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ"],
    "x": ["x"], "h": ["h"], "ʍ": ["ʍ"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "l": ["l"], "r": ["r"],
    "w": ["w"], "j": ["j"],
    "a": ["a"], "æ": ["æ"], "ɛ": ["ɛ"], "ɪ": ["ɪ"],
    "ɔ": ["ɔ"], "ʊ": ["ʊ"], "ə": ["ə"],
}

# ═══════════════════════════════════════════════════════════════════════════════
# PROTO-GOIDELIC (cel-x-goidelic) — ancestor of Irish, Scots Gaelic, Manx
# ═══════════════════════════════════════════════════════════════════════════════
# Not an ISO code; uses BCP-47 private-use tag.
# Splits from Proto-Celtic by kʷ → k (vs. Brythonic kʷ → p).

GRAPHEMES_GOI = {
    "a": ["a"], "ā": ["aː"], "e": ["e"], "ē": ["eː"],
    "i": ["i"], "ī": ["iː"], "o": ["o"], "ō": ["oː"],
    "u": ["u"], "ū": ["uː"],
    "b": ["b"], "t": ["t"], "d": ["d"],
    "k": ["k"], "g": ["ɡ"],
    "s": ["s"], "f": ["f"],  # f < *sw- or Latin loans
    "h": ["h"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "l": ["l"], "r": ["r"],
    "w": ["w"], "j": ["j"],
}
ALLOPHONES_GOI = {
    "b": ["b", "β", "v"], "t": ["t", "θ"], "d": ["d", "ð"],
    "k": ["k", "x"], "ɡ": ["ɡ", "ɣ"],
    "s": ["s", "ʃ"], "f": ["f"], "h": ["h"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "l": ["l", "ʎ"], "r": ["r"],
    "w": ["w"], "j": ["j"],
    "a": ["a"], "aː": ["aː"], "e": ["e"], "eː": ["eː"],
    "i": ["i"], "iː": ["iː"], "o": ["o"], "oː": ["oː"],
    "u": ["u"], "uː": ["uː"],
}

# ═══════════════════════════════════════════════════════════════════════════════
# IRISH (ga) — modern Goidelic
# ═══════════════════════════════════════════════════════════════════════════════
# Sources: Ó Siadhail (1989), Ní Chasaide (1999), de Bhaldraithe (1966)
# Standard Irish (An Caighdeán Oifigiúil) phonology

GRAPHEMES_GA = {
    "a": ["a", "ɑ"], "á": ["aː"], "e": ["ɛ"], "é": ["eː"],
    "i": ["ɪ"], "í": ["iː"], "o": ["ɔ"], "ó": ["oː"],
    "u": ["ʊ"], "ú": ["uː"],
    "b": ["bˠ", "bʲ"], "bh": ["w", "vʲ"],
    "c": ["k", "c"], "ch": ["x", "ç"],
    "d": ["d̪ˠ", "dʲ"], "dh": ["ɣ", "j"],
    "f": ["fˠ", "fʲ"], "fh": [""],  # silent
    "g": ["ɡ", "ɟ"], "gh": ["ɣ", "j"],
    "h": ["h"],
    "l": ["l̪ˠ", "lʲ"],
    "m": ["mˠ", "mʲ"], "mh": ["w", "vʲ"],
    "n": ["n̪ˠ", "nʲ"],
    "p": ["pˠ", "pʲ"], "ph": ["fˠ", "fʲ"],
    "r": ["ɾˠ", "ɾʲ"],
    "s": ["sˠ", "ʃ"], "sh": ["h"],
    "t": ["t̪ˠ", "tʲ"], "th": ["h"],
    "ng": ["ŋ", "ɲ"],
}
ALLOPHONES_GA = {
    "pˠ": ["pˠ"], "pʲ": ["pʲ"],
    "bˠ": ["bˠ"], "bʲ": ["bʲ"],
    "t̪ˠ": ["t̪ˠ"], "tʲ": ["tʲ"],
    "d̪ˠ": ["d̪ˠ"], "dʲ": ["dʲ"],
    "k": ["k"], "c": ["c"],
    "ɡ": ["ɡ"], "ɟ": ["ɟ"],
    "fˠ": ["fˠ"], "fʲ": ["fʲ"],
    "sˠ": ["sˠ"], "ʃ": ["ʃ"],
    "x": ["x"], "ç": ["ç"],
    "ɣ": ["ɣ"], "h": ["h"],
    "w": ["w"], "vʲ": ["vʲ"], "j": ["j"],
    "l̪ˠ": ["l̪ˠ"], "lʲ": ["lʲ"],
    "mˠ": ["mˠ"], "mʲ": ["mʲ"],
    "n̪ˠ": ["n̪ˠ"], "nʲ": ["nʲ"],
    "ŋ": ["ŋ"], "ɲ": ["ɲ"],
    "ɾˠ": ["ɾˠ"], "ɾʲ": ["ɾʲ"],
    "a": ["a"], "ɑ": ["ɑ"], "aː": ["aː"],
    "ɛ": ["ɛ"], "eː": ["eː"],
    "ɪ": ["ɪ"], "iː": ["iː"],
    "ɔ": ["ɔ"], "oː": ["oː"],
    "ʊ": ["ʊ"], "uː": ["uː"],
    "ə": ["ə"],
}

# ═══════════════════════════════════════════════════════════════════════════════
# SCOTTISH GAELIC (gd) — modern Goidelic
# ═══════════════════════════════════════════════════════════════════════════════
# Sources: Ó Baoill (2010), Gillies (2009), Ó Maolalaigh (2008)
# Broad/slender distinction as in Irish but different realisations.

GRAPHEMES_GD = {
    "a": ["a"], "à": ["aː"], "e": ["e", "ɛ"], "è": ["ɛː"],
    "é": ["eː"],
    "i": ["i", "ɪ"], "ì": ["iː"], "o": ["ɔ"], "ò": ["ɔː"],
    "ó": ["oː"],
    "u": ["u", "ʊ"], "ù": ["uː"],
    "b": ["p", "b"], "bh": ["v"],
    "c": ["kʰ", "cʰ"], "ch": ["x", "ç"],
    "d": ["t̪", "dʲ"], "dh": ["ɣ", "j"],
    "f": ["f"], "fh": [""],  # silent
    "g": ["k", "ɟ"], "gh": ["ɣ", "j"],
    "h": ["h"],
    "l": ["l̪ˠ", "lʲ"],
    "m": ["m"], "mh": ["v"],
    "n": ["n̪ˠ", "nʲ"], "nn": ["n̪ˠː"],
    "p": ["pʰ"], "ph": ["f"],
    "r": ["r", "ɾ"],
    "s": ["s", "ʃ"], "sh": ["h"],
    "t": ["t̪ʰ", "tʲ"], "th": ["h"],
    "ng": ["ŋ"],
}
ALLOPHONES_GD = {
    "p": ["p", "pʰ"], "b": ["b"],
    "t̪": ["t̪", "t̪ʰ"], "tʲ": ["tʲ"],
    "k": ["k"], "kʰ": ["kʰ"], "cʰ": ["cʰ"],
    "ɟ": ["ɟ"],
    "f": ["f"], "v": ["v"],
    "s": ["s"], "ʃ": ["ʃ"],
    "x": ["x"], "ç": ["ç"],
    "ɣ": ["ɣ"], "h": ["h"], "j": ["j"],
    "l̪ˠ": ["l̪ˠ"], "lʲ": ["lʲ"],
    "m": ["m"], "n̪ˠ": ["n̪ˠ"], "nʲ": ["nʲ"],
    "n̪ˠː": ["n̪ˠː"],
    "ŋ": ["ŋ"],
    "r": ["r"], "ɾ": ["ɾ"],
    "w": ["w"],
    "a": ["a"], "aː": ["aː"],
    "e": ["e"], "ɛ": ["ɛ"], "eː": ["eː"], "ɛː": ["ɛː"],
    "i": ["i"], "ɪ": ["ɪ"], "iː": ["iː"],
    "ɔ": ["ɔ"], "ɔː": ["ɔː"], "oː": ["oː"],
    "u": ["u"], "ʊ": ["ʊ"], "uː": ["uː"],
    "ə": ["ə"],
}

# ═══════════════════════════════════════════════════════════════════════════════
# MANX (gv) — Goidelic, extinct as L1 in 1974, revived
# ═══════════════════════════════════════════════════════════════════════════════
# Sources: Thomson (1992), Broderick (1984), Jackson (1955)
# English-influenced orthography (unlike Irish/Scots Gaelic).

GRAPHEMES_GV = {
    "a": ["a", "æ"], "aa": ["eː"], "e": ["ɛ"], "ee": ["iː"],
    "i": ["ɪ", "ə"], "oo": ["uː"], "o": ["ɔ"],
    "u": ["ʊ", "ɤ"],
    "b": ["b"], "d": ["d"], "g": ["ɡ"],
    "p": ["p"], "t": ["t"], "k": ["k"],
    "c": ["k"], "ck": ["k"],
    "f": ["f"], "v": ["v"],
    "s": ["s"], "sh": ["ʃ"],
    "th": ["θ", "ð"],  # varies
    "ch": ["x"], "gh": ["ɣ"],
    "m": ["m"], "n": ["n"],
    "l": ["l"], "r": ["r", "ɾ"],
    "w": ["w"], "y": ["j"],
    "h": ["h"],
    "j": ["dʒ"],
    "qu": ["kw"],
}
ALLOPHONES_GV = {
    "p": ["p"], "b": ["b"],
    "t": ["t"], "d": ["d"],
    "k": ["k"], "ɡ": ["ɡ"],
    "f": ["f"], "v": ["v"],
    "θ": ["θ"], "ð": ["ð"],
    "s": ["s"], "ʃ": ["ʃ"],
    "x": ["x"], "ɣ": ["ɣ"],
    "h": ["h"],
    "dʒ": ["dʒ"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "l": ["l"], "r": ["r"], "ɾ": ["ɾ"],
    "w": ["w"], "j": ["j"],
    "a": ["a"], "æ": ["æ"],
    "ɛ": ["ɛ"], "eː": ["eː"],
    "ɪ": ["ɪ"], "iː": ["iː"],
    "ɔ": ["ɔ"], "oː": ["oː"],
    "ʊ": ["ʊ"], "uː": ["uː"],
    "ə": ["ə"], "ɤ": ["ɤ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SPECS
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    # ── Proto-Celtic (root) ──────────────────────────────────────────────
    "cel": LanguageSpec(
        code="cel",
        name="Proto-Celtic (reconstructed)",
        family="Celtic",
        script="Latin",
        graphemes=GRAPHEMES_CEL,
        allophones=ALLOPHONES_CEL,
        parent="ine",
        notes=(
            "Proto-Celtic (~1200–800 BCE). Reconstructed common ancestor "
            "of all Celtic languages. Defining innovation: PIE *p → *ɸ → ∅ "
            "(complete p-loss). Other key changes: *gʷ → b, *ē → *ī, "
            "*ew → *ow. Preserves PIE labiovelars (*kʷ splits later: "
            "Goidelic → /k/, Brythonic → /p/). Incipient lenition of "
            "intervocalic stops. Source: Matasović (2009)."
        ),
    ),

    # ── Transalpine Gaulish (THE Gaulish substrate of French) ────────────
    "xtg": LanguageSpec(
        code="xtg",
        name="Transalpine Gaulish",
        family="Celtic",
        script="Latin",
        graphemes=GRAPHEMES_XTG,
        allophones=ALLOPHONES_XTG,
        parent="cel",
        notes=(
            "Transalpine Gaulish (6th c. BCE – 5th c. CE). ISO 639-3: xtg. "
            "Continental Celtic language of Gaul (modern France, Belgium, "
            "Switzerland). ~800+ inscriptions including Larzac, Chamalières "
            "tablets and Coligny calendar. "
            "THE key substrate for French and Gallo-Romance. "
            "Distinctive 'tau gallicum' /ts/ < *t (fronting). "
            "Nasal vowels attested. Celtic p-loss. Lenition well-developed. "
            "Vigesimal counting inherited by French (quatre-vingts). "
            "~200 words in French (Lambert 2003, Delamarre 2003). "
            "Written in Greek (south), Latin (north), and Lugano alphabets. "
        ),
    ),
    "xcg": LanguageSpec(
        code="xcg", name="Cisalpine Gaulish",
        family="Celtic", script="Latin",
        graphemes=GRAPHEMES_XCG, allophones=ALLOPHONES_XCG,
        parent="cel",
        notes=(
            "Cisalpine Gaulish (4th–1st c. BCE). Celtic of the Po valley "
            "(northern Italy), brought by La Tène Gauls. Overlays earlier "
            "Lepontic. Written in Lugano and Latin alphabets. Shares "
            "phonology with Transalpine but distinct epigraphic tradition. "
            "Refs: Lejeune (1971), Eska (2006)."
        ),
    ),
    # ── Lepontic (Cisalpine Celtic) ──────────────────────────────────────
    "xlp": LanguageSpec(
        code="xlp",
        name="Lepontic",
        family="Celtic",
        script="Latin",
        graphemes=GRAPHEMES_XLP,
        allophones=ALLOPHONES_XLP,
        parent="cel",
        notes=(
            "Lepontic (6th–3rd c. BCE). ISO 639-3: xlp. "
            "Earliest attested Celtic language. ~140 inscriptions from "
            "Cisalpine Gaul (Lombardy, Piedmont, Ticino, Trentino). "
            "Oldest text: Prestino stone (~575 BCE, Como). "
            "Written in Lugano alphabet (Etruscan-derived). "
            "Relationship to Transalpine Gaulish debated: "
            "Lejeune (1971) treats as Cisalpine Gaulish dialect; "
            "Eska & Stifter treat as separate language. "
            "Celtic p-loss; tau gallicum present. "
            "Distinctive /u/ > /o/ shift in some environments. "
            "Absorbed by Transalpine Gaulish influence and then Latin "
            "(post-191 BCE Roman conquest of Cisalpine Gaul). "
            "Refs: Lejeune (1971), Solinas (1995), Eska (2006)."
        ),
    ),

    # ── Galatian (Anatolian Celtic) ──────────────────────────────────────
    "xga": LanguageSpec(
        code="xga",
        name="Galatian",
        family="Celtic",
        script="Greek",
        graphemes=GRAPHEMES_XGA,
        allophones=ALLOPHONES_XGA,
        parent="cel",
        notes=(
            "Galatian (3rd c. BCE – 5th c. CE). ISO 639-3: xga. "
            "Celtic of central Anatolia (modern Ankara region). "
            "Spoken by Galatians — Celts who migrated from Balkans/Thrace "
            "to Asia Minor in 278 BCE (invited by Nicomedes I of Bithynia). "
            "Attestation: extremely sparse — ~120 glosses, personal names, "
            "and tribal names in Greek/Latin sources. No continuous texts. "
            "Jerome (347–420 CE) claimed Galatian was similar to Gaulish "
            "spoken around Trier. "
            "Celtic p-loss maintained. Beyond this, phonology is largely "
            "inferred from Gaulish comparison and Greek transcriptions. "
            "Speculative phonetics — included to close the Continental "
            "Celtic subtree. "
            "Refs: Freeman (2001), Mitchell (1993), Strobel (1996)."
        ),
    ),

    # ── Common Brythonic (Insular Celtic) ────────────────────────────────
    "xbr": LanguageSpec(
        code="xbr",
        name="Common Brythonic",
        family="Celtic",
        script="Latin",
        graphemes=GRAPHEMES_XBR,
        allophones=ALLOPHONES_XBR,
        parent="cel",
        notes=(
            "Common Brythonic / Proto-Brythonic. Celtic language of "
            "pre-Roman and Roman Britain. Ancestor of Welsh, Cornish, "
            "Breton. Substrate in English: place names (London, Thames, "
            "Kent, Dover), possibly influence on English phonology. "
            "Voiceless lateral /ɬ/ and voiceless rhotic /r̥/ are "
            "diagnostic features. "
            "Refs: Jackson (1953), Schrijver (1995)."
        ),
    ),
    "cy": LanguageSpec(
        code="cy", name="Welsh",
        family="Celtic", script="Latin",
        graphemes=GRAPHEMES_CY, allophones=ALLOPHONES_CY,
        parent="xbr",
        ancestors=(
            Ancestor("xbr", P, 0.90, "Descent from Common Brythonic"),
            Ancestor("la", AD, 0.05, "Latin adstrate: heavy lexical borrowing from Roman period"),
            Ancestor("en", AD, 0.03, "English adstrate: loanwords, contact influence"),
        ),
        notes=(
            "Welsh (Cymraeg). ~880,000 speakers (2021 census). "
            "Voiceless lateral /ɬ/ (⟨ll⟩), voiceless nasal /m̥ n̥/ (⟨mh nh⟩), "
            "voiceless rhotic /r̥/ (⟨rh⟩), velar fricative /x/ (⟨ch⟩). "
            "Initial consonant mutation: soft, nasal, aspirate. "
            "Stress on penultimate syllable. "
            "Refs: Thomas (1996), Ball & Müller (2009)."
        ),
    ),
    "br": LanguageSpec(
        code="br", name="Breton",
        family="Celtic", script="Latin",
        graphemes=GRAPHEMES_BR, allophones=ALLOPHONES_BR,
        parent="xbr",
        ancestors=(
            Ancestor("xbr", P, 0.85, "Descent from Common Brythonic via insular settlers"),
            Ancestor("fr", AD, 0.08, "French adstrate: heavy lexical and phonological influence"),
            Ancestor("xtg", SUB, 0.03, "Gaulish substrate traces in Armorican territory"),
        ),
        notes=(
            "Breton (Brezhoneg). ~200,000 speakers (est. 2020). Brittany, France. "
            "Brought from Britain by insular Brythonic speakers (~5th–6th c. CE). "
            "Four main dialects: Léonard (KLT basis), Trégorrois, Cornouaillais, "
            "Vannetais (most divergent). ⟨c'h⟩ = /x/; ⟨zh⟩ = /z/ (KLT) or /h/ (Vannetais). "
            "French strongly influenced phonology (uvular /ʁ/, nasal vowels in loans). "
            "Refs: Hemon (1975), Press (1986)."
        ),
    ),
    "kw": LanguageSpec(
        code="kw", name="Cornish",
        family="Celtic", script="Latin",
        graphemes=GRAPHEMES_KW, allophones=ALLOPHONES_KW,
        parent="xbr",
        ancestors=(
            Ancestor("xbr", P, 0.88, "Descent from Common Brythonic"),
            Ancestor("en", AD, 0.07, "English adstrate: heavy contact influence pre-extinction"),
        ),
        notes=(
            "Cornish (Kernewek). Revived language; last native speaker died 1777. "
            "Revival since early 20th c.; ~3,000 speakers (est. 2020). "
            "Three main revival orthographies: Kernewek Standard, Kernewek Unys, Spellyans. "
            "This spec follows revived Kernewek Standard pronunciation. "
            "Refs: George (1993), Brown (2001)."
        ),
    ),

    # ── Insular Celtic: Goidelic ─────────────────────────────────────────────
    "cel-x-goidelic": LanguageSpec(
        code="cel-x-goidelic", name="Proto-Goidelic (reconstructed)",
        family="Celtic", script="Latin",
        graphemes=GRAPHEMES_GOI, allophones=ALLOPHONES_GOI,
        parent="cel",
        notes=(
            "Proto-Goidelic. Ancestral to Irish, Scottish Gaelic, Manx. "
            "Key split from Proto-Celtic: PIE *kʷ → /k/ (Q-Celtic), "
            "vs. Brythonic *kʷ → /p/ (P-Celtic). "
            "Developed /f/ from *sw- and Latin loans. "
            "Broad/slender consonant distinction incipient."
        ),
    ),
    "ga": LanguageSpec(
        code="ga", name="Irish",
        family="Celtic", script="Latin",
        graphemes=GRAPHEMES_GA, allophones=ALLOPHONES_GA,
        parent="cel-x-goidelic",
        ancestors=(
            Ancestor("cel-x-goidelic", P, 0.90, "Goidelic descent"),
        ),
        notes=(
            "Irish (Gaeilge). ~1.7M speakers (2016 census; ~80K daily L1). "
            "PERVASIVE BROAD/SLENDER DISTINCTION: every consonant has two "
            "versions (velarised 'broad' vs. palatalised 'slender'). "
            "Initial mutation: lenition (séimhiú) and eclipsis (urú). "
            "Three main dialects: Munster, Connacht, Ulster. "
            "An Caighdeán Oifigiúil = written standard. "
            "Substrate of Hiberno-English (dental stops for θ/ð). "
            "Refs: Ó Siadhail (1989), Ní Chasaide (1999)."
        ),
    ),
    "gd": LanguageSpec(
        code="gd", name="Scottish Gaelic",
        family="Celtic", script="Latin",
        graphemes=GRAPHEMES_GD, allophones=ALLOPHONES_GD,
        parent="cel-x-goidelic",
        ancestors=(
            Ancestor("cel-x-goidelic", P, 0.88, "Goidelic descent"),
        ),
        notes=(
            "Scottish Gaelic (Gàidhlig). ~57,000 speakers (2011 census). "
            "Highlands and Islands of Scotland. "
            "Pre-aspiration of voiceless stops (diagnostic feature vs. Irish). "
            "Broad/slender distinction as in Irish. "
            "Lenition system similar to Irish. "
            "Substrate of Scottish English (/x/ in 'loch'). "
            "Refs: Ó Baoill (2010), Gillies (2009)."
        ),
    ),
    "gv": LanguageSpec(
        code="gv", name="Manx",
        family="Celtic", script="Latin",
        graphemes=GRAPHEMES_GV, allophones=ALLOPHONES_GV,
        parent="cel-x-goidelic",
        ancestors=(
            Ancestor("cel-x-goidelic", P, 0.85, "Goidelic descent"),
            Ancestor("en", AD, 0.10, "English adstrate: heavy influence, English-based orthography"),
        ),
        notes=(
            "Manx (Gaelg). Isle of Man. Last native speaker (Ned Maddrell) "
            "died 1974. Revival since 1970s; ~1,800 speakers (est. 2020). "
            "English-based orthography (unlike Irish/Scots Gaelic). "
            "Simplified mutation system vs. Irish/Scots Gaelic. "
            "Refs: Thomson (1992), Broderick (1984)."
        ),
    ),
}