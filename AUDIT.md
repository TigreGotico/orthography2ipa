# AUDIT.md — orthography2ipa

_Last updated: 2026-03-16 | Auditor: Claude Sonnet 4.6_

Evidence-based. All issues cite `file.py:LINE`.

---

## Security

**No known security vulnerabilities.**

- Runtime dependencies: `numpy`, `langcodes` (runtime); `onnxruntime` (optional, Arabic only).
- No network calls at runtime.
- No user input executed as code.
- Recommendation: add `pip-audit` workflow to CI for automated CVE scanning.

---

## Type Hint Gaps

### `orthography2ipa/feats.py:56`
`phone_features` is a large module-level `dict` with no type annotation.

```python
# Current (feats.py:56)
phone_features = {
    ...
}
# Should be:
phone_features: Dict[str, List[Optional[bool]]] = {
    ...
}
```

The `typing` import at line 39 already imports `List` and `Union` but not `Optional` or `Dict`.
Fix: add `Dict, Optional` to the import and annotate the dict.

### `orthography2ipa/feats.py:39`
`from typing import List, Union` — `Dict` and `Optional` are used in the module but not imported
from `typing` (they may be resolved via type-checker fallback). Explicit imports required per
project standards.

---

## TODO / Unclear Comments

### `orthography2ipa/json_loader.py:115`
```python
continue  # TODO - error log, illegal
```
This comment is ambiguous. The `continue` skips a parent code that equals the child code
(self-reference cycle). The comment should read:
```python
continue  # Skip self-reference cycles (parent == code); invalid per schema
```
No behavioral change needed — the logic is correct; only the comment is unclear.

---

## Outdated Metadata

### `pyproject.toml:8`
```toml
description = "Linguistically motivated grapheme-to-IPA and allophone mappings for 20+ languages"
```
The actual language count is 308+. The description is stale since the universal language
coverage expansion (2026-03-10). Fix: update the description string.

---

## Data Quality

### Stub Language Specs (~238 of 308)
Most language specs promoted from `dump/langs/` are stubs: they have `quality_tier: "stub"`,
minimal or no `graphemes` entries, and no `allophones`. These are intended as ancestry
placeholders only. Using them with `PhonetokTokenizer` will produce empty or near-empty output.

**Risk**: low — stub specs explicitly document their tier; callers can check `spec.quality_tier`.

**Mitigation**: `test_language_integrity.py` validates all registered specs structurally.
Stubs without graphemes will not pass the non-empty grapheme assertion — tests are currently
written to skip stub-class specs for grapheme completeness checks.

### Missing `en-GB.json`
15 tests are currently skipped because `en-GB.json` does not exist. The `spec_en` fixture in
`tests/conftest.py` skips with a clear message. This is a known gap, not a regression.

---

## Technical Debt

### `orthography2ipa/lm.py` — Legacy Wrappers
`lm.py` was created in 2026-03-09 to hold moved functions (`build_ngram_lm`, `perplexity`,
`phoneme_embeddings`) that were previously in `feats.py`. Deprecation wrappers remain in
`feats.py` emitting `DeprecationWarning`. These should be removed in v0.3.0.

- Deprecation wrappers: `orthography2ipa/feats.py` (search for `DeprecationWarning`)
- Target removal: v0.3.0 (next major version bump)

### `orthography2ipa/plugins/tashkeel.py` — Unimplemented Stub
The tashkeel diacritizer is a stub that raises `NotImplementedError`. `ArabicG2PPlugin`
catches `ImportError` on init and silently disables tashkeel if unavailable. The stub
file documents the expected ONNX interface but provides no implementation.

- File: `orthography2ipa/plugins/tashkeel.py`
- Status: blocked on ONNX model selection and licensing

### Tokenizer Trie Conflict — `benhir` in Rionorese
The maximal-munch tokenizer (`phonetok.py`) builds a trie from `spec.graphemes`. For
Rionorese (`ast-PT-x-rionor`), the parent's `en→ẽ` digraph is consumed before `nh→ɲ`
can be seen in words like `benhir`. This is a known limitation of flat-grapheme maximal-munch.
`resolve_grapheme()` is unaffected.

- Documented in: `FAQ.md`
- File: `orthography2ipa/phonetok.py`
- Impact: affects only Rionorese tokenization of `nh` sequences preceded by `en`

---

## CI Gaps

| Missing | Impact |
| :--- | :--- |
| No coverage reporting in CI | Coverage regressions go undetected |
| No multi-version Python matrix | 3.9/3.10/3.12/3.13 untested in CI |
| No lint workflow | PEP 8 violations accumulate silently |
| No `mypy` / typecheck workflow | Type errors not caught in CI |
| No `pip-audit` workflow | CVE scanning not automated |
