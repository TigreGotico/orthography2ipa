# Other G2P systems and the o2i ecosystem

<!-- agent-hint
covers: how o2i differs from other G2P systems, the comparison board, and the projects that build on o2i
source: `scripts/compare_systems.py`, `benchmarks/comparison.json`, the README of each linked project
generated: no
verify: `PYTHONPATH=$PWD python -m pytest tests/test_docs_prose.py`
see: `docs/evaluation/generated/comparison.md`, `docs/engine/lattice.md`
-->

This page compares o2i with other grapheme-to-phoneme (G2P) systems and lists the projects that use the o2i lattice.

## The comparison board

The [comparison board](../evaluation/generated/comparison.md) scores o2i and other G2P systems on the same gold words, language by language.

- The general systems on the board are [espeak-ng](https://github.com/espeak-ng/espeak-ng), [epitran](https://github.com/dmort27/epitran) and [gruut](https://github.com/rhasspy/gruut) (archived upstream).
- The board also scores engines for one language or one region:
  - [pycotovia](https://github.com/TigreGotico/pycotovia) for Galician and Spanish;
  - [ahotts-g2p](https://github.com/TigreGotico/ahotts-g2p) for Basque and Spanish;
  - [africa-g2p](https://github.com/AfriSpeech/africa-g2p) and [ghana-g2p](https://github.com/GhanaNLP/ghana-g2p) for African languages.

The ranking counts rules only. The board shows a system's bundled word lexicon, but the lexicon never wins a row, because o2i ships no lexicon of its own.

## Where each system keeps its knowledge

| System | Knowledge for each language | Output |
| :--- | :--- | :--- |
| espeak-ng | a rules file and an exception dictionary | one reading |
| gruut | a lexicon and a trained guesser | one reading |
| epitran | a mapping table | one reading |
| o2i | a cited JSON spec in one schema for every language | a ranked lattice of readings that a downstream engine can rescore |

## Projects that build on o2i

These engines each add, for one language, the context that spelling alone cannot give.

| Project | What it adds |
| :--- | :--- |
| [tugaphone](https://github.com/TigreGotico/tugaphone) | Portuguese: a curated lexicon, a rule fallback and output for each Lusophone dialect |
| [arbtok](https://github.com/TigreGotico/arbtok) | Arabic: short-vowel restoration (tashkeel), stress and dialect output |
| [euskaphone](https://github.com/TigreGotico/euskaphone) | Basque: dialect output for a TTS front end |

For Barranquenho, the contact variety of Barrancos, use `G2P("ext-PT-x-barranco")`. For Mirandese, use `G2P("mwl")`, or `G2P("mwl-x-sendim")` and `G2P("mwl-x-ifanes")` for the Sendinês and Ifanês varieties.

## Packages that supply data or steps

| Package | What it supplies |
| :--- | :--- |
| [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) | Residual lexicons, which a caller enables in code |
| [silabificador](https://github.com/TigreGotico/silabificador) | A Portuguese syllabifier that plugs into a `Pipeline` |
| [bifonia](https://github.com/TigreGotico/bifonia) | The reading of a European Portuguese homograph, chosen from its sentence |
| [scriptconv](https://github.com/TigreGotico/scriptconv) | Conversion between scripts and phoneme notations, which o2i does not do |
| [phoonnx](https://github.com/TigreGotico/phoonnx) | A TTS engine that offers o2i as one of its phonemizers |
| [loom-ai-org](https://github.com/loom-ai-org) | C++ ports of o2i and of several of these engines, for example [orthography2ipa.cpp](https://github.com/loom-ai-org/orthography2ipa.cpp) and [tugaphone.cpp](https://github.com/loom-ai-org/tugaphone.cpp) |

---
[← Known limitations](known_limitations.md) · [Home](../index.md) · [Python API →](../reference/api.md)
