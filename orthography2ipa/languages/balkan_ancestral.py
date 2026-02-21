"""Dacian/Thracian (xda) and Hungarian (hu) — minimal stubs.

These are referenced as substrate/adstrate in Romance ancestry chains
but cannot have full grapheme inventories due to limited attestation
(Dacian).

Sources:
Dacian:
- Duridanov, I. (1969). *Thrakisch-dakische Studien*. Bulg. Akad. Wiss.
- Russu, I.I. (1969). *Die Sprache der Thrako-Daker*. Ed. Științifică.
- Crossland, R.A. (1982). 'Linguistic problems of the Balkan area.' In
  *The Cambridge Ancient History* III.1. CUP.
- Georgiev, V. (1977). *Trakite i technijat ezik*. BAN.

Hungarian:
- Siptár, P. & Törkenczy, M. (2000). *The Phonology of Hungarian*. OUP.
"""
from orthography2ipa.types import LanguageSpec

# ═══════════════════════════════════════════════════════════════════════════
# DACIAN / THRACIAN (xda) — minimal reconstructed stub
# ═══════════════════════════════════════════════════════════════════════════
#
# Dacian and Thracian are poorly attested Indo-European languages
# of the pre-Roman Balkans. Only ~160 words attributed, plus
# onomastic material. Exact relationship between Dacian and Thracian
# is debated (same language? sister languages?).
#
# We model the MINIMUM phonological system inferable from:
# - Plant names in Dioscorides/Pseudo-Apuleius
# - Place names and personal names in Greek/Latin inscriptions
# - The ~100 Romanian-Albanian shared words of unknown origin
#
# THIS IS HIGHLY SPECULATIVE. The phonological system is a
# plausible reconstruction, not a certainty.

GRAPHEMES_XDA = {
    # Vowels (standard IE 5-vowel, inferred)
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
    # Consonants (inferred from onomastics and plant names)
    "b": ["b"], "p": ["p"], "d": ["d"], "t": ["t"],
    "g": ["ɡ"], "k": ["k"],
    "s": ["s"], "z": ["z"],
    "m": ["m"], "n": ["n"],
    "l": ["l"], "r": ["r"],
    # Aspirates (possible, IE heritage)
    "bh": ["bʱ"], "dh": ["dʱ"], "gh": ["ɡʱ"],
}

ALLOPHONES_XDA = {
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
    "b": ["b"], "p": ["p"], "d": ["d"], "t": ["t"],
    "ɡ": ["ɡ"], "k": ["k"],
    "s": ["s"], "z": ["z"],
    "m": ["m"], "n": ["n"],
    "l": ["l"], "r": ["r"],
    "bʱ": ["bʱ", "b"], "dʱ": ["dʱ", "d"], "ɡʱ": ["ɡʱ", "ɡ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# HUNGARIAN (hu) — phonological reference for adstrate chains
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_HU = {
    # --- Vowels (14-vowel system with length) ---
    "a": ["ɒ"],  # short open rounded
    "á": ["aː"],  # long open unrounded
    "e": ["ɛ"],
    "é": ["eː"],
    "i": ["i"],
    "í": ["iː"],
    "o": ["o"],
    "ó": ["oː"],
    "ö": ["ø"],
    "ő": ["øː"],
    "u": ["u"],
    "ú": ["uː"],
    "ü": ["y"],
    "ű": ["yː"],

    # --- Consonants ---
    "b": ["b"], "p": ["p"],
    "d": ["d"], "t": ["t"],
    "g": ["ɡ"], "k": ["k"],
    "f": ["f"], "v": ["v"],
    "sz": ["s"], "z": ["z"],
    "s": ["ʃ"], "zs": ["ʒ"],
    "c": ["ts"], "cs": ["tʃ"],
    "dz": ["dz"], "dzs": ["dʒ"],
    "h": ["h"],
    "j": ["j"], "ly": ["j"],  # ly = /j/ in modern standard
    "m": ["m"], "n": ["n"],
    "ny": ["ɲ"],
    "l": ["l"],
    "r": ["r"],
    "gy": ["ɟ"],  # palatal stop
    "ty": ["c"],  # palatal stop

    # --- Geminates (written doubled) ---
    "bb": ["bː"], "pp": ["pː"], "dd": ["dː"], "tt": ["tː"],
    "gg": ["ɡː"], "kk": ["kː"],
    "ff": ["fː"], "vv": ["vː"],
    "ssz": ["sː"], "zz": ["zː"],
    "ss": ["ʃː"], "zzs": ["ʒː"],
    "ll": ["lː"], "mm": ["mː"], "nn": ["nː"],
    "rr": ["rː"],
    "ccs": ["tːʃ"], "ggy": ["ɟː"], "tty": ["cː"],
    "nny": ["ɲː"],
}

ALLOPHONES_HU = {
    "ɒ": ["ɒ"], "aː": ["aː"],
    "ɛ": ["ɛ"], "eː": ["eː"],
    "i": ["i"], "iː": ["iː"],
    "o": ["o"], "oː": ["oː"],
    "ø": ["ø"], "øː": ["øː"],
    "u": ["u"], "uː": ["uː"],
    "y": ["y"], "yː": ["yː"],
    "b": ["b"], "p": ["p", "pʰ"],
    "d": ["d"], "t": ["t", "tʰ"],
    "ɡ": ["ɡ"], "k": ["k", "kʰ"],
    "ɟ": ["ɟ"], "c": ["c"],
    "f": ["f"], "v": ["v"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "ts": ["ts"], "tʃ": ["tʃ"],
    "dz": ["dz"], "dʒ": ["dʒ"],
    "h": ["h", "x", "ɦ"],
    "m": ["m"], "n": ["n", "ŋ", "ɱ"],
    "ɲ": ["ɲ"],
    "l": ["l"],
    "r": ["r", "ɾ"],
    "j": ["j"],
}

SPECS = {
    "xda": LanguageSpec(
        code="xda",
        name="Dacian/Thracian",
        family="Indo-European",
        script="Latin",
        graphemes=GRAPHEMES_XDA,
        allophones=ALLOPHONES_XDA,
        parent="ine",
        notes=(
            "Dacian/Thracian. Poorly attested pre-Roman Balkan IE "
            "languages. ~160 attributed words plus onomastic material. "
            "Exact classification debated: some link to Albanian, others "
            "to an extinct IE branch. THIS IS SPECULATIVE: phonological "
            "system is a plausible minimum reconstruction from onomastics, "
            "plant names, and Romanian-Albanian shared vocabulary "
            "(Russu 1969, Duridanov 1969)."
        ),
    ),
    "hu": LanguageSpec(
        code="hu",
        name="Hungarian",
        family="Uralic",
        script="Latin",
        graphemes=GRAPHEMES_HU,
        allophones=ALLOPHONES_HU,
        notes=(
            "Hungarian (Magyar). Uralic language with 14-vowel system "
            "(7 short + 7 long), vowel harmony, palatal stops /c, ɟ/, "
            "and rich agglutinative morphology. Referenced as adstrate "
            "for Romanian due to centuries of Transylvanian contact "
            "(Siptár & Törkenczy 2000)."
        ),
    ),
}
