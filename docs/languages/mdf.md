# Moksha (`mdf`)

<!-- agent-hint
covers: what the `mdf` spec holds: its place in the family tree, its sources and scores, its sounds, its spelling rules and transcribed examples
source: `orthography2ipa/data/mdf.json`, `benchmarks/results.json`, `scripts/atlas_snapshot.json`
generated: partly. `scripts/gen_language_atlas.py` writes this hint and the blocks between the `atlas:` markers. Edit the generator for those, and the page for the prose between them
verify: `PYTHONPATH=$PWD python scripts/gen_language_atlas.py --check`
see: `docs/languages/a-z.md`, `docs/specs/quality_tiers.md`, `orthography2ipa/data/SCHEMA.md`
-->

<!-- atlas:summary begin -->
Moksha is an Uralic language, written in the Cyrillic script. Glottolog places it in Russia. The `mdf` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mdf` |
| ISO 639-3 | [mdf](https://iso639-3.sil.org/code/mdf), Moksha |
| Glottolog | [moks1248](https://glottolog.org/resource/languoid/id/moks1248), Moksha |
| Wikidata | [Q13343](https://www.wikidata.org/wiki/Q13343) |
| Wikipedia | [Moksha language](https://en.wikipedia.org/wiki/Moksha_language) |
| Family | [Uralic](by-family.md#uralic) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Proto-Uralic (family node)](https://tigregotico.github.io/orthography2ipa/#urj) `urj` |
| Explorer | [`mdf` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mdf) |
| Spec file | [`mdf.json`](../../orthography2ipa/data/mdf.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Moksha (мокшень кяль), Mordvinic (Uralic), Russia. Written in a Cyrillic alphabet identical in inventory to Russian. Palatalisation is phonemic and is written the Russian way, with the soft sign <ь> or an iotated vowel letter <е ё ю я> after the consonant.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1999 to 2024. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 39 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mdf.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mdf` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-bartens1999"></a>Bartens, Raija (1999). *Mordvalaiskielten rakenne ja kehitys*. Suomalais-Ugrilainen Seura, Helsinki.
2. <a id="src-moksha_wiki"></a>Wikipedia contributors (2024). *Moksha language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Moksha_language)
3. <a id="src-mordvinic_alphabets_wiki"></a>Wikipedia contributors (2024). *Mordvinic alphabets*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Mordvinic_alphabets)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `mdf` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 330 | 0.2112 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 59 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bʲ p pʲ |  | d dʲ t tʲ |  |  | k kʲ ɡ ɡʲ |
| Affricate |  |  | ts |  | tɕ |  |
| Nasal | m mʲ |  | n nʲ |  |  |  |
| Trill |  |  | r rʲ r̥ r̥ʲ |  |  |  |
| Fricative |  | f fʲ v vʲ | s sʲ z zʲ | ʃ ʃʲ ʒ ʒʲ | ɕ ɕʲ | x xʲ |
| Approximant |  |  |  |  | j j̥ ʲj |  |
| Lateral approximant |  |  | l lʲ l̥ l̥ʲ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u ʲu |
| Close-mid | e ʲe |  | o ʲo |
| Mid |  | ə |  |
| Open-mid | ɛ |  |  |
| Near-open | æ |  |  |
| Open | a ʲa |  | ɑ |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [je] | after consonant [ʲe] · default [je] |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨йх⟩ | [j̥] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨лх⟩ | [l̥] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨рх⟩ | [r̥] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tɕ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨ье⟩ | [ʲje] |  |
| ⟨ью⟩ | [ʲju] |  |
| ⟨ья⟩ | [ʲja] |  |
| ⟨ьё⟩ | [ʲjo] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] | after consonant [ʲu] · default [ju] |
| ⟨я⟩ | [ja] | after consonant [ʲa] · default [ja] |
| ⟨ё⟩ | [jo] | after consonant [ʲo] · default [jo] |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mdf")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Mohawk](moh.md) · [Home](../index.md) · [Mongolian →](mn.md)
