# Engine changes

The engine is the Python code in `orthography2ipa/`. It knows no language.
The data in `orthography2ipa/data/` holds every fact about a language. This
page gives the rules for a change to the engine and the review gate that
every such change passes. The module map is in
[architecture.md](../architecture.md).

## The engine is language-agnostic

No language name, script name or language code may drive a branch in
`orthography2ipa/*.py`. A spec may not carry logic either. If a language
needs a behaviour that the engine cannot express, add a generic capability,
such as a context class or a rule field. Then use it from the data.
Never special-case the language in code, and never fake the capability by
enumerating data.

A closed set in engine code is allowed only when it is a cross-linguistic
class with a citation at the constant. The transparent-suffix graphemes are
an example.

## Accuracy outranks the score

A benchmark number is evidence, never a justification. If an enumeration, a
hack or a special case improves a score, it is still wrong, and it is still
removed. The score is allowed to drop. Removing a violation changes output,
and that change is the violation being undone. Ask "is this how the language
works?" and "can the architecture express it?". Do not ask whether the change
lowers PER.

## Add a capability

1. Add the capability as a language-neutral predicate or rule field, such as
   a `followed_by` class in `vowels.py` or `allophony.py`.
2. Add the field in four places: the dataclass and its docstring in
   `types.py`, the validation in `schema.py`, the parse in `json_loader.py`
   and the user documentation in
   [`SCHEMA.md`](../../orthography2ipa/data/SCHEMA.md).
3. Adopt the field in the specs that needed it. Delete the enumeration that
   stood in for it.
4. Add engine tests, and add a case to the family test file of each spec
   that adopts the field.

`json_loader.py` builds each rule from an explicit key list. A field absent
from that list is dropped when the spec loads, and the rule then matches on
its other conditions alone. Nothing warns. The tests in
`tests/test_allophone_rules.py::TestOffsetContext` pin the offset fields for
this reason. `tests/test_schema_documents_loader_keys.py` fails when the
loader reads a key that `SCHEMA.md` does not name.

## Plugins are steps, not engines

The pipeline has five steps that a package can replace: `normalize`,
`syllabify`, `stress`, `rescore` and `sandhi`. A syllabifier must reach the
same transcription by better means, and the conformance kit fails it if the
output moves. The other four steps change the output. So a spec or a caller
must name such a plugin by its entry-point name, through the spec's
`plugins` field or `G2P(code, plugins=...)`. A named plugin that is not
installed raises `MissingPlugin`. `orthography2ipa/plugins.py` states the
contract.

A downstream engine such as arbtok or tugaphone is built on this library,
not plugged into it. It refines the shared lattice with a `LatticeRescorer`
or keeps its own tokenizer. [lattice.md](../lattice.md) covers the choice.

## The review gate for engine code

Every pull request that touches `orthography2ipa/*.py` answers to these
points before it merges. A review that skips them is incomplete.

1. One concept, one place. A new rule condition is one field, checked in one
   place in the match loop, and documented in one docstring. If a behaviour
   needs two cooperating helper predicates, merge them into one named
   function with one documented contract first.
2. Additions mirror an existing pattern. A positive condition mirrors its
   negative twin (`followed_by_grapheme` and `followed_by_grapheme_not`). A
   new stress value extends the existing conditional. A new shape of code is
   an architecture change: name it in the pull request and justify it.
3. No language names in engine code.
4. Flat beats clever. The match loop is a flat sequence of independent
   condition checks. Keep it so: no nested dispatch, no metaprogramming, and
   no condition that reads another condition's result.
5. A new field lands in the four places listed above, or it does not land.
6. Leave it cleaner. If the diff touches a function that already has a smell,
   such as three cooperating predicates, a boolean parameter that flips the
   meaning, or a conditional longer than 20 lines, clean it or name the smell
   in the pull request.

No linter or type checker is configured. The code uses
`from __future__ import annotations` and typed dataclasses.

---
[← Board regeneration](board.md) · [Home](../index.md) · [Benchmarks →](../benchmarks.md)
