# Swedish (`sv`)

<!-- atlas:summary begin -->
Swedish is a North Germanic language, written in the Latin script. Glottolog places it in 5 countries. The `sv` spec is at the research tier. It cites 4 sources and has 4 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sv` |
| Aliases | `swe` |
| ISO 639-3 | [swe](https://iso639-3.sil.org/code/swe), Swedish |
| Glottolog | [swed1254](https://glottolog.org/resource/languoid/id/swed1254), Swedish |
| Wikidata | [Q9027](https://www.wikidata.org/wiki/Q9027) |
| Wikipedia | [Swedish language](https://en.wikipedia.org/wiki/Swedish_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > North Germanic](by-family.md#indo-european--germanic--northwest-germanic--north-germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [Denmark](by-region.md#denmark), [Finland](by-region.md#finland), [Norway](by-region.md#norway), [Sweden](by-region.md#sweden), [Åland Islands](by-region.md#åland-islands) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Parent | [North Germanic](https://tigregotico.github.io/orthography2ipa/#x-clade-nort3160) `x-clade-nort3160` |
| Child lects | 3, see [Related lects](#related-lects) |
| Explorer | [`sv` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sv) |
| Spec file | [`sv.json`](../../orthography2ipa/data/sv.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Central Standard Swedish. COMPLEMENTARY QUANTITY: in a stressed syllable a long vowel is followed by a short consonant and a short vowel by a long consonant or a cluster (Riad 2014, Wikipedia: 'a phonologically short consonant follows a long vowel and a long consonant follows a short vowel').

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1970 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 61 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sv.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `sv` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Swedish (Finland-Swedish)](https://tigregotico.github.io/orthography2ipa/#sv-FI) `sv-FI`: Finland, skeleton tier
- [Swedish (Rikssvenska)](https://tigregotico.github.io/orthography2ipa/#sv-x-rikssven) `sv-x-rikssven`: skeleton tier
- [Swedish (Scanian / Skånska)](https://tigregotico.github.io/orthography2ipa/#sv-x-skanska) `sv-x-skanska`: skeleton tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-riad2014"></a>Riad, T. (2014). *The Phonology of Swedish*. Oxford University Press.
2. <a id="src-engstrand1999"></a>Engstrand, O. (1999). *Swedish*. Cambridge University Press.
3. <a id="src-wikipedia_swedish_phonology"></a>Wikipedia contributors (2026). *Swedish phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Swedish_phonology)
4. <a id="src-elert1970"></a>Elert, C.-C. (1970). *Ljud och ord i svenskan*. Almqvist & Wiksell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `sv` | gold | lexicon-derived | MIT, each file its own | 21094 | 0.2377 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `sv` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 5076 | 0.2336 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `sv` | generated | espeak-derived | CC BY 4.0 | 5202 | 0.3412 | no |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `sv` | generated | epitran-derived | CC0 1.0 | 19492 | 0.3658 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 69 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bː p pʰ pː |  | d dː t tʰ tː |  | ɖ ʈ |  | k kʰ kː ɡ ɡː |  |  |
| Nasal | m mː |  | n nː |  | ɳ |  | ŋ |  |  |
| Trill |  |  | r rː |  |  |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |  |
| Fricative |  | f fː v vː | s sː | ʃ | ʂ | ɕ | x | ʁ | h |
| Approximant |  |  |  |  |  | j jː |  |  |  |
| Lateral approximant |  |  | l lː |  | ɭ |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː yː | ʉː | uː |
| Near-close | ɪ ʏ |  | ʊ |
| Close-mid | eː øː | ɵ | oː |
| Open-mid | œ œː ɛ ɛː |  | ɔ |
| Near-open | æ æː |  |  |
| Open | a |  | ɑː |

Sequences that the spec writes as one unit: [ks] [sk] [ŋk] [ŋn] [ɡn] [ɧ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] [ɑː] | default [a] · nucleus stressed [ɑː] |
| ⟨b⟩ | [b] |  |
| ⟨bb⟩ | [bː] |  |
| ⟨c⟩ | [k] [s] | before front vowel [s] · default [k] |
| ⟨ch⟩ | [ɕ] [ʃ] |  |
| ⟨ck⟩ | [kː] |  |
| ⟨d⟩ | [d] |  |
| ⟨dd⟩ | [dː] |  |
| ⟨dj⟩ | [j] |  |
| ⟨e⟩ | [ɛ] [eː] | default [ɛ] · nucleus stressed [eː] |
| ⟨f⟩ | [f] |  |
| ⟨ff⟩ | [fː] |  |
| ⟨g⟩ | [ɡ] [j] | before front vowel [j] · default [ɡ] |
| ⟨gg⟩ | [ɡː] |  |
| ⟨gj⟩ | [j] |  |
| ⟨gn⟩ | [ŋn] [ɡn] | default [ŋn] · word initial [ɡn] |
| ⟨h⟩ | [h] |  |
| ⟨hj⟩ | [j] |  |
| ⟨i⟩ | [ɪ] [iː] | default [ɪ] · nucleus stressed [iː] |
| ⟨j⟩ | [j] |  |
| ⟨jj⟩ | [jː] |  |
| ⟨k⟩ | [k] [ɕ] | before front vowel [ɕ] · default [k] |
| ⟨kj⟩ | [ɕ] |  |
| ⟨kk⟩ | [kː] |  |
| ⟨l⟩ | [l] |  |
| ⟨lj⟩ | [j] |  |
| ⟨ll⟩ | [lː] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [mː] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨nn⟩ | [nː] |  |
| ⟨o⟩ | [ɔ] [uː] | default [ɔ] · nucleus stressed [uː] |
| ⟨p⟩ | [p] |  |
| ⟨pp⟩ | [pː] |  |
| ⟨q⟩ | [k] |  |
| ⟨r⟩ | [r] [ɾ] |  |
| ⟨rr⟩ | [rː] |  |
| ⟨s⟩ | [s] |  |
| ⟨sc⟩ | [s] [sk] | before front vowel [s] · default [sk] |
| ⟨sch⟩ | [ʃ] |  |
| ⟨sj⟩ | [ɧ] |  |
| ⟨sk⟩ | [ɧ] [sk] | before front vowel [ɧ] · default [sk] |
| ⟨skj⟩ | [ɧ] |  |
| ⟨ss⟩ | [sː] |  |
| ⟨stj⟩ | [ɧ] |  |
| ⟨t⟩ | [t] |  |
| ⟨tj⟩ | [ɕ] |  |
| ⟨tt⟩ | [tː] |  |
| ⟨u⟩ | [ɵ] [ʉː] | default [ɵ] · nucleus stressed [ʉː] |
| ⟨v⟩ | [v] |  |
| ⟨vv⟩ | [vː] |  |
| ⟨w⟩ | [v] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [ʏ] [yː] | default [ʏ] · nucleus stressed [yː] |
| ⟨z⟩ | [s] |  |
| ⟨zz⟩ | [sː] |  |
| ⟨ä⟩ | [ɛ] [ɛː] | default [ɛ] · nucleus stressed [ɛː] |
| ⟨å⟩ | [ɔ] [oː] | default [ɔ] · nucleus stressed [oː] |
| ⟨ö⟩ | [œ] [øː] | default [œ] · nucleus stressed [øː] |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 48 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `SV_PRE_R_LOW_LONG_CLUSTER` | /ɛː/ → [æ], stressed, before a consonant cluster, before [r] [rː] | ⟨lära⟩ [læːra] | [Riad 2014](#src-riad2014) |
| `SV_PRE_R_LOW_LONG_SINGLE` | /ɛː/ → [æː], stressed, before [r] [rː] | ⟨lära⟩ [læːra] | [Riad 2014](#src-riad2014) |
| `SV_PRE_R_LOW_E_CLUSTER` | /eː/ → [æ], stressed, before a consonant cluster, before [r] [rː] | ⟨lära⟩ [læːra] | [Riad 2014](#src-riad2014) |
| `SV_PRE_R_LOW_SHORT` | /ɛ/ → [æ], stressed, before [r] [rː] [ʈ] [ɖ] [ɳ] [ɭ] [ʂ] | ⟨lära⟩ [læːra] | [Riad 2014](#src-riad2014) |
| `SV_SHORTEN_A` | /ɑː/ → [a], before a consonant cluster | - | - |
| `SV_SHORTEN_E` | /eː/ → [ɛ], before a consonant cluster | - | - |
| `SV_SHORTEN_I` | /iː/ → [ɪ], before a consonant cluster | - | - |
| `SV_SHORTEN_O` | /uː/ → [ɔ], before a consonant cluster | - | - |
| `SV_SHORTEN_U` | /ʉː/ → [ɵ], before a consonant cluster | - | - |
| `SV_SHORTEN_Y` | /yː/ → [ʏ], before a consonant cluster | - | - |
| `SV_SHORTEN_Å` | /oː/ → [ɔ], before a consonant cluster | - | - |
| `SV_SHORTEN_Ä` | /ɛː/ → [ɛ], before a consonant cluster | - | - |
| `SV_SHORTEN_Ö` | /øː/ → [œ], before a consonant cluster | - | - |
| `SV_AE_LOWER_LONG` | /ɛː/ → [æː], before [r] [rː] [ʈ] [ʂ] [ɖ] [ɳ] [ɭ] [rb] and 11 more, spelled ⟨ä⟩ | - | - |
| `SV_AE_LOWER_SHORT` | /ɛ/ → [æ], before [r] [rː] [ʈ] [ʂ] [ɖ] [ɳ] [ɭ] [rb] and 11 more, spelled ⟨ä⟩ | - | - |
| `SV_OE_LOWER_LONG` | /øː/ → [œː], before [r] [rː] [ʈ] [ʂ] [ɖ] [ɳ] [ɭ] [rb] and 11 more, spelled ⟨ö⟩ | - | - |
| `SV_OE_LOWER_SHORT` | /œ/ → [œ], before [r] [rː] [ʈ] [ʂ] [ɖ] [ɳ] [ɭ] [rb] and 11 more, spelled ⟨ö⟩ | - | - |
| `SV_SHORTEN_MG_ɑː` | /ɑː/ → [a], before ⟨ng⟩ ⟨nk⟩ ⟨sk⟩ | ⟨sjunga⟩ [ɧɵŋa] | [Riad 2014](#src-riad2014) |
| `SV_SHORTEN_MG_eː` | /eː/ → [ɛ], before ⟨ng⟩ ⟨nk⟩ ⟨sk⟩ | ⟨säng⟩ [sɛŋ] | [Riad 2014](#src-riad2014) |
| `SV_SHORTEN_MG_iː` | /iː/ → [ɪ], before ⟨ng⟩ ⟨nk⟩ ⟨sk⟩ | ⟨fisk⟩ [fɪsk] | [Riad 2014](#src-riad2014) |
| `SV_SHORTEN_MG_uː` | /uː/ → [ɔ], before ⟨ng⟩ ⟨nk⟩ ⟨sk⟩ | ⟨lång⟩ [lɔŋ] | [Riad 2014](#src-riad2014) |
| `SV_SHORTEN_MG_ʉː` | /ʉː/ → [ɵ], before ⟨ng⟩ ⟨nk⟩ ⟨sk⟩ | ⟨sjunga⟩ [ɧɵŋa] | [Riad 2014](#src-riad2014) |
| `SV_SHORTEN_MG_yː` | /yː/ → [ʏ], before ⟨ng⟩ ⟨nk⟩ ⟨sk⟩ | - | [Riad 2014](#src-riad2014) |
| `SV_SHORTEN_MG_oː` | /oː/ → [ɔ], before ⟨ng⟩ ⟨nk⟩ ⟨sk⟩ | ⟨lång⟩ [lɔŋ] | [Riad 2014](#src-riad2014) |
| `SV_SHORTEN_MG_ɛː` | /ɛː/ → [ɛ], before ⟨ng⟩ ⟨nk⟩ ⟨sk⟩ | ⟨säng⟩ [sɛŋ] | [Riad 2014](#src-riad2014) |
| `SV_SHORTEN_MG_øː` | /øː/ → [œ], before ⟨ng⟩ ⟨nk⟩ ⟨sk⟩ | - | [Riad 2014](#src-riad2014) |
| `SV_SHORT_BEFORE_J_ɑː` | /ɑː/ → [a], before ⟨j⟩ | - | [Riad 2014](#src-riad2014) |
| `SV_SHORT_BEFORE_J_eː` | /eː/ → [ɛ], before ⟨j⟩ | - | [Riad 2014](#src-riad2014) |
| `SV_SHORT_BEFORE_J_iː` | /iː/ → [ɪ], before ⟨j⟩ | - | [Riad 2014](#src-riad2014) |
| `SV_SHORT_BEFORE_J_uː` | /uː/ → [ɔ], before ⟨j⟩ | - | [Riad 2014](#src-riad2014) |
| `SV_SHORT_BEFORE_J_ʉː` | /ʉː/ → [ɵ], before ⟨j⟩ | - | [Riad 2014](#src-riad2014) |
| `SV_SHORT_BEFORE_J_yː` | /yː/ → [ʏ], before ⟨j⟩ | - | [Riad 2014](#src-riad2014) |
| `SV_SHORT_BEFORE_J_oː` | /oː/ → [ɔ], before ⟨j⟩ | - | [Riad 2014](#src-riad2014) |
| `SV_SHORT_BEFORE_J_ɛː` | /ɛː/ → [ɛ], before ⟨j⟩ | - | [Riad 2014](#src-riad2014) |
| `SV_SHORT_BEFORE_J_øː` | /øː/ → [œ], before ⟨j⟩ | - | [Riad 2014](#src-riad2014) |
| `SV_UNSTRESSED_O_FINAL` | /ɔ/ → [ʊ], word-finally, unstressed, spelled ⟨o⟩ | - | [Riad 2014](#src-riad2014) |
| `SV_UNSTRESSED_O_OPEN` | /ɔ/ → [ʊ], unstressed, before a consonant, spelled ⟨o⟩, with more context in the spec | - | [Riad 2014](#src-riad2014) |
| `SV_RETROFLEX_T` | /t/ → [ʈ], after [r] [ɾ] | ⟨kort⟩ [kɔʈː] | [Riad 2014](#src-riad2014), [Engstrand 1999](#src-engstrand1999) |
| `SV_RETROFLEX_D` | /d/ → [ɖ], after [r] [ɾ] | ⟨bord⟩ [buːɖ] | [Riad 2014](#src-riad2014), [Engstrand 1999](#src-engstrand1999) |
| `SV_RETROFLEX_N` | /n/ → [ɳ], after [r] [ɾ] | ⟨barn⟩ [bɑːɳ] | [Riad 2014](#src-riad2014), [Engstrand 1999](#src-engstrand1999) |
| `SV_RETROFLEX_S` | /s/ → [ʂ], after [r] [ɾ] | ⟨fars⟩ [faʂː] | [Riad 2014](#src-riad2014), [Engstrand 1999](#src-engstrand1999) |
| `SV_RETROFLEX_L` | /l/ → [ɭ], after [r] [ɾ] | ⟨pärla⟩ [pɛːɭa] | [Riad 2014](#src-riad2014), [Engstrand 1999](#src-engstrand1999) |
| `SV_RETROFLEX_R_ABSORB` | /r ɾ/ → ∅, before [t] [d] [n] [s] [l] | ⟨kort⟩ [kɔʈː] | [Riad 2014](#src-riad2014), [Engstrand 1999](#src-engstrand1999) |
| `SV_RETROFLEX_CASCADE_T` | /t/ → [ʈ], after [s] [t] [d] [n] [l], with more context in the spec | ⟨första⟩ [fœʂʈa] | [Riad 2014](#src-riad2014), [Elert 1970](#src-elert1970) |
| `SV_RETROFLEX_CASCADE_D` | /d/ → [ɖ], after [s] [t] [d] [n] [l], with more context in the spec | - | [Riad 2014](#src-riad2014), [Elert 1970](#src-elert1970) |
| `SV_RETROFLEX_CASCADE_N` | /n/ → [ɳ], after [s] [t] [d] [n] [l], with more context in the spec | ⟨barnsben⟩ [bɑːɳʂbeːn] | [Riad 2014](#src-riad2014), [Elert 1970](#src-elert1970) |
| `SV_RETROFLEX_CASCADE_L` | /l/ → [ɭ], after [s] [t] [d] [n] [l], with more context in the spec | - | [Riad 2014](#src-riad2014), [Elert 1970](#src-elert1970) |
| `SV_RETROFLEX_CASCADE_S` | /s/ → [ʂ], after [s] [t] [d] [n] [l], with more context in the spec | ⟨första⟩ [fœʂʈa] | [Riad 2014](#src-riad2014), [Elert 1970](#src-elert1970) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sv")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Swahili](sw.md) · [Home](../index.md) · [Swiss Standard German →](de-CH.md)
