"""Language registry with lazy loading."""
from __future__ import annotations

import importlib
from typing import Dict, List

from orthography2ipa.types import LanguageSpec

# module path inside orthography2ipa.languages for each code
_LATIN: Dict[str, str] = {

    "la": "orthography2ipa.languages.la",

    "la-x-hispania": "orthography2ipa.languages.iberian_medieval",
    "la-x-gallia": "orthography2ipa.languages.la_galloromance",

    # ── Italo-Romance Vulgar Latin (intermediate ancestor) ───────────────
    "la-x-italia": "orthography2ipa.languages.la_italoromance",

    # ── Balkan Romance Vulgar Latin (intermediate ancestor) ──────────────
    "la-x-balkans": "orthography2ipa.languages.la_balkanromance",

    # ── Sardinian (own primary branch of Romance) ────────────────────────
    "sc": "orthography2ipa.languages.sc",
}

_CELTIC = {

    # Celtic (ancestry for Celtiberian)
    "cel": "orthography2ipa.languages.celtic",
    "xcg": "orthography2ipa.languages.celtic",
}

_IBERIAN = {
    # Pre-Roman Iberian Peninsula
    "xce": "orthography2ipa.languages.iberian_preroman",
    "xib": "orthography2ipa.languages.iberian_preroman",
    "xlg": "orthography2ipa.languages.iberian_preroman",
    "txr": "orthography2ipa.languages.iberian_preroman",
    "xaq": "orthography2ipa.languages.iberian_preroman",

    # Phoenician (Iberian trading colonies)
    "phn": "orthography2ipa.languages.phoenician",

    # Medieval Iberian
    "mxi": "orthography2ipa.languages.iberian_medieval",
    "xaa": "orthography2ipa.languages.iberian_medieval",

    # Portuguese speaking countries
    "pt-BR": "orthography2ipa.languages.pt",
    "pt-AO": "orthography2ipa.languages.pt",

    # Languages of spain
    "gl": "orthography2ipa.languages.gl",
    "eu": "orthography2ipa.languages.eu",
    "ca": "orthography2ipa.languages.ca",

    # Minority Languages (Portugal)
    "mwl": "orthography2ipa.languages.mwl",  # Mirandese
    "mwl-x-sendim": "orthography2ipa.languages.mwl",
    "ext-PT-x-barrancos": "orthography2ipa.languages.barranquenho", # Barranquenho
    "ast-PT-x-rionor": "orthography2ipa.languages.rionorese", # Rionorese
    "ast-PT-x-guadramil": "orthography2ipa.languages.guadramilese", # Guadramilese

    # Minority Languages (Spain)
    "ast": "orthography2ipa.languages.ast",
    "fax": "orthography2ipa.languages.gl", # Fala
    "ext": "orthography2ipa.languages.ext",
    "an": "orthography2ipa.languages.an",
    "oc-x-aranes": "orthography2ipa.languages.ca", # Aranese (Gascon Occitan)

    # Asturian (Spain)
    "ast-x-occidental": "orthography2ipa.languages.ast",
    "ast-x-oriental": "orthography2ipa.languages.ast",
    "ast-ES-x-leon": "orthography2ipa.languages.ast",
    # Aragonese
    "an-x-occidental": "orthography2ipa.languages.an",
    "an-x-oriental": "orthography2ipa.languages.an",
    # Extremaduran (Spain)
    "ext-x-septentrional": "orthography2ipa.languages.ext",
    # Galician dialects
    "gl-x-occidental": "orthography2ipa.languages.gl",
    "gl-x-central": "orthography2ipa.languages.gl",
    "gl-x-oriental": "orthography2ipa.languages.gl",

    # Portuguese dialects
    "pt-PT-x-minho": "orthography2ipa.languages.pt_dialects",
    "pt-PT-x-porto": "orthography2ipa.languages.pt_dialects",
    "pt-PT-x-alfena": "orthography2ipa.languages.pt_dialects",
    "pt-PT-x-viana": "orthography2ipa.languages.pt_dialects",
    "pt-PT-x-aveiro": "orthography2ipa.languages.pt_dialects",
    "pt-PT-x-lisbon": "orthography2ipa.languages.pt_dialects",
    "pt-PT-x-alentejo": "orthography2ipa.languages.pt_dialects",
    "pt-PT-x-algarve": "orthography2ipa.languages.pt_dialects",
    "pt-PT-x-acores": "orthography2ipa.languages.pt_dialects",
    "pt-PT-x-madeira": "orthography2ipa.languages.pt_dialects",
    "pt-PT-x-trasosmontes": "orthography2ipa.languages.pt_dialects",

    # Brazilian Portuguese dialects
    "pt-BR-x-sp": "orthography2ipa.languages.pt_br_dialects",
    "pt-BR-x-caipira": "orthography2ipa.languages.pt_br_dialects",
    "pt-BR-x-rj": "orthography2ipa.languages.pt_br_dialects",
    "pt-BR-x-fluminense": "orthography2ipa.languages.pt_br_dialects",
    "pt-BR-x-mg": "orthography2ipa.languages.pt_br_dialects",
    "pt-BR-x-recife": "orthography2ipa.languages.pt_br_dialects",
    "pt-BR-x-bahia": "orthography2ipa.languages.pt_br_dialects",
    "pt-BR-x-ce": "orthography2ipa.languages.pt_br_dialects",
    "pt-BR-x-norte": "orthography2ipa.languages.pt_br_dialects",
    "pt-BR-x-sul": "orthography2ipa.languages.pt_br_dialects",
    "pt-BR-x-pr": "orthography2ipa.languages.pt_br_dialects",
    "pt-BR-x-brasilia": "orthography2ipa.languages.pt_br_dialects",

    # Spanish dialects of Spain
    "es-ES-x-andalusia-w": "orthography2ipa.languages.es",
    "es-ES-x-andalusia-e": "orthography2ipa.languages.es",
    "es-ES-x-murcia": "orthography2ipa.languages.es",
    "es-ES-x-canarias": "orthography2ipa.languages.es",
    "es-ES-x-cantabria": "orthography2ipa.languages.es",

    # Latin American Spanish dialects
    "es-419": "orthography2ipa.languages.es_latam",
    "es-AR": "orthography2ipa.languages.es_latam",
    "es-MX": "orthography2ipa.languages.es_latam",
    "es-MX-x-costa": "orthography2ipa.languages.es_latam",
    "es-CU": "orthography2ipa.languages.es_latam",
    "es-DO": "orthography2ipa.languages.es_latam",
    "es-PR": "orthography2ipa.languages.es_latam",
    "es-VE": "orthography2ipa.languages.es_latam",
    "es-GT": "orthography2ipa.languages.es_latam",
    "es-NI": "orthography2ipa.languages.es_latam",
    "es-CR": "orthography2ipa.languages.es_latam",
    "es-PA": "orthography2ipa.languages.es_latam",
    "es-CO": "orthography2ipa.languages.es_latam",
    "es-CO-x-costa": "orthography2ipa.languages.es_latam",
    "es-CO-x-paisa": "orthography2ipa.languages.es_latam",
    "es-PE": "orthography2ipa.languages.es_latam",
    "es-PE-x-lima": "orthography2ipa.languages.es_latam",
    "es-BO": "orthography2ipa.languages.es_latam",
    "es-EC": "orthography2ipa.languages.es_latam",
    "es-CL": "orthography2ipa.languages.es_latam",
    "es-PY": "orthography2ipa.languages.es_latam",
    "es-UY": "orthography2ipa.languages.es_latam",
    "es-GQ": "orthography2ipa.languages.es_latam",

    # Catalan dialects
    "ca-x-valencia": "orthography2ipa.languages.ca",
    "ca-x-balear": "orthography2ipa.languages.ca",
    "ca-x-nord": "orthography2ipa.languages.ca",
    "ca-x-occidental": "orthography2ipa.languages.ca",

    # Basque dialects
    "eu-x-bizkaiera": "orthography2ipa.languages.eu",
    "eu-x-gipuzkera": "orthography2ipa.languages.eu",
    "eu-x-nafarra-garaia": "orthography2ipa.languages.eu",
    "eu-x-zuberera": "orthography2ipa.languages.eu",
    "eu-x-nafarra-beherea": "orthography2ipa.languages.eu",
}

_GERMANIC = {
    # Proto-Germanic and Gothic
    "gem": "orthography2ipa.languages.germanic_ancestral",
    "gem-x-north": "orthography2ipa.languages.germanic_ancestral",
    "gem-x-northwest": "orthography2ipa.languages.germanic_ancestral",
    "gem-x-ingvaeonic": "orthography2ipa.languages.germanic_ancestral",
    "got": "orthography2ipa.languages.germanic_ancestral",

    # Historical/Medieval
    "non": "orthography2ipa.languages.germanic_ancestral",
    "ang": "orthography2ipa.languages.germanic_ancestral",
    "goh": "orthography2ipa.languages.germanic_ancestral",
    "osx": "orthography2ipa.languages.germanic_ancestral",
    "enm": "orthography2ipa.languages.germanic_ancestral",

    # Germanic
    "en": "orthography2ipa.languages.en",
    "de": "orthography2ipa.languages.de",
    "nl": "orthography2ipa.languages.nl",
    "sv": "orthography2ipa.languages.sv",
    "da": "orthography2ipa.languages.da",
    "no": "orthography2ipa.languages.no",
}

_ROMANCE = {
    "pt": "orthography2ipa.languages.pt",
    "es": "orthography2ipa.languages.es",
    "oc": "orthography2ipa.languages.oc",
    "fr": "orthography2ipa.languages.fr",
    "it": "orthography2ipa.languages.it",
    "ro": "orthography2ipa.languages.ro",

    # ── Franco-Provençal / Arpitan ───────────────────────────────────────
    "frp": "orthography2ipa.languages.romance_galloromance",

    # ── Rhaeto-Romance ───────────────────────────────────────────────────
    "rm": "orthography2ipa.languages.romance_galloromance",
    "lld": "orthography2ipa.languages.romance_galloromance",
    "fur": "orthography2ipa.languages.romance_galloromance",

    # ── Southern Italo-Romance ───────────────────────────────────────────
    "nap": "orthography2ipa.languages.romance_italo",
    "scn": "orthography2ipa.languages.romance_italo",
    "co": "orthography2ipa.languages.romance_italo",

    # ── Sardinian dialects ────────────────────────
    "sc-x-logudorese": "orthography2ipa.languages.sc",
    "sc-x-campidanese": "orthography2ipa.languages.sc",
}

_SLAVIC = {
    # Balkan substrates
    "xda": "orthography2ipa.languages.balkan_ancestral",
    "hu": "orthography2ipa.languages.balkan_ancestral",

    # ── Slavic: Proto and OCS ────────────────────────────────────────────────
    "sla": "orthography2ipa.languages.sla",
    "cu": "orthography2ipa.languages.cu",
    # ── Slavic: East ────────────────────────────────────────────────────────
    "ru": "orthography2ipa.languages.ru",
    "ru-x-moscow": "orthography2ipa.languages.ru",
    "ru-x-northern": "orthography2ipa.languages.ru",
    "ru-x-arkhangelsk": "orthography2ipa.languages.ru",
    "ru-x-vologda": "orthography2ipa.languages.ru",
    "ru-x-southern": "orthography2ipa.languages.ru",
    "ru-x-kursk-orel": "orthography2ipa.languages.ru",
    "ru-x-don": "orthography2ipa.languages.ru",
    "ru-x-siberian": "orthography2ipa.languages.ru",
    "ru-x-pskov": "orthography2ipa.languages.ru",
    "ru-x-ural": "orthography2ipa.languages.ru",
    "uk": "orthography2ipa.languages.uk",
    "be": "orthography2ipa.languages.be",
    # ── Slavic: West ─────────────────────────────────────────────────────────
    "pl": "orthography2ipa.languages.pl",
    "cs": "orthography2ipa.languages.cs",
    "sk": "orthography2ipa.languages.sk",
    # ── Slavic: South ────────────────────────────────────────────────────────
    "sr": "orthography2ipa.languages.sr",
    "hr": "orthography2ipa.languages.hr",
    "sl": "orthography2ipa.languages.sl",
    "bg": "orthography2ipa.languages.bg",
    "mk": "orthography2ipa.languages.mk",
}

_SEMITIC = {
    # ── Semitic: Proto chain ──────────────────────────────────────────────
    "sem": "orthography2ipa.languages.ar_proto",
    "sem-x-west": "orthography2ipa.languages.ar_proto",
    "sem-x-central": "orthography2ipa.languages.ar_proto",
    "xpa": "orthography2ipa.languages.ar_proto",
    # ── Semitic: Classical Arabic + branch nodes ──────────────────────────
    "arb": "orthography2ipa.languages.ar_classical",
    "ar-x-mashriqi": "orthography2ipa.languages.ar_classical",
    "ar-x-maghrebi": "orthography2ipa.languages.ar_classical",
    "ar-x-peninsular": "orthography2ipa.languages.ar_classical",
    # ── Semitic: MSA ─────────────────────────────────────────────────────
    "ar": "orthography2ipa.languages.ar",
    # ── Semitic: Eastern (Mashriqi) dialects ─────────────────────────────
    "ar-EG": "orthography2ipa.languages.ar_mashriqi",
    "ar-EG-x-said": "orthography2ipa.languages.ar_mashriqi",
    "ar-SD": "orthography2ipa.languages.ar_mashriqi",
    "ar-SY": "orthography2ipa.languages.ar_mashriqi",
    "ar-LB": "orthography2ipa.languages.ar_mashriqi",
    "ar-PS": "orthography2ipa.languages.ar_mashriqi",
    "ar-JO": "orthography2ipa.languages.ar_mashriqi",
    # ── Semitic: Maghrebi dialects ────────────────────────────────────────
    "ar-MA": "orthography2ipa.languages.ar_maghrebi",
    "ar-DZ": "orthography2ipa.languages.ar_maghrebi",
    "ar-TN": "orthography2ipa.languages.ar_maghrebi",
    "ar-LY": "orthography2ipa.languages.ar_maghrebi",
    "ar-MR": "orthography2ipa.languages.ar_maghrebi",
    # ── Semitic: Peninsular dialects ──────────────────────────────────────
    "ar-SA-x-hejaz": "orthography2ipa.languages.ar_peninsular",
    "ar-SA-x-najd": "orthography2ipa.languages.ar_peninsular",
    "ar-x-gulf": "orthography2ipa.languages.ar_peninsular",
    "ar-KW": "orthography2ipa.languages.ar_peninsular",
    "ar-BH": "orthography2ipa.languages.ar_peninsular",
    "ar-QA": "orthography2ipa.languages.ar_peninsular",
    "ar-AE": "orthography2ipa.languages.ar_peninsular",
    "ar-OM": "orthography2ipa.languages.ar_peninsular",
    "ar-YE": "orthography2ipa.languages.ar_peninsular",
    # ── Semitic: Peripheral / contact dialects ────────────────────────────
    "ar-IQ": "orthography2ipa.languages.ar_peripheral",
    "ar-IQ-x-qeltu": "orthography2ipa.languages.ar_peripheral",
    "ar-TD": "orthography2ipa.languages.ar_peripheral",
    "ar-NG": "orthography2ipa.languages.ar_peripheral",
    "acy": "orthography2ipa.languages.ar_peripheral",
}

_IRANIAN = {
    # ── Iranian: Proto chain ──────────────────────────────────────────────
    "iir": "orthography2ipa.languages.fa_proto",
    "ira": "orthography2ipa.languages.fa_proto",
    "peo": "orthography2ipa.languages.fa_proto",
    "pal": "orthography2ipa.languages.fa_proto",
    "fa-x-early": "orthography2ipa.languages.fa_proto",
    # ── Iranian: Standard Persian (fa) ────────────────────────────────────
    "fa": "orthography2ipa.languages.fa",
    # ── Iranian: Persian regional dialects ───────────────────────────────
    "fa-x-tehran": "orthography2ipa.languages.fa_dialects",
    "fa-x-isfahani": "orthography2ipa.languages.fa_dialects",
    "fa-x-shirazi": "orthography2ipa.languages.fa_dialects",
    "fa-x-kermani": "orthography2ipa.languages.fa_dialects",
    "fa-x-khorasani": "orthography2ipa.languages.fa_dialects",
    "fa-x-yazdi": "orthography2ipa.languages.fa_dialects",
    "fa-x-mashhadi": "orthography2ipa.languages.fa_dialects",
    # ── Iranian: Dari and Tajik ───────────────────────────────────────────
    "fa-AF": "orthography2ipa.languages.fa_dialects",
    "fa-x-hazaragi": "orthography2ipa.languages.fa_dialects",
    "tg": "orthography2ipa.languages.fa_dialects",
}

_INDO_ARIAN = {
    # ── Indo-Aryan: Proto and Classical ─────────────────────────────────────
    "sa": "orthography2ipa.languages.sa",  # Sanskrit
    "sa-x-vedic": "orthography2ipa.languages.sa",  # Vedic Sanskrit
    "pi": "orthography2ipa.languages.sa",  # Pali

    # ── Indo-Aryan: Hindi-Urdu belt ─────────────────────────────────────────
    "hi": "orthography2ipa.languages.hi",  # Hindi
    "ur": "orthography2ipa.languages.ur",  # Urdu
    "bho": "orthography2ipa.languages.indic_other",  # Bhojpuri

    # ── Indo-Aryan: Dardic ───────────────────────────────────────────────────
    "ks": "orthography2ipa.languages.indic_east",  # Kashmiri

    # ── Indo-Aryan: Northwest ────────────────────────────────────────────────
    "pa": "orthography2ipa.languages.pa",  # Punjabi (Gurmukhi)
    "pa-PK": "orthography2ipa.languages.pa",  # Western Punjabi (Shahmukhi)
    "sd": "orthography2ipa.languages.indic_east",  # Sindhi

    # ── Indo-Aryan: West ────────────────────────────────────────────────────
    "gu": "orthography2ipa.languages.gu_mr_ne",  # Gujarati
    "mr": "orthography2ipa.languages.gu_mr_ne",  # Marathi
    "kok": "orthography2ipa.languages.indic_other",  # Konkani

    # ── Indo-Aryan: East ────────────────────────────────────────────────────
    "bn": "orthography2ipa.languages.bn",  # Bengali
    "as": "orthography2ipa.languages.bn",  # Assamese
    "or": "orthography2ipa.languages.indic_east",  # Odia
    "mai": "orthography2ipa.languages.indic_east",  # Maithili

    # ── Indo-Aryan: South ────────────────────────────────────────────────────
    "ne": "orthography2ipa.languages.gu_mr_ne",  # Nepali
    "si": "orthography2ipa.languages.indic_other",  # Sinhala


}

_DRAVIDIAN = {

    # ── Dravidian: Proto ─────────────────────────────────────────────────────
    "ta-x-proto-dravidian": "orthography2ipa.languages.indic_misc",

    # ── Dravidian: South I ───────────────────────────────────────────────────
    "ta": "orthography2ipa.languages.ta",  # Tamil
    "ml": "orthography2ipa.languages.te_kn_ml",  # Malayalam
    "kn": "orthography2ipa.languages.te_kn_ml",  # Kannada
    "tcy": "orthography2ipa.languages.indic_misc",  # Tulu

    # ── Dravidian: South II ──────────────────────────────────────────────────
    "te": "orthography2ipa.languages.te_kn_ml",  # Telugu
}

_ASIAN = {
    # CJK
    "zh": "orthography2ipa.languages.zh",
    "ja": "orthography2ipa.languages.ja",
    "ko": "orthography2ipa.languages.ko",
}

_LANG_MODULES: Dict[str, str] = {
    **_LATIN,
    **_ROMANCE,
    **_IBERIAN,
    **_CELTIC,
    **_SLAVIC,
    **_GERMANIC,
    **_SEMITIC,
    **_IRANIAN,
    **_INDO_ARIAN,
    **_DRAVIDIAN,
    **_ASIAN,

    # Classical / reconstructed
    "grc": "orthography2ipa.languages.grc",
    "ine": "orthography2ipa.languages.ine",

    # Turkic
    "tr": "orthography2ipa.languages.tr",
    # Uralic
    "fi": "orthography2ipa.languages.fi",
    # Hellenic
    "el": "orthography2ipa.languages.el",


    # ── Austroasiatic: Munda ─────────────────────────────────────────────────
    "sat": "orthography2ipa.languages.munda_tb",  # Santali
    "unr": "orthography2ipa.languages.munda_tb",  # Mundari

    # ── Austroasiatic: Mon-Khmer ─────────────────────────────────────────────
    "kha": "orthography2ipa.languages.indic_misc",  # Khasi

    # ── Tibeto-Burman ────────────────────────────────────────────────────────
    "mni": "orthography2ipa.languages.munda_tb",  # Meitei/Manipuri
    "brx": "orthography2ipa.languages.munda_tb",  # Bodo

}

_cache: Dict[str, LanguageSpec] = {}


def _resolve_code(code: str) -> str:
    """Normalise common aliases."""
    # TODO - use langcodes library
    aliases = {
        "por": "pt", "eng": "en", "spa": "es", "fra": "fr", "deu": "de",
        "ita": "it", "nld": "nl", "swe": "sv", "dan": "da", "nor": "no",
        "rus": "ru", "ukr": "uk", "ara": "ar", "fas": "fa", "hin": "hi",
        "zho": "zh", "jpn": "ja", "kor": "ko", "eus": "eu", "cat": "ca",
        "glg": "gl", "oci": "oc", "tur": "tr", "fin": "fi", "ell": "el",
        "pol": "pl", "ces": "cs", "ron": "ro",
        "mwl": "mwl",  # Mirandese ISO 639-3
        "arg": "an",  # Aragonese ISO 639-3
        "lat": "la",  # Classical Latin ISO 639-2
        # Semitic proto-languages and contact varieties
        "arb": "arb",  # Classical Arabic ISO 639-3
        "phn": "phn",  # Phoenician ISO 639-3
        "acy": "acy",  # Cypriot Maronite Arabic ISO 639-3
        # Iranian proto-languages
        "peo": "peo",  # Old Persian ISO 639-3
        "pal": "pal",  # Middle Persian / Pahlavi ISO 639-3
        # Tajik aliases
        "tgk": "tg",  # Tajik ISO 639-3
        # Dari alias
        "prs": "fa-AF",  # Dari ISO 639-3
    }
    return aliases.get(code, code)


def get(code: str) -> LanguageSpec:
    """Return the :class:`LanguageSpec` for *code*, loading lazily.

    Args:
        code: BCP-47 language code (e.g. ``'en'``, ``'pt-BR'``) or
              ISO 639-3 three-letter code (e.g. ``'eng'``, ``'por'``).

    Raises:
        KeyError: If the language is not registered.
    """
    code = _resolve_code(code)
    if code in _cache:
        return _cache[code]

    mod_path = _LANG_MODULES.get(code)
    if mod_path is None:
        raise KeyError(
            f"Language '{code}' is not registered. "
            f"Available: {', '.join(sorted(available_codes()))}"
        )

    mod = importlib.import_module(mod_path)
    # Each module exposes SPECS: dict[str, LanguageSpec]
    specs: Dict[str, LanguageSpec] = mod.SPECS
    # Cache every spec the module provides
    for c, spec in specs.items():
        _cache[c] = spec

    if code not in _cache:
        raise KeyError(
            f"Module {mod_path} does not provide code '{code}'. "
            f"It provides: {', '.join(specs)}"
        )
    return _cache[code]


def available_codes() -> List[str]:
    """Return all registered language codes."""
    return sorted(_LANG_MODULES)


def available_families() -> Dict[str, List[str]]:
    """Return ``{family: [codes]}`` for every loaded language."""
    fam: Dict[str, List[str]] = {}
    for code in available_codes():
        try:
            spec = get(code)
        except (KeyError, ModuleNotFoundError):
            continue
        fam.setdefault(spec.family, []).append(code)
    return fam
