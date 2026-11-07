"""Optional per-language IPA lexicon overlay.

A **lexicon** is a ``word<TAB>ipa`` TSV — one pair per line, UTF-8,
NFC-normalised, first-entry-wins. It is the unblocker for deep-orthography
languages (English, Danish, Irish) whose rule systems cannot reach production
accuracy from grapheme rules alone.

**Nothing is bundled.** A lexicon is a word list, not a description of a
language, so it is not this library's payload — shipping one would bloat the
wheel and freeze a corpus into a release. The caller supplies it, from a local
file, a URL, or a Hugging Face dataset id, and gives it to one engine::

    from orthography2ipa import G2P, Pipeline, load_lexicon

    lexicon = load_lexicon("/data/en-GB.tsv")                    # local file
    lexicon = load_lexicon("https://example.org/en.tsv")         # URL
    lexicon = load_lexicon("hf://TigreGotico/en-lexicon/en-GB.tsv")
    engine = G2P("en-GB", pipeline=Pipeline(lexicon=lexicon))

Remote sources are fetched on the first read and cached under
``$XDG_CACHE_HOME/orthography2ipa``. An engine with no lexicon takes the rules,
exactly as if this module did not exist.

A package can also supply default lexicons, such as ``o2i-lexicons``
(``pip install orthography2ipa[lexicons]``). Installing it changes nothing: the
caller reads a lexicon in code and gives it to the engine that wants it::

    from orthography2ipa import G2P, Pipeline, packaged_lexicon

    engine = G2P("en-GB", pipeline=Pipeline(lexicon=packaged_lexicon("en-GB")))

Such a package declares one entry point per language code in the group
``orthography2ipa.lexicons``. The entry point loads a callable that takes the
code and returns the path of a local ``word<TAB>ipa`` file::

    [project.entry-points."orthography2ipa.lexicons"]
    "en-GB" = "o2i_lexicons:tsv_path"

Design contract
---------------

- **Per engine.** :func:`load_lexicon` and :func:`packaged_lexicon` return a
  mapping and set no state. The engine that holds the mapping uses it, and
  another engine in the process does not see it.
- **Never implicit.** No lexicon is consulted unless the caller named one.
  Installing a provider package only makes its lexicons discoverable
  (:func:`packaged_lexicon_sources`): the transcription is a function of the
  spec, the input and the caller's explicit configuration, never of the
  environment. The library does not download anything on its own, and a
  provider returns a local file.
- **Same pathway as ``word_exceptions``.** :class:`~orthography2ipa.g2p.G2P`
  folds a lexicon hit into the *exact* override path that
  ``spec.word_exceptions`` uses — so a lexicon entry still routes through
  stress-mark insertion and cross-word sandhi, and is reported with the same
  ``confidence == 1.0`` (a certain answer).
- **Precedence.** inline ``spec.word_exceptions`` > the engine's lexicon >
  rules. An inline exception always wins over the sidecar; the sidecar always
  wins over the grapheme/positional beam.
- **Discovery is lazy.** The ``orthography2ipa.lexicons`` entry points are read
  only by :func:`packaged_lexicon`, :func:`packaged_lexicon_sources` and
  :func:`use_packaged_lexicons`, once per process, never at import and never
  during transcription.

Deprecated process-wide API
---------------------------

:func:`register_lexicon`, :func:`set_lexicon_dir`,
``$ORTHOGRAPHY2IPA_LEXICON_DIR``, :func:`use_packaged_lexicons`,
:func:`clear_lexicons` and :func:`get_lexicon` act on the whole process: every
engine that has no :attr:`~orthography2ipa.pipeline.Pipeline.lexicon` reads
them. They keep working for one stable cycle and warn with the release that
removes them. Their precedence is :func:`register_lexicon`, then
:func:`set_lexicon_dir`, then an enabled packaged lexicon. A process-wide
lexicon is read once per code, on first use, and cached for the process
lifetime.

``scripts/build_en_lexicon.py`` builds a CMUdict-derived ``en-GB.tsv`` you can
load; see ``docs/guide/lexicon.md``.
"""
from __future__ import annotations

import logging
import os
import unicodedata
import urllib.request
import warnings
from functools import lru_cache
from importlib.metadata import EntryPoint, entry_points
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple, Union

from orthography2ipa.registry import resolve, resolves_exactly
from orthography2ipa.version import VERSION_MAJOR

_LOG = logging.getLogger(__name__)

__all__ = [
    "get_lexicon",
    "register_lexicon",
    "clear_lexicons",
    "set_lexicon_dir",
    "resolve_lexicon_source",
    "available_lexicon_codes",
    "use_packaged_lexicons",
    "load_lexicon",
    "packaged_lexicon",
    "packaged_lexicon_sources",
    "lexicon_path",
    "parse_lexicon_text",
    "validate_lexicon_text",
    "is_ipa_string",
]

#: Env var naming a directory of ``{code}.tsv`` lexicons.
LEXICON_DIR_ENV = "ORTHOGRAPHY2IPA_LEXICON_DIR"

#: Entry-point group through which an installed package supplies default
#: lexicons, one entry point per language code.
ENTRY_POINT_GROUP = "orthography2ipa.lexicons"

#: The release that removes the process-wide lexicon API.
_REMOVAL_VERSION = f"{VERSION_MAJOR + 1}.0.0"

#: Where fetched remote lexicons are cached.
CACHE_DIR = Path(
    os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")
) / "orthography2ipa" / "lexicons"

# resolved code -> source (path, URL or hf:// id), set by register_lexicon()
_REGISTERED: Dict[str, str] = {}
_LEXICON_DIR: Optional[Path] = None
# resolved code -> provider entry point; None until the first discovery
_PACKAGED: Optional[Dict[str, EntryPoint]] = None
# resolved codes whose packaged lexicon the caller enabled
_ENABLED: Set[str] = set()

# Non-letter IPA symbols allowed in a transcription: length/stress/tone marks,
# spacing modifiers (aspiration, palatalisation …), tie bars and the affricate
# ties, plus combining diacritics (voiceless ring, dental bridge, no-audible-
# release …). Base *letters* are validated separately by Unicode category.
_IPA_MODIFIERS = frozenset(
    "ːˑ"          # length
    "ˈˌ"          # primary / secondary stress
    "ʰʷʲˠˤʼⁿ"     # release / secondary-articulation / ejective / nasal-release
    "‿͜͡"          # linking / tie bars
    ".|‖"         # syllable / prosodic boundaries (tolerated, not required)
    "˥˦˧˨˩"        # tone letters
)


def _warn_deprecated(name: str, replacement: str) -> None:
    warnings.warn(
        f"{name} is deprecated and will be removed in {_REMOVAL_VERSION}; "
        f"use {replacement}.",
        DeprecationWarning,
        stacklevel=3,
    )


def _is_ipa_char(ch: str) -> bool:
    if ch in _IPA_MODIFIERS:
        return True
    cat = unicodedata.category(ch)
    # Combining marks (IPA diacritics) and letters (Latin + IPA Extensions,
    # e.g. ɡ ʃ ð ŋ ɐ ɹ ʊ) are the phonetic-symbol classes.
    if cat.startswith("M") or cat.startswith("L"):
        return True
    return False


def is_ipa_string(ipa: str) -> bool:
    """Return ``True`` when *ipa* is NFC and contains only IPA characters.

    "IPA characters" = phonetic letters (Latin + IPA-Extensions letters),
    combining diacritics, and the length/stress/tie/tone modifiers used in
    broad and narrow transcription. Whitespace, digits and ASCII punctuation
    (other than the tolerated prosodic boundaries) are rejected. An empty
    string is not a valid transcription.
    """
    if not ipa:
        return False
    if unicodedata.normalize("NFC", ipa) != ipa:
        return False
    return all(_is_ipa_char(ch) for ch in ipa)


def register_lexicon(code: str, source: str) -> None:
    """Deprecated: register the lexicon *source* to use for language *code*.

    Every engine with no lexicon of its own reads the registration. Use
    ``G2P(code, pipeline=Pipeline(lexicon=load_lexicon(source)))``.

    *source* is a local path, an ``http(s)://`` URL, or a Hugging Face id
    (``hf://<repo_id>/<path>``, optionally ``@<revision>``). Nothing is read
    or fetched here — resolution is lazy, on first transcription for *code*.

    *code* is whatever tag the caller transcribes with (``en``, ``en-GB``): it
    is resolved to the spec that :func:`~orthography2ipa.get` answers it with,
    and the lexicon belongs to that spec. Two tags that resolve to the same
    spec share one slot; the later registration replaces the earlier.
    """
    _warn_deprecated("register_lexicon", "Pipeline(lexicon=load_lexicon(source))")
    _REGISTERED[resolve(code)] = source
    _process_lexicon.cache_clear()


def set_lexicon_dir(path) -> None:
    """Deprecated: use *path* as a directory of ``{code}.tsv`` lexicons (``None`` to unset).

    Every engine with no lexicon of its own reads the directory. Use
    ``Pipeline(lexicon=load_lexicon(path))`` with the one file the engine needs.

    A lexicon registered with :func:`register_lexicon` still wins for its code.
    A file belongs to the spec its name resolves to, so ``en.tsv`` serves
    ``en-GB``; a file named exactly for the resolved code wins over the others.
    """
    _warn_deprecated("set_lexicon_dir", "Pipeline(lexicon=load_lexicon(path))")
    global _LEXICON_DIR
    _LEXICON_DIR = Path(path).expanduser() if path is not None else None
    _process_lexicon.cache_clear()


def clear_lexicons() -> None:
    """Deprecated: forget every registered lexicon, the lexicon dir and the enabled packaged lexicons.

    An engine's :attr:`~orthography2ipa.pipeline.Pipeline.lexicon` needs no
    clearing: it ends with the engine.
    """
    _warn_deprecated("clear_lexicons", "Pipeline(lexicon=...), which needs no clearing")
    global _LEXICON_DIR, _PACKAGED
    _REGISTERED.clear()
    _LEXICON_DIR = None
    _PACKAGED = None
    _ENABLED.clear()
    _process_lexicon.cache_clear()


def use_packaged_lexicons(codes: Optional[Iterable[str]] = None) -> List[str]:
    """Deprecated: enable the installed packaged lexicons for *codes*, or for all of them.

    Every engine with no lexicon of its own reads an enabled lexicon, so this
    changes the output of engines the caller did not name. Use
    ``G2P(code, pipeline=Pipeline(lexicon=packaged_lexicon(code)))``.

    A packaged lexicon comes from an installed package that declares an entry
    point in the ``orthography2ipa.lexicons`` group. It ranks below
    :func:`register_lexicon` and :func:`set_lexicon_dir`, and above the rules.
    :func:`clear_lexicons` disables it again. Returns the enabled codes.

    Raises
    ------
    LookupError
        A code in *codes* has no installed provider. Asking for a lexicon that
        is absent is an error, never a quiet fall back to the rules.
    """
    _warn_deprecated("use_packaged_lexicons", "Pipeline(lexicon=packaged_lexicon(code))")
    providers = _packaged_providers()
    if codes is None:
        wanted = set(providers)
    else:
        wanted = {resolve(code) for code in codes}
        missing = sorted(wanted - set(providers))
        if missing:
            raise LookupError(
                f"no installed package provides a lexicon for {missing}; "
                f"installed: {sorted(providers) or 'nothing'}")
    _ENABLED.update(wanted)
    _process_lexicon.cache_clear()
    return sorted(_ENABLED)


def load_lexicon(source: Union[str, os.PathLike]) -> Dict[str, str]:
    """Read the lexicon at *source* into a ``{word: ipa}`` mapping.

    *source* is a local path, an ``http(s)://`` URL, or a Hugging Face id
    (``hf://<repo_id>/<path>``, optionally ``@<revision>``). The mapping is the
    caller's to give to :class:`~orthography2ipa.pipeline.Pipeline`, and this
    call sets no state.

    Raises
    ------
    FileNotFoundError
        A local source that does not exist.
    """
    path = resolve_lexicon_source(os.fspath(source))
    return parse_lexicon_text(path.read_text(encoding="utf-8"))


def packaged_lexicon(code: str) -> Dict[str, str]:
    """The ``{word: ipa}`` mapping an installed package supplies for *code*.

    The mapping is the caller's to give to
    :class:`~orthography2ipa.pipeline.Pipeline`, and this call sets no state.

    Raises
    ------
    LookupError
        No installed package supplies a lexicon file for *code*. Asking for a
        lexicon that is absent is an error, never a quiet fall back to the
        rules.
    """
    resolved = resolve(code)
    path = _packaged_path(resolved)
    if path is None:
        raise LookupError(
            f"no installed package supplies a lexicon file for {resolved!r}; "
            f"installed: {sorted(_packaged_providers()) or 'nothing'}")
    return load_lexicon(path)


def packaged_lexicon_sources() -> Dict[str, Path]:
    """The installed packaged lexicons, as ``{resolved code: local file}``.

    This lists them and enables nothing. A provider that fails is left out and
    logged at WARNING.
    """
    found = {}
    for code in sorted(_packaged_providers()):
        path = _packaged_path(code)
        if path is not None:
            found[code] = path
    return found


def _packaged_providers() -> Dict[str, EntryPoint]:
    """The ``orthography2ipa.lexicons`` entry points, by resolved spec code.

    Read once per process. An entry point must name a registered spec exactly;
    one that only a nearest-language guess would place is skipped, so a
    provider never lands on a spec it did not name. When two providers serve
    one spec, the one named for the exact resolved code wins, then the first
    by distribution and entry-point name.
    """
    global _PACKAGED
    if _PACKAGED is not None:
        return _PACKAGED
    candidates = []
    for ep in entry_points(group=ENTRY_POINT_GROUP):
        if resolves_exactly(ep.name):
            candidates.append((resolve(ep.name), ep))
        else:
            _LOG.warning("lexicon provider %r names no registered spec; skipped",
                         ep.name)
    candidates.sort(key=lambda c: (c[1].name != c[0],
                                   c[1].dist.name if c[1].dist else "",
                                   c[1].name))
    found: Dict[str, EntryPoint] = {}
    for code, ep in candidates:
        if code in found:
            _LOG.warning("lexicon providers %r and %r both serve %r; using %r",
                         found[code].value, ep.value, code, found[code].value)
        else:
            found[code] = ep
    _PACKAGED = found
    return found


def _packaged_path(code: str) -> Optional[Path]:
    """The file a packaged provider supplies for resolved *code*, or ``None``."""
    ep = _packaged_providers().get(code)
    if ep is None:
        return None
    try:
        path = Path(ep.load()(ep.name))
    except Exception as exc:
        _LOG.warning("lexicon provider %r failed for %r: %s", ep.value, code, exc)
        return None
    if not path.is_file():
        _LOG.warning("lexicon provider %r returned %s, which is not a file",
                     ep.value, path)
        return None
    return path


def _lexicon_dir() -> Optional[Path]:
    if _LEXICON_DIR is not None:
        return _LEXICON_DIR
    env = os.environ.get(LEXICON_DIR_ENV)
    if not env:
        return None
    _warn_deprecated(f"${LEXICON_DIR_ENV}", "Pipeline(lexicon=load_lexicon(path))")
    return Path(env).expanduser()


def resolve_lexicon_source(source: str) -> Path:
    """Resolve a lexicon *source* to a local file, fetching it if remote.

    Local paths are returned as-is. ``http(s)://`` URLs and ``hf://`` ids are
    downloaded once into :data:`CACHE_DIR` and reused on later calls.

    Raises
    ------
    FileNotFoundError
        A local source that does not exist.
    """
    if source.startswith("hf://"):
        return _fetch_hf(source[len("hf://"):])
    if source.startswith(("http://", "https://")):
        return _fetch_url(source)
    path = Path(source).expanduser()
    if not path.is_file():
        raise FileNotFoundError(f"lexicon not found: {source}")
    return path


def _cache_path(key: str) -> Path:
    safe = "".join(c if c.isalnum() or c in "-._" else "_" for c in key)
    return CACHE_DIR / safe


def _fetch_url(url: str) -> Path:
    dest = _cache_path(url)
    if dest.is_file():
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as resp:              # noqa: S310 - caller-supplied
        data = resp.read()
    dest.write_bytes(data)
    return dest


def _fetch_hf(spec: str) -> Path:
    """Fetch ``<repo_id>/<path>[@<revision>]`` from the Hugging Face Hub.

    Needs ``huggingface_hub``; it is an optional dependency because a lexicon
    is optional and the library must import without network machinery.
    """
    ref, _, revision = spec.partition("@")
    owner, repo, *rest = ref.split("/")
    if not rest:
        raise ValueError(
            f"hf lexicon must be 'hf://<owner>/<repo>/<file>', got 'hf://{spec}'"
        )
    try:
        from huggingface_hub import hf_hub_download
    except ImportError as exc:                              # pragma: no cover
        raise ImportError(
            "a hf:// lexicon needs huggingface_hub — "
            "pip install orthography2ipa[hf]"
        ) from exc
    return Path(hf_hub_download(
        repo_id=f"{owner}/{repo}",
        filename="/".join(rest),
        revision=revision or None,
        repo_type="dataset",
    ))


def lexicon_path(code: str) -> Optional[Path]:
    """The local file backing *code*'s lexicon, or ``None`` if there is none.

    The caller's registration wins, then the lexicon dir, then a packaged
    lexicon the caller enabled with :func:`use_packaged_lexicons`. Fetches a remote source on first call. Never raises for an
    unregistered language — that is the common case.
    """
    code = resolve(code)
    source = _REGISTERED.get(code)
    if source is not None:
        return resolve_lexicon_source(source)
    d = _lexicon_dir()
    if d is not None:
        exact = d / f"{code}.tsv"
        if exact.is_file():
            return exact
        for p in sorted(d.glob("*.tsv")):
            if resolve(p.stem) == code:
                return p
    return _packaged_path(code) if code in _ENABLED else None


def available_lexicon_codes() -> List[str]:
    """Sorted codes with a registered lexicon, a ``{code}.tsv`` in the dir, or an enabled packaged one."""
    codes = set(_REGISTERED) | _ENABLED
    d = _lexicon_dir()
    if d is not None and d.is_dir():
        codes.update(p.stem for p in d.glob("*.tsv"))
    return sorted(codes)


def parse_lexicon_text(text: str) -> Dict[str, str]:
    """Parse TSV *text* into a ``{word: ipa}`` map, first entry winning.

    Blank lines are skipped. Each non-blank line must be ``word<TAB>ipa``;
    the word is NFC-normalised (keys are stored as-authored, i.e. already
    lowercase in a well-formed file — see :func:`validate_lexicon_text`).
    A duplicate word keeps the FIRST occurrence (sorted files make "first"
    deterministic).
    """
    out: Dict[str, str] = {}
    for line in text.split("\n"):
        if not line or not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) != 2:
            continue
        word = unicodedata.normalize("NFC", parts[0])
        ipa = unicodedata.normalize("NFC", parts[1])
        if word and ipa and word not in out:
            out[word] = ipa
    return out


def validate_lexicon_text(text: str) -> List[Tuple[int, str]]:
    """Validate a lexicon TSV body; return a list of ``(line_no, reason)``.

    An empty list means the file is clean. Checks, per non-blank line:

    - exactly one TAB (``word<TAB>ipa`` shape);
    - word and IPA both non-empty;
    - word is NFC and lowercase (``word == word.lower()``);
    - IPA is NFC and contains only IPA characters (:func:`is_ipa_string`);
    - the word is not a duplicate of an earlier line.

    Run it over a lexicon before registering it.
    """
    problems: List[Tuple[int, str]] = []
    seen: set = set()
    for i, line in enumerate(text.split("\n"), start=1):
        if not line or not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) != 2:
            problems.append((i, f"expected 'word<TAB>ipa', got {len(parts)} fields"))
            continue
        word, ipa = parts
        if not word or not ipa:
            problems.append((i, "empty word or IPA"))
            continue
        if unicodedata.normalize("NFC", word) != word:
            problems.append((i, f"word not NFC-normalised: {word!r}"))
        if word != word.lower():
            problems.append((i, f"word not lowercase: {word!r}"))
        if not is_ipa_string(ipa):
            problems.append((i, f"IPA not NFC / not IPA-only: {ipa!r}"))
        if word in seen:
            problems.append((i, f"duplicate word: {word!r}"))
        seen.add(word)
    return problems


@lru_cache(maxsize=None)
def _process_lexicon(code: str) -> Dict[str, str]:
    """The process-wide ``{word: ipa}`` overlay for *code*, or ``{}`` if none is set.

    Reads (and, for a remote source, fetches) the lexicon on first call for
    *code*, then caches it. Nothing is bundled: this returns ``{}`` unless the
    caller registered a lexicon (:func:`register_lexicon`), set a lexicon dir
    (:func:`set_lexicon_dir`), or enabled a packaged one
    (:func:`use_packaged_lexicons`). An absent lexicon is the common case and
    keeps the engine byte-identical for that language.

    *code* must be the resolved, registered language code (e.g. ``"en-GB"``),
    exactly as :attr:`orthography2ipa.g2p.G2P.lang` holds it.
    """
    path = lexicon_path(code)
    if path is None or not path.is_file():
        return {}
    return parse_lexicon_text(path.read_text(encoding="utf-8"))


def get_lexicon(code: str) -> Dict[str, str]:
    """Deprecated: return the process-wide ``{word: ipa}`` overlay for *code*.

    An engine's lexicon is the mapping the caller built, held in
    :attr:`~orthography2ipa.pipeline.Pipeline.lexicon`.
    """
    _warn_deprecated("get_lexicon", "Pipeline.lexicon")
    return _process_lexicon(code)


get_lexicon.cache_clear = _process_lexicon.cache_clear
get_lexicon.cache_info = _process_lexicon.cache_info
