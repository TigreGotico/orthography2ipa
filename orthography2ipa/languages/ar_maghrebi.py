"""Arabic — Maghrebi dialects (Moroccan, Algerian, Tunisian, Libyan, Hassaniya).

Maghrebi Arabic comprises the varieties spoken in North Africa west of Egypt.
It forms the most phonologically distinctive cluster of Arabic dialects, chiefly
due to the radical vowel reduction inherited from medieval contact with Berber
(Tamazight) and the earlier Latinised population of Roman North Africa.

Genealogy:
  Classical Arabic (arb)
       ↓
  Proto-Maghrebi Arabic (ar-x-maghrebi)     ~9th–12th c. CE
       ↓
  ┌──────────┬───────────┬──────────┬──────────────┐
  ar-MA    ar-DZ     ar-TN    ar-LY          ar-MR
(Moroccan) (Algerian) (Tunisian) (Libyan)   (Hassaniya)

Sources:
- Harrell, R.S. (1962). *The Phonology of Colloquial Egyptian Arabic*. ACLS.
  [Comparative reference]
- Heath, J. (2002). *Jewish and Muslim Dialects of Moroccan Arabic*. Routledge.
- Caubet, D. (1993). *L'Arabe marocain*. Peeters. [2 vols.]
- Herce, B. (2021). "The Collapse of Short Vowels in Moroccan Arabic."
  Phonology 38(3).
- Marçais, W. (1902). *Le dialecte arabe parlé à Tlemcen*. Leroux.
  [Algerian Arabic]
- Marçais, P. (1977). *Esquisse grammaticale de l'arabe maghrébin*. Maisonneuve.
- Talmoudi, F. (1980). *The Arabic Dialect of Sūsa*. Gothenburg UP. [Tunisian]
- Gibson, M. (2002). *Tunis Arabic*. München. [LINCOM Grammar]
- Owens, J. & Elgibali, A. (2010). *Information Structure in Spoken Arabic*. Routledge.
- Mitchell, T.F. (1960). *Colloquial Arabic: The Living Language of Egypt*.
  EUP. [Comparative]
- Holes, C. (2004). *Modern Arabic*. Georgetown UP.
- Ould Mohamed Baba, A.S. (2010). "Hassaniya Arabic." In: *Encyclopedia of Arabic
  Language and Linguistics*. Brill.
"""

from orthography2ipa.languages.ar_classical import (
    GRAPHEMES_MAGHREBI_BASE, ALLOPHONES_MAGHREBI_BASE,
)
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
AD = AncestorRole.ADSTRATE
SUP = AncestorRole.SUPERSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# MOROCCAN ARABIC / DARIJA (ar-MA)
# ═══════════════════════════════════════════════════════════════════════════
#
# Moroccan Arabic (called "Darija" دارجة) is the most divergent of the
# mainstream Arabic dialects. Its extreme divergence is primarily due to:
#   1. VOWEL DELETION: Most unstressed short vowels are deleted in fast speech,
#      creating consonant clusters unknown in other Arabic dialects.
#   2. Berber (Tamazight/Tachelhit) substrate — the most powerful influence
#      after Classical Arabic itself. Morocco had dense Berber-speaking
#      populations when Arabic arrived.
#   3. Andalusi Arabic adstrate (returned Moriscos after 1609 CE)
#   4. Romance/Spanish substrate (northern Morocco)
#   5. French colonial influence (1912–1956) — established /p/ and /v/
#
# PHONOLOGICAL PROFILE:
#
# Consonants:
#   ث → /t/ (complete merger; some rural/conservative → /s/)
#   ذ → /d/ (complete merger)
#   ظ → /dˤ/ (emphatic d)
#   ض → /dˤ/ (lateral lost; merged with ط/ظ)
#   ق → /q/ PRESERVED (unlike Eastern urban dialects) — this is a key
#     Maghrebi feature; some northern/Jbala area speakers have /ɡ/
#   ج → /dʒ/ preserved
#   Pharyngeals ħ, ʕ REINFORCED by Berber substrate (very prominent)
#   New: /p/ (from French/Spanish), /v/ (from French)
#   New: /tʃ/ in loanwords
#
# Vowels:
#   SHORT VOWELS DELETED in many unstressed environments:
#     Classical *kitāb → Moroccan /ktab/ (no short vowel in first syllable)
#     Classical *walad → Moroccan /wld/
#   Long vowels maintained but shortened in unstressed syllables
#   /e/ and /o/ from French loanwords
#
# The resulting consonant clusters (2–4 consonants) are typologically unusual
# in Arabic but normal in Berber — clear substrate effect.

GRAPHEMES_MA = {
    **GRAPHEMES_MAGHREBI_BASE,
    # Interdentals: fully merged
    "ث": ["t"],  # θ → t (some elderly/rural: s or θ)
    "ذ": ["d"],
    "ظ": ["dˤ"],
    "ض": ["dˤ"],  # merged with ط in practice
    # ق PRESERVED in standard Darija
    "ق": ["q"],  # uvular q (unlike Cairo ʔ)
    # European loanwords
    "e": ["e"],  # French /e/ in loanwords: le café → [kafé]
    "o": ["o"],
}

ALLOPHONES_MA = {
    **ALLOPHONES_MAGHREBI_BASE,
    "ɮˤ": ["dˤ"],
    "θ": ["t"],
    "ð": ["d"],
    "ðˤ": ["dˤ"],
    # ق: q in most Darija; ɡ in some northern dialects
    "q": ["q", "ɡ"],
    # Extreme vowel reduction
    "a": ["a", "ə", "∅"],  # deleted in many unstressed environments
    "i": ["i", "ə", "∅"],
    "u": ["u", "ə", "∅"],
    "aː": ["aː", "æː"],
    "iː": ["iː"],
    "uː": ["uː"],
    # European phonemes established
    "p": ["p"],
    "v": ["v"],
    "e": ["e"],
    "o": ["o"],
    # Nasals — place assimilation as in other dialects
    "n": ["n", "m", "ŋ"],
    "l": ["l", "ɫ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# ALGERIAN ARABIC (ar-DZ)
# ═══════════════════════════════════════════════════════════════════════════
#
# Algerian Arabic is intermediate between Moroccan (more reduced) and
# Tunisian (less reduced). It spans several regional varieties:
#   - Western Algeria (Oran/Wahrān): Spanish and French influence
#   - Eastern Algeria (Constantine/Qusanṭīna): more conservative
#   - Algiers (Madīnat al-Jazāʾir): urban koiné, French-influenced
#
# PHONOLOGICAL PROFILE:
#   Very similar to Moroccan but with:
#   - Somewhat less extreme vowel reduction than Moroccan
#   - Heavier French integration (130 years of colonial rule, 1830–1962)
#   - /p/, /v/ from French thoroughly established
#   - ق → /q/ (eastern) or /ɡ/ (western/Oran area)
#   - Some Berber substrate (less dense than Morocco in coastal areas,
#     but very dense in Kabylie/Berber-speaking areas)

GRAPHEMES_DZ = {
    **GRAPHEMES_MAGHREBI_BASE,
    "ث": ["t", "s"],  # t in most areas; s in eastern Algerian
    "ذ": ["d", "z"],  # d most common; z in eastern dialects
    "ظ": ["dˤ", "zˤ"],
    "ض": ["dˤ"],
    "ق": ["q", "ɡ"],  # q eastern/conservative; ɡ western/Oran
    "e": ["e"],
    "o": ["o"],
}

ALLOPHONES_DZ = {
    **ALLOPHONES_MAGHREBI_BASE,
    "ɮˤ": ["dˤ"],
    "θ": ["t", "s"],
    "ð": ["d", "z"],
    "ðˤ": ["dˤ", "zˤ"],
    "q": ["q", "ɡ"],
    # Vowel reduction — moderate (less than Moroccan)
    "a": ["a", "ə", "∅"],
    "i": ["i", "ə", "∅"],
    "u": ["u", "ə", "∅"],
    "p": ["p"],
    "v": ["v"],
    "e": ["e"],
    "o": ["o"],
    "n": ["n", "m", "ŋ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# TUNISIAN ARABIC (ar-TN)
# ═══════════════════════════════════════════════════════════════════════════
#
# Tunisian Arabic (Tūnsī / Derja تونسية) is the most studied Maghrebi dialect
# due to good documentation (Marçais, Gibson, Saada) and relative transparency.
# It is intermediate between the Algerian and Libyan varieties.
#
# PHONOLOGICAL PROFILE:
#   - Vowel reduction: SIGNIFICANT but LESS than Moroccan
#     (short unstressed vowels reduced to schwa, often deleted)
#   - ث → /t/ (urban Tunis); some rural → /θ/ or /s/
#   - ذ → /d/
#   - ظ → /dˤ/ (Tunis) or /zˤ/ (some coastal areas)
#   - ض → /dˤ/
#   - ق → /q/ (preserved) or /ɡ/ (urban Tunis, borrowing from Maghrebi pattern)
#   - ج → /dʒ/ preserved
#   - French influence: /p/ and /v/ established
#   - Italian influence: /tʃ/ in some loanwords (historical Sicilian contact)
#   - Distinct vowel: Tunisian has developed /ɪ/ and /ʊ/ allophones
#     from short vowel weakening

GRAPHEMES_TN = {
    **GRAPHEMES_MAGHREBI_BASE,
    "ث": ["t", "θ"],  # t urban; θ rural/conservative
    "ذ": ["d"],
    "ظ": ["dˤ", "zˤ"],
    "ض": ["dˤ"],
    "ق": ["q", "ɡ"],  # q rural/conservative; ɡ urban Tunis
    "e": ["e"],
    "o": ["o"],
}

ALLOPHONES_TN = {
    **ALLOPHONES_MAGHREBI_BASE,
    "ɮˤ": ["dˤ"],
    "θ": ["t", "θ", "s"],
    "ð": ["d", "z"],
    "ðˤ": ["dˤ", "zˤ"],
    "q": ["q", "ɡ"],
    # Moderate vowel reduction
    "a": ["a", "ə", "∅"],
    "i": ["i", "ɪ", "ə", "∅"],
    "u": ["u", "ʊ", "ə", "∅"],
    "p": ["p"],
    "v": ["v"],
    "e": ["e"],
    "o": ["o"],
    "n": ["n", "m", "ŋ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# LIBYAN ARABIC (ar-LY)
# ═══════════════════════════════════════════════════════════════════════════
#
# Libyan Arabic spans two main varieties:
#   - Western (Tripoli / Tarābulus): urban, Tunisian-influenced
#   - Eastern (Benghazi / Barqa): more conservative, Egyptian-influenced
#
# PHONOLOGICAL PROFILE:
#   - Less vowel reduction than Moroccan/Algerian (closer to Eastern Arabic)
#   - ث → /t/ (urban western) or preserved /θ/ (eastern, Benghazi area)
#   - ذ → /d/ (western) or preserved /ð/ (eastern)
#   - ظ → /dˤ/ or /zˤ/ (varies east/west)
#   - ض → /dˤ/
#   - ق → /q/ PRESERVED (conservative Libyan feature)
#   - ج → /dʒ/ preserved (not ɡ as in Egyptian)
#   - Italian influence: /p/ and some /tʃ/ from Italian colonial period (1911–1943)
#   - Berber (Amazigh) substrate in interior / Nafusa plateau dialects

GRAPHEMES_LY = {
    **GRAPHEMES_MAGHREBI_BASE,
    "ث": ["t", "θ"],  # t western; θ eastern (Benghazi area)
    "ذ": ["d", "ð"],  # d western; ð eastern
    "ظ": ["dˤ", "zˤ"],
    "ض": ["dˤ"],
    "ق": ["q"],  # PRESERVED in most Libyan varieties
    "e": ["e"],
    "o": ["o"],
}

ALLOPHONES_LY = {
    **ALLOPHONES_MAGHREBI_BASE,
    "ɮˤ": ["dˤ"],
    "θ": ["t", "θ"],
    "ð": ["d", "ð"],
    "ðˤ": ["dˤ", "zˤ"],
    "q": ["q"],  # uvular preserved
    # Vowel reduction: less extreme than Moroccan/Algerian
    "a": ["a", "ə"],
    "i": ["i", "ə"],
    "u": ["u", "ə"],
    "p": ["p"],  # from Italian loanwords
    "e": ["e"],
    "o": ["o"],
    "n": ["n", "m", "ŋ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# HASSANIYA ARABIC (ar-MR)  — Mauritania / Western Sahara
# ═══════════════════════════════════════════════════════════════════════════
#
# Hassaniya (ħassāniyya حسانية) is spoken in Mauritania, Western Sahara,
# and parts of Mali, Senegal, Morocco, and southern Algeria.
# It is named after the Banū Ḥassān tribe who brought Arabic to the region.
#
# PHONOLOGICAL PROFILE (the most conservative Maghrebi variety):
#   - Closer to Classical/Peninsula than other Maghrebi dialects
#   - θ and ð OFTEN PRESERVED (unlike Moroccan/Tunisian/Algerian)
#   - ق → /q/ preserved
#   - ج → /ʒ/ (has merged with French ʒ; some varieties → dʒ)
#   - Emphatics well preserved
#   - Pharyngeals ħ, ʕ very robust
#   - Vowel reduction LESS EXTREME than Moroccan
#   - Wolof / Berber / Fulani contact: some substrate effects
#   - /ŋ/ as phoneme in some Fulani-influenced areas

GRAPHEMES_MR = {
    **GRAPHEMES_MAGHREBI_BASE,
    # More conservative: θ, ð preserved
    "ث": ["θ", "t"],  # θ preserved in much of Hassaniya
    "ذ": ["ð", "d"],  # ð preserved
    "ظ": ["ðˤ", "dˤ"],  # ðˤ preserved (closer to Classical)
    "ض": ["dˤ", "ðˤ"],
    "ق": ["q"],  # preserved
    "ج": ["ʒ", "dʒ"],  # ʒ standard; dʒ in some conservative speech
}

ALLOPHONES_MR = {
    **ALLOPHONES_MAGHREBI_BASE,
    "ɮˤ": ["dˤ", "ðˤ"],
    "θ": ["θ", "t"],
    "ð": ["ð", "d"],
    "ðˤ": ["ðˤ", "dˤ"],
    "q": ["q"],
    "dʒ": ["ʒ", "dʒ"],
    "ʒ": ["ʒ"],
    # Less extreme vowel reduction than Moroccan
    "a": ["a", "ə"],
    "i": ["i", "ə"],
    "u": ["u", "ə"],
    "aː": ["aː"],
    "n": ["n", "m", "ŋ"],
    # Fulani contact: ŋ in some proper nouns / borrowings
    "ŋ": ["ŋ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SPECS
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "ar-MA": LanguageSpec(
        code="ar-MA",
        name="Moroccan Arabic (Darija)",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_MA,
        allophones=ALLOPHONES_MA,
        parent="ar-x-maghrebi",
        ancestors=(
            Ancestor("ar-x-maghrebi", P, 0.78,
                     "Maghrebi Arabic base"),
            Ancestor("arb", P, 0.75,
                     "Classical Arabic descent via 7th–8th c. Umayyad expansion"),
            Ancestor("ber", SUB, 0.15,
                     "Berber (Tamazight/Tachelhit) substrate: "
                     "CHIEF cause of vowel deletion; emphatic system reinforced; "
                     "consonant cluster tolerance from Berber phonotactics"),
            Ancestor("xaa", AD, 0.04,
                     "Andalusi Arabic adstrate from Moriscos (post-1492/1609)"),
            Ancestor("fr", AD, 0.03,
                     "French adstrate: /p/, /v/, /e/, /o/ phonemes"),
        ),
        notes=(
            "Moroccan Arabic 'Darija' (دارجة). Most divergent mainstream dialect. "
            "DEFINING FEATURE: extreme vowel deletion — short unstressed vowels "
            "often deleted, creating 3–4 consonant clusters unusual in Arabic. "
            "θ → /t/, ð → /d/, ðˤ → /dˤ/ (emphatic lateral ض → dˤ). "
            "ق → /q/ PRESERVED (Maghrebi conservative feature). "
            "Pharyngeals ħ, ʕ very strong (Berber substrate reinforcement). "
            "French loanwords: /p/ and /v/ established as phonemes. "
            "Berber substrate is the primary explanation for vowel reduction "
            "and consonant cluster tolerance (Herce 2021, Caubet 1993)."
        ),
    ),

    "ar-DZ": LanguageSpec(
        code="ar-DZ",
        name="Algerian Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_DZ,
        allophones=ALLOPHONES_DZ,
        parent="ar-x-maghrebi",
        ancestors=(
            Ancestor("ar-x-maghrebi", P, 0.80,
                     "Maghrebi Arabic base"),
            Ancestor("arb", P, 0.78,
                     "Classical Arabic descent"),
            Ancestor("ber", SUB, 0.12,
                     "Berber (Tamazight/Kabyle) substrate: vowel reduction, "
                     "consonant cluster tolerance; dense Berber-speaking areas "
                     "especially Kabylie"),
            Ancestor("fr", AD, 0.05,
                     "French adstrate (1830–1962): /p/, /v/ phonemes, "
                     "heavy loanword influence"),
        ),
        notes=(
            "Algerian Arabic. Complex dialect landscape from Oran (west) "
            "to Constantine (east). "
            "Intermediate between Moroccan (more reduced) and Tunisian. "
            "θ → /t/ or /s/; ð → /d/ or /z/. "
            "ق → /q/ (eastern) or /ɡ/ (western, Oran area). "
            "Berber substrate (especially Kabylie) reinforces emphatics. "
            "French integration deepest of all Maghrebi dialects "
            "(130+ years colonial rule)."
        ),
    ),

    "ar-TN": LanguageSpec(
        code="ar-TN",
        name="Tunisian Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_TN,
        allophones=ALLOPHONES_TN,
        parent="ar-x-maghrebi",
        ancestors=(
            Ancestor("ar-x-maghrebi", P, 0.83,
                     "Maghrebi Arabic base"),
            Ancestor("arb", P, 0.80,
                     "Classical Arabic descent"),
            Ancestor("ber", SUB, 0.08,
                     "Berber substrate (less dense than Morocco/Kabylie)"),
            Ancestor("fr", AD, 0.04,
                     "French adstrate: /p/, /v/ established"),
        ),
        notes=(
            "Tunisian Arabic (Derja تونسية). "
            "Intermediate Maghrebi variety. Vowel reduction significant "
            "but less extreme than Moroccan. "
            "θ → /t/ (urban Tunis); some rural varieties preserve /θ/. "
            "ق → /q/ conservative; /ɡ/ in urban Tunis. "
            "Historical Italian/Sicilian contact: /tʃ/ in some loans. "
            "Best-documented Maghrebi dialect (Gibson 2002, Talmoudi 1980)."
        ),
    ),

    "ar-LY": LanguageSpec(
        code="ar-LY",
        name="Libyan Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_LY,
        allophones=ALLOPHONES_LY,
        parent="ar-x-maghrebi",
        ancestors=(
            Ancestor("ar-x-maghrebi", P, 0.85,
                     "Maghrebi Arabic base"),
            Ancestor("arb", P, 0.83,
                     "Classical Arabic descent"),
            Ancestor("ber", SUB, 0.07,
                     "Berber substrate (Nafusa plateau / interior)"),
        ),
        notes=(
            "Libyan Arabic. Two main varieties: "
            "Western (Tripoli): Maghrebi features, θ → /t/; "
            "Eastern (Benghazi/Barqa): more conservative, θ preserved, "
            "Egyptian-influenced features. "
            "ق → /q/ PRESERVED in most Libyan varieties (conservative). "
            "Vowel reduction less extreme than Moroccan. "
            "Italian colonial influence (1911–1943): /p/ in loans, some /tʃ/."
        ),
    ),

    "ar-MR": LanguageSpec(
        code="ar-MR",
        name="Hassaniya Arabic (Mauritanian)",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_MR,
        allophones=ALLOPHONES_MR,
        parent="ar-x-maghrebi",
        ancestors=(
            Ancestor("ar-x-maghrebi", P, 0.80,
                     "Maghrebi Arabic base (but more conservative)"),
            Ancestor("arb", P, 0.82,
                     "Classical Arabic descent — most conservative Maghrebi"),
            Ancestor("ber", SUB, 0.10,
                     "Berber (Znaga/Sanhaja) substrate"),
        ),
        notes=(
            "Hassaniya Arabic (ħassāniyya حسانية). Spoken in Mauritania, "
            "Western Sahara, southern Morocco/Algeria, Mali, Senegal. "
            "MOST CONSERVATIVE Maghrebi dialect: "
            "θ and ð often preserved (unlike other Maghrebi varieties); "
            "ðˤ (ظ) preserved in many varieties; "
            "ق → /q/ preserved; vowel reduction less extreme. "
            "Berber (Znaga/Sanhaja) substrate: phonological reinforcement. "
            "Sub-Saharan contact (Wolof, Fulani, Soninke): some borrowings; "
            "/ŋ/ phoneme present in some Fulani-influenced varieties."
        ),
    ),
}
