# TODO.md — orthography2ipa

_Last updated: 2026-03-16 | Reviewed by: Claude Sonnet 4.6_

Legend: 🔴 Blocking · 🟡 High · 🟢 Medium · ⚪ Low

---

## 🔴 BLOCKING (required before 0.2.0 stable release)

- [ ] **Create `QUICK_FACTS.md`** (required by project standards)
  - Package name, version, Python support range
  - Key public classes + entry points with file paths
  - Install command, quick usage example

- [ ] **Create `AUDIT.md`** (required by project standards)
  - Known issues with `file.py:LINE` citations
  - Tech debt items (type hint gaps, TODO comments)
  - Data quality notes (stub spec count, coverage gaps)
  - Security: no known vulnerabilities (document this explicitly)

- [ ] **Create `SUGGESTIONS.md`** (required by project standards)
  - Proposed: add `mypy` to CI for static type checking
  - Proposed: deprecate/remove `lm.py` legacy wrappers in v0.3.0
  - Proposed: expand African and Southeast Asian language coverage
  - Proposed: implement tashkeel ONNX model loading
  - Proposed: cache beam-search paths for repeated tokenization

---

## 🟡 HIGH (target: 0.2.0 stable)

- [ ] **Complete type annotations in `feats.py`**
  - `orthography2ipa/feats.py:56` — annotate `phone_features: Dict[str, List[Optional[bool]]]`
  - Run `mypy orthography2ipa/feats.py` to verify

- [ ] **Complete type annotations in `plugins/arabic_g2p.py`**
  - Add `-> bool` return type to `_has_diacritics` (already has it; verify no gaps remain)
  - Run `mypy orthography2ipa/plugins/arabic_g2p.py` to verify

- [ ] **Add CI coverage reporting**
  - Add `--cov=orthography2ipa --cov-report=xml` to `unit_tests.yml`
  - Upload coverage artifact or add coverage badge to README.md
  - Establish baseline coverage percentage as regression gate

- [ ] **Update `pyproject.toml` description**
  - Change: `"Linguistically motivated grapheme-to-IPA ... for 20+ languages"`
  - To: `"Linguistically motivated grapheme-to-IPA and allophone mappings for 308+ language codes"`

---

## 🟢 MEDIUM (target: 0.2.x patch releases)

- [ ] **Clarify TODO comment in `json_loader.py:115`**
  - Current: `continue  # TODO - error log, illegal`
  - Replace with: `continue  # Skip self-reference cycles (parent == code); invalid per schema`

- [ ] **Add multi-version Python CI matrix**
  - Test against Python 3.9, 3.10, 3.11, 3.12, 3.13
  - Add matrix to `unit_tests.yml`: `python-version: ["3.9", "3.10", "3.11", "3.12", "3.13"]`

- [ ] **Add lint workflow**
  - Add `.github/workflows/lint.yml` using `ruff` or `flake8`
  - Fix any existing lint errors before enabling in CI

- [ ] **Add `mypy` to CI**
  - Add `.github/workflows/typecheck.yml`
  - Start with `--ignore-missing-imports` to get baseline
  - Fix type errors systematically; do not suppress wholesale

- [ ] **Update `MAINTENANCE_REPORT.md`** with this review session
  - Date: 2026-03-16
  - Model: Claude Sonnet 4.6
  - Actions: Full review, PLAN.md + TODO.md created

---

## ⚪ LOW / FUTURE (backlog — no fixed release target)

- [ ] **Implement Arabic tashkeel via ONNX**
  - File: `orthography2ipa/plugins/tashkeel.py:50`
  - Requires: choosing + bundling an ONNX model for Arabic diacritization
  - Blocked on: model licensing decision

- [ ] **Add deprecation to `lm.py` legacy functions**
  - Use standard `DeprecationWarning` via `warnings.warn()`
  - Plan removal in v0.3.0 (breaking change → bump major version)

- [ ] **Expand stub language data**
  - ~238 stub specs have minimal grapheme data
  - Community contributions welcome; see `docs/adding_a_language.md`
  - Priority languages: Swahili variants, Tagalog dialects, Tibetan

- [ ] **Add pip-audit workflow**
  - `numpy` and `onnxruntime` are the only runtime deps; low risk
  - Still good practice to automate vulnerability scanning

- [ ] **Validate Python version support claim in pyproject.toml**
  - Classifiers list 3.9–3.13 but CI only tests one version currently
  - Blocked on: multi-version matrix (see MEDIUM above)

- [ ] **Add `docs/transforms.md`**
  - Current transforms docs are embedded in docstrings in `transforms.py`
  - Extract to standalone doc with examples for each of 15 profiles

- [ ] **Performance: cache beam-search paths**
  - `phonetok.py` beam search recomputes paths on each call
  - Cache by `(language_code, grapheme_sequence)` key for repeated calls

- [ ] **Input validation in `distance.py`**
  - `segment_distance(a, b)` accepts malformed IPA silently
  - Add optional `strict=False` parameter; raise `ValueError` if `strict=True`
