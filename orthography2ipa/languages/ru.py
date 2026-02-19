"""Russian dialect sub-specifications (ru_dialects) — grapheme→IPA and allophone mappings.

Sources:
- Filin, F.P. (1972). *Proisxozhdeniye russkogo, ukrainskogo i belorusskogo yazykov*. Leningrad.
- Avanesov, R.I. (1949). *Ocherki russkoy dialektologii*. Moscow.
- Coats, H.S. (1999). 'Russian' in *The Slavonic Languages* (ed. Comrie & Corbett).
- Yanushevskaya & Bunčić (2015). Russian. *JIPA*.
"""
from orthography2ipa.types import LanguageSpec

# ---------------------------------------------------------------------------
# Base graphemes shared by all Russian dialects (= Standard Russian)
# ---------------------------------------------------------------------------
_BASE_GRAPHEMES = {
    "а": ["a"], "е": ["je", "e"], "ё": ["jo"],
    "и": ["i"], "о": ["o"], "у": ["u"],
    "э": ["ɛ"], "ю": ["ju"], "я": ["ja"],
    "ы": ["ɨ"], "ъ": [""], "ь": ["ʲ"],
    "б": ["b"], "в": ["v"], "г": ["ɡ"],
    "д": ["d"], "ж": ["ʐ"], "з": ["z"],
    "й": ["j"], "к": ["k"], "л": ["l"],
    "м": ["m"], "н": ["n"], "п": ["p"],
    "р": ["r"], "с": ["s"], "т": ["t"],
    "ф": ["f"], "х": ["x"], "ц": ["ts"],
    "ч": ["tɕ"], "ш": ["ʂ"], "щ": ["ɕː"],
    "бь": ["bʲ"], "вь": ["vʲ"], "дь": ["dʲ"], "зь": ["zʲ"],
    "ль": ["lʲ"], "мь": ["mʲ"], "нь": ["nʲ"], "пь": ["pʲ"],
    "рь": ["rʲ"], "сь": ["sʲ"], "ть": ["tʲ"], "фь": ["fʲ"],
}

# ---------------------------------------------------------------------------
# Standard Moscow Russian (Moscovian / Central Russian)
# ---------------------------------------------------------------------------
# - Аканье (unstressed /o/ → [ɐ])
# - г = [ɡ] plosive
MOSCOW_GRAPHEMES = dict(_BASE_GRAPHEMES)

MOSCOW_ALLOPHONES = {
    "b": ["b", "p"], "bʲ": ["bʲ", "pʲ"],
    "d": ["d", "t"], "dʲ": ["dʲ", "tʲ"],
    "ɡ": ["ɡ", "k"],
    "p": ["p"], "pʲ": ["pʲ"],
    "t": ["t"], "tʲ": ["tʲ"],
    "k": ["k"],
    "f": ["f"], "fʲ": ["fʲ"],
    "v": ["v", "f"], "vʲ": ["vʲ", "fʲ"],
    "s": ["s"], "sʲ": ["sʲ"],
    "z": ["z", "s"], "zʲ": ["zʲ", "sʲ"],
    "ʂ": ["ʂ"], "ʐ": ["ʐ", "ʂ"],
    "ɕː": ["ɕː"],
    "x": ["x", "xʲ"],
    "ts": ["ts"], "tɕ": ["tɕ"],
    "m": ["m"], "mʲ": ["mʲ"],
    "n": ["n", "ŋ"], "nʲ": ["nʲ"],
    "l": ["ɫ"], "lʲ": ["lʲ"],
    "r": ["r"], "rʲ": ["rʲ"],
    "j": ["j"],
    "a": ["a", "ɐ", "ə"],
    "o": ["o", "ɐ", "ə"],  # аканье
    "e": ["e", "ɪ"],
    "ɛ": ["ɛ"],
    "i": ["i", "ɪ"],
    "ɨ": ["ɨ"],
    "u": ["u", "ʊ"],
}

# ---------------------------------------------------------------------------
# Northern Russian dialects
# ---------------------------------------------------------------------------
# - Оканье (no аканье; unstressed /o/ preserved as [o])
# - г = [ɡ] plosive (same as Moscow)
# - Often цоканье (ч → ц, no distinction)
NORTHERN_GRAPHEMES = dict(_BASE_GRAPHEMES)
# Merge ч → ц (цоканье) for Northern dialects
NORTHERN_GRAPHEMES["ч"] = ["ts"]  # цоканье

NORTHERN_ALLOPHONES = dict(MOSCOW_ALLOPHONES)
# Override: оканье — /o/ stays [o] unstressed
NORTHERN_ALLOPHONES["o"] = ["o", "ʊ"]  # no аканье reduction
NORTHERN_ALLOPHONES["a"] = ["a"]
NORTHERN_ALLOPHONES["tɕ"] = ["ts"]  # цоканье: merger with [ts]

# ---------------------------------------------------------------------------
# Southern Russian dialects
# ---------------------------------------------------------------------------
# - Аканье (like Moscow)
# - г = [ɣ] fricative (South Russian feature)
# - Яканье (various unstressed /e/ → /a/)
SOUTHERN_GRAPHEMES = dict(_BASE_GRAPHEMES)
SOUTHERN_GRAPHEMES["г"] = ["ɣ"]  # fricative г

SOUTHERN_ALLOPHONES = dict(MOSCOW_ALLOPHONES)
SOUTHERN_ALLOPHONES["ɡ"] = ["ɣ", "ɣ"]  # actually /ɣ/, devoiced → [x]
# Redefine with correct key
SOUTHERN_ALLOPHONES["ɣ"] = ["ɣ", "x"]  # voiced fricative, devoiced to [x]
del SOUTHERN_ALLOPHONES["ɡ"]
# Stronger яканье: unstressed /e/ → [a] after soft consonants
SOUTHERN_ALLOPHONES["e"] = ["e", "a", "ɪ"]

# ---------------------------------------------------------------------------
# Siberian Russian (Standard-adjacent but with some features)
# ---------------------------------------------------------------------------
# - Maintains /o/ contrast in some unstressed positions
# - г = [ɡ] plosive
# - Generally conservative
SIBERIAN_GRAPHEMES = dict(_BASE_GRAPHEMES)
SIBERIAN_ALLOPHONES = dict(MOSCOW_ALLOPHONES)
SIBERIAN_ALLOPHONES["o"] = ["o", "ɐ"]  # partial аканье

# ---------------------------------------------------------------------------
# Pskov / Novgorod transitional dialect
# ---------------------------------------------------------------------------
# - Mixed аканье/оканье
# - Partial цоканье
PSKOV_GRAPHEMES = dict(_BASE_GRAPHEMES)
PSKOV_GRAPHEMES["ч"] = ["ts", "tɕ"]  # partial цоканье

PSKOV_ALLOPHONES = dict(MOSCOW_ALLOPHONES)
PSKOV_ALLOPHONES["o"] = ["o", "ɐ", "ə"]  # mixed reduction

# ---------------------------------------------------------------------------
# Don Cossack (южнорусское наречие) dialect
# ---------------------------------------------------------------------------
# South Russian with strong fricative г and аканье
DON_GRAPHEMES = dict(_BASE_GRAPHEMES)
DON_GRAPHEMES["г"] = ["ɣ"]

DON_ALLOPHONES = dict(SOUTHERN_ALLOPHONES)

SPECS = {
    # --- Central / Standard ---
    "ru": LanguageSpec(
        code="ru",
        name="Russian",
        family="Slavic",
        script="Cyrillic",
        graphemes=MOSCOW_GRAPHEMES,
        allophones=MOSCOW_ALLOPHONES,
        parent="sla",
        notes=(
            "Standard Moscow Russian. Key features: pervasive "
            "palatalisation contrast, Аканье (unstressed /o/ → [ɐ]), "
            "г = [ɡ] plosive, final obstruent devoicing."
        ),
    ),
    "ru-x-moscow": LanguageSpec(
        code="ru-x-moscow",
        name="Moscow Russian",
        family="Slavic",
        script="Cyrillic",
        graphemes=MOSCOW_GRAPHEMES,
        allophones=MOSCOW_ALLOPHONES,
        parent="ru",
        notes="Central Russian, basis of the standard. Аканье, plosive [ɡ].",
    ),
    # --- Northern ---
    "ru-x-northern": LanguageSpec(
        code="ru-x-northern",
        name="Northern Russian",
        family="Slavic",
        script="Cyrillic",
        graphemes=NORTHERN_GRAPHEMES,
        allophones=NORTHERN_ALLOPHONES,
        parent="ru",
        notes=(
            "Northern Russian dialects (Arkhangelsk, Vologda, Kostroma region). "
            "Оканье: unstressed /o/ preserved. Often цоканье: ч/ц not distinguished."
        ),
    ),
    "ru-x-arkhangelsk": LanguageSpec(
        code="ru-x-arkhangelsk",
        name="Arkhangelsk Russian",
        family="Slavic",
        script="Cyrillic",
        graphemes=NORTHERN_GRAPHEMES,
        allophones=NORTHERN_ALLOPHONES,
        parent="ru-x-northern",
        notes="Northern Russian, Arkhangelsk subtype. Strong оканье, цоканье.",
    ),
    "ru-x-vologda": LanguageSpec(
        code="ru-x-vologda",
        name="Vologda Russian",
        family="Slavic",
        script="Cyrillic",
        graphemes=NORTHERN_GRAPHEMES,
        allophones=NORTHERN_ALLOPHONES,
        parent="ru-x-northern",
        notes="Northern Russian, Vologda region. Оканье, strong consonantism.",
    ),
    # --- Southern ---
    "ru-x-southern": LanguageSpec(
        code="ru-x-southern",
        name="Southern Russian",
        family="Slavic",
        script="Cyrillic",
        graphemes=SOUTHERN_GRAPHEMES,
        allophones=SOUTHERN_ALLOPHONES,
        parent="ru",
        notes=(
            "Southern Russian dialects (Ryazan, Kursk, Voronezh, Tula regions). "
            "г = [ɣ] fricative (not plosive). Strong аканье and яканье."
        ),
    ),
    "ru-x-kursk-orel": LanguageSpec(
        code="ru-x-kursk-orel",
        name="Kursk-Orel Russian",
        family="Slavic",
        script="Cyrillic",
        graphemes=SOUTHERN_GRAPHEMES,
        allophones=SOUTHERN_ALLOPHONES,
        parent="ru-x-southern",
        notes=(
            "South Russian, Kursk-Orel zone. Archetypal [ɣ] fricative, "
            "strong яканье."
        ),
    ),
    "ru-x-don": LanguageSpec(
        code="ru-x-don",
        name="Don Cossack Russian",
        family="Slavic",
        script="Cyrillic",
        graphemes=DON_GRAPHEMES,
        allophones=DON_ALLOPHONES,
        parent="ru-x-southern",
        notes=(
            "Don Cossack dialect (Rostov region). South Russian base "
            "with Ukrainian contact features: г = [ɣ], аканье."
        ),
    ),
    # --- Siberian ---
    "ru-x-siberian": LanguageSpec(
        code="ru-x-siberian",
        name="Siberian Russian",
        family="Slavic",
        script="Cyrillic",
        graphemes=SIBERIAN_GRAPHEMES,
        allophones=SIBERIAN_ALLOPHONES,
        parent="ru",
        notes=(
            "Siberian Russian (Novosibirsk, Tomsk, Krasnoyarsk regions). "
            "Generally conservative; partial аканье. "
            "г = [ɡ] plosive. Substrate influence from Siberian languages."
        ),
    ),
    # --- Pskov/Novgorod transitional ---
    "ru-x-pskov": LanguageSpec(
        code="ru-x-pskov",
        name="Pskov Russian",
        family="Slavic",
        script="Cyrillic",
        graphemes=PSKOV_GRAPHEMES,
        allophones=PSKOV_ALLOPHONES,
        parent="ru",
        notes=(
            "Pskov-Novgorod transitional dialect. "
            "Mixed North-Central features; partial цоканье; "
            "Baltic substrate influence (Pskov region)."
        ),
    ),
    # --- Ural ---
    "ru-x-ural": LanguageSpec(
        code="ru-x-ural",
        name="Ural Russian",
        family="Slavic",
        script="Cyrillic",
        graphemes=MOSCOW_GRAPHEMES,
        allophones=MOSCOW_ALLOPHONES,  # generally standard-like
        parent="ru",
        notes=(
            "Ural Russian (Perm, Yekaterinburg region). "
            "Predominantly standard-like; traces of Northern аканье in older speech. "
            "Tatar and Bashkir substrate influence."
        ),
    ),
}
