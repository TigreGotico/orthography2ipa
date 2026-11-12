"""Content revisions of a spec and of a packaged lexicon.

The output of an engine is a function of the spec, the input and the explicit
configuration of the caller. A revision names the first of these, so that a
consumer that recorded one when it trained can tell whether the engine it runs
reads the same rules.

:func:`spec_revision` hashes the spec files that the loader reads for a code
and the source of the engine modules that interpret them. :func:`lexicon_revision`
hashes the packaged lexicon that :func:`~orthography2ipa.lexicon.packaged_lexicon`
reads, because a lexicon changes output from outside the spec.
"""
from __future__ import annotations

import hashlib
import io
import json
import tokenize
from functools import lru_cache
from importlib.resources import files
from typing import Iterable, List, Optional, Tuple

from orthography2ipa.exceptions import EngineSourceUnavailable
from orthography2ipa.json_loader import _BASE_MERGE_FIELDS, _index
from orthography2ipa.lexicon import (
    ENTRY_POINT_GROUP,
    PATCH_ENTRY_POINT_GROUP,
    _packaged_path,
    _packaged_providers,
)
from orthography2ipa.registry import resolve

#: The version of the meaning of the spec fields. It goes up when a field of
#: a spec starts to mean something else, and every spec revision changes with it.
SPEC_FORMAT_VERSION = 1

#: The modules on the transcription path: the rules, the loader, the registry,
#: the lattice, stress, the pipeline and the plugin contracts. Their source
#: makes the engine fingerprint. Tooling (CLI, benchmarks, conformance,
#: distance metrics, validation) stays out.
ENGINE_MODULES: Tuple[str, ...] = (
    "allophony",
    "exceptions",
    "feats",
    "features",
    "g2p",
    "inventory",
    "json_loader",
    "lexicon",
    "lm",
    "markup",
    "phonetok",
    "pipeline",
    "plugins",
    "positional",
    "registry",
    "rescorer",
    "rescorer_plugin",
    "sandhi",
    "sentence",
    "stress",
    "stress_plugin",
    "syllabifier_plugin",
    "syllabifiers",
    "tone",
    "transforms",
    "types",
    "vowels",
    "weights",
)

# Comments and blank lines change no behaviour. ENCODING and ENDMARKER carry none.
_LAYOUT_TOKENS = frozenset({
    tokenize.COMMENT, tokenize.NL, tokenize.ENCODING, tokenize.ENDMARKER,
})
# Statement ends and block edges change behaviour. The width of an indent does
# not, so these tokens count with an empty string.
_STRUCTURE_TOKENS = frozenset({tokenize.NEWLINE, tokenize.INDENT, tokenize.DEDENT})
# Python 3.12 splits an f-string into parts. Python 3.11 gives one STRING
# token. The fingerprint uses the 3.11 form, so it is equal across versions.
_FSTRING_START = {name for name in ("FSTRING_START", "TSTRING_START")
                  if hasattr(tokenize, name)}
_FSTRING_END = {name for name in ("FSTRING_END", "TSTRING_END")
                if hasattr(tokenize, name)}


def _source_tokens(source: bytes) -> Iterable[Tuple[str, str]]:
    """The ``(type name, string)`` pairs of *source*, without comments and blank lines.

    NEWLINE, INDENT and DEDENT count with an empty string, so a line that moves
    in or out of a block counts and the width of an indent does not.
    """
    source = source.replace(b"\r\n", b"\n")
    lines = source.decode("utf-8").splitlines(keepends=True)
    depth = 0
    start = (0, 0)
    for token in tokenize.tokenize(io.BytesIO(source).readline):
        name = tokenize.tok_name[token.type]
        if name in _FSTRING_START:
            if depth == 0:
                start = token.start
            depth += 1
            continue
        if depth:
            if name in _FSTRING_END:
                depth -= 1
                if depth == 0:
                    yield "STRING", _span(lines, start, token.end)
            continue
        if token.type in _STRUCTURE_TOKENS:
            yield name, ""
        elif token.type not in _LAYOUT_TOKENS:
            yield name, token.string


def _span(lines: List[str], start: Tuple[int, int], end: Tuple[int, int]) -> str:
    """The source text from *start* to *end*, as tokenize gives positions."""
    (row0, col0), (row1, col1) = start, end
    if row0 == row1:
        return lines[row0 - 1][col0:col1]
    return (lines[row0 - 1][col0:] + "".join(lines[row0:row1 - 1])
            + lines[row1 - 1][:col1])


def _fingerprint(sources: Iterable[Tuple[str, bytes]]) -> str:
    """sha256 over the tokens of each ``(relative path, source)``, in the given order."""
    digest = hashlib.sha256()
    for path, source in sources:
        digest.update(json.dumps(["file", path]).encode() + b"\n")
        for pair in _source_tokens(source):
            digest.update(json.dumps(pair, ensure_ascii=False).encode() + b"\n")
    return digest.hexdigest()


def _module_source(name: str) -> bytes:
    try:
        return (files("orthography2ipa") / f"{name}.py").read_bytes()
    except OSError as e:
        raise EngineSourceUnavailable(
            f"cannot read the source of orthography2ipa.{name}: {e}") from e


@lru_cache(maxsize=None)
def engine_fingerprint() -> str:
    """sha256 over the tokens of the :data:`ENGINE_MODULES` source files.

    Comments, blank lines and the width of an indent do not count. Statement
    ends, block edges and docstrings do. The package version does not count,
    because an alpha release changes it with no change to the engine.

    The files are read at the first call in a process, and the value is kept.
    A process whose package files change on disk before that first call
    reports the files on disk, not the code it runs.

    Raises
    ------
    EngineSourceUnavailable
        The source of an engine module cannot be read, as in an install that
        ships only byte code.
    """
    return _fingerprint((f"orthography2ipa/{name}.py", _module_source(name))
                        for name in sorted(ENGINE_MODULES))


@lru_cache(maxsize=None)
def _canonical_spec(code: str) -> bytes:
    """The parsed spec file of *code* as JSON with sorted keys and no whitespace."""
    with _index[code].open(encoding="utf-8") as f:
        raw = json.load(f)
    return json.dumps(raw, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":")).encode()


def _data_parent(raw: dict) -> Optional[str]:
    """The ``parent`` that the loader walks through when it resolves a child.

    A clade with no ``parent`` key takes its first ``parent``-role ancestor,
    as :class:`~orthography2ipa.types.LanguageSpec` sets it, and the loader
    walks through a clade to the nearest spec with data.
    """
    if raw.get("parent") or not raw.get("clade"):
        return raw.get("parent")
    return next((a.get("code") for a in raw.get("ancestors") or ()
                 if a.get("role") == "parent"), None)


def _spec_dependencies(code: str) -> List[str]:
    """*code*, then every spec the loader merges into it, sorted.

    The loader merges data along ``parent`` (inherited rules and stress) and
    each ``<field>_base`` key, and so does this walk, to the end of each chain.
    Other ``ancestors`` codes are left out: the loader reads those specs but
    merges none of their data. A code with no spec file is skipped, as the
    loader skips it.
    """
    seen = {code}
    stack = [code]
    while stack:
        raw = json.loads(_canonical_spec(stack.pop()))
        edges = [_data_parent(raw),
                 *(raw.get(f"{field}_base") for field in _BASE_MERGE_FIELDS)]
        for dep in edges:
            if dep and dep in _index and dep not in seen:
                seen.add(dep)
                stack.append(dep)
    return [code, *sorted(seen - {code})]


@lru_cache(maxsize=None)
def _spec_revision(code: str) -> str:
    digest = hashlib.sha256()
    digest.update(f"spec-format:{SPEC_FORMAT_VERSION}\n".encode())
    for dep in _spec_dependencies(code):
        digest.update(f"spec:{dep}\n".encode() + _canonical_spec(dep) + b"\n")
    digest.update(f"engine:{engine_fingerprint()}\n".encode())
    return "sha256:" + digest.hexdigest()


def spec_revision(code: str) -> str:
    """sha256 over the canonical spec JSON, its parent chain and engine rule version.

    *code* resolves as :class:`~orthography2ipa.g2p.G2P` resolves it, so an
    alias and its canonical code give one revision. The hash input is, in this
    order: :data:`SPEC_FORMAT_VERSION`; the spec of *code*; every other spec
    the loader merges into it (``parent``, or the first ``parent``-role
    ancestor of a clade that has no ``parent``, and the ``<field>_base`` keys,
    followed to the end of each chain, sorted by code); and
    :func:`engine_fingerprint`. Each spec counts as its parsed JSON with
    sorted keys and no whitespace, tagged with its code, so a whitespace-only
    edit leaves the revision equal.

    Returns ``"sha256:"`` and the hex digest. The value is computed at the
    first call for a code in a process and kept, as the loader reads each spec
    once per process.

    Raises
    ------
    KeyError
        *code* resolves to no registered spec.
    EngineSourceUnavailable
        The source of an engine module cannot be read.
    """
    resolved = resolve(code)
    if resolved not in _index:
        raise KeyError(f"unsupported language: {code!r} resolves to no spec")
    return _spec_revision(resolved)


def lexicon_revision(code: str, patches: bool = False) -> str:
    """sha256 over the packaged lexicon files that ``packaged_lexicon(code, patches)`` reads.

    The hash input is the *patches* flag, the bytes of the exceptions file and,
    with *patches* ``True``, the bytes of the patch file. Returns ``"sha256:"``
    and the hex digest. The files are read on each call, as
    :func:`~orthography2ipa.lexicon.packaged_lexicon` reads them.

    Raises
    ------
    LookupError
        No installed package supplies a lexicon file for *code*, or *patches*
        is ``True`` and no installed package supplies a patch file for it.
    """
    resolved = resolve(code)
    groups = [("lexicon", ENTRY_POINT_GROUP)]
    if patches:
        groups.append(("patch", PATCH_ENTRY_POINT_GROUP))
    digest = hashlib.sha256(f"patches:{int(patches)}\n".encode())
    for kind, group in groups:
        path = _packaged_path(resolved, group)
        if path is None:
            raise LookupError(
                f"no installed package supplies a {kind} file for {resolved!r}; "
                f"installed: {sorted(_packaged_providers(group)) or 'nothing'}")
        data = path.read_bytes()
        digest.update(f"{kind}:{len(data)}\n".encode() + data)
    return "sha256:" + digest.hexdigest()
