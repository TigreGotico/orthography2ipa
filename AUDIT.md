# AUDIT.md — orthography2ipa

_Last updated: 2026-03-17 | Auditor: Claude Sonnet 4.6_

Evidence-based. All issues cite `file.py:LINE`.

---

## Security

**No known security vulnerabilities.**

- Runtime dependencies: `numpy`, `langcodes`; `onnxruntime` optional (Arabic only).
- No network calls at runtime.
- No user input executed as code.
- No SQL or shell injection surfaces.
- **Open item**: `pip-audit` is not yet in CI — CVE scanning not automated. See CI Gaps below.

---

## ✅ Resolved Since Last Audit (2026-03-16 → 2026-03-17)

| Issue | File | Resolution |
| :--- | :--- | :--- |
| `phone_features` missing type annotation | `feats.py:56` | Annotated as `Dict[str, List[Optional[bool]]]`; `Dict, Optional` added to imports at `feats.py:39` |
| Ambiguous TODO comment | `json_loader.py:116` | Rewritten to `# Skip self-reference cycles (parent == code); invalid per schema` |
| Stale `pyproject.toml` description ("20+ languages") | `pyproject.toml:8` | Updated to `"308+ language codes"` |
| `en-GB.json` missing (15 tests skipped) | `orthography2ipa/data/en-GB.json` | File now exists; tests no longer skip |
| `LinguisticSource` type missing | `types.py` | `LinguisticSource` frozen dataclass added; `LanguageSpec.sources` field added |
| `json_loader.py` not parsing `sources` | `json_loader.py` | `sources` array parsed into `Tuple[LinguisticSource, ...]` |

---

## Open Issues

### 1. Missing Sources — 221 Non-Stub Languages (HIGH)

`tests/test_sources.py::test_non_stub_has_sources` currently fails for 221 language codes.
All non-stub (`quality: "research"` or `quality: "skeleton"`) languages require at least one
`LinguisticSource` entry, but only the 33 Germanic files have been sourced so far.

**Affected tiers** (per `orthography2ipa/data/*.json`):

| Tier | Count | Sources completed |
| :--- | :--- | :--- |
| `"stub"` | 61 | — (exempt) |
| `"skeleton"` | 222 | 33 (Germanic only) |
| `"research"` | 25 | 0 |

**Tracking**: `PLAN.md` — Phases 2–6 outstanding. `TODO.md` — per-language checklist.

**Test command**:
```bash
uv run pytest tests/test_sources.py -v
```

---

### 2. Tokenizer Trie Conflict — Rionorese `nh` Sequences (MEDIUM)

The maximal-munch tokenizer (`phonetok.py`) builds a prefix trie from `spec.graphemes`.
For Rionorese (`ast-PT-x-rionor`), the inherited `en→ẽ` digraph is consumed before `nh→ɲ`
can be seen in words like `benhir`. The trie greedily takes `en` first.

- File: `orthography2ipa/phonetok.py`
- Impact: Rionorese tokenization of `nh` sequences preceded by `en` only
- `resolve_grapheme()` is unaffected (positional lookup bypasses the trie)
- Workaround: use `resolve_grapheme()` directly for production Rionorese text
- Fix direction: weighted trie or context-aware trie construction

---

### 3. `tashkeel.py` — Unimplemented Stub (LOW)

The Arabic tashkeel diacritizer raises `NotImplementedError`.
`ArabicG2PPlugin` catches `ImportError` on init and silently disables tashkeel when unavailable.

- File: `orthography2ipa/plugins/tashkeel.py`
- Status: blocked on ONNX model selection and licensing
- No user-facing regression — Arabic G2P works without tashkeel; diacritized input
  simply bypasses the tashkeel step

---

### 4. `lm.py` — Deprecation Wrappers Not Yet Removed (LOW)

Legacy functions (`build_ngram_lm`, `perplexity`, `phoneme_embeddings`) were moved to
`orthography2ipa/lm.py`. Deprecation shims remain in `feats.py` emitting `DeprecationWarning`.

- Shim locations: `orthography2ipa/feats.py:653`, `feats.py:665`, `feats.py:677`
- Target removal: v0.3.0 (breaking change, requires major version bump)
- These are intentionally kept for backwards compatibility until v0.3.0

---

### 5. `conftest.py` — `spec_en` Fixture Hardcoded to `en-GB` (LOW)

`tests/conftest.py` defines `spec_en` as `get("en-GB")`. Tests that rely on a generic
"English" spec will silently use British English assumptions. If a test needs GA-specific
behaviour it should use `get("en-US")` explicitly.

- File: `tests/conftest.py`
- Impact: cosmetic; no incorrect results, but easy to misread

---

## Data Quality

### Quality Tier Breakdown (2026-03-17)

| Tier | Count | Description |
| :--- | :--- | :--- |
| `"stub"` | 61 | Ancestry placeholder only; no graphemes expected |
| `"skeleton"` | 222 | Minimal grapheme inventory; allophone coverage may be incomplete |
| `"research"` | 25 | Reviewed against academic sources; full allophone inventories |
| **Total** | **308** | — |

`test_language_integrity.py` validates all 308 specs structurally.
Stub and skeleton specs pass structural tests at their documented tier.

---

## CI Gaps

| Missing | Impact | Priority |
| :--- | :--- | :--- |
| No coverage reporting (`--cov`) | Coverage regressions undetected | High |
| No multi-version Python matrix (3.10–3.13) | Compatibility breakage goes unnoticed | High |
| No lint workflow (flake8 / ruff) | PEP 8 violations accumulate | Medium |
| No `mypy` / type-check workflow | Type errors not caught in CI | Medium |
| No `pip-audit` workflow | CVE scanning not automated | Medium |

Current workflows: `unit_tests.yml`, `release_workflow.yml`, `publish_stable.yml`, `conventional-label.yaml`.
