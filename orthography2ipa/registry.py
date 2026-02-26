"""Language registry with lazy loading."""
from __future__ import annotations

from typing import Dict, List

from orthography2ipa.json_loader import available_json_codes, load_json_spec
from orthography2ipa.types import LanguageSpec

_cache: Dict[str, LanguageSpec] = {}


def _resolve_code(code: str) -> str:
    """Normalise common aliases."""
    # TODO - use langcodes library
    aliases = {
        "por": "pt-PT", "eng": "en-GB", "spa": "es-ES", "fra": "fr-FR", "deu": "de-DE",
        "ita": "it-IT", "nld": "nl", "swe": "sv", "dan": "da", "nor": "no",
        "rus": "ru", "ukr": "uk", "ara": "ar", "fas": "fa", "hin": "hi",
        "zho": "zh", "jpn": "ja", "kor": "ko", "eus": "eu", "cat": "ca",
        "glg": "gl-ES", "oci": "oc", "tur": "tr", "fin": "fi", "ell": "el",
        "pol": "pl", "ces": "cs", "ron": "ro-RO",
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
