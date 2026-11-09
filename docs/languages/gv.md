# Manx (`gv`)

<!-- atlas:summary begin -->
Manx is a Goidelic language, written in the Latin script. Glottolog places it in Isle of Man and United Kingdom. The `gv` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `gv` |
| ISO 639-3 | [glv](https://iso639-3.sil.org/code/glv), Manx |
| Glottolog | [manx1243](https://glottolog.org/resource/languoid/id/manx1243), Manx |
| Wikidata | [Q12175](https://www.wikidata.org/wiki/Q12175) |
| Wikipedia | [Manx language](https://en.wikipedia.org/wiki/Manx_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Celtic > Goidelic](by-family.md#indo-european--celtic--goidelic) |
| Region | [Eurasia](by-region.md#eurasia) > [Isle of Man](by-region.md#isle-of-man), [United Kingdom](by-region.md#united-kingdom) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 600, living |
| Ancestor | [Proto-Goidelic (reconstructed)](https://tigregotico.github.io/orthography2ipa/#cel-x-goidelic) `cel-x-goidelic` |
| Explorer | [`gv` in the data explorer](https://tigregotico.github.io/orthography2ipa/#gv) |
| Spec file | [`gv.json`](../../orthography2ipa/data/gv.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Manx (Gaelg). Isle of Man. Last native speaker (Ned Maddrell) died 1974. Revival since 1970s, ~1,800 speakers (est. 2020). English/Welsh-based orthography descending from Bishop John Phillips' Book of Common Prayer tradition (unlike Irish/Scots Gaelic script). Simplified mutation system vs. Irish/Scots Gaelic.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1955 to 2020. [Sources](#sources) lists them. The spec file writes all 58 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/gv.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `gv` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-macaulay1992"></a>MacAulay, D. (ed.) (1992). *The Celtic Languages*. Cambridge University Press.
2. <a id="src-broderick1984"></a>Broderick, G. (1984). *A Handbook of Late Spoken Manx*. Niemeyer.
3. <a id="src-jackson1955"></a>Jackson, K.H. (1955). *Contributions to the Study of Manx Phonology*. Nelson.
4. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
5. <a id="src-lewin2020"></a>Lewin, Christopher (2020). *Aspects of the historical phonology of Manx*. PhD thesis, University of Edinburgh. Cited: 68-72. [era.ed.ac.uk](https://era.ed.ac.uk/handle/1842/37271)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `gv` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 690 | 0.2460 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 51 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  | n nʲ |  |  | ŋ |  |
| Trill |  |  | r rʲ |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f v | s | ʃ |  | x ɣ | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l lʲ |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː i̯ |  | u uː |
| Near-close | ɪ |  | ʊ |
| Close-mid | e eː |  | o oː ɤ |
| Mid |  | ə əː |  |
| Open-mid | ɛ ɛː |  | ɔ |
| Near-open | æ |  |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [eu] [iə] [kw] [w] [əi] [ɛːi] [ɛːu].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | ∅ |  |
| ⟨a⟩ | [a] [æ] |  |
| ⟨aa⟩ | [ɛː] [eː] |  |
| ⟨aaie⟩ | [ɛːi] |  |
| ⟨ae⟩ | [ɛː] |  |
| ⟨aie⟩ | [ɛːi] |  |
| ⟨aigh⟩ | [ɛːi] |  |
| ⟨aih⟩ | [ɛːi] |  |
| ⟨aiy⟩ | [eː] |  |
| ⟨aue⟩ | [ɛːu] |  |
| ⟨ay⟩ | [e] [eː] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] |  |
| ⟨ch⟩ | [x] |  |
| ⟨ck⟩ | [k] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨ea⟩ | [eː] [ɛː] |  |
| ⟨eay⟩ | [əː] |  |
| ⟨ee⟩ | [iː] |  |
| ⟨eea⟩ | [iə] |  |
| ⟨eigh⟩ | [əi] |  |
| ⟨eih⟩ | [əː] [əi] |  |
| ⟨eu⟩ | [eu] |  |
| ⟨ey⟩ | [əː] [ə] | word final [ə] |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gh⟩ | [x] [ɣ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] [ɪ] [ə] |  |
| ⟨ie⟩ | [i] [i̯] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨lh⟩ | [lʲ] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nn⟩ | [n] [nʲ] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨oa⟩ | [oː] |  |
| ⟨oie⟩ | [əi] [iː] |  |
| ⟨oo⟩ | [uː] |  |
| ⟨p⟩ | [p] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [r] [ɾ] |  |
| ⟨rr⟩ | [r] [rʲ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [t] |  |
| ⟨u⟩ | [u] [ʊ] [ɤ] |  |
| ⟨uy⟩ | [əː] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] | before vowel [j] · default [ə] [i] · word initial [j] |
| ⟨çh⟩ | [tʃ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 2 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `GV_SLENDER_FINAL_N` | /i e/ → [ə], before [n], with more context in the spec | ⟨Mannin⟩ [manənʲ] | [Broderick 1984](#src-broderick1984), Thomson 1992 |
| `GV_SLENDER_ONSET_CONSONANT` | /i e/ → ∅, after a consonant, before a vowel, with more context in the spec | ⟨giare⟩ [ɡʲɛːr] | [Broderick 1984](#src-broderick1984), Thomson 1992 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "gv")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Mansi](mns.md) · [Home](../index.md) · [Mapudungun →](arn.md)
