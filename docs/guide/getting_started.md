# Getting Started

This page starts from one call, `transcribe()`, and works out to the rest of the API. It covers the specs and their two maps, beam search, language lookup, the command line, plugins and the data explorer.

## Why the library has no model weights

Most G2P (grapheme-to-phoneme) tools take one of two forms. One form is a hand-tuned rule set that serves one TTS engine. The other form is a trained sequence model per language, which needs data collection and retraining.

`orthography2ipa` is data. Each language is a JSON file that states which graphemes map to which IPA phonemes. A grapheme is a letter, a digraph or a trigraph. The same file states how those phonemes surface as allophones in context. To add a language, you write data, not a model or code.

This design has a consequence that you must know first. For an ambiguous spelling, the engine picks the most common reading in the language, not the reading that the context requires. No language model scores the candidates against the neighbouring words. Read the [limitations](../index.md#honest-limitations-read-this-before-you-trust-a-tier) before you use the output where a mistake is costly.

## Install

The [README](../../README.md#install) gives the install command. The runtime dependencies are `numpy`, `langcodes` and `ovos-spec-tools`, as `requirements.txt` lists them. The distinctive-feature matrix that the distance metrics use is part of the package (`orthography2ipa/feats.py`). These optional extras add features:

| Extra | Adds | Use it for |
| :--- | :--- | :--- |
| `hf` | `huggingface_hub` | Lexicons fetched from a Hugging Face dataset id ([lexicon.md](lexicon.md)) |
| `validation` | `pydantic` | `orthography2ipa validate` on spec JSON files |
| `portuguese` | `silabificador` | A real Portuguese syllabifier in place of the bundled vowel-group splitter |
| `test` | `pytest` and the tools that the gold-set loaders need | The test suite of a clone ([CONTRIBUTING.md](../../CONTRIBUTING.md#tests)) |

## Your first transcription

`transcribe(text, language_code)` returns an IPA string with the stress marks (`ˈ`) in place:

```python
import orthography2ipa
orthography2ipa.transcribe("hello world", "en")    # 'ˈhɛləʊ ˈwɔːld'
orthography2ipa.transcribe("bona nuèit", "oc")     # 'ˈbunɔ ˈnɥɛit'
```

`transcribe()` runs a fixed pipeline. It tokenizes each word into graphemes with the spec of the target language. It then picks the most likely IPA for each grapheme, with greedy search by default. Next it applies the spec's allophone rules and stress rules, and the cross-word sandhi rules if the language has any. Data in the language's `LanguageSpec` drives each step, and no hidden model sits behind it. [architecture.md](../engine/architecture.md) gives the full order of the stages.

The library does not normalise text. A caller that needs number expansion or diacritic restoration passes a `normalizer` to `G2P` or installs a normalize plugin.

## The two maps: graphemes and allophones

Each language spec keeps two maps apart. The grapheme map says which phonemes a spelling can stand for. The allophone map says how a phoneme surfaces in context. Transcription, from text to phonemes, reads the grapheme map. A model of pronunciation, from phoneme to surface form, reads the allophone map. G2P systems that mix the two get bugs from it, so this library keeps them apart.

### The grapheme map

Each grapheme key maps to a list of IPA phonemes, and the first entry is the most common one:

```python
import orthography2ipa
en = orthography2ipa.get("en-GB")
en.graphemes["th"]      # ['θ', 'ð']: the sounds of "thin" and "this"
en.graphemes["c"]       # ['k', 's']
es = orthography2ipa.get("es-ES")
es.graphemes["c"]       # ['k', 'θ']: Castilian /k/ or /θ/
es.graphemes["ll"]      # ['ʝ']: the yeísmo merger of ⟨ll⟩ with ⟨y⟩
pt_br = orthography2ipa.get("pt-BR")
pt_br.graphemes["lh"]   # ['ʎ']
```

Digraphs and trigraphs are keys of their own. The tokenizer matches the longest key first (maximal munch). [tokenizer.md](../engine/tokenizer.md) explains the match.

### The allophone map

The allophone map lists the surface forms of a phoneme after the engine chooses it:

```python
en.allophones["t"]      # ['t', 'tʰ', 'ʔ', 'ɾ']
# tʰ: aspirated, word-initial. ʔ: glottalised, before a pause.
# ɾ: flapped between vowels, as in American "butter".
es.allophones["b"]      # ['b', 'β']
# b: after a pause or a nasal. β: between vowels (lenition).
```

## Fetching a language spec

`transcribe()` is a wrapper. To rank alternatives, inspect allophones or compare languages, start from `get()`, which returns the `LanguageSpec`:

```python
import orthography2ipa
en = orthography2ipa.get("en-GB")     # by BCP-47 code
eng = orthography2ipa.get("eng")      # ISO 639-3 alias: the same spec object
pt_br = orthography2ipa.get("pt-BR")  # a regional variety
```

## Finding a language code

Codes are BCP-47 tags (`pt-BR`, `en-GB`, `zh`), and ISO 639-3 codes work as aliases. The set of specs changes with each data change, so no page lists it by hand. Use one of these live sources:

| Source | What it gives |
| :--- | :--- |
| `orthography2ipa list` | Each language code, and `--family <name>` filters by any step of the family path |
| `orthography2ipa.available_codes()` | The language codes as a sorted list |
| `orthography2ipa.available_families()` | The codes grouped by family path |
| The [explorer](#browsing-the-specs-in-the-explorer) | One browsable page for each spec |
| [languages/index.md](../languages/index.md) | The languages that have a page of notes of their own |

To see which spec a code reaches before you load it, call `resolve()`:

```python
orthography2ipa.resolve("por")    # 'pt-PT'
orthography2ipa.resolve("pt")     # 'pt-PT'
orthography2ipa.resolve("en-NZ")  # 'en-GB'
```

`get()` raises `KeyError` for a code that reaches no spec:

```python
try:
    orthography2ipa.get("xx")
except KeyError as e:
    print(e)  # "unsupported language: 'xx.json' not found. Available: {...}"
```

An unregistered regional tag such as `en-NZ` reaches the nearest registered variety. Pass `strict=True` to `get()` to refuse that guess and get the `KeyError`. [registry.md](../reference/registry.md) gives the resolution order, the curated defaults and the alias table.

## Ranking ambiguous spellings with beam search

`transcribe()` uses greedy search, so it takes the best candidate at each grapheme. For the full ranked list, use `PhonetokTokenizer`. The list helps you debug a bad transcription or rescore the output downstream.

```python
from orthography2ipa import get
from orthography2ipa.phonetok import PhonetokTokenizer
tok = PhonetokTokenizer(get("en-GB"))
tok.ipa_best("through")   # 'θɹɔː'
for path in tok.ipa_beam("through", beam_width=8):
    print(path.ipa, path.score)
# θɹɔː 0.0
# ðɹɔː 1.0
# θɹəʊ 1.0
# ðɹəʊ 2.0
# θɹʌf 2.0
# ðɹʌf 3.0
# θɹɒf 3.0
# θɹaʊ 4.0
```

The score is a cost, and the best path has the lowest cost. A spec without candidate weights costs each candidate by its rank: the first costs 0.0, the second 1.0 and so on. A spec with weights costs a candidate `-log(p)`. [lattice.md](../engine/lattice.md#how-cost-works) gives the rule. Only the word itself informs the ranking, as the [limitations](../index.md#honest-limitations-read-this-before-you-trust-a-tier) explain.

`G2P.transcribe_detailed` gives the ranked candidates of each word together with the transcription of the full sentence:

```python
from orthography2ipa import G2P
engine = G2P("pt-PT")
result = engine.transcribe_detailed("um café", search="beam", beam_width=4)
result.ipa                      # 'ˈũ kɐˈfɛ'
result.words[1].candidates[:3]
# (IPAPath('kɐfɛ', score=0.0), IPAPath('kafɛ', score=1.0), IPAPath('sɐfɛ', score=1.0))
```

To re-cost the candidates with your own rules, write a `LatticeRescorer`. [lattice.md](../engine/lattice.md) explains when to write one and when to keep a separate tokenizer.

## Measuring distance between languages

The `orthography2ipa.distance` module compares two languages, or two dialects of one language, on several independent axes. [distance.md](distance.md) describes each metric and its limits, and [ancestry.md](../specs/ancestry.md) gives the variants that descent weights. The command line gives the phonological distance of two specs:

```bash
orthography2ipa distance pt-BR pt-PT
```

```text
Brazilian Portuguese (pt-BR) ↔ European Portuguese (pt-PT)
  combined:   0.0511
  inventory:  0.0172
  allophone:  0.8980
  grapheme:   0.0238   (orthography — not part of combined)
```

## The command line

The `orthography2ipa` command reaches the same functions from the shell:

```bash
orthography2ipa list                           # every language code
orthography2ipa list --family Romance          # matches any step of the family path
orthography2ipa list --family Ibero-Romance    # a sub-branch matches too
orthography2ipa info pt-BR                     # spec summary
orthography2ipa info pt-BR --graphemes         # the full grapheme-to-IPA map
orthography2ipa transcribe en-GB "through" --search beam --beam-width 8
```

Each subcommand accepts `--json` for output that a program reads. `orthography2ipa --help` lists the subcommands, and [reference/cli.md](../reference/cli.md) documents each flag.

## Inspecting language metadata

Each `LanguageSpec` carries its provenance and its ancestry together with the phoneme data:

```python
es = orthography2ipa.get("es-ES")
es.name      # 'Castilian Spanish'
es.family    # 'Indo-European > Italic > Romance > Ibero-Romance'
es.script    # 'Latin'
es.quality   # QualityTier.PRODUCTION: see quality_tiers.md
es.location  # Location(latitude=40.416944, longitude=-3.703333, source='wikidata', ...)
for anc in es.get_ancestors():
    print(anc)
# Ancestor('es-ES-x-medieval', parent, w=0.85)
# Ancestor('xaq', substrate, w=0.06)
# Ancestor('got', superstrate, w=0.04)
# Ancestor('xaa', adstrate, w=0.06)
```

The loader derives `family`, and no spec author writes it. It is the chain of clade nodes above the spec in the ancestry graph, joined with `" > "`. A clade node (`Romance`, `West Germanic`) is a spec for classification only, and `available_codes()` leaves it out unless you pass `include_clades=True`. [ancestry.md](../specs/ancestry.md#clade-nodes-and-the-derived-family) explains the chain.

## Installing and writing a plugin

A plugin takes over one stage of the pipeline for the languages that it claims. [architecture.md](../engine/architecture.md#pluggable-steps) lists the stages and their base classes. To install a plugin, install the package that ships it. The `portuguese` extra installs `silabificador`, and the bundled entry point then gives the Portuguese codes a real syllabifier:

```bash
uv pip install --prerelease=allow 'orthography2ipa[portuguese]'
```

`orthography2ipa.who_answers(code)` then reports which syllabifier and which rescorers answer for a code.

To write a plugin, do these steps:

1. Subclass the base class of the stage. Set `language_codes`, and set `priority` if another plugin claims the same codes.
2. Check the class with the contract checks in `orthography2ipa.conformance`. `assert_syllabifier_conforms` fails if a syllabifier does not join back to the word or if it changes the transcription. `assert_rescorer_conforms` checks a rescorer.
3. Declare the class as an entry point in the `pyproject.toml` of your package, in the group of the stage.
4. For a stage other than `syllabify`, name the plugin by its entry-point name in the `plugins` field of the spec, or pass `G2P(code, plugins={"<stage>": "<name>"})`.

A syllabifier for Italian that closes a syllable after each vowel run passes the check:

```python
import re
from orthography2ipa import SyllabifierPlugin
from orthography2ipa.conformance import assert_syllabifier_conforms

V = "aeiouàèéìòù"

class ItalianSyllabifier(SyllabifierPlugin):
    language_codes = ["it-IT"]

    def syllabify(self, word, lang=None):
        return re.findall(f"[^{V}]*[{V}]+(?:[^{V}]+$)?", word) or [word]

plugin = ItalianSyllabifier()
plugin.syllabify("amore")    # ['a', 'mo', 're']
assert_syllabifier_conforms(plugin, words=["amore", "casa", "parlare"])   # passes, returns None
```

The package that ships it declares the entry point:

```toml
[project.entry-points."orthography2ipa.syllabify"]
italian = "my_package.syllabifier:ItalianSyllabifier"
```

## Browsing the specs in the explorer

The language data explorer is one HTML page that shows each registered `LanguageSpec`. It is published at <https://tigregotico.pt/orthography2ipa/>. The page needs no network after it loads, so you can also open a local copy from disk.

The sidebar lists each code. You can search it, and filter it by family, script or quality tier. The page for one language shows these sections:

| Section | Content |
| :--- | :--- |
| Header | Name, code, family, script and the quality tier |
| Gold benchmark results | Each scored row from `benchmarks/results.json`: dataset, `n`, PER, 95% CI, exact match, provenance |
| Ancestry | The parent and the weighted ancestors, as links to their specs |
| Mappings | The grapheme table, the allophone map, the positional overrides and the allophone rules |
| Sources | The citations behind the spec: author, year, title, pages and URL |
| Notes | The notes of the spec, with input-contract warnings (Pinyin, jamo, tashkeel) set apart |

The address bar holds the selected language as a fragment, for example `#eu-x-zuberera`. Share that URL to open one language.

To build the page on your machine, run this command from a checkout:

```bash
python scripts/gen_explorer.py
```

The script writes `docs/explorer.html`, with the data embedded in the page. The same specs and the same results file give the same bytes on each run. The file is not in the repository, because `.gitignore` lists it. The workflow `.github/workflows/pages.yml` builds it on each push to `dev` and publishes it to the `gh-pages` branch as `index.html`. [benchmarks.md](../evaluation/benchmarks.md) and [scoreboard.md](../evaluation/generated/scoreboard.md) say how far each PER figure on the page goes.

## Where to go next

| You want to | Read |
| :--- | :--- |
| Build a pipeline on the engine | [tokenizer.md](../engine/tokenizer.md), [architecture.md](../engine/architecture.md), [lattice.md](../engine/lattice.md) |
| Feed the lattice to a learned model | [lattice.md](../engine/lattice.md#feature-export-for-a-learned-model) |
| Add or correct a language | [spec_authoring.md](../contributing/spec_authoring.md) |
| Decide if a language is accurate enough to ship | [quality_tiers.md](../specs/quality_tiers.md), [scoreboard.md](../evaluation/generated/scoreboard.md) |
| Read every field of `LanguageSpec` | [data_model.md](../specs/data_model.md) |
| Force the pronunciation of a word | [lexicon.md](lexicon.md) |

---
[Home](../index.md) · [Lexicons and forced pronunciations →](lexicon.md)
