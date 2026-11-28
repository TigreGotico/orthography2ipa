"""IR primitives 13 to 16: the dialect program (docs/ir/o2i-ir-v1.md, 3.10.2-3.10.3).

A program is an ordered list of steps over the joined sentence IPA. Each
step has a gate on the joined spelling and one action: a literal or pattern
rewrite, a positional literal rewrite, a gated codepoint map, or an aligned
word rewrite.
"""
from typing import List

from orthography2ipa.ir import pattern

__all__ = ["run_program"]


def _cps(s: str) -> List[int]:
    return [ord(c) for c in s]


def _gate(g: list, spelling: List[int]) -> bool:
    op = g[0]
    if op == "true":
        return True
    if op == "spell_search":
        return pattern.search(g[1], spelling, 0, pattern.group_count(g[1])) is not None
    if op == "spell_empty":
        return not spelling
    if op == "and":
        return all(_gate(x, spelling) for x in g[1:])
    if op == "or":
        return any(_gate(x, spelling) for x in g[1:])
    if op == "not":
        return not _gate(g[1], spelling)
    raise ValueError(f"unknown gate node {op!r}")


def _at(p: list, x: str, i: int, n: int, spelling: List[int]) -> bool:
    op = p[0]
    if op == "back_reach":
        for j in range(i - 1, -1, -1):
            if x[j] in p[1]:
                return True
            if x[j] in p[2]:
                return False
        return False
    if op == "at_in":
        j = i + p[1]
        return 0 <= j < len(x) and x[j] in p[2]
    if op == "at_end_or_in":
        return i + n >= len(x) or x[i + n] in p[1]
    if op == "ahead_match":
        return pattern.match_at(p[2], _cps(x), i + p[1]) if i + p[1] <= len(x) else False
    if op == "covered_by":
        return any(x.startswith(s, j) for s in p[1] for j in range(max(0, i - len(s) + 1), i + 1))
    if op == "later_has":
        return any(c in p[1] for c in x[i:])
    if op == "spell":
        return _gate(p[1], spelling)
    if op == "true":
        return True
    if op == "and":
        return all(_at(q, x, i, n, spelling) for q in p[1:])
    if op == "or":
        return any(_at(q, x, i, n, spelling) for q in p[1:])
    if op == "not":
        return not _at(p[1], x, i, n, spelling)
    raise ValueError(f"unknown dialect predicate node {op!r}")


def _contextual(x: str, find: str, rep: str, when: list, spelling: List[int]) -> str:
    out: List[str] = []
    i, n = 0, len(find)
    while i < len(x):
        if x[i:i + n] == find and _at(when, x, i, n, spelling):
            out.append(rep)
            i += n
            continue
        out.append(x[i])
        i += 1
    return "".join(out)


def _chain(x: str, on, off, when_on: bool, mapping: dict) -> str:
    state = False
    out: List[str] = []
    for c in x:
        if c in on:
            state = True
            out.append(c)
            continue
        out.append(c if (when_on and not state) else mapping.get(c, c))
        if c in off and state:
            state = False
    return "".join(out)


def _split(interp, text: str) -> List[str]:
    words, current = [], []
    for c in text:
        if interp._c(c, "whitespace"):
            if current:
                words.append("".join(current))
                current = []
        else:
            current.append(c)
    if current:
        words.append("".join(current))
    return words


def _lexical(interp, x: str, spelling: str, rules: list) -> str:
    xw, sw = _split(interp, x), _split(interp, spelling)
    if len(xw) != len(sw):
        return x
    for w in range(len(xw)):
        original = xw[w]
        key = interp.lower(sw[w])
        for word, find, rep in rules:
            if key == word:
                xw[w] = original.replace(find, rep)
    return " ".join(xw)


def run_program(interp, steps: list, ipa: str, spelling: str) -> str:
    cps = _cps(spelling)
    for step in steps:
        if not _gate(step["gate"], cps):
            continue
        kind = step["kind"]
        if kind == "replace":
            ipa = ipa.replace(step["find"], step["rep"])
        elif kind == "sub":
            ipa = interp._sub(step["pattern"], step["template"], _cps(ipa))
        elif kind == "contextual":
            ipa = _contextual(ipa, step["find"], step["rep"], step["when"], cps)
        elif kind == "chain":
            ipa = _chain(ipa, set(step["on"]), set(step["off"]), bool(step["when_on"]), dict(step["map"]))
        elif kind == "lexical":
            ipa = _lexical(interp, ipa, spelling, step["rules"])
        else:
            raise ValueError(f"unknown dialect step {kind!r}")
    return ipa
