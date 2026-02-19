"""Phoenician and Punic — Semitic languages of Iberian colonies.

Phoenician traders established colonies across Iberia from ~9th c. BCE
(Cádiz/Gadir ~1100 BCE traditional, ~9th c. BCE archaeological).
Punic (Western Phoenician) continued through Carthaginian control
until Roman conquest (3rd–2nd c. BCE).

Sources:
- Krahmalkov, C.R. (2001). *A Phoenician-Punic Grammar*. Brill.
- Segert, S. (1976). *A Grammar of Phoenician and Punic*. Beck.
- Friedrich, J. & Röllig, W. (1999). *Phönizisch-Punische Grammatik*. 3rd ed.
- Harris, Z. (1936). *A Grammar of the Phoenician Language*. AOS.
- Huehnergard, J. (2019). "Phoenician and Punic Phonology."
  In: *The Semitic Languages*. 2nd ed. Routledge.
"""
from orthography2ipa.types import LanguageSpec

# ═══════════════════════════════════════════════════════════════════════════
# PHOENICIAN (phn)
# ═══════════════════════════════════════════════════════════════════════════
#
# Classification: Semitic > Northwest Semitic > Canaanite
# Script: Phoenician alphabet (abjad) — consonant-only; THE ancestor
#   of Greek, Latin, Arabic, Hebrew, and virtually all modern alphabets.
# Attestation: Thousands of inscriptions across the Mediterranean
#   including Iberian sites (Cádiz, Málaga, Ibiza, Almuñécar, etc.)
# Time: ~1050 BCE – 1st c. CE (Phoenician proper)
#        ~6th c. BCE – 2nd c. CE (Punic, Western)
#
# The Phoenician alphabet DOES NOT WRITE VOWELS (abjad).
# Vowel quality is reconstructed from:
#   1. Greek transcriptions of Phoenician names
#   2. Comparison with Hebrew (closely related Canaanite language)
#   3. Latin transcriptions (Plautus's Poenulus scene)
#   4. Neo-Punic and Latino-Punic inscriptions (partial vowel indication)
#
# We transcribe using standard Semitist Latin conventions.

GRAPHEMES = {
    # --- Consonants (the 22 Phoenician letters) ---
    # ʾaleph — glottal stop
    "ʾ": ["ʔ"],
    # beth
    "b": ["b"],
    # gimel
    "g": ["ɡ"],
    # daleth
    "d": ["d"],
    # he — voiceless glottal fricative (weak)
    "h": ["h"],
    # waw — labial glide (also mater lectionis for /u, o/)
    "w": ["w"],
    # zayin — voiced alveolar
    "z": ["z"],
    # ḥeth — voiceless pharyngeal fricative (emphatic h)
    "ḥ": ["ħ"],
    # ṭeth — emphatic (pharyngealised) t
    "ṭ": ["tˤ"],
    # yod — palatal glide (also mater lectionis for /i, e/)
    "y": ["j"],
    # kaph
    "k": ["k"],
    # lamedh
    "l": ["l"],
    # mem
    "m": ["m"],
    # nun
    "n": ["n"],
    # samekh — voiceless alveolar affricate or fricative
    "s": ["s"],
    # ʿayin — voiced pharyngeal fricative
    "ʿ": ["ʕ"],
    # pe
    "p": ["p"],
    # ṣade — emphatic (pharyngealised) s
    "ṣ": ["sˤ"],
    # qoph — uvular stop
    "q": ["q"],
    # resh
    "r": ["r"],
    # shin
    "š": ["ʃ"],
    # taw
    "t": ["t"],

    # --- Vowels (reconstructed; NOT in the original script) ---
    # We include them for the Latin-alphabet transcription model.
    # Based on Canaanite vowel system (reconstructed from Greek, Hebrew).
    "a": ["a"],
    "ā": ["aː"],
    "e": ["e"],  # < Proto-Canaanite *i in some positions
    "ē": ["eː"],  # < Canaanite shift *ā > *ō (NOT in Phoenician)
    "i": ["i"],
    "ī": ["iː"],
    "o": ["o"],
    "ō": ["oː"],  # < Canaanite shift *ā > *ō in stressed syllables
    "u": ["u"],
    "ū": ["uː"],
}

ALLOPHONES = {
    # Stops
    "ʔ": ["ʔ"],  # weakened / lost in late Punic
    "b": ["b", "β"],  # spirantisation in Punic (bgdkpt pattern)
    "ɡ": ["ɡ", "ɣ"],
    "d": ["d", "ð"],
    "k": ["k", "x"],
    "p": ["p", "f"],  # spirantisation
    "t": ["t", "θ"],  # spirantisation
    "q": ["q"],

    # Emphatics
    "tˤ": ["tˤ"],
    "sˤ": ["sˤ"],

    # Fricatives
    "h": ["h", "∅"],  # weakening in late Phoenician
    "ħ": ["ħ"],
    "ʕ": ["ʕ"],
    "s": ["s"],
    "z": ["z"],
    "ʃ": ["ʃ"],

    # Nasals
    "m": ["m"],
    "n": ["n", "ŋ"],

    # Liquids
    "l": ["l"],
    "r": ["r", "ɾ"],

    # Glides
    "w": ["w"],
    "j": ["j"],

    # Vowels
    "a": ["a"], "aː": ["aː"],
    "e": ["e"], "eː": ["eː"],
    "i": ["i"], "iː": ["iː"],
    "o": ["o"], "oː": ["oː"],
    "u": ["u"], "uː": ["uː"],
}

SPECS = {
    "phn": LanguageSpec(
        code="phn", name="Phoenician/Punic",
        family="Semitic", script="Latin",
        graphemes=GRAPHEMES, allophones=ALLOPHONES,
        notes=(
            "Phoenician/Punic (~1050 BCE – 2nd c. CE). Northwest Semitic "
            "(Canaanite) language. Colonies in Iberia from ~9th c. BCE: "
            "Gadir (Cádiz), Malaka (Málaga), Sexi (Almuñécar), Ebusus "
            "(Ibiza). The Phoenician ALPHABET (22 consonant letters, no "
            "vowels) is the ancestor of virtually all modern alphabets. "
            "Vowels reconstructed from Greek transcriptions and Hebrew "
            "comparison. Punic features bgdkpt spirantisation. Emphatic "
            "(pharyngealised) consonants /tˤ, sˤ/ and pharyngeals /ħ, ʕ/. "
            "Substrate influence on Iberian languages debated."
        ),
    ),
}
