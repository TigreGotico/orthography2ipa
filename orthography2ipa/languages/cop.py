"""Coptic (cop) — grapheme→IPA and allophone mappings.

Coptic is the final stage of the Ancient Egyptian language, written in a
Greek-derived alphabet. It is referenced as the substrate of Egyptian
Arabic (ar-EG).

Coptic was the spoken language of Egypt until approximately the 14th–17th
century CE, when it was fully replaced by Arabic. It survives today only
as the liturgical language of the Coptic Orthodox Church.

This spec represents Sahidic Coptic, the literary standard dialect
(Upper Egypt, ~4th–10th c. CE), which is the best-documented variety.

Sources:
- Loprieno, A. (1995). *Ancient Egyptian: A Linguistic Introduction*. CUP.
- Layton, B. (2000). *A Coptic Grammar*. Harrassowitz.
- Peust, C. (1999). *Egyptian Phonology*. Göttingen.
- Lambdin, T.O. (1983). *Introduction to Sahidic Coptic*. Mercer UP.
- Kasser, R. (1991). "Dialects." In: *Coptic Encyclopedia*, vol. 8. Macmillan.
"""
from orthography2ipa.types import LanguageSpec

# ═══════════════════════════════════════════════════════════════════════════
# COPTIC — SAHIDIC DIALECT (cop)
# ═══════════════════════════════════════════════════════════════════════════
#
# Classification: Afroasiatic > Egyptian (own primary branch; no siblings)
# Script: Coptic alphabet (Greek + 6 Demotic-derived letters)
# Time: ~2nd century CE (earliest texts) to ~14th–17th c. CE (extinction)
# Dialects: Sahidic (literary standard), Bohairic (liturgical, Lower Egypt),
#           Fayyumic, Akhmimic, Lycopolitan, Oxyrhynchite
#
# KEY PHONOLOGICAL FEATURES (Peust 1999, Loprieno 1995):
# - Simple consonant inventory vs. earlier Egyptian
# - Aspirated stops: pʰ tʰ kʰ (from Greek orthography — may reflect
#   Egyptian aspiration or Greek spelling convention)
# - Affricate /tʃ/ from Egyptian *tj palatalization
# - Egyptian emphatics (ṭ, ḍ, etc.) LOST by Coptic stage
#   (already merged in late Demotic)
# - Sonorant /l/ stable (unlike earlier Egyptian where l~r merged)
# - No pharyngeals ħ, ʕ (lost by Coptic; present in Old Egyptian)
# - Glottal stop /ʔ/ remnant of earlier pharyngeals/laryngeals
# - Rich vowel system with qualitative distinctions (not just length)
# - Stress-timed prosody (unlike Arabic)
#
# SUBSTRATE EFFECTS ON EGYPTIAN ARABIC:
# Minimal phonological impact (Arabic phonology dominated).
# Main substrate effects are LEXICAL (agricultural terms, place names)
# and possibly some vowel patterns (Coptic stress patterns may have
# influenced Egyptian Arabic intonation).

GRAPHEMES = {
    # --- Coptic alphabet letters (Greek-derived) ---
    # Vowels
    "ⲁ": ["a"],  # alpha
    "ⲉ": ["ɛ"],  # ei
    "ⲏ": ["eː"],  # eta
    "ⲓ": ["i"],  # iota
    "ⲟ": ["ɔ"],  # omicron
    "ⲱ": ["oː"],  # omega
    "ⲩ": ["u"],  # upsilon (also [w] in diphthongs)

    # Consonants (Greek-derived)
    "ⲃ": ["b"],  # beta (= /b/ not /v/ in Coptic)
    "ⲅ": ["ɡ"],  # gamma
    "ⲇ": ["d"],  # delta
    "ⲍ": ["z"],  # zeta (= /z/ in Sahidic)
    "ⲑ": ["tʰ"],  # theta (aspirated)
    "ⲕ": ["k"],  # kappa
    "ⲗ": ["l"],  # lambda
    "ⲙ": ["m"],  # mu
    "ⲛ": ["n"],  # nu
    "ⲝ": ["ks"],  # ksi
    "ⲡ": ["p"],  # pi
    "ⲣ": ["ɾ"],  # rho
    "ⲥ": ["s"],  # sigma
    "ⲧ": ["t"],  # tau
    "ⲫ": ["pʰ"],  # phi (aspirated in Coptic)
    "ⲭ": ["kʰ"],  # khi (aspirated)
    "ⲯ": ["ps"],  # psi

    # Consonants (Demotic-derived, unique to Coptic)
    "ϣ": ["ʃ"],  # shai
    "ϥ": ["f"],  # fai
    "ϩ": ["h"],  # hori
    "ϫ": ["tʃ"],  # djandja (< Eg. *tj palatalisation)
    "ϭ": ["kʲ"],  # tshima (palatalised velar)
    "ϯ": ["ti"],  # ti (ligature)

    # Supralinear stroke marks syllabic consonants:
    # ⲛ̄ = syllabic [n̩], ⲙ̄ = syllabic [m̩]
    "ⲛ̄": ["n̩"],
    "ⲙ̄": ["m̩"],

    # --- Common digraphs ---
    "ⲟⲩ": ["uː"],  # ou digraph = /uː/
    "ⲉⲓ": ["iː"],  # ei digraph = /iː/ (raised)
}

ALLOPHONES = {
    # Stops
    "p": ["p"], "pʰ": ["pʰ"],
    "b": ["b"],
    "t": ["t"], "tʰ": ["tʰ"],
    "d": ["d"],
    "k": ["k"], "kʰ": ["kʰ"], "kʲ": ["kʲ"],
    "ɡ": ["ɡ"],

    # Affricates
    "tʃ": ["tʃ"],

    # Fricatives
    "f": ["f"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"],
    "h": ["h"],

    # Nasals
    "m": ["m", "m̩"],
    "n": ["n", "n̩", "ŋ"],

    # Liquids
    "l": ["l"],
    "ɾ": ["ɾ", "r"],

    # Glides
    "j": ["j"],
    "w": ["w"],

    # Vowels (Sahidic system)
    "a": ["a", "ɐ"],
    "ɛ": ["ɛ"],
    "eː": ["eː"],
    "i": ["i"],
    "iː": ["iː"],
    "ɔ": ["ɔ"],
    "oː": ["oː"],
    "u": ["u"],
    "uː": ["uː"],
    "ə": ["ə"],  # reduced vowel in unstressed syllables
}

SPECS = {
    "cop": LanguageSpec(
        code="cop",
        name="Coptic (Sahidic)",
        family="Afroasiatic",
        script="Coptic",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent=None,
        notes=(
            "Coptic — final stage of the Ancient Egyptian language. "
            "Sahidic dialect (Upper Egypt, literary standard, ~4th–10th c. CE). "
            "Written in Coptic alphabet (Greek + 6 Demotic letters). "
            "Classification: Afroasiatic > Egyptian (own primary branch). "
            "Extinct as spoken language ~14th–17th c. CE (replaced by Arabic). "
            "Survives as liturgical language of Coptic Orthodox Church. "
            "SUBSTRATE EFFECTS ON EGYPTIAN ARABIC: primarily lexical "
            "(agricultural terms, place names); minimal phonological impact. "
            "KEY DIFFERENCES FROM OLD EGYPTIAN: emphatics lost, pharyngeals "
            "lost, aspirated stops (pʰ tʰ kʰ), affricate /tʃ/ from *tj, "
            "rich qualitative vowel system. "
            "Refs: Loprieno (1995), Layton (2000), Peust (1999)."
        ),
    ),
}
