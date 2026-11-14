# Tarifit (Riffian Berber) (`rif`)

<!-- atlas:summary begin -->
Tarifit (Riffian Berber) is a Berber language, written in the Latin script. Glottolog places it in Algeria, Morocco and Spain. The `rif` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `rif` |
| ISO 639-3 | [rif](https://iso639-3.sil.org/code/rif), Tarifit |
| Glottolog | [tari1263](https://glottolog.org/resource/languoid/id/tari1263), Tarifiyt-Beni-Iznasen-Eastern Middle Atlas Berber |
| Wikidata | [Q34174](https://www.wikidata.org/wiki/Q34174) |
| Wikipedia | [Tarifit](https://en.wikipedia.org/wiki/Tarifit) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Berber](by-family.md#afro-asiatic--berber) |
| Region | [Africa](by-region.md#africa) > [Algeria](by-region.md#algeria), [Morocco](by-region.md#morocco), [Spain](by-region.md#spain) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1900, living |
| Ancestor | [Berber (Proto-Berber / Common Tamazight)](https://tigregotico.github.io/orthography2ipa/#ber) `ber` |
| Explorer | [`rif` in the data explorer](https://tigregotico.github.io/orthography2ipa/#rif) |
| Spec file | [`rif.json`](../../orthography2ipa/data/rif.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Tarifit / Riffian Berber, a Zenati Northern Berber language of the Rif region of northern Morocco (~1.2M speakers).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 2009 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 50 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/rif.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `rif` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 4 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-kossmann_mourigh2020"></a>Kossmann, Maarten & Mourigh, Khalid (2020). *An introduction to Tarifiyt Berber (Nador, Morocco)*. Ugarit Verlag. [dokumen.pub](https://dokumen.pub/an-introduction-to-tarifiyt-berber-nador-morocco-9783868353075.html)
2. <a id="src-tarifit_wiki"></a>Wikipedia contributors (2026). *Tarifit*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Tarifit)
3. <a id="src-berber_latin_wiki"></a>Wikipedia contributors (2024). *Berber Latin alphabet*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Berber_Latin_alphabet)
4. <a id="src-wold_tarifiyt_kossmann"></a>Kossmann, Maarten (2009). *Tarifiyt Berber vocabulary (WOLD chapter 12, 'Loanwords in Tarifiyt Berber')*. World Loanword Database (Max Planck Institute for Evolutionary Anthropology). [wold.clld.org](https://wold.clld.org/vocabulary/6)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wold` ([lexibank/wold](https://github.com/lexibank/wold)) | `rif` | gold | lexicon-derived | CC BY 4.0 | 1533 | 0.0929 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 42 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k kːʷ ɡ ɡːʷ | q |  | ʔ |
| Affricate |  |  |  |  | dʒ tʃ |  |  |  |  |  |
| Nasal | m |  |  | n |  |  | ŋ |  |  |  |
| Trill |  |  |  | r |  |  |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |  |  |
| Fricative | β | f | ð θ | s z | ʃ ʒ | ɕ | x ɣ |  | ħ ʕ | ɦ |
| Approximant |  |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Near-close | ɪ |  | ʊ |
| Mid |  | ə |  |
| Near-open | æ |  |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨3⟩ | [ʕ] |  |
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dh⟩ | [ð] |  |
| ⟨e⟩ | [ə] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gh⟩ | [ɣ] |  |
| ⟨gw⟩ | [ɡːʷ] |  |
| ⟨h⟩ | [ħ] |  |
| ⟨hh⟩ | [ɦ] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kw⟩ | [kːʷ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [q] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [θ] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ç⟩ | [ɕ] |  |
| ⟨ā⟩ | [aː] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨đ⟩ | [ð] |  |
| ⟨ħ⟩ | [ħ] |  |
| ⟨ŋ⟩ | [ŋ] |  |
| ⟨ř⟩ | [r] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ŧ⟩ | [θ] |  |
| ⟨ž⟩ | [ʒ] |  |
| ⟨ƀ⟩ | [β] |  |
| ⟨ǧ⟩ | [dʒ] |  |
| ⟨ə⟩ | [ə] |  |
| ⟨ɣ⟩ | [ɣ] |  |
| ⟨ʔ⟩ | [ʔ] |  |
| ⟨ʕ⟩ | [ʕ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "rif")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Tamil](ta.md) · [Home](../index.md) · [Tatar →](tt.md)
