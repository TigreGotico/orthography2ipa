"""Language registry with lazy loading and plugin discovery."""
from __future__ import annotations

import logging
from functools import lru_cache
from typing import TYPE_CHECKING, Dict, List, Optional

from ovos_spec_tools.language import closest_lang

from orthography2ipa.json_loader import available_json_codes, load_json_spec
from orthography2ipa.types import LanguageSpec

if TYPE_CHECKING:
    from orthography2ipa.syllabifier_plugin import SyllabifierPlugin

_cache: Dict[str, LanguageSpec] = {}

_LOG = logging.getLogger(__name__)

# Fallback alias table for ISO 639-3 → BCP-47 normalisation.
# When ``langcodes`` is available, standard codes are resolved via that library.
# Private-use subtags (e.g. ``ast-PT-x-rionor``) always use this table.
_ALIASES: Dict[str, str] = {
    "por": "pt-PT", "eng": "en-GB", "spa": "es-ES", "fra": "fr-FR", "deu": "de-DE",
    "ita": "it-IT", "nld": "nl", "swe": "sv", "dan": "da", "nor": "no",
    "rus": "ru", "ukr": "uk", "ara": "ar", "fas": "fa", "hin": "hi",
    "zho": "zh", "jpn": "ja", "kor": "ko", "eus": "eu", "cat": "ca",
    "glg": "gl", "oci": "oc", "tur": "tr", "fin": "fi", "ell": "el",
    "pol": "pl", "ces": "cs", "ron": "ro-RO",
    "mwl": "mwl",  # Mirandese ISO 639-3
    "ast": "ast",  # Asturian ISO 639-3
    "arg": "an",   # Aragonese ISO 639-3
    "lat": "la",   # Classical Latin ISO 639-2
    # Semitic proto-languages and contact varieties
    "arb": "arb",  # Classical Arabic ISO 639-3
    "phn": "phn",  # Phoenician ISO 639-3
    "acy": "acy",  # Cypriot Maronite Arabic ISO 639-3
    # Iranian proto-languages
    "peo": "peo",  # Old Persian ISO 639-3
    "pal": "pal",  # Middle Persian / Pahlavi ISO 639-3
    # Tajik aliases
    "tgk": "tg",   # Tajik ISO 639-3
    # Dari alias
    "prs": "fa-AF",  # Dari ISO 639-3
}

# Default variant for a bare primary-language tag whose specs are all
# regional. ``langcodes`` resolves a bare tag towards its most-populous
# region (``pt`` → ``pt-BR``); the unmarked form of a language should
# resolve to its reference variety instead, matching the ISO 639-3
# aliases above (``por`` → ``pt-PT``, ``eng`` → ``en-GB``).
_BARE_DEFAULTS: Dict[str, str] = {
    "de": "de-DE",
    "en": "en-GB",
    "es": "es-ES",
    "fr": "fr-FR",
    "it": "it-IT",
    "pt": "pt-PT",
    "ro": "ro-RO",
}

try:
    import langcodes as _langcodes
    _HAS_LANGCODES = True
except ImportError:
    _HAS_LANGCODES = False


@lru_cache(maxsize=None)
def _resolve_code(code: str) -> str:
    """Normalise common aliases to canonical BCP-47 codes.

    Resolution order:
    1. Manual alias table (handles private-use subtags and ISO 639-3 codes
       that ``langcodes`` may not round-trip cleanly).
    2. ``langcodes.standardize_tag()`` when the library is available and the
       code is not a private-use subtag (``x-`` extension).
    3. Exact match against the registered spec codes.
    4. Curated default variant for a bare primary-language tag
       (``pt`` → ``pt-PT``).
    5. Nearest registered code by language distance
       (``en-NZ`` → ``en-GB``); no usable match leaves *code* unchanged.
    """
    if code in _ALIASES:
        return _ALIASES[code]
    if _HAS_LANGCODES and "-x-" not in code and not code.startswith("x-"):
        try:
            code = _langcodes.standardize_tag(code, macro=True)
        except Exception:
            pass
        if code in _ALIASES:
            return _ALIASES[code]
    available = available_json_codes()
    if code in available:
        return code
    if code in _BARE_DEFAULTS:
        return _BARE_DEFAULTS[code]
    match = closest_lang(code, available)
    if match:
        _LOG.debug("resolved language code %r to nearest registered %r",
                   code, match)
        return match
    return code


def resolve(code: str) -> str:
    """Return the registered spec code that *code* resolves to.

    Applies the same normalisation as :func:`get` — alias tables,
    BCP-47 standardization, curated bare-tag defaults and
    nearest-language matching — without loading the spec. A code with
    no usable resolution is returned unchanged (so :func:`get` raises
    ``KeyError`` for it).
    """
    return _resolve_code(code)


def get(code: str) -> LanguageSpec:
    """Return the :class:`LanguageSpec` for *code*, loading lazily.

    Args:
        code: BCP-47 language code (e.g. ``'en'``, ``'pt-BR'``) or
              ISO 639-3 three-letter code (e.g. ``'eng'``, ``'por'``).

    Raises:
        KeyError: If the language is not registered.
    """
    global _cache
    code = _resolve_code(code)
    if code not in _cache:
        _cache[code] = load_json_spec(code)
    return _cache[code]


def available_codes() -> List[str]:
    """Return all registered language codes."""
    return sorted(available_json_codes())


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


_syllabifiers: Optional[Dict[str, "SyllabifierPlugin"]] = None


def _discover_syllabifiers() -> Dict[str, "SyllabifierPlugin"]:
    """Discover syllabifier plugins via importlib entry_points.

    When several plugins claim the same language code, the one with the
    highest :attr:`SyllabifierPlugin.priority` wins.
    """
    import logging
    from importlib.metadata import entry_points

    plugins: Dict[str, "SyllabifierPlugin"] = {}
    try:
        eps = entry_points(group="orthography2ipa.syllabify")
    except TypeError:
        # Python 3.9 compat
        eps = entry_points().get("orthography2ipa.syllabify", [])
    for ep in eps:
        try:
            instance = ep.load()()
            for code in instance.language_codes:
                incumbent = plugins.get(code)
                if incumbent is None or instance.priority > incumbent.priority:
                    plugins[code] = instance
        except Exception as exc:
            logging.getLogger(__name__).warning(
                "failed to load syllabifier plugin %r: %s", ep.name, exc)
            continue
    return plugins


def get_syllabifier(code: str) -> Optional["SyllabifierPlugin"]:
    """Return the syllabifier plugin for *code*, if one is registered."""
    global _syllabifiers
    if _syllabifiers is None:
        _syllabifiers = _discover_syllabifiers()
    code = _resolve_code(code)
    return _syllabifiers.get(code)
