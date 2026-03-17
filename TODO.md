# TODO.md — orthography2ipa

_Last updated: 2026-03-17 | Reviewed by: Claude Sonnet 4.6_

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

---

## Linguistic Reference Audit Checklist

### Phase 0 — Infrastructure (COMPLETE 2026-03-17)
- [x] `LinguisticSource` dataclass in `types.py`
- [x] `sources` field in `LanguageSpec`
- [x] `json_loader.py` parses `sources` array
- [x] `SCHEMA.md` documents `sources` field
- [x] `tests/test_sources.py` enforces non-stub sources

### Phase 1 — Germanic (COMPLETE 2026-03-17)
- [x] en-GB
- [x] en-US
- [x] en-AU
- [x] en-CA
- [x] en-IE
- [x] en-ZA
- [x] en-GB-x-scotland
- [x] de-DE
- [x] de-AT
- [x] de-CH
- [x] nl
- [x] nl-NL
- [x] nl-BE
- [x] sv
- [x] sv-x-rikssvenska
- [x] nb
- [x] nn
- [x] no
- [x] da
- [x] da-x-copenhagen
- [x] is
- [x] fo
- [x] af
- [x] nds
- [x] enm
- [x] ang
- [x] non
- [x] osx
- [x] goh
- [x] gem
- [x] gem-x-ingvaeonic
- [x] gem-x-north
- [x] gem-x-northwest

### Phase 2 — Romance (TODO)
- [ ] es-ES (Castilian)
- [ ] es-ES-x-andalusia-e
- [ ] es-ES-x-andalusia-w
- [ ] es-ES-x-canarias
- [ ] es-ES-x-cantabria
- [ ] es-ES-x-murcia
- [ ] es-419
- [ ] es-AR
- [ ] es-BO
- [ ] es-CL
- [ ] es-CO / es-CO-x-costa / es-CO-x-paisa
- [ ] es-CR
- [ ] es-CU
- [ ] es-DO
- [ ] es-EC
- [ ] es-GQ
- [ ] es-GT
- [ ] es-MX / es-MX-x-costa
- [ ] es-NI
- [ ] es-PA
- [ ] es-PE / es-PE-x-lima
- [ ] es-PR
- [ ] es-PY
- [ ] es-UY
- [ ] es-VE
- [ ] pt-PT / pt-PT-x-lisbon / pt-PT-x-* dialects
- [ ] pt-BR / pt-BR-x-* dialects
- [ ] pt-AO
- [ ] fr-FR
- [ ] frp (Franco-Provençal)
- [ ] it-IT / it-IT-x-* dialects
- [ ] ca / ca-x-* dialects
- [ ] ro-RO
- [ ] gl-ES / gl-x-central
- [ ] oc-x-aranes
- [ ] sc / sc-x-campidanese / sc-x-logudorese
- [ ] scn (Sicilian)
- [ ] lij (Ligurian)
- [ ] lmo (Lombard)
- [ ] vec (Venetian)
- [ ] fur (Friulian)
- [ ] nap (Neapolitan)
- [ ] egl (Emilian)
- [ ] pms (Piedmontese)
- [ ] lld (Ladin)
- [ ] rm (Romansh)
- [ ] mwl / mwl-x-* (Mirandese)
- [ ] ext (Extremaduran)
- [ ] ast / ast-* (Asturian)
- [ ] fax (Faroese? — verify)
- [ ] roa-x-galaicopt
- [ ] la-x-* (Latin dialects)
- [ ] co (Corsican)

### Phase 3 — Semitic/Arabic (TODO)
- [ ] ar (Modern Standard Arabic)
- [ ] arb (Standard Arabic)
- [ ] ar-AE / ar-BH / ar-DZ / ar-IQ / ar-KW / ar-LY / ar-MA
- [ ] ar-MR / ar-NG / ar-OM / ar-QA / ar-SA-* / ar-TD / ar-TN / ar-YE
- [ ] ar-IQ-x-qeltu
- [ ] ar-x-gulf / ar-x-maghrebi / ar-x-mashriqi / ar-x-peninsular
- [ ] sem / sem-x-central / sem-x-west
- [ ] phn (Phoenician)
- [ ] cop (Coptic)
- [ ] ber (Berber)

### Phase 4 — Indo-Iranian (TODO)
- [ ] hi (Hindi)
- [ ] ur (Urdu)
- [ ] bn (Bengali)
- [ ] pa / pa-PK (Punjabi)
- [ ] gu (Gujarati)
- [ ] mr (Marathi)
- [ ] ne (Nepali)
- [ ] sa / sa-x-vedic (Sanskrit)
- [ ] pi (Pali)
- [ ] fa / fa-AF / fa-x-* (Farsi dialects)
- [ ] ps (Pashto)
- [ ] sd (Sindhi)
- [ ] ks (Kashmiri)
- [ ] tg (Tajik)
- [ ] iir (Proto-Indo-Iranian)
- [ ] ira (Proto-Iranian)
- [ ] pal (Pahlavi/Middle Persian)
- [ ] peo (Old Persian)

### Phase 5 — Other Modern (TODO)
- [ ] ru / ru-x-* dialects
- [ ] uk (Ukrainian)
- [ ] be (Belarusian)
- [ ] bg (Bulgarian)
- [ ] mk (Macedonian)
- [ ] sr (Serbian)
- [ ] hr (Croatian)
- [ ] cs (Czech)
- [ ] sk (Slovak)
- [ ] pl (Polish)
- [ ] sl (Slovenian)
- [ ] sla (Proto-Slavic)
- [ ] el (Greek)
- [ ] cy (Welsh)
- [ ] ga (Irish)
- [ ] gd (Scottish Gaelic)
- [ ] kw (Cornish)
- [ ] br (Breton)
- [ ] gv (Manx)
- [ ] cel / cel-x-* (Proto-Celtic)
- [ ] eu / eu-x-* (Basque)
- [ ] tr (Turkish)
- [ ] fi (Finnish)
- [ ] hu (Hungarian)
- [ ] ko (Korean)
- [ ] ja (Japanese)
- [ ] zh (Chinese)
- [ ] ms (Malay)
- [ ] ta / ta-x-* (Tamil)
- [ ] kn (Kannada)
- [ ] te (Telugu)
- [ ] ml (Malayalam)
- [ ] si (Sinhala)
- [ ] or (Odia)
- [ ] as (Assamese)
- [ ] mai (Maithili)
- [ ] bho (Bhojpuri)
- [ ] kok (Konkani)
- [ ] sat / sat-x-* (Santali)
- [ ] mni / mni-x-* (Meitei)
- [ ] brx / brx-x-* (Bodo)
- [ ] unr (Mundari)
- [ ] kha / kha-x-* (Khasi)
- [ ] tcy (Tulu)
- [ ] ar related: already in Phase 3

### Phase 6 — Ancient/Reconstructed/Extinct (TODO)
- [ ] ine (Proto-Indo-European)
- [ ] ine-x-italic
- [ ] iir (already in Phase 4)
- [ ] gem-* (already in Phase 1)
- [ ] cel-x-gallaecia / cel-x-goidelic
- [ ] osc (Oscan)
- [ ] xum (Umbrian)
- [ ] xlp (Leptonic?)
- [ ] xaq (Aquitanian)
- [ ] xib (Iberian)
- [ ] xcg (Celtiberian)
- [ ] xtg (Gaulish)
- [ ] xlg (Ligurian ancient)
- [ ] xga (Galatian)
- [ ] xbr (Brythonic)
- [ ] xda (Dacian)
- [ ] xpa (Phrygian)
- [ ] etr (Etruscan)
- [ ] cu (Church Slavonic)
- [ ] cop (already Phase 3)
- [ ] phn (already Phase 3)
- [ ] pal (already Phase 4)
- [ ] peo (already Phase 4)
- [ ] goh (already Phase 1)
- [ ] ang (already Phase 1)
- [ ] non (already Phase 1)
- [ ] osx (already Phase 1)
- [ ] la-x-balkans / la-x-galloitalic / la-x-italia
