"""Berber / Proto-Berber (ber) — grapheme→IPA and allophone mappings.

Berber (Tamazight) is the Afroasiatic substrate language family of North
Africa. It is referenced as a substrate by Moroccan, Algerian, Tunisian,
Libyan, and Hassaniya Arabic.

This spec represents Common/Proto-Berber phonology — the reconstructed
ancestor of modern Tamazight varieties (Kabyle, Tachelhit, Tarifit,
Central Atlas, Tuareg, Nafusi, etc.).

Sources:
- Kossmann, M. (1999). *Essai sur la phonologie du proto-berbère*. Rüdiger Köppe.
- Chaker, S. (1995). *Linguistique berbère: études de syntaxe et de
  diachronie*. Peeters.
- Basset, A. (1952). *La langue berbère*. Oxford UP / IAI.
- Prasse, K.-G. (1972). *Manuel de grammaire touarègue* (tahaggart). Akad.
- Galand, L. (2010). *Regards sur le berbère*. Centro Studi Camito-Semitici.
- Louali, N. & Philippson, G. (2004). "Berber Phonology."
  In: *Phonologies of Asia and Africa*, ed. A.S. Kaye, vol. 1. Eisenbrauns.
"""
from orthography2ipa.types import LanguageSpec

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-BERBER / COMMON BERBER (ber)
# ═══════════════════════════════════════════════════════════════════════════
#
# Classification: Afroasiatic > Berber (own primary branch)
# Time: proto-stage ~3000–2000 BCE (speculative)
# Modern varieties: ~30–40 million speakers across North Africa
#
# KEY PHONOLOGICAL FEATURES (Kossmann 1999, Louali & Philippson 2004):
#
# 1. EMPHATIC (pharyngealised) consonant series: tˤ, dˤ, sˤ, zˤ, (ɾˤ)
#    This is the single most important substrate effect on Maghrebi Arabic:
#    Berber emphatics REINFORCED Arabic emphatics in contact.
#
# 2. CONSONANT CLUSTERS: Berber tolerates extensive CC and CCC clusters,
#    even word-initially and word-finally. This is the direct cause of
#    Moroccan Arabic's extreme vowel deletion — Berber speakers transferred
#    their cluster tolerance into Arabic.
#    Example: Tachelhit /tftkt/ "you sprained it" — no vowels at all.
#
# 3. LABIOVELAR series: kʷ, gʷ, xʷ (preserved in many varieties)
#
# 4. PHARYNGEALS: ħ, ʕ strongly maintained (shared with Arabic;
#    mutual reinforcement in contact)
#
# 5. VOWEL SYSTEM: Only 3 phonemic vowels /a i u/ (plus schwa ə as
#    epenthetic). This extreme vowel poverty contributed to Arabic
#    vowel reduction in Maghrebi dialects.
#
# 6. GEMINATION: contrastive consonant length throughout
#
# 7. UVULARS: q, χ, ʁ well-established

GRAPHEMES = {
    # --- Vowels (minimal 3-vowel + schwa system) ---
    "a": ["a"], "i": ["i"], "u": ["u"],
    "ə": ["ə"],  # epenthetic schwa (predictable but pervasive)

    # --- Plain stops ---
    "b": ["b"],
    "t": ["t"], "d": ["d"],
    "k": ["k"], "g": ["ɡ"],
    "q": ["q"],

    # --- Emphatic (pharyngealised) stops and fricatives ---
    "ṭ": ["tˤ"], "ḍ": ["dˤ"],
    "ṣ": ["sˤ"], "ẓ": ["zˤ"],

    # --- Labiovelar stops ---
    "kʷ": ["kʷ"], "gʷ": ["ɡʷ"],

    # --- Fricatives ---
    "f": ["f"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "x": ["x"], "ɣ": ["ɣ"],
    "χ": ["χ"], "ʁ": ["ʁ"],
    "h": ["h"],
    "ħ": ["ħ"], "ʕ": ["ʕ"],

    # --- Affricates (some varieties) ---
    "ts": ["ts"], "dz": ["dz"],

    # --- Nasals ---
    "m": ["m"], "n": ["n"],

    # --- Liquids ---
    "l": ["l"], "r": ["r"],

    # --- Glides ---
    "w": ["w"], "j": ["j"],

    # --- Geminate notation (common in Tifinagh/Latin transcription) ---
    "tt": ["tː"], "dd": ["dː"], "ss": ["sː"], "zz": ["zː"],
    "kk": ["kː"], "gg": ["ɡː"], "ff": ["fː"],
    "ll": ["lː"], "mm": ["mː"], "nn": ["nː"], "rr": ["rː"],
}

ALLOPHONES = {
    "b": ["b", "β"],  # spirantisation in many varieties
    "t": ["t", "θ"],  # spirantisation: Kabyle, Rifi
    "d": ["d", "ð"],
    "k": ["k", "x"],  # spirantisation
    "ɡ": ["ɡ", "ɣ"],  # spirantisation
    "q": ["q", "ʔ"],  # glottalisation in some varieties

    "tˤ": ["tˤ"], "dˤ": ["dˤ"],
    "sˤ": ["sˤ"], "zˤ": ["zˤ"],

    "kʷ": ["kʷ"], "ɡʷ": ["ɡʷ"],

    "f": ["f"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "x": ["x"], "ɣ": ["ɣ"],
    "χ": ["χ"], "ʁ": ["ʁ"],
    "h": ["h"],
    "ħ": ["ħ"], "ʕ": ["ʕ"],

    "ts": ["ts"], "dz": ["dz"],

    "m": ["m"], "n": ["n", "ŋ"],
    "l": ["l", "ɫ"],  # velarised lateral in many varieties
    "r": ["r", "ɾ"],

    "w": ["w"], "j": ["j"],

    "a": ["a", "æ"],
    "i": ["i", "ɪ"],
    "u": ["u", "ʊ"],
    "ə": ["ə"],

    # Geminates
    "tː": ["tː"], "dː": ["dː"], "sː": ["sː"], "zː": ["zː"],
    "kː": ["kː"], "ɡː": ["ɡː"], "fː": ["fː"],
    "lː": ["lː"], "mː": ["mː"], "nː": ["nː"], "rː": ["rː"],
}


SPECS = {
    "ber": LanguageSpec(
        code="ber",
        name="Berber (Proto-Berber / Common Tamazight)",
        family="Afroasiatic",
        script="Tifinagh",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent=None,
        notes=(
            "Proto-Berber / Common Berber. Afroasiatic > Berber branch. "
            "Reconstructed ancestor of all Tamazight varieties (Kabyle, "
            "Tachelhit, Tarifit, Central Atlas, Tuareg, Nafusi, etc.). "
            "~30–40 million speakers across North Africa. "
            "KEY SUBSTRATE EFFECTS ON MAGHREBI ARABIC: "
            "(1) Emphatic (pharyngealised) consonant reinforcement; "
            "(2) Extreme consonant cluster tolerance (→ Moroccan vowel deletion); "
            "(3) Minimal vowel system (3 phonemic: /a i u/ + ə); "
            "(4) Spirantisation of stops (b→β, t→θ, k→x). "
            "Traditional script: Tifinagh (Tuareg preserve oldest forms). "
            "Refs: Kossmann (1999), Chaker (1995), Louali & Philippson (2004)."
        ),
    ),
}
