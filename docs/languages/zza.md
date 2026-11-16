# Zaza (`zza`)

<!-- atlas:summary begin -->
Zaza is an Iranian language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `zza` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `zza` |
| ISO 639-3 | [zza](https://iso639-3.sil.org/code/zza), Zaza |
| Wikipedia | [Zaza language](https://en.wikipedia.org/wiki/Zaza_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Iranian](by-family.md#indo-european--indo-iranian--iranian) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Iranian](https://tigregotico.github.io/orthography2ipa/#x-clade-iran1269) `x-clade-iran1269` |
| Explorer | [`zza` in the data explorer](https://tigregotico.github.io/orthography2ipa/#zza) |
| Spec file | [`zza.json`](../../orthography2ipa/data/zza.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Zaza (Zazaki), a Northwestern Iranian (Indo-European) language of eastern Anatolia.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2009 to 2024. [Sources](#sources) lists them. The spec file writes all 37 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/zza.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `zza` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-zza_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Zaza (zaza1246)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/zaza1246)
2. <a id="src-paul2009"></a>Paul, L. (2009). *Zazaki (chapter 9)*. In G. Windfuhr (ed.), The Iranian Languages, Routledge. Cited: 545-548. DOI [10.4324/9780203641736-16](https://doi.org/10.4324/9780203641736-16)
3. <a id="src-werner2012"></a>Werner, B. (2012). *Morphological Sketch of Southern Zazaki spoken in the area of Çermik, Çüngüş, Siverek and Gerger*. SIL International. Cited: 5-7. [forum-linguistik.de](https://forum-linguistik.de/sites/www.forum-linguistik.de/files/uploads/Zazaki%20Grammar%20Sketch%20English%20(from%20Dictionary%202012).pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `zza` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 196 | 0.2464 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 36 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | q |  |  |
| Affricate |  |  |  | dʒ tʃ |  |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x ɣ |  | ʕ | h |
| Approximant |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  | l ɫ |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː | ɨ | u uː |
| Close-mid | e |  | o |
| Open-mid | ɛ |  |  |
| Open |  |  | ɑ |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʕ] |  |
| ⟨a⟩ | [ɑ] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [dʒ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [ɫ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [q] |  |
| ⟨r⟩ | [ɾ] | word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ç⟩ | [tʃ] |  |
| ⟨ê⟩ | [e] |  |
| ⟨î⟩ | [iː] |  |
| ⟨û⟩ | [uː] |  |
| ⟨ğ⟩ | [ɣ] |  |
| ⟨ı⟩ | [ɨ] |  |
| ⟨ş⟩ | [ʃ] |  |
| ⟨‘⟩ | [ʕ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "zza")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Yucatec Mexican Spanish](es-MX-x-yucatan.md) · [Home](../index.md) · [Zazaki →](diq.md)
