"""Outputs of the rules engine that the compiled IR replaced.

The rules engine read the spec directly, with no compiler between, so its
outputs are a check on compile + interpret that does not come from the code
under test. ``tests/data/rules_outputs.json`` holds them, recorded from the
last commit that had the rules engine with ``O2I_RECORD_RULES`` set to that
path. A key names the scope (the test, by default), the language, the
engine method and its arguments; a key called more than once in one scope
keeps its values in call order.
"""
import json
import os
from dataclasses import fields, is_dataclass
from enum import Enum
from pathlib import Path

from orthography2ipa import G2P
from orthography2ipa.features import GraphemeFeatures, WordFeatures
from orthography2ipa.g2p import ConfidenceBreakdown, TranscriptionResult, WordTranscription
from orthography2ipa.phonetok import Candidate, IPAPath, SegmentSlot
from orthography2ipa.sentence import Position, SentenceLattice, WordSlot

PATH = Path(__file__).parent / "data" / "rules_outputs.json"
_TYPES = {cls.__name__: cls for cls in (
    TranscriptionResult, WordTranscription, ConfidenceBreakdown, IPAPath, SegmentSlot,
    Candidate, SentenceLattice, WordSlot, WordFeatures, GraphemeFeatures, Position)}
_RECORD = os.environ.get("O2I_RECORD_RULES")
_store = json.loads(Path(_RECORD or PATH).read_text(encoding="utf-8")) \
    if Path(_RECORD or PATH).is_file() else {}
_calls: dict = {}


def _encode(value):
    if isinstance(value, Enum):
        return {"enum": type(value).__name__, "name": value.name}
    if is_dataclass(value):
        return {"type": type(value).__name__,
                "fields": {f.name: _encode(getattr(value, f.name)) for f in fields(value) if f.init}}
    if isinstance(value, tuple):
        return {"tuple": [_encode(v) for v in value]}
    if isinstance(value, list):
        return [_encode(v) for v in value]
    if isinstance(value, frozenset):
        return {"frozenset": sorted(_encode(v) for v in value)}
    if isinstance(value, dict):
        return {"dict": [[_encode(k), _encode(v)] for k, v in value.items()]}
    return value


def _decode(value):
    if isinstance(value, list):
        return [_decode(v) for v in value]
    if not isinstance(value, dict):
        return value
    if "enum" in value:
        return _TYPES[value["enum"]][value["name"]]
    if "type" in value:
        return _TYPES[value["type"]](**{k: _decode(v) for k, v in value["fields"].items()})
    if "tuple" in value:
        return tuple(_decode(v) for v in value["tuple"])
    if "frozenset" in value:
        return frozenset(_decode(v) for v in value["frozenset"])
    return {_decode(k): _decode(v) for k, v in value["dict"]}


class FrozenRules:
    """Stands in for ``G2P(code, **options)`` on the rules engine."""

    def __init__(self, code, scope=None, **options):
        self.code = code
        self.scope = scope or os.environ["PYTEST_CURRENT_TEST"].rsplit(" ", 1)[0]
        self.options = options

    def __getattr__(self, method):
        def call(*args, **kwargs):
            key = json.dumps([self.scope, self.code, method, repr(args), repr(sorted(kwargs.items()))],
                             ensure_ascii=False)
            n = _calls[key] = _calls.get(key, -1) + 1
            if _RECORD:
                engine = G2P(self.code, **self.options)
                engine.__dict__["_interpreter"] = None
                value = getattr(engine, method)(*args, **kwargs)
                values = _store.setdefault(key, [])
                del values[n:]
                values.append(_encode(value))
                Path(_RECORD).write_text("{\n" + ",\n".join(
                    json.dumps(k, ensure_ascii=False) + ":" + json.dumps(v, ensure_ascii=False, separators=(",", ":"))
                    for k, v in sorted(_store.items())) + "\n}\n", encoding="utf-8")
                return value
            return _decode(_store[key][n])
        return call
