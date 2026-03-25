# TODO.md — orthography2ipa

_Last updated: 2026-03-25 | Reviewed by: Claude Opus 4.6_

Legend: 🔴 Blocking · 🟡 High · 🟢 Medium · ⚪ Low

---

## 🔴 BLOCKING (required before 0.2.0 stable release)

All blocking items resolved. ✅

---

## 🟡 HIGH (target: 0.2.0 stable)

- [ ] **Extend `.gitignore`**
  - Add `__pycache__/`, `*.pyc`, `.idea/`, `*.egg-info/`, `.pytest_cache/`, `.coverage`, `dist/`, `build/`
  - Remove tracked `.pyc` files from git index

- [ ] **Fix bare `except:` clauses in `feats.py`**
  - `feats.py:578` — `is_vowel_phone()`: replace with `except (ValueError, KeyError, IndexError):`
  - `feats.py:636` — `phonetic_distance()`: replace with `except (ValueError, KeyError, IndexError):`

- [ ] **Fix `spec_en` fixture in `tests/conftest.py:26-29`**
  - `en-GB.json` now exists — replace `pytest.skip()` with `return orthography2ipa.get("en-GB")`

- [ ] **Add Python 3.13 to CI matrix**
  - `.github/workflows/unit_tests.yml:23` currently tests 3.10, 3.11, 3.12
  - `pyproject.toml` claims 3.9–3.13 support

- [ ] **Add type hints to deprecation shims in `feats.py`**
  - `feats.py:650` — `phoneme_embeddings(spec)`
  - `feats.py:662` — `build_ngram_lm(words, spec, n=3)`
  - `feats.py:674` — `perplexity(lm, test_words, spec, n=3)`

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
