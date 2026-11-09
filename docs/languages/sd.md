# Sindhi (`sd`)

<!-- atlas:summary begin -->
Sindhi is an Indo-Aryan language, written in the Latin script. Glottolog places it in India and Pakistan. The `sd` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sd` |
| ISO 639-3 | [snd](https://iso639-3.sil.org/code/snd), Sindhi |
| Glottolog | [sind1272](https://glottolog.org/resource/languoid/id/sind1272), Sindhi |
| Wikidata | [Q33997](https://www.wikidata.org/wiki/Q33997) |
| Wikipedia | [Sindhi language](https://en.wikipedia.org/wiki/Sindhi_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [India](by-region.md#india), [Pakistan](by-region.md#pakistan) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1200, living |
| Parent | [Sanskrit](sa.md) `sa` |
| Explorer | [`sd` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sd) |
| Spec file | [`sd.json`](../../orthography2ipa/data/sd.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Sindhi (Pakistan/India). Typologically remarkable: four implosives /ɓ ɗ ʄ ɠ/, rare in Indo-Aryan. Full four-way laryngeal contrast plus implosives. Written in Perso-Arabic (Pakistan), Devanagari (India), and the Khudabadi script (traditional).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1872 to 2003. [Sources](#sources) lists them. The spec file writes all 53 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sd.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sd` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-masica1991"></a>Masica, C. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
2. <a id="src-cardona_jain2003"></a>Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
3. <a id="src-trump1872"></a>Trump, E. (1872). *Grammar of the Sindhi Language*. Trübner.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 55 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d̪ t̪ t̪ʰ |  | ɖ ʈ ʈʰ |  | k kʰ ɡ | q |  |
| Affricate |  |  |  |  |  | dʑ tɕ tɕʰ |  |  |  |
| Nasal | m |  | n |  | ɳ | ɲ | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Tap |  |  |  |  | ɽ |  |  |  |  |
| Fricative |  | f | s z | ʃ | ʂ |  | x ɣ |  | h ɦ |
| Approximant |  | ʋ |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | eː | oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [bʱ] [dʑʱ] [d̪ʱ] [w] [ɓ] [ɖʱ] [ɗ] [əi] [əu] [ɠ] [ɡʱ] [ʄ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [əi] |  |
| ⟨au⟩ | [əu] |  |
| ⟨b⟩ | [b] |  |
| ⟨bh⟩ | [bʱ] |  |
| ⟨b̈⟩ | [ɓ] |  |
| ⟨c⟩ | [tɕ] |  |
| ⟨ch⟩ | [tɕʰ] |  |
| ⟨d⟩ | [d̪] |  |
| ⟨dh⟩ | [d̪ʱ] |  |
| ⟨e⟩ | [eː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gh⟩ | [ɡʱ] |  |
| ⟨h⟩ | [ɦ] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʑ] |  |
| ⟨jh⟩ | [dʑʱ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨q⟩ | [q] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t̪] |  |
| ⟨th⟩ | [t̪ʰ] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [ʋ] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ā⟩ | [aː] |  |
| ⟨ġ⟩ | [ɣ] |  |
| ⟨ī⟩ | [iː] |  |
| ⟨ś⟩ | [ʃ] |  |
| ⟨ū⟩ | [uː] |  |
| ⟨ǰ⟩ | [ʄ] |  |
| ⟨ḍ⟩ | [ɖ] |  |
| ⟨ḍh⟩ | [ɖʱ] |  |
| ⟨ḍ̈⟩ | [ɗ] |  |
| ⟨ḡ⟩ | [ɠ] |  |
| ⟨ṅ⟩ | [ŋ] |  |
| ⟨ṇ⟩ | [ɳ] |  |
| ⟨ṛ⟩ | [ɽ] |  |
| ⟨ṣ⟩ | [ʂ] |  |
| ⟨ṭ⟩ | [ʈ] |  |
| ⟨ṭh⟩ | [ʈʰ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sd")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Silesian](szl.md) · [Home](../index.md) · [Sinhala →](si.md)
