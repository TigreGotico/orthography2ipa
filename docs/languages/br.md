# Breton (`br`)

<!-- atlas:summary begin -->
Breton is a Brythonic language, written in the Latin script. Glottolog places it in France. The `br` spec is at the research tier. It cites 6 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `br` |
| ISO 639-3 | [bre](https://iso639-3.sil.org/code/bre), Breton |
| Glottolog | [bret1244](https://glottolog.org/resource/languoid/id/bret1244), Breton |
| Wikidata | [Q12107](https://www.wikidata.org/wiki/Q12107) |
| Wikipedia | [Breton language](https://en.wikipedia.org/wiki/Breton_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Celtic > Brythonic](by-family.md#indo-european--celtic--brythonic) |
| Region | [Eurasia](by-region.md#eurasia) > [France](by-region.md#france) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Ancestor | [Common Brythonic](https://tigregotico.github.io/orthography2ipa/#xbr) `xbr` |
| Explorer | [`br` in the data explorer](https://tigregotico.github.io/orthography2ipa/#br) |
| Spec file | [`br.json`](../../orthography2ipa/data/br.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Breton (Brezhoneg). ~200,000 speakers (est. 2020). Brittany, France. Brought from Britain by insular Brythonic speakers (~5th, 6th c. CE). Four main dialects: Léonard (KLT basis), Trégorrois, Cornouaillais, Vannetais (most divergent).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 6 works, from 1978 to 2026. [Sources](#sources) lists them. The spec file writes all 52 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/br.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `br` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 2 of them have a DOI or a URL. The spec file holds a note on what 3 of them support.

1. <a id="src-macaulay1992"></a>MacAulay, D. (ed.) (1992). *The Celtic Languages*. Cambridge University Press.
2. <a id="src-ternes1992"></a>Ternes, E. (1992). *The Breton Language*. in D. MacAulay (ed.), The Celtic Languages.
3. <a id="src-favereau1997"></a>Favereau, F. (1997). *Grammaire du breton contemporain*. Skol Vreizh.
4. <a id="src-hewitt1978"></a>Hewitt, S. (1978). *Breton (Treger dialect)*. Journal of the International Phonetic Association 8(1-2). Cited: p. 80. [doi.org](https://doi.org/10.1017/S0025100300001766)
5. <a id="src-arbres_accentuation"></a>Jouitteau, M. (ed.) (2026). *ARBRES: wikigrammaire des dialectes du breton, Accentuation*. IKER, CNRS. [arbres.iker.cnrs.fr](https://arbres.iker.cnrs.fr/index.php/Accentuation)
6. <a id="src-press1986"></a>Press, I. (1986). *A Grammar of Modern Breton*. Mouton de Gruyter (Mouton Grammar Library 2), Berlin. Cited: pp. 21-24, 27-29, 34.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `br` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 803 | 0.3073 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 53 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x | ʁ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  | ʎ |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y ĩ ỹ | u |
| Close-mid | e eː ø øː ẽ | o oː |
| Open-mid | œ œ̃ ɛ | ɔ ɔ̃ |
| Open | a aː | ɑ̃ |

Sequences that the spec writes as one unit: [aw] [ew] [w] [wa] [we] [ɔw] [ɛj] [ɥ] [ɥi] [ː].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ae⟩ | [ɛ] |  |
| ⟨aou⟩ | [aw] [ɔw] |  |
| ⟨añ⟩ | [ɑ̃] |  |
| ⟨b⟩ | [b] |  |
| ⟨c'h⟩ | [x] [h] |  |
| ⟨ch⟩ | [ʃ] |  |
| ⟨cʼh⟩ | [x] [h] |  |
| ⟨c’h⟩ | [x] [h] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨ei⟩ | [ɛj] |  |
| ⟨eo⟩ | [ew] |  |
| ⟨eu⟩ | [œ] [ø] |  |
| ⟨euñ⟩ | [œ̃] |  |
| ⟨eñ⟩ | [ẽ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gn⟩ | [ɲ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨iñ⟩ | [ĩ] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨lh⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨nn⟩ | [n] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨oa⟩ | [wa] |  |
| ⟨oe⟩ | [we] |  |
| ⟨ou⟩ | [u] |  |
| ⟨oñ⟩ | [ɔ̃] |  |
| ⟨où⟩ | [u] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ʁ] [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [y] |  |
| ⟨ui⟩ | [ɥi] |  |
| ⟨uñ⟩ | [ỹ] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨zh⟩ | [z] [h] |  |
| ⟨â⟩ | [aː] |  |
| ⟨ê⟩ | [eː] |  |
| ⟨ñ⟩ | ∅ |  |
| ⟨ô⟩ | [oː] |  |

Stress falls on the penult by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 11 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `BR_STRESSED_LONG_BEFORE_LENIS` | insert [ː] after /a e ɛ i o ɔ u y œ ø ɑ̃ ẽ ĩ ɔ̃ ỹ/, stressed, before [b] [d] [ɡ] [v] [z] [ʒ] [ɣ] [l] and 3 more, with more context in the spec | - | [Hewitt 1978](#src-hewitt1978) |
| `BR_STRESSED_LONG_OPEN_FINAL` | insert [ː] after /a e ɛ i o ɔ u y œ ø ɑ̃ ẽ ĩ ɔ̃ ỹ/, word-finally, stressed | ⟨du⟩ [dyː] | [Hewitt 1978](#src-hewitt1978) |
| `BR_FINAL_DEVOICE_Z` | /z/ → [s], word-finally | ⟨Breizh⟩ [bʁɛjs] | [Hewitt 1978](#src-hewitt1978) |
| `BR_FINAL_DEVOICE_D` | /d/ → [t], word-finally | ⟨Gwened⟩ [ɡweːnet] | [Hewitt 1978](#src-hewitt1978) |
| `BR_FINAL_DEVOICE_G` | /ɡ/ → [k], word-finally | ⟨chug⟩ [ʃyːk] | [Hewitt 1978](#src-hewitt1978) |
| `BR_FINAL_DEVOICE_B` | /b/ → [p], word-finally | ⟨verb⟩ [veʁp] | [Hewitt 1978](#src-hewitt1978) |
| `BR_FINAL_DEVOICE_J` | /ʒ/ → [ʃ], word-finally | - | [Hewitt 1978](#src-hewitt1978) |
| `BR_E_OPEN_BEFORE_CH` | /e/ → [ɛ], before [x] | ⟨trec'h⟩ ['trɛːɣ] | [Press 1986](#src-press1986) |
| `BR_E_OPEN_BEFORE_LCH` | /e/ → [ɛ], before [l], with more context in the spec | ⟨kelc'h⟩ ['kɛlx] | [Press 1986](#src-press1986) |
| `BR_E_OPEN_BEFORE_R_CLUSTER` | /e/ → [ɛ], before [ʁ], with more context in the spec | ⟨sec'h⟩ ['sɛːɣ] | [Press 1986](#src-press1986) |
| `BR_STRESSED_LONG_BEFORE_FINAL_LENIS` | insert [ː] after /a e ɛ i o ɔ u y œ ø ɑ̃ ẽ ĩ ɔ̃ ỹ/, stressed, before [b] [d] [ɡ] [v] [z] [ʒ] [ɣ] [l] and 3 more, with more context in the spec | ⟨a-ratre⟩ [aˈraːtre] | [Hewitt 1978](#src-hewitt1978), [Press 1986](#src-press1986) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "br")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Bouyei](pcc.md) · [Home](../index.md) · [British English →](en-GB.md)
