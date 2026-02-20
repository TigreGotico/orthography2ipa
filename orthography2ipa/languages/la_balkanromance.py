"""Balkan Romance Vulgar Latin (la-x-balkans) — intermediate ancestor.

The spoken Latin of the Balkans / Danubian provinces (~3rd–7th c. CE),
ancestral to Romanian, Aromanian, Megleno-Romanian, and Istro-Romanian.
Also the ancestor of extinct Dalmatian (which some classify separately).

Eastern Romance is sharply distinguished from Western Romance by the
absence of lenition, postposed articles, and heavy Slavic contact.

Sources:
- Nandriș, O. (1963). *Phonétique historique du roumain*. Klincksieck.
- Rosetti, A. (1986). *Istoria limbii române*. 7th ed. Ed. Știintifică.
- Sala, M. (2005). *From Latin to Romanian*. U of Mississippi Press.
- Maiden, M. (2016). 'Romanian, Istro-Romanian, Megleno-Romanian,
  and Aromanian.' In Ledgeway & Maiden (eds.), *The Oxford Guide to
  the Romance Languages*. OUP.
- Alkire, T. & Rosen, C. (2010). *Romance Languages: A Historical
  Introduction*. CUP.
- Mihăescu, H. (1978). *La langue latine dans le sud-est de l'Europe*.
  Bucarest: Ed. Academiei.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# BALKAN ROMANCE VULGAR LATIN (la-x-balkans)
# ═══════════════════════════════════════════════════════════════════════════
#
# The spoken Latin of the Danubian/Balkan Roman provinces: Dacia,
# Moesia, Dalmatia, Pannonia. Transitional between Classical Latin and
# the Eastern Romance languages.
#
# KEY SOUND CHANGES (Eastern Romance innovations):
#
# 1. VOWEL SYSTEM:
#    Same 10→7 merger as Western Romance, BUT with additional
#    CENTRAL VOWELS developing:
#    - /ɨ/ (close central unrounded) — from /a/ before nasals and
#      other contexts. Written ⟨â⟩ / ⟨î⟩ in Romanian.
#    - /ə/ (mid central, schwa) — from unstressed /a/ and other
#      reduced vowels. Written ⟨ă⟩ in Romanian.
#    These central vowels are THE diagnostic of Eastern Romance.
#
# 2. NO LENITION:
#    Unlike Western Romance, intervocalic voiceless stops are
#    PRESERVED (not voiced):
#    LUPUM → Ro. lup [lup] (vs Sp. lobo, Fr. loup/[lu])
#    FOCUM → Ro. foc [fok] (vs Sp. fuego, Fr. feu)
#    This is the major East-West Romance split.
#
# 3. PALATALISATION (different path from Western):
#    /k/ before e,i → [tʃ] (like Western)
#    BUT: labials before /e,i/ → palatalised:
#    /p/ → /pʲ/, /b/ → /bʲ/, /m/ → /mʲ/, /v/ → /vʲ/
#    This labial palatalisation is unique to Eastern Romance.
#
# 4. RHOTACISM:
#    Intervocalic /l/ → /r/ (in some environments):
#    Latin SOLEM → Ro. soare (not *sole)
#    (Shared with some Italic dialects but NOT Western Romance)
#
# 5. POSTPOSED DEFINITE ARTICLE:
#    Unique in Romance. The article follows the noun:
#    lupul "the wolf" (lup + -ul)
#    This may reflect Balkan sprachbund influence (also found in
#    Albanian and Bulgarian).
#
# 6. SLAVIC INFLUENCE (massive, post-6th c.):
#    Phonological: possible influence on central vowels,
#    palatalisation patterns.
#    Lexical: ~40% of Romanian vocabulary from Slavic.
#    Structural: verb prefixing, some derivational morphology.
#
# 7. ALBANIAN/THRACIAN SUBSTRATE:
#    The pre-Roman substrate (Thracian/Dacian, possibly related to
#    Albanian) may explain shared Romanian-Albanian features:
#    - Central vowel /ə/ (also in Albanian)
#    - Postposed article (also in Albanian, Bulgarian)
#    - Shared vocabulary not from Latin or Slavic (~100 words)

GRAPHEMES = {
    # --- Vowels (7-vowel + central vowels) ---
    "a": ["a"],
    "e": ["e"],       # < ĭ, ē
    "ɛ": ["ɛ"],       # < ĕ (but no diphthongisation to [je] in most contexts)
    "i": ["i"],       # < ī
    "o": ["o"],       # < ŭ, ō
    "ɔ": ["ɔ"],       # < ŏ (diphthongises to [o̯a] in Romanian)
    "u": ["u"],       # < ū (preserved, not fronted)
    "ə": ["ə"],       # CENTRAL — Balkan innovation
    "ɨ": ["ɨ"],       # CENTRAL — Balkan innovation

    # --- Consonants ---
    "p": ["p"],        # PRESERVED intervocalically (no lenition!)
    "b": ["b"],
    "t": ["t"],        # PRESERVED
    "d": ["d"],
    "c": ["k", "tʃ"],  # [tʃ] before e,i
    "g": ["ɡ", "dʒ"],  # [dʒ] before e,i
    "f": ["f"],
    "v": ["v"],
    "s": ["s"],
    "z": ["z"],
    "h": ["h"],        # /h/ preserved or restored (unlike W. Romance)

    # --- Palatals ---
    "gn": ["ɲ"],       # < -gn-, -ni-

    # --- Affricates (richer than W. Romance) ---
    "ts": ["ts"],       # from Latin /k/ before e,i in some contexts
    "dz": ["dz"],

    # --- Nasals ---
    "m": ["m"],
    "n": ["n"],

    # --- Liquids ---
    "l": ["l"],
    "r": ["r", "ɾ"],   # rhotacism: /l/ → /r/ in some words

    # --- Diphthongs ---
    "ea": ["e̯a"],      # < /ɛ/ or /e/ + /a/
    "oa": ["o̯a"],      # < /ɔ/ (THE Romanian diphthongisation)
    "ai": ["aj"],
    "au": ["aw"],
    "ei": ["ej"],
    "oi": ["oj"],
}

ALLOPHONES = {
    "p": ["p"],
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "k": ["k"],
    "ɡ": ["ɡ"],
    "tʃ": ["tʃ"],
    "dʒ": ["dʒ"],
    "ts": ["ts"],
    "dz": ["dz"],
    "f": ["f"],
    "v": ["v"],
    "s": ["s"],
    "z": ["z"],
    "ʃ": ["ʃ"],
    "ʒ": ["ʒ"],
    "h": ["h", "x"],
    "ɲ": ["ɲ"],
    "m": ["m"],
    "n": ["n", "ŋ"],
    "l": ["l"],
    "r": ["r", "ɾ"],
    "j": ["j"],
    "w": ["w"],
    # Vowels
    "a": ["a"], "e": ["e"], "ɛ": ["ɛ"], "i": ["i"],
    "o": ["o"], "ɔ": ["ɔ"], "u": ["u"],
    "ə": ["ə"], "ɨ": ["ɨ"],
}

SPECS = {
    "la-x-balkans": LanguageSpec(
        code="la-x-balkans",
        name="Balkan Romance Vulgar Latin",
        family="Italic",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="la",
        ancestors=(
            Ancestor("la", P, 0.75,
                     "Primary descent from Classical Latin"),
            Ancestor("grc", SUB, 0.06,
                     "Greek substrate/adstrate: Balkans were heavily "
                     "Hellenised; Greek coexisted with Latin for centuries. "
                     "Some shared morphological features."),
            Ancestor("xda", SUB, 0.10,
                     "Dacian/Thracian substrate: pre-Roman Balkan IE "
                     "languages. Possibly explains central vowels /ə, ɨ/, "
                     "postposed article, and ~100 Romanian-Albanian "
                     "shared words of unknown origin (e.g. copil, moș, "
                     "viezure). Exact Dacian phonology unrecoverable."),
        ),
        notes=(
            "Balkan Romance Vulgar Latin (~3rd–7th c. CE). Spoken Latin "
            "of Roman Dacia, Moesia, Dalmatia. KEY features vs Western "
            "Romance: (1) NO intervocalic lenition (lup, foc, not *lub, "
            "*fogo). (2) Central vowels /ə, ɨ/ develop. (3) Labial "
            "palatalisation before front vowels. (4) Rhotacism: "
            "intervocalic /l/ → /r/. (5) Postposed definite article "
            "(Balkan sprachbund). (6) Rich diphthong system: /ɔ/ → "
            "[o̯a]. Dacian/Thracian substrate and later massive Slavic "
            "superstrate are defining contact influences (Rosetti 1986, "
            "Sala 2005)."
        ),
    ),
}
