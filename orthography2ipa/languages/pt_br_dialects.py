"""Brazilian Portuguese dialects — grapheme→IPA and allophone mappings.

Brazil's dialectal landscape is traditionally divided into two macro-zones
(Nascentes 1953): Northern (Amazônico, Nordestino, Baiano) and Southern
(Fluminense, Mineiro, Sulista, Paulistano, Caipira, Brasiliense).

Major axes of variation: (1) rhotic realisation, (2) /t,d/ palatalisation,
(3) coda /s/ (alveolar vs palatal), (4) /l/ vocalisation, (5) vowel
raising patterns, (6) prosody/rhythm (not captured here).

Sources:
- Bisol, L. (2005). *Introdução a estudos de fonologia do PB*. EDIPUCRS.
- Cristófaro Silva, T. (2012). *Fonética e fonologia do português*. Contexto.
- Cardoso, S.A. et al. (2014). *Atlas Linguístico do Brasil* (ALiB).
- Noll, V. (2008). *O português brasileiro*. Globo.
- Callou, D. & Leite, Y. (2002). "As vogais pretônicas no PB."
- Bortoni-Ricardo, S.M. (2004). *Educação em língua materna*.

Conventions:
- All inherit base pt-BR graphemes from pt.py.
- Codes: pt-BR-x-{region}.
"""
from orthography2ipa.languages.pt import (
    GRAPHEMES_PT_BR,
    ALLOPHONES_PT_BR,
)
from orthography2ipa.types import LanguageSpec

# ═══════════════════════════════════════════════════════════════════════════
# Paulistano (São Paulo city) — the prestige urban standard
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_SP = {
    **ALLOPHONES_PT_BR,
    # /t,d/ palatalisation before /i/ — fully systematic
    "t": ["t", "tʃ"],
    "d": ["d", "dʒ"],
    # /r/ onset: velar/glottal dominant
    "ʁ": ["h", "x", "ɦ"],
    # Coda /r/: TAP [ɾ] preserved in educated SP speech (not retroflex)
    "ɾ": ["ɾ"],
    # Coda /l/ → [w] universal
    "ɫ": ["w"],
    # Coda /s/: alveolar [s, z] (NOT palatal [ʃ, ʒ])
    "s": ["s"],
    "z": ["z"],
    # /ʎ/ preserved
    "ʎ": ["ʎ"],
    # Vowels: standard Brazilian open/closed distinction
    "ə": ["i"],  # final unstressed /e/ → [i]
}

# ═══════════════════════════════════════════════════════════════════════════
# Caipira (São Paulo interior / Minas Gerais west / Goiás / Mato Grosso)
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_CAIPIRA = {
    **ALLOPHONES_PT_BR,
    "t": ["t", "tʃ"],
    "d": ["d", "dʒ"],
    # Hallmark: retroflex rhotic [ɻ] in coda and clusters
    "ʁ": ["h", "x"],
    "ɾ": ["ɻ", "ɹ", "ɾ"],  # retroflex approximant — the 'erre caipira'
    # Coda /l/ → [w]
    "ɫ": ["w"],
    # Coda /s/ alveolar
    "s": ["s"],
    "z": ["z"],
    # /ʎ/ → [j] in some rural areas (depalatalisation)
    "ʎ": ["ʎ", "j"],
    "ɲ": ["ɲ", "j̃"],  # [j̃] in very rural speech
    # Vowel raising less systematic than urban
    "ə": ["i", "e"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Carioca (Rio de Janeiro)
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_RJ = {
    **ALLOPHONES_PT_BR,
    # Hallmark: palatal sibilants in coda [ʃ, ʒ] (like European Portuguese!)
    "s": ["s", "ʃ"],  # coda: [ʃ] before voiceless C / pause
    "z": ["z", "ʒ"],  # coda: [ʒ] before voiced C
    # /t,d/ palatalisation before /i/ — full
    "t": ["t", "tʃ"],
    "d": ["d", "dʒ"],
    # /r/ onset: velar/uvular [x, χ]
    "ʁ": ["x", "χ", "h"],
    # Coda /r/: aspirated [h] or [x] (NOT tap)
    "ɾ": ["ɾ", "h", "x"],  # coda: aspiration; intervocalic: tap
    # Coda /l/ → [w]
    "ɫ": ["w"],
    # /ʎ/ preserved in educated speech
    "ʎ": ["ʎ"],
    "ə": ["i"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Fluminense (Rio de Janeiro state, broader — differs from Carioca city)
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_FLUM = {
    **ALLOPHONES_RJ,
    # Same palatal sibilants as Carioca but may be less systematic
    # in rural areas of Rio de Janeiro state
    "s": ["s", "ʃ"],
    "z": ["z", "ʒ"],
    # Some speakers lack full /t,d/ palatalisation
    "t": ["t", "tʃ"],
    "d": ["d", "dʒ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Mineiro (Minas Gerais — Belo Horizonte)
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_MG = {
    **ALLOPHONES_PT_BR,
    "t": ["t", "tʃ"],
    "d": ["d", "dʒ"],
    # /r/ onset: velar/glottal
    "ʁ": ["h", "x"],
    # Coda /r/: variable — retroflex [ɻ] in interior, tap in BH city
    "ɾ": ["ɾ", "ɻ", "ɹ"],
    "ɫ": ["w"],
    # Coda /s/: alveolar (like SP)
    "s": ["s"],
    "z": ["z"],
    # Hallmark: extreme vowel raising and word-final reduction
    # uai (interjection) as cultural marker
    "ə": ["i"],
    "o": ["o", "u"],  # pretonic raising more systematic
    "e": ["e", "i"],  # pretonic raising
    "ʎ": ["ʎ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Nordestino (Northeast — Recife, Salvador, Fortaleza, etc.)
# Divided into Recife-type and Bahian-type
# ═══════════════════════════════════════════════════════════════════════════

# Recife / Pernambucano
ALLOPHONES_NE_RECIFE = {
    **ALLOPHONES_PT_BR,
    # NO /t,d/ palatalisation — defining Northeastern feature
    "t": ["t"],  # [t] even before /i/: tia → [ˈtia] NOT [ˈtʃia]
    "d": ["d"],
    # /r/ onset: velar/glottal
    "ʁ": ["h", "x", "ɦ"],
    # Coda /r/: glottal [h] or tap [ɾ]
    "ɾ": ["ɾ", "h"],
    "ɫ": ["w"],
    # Coda /s/ alveolar
    "s": ["s"],
    "z": ["z"],
    # Pretonic vowel: open realisation — NOT raised
    # /e/ pretonic → [ɛ], /o/ pretonic → [ɔ] (opposite of southern raising)
    "e": ["e", "ɛ"],
    "o": ["o", "ɔ"],
    "ə": ["i"],
    "ʎ": ["ʎ"],
}

# Bahian (Salvador)
ALLOPHONES_NE_BAHIA = {
    **ALLOPHONES_PT_BR,
    # NO /t,d/ palatalisation
    "t": ["t"],
    "d": ["d"],
    "ʁ": ["h", "x"],
    "ɾ": ["ɾ", "h"],
    "ɫ": ["w"],
    # Coda /s/: alveolar
    "s": ["s"],
    "z": ["z"],
    # Open pretonic vowels
    "e": ["e", "ɛ"],
    "o": ["o", "ɔ"],
    "ə": ["i"],
    # /ʎ/ preserved but weakening
    "ʎ": ["ʎ", "j"],
}

# Cearense (Fortaleza)
ALLOPHONES_NE_CE = {
    **ALLOPHONES_NE_RECIFE,
    # Similar to Recife but with some specific features:
    # /t,d/ NOT palatalised
    "t": ["t"],
    "d": ["d"],
    # Open pretonic vowels
    "e": ["e", "ɛ"],
    "o": ["o", "ɔ"],
    # Coda /s/ aspiration tendency in some contexts
    "s": ["s", "h"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Nortista / Amazônico (Belém, Manaus, Amazon region)
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_NORTE = {
    **ALLOPHONES_PT_BR,
    # NO /t,d/ palatalisation (like Northeast)
    "t": ["t"],
    "d": ["d"],
    # /r/ onset: velar/glottal
    "ʁ": ["h", "x"],
    "ɾ": ["ɾ"],
    "ɫ": ["w"],
    # Coda /s/ alveolar
    "s": ["s"],
    "z": ["z"],
    # Open pretonic vowels (like Northeast)
    "e": ["e", "ɛ"],
    "o": ["o", "ɔ"],
    "ə": ["i"],
    "ʎ": ["ʎ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Sulista (Southern — Porto Alegre / gaúcho)
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_SUL = {
    **ALLOPHONES_PT_BR,
    # /t,d/ palatalisation: VARIABLE — some speakers palatalise, some don't
    "t": ["t", "tʃ"],
    "d": ["d", "dʒ"],
    # /r/ onset: alveolar trill [r] or tap — NOT glottal (archaic pattern)
    "ʁ": ["r", "ɾ", "h"],  # [r] trill still alive in gaúcho speech
    "ɾ": ["ɾ"],
    "ɫ": ["w"],
    # Coda /s/: alveolar
    "s": ["s"],
    "z": ["z"],
    # Vowels: less raising than SP, more European-like
    "e": ["e"],
    "o": ["o"],
    "ə": ["e", "i"],  # less systematic raising of final /e/
    "ʎ": ["ʎ"],
}

# Curitibano / Paranaense
ALLOPHONES_PR_BR = {
    **ALLOPHONES_PT_BR,
    "t": ["t", "tʃ"],
    "d": ["d", "dʒ"],
    "ʁ": ["h", "x", "ɾ"],  # mixed: some tap in onset (transitional)
    "ɾ": ["ɾ"],
    "ɫ": ["w"],
    "s": ["s"],
    "z": ["z"],
    "e": ["e"],
    "o": ["o"],
    "ə": ["i"],
    "ʎ": ["ʎ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Brasiliense (Brasília — the planned capital's emerging dialect)
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_BSB = {
    **ALLOPHONES_PT_BR,
    # Mix of all regions (planned city, migrants from everywhere)
    # Dominant pattern: SP/southeastern with some Northeastern features
    "t": ["t", "tʃ"],
    "d": ["d", "dʒ"],
    "ʁ": ["h", "x"],
    "ɾ": ["ɾ"],
    "ɫ": ["w"],
    "s": ["s"],
    "z": ["z"],
    "e": ["e"],
    "o": ["o"],
    "ə": ["i"],
    "ʎ": ["ʎ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Specs
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "pt-BR-x-sp": LanguageSpec(
        code="pt-BR-x-sp", name="Paulistano Portuguese",
        family="Romance", script="Latin",
        graphemes=GRAPHEMES_PT_BR, allophones=ALLOPHONES_SP, parent="pt-BR",
        notes=(
            "São Paulo city (paulistano). Urban prestige standard for "
            "southeastern Brazil. Full /t,d/ → [tʃ,dʒ] palatalisation "
            "before /i/. Onset /r/ → [h,x]. Coda /r/ → tap [ɾ] "
            "(NOT retroflex). Coda /s/ alveolar [s,z] (NOT palatal). "
            "Coda /l/ → [w]. Dominates Brazilian media alongside Carioca."
        ),
    ),
    "pt-BR-x-caipira": LanguageSpec(
        code="pt-BR-x-caipira", name="Caipira Portuguese",
        family="Romance", script="Latin",
        graphemes=GRAPHEMES_PT_BR, allophones=ALLOPHONES_CAIPIRA, parent="pt-BR",
        notes=(
            "Caipira (SP interior, western MG, Goiás, MS, MT). Hallmark: "
            "retroflex rhotic [ɻ/ɹ] in coda and clusters — the 'erre caipira' "
            "or 'erre retroflexo'. Possibly the oldest Brazilian rhotic "
            "pattern. Depalatalisation of /ʎ/ → [j] in rural speech. "
            "Full /t,d/ palatalisation. /r/ onset → [h,x]."
        ),
    ),
    "pt-BR-x-rj": LanguageSpec(
        code="pt-BR-x-rj", name="Carioca Portuguese",
        family="Romance", script="Latin",
        graphemes=GRAPHEMES_PT_BR, allophones=ALLOPHONES_RJ, parent="pt-BR",
        notes=(
            "Carioca (Rio de Janeiro city). Hallmark: palatal sibilants "
            "in coda [ʃ,ʒ] — shared with European Portuguese but unique "
            "in Brazil (mesmo → [ˈmeʒmu], paz → [ˈpaʃ]). Onset /r/ → "
            "[x,χ] (strong velar/uvular). Coda /r/ → aspiration [h]. "
            "Full /t,d/ palatalisation. The 'standard accent' for "
            "Brazilian TV/media alongside Paulistano."
        ),
    ),
    "pt-BR-x-fluminense": LanguageSpec(
        code="pt-BR-x-fluminense", name="Fluminense Portuguese",
        family="Romance", script="Latin",
        graphemes=GRAPHEMES_PT_BR, allophones=ALLOPHONES_FLUM, parent="pt-BR",
        notes=(
            "Fluminense (Rio de Janeiro state, broader than Carioca city). "
            "Shares palatal coda sibilants [ʃ,ʒ] with Carioca but may be "
            "less consistent in rural areas. Palatalisation variable."
        ),
    ),
    "pt-BR-x-mg": LanguageSpec(
        code="pt-BR-x-mg", name="Mineiro Portuguese",
        family="Romance", script="Latin",
        graphemes=GRAPHEMES_PT_BR, allophones=ALLOPHONES_MG, parent="pt-BR",
        notes=(
            "Mineiro (Minas Gerais, centred on Belo Horizonte). Transitional "
            "between Paulistano and Caipira: retroflex [ɻ] in interior, "
            "tap [ɾ] in BH city. Strong pretonic vowel raising. "
            "Full /t,d/ palatalisation. Cultural marker: 'uai' interjection. "
            "Alveolar coda /s/."
        ),
    ),
    "pt-BR-x-recife": LanguageSpec(
        code="pt-BR-x-recife", name="Pernambucano Portuguese",
        family="Romance", script="Latin",
        graphemes=GRAPHEMES_PT_BR, allophones=ALLOPHONES_NE_RECIFE, parent="pt-BR",
        notes=(
            "Pernambucano (Recife). Northeastern type. Defining features: "
            "NO /t,d/ palatalisation (tia → [ˈtia], dia → [ˈdia]), "
            "open pretonic vowels (/e/ → [ɛ], /o/ → [ɔ]: menino → "
            "[mɛˈninu]). These two features are the strongest north/south "
            "isoglosses in Brazilian Portuguese."
        ),
    ),
    "pt-BR-x-bahia": LanguageSpec(
        code="pt-BR-x-bahia", name="Bahian Portuguese",
        family="Romance", script="Latin",
        graphemes=GRAPHEMES_PT_BR, allophones=ALLOPHONES_NE_BAHIA, parent="pt-BR",
        notes=(
            "Bahian (Salvador). Northeastern type: no /t,d/ palatalisation, "
            "open pretonic vowels. Some /ʎ/ → [j] weakening. /r/ onset → "
            "[h,x]. Historically the cultural capital of colonial Brazil; "
            "distinctive Afro-Brazilian prosodic influence."
        ),
    ),
    "pt-BR-x-ce": LanguageSpec(
        code="pt-BR-x-ce", name="Cearense Portuguese",
        family="Romance", script="Latin",
        graphemes=GRAPHEMES_PT_BR, allophones=ALLOPHONES_NE_CE, parent="pt-BR",
        notes=(
            "Cearense (Fortaleza). Northeastern type: no palatalisation, "
            "open pretonic vowels. Some tendency toward coda /s/ aspiration "
            "[h] in certain contexts (less systematic than Carioca chiado). "
            "Distinctive melodic prosody."
        ),
    ),
    "pt-BR-x-norte": LanguageSpec(
        code="pt-BR-x-norte", name="Nortista/Amazônico Portuguese",
        family="Romance", script="Latin",
        graphemes=GRAPHEMES_PT_BR, allophones=ALLOPHONES_NORTE, parent="pt-BR",
        notes=(
            "Nortista/Amazônico (Belém, Manaus, Amazon region). No /t,d/ "
            "palatalisation, open pretonic vowels (like Northeast). "
            "Indigenous language substrate influence in some lexical and "
            "prosodic features. Tupí/Nheengatu contact."
        ),
    ),
    "pt-BR-x-sul": LanguageSpec(
        code="pt-BR-x-sul", name="Sulista/Gaúcho Portuguese",
        family="Romance", script="Latin",
        graphemes=GRAPHEMES_PT_BR, allophones=ALLOPHONES_SUL, parent="pt-BR",
        notes=(
            "Sulista/Gaúcho (Porto Alegre, RS). Distinctive: alveolar "
            "trill [r] or tap in onset position (NOT glottal) — the most "
            "European-sounding Brazilian rhotic. /t,d/ palatalisation "
            "variable (generational shift toward palatalisation). "
            "Less vowel raising. Italian/German settler substrate "
            "influence in some communities."
        ),
    ),
    "pt-BR-x-pr": LanguageSpec(
        code="pt-BR-x-pr", name="Curitibano/Paranaense Portuguese",
        family="Romance", script="Latin",
        graphemes=GRAPHEMES_PT_BR, allophones=ALLOPHONES_PR_BR, parent="pt-BR",
        notes=(
            "Curitibano/Paranaense (Curitiba, Paraná). Transitional between "
            "Sulista and Paulistano. /t,d/ palatalisation present. "
            "Mixed rhotic patterns (some onset tap). Alveolar coda /s/. "
            "Slavic/Italian settler substrate in some phonetic features."
        ),
    ),
    "pt-BR-x-brasilia": LanguageSpec(
        code="pt-BR-x-brasilia", name="Brasiliense Portuguese",
        family="Romance", script="Latin",
        graphemes=GRAPHEMES_PT_BR, allophones=ALLOPHONES_BSB, parent="pt-BR",
        notes=(
            "Brasiliense (Brasília). Emerging koiné dialect of the planned "
            "capital (inaugurated 1960). Mix of features from all regions "
            "due to migrant population. Tends toward southeastern standard "
            "(SP/MG) with some Northeastern features from Goiás substrate. "
            "Full /t,d/ palatalisation. /r/ onset → [h,x]."
        ),
    ),
}
