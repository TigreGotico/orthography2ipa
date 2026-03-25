# TODO.md — orthography2ipa

_Last updated: 2026-03-25 | Reviewed by: Claude Sonnet 4.6_

Legend: 🔴 Blocking · 🟡 High · 🟢 Medium · ⚪ Low

---

## 🔴 BLOCKING (required before 0.2.0 stable release)

All blocking items resolved. ✅

---

## 🟡 HIGH (target: 0.2.0 stable)

- [x] **Extend `.gitignore`** ✅ 2026-03-25
- [x] **Fix bare `except:` clauses in `feats.py`** ✅ 2026-03-25
- [x] **Fix `spec_en` fixture in `tests/conftest.py`** ✅ 2026-03-25
- [x] **Add Python 3.13 to CI matrix** ✅ 2026-03-25
- [x] **Add type hints to deprecation shims in `feats.py`** ✅ 2026-03-25
- [x] **Complete global Portuguese coverage** ✅ 2026-03-25
  - Added pt-MZ, pt-CV, pt-GW, pt-ST, pt-TL, pt-MO
  - Fixed quality/metadata on pt-PT, pt-BR, pt-PT-x-medieval
  - Added contact language stubs: sw, ny, ts, kea, pov, ff, tet, id, mcm

All 🟡 HIGH items resolved. Ready for 0.2.0 stable. ✅

---

## 🟢 MEDIUM (target: 0.2.x patch releases)

- [ ] **Add lint workflow**
  - Add `.github/workflows/lint.yml` using `ruff`
  - Fix any existing lint errors before enabling in CI

- [ ] **Add `mypy` type-check workflow**
  - Add `.github/workflows/typecheck.yml` with `--ignore-missing-imports`

- [ ] **Add `pip-audit` workflow**

- [ ] **Add `docs/transforms.md`**
  - Extract 15 dialect profile details from `transforms.py` docstrings to standalone doc

- [ ] **Add coverage gate to CI**
  - `unit_tests.yml` runs `--cov` but has no enforcement/reporting

---

## ⚪ LOW / FUTURE

- [ ] **Implement Arabic tashkeel via ONNX**
  - `orthography2ipa/plugins/tashkeel.py`
  - Blocked on: model licensing decision

- [ ] **Remove `lm.py` deprecation shims from `feats.py` in v0.3.0**
  - `feats.py:650-683` — three wrapper functions with `DeprecationWarning`

- [ ] **Add Saotomense (Forro) Gulf of Guinea creole**
  - São Tomense creole, São Tomé island; part of Gulf of Guinea cluster with pre/aoa
  - ISO 639-3 needs verification before creating file (not "crs" which is Seychellois)

- [ ] **Expand stub language data**
  - ~238 stub specs have minimal grapheme data
  - Priority: Swahili variants, Tagalog dialects, Tibetan

- [ ] **Performance: cache beam-search paths**
  - `phonetok.py` beam search recomputes paths on each call
  - Cache by `(language_code, grapheme_sequence)` key

- [ ] **Fix Rionorese `nh` tokenizer conflict**
  - `phonetok.py` trie greedily consumes `en→ẽ` before `nh→ɲ`
  - Fix direction: weighted trie or context-aware construction

---

## Temporal Coverage (COMPLETE 2026-03-25) ✅

- [x] `TimeSpan` dataclass + `LanguageSpec.timespan` field — `types.py`
- [x] `temporal_distance()` — Jaccard-interval metric — `distance.py`
- [x] `_temporal_decay()` + `ancestry_similarity(temporal_decay=True)` — `distance.py`
- [x] `weighted_full_distance(w_temporal=...)` integration — `distance.py`
- [x] 29 JSON files annotated (Germanic chain + key modern languages)
- [x] **Extended timespan coverage to all 330 language files** (2026-03-25)
- [ ] **Consider `temporal_distance` in `pairwise_distances()` metric enum**

## Metadata Completeness (COMPLETE 2026-03-25) ✅

- [x] `glottolog_code` added to all 330 language files (87 dialect variants correctly left null)
- [x] `iso639_3` added to all 330 files (20 proto-languages correctly left null)
- [x] 140 files upgraded from stub/skeleton → research quality
- [x] Fix: `xce.json` sources[0].url was publisher string
- [ ] **Upgrade remaining 86 skeleton files** (add positional_graphemes / validate phonology)
- [ ] **Reach production tier** (requires regression tests per language)

---

## Linguistic Reference Audit Checklist

### Phase 0 — Infrastructure (COMPLETE 2026-03-17) ✅
### Phase 1 — Germanic (COMPLETE 2026-03-17) ✅
### Phase 2 — Romance (COMPLETE) ✅
### Phase 3 — Semitic/Arabic (COMPLETE) ✅
### Phase 4 — Indo-Iranian (COMPLETE) ✅
### Phase 5 — Other Modern (COMPLETE) ✅
### Phase 6 — Ancient/Reconstructed/Extinct (COMPLETE) ✅

All 308 non-stub language codes now have at least one bibliographic source or Wikipedia reference.
`wikipedia` field migrated to `Tuple[str, ...]` format (2026-03-19).
