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
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec, GraphemePosition as GP

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
AD = AncestorRole.ADSTRATE
SUP = AncestorRole.SUPERSTRATE

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

# Portuguese has the richest positional grapheme variation of any Iberian
# language. The ⟨s⟩/⟨z⟩ system, ⟨r⟩ distribution, ⟨l⟩ velarisation,
# and ⟨b⟩/⟨d⟩/⟨g⟩ lenition are all highly position-dependent.
#
# Mateus & d'Andrade (2000), ch. 2–4.

POSITIONAL_PT_PT = {
    # ── ⟨s⟩: the most position-sensitive grapheme in Portuguese ─────────
    # Word-initial: always voiceless [s]
    # Intervocalic: always voiced [z]  (casa [kazɐ])
    # Coda before voiceless C: [ʃ]  (estar [ɨʃtar])
    # Coda before voiced C: [ʒ]  (mesmo [meʒmu])
    # Word-final: [ʃ]  (gatos [gatuʃ])
    # Cross-word before vowel: [z]  (os amigos [uz‿ɐmiɡuʃ])
    "s": {
        GP.WORD_INITIAL: ["s"],
        GP.INTERVOCALIC: ["z"],
        GP.CODA: ["ʃ", "ʒ"],  # [ʃ] default; [ʒ] before voiced C
        GP.WORD_FINAL: ["ʃ"],
        GP.INTERVOCALIC_CROSS_WORD: ["z"],
    },
    # ── ⟨z⟩: voiced sibilant with coda devoicing ────────────────────────
    "z": {
        GP.DEFAULT: ["z"],
        GP.WORD_FINAL: ["ʃ"],  # devoiced and postalveolar in EP
        GP.CODA: ["ʒ", "ʃ"],
    },
    # ── ⟨r⟩: uvular vs. tap distribution ────────────────────────────────
    # Word-initial: uvular [ʁ]  (rato [ʁatu])
    # Intervocalic: tap [ɾ]  (caro [kaɾu])
    # Coda: tap [ɾ] or uvular depending on dialect
    "r": {
        GP.WORD_INITIAL: ["ʁ"],
        GP.INTERVOCALIC: ["ɾ"],
        GP.CODA: ["ɾ"],
        GP.ONSET: ["ɾ"],  # post-consonantal onset: tap (pr, tr, cr)
    },
    # ── ⟨l⟩: clear onset vs. dark/velarised coda ─────────────────────────
    "l": {
        GP.ONSET: ["l"],
        GP.CODA: ["ɫ"],  # velarised (dark l)
    },
    # ── Voiced stops: lenition intervocalically ──────────────────────────
    # Mateus & d'Andrade (2000): "voiced stops are realised as
    # approximants in intervocalic position in casual speech"
    "b": {
        GP.DEFAULT: ["b"],
        GP.INTERVOCALIC: ["β"],
    },
    "d": {
        GP.DEFAULT: ["d"],
        GP.INTERVOCALIC: ["ð"],
    },
    "g": {
        GP.DEFAULT: ["ɡ"],
        GP.INTERVOCALIC: ["ɣ"],
    },
    # ── ⟨e⟩: stressed vs. unstressed vowel reduction ────────────────────
    # Unstressed /e/ → [ɨ] or [ə] in EP (nucleus position = unstressed)
    "e": {
        GP.DEFAULT: ["e", "ɛ", "ə"],
        GP.NUCLEUS: ["ɨ", "ə"],  # unstressed reduction
    },
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

# Bisol (2005), Cristófaro Silva (2012).

POSITIONAL_PT_BR = {
    "s": {
        GP.WORD_INITIAL: ["s"],
        GP.INTERVOCALIC: ["z"],
        GP.CODA: ["s", "z"],  # alveolar [s] before voiceless, [z] before voiced
        GP.WORD_FINAL: ["s"],  # no postalveolar in most dialects
        GP.INTERVOCALIC_CROSS_WORD: ["z"],
    },
    "z": {
        GP.DEFAULT: ["z"],
        GP.WORD_FINAL: ["s"],  # devoiced: voz [vos]
        GP.CODA: ["z", "s"],
    },
    "r": {
        GP.WORD_INITIAL: ["h", "x", "ʁ"],  # glottal/velar dominant
        GP.INTERVOCALIC: ["ɾ"],
        GP.CODA: ["ɾ", "h", "x"],  # varies by dialect
        GP.ONSET: ["ɾ"],  # post-consonantal: tap
    },
    "l": {
        GP.ONSET: ["l"],
        GP.CODA: ["w"],  # l-vocalisation: [w]
    },
    # ── ⟨t⟩/⟨d⟩: palatalisation before /i/ (modelled as onset) ──────────
    # This is arguably the strongest north/south isogloss in Brazil
    "t": {
        GP.DEFAULT: ["t"],
        GP.ONSET: ["t", "tʃ"],  # [tʃ] before /i/
    },
    "d": {
        GP.DEFAULT: ["d"],
        GP.ONSET: ["d", "dʒ"],  # [dʒ] before /i/
    },
    "b": {
        GP.DEFAULT: ["b"],
        GP.INTERVOCALIC: ["β"],
    },
    "e": {
        GP.DEFAULT: ["e", "ɛ"],
        GP.WORD_FINAL: ["i"],  # final raising: leite [ˈlejtʃi]
    },
    "o": {
        GP.DEFAULT: ["o", "ɔ"],
        GP.WORD_FINAL: ["u"],  # final raising: livro [ˈlivɾu]
    },
}

# ── Carioca (pt-BR-x-rj): palatal coda sibilants like EP ────────────────
POSITIONAL_PT_BR_RJ = {
    **POSITIONAL_PT_BR,
    "s": {
        GP.WORD_INITIAL: ["s"],
        GP.INTERVOCALIC: ["z"],
        GP.CODA: ["ʃ", "ʒ"],  # palatal sibilants (unique in Brazil)
        GP.WORD_FINAL: ["ʃ"],
        GP.INTERVOCALIC_CROSS_WORD: ["z"],
    },
    "z": {
        GP.DEFAULT: ["z"],
        GP.WORD_FINAL: ["ʃ"],
        GP.CODA: ["ʒ", "ʃ"],
    },
}

# ── Caipira (pt-BR-x-caipira): retroflex coda r ─────────────────────────
POSITIONAL_PT_BR_CAIPIRA = {
    **POSITIONAL_PT_BR,
    "r": {
        GP.WORD_INITIAL: ["h", "x"],
        GP.INTERVOCALIC: ["ɾ"],
        GP.CODA: ["ɻ", "ɹ"],  # retroflex 'erre caipira'
        GP.ONSET: ["ɾ"],
    },
}

# ── Gaúcho/Sulista (pt-BR-x-sul): alveolar trill in onset ───────────────
POSITIONAL_PT_BR_SUL = {
    **POSITIONAL_PT_BR,
    "r": {
        GP.WORD_INITIAL: ["r", "ɾ"],  # alveolar trill or tap (not glottal)
        GP.INTERVOCALIC: ["ɾ"],
        GP.CODA: ["ɾ"],
        GP.ONSET: ["ɾ"],
    },
}

# ── Nordeste (Recife, Bahia, Ceará): no t/d palatalisation ──────────────
POSITIONAL_PT_BR_NE = {
    **POSITIONAL_PT_BR,
    "t": {
        GP.DEFAULT: ["t"],
        GP.ONSET: ["t"],  # NO palatalisation before /i/
    },
    "d": {
        GP.DEFAULT: ["d"],
        GP.ONSET: ["d"],  # NO palatalisation before /i/
    },
    # Pretonic vowel opening (Northeastern isogloss)
    "e": {
        GP.DEFAULT: ["ɛ", "e"],  # open pretonic /e/ → [ɛ]
        GP.WORD_FINAL: ["i"],
    },
    "o": {
        GP.DEFAULT: ["ɔ", "o"],  # open pretonic /o/ → [ɔ]
        GP.WORD_FINAL: ["u"],
    },
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
    "pt-PT": LanguageSpec(
        code="pt-PT",
        name="European Portuguese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_PT,
        allophones=ALLOPHONES_PT,
        parent="la-x-hispania",
        ancestors=(
            Ancestor("la-x-hispania", P, 0.78,
                     "Primary descent from Hispanic Vulgar Latin"),
            Ancestor("xlg", SUB, 0.05,
                     "Lusitanian substrate: possibly reinforced "
                     "preservation of /v/ distinct from /b/ (unlike Castilian)"),
            Ancestor("cel", SUB, 0.04,
                     "Celtic (Gallaecian) substrate in NW Iberia: "
                     "toponyms, possible influence on nasal vowel development"),
            Ancestor("xsb", SUP, 0.04,
                     "Suebi (Germanic) superstrate in Gallaecia (411-585 CE): "
                     "~200 place names, vocabulary (guerra, roubar, branco)"),
            Ancestor("got", SUP, 0.03,
                     "Visigothic superstrate shared with all Ibero-Romance"),
            Ancestor("xaa", AD, 0.06,
                     "Andalusi Arabic adstrate: ~1000 loanwords, "
                     "less influence than in Spanish due to earlier Reconquista"),
        ),
        notes=(
            "European Portuguese (PT-PT). Base mapping uses Lisbon standard. "
            "Digraphs per Acordo Ortográfico. Portuguese preserves the "
            "/v/~/b/ distinction (unique in Ibero-Romance — Castilian merged them). "
            "Nasal vowels and extreme vowel reduction are diagnostic features."
        ),
    ),
    "pt-BR": LanguageSpec(
        code="pt-BR",
        name="Brazilian Portuguese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_PT_BR,
        allophones=ALLOPHONES_PT_BR,
        parent="pt-PT",
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
        parent="pt-PT",
        notes="Based on Luanda educated speech.",
    ),
}
