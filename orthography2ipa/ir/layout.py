"""The layout of an IR v1 document, and its canonical JSON form.

The readable form holds Python strings. The canonical form (section 2.1 and
8.1 of docs/ir/o2i-ir-v1.md) holds every data string once, as a codepoint
array in ``strings``, sorted by codepoint order, and refers to it by index.
Both directions walk the same layout, so ``decode(encode(ir))`` gives the
runtime part back with the same JSON form: a tuple may come back as a list.
"""
import hashlib
import json
from typing import Callable, Dict, List

__all__ = ["encode", "decode", "canonical_bytes", "spec_revision", "SEMANTICS", "manifest"]

S, I, PAT, OPAQUE = "s", "i", "pat", "opaque"
SSET = "sset"
PRED, GATE, DPRED, TPL, ESET = "pred", "gate", "dpred", "tpl", "eset"


def L(t):
    return ("list", t)


def O(**fields):
    return ("obj", fields)


_RULE = O(phonemes=L(S), out=L(S), aware=L(I), when=PRED, slot_when=PRED,
          trig_next=I, trig_prev=I, mutate=S, mutate_at=I,
          seg=O(initial=I, final=I, prev=SSET, next=SSET))
_STEP = O(gate=GATE, kind=OPAQUE, find=S, rep=S, pattern=PAT, template=TPL, on=SSET, off=SSET,
          when_on=I, map=L(L(S)), rules=L(L(S)), when=DPRED)
LAYOUT = O(
    entries=L(O(key=S, cands=L(S), costs=L(I), bits=I, trie=I, onset=L(S),
                positional=L(("pair", PRED, L(S))))),
    fallback=SSET,
    word=O(exceptions=L(L(S)), internal_apostrophe=I, apostrophe_elision=I,
           collapse_geminates=I, context_beam=I, tone_dock=L(S), clitic_marks=SSET, silent_stress_marks=SSET,
           virama_final=S),
    beam=O(tilde=S),
    allophone_map=L(("pair", S, L(S))),
    syllable=O(diphthongs=L(S), onset_graphemes=SSET, semivowels=L(L(S)),
               closed_hiatus=O(pairs=L(S), onsets=L(S), codas=L(S), multi_keys=L(S)),
               final_diphthongs=O(diphthongs=L(S), finals=L(S)), vowel_letters=SSET, silent_tail=SSET,
               onsets=O(max=I, units=L(S), velar=SSET, table=L(L(S)))),
    stress=O(mark=S, secondary_mark=S, alternating=I, prefixes=L(S), schwa_rimes=SSET, coda_liquid=I, accent2=O(mark=S, finals=SSET), iambic=O(max_onset=I), marked=SSET, final=L(S), penult=L(S), antepenult=L(S),
             default=I, cliticless=SSET, compound_last=I, mark_diphthongs=L(S),
             tonic_after_diphthong=L(S), stand_in=S, apply=I, contact_units=L(S),
             silent_units=SSET, ipa_diphthongs=L(S), ipa_count=I,
             mark_onsets=O(max=I, velar=S, table=L(L(S))),
             weight=O(max_onset=I, superheavy_final=I)),
    atoms=O(mark=L(S), affricates=L(S)),
    allophony=O(passes=I, atoms=L(S), geminate=I, rules=L(_RULE)),
    sandhi=L(O(left=PAT, right=PAT, obligatory=I, left_out=TPL, right_out=TPL)),
    dialect=L(_STEP),
    char_maps=O(casefold=L(("pair", I, S)), plain_lower=L(("pair", I, S)), nfd=L(("pair", I, S)),
                ccc=L(L(I)), compose=L(L(I)), presentation=L(("pair", I, S)), fold=SSET),
    rewrites=L(O(pattern=PAT, template=TPL)),
    consonant_nuclei=L(("pair", S, S)),
    tone=O(classes=L(("pair", S, S)), marks=L(("pair", S, S)), no_mark=S, dead_codas=L(S),
           table=L(L(S)), atoms=L(S)),
    inherent=O(vowel=S, final=S, coda_no=I, signs=L(("pair", S, I))),
    endings=O(table=L(O(key=S, ipa=S, alts=L(S), costs=L(I))), suffix=SSET,
              vowels=L(O(key=S, reduced=SSET, readings=SSET)),
              sources=L(O(surface=S, vowels=SSET))),
)
RUNTIME_FIELDS = tuple(LAYOUT[1]) + ("chars",)

# The semantics version of every primitive and predicate node (section 8.1).
SEMANTICS = {
    "codepoint_map": 1, "pattern": 1, "trie": 1, "bits": 1, "predicate": 1, "candidates": 1,
    "beam": 1, "splitter": 1, "decision": 1, "sequencer": 1, "segment": 1, "word_has": 1,
    "spell_gate": 1, "positional_rewrite": 1, "gated_map": 1, "aligned_rewrite": 1,
    "allophony": 1, "mark_placement": 1, "sandhi": 1, "rewrite": 1, "endings": 1, "inherent": 1, "written_onsets": 1, "vowel_letters": 1, "secondary": 1, "aperture": 1, "prefixes": 1, "coda_liquid": 1, "mutate": 1, "accent2": 1, "fold": 1, "tone_dock": 1, "iambic": 1, "prevocalic_backoff": 1,
    "weight": 1, "virama_final": 1, "vowel_signs": 1, "preposed": 1, "ipa_count": 1, "consonant_nuclei": 1, "computed_tone": 1,
    "internal_apostrophe": 1, "apostrophe_elision": 1, "collapse_geminates": 1, "context_beam": 1,
    "clitic_marks": 1, "silent_stress_marks": 1, "overrides": 1, "allophone_map": 1, "hiatus": 1,
    "semivowels": 1, "cliticless": 1, "compound_last": 1, "tonic_after_diphthong": 1,
    "ipa_diphthongs": 1, "mark_onsets": 1, "allophony_geminate": 1,
    "node.and": 1, "node.or": 1, "node.not": 1, "node.true": 1, "node.false": 1,
    "node.exists": 1, "node.ebit": 1, "node.entry_in": 1, "node.top_in": 1,
    "node.top_seg_in": 1, "node.syll": 1, "node.word_in": 1, "node.word_has": 1,
    "node.syllpos": 1, "node.word_final": 1, "node.count": 1, "node.word_has_entry": 1, "node.reading_vowel": 1,
    "syll.has_stress": 1, "syll.idx_eq_stressed": 1, "syll.idx_lt_stressed": 1,
    "syll.idx_gt_stressed": 1, "syll.idx_eq_stressed_minus_1": 1, "syll.idx_in_secondary": 1,
    "syll.open": 1, "syll.closed": 1, "node.top_nucleus": 1,
}

_SLOT_ARGS: Dict[str, tuple] = {
    "and": "preds", "or": "preds", "not": (PRED,), "true": (), "false": (),
    "exists": (I,), "ebit": (I, I), "entry_in": (I, ESET), "top_in": (I, SSET),
    "top_seg_in": (I, I, SSET), "syll": (OPAQUE,), "word_in": (SSET,), "word_has": (SSET,),
    "syllpos": (I, OPAQUE), "word_final": (),
    "count": (OPAQUE, OPAQUE, PRED, I, OPAQUE), "word_has_entry": (ESET,), "reading_vowel": (I,), "top_nucleus": (OPAQUE,),
}
_GATE_ARGS = {"and": "preds", "or": "preds", "not": (GATE,), "true": (),
              "spell_search": (PAT,), "spell_empty": ()}
_DPRED_ARGS = {"and": "preds", "or": "preds", "not": (DPRED,), "true": (),
               "back_reach": (SSET, SSET), "at_in": (I, SSET), "at_end_or_in": (SSET,),
               "ahead_match": (I, PAT), "covered_by": (SSET,), "later_has": (SSET,),
               "spell": (GATE,)}
_PRED_TABLES = {PRED: _SLOT_ARGS, GATE: _GATE_ARGS, DPRED: _DPRED_ARGS}


def _walk(t, v, fs: Callable, fe: Callable, sort_sets: bool):
    """Map every data string of *v* (layout *t*) through *fs*, entry keys
    through *fe*."""
    if t == S:
        return fs(v)
    if t == SSET:
        out = [fs(x) for x in v]
        return sorted(out) if sort_sets else out
    if t == ESET:
        out = [fe(x) for x in v]
        return sorted(out) if sort_sets else out
    if t in (I, PAT, OPAQUE):
        return v
    if t == TPL:
        return [[p[0], fs(p[1])] if p[0] == "lit" else list(p) for p in v]
    if isinstance(t, str) and t in _PRED_TABLES:
        table = _PRED_TABLES[t]
        op = v[0]
        args = table[op]
        if args == "preds":
            return [op, *(_walk(t, x, fs, fe, sort_sets) for x in v[1:])]
        return [op, *(_walk(a, x, fs, fe, sort_sets) for a, x in zip(args, v[1:]))]
    kind = t[0]
    if kind == "list":
        return [_walk(t[1], x, fs, fe, sort_sets) for x in v]
    if kind == "pair":
        return [_walk(t[1], v[0], fs, fe, sort_sets), _walk(t[2], v[1], fs, fe, sort_sets)]
    if kind == "obj":
        return {k: _walk(t[1][k], x, fs, fe, sort_sets) for k, x in v.items()}
    raise TypeError(t)


def _normal(p: list, table) -> list:
    """The predicate normal form of section 8.1."""
    op = p[0]
    args = table[op]
    if args == "preds":
        kids = []
        for q in (_normal(x, table) for x in p[1:]):
            kids += q[1:] if q[0] == op else [q]
        if op == "and":
            kids = [q for q in kids if q != ["true"]]
        uniq = {json.dumps(q, sort_keys=True, ensure_ascii=False): q for q in kids}
        kids = [uniq[k] for k in sorted(uniq)]
        if len(kids) == 1:
            return kids[0]
        return [op, *kids] if kids else ["true"]
    if op == "not":
        inner = _normal(p[1], table)
        return inner[1] if inner[0] == "not" else ["not", inner]
    return [op, *(_normal(x, _PRED_TABLES[a]) if isinstance(a, str) and a in _PRED_TABLES else x
                  for a, x in zip(args, p[1:]))]


def _normalise_preds(t, v):
    if isinstance(t, str) and t in _PRED_TABLES:
        return _normal(v, _PRED_TABLES[t])
    if isinstance(t, tuple):
        if t[0] == "list":
            return [_normalise_preds(t[1], x) for x in v]
        if t[0] == "pair":
            return [_normalise_preds(t[1], v[0]), _normalise_preds(t[2], v[1])]
        if t[0] == "obj":
            return {k: _normalise_preds(t[1][k], x) for k, x in v.items()}
    return v


def _cps(s: str) -> List[int]:
    return [ord(c) for c in s]


def _ranges(chars: Dict[int, int]) -> List[List[int]]:
    out: List[List[int]] = []
    for cp in sorted(chars):
        bits = chars[cp]
        if out and out[-1][1] == cp - 1 and out[-1][2] == bits:
            out[-1][1] = cp
        else:
            out.append([cp, cp, bits])
    return out


def encode(ir: dict) -> dict:
    """The canonical JSON-ready form of a readable IR."""
    runtime = {k: v for k, v in ir.items() if k in LAYOUT[1]}
    runtime = _normalise_preds(LAYOUT, runtime)
    seen = {""}
    _walk(LAYOUT, runtime, lambda s: seen.add(s), lambda e: None, False)
    strings = sorted(seen, key=_cps)
    index = {s: i for i, s in enumerate(strings)}
    entry_index = {e["key"]: i for i, e in enumerate(ir.get("entries", ()))}
    body = _walk(LAYOUT, runtime, index.__getitem__, entry_index.__getitem__, True)
    doc = {"ir_version": ir["ir_version"], "lang": ir["lang"], "source": ir.get("source", {}),
           "strings": [_cps(s) for s in strings],
           "chars": {"ranges": _ranges(ir["chars"])}}
    doc.update(body)
    doc["primitives"] = dict(item.split("=") for item in manifest(ir).split(";"))
    doc["primitives"] = {k: int(v) for k, v in doc["primitives"].items()}
    doc["bits"] = ir.get("bits", {})
    doc["debug"] = ir.get("debug", {})
    return doc


def decode(doc: dict) -> dict:
    """The readable form of a canonical IR document."""
    strings = ["".join(map(chr, s)) for s in doc["strings"]]
    keys = [strings[e["key"]] for e in doc.get("entries", ())]
    body = {k: v for k, v in doc.items() if k in LAYOUT[1]}
    ir = _walk(LAYOUT, body, strings.__getitem__, keys.__getitem__, False)
    chars = {}
    for lo, hi, bits in doc["chars"]["ranges"]:
        for cp in range(lo, hi + 1):
            chars[cp] = bits
    ir.update(ir_version=doc["ir_version"], lang=doc["lang"], source=doc.get("source", {}),
              chars=chars, bits=doc.get("bits", {}), debug=doc.get("debug", {}))
    return ir


def canonical_bytes(doc: dict) -> bytes:
    runtime = {k: v for k, v in doc.items()
               if k not in ("source", "debug", "ir_version", "primitives")}
    return json.dumps(runtime, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def _ops(t, v, out: set) -> None:
    if isinstance(t, str) and t in _PRED_TABLES:
        if t == PRED:
            out.add("node." + v[0])
            if v[0] == "syll":
                out.add("syll." + v[1])
        table = _PRED_TABLES[t]
        args = table[v[0]]
        if args == "preds":
            for x in v[1:]:
                _ops(t, x, out)
        else:
            for a, x in zip(args, v[1:]):
                _ops(a, x, out)
    elif isinstance(t, tuple):
        if t[0] == "list":
            for x in v:
                _ops(t[1], x, out)
        elif t[0] == "pair":
            _ops(t[1], v[0], out)
            _ops(t[2], v[1], out)
        elif t[0] == "obj":
            for k, x in v.items():
                _ops(t[1][k], x, out)


#: Optional fields that change output, and the semantics version each one adds when it is set.
FIELD_SEMANTICS = {
    ("word", "internal_apostrophe"): "internal_apostrophe",
    ("word", "apostrophe_elision"): "apostrophe_elision",
    ("word", "collapse_geminates"): "collapse_geminates",
    ("word", "context_beam"): "context_beam",
    ("word", "clitic_marks"): "clitic_marks",
    ("word", "silent_stress_marks"): "silent_stress_marks",
    ("word", "exceptions"): "overrides",
    ("allophone_map",): "allophone_map",
    ("syllable", "closed_hiatus"): "hiatus",
    ("syllable", "final_diphthongs"): "hiatus",
    ("syllable", "semivowels"): "semivowels",
    ("stress", "cliticless"): "cliticless",
    ("stress", "compound_last"): "compound_last",
    ("stress", "tonic_after_diphthong"): "tonic_after_diphthong",
    ("stress", "ipa_diphthongs"): "ipa_diphthongs",
    ("stress", "mark_onsets"): "mark_onsets",
    ("allophony", "geminate"): "allophony_geminate",
}


def manifest(ir: dict) -> str:
    """``name=version`` of every primitive and node the IR uses, sorted."""
    used = {"codepoint_map", "trie", "bits", "predicate", "candidates", "beam", "sequencer",
            "segment", "splitter"}
    if ir.get("stress"):
        used |= {"decision", "mark_placement"}
        if ir["stress"].get("alternating"):
            used.add("secondary")
        if ir["stress"].get("iambic"):
            used.add("iambic")
        if ir["stress"].get("accent2"):
            used.add("accent2")
        if ir["stress"].get("coda_liquid"):
            used.add("coda_liquid")
        if ir["stress"].get("prefixes"):
            used.add("prefixes")
        if ir["stress"].get("weight"):
            used.add("weight")
        if ir["stress"].get("ipa_count"):
            used.add("ipa_count")
    syllable = ir.get("syllable", {})
    if syllable.get("onsets"):
        used.add("written_onsets")
    if "silent_tail" in syllable:
        used.add("aperture")
    if syllable.get("vowel_letters"):
        used.add("vowel_letters")
    if ir.get("allophony"):
        used.add("allophony")
        if any("mutate" in r for r in ir["allophony"]["rules"]):
            used.add("mutate")
    if ir.get("sandhi"):
        used |= {"sandhi", "pattern"}
    if ir.get("char_maps", {}).get("fold"):
        used.add("fold")
    if "tone_dock" in ir.get("word", {}):
        used.add("tone_dock")
    entry_bits = ir.get("bits", {}).get("entry", [])
    if "prevocalic_backoff" in entry_bits:
        mask = 1 << entry_bits.index("prevocalic_backoff")
        if any(e["bits"] & mask for e in ir.get("entries", ())):
            used.add("prevocalic_backoff")
    if ir.get("rewrites"):
        used |= {"rewrite", "pattern"}
    if ir.get("endings"):
        used.add("endings")
    if ir.get("inherent"):
        used.add("inherent")
    vowel_sign = 1 << ir["bits"]["entry"].index("vowel_sign")
    if "signs" in ir.get("inherent", {}) or any(e["bits"] & vowel_sign for e in ir["entries"]):
        used.add("vowel_signs")
    if any(e["bits"] & 1 << ir["bits"]["entry"].index("preposed") for e in ir["entries"]):
        used.add("preposed")
    if ir.get("tone"):
        used.add("computed_tone")
    if ir.get("consonant_nuclei"):
        used.add("consonant_nuclei")
    if "virama_final" in ir["word"]:
        used.add("virama_final")
    for step in ir.get("dialect", ()):
        used |= {"spell_gate", {"replace": "pattern", "sub": "pattern",
                                "contextual": "positional_rewrite", "chain": "gated_map",
                                "lexical": "aligned_rewrite"}[step["kind"]]}
    for path, name in FIELD_SEMANTICS.items():
        value = ir
        for key in path:
            value = value.get(key) if isinstance(value, dict) else None
        if value:
            used.add(name)
    nodes: set = set()
    runtime = {k: v for k, v in ir.items() if k in LAYOUT[1]}
    _ops(LAYOUT, runtime, nodes)
    if "node.word_has" in nodes:
        used.add("word_has")
    used |= nodes
    return ";".join(sorted(f"{name}={SEMANTICS[name]}" for name in used))


def spec_revision(ir: dict) -> str:
    """``spec_revision`` of section 8.1 for a readable IR."""
    doc = encode(ir)
    payload = b"o2i-ir\n" + manifest(ir).encode() + b"\n" + canonical_bytes(doc)
    return "sha256:" + hashlib.sha256(payload).hexdigest()
