"""Persian dialects — Tehran (standard), regional Iranian varieties, Dari, Tajik.

Modern Persian (New Persian / Fārsī) has three principal standard forms:
  1. Iranian Persian (fa / fa-IR)  — Tehran standard; official in Iran
  2. Dari (fa-AF)                  — Afghanistan; closer to Classical Persian
  3. Tajik (tg)                    — Tajikistan; Cyrillic script

Plus a rich landscape of regional dialects within Iran:
  fa-x-tehran      Standard Tehran (the base)
  fa-x-isfahani    Isfahani / Central dialect
  fa-x-shirazi     Shirazi / Fars province dialect
  fa-x-kermani     Kermani / Southern dialect
  fa-x-khorasani   Khorasani / Eastern dialect (conservative)
  fa-x-yazdi       Yazdi / Central plateau dialect
  fa-x-mashhadi    Mashhadi / second-city standard variety

Sources:
- Windfuhr, G. ed. (2009). *The Iranian Languages*. Routledge.
- Majidi, M.-R. & Ternes, E. (1999). "Persian (Farsi)." JIPA 29(2), 97–99.
- Bijankhan, M. (2018). *Persian Phonology*. IHCS.
- Mahootian, S. (1997). *Persian*. Routledge. [Descriptive grammar]
- Lazard, G. (1992). *A Grammar of Contemporary Persian*. Mazda.
- Windfuhr, G. (1979). *Persian Grammar*. Mouton.
- Karimi, S. (2005). *A Minimalist Approach to Scrambling*. Mouton. [Tehran]
- Perry, J. (2005). *A Tajik Persian Reference Grammar*. Brill.
  [THE reference for Tajik]
- Kieffer, C. (2009). "Afghan Persian, Dari." In: Windfuhr (2009).
- Hallberg, D.G. (1992). *Sociolinguistic Survey of Northern Pakistan 4*.
  [Dari/Afghan Persian data]
- Yar-Shater, E. (1974). "The classification of Iranian dialects." In:
  *Dr. J.M. Unvala Memorial Volume*. [Regional classification]
- Paul, L. (2009). "Zazaki." In: Windfuhr (2009).
- Windfuhr, G. (1987). "Isoglosses: A Sketch on Persians and Medes,
  Ancient and Modern." Acta Iranica 25.
- Lazard, G. (1963). *La langue des plus anciens monuments de la prose
  persane*. Klincksieck. [Classical reference]
"""

from orthography2ipa.languages.fa import GRAPHEMES, ALLOPHONES
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
AD = AncestorRole.ADSTRATE
SUP = AncestorRole.SUPERSTRATE

# ══════════════════════════════════════════════════════════════════════════
# TEHRAN PERSIAN — the national standard
# ══════════════════════════════════════════════════════════════════════════
#
# MODERN PERSIAN VOWEL SYSTEM (Tehran):
#
# Classical Persian had 6 quality + length distinctions:
#   Long:  ā [aː], ē [eː], ī [iː], ō [oː], ū [uː]
#   Short: a, i, u
#
# Modern Tehran Persian has COLLAPSED to 6 MONOPHTHONG QUALITIES
# (no contrastive length in the original Classical sense):
#   ɒː  (< Classical ā)  — low back long
#   æ   (< Classical a)  — low front short
#   e   (< Classical ē + i merge)  — mid front
#   o   (< Classical ō + u merge)  — mid back
#   i   (< Classical ī)  — high front
#   u   (< Classical ū)  — high back
#
# This is the "vowel shift" (čarxeš-e sadāʾi) — the most discussed feature
# of Tehran Persian vs. Classical/Dari/Tajik.
#
# CONSONANTS (Tehran):
#   - /q/ → [ɢ] or [ɣ] (uvular; NOT lost as in Levantine Arabic)
#     Actually in Tehran, /q/ and /ɣ/ have merged in many speakers:
#     Arabic ق and Arabic غ both → [ɣ] or [ɢ] depending on environment
#   - /ʔ/ (hamza) weakened; often dropped
#   - /ħ/ → /h/ (Arabic ح merged with ه)
#   - /r/ → [ɾ] (tap) in most positions; [r] (trill) emphatic/geminate
#   - Aspiration: voiceless stops aspirated [pʰ tʰ kʰ] in onset
#   - No emphatic consonants (Arabic emphatics in loanwords assimilated)

# Tehran grapheme layer — inherits from fa.py and refines
GRAPHEMES_TEHRAN = {
    **GRAPHEMES,  # base from fa.py (MSA-script Persian)
    # Explicit Tehran phonemic values for the 6-vowel system
    # (already set correctly in fa.py; listed here for documentation)
    # ā → ɒː (low back long — Tehran's distinctive vowel)
    "آ": ["ʔɒː"],
    "ا": ["ʔ", "ɒː"],
    # و can be /v/ (consonantal) or /ow/ diphthong (archaic) or /uː/
    "و": ["v", "uː", "ow"],
}

ALLOPHONES_TEHRAN = {
    **ALLOPHONES,
    # Aspirated stops (Tehran feature — clearly aspirated in onset)
    "p": ["p", "pʰ"],
    "t": ["t", "tʰ"],
    "k": ["k", "kʰ"],
    # q/ɣ merger
    "q": ["ɣ", "ɢ"],
    "ɣ": ["ɣ", "ɢ"],
    # ʔ weakened
    "ʔ": ["ʔ", "∅"],
    # r as tap (trill only emphatic/geminate)
    "ɾ": ["ɾ", "r"],
    # Vowels — the Tehran 6-vowel system
    "ɒː": ["ɒː"],
    "æ": ["æ"],
    "e": ["e"],
    "o": ["o"],
    "iː": ["iː"],
    "uː": ["uː"],
    # Short i, u (in unstressed syllables)
    "i": ["i", "e"],
    "u": ["u", "o"],
}

# ══════════════════════════════════════════════════════════════════════════
# ISFAHANI PERSIAN (fa-x-isfahani)
# ══════════════════════════════════════════════════════════════════════════
#
# Isfahan (Eṣfahān) was the Safavid capital (1598–1722) and remains
# Iran's third city. Isfahani Persian is central-western Iranian and
# shares much with Tehran but has distinct phonological features:
#
#   1. SHORT VOWELS: /æ/ and /e/ may be less clearly distinguished
#      than in Tehran; some raising of /æ/ → [ɛ] before nasals
#   2. /q/ → [ɣ] with some uvular [ɢ] in formal speech (similar to Tehran)
#   3. CODA CONSONANTS: final consonants more clearly articulated than Tehran
#   4. /ɒː/ maintained similarly to Tehran
#   5. Some conservative features vs. Tehran: slightly less reduction of
#      unstressed vowels

GRAPHEMES_ISFAHANI = {**GRAPHEMES_TEHRAN}  # same grapheme set as Tehran

ALLOPHONES_ISFAHANI = {
    **ALLOPHONES_TEHRAN,
    # Slightly less vowel reduction than Tehran
    "æ": ["æ", "ɛ"],  # /æ/ → [ɛ] before nasals
    "e": ["e"],
    # Uvular articulation somewhat more robust than Tehran
    "q": ["ɢ", "ɣ"],
}

# ══════════════════════════════════════════════════════════════════════════
# SHIRAZI PERSIAN (fa-x-shirazi)  — Fars province
# ══════════════════════════════════════════════════════════════════════════
#
# Shiraz (Šīrāz) is the center of Fars province — the heartland of Persian
# civilisation (Persepolis, Pasargadae). Shirazi has historically been
# considered the most "refined" Persian dialect (e.g. Hafez, Saadi wrote here).
#
# DISTINCTIVE SHIRAZI FEATURES:
#   1. /ɒː/ → [ɔː] (slightly higher/rounder than Tehran)
#   2. /æ/ → [a] in many environments (lower, less front than Tehran)
#      This is the main Shirazi isogloss: "kam" [kam] where Tehran has [kæm]
#   3. Some preservation of the Classical /e/ vs /æ/ distinction
#   4. Word-final unstressed vowels more clearly pronounced than Tehran
#   5. Some IMĀLA: raising of /a/ → /e/ near front consonants (Arabic-inherited
#      feature, retained in Shirazi more than Tehran)

GRAPHEMES_SHIRAZI = {**GRAPHEMES_TEHRAN}

ALLOPHONES_SHIRAZI = {
    **ALLOPHONES_TEHRAN,
    # Key Shirazi feature: æ → a
    "æ": ["a", "æ"],  # [a] is primary; Tehran has [æ]
    "ɒː": ["ɔː", "ɒː"],  # slightly higher/rounder
    # Imāla: some vowel raising near front consonants
    "a": ["a", "e"],  # imāla in some contexts
}

# ══════════════════════════════════════════════════════════════════════════
# KERMANI PERSIAN (fa-x-kermani)  — Southern/southeastern dialect
# ══════════════════════════════════════════════════════════════════════════
#
# Kerman is a southern Iranian city with a distinctive dialect cluster.
# Kermani Persian is considered somewhat divergent from Tehran standard.
#
# DISTINCTIVE KERMANI FEATURES:
#   1. SHORT /a/ maintained as [a] (like Shirazi, not [æ])
#   2. /o/ vowel often raised or realised differently
#   3. Some word-final vowel differences
#   4. Conservative: some maintenance of Classical vowel distinctions
#   5. Contact with Balochi and regional languages (southeastern Iran)
#   6. /q/ → [q] maintained in some conservative educated speech
#      (more than Tehran where q → ɣ completely)

GRAPHEMES_KERMANI = {**GRAPHEMES_TEHRAN}

ALLOPHONES_KERMANI = {
    **ALLOPHONES_TEHRAN,
    "æ": ["a", "æ"],  # /a/ more open/back than Tehran (Shirazi-type)
    "ɒː": ["ɒː", "aː"],
    "q": ["q", "ɣ"],  # /q/ retained more than Tehran
    "o": ["o", "u"],  # /o/ sometimes raised toward [u]
}

# ══════════════════════════════════════════════════════════════════════════
# KHORASANI PERSIAN (fa-x-khorasani)  — Eastern/conservative dialect
# ══════════════════════════════════════════════════════════════════════════
#
# Khorasan (Xorāsān) is the northeastern region of Iran, bordering
# Afghanistan and Turkmenistan. Mashhad is its capital (Iran's second
# most populous city).
#
# Khorasani Persian is PHONOLOGICALLY CONSERVATIVE relative to Tehran.
# It forms the geographic and historical bridge to Dari (Afghan Persian).
#
# DISTINCTIVE KHORASANI FEATURES:
#   1. VOWEL SYSTEM: More conservative than Tehran.
#      Classical /æ/ (short a) is often [a] (not fronted to [æ])
#      Classical /ē/ ~ /e/ and /ō/ ~ /o/ better preserved
#   2. /q/ → [q] MORE PRESERVED (less merger with ɣ than in Tehran)
#   3. Some preservation of Classical long/short vowel distinctions
#   4. /ɾ/ vs. /r/: trill [r] more prominent in emphatic positions
#   5. Transition zone to Dari: some Khorasani features overlap with
#      Afghan Persian (Dari)
#   6. Turkic (Uzbek, Turkmen) contact: some loanwords with /ŋ/

GRAPHEMES_KHORASANI = {
    **GRAPHEMES_TEHRAN,
    # More conservative: some Classical vowels reflected
}

ALLOPHONES_KHORASANI = {
    **ALLOPHONES_TEHRAN,
    "æ": ["a", "æ"],  # more open [a] than Tehran [æ]
    "ɒː": ["aː", "ɒː"],  # long ā more open/front (closer to Classical)
    "q": ["q", "ɣ"],  # /q/ maintained more robustly
    "ɾ": ["ɾ", "r"],  # trill [r] more prominent
    "n": ["n", "ŋ"],  # /ŋ/ in some Turkic loanwords
}

# ══════════════════════════════════════════════════════════════════════════
# YAZDI PERSIAN (fa-x-yazdi)  — Central plateau dialect
# ══════════════════════════════════════════════════════════════════════════
#
# Yazd (Yazd / Yezd) is a central Iranian city famous for its Zoroastrian
# community. Yazdi Persian has several conservative/archaic features.
#
# DISTINCTIVE YAZDI FEATURES:
#   1. Some Zoroastrian Dari influence (the liturgical/community language
#      of Yazdi Zoroastrians) — a different "Dari" from Afghan Dari,
#      this is the Persian of Zoroastrian communities in Yazd and Kerman
#   2. Short /a/ realized as [a] (not fronted to [æ] as in Tehran)
#   3. Some archaic vocabulary preserved
#   4. /q/ maintained in some older/conservative speakers

GRAPHEMES_YAZDI = {**GRAPHEMES_TEHRAN}

ALLOPHONES_YAZDI = {
    **ALLOPHONES_TEHRAN,
    "æ": ["a", "æ"],
    "q": ["q", "ɣ"],
    "ɒː": ["aː", "ɒː"],  # more open, slightly front
}

# ══════════════════════════════════════════════════════════════════════════
# MASHHADI PERSIAN (fa-x-mashhadi)
# ══════════════════════════════════════════════════════════════════════════
#
# Mashhad (Mašhad) is Iran's second largest city and the capital of Khorasan.
# Its dialect is the urban variety of Khorasani Persian and is considered
# a prestige variety in northeastern Iran.
#
# Mashhadi is the most studied Khorasani variety and forms the reference
# for northeastern Iranian Persian.
#
# DISTINCTIVE MASHHADI FEATURES:
#   1. More conservative vowels than Tehran (Khorasani base)
#   2. /q/ maintained as [q] in careful speech
#   3. Some imāla: /ɒː/ → [eː] in certain environments
#   4. Religious vocabulary from Arabic well-preserved (pilgrimage city)

GRAPHEMES_MASHHADI = {**GRAPHEMES_KHORASANI}

ALLOPHONES_MASHHADI = {
    **ALLOPHONES_KHORASANI,
    "ɒː": ["aː", "eː", "ɒː"],  # imāla in some formal/religious vocabulary
    "q": ["q", "ɣ"],
}

# ══════════════════════════════════════════════════════════════════════════
# DARI — Afghan Persian (fa-AF)
# ══════════════════════════════════════════════════════════════════════════
#
# Dari (دری) is the Persian of Afghanistan, one of two official languages
# alongside Pashto. It is called "Dari" (دری, "of the court") and is
# functionally the lingua franca of Afghanistan.
#
# Dari is often considered MORE CONSERVATIVE than Iranian Persian because:
#   1. It largely PRESERVES the Classical 6-vowel system
#   2. Vowel shift (Tehran: ā→ɒː, a→æ) did NOT happen in Dari
#   3. Long/short vowel distinction maintained better
#   4. Some Classical consonant distinctions preserved
#
# THE DARI VOWEL SYSTEM (vs. Tehran):
#
#   Classical/Dari         Tehran Persian
#   ──────────────────     ───────────────
#   ā [aː]                 → ɒː (backed and lowered)
#   a [a]                  → æ (fronted)
#   ē [eː] → e [e]         → e (shortened; same quality)
#   ō [oː] → o [o]         → o (shortened; same quality)
#   ī [iː]                 → iː (unchanged)
#   ū [uː]                 → uː (unchanged)
#
# OTHER DARI FEATURES:
#   - /q/ → [q] MAINTAINED (uvular; not merged with ɣ as in Tehran)
#   - /ʕ/ (Arabic ع) maintained as [ʕ] in Arabic loanwords (more carefully
#     than Tehran where ʕ → ʔ or ∅)
#   - /ħ/ (Arabic ح) maintained as [ħ] in careful speech (vs. Tehran h)
#   - Word-final consonants more clearly articulated than Tehran
#   - Less aspiration of voiceless stops than Tehran
#   - Pashto and Turkic (Uzbek, Hazaragi) contact influence
#
# Hazaragi (a Dari dialect of Hazara people) has Mongolian substrate features:
#   - uvular consonants more prominent
#   - Some Mongolian loanwords

GRAPHEMES_DARI = {
    **GRAPHEMES,  # base Persian graphemes
    # Dari maintains Classical vowel values
    # Long ā as [aː] (not [ɒː] as in Tehran)
    "آ": ["ʔaː"],
    "ا": ["ʔ", "aː"],
    # و : consonantal v or long ū (no 'ow' diphthong in Dari)
    "و": ["v", "uː"],
    # Arabic consonants maintained more carefully in Dari loanwords
    "ع": ["ʕ", "ʔ"],  # pharyngeal maintained (→ ʔ colloquially)
    "ح": ["ħ", "h"],  # pharyngeal maintained in careful speech
    "ق": ["q"],  # uvular stop preserved
}

ALLOPHONES_DARI = {
    **ALLOPHONES,
    # Stops — less aspirated than Tehran
    "p": ["p", "pʰ"],  # aspiration less prominent than Tehran
    "t": ["t", "tʰ"],
    "k": ["k", "kʰ"],
    # /q/ preserved as uvular
    "q": ["q"],
    # Pharyngeals maintained more than Tehran
    "ʕ": ["ʕ", "ʔ"],
    "ħ": ["ħ", "h"],
    # /r/ as tap (same as Tehran)
    "ɾ": ["ɾ", "r"],
    # DARI VOWELS — Classical system (no Tehran vowel shift)
    "aː": ["aː"],  # long ā as [aː] — NOT backed to [ɒː]
    "a": ["a"],  # short a as [a] — NOT fronted to [æ]
    "e": ["e"],
    "o": ["o"],
    "iː": ["iː"],
    "uː": ["uː"],
    # No ɒː or æ as primary phonemes in Dari
    "ɒː": ["aː"],  # if needed for Arabic loans: → aː
    "æ": ["a"],
    # Nasals
    "n": ["n", "m", "ŋ"],
    "m": ["m"],
}

# ══════════════════════════════════════════════════════════════════════════
# HAZARAGI DARI (fa-x-hazaragi)
# ══════════════════════════════════════════════════════════════════════════
#
# Hazaragi is the Persian/Dari dialect of the Hazara people of central
# Afghanistan (Hazarajat). The Hazara are descended from Mongol-Turkic
# settlers (~13th c. CE) who adopted Dari as their language but retained
# significant Mongolian substrate features.
#
# DISTINCTIVE HAZARAGI FEATURES:
#   1. Mongolian/Turkic substrate: uvular and velar consonants prominent
#   2. /q/ maintained as [q] or even strengthened
#   3. Some vowel differences from standard Kabul Dari
#   4. Specific Mongolian loanwords
#   5. /ŋ/ as phoneme (from Mongolian/Turkic)

GRAPHEMES_HAZARAGI = {**GRAPHEMES_DARI}

ALLOPHONES_HAZARAGI = {
    **ALLOPHONES_DARI,
    "q": ["q", "ɢ"],  # uvular maintained and possibly strengthened
    "n": ["n", "ŋ"],
    "ŋ": ["ŋ"],  # phonemic in Mongolian loanwords
    "ɣ": ["ɣ", "ɢ"],
}

# ══════════════════════════════════════════════════════════════════════════
# TAJIK (tg)  — Tajikistan Persian (Cyrillic script)
# ══════════════════════════════════════════════════════════════════════════
#
# Tajik (Тоҷикӣ / Tojikī) is the Persian of Tajikistan and parts of
# Uzbekistan and Afghanistan. It is the most diverged of the three main
# Persian standard forms due to:
#   1. Cyrillic script (since Soviet era ~1939)
#   2. Russian superstrate (Soviet period 1929–1991)
#   3. Uzbek/Turkic substrate (geographic immersion in Turkic area)
#   4. Some conservative phonological features (like Dari)
#   5. Some innovative features not seen in Iranian Persian or Dari
#
# PHONOLOGICAL PROFILE:
#   - Vowel system: 6 qualities (similar to Dari), written in Cyrillic
#   - /i/ and /u/ maintained (not reduced as in Tehran)
#   - /q/ → [q] maintained (like Dari; more strongly than Tehran)
#   - UVULAR vowel /ʊ/ in some words (Russian/Uzbek influence)
#   - Final -i suffix as /ī/ (preserved from Classical)
#   - /tʃ/ affricate strong (Tajik has a robust affricate)
#   - Uzbek/Turkic influence: /ŋ/ phoneme in Turkic loanwords
#   - Russian loanwords: /p/, /v/, /f/ reinforced; /ts/, /ʒ/ established
#   - Word-final consonant clusters from Russian loanwords
#
# Script: Cyrillic (with special letters Ӣ ī, Ӯ ū, Ҳ h, Ҷ dʒ, Қ q, Ғ ɣ)
# We use romanization here for IPA mapping.

GRAPHEMES_TAJIK = {
    # ── Cyrillic → Latin romanization → IPA ──────────────────────────────
    # This represents the PHONEMIC values in Tajik Cyrillic

    # Stops
    "б": ["b"],
    "п": ["p"],
    "т": ["t"],
    "д": ["d"],
    "к": ["k"],
    "г": ["ɡ"],
    "қ": ["q"],  # Қ: uvular stop — maintained as [q]
    "ъ": ["ʔ"],  # hard sign: glottal stop in Arabic loanwords

    # Fricatives
    "ф": ["f"],
    "в": ["v"],
    "с": ["s"],
    "з": ["z"],
    "ш": ["ʃ"],
    "ж": ["ʒ"],
    "х": ["x"],
    "ғ": ["ɣ"],  # Ғ: voiced velar fricative
    "ҳ": ["h"],  # Ҳ: glottal fricative (Arabic ه and ح)

    # Affricates
    "ч": ["tʃ"],
    "ҷ": ["dʒ"],  # Ҷ: voiced affricate

    # Nasals
    "м": ["m"],
    "н": ["n"],
    "нг": ["ŋ"],  # /ŋ/ in Turkic loanwords

    # Liquids
    "л": ["l"],
    "р": ["r", "ɾ"],

    # Glides
    "й": ["j"],

    # ── Vowels (Tajik 6-vowel system in Cyrillic) ─────────────────────────
    "а": ["a"],  # short a (Tajik [a], not fronted like Tehran)
    "о": ["o"],  # /o/ (Classical ō preserved)
    "е": ["e"],  # /e/ (Classical ē preserved)
    "и": ["i"],  # short i
    "у": ["u"],  # short u
    "ӣ": ["iː"],  # Ӣ: long ī
    "ӯ": ["uː"],  # Ӯ: long ū
    "ӯ": ["uː"],

    # Russian loanword vowels
    "э": ["e"],
    "ю": ["ju"],
    "я": ["ja"],
    "ё": ["jo"],
}

ALLOPHONES_TAJIK = {
    "b": ["b"], "p": ["p", "pʰ"],
    "t": ["t", "tʰ"], "d": ["d"],
    "k": ["k", "kʰ"], "ɡ": ["ɡ"],
    "q": ["q"],  # uvular maintained
    "ʔ": ["ʔ", "∅"],
    "f": ["f"], "v": ["v"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "x": ["x"], "ɣ": ["ɣ"],
    "h": ["h"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ"],
    # Uzbek/Russian: /ts/ in loanwords
    "ts": ["ts"],
    "m": ["m"], "n": ["n", "ŋ"],
    "ŋ": ["ŋ"],  # phonemic in Turkic loanwords
    "l": ["l"],
    "r": ["r", "ɾ"],
    "j": ["j"],
    # Tajik vowels — Conservative (no Tehran vowel shift)
    "a": ["a"],
    "o": ["o"],
    "e": ["e"],
    "i": ["i"],
    "u": ["u"],
    "iː": ["iː"],
    "uː": ["uː"],
}

# ══════════════════════════════════════════════════════════════════════════
# SPECS
# ══════════════════════════════════════════════════════════════════════════

SPECS = {
    "fa-x-tehran": LanguageSpec(
        code="fa-x-tehran",
        name="Tehran Persian (Standard Iranian)",
        family="Iranian",
        script="Arabic",
        graphemes=GRAPHEMES_TEHRAN,
        allophones=ALLOPHONES_TEHRAN,
        parent="fa",
        ancestors=(
            Ancestor("fa-x-early", P, 0.90,
                     "New Persian descent; Tehran dialect became standard ~19th c."),
            Ancestor("ar", AD, 0.08,
                     "Arabic adstrate: 40–50% of formal vocabulary; "
                     "consonants θ/ð/ħ/ʕ/q assimilated phonologically"),
        ),
        notes=(
            "Tehran Standard Persian — the national standard of Iran. "
            "DEFINING VOWEL SHIFT (vs. Classical/Dari/Tajik): "
            "Classical ā [aː] → Tehran [ɒː] (backed); "
            "Classical a → [æ] (fronted). "
            "6-VOWEL SYSTEM: ɒː, æ, e, o, iː, uː (no contrastive length). "
            "Voiceless stops aspirated [pʰ tʰ kʰ] in onset. "
            "q/ɣ merger: Arabic ق and غ both → [ɣ] or [ɢ]. "
            "ħ → h (pharyngeal lost); ʕ → ʔ (often deleted). "
            "r → [ɾ] tap in most positions."
        ),
    ),

    "fa-x-isfahani": LanguageSpec(
        code="fa-x-isfahani",
        name="Isfahani Persian",
        family="Iranian",
        script="Arabic",
        graphemes=GRAPHEMES_ISFAHANI,
        allophones=ALLOPHONES_ISFAHANI,
        parent="fa-x-tehran",
        ancestors=(
            Ancestor("fa-x-early", P, 0.88, "New Persian descent"),
        ),
        notes=(
            "Isfahani Persian (Eṣfahānī). Isfahan — former Safavid capital. "
            "Similar to Tehran but: "
            "/æ/ → [ɛ] before nasals; uvular [ɢ] somewhat more frequent; "
            "slightly less vowel reduction of unstressed syllables. "
            "Historically considered a prestige variety alongside Tehran."
        ),
    ),

    "fa-x-shirazi": LanguageSpec(
        code="fa-x-shirazi",
        name="Shirazi Persian",
        family="Iranian",
        script="Arabic",
        graphemes=GRAPHEMES_SHIRAZI,
        allophones=ALLOPHONES_SHIRAZI,
        parent="fa-x-tehran",
        ancestors=(
            Ancestor("fa-x-early", P, 0.88, "New Persian descent"),
        ),
        notes=(
            "Shirazi Persian (Šīrāzī). Shiraz — Fars province; "
            "homeland of Hafez and Saadi. "
            "KEY ISOGLOSS: /æ/ → [a] (short a lower and less fronted than Tehran). "
            "ā → [ɔː] (slightly higher/rounder than Tehran's [ɒː]). "
            "Historically regarded as the 'purest' Persian dialect. "
            "Some imāla (vowel raising) in Classical vocabulary."
        ),
    ),

    "fa-x-kermani": LanguageSpec(
        code="fa-x-kermani",
        name="Kermani Persian",
        family="Iranian",
        script="Arabic",
        graphemes=GRAPHEMES_KERMANI,
        allophones=ALLOPHONES_KERMANI,
        parent="fa-x-tehran",
        ancestors=(
            Ancestor("fa-x-early", P, 0.85, "New Persian descent"),
        ),
        notes=(
            "Kermani Persian (Kermānī). Southern Iranian; Kerman province. "
            "/æ/ → [a] (more open/back than Tehran; similar to Shirazi). "
            "/q/ somewhat more maintained than Tehran. "
            "Contact with Balochi (southeastern Iran): minor phonological effects. "
            "Zoroastrian community in Kerman shares some features with Yazdi."
        ),
    ),

    "fa-x-khorasani": LanguageSpec(
        code="fa-x-khorasani",
        name="Khorasani Persian",
        family="Iranian",
        script="Arabic",
        graphemes=GRAPHEMES_KHORASANI,
        allophones=ALLOPHONES_KHORASANI,
        parent="fa-x-tehran",
        ancestors=(
            Ancestor("fa-x-early", P, 0.88, "New Persian; Khorasan is its cradle"),
            Ancestor("tg", AD, 0.05,
                     "Tajik adstrate: geographic continuum; "
                     "Uzbek/Turkmen contact words"),
        ),
        notes=(
            "Khorasani Persian (Xorāsānī). Northeastern Iran — the historical "
            "cradle of New Persian literature (Ferdowsi's Shahnameh). "
            "CONSERVATIVE: /a/ → [a] (not fronted to [æ] as in Tehran); "
            "ā → [aː] (not backed to [ɒː]); "
            "/q/ maintained more robustly than Tehran. "
            "Geographic bridge to Dari (Afghan Persian). "
            "Turkic (Uzbek, Turkmen) contact: /ŋ/ in loanwords."
        ),
    ),

    "fa-x-yazdi": LanguageSpec(
        code="fa-x-yazdi",
        name="Yazdi Persian",
        family="Iranian",
        script="Arabic",
        graphemes=GRAPHEMES_YAZDI,
        allophones=ALLOPHONES_YAZDI,
        parent="fa-x-tehran",
        ancestors=(
            Ancestor("fa-x-tehran", AD, 0.82, "Tehran standard base"),
        ),
        notes=(
            "Yazdi Persian (Yazdī). Yazd — central Iranian plateau. "
            "Zoroastrian heartland; some archaic features in Zoroastrian "
            "community speech ('Dari' of Zoroastrians — not Afghan Dari). "
            "/æ/ → [a] (conservative, like Shirazi/Kermani). "
            "/q/ somewhat preserved in older/conservative speech."
        ),
    ),

    "fa-x-mashhadi": LanguageSpec(
        code="fa-x-mashhadi",
        name="Mashhadi Persian",
        family="Iranian",
        script="Arabic",
        graphemes=GRAPHEMES_MASHHADI,
        allophones=ALLOPHONES_MASHHADI,
        parent="fa-x-khorasani",
        ancestors=(
            Ancestor("fa-x-khorasani", P, 0.88, "Khorasani base"),
        ),
        notes=(
            "Mashhadi Persian (Mašhadī). Iran's second-largest city; "
            "capital of Khorasan. Urban Khorasani variety; prestige dialect "
            "of northeastern Iran. "
            "Conservative vowels (Khorasani base); some imāla in religious/Arabic "
            "vocabulary (pilgrimage city: shrine of Imam Reza). "
            "/q/ maintained in careful speech."
        ),
    ),

    "fa-AF": LanguageSpec(
        code="fa-AF",
        name="Dari (Afghan Persian)",
        family="Iranian",
        script="Arabic",
        graphemes=GRAPHEMES_DARI,
        allophones=ALLOPHONES_DARI,
        parent="fa",
        ancestors=(
            Ancestor("fa-x-early", P, 0.92,
                     "Classical New Persian — Dari is the most conservative major variety"),
            Ancestor("ps", AD, 0.05,
                     "Pashto adstrate: some phonological and lexical influence"),
        ),
        notes=(
            "Dari (دری) — Afghan Persian; official language of Afghanistan. "
            "CONSERVATIVE VOWEL SYSTEM: retains Classical values; "
            "NO Tehran vowel shift (ā = [aː] not [ɒː]; a = [a] not [æ]). "
            "/q/ → [q] maintained as uvular (not merged with ɣ). "
            "/ħ/ → [ħ] maintained in careful speech (Arabic ح). "
            "/ʕ/ → [ʕ] maintained in Arabic loanwords (more than Tehran). "
            "Pashto adstrate: some retroflex-influenced articulation in some speakers. "
            "Hazaragi variety (Hazara people): Mongolian substrate (see fa-x-hazaragi). "
            "Kabul Dari is the prestige/media standard."
        ),
    ),

    "fa-x-hazaragi": LanguageSpec(
        code="fa-x-hazaragi",
        name="Hazaragi (Afghan Dari, Hazara)",
        family="Iranian",
        script="Arabic",
        graphemes=GRAPHEMES_HAZARAGI,
        allophones=ALLOPHONES_HAZARAGI,
        parent="fa-AF",
        ancestors=(
            Ancestor("fa-AF", P, 0.80, "Dari base"),
        ),
        notes=(
            "Hazaragi (هزارگی). Dari dialect of Hazara people of "
            "central Afghanistan (Hazarajat). "
            "Hazara descend from Mongol-Turkic settlers (~13th c. CE) "
            "who adopted Dari but retain Mongolian substrate features. "
            "/q/ and /ɢ/ prominent; /ŋ/ phonemic in Mongolian loanwords. "
            "Some uvular vowel features. "
            "Spoken by ~2–3 million people; large diaspora in Iran, Pakistan, "
            "and internationally."
        ),
    ),

    "tg": LanguageSpec(
        code="tg",
        name="Tajik",
        family="Iranian",
        script="Cyrillic",
        graphemes=GRAPHEMES_TAJIK,
        allophones=ALLOPHONES_TAJIK,
        parent="fa",
        ancestors=(
            Ancestor("fa-x-early", P, 0.85,
                     "Classical New Persian base; Tajik most conservative in vowels"),
            Ancestor("ru", SUP, 0.08,
                     "Russian superstrate (Soviet period 1929–1991): "
                     "Cyrillic script imposed; Russian loanwords; "
                     "/ts/, /ʒ/ reinforced; consonant clusters from loans"),
        ),
        notes=(
            "Tajik (Тоҷикӣ / Tojikī). Official language of Tajikistan. "
            "Persian with Cyrillic script (since ~1939, Soviet era). "
            "CONSERVATIVE VOWELS: No Tehran vowel shift; a=[a], ā=[aː]. "
            "/q/ → [q] maintained (like Dari; more than Tehran). "
            "DISTINCTIVE: Cyrillic script with special letters "
            "(Ӣ=ī, Ӯ=ū, Қ=q, Ғ=ɣ, Ҷ=dʒ, Ҳ=h). "
            "Uzbek/Turkic substrate: /ŋ/ phoneme in Turkic loanwords; "
            "uvular consonants reinforced. "
            "Russian superstrate: loanwords with initial consonant clusters "
            "unusual in native Persian (school/škola → Tg. maktab but also "
            "borrowed terms). /ts/ established from Russian loans. "
            "Perry (2005) is the primary reference grammar."
        ),
    ),
}
