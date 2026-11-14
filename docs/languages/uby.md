# Ubykh (`uby`)

<!-- atlas:summary begin -->
Ubykh is an Abkhaz-Adyge language, written in the Cyrillic script. Glottolog places it in the Eurasia macroarea. The `uby` spec is at the research tier. It cites 6 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `uby` |
| ISO 639-3 | [uby](https://iso639-3.sil.org/code/uby), Ubykh |
| Wikipedia | [Ubykh language](https://en.wikipedia.org/wiki/Ubykh_language) |
| Family | [Abkhaz-Adyge](by-family.md#abkhaz-adyge) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Abkhaz-Adyge](https://tigregotico.github.io/orthography2ipa/#x-clade-abkh1242) `x-clade-abkh1242` |
| Explorer | [`uby` in the data explorer](https://tigregotico.github.io/orthography2ipa/#uby) |
| Spec file | [`uby.json`](../../orthography2ipa/data/uby.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Ubykh was a Northwest Caucasian language, extinct since 1992, famous for one of the largest consonant inventories on record (around eighty consonants) over a two- or three-vowel system. It never had a community orthography, so there is no native spelling to convert.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 6 works, from 1931 to 2024. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 90 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/uby.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `uby` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 4 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-vogt1963"></a>Vogt, Hans (1963). *Dictionnaire de la langue oubykh*. Instituttet for Sammenlignende Kulturforskning / Adrien Maisonneuve.
2. <a id="src-dumezil1931"></a>Dumezil, Georges (1931). *La langue des Oubykhs*. Librairie Ancienne Honore Champion.
3. <a id="src-uby_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Ubykh (ubyk1235)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/ubyk1235)
4. <a id="src-uby_wiktionary_guidelines"></a>Wiktionary contributors (2022). *Wiktionary:Ubykh entry guidelines, alphabet and phonology table*. Wiktionary. [en.wiktionary.org](https://en.wiktionary.org/wiki/Wiktionary:Ubykh_entry_guidelines)
5. <a id="src-abkhaz_alphabet"></a>Wikipedia contributors (2024). *Abkhaz alphabet*. [en.wikipedia.org](https://en.wikipedia.org/wiki/Abkhaz_alphabet)
6. <a id="src-uby_wikipedia"></a>Wikipedia contributors (2024). *Ubykh language*. [en.wikipedia.org](https://en.wikipedia.org/wiki/Ubykh_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `uby` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1317 | 0.0247 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 94 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bˤ pʰ pʼ pˤʰ pˤʼ |  | d dʷ tʰ tʰʷ tʼ tʼʷ |  |  |  | kʰ kʰʲ kʰʷ kʼ kʼʲ kʼʷ ɡʲ ɡʷ | q qʲ qʷ qʼ qʼʲ qʼʷ qˤ qˤʷ qˤʼ qˤʼʷ | ʔ |
| Affricate |  |  | dz tsʰ tsʼ | dʒ tʃʰ tʃʼ | ɖʐ ʈʂʰ ʈʂʼ | dʑ dʑʷ tɕʰ tɕʰʷ tɕʼ tɕʼʷ |  |  |  |
| Nasal | m mˤ |  | n |  |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Fricative |  | f v vˤ | s z | ʃ ʃʷ ʒ ʒʷ | ʂ ʐ | ɕ ɕʷ ʑ ʑʷ | ɣ | ʁ ʁʲ ʁʷ ʁˤ ʁˤʷ χ χʲ χʷ χˤ χˤʷ | h |
| Lateral fricative |  |  | ɬ ɬʼ |  |  |  |  |  |  |
| Approximant |  |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close-mid | e̞ |  | o̞ o̞ː |
| Mid |  | ə |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [jə] [o̞w] [w] [wə] [wˤ] [əj] [əw].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨аа⟩ | [aː] |  |
| ⟨б⟩ | [b] |  |
| ⟨б'⟩ | [bˤ] |  |
| ⟨в⟩ | [v] |  |
| ⟨в'⟩ | [vˤ] |  |
| ⟨г⟩ | [ɣ] |  |
| ⟨гь⟩ | [ɡʲ] |  |
| ⟨гә⟩ | [ɡʷ] |  |
| ⟨д⟩ | [d] |  |
| ⟨дә⟩ | [dʷ] |  |
| ⟨е⟩ | [e̞] |  |
| ⟨ж⟩ | [ʐ] |  |
| ⟨жь⟩ | [ʒ] |  |
| ⟨жә⟩ | [ʒʷ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [j] | after consonant [əj] · default [j] · word initial [jə] |
| ⟨к⟩ | [kʼ] |  |
| ⟨кь⟩ | [kʼʲ] |  |
| ⟨кә⟩ | [kʼʷ] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨м'⟩ | [mˤ] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o̞] |  |
| ⟨оо⟩ | [o̞ː] |  |
| ⟨оу⟩ | [o̞w] |  |
| ⟨п⟩ | [pʼ] |  |
| ⟨п'⟩ | [pˤʼ] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [tʼ] |  |
| ⟨тә⟩ | [tʼʷ] |  |
| ⟨у⟩ | [w] | after consonant [əw] · after vowel [wə] · before consonant [wə] · default [w] · intervocalic [w] |
| ⟨у'⟩ | [wˤ] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [χ] |  |
| ⟨х'⟩ | [χˤ] |  |
| ⟨х'ә⟩ | [χˤʷ] |  |
| ⟨хь⟩ | [χʲ] |  |
| ⟨хә⟩ | [χʷ] |  |
| ⟨ц⟩ | [tsʰ] |  |
| ⟨ць⟩ | [tɕʰ] |  |
| ⟨цә⟩ | [tɕʰʷ] |  |
| ⟨ч⟩ | [tʃʰ] |  |
| ⟨ш⟩ | [ʂ] |  |
| ⟨шь⟩ | [ʃ] |  |
| ⟨шә⟩ | [ʃʷ] |  |
| ⟨ы⟩ | [ə] |  |
| ⟨џ⟩ | [ɖʐ] |  |
| ⟨џь⟩ | [dʒ] |  |
| ⟨ҙ⟩ | [ʑ] |  |
| ⟨ҙә⟩ | [ʑʷ] |  |
| ⟨қ⟩ | [kʰ] |  |
| ⟨қь⟩ | [kʰʲ] |  |
| ⟨қә⟩ | [kʰʷ] |  |
| ⟨ҟ⟩ | [qʼ] |  |
| ⟨ҟ'⟩ | [qˤʼ] |  |
| ⟨ҟ'ә⟩ | [qˤʼʷ] |  |
| ⟨ҟь⟩ | [qʼʲ] |  |
| ⟨ҟә⟩ | [qʼʷ] |  |
| ⟨ҫ⟩ | [ɕ] |  |
| ⟨ҫә⟩ | [ɕʷ] |  |
| ⟨ҭ⟩ | [tʰ] |  |
| ⟨ҭә⟩ | [tʰʷ] |  |
| ⟨ҳ⟩ | [h] |  |
| ⟨ҵ⟩ | [tsʼ] |  |
| ⟨ҵь⟩ | [tɕʼ] |  |
| ⟨ҵә⟩ | [tɕʼʷ] |  |
| ⟨ҷ⟩ | [tʃʼ] |  |
| ⟨ҽ⟩ | [ʈʂʰ] |  |
| ⟨ҿ⟩ | [ʈʂʼ] |  |
| ⟨ӄ⟩ | [q] |  |
| ⟨ӄ'⟩ | [qˤ] |  |
| ⟨ӄ'ә⟩ | [qˤʷ] |  |
| ⟨ӄь⟩ | [qʲ] |  |
| ⟨ӄә⟩ | [qʷ] |  |
| ⟨ӏ⟩ | [ʔ] |  |
| ⟨ӡ⟩ | [dz] |  |
| ⟨ӡь⟩ | [dʑ] |  |
| ⟨ӡә⟩ | [dʑʷ] |  |
| ⟨ӷ⟩ | [ʁ] |  |
| ⟨ӷ'⟩ | [ʁˤ] |  |
| ⟨ӷ'ә⟩ | [ʁˤʷ] |  |
| ⟨ӷь⟩ | [ʁʲ] |  |
| ⟨ӷә⟩ | [ʁʷ] |  |
| ⟨ԥ⟩ | [pʰ] |  |
| ⟨ԥ'⟩ | [pˤʰ] |  |
| ⟨ԯ⟩ | [ɬ] |  |
| ⟨ԯь⟩ | [ɬʼ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "uby")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Tyap](kcg.md) · [Home](../index.md) · [Udmurt →](udm.md)
