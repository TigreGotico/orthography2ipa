"""Portuguese (pt, pt-BR, pt-AO) — grapheme→IPA and allophone mappings.

Sources:
- Mateus, M.H. & d'Andrade, E. (2000). *The Phonology of Portuguese*.
- Bisol, L. (2005). *Introdução a estudos de fonologia do português brasileiro*.
- Cristófaro Silva, T. (2012). *Fonética e fonologia do português*.

Conventions:
- Base mapping is European Portuguese (PT-PT).
- Brazilian (pt-BR) and Angolan (pt-AO) override where pronunciation
  diverges systematically.
- Digraphs ⟨lh⟩, ⟨nh⟩, ⟨ch⟩, ⟨rr⟩, ⟨ss⟩, ⟨qu⟩, ⟨gu⟩ are the
  officially recognised Portuguese digraphs per the *Acordo Ortográfico*.
"""
from orthography2ipa.types import LanguageSpec

# ═══════════════════════════════════════════════════════════════════════════
# European Portuguese (PT-PT)
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_PT = {
    # --- Single vowels ---
    "a": ["a", "ɐ"],
    "e": ["e", "ɛ", "ə"],
    "i": ["i"],
    "o": ["o", "ɔ", "u"],
    "u": ["u"],

    # --- Accented vowels ---
    "á": ["a"],
    "à": ["a"],
    "â": ["ɐ"],
    "ã": ["ɐ̃"],
    "é": ["ɛ"],
    "ê": ["e"],
    "í": ["i"],
    "ó": ["ɔ"],
    "ô": ["o"],
    "õ": ["õ"],
    "ú": ["u"],
    "ü": ["u"],  # rare, loanwords

    # --- Single consonants ---
    "b": ["b"],
    "c": ["k", "s"],  # /k/ before a,o,u; /s/ before e,i
    "ç": ["s"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "ʒ"],  # /ɡ/ before a,o,u; /ʒ/ before e,i
    "h": [""],  # always silent
    "j": ["ʒ"],
    "k": ["k"],  # loanwords
    "l": ["l", "ɫ"],  # clear onset; dark coda
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],  # only in ⟨qu⟩
    "r": ["ʁ", "ɾ"],  # uvular initial/coda; tap intervocalic
    "s": ["s", "z", "ʃ", "ʒ"],  # complex: /z/ intervocalic, /ʃ/ coda (PT-PT)
    "t": ["t"],
    "v": ["v"],
    "w": ["w"],  # loanwords
    "x": ["ʃ", "ks", "z", "s"],
    "y": ["i"],  # loanwords
    "z": ["z", "ʃ"],  # /ʃ/ word-finally (PT-PT)

    # --- Consonant digraphs (official) ---
    "ch": ["ʃ"],
    "lh": ["ʎ"],
    "nh": ["ɲ"],
    "rr": ["ʁ"],  # always uvular/velar
    "ss": ["s"],  # intervocalic voiceless

    # --- ⟨qu⟩ / ⟨gu⟩ digraphs ---
    "qu": ["k", "kw"],  # /k/ before e,i (⟨u⟩ silent); /kw/ before a,o
    "gu": ["ɡ", "ɡw"],  # /ɡ/ before e,i (⟨u⟩ silent); /ɡw/ before a,o

    # --- Oral diphthongs ---
    "ai": ["aj"],
    "au": ["aw"],
    "ei": ["ej"],
    "eu": ["ew"],
    "iu": ["iw"],
    "oi": ["oj"],
    "ou": ["ow"],
    "ui": ["uj"],

    # --- Nasal diphthongs ---
    "ão": ["ɐ̃w̃"],
    "ãe": ["ɐ̃j̃"],
    "õe": ["õj̃"],
}

ALLOPHONES_PT = {
    # Plosives
    "p": ["p"],
    "b": ["b", "β"],  # spirantised intervocalic in casual speech
    "t": ["t"],
    "d": ["d", "ð"],  # spirantised intervocalic in casual speech
    "k": ["k"],
    "ɡ": ["ɡ", "ɣ"],

    # Fricatives
    "f": ["f"],
    "v": ["v"],
    "s": ["s"],
    "z": ["z"],
    "ʃ": ["ʃ"],
    "ʒ": ["ʒ"],

    # Uvular/rhotic
    "ʁ": ["ʁ", "χ", "h", "ɦ"],  # uvular fricative, voiceless, or glottal
    "ɾ": ["ɾ"],  # alveolar tap

    # Nasals
    "m": ["m"],
    "n": ["n", "ŋ"],  # velar before /k,ɡ/
    "ɲ": ["ɲ"],
    "ŋ": ["ŋ"],  # not phonemic, allophone of /n/

    # Laterals
    "l": ["l"],
    "ɫ": ["ɫ", "w"],  # dark l → [w] vocalisation in PT-BR
    "ʎ": ["ʎ"],

    # Glides
    "w": ["w"],
    "j": ["j"],

    # Monophthongs
    "a": ["a"],
    "ɐ": ["ɐ"],
    "e": ["e"],
    "ɛ": ["ɛ"],
    "ə": ["ə", "ɨ"],  # [ɨ] common in PT-PT unstressed
    "i": ["i"],
    "o": ["o"],
    "ɔ": ["ɔ"],
    "u": ["u"],

    # Nasal vowels
    "ɐ̃": ["ɐ̃"],
    "ẽ": ["ẽ"],
    "ĩ": ["ĩ"],
    "õ": ["õ"],
    "ũ": ["ũ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Brazilian Portuguese (pt-BR)
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_PT_BR = {
    **GRAPHEMES_PT,
    "r": ["ɾ", "h", "x"],  # tap intervocalic; /h/ onset in many dialects
    "s": ["s", "z"],  # no coda /ʃ/ in most dialects
    "t": ["t", "tʃ"],  # /tʃ/ before /i/ (palatalisation)
    "d": ["d", "dʒ"],  # /dʒ/ before /i/ (palatalisation)
    "z": ["z", "s"],  # /s/ word-finally (devoicing)
    "l": ["l", "w"],  # dark-l fully vocalised to [w] in coda
}

ALLOPHONES_PT_BR = {
    **ALLOPHONES_PT,
    "t": ["t", "tʃ"],  # palatalised before /i/
    "d": ["d", "dʒ"],  # palatalised before /i/
    "ɫ": ["w"],  # full vocalisation
    "ʁ": ["h", "x", "ɦ", "ʁ"],  # glottal/velar dominant in most dialects
    "ɾ": ["ɾ", "ɹ"],  # retroflex tap in paulista/caipira dialects
    "ə": ["ə", "i"],  # word-final unstressed /e/ → [i]
}

# ═══════════════════════════════════════════════════════════════════════════
# Angolan Portuguese (pt-AO)
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_PT_AO = {
    **GRAPHEMES_PT,
    "r": ["ʁ"],  # uvular dominant in all positions
    "s": ["s"],  # no intervocalic voicing for many speakers
}

ALLOPHONES_PT_AO = {
    **ALLOPHONES_PT,
    "ʁ": ["ʁ", "r"],  # some speakers use alveolar trill
}

# ── Specs ──────────────────────────────────────────────────────────────────
SPECS = {
    "pt": LanguageSpec(
        code="pt",
        name="European Portuguese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_PT,
        allophones=ALLOPHONES_PT,
        parent="la",
        notes="Based on standard Lisbon pronunciation.",
    ),
    "pt-BR": LanguageSpec(
        code="pt-BR",
        name="Brazilian Portuguese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_PT_BR,
        allophones=ALLOPHONES_PT_BR,
        parent="pt",
        notes=(
            "Key differences from PT-PT: palatalisation of /t,d/ before /i/, "
            "coda /l/ → [w], onset /r/ → [h] in most dialects, no coda /ʃ/."
        ),
    ),
    "pt-AO": LanguageSpec(
        code="pt-AO",
        name="Angolan Portuguese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_PT_AO,
        allophones=ALLOPHONES_PT_AO,
        parent="pt",
        notes="Based on Luanda educated speech.",
    ),
}
