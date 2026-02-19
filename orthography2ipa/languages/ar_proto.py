"""Proto-Semitic, Proto-West-Semitic, Proto-Central-Semitic, Proto-Arabic.

Reconstructed phonological systems tracing the branch from the ancestral
Semitic family through to the immediate pre-Classical Arabic stage.

──────────────────────────────────────────────────────────────────────────────
Genealogical chain (approximate dates are highly contested):
  Proto-Semitic (sem)            ~5000–4000 BCE  (Afroasiatic daughter)
       ↓
  Proto-West-Semitic (sem-x-west) ~3500 BCE      (excl. East Sem./Akkadian)
       ↓
  Proto-Central-Semitic (sem-x-central) ~2500 BCE (excl. Ethiopic/South Sem.)
       ↓
  Proto-Arabic (xpa)             ~500 BCE–500 CE (Old North Arabian ancestor)
──────────────────────────────────────────────────────────────────────────────

All grapheme keys use the conventional Semitist romanization (without
leading asterisks). IPA values are best-current reconstructions.

Sources:
- Lipiński, E. (2001). *Semitic Languages: Outline of a Comparative Grammar*.
  2nd ed. Peeters. [Primary reference for consonant inventory]
- Huehnergard, J. (2019). "Proto-Semitic Language and Culture." In:
  *The Semitic Languages*. 2nd ed. Routledge. pp. 49–79.
- Faber, A. (1997). "Genetic Subgrouping of the Semitic Languages." In:
  *The Semitic Languages*. Routledge.
- Dolgopolsky, A. (1999). "Emphatic Consonants in Semitic." Folia Ling. Hist.
- Kienast, B. (2001). *Historische Semitische Sprachwissenschaft*. Harrassowitz.
- Versteegh, K. (2014). *The Arabic Language*. 2nd ed. Edinburgh UP. Ch. 1–3.
- Owens, J. (2006). *A Linguistic History of Arabic*. OUP. Ch. 1–4.
- Al-Jallad, A. (2015). *An Outline of the Grammar of the Safaitic Inscriptions*.
  Brill. [Evidence for Old Arabic consonantism]
- Macdonald, M.C.A. (2000). "Reflections on the linguistic map of pre-Islamic
  Arabia." Arabian Archaeology and Epigraphy 11. [Old North Arabian evidence]
- Cantineau, J. (1960). *Études de linguistique sémitique et arabe*. Mouton.
"""

from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-SEMITIC (sem)  ~5000–4000 BCE
# ═══════════════════════════════════════════════════════════════════════════
#
# The 29-consonant system is the most broadly accepted reconstruction.
# The 29th phoneme (*ṣ́, "emphatic lateral fricative") is the most
# controversial; it is attested as distinct in Akkadian, Arabic, Geez,
# and is reconstructed as /ɬˤ/ or /ɮˤ/ (emphatic voiced lateral fricative).
#
# The lateral fricative *ś (/ɬ/) merged differently across daughters:
#   Hebrew:  *ś → /ʃ/ (shin שׁ) in most forms
#   Arabic:  *ś → /s/ (sīn س) in most environments; → /ʃ/ only in شِمس
#   Akkadian: *ś → /ʃ/
#   Ethiopic: *ś → /s/
#
# Emphatics: The "pharyngealisation" theory (Jakobson) treats emphatics as
# [+RTR] (retracted tongue root). The "uvularisation/glottalisation" theory
# (Cantineau, McCarthy) treats them as uvularised or ejective. Most current
# Semitists treat them as pharyngealised [Cˤ]. We follow this convention.
#
# Vowels: Three-vowel quality system (a, i, u) with contrastive length.
# The reconstructed morphology requires these six (3 short + 3 long).

GRAPHEMES_PSEM = {
    # ── STOPS ─────────────────────────────────────────────────────────────
    # Bilabial
    "b": ["b"],
    "p": ["p"],  # *p preserved in most PSem descendants;
    # later shifts to /f/ in Arabic, /p-f/ in Hebrew

    # Dental/alveolar
    "t": ["t"],
    "d": ["d"],
    "ṭ": ["tˤ"],  # emphatic (pharyngealised) t

    # Velar
    "k": ["k"],
    "g": ["ɡ"],  # voiced velar stop; → Arabic /dʒ/ much later

    # Uvular
    "q": ["q"],  # uvular stop; reconstructed as emphatic velar
    # by some scholars (*kˤ), but uvular by others

    # Glottal
    "ʾ": ["ʔ"],  # aleph / glottal stop

    # ── INTERDENTALS ──────────────────────────────────────────────────────
    "ṯ": ["θ"],  # voiceless interdental (= Arabic ث, Hebrew שׂ~ś)
    "ḏ": ["ð"],  # voiced interdental (= Arabic ذ)
    "ẓ": ["ðˤ"],  # emphatic interdental (= Arabic ظ)

    # ── SIBILANTS ─────────────────────────────────────────────────────────
    "s": ["s"],  # basic voiceless alveolar (= Arabic س)
    "z": ["z"],  # voiced alveolar (= Arabic ز)
    "ṣ": ["sˤ"],  # emphatic alveolar (= Arabic ص)
    "ś": ["ɬ"],  # voiceless lateral fricative (Welsh "ll")
    # → Arabic /s/ (سـ); Hebrew /ʃ/ (שׁ)
    "š": ["ʃ"],  # postalveolar fricative (= Arabic ش, Akkadian š)

    # ── EMPHATIC LATERAL (the 29th consonant) ─────────────────────────────
    "ṣ́": ["ɬˤ"],  # emphatic lateral fricative — the most debated
    # PSem consonant. → Arabic ض /ðˤ/ (later /dˤ/)
    # → Ethiopic /ṣ/; → Hebrew /ṣ/ (ẓ)
    # Reconstructed as /ɬˤ/, /ɮˤ/, or /dˤ/ by diff. scholars.

    # ── VELARS / UVULARS ──────────────────────────────────────────────────
    "x": ["x"],  # voiceless velar fricative (= Arabic خ)
    "ɣ": ["ɣ"],  # voiced velar fricative (= Arabic غ)

    # ── PHARYNGEALS ───────────────────────────────────────────────────────
    "ḥ": ["ħ"],  # voiceless pharyngeal fricative (= Arabic ح)
    "ʿ": ["ʕ"],  # voiced pharyngeal fricative (= Arabic ع)

    # ── GLOTTAL FRICATIVE ─────────────────────────────────────────────────
    "h": ["h"],

    # ── NASALS ────────────────────────────────────────────────────────────
    "m": ["m"],
    "n": ["n"],

    # ── LIQUIDS ───────────────────────────────────────────────────────────
    "l": ["l"],
    "r": ["r"],

    # ── GLIDES ────────────────────────────────────────────────────────────
    "w": ["w"],
    "y": ["j"],

    # ── VOWELS (reconstructed) ────────────────────────────────────────────
    "a": ["a"],
    "i": ["i"],
    "u": ["u"],
    "ā": ["aː"],
    "ī": ["iː"],
    "ū": ["uː"],
}

ALLOPHONES_PSEM = {
    # Stops — no spirantisation yet (that is a later Canaanite/Hebrew feature)
    "b": ["b"], "p": ["p"],
    "t": ["t"], "d": ["d"], "tˤ": ["tˤ"],
    "k": ["k"], "ɡ": ["ɡ"],
    "q": ["q"],
    "ʔ": ["ʔ"],

    # Emphatics
    "sˤ": ["sˤ"], "tˤ": ["tˤ"], "ðˤ": ["ðˤ"],
    "ɬˤ": ["ɬˤ"],  # emphatic lateral — little allophony reconstructed

    # Fricatives
    "θ": ["θ"], "ð": ["ð"],
    "s": ["s"], "z": ["z"],
    "ɬ": ["ɬ"], "ʃ": ["ʃ"],
    "x": ["x"], "ɣ": ["ɣ"],
    "ħ": ["ħ"], "ʕ": ["ʕ"],
    "h": ["h"],

    # Sonorants
    "m": ["m"], "n": ["n", "m", "ŋ"],  # place assimilation before stops
    "l": ["l"], "r": ["r"],
    "w": ["w"], "j": ["j"],

    # Vowels
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
}

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-WEST-SEMITIC (sem-x-west)  ~3500–3000 BCE
# ═══════════════════════════════════════════════════════════════════════════
#
# West Semitic splits from East Semitic (Akkadian and Eblaite) and forms
# the ancestor of all the surviving Semitic languages except Akkadian.
#
# Proto-West-Semitic (PWS) vs. Proto-Semitic (PSem) innovations:
#   1. Loss of *p-/f distinction in some environments (varies by branch)
#   2. Early drift in emphatic system
#   3. *ś begins merging with *s or *š in some branches
#   4. No morphophonemic spirantisation yet (that is Canaanite)
#
# The consonant inventory is nearly identical to PSem.
# Main changes are morphological / morphophonological.
# We keep the same 29 graphemes but note directional shifts in notes.

GRAPHEMES_PWSEM = {
    **GRAPHEMES_PSEM,
    # Same consonant and vowel inventory as PSem.
    # Differences are mostly morphological and accentual at this stage.
    # The *ś lateral fricative is still distinct from *š and *s here.
}

ALLOPHONES_PWSEM = {
    **ALLOPHONES_PSEM,
}

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-CENTRAL-SEMITIC (sem-x-central)  ~2500–2000 BCE
# ═══════════════════════════════════════════════════════════════════════════
#
# Central Semitic = Arabic + Northwest Semitic (Canaanite + Aramaic).
# It excludes the South Semitic branch (Ethiopic, South Arabian).
#
# KEY INNOVATIONS distinguishing Central Semitic from PWS:
#
#   1. LOSS OF SPIRANTISATION in stops (or, more precisely, spirantisation
#      never occurred — it is a later Canaanite innovation)
#
#   2. *ś /ɬ/ MERGER UNDERWAY:
#      In Proto-Central-Semitic, *ś begins shifting — the evidence from
#      Ugaritic (a conservative member) shows *ś → /s/ in Aramaic/Arabic,
#      and /ʃ/ in Canaanite.
#
#   3. THE DENTAL EMPHATIC SYSTEM: *ṭ /tˤ/, *ṣ /sˤ/, *ẓ /ðˤ/ all preserved.
#      *ṣ́ /ɬˤ/ still present but beginning to shift in some branches.
#
#   4. SHORT VOWEL REDUCTION beginning in unstressed syllables

GRAPHEMES_PCSEM = {
    **GRAPHEMES_PSEM,
    # ś is beginning to lose lateral quality → variant [ɬ~s]
    "ś": ["ɬ", "s"],  # lateral fricative beginning to merge with /s/
    # (completed in Aramaic; partially in Arabic)
    # *ṣ́ beginning to shift — still /ɬˤ/ but trending toward /ðˤ/ or /dˤ/
    "ṣ́": ["ɬˤ", "ðˤ"],
}

ALLOPHONES_PCSEM = {
    **ALLOPHONES_PSEM,
    "ɬ": ["ɬ", "s"],
    "ɬˤ": ["ɬˤ", "ðˤ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-ARABIC (xpa)  ~500 BCE – 500 CE  ("Old Arabic" / Old North Arabian)
# ═══════════════════════════════════════════════════════════════════════════
#
# Proto-Arabic is the reconstructed ancestor of all Arabic dialects,
# attested indirectly through:
#   1. Old North Arabian (ONA) inscriptions: Safaitic, Hismaic, Dadanitic,
#      Taymanitic (~8th c. BCE – 4th c. CE) — show a pre-Classical system
#   2. Classical Arabic phonology and morphology (backward reconstruction)
#   3. Early Arabic loanwords in Akkadian (~8th c. BCE Assyrian records)
#
# KEY INNOVATIONS distinguishing Proto-Arabic from Proto-Central-Semitic:
#
#   1. *p → /f/  [THE DEFINING ARABIC INNOVATION]
#      - Arabic is the only Semitic language where *p became /f/ uniformly.
#      - Hebrew, Aramaic, Ethiopic all preserve /p/ (with later spirantisation).
#      - Examples: PSem *palg- → Ar. falq "to split"; *pay- → fi
#
#   2. *ś /ɬ/ → /s/ (fully merged with *s)
#      - Arabic سِ from both *s and *ś sources
#      - But *š → /ʃ/ preserved separately
#
#   3. *ṣ́ /ɬˤ/ → /ðˤ/ (Arabic ض)
#      - The Arabic ḍāḏ (ض) is the famous reflex of the emphatic lateral
#      - Classical Arabic ض was traditionally pronounced as lateral [ɮˤ]
#        or lateral affricate; modern dialects have dˤ or zˤ
#
#   4. *g /ɡ/ begins shifting → later becomes /dʒ/ in most dialects
#      but evidence suggests Proto-Arabic still had /ɡ/ (ONA inscriptions)
#
#   5. The 28-consonant system of Classical Arabic is nearly established
#      (loss of the lateral *ṣ́ as distinct from ض)
#
#   6. VOWEL SYSTEM: *i, *a, *u (short) and *iː, *aː, *uː (long)
#      plus diphthongs *aj, *aw preserved
#
# Note on "Proto-Arabic" vs. "Old Arabic":
#   Scholars use these terms somewhat differently. Here, "Proto-Arabic"
#   covers the stage immediately before Classical Arabic was codified
#   (~7th century CE). Old North Arabian inscriptions give the best window.

GRAPHEMES_PROTO_AR = {
    # ── STOPS ─────────────────────────────────────────────────────────────
    # *p → f (THE Arabic innovation)
    "f": ["f"],  # < PSem *p; fully fricativized
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "ṭ": ["tˤ"],  # emphatic t (Arabic ط)
    "k": ["k"],
    "g": ["ɡ"],  # still /ɡ/ in Proto-Arabic; → dʒ later in most dialects
    "q": ["q"],  # uvular stop (Arabic ق)
    "ʾ": ["ʔ"],  # glottal stop (Arabic ء/ا)

    # ── INTERDENTALS ──────────────────────────────────────────────────────
    "ṯ": ["θ"],  # (Arabic ث)
    "ḏ": ["ð"],  # (Arabic ذ)
    "ẓ": ["ðˤ"],  # emphatic interdental (Arabic ظ)

    # ── SIBILANTS ─────────────────────────────────────────────────────────
    "s": ["s"],  # Arabic س — from both *s and *ś
    "z": ["z"],  # Arabic ز
    "ṣ": ["sˤ"],  # emphatic s (Arabic ص)
    "š": ["ʃ"],  # Arabic ش

    # ── EMPHATIC LATERAL → Arabic ض ──────────────────────────────────────
    "ḍ": ["ðˤ", "ɮˤ"],  # Arabic ض; reflex of PSem *ṣ́; still partially lateral
    # in Proto-Arabic; Classical Arabic had lateral [ɮˤ];
    # modern dialects: /dˤ/ (Egypt, Levant) or /zˤ/ (others)

    # ── VELARS / UVULARS ──────────────────────────────────────────────────
    "x": ["x"],  # Arabic خ
    "ɣ": ["ɣ"],  # Arabic غ

    # ── PHARYNGEALS ───────────────────────────────────────────────────────
    "ḥ": ["ħ"],  # Arabic ح
    "ʿ": ["ʕ"],  # Arabic ع

    # ── GLOTTAL ───────────────────────────────────────────────────────────
    "h": ["h"],  # Arabic ه

    # ── SONORANTS ─────────────────────────────────────────────────────────
    "m": ["m"],
    "n": ["n"],
    "l": ["l"],
    "r": ["r"],
    "w": ["w"],
    "y": ["j"],

    # ── VOWELS ────────────────────────────────────────────────────────────
    "a": ["a"],
    "i": ["i"],
    "u": ["u"],
    "ā": ["aː"],
    "ī": ["iː"],
    "ū": ["uː"],
    "ay": ["aj"],  # diphthong *aj → Arabic /aj/
    "aw": ["aw"],  # diphthong *aw → Arabic /aw/
}

ALLOPHONES_PROTO_AR = {
    # Stops
    "b": ["b"], "f": ["f"],
    "t": ["t"], "d": ["d"], "tˤ": ["tˤ"],
    "k": ["k"], "ɡ": ["ɡ"],
    "q": ["q"], "ʔ": ["ʔ"],

    # Emphatics
    "sˤ": ["sˤ"],
    "tˤ": ["tˤ"],
    "ðˤ": ["ðˤ"],  # (ظ)
    "ɮˤ": ["ɮˤ", "ðˤ"],  # (ض) — transitional; lateral or emphatic interdental

    # Fricatives
    "θ": ["θ"], "ð": ["ð"],
    "s": ["s"], "z": ["z"], "ʃ": ["ʃ"],
    "x": ["x"], "ɣ": ["ɣ"],
    "ħ": ["ħ"], "ʕ": ["ʕ"],
    "h": ["h"],

    # Sonorants
    "m": ["m"], "n": ["n", "m", "ŋ"],
    "l": ["l"], "r": ["r", "ɾ"],
    "w": ["w"], "j": ["j"],

    # Vowels
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "aj": ["aj"], "aw": ["aw"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SPECS
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "sem": LanguageSpec(
        code="sem",
        name="Proto-Semitic",
        family="Afroasiatic",
        script="Latin",
        graphemes=GRAPHEMES_PSEM,
        allophones=ALLOPHONES_PSEM,
        notes=(
            "Proto-Semitic (~5000–4000 BCE). Reconstructed ancestor of all "
            "Semitic languages. 29-consonant inventory including: "
            "(1) emphatic series /sˤ tˤ ðˤ ɬˤ/; "
            "(2) lateral fricatives /ɬ/ (*ś) and /ɬˤ/ (*ṣ́); "
            "(3) interdentals /θ ð ðˤ/; "
            "(4) pharyngeals /ħ ʕ/; "
            "(5) uvular /q/; (6) bilabial stop /p/ (→ f in Arabic). "
            "Three-vowel system (a, i, u) with contrastive length. "
            "Notation follows Huehnergard (2019) and Lipiński (2001). "
            "Script: romanization (PSem was unwritten)."
        ),
    ),

    "sem-x-west": LanguageSpec(
        code="sem-x-west",
        name="Proto-West-Semitic",
        family="Afroasiatic",
        script="Latin",
        graphemes=GRAPHEMES_PWSEM,
        allophones=ALLOPHONES_PWSEM,
        parent="sem",
        ancestors=(
            Ancestor("sem", P, 1.0, "Direct descent from Proto-Semitic"),
        ),
        notes=(
            "Proto-West-Semitic (~3500–3000 BCE). Excludes Akkadian and Eblaite "
            "(East Semitic). Ancestor of all surviving Semitic languages. "
            "Consonant inventory nearly identical to Proto-Semitic; differences "
            "are primarily morphological and accentual. *ś /ɬ/ lateral fricative "
            "still distinct. Spirantisation of stops (bgdkpt pattern) is a LATER "
            "innovation (Canaanite/Hebrew) and NOT a Proto-West-Semitic feature."
        ),
    ),

    "sem-x-central": LanguageSpec(
        code="sem-x-central",
        name="Proto-Central-Semitic",
        family="Afroasiatic",
        script="Latin",
        graphemes=GRAPHEMES_PCSEM,
        allophones=ALLOPHONES_PCSEM,
        parent="sem-x-west",
        ancestors=(
            Ancestor("sem-x-west", P, 1.0, "Descent from Proto-West-Semitic"),
        ),
        notes=(
            "Proto-Central-Semitic (~2500–2000 BCE). Ancestor of: "
            "Arabic, Northwest Semitic (Canaanite + Aramaic). "
            "Excludes South Semitic (Ethiopic, South Arabian). "
            "KEY INNOVATIONS: (1) *ś /ɬ/ begins merging with /s/ (not /ʃ/ — "
            "that is the Canaanite reflex); (2) *ṣ́ /ɬˤ/ begins shifting toward "
            "/ðˤ/ in the Arabic branch; (3) short vowel reduction in unstressed "
            "syllables (morphophonological). Consonant inventory: 29 phonemes "
            "(same letters as PSem but with *ś and *ṣ́ in transitional states)."
        ),
    ),

    "xpa": LanguageSpec(
        code="xpa",
        name="Proto-Arabic (Old Arabic)",
        family="Semitic",
        script="Latin",
        graphemes=GRAPHEMES_PROTO_AR,
        allophones=ALLOPHONES_PROTO_AR,
        parent="sem-x-central",
        ancestors=(
            Ancestor("sem-x-central", P, 1.0,
                     "Descent from Proto-Central-Semitic"),
        ),
        notes=(
            "Proto-Arabic / Old Arabic (~500 BCE – 500 CE). Reconstructed "
            "from Old North Arabian inscriptions (Safaitic, Hismaic, "
            "Dadanitic, Taymanitic) and backward reconstruction from "
            "Classical Arabic. "
            "DEFINING INNOVATIONS vs. Proto-Central-Semitic: "
            "(1) *p → /f/ uniformly — THE diagnostic Arabic innovation; "
            "(2) *ś /ɬ/ → /s/ (merged completely with *s); "
            "(3) *ṣ́ /ɬˤ/ → /ðˤ~ɮˤ/ (= Arabic ض, the 'emphatic lateral'); "
            "(4) *g /ɡ/ still present (→ /dʒ/ only in Classical period or later); "
            "(5) the 28-consonant Classical system nearly established. "
            "Vowel system: three short (/a i u/) + three long (/aː iː uː/) "
            "+ diphthongs /aj/ and /aw/. "
            "Emphatics triggered vowel backing in adjacent syllables (same as "
            "Classical and modern dialects). "
            "Script: notation follows Al-Jallad (2015) ONA romanization system."
        ),
    ),
}
