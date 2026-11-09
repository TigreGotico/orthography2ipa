# Turkish (`tr`)

<!-- atlas:summary begin -->
Turkish is a Turkic language, written in the Latin script. Glottolog places it in 12 countries. The `tr` spec is at the research tier. It cites 4 sources and has 3 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `tr` |
| Aliases | `tur` |
| ISO 639-3 | [tur](https://iso639-3.sil.org/code/tur), Turkish |
| Glottolog | [nucl1301](https://glottolog.org/resource/languoid/id/nucl1301), Turkish |
| Wikidata | [Q256](https://www.wikidata.org/wiki/Q256) |
| Wikipedia | [Turkish language](https://en.wikipedia.org/wiki/Turkish_language) |
| Family | [Turkic](by-family.md#turkic) |
| Region | [Eurasia](by-region.md#eurasia) > [Albania](by-region.md#albania), [Armenia](by-region.md#armenia), [Azerbaijan](by-region.md#azerbaijan), [Bulgaria](by-region.md#bulgaria), [Cyprus](by-region.md#cyprus), [Georgia](by-region.md#georgia), [Greece](by-region.md#greece), [Iran](by-region.md#iran) and 4 more |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Parent | [Proto-Turkic (family node)](https://tigregotico.github.io/orthography2ipa/#trk) `trk` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`tr` in the data explorer](https://tigregotico.github.io/orthography2ipa/#tr) |
| Spec file | [`tr.json`](../../orthography2ipa/data/tr.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Istanbul Turkish. Near-transparent orthography. 8-vowel system with front/back × rounded/unrounded × high/low vowel harmony.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1967 to 2005. [Sources](#sources) lists them. The spec file writes all 29 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/tr.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `tr` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Ottoman Turkish (1500-1928)](ota.md) `ota`: research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-goksel_kerslake2005"></a>Göksel, A. & Kerslake, C. (2005). *Turkish: A Comprehensive Grammar*. Routledge. Cited: 1-39 (Part I: Phonology and orthography). [routledge.com](https://www.routledge.com/Turkish-A-Comprehensive-Grammar/Goksel-Kerslake/p/book/9781138350533)
2. <a id="src-zimmer_orgun1992"></a>Zimmer, K. & Orgun, O. (1992). *Turkish (Illustrations of the IPA)*. Journal of the International Phonetic Association, 22(1-2), 43-45. Cited: 43-45. [doi.org](https://doi.org/10.1017/S0025100300004588)
3. <a id="src-lewis1967"></a>Lewis, G.L. (1967). *Turkish Grammar*. Oxford University Press.
4. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `tr` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 11579 | 0.1230 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `tr` | generated | espeak-derived | CC BY 4.0 | 2748 | 0.1372 | no |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `tr` | generated | epitran-derived | CC0 1.0 | 47013 | 0.0399 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 35 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | c ɟ | k ɡ |  |
| Affricate |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | ç | x | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l ɫ |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u ɯ |
| Close-mid | e | o |
| Open-mid | œ |  |
| Open | a |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] | default [b] · word final [p] |
| ⟨c⟩ | [dʒ] | default [dʒ] · word final [tʃ] |
| ⟨d⟩ | [d] | default [d] · word final [t] |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [ɟ] | default [ɡ] · word final [k] |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] [c] | after vowel [k] [c] · before e [c] · before i [c] · default [k] |
| ⟨l⟩ | [l] [ɫ] | before a [ɫ] · before e [l] · before i [l] · before o [ɫ] · before u [ɫ] · default [l] |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ç⟩ | [tʃ] |  |
| ⟨ö⟩ | [œ] |  |
| ⟨ü⟩ | [y] |  |
| ⟨ğ⟩ | ∅ | after vowel ∅ · default ∅ · intervocalic [j] |
| ⟨ı⟩ | [ɯ] |  |
| ⟨ş⟩ | [ʃ] |  |

Stress falls on the last syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "tr")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Tunisian Arabic](aeb-TN.md) · [Home](../index.md) · [Turkmen →](tk.md)
