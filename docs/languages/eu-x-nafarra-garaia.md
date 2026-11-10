# Upper Navarrese Basque (`eu-x-nafarra-garaia`)

<!-- atlas:summary begin -->
Upper Navarrese Basque is a Vasconic variety, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `eu-x-nafarra-garaia` spec is at the research tier. It cites 6 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `eu-x-nafarra-garaia` |
| ISO 639-3 | [eus](https://iso639-3.sil.org/code/eus), Basque |
| Wikidata | [Q3125314](https://www.wikidata.org/wiki/Q3125314) |
| Wikipedia | [Upper Navarrese dialect](https://en.wikipedia.org/wiki/Upper_Navarrese_dialect) |
| Family | [Vasconic](by-family.md#vasconic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1600, living |
| Parent | [Basque (Euskara)](https://tigregotico.github.io/orthography2ipa/#eu) `eu` |
| Explorer | [`eu-x-nafarra-garaia` in the data explorer](https://tigregotico.github.io/orthography2ipa/#eu-x-nafarra-garaia) |
| Spec file | [`eu-x-nafarra-garaia.json`](../../orthography2ipa/data/eu-x-nafarra-garaia.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Upper (High) Navarrese (Goi-Nafar). Navarrese Basque of the Pamplona basin and northern Navarre. VALIDATED and CORRECTED against Hualde, Lujanbio & Zubiri (2010), an Illustration of the IPA of Goizueta Basque, a conservative High Navarrese variety.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 6 works, from 1988 to 2022. [Sources](#sources) lists them. The spec file writes 1 of the 35 spellings of its letter table and takes the other 34 from [Basque (Euskara)](https://tigregotico.github.io/orthography2ipa/#eu) `eu`.

The [spec file](../../orthography2ipa/data/eu-x-nafarra-garaia.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `eu-x-nafarra-garaia` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 3 of them have a DOI or a URL. The spec file holds a note on what 3 of them support.

1. <a id="src-hualde_lujanbio_zubiri2010"></a>Hualde, J.I., Lujanbio, O. & Zubiri, J.J. (2010). *Goizueta Basque (Illustrations of the IPA)*. Journal of the International Phonetic Association 40(1). Cited: 113-127. [doi.org](https://doi.org/10.1017/S0025100309990260)
2. <a id="src-hualde2018_aspiration"></a>Hualde, J.I. (2018). *Aspiration in Basque*. Papers in Historical Phonology 3. Cited: 1-27. [doi.org](https://doi.org/10.2218/pihph.3.2018.2602)
3. <a id="src-hualde_ortiz_de_urbina2003"></a>Hualde, J.I. & Ortiz de Urbina, J. (eds.) (2003). *A Grammar of Basque*. Mouton de Gruyter. Cited: 15-65 (Hualde, 'Segmental phonology').
4. <a id="src-saltarelli1988"></a>Saltarelli, M. (1988). *Basque*. Croom Helm.
5. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
6. <a id="src-hualde2022_ocb"></a>Hualde, J.I. (2022). *The reconstruction of Old Common Basque accentuation: Closing open issues*. Anuario del Seminario de Filología Vasca Julio de Urquijo (ASJU) 56(2). Cited: 77-106. [doi.org](https://doi.org/10.1387/asju.23983)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `spain_romance_tts` | `eu-x-nafarra-garaia` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.1107 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 42 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  | c ɟ | k ɡ |  |
| Affricate |  |  |  | ts̺ ts̻ | tʃ |  |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |
| Trill |  |  |  | r |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative | β | f | ð | s̺ s̻ | ʃ | ʝ | x ɣ | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  | ʎ |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [ai̯] [au̯] [ei̯] [eu̯] [oi̯] [ui̯] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [ai̯] |  |
| ⟨au⟩ | [au̯] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨dd⟩ | [ɟ] |  |
| ⟨e⟩ | [e] |  |
| ⟨ei⟩ | [ei̯] |  |
| ⟨eu⟩ | [eu̯] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] [x] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨oi⟩ | [oi̯] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] | before consonant [r] · intervocalic [ɾ] · word final [r] · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s̺] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [ts̺] |  |
| ⟨tt⟩ | [c] |  |
| ⟨tx⟩ | [tʃ] |  |
| ⟨tz⟩ | [ts̻] |  |
| ⟨u⟩ | [u] |  |
| ⟨ui⟩ | [ui̯] |  |
| ⟨x⟩ | [ʃ] |  |
| ⟨z⟩ | [s̻] |  |
| ⟨ñ⟩ | [ɲ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 10 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `NASAL_LABIAL_ASSIM` | /n/ → [m], before [b] [p] [m] | ⟨anbulantzia⟩ [ambulants̩ia] | [Hualde 2010](#src-hualde_lujanbio_zubiri2010), Lujanbio & Zubiri 2010 |
| `EU_SPIRANT_B` | /b/ → [β], after a vowel | ⟨abere⟩ [aβeɾe] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |
| `EU_SPIRANT_D` | /d/ → [ð], after a vowel | ⟨adar⟩ [aðar] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |
| `EU_SPIRANT_Ɡ` | /ɡ/ → [ɣ], after a vowel | ⟨egin⟩ [eɣin] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |
| `EU_OFFGLIDE_I` | /i/ → [j], after a vowel, before a consonant | ⟨ai⟩ [aj] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |
| `EU_OFFGLIDE_I_FINAL` | /i/ → [j], word-finally, after a vowel | ⟨ai⟩ [aj] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |
| `EU_OFFGLIDE_U` | /u/ → [w], after a vowel, before a consonant | ⟨au⟩ [aw] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |
| `EU_OFFGLIDE_U_FINAL` | /u/ → [w], word-finally, after a vowel | ⟨au⟩ [aw] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |
| `EU_TRILL_CODA` | /ɾ/ → [r], before a consonant | ⟨adar⟩ [aðar] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |
| `EU_TRILL_FINAL` | /ɾ/ → [r], word-finally | ⟨adar⟩ [aðar] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |

The spec applies 6 rules across a word boundary. The contexts are regular expressions on the IPA of the two words.

| Rule | End of word | Start of next word | Change | Example | Cited |
|:--|:--|:--|:--|:--|:--|
| `EU_EZ_D_DEVOICE` | `^[ˈˌ]?es̻$` | `^([ˈˌ]?)d` | right [t] | ⟨eztut⟩ [es̻ tut] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003, Hualde 1991 |
| `EU_EZ_Z_AFFRICATE` | `^([ˈˌ]?)es̻$` | `^([ˈˌ]?)s̻` | left [e], right [ts̻] | - | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003, Hualde 1991 |
| `EU_EZ_N_ASSIM` | `^([ˈˌ]?)es̻$` | `^[ˈˌ]?n` | left [e] | ⟨enaiz⟩ [e nais̻] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003, Hualde 1991 |
| `EU_EZ_L_ASSIM` | `^([ˈˌ]?)es̻$` | `^[ˈˌ]?l` | left [e] | ⟨eluke⟩ [e luke] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003, Hualde 1991 |
| `EU_EZ_B_DEVOICE` | `^[ˈˌ]?es̻$` | `^([ˈˌ]?)b` | right [p] | ⟨ezpalitz⟩ [es̻ palits̻] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003, Hualde 1991 |
| `EU_EZ_G_DEVOICE` | `^[ˈˌ]?es̻$` | `^([ˈˌ]?)ɡ` | right [k] | ⟨ezkara⟩ [es̻ kaɾa] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003, Hualde 1991 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "eu-x-nafarra-garaia")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

| Repository | What it does with this spec |
|:--|:--|
| [euskaphone](https://github.com/TigreGotico/euskaphone) | A dialect-aware Basque phonemizer over the orthography2ipa lattice. |
<!-- atlas:related end -->

---
[← Uneapa](bbn.md) · [Home](../index.md) · [Upper Sorbian →](hsb.md)
