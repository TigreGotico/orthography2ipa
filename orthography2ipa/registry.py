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


def available_codes(include_clades: bool = False) -> List[str]:
    """Return all registered language codes.

    Classification-only clade nodes (``Romance``, ``West Germanic``) are not
    languages — they carry no phonology and cannot be transcribed — so they
    are excluded unless *include_clades* is set.
    """
    codes = sorted(available_json_codes())
    if include_clades:
        return codes
    keep: List[str] = []
    for code in codes:
        try:
            if not get(code).clade:
                keep.append(code)
        except (KeyError, ValueError, ModuleNotFoundError):
            keep.append(code)
    return keep


def ancestry_chain(code: str) -> List[str]:
    """Return the ``parent`` chain above *code*, nearest ancestor first.

    Includes the classification-only clade nodes the chain passes through
    (``["ber", "x-clade-berb1260", "afa", "x-clade-afro1255"]``).
    """
    chain: List[str] = []
    seen = {resolve(code)}
    parent = get(code).parent
    while parent and parent not in seen:
        chain.append(parent)
        seen.add(parent)
        try:
            parent = get(parent).parent
        except KeyError:
            break
    return chain


def available_families() -> Dict[str, List[str]]:
    """Return ``{family: [codes]}`` for every loaded language.

    The key is the classification path derived from the clade nodes on the
    ancestry chain (``"Indo-European > Italic > Romance > Ibero-Romance"``).
    Callers filter at any depth — ``orthography2ipa list --family Romance``
    matches any single step of the path.
    """
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
    eps = entry_points(group="orthography2ipa.syllabify")
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


# ═══════════════════════════════════════════════════════════════════════════
# Rescorer plugins — phonology contributed for one language
# ═══════════════════════════════════════════════════════════════════════════

_rescorer_plugins: Optional[Dict[str, List["RescorerPlugin"]]] = None


def _discover_rescorer_plugins() -> Dict[str, List["RescorerPlugin"]]:
    """Discover rescorer plugins via importlib entry points.

    Unlike a syllabifier, several rescorer plugins may claim the same language and
    ALL of them run: realization is a cascade, not a competition. They are ordered
    by priority, lowest first, so a higher-priority plugin sees the lower one's
    work and gets the last word.
    """
    import logging
    from importlib.metadata import entry_points

    plugins: Dict[str, List["RescorerPlugin"]] = {}
    for ep in entry_points(group="orthography2ipa.rescore"):
        try:
            instance = ep.load()()
            for code in instance.language_codes:
                plugins.setdefault(code, []).append(instance)
        except Exception as exc:
            logging.getLogger(__name__).warning(
                "failed to load rescorer plugin %r: %s", ep.name, exc)
            continue
    for code in plugins:
        plugins[code].sort(key=lambda p: p.priority)
    return plugins


def get_rescorers(code: str) -> List["LatticeRescorer"]:
    """The rescorers every registered plugin contributes for *code*, in order."""
    global _rescorer_plugins
    if _rescorer_plugins is None:
        _rescorer_plugins = _discover_rescorer_plugins()
    resolved = _resolve_code(code)
    out: List["LatticeRescorer"] = []
    for plugin in _rescorer_plugins.get(resolved, ()):
        out.extend(plugin.rescorers(resolved))
    return out


def who_answers(code: str) -> Dict[str, object]:
    """Who is answering for *code*, and from where.

    The first question anyone debugging a plugin asks, given an API. A
    transcription that depends on what is installed should at least be able to say
    what is installed.
    """
    resolved = _resolve_code(code)
    syllabifier = get_syllabifier(resolved)
    global _rescorer_plugins
    if _rescorer_plugins is None:
        _rescorer_plugins = _discover_rescorer_plugins()
    return {
        "code": resolved,
        "syllabify": (
            f"{type(syllabifier).__module__}.{type(syllabifier).__name__}"
            if syllabifier is not None else "built-in"
        ),
        "rescore": [
            f"{type(p).__module__}.{type(p).__name__} (priority {p.priority})"
            for p in _rescorer_plugins.get(resolved, ())
        ] or ["built-in (spec allophone_rules only)"],
    }


# ═══════════════════════════════════════════════════════════════════════════
# Stress plugins — consulted only when the SPEC asks for one
# ═══════════════════════════════════════════════════════════════════════════

_stress_plugins: Optional[Dict[str, "StressPlugin"]] = None


def _discover_stress_plugins() -> Dict[str, "StressPlugin"]:
    import logging
    from importlib.metadata import entry_points

    plugins: Dict[str, "StressPlugin"] = {}
    for ep in entry_points(group="orthography2ipa.stress"):
        try:
            instance = ep.load()()
            for code in instance.language_codes:
                incumbent = plugins.get(code)
                if incumbent is None or instance.priority > incumbent.priority:
                    plugins[code] = instance
        except Exception as exc:
            logging.getLogger(__name__).warning(
                "failed to load stress plugin %r: %s", ep.name, exc)
            continue
    return plugins


def get_stress_plugin(code: str) -> Optional["StressPlugin"]:
    """The stress plugin registered for *code*, if any."""
    global _stress_plugins
    if _stress_plugins is None:
        _stress_plugins = _discover_stress_plugins()
    return _stress_plugins.get(_resolve_code(code))


class MissingStressPlugin(RuntimeError):
    """A spec asked for a stress plugin and none is registered.

    Deliberately fatal. A spec that sets ``stress.source = "plugin"`` is saying its
    stress cannot be expressed by the declarative rules — so falling back to them
    would not be a graceful degradation, it would be a DIFFERENT ANSWER, silently.
    The transcription must be a function of the spec and the input; quietly
    substituting a different stress model makes it a function of what happens to
    be installed, which is the bug this rule exists to prevent.
    """


# ═══════════════════════════════════════════════════════════════════════════
# Declared plugins — the spec names them, by entry-point name
# ═══════════════════════════════════════════════════════════════════════════

class MissingPlugin(RuntimeError):
    """A spec named a plugin and it is not installed.

    Deliberately fatal. The spec asked for this plugin because the built-in answer
    is not the answer it wants — so falling back to the built-in would not be a
    graceful degradation, it would be a DIFFERENT TRANSCRIPTION, silently, with no
    way for the caller to know which one they got.
    """


_declared: Dict[str, Dict[str, object]] = {}


def _discover_stage(stage: str) -> Dict[str, object]:
    """Every plugin registered for *stage*, keyed by its ENTRY-POINT NAME.

    The name is the plugin's identity, and it is what a spec names. That makes the
    declaration readable and greppable — and it means two packages cannot fight
    over a language, because the spec already said which one it wanted.
    """
    import logging
    from importlib.metadata import entry_points

    from orthography2ipa.plugins import ENTRY_POINT_GROUPS

    found: Dict[str, object] = {}
    for ep in entry_points(group=ENTRY_POINT_GROUPS[stage]):
        try:
            found[ep.name] = ep.load()()
        except Exception as exc:
            logging.getLogger(__name__).warning(
                "failed to load %s plugin %r: %s", stage, ep.name, exc)
    return found


def get_declared_plugins(stage: str, spec) -> List[object]:
    """The plugins *spec* names for *stage*, in the order it names them.

    Raises :class:`MissingPlugin` for a name the spec asks for and nothing
    provides.
    """
    names = (spec.plugins or {}).get(stage, ())
    if not names:
        return []

    if stage not in _declared:
        _declared[stage] = _discover_stage(stage)
    available = _declared[stage]

    out: List[object] = []
    for name in names:
        plugin = available.get(name)
        if plugin is None:
            raise MissingPlugin(
                f"the {spec.code!r} spec names the {stage} plugin {name!r}, and it "
                f"is not installed.\n\n"
                f"Installed for this stage: {sorted(available) or 'nothing'}.\n\n"
                f"This is fatal on purpose. The spec asked for this plugin because "
                f"the built-in answer is not the answer it wants — so falling back "
                f"would not be a graceful degradation, it would be a DIFFERENT "
                f"TRANSCRIPTION, silently. Install it, or change the spec."
            )
        out.append(plugin)
    return out
