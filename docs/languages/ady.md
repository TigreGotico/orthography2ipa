# Adyghe (`ady`)

<!-- atlas:summary begin -->
Adyghe is an Abkhaz-Adyge language, written in the Cyrillic script. Glottolog places it in 5 countries. The `ady` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ady` |
| ISO 639-3 | [ady](https://iso639-3.sil.org/code/ady), Adyghe |
| Glottolog | [adyg1241](https://glottolog.org/resource/languoid/id/adyg1241), West Circassian |
| Wikidata | [Q27776](https://www.wikidata.org/wiki/Q27776) |
| Wikipedia | [Adyghe language](https://en.wikipedia.org/wiki/Adyghe_language) |
| Family | [Abkhaz-Adyge](by-family.md#abkhaz-adyge) |
| Region | [Eurasia](by-region.md#eurasia) > [Israel](by-region.md#israel), [Jordan](by-region.md#jordan), [Russia](by-region.md#russia), [Syria](by-region.md#syria), [Türkiye](by-region.md#türkiye) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Abkhaz-Adyge](https://tigregotico.github.io/orthography2ipa/#x-clade-abkh1242) `x-clade-abkh1242` |
| Explorer | [`ady` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ady) |
| Spec file | [`ady.json`](../../orthography2ipa/data/ady.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Adyghe (адыгабзэ, West Circassian), Northwest Caucasian, standard orthography is Cyrillic (an Arabic-based orthography is used by parts of the diaspora and is not modelled here).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2013 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 64 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ady.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ady` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-adyghe_wiki"></a>Wikipedia contributors (2024). *Adyghe language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Adyghe_language)
2. <a id="src-adyghe_phonology_wiki"></a>Wikipedia contributors (2026). *Adyghe language, Modern (Cyrillic) alphabet and phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Adyghe_language)
3. <a id="src-applebaum_gordon2013"></a>Applebaum, Ayla and Gordon, Matthew (2013). *Illustrations of the IPA: Adyghe (West Circassian)*. Journal of the International Phonetic Association.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `ady` | gold | lexicon-derived | CC BY 4.0 | 928 | 0.1684 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 65 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʷʼ pʼ |  | d t tʷʼ tʼ |  |  |  | k kʷ kʷʼ ɡʷ | q qʷ |  | ʔ ʔʷ |
| Affricate |  |  | d͡z t͡s t͡sʼ | d͡ʒ t͡ʃ t͡ʃʼ |  |  |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |  |  |
| Fricative |  | f | s z | ʃ ʒ | ʂ ʂʷ ʂʷʼ ʂʼ ʐ ʐʷ | ɕ ʑ | x xʷ ɣ | ʁ ʁʷ χ χʷ | ħ |  |
| Lateral fricative |  |  | ɬ ɬʼ ɮ |  |  |  |  |  |  |  |
| Approximant |  |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |  |

| Vowels | Front | Central |
|:--|:-:|:-:|
| Mid |  | ə |
| Open | a aː |  |

Sequences that the spec writes as one unit: [aw] [d͡ʐʷ] [ja] [jaː] [jo] [ju] [jə] [t͡ʂ] [t͡ʂʷ] [t͡ʂʼ] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [aː] |  |
| ⟨б⟩ | [b] |  |
| ⟨г⟩ | [ɣ] |  |
| ⟨гу⟩ | [ɡʷ] |  |
| ⟨гъ⟩ | [ʁ] |  |
| ⟨гъу⟩ | [ʁʷ] |  |
| ⟨д⟩ | [d] |  |
| ⟨дж⟩ | [d͡ʒ] |  |
| ⟨дз⟩ | [d͡z] |  |
| ⟨дзу⟩ | [d͡ʐʷ] |  |
| ⟨е⟩ | [ja] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨жъ⟩ | [ʐ] |  |
| ⟨жъу⟩ | [ʐʷ] |  |
| ⟨жь⟩ | [ʑ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [jə] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨ку⟩ | [kʷ] |  |
| ⟨къ⟩ | [q] |  |
| ⟨къу⟩ | [qʷ] |  |
| ⟨кӏ⟩ | [t͡ʃʼ] |  |
| ⟨кӏу⟩ | [kʷʼ] |  |
| ⟨л⟩ | [ɮ] [l] |  |
| ⟨лъ⟩ | [ɬ] |  |
| ⟨лӏ⟩ | [ɬʼ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [aw] |  |
| ⟨п⟩ | [p] |  |
| ⟨пӏ⟩ | [pʼ] |  |
| ⟨пӏу⟩ | [pʷʼ] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨тӏ⟩ | [tʼ] |  |
| ⟨тӏу⟩ | [tʷʼ] |  |
| ⟨у⟩ | [w] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ху⟩ | [xʷ] |  |
| ⟨хъ⟩ | [χ] |  |
| ⟨хъу⟩ | [χʷ] |  |
| ⟨хь⟩ | [ħ] |  |
| ⟨ц⟩ | [t͡s] |  |
| ⟨цу⟩ | [t͡ʂʷ] |  |
| ⟨цӏ⟩ | [t͡sʼ] |  |
| ⟨ч⟩ | [t͡ʃ] |  |
| ⟨чъ⟩ | [t͡ʂ] |  |
| ⟨чӏ⟩ | [t͡ʂʼ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨шъ⟩ | [ʂ] |  |
| ⟨шъу⟩ | [ʂʷ] |  |
| ⟨шӏ⟩ | [ʂʼ] |  |
| ⟨шӏу⟩ | [ʂʷʼ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ы⟩ | [ə] |  |
| ⟨э⟩ | [a] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [jaː] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨ӏ⟩ | [ʔ] |  |
| ⟨ӏу⟩ | [ʔʷ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ady")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Acehnese](ace.md) · [Home](../index.md) · [Afar →](aa.md)
