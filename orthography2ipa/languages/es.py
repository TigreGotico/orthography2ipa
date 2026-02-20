"""Spanish regional dialects of Spain — grapheme→IPA and allophone mappings.

Covers the major dialectal zones of Peninsular and Insular Spanish that
diverge significantly from standard Castilian phonology.

Sources:
- Hualde, J.I. (2005). *The Sounds of Spanish*.
- RAE (2011). *Nueva gramática de la lengua española: Fonética y fonología*.
- Quilis, A. (1993). *Tratado de fonología y fonética españolas*.
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
from orthography2ipa.types import LanguageSpec
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE
# ═══════════════════════════════════════════════════════════════════════════
# Castilian Spanish (Peninsular)
# ═══════════════════════════════════════════════════════════════════════════
GRAPHEMES_ES = {
    # --- Vowels (5-vowel system, transparent orthography) ---
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],
    "á": ["a"],
    "é": ["e"],
    "í": ["i"],
    "ó": ["o"],
    "ú": ["u"],
    "ü": ["w"],  # diaeresis: pronounced /w/ in ⟨güe⟩, ⟨güi⟩

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "θ"],  # /k/ before a,o,u; /θ/ before e,i (Castilian)
    "ç": ["s"],  # historical, rare
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "x"],  # /ɡ/ before a,o,u; /x/ before e,i
    "h": [""],  # always silent
    "j": ["x"],
    "k": ["k"],  # loanwords
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "ñ": ["ɲ"],
    "p": ["p"],
    "q": ["k"],  # only in ⟨qu⟩
    "r": ["ɾ"],  # tap (single ⟨r⟩ intervocalic)
    "s": ["s"],
    "t": ["t"],
    "v": ["b"],  # merged with /b/ in standard Spanish
    "w": ["w"],  # loanwords
    "x": ["ks", "s"],  # /ks/ standard; /s/ in some words (México)
    "y": ["ʝ", "i"],  # consonantal /ʝ/; vowel /i/ (word-final)
    "z": ["θ"],  # Castilian

    # --- Consonant digraphs ---
    "ch": ["tʃ"],
    "ll": ["ʎ", "ʝ"],  # /ʎ/ traditional; /ʝ/ yeísmo
    "rr": ["r"],  # alveolar trill
    "qu": ["k"],  # ⟨u⟩ silent before e,i
    "gu": ["ɡ"],  # ⟨u⟩ silent before e,i

    # --- Diphthongs (official rising and falling) ---
    # Rising (semivowel + vowel)
    "ia": ["ja"], "ie": ["je"], "io": ["jo"], "iu": ["ju"],
    "ua": ["wa"], "ue": ["we"], "uo": ["wo"], "ui": ["wi"],
    # Falling (vowel + semivowel)
    "ai": ["aj"], "ei": ["ej"], "oi": ["oj"],
    "au": ["aw"], "eu": ["ew"], "ou": ["ow"],
    # ⟨ay⟩, ⟨ey⟩, ⟨oy⟩ word-final variants
    "ay": ["aj"], "ey": ["ej"], "oy": ["oj"],

    # --- Triphthongs ---
    "iai": ["jaj"], "iei": ["jej"], "uai": ["waj"], "uei": ["wej"],
    "ioi": ["joj"],
}

ALLOPHONES_ES = {
    # Plosives → spirants (lenition)
    "b": ["b", "β"],  # [β] intervocalic / after continuant
    "d": ["d", "ð"],  # [ð] intervocalic / after continuant
    "ɡ": ["ɡ", "ɣ"],  # [ɣ] intervocalic / after continuant

    "p": ["p"],
    "t": ["t", "t̪"],  # dental before /θ/
    "k": ["k"],

    # Fricatives
    "f": ["f"],
    "θ": ["θ"],  # Castilian only
    "s": ["s", "z"],  # [z] before voiced consonant
    "x": ["x", "h"],  # [h] in Caribbean/Andalusian dialects
    "ʝ": ["ʝ", "ɟʝ", "ʃ"],  # affricated post-pausal; [ʃ] in Rioplatense

    # Affricates
    "tʃ": ["tʃ"],

    # Nasals
    "m": ["m"],
    "n": ["n", "m", "ɱ", "n̪", "ŋ", "ɲ"],  # assimilates to following C place
    "ɲ": ["ɲ"],

    # Laterals
    "l": ["l", "l̪", "ɫ"],  # dental before /t,d/; dark in coda (dialectal)
    "ʎ": ["ʎ"],  # only in lleísta dialects

    # Rhotics
    "ɾ": ["ɾ"],  # tap
    "r": ["r"],  # trill

    # Glides
    "j": ["j"],
    "w": ["w", "ɣʷ"],  # [ɣʷ] after consonant in some analyses

    # Vowels (no significant allophony — transparent system)
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],
}



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
    "es": LanguageSpec(
        code="es-ES",
        name="Spanish (Castilian)",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_ES,
        allophones=ALLOPHONES_ES,
        parent="la-x-hispania",
        ancestors=(
            Ancestor("la-x-hispania", P, 0.80,
                     "Primary descent from Hispanic Vulgar Latin"),
            Ancestor("xaq", SUB, 0.08,
                     "Basque substrate: f->h, 5-vowel reinforcement"),
            Ancestor("xaa", AD, 0.07,
                     "Andalusi Arabic adstrate: ~4000 loanwords"),
            Ancestor("got", SUP, 0.05,
                     "Visigothic superstrate: guerra, guardar, ropa"),
        ),
        notes="Peninsular Castilian with distinción (θ/s contrast).",
    ),
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
