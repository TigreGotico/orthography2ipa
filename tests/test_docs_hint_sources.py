"""Each file and symbol that an engine page names in its agent-hint ``source``
exists in the code.

An entry is a path (globs allowed), or ``path:Name`` / ``path:Class.method``
for a symbol defined at the top level of a Python file.
"""
import ast
import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = [*sorted((ROOT / "docs" / "engine").glob("*.md")),
         ROOT / "docs" / "contributing" / "engine.md"]
SOURCE = re.compile(r"<!-- agent-hint\n.*?^source: (.*?)$", re.S | re.M)


def _entries(page: pathlib.Path):
    line = SOURCE.search(page.read_text(encoding="utf-8")).group(1)
    return [e.strip().strip("`") for e in line.split(", ")]


def _defines(path: pathlib.Path, dotted: str) -> bool:
    body = ast.parse(path.read_text(encoding="utf-8")).body
    for part in dotted.split("."):
        names = {}
        for node in body:
            if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                names[node.name] = node
            elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                names.update({t.id: node for t in targets if isinstance(t, ast.Name)})
        if part not in names:
            return False
        body = getattr(names[part], "body", [])
    return True


@pytest.mark.parametrize("page", PAGES, ids=lambda p: str(p.relative_to(ROOT)))
def test_hint_sources_exist(page):
    for entry in _entries(page):
        path, _, symbol = entry.partition(":")
        assert list(ROOT.glob(path)), f"{entry}: no such file"
        if symbol:
            assert _defines(ROOT / path, symbol), f"{entry}: no such symbol"
