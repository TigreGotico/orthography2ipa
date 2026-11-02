# orthography2ipa

`orthography2ipa` turns the spelling of a language into IPA, and it measures
how languages relate to each other. Each language is a cited JSON spec in
`orthography2ipa/data/`. A shared engine with no language-specific code turns
the specs into transcriptions and into ranked pronunciation lattices. The
library ships no trained weights.

The registry holds thousands of language codes, from major standard
languages to dialects, creoles and reconstructed proto-languages. Most of them
are stubs. The [language explorer](https://tigregotico.pt/orthography2ipa/)
shows each one.

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

[CONTRIBUTING.md](CONTRIBUTING.md#tests) sets up a clone of the repository
for development.

## Quick start

```python
import orthography2ipa

orthography2ipa.transcribe("olá mundo", "pt")       # 'oˈla ˈmũdu'
```

[docs/guide/getting_started.md](docs/guide/getting_started.md) is the
tutorial that starts from this call. It covers the dependencies and the
optional extras, the two maps of a spec, beam search, language lookup, the
command line, plugins and the explorer.

## Documentation

| You want to | Read |
| :--- | :--- |
| Find a page by task | [docs/index.md](docs/index.md) |
| Rank the readings of an ambiguous spelling, or rescore them | [docs/engine/lattice.md](docs/engine/lattice.md) |
| Export the lattice as features for a CRF or another ML model | [docs/engine/lattice.md](docs/engine/lattice.md#feature-export-for-a-learned-model) |
| Measure how two languages differ in sound, spelling, script, ancestry, time or place | [docs/guide/distance.md](docs/guide/distance.md) |
| See the PER, the word count and the provenance of each gold set | [docs/evaluation/generated/scoreboard.md](docs/evaluation/generated/scoreboard.md) |
| Compare the same rows with espeak-ng, epitran and gruut | [docs/evaluation/generated/comparison.md](docs/evaluation/generated/comparison.md) |
| Learn what a gold set can prove, and the reliability tiers | [docs/evaluation/benchmarks.md](docs/evaluation/benchmarks.md) |
| Read the full `--help` output | [docs/reference/cli.md](docs/reference/cli.md) |
| Look up an exported name | [docs/reference/api.md](docs/reference/api.md) |
| Read every field of a spec | [orthography2ipa/data/SCHEMA.md](orthography2ipa/data/SCHEMA.md) |
| Write a spec, a citation, a board change or an engine change | [docs/contributing/](docs/contributing/spec_authoring.md) |
| Learn the repository map, the setup and the hard rules | [AGENTS.md](AGENTS.md) |
| Follow the branch model and the commit messages | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Give a language model a map of the repository | [llms.txt](llms.txt) |

[arbtok](https://github.com/TigreGotico/arbtok) (Arabic),
[tugaphone](https://github.com/TigreGotico/tugaphone) (Portuguese),
[g2p_barranquenho](https://github.com/TigreGotico/g2p_barranquenho) and
[mwl_phonemizer](https://github.com/TigreGotico/mwl_phonemizer) build on this
library.

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

## License

Apache 2.0
