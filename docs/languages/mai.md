# Maithili (`mai`)

<!-- agent-hint
covers: what the `mai` spec holds: its place in the family tree, its sources and scores, its sounds, its spelling rules and transcribed examples
source: `orthography2ipa/data/mai.json`, `benchmarks/results.json`, `scripts/atlas_snapshot.json`
generated: partly. `scripts/gen_language_atlas.py` writes this hint and the blocks between the `atlas:` markers. Edit the generator for those, and the page for the prose between them
verify: `PYTHONPATH=$PWD python scripts/gen_language_atlas.py --check`
see: `docs/languages/sa.md`, `docs/languages/a-z.md`, `docs/specs/quality_tiers.md`, `orthography2ipa/data/SCHEMA.md`
-->

<!-- atlas:summary begin -->
Maithili is an Indo-Aryan language, written in the Devanagari script. Glottolog places it in India and Nepal. The `mai` spec is at the research tier. It cites 5 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mai` |
| ISO 639-3 | [mai](https://iso639-3.sil.org/code/mai), Maithili |
| Glottolog | [mait1250](https://glottolog.org/resource/languoid/id/mait1250), Maithili |
| Wikidata | [Q36109](https://www.wikidata.org/wiki/Q36109) |
| Wikipedia | [Maithili language](https://en.wikipedia.org/wiki/Maithili_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [India](by-region.md#india), [Nepal](by-region.md#nepal) |
| Script | [Devanagari](by-script.md#devanagari) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1400, living |
| Parent | [Sanskrit](sa.md) `sa` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`mai` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mai) |
| Spec file | [`mai.json`](../../orthography2ipa/data/mai.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Maithili (Bihar / Nepal Terai). One of 22 scheduled languages of India (added 2003). Traditional Tirhuta script, Devanagari used officially. Phonologically close to Bengali and Nepali.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 5 works, from 1958 to 2024. [Sources](#sources) lists them. The spec file writes all 60 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mai.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `mai` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Bajjika](https://tigregotico.github.io/orthography2ipa/#vjk) `vjk`: India, stub tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 2 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-masica1991"></a>Masica, C. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
2. <a id="src-cardona_jain2003"></a>Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
3. <a id="src-jha1958"></a>Jha, S. (1958). *The Formation of the Maithili Language*. Luzac.
4. <a id="src-unicode16_ch12"></a>The Unicode Consortium (2024). *The Unicode Standard, Version 16.0, Chapter 12: South and Central Asia-I (Devanagari)*. The Unicode Consortium. [unicode.org](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-12/)
5. <a id="src-unicode16_nameslist"></a>The Unicode Consortium (2024). *Unicode 16.0.0 NamesList.txt*. The Unicode Consortium. [unicode.org](https://www.unicode.org/Public/16.0.0/ucd/NamesList.txt)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 52 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d̪ t̪ t̪ʰ |  | ɖ ʈ ʈʰ |  | k kʰ ɡ |  |
| Affricate |  |  |  |  |  | dʑ tɕ tɕʰ |  |  |
| Nasal | m |  | n |  | ɳ | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |  |
| Tap |  |  |  |  | ɽ |  |  |  |
| Fricative |  |  | s | ʃ | ʂ |  |  | h ɦ |
| Approximant |  | ʋ |  |  |  | j j̃ |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː ĩ ĩː |  | u uː ũ ũː |
| Close-mid | e ẽ |  | o õ |
| Mid |  | ə ə̃ |  |
| Open | aː ãː |  |  |

Sequences that the spec writes as one unit: [bʱ] [dʑʱ] [d̪ʱ] [ɖʱ] [ɡʱ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ँ⟩ | [̃] |  |
| ⟨ं⟩ | [̃] |  |
| ⟨ः⟩ | [h] |  |
| ⟨अ⟩ | [ə] |  |
| ⟨आ⟩ | [aː] |  |
| ⟨इ⟩ | [i] |  |
| ⟨ई⟩ | [iː] |  |
| ⟨उ⟩ | [u] |  |
| ⟨ऊ⟩ | [uː] |  |
| ⟨ए⟩ | [e] |  |
| ⟨ऐ⟩ | [əi] |  |
| ⟨ओ⟩ | [o] |  |
| ⟨औ⟩ | [əu] |  |
| ⟨क⟩ | [k] |  |
| ⟨ख⟩ | [kʰ] |  |
| ⟨ग⟩ | [ɡ] |  |
| ⟨घ⟩ | [ɡʱ] |  |
| ⟨ङ⟩ | [ŋ] |  |
| ⟨च⟩ | [tɕ] |  |
| ⟨छ⟩ | [tɕʰ] |  |
| ⟨ज⟩ | [dʑ] |  |
| ⟨झ⟩ | [dʑʱ] |  |
| ⟨ञ⟩ | [ɲ] |  |
| ⟨ट⟩ | [ʈ] |  |
| ⟨ठ⟩ | [ʈʰ] |  |
| ⟨ड⟩ | [ɖ] |  |
| ⟨ड़⟩ | [ɽ] |  |
| ⟨ढ⟩ | [ɖʱ] |  |
| ⟨ण⟩ | [ɳ] |  |
| ⟨त⟩ | [t̪] |  |
| ⟨थ⟩ | [t̪ʰ] |  |
| ⟨द⟩ | [d̪] |  |
| ⟨ध⟩ | [d̪ʱ] |  |
| ⟨न⟩ | [n] |  |
| ⟨ऩ⟩ | [n] |  |
| ⟨प⟩ | [p] |  |
| ⟨फ⟩ | [pʰ] |  |
| ⟨ब⟩ | [b] |  |
| ⟨भ⟩ | [bʱ] |  |
| ⟨म⟩ | [m] |  |
| ⟨य⟩ | [j] |  |
| ⟨र⟩ | [r] |  |
| ⟨ऱ⟩ | [r] |  |
| ⟨ल⟩ | [l] |  |
| ⟨ऴ⟩ | [l] |  |
| ⟨व⟩ | [ʋ] |  |
| ⟨श⟩ | [ʃ] |  |
| ⟨ष⟩ | [ʂ] |  |
| ⟨स⟩ | [s] |  |
| ⟨ह⟩ | [ɦ] |  |
| ⟨ा⟩ | [aː] |  |
| ⟨ि⟩ | [i] |  |
| ⟨ी⟩ | [iː] |  |
| ⟨ु⟩ | [u] |  |
| ⟨ू⟩ | [uː] |  |
| ⟨े⟩ | [e] |  |
| ⟨ै⟩ | [əi] |  |
| ⟨ो⟩ | [o] |  |
| ⟨ौ⟩ | [əu] |  |
| ⟨्⟩ | ∅ |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mai")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Maguindanaon](mdh.md) · [Home](../index.md) · [Makasar →](mak.md)
