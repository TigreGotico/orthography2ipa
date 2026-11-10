# orthography2ipa

`orthography2ipa` (o2i) turns the spelling of a language into the
[International Phonetic Alphabet](https://www.internationalphoneticassociation.org/content/full-ipa-chart)
(IPA), and it measures how languages relate to each other. Each language is a
cited JSON spec in `orthography2ipa/data/`. A shared engine with no
language-specific code turns the specs into transcriptions and into ranked
pronunciation lattices. The library ships no trained weights and no word
lists.

The registry holds thousands of language codes: major standard languages,
regional dialects, creoles and reconstructed proto-languages. Run
`orthography2ipa list` for the live list. Most of these codes are stubs. The
[language explorer](https://tigregotico.pt/orthography2ipa/) shows each spec,
its tier and its sources.

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

The project installs with [uv](https://docs.astral.sh/uv/).
[CONTRIBUTING.md](CONTRIBUTING.md#tests) sets up a clone of the repository
for development.

## Quick start

```python
import orthography2ipa

orthography2ipa.transcribe("olá mundo", "pt")       # 'ɔˈla ˈmũdu'
```

[docs/guide/getting_started.md](docs/guide/getting_started.md) is the
tutorial that starts from this call. It covers the dependencies and the
optional extras, the two maps of a spec, beam search, language lookup, the
command line, plugins and the explorer.

## Documentation

[docs/index.md](docs/index.md) is the front door of the documentation. It
states what the library does and where its accuracy stops, and it sets the
reading order of every page. The table below goes straight to the page for a
common task.

| You want to | Read |
| :--- | :--- |
| Rank the readings of an ambiguous spelling, or rescore them | [docs/engine/lattice.md](docs/engine/lattice.md) |
| Export the lattice as features for a CRF or another ML model | [docs/engine/lattice.md](docs/engine/lattice.md#feature-export-for-a-learned-model) |
| Measure how two languages differ in sound, spelling, script, ancestry, time or place | [docs/guide/distance.md](docs/guide/distance.md) |
| See the PER, the word count and the provenance of each gold set | [docs/evaluation/generated/scoreboard.md](docs/evaluation/generated/scoreboard.md) |
| Compare the same rows with other G2P systems | [docs/evaluation/generated/comparison.md](docs/evaluation/generated/comparison.md) |
| Learn what a gold set can prove, and the reliability tiers | [docs/evaluation/benchmarks.md](docs/evaluation/benchmarks.md) |
| Read the full `--help` output | [docs/reference/cli.md](docs/reference/cli.md) |
| Look up an exported name | [docs/reference/api.md](docs/reference/api.md) |
| Read every field of a spec | [orthography2ipa/data/SCHEMA.md](orthography2ipa/data/SCHEMA.md) |
| Write a spec, a citation, a board change or an engine change | [docs/contributing/](docs/contributing/spec_authoring.md) |
| Learn the repository map, the setup and the hard rules | [AGENTS.md](AGENTS.md) |
| Follow the branch model and the commit messages | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Give a language model a map of the repository | [llms.txt](llms.txt), or [llms-full.txt](llms-full.txt) with every language page |

## How it compares

The [comparison board](docs/evaluation/generated/comparison.md) scores o2i and
other grapheme-to-phoneme (G2P) systems on the same gold words, language by
language. The general systems on the board are
[espeak-ng](https://github.com/espeak-ng/espeak-ng),
[epitran](https://github.com/dmort27/epitran) and
[gruut](https://github.com/rhasspy/gruut). The board also scores engines for
one language or one region:
[pycotovia](https://github.com/TigreGotico/pycotovia) for Galician and
Spanish, [ahotts-g2p](https://github.com/TigreGotico/ahotts-g2p) for Basque and
Spanish, and [africa-g2p](https://github.com/AfriSpeech/africa-g2p) and
[ghana-g2p](https://github.com/GhanaNLP/ghana-g2p) for African languages.
The ranking counts rules only. A system's bundled word lexicon is shown on
the board, but it never wins a row, because o2i ships no lexicon of its own.

o2i keeps its knowledge in a different place from these systems. espeak-ng
keeps a rules file and an exception dictionary for each language. gruut keeps
a lexicon and a trained guesser for each language. epitran keeps a mapping
table for each language and returns one reading. o2i keeps every language in one schema, cites each
mapping, and returns a ranked lattice of readings that a downstream engine
can rescore.

## Ecosystem

Several engines build on the o2i lattice. Each one adds, for one language,
the context that spelling alone cannot give.

| Project | What it adds |
| :--- | :--- |
| [tugaphone](https://github.com/TigreGotico/tugaphone) | Portuguese: a curated lexicon, a rule fallback and output for each Lusophone dialect |
| [arbtok](https://github.com/TigreGotico/arbtok) | Arabic: short-vowel restoration (tashkeel), stress and dialect output |
| [euskaphone](https://github.com/TigreGotico/euskaphone) | Basque: dialect output for a TTS front end |
| [g2p_barranquenho](https://github.com/TigreGotico/g2p_barranquenho) | Barranquenho, the contact variety of Barrancos |
| [mwl_phonemizer](https://github.com/TigreGotico/mwl_phonemizer) | Mirandese |

Other packages supply data or steps that o2i does not hold.
[o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) ships residual
lexicons, which a caller enables in code.
[silabificador](https://github.com/TigreGotico/silabificador) is a
Portuguese syllabifier that plugs into a `Pipeline`.
[bifonia](https://github.com/TigreGotico/bifonia) chooses the reading of a
European Portuguese homograph from its sentence.
[scriptconv](https://github.com/TigreGotico/scriptconv) converts between
scripts and phoneme notations, which o2i does not do.
[phoonnx](https://github.com/TigreGotico/phoonnx) is a TTS engine that offers
o2i as one of its phonemizers. C++ ports of o2i and of several of these
engines are in [loom-ai-org](https://github.com/loom-ai-org), for example
[orthography2ipa.cpp](https://github.com/loom-ai-org/orthography2ipa.cpp)
and [tugaphone.cpp](https://github.com/loom-ai-org/tugaphone.cpp).

## AI transparency

Large language models (Anthropic Claude) wrote most specs, under the
direction of a human maintainer. No small project can recruit a
native-speaker linguist for thousands of languages, so the choice was between
an AI-written spec and no spec. Every mapping must trace to a published
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

Apache 2.0. See [LICENSE](LICENSE).
