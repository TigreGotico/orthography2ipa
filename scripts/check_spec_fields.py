"""Every LanguageSpec field is lowered, refused or declared inert.

The check walks LanguageSpec and every dataclass nested in it. For each
field it compiles a small spec with that field set to a non-default value.
The field passes when the IR changes, when the compiler raises
IRUnsupportedFeature naming the field, or when the field is in INERT with
a reason. A field that is none of these fails, because the compiler would
drop its behaviour without an error.

Run: python -I scripts/check_spec_fields.py
"""
import dataclasses
import enum
import sys
import typing
from typing import Any, Dict, Iterator, List, Optional, Tuple

from orthography2ipa import registry
from orthography2ipa.ir.compiler import IRUnsupportedFeature, build_ir
from orthography2ipa.types import LanguageSpec

# Specs to probe, cheapest first. Together they set stress, closed hiatus,
# final diphthongs, allophony, sandhi, tone, an inherent vowel and endings.
BASES = ("th", "hi", "nrf", "es-CR", "pt-PT")

# IR members that carry no behaviour: provenance and debug output. The
# alphabet tables are left out too: a probe value with a new letter grows
# them even when the compiler drops the field itself.
IGNORED_IR_KEYS = ("source", "debug", "chars", "char_maps", "fallback")

# Fields that hold no G2P behaviour. Key: "Class.field".
INERT: Dict[str, str] = {
    "LanguageSpec.name": "display name",
    "LanguageSpec.family": "classification metadata",
    "LanguageSpec.family_path": "classification metadata",
    "LanguageSpec.clade": "marks a grouping node in the registry",
    "LanguageSpec.inherits": "inheritance is resolved before the compiler runs",
    "LanguageSpec.ancestors": "read by the distance metric, not by G2P",
    "LanguageSpec.orthography_kind": "classification metadata",
    "LanguageSpec.glottolog_code": "external identifier",
    "LanguageSpec.iso639_3": "external identifier",
    "LanguageSpec.wikidata_qid": "external identifier",
    "LanguageSpec.phoible_id": "external identifier",
    "LanguageSpec.wals_code": "external identifier",
    "LanguageSpec.notes": "prose",
    "LanguageSpec.quality": "quality tier for reports",
    "LanguageSpec.sources": "citations",
    "LanguageSpec.wikipedia": "citations",
    "LanguageSpec.urls": "citations",
    "LanguageSpec.orthography_standard": "citation of the written norm",
    "LanguageSpec.location": "map metadata",
    "LanguageSpec.timespan": "map metadata",
    "LanguageSpec.valid_ceiling": "benchmark metadata",
    "LanguageSpec.audit": "benchmark metadata",
    "LanguageSpec.tone_inventory": "read by the distance metric and the CLI, not by G2P",
    "LanguageSpec.optional_marks": "read by the underspecification analysis API, not by G2P",
    "StressRules.notes": "prose",
    "ToneRules.notes": "prose",
    "SandhiRule.id": "rule label",
    "SandhiRule.name": "rule label",
    "SandhiRule.notes": "prose",
    "AllophoneRule.id": "rule label",
    "AllophoneRule.notes": "prose",
}

# Probe hints. A field that takes a closed vocabulary gets valid values, and a
# field the compiler reads only inside a feature gets the setting that turns
# the feature on. A hint is not a waiver: the IR must still change.
HINTS: Dict[str, Dict[str, Any]] = {
    # A script name adds behaviour only where it adds rewrites; elsewhere it
    # only grows the alphabet.
    "LanguageSpec.script": {"values": ("Gurmukhi", "Arabic")},
    "AllophoneRule.stress": {"values": ("stressed", "unstressed", "pretonic", "posttonic")},
    "AllophoneRule.syllable_position": {"values": ("onset", "coda")},
    "AllophoneRule.preceded_by": {"values": ("vowel", "consonant", "word_boundary")},
    "AllophoneRule.followed_by": {"values": ("vowel", "consonant", "word_boundary")},
    "AllophoneRule.preceded_by_2": {"values": ("vowel", "consonant")},
    "AllophoneRule.followed_by_2": {"values": ("vowel", "consonant")},
    "AllophoneRule.preceded_by_3": {"values": ("vowel", "consonant")},
    "AllophoneRule.followed_by_3": {"values": ("vowel", "consonant")},
    "AllophoneRule.append": {"values": ("ʰ", "ː"), "context": {"surface": ""}},
    "AllophoneRule.mutates_neighbor": {"values": ("ʔ", "x"),
                                       "context": {"mutates_neighbor": "ʔ",
                                                   "mutates_neighbor_side": "following"}},
    "AllophoneRule.mutates_neighbor_side": {"values": ("preceding", "following"),
                                            "context": {"mutates_neighbor": "ʔ",
                                                        "mutates_neighbor_side": "following"}},
    "StressRules.superheavy_final_attracts": {"context": {"quantity_sensitive": True}},
    "StressRules.max_onset": {"context": {"quantity_sensitive": True}},
    "StressRules.accent2_final_letters": {"context": {"accent2_mark": "ˋ"}},
    "LanguageSpec.grapheme_weights": {"values": "weights"},
}

_SEED_STRS = ("a", "e", "i", "n", "k", "ka", "ə", "-", "alternating", "last", "plugin", "none")


def _hints(cls) -> Dict[str, Any]:
    return typing.get_type_hints(cls)


def _unwrap(tp):
    args = typing.get_args(tp)
    if typing.get_origin(tp) is typing.Union and type(None) in args:
        return next(a for a in args if a is not type(None))
    return tp


def _seeds(tp) -> Iterator[Any]:
    """Non-default values of type *tp*, for a field that is None or empty."""
    tp = _unwrap(tp)
    origin = typing.get_origin(tp) or tp
    args = typing.get_args(tp)
    if tp is bool:
        yield True
    elif tp is int:
        yield from (1, 2)
    elif tp is float:
        yield 0.5
    elif tp is str:
        yield from _SEED_STRS
    elif isinstance(tp, type) and issubclass(tp, enum.Enum):
        yield from tp
    elif dataclasses.is_dataclass(tp):
        try:
            yield tp()
        except TypeError:
            return
    elif origin in (tuple, list):
        elem = args[0] if args else str
        for v in _seeds(elem):
            yield (v,) if origin is tuple else [v]
    elif origin in (dict, typing.Mapping) or str(origin).endswith("Mapping"):
        key_tp, val_tp = args if args else (str, str)
        for k in _seeds(key_tp):
            for v in list(_seeds(val_tp))[:2]:
                yield {k: v}


def _spec_seeds(spec: LanguageSpec, tp) -> Iterator[Any]:
    """Values built from the spec's own graphemes, for an empty string tuple."""
    tp = _unwrap(tp)
    if typing.get_origin(tp) is tuple and typing.get_args(tp)[:1] == (str,):
        keys = sorted(k for k in spec.graphemes if k)
        for k in [k for k in keys if len(k) > 1][:4] + keys[:4]:
            yield (k,)


def _weights(spec: LanguageSpec) -> Iterator[Any]:
    for key, readings in spec.graphemes.items():
        if len(readings) > 1:
            yield {**(spec.grapheme_weights or {}), key: [1.0] + [3.0] * (len(readings) - 1)}
            return


def _variants(value, tp, spec: LanguageSpec, key: str) -> Iterator[Any]:
    """Values that differ from *value*, of the field type *tp*."""
    hint = HINTS.get(key, {}).get("values")
    if hint == "weights":
        yield from _weights(spec)
    elif hint:
        yield from (v for v in hint if v != value)
    if isinstance(value, tuple) and not value:
        yield from _spec_seeds(spec, tp)
    if value is None:
        yield from _seeds(tp)
        return
    if isinstance(value, bool):
        yield not value
    elif isinstance(value, enum.Enum):
        yield from (m for m in type(value) if m != value)
    elif isinstance(value, int):
        yield from (value + 1, value - 1)
    elif isinstance(value, float):
        yield value + 0.25
    elif isinstance(value, str):
        yield from (s for s in (value + "a", *_SEED_STRS) if s != value)
    elif isinstance(value, (tuple, list)):
        if value:
            yield value[1:]
            yield type(value)(reversed(value))
            if isinstance(value[0], str):
                yield type(value)((*value, value[0] + "a"))
        else:
            yield from _seeds(tp)
    elif isinstance(value, dict):
        if value:
            keys = list(value)
            yield {k: v for k, v in value.items() if k != keys[0]}
            if len(keys) > 1:
                yield {**value, keys[0]: value[keys[1]]}
            first = value[keys[0]]
            if isinstance(first, str):
                yield {**value, keys[0]: first + "a"}
            yield {**value, "zq": first}
        else:
            yield from _seeds(tp)
    if not dataclasses.is_dataclass(value) and _unwrap(tp) is not tp:
        yield None


def _instances(spec: LanguageSpec, cls) -> Iterator[Tuple[tuple, Any]]:
    """(path, instance) of each *cls* object in *spec*, at most two per list."""
    if cls is LanguageSpec:
        yield (), spec
        return
    for f in dataclasses.fields(spec):
        value = getattr(spec, f.name)
        if isinstance(value, cls):
            yield (f.name,), value
        elif isinstance(value, tuple) and value and isinstance(value[0], cls):
            for i, item in enumerate(value[:2]):
                yield (f.name, i), item
        elif dataclasses.is_dataclass(value):
            for sub in dataclasses.fields(value):
                inner = getattr(value, sub.name)
                if isinstance(inner, cls):
                    yield (f.name, sub.name), inner
    # A nested dataclass the base leaves unset is probed from its defaults.
    for parent, f in _owners(cls):
        if parent is LanguageSpec and getattr(spec, f) is None:
            seed = next(_seeds(cls), None)
            if seed is not None:
                yield (f,), seed
        elif parent is not LanguageSpec:
            for path, holder in _instances(spec, parent):
                if path and getattr(holder, f) is None:
                    seed = next(_seeds(cls), None)
                    if seed is not None:
                        yield (*path, f), seed


def _owners(cls) -> List[Tuple[type, str]]:
    out = []
    for parent in _classes():
        for name, tp in _hints(parent).items():
            if _unwrap(tp) is cls:
                out.append((parent, name))
    return out


def _with(obj, path: tuple, new):
    if not path:
        return new
    if obj is None:
        raise LookupError("the path runs through an unset field")
    head, rest = path[0], path[1:]
    if isinstance(head, int):
        items = list(obj)
        items[head] = _with(items[head], rest, new)
        return tuple(items)
    return dataclasses.replace(obj, **{head: _with(getattr(obj, head), rest, new)})


_ROOT = [LanguageSpec]


def _classes() -> List[type]:
    """LanguageSpec and every dataclass reachable from a non-inert field."""
    seen: List[type] = []
    todo = list(_ROOT)
    while todo:
        cls = todo.pop(0)
        if cls in seen:
            continue
        seen.append(cls)
        for name, tp in _hints(cls).items():
            if f"{cls.__name__}.{name}" in INERT:
                continue
            stack = [tp]
            while stack:
                t = stack.pop()
                if dataclasses.is_dataclass(t) and isinstance(t, type):
                    todo.append(t)
                stack.extend(a for a in typing.get_args(t) if not isinstance(a, str))
    return seen


def _ir(spec: LanguageSpec) -> dict:
    ir = build_ir(spec.code, spec=spec, expand_allophones=True)
    return {k: v for k, v in ir.items() if k not in IGNORED_IR_KEYS}


def probe(cls, name: str, bases: Dict[str, LanguageSpec], budget: Optional[int] = None) -> str:
    """'lowered', 'refused' or 'inert' for the field *cls.name*."""
    tp = _hints(cls)[name]
    key = f"{cls.__name__}.{name}"
    context = HINTS.get(key, {}).get("context", {})
    tries = 0
    for spec in bases.values():
        for path, inst in _instances(spec, cls):
            try:
                inst = dataclasses.replace(inst, **context)
                start = _with(spec, path, inst) if path else spec
                before = _ir(start)
            except (IRUnsupportedFeature, LookupError, ValueError):
                continue
            for value in _variants(getattr(inst, name), tp, spec, key):
                tries += 1
                try:
                    after = _ir(_with(start, path, dataclasses.replace(inst, **{name: value})))
                except IRUnsupportedFeature as exc:
                    if name in exc.feature:
                        return "refused"
                    continue
                except Exception:  # an invalid probe value; try the next one
                    continue
                if after != before:
                    return "lowered"
                if budget is not None and tries >= budget:
                    return "inert"
    return "inert"


def check(root=LanguageSpec, bases: Tuple[str, ...] = BASES) -> List[str]:
    """The failures: one line per field that is neither read, refused nor declared."""
    _ROOT[:] = [root]
    specs = {c: registry.get(registry.resolve(c)) for c in bases}
    if root is not LanguageSpec:
        specs = {c: root(**{f.name: getattr(s, f.name) for f in dataclasses.fields(s)})
                 for c, s in specs.items()}
    known = set()
    failures = []
    counts = {"lowered": 0, "refused": 0, "inert": 0, "declared": 0}
    for cls in _classes():
        for f in dataclasses.fields(cls):
            key = f"{cls.__name__}.{f.name}"
            known.add(key)
            if key in INERT:
                # A cheap check that a declared field is still inert.
                cheap = dict(list(specs.items())[:1])
                if probe(cls, f.name, cheap, budget=3) == "lowered":
                    failures.append(f"{key}: declared inert, but the IR changes with it")
                counts["declared"] += 1
                continue
            status = probe(cls, f.name, specs)
            print(f"{status:8} {key}")
            counts[status] += 1
            if status == "inert":
                failures.append(f"{key}: the compiler ignores it; lower it, refuse it by name, "
                                "or declare it in INERT")
    print(f"{len(known)} fields in {len(_classes())} classes: "
          + ", ".join(f"{n} {k}" for k, n in counts.items()))
    if sum(counts.values()) != len(known):
        failures.append(f"probed {sum(counts.values())} of {len(known)} fields")
    for key in sorted(set(INERT) - known):
        failures.append(f"{key}: in INERT, but no such field")
    return failures


def main() -> int:
    failures = check()
    for line in failures:
        print("FAIL", line)
    print(f"{len(failures)} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
