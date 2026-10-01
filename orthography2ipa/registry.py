"""Language registry with lazy loading and plugin discovery."""
from __future__ import annotations

import logging
from functools import lru_cache
from importlib.metadata import entry_points
from typing import TYPE_CHECKING, Dict, List, Optional, Tuple

from ovos_spec_tools.language import closest_lang

from orthography2ipa.exceptions import UnknownLanguageVariantError
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
    # Individual-code specs that langcodes would otherwise collapse into a
    # newly-added macrolanguage spec: ``bxr`` (Russia Buriat) standardizes to
    # ``bua`` (Buriat macrolanguage) and ``diq`` (Dimli) to ``zza`` (Zaza
    # macrolanguage). Both the individual and the macro spec exist and are
    # distinct targets, so pin each individual code to itself before the
    # macro-collapse step can rewrite it.
    "bxr": "bxr",
    "diq": "diq",
    # ``quz`` (Cusco Quechua) and ``quy`` (Ayacucho Quechua) are individual
    # -language codes that langcodes' macro=True standardisation collapses
    # into their macrolanguage ``qu`` (Quechua), same class of collision as
    # bxr/diq above. Both the individual specs and the macro node exist and
    # are distinct targets — ``qu`` is only a structural adstrate stub.
    "quz": "quz",
    "quy": "quy",
    # ``tw`` (Twi) and ``fat`` (Fante) are individual-language codes that
    # langcodes' macro=True standardisation collapses into their
    # macrolanguage ``ak`` (Akan), same class of collision as bxr/diq above.
    # Both the individual and the macro spec exist and are distinct targets.
    "tw": "tw",
    "fat": "fat",
    # Individual-code specs collapsing into the newly-added Mari macrolanguage
    # spec: ``mhr`` (Eastern/Meadow Mari) and ``mrj`` (Hill/Western Mari)
    # standardize to ``chm`` (Mari macrolanguage). Pin each individual code to
    # itself so the macro-collapse step does not rewrite it.
    "mhr": "mhr",
    "mrj": "mrj",
    # ``aju`` (Judeo-Moroccan Arabic) is an individual-language code that
    # langcodes' macro=True standardisation collapses into its
    # macrolanguage ``jrb`` (Judeo-Arabic), same class of collision as
    # bxr/diq/tw/fat above. Both the individual and the macro spec exist
    # and are distinct targets.
    "aju": "aju",
    # ``als`` (Tosk Albanian) standardizes to ``sq`` (Albanian macrolanguage)
    # and ``rmy`` (Vlax Romani) standardizes to ``rom`` (Romani macrolanguage).
    # Both the individual and the macro spec exist and are distinct targets,
    # so pin each individual code to itself before the macro-collapse step.
    "als": "als",
    "rmy": "rmy",
    # ``src`` (Logudorese Sardinian) standardizes straight to ``sc`` (the
    # generic Sardinian macrolanguage spec) under ``langcodes``, which would
    # otherwise shadow the dedicated ``src`` spec. Pin it to itself.
    "src": "src",
    # ``oji`` (Ojibwa macrolanguage) and ``mnk`` (Mandinka) gained real specs
    # while the registry also carries their langcodes-preferred siblings
    # (``ojg`` Eastern Ojibwa, ``emk`` Eastern Maninkakan). Pin each to itself
    # so standardisation does not rewrite an exact-file hit, same class of
    # collision as bxr/diq above.
    "oji": "oji",
    "mnk": "mnk",
    # ``haz`` (Hazaragi) has no own spec; the modelled variety lives at
    # ``fa-x-hazaragi`` (Persian dialect continuum, Mongolic substrate).
    "haz": "fa-x-hazaragi",
    # ``kas`` (Kashmiri) is an ISO 639-3 individual code that langcodes'
    # macro=True standardisation collapses into its macrolanguage tag ``ks``
    # (Kashmiri, ISO 639-1) — same collision class as bxr/diq above. ``ks``
    # already carries a Latin-transliteration research-tier spec; ``kas``
    # is a distinct, separately-cited spec for the Perso-Arabic native
    # script. Pin it to itself so the macro-collapse step does not shadow it.
    "kas": "kas",
    # ``bcc`` (Southern Balochi) is an ISO 639-3 individual code that
    # langcodes' macro=True standardisation collapses into its
    # macrolanguage tag ``bal`` (Balochi) — same collision class as
    # bxr/diq above. ``bal`` is a newly-added macrolanguage-level spec;
    # ``bcc`` is a distinct, separately-cited individual-variety spec.
    # Pin it to itself so the macro-collapse step does not shadow it.
    "bcc": "bcc",
    # Arabic spoken-dialect ISO 639-3 codes → the o2i lect that describes the
    # same variety. WikiPron and most NLP corpora tag Arabic dialects by these
    # ISO 639-3 codes; o2i keys them by BCP-47 region/variant subtags. These
    # aliases let ``get("arz")`` resolve to the Egyptian Arabic spec, etc.
    "arz": "ar-EG",           # Egyptian Arabic
    "ary": "ar-MA",           # Moroccan Arabic (Darija)
    "apc": "ar-SY",           # North Levantine Arabic (Syrian/Lebanese core)
    "ajp": "ar-JO",           # South Levantine Arabic (Jordanian/Palestinian)
    "afb": "ar-x-gulf",       # Gulf Arabic
    "acw": "ar-SA-x-hejaz",   # Hijazi Arabic
    # ``abv`` (Baharna) resolved to a zero-grapheme placeholder while the modelled
    # spec describes the variety with the Gulf table plus its own reflexes. The
    # placeholder is deleted with the alias, as for acm: a spec file must stay
    # reachable by its own code.
    "abv": "ar-BH-x-baharna",  # Bahārna Arabic (B dialects of Bahrain)
    "aec": "ar-EG-x-saidi",   # Saʿīdi (Upper Egyptian) Arabic
    "avl": "ar-EG-x-bedawi",  # Eastern Egyptian Bedawi Arabic
    "adf": "ar-OM-x-dhofari", # Dhofari Arabic
    "acx": "ar-OM",           # Omani Arabic
    "apd": "ar-SD",           # Sudanese Arabic
    "ayn": "ar-YE",           # Sanaani Arabic
    "mey": "ar-MR",           # Hassaniyya
    "shu": "ar-TD",           # Chadian Arabic (ar-NG is its child)
    # ``pnb`` (Western Panjabi) is an ISO 639-3 individual code that resolved to
    # ``lah``, its macrolanguage, which carries no graphemes at all -- so the
    # code reached a spec that produces nothing while ``pa-PK`` describes the
    # same variety with 57 keys and declares the code.
    "pnb": "pa-PK",           # Western Punjabi (Shahmukhi)
    # Codes with exactly one declaring spec, whose name is the same language as
    # the code's, and no file of their own to shadow them. Same shape as the
    # Arabic country codes above.
    "ajg": "aja",             # Aja (Adja)
    "gej": "gen",             # Gen (Mina)
    "xdc": "xda",             # Dacian/Thracian
    # ``cbk`` resolved to ``cbk-x-cavite``, a variety spec that declares no
    # graphemes and inherits none, so the code reached an empty table while
    # ``cbk-zam`` describes Chavacano with 37 keys and declares the code.
    "cbk": "cbk-zam",         # Chavacano (Zamboangueño)
    # ``bar`` resolved to ``bar.json``, a placeholder with no graphemes and no
    # base, while ``de-x-bavarian`` declares the code and inherits a table
    # through ``graphemes_base: de-AT``. Deleting the placeholder rather than
    # leaving it to shadow the real spec is the same call this batch makes for
    # aec, avl and adf, and the placeholder's own notes already describe
    # Bavarian as "an Upper German variety of Bavaria, Austria and South Tyrol".
    "bar": "de-x-bavarian",   # Bavarian (Boarisch)
    # ``ars`` (Najdi Arabic) is declared by four Saudi specs and was reached by
    # none of them: langcodes placed it on ``ar-SA`` and the nearest match came
    # back ``ar-SA-x-dawasir``, which declares ``afb`` and is a different
    # variety, so the caller got Gulf Arabic for a Najdi tag with no error.
    #
    # ``ar-SA-x-najd`` is the target because it is the only one of the four
    # named Najdi Arabic and the only one holding glottocode najd1235 in its own
    # right; ``ar-SA-x-qassim`` is its child and shares that code. The other two
    # are not sub-varieties of it -- ``ar-SA-x-rijal-alma`` and
    # ``ar-SA-x-tihama-qahtan`` both parent to ``ar-x-peninsular`` with no
    # glottocode, and neither ʿAsīr nor the Tihāma coast is in Najd. That those
    # two declare ``ars`` at all is a separate question from which spec the code
    # should reach, and one this alias does not answer.
    "ars": "ar-SA-x-najd",    # Najdi Arabic
    # ``acm`` (Mesopotamian Arabic) is the ISO code for the variety ``ar-IQ``
    # already describes: ``ar-IQ`` declares ``glottolog_code`` meso1252 (Gilit
    # Mesopotamian Arabic) and ``iso639_3`` acm. It resolved to a separate
    # 44-key skeleton whose key set was a strict subset of ``ar-IQ``'s, so
    # ``get("acm")`` returned a poorer description of the same dialect.
    "acm": "ar-IQ",           # Mesopotamian Arabic (gilit; Glottolog meso1252)
    # Dialects named in a private-use subtag. langcodes ignores private-use
    # content when it measures tag distance, so ``ar-x-najdi`` would otherwise
    # fall to the nearest bare match (``ar``); pin the spoken adjective to the
    # spec, whose own token differs (``najdi`` -> ``najd``).
    "ar-x-najdi": "ar-SA-x-najd",     # Najdi Arabic
    "ar-x-hejazi": "ar-SA-x-hejaz",   # Hejazi Arabic
    "ar-x-hijazi": "ar-SA-x-hejaz",   # Hejazi Arabic (alternate romanization)
    # Barranquenho is keyed ``ext-PT-x-barrancos``: a language of its own spoken
    # in Portugal, not a Portuguese dialect. ``pt-PT-x-barrancos`` is a retired
    # spelling of the same lect; without the alias ``closest_lang`` resolves it
    # to ``pt-AO`` and returns Angolan Portuguese.
    "pt-PT-x-barrancos": "ext-PT-x-barrancos",
    # Spellings the downstream Portuguese front-end uses for three lects
    # whose spec keys are shorter; without these the tags fall to the bare
    # region and lose the lect.
    "pt-BR-x-sao-paulo": "pt-BR-x-sp",
    "pt-BR-x-rio-janeiro": "pt-BR-x-rj",
    "pt-PT-x-lisboa": "pt-PT-x-lisbon",
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

# Default variety for a region tag whose specs are all sub-regional, so a bare
# region has no exact spec and langcodes' nearest match would pick whichever
# private-use sibling sorts first. This is an explicit editorial convention,
# not a claim in the spec data: Saudi Arabia has several documented varieties
# (Najdi, Hejazi, ...) and no single standard spoken form, so ``ar-SA`` is
# steered to Najdi — the variety of the capital region (Riyadh) and the most
# widely spoken (Ingham, Najdi Arabic, 1994) — rather than asserting that
# Saudi Arabic *is* Najdi anywhere in the data.
_REGION_DEFAULTS: Dict[str, str] = {
    "ar-SA": "ar-SA-x-najd",
}

try:
    import langcodes as _langcodes
    _HAS_LANGCODES = True
except ImportError:
    _HAS_LANGCODES = False


@lru_cache(maxsize=None)
def _declares_iso(spec_code: str, requested: str) -> bool:
    """True when the spec at *spec_code* names *requested* as its own ISO
    639-3 code.

    A declared ISO code crosses the primary subtag by design: ``ar-TN``
    declares ``aeb`` and ``tl`` declares ``tgl``, and a caller asking for
    Tunisian Arabic by its ISO code is asking for exactly that spec. Reading
    the spec costs one load, and only on the path where the distance match
    already crossed languages.
    """
    if "-" in requested or len(requested) != 3:
        return False
    try:
        declared = getattr(load_json_spec(spec_code), "iso639_3", None)
    except Exception:
        return False
    return bool(declared) and declared.lower() == requested.lower()


@lru_cache(maxsize=None)
def _resolve_detail(code: str) -> Tuple[str, str]:
    """Resolve *code* and say HOW it resolved.

    Returns ``(resolved, kind)``. The kind is what decides whether a caller
    has to opt in:

    - ``"exact"``: the code names a registered spec, directly or through the
      alias table, case folding, BCP-47 standardization or a curated default.
      Every one of those names a spec deliberately.
    - ``"region"``: no spec for this region, and the nearest registered code
      is in the same language (``ar-ZZ`` -> ``ar``, ``en-NZ`` -> ``en-GB``).
      Ordinary BCP-47 matching, and a caller can want it.
    - ``"unknown-variant"``: the code carries a private-use ``-x-`` subtag
      that no spec and no alias answers. The caller named a lect; a sibling
      is a different lect.
    - ``"cross-language"``: the nearest match changes the primary language.
    - ``"unresolved"``: nothing matched; *resolved* is *code* unchanged, and
      :func:`get` raises ``KeyError`` for it.

    The two guessing kinds are refused by :func:`get` and :func:`resolve`
    unless the caller passes ``fallback=True`` (decision
    ``o2i-resolver-fallback``, 2026-09-25).
    """
    requested = code
    if code in _ALIASES:
        return _ALIASES[code], "exact"
    if _HAS_LANGCODES and "-x-" not in code and not code.startswith("x-"):
        try:
            code = _langcodes.standardize_tag(code, macro=True)
        except Exception:
            pass
        if code in _ALIASES:
            return _ALIASES[code], "exact"
    available = available_json_codes()
    if code in available:
        return code, "exact"
    if "-x-" in code:
        # BCP-47 tags are case-insensitive, and langcodes never sees a
        # private-use tag, so fold the case here; otherwise
        # ``ar-sa-x-najd`` misses ``ar-SA-x-najd`` and the distance match
        # below lands it on a sibling lect.
        folded = code.lower()
        for known in _ALIASES:
            if known.lower() == folded:
                return _ALIASES[known], "exact"
        for known in available:
            if known.lower() == folded:
                return known, "exact"
    if code in _BARE_DEFAULTS:
        return _BARE_DEFAULTS[code], "exact"
    if code in _REGION_DEFAULTS:
        return _REGION_DEFAULTS[code], "exact"
    match = closest_lang(code, available)
    if not match:
        return code, "unresolved"
    if "-x-" in requested or requested.startswith("x-"):
        # The request named a lect. Nothing above answered it, so whatever
        # the distance match found is a different lect or its parent.
        return match, "unknown-variant"
    if _declares_iso(match, requested):
        # The matched spec names this ISO 639-3 code as its own
        # (``ar-TN`` declares ``aeb``, ``tl`` declares ``tgl``). That is the
        # spec's own claim about what language it describes, so reaching it by
        # that code is as deliberate as an alias, whatever the distance
        # metric had to do to find it.
        return match, "exact"
    # Compare against the requested primary subtag AND the standardized one.
    # ``standardize_tag(macro=True)`` folds a member language into its
    # macrolanguage (``bcl`` -> ``bik``), so the match that comes back to a
    # registered member is the same language by the caller's own spelling and
    # is not a cross-language guess.
    primaries = {requested.split("-")[0].lower(), code.split("-")[0].lower()}
    if match.split("-")[0].lower() not in primaries:
        return match, "cross-language"
    _LOG.debug("resolved language code %r to nearest registered %r",
               requested, match)
    return match, "region"


def _resolve_code(code: str, *, allow_nearest: bool = True) -> str:
    """Normalise common aliases to canonical BCP-47 codes.

    Thin wrapper over :func:`_resolve_detail`, kept because the engine's
    internal call sites want the code and not the kind. *allow_nearest*
    ``False`` refuses every guessing kind, so an unresolved or guessed code
    comes back unchanged.
    """
    resolved, kind = _resolve_detail(code)
    if kind in ("exact", "unresolved"):
        return resolved
    if not allow_nearest:
        return code
    return resolved


def resolves_exactly(code: str) -> bool:
    """True when *code* names a spec without nearest-language guessing.

    Alias tables, case folding, BCP-47 standardization and the curated bare-tag
    defaults all name a spec deliberately; ``closest_lang`` guesses. This
    separates the two, so a caller can tell "this code is registered" from
    "something vaguely like it is".
    """
    return _resolve_code(code, allow_nearest=False) in available_json_codes()


_GUESS_KINDS = ("unknown-variant", "cross-language")


def _checked(code: str, *, fallback: bool) -> Tuple[str, bool]:
    """Resolve *code*, refusing a guess unless *fallback*.

    Returns ``(resolved, substituted)``. ``substituted`` is True only when a
    guess was accepted, so a caller that opted in can say so.

    Decision ``o2i-resolver-fallback``, 2026-09-25: refuse by default, with
    ``fallback=True`` as the opt-in, and expose the substitution when a caller
    opts in.
    """
    resolved, kind = _resolve_detail(code)
    if kind in _GUESS_KINDS:
        if not fallback:
            raise UnknownLanguageVariantError(code, resolved, kind)
        return resolved, True
    return resolved, False


def resolve(code: str, fallback: bool = False) -> str:
    """Return the registered spec code that *code* resolves to.

    Applies the same normalisation as :func:`get` — alias tables, BCP-47
    standardization, curated bare-tag defaults and region matching within one
    language — without loading the spec. A code with no usable resolution is
    returned unchanged (so :func:`get` raises ``KeyError`` for it).

    Args:
        code: the requested BCP-47 or ISO 639-3 code.
        fallback: accept a guess. Without it, a private-use ``-x-`` variant
            this registry does not carry raises
            :class:`~orthography2ipa.exceptions.UnknownLanguageVariantError`
            rather than answering with a sibling lect.
    """
    return _checked(code, fallback=fallback)[0]


def get(code: str, strict: bool = False, fallback: bool = False) -> LanguageSpec:
    """Return the :class:`LanguageSpec` for *code*, loading lazily.

    Args:
        code: BCP-47 language code (e.g. ``'en'``, ``'pt-BR'``) or
              ISO 639-3 three-letter code (e.g. ``'eng'``, ``'por'``).
        strict: kept for the callers written before the default changed. It
            asked for what is now the default, so it is accepted and changes
            nothing.
        fallback: accept a substitution this registry would otherwise refuse.

    A private-use ``-x-`` subtag claims a named lect exists. Before
    ``ar-BH-x-baharna`` had a spec, ``get`` answered it with a 261-grapheme
    table and plausible Arabic output — the Bahraini Sunni one — with nothing
    in the result saying a substitution had happened, and a reviewer read a
    complete, confident baseline column from the wrong spec. So that answer is
    now refused unless the caller asks for it (decision
    ``o2i-resolver-fallback``, 2026-09-25).

    Region matching inside one language is NOT refused: ``ar-ZZ`` → ``ar`` and
    ``en-NZ`` → ``en-GB`` are ordinary BCP-47 matching, and a caller can want
    them.

    Raises:
        KeyError: if the language is not registered at all.
        ~orthography2ipa.exceptions.UnknownLanguageVariantError: a
            ``KeyError`` subclass — if the code resolves only by guessing a
            variant or a different language and *fallback* is not set.
    """
    code = _checked(code, fallback=fallback)[0]
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

    A bundled plugin's own optional third-party dependency being absent is the
    normal case for an ordinary install (see :mod:`orthography2ipa.syllabifiers`)
    — it is logged at DEBUG, naming the extra that would enable it. Anything
    else that goes wrong loading or instantiating a plugin is a real problem
    and is logged at WARNING.
    """
    plugins: Dict[str, "SyllabifierPlugin"] = {}
    eps = entry_points(group="orthography2ipa.syllabify")
    for ep in eps:
        try:
            cls = ep.load()
        except Exception as exc:
            _LOG.warning(
                "failed to load syllabifier plugin %r: %s", ep.name, exc)
            continue
        try:
            instance = cls()
        except ModuleNotFoundError as exc:
            _LOG.debug(
                "syllabifier plugin %r is disabled: its optional dependency is "
                "not installed (%s). Install the matching extra to enable it.",
                ep.name, exc)
            continue
        except Exception as exc:
            _LOG.warning(
                "failed to load syllabifier plugin %r: %s", ep.name, exc)
            continue
        for code in instance.language_codes:
            incumbent = plugins.get(code)
            if incumbent is None or instance.priority > incumbent.priority:
                plugins[code] = instance
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
    plugins: Dict[str, List["RescorerPlugin"]] = {}
    for ep in entry_points(group="orthography2ipa.rescore"):
        try:
            instance = ep.load()()
            for code in instance.language_codes:
                plugins.setdefault(code, []).append(instance)
        except Exception as exc:
            _LOG.warning(
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
    plugins: Dict[str, "StressPlugin"] = {}
    for ep in entry_points(group="orthography2ipa.stress"):
        try:
            instance = ep.load()()
            for code in instance.language_codes:
                incumbent = plugins.get(code)
                if incumbent is None or instance.priority > incumbent.priority:
                    plugins[code] = instance
        except Exception as exc:
            _LOG.warning(
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
    from orthography2ipa.plugins import ENTRY_POINT_GROUPS

    found: Dict[str, object] = {}
    for ep in entry_points(group=ENTRY_POINT_GROUPS[stage]):
        try:
            found[ep.name] = ep.load()()
        except Exception as exc:
            _LOG.warning(
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
