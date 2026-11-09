# Shona (`sn`)

<!-- atlas:summary begin -->
Shona is a Bantu language, written in the Latin script. Glottolog places it in Botswana, South Africa, Zambia and Zimbabwe. The `sn` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sn` |
| ISO 639-3 | [sna](https://iso639-3.sil.org/code/sna), Shona |
| Glottolog | [shon1251](https://glottolog.org/resource/languoid/id/shon1251), Shona |
| Wikipedia | [Shona language](https://en.wikipedia.org/wiki/Shona_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) > [Bantu](by-family.md#atlantic-congo--bantu) |
| Region | [Africa](by-region.md#africa) > [Botswana](by-region.md#botswana), [South Africa](by-region.md#south-africa), [Zambia](by-region.md#zambia), [Zimbabwe](by-region.md#zimbabwe) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1931, living |
| Parent | [Bantu](https://tigregotico.github.io/orthography2ipa/#x-clade-narr1281) `x-clade-narr1281` |
| Explorer | [`sn` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sn) |
| Spec file | [`sn.json`](../../orthography2ipa/data/sn.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Shona (chiShona), Bantu language of Zimbabwe, standard orthography (1955/1967 revision) in the Latin script. Regular and largely phonemic, with a five-vowel system /a e i o u/ and open (CV) syllables.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1931 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 46 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sn.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sn` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-doke1931"></a>Doke, Clement M. (1931). *Report on the Unification of the Shona Dialects*. Government of Southern Rhodesia.
2. <a id="src-fortune1985"></a>Fortune, George (1985). *Shona Grammatical Constructions*. Mercury Press, Harare.
3. <a id="src-shona_wiki"></a>Wikipedia contributors (2025). *Shona language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Shona_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 46 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b̤ p |  | d̤ t ⁿd |  |  | k ɡ̤ |  |
| Affricate |  | p͡f | d͡z̤ t͡s | d͡ʒ̤ t͡ʃ ⁿd͡ʒ̤ |  |  |  |
| Nasal | m m̤ |  | n n̤ |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v̤ | s z̤ ⁿz̤ | ʃ ʒ̤ |  |  | ɦ |
| Approximant |  | ʋ |  |  | j |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [b͡v̤] [d͡z̤ᵝ] [mʋ̤] [sᶲ] [t͡sᶲ] [w] [z̤ᵝ] [ɓ] [ɗ] [ᵐb] [ⁿz̤ᵝ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [ɓ] |  |
| ⟨bh⟩ | [b̤] |  |
| ⟨bv⟩ | [b͡v̤] |  |
| ⟨ch⟩ | [t͡ʃ] |  |
| ⟨d⟩ | [ɗ] |  |
| ⟨dh⟩ | [d̤] |  |
| ⟨dz⟩ | [d͡z̤] |  |
| ⟨dzv⟩ | [d͡z̤ᵝ] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ̤] |  |
| ⟨h⟩ | [ɦ] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [d͡ʒ̤] |  |
| ⟨k⟩ | [k] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [ᵐb] |  |
| ⟨mh⟩ | [m̤] |  |
| ⟨mv⟩ | [mʋ̤] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [ⁿd] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nh⟩ | [n̤] |  |
| ⟨nj⟩ | [ⁿd͡ʒ̤] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨nz⟩ | [ⁿz̤] |  |
| ⟨nzv⟩ | [ⁿz̤ᵝ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨pf⟩ | [p͡f] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨sv⟩ | [sᶲ] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [t͡s] |  |
| ⟨tsv⟩ | [t͡sᶲ] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [ʋ] |  |
| ⟨vh⟩ | [v̤] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z̤] |  |
| ⟨zh⟩ | [ʒ̤] |  |
| ⟨zv⟩ | [z̤ᵝ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sn")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Shihhi Arabic](ssh.md) · [Home](../index.md) · [Shor →](cjs.md)
