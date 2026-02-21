"""Arabic — Egyptian, Sudanese, and Levantine dialects.

Covers the sedentary-origin Eastern Arabic dialects of the Nile Valley
and the Fertile Crescent (Levant / Bilād al-Shām).

Sources:
- Woidich, M. (2006). *Das Kairenisch-Arabische: Eine Grammatik*. Harrassowitz.
  [The definitive grammar of Cairo Arabic]
- Mitchell, T.F. (1990). *Pronouncing Arabic 1*. OUP.
- Blanc, H. (1964). *Communal Dialects in Baghdad*. Harvard UP.
- Cowell, M.W. (1964). *A Reference Grammar of Syrian Arabic*. Georgetown.
- Feghali, M.T. (1928). *Syntaxe des parlers arabes actuels du Liban*. Geuthner.
- Bauer, L. (1926). *Das palästinensische Arabisch*. Hinrichs.
- Cantineau, J. (1936). *Les parlers arabes du Ḥawrān*. Klincksieck.
- Abd-El-Jawad, H. (1987). "Cross-Dialectal Variation in Arabic." Language
  Variation and Change 3(4).
- Watson, J.C.E. (2002). *The Phonology and Morphology of Arabic*. OUP.
- Ingham, B. (1994). *Najdi Arabic*. John Benjamins.
- Miller, C. et al. (2007). *Arabic in the City*. Routledge.
- Versteegh, K. (2014). *The Arabic Language*. 2nd ed. Edinburgh UP.
- Holes, C. (2004). *Modern Arabic: Structures, Functions and Varieties*. Georgetown.
- Sawaie, M. (2007). *Fundamentals of Arabic Grammar*. Routledge.
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
# EGYPTIAN ARABIC (ar-EG)  — Cairene / Delta
# ═══════════════════════════════════════════════════════════════════════════
#
# Egyptian Arabic (ʕāmmiyyat maṣr) is the most widely understood spoken
# Arabic dialect worldwide, due to Egypt's dominance in film, TV, and music.
#
# PHONOLOGICAL PROFILE:
#
# THE DEFINING FEATURE: ج → /ɡ/
#   - Egyptian Arabic pronounces ج as a voiced velar stop [ɡ].
#   - This is unique among major Arabic varieties. It preserves the Proto-
#     Semitic/Proto-Arabic *g that became /dʒ/ elsewhere.
#   - Upper Egyptian (Saʿidi): also /ɡ/.
#   - Some educated/formal registers: /dʒ/ or /ʒ/ instead.
#
# ق → /ʔ/ (Cairo / Delta / Lower Egypt)
#   - Urban Cairene: ق → glottal stop [ʔ]
#   - Upper Egyptian (Saʿidi): ق → [ɡ] (same as ج elsewhere)
#   NOTE: Upper Egyptian ج → /dʒ/, ق → /ɡ/. Cairene: ج → /ɡ/, ق → /ʔ/.
#
# Interdentals:
#   - ث → [t] (fully merged with /t/)
#   - ذ → [d] (fully merged with /d/)
#   - ظ → [zˤ] (emphatic z, not ðˤ or dˤ)
#
# ض → [dˤ] (lateral quality fully lost)
#
# Vowels:
#   - Imāla (vowel raising): in some environments /aː/ → [eː] or [æː]
#   - New phonemes /e/ and /o/ from loanwords and vowel shifts
#   - Final short vowels maintained (unlike Maghrebi)
#   - Unstressed short vowels shortened but not deleted (unlike Maghrebi)

GRAPHEMES_EG = {
    **GRAPHEMES_MASHRIQI_BASE,
    "ث": ["t"],  # θ → t (complete merger; NO [θ] allophone)
    "ج": ["ɡ"],  # THE defining feature: g not dʒ
    "ذ": ["d"],  # ð → d (complete merger)
    "ظ": ["zˤ"],  # emphatic z (not ðˤ or dˤ)
    "ض": ["dˤ"],  # emphatic d (lateral lost)
    "ق": ["ʔ"],  # glottal stop (Cairo / urban / Delta)
    # New vowels from vowel changes and loanwords
    "e": ["e"],  # /e/ from imāla and loans
    "o": ["o"],  # /o/ from loans (Italian, French, English)
}

ALLOPHONES_EG = {
    **ALLOPHONES_MASHRIQI_BASE,
    # THE key allophone: ɡ is the primary phone for ج
    "ɡ": ["ɡ"],
    # ق → ʔ (Cairo urban); ɡ (Upper Egypt/Saʿidi)
    "q": ["ʔ", "q"],  # ʔ in Cairo; q in formal/recitation contexts
    "ʔ": ["ʔ"],
    # Interdentals — fully merged
    "θ": ["t"],  # no [θ] in Egyptian
    "ð": ["d"],
    "ðˤ": ["zˤ"],  # ظ: emphatic z
    "ɮˤ": ["dˤ"],  # ض: emphatic d
    # Nasals
    "n": ["n", "m", "ŋ"],
    # Emphatic /l/ in الله
    "l": ["l", "ɫ"],
    # Vowels — Egyptian system
    "a": ["a", "æ", "ɑ"],
    "aː": ["aː", "æː", "eː"],  # imāla: aː → eː near front consonants
    "i": ["i", "ɪ", "e"],
    "u": ["u", "ʊ", "o"],
    "iː": ["iː"],
    "uː": ["uː"],
    "e": ["e"],
    "o": ["o"],
}

# ═══════════════════════════════════════════════════════════════════════════
# UPPER EGYPTIAN / SAʿIDI ARABIC (ar-EG-x-said)
# ═══════════════════════════════════════════════════════════════════════════
#
# Upper Egypt (Ṣaʿīd maṣr) forms the southern part of Egypt.
# Saʿidi differs from Cairene in a crucial way:
#   - ج → /dʒ/ (affricate, like MSA; NOT the Cairene /ɡ/)
#   - ق → /ɡ/ (Saʿidi Bedouin/rural feature)
#
# This creates the interesting "complementary" relationship with Cairo:
#   Cairo:   ج → ɡ,   ق → ʔ
#   Saʿidi:  ج → dʒ,  ق → ɡ

GRAPHEMES_EG_SAID = {
    **GRAPHEMES_EG,
    "ج": ["dʒ"],  # affricate (not ɡ as in Cairo)
    "ق": ["ɡ"],  # voiced velar stop (not ʔ as in Cairo)
}

ALLOPHONES_EG_SAID = {
    **ALLOPHONES_EG,
    "dʒ": ["dʒ"],
    "q": ["ɡ", "q"],
    "ɡ": ["ɡ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SUDANESE ARABIC (ar-SD)
# ═══════════════════════════════════════════════════════════════════════════
#
# Sudanese Arabic is spoken in Sudan and parts of Chad. It is sometimes
# classified with Eastern Arabic but has distinct features from Egyptian.
# It arose from Arabic that came with 7th–8th century expansion south
# of Egypt, influenced by:
#   1. Nubian substrate (Nile Nubian languages: Nobiin, Nubiin)
#   2. Sub-Saharan African substrate (Dinka, Nuer, Nilotic languages)
#   3. Some Coptic/Egyptian Arabic contact to the north
#
# PHONOLOGICAL PROFILE:
#   - ج → /dʒ/ (preserved — NOT the Egyptian /ɡ/)
#   - ق → /q/ (preserved — NOT the Cairo /ʔ/)
#   - ث → /t/ (merged — not /θ/)
#   - ذ → /d/ (merged)
#   - ظ → /dˤ/ or /zˤ/ (varies)
#   - ض → /dˤ/ (lateral lost)
#   - Vowel reduction in unstressed syllables (partially, less than Maghrebi)
#   - Some sub-Saharan substrate features: tone-like features debated

GRAPHEMES_SD = {
    **GRAPHEMES_MASHRIQI_BASE,
    "ث": ["t"],
    "ذ": ["d"],
    "ظ": ["dˤ", "zˤ"],
    "ض": ["dˤ"],
    "ج": ["dʒ"],  # not ɡ (cf. Egyptian)
    "ق": ["q"],  # preserved (not ʔ)
}

ALLOPHONES_SD = {
    **ALLOPHONES_MASHRIQI_BASE,
    "ɮˤ": ["dˤ"],
    "θ": ["t"],
    "ð": ["d"],
    "ðˤ": ["dˤ", "zˤ"],
    "q": ["q"],
    "dʒ": ["dʒ"],
    "a": ["a", "ɑ"],
    "aː": ["aː", "ɑː"],
    "n": ["n", "m", "ŋ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# LEVANTINE ARABIC — GENERAL FEATURES
# ═══════════════════════════════════════════════════════════════════════════
#
# Levantine Arabic covers Syria, Lebanon, Palestine/Israel, and Jordan.
# All Levantine dialects share:
#   - ج → /ʒ/ (voiced postalveolar fricative — THE pan-Levantine feature)
#   - ث → /t/ (urban); preserved in some rural/Bedouin
#   - ذ → /d/ (urban); preserved in some rural
#   - ق → /ʔ/ (urban sedentary); /q/ (rural/Bedouin)
#   - ض → /dˤ/ or /ðˤ/ (varies; usually /dˤ/)
#   - ظ → /dˤ/ or /zˤ/ (varies)
#   - Short vowels maintained (not deleted as in Maghrebi)
#   - New /p/ and /v/ from loanwords (Turkish, French, English)
#
# Vowel system:
#   - /e/ and /o/ as distinct phonemes from vowel changes and loans
#   - Vowel shortening in some unstressed syllables

_GRAPHEMES_LEVANT_BASE = {
    **GRAPHEMES_MASHRIQI_BASE,
    "ث": ["t", "θ"],  # t urban; θ rural/conservative
    "ج": ["ʒ"],  # THE Levantine marker
    "ذ": ["d", "ð"],  # d urban; ð rural
    "ظ": ["dˤ", "zˤ"],
    "ض": ["dˤ"],
    "ق": ["ʔ", "q"],  # ʔ urban; q rural
}

_ALLOPHONES_LEVANT_BASE = {
    **ALLOPHONES_MASHRIQI_BASE,
    "ɮˤ": ["dˤ"],
    "θ": ["t", "θ"],
    "ð": ["d", "ð"],
    "ðˤ": ["dˤ", "zˤ"],
    "q": ["ʔ", "q"],
    "dʒ": ["ʒ"],  # ج → ʒ in Levantine
    "ʒ": ["ʒ"],
    "a": ["a", "æ", "ɛ"],
    "aː": ["aː", "eː", "æː"],
    "p": ["p"],
    "v": ["v"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SYRIAN ARABIC (ar-SY)  — Damascus / Standard Levantine
# ═══════════════════════════════════════════════════════════════════════════
#
# Damascus Arabic is usually taken as the prestige Levantine variety.
# Distinctive features vs. other Levantine:
#   - ق → /ʔ/ in Damascus city; /q/ in rural and eastern Syria
#   - /e/ and /o/ phonemic from vowel raising and loanwords
#   - Some Aramaic substrate vocabulary (but minimal phonological impact)

GRAPHEMES_SY = {
    **_GRAPHEMES_LEVANT_BASE,
    "ق": ["ʔ", "q"],
    "e": ["e"],
    "o": ["o"],
}

ALLOPHONES_SY = {
    **_ALLOPHONES_LEVANT_BASE,
    "q": ["ʔ", "q"],
    "e": ["e"],
    "o": ["o"],
}

# ═══════════════════════════════════════════════════════════════════════════
# LEBANESE ARABIC (ar-LB)
# ═══════════════════════════════════════════════════════════════════════════
#
# Lebanese Arabic has been heavily studied due to diaspora presence.
# Features that distinguish it from Syrian:
#   1. Pronounced French influence (including established /p/ and /v/)
#   2. Distinctive imāla: /a/ → [ɛ] near front consonants
#   3. Aramaic/Syriac substrate (somewhat stronger than Syrian)
#   4. Some speakers maintain /θ/ and /ð/ (educated or older)
#   5. Word-final vowels sometimes raised or fronted

GRAPHEMES_LB = {
    **_GRAPHEMES_LEVANT_BASE,
    "ق": ["ʔ", "q"],
    "e": ["e"],
    "o": ["o"],
}

ALLOPHONES_LB = {
    **_ALLOPHONES_LEVANT_BASE,
    "q": ["ʔ", "q"],
    "a": ["a", "æ", "ɛ"],  # fronting of /a/ is more prominent in Lebanese
    "aː": ["aː", "eː", "æː"],
    "e": ["e"],
    "o": ["o"],
    "p": ["p"],  # established phoneme from French
    "v": ["v"],  # established phoneme from French
}

# ═══════════════════════════════════════════════════════════════════════════
# PALESTINIAN ARABIC (ar-PS)  — Urban / Jerusalem
# ═══════════════════════════════════════════════════════════════════════════
#
# Palestinian Arabic varies from the coastal cities to the highlands.
# Urban (Jerusalem, Ramallah, Nablus):
#   - ق → /ʔ/
#   - ج → /ʒ/
#   - ث → /t/, ذ → /d/
#
# Rural / Bedouin:
#   - ق → /q/ or /k/
#   - ث → /θ/ preserved in many rural dialects
#   - Some unique vowel patterns from Canaanite shift
#
# Distinctive: Hebrew/Aramaic adstrate lexical influence (place names,
# some vocabulary), especially in villages.

GRAPHEMES_PS = {
    **_GRAPHEMES_LEVANT_BASE,
    "ق": ["ʔ", "q"],
    "ث": ["t", "θ"],  # t urban; θ rural / conservative
    "ذ": ["d", "ð"],
}

ALLOPHONES_PS = {
    **_ALLOPHONES_LEVANT_BASE,
    "q": ["ʔ", "q", "k"],  # ʔ urban; q/k rural/Bedouin
    "θ": ["t", "θ"],
    "ð": ["d", "ð"],
}

# ═══════════════════════════════════════════════════════════════════════════
# JORDANIAN ARABIC (ar-JO)
# ═══════════════════════════════════════════════════════════════════════════
#
# Jordan has a complex dialect landscape:
#   - Urban Amman: heavily influenced by Palestinian Arabic (refugee influx)
#     ق → /ʔ/, ج → /ʒ/, ث → /t/
#   - Saltī / Central Jordanian (traditional sedentary):
#     ق → /q/ preserved
#   - Eastern Jordanian / Bedouin:
#     ق → /ɡ/ (Bedouin feature)
#     ث → /θ/, ذ → /ð/ (more conservative)
#     ج → /dʒ/ or /ɡ/ (Bedouin)
#
# The Amman urban koiné is increasingly the prestige variety.

GRAPHEMES_JO = {
    **_GRAPHEMES_LEVANT_BASE,
    "ق": ["ʔ", "q", "ɡ"],  # ʔ Amman/urban; q Saltī; ɡ Bedouin/eastern
    "ث": ["t", "θ"],
    "ذ": ["d", "ð"],
    "ج": ["ʒ", "dʒ"],  # ʒ urban; dʒ rural/Bedouin
}

ALLOPHONES_JO = {
    **_ALLOPHONES_LEVANT_BASE,
    "q": ["ʔ", "q", "ɡ"],
    "θ": ["t", "θ"],
    "ð": ["d", "ð"],
    "dʒ": ["ʒ", "dʒ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SPECS
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "ar-EG": LanguageSpec(
        code="ar-EG",
        name="Egyptian Arabic (Cairene)",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_EG,
        allophones=ALLOPHONES_EG,
        parent="ar-x-mashriqi",
        ancestors=(
            Ancestor("ar-x-mashriqi", P, 0.90,
                     "Eastern Arabic base"),
            Ancestor("arb", P, 0.85,
                     "Classical Arabic descent via Nile Valley settlement"),
            Ancestor("cop", SUB, 0.07,
                     "Coptic substrate: some lexical items, vowel patterns; "
                     "Coptic extinct by ~17th c. as spoken language"),
        ),
        notes=(
            "Cairene / Lower Egyptian Arabic (ʕāmmiyyat maṣr). "
            "Most widely understood colloquial Arabic globally due to media. "
            "DEFINING FEATURE: ج → /ɡ/ (preserving Proto-Semitic *g). "
            "ق → /ʔ/ in Cairo/urban; ق → /ɡ/ in Upper Egypt (Saʿidi). "
            "ث → /t/, ذ → /d/ (complete merger). "
            "ظ → /zˤ/ (not /dˤ/). "
            "ض → /dˤ/ (lateral quality fully lost). "
            "Coptic substrate: minimal phonological impact, some vocabulary. "
            "Vowels: imāla of /aː/ → [eː] near front consonants; "
            "/e/ and /o/ phonemic in educated/urban speech."
        ),
    ),

    "ar-EG-x-said": LanguageSpec(
        code="ar-EG-x-said",
        name="Egyptian Arabic (Saʿidi / Upper Egypt)",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_EG_SAID,
        allophones=ALLOPHONES_EG_SAID,
        parent="ar-EG",
        ancestors=(
            Ancestor("ar-EG", P, 0.85, "Shares Egyptian Arabic base"),
            Ancestor("arb", P, 0.80, "Classical Arabic descent"),
        ),
        notes=(
            "Saʿidi (Upper Egyptian) Arabic. "
            "COMPLEMENTARY TO CAIRO: ج → /dʒ/ (not /ɡ/), ق → /ɡ/ (not /ʔ/). "
            "More conservative in some phonological features than Cairene. "
            "Nubian substrate influence in southernmost varieties."
        ),
    ),

    "ar-SD": LanguageSpec(
        code="ar-SD",
        name="Sudanese Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_SD,
        allophones=ALLOPHONES_SD,
        parent="ar-x-mashriqi",
        ancestors=(
            Ancestor("ar-x-mashriqi", P, 0.88,
                     "Eastern Arabic descent"),
            Ancestor("arb", P, 0.85,
                     "Classical Arabic via 7th–8th c. expansion"),
        ),
        notes=(
            "Sudanese Arabic (ʕarabī masārī). "
            "ج → /dʒ/ (preserved — not the Egyptian /ɡ/). "
            "ق → /q/ (preserved — not the Cairene /ʔ/). "
            "ث → /t/, ذ → /d/ (merged). "
            "Vowel reduction partial (less extreme than Maghrebi). "
            "Sub-Saharan African substrate: minimal phonological impact but "
            "tonal features debated in some southern varieties. "
            "Contact with Nubian languages to the south."
        ),
    ),

    "ar-SY": LanguageSpec(
        code="ar-SY",
        name="Syrian Arabic (Damascene)",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_SY,
        allophones=ALLOPHONES_SY,
        parent="ar-x-mashriqi",
        ancestors=(
            Ancestor("ar-x-mashriqi", P, 0.88,
                     "Eastern Arabic base"),
            Ancestor("arb", P, 0.85,
                     "Classical Arabic descent"),
        ),
        notes=(
            "Damascus Arabic (ʕarabī šāmi). Prestige Levantine variety. "
            "ج → /ʒ/ (THE pan-Levantine feature). "
            "ق → /ʔ/ in Damascus city; /q/ in rural/eastern Syria. "
            "ث → /t/ (urban); ذ → /d/ (urban). "
            "Vowels: /e/ and /o/ phonemic; some imāla of /aː/ → [eː]. "
            "Aramaic substrate: mainly lexical (minimal phonological impact)."
        ),
    ),

    "ar-LB": LanguageSpec(
        code="ar-LB",
        name="Lebanese Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_LB,
        allophones=ALLOPHONES_LB,
        parent="ar-x-mashriqi",
        ancestors=(
            Ancestor("ar-x-mashriqi", P, 0.85,
                     "Eastern Arabic base"),
            Ancestor("arb", P, 0.83,
                     "Classical Arabic descent"),
            Ancestor("fr-FR", AD, 0.05,
                     "French adstrate: established /p/ and /v/ phonemes, "
                     "heavy loanword influence"),
        ),
        notes=(
            "Lebanese Arabic (ʕarabī libnānī). "
            "ج → /ʒ/ (Levantine). ق → /ʔ/ (most speakers). "
            "ث → /t/, ذ → /d/ (urban); some educated speakers maintain θ, ð. "
            "DISTINCTIVE: more fronting of /a/ → [ɛ] than Syrian. "
            "French adstrate: /p/ and /v/ well-established phonemes. "
            "Aramaic/Syriac substrate: some vocabulary, minimal phonological impact."
        ),
    ),

    "ar-PS": LanguageSpec(
        code="ar-PS",
        name="Palestinian Arabic (Urban)",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_PS,
        allophones=ALLOPHONES_PS,
        parent="ar-x-mashriqi",
        ancestors=(
            Ancestor("ar-x-mashriqi", P, 0.87,
                     "Eastern Arabic base"),
            Ancestor("arb", P, 0.85,
                     "Classical Arabic descent"),
        ),
        notes=(
            "Palestinian Arabic (ʕarabī filasṭīnī) — urban variety "
            "(Jerusalem, Ramallah, Nablus, Haifa). "
            "ج → /ʒ/ (Levantine). ق → /ʔ/ (urban). "
            "ث → /t/ (urban), ث → /θ/ (rural/conservative). "
            "Bedouin / rural varieties are more conservative: "
            "θ, ð preserved; q → /q/ or /k/. "
            "Hebrew adstrate: place names, recent loanwords (minimal phonology). "
            "Aramaic substrate: minimal phonological impact."
        ),
    ),

    "ar-JO": LanguageSpec(
        code="ar-JO",
        name="Jordanian Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_JO,
        allophones=ALLOPHONES_JO,
        parent="ar-x-mashriqi",
        ancestors=(
            Ancestor("ar-x-mashriqi", P, 0.87,
                     "Eastern Arabic base"),
            Ancestor("arb", P, 0.85,
                     "Classical Arabic descent"),
        ),
        notes=(
            "Jordanian Arabic — complex dialect landscape. "
            "Urban Amman (influenced by Palestinian): ج → /ʒ/, ق → /ʔ/. "
            "Traditional Saltī / Central Jordanian: ق → /q/ preserved. "
            "Eastern / Bedouin: ق → /ɡ/, ث → /θ/ preserved, ج → /dʒ/. "
            "The urban Amman koiné is increasingly dominant due to "
            "Palestinian refugee influx and rural-urban migration."
        ),
    ),
}
