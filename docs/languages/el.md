# Modern Greek (`el`)

<!-- atlas:summary begin -->
Modern Greek is a Hellenic language, written in the Greek script. Glottolog places it in 10 countries. The `el` spec is at the research tier. It cites 3 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `el` |
| Aliases | `ell` |
| ISO 639-3 | [ell](https://iso639-3.sil.org/code/ell), Modern Greek (1453-) |
| Glottolog | [mode1248](https://glottolog.org/resource/languoid/id/mode1248), Modern Greek |
| Wikidata | [Q36510](https://www.wikidata.org/wiki/Q36510) |
| Wikipedia | [Modern Greek](https://en.wikipedia.org/wiki/Modern_Greek) |
| Family | [Indo-European](by-family.md#indo-european) > [Hellenic](by-family.md#indo-european--hellenic) |
| Region | [Eurasia](by-region.md#eurasia) > [Albania](by-region.md#albania), [Bulgaria](by-region.md#bulgaria), [Cyprus](by-region.md#cyprus), [Egypt](by-region.md#egypt), [Greece](by-region.md#greece), [Italy](by-region.md#italy), [North Macedonia](by-region.md#north-macedonia), [Romania](by-region.md#romania) and 2 more |
| Script | [Greek](by-script.md#greek) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Ancestor | [Classical Greek (Attic)](https://tigregotico.github.io/orthography2ipa/#grc) `grc` |
| Child lects | 4, see [Related lects](#related-lects) |
| Explorer | [`el` in the data explorer](https://tigregotico.github.io/orthography2ipa/#el) |
| Spec file | [`el.json`](../../orthography2ipa/data/el.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Modern Greek (Demotic). 5-vowel system despite many graphemic representations. Digraphs ⟨μπ⟩, ⟨ντ⟩, ⟨γκ⟩ represent voiced stops, with prenasalisation medially.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1996 to 1999. [Sources](#sources) lists them. The spec file writes all 90 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/el.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `el` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Pontic Greek](pnt.md) `pnt`: Bulgaria, Greece, North Macedonia, Türkiye, research tier
- [Cypriot Greek](el-CY.md) `el-CY`: Cyprus, research tier
- [Yevanic](https://tigregotico.github.io/orthography2ipa/#yej) `yej`: Greece, stub tier
- [Cappadocian Greek](https://tigregotico.github.io/orthography2ipa/#cpg) `cpg`: Greece, Türkiye, skeleton tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-arvaniti1999"></a>Arvaniti, A. (1999). *Greek*. Journal of the International Phonetic Association. Cited: 167-172.
2. <a id="src-holton_mackridge_philippaki1997"></a>Holton, D., Mackridge, P. & Philippaki-Warburton, I. (1997). *Greek: A Comprehensive Grammar of the Modern Language*. Routledge.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `el` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 19108 | 0.0327 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `el` | generated | epitran-derived | CC0 1.0 | 5983 | 0.2653 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 42 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t | c | k ɡ |
| Affricate |  |  |  | dz ts |  |  |
| Nasal | m |  |  | n |  | ŋ |
| Trill |  |  |  | r |  |  |
| Tap |  |  |  | ɾ |  |  |
| Fricative |  | f v | ð θ | s z | ç ʝ | x ɣ |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  |  | l |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [af] [av] [ef] [ev] [ks] [mb] [nd] [ps] [ŋɟ] [ŋɡ] [ʝi].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ΐ⟩ | [i] |  |
| ⟨ά⟩ | [a] |  |
| ⟨έ⟩ | [e] |  |
| ⟨ή⟩ | [i] |  |
| ⟨ί⟩ | [i] |  |
| ⟨ΰ⟩ | [i] |  |
| ⟨α⟩ | [a] |  |
| ⟨αί⟩ | [e] |  |
| ⟨αι⟩ | [e] |  |
| ⟨αυ⟩ | [av] [af] | before consonant [af] [av] · default [av] |
| ⟨αύ⟩ | [av] [af] | before consonant [af] [av] · default [av] |
| ⟨αὶ⟩ | [e] |  |
| ⟨αὺ⟩ | [av] [af] |  |
| ⟨αῖ⟩ | [e] |  |
| ⟨αῦ⟩ | [av] [af] |  |
| ⟨β⟩ | [v] |  |
| ⟨ββ⟩ | [v] |  |
| ⟨γ⟩ | [ɣ] [ʝ] | before front vowel [ʝ] · default [ɣ] |
| ⟨γγ⟩ | [ŋɡ] | before front vowel [ŋɟ] · default [ŋɡ] |
| ⟨γκ⟩ | [ɡ] [ŋɡ] | before front vowel [ŋɟ] · default [ŋɡ] · word initial [ɡ] |
| ⟨δ⟩ | [ð] |  |
| ⟨ε⟩ | [e] |  |
| ⟨εί⟩ | [i] |  |
| ⟨ει⟩ | [i] |  |
| ⟨ευ⟩ | [ev] [ef] | before consonant [ef] [ev] · default [ev] |
| ⟨εύ⟩ | [ev] [ef] | before consonant [ef] [ev] · default [ev] |
| ⟨εὶ⟩ | [i] |  |
| ⟨εὺ⟩ | [ev] [ef] |  |
| ⟨εῖ⟩ | [i] |  |
| ⟨εῦ⟩ | [ev] [ef] |  |
| ⟨ζ⟩ | [z] |  |
| ⟨η⟩ | [i] |  |
| ⟨θ⟩ | [θ] |  |
| ⟨ι⟩ | [i] |  |
| ⟨κ⟩ | [k] [c] | before front vowel [c] · default [k] |
| ⟨κκ⟩ | [k] |  |
| ⟨λ⟩ | [l] | default [l] |
| ⟨λλ⟩ | [l] |  |
| ⟨μ⟩ | [m] |  |
| ⟨μμ⟩ | [m] |  |
| ⟨μπ⟩ | [b] [mb] | default [mb] · word initial [b] |
| ⟨ν⟩ | [n] |  |
| ⟨νν⟩ | [n] |  |
| ⟨ντ⟩ | [d] [nd] | default [nd] · word initial [d] |
| ⟨ξ⟩ | [ks] |  |
| ⟨ο⟩ | [o] |  |
| ⟨οί⟩ | [i] |  |
| ⟨οι⟩ | [i] |  |
| ⟨ου⟩ | [u] |  |
| ⟨ού⟩ | [u] |  |
| ⟨οὶ⟩ | [i] |  |
| ⟨οὺ⟩ | [u] |  |
| ⟨οῖ⟩ | [i] |  |
| ⟨οῦ⟩ | [u] |  |
| ⟨π⟩ | [p] |  |
| ⟨ππ⟩ | [p] |  |
| ⟨ρ⟩ | [ɾ] [r] |  |
| ⟨ρρ⟩ | [ɾ] |  |
| ⟨ς⟩ | [s] |  |
| ⟨σ⟩ | [s] | before consonant [s] [z] · default [s] · word final [s] |
| ⟨σσ⟩ | [s] |  |
| ⟨τ⟩ | [t] |  |
| ⟨τζ⟩ | [dz] |  |
| ⟨τσ⟩ | [ts] |  |
| ⟨ττ⟩ | [t] |  |
| ⟨υ⟩ | [i] |  |
| ⟨υι⟩ | [i] |  |
| ⟨φ⟩ | [f] |  |
| ⟨χ⟩ | [x] [ç] | before front vowel [ç] · default [x] |
| ⟨ψ⟩ | [ps] |  |
| ⟨ω⟩ | [o] |  |
| ⟨ϊ⟩ | [i] |  |
| ⟨ϋ⟩ | [i] |  |
| ⟨ό⟩ | [o] |  |
| ⟨ύ⟩ | [i] |  |
| ⟨ώ⟩ | [o] |  |
| ⟨ὰ⟩ | [a] |  |
| ⟨ὲ⟩ | [e] |  |
| ⟨ὴ⟩ | [i] |  |
| ⟨ὶ⟩ | [i] |  |
| ⟨ὸ⟩ | [o] |  |
| ⟨ὺ⟩ | [i] |  |
| ⟨ὼ⟩ | [o] |  |
| ⟨ᾶ⟩ | [a] |  |
| ⟨ῆ⟩ | [i] |  |
| ⟨ῖ⟩ | [i] |  |
| ⟨ῗ⟩ | [i] |  |
| ⟨ῦ⟩ | [i] |  |
| ⟨ῧ⟩ | [i] |  |
| ⟨ῶ⟩ | [o] |  |

Stress falls on the penult by default. A written ⟨ά⟩ ⟨έ⟩ ⟨ή⟩ ⟨ί⟩ ⟨ό⟩ ⟨ύ⟩ ⟨ώ⟩ ⟨ΐ⟩ ⟨ΰ⟩ ⟨ᾶ⟩ ⟨ῆ⟩ ⟨ῖ⟩ ⟨ῦ⟩ ⟨ῶ⟩ ⟨ῗ⟩ ⟨ῧ⟩ ⟨ὰ⟩ ⟨ὲ⟩ ⟨ὴ⟩ ⟨ὶ⟩ ⟨ὸ⟩ ⟨ὺ⟩ ⟨ὼ⟩ marks the stressed vowel.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 2 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `EL_S_VOICING` | /s/ → [z], before [m] [n] [l] [ɾ] [r] [v] [ð] [ɣ] and 5 more | ⟨Άρκανσας⟩ [aɾkanzas] | Arvaniti 2007 |
| `EL_GAMMA_FRONTING` | /ɣ/ → [ʝ], before a front vowel, spelled ⟨γ⟩ | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "el")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Mizo](lus.md) · [Home](../index.md) · [Mohawk →](moh.md)
