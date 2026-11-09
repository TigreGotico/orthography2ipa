# Irish (`ga`)

<!-- atlas:summary begin -->
Irish is a Goidelic language, written in the Latin script. Glottolog places it in Ireland and United Kingdom. The `ga` spec is at the research tier. It cites 6 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ga` |
| ISO 639-3 | [gle](https://iso639-3.sil.org/code/gle), Irish |
| Glottolog | [iris1253](https://glottolog.org/resource/languoid/id/iris1253), Irish |
| Wikidata | [Q9142](https://www.wikidata.org/wiki/Q9142) |
| Wikipedia | [Irish language](https://en.wikipedia.org/wiki/Irish_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Celtic > Goidelic](by-family.md#indo-european--celtic--goidelic) |
| Region | [Eurasia](by-region.md#eurasia) > [Ireland](by-region.md#ireland), [United Kingdom](by-region.md#united-kingdom) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1600, living |
| Ancestor | [Proto-Goidelic (reconstructed)](https://tigregotico.github.io/orthography2ipa/#cel-x-goidelic) `cel-x-goidelic` |
| Explorer | [`ga` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ga) |
| Spec file | [`ga.json`](../../orthography2ipa/data/ga.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Irish (Gaeilge). ~1.7M speakers (2016 census, ~80K daily L1). PERVASIVE BROAD/SLENDER DISTINCTION: every consonant has two versions (velarised 'broad' vs palatalised 'slender'), and the flanking vowel LETTERS encode which, 'caol le caol agus leathan le leathan'.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 6 works, from 1989 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 45 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ga.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ga` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 2 of them have a DOI or a URL. The spec file holds a note on what 3 of them support.

1. <a id="src-odochartaigh1992"></a>Ó Dochartaigh, C. (1992). *The Irish Language*. Dublin Institute for Advanced Studies.
2. <a id="src-macaulay1992"></a>MacAulay, D. (ed.) (1992). *The Celtic Languages*. Cambridge University Press.
3. <a id="src-o_siadhail1989"></a>Ó Siadhail, M. (1989). *Modern Irish: Grammatical Structure and Dialectal Variation*. Cambridge University Press.
4. <a id="src-ni_chiosain1999"></a>Ní Chiosáin, M. (1999). *Syllables and Phonotactics in Irish*. Cambridge University Press.
5. <a id="src-wp_ga_orthography"></a>Wikipedia contributors (2026). *Irish orthography*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Irish_orthography)
6. <a id="src-wp_ga_phonology"></a>Wikipedia contributors (2026). *Irish phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Irish_phonology)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ga` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 9616 | 0.1834 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `ga` | generated | espeak-derived | CC BY 4.0 | 1611 | 0.2989 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 59 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | bʲ bˠ pʲ pˠ |  | dʲ d̪ˠ tʲ t̪ˠ |  | c ɟ | k ɡ |  |
| Nasal | mʲ mˠ |  | nʲ nˠ n̪ˠ |  | ɲ | ŋ |  |
| Tap |  |  | ɾʲ ɾˠ |  |  |  |  |
| Fricative |  | fʲ fˠ vʲ | sˠ | ʃ | ç | x ɣ | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | lʲ lˠ l̪ˠ |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Near-close | ɪ |  | ʊ |
| Close-mid | e eː |  | o oː |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Open | a aː |  | ɑ |

Sequences that the spec writes as one unit: [lʲə] [lˠə] [l̪ˠə] [nʲə] [nˠə] [n̪ˠə] [w] [ɾʲə] [ɾˠə].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] [ɑ] | after i [ə] · after u [ə] · before front vowel ∅ · before i [a] · nucleus unstressed [ə] · word final [ə] |
| ⟨ae⟩ | [eː] |  |
| ⟨ao⟩ | [iː] [eː] |  |
| ⟨b⟩ | [bˠ] [bʲ] | after front vowel [bʲ] · before front vowel [bʲ] |
| ⟨bh⟩ | [w] [vʲ] | after front vowel [vʲ] · before front vowel [vʲ] |
| ⟨bhf⟩ | [w] [vʲ] | after front vowel [vʲ] · before front vowel [vʲ] |
| ⟨bp⟩ | [bˠ] [bʲ] | after front vowel [bʲ] · before front vowel [bʲ] |
| ⟨c⟩ | [k] [c] | after front vowel [c] · before front vowel [c] |
| ⟨ch⟩ | [x] [ç] | after front vowel [ç] · before front vowel [ç] |
| ⟨d⟩ | [d̪ˠ] [dʲ] | after front vowel [dʲ] · before front vowel [dʲ] |
| ⟨dh⟩ | [ɣ] [j] | after front vowel [j] · before front vowel [j] · word final ∅ |
| ⟨dt⟩ | [d̪ˠ] [dʲ] | after front vowel [dʲ] · before front vowel [dʲ] |
| ⟨e⟩ | [ɛ] [e] | before back vowel ∅ · nucleus unstressed [ə] · word final [ə] |
| ⟨f⟩ | [fˠ] [fʲ] | after front vowel [fʲ] · before front vowel [fʲ] |
| ⟨fh⟩ | ∅ |  |
| ⟨g⟩ | [ɡ] [ɟ] | after front vowel [ɟ] · before front vowel [ɟ] |
| ⟨gc⟩ | [ɡ] [ɟ] | after front vowel [ɟ] · before front vowel [ɟ] |
| ⟨gh⟩ | [ɣ] [j] | after front vowel [j] · before front vowel [j] · word final ∅ |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ɪ] [i] | after vowel ∅ · before a [i] · before u ∅ |
| ⟨l⟩ | [l̪ˠ] [lˠ] [lʲ] | after front vowel [lʲ] · before front vowel [lʲ] · intervocalic [lˠ] [l̪ˠ] · word initial [l̪ˠ] |
| ⟨ll⟩ | [l̪ˠ] [lʲ] | after front vowel [lʲ] · before front vowel [lʲ] |
| ⟨m⟩ | [mˠ] [mʲ] | after front vowel [mʲ] · before front vowel [mʲ] |
| ⟨mb⟩ | [mˠ] [mʲ] | after front vowel [mʲ] · before front vowel [mʲ] |
| ⟨mh⟩ | [w] [vʲ] | after front vowel [vʲ] · before front vowel [vʲ] |
| ⟨n⟩ | [n̪ˠ] [nˠ] [nʲ] | after front vowel [nʲ] · before front vowel [nʲ] · intervocalic [nˠ] [n̪ˠ] · word initial [n̪ˠ] |
| ⟨nd⟩ | [n̪ˠ] [nʲ] | after front vowel [nʲ] · before front vowel [nʲ] |
| ⟨ng⟩ | [ŋ] [ɲ] | after front vowel [ɲ] · before front vowel [ɲ] |
| ⟨nn⟩ | [n̪ˠ] [nʲ] | after front vowel [nʲ] · before front vowel [nʲ] |
| ⟨o⟩ | [ɔ] [o] | after e [oː] · after front vowel ∅ · nucleus unstressed [ə] |
| ⟨p⟩ | [pˠ] [pʲ] | after front vowel [pʲ] · before front vowel [pʲ] |
| ⟨ph⟩ | [fˠ] [fʲ] | after front vowel [fʲ] · before front vowel [fʲ] |
| ⟨r⟩ | [ɾˠ] [ɾʲ] | after front vowel [ɾʲ] · before front vowel [ɾʲ] |
| ⟨rr⟩ | [ɾˠ] |  |
| ⟨s⟩ | [sˠ] [ʃ] | after front vowel [ʃ] · before front vowel [ʃ] |
| ⟨sh⟩ | [h] |  |
| ⟨t⟩ | [t̪ˠ] [tʲ] | after front vowel [tʲ] · before front vowel [tʲ] |
| ⟨th⟩ | [h] |  |
| ⟨ts⟩ | [t̪ˠ] [tʲ] | after front vowel [tʲ] · before front vowel [tʲ] |
| ⟨u⟩ | [ʊ] [u] | before a [u] · before front vowel ∅ · before i [ɪ] · nucleus unstressed [ə] |
| ⟨á⟩ | [aː] |  |
| ⟨é⟩ | [eː] |  |
| ⟨í⟩ | [iː] |  |
| ⟨ó⟩ | [oː] |  |
| ⟨ú⟩ | [uː] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 8 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `GA_SVARABHAKTI_L_BROAD_DENTAL` | /l̪ˠ/ → [l̪ˠə], before [bˠ] [bʲ] [w] [vʲ] [x] [ç] [fˠ] [fʲ] and 6 more | - | Siadhail 1989 |
| `GA_SVARABHAKTI_L_BROAD` | /lˠ/ → [lˠə], before [bˠ] [bʲ] [w] [vʲ] [x] [ç] [fˠ] [fʲ] and 6 more | - | Siadhail 1989 |
| `GA_SVARABHAKTI_L_SLENDER` | /lʲ/ → [lʲə], before [bˠ] [bʲ] [w] [vʲ] [x] [ç] [fˠ] [fʲ] and 6 more | - | Siadhail 1989 |
| `GA_SVARABHAKTI_N_BROAD_DENTAL` | /n̪ˠ/ → [n̪ˠə], before [bˠ] [bʲ] [w] [vʲ] [x] [ç] [fˠ] [fʲ] and 6 more | - | Siadhail 1989 |
| `GA_SVARABHAKTI_N_BROAD` | /nˠ/ → [nˠə], before [bˠ] [bʲ] [w] [vʲ] [x] [ç] [fˠ] [fʲ] and 6 more | ⟨leanbh⟩ [ˈl̠ʲanˠəw] | Siadhail 1989 |
| `GA_SVARABHAKTI_N_SLENDER` | /nʲ/ → [nʲə], before [bˠ] [bʲ] [w] [vʲ] [x] [ç] [fˠ] [fʲ] and 6 more | ⟨ainm⟩ [ˈanʲəmʲ] | Siadhail 1989 |
| `GA_SVARABHAKTI_R_BROAD` | /ɾˠ/ → [ɾˠə], before [bˠ] [bʲ] [w] [vʲ] [x] [ç] [fˠ] [fʲ] and 6 more | ⟨gorm⟩ [ˈɡɔɾˠəmˠ] | Siadhail 1989 |
| `GA_SVARABHAKTI_R_SLENDER` | /ɾʲ/ → [ɾʲə], before [bˠ] [bʲ] [w] [vʲ] [x] [ç] [fˠ] [fʲ] and 6 more | - | Siadhail 1989 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ga")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Iraqw](irk.md) · [Home](../index.md) · [Isthmus-Mecayapan Nahuatl →](nhx.md)
