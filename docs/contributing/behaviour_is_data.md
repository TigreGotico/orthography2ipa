# Behaviour is data

<!-- agent-hint
covers: how to add a language behaviour by extending spec data, when an added IR mechanism is justified, the version and spec rule, and how to run the IR guards
source: orthography2ipa/ir/compiler.py, orthography2ipa/ir/layout.py:SEMANTICS, scripts/check_engine_agnostic.py, scripts/check_ir_version_doc.py, scripts/ir_parity_ci.py, scripts/ir_lua_parity.py, .github/workflows/ir-guards.yml
generated: no
verify: .venv/bin/python -m doctest docs/contributing/behaviour_is_data.md
see: docs/engine/ir.md, docs/contributing/spec_authoring.md, docs/contributing/engine.md, docs/ir/o2i-ir-v1.md
-->

All language behaviour lives in the spec data. The compiler turns that data into the IR, and the interpreters run the IR with no knowledge of any language. This page shows how to add a behaviour, when the IR needs another mechanism, and how to run the checks that hold the rule.

## A spec field becomes IR data

Start from a behaviour that exists. In European Portuguese, a stressed ⟨e⟩ reads `ɛ` or `e`. The spec states it as a positional reading of the grapheme:

```python
>>> import orthography2ipa
>>> spec = orthography2ipa.get("pt-PT")
>>> spec.positional_graphemes["e"]  # doctest: +ELLIPSIS
{...<GraphemePosition.NUCLEUS_STRESSED: 'nucleus_stressed'>: ['ɛ', 'e']...}

```

The compiler lowers the named position to a predicate over entry bits and syllable relations. The interpreter evaluates the predicate and knows nothing of Portuguese:

```python
>>> import json
>>> from orthography2ipa.ir.compiler import build_ir
>>> ir = build_ir("pt-PT")
>>> e = next(e for e in ir["entries"] if e["key"] == "e")
>>> print(json.dumps(e["positional"][2], ensure_ascii=False))
[["and", ["or", ["ebit", 0, 0], ["ebit", 0, 21]], ["and", ["syll", "has_stress"]], ["syll", "idx_eq_stressed"]], ["ɛ", "e"]]

```

A stress field follows the same path. The spec lists the endings that take final stress, and the IR holds them in the decision list:

```python
>>> import orthography2ipa
>>> from orthography2ipa.ir.compiler import build_ir
>>> orthography2ipa.get("pt-PT").stress.final_stress_endings[:6]
('r', 'l', 'z', 'x', 'i', 'u')
>>> set(orthography2ipa.get("pt-PT").stress.final_stress_endings) <= set(build_ir("pt-PT")["stress"]["final"])
True

```

## Add a behaviour

Most behaviour needs only data. Work in this order:

1. Express the behaviour with the spec fields that exist. [spec_authoring.md](spec_authoring.md) and `SCHEMA.md` list them: positional readings, allophone rules with their contexts, stress lists, onset clusters, sandhi rules and word exceptions.
2. If no field expresses it, add a field. The field lands in `types.py`, `schema.py`, `json_loader.py` and `SCHEMA.md` together ([engine.md](engine.md#add-a-capability)).
3. Lower the field in `orthography2ipa/ir/compiler.py` to the primitives that exist: attribute bits, predicate nodes at any slot offset, the `count` quantifier, pattern rewrites, codepoint maps and tables. The compiler may hold tables of language facts. The interpreters may not.
4. Run the parity check. The Python interpreter, the Lua interpreter and the recorded golden output must agree.

Section 7.2 of [o2i-ir-v1.md](../ir/o2i-ir-v1.md#72-test-every-field-added-since-tag-7300) shows the lowering of each field that the spec format added over many releases. Nearly all of them needed a compiler change and no interpreter change.

## When another mechanism is justified

Add a primitive only when a field reads a kind of fact that no primitive can express. The `word_has` primitive is the example: a substring test over the whole spelled word, which no predicate over grapheme slots can state.

A primitive is never a shortcut for one language. It is general, it gets its own semantics version starting at 1, and one pull request adds it to every interpreter and defines it in [o2i-ir-v1.md](../ir/o2i-ir-v1.md).

## Change a version, change the spec

Each primitive and each predicate node has a semantics version in `layout.SEMANTICS`. Bump it when the behaviour of that primitive changes on any input, such as a bug fix. A compiler change never bumps it. `IR_VERSION` changes only for a change that is not additive, such as a removed table.

A version change and a change to `docs/ir/o2i-ir-v1.md` go in the same pull request. `check_ir_version_doc.py` compares the versions at a base ref with the working tree. With no change it passes:

```text
$ python3 -I scripts/check_ir_version_doc.py --base HEAD
base 100e78322943: 4 version values before, 4 after, 0 changed; docs/ir/o2i-ir-v1.md changed: False
```

With `"beam": 2` in `layout.SEMANTICS` and no edit to the spec, it fails with exit status 1:

```text
$ python3 -I scripts/check_ir_version_doc.py --base HEAD
base 100e78322943: 4 version values before, 4 after, 1 changed; docs/ir/o2i-ir-v1.md changed: False
  layout.SEMANTICS['beam']: 1 -> 2
error: an IR version or semantics version changed, and docs/ir/o2i-ir-v1.md did not. Define the change in the spec in the same pull request.
```

## Run the guards

The `IR Guards` workflow runs four checks on each pull request that touches `orthography2ipa/`, `docs/ir/` or the check scripts. Run them before you push.

### No language knowledge in an interpreter

`check_engine_agnostic.py` parses `interpreter.py`, `pattern.py`, `dialect.py`, `layout.py` and `interpreter.lua`. It refuses a language code, a script or family name, a Unicode name lookup and a codepoint range test that guesses a script. The forbidden names come from the spec data:

```text
$ .venv/bin/python -I scripts/check_engine_agnostic.py
checked 5 files against 7679 language codes and 81 script and family names: 0 violations
```

The check also takes file names. A file with `if lang == "pt-PT":` fails with exit status 1:

```text
$ .venv/bin/python -I scripts/check_engine_agnostic.py bad.py
checked 1 files against 7679 language codes and 81 script and family names: 1 violations
bad.py:2: language code literal 'pt-PT'
```

Some IR words are also ISO 639-3 codes, such as `and`, `set` and `end`. The check allows those words. Do not add a word to `IR_OPAQUE_WORDS` to pass the check: it holds only IR words that the spec defines.

### Every spec field is read or refused

`check_spec_fields.py` sets each field of `LanguageSpec`, and of each rule and stress object in it, to a different value on a few small specs. Then it compiles the spec. The field passes when the IR changes, or when the compiler raises `IRUnsupportedFeature` with the field name. A field with no behaviour, such as a citation or a display name, goes in the `INERT` table with a one-line reason. Any other field fails the check, because the compiler would drop its behaviour with no error. When a field is read only inside a feature, or takes a closed set of values, add an entry to `HINTS`. A hint gives the probe a valid value and does not exempt the field. The check sees a field that the compiler drops fully, not one that it drops in only one of its read sites. A run takes about one minute:

```text
$ .venv/bin/python -I -W ignore scripts/check_spec_fields.py
...
139 fields in 7 classes: 106 lowered, 2 refused, 0 inert, 31 declared
0 failure(s)
```

### The version rule

```bash
python3 -I scripts/check_ir_version_doc.py --base origin/dev
```

### Parity

`ir_parity_ci.py` compares the Python interpreter with the golden output in `tests/data/ir_golden_ci.json`, a fixed sample of languages plus `pt-PT`. It then compares the Python interpreter with the Lua interpreter on the same languages plus `kab`. The Lua step needs `luajit` on `PATH`. A run takes about two minutes:

```bash
.venv/bin/python -I scripts/ir_parity_ci.py
```

The last lines of a passing run:

```text
zu [wikipron]: N in 297, N out 297, N identical 297, mismatches 0 (errors py 0 lua 0; python 1446 texts/s, lua 3094 texts/s)
kab: N in 20, N out 20, N identical 20, mismatches 0 (errors py 0 lua 0; python 1234 texts/s, lua 1000 texts/s)
lua parity: 21 codes in, 21 results out
```

Any difference from the golden output fails. An intended output change records the golden file again with `scripts/ir_parity.py --write-golden`. Any difference between Python and Lua fails, because both read the same IR. The reports go to `ir-parity-reports/`.

---
[← Engine changes](engine.md) · [Home](../index.md) · [Silver IPA correction →](silver_correction.md)
