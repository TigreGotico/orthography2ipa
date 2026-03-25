# AUDIT.md — orthography2ipa

_Last updated: 2026-03-25 | Auditor: Claude Opus 4.6_

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

## ✅ Resolved Since Last Audit (2026-03-17 → 2026-03-25)

| Issue | File | Resolution |
| :--- | :--- | :--- |
| Stale docs referencing non-existent Python modules | `docs/architecture.md` | Complete rewrite — all module refs now point to actual files |
| 27+ incorrect line-number citations in docs | `docs/index.md` | All citations verified against source |
| 8 undocumented modules | `docs/architecture.md` | All modules now documented with line refs |
| 15 missing `GraphemePosition` enum values in docs | `docs/positional_graphemes.md` | All 21 values documented |
| `json_loader.py:115` unclear TODO comment | `json_loader.py` | Resolved (no TODO/FIXME comments remain) |
| Linguistic Reference Audit Phases 2–6 | `orthography2ipa/data/*.json` | All 6 phases COMPLETE per TODO.md |

---

## Open Issues

### 1. `.gitignore` Incomplete — Tracking Unnecessary Files (HIGH)

Current `.gitignore` only excludes `/dump/*`, `CLAUDE.md`, `.claude`.

**Missing exclusions**: `__pycache__/`, `*.pyc`, `.idea/`, `*.egg-info/`, `.pytest_cache/`, `.coverage`, `dist/`, `build/`.

**Evidence**: `git status` shows modified `.pyc` files and untracked `.idea/`, `*.egg-info/` directories.

- File: `.gitignore`

---

### 2. Bare `except:` Clauses in `feats.py` (HIGH)

Two bare exception handlers catch all exceptions indiscriminately, masking bugs and suppressing `KeyboardInterrupt`/`SystemExit`.

- `feats.py:578` — `is_vowel_phone()`: catches all exceptions, returns `False`
- `feats.py:636` — `phonetic_distance()`: catches all exceptions, returns `3.0`

**Fix**: Replace with `except (ValueError, KeyError, IndexError):`.

---

### 3. Missing Type Hints on Deprecation Shims (MEDIUM)

Three deprecated wrapper functions in `feats.py` lack all type annotations, violating the mandatory type hints policy.

- `feats.py:650` — `phoneme_embeddings(spec)` — no type hints
- `feats.py:662` — `build_ngram_lm(words, spec, n=3)` — no type hints
- `feats.py:674` — `perplexity(lm, test_words, spec, n=3)` — no type hints

**Fix**: Add parameter and return type annotations matching `lm.py` implementations.

---

### 4. Outdated `spec_en` Fixture — Still Skipped (MEDIUM)

`tests/conftest.py:26-29` skips the `spec_en` fixture claiming `en-GB.json` does not exist. The file **does exist** and loads successfully.

**Fix**: Replace `pytest.skip(...)` with `return orthography2ipa.get("en-GB")`.

---

### 5. CI Python Version Mismatch (MEDIUM)

`pyproject.toml` declares support for Python 3.9–3.13. CI only tests 3.10, 3.11, 3.12.

- File: `.github/workflows/unit_tests.yml:23`
- Mismatch: Python 3.9 and 3.13 not tested

---

### 6. Tokenizer Trie Conflict — Rionorese `nh` Sequences (MEDIUM)

The maximal-munch tokenizer (`phonetok.py`) greedily consumes `en→ẽ` before `nh→ɲ` in words like `benhir`.

- File: `orthography2ipa/phonetok.py`
- Impact: Rionorese tokenization of `nh` sequences preceded by `en` only
- `resolve_grapheme()` is unaffected (positional lookup bypasses the trie)
- Fix direction: weighted trie or context-aware trie construction

---

### 7. `tashkeel.py` — Unimplemented Stub (LOW)

The Arabic tashkeel diacritizer raises `NotImplementedError`. Plugin fails gracefully.

- File: `orthography2ipa/plugins/tashkeel.py`
- Status: blocked on ONNX model selection and licensing

---

### 8. `lm.py` — Deprecation Wrappers Not Yet Removed (LOW)

Legacy functions remain as shims in `feats.py:650-683` emitting `DeprecationWarning`.

- Target removal: v0.3.0 (breaking change)
- Intentionally kept for backwards compatibility

---

## Data Quality

### Quality Tier Breakdown (2026-03-25)

| Tier | Count | Description |
| :--- | :--- | :--- |
| `"stub"` | ~61 | Ancestry placeholder only; no graphemes expected |
| `"skeleton"` | ~222 | Minimal grapheme inventory; allophone coverage may be incomplete |
| `"research"` | ~25 | Reviewed against academic sources; full allophone inventories |
| **Total** | **308** | All 308 specs pass structural tests |

All 6 phases of Linguistic Reference Audit complete — all non-stub languages have at least one bibliographic source or Wikipedia reference.

---

## CI Gaps

| Missing | Impact | Priority |
| :--- | :--- | :--- |
| No coverage gate | Coverage regressions undetected | High |
| Python 3.9/3.13 not in CI matrix | Classifier claims untested | High |
| No lint workflow (ruff) | PEP 8 violations accumulate | Medium |
| No `mypy` type-check workflow | Type errors not caught in CI | Medium |
| No `pip-audit` workflow | CVE scanning not automated | Medium |

Current workflows: `unit_tests.yml`, `release_workflow.yml`, `publish_stable.yml`, `conventional-label.yaml`.
