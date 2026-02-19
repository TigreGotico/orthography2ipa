"""Celtic languages — Proto-Celtic and Gaulish.

Ancestry for Celtiberian (xce). Proto-Celtic is the reconstructed common
ancestor; Gaulish is the best-attested Continental Celtic language and the
closest comparandum to Celtiberian (they share the Continental branch).

Sources:
- Matasović, R. (2009). *Etymological Dictionary of Proto-Celtic*. Brill.
- Lambert, P.-Y. (2003). *La langue gauloise*. 2nd ed. Errance.
- Stifter, D. (2006). *Sengoídelc*. Syracuse UP.
- Eska, J.F. (2006). "The genitive singular in Continental Celtic."
- McCone, K. (1996). *Towards a Relative Chronology of Ancient and
  Medieval Celtic Sound Change*. Maynooth.
- Delamarre, X. (2003). *Dictionnaire de la langue gauloise*. Errance.
"""
from orthography2ipa.types import LanguageSpec

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
# GAULISH (xcg)
# ═══════════════════════════════════════════════════════════════════════════
#
# Classification: Celtic > Continental Celtic > Gallo-Brittonic (debated)
# Attestation: ~800+ inscriptions, including:
#   - Larzac lead tablet (longest: ~1000 characters, magical/juridical)
#   - Chamalières lead tablet (magical)
#   - Coligny calendar (astronomical/ritual, ~2nd c. CE)
#   - Lezoux graffiti, La Graufesenque accounts
#   - Many coin legends, potters' marks, votive inscriptions
# Scripts: (a) Greek alphabet (southern Gaul, Massalia influence)
#          (b) Latin alphabet (central/northern Gaul)
#          (c) Lepontic/Lugano alphabet (Cisalpine)
# Geography: Gaul (modern France, Belgium, Switzerland, N. Italy)
# Time: ~3rd century BCE to ~5th century CE
#
# Gaulish is the best-attested Continental Celtic language and the
# primary comparandum for Celtiberian. They share:
#   - p-loss (hallmark Celtic feature)
#   - Some treatment of labiovelars
#   - Continental innovations not shared with Insular Celtic
#
# KEY PHONOLOGICAL FEATURES:
#   - /p/ absent in native words (Celtic p-loss)
#   - /ts/ < PIE *t before certain vowels (Lambert)
#   - Nasal vowels (well-attested in spelling variations)
#   - Tau Gallicum: /ts/ (a distinctive Gaulish sound, possibly [θ] or [ts])
#   - /x/ attested (from lenition of /k/)
#   - Long vowels well-established from Greek-alphabet spellings

GRAPHEMES_XCG = {
    # --- Vowels ---
    "a": ["a"], "ā": ["aː"],
    "e": ["e"], "ē": ["eː"],
    "i": ["i"], "ī": ["iː"],
    "o": ["o"], "ō": ["oː"],
    "u": ["u"], "ū": ["uː"],

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

    # --- Glides ---
    "u": ["u", "w"],
    "i": ["i", "j"],

    # --- Geminates ---
    "ss": ["sː"],
    "ll": ["lː"],
    "nn": ["nː"],
    "rr": ["rː"],
    "dd": ["dː"],
    "cc": ["kː"],
    "tt": ["tː"],
}

ALLOPHONES_XCG = {
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

SPECS = {
    "cel": LanguageSpec(
        code="cel", name="Proto-Celtic (reconstructed)",
        family="Celtic", script="Latin",
        graphemes=GRAPHEMES_CEL, allophones=ALLOPHONES_CEL,
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
    "xcg": LanguageSpec(
        code="xcg", name="Gaulish",
        family="Celtic", script="Latin",
        graphemes=GRAPHEMES_XCG, allophones=ALLOPHONES_XCG,
        parent="cel", notes=(
            "Gaulish (3rd c. BCE – 5th c. CE). Best-attested Continental "
            "Celtic language, ~800+ inscriptions. Primary comparandum for "
            "Celtiberian. Distinctive 'tau gallicum' [ts] < *t (fronting). "
            "Nasal vowels attested. Celtic p-loss. Lenition well-developed. "
            "Written in Greek, Latin, and Lepontic alphabets. Key texts: "
            "Larzac tablet, Chamalières tablet, Coligny calendar."
        ),
    ),
}
