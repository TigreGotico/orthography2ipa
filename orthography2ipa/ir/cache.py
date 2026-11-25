"""Compiled IR per language, kept in memory and on disk.

:func:`interpreter` is what the public transcription path runs. The first
call for a language and a set of options compiles the spec, which takes from
a fraction of a second to about a minute (the French varieties are the
slowest), and stores the canonical IR document. Later calls in the process
reuse the interpreter; later processes read the document back.

A document is looked up in this order:

1. the package directory ``orthography2ipa/ir/precompiled``, filled at
   release time by ``scripts/build_ir_cache.py``;
2. the user cache directory, ``$O2I_IR_CACHE`` or
   ``$XDG_CACHE_HOME/orthography2ipa/ir`` (``~/.cache`` by default).

The file name holds a key over the spec chain of the language, the engine
source with the IR package and the options, so a changed spec, engine or
compiler never reads a stale document. Set
``O2I_IR_CACHE=off`` to keep the documents in memory only.
"""
from __future__ import annotations

import hashlib
import json
import lzma
import os
import tempfile
from contextlib import suppress
from pathlib import Path
from typing import Dict, Optional, Tuple

from phonematcher.version import VERSION_STR as PHONEMATCHER_VERSION

from orthography2ipa.exceptions import EngineSourceUnavailable
from orthography2ipa.ir.compiler import compile_spec, fragment_digest
from orthography2ipa.ir.interpreter import Interpreter
from functools import lru_cache

import orthography2ipa.revision as source_revision
from orthography2ipa.ir import layout, unidata
from orthography2ipa.registry import resolve

__all__ = ["interpreter", "document", "revision", "document_revision", "cache_key", "write", "PRECOMPILED", "DEFAULT_OPTIONS"]

PRECOMPILED = Path(__file__).resolve().parent / "precompiled"
#: The options of ``G2P(code)`` with no keyword arguments.
DEFAULT_OPTIONS = {"dialect_profile": None, "apply_stress": True, "apply_allophony": True,
                   "apply_sandhi": True, "expand_allophones": False}

_interpreters: Dict[Tuple, Interpreter] = {}


@lru_cache(maxsize=None)
def _engine_bytes() -> str:
    """sha256 over the raw engine source. Unlike the token fingerprint of
    :func:`~orthography2ipa.revision.engine_fingerprint` it costs no
    tokenizing, and a comment edit only makes the cache miss once."""
    # The compiler reads phonematcher, so its version is part of the engine.
    digest = hashlib.sha256(f"unidata:{unidata.VERSION}\nphonematcher:{PHONEMATCHER_VERSION}\n".encode())
    for name in sorted(source_revision.ENGINE_MODULES):
        digest.update(name.encode() + b"\n" + source_revision._module_source(name))
    return digest.hexdigest()


def _key_options(options: Dict[str, object]) -> Dict[str, object]:
    """*options* with the fragments replaced by their digests. No fragment
    leaves the options as they were, so a key without fragments does not move."""
    options = dict(options)
    fragments = options.pop("fragments", ())
    if fragments:
        options["fragments"] = tuple(fragment_digest(f) for f in fragments)
    return options


def cache_key(code: str, options: Dict[str, object]) -> str:
    """The file key of the IR of *code* compiled with *options*: the spec
    chain that :func:`~orthography2ipa.revision.spec_revision` hashes, the
    engine source with the IR package, and the options. Fragments count by
    their digests."""
    digest = hashlib.sha256(f"spec-format:{source_revision.SPEC_FORMAT_VERSION}\n".encode())
    for dep in source_revision._spec_dependencies(resolve(code)):
        digest.update(f"spec:{dep}\n".encode() + source_revision._canonical_spec(dep) + b"\n")
    digest.update(_engine_bytes().encode() + json.dumps(sorted(_key_options(options).items())).encode())
    return digest.hexdigest()[:24]


def _user_dir() -> Optional[Path]:
    env = os.environ.get("O2I_IR_CACHE")
    if env == "off":
        return None
    if env:
        return Path(env)
    base = os.environ.get("XDG_CACHE_HOME") or Path.home() / ".cache"
    return Path(base) / "orthography2ipa" / "ir"


def _read(path: Path) -> Optional[dict]:
    try:
        return json.loads(lzma.decompress(path.read_bytes()))
    except (OSError, ValueError, lzma.LZMAError):
        return None


def write(directory: Path, name: str, doc: dict) -> None:
    """Write *doc* to *directory* / *name* atomically."""
    directory.mkdir(parents=True, exist_ok=True)
    data = lzma.compress(json.dumps(doc, ensure_ascii=False, separators=(",", ":")).encode())
    fd, tmp = tempfile.mkstemp(dir=directory, prefix=".tmp-")
    with os.fdopen(fd, "wb") as f:
        f.write(data)
    os.replace(tmp, directory / name)


def document(code: str, **options) -> dict:
    """The canonical IR document of *code*, from a cache or compiled.

    Raises :class:`~orthography2ipa.ir.compiler.IRUnsupportedFeature` when
    the compiler does not lower the spec.
    """
    try:
        name = f"{code}-{cache_key(code, options)}.json.xz"
    except EngineSourceUnavailable:
        # Without the engine source no cached document can be trusted.
        return compile_spec(code, **options)
    user = _user_dir()
    for directory in (PRECOMPILED, user):
        if directory is not None:
            doc = _read(directory / name)
            if doc is not None:
                return doc
    doc = compile_spec(code, **options)
    if user is not None:
        with suppress(OSError):
            write(user, name, doc)
    return doc


def interpreter(code: str, **options) -> Interpreter:
    """The interpreter of *code* with *options*.

    Raises :class:`~orthography2ipa.ir.compiler.IRUnsupportedFeature` when
    the compiler does not lower the spec.
    """
    key = (code, tuple(sorted(_key_options(options).items())))
    if key not in _interpreters:
        _interpreters[key] = Interpreter(document(code, **options))
    return _interpreters[key]


def document_revision(doc: dict) -> str:
    """``spec_revision`` of section 8.1 for a canonical IR document; equal to
    :func:`~orthography2ipa.ir.layout.spec_revision` of its readable form."""
    manifest = ";".join(sorted(f"{name}={version}" for name, version in doc["primitives"].items()))
    payload = b"o2i-ir\n" + manifest.encode() + b"\n" + layout.canonical_bytes(doc)
    return "sha256:" + hashlib.sha256(payload).hexdigest()


@lru_cache(maxsize=None)
def revision(code: str) -> str:
    """The ``spec_revision`` of the IR that ``G2P(code)`` runs."""
    cache_key(code, DEFAULT_OPTIONS)  # raises EngineSourceUnavailable without the engine source
    return document_revision(document(code, **DEFAULT_OPTIONS))
