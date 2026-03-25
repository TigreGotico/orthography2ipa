
# orthography2ipa — FAQ

## Installation

**Q: How do I install orthography2ipa?**

```bash
pip install orthography2ipa
# or
uv pip install orthography2ipa
```

**Q: Why does installing from source not include the language data files?**

This was a packaging bug (T-01). Fixed in `0.2.0a1`: `pyproject.toml` now declares `[tool.setuptools.package-data]` so all `data/*.json` files are included in the wheel.

---

## Script Types

**Q: What is `"script": "IPA-reconstruction"` and `"script_type": "reconstruction"`?**

Proto-languages (e.g., Proto-Indo-European, Proto-Germanic, Proto-Semitic) were never written. Their phonological inventories are scholarly reconstructions notated in IPA. These files use `"script": "IPA-reconstruction"` to distinguish them from languages with attested writing systems (Latin, Arabic, etc.), and `"script_type": "reconstruction"` to flag them programmatically. Attested ancient languages (e.g., Gallaecian, Lusitanian) that survive in Latin-alphabet inscriptions keep `"script": "Latin"`.

---

## Supported Languages

**Q: Which languages are supported?**

Run `orthography2ipa.available_codes()` to get the full list. As of `0.2.0a1`, the registry includes Ibero-Romance languages and their ancestors/dialects: `pt-PT`, `pt-BR`, `es-ES`, `ast`, `mwl`, `gl`, `oc`, `an`, `ext`, `la` and many variants. Arabic (`arb`), Gothic (`got`), and Ancient Greek (`grc`) are also present.

**Q: Is English supported?**

`en-GB.json` is not yet populated. `get("en-GB")` raises `KeyError`. This is tracked in T-07 scope.

**Q: Is Rionorese supported?**

Yes. `get("ast-PT-x-rionor")` returns the full Rionorese spec (T-07, completed). Graphemes, allophones, and positional rules are populated from `ipa_research/rionorese_phonemizer.py`. Key features: full betacism (`v→b`), dental fricative merger (`z/ç/c+e/i→θ`), `ch→ʃ` (not `tʃ`), positional rhotics (trill word-initial, flap intervocalic), `tch→tʃ` trigraph, Leonese diphthongs `iê/ie→je`, `uâ→wa`, `uô→wɔ`.

**Q: Is Guadramilese supported?**

Yes. `get("ast-PT-x-guadramil")` returns the full Guadramilese spec (T-08, completed). Guadramilese is phonologically near-identical to Rionorese (~85% shared features) and inherits all grapheme rules via `graphemes_base: ast-PT-x-rionor`. The key divergences are morphological (article system: `o` not `al`; 3pl imperfect: `-ien` not `-ian`; `ir` imperfect: `diba/diban`) and are documented in the JSON `notes` field. Source: Miro (2026) Paper III.

**Q: Is Barranquenho supported?**

Yes. `get("ext-PT-x-barrancos")` returns the Barranquenho spec (T-09, completed). Barranquenho is a Portuguese-base contact variety with heavy Spanish/Andalusian adstrate. Key overrides from pt-PT: betacism (`v→b`), aspirated `h→h` (not silent), `rr→r` and word-initial `r→r` (alveolar trill, not uvular ʁ), `tch→tʃ` trigraph. Sibilants follow Portuguese conventions (`c/ç→s`, `z→z`, `g+e/i→ʒ`), not Spanish/Rionorese (`θ`, `x`). Source: 2025 Convenção Ortográfica do Barranquenho and `g2p-barranquenho` phonemizer.

**Q: How do I use the bundled Rionorese IPA dictionary?**

```python
import orthography2ipa
lex = orthography2ipa.load_lexicon("ast-PT-x-rionor")
# lex is a Dict[str, str] — word → IPA string
print(lex["abajo"])   # "aˈbaʒo"
print(len(lex))       # 917
```

The dictionary contains 917 entries: 141 attested (Macias 2003) and 776 rule-derived (Paper II). It is bundled as `data/lexicons/ast-PT-x-rionor.csv` in the package. Use `load_lexicon()` for lexicon lookup before falling back to `PhonetokTokenizer.ipa_best()` for unknown words.

**Q: Why does `benhir` (Rionorese "to come") not tokenize `nh` correctly?**

The parent's `en→ẽ` nasal-vowel digraph is matched greedily by the trie before `nh→ɲ` can be seen. The tokenizer does maximal-munch left-to-right, so `b+en+h+i+r` rather than `b+e+nh+i+r`. This is a known limitation: the flat grapheme table cannot express "match `nh` only when not preceded by a vowel nasal." The `positional_graphemes` system and `LanguageSpec.resolve_grapheme()` are unaffected — `nh→ɲ` is correct there.

---

## Language Codes

**Q: Can I use ISO 639-3 three-letter codes?**

Yes. `get("por")` resolves to `get("pt-PT")`. A manual alias table handles common ISO 639-3 codes; the `langcodes` library (T-05, partially implemented) will eventually handle the full BCP-47 normalization. Private-use subtags (`ast-PT-x-rionor`) always use the manual table.

---

## How to Add a Language

**Q: How do I add support for a new language?**

Create a JSON file at `orthography2ipa/data/{code}.json` following the schema in `data/SCHEMA.md`. The file is picked up automatically by the registry at import time. Key fields: `code`, `name`, `family`, `script`, `graphemes`, `allophones`. Optional: `positional_graphemes`, `ancestors`, `parent`, `graphemes_base`, `allophones_base`.

See `docs/adding_a_language.md` for a step-by-step guide.

---

## Usage

**Q: What is the difference between `ipa_best()` and `ipa_beam()`?**

`PhonetokTokenizer.ipa_beam(word, beam_width=N)` returns the top-N IPA path candidates as `IPAPath` objects, ordered by probability. `ipa_best(word)` is shorthand for `ipa_beam(word, beam_width=1)[0].ipa` — returns a single string.

**Q: How do I use orthography2ipa with eSpeak-NG output?**

eSpeak-NG output is already IPA — you do not need `PhonetokTokenizer` to parse it. Use `orthography2ipa.debias_lisbon(ipa)` to remove Lisbon-dialect artifacts from eSpeak output, then `orthography2ipa.apply_transform(ipa, profile_code)` to apply a dialect transform.

```python
import orthography2ipa

# eSpeak-NG output (biased toward Lisbon):
espeak_out = "u βɛˈʎu ˈveɾdɨ"  # "O velho verde"

# De-bias, then apply Northern (Transmontano) transform:
neutral = orthography2ipa.debias_lisbon(espeak_out)
northern = orthography2ipa.apply_transform(neutral, "transmontano")
```

See `orthography2ipa.available_profiles()` for the full list of 15 dialect profiles.

**Q: What dialect profiles are available?**

The `orthography2ipa.transforms` module (T-13–T-16) implements 15 dialect profiles:

| Profile key | Variety |
| :--- | :--- |
| `estremenho` | Centro-Litoral / Estremenho (neutral — closest to standard) |
| `lisbon` | Lisbon / Lisboa |
| `ribatejano` | Ribatejano / Baixo-Beirão / Alentejano |
| `beira_baixa` | Beira-Baixa / Alto-Alentejo (u→y, vowel shifts) |
| `algarve_barlavento` | Barlavento Algarvio (simultaneous chain shift) |
| `northern` | Northern Portuguese (betacism only) |
| `transmontano` | Transmontano / Alto-Minhoto (4-sibilant + ch affrication) |
| `baixo_minhoto` | Baixo-Minhoto / Duriense / Beirão (2-sibilant) |
| `porto` | Porto / Douro Litoral (e→je, o→wo diphthongization) |
| `beira_alta` | Beira-Alta (2-sibilant, no diphthongization) |
| `galician` | Eastern Galician (betacism + sibilant devoicing) |
| `galician_west` | Western Galician (+ geada ɡ→x) |
| `leonese` | Leonese enclave (common rules) |
| `rionorese` | Rionorese — full Leonese + article o→al |
| `guadramilese` | Guadramilese — Leonese + pronoun eu→you |

**Q: How do I use CLUP allophone data with the transforms?**

Use `load_clup_profile()` to read a CLUP allophone profile for a specific region, then pass it as `allophone_weights` to `apply_transform()`:

```python
from orthography2ipa.transforms import load_clup_profile, apply_transform

weights = load_clup_profile("Vizela", "/path/to/clup_analysis_allophone_flags.csv")
result = apply_transform(espeak_ipa, "northern", allophone_weights=weights)
```

When `allophone_weights` is provided and the region shows high spirantization (rate > 0.02), the de-biasing step preserves spirants (β, ð, ɣ) instead of normalizing them — because they are genuine dialectal features, not phonemizer artifacts.

---

## Universal Language Coverage (2026-03-10)

**Q: How many languages does orthography2ipa now support?**

308 language specs are loadable via `available_codes()` (added `ar.json`, `ms.json`). Of these, ~50 are production-quality (regression-tested), ~20 are research-quality (validated positional rules), and ~236 are skeleton/stub quality (promoted from `dump/langs/` with automated metadata enrichment).

**Q: What scripts are supported?**

Latin (184 specs), Arabic (37), Cyrillic (18), Devanagari (9), IPA-reconstruction (8 proto-languages), Bengali (2), Greek (2), Kannada (2), plus Hangul, Hanzi/Pinyin, Kana, Tamil, Telugu, Malayalam, Gujarati, Gurmukhi, and more. The `ScriptType` enum classifies each script as `ALPHABET`, `ABJAD`, `ABUGIDA`, `SYLLABARY`, `LOGOGRAPHIC`, `FEATURAL`, `MIXED`, or `RECONSTRUCTION`.

**Q: What new features were added?**

- `QualityTier` enum: classifies specs as `STUB`, `SKELETON`, `RESEARCH`, or `PRODUCTION`
- `ScriptType` enum: typological classification of writing systems
- `SandhiRule` dataclass + `SandhiEngine`: cross-word-boundary phonological rules (liaison, sandhi)
- `script_distance` module: measures typological distance between writing systems
- `tone_distance()`: Jaccard distance on tone inventories
- `orthographic_distance()`: combines grapheme divergence with script distance
- `G2PPlugin` ABC: plugin architecture for complex language-specific G2P
- `ArabicG2PPlugin`: rule-based Arabic-to-IPA (consonants, harakat, sun-letter assimilation)
- 23-feature system (was 21): added `click` and `nasal_vowel` features
- ~20 new phones: clicks (ǀ ǁ ǂ ǃ ʘ), ejectives (pʼ tʼ kʼ qʼ), prenasalized stops (ᵐb ⁿd ᵑɡ), nasalized vowels (ã ẽ ĩ õ ũ)
- 6 new modifiers: nasalization (̃), voicelessness (̥), palatalization (ʲ), labialization (ʷ), prenasalization (ⁿ), ejective (ʼ)
- NFC normalization in tokenizer (handles Arabic combining marks, accented Latin)
- `LanguageSpec` new fields: `quality`, `script_type`, `inherent_vowel`, `iso639_3`, `sandhi_rules`, `tone_inventory`
- `GraphemePosition.DEFAULT` and `GraphemePosition.NUCLEUS` added

**Q: How was the stub data promoted?**

The `scripts/validate_and_promote.py` script enriched each of the 256 stubs in `dump/langs/` with metadata (`quality`, `script_type`, `inherent_vowel`, `iso639_3`) and copied them to `data/`. The JSON loader was made lenient for stubs/skeletons: missing ancestry references no longer cause hard failures.

**Q: What about Arabic support?**

An `ArabicG2PPlugin` implements rule-based Arabic-to-IPA transcription, handling diacritized input (harakat mapping), long vowels, and shadda gemination. A tashkeel (automatic diacritization) ONNX wrapper is stubbed for future integration. GPL-free Arabic utilities (`arabic_utils.py`) replace `pyarabic` dependency. Install with `pip install orthography2ipa[arabic]` for ONNX support. The Arabic plugin is now discoverable via entry_points in `pyproject.toml`.

**Q: Which languages have sandhi rules?**

French (`fr-FR.json`, 6 rules: z/t/n/r/p-liaison + enchaînement), Portuguese (`pt-PT.json`, 3 rules: coda-s voicing, resyllabification, schwa elision), and Arabic (`arb.json`, 3 rules: sun-letter assimilation, hamzat al-wasl, pausal tanwin). Use `spec.sandhi_rules` to access them or `SandhiEngine(spec.sandhi_rules).apply(words_ipa)` to apply.

**Q: How does inherent vowel handling work for abugidas?**

When `spec.inherent_vowel` is set (e.g., `"ə"` for Hindi), the tokenizer automatically appends the inherent vowel after consonant graphemes unless a virama/halant character follows. This enables Devanagari, Bengali, Tamil, and other Brahmic scripts without script-specific code — it's entirely data-driven via the JSON `inherent_vowel` field.

**Q: What is the current test count?**

7375 tests pass, 0 skipped, 0 failures. All 14 proto-language specs now have populated graphemes, allophones, `script: "IPA-reconstruction"`, and `script_type: "reconstruction"`. Previously 322 tests were skipped; all have been resolved.

---

## Documentation

**Q: Where is each module documented?**

`docs/architecture.md` has a section for every module with line-number citations: `types.py`, `registry.py`, `json_loader.py`, `phonetok.py`, `distance.py`, `feats.py`, `transforms.py`, `script_distance.py`, `sandhi.py`, `lm.py`, `g2p_plugin.py`. `docs/index.md` has Key Classes and Key Functions tables with all public types and functions.

**Q: Why do the docs reference Python module files like `en.py` that don't exist?**

They no longer do. As of 2026-03-25, all references to the pre-migration Python language modules were replaced with the current JSON-based data architecture. If you find any stale reference, file a bug.

---

## Testing

**Q: Why are some tests skipped?**

0 tests are skipped. Proto-languages now have `script: "IPA-reconstruction"` and populated graphemes/allophones. English tests (`en-GB`) use dynamic `pytest.skip()` when grapheme data is unavailable instead of unconditional `@pytest.mark.skip()`. Run `uv run --no-sync pytest tests/ -q` to verify.

**Q: Why was `test_distance.py` previously all-skipped?**

All 7 distance test classes were decorated with `@pytest.mark.skip()` from the initial scaffold. Fixed in Phase 1 (T-04): skips removed, fixtures corrected (no French or Japanese JSON exists — replaced with Occitan `oc` and Classical Arabic `arb`), and one assertion updated to use Jaccard distance instead of `feature_mean` for relatedness comparison.

---

## Version

**Q: What version is this?**

`0.2.0a1`. Check with `python -c "import orthography2ipa; print(orthography2ipa.__version__)"`.

Previously `__init__.py` hardcoded `"0.1.0"` regardless of `version.py`. Fixed in T-02.

---

## Temporal Distance

**Q: How does the time dimension work in distance metrics?**

`LanguageSpec` now has an optional `timespan: TimeSpan` field with `start_year` and `end_year` (use `None` for living languages). Three new capabilities build on this:

1. **`temporal_distance(spec_a, spec_b)`** — Jaccard-interval distance [0, 1] between attestation periods. Returns `None` if either language lacks timespan data. Languages with zero temporal overlap return `1.0`; fully coincident periods return `0.0`.

2. **`ancestry_similarity(..., temporal_decay=True)`** — Applies exponential weight decay (`exp(-gap/halflife)`) to each ancestor link based on the time gap between ancestor's era and the descendant's start. Default `halflife=1000` years. Ancient ancestors (e.g. Proto-Germanic for West Frisian, ~1300-year gap) are weighted ≈0.49× their static value.

3. **`weighted_full_distance(..., w_temporal=0.0)`** — `w_temporal=0.0` by default (backward-compatible). Set to a positive value to fold `temporal_distance` into the combined score. If timespan data is missing for either language, the component is automatically excluded and remaining weights renormalised.

**Q: How do I add a timespan to a JSON file?**

Add a `"timespan"` key at the top level:
```json
"timespan": {"start_year": 450, "end_year": 1150}
```
For living languages set `"end_year": null`. Use negative values for BCE (e.g. `-500`). Currently ~29 files in the Germanic chain have timespan data.

---

## Tone Inventory

**Q: Which languages have tone_inventory data?**

As of 2026-03-10, `zh.json` (Mandarin Chinese) includes a `tone_inventory` field mapping Chao tone letters to tone names (1st through 5th/neutral). Other tonal languages (Vietnamese, Thai, Yoruba, Burmese) do not yet have JSON spec files in `orthography2ipa/data/`.
