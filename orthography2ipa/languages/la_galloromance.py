"""Gallo-Romance Vulgar Latin (la-x-gallia) — intermediate ancestor.

The spoken Latin of Gaul and northeastern Hispania (~3rd–7th c. CE),
ancestral to French, Occitan, Catalan, Franco-Provençal, and Romansh.

Gallo-Romance is distinguished from Ibero-Romance by a DIFFERENT set
of innovations from the same Vulgar Latin base.

Sources:
- Posner, R. (1996). *The Romance Languages*. CUP.
- Bec, P. (1970–1971). *Manuel pratique de philologie romane*. Picard.
- Alkire, T. & Rosen, C. (2010). *Romance Languages: A Historical
  Introduction*. CUP.
- Sala, M. (1998). *Lenguas en contacto*. Gredos.
- Price, G. (1971). *The French Language: Present and Past*. Arnold.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# GALLO-ROMANCE VULGAR LATIN (la-x-gallia)
# ═══════════════════════════════════════════════════════════════════════════
#
# The spoken Latin of Roman Gaul and the NE corner of Hispania (Catalonia).
# Transitional between Classical Latin and the Gallo-Romance languages.
#
# KEY SOUND CHANGES (Gallo-Romance innovations, contrasting with Ibero):
#
# 1. VOWEL SYSTEM:
#    Same 10→7 merger as all Western Romance, BUT additionally:
#    - Fronting of /u/ → /y/ (unique to Gallo-Romance + some N. Italian)
#      Latin MŪRUM [muːrum] → GalloRom [myːr] → Fr. mur [myʁ]
#      This does NOT happen in Ibero-Romance (Sp. muro [muɾo])
#    - More extensive vowel reduction in unstressed syllables
#    - Nasal vowels develop (from VN sequences)
#
# 2. LENITION (stronger than Ibero-Romance):
#    Intervocalic voiceless stops weaken further, often to ∅:
#    -p- → -b- → -β- → -v-;   SAPŌNEM → Fr. savon (vs Sp. jabón)
#    -t- → -d- → -ð- → ∅;     VĪTAM → Fr. vie (vs Sp. vida)
#    -k- → -g- → -ɣ- → ∅;     FOCUM → Fr. feu (vs Sp. fuego)
#
# 3. PALATALISATION (more extensive than Ibero):
#    Latin CA- → [tʃa] → Fr. [ʃa] (vs Sp. keeps [ka])
#    CANTĀRE → Fr. chanter [ʃɑ̃te] (vs Sp. cantar [kantaɾ])
#    Latin -CT- → [jt] → Fr. [jt]/[t] (like Ibero, but further)
#
# 4. F- PRESERVED:
#    Unlike Castilian (F- → h-), Gallo-Romance KEEPS /f/:
#    FILIUM → Fr. fils, Oc. filh, Cat. fill (vs Sp. hijo)
#
# 5. FINAL CONSONANT RETENTION:
#    Gallo-Romance retains final consonants longer than Ibero:
#    Latin -S → kept in Gallo-Romance (Fr. plural -s)
#    Final vowels lost more aggressively than in Ibero-Romance.
#
# 6. DIPHTHONGISATION:
#    /ɛ/ → various complex diphthongs (Fr. [je], [wa], etc.)
#    /ɔ/ → [we] > [ø] in French; simpler in Occitan/Catalan
#    More complex trajectory than Ibero-Romance diphthongisation.

GRAPHEMES = {
    # --- Vowels (7-vowel system + /y/ innovation) ---
    "a": ["a"],
    "e": ["e"],  # < ĭ, ē
    "ɛ": ["ɛ"],  # < ĕ (diphthongises variously)
    "i": ["i"],  # < ī
    "o": ["o"],  # < ŭ, ō
    "ɔ": ["ɔ"],  # < ŏ (diphthongises)
    "u": ["y"],  # FRONTED < ū — THE Gallo-Romance innovation

    # --- Nasal vowels (developing) ---
    "an": ["ã"],
    "en-GB": ["ẽ"],
    "in": ["ĩ"],
    "on": ["õ"],

    # --- Consonants ---
    "p": ["p"],
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "c": ["k", "tʃ"],  # [tʃ] before e/i; more palatalisation than Ibero
    "g": ["ɡ", "dʒ"],
    "f": ["f"],  # PRESERVED (not → [h] like Castilian)
    "v": ["v"],  # /v/ survives (Ibero merges with /b/)
    "s": ["s"],
    "z": ["z"],  # voiced sibilant preserved
    "h": ["∅"],  # lost (Gallo-Romance is h-less)

    # --- Palatals (more extensive than Ibero) ---
    "ch": ["tʃ"],  # < CA- palatalisation
    "j": ["dʒ"],  # < Latin I before vowel, G before e/i
    "ñ": ["ɲ"],  # < -ni-, -gn-
    "ll": ["ʎ"],  # < -li-, -cl-, -gl-

    # --- Nasals ---
    "m": ["m"],
    "n": ["n"],

    # --- Liquids ---
    "l": ["l"],
    "r": ["ɾ"],
    "rr": ["r"],

    # --- Diphthongs ---
    "ie": ["je"],  # < /ɛ/
    "ue": ["we"],  # < /ɔ/
    "ai": ["aj"],
    "au": ["aw"],
    "ei": ["ej"],
    "ou": ["ow"],
}

ALLOPHONES = {
    "p": ["p"],
    "b": ["b", "β", "v"],  # lenition more advanced than Ibero
    "t": ["t"],
    "d": ["d", "ð", "∅"],  # can elide entirely (→ French)
    "k": ["k"],
    "ɡ": ["ɡ", "ɣ", "∅"],  # can elide entirely
    "tʃ": ["tʃ"],
    "dʒ": ["dʒ", "ʒ"],
    "f": ["f"],
    "v": ["v"],
    "s": ["s"],
    "z": ["z"],
    "ɲ": ["ɲ"],
    "ʎ": ["ʎ"],
    "m": ["m"],
    "n": ["n", "ŋ"],
    "l": ["l"],
    "ɾ": ["ɾ"],
    "r": ["r"],
    "y": ["y"],  # fronted /u/
    "a": ["a"], "e": ["e"], "ɛ": ["ɛ"], "i": ["i"],
    "o": ["o"], "ɔ": ["ɔ"],
    "ã": ["ã"], "ẽ": ["ẽ"], "ĩ": ["ĩ"], "õ": ["õ"],
}

SPECS = {
    "la-x-gallia": LanguageSpec(
        code="la-x-gallia",
        name="Gallo-Romance Vulgar Latin",
        family="Italic",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="la",
        ancestors=(
            Ancestor("la", P, 0.80,
                     "Primary descent from Classical Latin"),
            Ancestor("xcg", SUB, 0.12,
                     "Gaulish substrate: vigesimal counting, "
                     "u-fronting [u]>[y], lexicon (briser, "
                     "chemin, char). Heaviest Celtic substrate "
                     "in any Romance language."),
            Ancestor("gem", SUP, 0.08,
                     "Early Germanic superstrate (Visigoths, "
                     "Burgundians in S. Gaul; Franks in N. Gaul). "
                     "Lexicon: blanc, guerre, jardin."),
        ),
        notes=(
            "Gallo-Romance Vulgar Latin (~3rd–7th c. CE). Spoken Latin "
            "of Gaul and NE Hispania. Ancestral to French, Occitan, "
            "Catalan, Franco-Provençal. Key innovations vs Ibero-Romance: "
            "(1) /u/ → /y/ fronting (mūrum → [myːr]). (2) More aggressive "
            "lenition (intervocalic stops → ∅). (3) CA- → [tʃ] "
            "palatalisation. (4) F- PRESERVED (not → [h]). (5) Nasal "
            "vowels develop. (6) Final vowel loss more extreme. "
            "(7) Voiced /v/ preserved (not merged with /b/). "
            "Gaulish substrate is the strongest Celtic substrate "
            "in any Romance language (Price 1971, Bec 1970)."
        ),
    ),
}
