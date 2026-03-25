# PLAN.md — orthography2ipa

_Last updated: 2026-03-25_

## Project Status: Alpha (v0.2.0a1)

orthography2ipa is a linguistically motivated grapheme-to-IPA conversion library
covering 308+ language codes with allophone inventories, dialect transforms, phonological
distance metrics, language ancestry modelling, and a G2P plugin architecture.

---

## Architecture Overview

| Layer | Module | Responsibility |
| :--- | :--- | :--- |
| Data model | `types.py` | Frozen dataclasses: `LanguageSpec`, `Ancestor`, `SandhiRule`, enums |
| Registry | `registry.py` | Lazy-load registry + entry-point plugin discovery |
| JSON loading | `json_loader.py` | JSON→LanguageSpec conversion, inheritance resolution |
| Tokenizer | `phonetok.py` | Maximal-munch tokenizer + beam-search IPA expansion |
| Distance | `distance.py` | Phonological distance (inventory, grapheme, ancestry) |
| Features | `feats.py` | 23-feature SPE/IPA distinctive-feature system |
| Transforms | `transforms.py` | 15 dialect transform profiles (Iberian Romance) |
| Script distance | `script_distance.py` | Typological distance between writing systems |
| Sandhi | `sandhi.py` | Cross-word-boundary phonological rules |
| CLI | `cli.py` | Command-line interface (entry point) |
| Plugins | `plugins/` | Arabic G2P, tashkeel stub, abstract plugin interface |
| Public API | `__init__.py` | Aggregated public surface |

**Data**: 308 JSON language specs in `data/`, 1 CSV lexicon.
**CI**: 4 GitHub Actions workflows (unit tests, release, PyPI publish, commit labeling).
**Tests**: 30+ test files, 7375 passing tests.

---

## Current Phase: Code Quality & CI Hardening

### Completed (2026-03-25)
- ✅ Full `/docs` audit — all stale references, line numbers, missing modules fixed
- ✅ Linguistic Reference Audit — all 6 phases complete
- ✅ `positional_graphemes` added for nl, sv, pl, cs, el, tr, hi
- ✅ Documentation files (FAQ, AUDIT, SUGGESTIONS, AGENTS) up to date

### Next Steps (0.2.0 stable)
1. Extend `.gitignore` — exclude `__pycache__/`, `.idea/`, `*.egg-info/`
2. Fix bare `except:` in `feats.py:578,636`
3. Add type hints to deprecation shims in `feats.py:650-683`
4. Fix `spec_en` fixture in `tests/conftest.py:26`
5. Add Python 3.13 to CI matrix

### Out of Scope (next major version)
- Tashkeel ONNX implementation (requires external model; optional feature)
- Expanding stub language data (ongoing linguistics work)
- New dialect transform profiles
- Removing deprecation shims (v0.3.0 breaking change)

---

## Planned Changes

### P1 — Code Quality Fixes (0.2.0 stable)

| File | Issue | Fix |
| :--- | :--- | :--- |
| `.gitignore` | Missing standard exclusions | Add `__pycache__/`, `.idea/`, `*.egg-info/`, etc. |
| `feats.py:578` | Bare `except:` in `is_vowel_phone()` | Replace with specific exceptions |
| `feats.py:636` | Bare `except:` in `phonetic_distance()` | Replace with specific exceptions |
| `feats.py:650-683` | Deprecation shims missing type hints | Add annotations matching `lm.py` |
| `tests/conftest.py:26` | `spec_en` fixture skips despite `en-GB.json` existing | Return loaded spec |

### P2 — CI Improvements (0.2.x)

| Workflow to Add | Purpose |
| :--- | :--- |
| Python 3.13 in matrix | Verify claimed compatibility |
| Coverage gate | Track coverage %; prevent regressions |
| Lint (ruff) | Enforce PEP 8 |
| `mypy` | Catch type errors in CI |
| `pip-audit` | CVE scanning |

---

## Data Roadmap

| Tier | Count | Status |
| :--- | :--- | :--- |
| Production-quality | ~50 | ✓ Validated, allophone inventories complete |
| Research-quality | ~25 | ✓ Reviewed against academic sources |
| Stub/skeleton | ~233 | Auto-generated; minimal data |

All non-stub specs have at least one bibliographic source or Wikipedia reference.
Stub specs need community/contributor data; not a solo-agent task.

---

## Dependency Strategy

- `numpy` — feature vector operations in `feats.py`; keep
- `langcodes` — BCP-47 normalization; keep
- `onnxruntime` — optional for Arabic tashkeel; keep optional
- No new runtime dependencies planned

---

## Testing Strategy

- All new code changes require unit tests in `tests/`
- Run: `uv run pytest tests/ -v --cov=orthography2ipa --cov-report=term-missing`
- Target: maintain or increase coverage percentage
- Custom markers: `slow`, `linguistic`, `iberian`, `germanic`, `celtic`, `slavic`

---

## Linguistic Reference Audit — COMPLETE ✅

All 6 phases complete. Every non-stub spec has a populated `sources` array or Wikipedia reference.

| Phase | Languages | Status |
| :--- | :--- | :--- |
| Phase 0 — Infrastructure | `LinguisticSource` type, loader, schema | **COMPLETE** |
| Phase 1 — Germanic | 33 files | **COMPLETE** |
| Phase 2 — Romance | 60+ files | **COMPLETE** |
| Phase 3 — Semitic/Arabic | ar-*, arb, sem-*, phn, cop | **COMPLETE** |
| Phase 4 — Indo-Iranian | hi, ur, bn, fa-*, etc. | **COMPLETE** |
| Phase 5 — Other Modern | ru-*, uk, cs, pl, el, tr, fi, etc. | **COMPLETE** |
| Phase 6 — Ancient/Extinct | ine, cel-*, peo, pal, etc. | **COMPLETE** |

### Session Resume Instructions
1. Read this `PLAN.md` for current progress
2. Read `TODO.md` for actionable items
3. Check `MAINTENANCE_REPORT.md` for last session's changes
4. Work through TODO items by priority (🔴 → 🟡 → 🟢 → ⚪)
