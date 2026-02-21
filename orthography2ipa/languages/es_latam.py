"""Latin American Spanish dialects — grapheme→IPA and allophone mappings.

All Latin American varieties share seseo (no /θ/) and yeísmo (/ʎ/ → /ʝ/).
The major phonological axes of variation are: (1) coda /s/ treatment
(full retention → aspiration → deletion), (2) /x/ realisation
([x] vs [h]), (3) /ʝ/ strength, (4) liquid neutralisation, (5) final
consonant behaviour, (6) intonational patterns (not captured here).

Sources:
- Hualde, J.I. (2005). *The Sounds of Spanish*. CUP.
- Lipski, J.M. (1994). *Latin American Spanish*. Longman.
- RAE (2011). *Nueva gramática: Fonética y fonología*.
- Canfield, D.L. (1981). *Spanish Pronunciation in the Americas*. UCP.
- Moreno de Alba, J.G. (1994). *La pronunciación del español en México*.
- Piñeros, C.E. (2016). *The phonology of Spanish*. In: OUP Handbook.
- Quesada Pacheco, M.Á. (2010). *El español hablado en América Central*.

Conventions:
- All inherit base es-419 graphemes (seseo + yeísmo).
- Private-use subtags: es-{COUNTRY} or es-{COUNTRY}-x-{region}.
"""
from orthography2ipa.languages.es import GRAPHEMES_ES, ALLOPHONES_ES
from orthography2ipa.types import LanguageSpec

# Shared base: seseo + yeísmo
_GRAPHEMES_LA = {
    **GRAPHEMES_ES,
    "c": ["k", "s"],
    "z": ["s"],
    "ll": ["ʝ"],
    "y": ["ʝ", "i"],
}
_ALLOPHONES_LA = {
    **ALLOPHONES_ES,
    # no /θ/ phoneme
    "s": ["s", "z", "h"],  # aspiration in Caribbean, coda weakening
}

# ═══════════════════════════════════════════════════════════════════════════
# Mexican Spanish (es-MX)
# Highland (Mexico City) and Lowland (coasts) differ substantially
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_MX = {
    **ALLOPHONES_ES,
    # Highland Mexican: full /s/ in coda (conservative)
    "s": ["s", "z"],
    # /x/ fully velar [x] (not aspirated)
    "x": ["x"],
    # Strong affricate [tʃ] — very tense
    "tʃ": ["tʃ"],
    # /ʝ/ relatively weak, often approximant [ʝ̞]
    "ʝ": ["ʝ", "ɟʝ"],
    # Weakened unstressed vowels (devoicing, especially sentence-final)
    "e": ["e", "e̥"],
    "o": ["o", "o̥"],
    # Conservative /n/ — alveolar (no velarisation)
    "n": ["n", "m", "ŋ"],
    # Lenition
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
}

ALLOPHONES_MX_COAST = {
    **ALLOPHONES_MX,
    # Coastal Mexican (Veracruz, Tabasco, coasts): coda aspiration
    "s": ["s", "h", "z"],
    "x": ["x", "h"],
    # Liquid neutralisation in some coastal areas
    "l": ["l", "ɾ"],
    "n": ["n", "ŋ"],  # final velarisation
    "d": ["d", "ð", "∅"],  # -d deletion
}

# ═══════════════════════════════════════════════════════════════════════════
# Caribbean Spanish (es-CU, es-DO, es-PR)
# Shared: aspiration, velar [ŋ], liquid neutralisation, -d deletion
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_CARIB = {
    **ALLOPHONES_ES,
    # Coda aspiration — the defining Caribbean feature
    "s": ["s", "h", "∅"],
    # /x/ → [h] (glottal)
    "x": ["h"],
    # Liquid neutralisation (lambdacism/rhotacism)
    "l": ["l", "ɾ", "j"],  # /l/ → [ɾ] in coda (Puerto Rico)
    "ɾ": ["ɾ", "l"],  # /ɾ/ → [l] in coda (lateralisation, esp. PR)
    # Final /n/ velarisation — universal
    "n": ["n", "ŋ"],
    # -d- deletion
    "d": ["d", "ð", "∅"],
    # /r/ trill: various realisations
    "r": ["r", "ʁ", "x"],  # uvular in PR (erre puertorriqueña)
    # Lenition
    "b": ["b", "β"],
    "ɡ": ["ɡ", "ɣ"],
    "ʝ": ["ʝ", "ɟʝ"],
}

# Puerto Rico-specific: uvular /r/, extreme lateralisation
ALLOPHONES_PR = {
    **ALLOPHONES_CARIB,
    "r": ["ʁ", "χ", "r"],  # uvular dominant
    "ɾ": ["ɾ", "l"],  # coda lateralisation very strong
}

# Dominican-specific: extreme coda deletion, /s/ → ∅
ALLOPHONES_DO = {
    **ALLOPHONES_CARIB,
    "s": ["s", "h", "∅"],  # extreme: often fully deleted
    "d": ["d", "ð", "∅"],  # very frequent deletion
    "ɾ": ["ɾ", "i", "l"],  # coda /ɾ/ → [i] vocalisation in some speakers
    "r": ["r"],  # alveolar trill preserved
}

# Cuban-specific
ALLOPHONES_CU = {
    **ALLOPHONES_CARIB,
    "r": ["r"],  # alveolar trill (not uvular like PR)
    "s": ["s", "h", "∅"],
    "tʃ": ["tʃ", "ʃ"],  # some deaffrication in western Cuba
}

# ═══════════════════════════════════════════════════════════════════════════
# Central American Spanish
# Guatemala-Honduras-El Salvador-Nicaragua-Costa Rica-Panama
# ═══════════════════════════════════════════════════════════════════════════

# Guatemala/Honduras/El Salvador (conservative highland)
ALLOPHONES_GT = {
    **ALLOPHONES_ES,
    "s": ["s", "z"],  # coda /s/ largely retained (highland)
    "x": ["x", "h"],  # variable
    "tʃ": ["tʃ"],
    "ʝ": ["ʝ"],
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
    "n": ["n", "ŋ"],
}

# Nicaragua/Honduras lowland
ALLOPHONES_NI = {
    **ALLOPHONES_GT,
    "s": ["s", "h"],  # aspiration in lowlands
    "x": ["h"],  # aspirated
    "d": ["d", "ð", "∅"],
}

# Costa Rica
ALLOPHONES_CR = {
    **ALLOPHONES_ES,
    "s": ["s", "z"],  # Central Valley: coda preserved
    "x": ["x", "h"],
    # Distinctive: /rr/ → [ɹ] or [ɹ̝] (assibilated)
    "r": ["r", "ɹ̝", "ɹ"],  # assibilated /rr/ — Costa Rican hallmark
    "ɾ": ["ɾ", "ɹ"],  # assibilated in clusters too
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
    "n": ["n"],
    "ʝ": ["ʝ", "ɟʝ"],
}

# Panama
ALLOPHONES_PA = {
    **ALLOPHONES_CARIB,
    # Panamanian shares Caribbean aspiration features
    "s": ["s", "h", "∅"],
    "x": ["h"],
    "n": ["n", "ŋ"],
    "r": ["r"],
    "d": ["d", "ð", "∅"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Colombian Spanish (es-CO)
# Highly diverse: highland (Bogotá), coastal (Cartagena), paisa (Medellín)
# ═══════════════════════════════════════════════════════════════════════════

# Bogotá highland (rolo)
ALLOPHONES_CO_BOG = {
    **ALLOPHONES_ES,
    "s": ["s", "z"],  # coda /s/ fully retained
    "x": ["x", "h"],
    "ʝ": ["ʝ", "ɟʝ"],  # strong onset affrication
    "tʃ": ["tʃ"],
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
    "n": ["n"],  # alveolar (no velarisation)
}

# Colombian coast (costeño)
ALLOPHONES_CO_COAST = {
    **ALLOPHONES_CARIB,
    # Caribbean features: aspiration, velar /n/, liquid neutralisation
}

# Paisa (Medellín/Antioquia)
ALLOPHONES_CO_PAISA = {
    **ALLOPHONES_ES,
    "s": ["s", "z"],  # retained but with apicoalveolar tendency
    "x": ["x", "h"],
    "ʝ": ["ʝ", "ɟʝ"],  # strong affricate realisation
    "tʃ": ["tʃ"],
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
    "n": ["n"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Venezuelan Spanish (es-VE)
# Caribbean-type with strong aspiration
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_VE = {
    **ALLOPHONES_CARIB,
    "s": ["s", "h", "∅"],
    "x": ["h"],
    "n": ["n", "ŋ"],  # final velarisation
    "r": ["r"],  # alveolar trill
    "d": ["d", "ð", "∅"],
    "ʝ": ["ʝ", "ɟʝ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Andean Spanish (es-PE, es-BO, es-EC)
# Highland: conservative, Quechua substrate influence
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_ANDEAN = {
    **ALLOPHONES_ES,
    # Highland Andean: very conservative coda /s/
    "s": ["s", "z"],
    "x": ["x"],  # full velar
    # Possible /ʎ/ preservation (lleísmo) in rural areas
    "ʎ": ["ʎ", "ʝ"],  # some speakers retain [ʎ]
    # Assibilated /rr/ in some Andean varieties
    "r": ["r", "ɹ̝"],
    "ɾ": ["ɾ", "ɹ̝"],  # assibilated in clusters (Ecuador highland)
    # Quechua substrate: possible ejectives in bilingual speech (marginal)
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
    "tʃ": ["tʃ"],
    "n": ["n"],
    # Vowel raising/lowering from Quechua contact
    "e": ["e", "i"],  # /e/ → [i] in contact speakers
    "o": ["o", "u"],  # /o/ → [u] in contact speakers
}

# Peruvian coast (Lima)
ALLOPHONES_PE_LIMA = {
    **ALLOPHONES_ES,
    "s": ["s", "z"],  # coda retained
    "x": ["x", "h"],
    "ʝ": ["ʝ"],
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
    "n": ["n"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Chilean Spanish (es-CL)
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_CL = {
    **ALLOPHONES_ES,
    # Coda aspiration (moderate)
    "s": ["s", "h"],
    # /x/ → [x] (velar, not aspirated)
    "x": ["x", "ç"],  # [ç] before front vowels common in Chile
    # CH deaffrication in casual speech
    "tʃ": ["tʃ", "ʃ"],  # [ʃ] stigmatised but widespread
    # /ʝ/ variable
    "ʝ": ["ʝ", "ɟʝ"],
    # -d deletion
    "d": ["d", "ð", "∅"],
    # /r/ trill standard
    "r": ["r"],
    # Lenition
    "b": ["b", "β"],
    "ɡ": ["ɡ", "ɣ"],
    "n": ["n"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Paraguayan Spanish (es-PY)
# Guaraní substrate; unique phonological features
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_PY = {
    **_GRAPHEMES_LA,
    # Guaraní-influenced features: glottal stop, nasal vowels in loans
    "ll": ["ʝ", "ʒ"],  # žeísmo in some speakers (contact with Rioplatense)
}

ALLOPHONES_PY = {
    **ALLOPHONES_ES,
    "s": ["s", "z"],  # coda /s/ generally retained
    "x": ["x", "h"],
    "ʝ": ["ʝ", "ʒ"],  # žeísmo influence from Argentine contact
    # Guaraní substrate: prenasalised stops in bilingual speech
    "b": ["b", "β", "ᵐb"],  # prenasalisation in contact
    "d": ["d", "ð", "ⁿd"],
    "ɡ": ["ɡ", "ɣ", "ᵑɡ"],
    # /r/ standard alveolar trill
    "r": ["r"],
    "ɾ": ["ɾ"],
    # Guaraní substrate: possible glottal stop [ʔ] and nasal V in loans
    "n": ["n"],
    "tʃ": ["tʃ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Uruguayan Spanish (es-UY)
# Rioplatense base with some distinctive features
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_UY = {
    **ALLOPHONES_ES,
    "s": ["s", "z"],  # less aspiration than Caribbean
    "x": ["x"],
    # Žeísmo / šeísmo (shared with Buenos Aires)
    "ʝ": ["ʃ", "ʒ"],  # devoicing trend
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
    "r": ["r"],
    "n": ["n"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Rioplatense Spanish (es-AR)
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_ES_AR = {
    **_GRAPHEMES_LA,
    "ll": ["ʃ", "ʒ"],  # žeísmo / šeísmo
    "y": ["ʃ", "ʒ", "i"],
}

ALLOPHONES_ES_AR = {
    **_ALLOPHONES_LA,
    "ʝ": ["ʃ", "ʒ"],  # devoiced in younger Buenos Aires speakers
}


# ═══════════════════════════════════════════════════════════════════════════
# Equatoguinean Spanish (es-GQ)
# Only Spanish-speaking country in Africa; Bantu substrate
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_GQ = {
    **ALLOPHONES_ES,
    "s": ["s", "z"],  # seseo, coda retained
    "x": ["x"],
    # Bantu substrate: possible prenasalisation, tonal influence (not captured)
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
    # Distinction between /ɾ/ and /r/ can be weak
    "ɾ": ["ɾ", "r"],
    "r": ["r", "ɾ"],
    "ʝ": ["ʝ", "ɟʝ"],
    "n": ["n"],
    "tʃ": ["tʃ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Specs
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {

    "es-419": LanguageSpec(
        code="es-419",
        name="Latin American Spanish",
        family="Romance",
        script="Latin",
        graphemes=_GRAPHEMES_LA,
        allophones=_ALLOPHONES_LA,
        parent="es-ES",
        notes="Seseo, yeísmo. Coda /s/ aspiration noted in allophone map.",
    ),

    # --- Mexico ---
    "es-MX": LanguageSpec(
        code="es-MX", name="Mexican Spanish (Highland)",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_MX, parent="es-ES",
        notes=(
            "Highland Mexican (Mexico City / Central Plateau). Conservative: "
            "full coda /s/, velar [x], no aspiration. Distinctive unstressed "
            "vowel devoicing (especially sentence-finally). Very tense [tʃ]. "
            "Weak approximant [ʝ̞]. Largest Spanish-speaking country."
        ),
    ),
    "es-MX-x-costa": LanguageSpec(
        code="es-MX-x-costa", name="Mexican Spanish (Coastal)",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_MX_COAST, parent="es-ES",
        notes=(
            "Coastal Mexican (Veracruz, Tabasco, Gulf/Pacific lowlands). "
            "Caribbean-influenced: coda /s/ aspiration, /x/ → [h], "
            "final /n/ velarisation, some liquid neutralisation."
        ),
    ),
    # --- Caribbean ---
    "es-CU": LanguageSpec(
        code="es-CU", name="Cuban Spanish",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_CU, parent="es-ES",
        notes=(
            "Cuban Spanish. Caribbean type: coda aspiration/deletion, "
            "/x/ → [h], final [ŋ], -d deletion. Some deaffrication of "
            "[tʃ] → [ʃ] in western Cuba. Liquid neutralisation. "
            "Heavy Canarian substrate historically."
        ),
    ),
    "es-DO": LanguageSpec(
        code="es-DO", name="Dominican Spanish",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_DO, parent="es-ES",
        notes=(
            "Dominican Spanish. Most extreme Caribbean phonology: "
            "pervasive coda /s/ deletion, heavy -d deletion, "
            "coda /ɾ/ vocalisation to [i] (puerta → [ˈpweita]) in "
            "Cibaeño dialect. Final [ŋ]. /x/ → [h]."
        ),
    ),
    "es-PR": LanguageSpec(
        code="es-PR", name="Puerto Rican Spanish",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_PR, parent="es-ES",
        notes=(
            "Puerto Rican Spanish. Caribbean base with distinctive "
            "uvular /rr/ [ʁ~χ] ('erre puertorriqueña'), extreme coda "
            "/ɾ/ → [l] lateralisation (comer → [koˈmel]), coda aspiration, "
            "/x/ → [h], final [ŋ]. Strong English contact influence."
        ),
    ),
    "es-VE": LanguageSpec(
        code="es-VE", name="Venezuelan Spanish",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_VE, parent="es-ES",
        notes=(
            "Venezuelan Spanish. Caribbean type: coda aspiration, "
            "/x/ → [h], final [ŋ], -d deletion. Alveolar trill [r] "
            "preserved. Interior highland zones more conservative."
        ),
    ),
    # --- Central America ---
    "es-GT": LanguageSpec(
        code="es-GT", name="Guatemalan Spanish",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_GT, parent="es-ES",
        notes=(
            "Guatemalan/highland Central American Spanish. Conservative: "
            "coda /s/ largely retained, velar [x]. Mayan substrate "
            "influence in bilingual areas (glottalisation, vowel length)."
        ),
    ),
    "es-NI": LanguageSpec(
        code="es-NI", name="Nicaraguan Spanish",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_NI, parent="es-ES",
        notes=(
            "Nicaraguan/lowland Central American Spanish. Coda aspiration, "
            "/x/ → [h], -d deletion. Voseo universal (shared with most "
            "Central American varieties). Transitional between highland "
            "conservative and Caribbean patterns."
        ),
    ),
    "es-CR": LanguageSpec(
        code="es-CR", name="Costa Rican Spanish",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_CR, parent="es-ES",
        notes=(
            "Costa Rican Spanish. Distinctive assibilated /rr/ → [ɹ̝] "
            "or [ɹ] (the 'erre tica') — strongest diagnostic feature. "
            "Central Valley: coda /s/ conserved. Rural: more aspiration. "
            "Assibilation also in clusters (tres → [tɹ̝es])."
        ),
    ),
    "es-PA": LanguageSpec(
        code="es-PA", name="Panamanian Spanish",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_PA, parent="es-ES",
        notes=(
            "Panamanian Spanish. Caribbean type: aspiration, /x/ → [h], "
            "final [ŋ], -d deletion. Canal Zone English contact influence. "
            "Transitional between Central American and Caribbean."
        ),
    ),
    # --- Colombia ---
    "es-CO": LanguageSpec(
        code="es-CO", name="Colombian Spanish (Bogotá)",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_CO_BOG, parent="es-ES",
        notes=(
            "Bogotá highland Spanish (rolo). Very conservative: full coda "
            "/s/, alveolar /n/, no aspiration. Strong [ɟʝ] affricate for "
            "/ʝ/. Often cited as one of the 'clearest' Latin American varieties. "
            "The standard reference for Colombian media."
        ),
    ),
    "es-CO-x-costa": LanguageSpec(
        code="es-CO-x-costa", name="Colombian Spanish (Coastal)",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_CO_COAST, parent="es-ES",
        notes=(
            "Colombian coastal (costeño — Cartagena, Barranquilla, Santa Marta). "
            "Full Caribbean phonology: aspiration, [ŋ], liquid neutralisation, "
            "-d deletion. Phonologically divergent from Bogotá highland."
        ),
    ),
    "es-CO-x-paisa": LanguageSpec(
        code="es-CO-x-paisa", name="Colombian Spanish (Paisa/Medellín)",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_CO_PAISA, parent="es-ES",
        notes=(
            "Paisa/Antioqueño (Medellín). Conservative coda /s/, strong "
            "[ɟʝ] affrication, distinctive voseo. Sometimes apicoalveolar "
            "sibilant tendency. Melodic intonation (not captured here)."
        ),
    ),
    # --- Andean ---
    "es-PE": LanguageSpec(
        code="es-PE", name="Peruvian Spanish (Andean)",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_ANDEAN, parent="es-ES",
        notes=(
            "Andean Peruvian Spanish (highland). Very conservative: full "
            "coda /s/, velar [x]. Possible /ʎ/ retention in rural lleísta "
            "areas. Quechua substrate: vowel raising (/e,o/ → [i,u] in "
            "bilingual speakers), some assibilated /rr/."
        ),
    ),
    "es-PE-x-lima": LanguageSpec(
        code="es-PE-x-lima", name="Peruvian Spanish (Lima)",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_PE_LIMA, parent="es-ES",
        notes=(
            "Lima coastal Peruvian Spanish. Conservative coda /s/, "
            "yeísmo universal (no /ʎ/). Less Quechua influence than "
            "highland. Standard reference for Peruvian media."
        ),
    ),
    "es-BO": LanguageSpec(
        code="es-BO", name="Bolivian Spanish",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_ANDEAN, parent="es-ES",
        notes=(
            "Bolivian Spanish (highland). Andean type: conservative coda "
            "/s/, velar [x], possible /ʎ/ in rural areas, assibilated /rr/. "
            "Quechua/Aymara substrate: vowel raising in bilinguals. "
            "Lowland (Santa Cruz) tends toward more aspiration."
        ),
    ),
    "es-EC": LanguageSpec(
        code="es-EC", name="Ecuadorian Spanish",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_ANDEAN, parent="es-ES",
        notes=(
            "Ecuadorian Spanish (highland, Quito). Andean type: conservative "
            "coda /s/, assibilated /rr/ → [ɹ̝] in highland. Quechua "
            "substrate vowel influence. Coastal (Guayaquil) → aspiration "
            "and Caribbean-type features."
        ),
    ),
    # --- Southern Cone ---
    "es-CL": LanguageSpec(
        code="es-CL", name="Chilean Spanish",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_CL, parent="es-ES",
        notes=(
            "Chilean Spanish. Moderate coda aspiration. /x/ → [x] with "
            "[ç] allophone before front vowels (gente [ˈçente]) — distinctive "
            "Chilean feature. Deaffrication [tʃ] → [ʃ] in casual speech "
            "(stigmatised). -d deletion common. Distinctive intonation."
        ),
    ),
    "es-PY": LanguageSpec(
        code="es-PY", name="Paraguayan Spanish",
        family="Romance", script="Latin",
        graphemes=GRAPHEMES_PY, allophones=ALLOPHONES_PY, parent="es-ES",
        notes=(
            "Paraguayan Spanish. Uniquely influenced by Guaraní bilingualism "
            "(90%+ of population bilingual). Guaraní substrate: prenasalised "
            "stops [ᵐb, ⁿd, ᵑɡ] in contact speech, possible glottal stop "
            "and nasal vowels in Guaraní loans. Some žeísmo from Argentine "
            "influence. Coda /s/ generally conserved."
        ),
    ),
    "es-UY": LanguageSpec(
        code="es-UY", name="Uruguayan Spanish",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_UY, parent="es-ES",
        notes=(
            "Uruguayan Spanish. Rioplatense base: žeísmo/šeísmo for "
            "⟨ll⟩/⟨y⟩ (devoicing trend toward [ʃ] in younger speakers). "
            "Less extreme than Buenos Aires in some features. "
            "Border dialects show Portuguese influence (DPU — Dialectos "
            "Portugueses del Uruguay)."
        ),
    ),
    # Argentina
    "es-AR": LanguageSpec(
        code="es-AR",
        name="Rioplatense Spanish",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_ES_AR,
        allophones=ALLOPHONES_ES_AR,
        parent="es-ES",
        notes="Buenos Aires / Rioplatense: žeísmo/šeísmo for ⟨ll⟩/⟨y⟩.",
    ),
    # --- Equatorial Guinea ---
    "es-GQ": LanguageSpec(
        code="es-GQ", name="Equatoguinean Spanish",
        family="Romance", script="Latin",
        graphemes=_GRAPHEMES_LA, allophones=ALLOPHONES_GQ, parent="es-ES",
        notes=(
            "Equatoguinean Spanish. Only Spanish-speaking country in "
            "sub-Saharan Africa. Bantu substrate (Fang, Bubi): possible "
            "prenasalisation, weakened /ɾ/-/r/ distinction. Seseo, yeísmo. "
            "Conservative in many features. Tonal influence from substrate "
            "languages (suprasegmental, not captured here)."
        ),
    ),
}
