# orthography2ipa

A library for measuring **how languages relate to each other**, and for turning
their spelling into IPA on the way there.

Two languages can be close on one axis and far apart on another. Galician and
Portuguese *sound* nearly the same and are written differently; Galician and
Castilian *sound* different and are written alike. A single "language similarity"
number hides that. `orthography2ipa` keeps the axes apart and measures each one on
its own:

| Axis | Question | API |
|---|---|---|
| **Phonological** | Do they use the same sounds? | `inventory_distance`, `allophone_overlap`, `phonological_distance` |
| **Reading** | Given the same *text*, do they sound alike? | `grapheme_divergence` |
| **Spelling** | Given the same *sound*, do they write it alike? | `spelling_divergence` |
| **Script** | Are the writing systems typologically alike? | `script_distance`, `orthographic_distance` |
| **Genealogical** | Do they descend from the same ancestors? | `ancestry_similarity`, `ancestry_chain` |
| **Temporal** | Were they spoken at the same time? | `timespan` (decays ancestry weights) |
| **Geographic** | Are they spoken in the same place? | `geographic_distance` |

```python
import orthography2ipa as o2i
from orthography2ipa.distance import grapheme_divergence, spelling_divergence

gl = o2i.get("gl")                  # Galician, RAG norm — writes /ɲ/ as ⟨ñ⟩, as Castilian does
glr = o2i.get("gl-x-reintegrado")   # Galician, reintegrationist norm — as ⟨nh⟩, as Portuguese does

grapheme_divergence(gl, glr).mean_ipa_distance   # 0.0233 — reading: same text, same sounds
spelling_divergence(gl, glr).mean_distance       # 0.0659 — spelling: same sounds, written differently
```

The two norms are the same language with the same phonology, and only the spelling
axis can see what separates them. That is the library: the axes are independent,
so they are measured independently.

The phonology those axes compare comes from a **per-language data spec** —
graphemes, allophones, positional rules, ancestry, sources — and the same specs
drive a grapheme-to-IPA engine:

```python
>>> import orthography2ipa
>>> orthography2ipa.transcribe("olá mundo", "pt")
'oˈla ˈmũdu'
```

**491 languages** and **63 clade nodes** ship with the package (554 spec files in
`orthography2ipa/data/`; `available_codes()` returns the 491 languages,
`available_codes(include_clades=True)` all 554), spread across 30 top-level
families from Indo-European to Quechuan, plus reconstructed proto-languages,
regional dialects and creoles.

New to the library? **[docs/index.md](docs/index.md)** routes you by what you are
trying to do, and states the known accuracy limits up front.

## The engine is data, not weights

Every language is a JSON file describing which graphemes map to which IPA phonemes
and how those phonemes surface in context. A shared, language-agnostic engine —
tokenizer, beam search, allophone rules, stress, sandhi — turns that data into
transcriptions. There are no trained weights to ship, and adding a language means
writing cited data, not training a model.

### Two maps, kept apart

- A **grapheme map** tells you which phonemes a spelling *can* represent.
  English ⟨th⟩ → `['θ', 'ð']`.
- An **allophone map** tells you how a phoneme *surfaces* in context.
  English /t/ → `['t', 'tʰ', 'ʔ', 'ɾ']`.

The pre-lexical map (orthography → phoneme) is conditioned by
`positional_graphemes`, vowel-class positions and candidate weights. The
post-lexical map (phoneme → surface allophone) is applied by declarative
**`allophone_rules`** — context-conditioned rewrites keyed on syllable position,
stress, word position and neighbouring segments. They compile into a lattice
rescorer that runs after phoneme selection and before stress and sandhi. Catalan
uses them for word-final obstruent devoicing (`fred` → `[ˈfɾet]`) and nasal place
assimilation (`banc` → `[ˈbaŋk]`); see [docs/allophony.md](docs/allophony.md).

### The pronunciation lattice

When a spelling is ambiguous the engine does not just pick a guess — it builds a
ranked, cost-annotated lattice for the word, and that lattice is what specialised
phonemizers stand on. For any registered language you get, per grapheme, every IPA
option it can realise and a `-log P` cost ranking them:

```python
from orthography2ipa import get
from orthography2ipa.phonetok import PhonetokTokenizer

tok = PhonetokTokenizer(get("en-GB"))
for slot in tok.ipa_lattice("cough"):
    print(slot.grapheme, [(c.ipa, c.cost) for c in slot.candidates])
    # c    → [('k', 0.0), ('s', 1.0)]
    # ough → [('ɔː', 0.0), ('oʊ', 1.0), ('ʌf', 2.0), ('ɒf', 3.0), ('aʊ', 4.0), ('uː', 5.0)]
```

**It tells you when it is unsure.** A per-word confidence — each slot's top-1 vs
top-2 cost margin folded with grapheme coverage — flags which words a downstream
engine should spend its expensive lexicon or rules on, and which it can take on
trust:

```python
from orthography2ipa import G2P

g = G2P("en-GB")
g.word_confidence("bar")     # 1.0    — one reading, take it
g.word_confidence("cough")   # 0.6321 — ambiguous, look closer
g.word_confidence("bar你")   # 0.75   — one OOV grapheme drops coverage to 3/4
```

**A downstream engine refines the lattice with a rescorer.** A rule is a
`LatticeRescorer`: a pure function over one slot and its context that re-costs
candidates. A candidate wins by being made strictly cheapest. Here is a complete
mini-phonemizer that teaches English ⟨ough⟩ its `/ʌf/` reading (*rough*, *tough*,
*enough*):

```python
from orthography2ipa import get
from orthography2ipa.phonetok import PhonetokTokenizer, Candidate
from orthography2ipa.rescorer import LatticeRescorer

class RoughOugh(LatticeRescorer):
    def rescore(self, slot, context):
        if slot.grapheme != "ough":
            return slot.candidates                    # no-op elsewhere
        others = [c for c in slot.candidates if c.ipa != "ʌf"]
        return [Candidate("ʌf", 0.0)] + [Candidate(c.ipa, c.cost + 1.0)
                                         for c in others]

tok = PhonetokTokenizer(get("en-GB"))
tok.ipa_best("tough")                        # 'tɔː'  — generic beam
tok.ipa_best("tough", rescorer=RoughOugh())  # 'tʌf'  — refined
```

The beam is the **universal fallback**: it produces a defensible transcription for
every word in every registered language. Refining it with a rescorer is one of two
supported ways to build a specialised engine on this library; keeping a bespoke
tokenizer is the other. [arbtok](https://github.com/TigreGotico/arbtok),
[tugaphone](https://github.com/TigreGotico/tugaphone),
[g2p_barranquenho](https://github.com/TigreGotico/g2p_barranquenho) and
[mwl_phonemizer](https://github.com/TigreGotico/mwl_phonemizer) build on this
library; see [Refine or fork?](docs/lattice.md#refine-the-lattice-or-fork-the-tokenizer)
for the trade-offs.

Because the library ships no trained weights it is also a clean *feature provider*
for an ML G2P: `G2P.features(text)` exposes, per grapheme, the phonological-class
predicates, word-local neighbours, the ranked `(ipa, cost)` lattice and the
confidence signal as flat, JSON-able dicts — so a CRF trains on
linguistically-grounded features and plugs back in as a `LatticeRescorer`, spending
its learned capacity where confidence says the base engine is unsure. See
[Features for ML / CRF G2P](docs/features.md).

## Families are nodes, not labels

There is no authored `family` string. A family is a **clade node** in the ancestry
graph — a spec with `"clade": true`, carrying classification and nothing else — and
`spec.family` is *derived* by walking the parent chain up through the clades it
passes:

```python
import orthography2ipa

orthography2ipa.get("pt-BR").family_path   # ('Indo-European', 'Italic', 'Romance', 'Ibero-Romance')
orthography2ipa.get("pt-BR").family        # 'Indo-European > Italic > Romance > Ibero-Romance'
```

Because it is a chain and not a fixed-depth label, a consumer can ask at any depth:
`--family Romance` and `--family Ibero-Romance` both match `pt-BR`. Clade nodes are
classification-only — never a data source, never inherited from, and excluded from
`available_codes()` by default. An explicit `family` string stays accepted for
groupings that are *not* genetic clades: creoles, constructed languages, isolates,
unclassified languages. See [docs/ancestry.md](docs/ancestry.md).

## Installation

```bash
pip install orthography2ipa
```

For richer language-specific pipelines, install a downstream engine built on this
library: [arbtok](https://github.com/TigreGotico/arbtok) for Arabic,
[tugaphone](https://github.com/TigreGotico/tugaphone) for Portuguese.

## Quick start

```python
import orthography2ipa

orthography2ipa.transcribe("olá mundo", "pt")     # 'oˈla ˈmũdu'
orthography2ipa.transcribe("hello world", "en")   # 'hələʊ wɜːld'
orthography2ipa.transcribe("bona nuèit", "oc")    # 'ˈbunɔ ˈnyɛjt'

# Beam search keeps ranked alternatives per word
from orthography2ipa import G2P

engine = G2P("pt-PT")
result = engine.transcribe_detailed("um café", search="beam", beam_width=4)
result.ipa                          # 'ˈũ kɐˈfɛ'
result.words[1].candidates          # ranked IPAPath alternatives
```

The pipeline is: normalize → tokenize → greedy/beam per word → allophone rules →
stress marks (when the spec declares stress rules) → sandhi → dialect transform.

### Language specs

```python
import orthography2ipa

en = orthography2ipa.get("en-GB")
en.graphemes["th"]    # ['θ', 'ð']              — grapheme → phoneme candidates
en.allophones["t"]    # ['t', 'tʰ', 'ʔ', 'ɾ']   — phoneme → surface realisations
en.name               # 'British English (RP)'
en.script             # 'Latin'
en.family             # 'Indo-European > Germanic > Northwest Germanic > West Germanic'

# Regional variants share ancestry but diverge where pronunciation does
orthography2ipa.get("pt-BR").graphemes["t"]   # ['t', 't͡ʃ'] — palatalisation before /i/

# Bare tags, ISO 639-3 aliases and near matches all resolve
orthography2ipa.get("eng").name    # 'British English (RP)'
orthography2ipa.resolve("pt")      # 'pt-PT' — reference variety
orthography2ipa.resolve("en-NZ")   # 'en-GB' — nearest registered

# Discover what's available
orthography2ipa.available_codes()      # 491 language codes (clades excluded)
orthography2ipa.available_families()   # codes grouped by derived family path
```

### Distance metrics

```python
import orthography2ipa as o2i
from orthography2ipa.distance import (phonological_distance, spelling_divergence,
                                      geographic_distance, ancestry_similarity)

pt, es = o2i.get("pt-PT"), o2i.get("es-ES")

d = phonological_distance(pt, es)
d.combined                              # 0.1859 — sound-level distance
d.inventory.feature_mean                # phoneme-inventory distance
d.grapheme.mean_ipa_distance            # 0.1102 — reading divergence

spelling_divergence(pt, es).mean_distance      # 0.2068 — writing divergence
ancestry_similarity(pt, es)                    # 0.5304 — shared-ancestor weight
geographic_distance(pt, es, normalize=False)   # 377.8 — km between the two points
```

Every axis, with its caveats, is in [docs/distance.md](docs/distance.md).

## Command-line interface

Every subcommand accepts `--json` for machine-readable output.

```bash
# List languages and families
orthography2ipa list
orthography2ipa list --families
orthography2ipa list --family Romance          # any step of the path matches
orthography2ipa list --family Ibero-Romance    # ... including the sub-branch

# Inspect a language
orthography2ipa info pt-BR
orthography2ipa info pt-BR --graphemes
orthography2ipa info pt-BR --json

# Transcribe text to IPA
orthography2ipa transcribe pt "olá mundo"
orthography2ipa transcribe en-GB "through" --search beam --beam-width 8

# Distance between two languages
orthography2ipa distance pt-BR pt-PT
orthography2ipa distance es-ES it-IT --json
```

## What each language carries

Every `LanguageSpec` provides:

1. **Graphemes** — orthographic units (characters, digraphs, trigraphs) mapped to canonical IPA phonemes.
2. **Allophones** — each phoneme mapped to its positional/contextual surface realisations.
3. **Positional graphemes** — context-sensitive overrides (word-initial, intervocalic, before a front vowel, …).
4. **Allophone rules** — post-lexical `phoneme → surface` rewrites (final devoicing, assimilation, reduction, flapping).
5. **Ancestry** — weighted multi-ancestor lineage (parent, substrate, superstrate, adstrate, …), through which `family` is derived.
6. **Sandhi rules** — cross-word phonological processes.
7. **Stress rules**, **tone inventory** and **word exceptions**, where applicable.
8. **Orthography standard** — the official published spelling norm, when the language has one.
9. **Location** and **timespan** — where and when the variety is spoken.
10. **Provenance** — `QualityTier` (stub → skeleton → research → production), `ScriptType`, bibliographic `sources`, `wikipedia` / `urls`, and cross-reference identifiers (`glottolog_code`, `wikidata_qid`, `phoible_id`, `wals_code`, `iso639_3`).

Regional varieties get their own `LanguageSpec` linked through ancestry, and
`graphemes_base` / `allophones_base` inheritance lets a dialect declare only what
differs from its parent. The full field list is in
[docs/data_model.md](docs/data_model.md); the authoring reference is
[`orthography2ipa/data/SCHEMA.md`](orthography2ipa/data/SCHEMA.md).

## Benchmarks

The engine is evaluated against the best gold sets available — the Portal da
Língua Portuguesa lexicon (via [tugalex](https://github.com/TigreGotico/tugalex)),
WikiPron, Infopédia, CMUdict, the Mirandese gold set, 4CatAc and others. The
published [scoreboard](docs/scoreboard.md) scores the **entire** gold set of every
registered dataset/language pair — no cap — so each row's `N` is the real number of
covered gold words, not a sample size. Reproduce any row with
`python scripts/benchmark.py --scoreboard`.

**Take every number with a grain of salt.** Reliable G2P gold barely exists, so
most datasets are semi-automated, dictionary-extracted, community-scraped, or a
phonemizer's own output reused as a reference. Read PER as *directional*, not
precise. Every dataset carries a reliability tier in the scoreboard's `provenance`
column, and one of those tiers deserves naming here:

> **`espeak-derived` gold measures agreement with espeak, not correctness.**
> The `styletts2_phonemes` rows are the output of an espeak-ng-backed phonemizer —
> a competitor this library benchmarks *against* in
> [comparison.md](docs/comparison.md). Diverging from espeak can mean we are right
> and it is wrong, which shows up in those rows as a *worse* score. An
> `espeak-derived` row can therefore neither qualify a language for a production
> promotion nor block one. It is breadth, and a directional signal, and nothing
> more.

Contextual (positional) scoring is still limited, no language currently sits at the
`production` quality tier, and PER is genuinely mediocre for several languages —
see
[Honest limitations](docs/index.md#honest-limitations-read-this-before-you-trust-a-tier)
before depending on this for anything accuracy-sensitive. Methodology, per-dataset
evidence and the full reliability taxonomy are in
[docs/benchmarks.md](docs/benchmarks.md).

Candidate ordering defaults to rank order (most common pronunciation first). A spec
can attach per-candidate **weights** — candidate frequencies from cited corpora —
so the beam favours the corpus-dominant phoneme and a path's score becomes a real
log-probability; see [candidate scoring](docs/candidate_scoring.md).

### Comparison to other G2P systems

`scripts/compare_systems.py` runs the same gold rows through orthography2ipa,
espeak-ng, epitran and gruut with identical normalization and scoring, and commits
the result to [docs/comparison.md](docs/comparison.md)
([benchmarks/comparison.json](benchmarks/comparison.json) for the machine-readable
form). It is an honest table: some languages win against espeak-ng, some lose, and
coverage against epitran/gruut is partial by nature of those projects' own language
lists. No row is cherry-picked.

## Design principles

- **Independent axes** — phonology, reading, spelling, script, ancestry, time and geography are measured separately, because languages relate along each of them differently.
- **Linguistically motivated only** — digraphs like English ⟨th⟩, Portuguese ⟨lh⟩ or German ⟨sch⟩ are included because they are standard orthographic units; arbitrary substrings are not.
- **Graphemes ≠ allophones** — spelling-to-phoneme and phoneme-to-surface are modelled separately.
- **Classification is a graph** — families are clade nodes on the ancestry chain, not labels on a spec.
- **Pure data, self-contained logic** — mappings are declarative JSON; the engine never loads external G2P implementations.
- **Honest numbers** — every benchmark row states where its gold came from and how much it can carry.

## Building engines on top

`G2PPlugin` and `WordContext` are the base types for richer language-specific
engines built **on** this library — [arbtok](https://github.com/TigreGotico/arbtok)
(Arabic: contextual rule cascade + tashkeel diacritization) and
[tugaphone](https://github.com/TigreGotico/tugaphone) (Portuguese: lexicon, POS and
regional-accent layers). They consume the spec data, tokenizer and stress machinery
and own their own pipelines. Whether such an engine expresses its rules as rescorers
over the shared lattice or keeps a bespoke tokenizer is a design choice covered in
[Refine or fork?](docs/lattice.md#refine-the-lattice-or-fork-the-tokenizer).

Component plugins that slot into the bundled engine's own logic use dedicated
entry-point groups: per-language syllabifiers register under
`orthography2ipa.syllabify` (e.g. `silabificador` for Portuguese) and are honoured
by stress detection automatically.

## Contributing

To add a language, create `orthography2ipa/data/{code}.json` following
[`orthography2ipa/data/SCHEMA.md`](orthography2ipa/data/SCHEMA.md) and the
walkthrough in [docs/adding_a_language.md](docs/adding_a_language.md). For dialects,
use `graphemes_base` / `allophones_base` to inherit from the parent.

## License

Apache 2.0
