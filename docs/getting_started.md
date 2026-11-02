# Getting Started

`transcribe(text, language_code)` returns an IPA string with the stress marks (`ˈ`) in place:

```python
>>> import orthography2ipa
>>> orthography2ipa.transcribe("olá mundo", "pt")
'oˈla ˈmũdu'
```

This page starts from that one call and works out to the rest of the API. It covers the specs and their two maps, beam search, the distance metrics, the command line and the data explorer.

## Why the library has no model weights

Most G2P (grapheme-to-phoneme) tools take one of two forms. One form is a hand-tuned rule set that serves one TTS engine. The other form is a trained sequence model per language, which needs data collection and retraining.

`orthography2ipa` is data. Each language is a JSON file that states, with citations, which graphemes map to which IPA phonemes. A grapheme is a letter, a digraph or a trigraph. The same file states how those phonemes surface as allophones in context. One shared engine with no language-specific code turns that data into transcriptions. To add a language, you write data, not a model or code.

This design has a consequence that you must know first. For an ambiguous spelling, the engine picks the most common reading in the language, not the reading that the context requires. No language model scores the candidates against the neighbouring words. Read the [limitations](index.md#honest-limitations-read-this-before-you-trust-a-tier) before you use the output where a mistake is costly.

## Install

```bash
uv pip install --prerelease=allow orthography2ipa
```

The runtime dependencies are `numpy`, `langcodes` and `ovos-spec-tools`, as `requirements.txt` lists them. The 21-feature distinctive-feature matrix that the distance metrics use is part of the package (`orthography2ipa/feats.py`). Three optional extras add features:

| Extra | Adds | Use it for |
| :--- | :--- | :--- |
| `hf` | `huggingface_hub` | Lexicons fetched from a Hugging Face dataset id ([lexicon.md](lexicon.md)) |
| `validation` | `pydantic` | `orthography2ipa validate` on spec JSON files |
| `portuguese` | `silabificador` | A real Portuguese syllabifier in place of the bundled vowel-group splitter |

## Your first transcription

```python
import orthography2ipa
orthography2ipa.transcribe("olá mundo", "pt")      # 'oˈla ˈmũdu'
orthography2ipa.transcribe("hello world", "en")    # 'ˈhɛləʊ ˈwɔːld'
orthography2ipa.transcribe("bona nuèit", "oc")     # 'ˈbunɔ ˈnɥɛit'
```

`transcribe()` runs a fixed pipeline. It tokenizes each word into graphemes with the spec of the target language. It then picks the most likely IPA for each grapheme, with greedy search by default. Next it applies the spec's allophone rules and stress rules, and the cross-word sandhi rules if the language has any. Data in the language's `LanguageSpec` drives each step, and no hidden model sits behind it. [architecture.md](architecture.md) gives the full order of the stages.

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

Digraphs and trigraphs are keys of their own. The tokenizer matches the longest key first (maximal munch). [tokenizer.md](tokenizer.md) explains the match.

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

The lookup is lazy and cached. Import reads the file names in the data directory and parses no JSON. The loader parses the file of a language the first time a caller asks for it.

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

The score is a cost, and the best path has the lowest cost. A spec without candidate weights costs each candidate by its rank: the first costs 0.0, the second 1.0 and so on. A spec with weights costs a candidate `-log(p)`. [candidate_scoring.md](candidate_scoring.md) gives the rule. Only the word itself informs the ranking, as the [limitations](index.md#honest-limitations-read-this-before-you-trust-a-tier) explain.

`G2P.transcribe_detailed` gives the ranked candidates of each word together with the transcription of the full sentence:

```python
from orthography2ipa import G2P
engine = G2P("pt-PT")
result = engine.transcribe_detailed("um café", search="beam", beam_width=4)
result.ipa                      # 'ˈũ kɐˈfɛ'
result.words[1].candidates[:3]
# (IPAPath('kɐfɛ', score=0.0), IPAPath('kafɛ', score=1.0), IPAPath('sɐfɛ', score=1.0))
```

## Measuring distance between languages

You can compare two languages, or two dialects of one language, on the phoneme inventory, the grapheme map and the allophone overlap:

```python
import orthography2ipa
from orthography2ipa.distance import phonological_distance, segment_distance
# Segment level: how different are two IPA sounds?
segment_distance("p", "b")   # 0.0426: they differ only in voicing
segment_distance("p", "a")   # 1.0: a consonant against a vowel
# Language level: how different are two varieties?
pt_br = orthography2ipa.get("pt-BR")
pt_pt = orthography2ipa.get("pt-PT")
dist = phonological_distance(pt_br, pt_pt)
dist.combined                    # 0.0511: inventory and allophony together
dist.inventory.feature_mean      # 0.0172: phoneme-inventory distance
dist.allophone_sim               # 0.8980: allophone overlap, higher is more alike
dist.grapheme.mean_ipa_distance  # 0.0238: reported, but not in the combined score
```

The grapheme divergence stays out of the combined score, because the spelling of a language is not its sound. [distance.md](distance.md) lists every metric, and [ancestry.md](ancestry.md) gives the variants that descent weights.

## The command line

The `orthography2ipa` command reaches the same functions from the shell:

```bash
orthography2ipa list                           # every language code
orthography2ipa list --family Romance          # matches any step of the family path
orthography2ipa list --family Ibero-Romance    # a sub-branch matches too
orthography2ipa info pt-BR                     # spec summary
orthography2ipa info pt-BR --graphemes         # the full grapheme-to-IPA map
orthography2ipa transcribe en-GB "through" --search beam --beam-width 8
orthography2ipa distance pt-BR pt-PT
```

Each subcommand accepts `--json` for output that a program reads. `orthography2ipa --help` lists the subcommands, and [reference/cli.md](reference/cli.md) documents each flag.

## Finding a language code

Codes are BCP-47 tags (`pt-BR`, `en-GB`, `zh`). The registry also accepts ISO 639-3 codes as aliases:

```python
orthography2ipa.get("por")        # the pt-PT spec
orthography2ipa.get("spa")        # the es-ES spec
orthography2ipa.resolve("pt")     # 'pt-PT': the reference variety for a bare tag
orthography2ipa.resolve("en-NZ")  # 'en-GB': the nearest registered variety
```

These calls list what is available:

```python
orthography2ipa.available_codes()                      # language codes
orthography2ipa.available_codes(include_clades=True)   # adds the clade nodes
orthography2ipa.available_families()                   # codes grouped by family path
```

A clade node (`Romance`, `West Germanic`) is a spec for classification only. It carries no phoneme data, and `available_codes()` leaves it out unless you ask for it. [registry.md](registry.md) describes code resolution and the alias table.

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

The loader derives `family`, and no spec author writes it. It is the chain of clade nodes above the spec in the ancestry graph, joined with `" > "`. [ancestry.md](ancestry.md#clade-nodes-and-the-derived-family) explains the chain.

## Handling unknown codes

```python
try:
    orthography2ipa.get("xx")
except KeyError as e:
    print(e)  # "unsupported language: 'xx.json' not found. Available: {...}"
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

The script writes `docs/explorer.html`, with the data embedded in the page. The same specs and the same results file give the same bytes on each run. The file is not in the repository, because `.gitignore` lists it. The workflow `.github/workflows/pages.yml` builds it on each push to `dev` and publishes it to the `gh-pages` branch as `index.html`. The PER figures on the page show a direction, not a certification. [benchmarks.md](benchmarks.md) and [scoreboard.md](scoreboard.md) say how far each figure goes.

## Where to go next

| You want to | Read |
| :--- | :--- |
| Build a pipeline on the engine | [tokenizer.md](tokenizer.md), [architecture.md](architecture.md) |
| Add or correct a language | [adding_a_language.md](adding_a_language.md) |
| Decide if a language is accurate enough to ship | [quality_tiers.md](quality_tiers.md), [scoreboard.md](scoreboard.md) |
| Read every field of `LanguageSpec` | [data_model.md](data_model.md) |
| Force the pronunciation of a word | [lexicon.md](lexicon.md) |

---
[Home](index.md) · [Architecture →](architecture.md)
