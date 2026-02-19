"""Arabic — Iraqi, Chadian, Nigerian (Shuwa), and Cypriot Maronite dialects.

These four varieties complete the coverage of Arabic dialects outside the main
Mashriqi/Maghrebi/Peninsular clusters, each representing a distinct contact
situation and phonological trajectory.

Genealogy sketch:
  Classical Arabic (arb)
       ├── ar-x-mashriqi  →  ar-IQ  (Iraqi — Eastern branch)
       ├── ar-x-maghrebi  →  ar-TD  (Chadian — peripheral Maghrebi)
       │                  →  ar-NG  (Nigerian Shuwa — far periphery)
       └── arb            →  acy    (Cypriot Maronite — isolated/extinct)

Sources:
- Blanc, H. (1964). *Communal Dialects in Baghdad*. Harvard UP.
  [THE reference for Iraqi Arabic; Muslim/Jewish/Christian registers]
- Erwin, W.M. (1963). *A Short Reference Grammar of Iraqi Arabic*. Georgetown.
- Woodhead, D.R. & Beene, W. (1967). *A Dictionary of Iraqi Arabic*. Georgetown.
- Owens, J. (1993). *A Reference Grammar of Nigerian Arabic*. Harrassowitz.
  [Comprehensive Shuwa grammar]
- Owens, J. (1985). *The Foundations of Grammar: An Introduction to
  Medieval Arabic Grammatical Theory*. Benjamins. [Chadian comparison]
- Khalafallah, A. (1969). *A Descriptive Grammar of Saidī Arabic*. Mouton.
- Zaborski, A. (1990). "Chadic-Arabic Contacts." Afrika und Übersee 73.
- Lucas, C. & Čéplö, S. eds. (2016). *Clitic and Affix Combinations*.
  Benjamins. [Cypriot Maronite Arabic chapter]
- Tsiapera, M. (1969). *A Descriptive Analysis of Cypriot Maronite Arabic*.
  Mouton.
- Borg, A. (1985). *Cypriot Arabic*. Deutsche Morgenländische Gesellschaft.
- Versteegh, K. (2014). *The Arabic Language*. 2nd ed. Edinburgh UP.
- Watson, J.C.E. (2002). *The Phonology and Morphology of Arabic*. OUP.
- Holes, C. (2004). *Modern Arabic*. Georgetown UP.
"""

from orthography2ipa.languages.ar_classical import (
    GRAPHEMES_MASHRIQI_BASE, ALLOPHONES_MASHRIQI_BASE,
)
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
AD = AncestorRole.ADSTRATE
SUP = AncestorRole.SUPERSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# IRAQI ARABIC (ar-IQ)
# ═══════════════════════════════════════════════════════════════════════════
#
# Iraqi Arabic (ʕarabī ʕirāqī) is one of the most internally varied of all
# Arabic dialects, with significant differences between:
#   1. Baghdad Muslim Arabic (the prestigious urban variety)
#   2. Baghdad Jewish Arabic (now largely extinct; Blanc 1964)
#   3. Baghdad Christian Arabic (a distinct "qəltu" dialect)
#   4. Northern / Mosul Arabic (qəltu type, more conservative)
#   5. Southern / Basra Arabic (gilit type, Bedouin-influenced)
#
# The fundamental IRAQI DIALECT SPLIT:
#   "gilit" dialects (southern, Bedouin-origin):
#     - ق → /ɡ/ (voiced velar — Bedouin feature preserved)
#     - ج → /dʒ/ or /ɡ/
#     - Shorter unstressed vowels
#   "qəltu" dialects (northern, urban sedentary-origin):
#     - ق → /q/ (preserved uvular)
#     - ج → /dʒ/
#     - More conservative vowel system
#     - Closer to Classical Arabic morphology
#
# SHARED IRAQI FEATURES (vs. other Eastern Arabic):
#   - ث → /θ/ (PRESERVED — unlike Levantine/Egyptian where θ → t)
#     This is a defining Iraqi conservative feature
#   - ذ → /ð/ (PRESERVED)
#   - ظ → /ðˤ/ (PRESERVED — emphatic interdental maintained)
#   - ض → /dˤ/ (lateral lost, but ذˤ → ðˤ still distinct)
#   - k → /tʃ/ before front vowels in some varieties (Gulf feature shared)
#   - Extensive Persian loanwords (reflecting proximity to Iran)
#   - Turkish loanwords (Ottoman period, 1534–1918)
#   - p and v as established phonemes (from Persian/Turkish/English)
#   - New vowel /e/ and /o/ from contact languages

# ── Iraqi "gilit" base (southern/Bedouin — Baghdad Muslim) ──────────────

GRAPHEMES_IQ_GILIT = {
    **GRAPHEMES_MASHRIQI_BASE,
    # CONSERVATIVE: interdentals PRESERVED
    "ث": ["θ"],  # voiceless interdental — PRESERVED in Iraqi
    "ذ": ["ð"],  # voiced interdental — PRESERVED
    "ظ": ["ðˤ"],  # emphatic interdental — PRESERVED
    "ض": ["dˤ"],  # lateral lost → dˤ
    # gilit: ق → ɡ
    "ق": ["ɡ"],  # Bedouin/southern: voiced velar stop
    "ج": ["dʒ"],
    # Contact language phonemes
    "پ": ["p"],
    "ڤ": ["v"],
    "چ": ["tʃ"],
    "ژ": ["ʒ"],
    "e": ["e"],
    "o": ["o"],
}

ALLOPHONES_IQ_GILIT = {
    **ALLOPHONES_MASHRIQI_BASE,
    # Interdentals preserved
    "θ": ["θ"],
    "ð": ["ð"],
    "ðˤ": ["ðˤ"],
    "ɮˤ": ["dˤ"],
    # ق → ɡ in gilit
    "q": ["ɡ"],
    "ɡ": ["ɡ"],
    "dʒ": ["dʒ"],
    # k → tʃ before front vowels (some speakers)
    "k": ["k", "tʃ"],
    # Vowels
    "a": ["a", "æ", "ɑ"],
    "aː": ["aː", "eː"],  # imāla in some environments
    "e": ["e"],
    "o": ["o"],
    "p": ["p"],
    "v": ["v"],
    "tʃ": ["tʃ"],
    "ʒ": ["ʒ"],
    "n": ["n", "m", "ŋ"],
}

# ── Iraqi "qəltu" base (northern/sedentary — Mosul, Christian Baghdad) ──

GRAPHEMES_IQ_QELTU = {
    **GRAPHEMES_IQ_GILIT,
    # qəltu: ق preserved as uvular
    "ق": ["q"],  # conservative uvular preserved
}

ALLOPHONES_IQ_QELTU = {
    **ALLOPHONES_IQ_GILIT,
    "q": ["q"],  # uvular preserved (not ɡ as in gilit)
}

# ═══════════════════════════════════════════════════════════════════════════
# CHADIAN ARABIC (ar-TD)
# ═══════════════════════════════════════════════════════════════════════════
#
# Chadian Arabic (ʕarabī šuwā) — also called "Shuwa" though this term
# is sometimes restricted to Nigerian Arabic — is spoken in Chad, northern
# Cameroon, northeastern Nigeria, and the Central African Republic.
# It derives from the Arabic that arrived with the trans-Saharan trade
# routes from the east (Sudan) and northwest (Maghreb).
#
# PHONOLOGICAL PROFILE:
#   - Generally conservative in consonant inventory
#   - θ and ð often preserved (like Sudanese/Gulf — not merged)
#   - ق → /q/ preserved
#   - ج → /dʒ/ preserved (not /ɡ/ as in Egyptian)
#   - ض → /dˤ/ (lateral lost)
#   - ظ → /dˤ/ (merged with ض in many Chadian varieties)
#   - Extreme vowel reduction in some varieties (sub-Saharan influence)
#   - New phonemes from Sub-Saharan contact languages:
#     /ŋ/ (from Chadic languages: Hausa, Kanuri, Sara)
#     implosives [ɓ, ɗ] attested in some varieties from sub-Saharan substrate
#   - Some prenasalised stops [ᵐb, ⁿd] in contact-influenced speech
#
# Substrate: Chadic languages (Hausa, Kanuri, Sara, Maba, Fulani) are
# profound substrates, introducing phonological features typologically
# unusual in Arabic.

GRAPHEMES_TD = {
    **GRAPHEMES_MASHRIQI_BASE,
    "ث": ["θ", "t"],  # θ often preserved
    "ذ": ["ð", "d"],  # ð often preserved
    "ظ": ["dˤ"],  # merged with ض in most Chadian
    "ض": ["dˤ"],
    "ق": ["q"],  # uvular preserved
    "ج": ["dʒ"],
}

ALLOPHONES_TD = {
    **ALLOPHONES_MASHRIQI_BASE,
    "θ": ["θ", "t"],
    "ð": ["ð", "d"],
    "ðˤ": ["dˤ"],
    "ɮˤ": ["dˤ"],
    "q": ["q"],
    "dʒ": ["dʒ"],
    # Sub-Saharan substrate features
    "b": ["b", "ɓ"],  # implosive allophone in some varieties
    "d": ["d", "ɗ"],  # implosive allophone in some varieties
    "n": ["n", "ŋ", "m"],
    "ŋ": ["ŋ"],  # phonemic in Chadic-influenced varieties
    # Vowels — moderate reduction
    "a": ["a", "ə"],
    "i": ["i", "ə"],
    "u": ["u", "ə"],
    "aː": ["aː"],
}

# ═══════════════════════════════════════════════════════════════════════════
# NIGERIAN (SHUWA) ARABIC (ar-NG)
# ═══════════════════════════════════════════════════════════════════════════
#
# Nigerian Arabic — known as "Shuwa Arabic" after the Shuwa Arab ethnic group
# — is spoken in northeastern Nigeria (Borno, Yobe states), Cameroon,
# Niger, and Chad. It is closely related to Chadian Arabic but has developed
# under intense contact with Hausa, Kanuri, and Fulani (Fula).
#
# It is one of the most contact-modified Arabic varieties and has acquired
# phonological features entirely foreign to other Arabic dialects:
#
# PHONOLOGICAL PROFILE:
#   - θ → /t/ (complete merger, Hausa-influenced)
#   - ð → /d/ (complete merger)
#   - ق → /q/ preserved in educated speech; → /ɡ/ in vernacular
#   - ج → /dʒ/ preserved
#   - ض → /dˤ/ (lateral lost)
#   - ظ → /dˤ/ (merged with ض)
#   - TONE: some Shuwa Arabic varieties have acquired lexical tone
#     from Hausa/Kanuri, though this is debated (Owens 1993)
#   - implosives /ɓ, ɗ/ from Hausa substrate (highly marked typologically)
#   - /ŋ/ as phoneme from Hausa (present in many loanwords)
#   - Vowel length contrast reduced in contact-heavy speech

GRAPHEMES_NG = {
    **GRAPHEMES_TD,
    "ث": ["t"],  # complete merger (cf. Chadian still has θ)
    "ذ": ["d"],
    "ق": ["q", "ɡ"],
}

ALLOPHONES_NG = {
    **ALLOPHONES_TD,
    "θ": ["t"],  # no θ allophone in Nigerian Shuwa
    "ð": ["d"],
    "q": ["q", "ɡ"],
    # Hausa substrate: implosives more prominent
    "b": ["b", "ɓ"],
    "d": ["d", "ɗ"],
    # Hausa/Kanuri: /ŋ/ phonemic
    "ŋ": ["ŋ"],
    # Tone-affected vowels in some varieties (approximated)
    "aː": ["aː", "á", "à"],
    "iː": ["iː", "í", "ì"],
    "uː": ["uː", "ú", "ù"],
}

# ═══════════════════════════════════════════════════════════════════════════
# CYPRIOT MARONITE ARABIC (acy)  — endangered / near-extinct
# ═══════════════════════════════════════════════════════════════════════════
#
# Cypriot Maronite Arabic (CMA, locally called "Sanna" or "Arabiya")
# is one of the most unique and endangered Arabic varieties in the world.
# It is spoken by the Maronite Christian community of Cyprus, descended
# from Levantine Arabic speakers who migrated to Cyprus ~8th–12th century CE.
#
# CMA has been almost completely isolated from other Arabic varieties for
# ~800 years, evolving under intense contact with Greek (Cypriot Greek).
# The result is a contact language with Arabic structure but massive Greek
# phonological and lexical influence.
#
# Status: Critically endangered (UNESCO). Perhaps 1,000–2,000 speakers as of
# 2020, mostly elderly. The 1974 Turkish invasion displaced Maronite villages.
#
# PHONOLOGICAL PROFILE — the most Greek-influenced Arabic variety:
#
# Greek influence:
#   1. /θ/ and /ð/ are MAINTAINED but as Greek-style dental fricatives
#      (NOT Arabic interdentals in classical sense — reinforced by Greek)
#   2. Loss of pharyngeals ħ and ʕ → merged with h and ∅
#   3. /q/ → [k] (Hellenisation — Greek has no uvular)
#   4. Gemination pattern from Greek stress system
#   5. New vowels /e/ and /o/ as primary system (Arabic vowels restructured)
#   6. ج → /dʒ/ or /tʃ/ (Greek influence on affricate voicing)
#   7. Loss of most Arabic emphatic quality (emphatics partially deemphasised)
#
# Arabic base:
#   - Still recognisably Arabic morphology
#   - Retains Arabic consonants: f, b, t, d, k, ɡ, s, z, ʃ, m, n, l, r, w, j
#   - Retains /x/ (Arabic خ, also Greek χ)
#
# This is modelled with ISO 639-3 code `acy`.

GRAPHEMES_ACY = {
    # ── Arabic-origin consonants (still present) ─────────────────────────
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "k": ["k"],
    "ɡ": ["ɡ"],
    "f": ["f"],
    "s": ["s"],
    "z": ["z"],
    "ʃ": ["ʃ"],
    "x": ["x"],  # Arabic خ, also aligns with Greek χ
    "h": ["h"],  # ħ merged → h
    "m": ["m"],
    "n": ["n"],
    "l": ["l"],
    "r": ["r"],
    "w": ["w"],
    "j": ["j"],

    # ── Greek-reinforced / modified ───────────────────────────────────────
    "θ": ["θ"],  # maintained (Greek θ reinforces Arabic ث)
    "ð": ["ð"],  # maintained (Greek δ reinforces Arabic ذ)
    "ɣ": ["ɣ"],  # Arabic غ, also Greek γ (intervocalic)
    "dʒ": ["dʒ", "tʃ"],  # ج — voicing variable under Greek influence

    # ── Lost from Arabic ──────────────────────────────────────────────────
    # ħ → h (pharyngeal voiceless lost)
    # ʕ → ∅ or h (pharyngeal voiced lost)
    # q → k (uvular lost; assimilated to Greek phonological space)
    # emphatic series ṣˤ tˤ ðˤ sˤ → mostly deemphasised

    # ── Emphatics (weakened but not entirely lost) ────────────────────────
    "sˤ": ["sˤ", "s"],  # partial deemphasisation in CMA
    "tˤ": ["tˤ", "t"],
    "dˤ": ["dˤ", "d"],

    # ── Greek-origin consonants in loanwords ──────────────────────────────
    "p": ["p"],  # Greek π (Arabic lacks /p/ natively)
    "v": ["v"],  # Greek β [v] in Modern Greek pronunciation

    # ── Vowels — restructured toward Greek system ─────────────────────────
    # Classical Arabic 3-quality + length → CMA 5-quality system
    "a": ["a"],
    "e": ["e"],  # from Greek (replaces Classical short i in some envs)
    "i": ["i"],
    "o": ["o"],  # from Greek
    "u": ["u"],
    # Long vowels maintained but system simplified
    "aː": ["aː"],
    "iː": ["iː"],
    "uː": ["uː"],
    # Greek vowel in full loans
    "ɛː": ["ɛː"],  # Greek η
    "oː": ["oː"],  # Greek ω
}

ALLOPHONES_ACY = {
    "b": ["b"], "p": ["p"],
    "t": ["t"], "d": ["d"],
    "k": ["k"], "ɡ": ["ɡ"],
    "ʔ": ["h", "∅"],  # hamza weakened → h or deleted
    # Interdentals (maintained via Greek reinforcement)
    "θ": ["θ"], "ð": ["ð"],
    # Fricatives
    "f": ["f"], "v": ["v"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"],
    "x": ["x"], "ɣ": ["ɣ"],
    "h": ["h", "∅"],
    # Pharyngeals LOST
    "ħ": ["h", "∅"],  # pharyngeal → h or zero
    "ʕ": ["∅", "h"],  # pharyngeal lost
    # q → k (uvular lost)
    "q": ["k"],
    # Affricate
    "dʒ": ["dʒ", "tʃ"],
    # Emphatics (weakened)
    "sˤ": ["sˤ", "s"],
    "tˤ": ["tˤ", "t"],
    "dˤ": ["dˤ", "d"],
    # Nasals
    "m": ["m"], "n": ["n", "m", "ŋ"],
    # Liquids
    "l": ["l"], "r": ["r", "ɾ"],
    # Glides
    "w": ["w"], "j": ["j"],
    # Vowels
    "a": ["a"], "aː": ["aː"],
    "e": ["e"], "eː": ["eː"],
    "i": ["i"], "iː": ["iː"],
    "o": ["o"], "oː": ["oː"],
    "u": ["u"], "uː": ["uː"],
    "ɛː": ["ɛː"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SPECS
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "ar-IQ": LanguageSpec(
        code="ar-IQ",
        name="Iraqi Arabic (Baghdad / gilit)",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_IQ_GILIT,
        allophones=ALLOPHONES_IQ_GILIT,
        parent="ar-x-mashriqi",
        ancestors=(
            Ancestor("ar-x-mashriqi", P, 0.88,
                     "Eastern Arabic base"),
            Ancestor("arb", P, 0.85,
                     "Classical Arabic descent"),
            Ancestor("fa", AD, 0.05,
                     "Persian adstrate: extensive loanwords; /p/, /v/, /tʃ/, /ʒ/ "
                     "phonemes; some phonological calques"),
        ),
        notes=(
            "Iraqi Arabic — Baghdad Muslim / southern 'gilit' variety. "
            "CONSERVATIVE FEATURE: θ (ث) and ð (ذ) and ðˤ (ظ) PRESERVED "
            "as interdentals — unlike Levantine/Egyptian where they merge to t/d. "
            "GILIT FEATURE: ق → /ɡ/ (voiced velar; Bedouin origin). "
            "Northern 'qəltu' varieties (Mosul, Christian Baghdad): ق → /q/. "
            "k → /tʃ/ before front vowels in many speakers. "
            "Persian adstrate: /p/, /v/, /tʃ/, /ʒ/ established as phonemes; "
            "thousands of Persian loanwords. "
            "Turkish (Ottoman) loanwords also present. "
            "Blanc (1964) documents three communal dialects in Baghdad: "
            "Muslim (gilit), Jewish, and Christian (qəltu)."
        ),
    ),

    "ar-IQ-x-qeltu": LanguageSpec(
        code="ar-IQ-x-qeltu",
        name="Iraqi Arabic (Northern / qəltu)",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_IQ_QELTU,
        allophones=ALLOPHONES_IQ_QELTU,
        parent="ar-IQ",
        ancestors=(
            Ancestor("ar-IQ", P, 0.88, "Iraqi Arabic base"),
            Ancestor("ar-x-mashriqi", P, 0.85, "Eastern Arabic lineage"),
        ),
        notes=(
            "Northern Iraqi 'qəltu' Arabic — Mosul, Tikrit, Christian Baghdad, "
            "Jewish Baghdad (now largely diaspora). "
            "ق → /q/ PRESERVED (uvular; unlike southern gilit /ɡ/). "
            "ج → /dʒ/ (not modified). "
            "θ, ð, ðˤ preserved (same as gilit — conservative Iraqi feature). "
            "More archaic morphology than gilit; closer to Classical paradigms. "
            "Blanc (1964): Jewish Baghdad Arabic is a qəltu variety. "
            "Endangered: Mosul Arabic heavily disrupted by IS conflict (2014–17)."
        ),
    ),

    "ar-TD": LanguageSpec(
        code="ar-TD",
        name="Chadian Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_TD,
        allophones=ALLOPHONES_TD,
        parent="ar-x-maghrebi",
        ancestors=(
            Ancestor("ar-x-maghrebi", P, 0.75,
                     "Maghrebi/peripheral Arabic base"),
            Ancestor("arb", P, 0.78,
                     "Classical Arabic via trans-Saharan and Nilotic routes"),
        ),
        notes=(
            "Chadian Arabic (ʕarabī šuwā). Spoken in Chad, northern Cameroon, "
            "CAR, and northeastern Nigeria. "
            "Arrived via Sudan/Saharan trade routes (~11th–14th c. CE). "
            "CONSERVATIVE: θ (ث) and ð (ذ) often preserved. "
            "ق → /q/ maintained. ض → /dˤ/ (lateral lost). "
            "Sub-Saharan Chadic substrate (Hausa, Kanuri, Sara, Maba, Fulani): "
            "implosive allophones /ɓ, ɗ/; /ŋ/ phoneme; "
            "prenasalised stops [ᵐb, ⁿd] in some varieties. "
            "Moderate vowel reduction."
        ),
    ),

    "ar-NG": LanguageSpec(
        code="ar-NG",
        name="Nigerian Arabic (Shuwa)",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_NG,
        allophones=ALLOPHONES_NG,
        parent="ar-TD",
        ancestors=(
            Ancestor("ar-TD", P, 0.85,
                     "Closely related to Chadian Arabic"),
            Ancestor("arb", P, 0.75,
                     "Classical Arabic descent"),
        ),
        notes=(
            "Nigerian Shuwa Arabic. Spoken in Borno and Yobe states (NE Nigeria), "
            "Cameroon, Niger. Shuwa Arab ethnic group. "
            "More contact-modified than Chadian Arabic. "
            "θ → /t/, ð → /d/ (complete merger — Hausa influence). "
            "ق → /q/ educated speech; /ɡ/ vernacular. "
            "Hausa substrate: /ɓ, ɗ/ implosives; /ŋ/ phoneme. "
            "Possible incipient lexical tone in some varieties (Owens 1993 — debated). "
            "Owens (1993) *A Reference Grammar of Nigerian Arabic* is the primary source."
        ),
    ),

    "acy": LanguageSpec(
        code="acy",
        name="Cypriot Maronite Arabic",
        family="Semitic",
        script="Latin",
        graphemes=GRAPHEMES_ACY,
        allophones=ALLOPHONES_ACY,
        parent="arb",
        ancestors=(
            Ancestor("arb", P, 0.65,
                     "Classical/Levantine Arabic base (~8th–12th c. CE)"),
            Ancestor("el", AD, 0.30,
                     "Cypriot Greek adstrate — 800+ years of intense contact: "
                     "loss of pharyngeals ħ/ʕ; uvular q → k; "
                     "vowel system restructured toward Greek 5-vowel system; "
                     "/p/ and /v/ from Greek; gemination patterns; "
                     "massive Greek lexical borrowing"),
        ),
        notes=(
            "Cypriot Maronite Arabic (CMA) — ISO 639-3: acy. "
            "Locally called 'Sanna' (our language) or 'Arabiya'. "
            "Critically endangered (UNESCO): ~1,000–2,000 speakers (2020), mostly elderly. "
            "Maronite Christians migrated from Levant to Cyprus ~8th–12th c. CE. "
            "Isolated from Arabic for ~800 years; profound Greek influence. "
            "KEY CHANGES: "
            "(1) Pharyngeals ħ and ʕ LOST (→ h and ∅); "
            "(2) Uvular q → /k/ (Greek phonological space); "
            "(3) Emphatics WEAKENED (deemphasisation); "
            "(4) Vowel system restructured: 5-quality system (a e i o u) "
            "    replacing Classical 3-quality + length; "
            "(5) /p/ and /v/ from Greek (Arabic normally lacks these); "
            "(6) θ and ð MAINTAINED (Greek θ/δ reinforce Arabic originals). "
            "Revitalisation efforts ongoing by Cypriot government. "
            "Script: Latin (academic transcription); no standardised native script."
        ),
    ),
}
