"""Portuguese regional dialects — grapheme→IPA and allophone mappings.

Covers the major dialectal zones of European Portuguese (mainland + insular)
as identified in phonological atlas data (18 localities). Each spec inherits
the base PT-PT graphemes and overrides/extends allophones to capture the
diagnostic features of each zone.

Sources:
- Phonological Atlas of Portuguese Dialects (18 regional speech samples).
- Cintra, L.F.L. (1971). "Nova proposta de classificação dos dialectos
  galego-portugueses."
- Segura, L. & Saramago, J. (2001). "Variedades dialetais portuguesas."
- Mateus, M.H. & d'Andrade, E. (2000). *The Phonology of Portuguese*.
- Brissos, F. (2014). "Dialectos portugueses do Centro-Sul."

Conventions:
- All codes use the private-use subtag format: pt-PT-x-{region}.
- Graphemes are inherited from base PT-PT; dialect-specific graphemes
  are added only where orthographic conventions genuinely differ.
- Allophone maps capture the systematic surface realisations documented
  for each zone, extending the base PT-PT inventory.
"""
# Import base PT-PT mappings
from orthography2ipa.languages.pt import GRAPHEMES_PT, ALLOPHONES_PT, POSITIONAL_PT_PT
from orthography2ipa.types import LanguageSpec

# ═══════════════════════════════════════════════════════════════════════════
# Shared allophone sets for dialect groups
# ═══════════════════════════════════════════════════════════════════════════

# --- Northern retroflex extensions (Porto, Braga, Viana, Aveiro) ---
_NORTHERN_RETROFLEX_ALLOPHONES = {
    "s": ["s"],
    "z": ["z"],
    "ʃ": ["ʃ", "ʂ"],  # coda /ʃ/ → [ʂ] in many northern environments
    "ʒ": ["ʒ", "ʐ"],  # coda /ʒ/ → [ʐ] before voiced C
}

# --- Northern uvular extensions ---
_NORTHERN_UVULAR_ALLOPHONES = {
    "ʁ": ["ʁ", "χ", "x"],  # voiceless uvular [χ] in coda, velar [x] in some areas
}

# ═══════════════════════════════════════════════════════════════════════════
# 1. Northern Interior — Minho (Vizela, Braga)
#    Extreme vowel reduction, voiceless uvular [χ], retroflex traces
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_MINHO = {
    **ALLOPHONES_PT,
    # Extreme vowel reduction — unstressed vowels devoice or delete
    "ɐ": ["ɐ", "ɐ̥", "∅"],
    "ə": ["ə", "ɨ", "ɨ̥", "∅"],
    "u": ["u", "u̥", "∅"],
    # Uvular: voiceless dominant in coda
    "ʁ": ["ʁ", "χ"],
    "ɾ": ["ɾ", "ɽ"],  # retroflex flap attested (Vizela)
    # Retroflex sibilants in coda
    "ʃ": ["ʃ", "ʂ"],
    "ʒ": ["ʒ", "ʐ"],
    # Stops: slight aspiration traces in Vizela
    "t": ["t", "tʰ"],
    "k": ["k"],
    "p": ["p"],
    # Lenition (universal but strongest here)
    "b": ["b", "β"],
    "d": ["d", "ð", "∅"],
    "ɡ": ["ɡ", "ɣ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# 2. Northern Litoral — Porto city
#    Heavy vowel reduction, velarized laterals, uvular variation
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_PORTO = {
    **ALLOPHONES_PT,
    # Vowel reduction (heavy but less extreme than Minho interior)
    "ɐ": ["ɐ", "ɐ̥"],
    "ə": ["ə", "ɨ", "∅"],
    # Uvular variation
    "ʁ": ["ʁ", "χ", "ʀ", "x"],  # Gaia: uvular trill [ʀ] and velar [x]
    # Retroflex sibilants (moderate in Gaia/Alvarenga)
    "ʃ": ["ʃ", "ʂ"],
    "ʒ": ["ʒ", "ʐ"],
    # Strong lenition
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
    # Laterals
    "l": ["l"],
    "ɫ": ["ɫ"],  # heavily velarised in coda
}

# ═══════════════════════════════════════════════════════════════════════════
# 3. Greater Porto — Alfena vowel-breaking zone
#    Unique centering diphthongization [ɛ͡ɐ, ɔ͡ɐ, e͡ɐ, o͡ɐ]
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_ALFENA = {
    **ALLOPHONES_PORTO,
    # Vowel breaking — mid vowels develop centering offglide under stress
    "ɛ": ["ɛ", "ɛ͡ɐ"],
    "ɔ": ["ɔ", "ɔ͡ɐ"],
    "e": ["e", "e͡ɐ"],
    "o": ["o", "o͡ɐ"],
    "ẽ": ["ẽ", "ẽ͡ɐ̃"],
    # Backed rounded nasal [ɒ̃] for /ɐ̃/
    "ɐ̃": ["ɐ̃", "ɒ̃"],
    # Retroflex lateral cluster [pɭ]
    "l": ["l", "ɭ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# 4. Alto Minho — Viana do Castelo
#    Systematic retroflex lateral [ɭ], retroflex sibilants, flap [ɽ]
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_ALTO_MINHO = {
    **ALLOPHONES_PT,
    # Retroflex lateral — systematic in onset and clusters
    "l": ["l", "ɭ"],
    # Retroflex sibilants
    "ʃ": ["ʃ", "ʂ"],
    "ʒ": ["ʒ", "ʐ"],
    # Retroflex flap
    "ɾ": ["ɾ", "ɽ"],
    # Uvular
    "ʁ": ["ʁ", "χ"],
    # Standard lenition
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# 5. Beira Litoral — Aveiro/Vagos
#    Heaviest retroflex lateral [ɭ] attestation
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_BEIRA_LITORAL = {
    **ALLOPHONES_PT,
    # Retroflex lateral — heaviest attestation of all regions
    "l": ["l", "ɭ"],
    "ɫ": ["ɫ", "ɭ"],
    # Standard sibilants (no retroflex fricatives in this zone)
    # Standard lenition
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# 6. Lisbon — Standard reference
#    Already covered by base pt, but we provide a spec with explicit label
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_LISBON = {
    **ALLOPHONES_PT,
    # Explicit: voiced uvular dominant
    "ʁ": ["ʁ"],
    # Central vowel in unstressed
    "ə": ["ɨ"],
    # Moderate lenition
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# 7. Alto Alentejo — Portalegre/Crato
#    Transitional zone: vowel breaking (shared with Alfena), moderate reduction
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_ALTO_ALENTEJO = {
    **ALLOPHONES_PT,
    # Vowel breaking — same pattern as Alfena but less systematic
    "ɛ": ["ɛ", "ɛ͡ɐ"],
    "ɔ": ["ɔ"],
    # Standard uvular
    "ʁ": ["ʁ"],
    # Moderate lenition
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# 8. Algarve — Quarteira
#    Southern standard-adjacent: consistent [ʁ], minimal reduction
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_ALGARVE = {
    **ALLOPHONES_PT,
    "ʁ": ["ʁ"],  # consistent voiced uvular
    # Less vowel reduction than north
    "ə": ["ɨ"],
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# 9. Azores — Terceira
#    Raised nasal diphthong [õw̃], preserved full vowels, less reduction
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_AZORES = {
    **GRAPHEMES_PT,
    # Nasal diphthong raising
    "ão": ["õw̃"],  # [õw̃] not [ɐ̃w̃]
}

ALLOPHONES_AZORES = {
    **ALLOPHONES_PT,
    # Raised nasal diphthong
    "ɐ̃": ["ɐ̃", "õ"],  # tendency toward raised quality
    # Preserved full vowels — less reduction
    "ə": ["ɨ", "e"],  # unstressed /e/ may stay closer to [e]
    # /ũj/ simplification
    "ũ": ["ũ"],  # muito → [mũt]
}

# ═══════════════════════════════════════════════════════════════════════════
# 10. Madeira — Ribeira Brava
#     Systematic stop aspiration [pʰ, tʰ, kʰ], retroflex lateral, devoicing
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_MADEIRA = {
    **ALLOPHONES_PT,
    # Systematic stop aspiration — unique among all Portuguese dialects
    "p": ["p", "pʰ"],
    "t": ["t", "tʰ"],
    "k": ["k", "kʰ"],
    # Retroflex lateral (light)
    "l": ["l", "ɭ"],
    # Heavy final devoicing
    "b": ["b", "b̥"],
    "d": ["d", "d̥"],
    "ɡ": ["ɡ", "ɡ̥"],
    "z": ["z", "z̥"],
    "v": ["v", "v̥"],
}

# ═══════════════════════════════════════════════════════════════════════════
# 11. Northern Interior Rural — Alvarenga
#     Most extreme retroflex [ʐ/ʂ] — nearly every final /s/
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_TRAS_OS_MONTES = {
    **ALLOPHONES_PT,
    # Most extreme retroflex sibilants of all regions
    "ʃ": ["ʃ", "ʂ"],
    "ʒ": ["ʒ", "ʐ"],
    # Extreme vowel reduction
    "ɐ": ["ɐ", "ɐ̥", "∅"],
    "ə": ["ə", "ɨ", "∅"],
    "u": ["u", "u̥"],
    # Uvular
    "ʁ": ["ʁ", "χ"],
    # Lenition
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Specs
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "pt-PT-x-minho": LanguageSpec(
        code="pt-PT-x-minho",
        name="Minhoto Portuguese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_PT,
        allophones=ALLOPHONES_MINHO,
        positional_graphemes=POSITIONAL_PT_PT,
        parent="pt-PT",
        notes=(
            "Northern interior dialect (Vizela, Braga). Extreme unstressed vowel "
            "reduction (deletion, devoicing). Voiceless uvular [χ] in coda. "
            "Retroflex flap [ɽ], traces of retroflex sibilants [ʂ, ʐ]. "
            "Heaviest vowel elision of all EP dialects."
        ),
    ),
    "pt-PT-x-porto": LanguageSpec(
        code="pt-PT-x-porto",
        name="Portuense Portuguese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_PT,
        allophones=ALLOPHONES_PORTO,
        positional_graphemes=POSITIONAL_PT_PT,
        parent="pt-PT",
        notes=(
            "Porto city and Greater Porto (Gaia, Miragaia, Leça, Vitória). "
            "Heavy vowel reduction but syllable structure more preserved than "
            "Minho interior. Uvular variation: [ʁ, χ, ʀ, x]. "
            "Retroflex sibilants moderate in suburban/rural fringes (Alvarenga, Gaia). "
            "Heavily velarised coda [ɫ]."
        ),
    ),
    "pt-PT-x-alfena": LanguageSpec(
        code="pt-PT-x-alfena",
        name="Alfena Portuguese (vowel-breaking)",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_PT,
        allophones=ALLOPHONES_ALFENA,
        positional_graphemes=POSITIONAL_PT_PT,
        parent="pt-PT",
        notes=(
            "Greater Porto suburban dialect with unique vowel breaking "
            "(Brechung): stressed mid vowels develop centering offglide — "
            "[ɛ͡ɐ, ɔ͡ɐ, e͡ɐ, o͡ɐ, ẽ͡ɐ̃]. Also attested in Portalegre (Crato). "
            "Backed rounded nasal [ɒ̃] for /ɐ̃/. Retroflex lateral [ɭ] in clusters."
        ),
    ),
    "pt-PT-x-viana": LanguageSpec(
        code="pt-PT-x-viana",
        name="Alto Minho Portuguese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_PT,
        allophones=ALLOPHONES_ALTO_MINHO,
        positional_graphemes=POSITIONAL_PT_PT,
        parent="pt-PT",
        notes=(
            "Viana do Castelo / Ponte de Lima. Systematic retroflex lateral [ɭ] "
            "in onset and clusters. Retroflex sibilants [ʂ, ʐ] in final position. "
            "Retroflex flap [ɽ] as free variant of /ɾ/. Voiceless uvular [χ] in coda."
        ),
    ),
    "pt-PT-x-aveiro": LanguageSpec(
        code="pt-PT-x-aveiro",
        name="Beira Litoral Portuguese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_PT,
        allophones=ALLOPHONES_BEIRA_LITORAL,
        positional_graphemes=POSITIONAL_PT_PT,
        parent="pt-PT",
        notes=(
            "Vagos, Aveiro area. Heaviest attestation of retroflex lateral [ɭ] "
            "of all Portuguese dialects — systematic in onset, post-consonantal, "
            "and coda positions. No retroflex sibilants. Otherwise moderate features."
        ),
    ),
    "pt-PT-x-lisbon": LanguageSpec(
        code="pt-PT-x-lisbon",
        name="Lisbon Portuguese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_PT,
        allophones=ALLOPHONES_LISBON,
        positional_graphemes=POSITIONAL_PT_PT,
        parent="pt-PT",
        notes=(
            "Standard Lisbon reference dialect. Consistent voiced uvular [ʁ]. "
            "Centralized [ɨ] for unstressed /e/. Moderate vowel reduction with "
            "syllable structure preserved. No retroflex consonants. "
            "Discourse marker [iɨ] characteristic of educated Lisbon speech."
        ),
    ),
    "pt-PT-x-alentejo": LanguageSpec(
        code="pt-PT-x-alentejo",
        name="Alto Alentejo Portuguese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_PT,
        allophones=ALLOPHONES_ALTO_ALENTEJO,
        positional_graphemes=POSITIONAL_PT_PT,
        parent="pt-PT",
        notes=(
            "Portalegre/Crato transitional zone between northern and southern "
            "dialects. Vowel breaking [ɛ͡ɐ] shared with Alfena (Greater Porto). "
            "Intermediate vowel reduction. Standard uvular [ʁ]."
        ),
    ),
    "pt-PT-x-algarve": LanguageSpec(
        code="pt-PT-x-algarve",
        name="Algarvio Portuguese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_PT,
        allophones=ALLOPHONES_ALGARVE,
        positional_graphemes=POSITIONAL_PT_PT,
        parent="pt-PT",
        notes=(
            "Quarteira, Faro. Southern dialect, standard-adjacent. Consistent "
            "voiced uvular [ʁ]. Minimal vowel reduction. Southern [ɐ] quality. "
            "No retroflex consonants."
        ),
    ),
    "pt-PT-x-acores": LanguageSpec(
        code="pt-PT-x-acores",
        name="Azorean Portuguese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_AZORES,
        allophones=ALLOPHONES_AZORES,
        positional_graphemes=POSITIONAL_PT_PT,
        parent="pt-PT",
        notes=(
            "Terceira, Azores. Diagnostic raised nasal diphthong [õw̃] for "
            "mainland [ɐ̃w̃] (não → [nõw̃]). Preserved full vowels in unstressed "
            "syllables (less reduction than mainland). Simplified clusters "
            "(muito → [mũt]). No retroflex consonants. Slower speech rhythm."
        ),
    ),
    "pt-PT-x-madeira": LanguageSpec(
        code="pt-PT-x-madeira",
        name="Madeiran Portuguese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_PT,
        allophones=ALLOPHONES_MADEIRA,
        positional_graphemes=POSITIONAL_PT_PT,
        parent="pt-PT",
        notes=(
            "Ribeira Brava, Madeira. Systematic aspiration of voiceless stops "
            "[pʰ, tʰ, kʰ] — unique among all Portuguese dialects, completely "
            "absent from mainland. Light retroflex lateral [ɭ]. "
            "Heavy final devoicing of voiced obstruents. "
            "Phonetically reminiscent of English/German aspiration patterns."
        ),
    ),
    "pt-PT-x-trasosmontes": LanguageSpec(
        code="pt-PT-x-trasosmontes",
        name="Transmontano Portuguese",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_PT,
        allophones=ALLOPHONES_TRAS_OS_MONTES,
        positional_graphemes=POSITIONAL_PT_PT,
        parent="pt-PT",
        notes=(
            "Rural northern interior (Alvarenga, Penafiel). Most extreme "
            "retroflex sibilants [ʂ, ʐ] of all EP dialects — nearly every "
            "final /s/ realised as retroflex. Extreme vowel reduction. "
            "Conservative rural speech closest to historical northern patterns."
        ),
    ),
}
