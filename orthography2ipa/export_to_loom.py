"""Export compiled o2i IRs as one self-contained loom GGUF.

The file carries one compiled IR (docs/ir/o2i-ir-v1.md) per requested
language and the Lua interpreter that runs it. Nothing else of the spec data
goes in: the compiler has already resolved inheritance, so the IR of a
language is its whole closure. A voice exports the languages it was trained
with, and ``rev`` compiles them from the spec data of that git ref, so the
file keeps the rules that produced its training phonemes.

loom passes only numbers between host and driver: ``infer`` takes the text
as an array of codepoints and a 0-based ``lang`` index into
``loom.text.languages``, and returns the IPA as an array of codepoints.

    python -m orthography2ipa.export_to_loom --langs pt-PT,kab --out X.gguf [--rev REF] [--fragment PATH ...]

A fragment is a JSON file of plugin data (docs/ir/o2i-ir-v1.md, 3.5). The export
merges each ``--fragment`` into the IR of each language in its scope and records the sha256
of each fragment in ``o2i.fragments``. The names that the fragments list as ``unsupported``
go to ``o2i.unsupported``: the rules the plugin still runs as a host hook.

Python callers use :func:`export_to_loom`, which returns the metadata it writes.
"""
import argparse
import json
from importlib import resources
from pathlib import Path
from typing import Dict, List, Optional, Sequence

from orthography2ipa.ir import layout
from orthography2ipa.ir.compiler import build_ir, fragment_digest, fragment_unsupported
from orthography2ipa.version import VERSION_STR

ARCHITECTURE = "o2i"
INTERPRETER = "interpreter.lua"

# loom refuses a file with no graph and no tensors; a rules-only model needs
# both checks relaxed upstream, so the export carries one inert graph and one
# marker tensor until then.
_INERT_TOPOLOGY = {
    "version": 1,
    "inputs": [],
    "nodes": [],
    "output": "o2i.ruleset",
}


def compile_irs(codes: List[str], rev: Optional[str] = None,
                fragments: Sequence[dict] = ()) -> Dict[str, dict]:
    """The canonical IR document of each code, compiled at spec data ``rev``
    with the plugin *fragments* merged in."""
    return {code: layout.encode(build_ir(code, rev, fragments=fragments)) for code in codes}


def revisions(irs: Dict[str, dict]) -> Dict[str, str]:
    return {code: layout.spec_revision(layout.decode(doc)) for code, doc in irs.items()}


def _lua_long_string(text: str) -> str:
    level = 0
    while f"]{'=' * level}]" in text:
        level += 1
    eq = "=" * level
    return f"[{eq}[{text}]{eq}]"


def _lua_table(items: Dict[str, str]) -> str:
    rows = ",\n".join(f"  [{json.dumps(k)}] = {v}" for k, v in sorted(items.items()))
    return f"{{\n{rows}\n}}"


def driver_script(codes: List[str], irs: Dict[str, dict], revs: Dict[str, str]) -> str:
    """The interpreter with the language list and the IR JSON as its prelude."""
    docs = {c: _lua_long_string(json.dumps(irs[c], ensure_ascii=False, separators=(",", ":"))) for c in codes}
    prelude = (
        f"O2I_VERSION = {json.dumps(VERSION_STR)}\n"
        f"O2I_LANGUAGES = {{{', '.join(json.dumps(c) for c in codes)}}}\n"
        f"O2I_REVISION = {_lua_table({c: json.dumps(revs[c]) for c in codes})}\n"
        f"O2I_IRS = {_lua_table(docs)}\n"
    )
    lua = resources.files("orthography2ipa.ir").joinpath(INTERPRETER).read_text(encoding="utf-8")
    return prelude + lua


def ruleset(codes: List[str], revs: Dict[str, str], rev: Optional[str]) -> str:
    head = f"orthography2ipa {VERSION_STR}" + (f" data_ref={rev}" if rev else "")
    return "; ".join([head] + [f"{c}={revs[c]}" for c in codes])


def phonemizer_identity(code: str, revision: str) -> Dict[str, Optional[str]]:
    """The identity of *code* with the keys of scriptconv's ``PhonemizerIdentity``,
    as a phoonnx voice records it in ``phonemizer_identity``."""
    return {"backend": "orthography2ipa", "distribution": "orthography2ipa", "version": VERSION_STR,
            "lang": code, "revision": revision, "frontend": None}


def export_to_loom(langs: List[str], out_path: Path, *, data_ref: Optional[str] = None,
                   expect_revisions: Optional[Dict[str, str]] = None,
                   fragments: Sequence[dict] = ()) -> dict:
    """Write the GGUF of *langs* to *out_path* and return the metadata it holds.

    Without a git checkout of orthography2ipa, the export compiles the
    installed data, and *data_ref* must be ``None``. *expect_revisions* maps a
    language to its IR revision (``layout.spec_revision``, the value of
    ``o2i.spec_revisions``), not to ``orthography2ipa.spec_revision``. A
    language whose IR revision differs stops the export before any file is
    written. *fragments* are plugin fragments merged into each language in their scope; the
    metadata lists their sha256 digests and the rules they name as unsupported.

    Raises:
        RuntimeError: *data_ref* is set and orthography2ipa is not a git checkout.
        ValueError: *expect_revisions* names a language that is not exported,
            or a revision differs.
    """
    import numpy as np
    from gguf import GGUFWriter

    from orthography2ipa.ir import compiler

    if data_ref is not None and compiler._checkout() is None:
        raise RuntimeError(f"data_ref={data_ref!r} needs a git checkout of orthography2ipa; "
                           f"an installed package exports only its own data (data_ref=None)")
    expect_revisions = expect_revisions or {}
    unknown = sorted(set(expect_revisions) - set(langs))
    if unknown:
        raise ValueError(f"expect_revisions names languages that are not exported: {', '.join(unknown)}")
    irs = compile_irs(langs, data_ref, fragments)
    revs = revisions(irs)
    for code, expected in expect_revisions.items():
        if revs[code] != expected:
            raise ValueError(f"{code}: expected revision {expected}, the data gives {revs[code]}")
    meta = {
        "ruleset": ruleset(langs, revs, data_ref),
        "o2i_version": VERSION_STR,
        "spec_revisions": {c: revs[c] for c in langs},
        "phonemizer_identity": {c: phonemizer_identity(c, revs[c]) for c in langs},
        "fragments": [fragment_digest(f) for f in fragments],
        "unsupported": fragment_unsupported(fragments),
    }
    writer = GGUFWriter(str(out_path), ARCHITECTURE)
    writer.add_string("loom.task", "text2phonemes")
    writer.add_string("loom.input.kind", "text")
    writer.add_string("loom.output.kind", "phonemes")
    writer.add_string("loom.text.phoneme_alphabet", "ipa")
    writer.add_string("loom.phonemizer.ruleset", meta["ruleset"])
    writer.add_array("loom.text.languages", langs)
    writer.add_string("o2i.version", VERSION_STR)
    writer.add_array("o2i.spec_revisions", [revs[c] for c in langs])
    if fragments:
        writer.add_array("o2i.fragments", meta["fragments"])
    if meta["unsupported"]:
        writer.add_array("o2i.unsupported", meta["unsupported"])
    writer.add_string("o2i.phonemizer_identity", json.dumps(meta["phonemizer_identity"], sort_keys=True))
    writer.add_string("model.driver_script", driver_script(langs, irs, revs))
    writer.add_string("model.graph_topology", json.dumps(_INERT_TOPOLOGY))
    writer.add_tensor("o2i.ruleset", np.zeros(1, dtype=np.float32))
    writer.write_header_to_file()
    writer.write_kv_data_to_file()
    writer.write_tensors_to_file()
    writer.close()
    return meta


def main(argv: Optional[List[str]] = None) -> None:
    ap = argparse.ArgumentParser(prog="python -m orthography2ipa.export_to_loom")
    ap.add_argument("--langs", required=True, help="comma-separated language codes")
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--rev", help="git tag or commit of the spec data to compile")
    ap.add_argument("--fragment", type=Path, action="append", default=[],
                    help="a plugin fragment JSON file; repeat for several")
    args = ap.parse_args(argv)
    codes = [c.strip() for c in args.langs.split(",") if c.strip()]
    fragments = [json.loads(path.read_text(encoding="utf-8")) for path in args.fragment]
    export_to_loom(codes, args.out, data_ref=args.rev, fragments=fragments)
    print(args.out)


if __name__ == "__main__":
    main()
