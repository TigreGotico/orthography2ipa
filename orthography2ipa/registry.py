"""Language registry with lazy loading and plugin discovery."""
from __future__ import annotations

import logging
import re
import warnings
from functools import lru_cache
from importlib.metadata import entry_points
from typing import TYPE_CHECKING, Dict, List, Optional

from linguatag import closest_lang, with_default_region

from orthography2ipa.json_loader import available_json_codes, load_json_spec
from orthography2ipa.types import LanguageSpec

if TYPE_CHECKING:
    from orthography2ipa.syllabifier_plugin import SyllabifierPlugin

_cache: Dict[str, LanguageSpec] = {}

_LOG = logging.getLogger(__name__)


#: The private-use singleton, which BCP 47 matches case-insensitively.
_PRIVATE_USE = re.compile("-x-", re.IGNORECASE)


class UnknownVariantWarning(UserWarning):
    """A private-use (``-x-``) subtag names no registered spec.

    The tag resolves to the nearest registered spec instead, which is a
    different variety than the one asked for.
    """


def _warn_unknown_variant(code: str, resolved: str, stacklevel: int) -> None:
    parts = _PRIVATE_USE.split(code, maxsplit=1)
    if (len(parts) == 1 or resolved not in available_json_codes()
            or resolves_exactly(code)):
        return
    discarded = parts[1]
    warnings.warn(
        f"unknown variant subtag {discarded!r} in {code!r}; "
        f"using {resolved!r} instead",
        UnknownVariantWarning,
        stacklevel=stacklevel,
    )


# Fallback alias table for ISO 639-3 → BCP-47 normalisation.
# When ``langcodes`` is available, standard codes are resolved via that library.
# Private-use subtags (e.g. ``ast-PT-x-rionor``) always use this table.
_ALIASES: Dict[str, str] = {
    "por": "pt-PT", "eng": "en-GB", "spa": "es-ES", "fra": "fr-FR", "deu": "de-DE",
    "ita": "it-IT", "nld": "nl", "swe": "sv", "dan": "da", "nor": "no",
    "rus": "ru", "ukr": "uk", "ara": "ar", "fas": "fa", "hin": "hi",
    "zho": "zh", "jpn": "ja", "kor": "ko", "eus": "eu", "cat": "ca",
    "glg": "gl-ES", "oci": "oc", "tur": "tr", "fin": "fi", "ell": "el",
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
    # Arabic spoken dialects are keyed by their ISO 639-3 individual code
    # (SCHEMA.md, "Minting a private-use lect code"). A bare code resolves to
    # the spec of that code; ``afb`` and ``apc`` name the abstract Gulf and
    # Levantine nodes, which carry the bare code as their own key.
    "arz": "arz-EG",          # Egyptian Arabic
    "aec": "aec-EG",          # Saʿīdi (Upper Egyptian) Arabic
    "avl": "avl-EG",          # Eastern Egyptian Bedawi Arabic
    "ary": "ary-MA",          # Moroccan Arabic (Darija)
    "arq": "arq-DZ",          # Algerian Arabic
    "aeb": "aeb-TN",          # Tunisian Arabic
    "mey": "mey-MR",          # Hassaniyya
    "apd": "apd-SD",          # Sudanese Arabic
    "shu": "shu-TD",          # Chadian Arabic (shu-NG is its child)
    "acx": "acx-OM",          # Omani Arabic
    "adf": "adf-OM",          # Dhofari Arabic
    "ayn": "ayn-YE",          # Sanaani Arabic
    "acm": "acm-IQ",          # Mesopotamian Arabic (gilit; Glottolog meso1252)
    "abv": "abv-BH",          # Bahārna Arabic (B dialects of Bahrain)
    "ars": "ars-SA",          # Najdi Arabic
    "acw": "acw-SA",          # Hijazi Arabic
    # SIL retired ``ajp`` (South Levantine Arabic) into ``apc``.
    "ajp": "apc-JO",
    # Other varieties keyed by their ISO 639-3 individual code. A bare code
    # resolves to the spec of that code.
    "haz": "haz-AF",          # Hazaragi
    "bar": "bar-AT",          # Bavarian
    # langcodes folds ``pnb`` into its macrolanguage ``lah``, a spec with no
    # graphemes, so the bare code is pinned.
    "pnb": "pnb-PK",          # Western Panjabi (Shahmukhi)
    "ajg": "ajg-BJ",          # Aja (Benin)
    "gej": "gej-TG",          # Gen (Mina)
    "cbk": "cbk-PH",          # Chavacano (Zamboangueño)
    # langcodes folds ``twi`` into its macrolanguage ``ak``; ``tw`` is the spec
    # that declares the code.
    "twi": "tw",              # Twi
    # Codes with exactly one declaring spec, whose name is the same language as
    # the code's, and no file of their own to shadow them.
    "xdc": "xda",             # Dacian/Thracian
    # Dialects named in a private-use subtag. langcodes ignores private-use
    # content when it measures tag distance, so ``ar-x-najdi`` would otherwise
    # fall to the nearest bare match (``ar``); pin the spoken adjective to the
    # spec it names.
    "ar-x-najdi": "ars-SA",       # Najdi Arabic
    "ar-x-hejazi": "acw-SA",      # Hejazi Arabic
    "ar-x-hijazi": "acw-SA",      # Hejazi Arabic (alternate romanization)
    # Barranquenho is keyed ``ext-PT-x-barranco``: a language of its own spoken
    # in Portugal, not a Portuguese dialect. ``pt-PT-x-barrancos`` is a retired
    # spelling of the same lect; without the alias ``closest_lang`` resolves it
    # to ``pt-AO`` and returns Angolan Portuguese.
    "pt-PT-x-barrancos": "ext-PT-x-barranco",
    # Spellings the downstream Portuguese front-end uses for three lects
    # whose spec keys are shorter; without these the tags fall to the bare
    # region and lose the lect.
    "pt-BR-x-sao-paulo": "pt-BR-x-sp",
    "pt-BR-x-rio-janeiro": "pt-BR-x-rj",
    # Brasília speech shows no feature that separates it from the pt-BR base
    # in the opened sources (alveolar coda /S/, 97 %: Hora 1999: 35), so the
    # code reads the base.
    "pt-BR-x-brasilia": "pt-BR",
    "pt-PT-x-lisboa": "pt-PT-x-lisbon",
    # Galician has one standard spec, ``gl-ES``, and its varieties carry the
    # region. These are the retired codes of the same varieties.
    "gl-x-central": "gl-ES-x-central",
    "gl-x-occidental": "gl-ES-x-occident",
    "gl-x-oriental": "gl-ES-x-oriental",
    "gl-x-eonavia": "gl-ES-x-eonavia",
    "gl-x-reintegrado": "gl-ES-x-reintegr",
    # The Cantonese spec reads Han text in either script. A bare ``yue`` is
    # mainland Cantonese in Simplified script, so the Hong Kong, Macau and
    # Traditional tags are too far from it to match without these.
    "yue-HK": "yue",
    "yue-MO": "yue",
    "yue-Hant": "yue",
}

#: The keys a spec had before it took its canonical key, mapped to that key.
#: Each is an exact alias. The nearest-match step still measures a tag against
#: the old key, so a tag that adds an unknown subtag to it (``ar-MA-x-fes``)
#: lands on the same spec as before the rename. An old key that is the ISO
#: 639-3 code of another language is not kept: ``aja``, the old key of
#: ``ajg-BJ``, is the code of Aja (South Sudan). For the same reason ``tmg``
#: (Ternateño, the extinct creole of the Moluccas) does not name the Cavite
#: spec ``cbk-PH-x-ternate``.
_RENAMED: Dict[str, str] = {
    "ar-EG":                "arz-EG",
    "ar-EG-x-fayyum":       "arz-EG-x-fayyum",
    "ar-EG-x-saidi":        "aec-EG",
    "ar-EG-x-bedawi":       "avl-EG",
    "ar-MA":                "ary-MA",
    "ar-DZ":                "arq-DZ",
    "ar-TN":                "aeb-TN",
    "ar-MR":                "mey-MR",
    "ar-SD":                "apd-SD",
    "ar-TD":                "shu-TD",
    "ar-NG":                "shu-NG",
    "ar-OM":                "acx-OM",
    "ar-OM-x-dhofari":      "adf-OM",
    "ar-YE":                "ayn-YE",
    "ar-YE-x-highland":     "ayn-YE-x-highland",
    "ar-YE-x-manakha":      "ayn-YE-x-manakha",
    "ar-IQ":                "acm-IQ",
    "ar-SY":                "apc-SY",
    "ar-TR-x-cukurova":     "apc-TR-x-cukurova",
    "ar-LB":                "apc-LB",
    "ar-JO":                "apc-JO",
    "ar-PS":                "apc-PS",
    "ar-x-levantine":       "apc",
    "ar-x-gulf":            "afb",
    "ar-SA-x-sharqiyya":    "afb-SA-x-sharqiya",
    "ar-SA-x-dawasir":      "afb-SA-x-dawasir",
    "ar-KW":                "afb-KW",
    "ar-QA":                "afb-QA",
    "ar-AE":                "afb-AE",
    "ar-BH":                "afb-BH",
    "ar-BH-x-baharna":      "abv-BH",
    "ar-SA-x-najd":         "ars-SA",
    "ar-SA-x-qassim":       "ars-SA-x-qassim",
    "ar-SA-x-shamali":      "ars-SA-x-shamali",
    "ar-SA-x-hejaz":        "acw-SA",
    "fa-x-hazaragi":        "haz-AF",
    "de-x-bavarian":        "bar-AT",
    "pa-PK":                "pnb-PK",
    "sa-x-vedic":           "vsn",
    "tpw":                  "tpn",
    "gen":                  "gej-TG",
    "cbk-zam":              "cbk-PH",
    "cbk-x-cavite":         "cbk-PH-x-cavite",
    "cbk-x-ternate":        "cbk-PH-x-ternate",
    # Keys that were not well-formed BCP 47 (RFC 5646 section 2.1): a private-use
    # subtag longer than 8 characters, or a subtag after the script that is
    # neither a region nor a variant.
    "an-x-benasques":       "an-x-benasque",
    "an-x-chistabin":       "an-x-chistau",
    "an-x-occidental":      "an-x-occident",
    "ar-Latn-buckwalter":   "ar-Latn-x-buckwalt",
    "ar-x-peninsular":      "ar-x-peninsul",
    "ast-PT-x-guadramil":   "ast-PT-x-guadrami",
    "ast-x-cantabrian":     "ast-x-cantabri",
    "ast-x-occidental":     "ast-x-occident",
    "ca-x-occidental":      "ca-x-occident",
    "cdo-Latn-buc":         "cdo-Latn-x-buc",
    "cel-x-gallaecia":      "cel-x-gallaeci",
    "da-x-copenhagen":      "da-x-copenhag",
    "de-x-alemannic":       "de-x-alemanni",
    "es-AR-x-patagonia":    "es-AR-x-patagoni",
    "es-CO-x-santander":    "es-CO-x-santande",
    "es-ES-x-andalusia-e":  "es-ES-x-andalusi-e",
    "es-ES-x-andalusia-w":  "es-ES-x-andalusi-w",
    "es-ES-x-cantabria":    "es-ES-x-cantabri",
    "es-ES-x-extremadura":  "es-ES-x-extremad",
    "es-PE-x-amazonico":    "es-PE-x-amazonia",
    "es-VE-x-maracucho":    "es-VE-x-zulia",
    "eu-x-bizkaiera":       "eu-biscayan",
    "eu-x-erronkariera":    "eu-x-roncal",
    "eu-x-gipuzkera":       "eu-x-gipuzkoa",
    "eu-x-lapurtera":       "eu-x-lapurdi",
    "ext-PT-x-barrancos":   "ext-PT-x-barranco",
    "fa-x-khorasani":       "fa-x-khorasan",
    "gem-x-ingvaeonic":     "gem-x-ingvaeon",
    "gem-x-northwest":      "gem-x-north-west",
    "gl-ES-x-occidental":   "gl-ES-x-occident",
    "gl-ES-x-reintegrado":  "gl-ES-x-reintegr",
    "hak-Latn-phak-fa-su":  "hak-Latn-x-phak-fa-su",
    "la-x-galloitalic":     "la-x-gallo-italic",
    "nan-Latn-poj":         "nan-Latn-pehoeji",
    "oc-x-provencau":       "oc-provenc",
    "pt-BR-x-fluminense":   "pt-BR-x-fluminen",
    "pt-PT-x-trasosmontes": "pt-PT-x-tras-os-montes",
    "roa-x-galaicopt":      "roa-x-galaico-pt",
    "ru-x-arkhangelsk":     "ru-x-arkhange",
    "sc-x-campidanese":     "sc-x-campidan",
    "sc-x-logudorese":      "sc-x-logudoro",
    "sv-x-rikssvenska":     "sv-x-rikssven",
    "ta-x-proto-dravidian": "ta-x-proto-dravidia",
    # SIL retired ``bbz`` as non-existent and names no replacement, so Babalia
    # Creole Arabic takes a private-use key. ``bbz`` is no other language's code.
    "bbz":                  "ar-TD-x-babalia",
}
_ALIASES.update(_RENAMED)

# Default variety for a region tag whose specs are all sub-regional, so a bare
# region has no exact spec and langcodes' nearest match would pick whichever
# private-use sibling sorts first. This is an explicit editorial convention,
# not a claim in the spec data: Saudi Arabia has several documented varieties
# (Najdi, Hejazi, ...) and no single standard spoken form, so ``ar-SA`` is
# steered to Najdi — the variety of the capital region (Riyadh) and the most
# widely spoken (Ingham, Najdi Arabic, 1994) — rather than asserting that
# Saudi Arabic *is* Najdi anywhere in the data.
_REGION_DEFAULTS: Dict[str, str] = {
    "ar-SA": "ars-SA",
}

try:
    import langcodes as _langcodes
    _HAS_LANGCODES = True
except ImportError:
    _HAS_LANGCODES = False


@lru_cache(maxsize=None)
def _resolve_code(code: str, *, allow_nearest: bool = True) -> str:
    """Normalise common aliases to canonical BCP-47 codes.

    Resolution order:
    1. Manual alias table (handles private-use subtags and ISO 639-3 codes
       that ``langcodes`` may not round-trip cleanly).
    2. Exact match against the registered spec codes, then
       ``langcodes.standardize_tag()`` when the library is available and the
       code is not a private-use subtag (``x-`` extension).
    3. Exact match of the standardized code.
    4. The default region of a bare primary-language tag, when that
       spec is registered (``pt`` → ``pt-PT``), or the curated default
       variant of a region tag with only sub-regional specs
       (``ar-SA`` → ``ars-SA``).
    5. Nearest registered code by language distance
       (``en-NZ`` → ``en-GB``); no usable match leaves *code* unchanged.
    """
    if code in _ALIASES:
        return _ALIASES[code]
    available = available_json_codes()
    # A registered code names its own spec. ``macro=True`` below folds an
    # individual language into its macrolanguage (``tl`` → ``fil``,
    # ``bcl`` → ``bik``), which would miss the spec.
    if code in available:
        return code
    if (_HAS_LANGCODES and not _PRIVATE_USE.search(code)
            and not code.startswith("x-")):
        try:
            code = _langcodes.standardize_tag(code, macro=True)
        except Exception:
            pass
        if code in _ALIASES:
            return _ALIASES[code]
    if code in available:
        return code
    if _PRIVATE_USE.search(code):
        # BCP-47 tags are case-insensitive, and langcodes never sees a
        # private-use tag (step 2), so fold the case here; otherwise
        # ``ar-sa-x-najd`` misses ``ar-SA-x-najd`` and the distance match
        # below lands it on a sibling lect.
        folded = code.lower()
        for known in _ALIASES:
            if known.lower() == folded:
                return _ALIASES[known]
        for known in available:
            if known.lower() == folded:
                return known
    # A bare tag names its motherland variety, not the most-populous region
    # langcodes would pick: ``pt`` is ``pt-PT``, not ``pt-BR``.
    if "-" not in code and (default := with_default_region(code)) in available:
        return default
    if code in _REGION_DEFAULTS:
        return _REGION_DEFAULTS[code]
    if not allow_nearest:
        return code
    # An unknown variant falls back to the standard variety, not to whichever
    # sibling lect ties with it: private use counts for nothing in the distance.
    match = closest_lang(code, sorted({*available, *_RENAMED}), lects="standard")
    if match:
        match = _RENAMED.get(match, match)
        _LOG.debug("resolved language code %r to nearest registered %r",
                   code, match)
        return match
    return code


def resolves_exactly(code: str) -> bool:
    """True when *code* names a spec without nearest-language guessing.

    Alias tables, case folding, BCP-47 standardization and the default region
    of a bare tag all name a spec deliberately; ``closest_lang`` guesses. This
    separates the two, so a caller can tell "this code is registered" from
    "something vaguely like it is".
    """
    return _resolve_code(code, allow_nearest=False) in available_json_codes()


def resolve(code: str) -> str:
    """Return the registered spec code that *code* resolves to.

    Applies the same normalisation as :func:`get` — alias tables,
    BCP-47 standardization, the default region of a bare tag and
    nearest-language matching — without loading the spec. A code with
    no usable resolution is returned unchanged (so :func:`get` raises
    ``KeyError`` for it). A private-use (``-x-``) tag that names no spec
    resolves to the nearest one and emits :class:`UnknownVariantWarning`.
    """
    resolved = _resolve_code(code)
    _warn_unknown_variant(code, resolved, stacklevel=3)
    return resolved


def get(code: str, strict: bool = False) -> LanguageSpec:
    """Return the :class:`LanguageSpec` for *code*, loading lazily.

    Args:
        code: BCP-47 language code (e.g. ``'en'``, ``'pt-BR'``) or
              ISO 639-3 three-letter code (e.g. ``'eng'``, ``'por'``).
        strict: refuse nearest-language guessing. Aliases, case folding,
            BCP-47 standardization and the default region of a bare tag
            still apply — those name a spec deliberately. What is refused is
            ``closest_lang``, which answers an unregistered code with the
            nearest thing it can find.

    The default is the guess, because callers depend on it. It is worth knowing
    what it costs: before ``ar-BH-x-baharna`` had a spec, ``get`` answered it with
    a 261-grapheme table and plausible Arabic output — the Bahraini Sunni one —
    with nothing in the result saying a substitution had happened. A reviewer
    reading a baseline that way got a complete, confident column from the wrong
    spec. ``strict=True`` is for any caller that would rather be told.

    Raises:
        KeyError: If the language is not registered, or — under *strict* — if it
            resolves only by nearest-language guessing.
    """
    requested = code
    code = _resolve_code(code, allow_nearest=not strict)
    if not strict:
        _warn_unknown_variant(requested, code, stacklevel=3)
    if code not in _cache:
        _cache[code] = load_json_spec(code)
    return _cache[code]


def available_codes(include_clades: bool = False) -> List[str]:
    """Return all registered language codes.

    Classification-only clade nodes (``Romance``, ``West Germanic``) are not
    languages — they carry no phonology and cannot be transcribed — so they
    are excluded unless *include_clades* is set.
    """
    return list(_available_codes(include_clades))


# The spec index is built once at import, so the filtered list never changes.
@lru_cache(maxsize=None)
def _available_codes(include_clades: bool) -> tuple:
    codes = sorted(available_json_codes())
    if include_clades:
        return tuple(codes)
    keep: List[str] = []
    for code in codes:
        try:
            if not get(code).clade:
                keep.append(code)
        except (KeyError, ValueError, ModuleNotFoundError):
            keep.append(code)
    return tuple(keep)


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
