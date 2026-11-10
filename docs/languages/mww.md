# Hmong Daw (`mww`)

<!-- atlas:summary begin -->
Hmong Daw is a Hmong-Mien language, written in the Latin script. Glottolog places it in China, Laos, Thailand and Vietnam. The `mww` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mww` |
| ISO 639-3 | [mww](https://iso639-3.sil.org/code/mww), Hmong Daw |
| Glottolog | [hmon1333](https://glottolog.org/resource/languoid/id/hmon1333), Hmong Daw |
| Wikipedia | [Hmong language](https://en.wikipedia.org/wiki/Hmong_language) |
| Family | [Hmong-Mien](by-family.md#hmong-mien) |
| Region | [Eurasia](by-region.md#eurasia) > [China](by-region.md#china), [Laos](by-region.md#laos), [Thailand](by-region.md#thailand), [Vietnam](by-region.md#vietnam) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Hmong-Mien](https://tigregotico.github.io/orthography2ipa/#x-clade-hmon1336) `x-clade-hmon1336` |
| Explorer | [`mww` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mww) |
| Spec file | [`mww.json`](../../orthography2ipa/data/mww.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> RPA (Romanized Popular Alphabet, Smalley/Barney/Bertrais 1953). Monosyllabic/tonal: no lexical word stress is orthographically predictable, so no `stress` block is set (docs/specs/quality_tiers.md stress exemption for tonal monosyllabic languages, cf. Vietnamese and Yoruba specs).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1976 to 2024. [Sources](#sources) lists them. The spec file writes all 66 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mww.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mww` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 2 of them have a DOI or a URL. The spec file holds a note on what 3 of them support.

1. <a id="src-glottolog2024"></a>Hammarström, Harald, Forkel, Robert, Haspelmath, Martin, Bank, Sebastian (2024). *Glottolog 5.0*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/)
2. <a id="src-ratliff2010"></a>Ratliff, Martha (2010). *Hmong-Mien Language History*. Pacific Linguistics, Australian National University.
3. <a id="src-smalley1976"></a>Smalley, William A. (1976). *The problem of consonants and tone: Hmong (Meo, Miao)*. In Consonant Types and Tone, ed. Larry M. Hyman, USC.
4. <a id="src-smalley1990"></a>Smalley, William A., Vang, Chia Koua, Yang, Gnia Yee (1990). *Mother of Writing: The Origin and Development of a Hmong Messianic Script*. University of Chicago Press.
5. <a id="src-wikipron"></a>Lee, Jackson L. et al. (2020). *WikiPron: A Multilingual Pronunciation Dictionary Scraped from Wiktionary*. LREC. [github.com](https://github.com/CUNY-CL/wikipron)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `mww` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 489 | 0.0107 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 83 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ pˡ pˡʰ |  | d t tʰ ⁿd ⁿtʰ | ʈ | c cʰ | k kʰ | q qʰ |  |
| Affricate |  |  | t͡s t͡sʰ ⁿd͡z ⁿt͡sʰ |  |  |  |  |  |
| Nasal | m mˡ m̥ |  | n n̥ |  | ɲ ɲ̊ |  |  |  |
| Fricative |  | f v | s | ʂ ʐ | ç ʝ |  |  | h |
| Lateral approximant |  |  | l l̥ |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid | e ẽ |  |  |
| Open | a |  | ɒ ɒ̃ |

Sequences that the spec writes as one unit: [ai̯] [ai̯˧] [au̯] [au̯˧] [aɨ̯] [aɨ̯˧] [a˧] [dʱ] [e˧] [iə̯] [iə̯˧] [i˧] [t͡ʂ] [t͡ʂʰ] [uə̯] [uə̯˧] [u˧] [ɒ˧] [ɒ̃˧] [ɨ˧] [˥] [˥˧] [˧˦] [˧˩̤] [˧́] [˩] [˩̰] [ᵐb] [ᵐbˡ] [ᵐpˡʰ] [ᵑkʰ] [ᵑɡ] [ᶮɟ] [ᶯd͡ʐ] [ᶯt͡ʂʰ] [ᶯɖ] [ᶰɢ] [ẽ˧].

Tones: [˧] mid (unmarked), [˥] high (-b), [˥˧] high-falling (-j), [˧˦] mid-rising (-v), [˩] low (-s), [˧˩̤] low breathy-falling (-g), [˩̰] low creaky/glottalized (-m), [˧́] raised-mid, loanword tone (-d).
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a˧] |  |
| ⟨ai⟩ | [ai̯˧] |  |
| ⟨au⟩ | [au̯˧] |  |
| ⟨aw⟩ | [aɨ̯˧] |  |
| ⟨b⟩ | [˥] |  |
| ⟨c⟩ | [c] |  |
| ⟨ch⟩ | [cʰ] |  |
| ⟨d⟩ | [d] | after vowel [˧́] · intervocalic [d] |
| ⟨dh⟩ | [dʱ] |  |
| ⟨e⟩ | [e˧] |  |
| ⟨ee⟩ | [ẽ˧] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [˧˩̤] |  |
| ⟨h⟩ | [h] |  |
| ⟨hl⟩ | [l̥] |  |
| ⟨hm⟩ | [m̥] |  |
| ⟨hn⟩ | [n̥] |  |
| ⟨hny⟩ | [ɲ̊] |  |
| ⟨i⟩ | [i˧] |  |
| ⟨ia⟩ | [iə̯˧] |  |
| ⟨j⟩ | [˥˧] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] | after vowel [˩̰] · intervocalic [m] |
| ⟨ml⟩ | [mˡ] |  |
| ⟨n⟩ | [n] |  |
| ⟨nc⟩ | [ᶮɟ] |  |
| ⟨nk⟩ | [ᵑɡ] |  |
| ⟨nkh⟩ | [ᵑkʰ] |  |
| ⟨np⟩ | [ᵐb] |  |
| ⟨npl⟩ | [ᵐbˡ] |  |
| ⟨nplh⟩ | [ᵐpˡʰ] |  |
| ⟨nq⟩ | [ᶰɢ] |  |
| ⟨nr⟩ | [ᶯɖ] |  |
| ⟨nt⟩ | [ⁿd] |  |
| ⟨nth⟩ | [ⁿtʰ] |  |
| ⟨nts⟩ | [ᶯd͡ʐ] |  |
| ⟨ntsh⟩ | [ᶯt͡ʂʰ] |  |
| ⟨ntx⟩ | [ⁿd͡z] |  |
| ⟨ntxh⟩ | [ⁿt͡sʰ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [ɒ˧] |  |
| ⟨oo⟩ | [ɒ̃˧] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨pl⟩ | [pˡ] |  |
| ⟨plh⟩ | [pˡʰ] |  |
| ⟨q⟩ | [q] |  |
| ⟨qh⟩ | [qʰ] |  |
| ⟨r⟩ | [ʈ] |  |
| ⟨s⟩ | [ʂ] | after vowel [˩] · intervocalic [ʂ] |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨ts⟩ | [t͡ʂ] |  |
| ⟨tsh⟩ | [t͡ʂʰ] |  |
| ⟨tx⟩ | [t͡s] |  |
| ⟨txh⟩ | [t͡sʰ] |  |
| ⟨u⟩ | [u˧] |  |
| ⟨ua⟩ | [uə̯˧] |  |
| ⟨v⟩ | [v] | after vowel [˧˦] · intervocalic [v] |
| ⟨w⟩ | [ɨ˧] |  |
| ⟨x⟩ | [s] |  |
| ⟨xy⟩ | [ç] |  |
| ⟨y⟩ | [ʝ] |  |
| ⟨z⟩ | [ʐ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 13 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `MWW_MID_UNSPELLED_a` | /a˧/ → [a], before [˥] [˥˧] [˧˦] [˩] [˧˩̤] [˩̰] [˧́] | - | [Ratliff 2010](#src-ratliff2010), [Smalley 1976](#src-smalley1976) |
| `MWW_MID_UNSPELLED_e` | /e˧/ → [e], before [˥] [˥˧] [˧˦] [˩] [˧˩̤] [˩̰] [˧́] | - | - |
| `MWW_MID_UNSPELLED_i` | /i˧/ → [i], before [˥] [˥˧] [˧˦] [˩] [˧˩̤] [˩̰] [˧́] | - | - |
| `MWW_MID_UNSPELLED_o` | /ɒ˧/ → [ɒ], before [˥] [˥˧] [˧˦] [˩] [˧˩̤] [˩̰] [˧́] | - | - |
| `MWW_MID_UNSPELLED_u` | /u˧/ → [u], before [˥] [˥˧] [˧˦] [˩] [˧˩̤] [˩̰] [˧́] | - | - |
| `MWW_MID_UNSPELLED_ee` | /ẽ˧/ → [ẽ], before [˥] [˥˧] [˧˦] [˩] [˧˩̤] [˩̰] [˧́] | - | - |
| `MWW_MID_UNSPELLED_oo` | /ɒ̃˧/ → [ɒ̃], before [˥] [˥˧] [˧˦] [˩] [˧˩̤] [˩̰] [˧́] | - | - |
| `MWW_MID_UNSPELLED_ia` | /iə̯˧/ → [iə̯], before [˥] [˥˧] [˧˦] [˩] [˧˩̤] [˩̰] [˧́] | - | - |
| `MWW_MID_UNSPELLED_ua` | /uə̯˧/ → [uə̯], before [˥] [˥˧] [˧˦] [˩] [˧˩̤] [˩̰] [˧́] | - | - |
| `MWW_MID_UNSPELLED_ai` | /ai̯˧/ → [ai̯], before [˥] [˥˧] [˧˦] [˩] [˧˩̤] [˩̰] [˧́] | - | - |
| `MWW_MID_UNSPELLED_au` | /au̯˧/ → [au̯], before [˥] [˥˧] [˧˦] [˩] [˧˩̤] [˩̰] [˧́] | - | - |
| `MWW_MID_UNSPELLED_aw` | /aɨ̯˧/ → [aɨ̯], before [˥] [˥˧] [˧˦] [˩] [˧˩̤] [˩̰] [˧́] | - | - |
| `MWW_MID_UNSPELLED_w` | /ɨ˧/ → [ɨ], before [˥] [˥˧] [˧˦] [˩] [˧˩̤] [˩̰] [˧́] | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mww")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Hiri Motu](ho.md) · [Home](../index.md) · [Hungarian →](hu.md)
