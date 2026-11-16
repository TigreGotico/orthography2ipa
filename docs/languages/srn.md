# Sranan Tongo (`srn`)

<!-- atlas:summary begin -->
Sranan Tongo is an English Creole language, written in the Latin script. Glottolog places it in Netherlands and Suriname. The `srn` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `srn` |
| ISO 639-3 | [srn](https://iso639-3.sil.org/code/srn), Sranan Tongo |
| Glottolog | [sran1240](https://glottolog.org/resource/languoid/id/sran1240), Sranan Tongo |
| Wikipedia | [Sranan Tongo](https://en.wikipedia.org/wiki/Sranan_Tongo) |
| Family | [English Creole](by-family.md#english-creole) |
| Region | [South America](by-region.md#south-america) > [Netherlands](by-region.md#netherlands), [Suriname](by-region.md#suriname) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1650, living |
| Explorer | [`srn` in the data explorer](https://tigregotico.github.io/orthography2ipa/#srn) |
| Spec file | [`srn.json`](../../orthography2ipa/data/srn.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Sranan Tongo (Sranantongo), the English-lexifier creole lingua franca of Suriname, with heavy Dutch and West African (Gbe, Kikongo) input.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1989 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 31 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/srn.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `srn` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 4 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-sranan_tongo_wiki"></a>Wikipedia contributors (2026). *Sranan Tongo*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Sranan_Tongo)
2. <a id="src-sranan_tongo_phonology_and_orthography_wiki"></a>Wikipedia contributors (2026). *Sranan Tongo phonology and orthography*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Sranan_Tongo_phonology_and_orthography)
3. <a id="src-srn_spelling_1986"></a>Stichting Volkslectuur Suriname (1995). *Korte handleiding voor de spelling van het Sranan volgens de Resolutie van 15 juli 1986 No. 4501, in Woordenlijst Sranan-Nederlands/Nederlands-Sranan/English-Sranan*. Vaco, Paramaribo. Cited: 34-35. [writersunlimited.nl](https://www.writersunlimited.nl/winternachten/documenten/korte_handleiding_sranan.pdf)
4. <a id="src-holm1989"></a>Holm, John (1989). *Pidgins and Creoles, Volume II: Reference Survey*. Cambridge University Press.
5. <a id="src-apics2013"></a>Michaelis, S.M., Maurer, P., Haspelmath, M. & Huber, M. (eds.) (2013). *The Atlas of Pidgin and Creole Language Structures (APiCS)*. Oxford University Press. [apics-online.info](https://apics-online.info/)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `srn` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 702 | 0.0450 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 31 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  | d͡ʒ t͡ʃ |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f | s z | ʃ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid |  | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [ai̯] [au̯] [ei̯] [oi̯] [ou̯] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [ai̯] |  |
| ⟨aw⟩ | [au̯] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨dy⟩ | [d͡ʒ] |  |
| ⟨e⟩ | [e] |  |
| ⟨ei⟩ | [ei̯] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] |  |
| ⟨oi⟩ | [oi̯] |  |
| ⟨ow⟩ | [ou̯] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sy⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨ty⟩ | [t͡ʃ] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ò⟩ | [ɔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "srn")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Southern Yukaghir](yux.md) · [Home](../index.md) · [Standard Moroccan Tamazight →](zgh.md)
