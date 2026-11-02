# orthography2ipa

`orthography2ipa` turns the spelling of a language into IPA, and it measures
how languages relate to each other. Each language is a cited JSON spec in
`orthography2ipa/data/`. A shared engine with no language-specific code turns
the specs into transcriptions and into ranked pronunciation lattices. The
library ships no trained weights.

The registry holds thousands of language codes, from major standard
languages to dialects, creoles and reconstructed proto-languages. Most of them
are stubs. Run `orthography2ipa list` for the live list, or browse the
[language explorer](https://tigregotico.github.io/orthography2ipa/).

> [!WARNING]
> Check the quality tier and the benchmark row of a language before you
> depend on it. Most specs are `stub` or `skeleton`, and few are
> `production`. PER is poor for several major languages, English among
> them. Most gold sets are semi-automatic, so read a PER as a direction, not
> a precise value. The limits are listed in
> [docs/index.md](docs/index.md#honest-limitations-read-this-before-you-trust-a-tier).

## Install

```bash
uv pip install --prerelease=allow orthography2ipa
```

The runtime dependencies are `numpy`, `langcodes` and `ovos-spec-tools`. The
extras are `hf` (Hugging Face lexicon sources), `validation` (pydantic schema
checks), `portuguese` (the silabificador syllabifier) and `test`. To work on
the repository, install it from a clone:

```bash
git clone https://github.com/TigreGotico/orthography2ipa
cd orthography2ipa
uv venv --python 3.11 .venv
uv pip install --python .venv --prerelease=allow -e '.[test]'
```

## Quick start

```python
import orthography2ipa
from orthography2ipa import G2P

orthography2ipa.transcribe("olá mundo", "pt")       # 'oˈla ˈmũdu'
orthography2ipa.transcribe("hello world", "en")     # 'ˈhɛləʊ ˈwɔːld'

result = G2P("pt-PT").transcribe_detailed("um café", search="beam", beam_width=4)
result.ipa                    # 'ˈũ kɐˈfɛ'
result.words[1].candidates    # (IPAPath('kɐfɛ', score=0.0), IPAPath('kafɛ', score=1.0), ...)
```

A code resolves to a registered spec. A bare tag gives the reference variety,
and an unregistered regional tag gives the nearest spec:

```python
orthography2ipa.resolve("pt")       # 'pt-PT'
orthography2ipa.resolve("en-NZ")    # 'en-GB'

en = orthography2ipa.get("en-GB")
en.graphemes["th"]     # ['θ', 'ð']: the phonemes a spelling can stand for
en.allophones["t"]     # ['t', 'tʰ', 'ʔ', 'ɾ']: how a phoneme can surface
en.family              # 'Indo-European > Germanic > Northwest Germanic > West Germanic'
en.quality             # <QualityTier.RESEARCH: 'research'>
```

The command line does the same work. Each subcommand takes `--json`:

```bash
orthography2ipa transcribe pt "olá mundo"                 # /oˈla ˈmũdu/
orthography2ipa transcribe en-GB "through" --search beam --beam-width 8
orthography2ipa info pt-BR
orthography2ipa list --family Ibero-Romance
orthography2ipa distance pt-BR pt-PT
```

[docs/reference/cli.md](docs/reference/cli.md) holds the full `--help`
output, and [docs/reference/api.md](docs/reference/api.md) lists every
exported name.

## The pronunciation lattice

When a spelling is ambiguous, the engine keeps every reading. For each
grapheme it gives the IPA options with a `-log P` cost:

```python
from orthography2ipa import get
from orthography2ipa.phonetok import PhonetokTokenizer

tok = PhonetokTokenizer(get("en-GB"))
for slot in tok.ipa_lattice("cough"):
    print(slot.grapheme, [(c.ipa, c.cost) for c in slot.candidates])
# c [('k', 0.0), ('s', 1.0)]
# ough [('ɔː', 0.0), ('əʊ', 1.0), ('ʌf', 2.0), ('ɒf', 3.0), ('aʊ', 4.0), ('uː', 5.0)]
```

`G2P.word_confidence` tells a downstream engine where the rules are unsure.
`G2P("en-GB").word_confidence("bar")` is `1.0` and `word_confidence("cough")`
is `0.6321`. A downstream engine refines the lattice with a
`LatticeRescorer`, which re-costs the candidates of a slot:

```python
from orthography2ipa.phonetok import Candidate
from orthography2ipa.rescorer import LatticeRescorer

class RoughOugh(LatticeRescorer):
    def rescore(self, slot, context):
        if slot.grapheme != "ough":
            return slot.candidates
        others = [c for c in slot.candidates if c.ipa != "ʌf"]
        return [Candidate("ʌf", 0.0)] + [Candidate(c.ipa, c.cost + 1.0) for c in others]

tok.ipa_best("tough")                         # 'tɔː'
tok.ipa_best("tough", rescorer=RoughOugh())   # 'tʌf'
```

[arbtok](https://github.com/TigreGotico/arbtok) (Arabic),
[tugaphone](https://github.com/TigreGotico/tugaphone) (Portuguese),
[g2p_barranquenho](https://github.com/TigreGotico/g2p_barranquenho) and
[mwl_phonemizer](https://github.com/TigreGotico/mwl_phonemizer) build on this
library. [docs/lattice.md](docs/lattice.md) explains when to write a
rescorer and when to keep a separate tokenizer. `G2P.features(text)` exports
the lattice as features for a CRF or another ML model
([docs/features.md](docs/features.md)).

## Distance between languages

Two languages can be close on one axis and far apart on another, so each
axis has its own measure:

| Axis | Question | API |
|---|---|---|
| Phonological | Do they use the same sounds? | `inventory_distance`, `allophone_overlap`, `phonological_distance` |
| Reading | Given the same text, do they sound alike? | `grapheme_divergence` |
| Spelling | Given the same sound, do they write it alike? | `spelling_divergence` |
| Script | Are the writing systems alike? | `script_distance`, `orthographic_distance` |
| Genealogical | Do they descend from the same ancestors? | `ancestry_similarity`, `ancestry_chain` |
| Temporal | Were they spoken at the same time? | `timespan`, which decays ancestry weights |
| Geographic | Are they spoken in the same place? | `geographic_distance` |

```python
from orthography2ipa import get
from orthography2ipa.distance import phonological_distance, spelling_divergence

pt, es = get("pt-PT"), get("es-ES")
phonological_distance(pt, es).combined       # 0.2166: sounds only, never spelling
spelling_divergence(pt, es).mean_distance    # 0.2697
```

[docs/distance.md](docs/distance.md) describes every axis and its limits.

## Benchmarks

The engine is scored against every gold set the harness can load, with no
cap on the number of words. The [scoreboard](docs/scoreboard.md) gives the
PER, the word count and the `provenance` of each gold set.
[docs/comparison.md](docs/comparison.md) compares the same rows with
espeak-ng, epitran and gruut. Some languages win and some lose.

A row whose gold is the output of espeak-ng or epitran measures agreement
with that tool, not correctness. A row whose gold a language model wrote has
no error model. Neither kind can qualify a spec for the `production` tier,
and neither can block one. [docs/benchmarks.md](docs/benchmarks.md) defines
the reliability tiers.

## AI transparency

Large language models (Anthropic Claude) wrote most specs, under the
direction of a human maintainer. No small project can recruit a
native-speaker linguist for thousands of languages. The choice was between an
AI-written spec and no spec. Every mapping must trace to a published
description: a reference grammar, a peer-reviewed paper or a university
dataset. The engine stays language-agnostic, so a spec cannot hide logic.
The tests check the structure, and the benchmarks score the output against
external data.

A cited spec that a model wrote is still not native-speaker validation, and
the `quality` tier records that. If you speak a language and its spec is
wrong, [open an issue](https://github.com/TigreGotico/orthography2ipa/issues)
with a citation or a native-speaker judgment. Corrections have priority over
all other work here.

## Documentation

- [docs/index.md](docs/index.md): the reading order for every page, routed by
  task.
- [AGENTS.md](AGENTS.md): the repository map, setup and hard rules for a
  contributor or a coding agent.
- [orthography2ipa/data/SCHEMA.md](orthography2ipa/data/SCHEMA.md): every
  field of a spec.
- [docs/contributing/](docs/contributing/spec_authoring.md): the rules for a
  spec, a citation, the benchmark board and the engine.
- [CONTRIBUTING.md](CONTRIBUTING.md): the branch model and commit messages.
- [llms.txt](llms.txt): a map of the repository for a language model.

## License

Apache 2.0
