#!/usr/bin/env python3
"""Generate the reference pages from the code they describe.

Three files are written from the source and never edited by hand:

* ``docs/reference/api.md`` lists every name in ``orthography2ipa.__all__``,
  grouped by the module that defines it, with the first line of its docstring.
* ``docs/reference/cli.md`` holds the ``--help`` output of the
  ``orthography2ipa`` command and of each subcommand.
* ``llms.txt`` is the map of the repository for a language model, built from
  the reading order of ``docs/index.md``.

Run it after changing a public name, a docstring summary, a CLI option or the
documentation index::

    PYTHONPATH=$PWD python scripts/gen_reference_docs.py --write
    PYTHONPATH=$PWD python scripts/gen_reference_docs.py --check

``--check`` writes nothing and exits 1 when a file is stale. The CLI help is
formatted by ``argparse``, whose layout changes between Python versions, so
CI runs the check on Python 3.11.
"""

from __future__ import annotations

import argparse
import importlib.util
import inspect
import os
import re
import subprocess
import sys
from collections import defaultdict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API_PAGE = "docs/reference/api.md"
CLI_PAGE = "docs/reference/cli.md"
LLMS_TXT = "llms.txt"
SUBCOMMANDS = ("list", "info", "transcribe", "distance", "validate")


def _docs_nav():
    path = os.path.join(REPO_ROOT, "scripts", "docs_nav.py")
    spec = importlib.util.spec_from_file_location("docs_nav", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _markdown(text: str) -> str:
    """Turn reStructuredText inline markup into Markdown, and drop em dashes."""
    text = re.sub(r":(?:class|func|meth|attr|mod|data|exc):`~?([^`]+)`",
                  lambda m: "`" + m.group(1).split(".")[-1] + "`", text)
    text = re.sub(r"``([^`]+)``", r"`\1`", text)
    text = re.sub(r"\s*—\s*([^—]+?)\s*—\s*", r" (\1) ", text)
    text = re.sub(r"\s*—\s*", ": ", text).replace("–", "-")
    return text.replace("|", "\\|").strip()


def _summary(obj) -> str:
    doc = inspect.getdoc(obj) or ""
    paragraph = doc.strip().split("\n\n")[0]
    return _markdown(" ".join(paragraph.split()))


def _kind(obj) -> str:
    return "class" if inspect.isclass(obj) else "function"


def _alias(obj) -> str:
    text = re.sub(r"\btyping\.", "", repr(obj))
    return re.sub(r"ForwardRef\('(\w+)'[^)]*\)", r"\1", text)


def api_page(order: list[str]) -> str:
    import orthography2ipa

    groups: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for name in orthography2ipa.__all__:
        obj = getattr(orthography2ipa, name)
        if hasattr(obj, "__origin__"):
            groups["constants and type aliases"].append(
                (name, "type alias", f"`{_alias(obj)}`"))
        elif inspect.isclass(obj) or callable(obj):
            groups[obj.__module__].append((name, _kind(obj), _summary(obj)))
        else:
            groups["constants and type aliases"].append(
                (name, "constant", f"A `{type(obj).__name__}`"))

    lines = [
        "# Python API",
        "",
        "These are the names `import orthography2ipa` exports, from "
        "`orthography2ipa.__all__`. Each summary is the first paragraph of "
        "the docstring. Read the docstring itself for the parameters.",
        "",
        "`scripts/gen_reference_docs.py` writes this page. Do not edit it "
        "by hand.",
    ]
    for module in sorted(groups):
        lines += ["", f"## `{module}`" if module.startswith("orthography2ipa")
                  else f"## {module.capitalize()}", "",
                  "| Name | Kind | Summary |", "| --- | --- | --- |"]
        for name, kind, summary in sorted(groups[module]):
            lines.append(f"| `{name}` | {kind} | {summary} |")
    text = "\n".join(lines) + "\n"
    return text.rstrip() + _docs_nav().footer("reference/api.md", order)


def _help(args: list[str]) -> str:
    env = dict(os.environ, COLUMNS="80", PYTHONPATH=REPO_ROOT)
    env.pop("FORCE_COLOR", None)
    env["NO_COLOR"] = "1"
    out = subprocess.run(
        [sys.executable, "-c",
         "import sys; from orthography2ipa.cli import main; main(sys.argv[1:])",
         *args, "--help"],
        capture_output=True, text=True, env=env, check=True, cwd=REPO_ROOT,
    ).stdout
    # The top-level description prints the live language count. The page
    # shows N so that adding a spec does not make it stale.
    return re.sub(r"tools for \d+ languages", "tools for N languages", out)


def _indented(text: str) -> str:
    """An indented code block. The help text holds blank lines, and the prose
    linter splits paragraphs at blank lines before it removes fenced code."""
    return "\n".join("    " + line if line else "" for line in text.rstrip().splitlines())


def cli_page(order: list[str]) -> str:
    lines = [
        "# Command line",
        "",
        "The package installs one command, `orthography2ipa`. Each subcommand "
        "takes `--json` for output that a program can read. The blocks below "
        "are the real `--help` output. The top-level description prints the "
        "number of registered languages, shown here as N.",
        "",
        "`scripts/gen_reference_docs.py` writes this page. Do not edit it "
        "by hand.",
        "",
        "## `orthography2ipa`",
        "",
        _indented(_help([])),
    ]
    for command in SUBCOMMANDS:
        lines += ["", f"## `orthography2ipa {command}`", "",
                  _indented(_help([command]))]
    return "\n".join(lines) + _docs_nav().footer("reference/cli.md", order)


def llms_txt(order: list[str]) -> str:
    nav = _docs_nav()
    lines = [
        "# orthography2ipa",
        "",
        "> Cited, per-language JSON specs that map spelling to IPA, a "
        "language-agnostic engine that turns them into transcriptions and "
        "ranked pronunciation lattices, and distance metrics that compare "
        "languages on separate axes. No trained weights.",
        "",
        "Start with AGENTS.md before you change anything. Every spec is a "
        "file in orthography2ipa/data/, and its fields are in "
        "orthography2ipa/data/SCHEMA.md.",
        "",
        "## Entry points",
        "",
        "- [README](README.md): what the library does, install, quick start",
        "- [AGENTS.md](AGENTS.md): repository map, setup, hard rules, "
        "checklist before a push",
        "- [Spec schema](orthography2ipa/data/SCHEMA.md): every JSON key the "
        "loader reads",
        "- [Python API](docs/reference/api.md): every exported name",
        "- [Command line](docs/reference/cli.md): every subcommand",
        "- [Scripts](scripts/README.md), [benchmarks](benchmarks/README.md), "
        "[tests](tests/README.md): what each directory holds",
        "",
        "## Documentation, in reading order",
        "",
    ]
    for rel in order:
        if rel.startswith("languages/") and rel != "languages/index.md":
            continue
        lines.append(f"- [{nav._label(rel)}](docs/{rel})")
    lines += [
        "",
        "## Optional",
        "",
        "- [Per-language pages](docs/languages/index.md): phonology notes "
        "for single languages and families",
        "- [Changelog](CHANGELOG.md)",
    ]
    return "\n".join(lines) + "\n"


def outputs() -> dict[str, str]:
    order = _docs_nav().reading_order()
    return {
        API_PAGE: api_page(order),
        CLI_PAGE: cli_page(order),
        LLMS_TXT: llms_txt(order),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="write the files")
    mode.add_argument("--check", action="store_true",
                      help="exit 1 when a file differs from what the code says")
    args = ap.parse_args()

    stale = []
    for rel, wanted in outputs().items():
        path = os.path.join(REPO_ROOT, rel)
        current = None
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                current = fh.read()
        if current == wanted:
            continue
        stale.append(rel)
        if args.write:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(wanted)

    if not stale:
        print("reference files up to date")
        return 0
    if args.write:
        print("wrote " + ", ".join(stale))
        return 0
    print("stale: " + ", ".join(stale)
          + "\nRun: PYTHONPATH=$PWD python scripts/gen_reference_docs.py --write")
    return 1


if __name__ == "__main__":
    sys.exit(main())
