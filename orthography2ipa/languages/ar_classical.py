"""Classical Arabic (arb) — grapheme→IPA and allophone mappings.

Classical Arabic (العربية الفصحى al-ʿArabiyya al-fuṣḥā) is the direct
ancestor of all modern Arabic dialects. It refers specifically to the
language of the pre-Islamic and early Islamic period (~6th–9th century CE),
codified from the Quranic recitation tradition and the poetry of the tribes.

This is distinct from Modern Standard Arabic (ar / MSA), which is a
19th–20th century academic/media standardisation. Dialects descend from
spoken Classical Arabic (not from MSA).

Sources:
- Cantineau, J. (1960). *Études de linguistique sémitique et arabe*. Mouton.
- Wright, W. (1896). *A Grammar of the Arabic Language*. 3rd ed. CUP.
  [Still the most complete Classical Arabic grammar]
- Carter, M.G. (2004). *Sībawayhi*. Georgetown UP.
  [The 8th-century Kitāb — primary historical phonological source]
- Sibawayhi (8th c. CE). *al-Kitāb*. [Original source; vowel/consonant description]
- Watson, J.C.E. (2002). *The Phonology and Morphology of Arabic*. OUP.
- Owens, J. (2006). *A Linguistic History of Arabic*. OUP.
- Versteegh, K. (2014). *The Arabic Language*. 2nd ed. Edinburgh UP.
- Al-Nassir, A.A. (1993). *Sibawayhi the Phonologist*. Kegan Paul.
- Thelwall, R. & Sa'Adeddin, M.A. (1990). "Arabic." JIPA 20(2), 37–41.

Phonological notes:
- The 28-consonant inventory of Classical Arabic is NEARLY identical to
  Modern Standard Arabic. Key differences:
  (1) ض was pronounced as a LATERAL EMPHATIC /ɮˤ/ or /dˤˡ/ in Classical
      Arabic, not the modern /dˤ/ or /zˤ/ of contemporary dialects.
      Sibawayhi explicitly describes it as a lateral sound.
  (2) Classical Arabic had full short vowel realisation (fatḥa, ḍamma,
      kasra all fully pronounced), unlike many modern dialects.
  (3) Word-final case vowels (i'rāb) were fully pronounced.
  (4) ج was probably /dʒ/ (this is debated; some evidence for /ɡ/).
  (5) Hamza (ء/ʔ) was fully realised, not dropped as in many dialects.
"""

from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT

# ═══════════════════════════════════════════════════════════════════════════
# GRAPHEME TABLE — Arabic Script
# ═══════════════════════════════════════════════════════════════════════════
#
# Keys: Arabic letters in their isolated forms (Unicode Arabic block).
# Values: primary IPA values as described by Sibawayhi and later grammarians.
#
# The KEY phonological difference from MSA (ar):
#   - ض → /ɮˤ/ (emphatic lateral) in Classical; /dˤ/ in MSA/dialects

GRAPHEMES_CLASSICAL = {
    # ── Long vowel matres lectionis ─────────────────────────────────────
    "ا": ["ʔ", "aː"],  # alif: glottal stop (word-initial) or long /aː/
    "أ": ["ʔa"],  # hamza above alif
    "إ": ["ʔi"],  # hamza below alif
    "آ": ["ʔaː"],  # alif madda — hamza + long a
    "ى": ["aː"],  # alif maqṣūra — word-final long a
    "ة": ["a", "at"],  # tāʾ marbūṭa: [a] pausal / [at] before suffix

    # ── Consonants (in traditional Arabic alphabetical order) ────────────
    "ب": ["b"],
    "ت": ["t"],
    "ث": ["θ"],  # voiceless interdental (PRESERVED in Classical)
    "ج": ["dʒ"],  # affricate; evidence for earlier /ɡ/ disputed
    "ح": ["ħ"],  # voiceless pharyngeal fricative
    "خ": ["x"],  # voiceless velar fricative
    "د": ["d"],
    "ذ": ["ð"],  # voiced interdental (PRESERVED in Classical)
    "ر": ["r"],  # alveolar trill
    "ز": ["z"],
    "س": ["s"],
    "ش": ["ʃ"],
    "ص": ["sˤ"],  # emphatic (pharyngealised) s
    "ض": ["ɮˤ"],  # emphatic lateral fricative — Classical pronunciation
    # Sibawayhi: "most powerful of Arabic sounds"
    # Modern dialects: → /dˤ/ (Egypt, Levant) or /zˤ/ (Gulf)
    "ط": ["tˤ"],  # emphatic t
    "ظ": ["ðˤ"],  # emphatic interdental (pharyngealised ð)
    "ع": ["ʕ"],  # voiced pharyngeal fricative
    "غ": ["ɣ"],  # voiced velar fricative
    "ف": ["f"],
    "ق": ["q"],  # uvular stop (PRESERVED in Classical)
    "ك": ["k"],
    "ل": ["l"],
    "م": ["m"],
    "ن": ["n"],
    "ه": ["h"],
    "و": ["w", "uː"],  # wāw: consonantal /w/ or long vowel /uː/
    "ي": ["j", "iː"],  # yāʾ: consonantal /j/ or long vowel /iː/
    "ء": ["ʔ"],  # hamza (standalone)

    # ── Short vowel diacritics (ḥarakāt) ────────────────────────────────
    "\u064E": ["a"],  # fatḥa (short a — FULLY REALISED in Classical)
    "\u064F": ["u"],  # ḍamma (short u)
    "\u0650": ["i"],  # kasra (short i)
    "\u064B": ["an"],  # tanwīn fatḥa (nunation)
    "\u064C": ["un"],  # tanwīn ḍamma
    "\u064D": ["in"],  # tanwīn kasra
    "\u0651": ["ː"],  # shadda (gemination mark)
    "\u0652": [""],  # sukūn (no vowel in this syllable)

    # ── Definite article ────────────────────────────────────────────────
    "ال": ["al", "a"],  # al- sun letter assimilation gives /a+C+:/ before
    # the 14 "sun letters" (dental/alveolar consonants)

    # ── Long vowels (as sequences) ───────────────────────────────────────
    "اَ": ["aː"],  # alif after fatḥa
    "وُ": ["uː"],  # wāw after ḍamma
    "يِ": ["iː"],  # yāʾ after kasra

    # ── Diphthongs ────────────────────────────────────────────────────────
    "وَ": ["aw"],  # wāw after fatḥa (falling diphthong)
    "يَ": ["aj"],  # yāʾ after fatḥa (falling diphthong)
}

ALLOPHONES_CLASSICAL = {
    # ── Stops ───────────────────────────────────────────────────────────
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "k": ["k"],
    "q": ["q"],  # no dialectal ʔ/ɡ variants in Classical
    "ʔ": ["ʔ"],  # fully realised in Classical (not dropped)

    # ── Emphatics ───────────────────────────────────────────────────────
    "sˤ": ["sˤ"],
    "ɮˤ": ["ɮˤ"],  # the Classical ض — lateral emphatic
    "tˤ": ["tˤ"],
    "ðˤ": ["ðˤ"],  # ظ

    # ── Fricatives ──────────────────────────────────────────────────────
    "f": ["f"],
    "θ": ["θ"],  # ث — not merged to /t/ or /s/ as in dialects
    "ð": ["ð"],  # ذ — not merged to /d/ as in dialects
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"],
    "x": ["x"],
    "ɣ": ["ɣ"],
    "ħ": ["ħ"],
    "ʕ": ["ʕ"],
    "h": ["h"],
    "dʒ": ["dʒ"],  # ج — Classical affricate

    # ── Sonorants ────────────────────────────────────────────────────────
    "m": ["m"],
    "n": ["n", "m", "ŋ"],  # nasal place assimilation before labials/velars
    "l": ["l", "ɫ"],  # emphatic /l/ in الله [aɫˈɫaːh]
    "r": ["r"],  # alveolar trill (robust in Classical)

    # ── Glides ────────────────────────────────────────────────────────────
    "w": ["w"], "j": ["j"],

    # ── Vowels ────────────────────────────────────────────────────────────
    # All six vowel qualities FULLY realised (no reduction in Classical)
    "a": ["a", "æ", "ɑ"],  # backed near emphatics, fronted elsewhere
    "i": ["i"],
    "u": ["u"],
    "aː": ["aː", "ɑː"],  # long a backed near emphatics
    "iː": ["iː"],
    "uː": ["uː"],
    "aj": ["aj"],
    "aw": ["aw"],
}

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-MASHRIQI ARABIC (ar-x-mashriqi)  ~8th–12th century CE
# ═══════════════════════════════════════════════════════════════════════════
#
# The Eastern Arabic branch encompasses: Egyptian, Sudanese, Levantine,
# Iraqi, and Gulf Arabic. It shares several features distinguishing it from
# Maghrebi Arabic, though it is not a single geographically contiguous branch.
#
# SHARED EASTERN FEATURES (vs. Maghrebi):
#   1. Short vowels generally RETAINED (not deleted in closed syllables)
#   2. ج /dʒ/ (not merged to /ʒ/ except Levant, not /ɡ/ except Egypt)
#   3. Long vowels generally maintained
#   4. Verbal morphology more regular / closer to Classical
#   5. ق → [q] (Bedouin/conservative) or [ʔ/ɡ] (sedentary/urban)
#
# See individual dialect specs for specific features.

GRAPHEMES_MASHRIQI_BASE = {
    **GRAPHEMES_CLASSICAL,
    # ث → /t/ in most urban Eastern varieties (not θ)
    "ث": ["t", "θ"],  # /t/ urban sedentary; /θ/ rural/conservative
    # ذ → /d/
    "ذ": ["d", "ð"],
    # ظ → /dˤ/ or /zˤ/ (the lateral emphatic is fully gone)
    "ظ": ["dˤ", "zˤ"],
    # ض → /dˤ/ (lateral quality fully lost; merge with ط in some varieties)
    "ض": ["dˤ"],
    # New loanword phonemes
    "پ": ["p"],  # /p/ in modern loanwords
    "ڤ": ["v"],  # /v/ in European loanwords
    "چ": ["tʃ"],  # /tʃ/ in some Gulf/Iraqi loanwords
}

ALLOPHONES_MASHRIQI_BASE = {
    **ALLOPHONES_CLASSICAL,
    "ɮˤ": ["dˤ"],  # ض → /dˤ/ (lateral feature lost)
    "ðˤ": ["dˤ", "zˤ"],  # ظ → /dˤ/ or /zˤ/
    "θ": ["θ", "t", "s"],  # ث → /t/ or /s/ in colloquial
    "ð": ["ð", "d", "z"],  # ذ → /d/ or /z/ in colloquial
    "q": ["q", "ʔ", "ɡ"],  # ق → varies by area
    "p": ["p"],
    "v": ["v"],
}

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-MAGHREBI ARABIC (ar-x-maghrebi)  ~9th–12th century CE
# ═══════════════════════════════════════════════════════════════════════════
#
# Maghrebi Arabic derives from the speech of Arab settlers who arrived in
# North Africa from ~647 CE onwards. It was profoundly shaped by:
#   1. Berber (Tamazight) substrate — pharyngeals reinforced, emphatics stable
#   2. Latin substratum (remnant of North African Latinity)
#   3. Later contact with Andalusi Arabic (9th–15th c.)
#   4. Ottoman Turkish influence (16th–19th c.)
#   5. French/Spanish/Italian colonial influence (19th–20th c.)
#
# DEFINING MAGHREBI INNOVATIONS:
#   1. VOWEL REDUCTION — unstressed short vowels deleted/reduced
#      (the most distinctive Maghrebi feature; cf. "consonant clusters")
#   2. ث → /t/ or /s/ (no interdental preservation in most varieties)
#   3. ذ → /d/ (interdental merger)
#   4. ظ → /dˤ/ (not /zˤ/ as in Gulf)
#   5. ق → /q/ (PRESERVED — unlike urban Eastern Arabic)
#      In many Maghrebi varieties /q/ is maintained, unlike Levant/Egyptian
#   6. ج → /dʒ/ preserved
#   7. Berber substrate: pharyngeals ħ, ʕ REINFORCED (not weakened)
#   8. New phonemes /p/ and /v/ from French/Spanish

GRAPHEMES_MAGHREBI_BASE = {
    **GRAPHEMES_CLASSICAL,
    # Interdental mergers
    "ث": ["t", "s"],  # θ → t (most varieties) or s (some eastern areas)
    "ذ": ["d"],  # ð → d
    "ظ": ["dˤ"],  # ðˤ → dˤ
    "ض": ["dˤ"],  # ɮˤ → dˤ (lateral lost)
    # ق generally preserved
    "ق": ["q"],  # uvular stop maintained (vs. Eastern ʔ/ɡ)
    # New phonemes from loanwords
    "پ": ["p"],
    "ڤ": ["v"],
}

ALLOPHONES_MAGHREBI_BASE = {
    **ALLOPHONES_CLASSICAL,
    "ɮˤ": ["dˤ"],
    "ðˤ": ["dˤ"],
    "θ": ["t", "s", "θ"],
    "ð": ["d"],
    # Short vowels deleted in many contexts — shown as ∅ variant
    "a": ["a", "∅"],
    "i": ["i", "∅"],
    "u": ["u", "∅"],
    "p": ["p"],
    "v": ["v"],
}

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-PENINSULAR ARABIC (ar-x-peninsular)  ~8th–12th century CE
# ═══════════════════════════════════════════════════════════════════════════
#
# Peninsular Arabic covers the varieties of the Arabian Peninsula:
# Hejazi, Najdi, Gulf, Yemeni, and Omani Arabic.
#
# SHARED PENINSULAR FEATURES:
#   1. Interdentals θ, ð OFTEN PRESERVED (more conservative than Eastern)
#   2. ق → /q/ preserved or → /ɡ/ (Bedouin)
#   3. ج → /dʒ/ generally preserved
#   4. Vowel imāla (raising of /aː/ → /eː/) in some varieties
#   5. k → /tʃ/ before front vowels in Gulf varieties
#   6. Three-vowel quality system generally maintained

GRAPHEMES_PENINSULAR_BASE = {
    **GRAPHEMES_CLASSICAL,
    # Interdentals often preserved
    "ث": ["θ", "t", "s"],  # θ preserved in many varieties
    "ذ": ["ð", "d"],  # ð preserved in many varieties
    "ظ": ["ðˤ", "dˤ"],  # ðˤ preserved or → dˤ
    "ض": ["dˤ", "ðˤ"],  # lateral lost; dˤ or ðˤ
    "ج": ["dʒ", "ɡ", "j"],  # dʒ standard; ɡ in some areas; j in others
    "ق": ["q", "ɡ"],  # q preserved (conservative) or ɡ (Bedouin)
}

ALLOPHONES_PENINSULAR_BASE = {
    **ALLOPHONES_CLASSICAL,
    "ɮˤ": ["dˤ", "ðˤ"],
    "θ": ["θ", "t"],
    "ð": ["ð", "d"],
    "ðˤ": ["ðˤ", "dˤ"],
    "q": ["q", "ɡ"],
    "k": ["k", "tʃ"],  # k → tʃ before front vowels (Gulf feature)
    "dʒ": ["dʒ", "ɡ", "j"],
}

SPECS = {
    "arb": LanguageSpec(
        code="arb",
        name="Classical Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_CLASSICAL,
        allophones=ALLOPHONES_CLASSICAL,
        parent="xpa",
        ancestors=(
            Ancestor("xpa", P, 1.0,
                     "Direct descent from Proto-Arabic / Old North Arabian"),
        ),
        notes=(
            "Classical Arabic (العربية الفصحى, al-ʿArabiyya al-fuṣḥā). "
            "The variety of the Quran and pre-Islamic poetry (~6th–9th c. CE). "
            "All modern Arabic dialects descend from spoken Classical Arabic "
            "(not from Modern Standard Arabic / MSA). "
            "28-consonant inventory. "
            "KEY CLASSICAL FEATURES: "
            "(1) ض /ɮˤ/ — emphatic LATERAL fricative (described by Sibawayhi "
            "as a lateral sound; modern dialects shift to /dˤ/ or /zˤ/); "
            "(2) ث /θ/ and ذ /ð/ fully preserved as interdentals; "
            "(3) ء /ʔ/ always realised (not dropped); "
            "(4) ق /q/ always uvular (no urban ʔ variant); "
            "(5) all three short vowels (/a i u/) fully pronounced (no deletion); "
            "(6) word-final case vowels (iʿrāb) pronounced; "
            "(7) diphthongs /aj/ and /aw/ preserved (not monophthongised). "
            "Source: Sibawayhi, al-Kitāb (8th c.); Wright (1896); Watson (2002)."
        ),
    ),

    "ar-x-mashriqi": LanguageSpec(
        code="ar-x-mashriqi",
        name="Proto-Mashriqi Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_MASHRIQI_BASE,
        allophones=ALLOPHONES_MASHRIQI_BASE,
        parent="arb",
        ancestors=(
            Ancestor("arb", P, 0.95, "Descent from Classical Arabic"),
        ),
        notes=(
            "Proto-Mashriqi (Eastern) Arabic — abstract ancestor node for "
            "Egyptian, Sudanese, Levantine, Iraqi, and Gulf Arabic. "
            "Key shared Eastern features: short vowels generally retained; "
            "ج /dʒ/ preserved; ث → /t/, ذ → /d/ in sedentary varieties; "
            "ض → /dˤ/ (lateral lost); long vowels maintained."
        ),
    ),

    "ar-x-maghrebi": LanguageSpec(
        code="ar-x-maghrebi",
        name="Proto-Maghrebi Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_MAGHREBI_BASE,
        allophones=ALLOPHONES_MAGHREBI_BASE,
        parent="arb",
        ancestors=(
            Ancestor("arb", P, 0.85,
                     "Descent from Classical Arabic via 7th–8th c. expansion"),
        ),
        notes=(
            "Proto-Maghrebi Arabic — abstract ancestor node for Moroccan, "
            "Algerian, Tunisian, Libyan, and Hassaniya Arabic. "
            "Key shared Maghrebi features: vowel reduction/deletion; "
            "ث → /t/; ذ → /d/; ق → /q/ preserved; Berber substrate "
            "reinforcing pharyngeals and emphatics."
        ),
    ),

    "ar-x-peninsular": LanguageSpec(
        code="ar-x-peninsular",
        name="Proto-Peninsular Arabic",
        family="Semitic",
        script="Arabic",
        graphemes=GRAPHEMES_PENINSULAR_BASE,
        allophones=ALLOPHONES_PENINSULAR_BASE,
        parent="arb",
        ancestors=(
            Ancestor("arb", P, 0.95, "Descent from Classical Arabic"),
        ),
        notes=(
            "Proto-Peninsular Arabic — abstract ancestor node for Hejazi, "
            "Najdi, Gulf, Yemeni, and Omani Arabic. "
            "Key shared peninsular features: interdentals often preserved; "
            "ق → /q/ or /ɡ/ (Bedouin); conservative consonant system."
        ),
    ),
}
