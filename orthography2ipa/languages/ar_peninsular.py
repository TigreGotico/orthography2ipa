"""Arabic — Peninsular dialects (Hejazi, Najdi, Gulf, Omani, Yemeni).

Covers the Arabic varieties of the Arabian Peninsula — the homeland of
Arabic and the region closest to the language's geographic origin.

Genealogy:
  Classical Arabic (arb)
       ↓
  Proto-Peninsular Arabic (ar-x-peninsular)
       ↓
  ┌───────────┬────────────┬──────────────┬──────────┬──────────┐
  ar-SA-x-hejaz  ar-SA-x-najd  ar-x-gulf  ar-OM    ar-YE

The Gulf varieties are further divided:
  ar-x-gulf
       ↓
  ┌──────────┬──────────┬──────────┬──────────┐
  ar-KW     ar-BH     ar-QA     ar-AE

Regional typology — the Peninsula preserves features lost elsewhere:
  - Interdentals /θ ð ðˤ/ often retained (especially Najdi, Gulf, Bedouin)
  - ق → /q/ or /ɡ/ (Bedouin), not glottal /ʔ/ as in Levantine/Egyptian urban
  - ج varies: /dʒ/ (Hejazi, Gulf), /ɡ/ (some Gulf/Najdi), /ʒ/ (some coastal)
  - k → /tʃ/ before front vowels in Gulf (major distinctive feature)
  - g → /j/ in some Yemeni environments
  - Vowel imāla (raising of /aː/ → /eː/) prominent in several varieties

Sources:
- Ingham, B. (1994). *Najdi Arabic*. John Benjamins.
- Prochazka, T. (1988). *Saudi Arabian Dialects*. Kegan Paul International.
- Al-Tajir, M.A. (1982). *Bahrain and the Gulf*. St Martin's Press.
  [Gulf Arabic documentation]
- Holes, C. (1990). *Gulf Arabic*. Routledge. [THE reference grammar]
- Holes, C. (2001). *Dialect, Culture and Society in Eastern Arabia*.
  Vol. 1: Glossary. Brill.
- Johnstone, T.M. (1967). *Eastern Arabian Dialect Studies*. OUP.
- Watson, J.C.E. (1993). *A Syntax of Ṣanʿānī Arabic*. Harrassowitz.
  [North Yemeni Arabic]
- Watson, J.C.E. (2002). *The Phonology and Morphology of Arabic*. OUP.
- Behnstedt, P. (1985). *Die Dialekte der Gegend von Ṣaʿda*. Harrassowitz.
- Naïm, S. (2009). "Yemeni Arabic." In: *Encyclopedia of Arabic Language
  and Linguistics*. Brill.
- Owens, J. (1984). *A Short Reference Grammar of Eastern Libyan Arabic*.
  Harrassowitz. [Comparison]
- Al-Wer, E. (2007). "The formation of the dialect of Amman." In:
  *Arabic in the City*. Routledge.
- Versteegh, K. (2014). *The Arabic Language*. 2nd ed. Edinburgh UP.
"""

from orthography2ipa.languages.ar_classical import (
    GRAPHEMES_PENINSULAR_BASE, ALLOPHONES_PENINSULAR_BASE,
)
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
AD = AncestorRole.ADSTRATE
SUP = AncestorRole.SUPERSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# HEJAZI ARABIC (ar-SA-x-hejaz)  — Mecca, Medina, Jeddah
# ═══════════════════════════════════════════════════════════════════════════
#
# The Hejaz (حجاز) is the western coastal strip of Saudi Arabia — the historic
# birthplace of Islam (Mecca and Medina) and long the most cosmopolitan region
# of the Peninsula due to the hajj pilgrimage drawing Arabic speakers from
# across the Islamic world.
#
# PHONOLOGICAL PROFILE — URBAN HEJAZI:
#   - ج → /dʒ/ (standard; no /ɡ/ as in Egyptian)
#   - ق → /ʔ/ in urban Jeddah/Mecca (massive non-Bedouin influence)
#         /q/ in Medina / more conservative speakers
#   - ث, ذ, ظ: MERGED in urban speech (→ /t, d, dˤ/)
#     PRESERVED in rural / tribal Hejazi Bedouin speech
#   - k → /tʃ/ before front vowels ABSENT (Hejazi urban lacks Gulf /k → tʃ/)
#   - Vowel imāla: moderate
#   - Short vowels maintained (not deleted)
#   - Heavy foreign community influence (Egyptian, Levantine, South Asian)
#     from pilgrimage; Hejazi often understood by speakers of other dialects
#
# PHONOLOGICAL PROFILE — RURAL/BEDOUIN HEJAZI:
#   - θ, ð, ðˤ preserved
#   - q → /q/ preserved or → /ɡ/ (Bedouin)
#   - More conservative overall

GRAPHEMES_HEJAZ = {
    **GRAPHEMES_PENINSULAR_BASE,
    # Urban Hejazi — sedentary features
    "ث": ["t", "θ"],  # t urban; θ rural/Bedouin
    "ذ": ["d", "ð"],  # d urban; ð rural
    "ظ": ["dˤ", "ðˤ"],
    "ض": ["dˤ"],
    "ج": ["dʒ"],  # preserved affricate (not ɡ or ʒ)
    "ق": ["ʔ", "q"],  # ʔ urban Jeddah; q Medina/rural
}

ALLOPHONES_HEJAZ = {
    **ALLOPHONES_PENINSULAR_BASE,
    "ɮˤ": ["dˤ"],
    "θ": ["t", "θ"],
    "ð": ["d", "ð"],
    "ðˤ": ["dˤ", "ðˤ"],
    "q": ["ʔ", "q"],
    "dʒ": ["dʒ"],
    # No k → tʃ shift (unlike Gulf)
    "k": ["k"],
    # Vowel system — imāla present but moderate
    "a": ["a", "æ", "ɑ"],
    "aː": ["aː", "æː", "eː"],  # mild imāla
    "i": ["i"],
    "u": ["u"],
    "iː": ["iː"],
    "uː": ["uː"],
    "n": ["n", "m", "ŋ"],
    "l": ["l", "ɫ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# NAJDI ARABIC (ar-SA-x-najd)  — Central Arabia / Riyadh
# ═══════════════════════════════════════════════════════════════════════════
#
# Najdi Arabic (النجدية) is spoken in central Saudi Arabia. It is often
# considered one of the most conservative mainland dialects:
#
# PHONOLOGICAL PROFILE:
#   - ث /θ/, ذ /ð/, ظ /ðˤ/ ALL PRESERVED (major conservative feature)
#     Only strongly urban speech shows merger to /t, d, dˤ/
#   - ق → /ɡ/ (Najdi Bedouin — the traditional rural Najdi reflex)
#     → /q/ (urban Riyadh, conservative/educated)
#   - ج → /dʒ/ (city Riyadh) or /ɡ/ (some Bedouin areas)
#   - k → no /tʃ/ shift (unlike Gulf coastal)
#   - ض → /dˤ/ (lateral fully lost)
#   - Short vowels generally maintained
#   - Distinctive vowel: /o/ from imāla of /u/ in some contexts (short u → o)
#   - Najdi has kept some archaic morphophonological patterns

GRAPHEMES_NAJD = {
    **GRAPHEMES_PENINSULAR_BASE,
    # θ, ð, ðˤ PRESERVED in Najdi
    "ث": ["θ", "t"],  # θ standard; t only in urban Riyadh casual speech
    "ذ": ["ð", "d"],
    "ظ": ["ðˤ", "dˤ"],
    "ض": ["dˤ"],
    "ج": ["dʒ", "ɡ"],  # dʒ city; ɡ Bedouin areas
    "ق": ["ɡ", "q"],  # ɡ traditional Najdi; q urban/formal
}

ALLOPHONES_NAJD = {
    **ALLOPHONES_PENINSULAR_BASE,
    "ɮˤ": ["dˤ"],
    "θ": ["θ", "t"],  # PRESERVED as primary phone
    "ð": ["ð", "d"],
    "ðˤ": ["ðˤ", "dˤ"],
    "q": ["ɡ", "q"],  # ɡ primary in traditional Najdi
    "dʒ": ["dʒ", "ɡ"],
    # No k → tʃ in Najdi
    "k": ["k"],
    "a": ["a", "ɑ"],
    "aː": ["aː", "ɑː", "oː"],  # some imāla toward /oː/
    "u": ["u", "o"],
    "n": ["n", "m", "ŋ"],
    "l": ["l", "ɫ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-GULF ARABIC (ar-x-gulf)  — Eastern Arabia
# ═══════════════════════════════════════════════════════════════════════════
#
# Gulf Arabic is spoken along the western shore of the Persian/Arabian Gulf
# — Kuwait, Bahrain, Qatar, UAE, and the Eastern Province of Saudi Arabia.
# All Gulf varieties share a set of highly distinctive features:
#
# SHARED GULF FEATURES:
#   1. k → /tʃ/ BEFORE FRONT VOWELS (/i, iː, e/)
#      This is THE most salient Gulf phonological feature:
#      classical /k/ → Gulf /tʃ/ before front vowels
#      e.g. Arabic kitāb → Gulf /tʃitāb/ "book"
#   2. g → /j/ in some environments (variable; mostly older/rural speech)
#   3. ق → /ɡ/ (common Gulf reflex; maintained from Bedouin pattern)
#   4. ث, ذ, ظ: PRESERVED in much of Gulf Arabic (conservative)
#   5. ج → /dʒ/ (mostly preserved; some /j/ in Bedouin speech)
#   6. Vowel imāla: prominent (aː → eː before/after front consonants)
#   7. Short vowels maintained
#   8. New phonemes from English/Indian contact: /p/, /v/, /tʃ/ (established)
#   9. Persian adstrate: some /p/ words predating English

GRAPHEMES_GULF_BASE = {
    **GRAPHEMES_PENINSULAR_BASE,
    # THE Gulf feature: k → tʃ before front vowels
    "ك": ["k", "tʃ"],  # k default; tʃ before /i, iː, e/
    # Conservative: θ, ð often preserved
    "ث": ["θ", "t"],
    "ذ": ["ð", "d"],
    "ظ": ["ðˤ", "dˤ"],
    "ض": ["dˤ"],
    # ق → ɡ (Bedouin/traditional Gulf)
    "ق": ["ɡ", "q"],
    "ج": ["dʒ", "j"],  # dʒ standard; j in some speech
    # European/Persian loanword phonemes
    "پ": ["p"],
    "ڤ": ["v"],
}

ALLOPHONES_GULF_BASE = {
    **ALLOPHONES_PENINSULAR_BASE,
    "ɮˤ": ["dˤ"],
    # k → tʃ is allophonic before front vowels (same phoneme, different surface)
    "k": ["k", "tʃ"],  # tʃ before /i, e/
    "θ": ["θ", "t"],
    "ð": ["ð", "d"],
    "ðˤ": ["ðˤ", "dˤ"],
    "q": ["ɡ", "q"],  # ɡ traditional; q formal/MSA register
    "dʒ": ["dʒ", "j"],
    # Vowel imāla
    "aː": ["aː", "eː", "æː"],
    "a": ["a", "æ"],
    "p": ["p"],
    "v": ["v"],
    "n": ["n", "m", "ŋ"],
    "l": ["l", "ɫ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# KUWAITI ARABIC (ar-KW)
# ═══════════════════════════════════════════════════════════════════════════
#
# Kuwaiti Arabic shares all core Gulf features. Distinctive aspects:
#   - Among the most well-documented Gulf varieties
#   - English influence very prominent (strong /p/ and /v/ from massive
#     anglophone contact since oil era)
#   - ث, ذ preserved by conservative/older speakers; merged by younger urban
#   - Bedouin/rural Kuwaiti: θ, ð, q → ɡ preserved more consistently
#   - /tʃ/ from k-before-front-vowel is very consistent and salient

GRAPHEMES_KW = {**GRAPHEMES_GULF_BASE}

ALLOPHONES_KW = {
    **ALLOPHONES_GULF_BASE,
    # English very dominant → /p/ and /v/ very well established
    "p": ["p"],
    "v": ["v"],
    # ŋ appears in English loanwords (parking, king etc.)
    "ŋ": ["ŋ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# BAHRAINI ARABIC (ar-BH)
# ═══════════════════════════════════════════════════════════════════════════
#
# Bahrain has a unique sociolinguistic situation: a large Shia Arab population
# (Baharna) historically with Persian ties, and a Sunni Arab minority.
#
# PHONOLOGICAL SPLIT:
#   - Sunni Bahraini (Baḥrīnī): typical Gulf features, k → tʃ, ق → ɡ
#   - Shia Bahraini (Bahārna): more conservative in some areas;
#     Persian influence on vocabulary
#   - Persian (Farsi) adstrate: some /p/ in older vocabulary predating English
#
# Distinctive Bahraini feature:
#   - Some varieties retain /tʃ/ as a "heavier" variant vs. Kuwaiti

GRAPHEMES_BH = {
    **GRAPHEMES_GULF_BASE,
    # Shia (Baharna) sometimes more conservative re: interdentals
    "ث": ["θ", "t"],
    "ذ": ["ð", "d"],
}

ALLOPHONES_BH = {
    **ALLOPHONES_GULF_BASE,
    "θ": ["θ", "t"],
    "ð": ["ð", "d"],
    # Persian adstrate: /p/ pre-dates English contact
    "p": ["p"],
    "v": ["v"],
}

# ═══════════════════════════════════════════════════════════════════════════
# QATARI ARABIC (ar-QA)
# ═══════════════════════════════════════════════════════════════════════════
#
# Qatar is largely tribal and Bedouin in origin; Qatari Arabic preserves
# some conservative features alongside typical Gulf traits.
#
# Features similar to Kuwaiti/Bahraini with slight Bedouin character:
#   - ث, ذ, ظ preserved by older/Bedouin speakers
#   - k → tʃ before front vowels (Gulf feature fully present)
#   - ق → ɡ (typical Gulf/Bedouin)
#   - Vowel imāla prominent

GRAPHEMES_QA = {**GRAPHEMES_GULF_BASE}

ALLOPHONES_QA = {
    **ALLOPHONES_GULF_BASE,
    # Somewhat more Bedouin character: θ, ð a bit more preserved
    "θ": ["θ", "t"],
    "ð": ["ð", "d"],
    "p": ["p"],
    "v": ["v"],
}

# ═══════════════════════════════════════════════════════════════════════════
# EMIRATI ARABIC (ar-AE)  — UAE
# ═══════════════════════════════════════════════════════════════════════════
#
# Emirati Arabic spans a large archipelago of tribal varieties:
#   - Abu Dhabi / Dubai: urban koiné, heavy English and South Asian contact
#   - Sharjah / Ras Al-Khaimah: more conservative tribal varieties
#
# The UAE has the most multilingual context of the Gulf states
# (large Indian, Pakistani, Filipino, Western expat communities).
#
# Distinctive UAE features:
#   - Very heavy English influence: /p/, /v/ thoroughly established
#   - Some speakers: ɡ → /j/ (older/rural feature)
#   - k → tʃ before front vowels: robust
#   - ق → ɡ (typical Gulf)
#   - More English loanwords than other Gulf dialects (Dubai effect)

GRAPHEMES_AE = {
    **GRAPHEMES_GULF_BASE,
    "ق": ["ɡ", "q"],
    # English loanword phonemes very established
    "پ": ["p"],
    "ڤ": ["v"],
}

ALLOPHONES_AE = {
    **ALLOPHONES_GULF_BASE,
    "q": ["ɡ", "q"],
    "p": ["p"],
    "v": ["v"],
    # English-influenced: /tʃ/ in many more environments (not just k-front)
    "tʃ": ["tʃ"],
    # ɡ → j in some older rural speech
    "ɡ": ["ɡ", "j"],
    "ŋ": ["ŋ"],  # from English loans
}

# ═══════════════════════════════════════════════════════════════════════════
# OMANI ARABIC (ar-OM)
# ═══════════════════════════════════════════════════════════════════════════
#
# Omani Arabic is geographically isolated on the southeastern corner of the
# Peninsula and has developed several unique features:
#
# PHONOLOGICAL PROFILE:
#   - ج → /dʒ/ (consistently; not /ɡ/ or /ʒ/)
#   - ق → /q/ PRESERVED in many Omani varieties (conservative)
#     → /ɡ/ in some interior Bedouin areas
#   - ث, ذ, ظ: often PRESERVED (conservative)
#   - k → /tʃ/ before front vowels (Gulf feature, present in Omani)
#   - UNIQUE: some Omani dialects preserve /dˤ/ as distinct from /ðˤ/
#     (distinction lost in most dialects)
#   - Very strong pharyngeals ħ, ʕ
#   - South Arabian (Modern South Arabian) adstrate in Dhofar/Salalah area:
#     some non-Arabic substrate features (Mehri, Jibbali)
#   - Swahili adstrate from historic Omani maritime trade and Zanzibar sultanate
#   - Persian adstrate from Hormuz Strait trade

GRAPHEMES_OM = {
    **GRAPHEMES_PENINSULAR_BASE,
    # Conservative: θ, ð, ðˤ often preserved
    "ث": ["θ", "t"],
    "ذ": ["ð", "d"],
    "ظ": ["ðˤ", "dˤ"],
    "ض": ["dˤ"],
    "ج": ["dʒ"],  # consistently affricate (not ɡ)
    "ق": ["q", "ɡ"],  # q preserved majority; ɡ Bedouin/interior
    # Gulf k → tʃ present
    "ك": ["k", "tʃ"],
}

ALLOPHONES_OM = {
    **ALLOPHONES_PENINSULAR_BASE,
    "ɮˤ": ["dˤ"],
    "θ": ["θ", "t"],
    "ð": ["ð", "d"],
    "ðˤ": ["ðˤ", "dˤ"],
    "q": ["q", "ɡ"],
    "dʒ": ["dʒ"],
    "k": ["k", "tʃ"],
    # Distinctive: dˤ and ðˤ sometimes maintained as separate phones
    "dˤ": ["dˤ"],
    "a": ["a", "æ", "ɑ"],
    "aː": ["aː", "eː"],
    "n": ["n", "m", "ŋ"],
    "l": ["l", "ɫ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# YEMENI ARABIC (ar-YE)  — North Yemeni / Ṣanʿānī as reference
# ═══════════════════════════════════════════════════════════════════════════
#
# Yemen has extreme internal dialect diversity. The main varieties are:
#   - Ṣanʿānī (Sanaa): the reference variety for North Yemen
#   - Aden/Taʿizz: South Yemeni, coastal, more conservative in some ways
#   - Tihama coastal: contact with East African Arabic
#   - Hadhrami Arabic: very conservative, spoken by major diaspora
#
# Ṣanʿānī (North Yemeni) PHONOLOGICAL PROFILE (Watson 1993):
#   - ج → /ɡ/ in Ṣanʿānī (like Egyptian)
#     This is one of few non-Egyptian varieties with ج → /ɡ/
#   - ق → /q/ PRESERVED (not ʔ or ɡ)
#   - ث /θ/, ذ /ð/ PRESERVED (very conservative)
#   - ظ → /ðˤ/ PRESERVED
#   - ض → /ðˤ/ (merged with ظ in Ṣanʿānī — unique feature!)
#     In most other dialects ض ≠ ظ; in Ṣanʿānī they merge to /ðˤ/
#   - k → NO /tʃ/ (unlike Gulf)
#   - Vowel imāla: prominent in some environments
#   - Short vowels maintained
#
# HADHRAMI ARABIC (Ḥaḍramī — ar-YE-x-hadrami) noted in variants:
#   Very conservative; historically important diaspora (Indonesia, E. Africa)
#   Features: θ, ð, ðˤ all preserved; q preserved; strong pharyngeals

GRAPHEMES_YE = {
    **GRAPHEMES_PENINSULAR_BASE,
    # Ṣanʿānī features
    "ج": ["ɡ", "dʒ"],  # ɡ in Ṣanʿānī (like Egyptian); dʒ South Yemen
    "ق": ["q"],  # PRESERVED (conservative)
    "ث": ["θ"],  # PRESERVED (very conservative)
    "ذ": ["ð"],  # PRESERVED
    "ظ": ["ðˤ"],  # PRESERVED
    # UNIQUE: ض merges with ظ in Ṣanʿānī
    "ض": ["ðˤ", "dˤ"],  # ðˤ Ṣanʿānī; dˤ South/coastal Yemen
    # No k → tʃ shift
    "ك": ["k"],
}

ALLOPHONES_YE = {
    **ALLOPHONES_PENINSULAR_BASE,
    # ɮˤ → ðˤ (unique Ṣanʿānī merger of ض with ظ)
    "ɮˤ": ["ðˤ", "dˤ"],
    "θ": ["θ"],  # very consistently preserved
    "ð": ["ð"],
    "ðˤ": ["ðˤ"],  # both ض and ظ → ðˤ in Ṣanʿānī
    "q": ["q"],
    "dʒ": ["ɡ", "dʒ"],  # ɡ Ṣanʿānī; dʒ South/coastal
    "k": ["k"],  # no tʃ in Yemeni
    "a": ["a", "æ"],
    "aː": ["aː", "eː"],  # imāla present
    "n": ["n", "m", "ŋ"],
    "l": ["l", "ɫ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SPECS
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "ar-SA-x-hejaz": LanguageSpec(
        code="ar-SA-x-hejaz",
        name="Hejazi Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_HEJAZ,
        allophones=ALLOPHONES_HEJAZ,
        parent="ar-x-peninsular",
        ancestors=(
            Ancestor("ar-x-peninsular", P, 0.90,
                     "Peninsular Arabic base"),
        ),
        notes=(
            "Hejazi Arabic (حجازي). Western Saudi Arabia: Mecca, Medina, Jeddah. "
            "Urban Hejazi: ج → /dʒ/; ق → /ʔ/ (Jeddah) or /q/ (Medina). "
            "ث → /t/, ذ → /d/ (urban); preserved in Bedouin/rural. "
            "No k → /tʃ/ shift (unlike Gulf). "
            "Cosmopolitan due to Hajj pilgrimage: heavy influence from Egyptian, "
            "Levantine, South Asian Arabic speakers. "
            "Often considered most internationally intelligible Peninsula dialect."
        ),
    ),

    "ar-SA-x-najd": LanguageSpec(
        code="ar-SA-x-najd",
        name="Najdi Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_NAJD,
        allophones=ALLOPHONES_NAJD,
        parent="ar-x-peninsular",
        ancestors=(
            Ancestor("ar-x-peninsular", P, 0.92,
                     "Peninsular Arabic base — most conservative"),
        ),
        notes=(
            "Najdi Arabic (نجدي). Central Arabia, including Riyadh. "
            "VERY CONSERVATIVE: ث /θ/, ذ /ð/, ظ /ðˤ/ ALL PRESERVED "
            "(only strong urban speech merges them). "
            "ق → /ɡ/ (traditional Najdi Bedouin) or /q/ (Riyadh urban/formal). "
            "ج → /dʒ/ (city) or /ɡ/ (Bedouin). "
            "No k → /tʃ/ shift (unlike coastal Gulf). "
            "Ingham (1994) is the primary linguistic reference. "
            "Prestige within Saudi Arabia."
        ),
    ),

    "ar-x-gulf": LanguageSpec(
        code="ar-x-gulf",
        name="Proto-Gulf Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_GULF_BASE,
        allophones=ALLOPHONES_GULF_BASE,
        parent="ar-x-peninsular",
        ancestors=(
            Ancestor("ar-x-peninsular", P, 0.90,
                     "Peninsular Arabic base"),
        ),
        notes=(
            "Proto-Gulf Arabic — abstract ancestor node for Kuwaiti, "
            "Bahraini, Qatari, and Emirati Arabic. "
            "DEFINING FEATURE: k → /tʃ/ before front vowels (/i, iː, e/). "
            "ق → /ɡ/ (Bedouin/traditional Gulf). "
            "θ, ð often preserved. Vowel imāla prominent. "
            "Holes (1990) is the primary reference grammar."
        ),
    ),

    "ar-KW": LanguageSpec(
        code="ar-KW",
        name="Kuwaiti Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_KW,
        allophones=ALLOPHONES_KW,
        parent="ar-x-gulf",
        ancestors=(
            Ancestor("ar-x-gulf", P, 0.92,
                     "Gulf Arabic base"),
        ),
        notes=(
            "Kuwaiti Arabic. Best-documented Gulf variety. "
            "k → /tʃ/ before front vowels: very salient and consistent. "
            "ق → /ɡ/ (traditional); /q/ in formal/MSA contexts. "
            "Heavy English influence (post-1950s oil era): "
            "/p/, /v/, /ŋ/ well-established from English loanwords. "
            "Holes (1990, 2001) primary reference."
        ),
    ),

    "ar-BH": LanguageSpec(
        code="ar-BH",
        name="Bahraini Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_BH,
        allophones=ALLOPHONES_BH,
        parent="ar-x-gulf",
        ancestors=(
            Ancestor("ar-x-gulf", P, 0.90,
                     "Gulf Arabic base"),
            Ancestor("fa", AD, 0.05,
                     "Persian adstrate: Shia community historical ties; "
                     "/p/ in some older loanwords predating English"),
        ),
        notes=(
            "Bahraini Arabic. Sunni (Baḥrīnī) and Shia (Bahārna) varieties. "
            "Sunni: typical Gulf features, k → /tʃ/, ق → /ɡ/. "
            "Shia (Bahārna): slightly more conservative, some Persian "
            "adstrate influence. "
            "Persian /p/ in some vocabulary predates English contact. "
            "Johnstone (1967) primary reference for Eastern Arabian varieties."
        ),
    ),

    "ar-QA": LanguageSpec(
        code="ar-QA",
        name="Qatari Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_QA,
        allophones=ALLOPHONES_QA,
        parent="ar-x-gulf",
        ancestors=(
            Ancestor("ar-x-gulf", P, 0.91,
                     "Gulf Arabic base"),
        ),
        notes=(
            "Qatari Arabic. Tribal/Bedouin character somewhat stronger than "
            "Kuwaiti. k → /tʃ/ before front vowels (Gulf feature). "
            "ث, ذ preserved more consistently by older/conservative speakers. "
            "ق → /ɡ/ (Bedouin/traditional). Vowel imāla prominent."
        ),
    ),

    "ar-AE": LanguageSpec(
        code="ar-AE",
        name="Emirati Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_AE,
        allophones=ALLOPHONES_AE,
        parent="ar-x-gulf",
        ancestors=(
            Ancestor("ar-x-gulf", P, 0.88,
                     "Gulf Arabic base"),
        ),
        notes=(
            "Emirati Arabic (إماراتي). UAE: Abu Dhabi, Dubai, Sharjah, RAK. "
            "k → /tʃ/ before front vowels (robust Gulf feature). "
            "ق → /ɡ/ (traditional). "
            "Heaviest English influence of all Gulf dialects (Dubai effect): "
            "/p/, /v/, /tʃ/, /ŋ/ thoroughly integrated. "
            "South Asian (Indian/Pakistani) community influence on lexicon. "
            "Interior/tribal varieties (RAK, Fujairah) more conservative."
        ),
    ),

    "ar-OM": LanguageSpec(
        code="ar-OM",
        name="Omani Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_OM,
        allophones=ALLOPHONES_OM,
        parent="ar-x-peninsular",
        ancestors=(
            Ancestor("ar-x-peninsular", P, 0.88,
                     "Peninsular Arabic base"),
            Ancestor("fa", AD, 0.05,
                     "Persian adstrate from Hormuz Strait trade and Muscat contacts"),
        ),
        notes=(
            "Omani Arabic. Conservative Peninsula variety on southeastern coast. "
            "ج → /dʒ/ consistently (not /ɡ/ as in Yemeni). "
            "ق → /q/ preserved in many varieties; /ɡ/ Bedouin/interior. "
            "θ, ð, ðˤ often preserved (conservative). "
            "k → /tʃ/ before front vowels (Gulf feature present). "
            "UNIQUE: some dialects preserve dˤ vs ðˤ distinction (rare). "
            "South Arabian (Mehri/Jibbali) adstrate in Dhofar. "
            "Swahili adstrate from Omani maritime trade / Zanzibar sultanate. "
            "Persian adstrate from Hormuz trade."
        ),
    ),

    "ar-YE": LanguageSpec(
        code="ar-YE",
        name="Yemeni Arabic (Ṣanʿānī)",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_YE,
        allophones=ALLOPHONES_YE,
        parent="ar-x-peninsular",
        ancestors=(
            Ancestor("ar-x-peninsular", P, 0.90,
                     "Peninsular Arabic base"),
        ),
        notes=(
            "Yemeni Arabic — Ṣanʿānī (North Yemeni) as reference variety. "
            "ج → /ɡ/ in Ṣanʿānī (shared with Egyptian; independent parallel). "
            "ق → /q/ PRESERVED (conservative). "
            "ث /θ/, ذ /ð/, ظ /ðˤ/ ALL PRESERVED (very conservative). "
            "UNIQUE: ض merges with ظ → /ðˤ/ in Ṣanʿānī "
            "(lost the distinction preserved in Classical and most other dialects). "
            "No k → /tʃ/ (unlike Gulf). Vowel imāla present. "
            "Watson (1993) primary reference for Ṣanʿānī Arabic. "
            "South Yemen (Aden/Taʿizz) more similar to Gulf in some features."
        ),
    ),
}
