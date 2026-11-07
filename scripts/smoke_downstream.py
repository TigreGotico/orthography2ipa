#!/usr/bin/env python3
"""Import a downstream G2P package and transcribe one word with it.

The engine's own tests never load a downstream, so a removed public name
(a module, a class, a function) breaks every consumer silently. This script
is the missing check: with a downstream installed at its declared floor and
this checkout of orthography2ipa installed over it, importing the package and
running one word through it fails loudly on anything the engine took away.

Run it by hand against an installed downstream:

    python scripts/smoke_downstream.py tugaphone

or list the packages it knows about with ``--list``.
"""
from __future__ import annotations

import argparse
import importlib
import sys
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Downstream:
    """A consumer package, the modules it must expose, and one word of work."""

    modules: tuple[str, ...]
    word: str
    transcribe: Callable[[str], object]


def _arbtok(word: str) -> object:
    from arbtok.plugin import word_ipa

    return word_ipa(word)


def _tugaphone(word: str) -> object:
    import tugaphone

    return tugaphone.phonemize(word)


def _euskaphone(word: str) -> object:
    from euskaphone import EuskaPhonemizer

    return EuskaPhonemizer().phonemize_sentence(word)


def _mwl_phonemizer(word: str) -> object:
    import mwl_phonemizer

    return mwl_phonemizer.phonemize(word)


def _g2p_barranquenho(word: str) -> object:
    import g2p_barranquenho

    return g2p_barranquenho.phonemize(word)


DOWNSTREAMS = {
    "arbtok": Downstream(("arbtok", "arbtok.plugin", "arbtok.o2i_plugins"), "كتاب", _arbtok),
    "tugaphone": Downstream(("tugaphone", "tugaphone.plugin"), "olá", _tugaphone),
    "euskaphone": Downstream(("euskaphone", "euskaphone.plugin"), "kaixo", _euskaphone),
    "mwl_phonemizer": Downstream(("mwl_phonemizer", "mwl_phonemizer.crf"), "lhéngua", _mwl_phonemizer),
    "g2p_barranquenho": Downstream(
        ("g2p_barranquenho", "g2p_barranquenho.plugin"), "Barrancos", _g2p_barranquenho
    ),
}


def smoke(name: str) -> None:
    spec = DOWNSTREAMS[name]
    for module in spec.modules:
        importlib.import_module(module)
        print(f"import {module}: ok")
    output = spec.transcribe(spec.word)
    if not output:
        raise SystemExit(f"{name}: transcribing {spec.word!r} produced nothing")
    print(f"{name}: {spec.word!r} -> {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", nargs="?", choices=sorted(DOWNSTREAMS))
    parser.add_argument("--list", action="store_true", help="print the known packages")
    args = parser.parse_args()

    if args.list:
        print("\n".join(sorted(DOWNSTREAMS)))
        return
    if not args.package:
        parser.error("a package name is required")

    import orthography2ipa

    print(f"orthography2ipa {orthography2ipa.__version__} from {orthography2ipa.__file__}")
    smoke(args.package)


if __name__ == "__main__":
    sys.exit(main())
