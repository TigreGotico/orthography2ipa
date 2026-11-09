# Icelandic (`is`)

<!-- atlas:summary begin -->
Icelandic is a North Germanic language, written in the Latin script. Glottolog places it in Iceland. The `is` spec is at the research tier. It cites 3 sources and has 3 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `is` |
| ISO 639-3 | [isl](https://iso639-3.sil.org/code/isl), Icelandic |
| Glottolog | [icel1247](https://glottolog.org/resource/languoid/id/icel1247), Icelandic |
| Wikidata | [Q294](https://www.wikidata.org/wiki/Q294) |
| Wikipedia | [Icelandic language](https://en.wikipedia.org/wiki/Icelandic_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > North Germanic](by-family.md#indo-european--germanic--northwest-germanic--north-germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [Iceland](by-region.md#iceland) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1200, living |
| Ancestor | [Old Norse](https://tigregotico.github.io/orthography2ipa/#non) `non` |
| Explorer | [`is` in the data explorer](https://tigregotico.github.io/orthography2ipa/#is) |
| Spec file | [`is.json`](../../orthography2ipa/data/is.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Icelandic (íslenska). Most conservative modern North Germanic language. PRESERVED: 4-case system, 3 grammatical genders, subjunctive, thorn þ [θ] and eth ð [ð], full umlaut (y, ø, œ). UNIQUE: Voiceless sonorants, hl [l̥], hn [n̥], hr [r̥].

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1945 to 2019. [Sources](#sources) lists them. The spec file writes all 53 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/is.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `is` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-einarsson1945"></a>Einarsson, S. (1945). *Icelandic: Grammar, Texts, Glossary*. Johns Hopkins Press.
2. <a id="src-arnason2011"></a>Árnason, K. (2011). *The Phonology of Icelandic and Faroese*. Oxford University Press.
3. <a id="src-flego2019"></a>Flego, S. & Berkson, K. H. (2019). *A Phonetic Illustration of the Sound System of Icelandic*. Indiana University Linguistics Club Working Papers. [scholarworks.iu.edu](https://scholarworks.iu.edu/journals/index.php/iulcwp/article/view/30216)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `is` | gold | lexicon-derived | MIT, each file its own | 60642 | 0.2354 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `is` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 10093 | 0.2045 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `is` | generated | espeak-derived | CC BY 4.0 | 4106 | 0.3397 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 72 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ pː ʰp |  |  | t tʰ tː ʰt | c cʰ | k kʰ kː ɡ ʰk |  |
| Nasal | m mː |  |  | n nː n̥ |  | ŋ |  |
| Trill |  |  |  | r rː r̥ |  |  |  |
| Fricative |  | f fː v | ð θ | s sː |  | x ɣ | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l l̥ |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Near-close | ɪ ɪː ʏ ʏː |  |
| Open-mid | œ œː ɛ ɛː | ɔ ɔː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [ai] [aiː] [au] [auː] [eɪ] [eɪː] [jɛ] [jɛː] [kv] [ou] [ouː] [tl] [tn] [xv] [øɪ] [øɪː] [ŋk] [ŋkʰ] [ŋɡ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] | default [a] · nucleus stressed [aː] |
| ⟨au⟩ | [øɪ] | default [øɪ] · nucleus stressed [øɪː] |
| ⟨b⟩ | [p] |  |
| ⟨bb⟩ | [pː] |  |
| ⟨d⟩ | [t] |  |
| ⟨dd⟩ | [tː] |  |
| ⟨e⟩ | [ɛ] | default [ɛ] · nucleus stressed [ɛː] |
| ⟨ei⟩ | [eɪ] | default [eɪ] · nucleus stressed [eɪː] |
| ⟨ey⟩ | [eɪ] | default [eɪ] · nucleus stressed [eɪː] |
| ⟨f⟩ | [f] [v] |  |
| ⟨ff⟩ | [fː] |  |
| ⟨g⟩ | [ɡ] [ɣ] [j] |  |
| ⟨gg⟩ | [kː] |  |
| ⟨h⟩ | [h] |  |
| ⟨hl⟩ | [l̥] |  |
| ⟨hn⟩ | [n̥] |  |
| ⟨hr⟩ | [r̥] |  |
| ⟨hv⟩ | [kv] [xv] |  |
| ⟨i⟩ | [ɪ] | default [ɪ] · nucleus stressed [ɪː] |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [kʰ] [c] [cʰ] |  |
| ⟨kk⟩ | [ʰk] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [tl] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [mː] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋɡ] [ŋk] |  |
| ⟨nk⟩ | [ŋkʰ] |  |
| ⟨nn⟩ | [nː] [tn] |  |
| ⟨o⟩ | [ɔ] | default [ɔ] · nucleus stressed [ɔː] |
| ⟨p⟩ | [pʰ] |  |
| ⟨pp⟩ | [ʰp] |  |
| ⟨r⟩ | [r] |  |
| ⟨rr⟩ | [rː] |  |
| ⟨s⟩ | [s] |  |
| ⟨ss⟩ | [sː] |  |
| ⟨t⟩ | [tʰ] |  |
| ⟨tt⟩ | [ʰt] |  |
| ⟨u⟩ | [ʏ] | default [ʏ] · nucleus stressed [ʏː] |
| ⟨v⟩ | [v] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [ɪ] | default [ɪ] · nucleus stressed [ɪː] |
| ⟨á⟩ | [au] | default [au] · nucleus stressed [auː] |
| ⟨æ⟩ | [ai] | default [ai] · nucleus stressed [aiː] |
| ⟨é⟩ | [jɛ] | default [jɛ] · nucleus stressed [jɛː] |
| ⟨í⟩ | [i] | default [i] · nucleus stressed [iː] |
| ⟨ð⟩ | [ð] |  |
| ⟨ó⟩ | [ou] | default [ou] · nucleus stressed [ouː] |
| ⟨ö⟩ | [œ] | default [œ] · nucleus stressed [œː] |
| ⟨ú⟩ | [u] | default [u] · nucleus stressed [uː] |
| ⟨ý⟩ | [i] | default [i] · nucleus stressed [iː] |
| ⟨þ⟩ | [θ] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 14 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `IS_SHORTEN_a` | /aː/ → [a], before a consonant cluster | - | - |
| `IS_SHORTEN_au` | /auː/ → [au], before a consonant cluster | - | - |
| `IS_SHORTEN_ɛ` | /ɛː/ → [ɛ], before a consonant cluster | - | - |
| `IS_SHORTEN_ɪ` | /ɪː/ → [ɪ], before a consonant cluster | - | - |
| `IS_SHORTEN_i` | /iː/ → [i], before a consonant cluster | - | - |
| `IS_SHORTEN_ɔ` | /ɔː/ → [ɔ], before a consonant cluster | - | - |
| `IS_SHORTEN_ou` | /ouː/ → [ou], before a consonant cluster | - | - |
| `IS_SHORTEN_ʏ` | /ʏː/ → [ʏ], before a consonant cluster | - | - |
| `IS_SHORTEN_u` | /uː/ → [u], before a consonant cluster | - | - |
| `IS_SHORTEN_œ` | /œː/ → [œ], before a consonant cluster | - | - |
| `IS_SHORTEN_eɪ` | /eɪː/ → [eɪ], before a consonant cluster | - | - |
| `IS_SHORTEN_øɪ` | /øɪː/ → [øɪ], before a consonant cluster | - | - |
| `IS_SHORTEN_ai` | /aiː/ → [ai], before a consonant cluster | - | - |
| `IS_SHORTEN_jɛ` | /jɛː/ → [jɛ], before a consonant cluster | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "is")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Iban](iba.md) · [Home](../index.md) · [Ido →](io.md)
