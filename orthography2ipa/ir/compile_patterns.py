"""Compile-time half of IR primitive 2: pattern text to the parse tree of
``orthography2ipa.ir.pattern`` (docs/ir/o2i-ir-v1.md, section 5.1).

Python's own parser reads the text, so the tree means exactly what ``re``
means. A construct outside the section 5.1 subset is an error.
"""
import re
from re import _constants as C
from re import _parser
from typing import List

__all__ = ["compile_pattern", "compile_template", "PatternOutsideSubset"]


class PatternOutsideSubset(ValueError):
    pass


def _whitespace_ranges() -> List[List[int]]:
    cps = [cp for cp in range(0x110000) if re.match(r"\s", chr(cp))]
    ranges: List[List[int]] = []
    for cp in cps:
        if ranges and ranges[-1][1] == cp - 1:
            ranges[-1][1] = cp
        else:
            ranges.append([cp, cp])
    return ranges


_WS = _whitespace_ranges()


def _class(items, text: str) -> list:
    neg = 0
    ranges: List[List[int]] = []
    for op, av in items:
        if op is C.NEGATE:
            neg = 1
        elif op is C.LITERAL:
            ranges.append([av, av])
        elif op is C.RANGE:
            ranges.append([av[0], av[1]])
        elif op is C.CATEGORY and av is C.CATEGORY_SPACE:
            ranges += _WS
        else:
            raise PatternOutsideSubset(f"{text!r}: class item {op} {av}")
    return ["set", neg, sorted(ranges)]


def _seq(items, text: str) -> list:
    nodes = [_node(op, av, text) for op, av in items]
    return nodes[0] if len(nodes) == 1 else ["seq", *nodes]


def _node(op, av, text: str) -> list:
    if op is C.LITERAL:
        return ["lit", av]
    if op is C.NOT_LITERAL:
        return ["set", 1, [[av, av]]]
    if op is C.ANY:
        return ["any"]
    if op is C.IN:
        return _class(av, text)
    if op is C.AT:
        if av is C.AT_BEGINNING:
            return ["bol"]
        if av is C.AT_END:
            return ["eol"]
    if op is C.SUBPATTERN:
        group, add, delete, sub = av
        if add or delete:
            raise PatternOutsideSubset(f"{text!r}: inline flags")
        inner = _seq(sub, text)
        return inner if group is None else ["group", group, inner]
    if op is C.BRANCH:
        return ["alt", *(_seq(branch, text) for branch in av[1])]
    if op is C.MAX_REPEAT:
        lo, hi, sub = av
        inner = _seq(sub, text)
        if _nullable(inner):
            raise PatternOutsideSubset(f"{text!r}: a quantifier over a body that can match empty")
        if (lo, hi) == (0, 1):
            return ["opt", inner]
        if (lo, hi) == (0, C.MAXREPEAT):
            return ["star", inner]
        if (lo, hi) == (1, C.MAXREPEAT):
            return ["plus", inner]
    if op is C.FAILURE:
        # Python 3.13 and later parse "(?!)" to FAILURE; 3.12 and earlier to an
        # empty negative lookahead. Both mean "never matches": emit the
        # lookahead so the IR is the same on every Python version.
        return ["ahead", 1, ["seq"]]
    if op in (C.ASSERT, C.ASSERT_NOT):
        direction, sub = av
        neg = int(op is C.ASSERT_NOT)
        inner = _seq(sub, text)
        if direction == 1:
            return ["ahead", neg, inner]
        if inner[0] in ("lit", "set", "any"):
            return ["behind", neg, inner]
        raise PatternOutsideSubset(f"{text!r}: lookbehind wider than one codepoint")
    raise PatternOutsideSubset(f"{text!r}: {op} is outside the IR pattern subset")


def _nullable(node: list) -> bool:
    op = node[0]
    if op in ("lit", "any", "set"):
        return False
    if op == "seq":
        return all(_nullable(n) for n in node[1:])
    if op == "alt":
        return any(_nullable(n) for n in node[1:])
    if op == "group":
        return _nullable(node[2])
    if op == "plus":
        return _nullable(node[1])
    return True


def compile_pattern(text: str) -> list:
    return _seq(_parser.parse(text), text) if text else ["seq"]


def compile_template(template: str) -> list:
    """``re.sub`` template text to ``[["lit", s] | ["group", n], ...]``."""
    parts: List[list] = []
    lit = ""
    i = 0
    escapes = {"n": "\n", "t": "\t", "r": "\r", "\\": "\\", "a": "\a", "f": "\f", "v": "\v"}
    while i < len(template):
        c = template[i]
        if c != "\\":
            lit += c
            i += 1
            continue
        nxt = template[i + 1:i + 2]
        if nxt.isdigit():
            j = i + 1
            while j < len(template) and template[j].isdigit() and j < i + 3:
                j += 1
            group = int(template[i + 1:j])
            i = j
        elif nxt == "g":
            end = template.index(">", i)
            group = int(template[i + 3:end])
            i = end + 1
        elif nxt in escapes:
            lit += escapes[nxt]
            i += 2
            continue
        else:
            raise PatternOutsideSubset(f"template {template!r}: escape \\{nxt}")
        if lit:
            parts.append(["lit", lit])
            lit = ""
        parts.append(["group", group])
    if lit:
        parts.append(["lit", lit])
    return parts
