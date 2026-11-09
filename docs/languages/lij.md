# Ligurian (`lij`)

<!-- atlas:summary begin -->
Ligurian is an Italo-Romance language, written in the Latin script. Glottolog places it in France, Italy and Monaco. The `lij` spec is at the research tier. It cites 6 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lij` |
| ISO 639-3 | [lij](https://iso639-3.sil.org/code/lij), Ligurian |
| Glottolog | [ligu1248](https://glottolog.org/resource/languoid/id/ligu1248), Ligurian |
| Wikidata | [Q36106](https://www.wikidata.org/wiki/Q36106) |
| Wikipedia | [Ligurian language (Romance)](https://en.wikipedia.org/wiki/Ligurian_language_(Romance)) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Italo-Romance](by-family.md#indo-european--italic--romance--italo-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [France](by-region.md#france), [Italy](by-region.md#italy), [Monaco](by-region.md#monaco) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Ancestor | [Gallo-Italic Vulgar Latin](https://tigregotico.github.io/orthography2ipa/#la-x-gallo-italic) `la-x-gallo-italic` |
| Explorer | [`lij` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lij) |
| Spec file | [`lij.json`](../../orthography2ipa/data/lij.json) |
<!-- atlas:header end -->

## Overview

Ligurian is a Gallo-Italic language of Liguria and was the historical lingua franca of Mediterranean maritime trade. The `lij` spec models Genoese. It inherits its grapheme and allophone base from the Gallo-Italic Vulgar Latin spec `la-x-gallo-italic` and overrides it with the Genoese values.

The reference variety is Genoese (*Zeneise*). The page places Ligurian in the Gallo-Italic group.

## Input contract

The spec follows the standard *grafia ofiçiâ* of the [Académia Ligùstica do Brénno](https://en.wikipedia.org/wiki/Academia_Ligustica_do_Brenno), the official Genoese orthography. The Ligurian Wikipedia and the dictionaries of Toso both use it. Give the spec text in that orthography, with accents and length marks. Ad-hoc or Italianising spellings are out of scope.

## The main grapheme correspondences

These correspondences are the features that a Genoese spec must get right. Several of them are diagnostic of the language and set it apart from Italian.

| Grapheme | IPA | Note |
|:---:|:---:|:---|
| `x` | /ʒ/ | The diagnostic Genoese letter, the sound of French ⟨j⟩ |
| `o` | /u/ | Genoese ⟨o⟩ is Italian ⟨u⟩. `ó` is /u/ and `ô` is /uː/ |
| `ò` | /ɔ/ | Open back, in contrast with `o` /u/. `ö` is /ɔː/ |
| `u` | /y/ | Front rounded. `û` and `ü` are /yː/ |
| `eu` | /ø/ | Front rounded mid. `êu` and `ëu` are /øː/ |
| `æ` | /ɛː/ | Long open-mid front |
| `ç` | /s/ | The voiceless sibilant with a cedilla |
| `z` | /z/ | Always /z/ and never an affricate, unlike Italian |
| `sc` | /ʃ/ before a front vowel, else /sk/ | positional |
| `scc` | /ʃtʃ/ | trigraph |
| `n-`, `nn-`, `ñ` | /ŋ/ | the velar nasal between vowels |

The table shows the first candidate of each grapheme. Some real output:

```python
>>> import orthography2ipa as o
>>> [o.transcribe(w, "lij") for w in ["gexa", "çittæ", "scciappâ", "lann-a"]]
['ˈdʒeʒa', 'siˈtɛː', 'ʃtʃiaˈpaː', 'ˈlãŋa']
```

`gexa` is 'church', `çittæ` is 'city' and `lann-a` is 'wool'.

### Softening of c and g

| Grapheme | Before a front vowel | Elsewhere |
|:---:|:---:|:---:|
| `c` | [tʃ] | [k] (`ch` is always [k]) |
| `g` | [dʒ] | [ɡ] (`gh` is always [ɡ]) |

### Vowel length and stress

The grafia writes length and stress with accent marks:

| Mark | Letters | Meaning |
|:---|:---|:---|
| Grave | `à è ì ò ù` | the stressed vowel, with the quality /a ɛ i ɔ y/ |
| Acute | `é ó` | stressed close-mid /e/ and /u/ |
| Circumflex | `â ê î ô û` | a long stressed vowel at the end of a word |
| Diaeresis | `ä ë ï ö ü` | a long vowel inside a word |

The default stress is on the penultimate syllable. A written accent, or the ligature `æ`, marks the stressed syllable and always wins. So the spelling gives the stress, and the `stress` block lists every accented letter as a stress mark.

## Allophone rules

The spec models the velar nasal and vowel nasalisation as allophone rules:

| Rule | Effect | Source |
|:---|:---|:---|
| `LIJ_N_VELAR_FINAL` | /n/ becomes [ŋ] at the end of a word (`can` gives `ˈkaŋ`, 'dog') | Toso 1997 |
| `LIJ_N_VELAR_ASSIM` | /n/ becomes [ŋ] before /k ɡ/ | Toso 1997 |
| `LIJ_N_LABIAL_ASSIM` | /n/ becomes [m] before /p b m f/ | Toso 1997 |
| `LIJ_NASAL_*` | a vowel becomes nasal before [ŋ] (`lann-a` gives `ˈlãŋa`) | Forner 1975, Toso 1997 |

Modern Genoese has total degemination. The spec maps each written double consonant to one phoneme, so `xatta` 'cat' gives `ˈʒata`.

## Vowel inventory

The close vowels are /i y u/, the mid vowels are /e ø ɛ ɔ/ and the open vowel is /a/. Each has a long counterpart /iː yː uː eː øː ɛː ɔː aː/, and each has nasal allophones before the velar nasal. The front rounded pair /y ø/ and the length contrast are the main vowel features (Forner 1975).

## Known limitations

After palatal `c` or `g`, a written ⟨i⟩ before a back vowel only marks the palatal. The spec handles it with the digraphs `cia cio ciu gia gio giu` and their accented forms. So `ciù` gives `ˈtʃy` and `giornâ` gives `dʒurˈnaː`, with no [i]. Before a consonant the ⟨i⟩ is a real vowel and stays, so `cina` gives `ˈtʃina`.

The spec reads `gl` as [ɡl], because Genoese does not have the Italian ⟨gli⟩ [ʎ].

## Benchmark

The `wikipron` row is crowd-scraped and can gate a promotion. The `vox_communis` row is epitran-derived, so it measures agreement with epitran and cannot gate. See the [scoreboard](../evaluation/generated/scoreboard.md) for the scores.

<!-- atlas:lects begin -->
## Related lects

No spec names `lij` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-academia_grafia_oficia"></a>Académia Ligùstica do Brénno (2008). *Grafia ofiçiâ: grafia moderna do zeneize*. Académia Ligùstica do Brénno. [zeneize.net](http://www.zeneize.net/)
2. <a id="src-omniglot_genoese"></a>Omniglot (2024). *Genoese (Zeneize) language and pronunciation*. Omniglot. [omniglot.com](https://www.omniglot.com/writing/genoese.htm)
3. <a id="src-toso1997_grammatica"></a>Toso, Fiorenzo (1997). *Grammatica del genovese: varietà urbana e di koinè*. Le Mani.
4. <a id="src-forner1975"></a>Forner, Werner (1975). *Generative Phonologie des Dialekts von Genua*. Buske.
5. <a id="src-maiden_parry1997"></a>Maiden, M. & Parry, M. (eds.) (1997). *The Dialects of Italy*. Routledge.
6. <a id="src-loporcaro2009"></a>Loporcaro, M. (2009). *Profilo linguistico dei dialetti italiani*. Laterza.
<!-- atlas:sources end -->

### Notes on the sources

Omniglot is a tertiary cross-check only.

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `lij` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 817 | 0.1157 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `lij` | generated | epitran-derived | CC0 1.0 | 3416 | 0.0844 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 68 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |
| Affricate |  |  |  | dʒ tʃ |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː y yː ĩ ỹ | u uː ũ |
| Close-mid | e eː ø øː ø̃ ẽ | o |
| Open-mid | ɛ ɛː ɛ̃ | ɔ ɔː ɔ̃ |
| Open | a aː ã |  |

Sequences that the spec writes as one unit: [dʒa] [dʒaː] [dʒu] [dʒuː] [dʒy] [dʒyː] [dʒɔ] [dʒɔː] [ej] [kw] [sk] [tʃa] [tʃaː] [tʃu] [tʃuː] [tʃy] [tʃyː] [tʃɔ] [tʃɔː] [w] [ɔw] [ʃtʃ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨bb⟩ | [b] |  |
| ⟨c⟩ | [k] | before front vowel [tʃ] · default [k] |
| ⟨cc⟩ | [k] |  |
| ⟨ch⟩ | [k] |  |
| ⟨cia⟩ | [tʃa] |  |
| ⟨cio⟩ | [tʃu] |  |
| ⟨ciu⟩ | [tʃy] |  |
| ⟨cià⟩ | [tʃa] |  |
| ⟨ciâ⟩ | [tʃaː] |  |
| ⟨ciä⟩ | [tʃaː] |  |
| ⟨ciò⟩ | [tʃɔ] |  |
| ⟨ció⟩ | [tʃu] |  |
| ⟨ciô⟩ | [tʃuː] |  |
| ⟨ciö⟩ | [tʃɔː] |  |
| ⟨ciù⟩ | [tʃy] |  |
| ⟨ciû⟩ | [tʃyː] |  |
| ⟨ciü⟩ | [tʃyː] |  |
| ⟨d⟩ | [d] |  |
| ⟨dd⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨ei⟩ | [ej] |  |
| ⟨eu⟩ | [ø] |  |
| ⟨f⟩ | [f] |  |
| ⟨ff⟩ | [f] |  |
| ⟨g⟩ | [ɡ] | before front vowel [dʒ] · default [ɡ] |
| ⟨gg⟩ | [ɡ] |  |
| ⟨gh⟩ | [ɡ] |  |
| ⟨gia⟩ | [dʒa] |  |
| ⟨gio⟩ | [dʒu] |  |
| ⟨giu⟩ | [dʒy] |  |
| ⟨già⟩ | [dʒa] |  |
| ⟨giâ⟩ | [dʒaː] |  |
| ⟨giä⟩ | [dʒaː] |  |
| ⟨giò⟩ | [dʒɔ] |  |
| ⟨gió⟩ | [dʒu] |  |
| ⟨giô⟩ | [dʒuː] |  |
| ⟨giö⟩ | [dʒɔː] |  |
| ⟨giù⟩ | [dʒy] |  |
| ⟨giû⟩ | [dʒyː] |  |
| ⟨giü⟩ | [dʒyː] |  |
| ⟨gn⟩ | [ɲ] |  |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨n-⟩ | [ŋ] |  |
| ⟨nn⟩ | [n] |  |
| ⟨nn-⟩ | [ŋ] |  |
| ⟨o⟩ | [u] |  |
| ⟨ou⟩ | [ɔw] |  |
| ⟨p⟩ | [p] |  |
| ⟨pp⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [r] |  |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sc⟩ | [ʃ] | before front vowel [ʃ] · default [sk] |
| ⟨scc⟩ | [ʃtʃ] |  |
| ⟨ss⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tt⟩ | [t] |  |
| ⟨u⟩ | [y] |  |
| ⟨v⟩ | [v] |  |
| ⟨vv⟩ | [v] |  |
| ⟨x⟩ | [ʒ] |  |
| ⟨z⟩ | [z] |  |
| ⟨zz⟩ | [z] |  |
| ⟨à⟩ | [a] |  |
| ⟨â⟩ | [aː] |  |
| ⟨ä⟩ | [aː] |  |
| ⟨æ⟩ | [ɛː] |  |
| ⟨ç⟩ | [s] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [e] |  |
| ⟨ê⟩ | [eː] |  |
| ⟨êu⟩ | [øː] |  |
| ⟨ë⟩ | [eː] |  |
| ⟨ëu⟩ | [øː] |  |
| ⟨ì⟩ | [i] |  |
| ⟨î⟩ | [iː] |  |
| ⟨ï⟩ | [iː] |  |
| ⟨ñ⟩ | [ŋ] |  |
| ⟨ò⟩ | [ɔ] |  |
| ⟨òu⟩ | [ɔw] |  |
| ⟨ó⟩ | [u] |  |
| ⟨ô⟩ | [uː] |  |
| ⟨ö⟩ | [ɔː] |  |
| ⟨ù⟩ | [y] |  |
| ⟨û⟩ | [yː] |  |
| ⟨ü⟩ | [yː] |  |

Stress falls on the penult by default. A written ⟨à⟩ ⟨è⟩ ⟨é⟩ ⟨ì⟩ ⟨ò⟩ ⟨ó⟩ ⟨ù⟩ ⟨â⟩ ⟨ê⟩ ⟨î⟩ ⟨ô⟩ ⟨û⟩ ⟨ä⟩ ⟨ë⟩ ⟨ï⟩ ⟨ö⟩ ⟨ü⟩ ⟨æ⟩ marks the stressed vowel.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 9 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `LIJ_N_VELAR_FINAL` | /n/ → [ŋ], word-finally | ⟨'dog'⟩ [kaŋ] | [Toso 1997](#src-toso1997_grammatica) |
| `LIJ_N_VELAR_ASSIM` | /n/ → [ŋ], before [k] [ɡ] | - | [Toso 1997](#src-toso1997_grammatica) |
| `LIJ_N_LABIAL_ASSIM` | /n/ → [m], before [p] [b] [m] [f] | - | [Toso 1997](#src-toso1997_grammatica) |
| `LIJ_NASAL_A` | /a/ → [ã], before [ŋ] | ⟨'wool'⟩ [ˈlãŋa] | [Toso 1997](#src-toso1997_grammatica), [Forner 1975](#src-forner1975) |
| `LIJ_NASAL_E` | /e/ → [ẽ], before [ŋ] | - | [Toso 1997](#src-toso1997_grammatica), [Forner 1975](#src-forner1975) |
| `LIJ_NASAL_I` | /i/ → [ĩ], before [ŋ] | - | [Toso 1997](#src-toso1997_grammatica), [Forner 1975](#src-forner1975) |
| `LIJ_NASAL_U` | /u/ → [ũ], before [ŋ] | - | [Toso 1997](#src-toso1997_grammatica), [Forner 1975](#src-forner1975) |
| `LIJ_NASAL_Y` | /y/ → [ỹ], before [ŋ] | - | [Toso 1997](#src-toso1997_grammatica), [Forner 1975](#src-forner1975) |
| `LIJ_NASAL_O` | /ɔ/ → [ɔ̃], before [ŋ] | - | [Toso 1997](#src-toso1997_grammatica), [Forner 1975](#src-forner1975) |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="cina|çittæ|ciù|gexa|giornâ|lann-a|can|xatta" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lij")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| cina | [ˈtʃina] |
| çittæ | [siˈtɛː] |
| ciù | [ˈtʃy] |
| gexa | [ˈdʒeʒa] |
| giornâ | [dʒurˈnaː] |
| lann-a | [ˈlãŋa] |
| can | [ˈkaŋ] |
| xatta | [ˈʒata] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Libyan Arabic](ayl.md) · [Home](../index.md) · [Limburgish →](li.md)
