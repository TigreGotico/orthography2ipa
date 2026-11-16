# Albanian (`sq`)

<!-- atlas:summary begin -->
Albanian is an Albanian language, written in the Latin script. Glottolog places it in Albania. The `sq` spec is at the research tier. It cites 3 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sq` |
| ISO 639-3 | [sqi](https://iso639-3.sil.org/code/sqi), Albanian |
| Glottolog | [alba1267](https://glottolog.org/resource/languoid/id/alba1267), Albanian |
| Wikidata | [Q8748](https://www.wikidata.org/wiki/Q8748) |
| Wikipedia | [Albanian language](https://en.wikipedia.org/wiki/Albanian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Albanian](by-family.md#indo-european--albanian) |
| Region | [Eurasia](by-region.md#eurasia) > [Albania](by-region.md#albania) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1462, living |
| Parent | [Albanian](https://tigregotico.github.io/orthography2ipa/#x-clade-alba1267) `x-clade-alba1267` |
| Explorer | [`sq` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sq) |
| Spec file | [`sq.json`](../../orthography2ipa/data/sq.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Albanian based on Tosk dialect. Unique Indo-European branch. Digraphs (dh, gj, ll, nj, rr, sh, th, xh, zh) listed before single letters. Ë = schwa /ə/. Q = palatal stop /c/. R = tap /ɾ/, rr = trill /r/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2023 to 2024. [Sources](#sources) lists them. The spec file writes all 36 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sq.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sq` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-wiki-sq"></a>Wikipedia contributors (2024). *Albanian language*.
2. <a id="src-wiki-sq-phon"></a>Wikipedia contributors (2024). *Albanian phonology*.
3. <a id="src-coretta2023"></a>Coretta, Stefano, Riverin-Coutlée, Josiane, Kapia, Enkeleida, Nichols, Stephen (2023). *Northern Tosk Albanian. Illustrations of the IPA*. Journal of the International Phonetic Association 53(3), 1122-1144 (open access, Edinburgh Research Explorer copy). Cited: 1124-1125, 1132. [doi.org](https://doi.org/10.1017/S0025100322000044)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `sq` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 4900 | 0.0964 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `sq` | generated | epitran-derived | CC0 1.0 | 11713 | 0.1432 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 36 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  | c ɟ | k ɡ |  |
| Affricate |  |  |  | dz ts | dʒ tʃ |  |  |  |
| Nasal | m |  |  | n |  | ɲ |  |  |
| Trill |  |  |  | r |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative |  | f v | ð θ | s z | ʃ ʒ |  |  | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l ɫ |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i y |  | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open | a |  |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨d⟩ | [d] |  |
| ⟨dh⟩ | [ð] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gj⟩ | [ɟ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [ɫ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨nj⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [c] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [θ] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨x⟩ | [dz] |  |
| ⟨xh⟩ | [dʒ] |  |
| ⟨y⟩ | [y] |  |
| ⟨z⟩ | [z] |  |
| ⟨zh⟩ | [ʒ] |  |
| ⟨ç⟩ | [tʃ] |  |
| ⟨ë⟩ | [ə] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sq")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Akoose](bss.md) · [Home](../index.md) · [Alemannic German →](de-x-alemanni.md)
