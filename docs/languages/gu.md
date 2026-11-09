# Gujarati (`gu`)

<!-- atlas:summary begin -->
Gujarati is an Indo-Aryan language, written in the Gujarati script. Glottolog places it in Bangladesh, India and Pakistan. The `gu` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `gu` |
| ISO 639-3 | [guj](https://iso639-3.sil.org/code/guj), Gujarati |
| Glottolog | [guja1252](https://glottolog.org/resource/languoid/id/guja1252), Gujarati |
| Wikidata | [Q5137](https://www.wikidata.org/wiki/Q5137) |
| Wikipedia | [Gujarati language](https://en.wikipedia.org/wiki/Gujarati_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [Bangladesh](by-region.md#bangladesh), [India](by-region.md#india), [Pakistan](by-region.md#pakistan) |
| Script | [Gujarati](by-script.md#gujarati) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1400, living |
| Parent | [Sanskrit](sa.md) `sa` |
| Explorer | [`gu` in the data explorer](https://tigregotico.github.io/orthography2ipa/#gu) |
| Spec file | [`gu.json`](../../orthography2ipa/data/gu.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Gujarati (Gujarat, India). Distinct Gujarati script derived from Devanagari. ⟨ળ⟩ = [ɭ] retroflex lateral is a phoneme (unlike most IA). Four-way laryngeal contrast retained.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1965 to 2003. [Sources](#sources) lists them. The spec file writes all 61 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/gu.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `gu` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-masica1991"></a>Masica, C. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
2. <a id="src-cardona_jain2003"></a>Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
3. <a id="src-cardona1965"></a>Cardona, G. (1965). *A Gujarati Reference Grammar*. University of Pennsylvania Press.
4. <a id="src-mistry1997"></a>Mistry, P. J. (1997). *Gujarati Phonology*. in Kaye, A.S. (ed.) Phonologies of Asia and Africa, Eisenbrauns. Cited: 653-673.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `gu` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 4082 | 0.1842 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 87 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d̪ t̪ t̪ʰ |  | ɖ ʈ ʈʰ |  | k kʰ ɡ |  |
| Affricate |  |  |  |  |  | dʑ tɕ tɕʰ |  |  |
| Nasal | m |  | n |  | ɳ | ɲ | ŋ |  |
| Trill |  |  | r̩ |  |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative |  | f | s z | ʃ | ʂ |  |  | h ɦ |
| Approximant |  | ʋ |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  | ɭ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open | aː |  | ɑ |

Sequences that the spec writes as one unit: [bə] [bʱ] [bʱə] [dʑə] [dʑʱ] [dʑʱə] [d̪ə] [d̪ʱ] [d̪ʱə] [fə] [jə] [kə] [kʰə] [lə] [mə] [nə] [pə] [pʰə] [sə] [tɕə] [tɕʰə] [t̪ə] [t̪ʰə] [w] [zə] [ŋə] [ɖə] [ɖʱ] [ɖʱə] [əi] [əu] [ɡə] [ɡʱ] [ɡʱə] [ɦə] [ɭə] [ɲə] [ɳə] [ɾə] [ʂə], and 5 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ઁ⟩ | [̃] |  |
| ⟨ં⟩ | [̃] |  |
| ⟨ઃ⟩ | [h] |  |
| ⟨અ⟩ | [ə] |  |
| ⟨આ⟩ | [ɑ] |  |
| ⟨ઇ⟩ | [i] |  |
| ⟨ઈ⟩ | [iː] |  |
| ⟨ઉ⟩ | [u] |  |
| ⟨ઊ⟩ | [uː] |  |
| ⟨ઋ⟩ | [r̩] |  |
| ⟨એ⟩ | [e] |  |
| ⟨ઐ⟩ | [əi] |  |
| ⟨ઓ⟩ | [o] |  |
| ⟨ઔ⟩ | [əu] |  |
| ⟨ક⟩ | [k] |  |
| ⟨ખ⟩ | [kʰ] |  |
| ⟨ગ⟩ | [ɡ] |  |
| ⟨ઘ⟩ | [ɡʱ] |  |
| ⟨ઙ⟩ | [ŋ] |  |
| ⟨ચ⟩ | [tɕ] |  |
| ⟨છ⟩ | [tɕʰ] |  |
| ⟨જ⟩ | [dʑ] |  |
| ⟨ઝ⟩ | [dʑʱ] |  |
| ⟨ઝ઼⟩ | [z] |  |
| ⟨ઞ⟩ | [ɲ] |  |
| ⟨ટ⟩ | [ʈ] |  |
| ⟨ઠ⟩ | [ʈʰ] |  |
| ⟨ડ⟩ | [ɖ] |  |
| ⟨ઢ⟩ | [ɖʱ] |  |
| ⟨ણ⟩ | [ɳ] |  |
| ⟨ત⟩ | [t̪] |  |
| ⟨થ⟩ | [t̪ʰ] |  |
| ⟨દ⟩ | [d̪] |  |
| ⟨ધ⟩ | [d̪ʱ] |  |
| ⟨ન⟩ | [n] |  |
| ⟨પ⟩ | [p] |  |
| ⟨ફ⟩ | [pʰ] [f] |  |
| ⟨ફ઼⟩ | [f] |  |
| ⟨બ⟩ | [b] |  |
| ⟨ભ⟩ | [bʱ] |  |
| ⟨મ⟩ | [m] |  |
| ⟨ય⟩ | [j] |  |
| ⟨ર⟩ | [ɾ] |  |
| ⟨લ⟩ | [l] |  |
| ⟨ળ⟩ | [ɭ] |  |
| ⟨વ⟩ | [ʋ] |  |
| ⟨શ⟩ | [ʃ] |  |
| ⟨ષ⟩ | [ʂ] |  |
| ⟨સ⟩ | [s] |  |
| ⟨હ⟩ | [ɦ] |  |
| ⟨ા⟩ | [ɑ] |  |
| ⟨િ⟩ | [i] |  |
| ⟨ી⟩ | [iː] |  |
| ⟨ુ⟩ | [u] |  |
| ⟨ૂ⟩ | [uː] |  |
| ⟨ૃ⟩ | [r̩] |  |
| ⟨ે⟩ | [e] |  |
| ⟨ૈ⟩ | [əi] |  |
| ⟨ો⟩ | [o] |  |
| ⟨ૌ⟩ | [əu] |  |
| ⟨્⟩ | ∅ |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 72 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `GU_SCHWA_FINAL_k` | /kə/ → [k], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_kʰ` | /kʰə/ → [kʰ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_ɡ` | /ɡə/ → [ɡ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_ɡʱ` | /ɡʱə/ → [ɡʱ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_ŋ` | /ŋə/ → [ŋ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_tɕ` | /tɕə/ → [tɕ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_tɕʰ` | /tɕʰə/ → [tɕʰ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_dʑ` | /dʑə/ → [dʑ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_dʑʱ` | /dʑʱə/ → [dʑʱ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_ɲ` | /ɲə/ → [ɲ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_ʈ` | /ʈə/ → [ʈ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_ʈʰ` | /ʈʰə/ → [ʈʰ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_ɖ` | /ɖə/ → [ɖ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_ɖʱ` | /ɖʱə/ → [ɖʱ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_ɳ` | /ɳə/ → [ɳ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_t̪` | /t̪ə/ → [t̪], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_t̪ʰ` | /t̪ʰə/ → [t̪ʰ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_d̪` | /d̪ə/ → [d̪], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_d̪ʱ` | /d̪ʱə/ → [d̪ʱ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_n` | /nə/ → [n], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_p` | /pə/ → [p], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_pʰ` | /pʰə/ → [pʰ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_f` | /fə/ → [f], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_b` | /bə/ → [b], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_bʱ` | /bʱə/ → [bʱ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_m` | /mə/ → [m], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_j` | /jə/ → [j], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_r` | /ɾə/ → [ɾ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_ɭ` | /ɭə/ → [ɭ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_l` | /lə/ → [l], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_ʋ` | /ʋə/ → [ʋ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_ʃ` | /ʃə/ → [ʃ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_ʂ` | /ʂə/ → [ʂ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_s` | /sə/ → [s], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_ɦ` | /ɦə/ → [ɦ], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_FINAL_z` | /zə/ → [z], not word-initially, word-finally | - | [Cardona 2003](#src-cardona_jain2003), [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_k` | /kə/ → [kə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_kʰ` | /kʰə/ → [kʰə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_ɡ` | /ɡə/ → [ɡə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_ɡʱ` | /ɡʱə/ → [ɡʱə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_ŋ` | /ŋə/ → [ŋə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_tɕ` | /tɕə/ → [tɕə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_tɕʰ` | /tɕʰə/ → [tɕʰə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_dʑ` | /dʑə/ → [dʑə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_dʑʱ` | /dʑʱə/ → [dʑʱə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_ɲ` | /ɲə/ → [ɲə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_ʈ` | /ʈə/ → [ʈə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_ʈʰ` | /ʈʰə/ → [ʈʰə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_ɖ` | /ɖə/ → [ɖə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_ɖʱ` | /ɖʱə/ → [ɖʱə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_ɳ` | /ɳə/ → [ɳə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_t̪` | /t̪ə/ → [t̪ə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_t̪ʰ` | /t̪ʰə/ → [t̪ʰə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_d̪` | /d̪ə/ → [d̪ə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_d̪ʱ` | /d̪ʱə/ → [d̪ʱə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_n` | /nə/ → [nə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_p` | /pə/ → [pə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_pʰ` | /pʰə/ → [pʰə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_f` | /fə/ → [fə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_b` | /bə/ → [bə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_bʱ` | /bʱə/ → [bʱə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_m` | /mə/ → [mə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_j` | /jə/ → [jə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_ɾ` | /ɾə/ → [ɾə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_ɭ` | /ɭə/ → [ɭə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_l` | /lə/ → [lə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_ʋ` | /ʋə/ → [ʋə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_ʃ` | /ʃə/ → [ʃə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_ʂ` | /ʂə/ → [ʂə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_s` | /sə/ → [sə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_ɦ` | /ɦə/ → [ɦə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
| `GU_SCHWA_KEEP_z` | /zə/ → [zə], not word-finally | - | [Mistry 1997](#src-mistry1997) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "gu")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Guaraní](gn.md) · [Home](../index.md) · [Gun →](guw.md)
