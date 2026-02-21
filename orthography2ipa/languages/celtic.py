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


# ═══════════════════════════════════════════════════════════════════════════
# LEPONTIC (xlp)
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
# GALATIAN (xga)
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
}