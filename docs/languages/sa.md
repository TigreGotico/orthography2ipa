# Sanskrit (`sa`)

<!-- atlas:summary begin -->
Sanskrit is an Indo-Aryan language, written in the Devanagari script. Glottolog places it in India. The `sa` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sa` |
| ISO 639-3 | [san](https://iso639-3.sil.org/code/san), Sanskrit |
| Glottolog | [sans1269](https://glottolog.org/resource/languoid/id/sans1269), Sanskrit |
| Wikidata | [Q11059](https://www.wikidata.org/wiki/Q11059) |
| Wikipedia | [Sanskrit](https://en.wikipedia.org/wiki/Sanskrit) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [India](by-region.md#india) |
| Script | [Devanagari](by-script.md#devanagari) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from -1500, living |
| Parent | [Indo-Aryan](https://tigregotico.github.io/orthography2ipa/#x-clade-indo1321) `x-clade-indo1321` |
| Child lects | 18, see [Related lects](#related-lects) |
| Explorer | [`sa` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sa) |
| Spec file | [`sa.json`](../../orthography2ipa/data/sa.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Classical Sanskrit (Pāṇinian standard, c. 4th c. BCE onward). Five-point place-of-articulation system: velar, palatal, retroflex, dental, labial. Four-way laryngeal contrast (plain/aspirated × voiced/voiceless). No short /e/ or /o/ (only long). ⟨व⟩ = [ʋ] labiodental approximant.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1889 to 2003. [Sources](#sources) lists them. The spec file writes all 65 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sa.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `sa` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Assamese](https://tigregotico.github.io/orthography2ipa/#as) `as`: Bangladesh, Bhutan, India, production tier
- [Hindi](hi.md) `hi`: Bangladesh, Bhutan, India, Nepal, research tier
- [Bengali](bn.md) `bn`: Bangladesh, India, Nepal, research tier
- [Gujarati](gu.md) `gu`: Bangladesh, India, Pakistan, research tier
- [Punjabi](pa.md) `pa`: Bangladesh, India, Pakistan, research tier
- [Haryanvi](https://tigregotico.github.io/orthography2ipa/#bgc) `bgc`: India, skeleton tier
- [Chhattisgarhi](https://tigregotico.github.io/orthography2ipa/#hne) `hne`: India, skeleton tier
- [Konkani](kok.md) `kok`: India, research tier
- [Marathi](mr.md) `mr`: India, research tier
- [Odia](or.md) `or`: India, research tier
- [Pali](https://tigregotico.github.io/orthography2ipa/#pi) `pi`: India, Myanmar (Burma), research tier
- [Maithili](mai.md) `mai`: India, Nepal, research tier
- [Dogri](https://tigregotico.github.io/orthography2ipa/#doi) `doi`: India, Pakistan, skeleton tier
- [Kashmiri](ks.md) `ks`: India, Pakistan, research tier
- [Sindhi](sd.md) `sd`: India, Pakistan, research tier
- [Nepali](ne.md) `ne`: Nepal, research tier
- [Sinhala](si.md) `si`: Sri Lanka, research tier
- [Rajasthani (macrolanguage)](https://tigregotico.github.io/orthography2ipa/#raj) `raj`: stub tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 1 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-coulson1992"></a>Coulson, M. (1992). *Sanskrit: An Introduction to the Classical Language*. Hodder & Stoughton.
2. <a id="src-masica1991"></a>Masica, C. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
3. <a id="src-cardona_jain2003"></a>Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
4. <a id="src-whitney1889"></a>Whitney, W. D. (1889). *Sanskrit Grammar*. Breitkopf and Härtel / Ginn & Co. Cited: §§19, 21, 52. [en.wikisource.org](https://en.wikisource.org/wiki/Sanskrit_Grammar_(Whitney)/Chapter_II)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `sa` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 9796 | 0.0161 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 57 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d̪ t̪ t̪ʰ | ɖ ʈ ʈʰ |  | k kʰ ɡ |  |
| Affricate |  |  |  |  | dʑ tɕ tɕʰ |  |  |
| Nasal | m |  | n n̪ | ɳ | ɲ | ŋ ̃ŋ |  |
| Trill |  |  | r r̩ r̩ː |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  |  | s | ʂ | ɕ |  | h ɦ |
| Approximant |  | ʋ |  |  | j |  |  |
| Lateral approximant |  |  | l l̩ |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Close-mid | eː |  | oː |
| Mid |  | ə |  |
| Near-open |  | ɐ |  |
| Open | aː |  | ɑː |

Sequences that the spec writes as one unit: [bʱ] [dʑɲ] [dʑʱ] [d̪ʱ] [kʂ] [t̪ɾ] [w] [ɖʱ] [əi] [əu] [ɡʱ] [̃].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ँ⟩ | [̃] |  |
| ⟨ं⟩ | [̃ŋ] |  |
| ⟨ः⟩ | [h] |  |
| ⟨अ⟩ | [ɐ] |  |
| ⟨आ⟩ | [ɑː] |  |
| ⟨इ⟩ | [i] |  |
| ⟨ई⟩ | [iː] |  |
| ⟨उ⟩ | [u] |  |
| ⟨ऊ⟩ | [uː] |  |
| ⟨ऋ⟩ | [r̩] |  |
| ⟨ऌ⟩ | [l̩] |  |
| ⟨ए⟩ | [eː] |  |
| ⟨ऐ⟩ | [əi] |  |
| ⟨ओ⟩ | [oː] |  |
| ⟨औ⟩ | [əu] |  |
| ⟨क⟩ | [k] |  |
| ⟨क्ष⟩ | [kʂ] |  |
| ⟨ख⟩ | [kʰ] |  |
| ⟨ग⟩ | [ɡ] |  |
| ⟨घ⟩ | [ɡʱ] |  |
| ⟨ङ⟩ | [ŋ] |  |
| ⟨च⟩ | [tɕ] |  |
| ⟨छ⟩ | [tɕʰ] |  |
| ⟨ज⟩ | [dʑ] |  |
| ⟨ज्ञ⟩ | [dʑɲ] |  |
| ⟨झ⟩ | [dʑʱ] |  |
| ⟨ञ⟩ | [ɲ] |  |
| ⟨ट⟩ | [ʈ] |  |
| ⟨ठ⟩ | [ʈʰ] |  |
| ⟨ड⟩ | [ɖ] |  |
| ⟨ढ⟩ | [ɖʱ] |  |
| ⟨ण⟩ | [ɳ] |  |
| ⟨त⟩ | [t̪] |  |
| ⟨त्र⟩ | [t̪ɾ] |  |
| ⟨थ⟩ | [t̪ʰ] |  |
| ⟨द⟩ | [d̪] |  |
| ⟨ध⟩ | [d̪ʱ] |  |
| ⟨न⟩ | [n̪] |  |
| ⟨प⟩ | [p] |  |
| ⟨फ⟩ | [pʰ] |  |
| ⟨ब⟩ | [b] |  |
| ⟨भ⟩ | [bʱ] |  |
| ⟨म⟩ | [m] |  |
| ⟨य⟩ | [j] |  |
| ⟨र⟩ | [ɾ] |  |
| ⟨ल⟩ | [l] |  |
| ⟨व⟩ | [ʋ] |  |
| ⟨श⟩ | [ɕ] |  |
| ⟨ष⟩ | [ʂ] |  |
| ⟨स⟩ | [s] |  |
| ⟨ह⟩ | [ɦ] |  |
| ⟨ा⟩ | [ɑː] |  |
| ⟨ि⟩ | [i] |  |
| ⟨ी⟩ | [iː] |  |
| ⟨ु⟩ | [u] |  |
| ⟨ू⟩ | [uː] |  |
| ⟨ृ⟩ | [r̩] |  |
| ⟨ॄ⟩ | [r̩ː] |  |
| ⟨े⟩ | [eː] |  |
| ⟨ै⟩ | [əi] |  |
| ⟨ो⟩ | [oː] |  |
| ⟨ौ⟩ | [əu] |  |
| ⟨्⟩ | ∅ |  |
| ⟨ॠ⟩ | [r̩ː] |  |
| ⟨ॢ⟩ | [l̩] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sa")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Sango](sg.md) · [Home](../index.md) · [Santali →](sat.md)
