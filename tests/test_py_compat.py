"""Tests for consistent type annotation style and package hygiene.

Validates:
- Every module using PEP 585/604 annotation syntax has the
  ``from __future__ import annotations`` escape hatch
- The public API exports the engine base types and sandhi entry points
"""
import ast
import pathlib

import pytest

PACKAGE_ROOT = pathlib.Path(__file__).parent.parent / "orthography2ipa"


def _has_future_annotations(tree: ast.Module) -> bool:
    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and node.module == "__future__":
            if any(alias.name == "annotations" for alias in node.names):
                return True
    return False


def _runtime_annotation_nodes(tree: ast.Module):
    """Yield annotation expressions evaluated at module import time.

    Function signatures and dataclass fields are evaluated eagerly unless
    ``from __future__ import annotations`` is in effect.
    """
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for arg in node.args.args + node.args.kwonlyargs:
                if arg.annotation:
                    yield arg.annotation
            if node.returns:
                yield node.returns
        elif isinstance(node, ast.AnnAssign) and node.annotation:
            yield node.annotation


def _uses_modern_syntax(annotation: ast.expr) -> bool:
    """True if the annotation needs Python 3.10+ without the future import."""
    for node in ast.walk(annotation):
        # PEP 604 unions: X | Y
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
            return True
        # PEP 585 builtin generics: dict[...], list[...], tuple[...], set[...]
        if (isinstance(node, ast.Subscript)
                and isinstance(node.value, ast.Name)
                and node.value.id in ("dict", "list", "tuple", "set",
                                      "frozenset", "type")):
            return True
    return False


@pytest.mark.parametrize(
    "module_path",
    sorted(PACKAGE_ROOT.rglob("*.py")),
    ids=lambda p: str(p.relative_to(PACKAGE_ROOT)),
)
def test_consistent_annotation_style(module_path):
    """Modules using modern annotation syntax must import future annotations."""
    tree = ast.parse(module_path.read_text(encoding="utf-8"))
    if _has_future_annotations(tree):
        return
    offending = [
        ast.unparse(node) for node in _runtime_annotation_nodes(tree)
        if _uses_modern_syntax(node)
    ]
    assert not offending, (
        f"{module_path.name} uses PEP 585/604 annotations without "
        f"'from __future__ import annotations': {offending}"
    )


class TestPublicExports:
    """Plugin and sandhi entry points are part of the public API."""

    def test_exports(self):
        import orthography2ipa

        for name in ("WordContext", "SandhiEngine"):
            assert name in orthography2ipa.__all__
            assert hasattr(orthography2ipa, name)
