# Karelian (`krl`)

<!-- atlas:summary begin -->
Karelian is a Finnic language, written in the Latin script. Glottolog places it in Finland and Russia. The `krl` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `krl` |
| ISO 639-3 | [krl](https://iso639-3.sil.org/code/krl), Karelian |
| Glottolog | [kare1335](https://glottolog.org/resource/languoid/id/kare1335), Karelian |
| Wikidata | [Q33557](https://www.wikidata.org/wiki/Q33557) |
| Wikipedia | [Karelian language](https://en.wikipedia.org/wiki/Karelian_language) |
| Family | [Uralic](by-family.md#uralic) > [Finnic](by-family.md#uralic--finnic) |
| Region | [Eurasia](by-region.md#eurasia) > [Finland](by-region.md#finland), [Russia](by-region.md#russia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Finnic](https://tigregotico.github.io/orthography2ipa/#x-clade-finn1317) `x-clade-finn1317` |
| Explorer | [`krl` in the data explorer](https://tigregotico.github.io/orthography2ipa/#krl) |
| Spec file | [`krl.json`](../../orthography2ipa/data/krl.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Karelian (karjala), a Finnic (Uralic) language of the Republic of Karelia and Tver Oblast, Russia. Its unified Latin orthography extends the Finnish letter set with ⟨š⟩ /ʃ/, ⟨ž⟩ /ʒ/, ⟨č⟩ /t͡ʃ/, the digraph ⟨dž⟩ /d͡ʒ/ and ⟨z⟩ /z/, ⟨c⟩ /t͡s/, ⟨v⟩ is the labial approximant /ʋ/ (inherited from the Finnish base).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1998 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes 9 of the 69 spellings of its letter table and takes the other 60 from [Finnish](fi.md) `fi`.

The [spec file](../../orthography2ipa/data/krl.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `krl` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-karelian_language_wikipedia"></a>Wikipedia contributors (2026). *Karelian language, Phonology and Orthography*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Karelian_language)
2. <a id="src-abondolo1998"></a>Abondolo, D. (ed.) (1998). *The Uralic Languages*. Routledge.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `krl` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 641 | 0.0519 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 74 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pː |  | d t tː |  |  | k kː ɡ |  |
| Affricate |  |  | t͡s | d͡ʒ t͡ʃ t͡ʃː |  |  |  |
| Nasal | m mː |  | n nː |  |  | ŋ ŋː |  |
| Trill |  |  | r rː |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f | s sː z | ʃ ʃː ʒ ʒː | ç | x | h ɦ |
| Approximant |  | ʋ |  |  | j |  |  |
| Lateral approximant |  |  | l lː |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː y yː | u uː |
| Close-mid | e eː ø øː | o oː |
| Near-open | æ æː |  |
| Open |  | ɑ ɑː |

Sequences that the spec writes as one unit: [ei] [eu] [ey] [ie] [iu] [iy] [oi] [ou] [ui] [uo] [w] [yi] [yø] [æi] [æy] [øi] [øy] [ŋk] [ɑi] [ɑu].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] |  |
| ⟨aa⟩ | [ɑː] |  |
| ⟨ai⟩ | [ɑi] |  |
| ⟨au⟩ | [ɑu] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [t͡s] |  |
| ⟨d⟩ | [d] | default [d] |
| ⟨dž⟩ | [d͡ʒ] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨ei⟩ | [ei] |  |
| ⟨eu⟩ | [eu] |  |
| ⟨ey⟩ | [ey] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ie⟩ | [ie] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨iu⟩ | [iu] |  |
| ⟨iy⟩ | [iy] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] | default [k] |
| ⟨kk⟩ | [kː] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [lː] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [mː] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋː] | default [ŋː] |
| ⟨nk⟩ | [ŋk] |  |
| ⟨nn⟩ | [nː] |  |
| ⟨o⟩ | [o] |  |
| ⟨oi⟩ | [oi] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨ou⟩ | [ou] |  |
| ⟨p⟩ | [p] | default [p] |
| ⟨pp⟩ | [pː] |  |
| ⟨r⟩ | [r] |  |
| ⟨rr⟩ | [rː] |  |
| ⟨s⟩ | [s] |  |
| ⟨ss⟩ | [sː] |  |
| ⟨t⟩ | [t] | default [t] |
| ⟨tt⟩ | [tː] |  |
| ⟨u⟩ | [u] |  |
| ⟨ui⟩ | [ui] |  |
| ⟨uo⟩ | [uo] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨v⟩ | [ʋ] |  |
| ⟨w⟩ | [ʋ] |  |
| ⟨y⟩ | [y] |  |
| ⟨yi⟩ | [yi] |  |
| ⟨yy⟩ | [yː] |  |
| ⟨yö⟩ | [yø] |  |
| ⟨z⟩ | [z] |  |
| ⟨ä⟩ | [æ] |  |
| ⟨äi⟩ | [æi] |  |
| ⟨äy⟩ | [æy] |  |
| ⟨ää⟩ | [æː] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨öi⟩ | [øi] |  |
| ⟨öy⟩ | [øy] |  |
| ⟨öö⟩ | [øː] |  |
| ⟨č⟩ | [t͡ʃ] |  |
| ⟨čč⟩ | [t͡ʃː] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨šš⟩ | [ʃː] |  |
| ⟨ž⟩ | [ʒ] |  |
| ⟨žž⟩ | [ʒː] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "krl")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Karakalpak](kaa.md) · [Home](../index.md) · [Kashmiri →](kas.md)
