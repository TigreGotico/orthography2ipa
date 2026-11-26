"""Run the Python examples of the README and the guide pages.

A line ``expr  # value`` is a claim that ``expr`` equals the literal ``value``: the test
evaluates it and fails on the first difference. Only a comment that is a
Python literal is a claim, so a prose comment stays a comment.
"""
import ast
import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = [ROOT / "README.md", *sorted((ROOT / "docs" / "guide").glob("*.md"))]
BLOCK = re.compile(r"^```python\n(.*?)^```", re.S | re.M)


RAISES = re.compile(r"^([A-Z]\w*(?:Error|Exception)): ")


def _claims(source: str):
    """(code before the comment, the literal it claims) for each claim line.
    A comment ``SomeError: ...`` claims that the line raises SomeError."""
    for line in source.splitlines():
        code, sep, comment = line.partition("  # ")
        if not sep or not code.strip() or code.startswith((" ", "\t")):
            continue
        raised = RAISES.match(comment.strip())
        if raised:
            yield code.strip(), raised
            continue
        try:
            value = ast.literal_eval(comment.strip())
            ast.parse(code.strip(), mode="eval")
        except (ValueError, SyntaxError):
            continue
        yield code.strip(), value


def _pages():
    for page in PAGES:
        blocks = BLOCK.findall(page.read_text(encoding="utf-8"))
        if any(True for block in blocks for _ in _claims(block)):
            yield pytest.param(blocks, id=str(page.relative_to(ROOT)))


@pytest.mark.parametrize("blocks", list(_pages()))
def test_example_prints_what_its_comment_says(blocks):
    """The blocks of one page run in order and share one scope, as a reader
    runs them."""
    scope: dict = {}
    for source in blocks:
        claims = dict(_claims(source))
        for stmt in ast.parse(source).body:
            code = ast.get_source_segment(source, stmt)
            claim = claims.get(code) if isinstance(stmt, ast.Expr) else None
            if isinstance(claim, re.Match):
                with pytest.raises(Exception) as caught:
                    eval(code, scope)
                assert type(caught.value).__name__ == claim.group(1), code
            elif code in claims and isinstance(stmt, ast.Expr):
                assert eval(code, scope) == claim, code
            else:
                exec(compile(ast.Module([stmt], []), "<docs>", "exec"), scope)
