"""Primitive 2 of the o2i IR: the pattern matcher (spec section 5).

A pattern is a parse tree that the compiler wrote. The matcher runs it over
a list of codepoints with Python ``re`` semantics: leftmost match, ordered
alternation, greedy quantifiers with backtracking, a group keeps its last
iteration. No pattern text is parsed here.

Nodes (all integers but the node name):

    ["lit", cp]                  one codepoint
    ["any"]                      any codepoint but U+000A, as ``.`` without DOTALL
    ["set", neg, [[lo, hi]...]]  a class of codepoints
    ["bol"], ["eol"]             the anchors ^ and $
    ["seq", node...], ["alt", node...]
    ["group", n, node]           capturing group n
    ["opt", node], ["star", node], ["plus", node]
    ["ahead", neg, node]         lookahead
    ["behind", neg, node]        one-codepoint lookbehind over lit or set
"""
from typing import Callable, List, Optional, Sequence, Tuple

Groups = Tuple[Optional[Tuple[int, int]], ...]
_Cont = Callable[[int, Groups], Optional[Tuple[int, Groups]]]


def _in_set(node: list, c: int) -> bool:
    hit = any(lo <= c <= hi for lo, hi in node[2])
    return hit != bool(node[1])


def _one(node: list, s: Sequence[int], i: int) -> bool:
    if i >= len(s):
        return False
    if node[0] == "lit":
        return s[i] == node[1]
    if node[0] == "any":
        return s[i] != 10
    return _in_set(node, s[i])


def _match(node: list, s: Sequence[int], i: int, groups: Groups, k: _Cont):
    op = node[0]
    if op in ("lit", "any", "set"):
        return k(i + 1, groups) if _one(node, s, i) else None
    if op == "seq":
        return _seq(node, 1, s, i, groups, k)
    if op == "alt":
        for alt in node[1:]:
            r = _match(alt, s, i, groups, k)
            if r is not None:
                return r
        return None
    if op == "bol":
        return k(i, groups) if i == 0 else None
    if op == "eol":
        n = len(s)
        return k(i, groups) if i == n or (i == n - 1 and s[i] == 10) else None
    if op == "group":
        n = node[1]

        def close(j: int, g: Groups):
            g = g[:n] + ((i, j),) + g[n + 1:]
            return k(j, g)
        return _match(node[2], s, i, groups, close)
    if op in ("star", "plus", "opt"):
        return _repeat(node, s, i, groups, k, 0)
    if op == "ahead":
        found = _match(node[2], s, i, groups, lambda j, g: (j, g))
        if node[1]:
            return k(i, groups) if found is None else None
        return k(i, found[1]) if found is not None else None
    if op == "behind":
        ok = i > 0 and _one(node[2], s, i - 1)
        return k(i, groups) if ok != bool(node[1]) else None
    raise ValueError(f"unknown pattern node {op!r}")


def _seq(node: list, at: int, s, i: int, groups: Groups, k: _Cont):
    if at == len(node):
        return k(i, groups)
    return _match(node[at], s, i, groups,
                  lambda j, g: _seq(node, at + 1, s, j, g, k))


def _repeat(node: list, s, i: int, groups: Groups, k: _Cont, count: int):
    op = node[0]
    limit = 1 if op == "opt" else -1
    if limit < 0 or count < limit:
        def more(j: int, g: Groups):
            if j == i:  # an empty iteration ends the loop, as in re
                return None
            return _repeat(node, s, j, g, k, count + 1)
        r = _match(node[1], s, i, groups, more)
        if r is not None:
            return r
    if op == "plus" and count == 0:
        return None
    return k(i, groups)


def group_count(node: list) -> int:
    if node[0] == "group":
        return max(node[1], group_count(node[2]))
    if node[0] in ("lit", "any", "set", "bol", "eol"):
        return 0
    children = node[2:] if node[0] in ("ahead", "behind") else node[1:]
    return max((group_count(c) for c in children if isinstance(c, list)), default=0)


def search(node: list, s: Sequence[int], start: int = 0, ngroups: int = 0,
           no_empty_at: int = -1) -> Optional[Tuple[int, int, Groups]]:
    """The leftmost match at or after *start*: (start, end, groups).

    A match at *no_empty_at* must not be empty.
    """
    empty: Groups = (None,) * (ngroups + 1)
    for i in range(start, len(s) + 1):
        if i == no_empty_at:
            r = _match(node, s, i, empty, lambda j, g: None if j == i else (j, g))
        else:
            r = _match(node, s, i, empty, lambda j, g: (j, g))
        if r is not None:
            return i, r[0], r[1]
    return None


def match_at(node: list, s: Sequence[int], i: int) -> bool:
    return _match(node, s, i, (None,) * (group_count(node) + 1),
                  lambda j, g: (j, g)) is not None


def sub(node: list, template: List[list], s: Sequence[int],
        strings: Sequence[Sequence[int]], count: int = 0) -> List[int]:
    """``re.sub``: replace every non-overlapping match, left to right.

    After an empty match the next match may start at the same place only
    if it is not empty, as in ``re`` from Python 3.7. A template part is
    ``["lit", string index]`` or ``["group", n]``.
    """
    ngroups = group_count(node)
    out: List[int] = []
    pos = done = made = 0
    no_empty_at = -1
    while pos <= len(s) and not (count and made == count):
        m = search(node, s, pos, ngroups, no_empty_at)
        if m is None:
            break
        start, end, groups = m
        out += s[done:start]
        for part in template:
            if part[0] == "lit":
                out += strings[part[1]]
            else:
                span = groups[part[1]]
                if span is not None:
                    out += s[span[0]:span[1]]
        done = pos = end
        no_empty_at = end if end == start else -1
        made += 1
    out += s[done:]
    return out
