# Hungarian (`hu`)

<!-- atlas:summary begin -->
Hungarian is an Uralic language, written in the Latin script. Glottolog places it in 8 countries. The `hu` spec is at the research tier. It cites 3 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `hu` |
| ISO 639-3 | [hun](https://iso639-3.sil.org/code/hun), Hungarian |
| Glottolog | [hung1274](https://glottolog.org/resource/languoid/id/hung1274), Hungarian |
| Wikidata | [Q9067](https://www.wikidata.org/wiki/Q9067) |
| Wikipedia | [Hungarian language](https://en.wikipedia.org/wiki/Hungarian_language) |
| Family | [Uralic](by-family.md#uralic) |
| Region | [Eurasia](by-region.md#eurasia) > [Austria](by-region.md#austria), [Croatia](by-region.md#croatia), [Hungary](by-region.md#hungary), [Romania](by-region.md#romania), [Serbia](by-region.md#serbia), [Slovakia](by-region.md#slovakia), [Slovenia](by-region.md#slovenia), [Ukraine](by-region.md#ukraine) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1200, living |
| Parent | [Proto-Uralic (family node)](https://tigregotico.github.io/orthography2ipa/#urj) `urj` |
| Explorer | [`hu` in the data explorer](https://tigregotico.github.io/orthography2ipa/#hu) |
| Spec file | [`hu.json`](../../orthography2ipa/data/hu.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Hungarian (Magyar). Uralic language with 14-vowel system (7 short + 7 long), vowel harmony, palatal stops /c, ɟ/, and rich agglutinative morphology. Referenced as adstrate for Romanian due to centuries of Transylvanian contact (Siptár & Törkenczy 2000).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1994 to 2001. [Sources](#sources) lists them. The spec file writes all 60 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/hu.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `hu` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-abondolo1998"></a>Abondolo, D. (ed.) (1998). *The Uralic Languages*. Routledge.
2. <a id="src-kornai1994"></a>Kornai, A. (1994). *Hungarian Vowel Harmony*. in I. Kenesei & G. Vago (eds.), Approaches to Hungarian.
3. <a id="src-rounds2001"></a>Rounds, C.H. (2001). *Hungarian: An Essential Grammar*. Routledge.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `hu` | generated | epitran-derived | CC BY 4.0 | 4776 | 0.0996 | no |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `hu` | generated | epitran-derived | CC0 1.0 | 74549 | 0.0758 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 64 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bː p pː |  | d dː t tː |  | c cː ɟ ɟː | k kː ɡ ɡː |  |
| Affricate |  |  | dz ts | dʒ tʃ tːʃ |  |  |  |
| Nasal | m mː | ɱ | n nː |  | ɲ ɲː | ŋ |  |
| Trill |  |  | r rː |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f fː v vː | s sː z zː | ʃ ʃː ʒ ʒː |  | x | h ɦ |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l lː |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː y yː | u uː |
| Close-mid | eː ø øː | o oː |
| Open-mid | ɛ |  |
| Open | aː | ɒ |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɒ] |  |
| ⟨b⟩ | [b] | default [b] |
| ⟨bb⟩ | [bː] |  |
| ⟨c⟩ | [ts] |  |
| ⟨ccs⟩ | [tːʃ] |  |
| ⟨cs⟩ | [tʃ] |  |
| ⟨d⟩ | [d] | default [d] |
| ⟨dd⟩ | [dː] |  |
| ⟨dz⟩ | [dz] |  |
| ⟨dzs⟩ | [dʒ] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨ff⟩ | [fː] |  |
| ⟨g⟩ | [ɡ] | default [ɡ] |
| ⟨gg⟩ | [ɡː] |  |
| ⟨ggy⟩ | [ɟː] |  |
| ⟨gy⟩ | [ɟ] | default [ɟ] |
| ⟨h⟩ | [h] | default [h] · word final ∅ |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨kk⟩ | [kː] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [lː] |  |
| ⟨ly⟩ | [j] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [mː] |  |
| ⟨n⟩ | [n] |  |
| ⟨nn⟩ | [nː] |  |
| ⟨nny⟩ | [ɲː] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨pp⟩ | [pː] |  |
| ⟨r⟩ | [r] |  |
| ⟨rr⟩ | [rː] |  |
| ⟨s⟩ | [ʃ] |  |
| ⟨ss⟩ | [ʃː] |  |
| ⟨ssz⟩ | [sː] |  |
| ⟨sz⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tt⟩ | [tː] |  |
| ⟨tty⟩ | [cː] |  |
| ⟨ty⟩ | [c] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] | default [v] |
| ⟨vv⟩ | [vː] |  |
| ⟨z⟩ | [z] | default [z] |
| ⟨zs⟩ | [ʒ] | default [ʒ] |
| ⟨zz⟩ | [zː] |  |
| ⟨zzs⟩ | [ʒː] |  |
| ⟨á⟩ | [aː] |  |
| ⟨é⟩ | [eː] |  |
| ⟨í⟩ | [iː] |  |
| ⟨ó⟩ | [oː] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨ú⟩ | [uː] |  |
| ⟨ü⟩ | [y] |  |
| ⟨ő⟩ | [øː] |  |
| ⟨ű⟩ | [yː] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "hu")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Hmong Daw](mww.md) · [Home](../index.md) · [Hunsrik →](hrx.md)
