# Norman (`nrf`)

<!-- atlas:summary begin -->
Norman is a Gallo-Romance language, written in the Latin script. Glottolog places it in France. The `nrf` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `nrf` |
| ISO 639-3 | [nrf](https://iso639-3.sil.org/code/nrf), Jèrriais |
| Glottolog | [norm1245](https://glottolog.org/resource/languoid/id/norm1245), Normand |
| Wikidata | [Q33850](https://www.wikidata.org/wiki/Q33850) |
| Wikipedia | [Norman language](https://en.wikipedia.org/wiki/Norman_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Gallo-Romance](by-family.md#indo-european--italic--romance--gallo-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [France](by-region.md#france) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 911, living |
| Parent | [Gallo-Romance](https://tigregotico.github.io/orthography2ipa/#x-clade-gallorom) `x-clade-gallorom` |
| Explorer | [`nrf` in the data explorer](https://tigregotico.github.io/orthography2ipa/#nrf) |
| Spec file | [`nrf.json`](../../orthography2ipa/data/nrf.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Norman (Nouormand), an Oïl (Gallo-Romance) language of Normandy, Jersey (Jèrriais), Guernsey (Dgèrnésiais) and Sark (Sercquiais).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1966 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 92 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/nrf.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `nrf` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-wiki-nrf"></a>Wikipedia contributors (2024). *Norman language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Norman_language)
2. <a id="src-wiki-jerriais"></a>Wikipedia contributors (2026). *Jèrriais*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/J%C3%A8rriais)
3. <a id="src-lemaistre1966"></a>Le Maistre, Frank (1966). *Dictionnaire Jersiais-Français*. Don Balleine Trust, Jersey.
4. <a id="src-liddicoat1994"></a>Liddicoat, Anthony J. (1994). *A Grammar of the Norman French of the Channel Islands: The Dialects of Jersey and Sark*. Mouton de Gruyter, Berlin.
5. <a id="src-jones2001"></a>Jones, Mari C. (2001). *Jersey Norman French: A Linguistic Study of an Obsolescent Dialect*. Blackwell, Oxford.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `nrf` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 143 | 0.2557 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 62 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  |  | n |  | ɲ |  |  |
| Trill |  |  |  | r |  |  |  |  |
| Fricative |  | f v | ð θ | s z | ʃ ʒ |  |  | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː y yː |  | u uː |
| Close-mid | e eː ø øː ø̃ ø̃ː ẽ ẽː |  | o oː õ õː |
| Mid |  | ə |  |
| Open-mid | œ œː ɛ ɛː ɛ̃ ɛ̃ː |  | ɔ ɔː |
| Open | a aː |  | ɑ̃ ɑ̃ː |

Sequences that the spec writes as one unit: [aj] [jo] [ks] [uj] [w] [wa] [wɛ] [ɛj].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [ɛ] [e] |  |
| ⟨ail⟩ | [aj] |  |
| ⟨aill⟩ | [aj] |  |
| ⟨au⟩ | [ɔ] |  |
| ⟨aî⟩ | [ɛː] |  |
| ⟨aï⟩ | [aj] |  |
| ⟨aû⟩ | [ɔː] |  |
| ⟨b⟩ | [b] |  |
| ⟨bb⟩ | [b] |  |
| ⟨c⟩ | [k] | before front vowel [s] · default [k] · word final ∅ |
| ⟨cc⟩ | [k] |  |
| ⟨ch⟩ | [ʃ] |  |
| ⟨ck⟩ | [k] |  |
| ⟨d⟩ | [d] | default [d] · word final ∅ |
| ⟨dd⟩ | [d] |  |
| ⟨dg⟩ | [dʒ] |  |
| ⟨e⟩ | [ə] [e] [ɛ] | default [ə] [e] [ɛ] · word final ∅ [ə] |
| ⟨eau⟩ | [o] |  |
| ⟨ei⟩ | [e] [ɛ] |  |
| ⟨eil⟩ | [ɛj] |  |
| ⟨eill⟩ | [ɛj] |  |
| ⟨eu⟩ | [ø] [œ] |  |
| ⟨eî⟩ | [eː] |  |
| ⟨eû⟩ | [øː] |  |
| ⟨f⟩ | [f] |  |
| ⟨ff⟩ | [f] |  |
| ⟨g⟩ | [ɡ] | before front vowel [ʒ] · default [ɡ] · word final ∅ |
| ⟨gg⟩ | [ɡ] |  |
| ⟨gn⟩ | [ɲ] |  |
| ⟨gu⟩ | [ɡ] |  |
| ⟨h⟩ | [h] ∅ | default ∅ · word initial [h] ∅ |
| ⟨i⟩ | [i] | before vowel [j] [i] · default [i] |
| ⟨iau⟩ | [jo] |  |
| ⟨ill⟩ | [j] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ngn⟩ | [ɲ] |  |
| ⟨nn⟩ | [n] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨oe⟩ | [ø] |  |
| ⟨oeu⟩ | [œ] |  |
| ⟨oi⟩ | [wa] [wɛ] |  |
| ⟨ou⟩ | [u] | before vowel [w] · default [u] |
| ⟨ouil⟩ | [uj] |  |
| ⟨ouill⟩ | [uj] |  |
| ⟨oê⟩ | [øː] |  |
| ⟨oî⟩ | [wɛ] |  |
| ⟨où⟩ | [u] |  |
| ⟨oû⟩ | [uː] |  |
| ⟨p⟩ | [p] | default [p] · word final ∅ |
| ⟨ph⟩ | [f] |  |
| ⟨pp⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [k] |  |
| ⟨r⟩ | [r] | default [r] · word final ∅ [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] [z] | default [s] · intervocalic [z] · word final ∅ |
| ⟨sc⟩ | [s] |  |
| ⟨ss⟩ | [s] |  |
| ⟨t⟩ | [t] | default [t] · word final ∅ |
| ⟨tch⟩ | [tʃ] |  |
| ⟨th⟩ | [ð] [θ] |  |
| ⟨tt⟩ | [t] |  |
| ⟨u⟩ | [y] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ks] | default [ks] · word final ∅ |
| ⟨y⟩ | [j] [i] |  |
| ⟨z⟩ | [z] |  |
| ⟨à⟩ | [a] |  |
| ⟨â⟩ | [aː] |  |
| ⟨ç⟩ | [ʃ] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [e] |  |
| ⟨ée⟩ | [eː] |  |
| ⟨ê⟩ | [ɛː] |  |
| ⟨ë⟩ | [ɛ] |  |
| ⟨î⟩ | [iː] |  |
| ⟨ï⟩ | [i] |  |
| ⟨òe⟩ | [œ] |  |
| ⟨òê⟩ | [œː] |  |
| ⟨ô⟩ | [oː] |  |
| ⟨ù⟩ | [y] |  |
| ⟨û⟩ | [yː] |  |
| ⟨ü⟩ | [y] |  |
| ⟨œu⟩ | [œ] |  |

The spec declares no stress rule.

Grammatical endings: ⟨-er⟩ [e], ⟨-ez⟩ [e], ⟨-ier⟩ [je].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 17 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `NRF_NASAL_a` | /a/ → [ɑ̃], before a coda nasal | - | - |
| `NRF_NASAL_aː` | /aː/ → [ɑ̃ː], before a coda nasal | - | - |
| `NRF_NASAL_IEN` | /ə/ → [ẽ], before a coda nasal, after [j], spelled ⟨e⟩ | - | - |
| `NRF_NASAL_ə` | /ə/ → [ɑ̃], before a coda nasal | - | - |
| `NRF_NASAL_i` | /i/ → [ẽ], before a coda nasal | - | - |
| `NRF_NASAL_iː` | /iː/ → [ẽː], before a coda nasal | - | - |
| `NRF_NASAL_o` | /o/ → [õ], before a coda nasal | - | - |
| `NRF_NASAL_oː` | /oː/ → [õː], before a coda nasal | - | - |
| `NRF_NASAL_u` | /u/ → [õ], before a coda nasal | ⟨raisoun⟩ [rɛzõ] | - |
| `NRF_NASAL_y` | /y/ → [ø̃], before a coda nasal | - | - |
| `NRF_NASAL_yː` | /yː/ → [ø̃ː], before a coda nasal | - | - |
| `NRF_NASAL_ɛ` | /ɛ/ → [ɛ̃], before a coda nasal | - | - |
| `NRF_NASAL_ɛː` | /ɛː/ → [ɛ̃ː], before a coda nasal | - | - |
| `NRF_NASAL_ABSORB` | /n m/ → ∅, in the coda, after a vowel | - | - |
| `NRF_CL_PALATAL` | /l/ → ∅, after a consonant, before ⟨i⟩ ⟨y⟩ | - | - |
| `NRF_E_CLOSED` | /ə/ → [ɛ], before a consonant cluster, spelled ⟨e⟩ | - | - |
| `NRF_E_FINAL_CLOSED` | /ə/ → [ɛ], before a coda, spelled ⟨e⟩, with more context in the spec | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "nrf")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Nogai](nog.md) · [Home](../index.md) · [Norman →](nrm.md)
