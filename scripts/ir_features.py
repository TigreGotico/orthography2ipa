"""The IR features that the conformance vectors of section 8.4 must exercise.

The feature list comes from the IR schema in ``orthography2ipa.ir.layout``:
every primitive and field name of ``SEMANTICS`` (with its ``node.*`` and
``syll.*`` predicate nodes), and every node of the spelling gates
(``gate.*``) and of the dialect predicates (``dnode.*``).

A case exercises a feature when the ablation of the feature changes the
output of the reference interpreter on that case. The ablation of a
predicate node wraps every node of that kind in ``not``. The ablation of a
field or a primitive removes the IR data that it reads.
"""
import copy
import json
from typing import Callable, Dict, List, Optional

from orthography2ipa.ir import layout

_TABLES = {layout.PRED: ("node.", layout._SLOT_ARGS), layout.GATE: ("gate.", layout._GATE_ARGS),
           layout.DPRED: ("dnode.", layout._DPRED_ARGS)}


def feature_names() -> List[str]:
    names = set(layout.SEMANTICS)
    names |= {"gate." + op for op in layout._GATE_ARGS}
    names |= {"dnode." + op for op in layout._DPRED_ARGS}
    return sorted(names)


def _node_name(t: str, node: list) -> str:
    if t == layout.PRED and node[0] == "syll":
        return "syll." + node[1]
    return _TABLES[t][0] + node[0]


def _negate(t, v, name: str):
    """*v* (layout *t*) with every predicate node called *name* wrapped in ``not``."""
    if isinstance(t, str) and t in _TABLES:
        args = _TABLES[t][1][v[0]]
        if args == "preds":
            node = [v[0], *(_negate(t, x, name) for x in v[1:])]
        else:
            node = [v[0], *(_negate(a, x, name) for a, x in zip(args, v[1:]))]
        hit = name in (_node_name(t, v), _TABLES[t][0] + v[0])
        return ["not", node] if hit else node
    if isinstance(t, tuple):
        if t[0] == "list":
            return [_negate(t[1], x, name) for x in v]
        if t[0] == "pair":
            return [_negate(t[1], v[0], name), _negate(t[2], v[1], name)]
        if t[0] == "obj":
            return {k: _negate(t[1][k], x, name) for k, x in v.items()}
    return v


def _clear(ir: dict, *path) -> None:
    *head, last = path
    node = ir
    for key in head:
        node = node.get(key)
        if not isinstance(node, dict):
            return
    if last in node:
        value = node[last]
        if isinstance(value, dict):
            del node[last]
        else:
            node[last] = 0 if isinstance(value, int) else type(value)()


def _drop(ir: dict, *path) -> None:
    *head, last = path
    node = ir
    for key in head:
        node = node.get(key)
        if not isinstance(node, dict):
            return
    node.pop(last, None)


def _entry_bit(ir: dict, name: str) -> None:
    mask = ~(1 << ir["bits"]["entry"].index(name))
    for e in ir["entries"]:
        e["bits"] &= mask


def _steps(ir: dict, *kinds) -> None:
    if "dialect" in ir:
        ir["dialect"] = [s for s in ir["dialect"] if s["kind"] not in kinds]


def _sandhi_pause(ir: dict) -> None:
    if "sandhi" in ir:
        ir["sandhi"] = [r for r in ir["sandhi"] if not r.get("pause")]


def _sandhi_spelling(ir: dict) -> None:
    for rule in ir.get("sandhi", ()):
        rule.pop("left_spelling", None)
        rule.pop("right_spelling", None)


def _sandhi_joined(ir: dict) -> None:
    for rule in ir.get("sandhi", ()):
        rule.pop("left_joined_spelling", None)
        rule.pop("right_joined_spelling", None)


def _mutate(ir: dict) -> None:
    for rule in (ir.get("allophony") or {}).get("rules", ()):
        rule.pop("mutate", None)
        rule.pop("mutate_at", None)


def _all(*fns: Callable) -> Callable:
    def run(ir):
        for fn in fns:
            fn(ir)
    return run


def _gates(ir: dict) -> None:
    for step in ir.get("dialect", ()):
        step["gate"] = ["not", step["gate"]]


def _first_candidate(ir: dict) -> None:
    for e in ir["entries"]:
        e["cands"], e["costs"] = e["cands"][:1], e["costs"][:1]


def _flat_costs(ir: dict) -> None:
    for e in ir["entries"]:
        e["costs"] = [0] * len(e["costs"])


def _no_trie(ir: dict) -> None:
    for e in ir["entries"]:
        e["trie"] = 0


def _runtime(ir: dict) -> dict:
    return {k: v for k, v in ir.items() if k in layout.LAYOUT[1]}


def _false_preds(t, v):
    if t == layout.PRED:
        return ["false"]
    if isinstance(t, tuple):
        if t[0] == "list":
            return [_false_preds(t[1], x) for x in v]
        if t[0] == "pair":
            return [_false_preds(t[1], v[0]), _false_preds(t[2], v[1])]
        if t[0] == "obj":
            return {k: _false_preds(t[1][k], x) for k, x in v.items()}
    return v


#: The ablation of each feature that is not a predicate node.
ABLATIONS: Dict[str, Callable[[dict], None]] = {
    "codepoint_map": _all(lambda ir: _clear(ir, "char_maps", "casefold"),
                          lambda ir: _clear(ir, "char_maps", "plain_lower")),
    "pattern": _all(lambda ir: _clear(ir, "rewrites"), lambda ir: _clear(ir, "sandhi"),
                    lambda ir: _steps(ir, "sub")),
    "trie": _no_trie,
    "bits": lambda ir: ir.update(chars={}),
    "predicate": lambda ir: ir.update(_false_preds(layout.LAYOUT, _runtime(ir))),
    "candidates": _first_candidate,
    "beam": _flat_costs,
    "splitter": _all(lambda ir: _clear(ir, "syllable", "diphthongs"),
                     lambda ir: _drop(ir, "syllable", "onsets")),
    "decision": _all(lambda ir: _clear(ir, "stress", "marked"), lambda ir: _clear(ir, "stress", "final"),
                     lambda ir: _clear(ir, "stress", "penult"), lambda ir: _clear(ir, "stress", "antepenult")),
    "sequencer": lambda ir: ir.pop("stress", None),
    "segment": _all(lambda ir: _clear(ir, "atoms", "mark"), lambda ir: _clear(ir, "atoms", "affricates"),
                    lambda ir: _clear(ir, "allophony", "atoms")),
    "word_has": lambda ir: ir.update(_negate(layout.LAYOUT, _runtime(ir), "node.word_has")),
    "spell_gate": _gates,
    "positional_rewrite": lambda ir: _steps(ir, "contextual"),
    "gated_map": lambda ir: _steps(ir, "chain"),
    "aligned_rewrite": lambda ir: _steps(ir, "lexical"),
    "allophony": lambda ir: ir.pop("allophony", None),
    "mark_placement": lambda ir: _clear(ir, "stress", "apply"),
    "sandhi": lambda ir: _clear(ir, "sandhi"),
    "sandhi_spelling": _sandhi_spelling,
    "sandhi_joined": _sandhi_joined,
    "sandhi_pause": _sandhi_pause,
    "rewrite": lambda ir: _clear(ir, "rewrites"),
    "endings": lambda ir: ir.pop("endings", None),
    "inherent": lambda ir: ir.pop("inherent", None),
    "written_onsets": lambda ir: _drop(ir, "syllable", "onsets"),
    "vowel_letters": lambda ir: _clear(ir, "syllable", "vowel_letters"),
    "secondary": lambda ir: _clear(ir, "stress", "alternating"),
    "aperture": lambda ir: _drop(ir, "syllable", "silent_tail"),
    "prefixes": lambda ir: _clear(ir, "stress", "prefixes"),
    "coda_liquid": lambda ir: _clear(ir, "stress", "coda_liquid"),
    "mutate": _mutate,
    "accent2": lambda ir: _drop(ir, "stress", "accent2"),
    "fold": lambda ir: _clear(ir, "char_maps", "fold"),
    "tone_dock": lambda ir: _drop(ir, "word", "tone_dock"),
    "iambic": lambda ir: _drop(ir, "stress", "iambic"),
    "prevocalic_backoff": lambda ir: _entry_bit(ir, "prevocalic_backoff"),
    "weight": lambda ir: _drop(ir, "stress", "weight"),
    "virama_final": lambda ir: _drop(ir, "word", "virama_final"),
    "vowel_signs": _all(lambda ir: _entry_bit(ir, "vowel_sign"), lambda ir: _drop(ir, "inherent", "signs")),
    "preposed": lambda ir: _entry_bit(ir, "preposed"),
    "ipa_count": lambda ir: _clear(ir, "stress", "ipa_count"),
    "consonant_nuclei": lambda ir: _clear(ir, "consonant_nuclei"),
    "computed_tone": lambda ir: ir.pop("tone", None),
    "hiatus": _all(lambda ir: _drop(ir, "syllable", "closed_hiatus"),
                   lambda ir: _drop(ir, "syllable", "final_diphthongs")),
    "allophone_map": lambda ir: ir.pop("allophone_map", None),
}
for _path, _name in layout.FIELD_SEMANTICS.items():
    if _name not in ABLATIONS:
        ABLATIONS[_name] = (lambda p: lambda ir: _clear(ir, *p))(_path)


def ablate(ir: dict, name: str) -> Optional[dict]:
    """A copy of the readable *ir* without feature *name*, or None when the IR does not hold it."""
    out = copy.deepcopy(ir)
    if name in ABLATIONS:
        ABLATIONS[name](out)
    else:
        out.update(_negate(layout.LAYOUT, _runtime(out), name))
    if json.dumps(out, sort_keys=True, ensure_ascii=False) == json.dumps(ir, sort_keys=True, ensure_ascii=False):
        return None
    return out
