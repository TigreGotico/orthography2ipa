"""Spanish regional dialects of Spain — grapheme→IPA and allophone mappings.

Covers the major dialectal zones of Peninsular and Insular Spanish that
diverge significantly from standard Castilian phonology.

Sources:
- Narbona, A., Cano, R. & Morillo, R. (2011). *El español hablado en Andalucía*.
- Penny, R. (2000). *Variation and Change in Spanish*.
- Alvar, M. (1996). *Manual de dialectología hispánica*.
- Muñoz Cortés, M. (1958). *El habla de Murcia*.
- Alvar, M. (1959). *El español hablado en Tenerife*.
- García Mouton, P. (1994). *Lenguas y dialectos de España*.

Conventions:
- All codes use es-ES-x-{region} private-use subtags.
- Base graphemes inherited from Castilian Spanish (es).
- Allophone maps capture systematic regional differences.
"""
from orthography2ipa.languages.es import GRAPHEMES_ES, ALLOPHONES_ES
from orthography2ipa.types import LanguageSpec

# ═══════════════════════════════════════════════════════════════════════════
# Andalusian Spanish (es-ES-x-andalusia)
# The most phonologically divergent major Castilian dialect
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_ANDALUSIA_W = {
    **GRAPHEMES_ES,
    # Western Andalusian: seseo AND ceceo zones
    "c": ["k", "s", "θ"],  # /s/ in seseo areas; /θ/ in ceceo areas before e,i
    "z": ["s", "θ"],  # same split
    "s": ["s", "h"],  # coda aspiration dominant
    "ll": ["ʝ"],  # universal yeísmo
}

ALLOPHONES_ANDALUSIA_W = {
    **ALLOPHONES_ES,
    # Coda /s/ → [h] aspiration or deletion (hallmark Andalusian feature)
    "s": ["s", "h", "∅"],
    # /x/ → [h] (aspiration of velar fricative)
    "x": ["h"],
    # Yeísmo universal
    "ʎ": ["ʝ"],
    "ʝ": ["ʝ", "ɟʝ"],
    # Lenition intensified
    "b": ["b", "β", "∅"],
    "d": ["d", "ð", "∅"],  # word-final -d deletion universal
    "ɡ": ["ɡ", "ɣ", "∅"],
    # /θ/ in ceceo zones replaces /s/ entirely
    "θ": ["θ", "s"],  # varies by locality
    # CH deaffrication in western areas
    "tʃ": ["tʃ", "ʃ"],  # [ʃ] in parts of Cádiz, Málaga, Sevilla
    # Final consonant weakening
    "n": ["n", "ŋ", "∅"],  # final -n velarisation or deletion
    "l": ["l", "ɾ"],  # /l/ → [ɾ] neutralisation in coda (huerga/huelga)
    "ɾ": ["ɾ", "l"],  # /ɾ/ → [l] neutralisation in coda
    # Vowel opening from lost -s (phonemic in eastern Andalusian)
    "a": ["a", "æ"],  # open allophone when following -s deleted
    "e": ["e", "ɛ"],
    "o": ["o", "ɔ"],
}

GRAPHEMES_ANDALUSIA_E = {
    **GRAPHEMES_ES,
    # Eastern Andalusian: distinción maintained but with aspiration
    "s": ["s", "h"],
    "ll": ["ʝ"],
}

ALLOPHONES_ANDALUSIA_E = {
    **ALLOPHONES_ES,
    "s": ["s", "h", "∅"],
    "x": ["h"],
    "ʎ": ["ʝ"],
    "ʝ": ["ʝ", "ɟʝ"],
    "b": ["b", "β"],
    "d": ["d", "ð", "∅"],
    "ɡ": ["ɡ", "ɣ"],
    "tʃ": ["tʃ"],  # affricate preserved in east
    # Eastern Andalusian vowel opening — approaching phonemic status
    # Loss of final -s triggers vowel opening: perros [ˈpɛrɔ] vs perro [ˈpero]
    "a": ["a", "æ"],
    "e": ["e", "ɛ"],
    "o": ["o", "ɔ"],
    "i": ["i", "ɪ"],
    "u": ["u", "ʊ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Murcian Spanish / Panocho (es-ES-x-murcia)
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_MURCIA = {
    **GRAPHEMES_ES,
    "s": ["s", "h"],  # coda aspiration (Andalusian-type)
    "ll": ["ʝ"],  # yeísmo
    "c": ["k", "θ", "s"],  # mixed: some seseo traces
}

ALLOPHONES_MURCIA = {
    **ALLOPHONES_ES,
    "s": ["s", "h", "∅"],  # aspiration like Andalusian
    "x": ["x", "h"],  # less aspiration than Andalusia
    "ʎ": ["ʝ"],
    "d": ["d", "ð", "∅"],  # -d deletion common
    "ɾ": ["ɾ", "l"],  # coda neutralisation
    "l": ["l", "ɾ"],
    "n": ["n", "ŋ"],  # final velarisation
    # Murcian vowel harmony / metaphony in some areas
    "e": ["e"],
    "o": ["o"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Canarian Spanish (es-ES-x-canarias)
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_CANARIAS = {
    **GRAPHEMES_ES,
    "c": ["k", "s"],  # seseo (no /θ/)
    "z": ["s"],  # seseo
    "s": ["s", "h"],  # coda aspiration
    "ll": ["ʝ"],  # yeísmo
}

ALLOPHONES_CANARIAS = {
    **ALLOPHONES_ES,
    "s": ["s", "h"],  # aspiration but less extreme than Andalusian
    "x": ["x", "h"],  # partial aspiration
    "ʎ": ["ʝ"],
    "d": ["d", "ð", "∅"],
    "tʃ": ["tʃ"],  # affricate preserved (sometimes tensed [tːʃ])
    # No /θ/ — seseo throughout
}

# ═══════════════════════════════════════════════════════════════════════════
# Cantabrian Spanish / Montañés (es-ES-x-cantabria)
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_CANTABRIA = {
    **GRAPHEMES_ES,
    # Conservative: distinción preserved
}

ALLOPHONES_CANTABRIA = {
    **ALLOPHONES_ES,
    # Asturleonese substrate features
    "s": ["s̺"],  # apico-alveolar (northern)
    "θ": ["θ"],
    "ʎ": ["ʎ"],  # conservative: no yeísmo (weakening)
    # Aspiration of final -s in some coastal areas
    # Metaphony traces (rare, western Cantabria: Leonese substrate)
    "e": ["e"],
    "o": ["o"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Specs
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "es-ES-x-andalusia-w": LanguageSpec(
        code="es-ES-x-andalusia-w",
        name="Western Andalusian Spanish",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_ANDALUSIA_W,
        allophones=ALLOPHONES_ANDALUSIA_W,
        parent="es",
        notes=(
            "Western Andalusian (Sevilla, Cádiz, Huelva, Córdoba, Málaga). "
            "Most phonologically innovative Castilian variety. Hallmarks: "
            "coda /s/ → [h] or ∅ (aspiration/deletion), /x/ → [h], "
            "universal yeísmo, seseo or ceceo (varies by locality), "
            "CH deaffrication [tʃ] → [ʃ] in Cádiz/Sevilla area, "
            "coda liquid neutralisation (/l/ ↔ /ɾ/), extreme lenition "
            "with consonant deletion, final -n velarisation. "
            "Basis for much of Latin American Spanish phonology."
        ),
    ),
    "es-ES-x-andalusia-e": LanguageSpec(
        code="es-ES-x-andalusia-e",
        name="Eastern Andalusian Spanish",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_ANDALUSIA_E,
        allophones=ALLOPHONES_ANDALUSIA_E,
        parent="es",
        notes=(
            "Eastern Andalusian (Granada, Almería, Jaén). Maintains "
            "distinción (/θ/ vs /s/) but shares aspiration with west. "
            "Distinctive vowel opening when final -s is deleted, creating "
            "near-phonemic open/closed vowel pairs (approaching 10-vowel "
            "system): perros [ˈpɛrɔ] vs perro [ˈpero]. "
            "Affricate [tʃ] preserved (no deaffrication)."
        ),
    ),
    "es-ES-x-murcia": LanguageSpec(
        code="es-ES-x-murcia",
        name="Murcian Spanish (Panocho)",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_MURCIA,
        allophones=ALLOPHONES_MURCIA,
        parent="es",
        notes=(
            "Murcian Spanish (Panocho/Murciano). Transitional between "
            "Castilian and Andalusian: shares coda aspiration, -d deletion, "
            "yeísmo, and liquid neutralisation with Andalusian. Some traces "
            "of Aragonese/Catalan substrate from medieval settlement "
            "(vowel harmony traces). Mixed distinción/seseo zones."
        ),
    ),
    "es-ES-x-canarias": LanguageSpec(
        code="es-ES-x-canarias",
        name="Canarian Spanish",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_CANARIAS,
        allophones=ALLOPHONES_CANARIAS,
        parent="es",
        notes=(
            "Canarian Spanish (Islas Canarias). Systematic seseo (no /θ/), "
            "yeísmo, coda /s/ aspiration (less extreme than Andalusian), "
            "partial /x/ aspiration. Strong historical connections to "
            "Andalusian and Caribbean Spanish. Conservative affricate [tʃ] "
            "preservation. -d deletion in participial -ado."
        ),
    ),
    "es-ES-x-cantabria": LanguageSpec(
        code="es-ES-x-cantabria",
        name="Cantabrian Spanish (Montañés)",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_CANTABRIA,
        allophones=ALLOPHONES_CANTABRIA,
        parent="es",
        notes=(
            "Cantabrian Spanish (Montañés). Northern conservative dialect "
            "with Asturleonese substrate. Apico-alveolar [s̺] (northern "
            "type), distinción preserved, conservative [ʎ] (weakening). "
            "Transitional between Castilian and Asturian. Some Leonese "
            "metaphony traces in western areas."
        ),
    ),
}
