"""Optional per-language IPA lexicon overlay.

A **lexicon** is a ``word<TAB>ipa`` TSV — one pair per line, UTF-8,
NFC-normalised, first-entry-wins. It is the unblocker for deep-orthography
languages (English, Danish, Irish) whose rule systems cannot reach production
accuracy from grapheme rules alone.

**Nothing is bundled.** A lexicon is a word list, not a description of a
language, so it is not this library's payload — shipping one would bloat the
wheel and freeze a corpus into a release. The caller supplies it, from a local
file, a URL, or a Hugging Face dataset id::

    import orthography2ipa as o2i

    o2i.register_lexicon("en-GB", "/data/en-GB.tsv")               # local file
    o2i.register_lexicon("en-GB", "https://example.org/en.tsv")    # URL
    o2i.register_lexicon("en-GB", "hf://TigreGotico/en-lexicon/en-GB.tsv")

Or point at a directory of ``{code}.tsv`` files, once::

    o2i.set_lexicon_dir("~/lexicons")                 # or $ORTHOGRAPHY2IPA_LEXICON_DIR

Remote sources are fetched lazily on first use and cached under
``$XDG_CACHE_HOME/orthography2ipa``. A language with no registered lexicon gets
an empty mapping and behaves exactly as if this module did not exist.

Design contract
---------------

- **Lazy.** Importing :mod:`orthography2ipa` (and even loading a
  :class:`~orthography2ipa.types.LanguageSpec`) reads **no** lexicon file, and
  never touches the network. A lexicon is read (and, if remote, fetched) once,
  on the first :func:`get_lexicon` call for that code, and cached for the
  process lifetime.
- **Never implicit.** No lexicon is consulted unless the caller registered one
  (or set a lexicon dir). The library does not download anything on its own.
- **Same pathway as ``word_exceptions``.** :class:`~orthography2ipa.g2p.G2P`
  folds a lexicon hit into the *exact* override path that
  ``spec.word_exceptions`` uses — so a lexicon entry still routes through
  stress-mark insertion and cross-word sandhi, and is reported with the same
  ``confidence == 1.0`` (a certain answer).
- **Precedence.** inline ``spec.word_exceptions`` > lexicon > rules. An inline
  exception always wins over the sidecar; the sidecar always wins over the
  grapheme/positional beam.
- **Absent lexicon → byte-identical.** A language with no registered lexicon
  gets an empty mapping and behaves exactly as it did before this module
  existed.

``scripts/build_en_lexicon.py`` builds a CMUdict-derived ``en-GB.tsv`` you can
register; see ``docs/bibliography.md``.
"""
from __future__ import annotations

import os
import unicodedata
import urllib.request
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Optional, Tuple

__all__ = [
    "get_lexicon",
    "register_lexicon",
    "clear_lexicons",
    "set_lexicon_dir",
    "resolve_lexicon_source",
    "available_lexicon_codes",
    "lexicon_path",
    "parse_lexicon_text",
    "validate_lexicon_text",
    "is_ipa_string",
]

#: Env var naming a directory of ``{code}.tsv`` lexicons.
LEXICON_DIR_ENV = "ORTHOGRAPHY2IPA_LEXICON_DIR"

#: Where fetched remote lexicons are cached.
CACHE_DIR = Path(
    os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")
) / "orthography2ipa" / "lexicons"

# code -> source (path, URL or hf:// id), set by register_lexicon()
_REGISTERED: Dict[str, str] = {}
_LEXICON_DIR: Optional[Path] = None

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
    """Register the lexicon *source* to use for language *code*.

    *source* is a local path, an ``http(s)://`` URL, or a Hugging Face id
    (``hf://<repo_id>/<path>``, optionally ``@<revision>``). Nothing is read
    or fetched here — resolution is lazy, on first transcription for *code*.
    """
    _REGISTERED[code] = source
    get_lexicon.cache_clear()


def set_lexicon_dir(path) -> None:
    """Use *path* as a directory of ``{code}.tsv`` lexicons (``None`` to unset).

    A lexicon registered with :func:`register_lexicon` still wins for its code.
    """
    global _LEXICON_DIR
    _LEXICON_DIR = Path(path).expanduser() if path is not None else None
    get_lexicon.cache_clear()


def clear_lexicons() -> None:
    """Forget every registered lexicon and the lexicon dir."""
    global _LEXICON_DIR
    _REGISTERED.clear()
    _LEXICON_DIR = None
    get_lexicon.cache_clear()


def _lexicon_dir() -> Optional[Path]:
    if _LEXICON_DIR is not None:
        return _LEXICON_DIR
    env = os.environ.get(LEXICON_DIR_ENV)
    return Path(env).expanduser() if env else None


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
    try:
        from huggingface_hub import hf_hub_download
    except ImportError as exc:                              # pragma: no cover
        raise ImportError(
            "a hf:// lexicon needs huggingface_hub — "
            "pip install orthography2ipa[hf]"
        ) from exc
    ref, _, revision = spec.partition("@")
    owner, repo, *rest = ref.split("/")
    if not rest:
        raise ValueError(
            f"hf lexicon must be 'hf://<owner>/<repo>/<file>', got 'hf://{spec}'"
        )
    return Path(hf_hub_download(
        repo_id=f"{owner}/{repo}",
        filename="/".join(rest),
        revision=revision or None,
        repo_type="dataset",
    ))


def lexicon_path(code: str) -> Optional[Path]:
    """The local file backing *code*'s lexicon, or ``None`` if there is none.

    Fetches a remote source on first call. Never raises for an unregistered
    language — that is the common case.
    """
    source = _REGISTERED.get(code)
    if source is not None:
        return resolve_lexicon_source(source)
    d = _lexicon_dir()
    if d is not None:
        p = d / f"{code}.tsv"
        if p.is_file():
            return p
    return None


def available_lexicon_codes() -> List[str]:
    """Sorted language codes with a registered lexicon or a ``{code}.tsv`` in the dir."""
    codes = set(_REGISTERED)
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
def get_lexicon(code: str) -> Dict[str, str]:
    """Return the ``{word: ipa}`` overlay for *code*, or ``{}`` if none is set.

    Reads (and, for a remote source, fetches) the lexicon on first call for
    *code*, then caches it. Nothing is bundled: this returns ``{}`` unless the
    caller registered a lexicon (:func:`register_lexicon`) or set a lexicon dir
    (:func:`set_lexicon_dir`). An absent lexicon is the common case and keeps
    the engine byte-identical for that language.

    *code* must be the resolved, registered language code (e.g. ``"en-GB"``),
    exactly as :attr:`orthography2ipa.g2p.G2P.lang` holds it.
    """
    path = lexicon_path(code)
    if path is None or not path.is_file():
        return {}
    return parse_lexicon_text(path.read_text(encoding="utf-8"))
