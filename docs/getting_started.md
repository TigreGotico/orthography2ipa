# Getting Started

## The problem, in one call

Say you're building a TTS pipeline and need to know how a Portuguese
sentence sounds before you synthesize it:

```python
>>> import orthography2ipa
>>> orthography2ipa.transcribe("olá mundo", "pt")
'oˈla ˈmundu'
```

That's it — `transcribe(text, language_code)` returns an IPA string with
stress marks (`ˈ`) already placed. The rest of this page walks from that
one call out to the full API: language specs, the tokenizer underneath
`transcribe()`, beam search over ambiguous spellings, and the distance
metrics used to compare languages.

## Install

```bash
pip install orthography2ipa
```

The only runtime dependency is **phonematcher**, which supplies the
21-feature distinctive-feature system the distance metrics use. It's
installed automatically.

## What just happened

`transcribe()` ran a fixed pipeline: normalize the input text, tokenize
it into graphemes using the target language's spec, pick the most
likely IPA phoneme for each grapheme (greedy search by default), attach
stress marks where the language's spec declares stress rules, apply
cross-word sandhi if the language has any, and join the result. Every
step is driven by data in the language's `LanguageSpec` — there's no
hidden model behind it.

```python
orthography2ipa.transcribe("hello world", "en")   # 'hɛllɒ wɔːɹld'
orthography2ipa.transcribe("bona nuèit", "oc")     # 'ˈbunɔ ˈnyɛjt'
```

## Fetching a language spec directly

`transcribe()` is a convenience wrapper. Most non-trivial use — ranking
alternatives, inspecting allophones, comparing languages — starts from
`get()`, which returns the underlying `LanguageSpec`:

```python
import orthography2ipa

en = orthography2ipa.get("en-GB")     # by BCP-47 code
eng = orthography2ipa.get("eng")      # ISO 639-3 alias — same spec
pt_br = orthography2ipa.get("pt-BR")  # regional variety
```

Lookups are lazy and cached: importing the package costs nothing, and
each language's JSON file is parsed only the first time it's requested.

### Grapheme → IPA mappings

Each grapheme key maps to a *list* of possible IPA phonemes — the first
entry is the most common:

```python
en.graphemes["th"]      # ['θ', 'ð']   — voiceless vs. voiced dental fricative
en.graphemes["c"]       # ['k', 's']
es = orthography2ipa.get("es-ES")
es.graphemes["c"]       # ['k', 'θ']   — Castilian /k/ or /θ/
es.graphemes["ll"]      # ['ʝ']        — modern yeísmo merger of ⟨ll⟩ with ⟨y⟩
pt_br.graphemes["lh"]   # ['ʎ']
```

Digraphs and trigraphs are first-class keys, matched by maximal munch
(longest orthographic unit first) — see [tokenizer.md](tokenizer.md) for
how that's implemented.

### Allophone inventories

Allophones describe how a *phoneme*, once chosen, actually surfaces
depending on context:

```python
en.allophones["t"]      # ['t', 'tʰ', 'ʔ', 'ɾ']
# tʰ aspirated (word-initial), ɾ flapped (intervocalic, US), ʔ glottalised (pre-pausal)

es.allophones["b"]      # ['b', 'β']
# b after pause/nasal, β intervocalic (lenition)
```

## Ranking ambiguous spellings with beam search

`transcribe()` uses greedy search — it always takes the single most
likely candidate at each grapheme. When you need the full ranked list
(useful for debugging a bad transcription, or for downstream re-scoring),
use `PhonetokTokenizer` directly:

```python
from orthography2ipa import get
from orthography2ipa.phonetok import PhonetokTokenizer

tok = PhonetokTokenizer(get("en-GB"))

tok.ipa_best("through")   # 'θɹɔː'

for path in tok.ipa_beam("through", beam_width=8):
    print(path.ipa, path.score)
# θɹɔː 0.0
# ðɹɔː 1.0
# θɹoʊ 1.0
# ðɹoʊ 2.0
# θɹʌf 2.0
# ...
```

Score is a rank-distance, not a probability — 0.0 is the top candidate,
and each step away from it costs 1.0 per grapheme substitution. This is
the naive-ordering limitation mentioned in [index.md](index.md#honest-limitations-read-this-before-you-trust-a-tier):
there's no context beyond the word itself informing the ranking.

For per-word candidates alongside a full sentence transcription, use
`G2P.transcribe_detailed`:

```python
from orthography2ipa import G2P

engine = G2P("pt-PT")
result = engine.transcribe_detailed("um café", search="beam", beam_width=4)
result.ipa                  # 'ˈum kɐˈfɛ'
result.words[1].candidates  # ranked IPAPath alternatives for "café"
```

## Measuring distance between languages

Two languages (or two dialects of the same language) can be compared
across phoneme inventory, grapheme mapping, and allophone overlap:

```python
from orthography2ipa.distance import phonological_distance, segment_distance

# Segment-level: how different are two IPA sounds?
segment_distance("p", "b")   # 0.0426 — differ only in voicing
segment_distance("p", "a")   # 1.0    — consonant vs. vowel, maximally different

# Language-level: how different are two varieties overall?
pt_pt = orthography2ipa.get("pt-PT")
dist = phonological_distance(pt_br, pt_pt)
dist.combined                    # 0.046 — near-identical
dist.inventory.feature_mean      # phoneme-inventory distance
dist.grapheme.mean_ipa_distance  # grapheme-mapping divergence
dist.allophone_sim               # allophone-overlap similarity (higher = more similar)
```

See [distance.md](distance.md) for the full metric catalogue and
[ancestry.md](ancestry.md) for phylogenetically-weighted variants.

## The command line

Everything above is also reachable from the shell once the package is
installed:

```bash
orthography2ipa list                          # every language code
orthography2ipa list --family Romance          # filter by family
orthography2ipa info pt-BR                     # spec summary
orthography2ipa info pt-BR --graphemes         # full grapheme→IPA map
orthography2ipa transcribe en-GB "through" --search beam --beam-width 8
orthography2ipa distance pt-BR pt-PT
```

Every subcommand accepts `--json` for machine-readable output. Run
`orthography2ipa --help` for the full list.

## Finding a language code

Codes are **BCP-47** (`pt-BR`, `en-GB`, `zh`), with ISO 639-3 three-letter
codes accepted as aliases:

```python
orthography2ipa.get("por")   # → resolves to the pt-PT spec
orthography2ipa.get("spa")   # → resolves to the es-ES spec
orthography2ipa.resolve("pt")     # 'pt-PT' — reference variety for a bare tag
orthography2ipa.resolve("en-NZ")  # 'en-GB' — nearest registered variety
```

To browse what's available:

```python
orthography2ipa.available_codes()      # every registered code
orthography2ipa.available_families()   # codes grouped by language family
```

or see the full table in [registry.md](registry.md).

## Inspecting language metadata

Every `LanguageSpec` carries provenance and ancestry alongside the
phoneme data:

```python
es = orthography2ipa.get("es-ES")
es.name      # 'Castilian Spanish'
es.family    # 'Romance'
es.script    # 'Latin'
es.quality   # QualityTier.RESEARCH — see quality_tiers.md

for anc in es.get_ancestors():
    print(anc)
# Ancestor('es-ES-x-medieval', parent, w=1.00)
```

## Handling unknown codes

```python
try:
    orthography2ipa.get("xx")
except KeyError as e:
    print(e)  # "unsupported language: 'xx.json' not found. Available: {...}"
```

## Where to go next

- Building a pipeline around this? [tokenizer.md](tokenizer.md) and
  [architecture.md](architecture.md) cover the engine internals.
- Adding or fixing a language? [adding_a_language.md](adding_a_language.md).
- Deciding whether a language is accurate enough to ship?
  [quality_tiers.md](quality_tiers.md) and [scoreboard.md](scoreboard.md).
- Full field-by-field reference for `LanguageSpec` and friends:
  [data_model.md](data_model.md).

---

**Navigation:** [Docs home](index.md) · [Getting started](getting_started.md) · [Architecture](architecture.md) · [Languages](languages/index.md) · [Scoreboard](scoreboard.md)

*Related: [Tokenizer](tokenizer.md) · [Data model](data_model.md) · [Quality tiers](quality_tiers.md) · [Distance](distance.md)*
