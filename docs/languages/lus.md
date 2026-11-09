# Mizo (`lus`)

<!-- atlas:summary begin -->
Mizo is a Sino-Tibetan language, written in the Latin script. Glottolog places it in Bangladesh, India and Myanmar (Burma). The `lus` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lus` |
| ISO 639-3 | [lus](https://iso639-3.sil.org/code/lus), Lushai |
| Glottolog | [lush1249](https://glottolog.org/resource/languoid/id/lush1249), Mizo |
| Wikidata | [Q36147](https://www.wikidata.org/wiki/Q36147) |
| Wikipedia | [Mizo language](https://en.wikipedia.org/wiki/Mizo_language) |
| Family | [Sino-Tibetan](by-family.md#sino-tibetan) |
| Region | [Eurasia](by-region.md#eurasia) > [Bangladesh](by-region.md#bangladesh), [India](by-region.md#india), [Myanmar (Burma)](by-region.md#myanmar-burma) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1894, living |
| Ancestor | [Proto-Kuki-Chin (reconstructed)](https://tigregotico.github.io/orthography2ipa/#mni-x-proto-kuki-chin) `mni-x-proto-kuki-chin` |
| Explorer | [`lus` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lus) |
| Spec file | [`lus.json`](../../orthography2ipa/data/lus.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Mizo (Lushai), spoken in Mizoram, India. Central Kuki-Chin branch, Sino-Tibetan. Alphabet devised 1894 by J.H. Lorrain & F.W. Savidge on Hunterian transliteration principles and is highly regular/phonemic (Wikipedia, Lorrain 1940 grammar). Circumflex marks long vowels (aâ eê iî oô uû).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1940 to 2009. [Sources](#sources) lists them. The spec file writes all 48 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/lus.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `lus` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-chhangte1993"></a>Chhangte, L. (1993). *Mizo Syntax*. University of Oregon PhD dissertation.
2. <a id="src-lorrain1940"></a>Lorrain, J.H. (1940). *Dictionary of the Lushai Language*. The Asiatic Society.
3. <a id="src-vanbik2009"></a>VanBik, K. (2009). *Proto-Kuki-Chin: A Reconstructed Ancestor of the Kuki-Chin Languages*. STEDT Monograph 8, UC Berkeley.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 50 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  |  | k kʰ |  |
| Affricate |  |  | ts tsʰ | tʃ tʃʰ |  |  |  |
| Nasal | m m̥ |  | n n̥ |  |  | ŋ ŋ̊ ŋ̥ |  |
| Trill |  |  | r r̥ |  |  |  |  |
| Fricative |  | f v | s z |  |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l l̥ |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open-mid |  | ɔ |
| Open | a aː |  |

Sequences that the spec writes as one unit: [ai] [au] [ei] [eu] [ia] [iu] [t͡ɾ] [t͡ɾʰ] [ua] [ui].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [ai] |  |
| ⟨au⟩ | [au] |  |
| ⟨aw⟩ | [ɔ] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [ts] |  |
| ⟨chh⟩ | [tsʰ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨ei⟩ | [ei] |  |
| ⟨eu⟩ | [eu] |  |
| ⟨f⟩ | [f] |  |
| ⟨h⟩ | [h] |  |
| ⟨hl⟩ | [l̥] |  |
| ⟨hm⟩ | [m̥] |  |
| ⟨hn⟩ | [n̥] |  |
| ⟨hng⟩ | [ŋ̥] |  |
| ⟨hr⟩ | [r̥] |  |
| ⟨i⟩ | [i] |  |
| ⟨ia⟩ | [ia] |  |
| ⟨iu⟩ | [iu] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ngh⟩ | [ŋ̊] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨u⟩ | [u] |  |
| ⟨ua⟩ | [ua] |  |
| ⟨ui⟩ | [ui] |  |
| ⟨v⟩ | [v] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨â⟩ | [aː] |  |
| ⟨ê⟩ | [eː] |  |
| ⟨î⟩ | [iː] |  |
| ⟨ô⟩ | [oː] |  |
| ⟨û⟩ | [uː] |  |
| ⟨ṭ⟩ | [t͡ɾ] |  |
| ⟨ṭh⟩ | [t͡ɾʰ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lus")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Mirandese](mwl.md) · [Home](../index.md) · [Modern Greek →](el.md)
