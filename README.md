# orthography2ipa

<!-- agent-hint
covers: what orthography2ipa does, how to install it, a first transcription and where each topic is documented
source: `pyproject.toml`, `orthography2ipa/__init__.py`, `orthography2ipa/g2p.py:transcribe`
generated: no
verify: `PYTHONPATH=$PWD python -c "import orthography2ipa; print(orthography2ipa.transcribe('olá mundo', 'pt'))"`
see: `docs/index.md`, `docs/guide/getting_started.md`, `AGENTS.md`
-->

`orthography2ipa` (o2i) turns the spelling of a language into the [International Phonetic Alphabet](https://www.internationalphoneticassociation.org/content/full-ipa-chart) (IPA), and it measures how languages relate to each other. Each language is a cited JSON spec in `orthography2ipa/data/`. One engine with no language-specific code turns the specs into transcriptions and ranked pronunciation lattices. The library ships no trained weights and no word lists.

Try it: [huggingface.co/spaces/TigreGotico/orthography2ipa](https://huggingface.co/spaces/TigreGotico/orthography2ipa) runs the package in your browser.

> [!WARNING]
> Check the quality tier and the benchmark row of a language before you depend on it. Most specs are `stub` or `skeleton`, and few are `production`. Most gold sets are semi-automatic, so read a PER as a direction, not a precise value. [docs/index.md](docs/index.md#honest-limitations-read-this-before-you-trust-a-tier) lists the limits.

## Install

```bash
uv pip install --prerelease=allow orthography2ipa
```

The optional extras (`hf`, `lexicons`, `validation`, `portuguese`, `loom`) add features and change no transcription. [getting_started.md](docs/guide/getting_started.md#install) lists them.

## Quick start

```python
import orthography2ipa

orthography2ipa.transcribe("olá mundo", "pt")       # 'ɔˈla ˈmũdu'
orthography2ipa.transcribe("olá mundo", "pt-BR")    # 'oˈla ˈmũdu'
```

## Documentation

| You want to | Read |
| :--- | :--- |
| Start from the first call | [docs/guide/getting_started.md](docs/guide/getting_started.md) |
| See every page in reading order | [docs/index.md](docs/index.md) |
| Rank or rescore the readings of a spelling | [docs/engine/lattice.md](docs/engine/lattice.md) |
| Measure how two languages differ | [docs/guide/distance.md](docs/guide/distance.md) |
| See the PER of each gold set | [docs/evaluation/generated/scoreboard.md](docs/evaluation/generated/scoreboard.md) |
| Compare o2i with other G2P systems, and find the projects that build on it | [docs/guide/ecosystem.md](docs/guide/ecosystem.md) |
| Look up an exported name or a CLI option | [docs/reference/api.md](docs/reference/api.md), [docs/reference/cli.md](docs/reference/cli.md) |
| Write or correct a spec | [docs/contributing/spec_authoring.md](docs/contributing/spec_authoring.md) |
| Learn who writes the specs and how to report an error | [docs/specs/quality_tiers.md](docs/specs/quality_tiers.md#who-writes-the-specs) |
| Change the repository | [AGENTS.md](AGENTS.md), [CONTRIBUTING.md](CONTRIBUTING.md) |

## License

Apache 2.0. See [LICENSE](LICENSE).
