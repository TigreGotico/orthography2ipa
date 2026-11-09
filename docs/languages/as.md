# Assamese (`as`)

<!-- atlas:summary begin -->
Assamese is an Indo-Aryan language, written in the Bengali script. Glottolog places it in Bangladesh, Bhutan and India. The `as` spec is at the production tier. It cites 4 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `as` |
| ISO 639-3 | [asm](https://iso639-3.sil.org/code/asm), Assamese |
| Glottolog | [assa1263](https://glottolog.org/resource/languoid/id/assa1263), Assamese |
| Wikidata | [Q29401](https://www.wikidata.org/wiki/Q29401) |
| Wikipedia | [Assamese language](https://en.wikipedia.org/wiki/Assamese_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [Bangladesh](by-region.md#bangladesh), [Bhutan](by-region.md#bhutan), [India](by-region.md#india) |
| Script | [Bengali](by-script.md#bengali) (abugida) |
| Tier | [production](../specs/quality_tiers.md#production) |
| Attested | from 1400, living |
| Parent | [Sanskrit](sa.md) `sa` |
| Explorer | [`as` in the data explorer](https://tigregotico.github.io/orthography2ipa/#as) |
| Spec file | [`as.json`](../../orthography2ipa/data/as.json) |
<!-- atlas:header end -->

## Overview

The `as` spec transcribes Standard Assamese. Mahanta (2012, p. 217) states that a neutral blend of eastern Assamese is the norm for the mass media. Her description comes from a speaker who grew up in Jorhat, in eastern Assam. The Assamese script shares its letters with Bengali, except two (Mahanta 2012, p. 219, note 2). The sound systems differ much more than the scripts. The spec reads the letters with the Assamese values of Mahanta (2012) and Roy & Mahanta (2018), not with the Bengali values.

Both main sources are open to read. Mahanta (2012) is the [Illustration of the IPA for Assamese](https://www.cambridge.org/core/journals/journal-of-the-international-phonetic-association/article/assamese/FD4090937A7BC4318FCF1117E82313E4). Roy & Mahanta (2018) is in the [ISCA archive](https://www.isca-archive.org/interspeech_2018/roy18_interspeech.pdf). It compares a rule-based Assamese G2P system with trained models. The training words come from the [xobdo](https://xobdo.org/) corpus and the RCILTS corpus (p. 2829).

The orthography counts as deep, so the production bar is a PER of 0.25 ([quality tiers](../specs/quality_tiers.md#the-per-threshold)). The script does not write the inherent vowel. It also keeps a retroflex series and three sibilant letters that the spoken language has merged. The sound changes are regular, but the letter-to-sound map is not shallow.

## Consonants

Mahanta (2012, p. 218) lists twenty consonants. Roy & Mahanta (2018, p. 2829) count twenty-three, and their Table 1 adapts the table of Mahanta (2012).

The table has one series of alveolar plosives and no retroflex series. The script still writes the retroflex letters ⟨ট ঠ ড ঢ ণ⟩. Mahanta (2012, p. 219) states that neither the dental nor the retroflex place is part of the consonant system, and that the obstruents are distinctly alveolar. The spec reads both letter series as /t tʰ d dʱ n/.

Assamese has no affricates as distinctive units (Mahanta 2012, p. 219). The spec reads ⟨চ ছ⟩ as /s/ and ⟨জ ঝ য⟩ as /z zʱ/, not as the palatals of their Bengali cognates. The word list gives ছাল [sɑl] 'roof of a house' and জাল [zɑl] 'net' (p. 218).

The sibilant letters ⟨শ ষ স⟩ write the velar fricative /x/, as in শাল [xɑl] 'loom' (Mahanta 2012, p. 218). The [Wikipedia article on Assamese](https://en.wikipedia.org/wiki/Assamese_language) calls this /x/ unusual among the eastern Indo-Aryan languages. Before a consonant, /x/ becomes [s]. Roy & Mahanta (2018, p. 2829) state the rule as "The consonant clusters xC becomes sC", with /oboxtʰaːn/ becoming /obostʰaːn/ 'station'. The allophone rule `AS_X_BEFORE_CONSONANT` encodes it, so স্কুল gives [skul].

The aspirate /kʰ/ often becomes a fricative. Mahanta (2012, p. 219) gives [ɡɑkʰiɹ], [ɡɑχiɹ] and [ɡɑxiɹ] for 'milk'. The choice depends on the speaker and on the care of the speech. The spec keeps [kʰ] as the reading of ⟨খ⟩ and puts the fricative in its allophone table.

The only rhotic is the approximant /ɹ/, written ⟨ৰ⟩, as in ৰাম [ɹɑm] (Mahanta 2012, p. 218). The spec also reads ⟨ড়⟩ as /ɹ/ and ⟨ঢ়⟩ as /ɹʱ/. The letter ⟨ৱ⟩ writes /w/, as in ছোৱালী [sʊwɑli] 'girl' (p. 218). The letters ⟨ৰ⟩ and ⟨ৱ⟩ are the two letters that differ from the Bengali script (p. 219, note 2).

## Vowels

Assamese has eight oral vowels, /i e ɛ u ʊ o ɔ ɑ/ (Mahanta 2012, p. 220). The spec reads ⟨ো⟩ as /ʊ/ and ⟨ে⟩ as /ɛ/, not as the /o/ and /e/ of their Bengali cognates. The vowel list gives বোল [bʊl] 'colour' and বেল [bɛl] 'stupid person' (p. 220).

The close-mid vowels [e] and [o] occur mostly before /i/ or /u/ in the next syllable (Mahanta 2012, p. 220). Regressive vowel harmony creates them: before a high vowel, /ɛ ɔ ʊ/ become /e o u/ (p. 221). Roy & Mahanta (2018, p. 2829) state the same rules, with /bɔsɔr/ becoming /bosori/ 'annually'. A nasal next to the trigger vowel blocks the harmony, and so does a coda consonant (Mahanta 2012, p. 221).

## The inherent vowel

The inherent vowel is /ɔ/ (Roy & Mahanta 2018, p. 2829). The same page says that it "is generally deleted in the end of a word". The spec encodes this deletion with `inherent_vowel_final`, so কলম gives [kɔlɔm] and অসম gives [ɔxɔm].

The deletion does not apply in two cases. If the syllable has no other nucleus, the vowel stays, so the monosyllable ক gives [kɔ]. Assamese syllables also admit no complex coda (Roy & Mahanta 2018, p. 2830). So the vowel stays where the deletion would leave two consonants at the end of the word: অংক gives [ɔŋkɔ] and ভক্ত gives [bʱɔktɔ].

## Prominence

The spec marks no stress. Mahanta (2012, p. 222) describes prominence as phonetic and not contrastive. Prominence falls on the second syllable if that syllable is closed and the first is open. In all other words it falls on the first syllable, and it never falls later than the second. The examples include 'eye', with prominence on the first syllable of [soku], and 'life', with prominence on the second syllable of [zibɔn]. The spec has no stress block, so the engine output carries no stress mark.

## Weak points

The engine does not apply vowel harmony. Mahanta (2012, p. 220) prints বেলি 'sun' as [beli], and the engine gives [bɛli]. The spec notes give ⟨চকু⟩ for [sòku] 'eye' (Mahanta 2012, p. 222), and the engine gives [sɔku]. The main target of the harmony is the unwritten inherent vowel, and no rule can address that slot. The rule language also cannot state the blocking by nasals and codas.

The engine always reads the inherent vowel as [ɔ]. Mahanta (2012, p. 220) prints বল 'let's go' as [bol], and the engine gives [bɔl]. The [Wikipedia article on Assamese](https://en.wikipedia.org/wiki/Assamese_language) gives the spelling ক'লা for [kola] 'black', against কলা [kɔla] 'deaf'. The engine splits ক'লা at the apostrophe and gives [kɔ la].

The spec writes the low vowel as [a]. Mahanta (2012, pp. 218, 220) prints [ɑ] in every word, so পাল 'to rear' is [pɑl] in the source and [pal] in the engine output. The source prints the voiced aspirates with a superscript [ʰ], as in ভাল [bʰɑl] 'good' (p. 218). The engine writes the breathy-voice mark [bʱ]. This second difference is notation only.

The board golds use three conventions that the sources do not print. They write [ɦ] for the glottal fricative, [ɪ ʊ] for the second element of a diphthong, and, in `vox_communis`, [ʱ] on voiceless stops. Mahanta (2012) prints [h] (p. 218) and the diphthongs /ei oi ai ou au/ (p. 222). The spec follows the source, so these words count as errors on the board. The [WikiPron Assamese list](https://github.com/CUNY-CL/wikipron/blob/master/data/scrape/tsv/asm_beng_broad.tsv) is the qualifying gold. The `vox_communis` row is epitran output, so it measures agreement with epitran, not with Assamese.

The spec does not encode consonant gemination. Mahanta (2012, p. 219) reports it after Moral (1996), as in [sɑppɔn] 'fifty six'. The spec also has no rule for the gemination before the ya-phala ⟨্য⟩.

<!-- atlas:lects begin -->
## Related lects

No spec names `as` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-mahanta2012"></a>Mahanta, S. (2012). *Assamese (Illustrations of the IPA)*. Journal of the International Phonetic Association 42(2). Cited: 217-224. [doi.org](https://doi.org/10.1017/S0025100312000096)
2. <a id="src-roy_mahanta2018"></a>Roy, S. & Mahanta, S. (2018). *A Hybrid Approach to Grapheme to Phoneme Conversion in Assamese*. Interspeech 2018, 2828-2831. Cited: 2828-2831. [doi.org](https://doi.org/10.21437/Interspeech.2018-1694)
3. <a id="src-masica1991"></a>Masica, C. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
4. <a id="src-goswami1966"></a>Goswami, G.C. (1966). *The Structure of Assamese*. Gauhati University.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `as` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2981 | 0.0918 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `as` | generated | epitran-derived | CC0 1.0 | 5328 | 0.2436 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 44 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  | k kʰ ɡ |  |  |
| Affricate |  |  | dz |  |  |  |  |
| Nasal | m |  | n |  | ŋ |  |  |
| Fricative | β | f v | s z |  | x | χ | h ɦ |
| Approximant |  |  | ɹ | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Near-close |  | ʊ |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a | ɑ |

Sequences that the spec writes as one unit: [bʱ] [dʱ] [oi] [ou] [w] [zʱ] [ɡʱ] [ɹi] [ɹʱ] [̃].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ঁ⟩ | [̃] |  |
| ⟨ং⟩ | [ŋ] |  |
| ⟨ঃ⟩ | [h] |  |
| ⟨অ⟩ | [ɔ] [o] |  |
| ⟨আ⟩ | [a] |  |
| ⟨ই⟩ | [i] |  |
| ⟨ঈ⟩ | [i] |  |
| ⟨উ⟩ | [u] |  |
| ⟨ঊ⟩ | [u] |  |
| ⟨ঋ⟩ | [ɹi] |  |
| ⟨এ⟩ | [ɛ] [e] |  |
| ⟨ঐ⟩ | [oi] |  |
| ⟨ও⟩ | [ʊ] [u] |  |
| ⟨ঔ⟩ | [ou] |  |
| ⟨ক⟩ | [k] |  |
| ⟨ক্ষ⟩ | [kʰ] |  |
| ⟨খ⟩ | [kʰ] |  |
| ⟨গ⟩ | [ɡ] |  |
| ⟨ঘ⟩ | [ɡʱ] |  |
| ⟨ঙ⟩ | [ŋ] |  |
| ⟨চ⟩ | [s] |  |
| ⟨ছ⟩ | [s] |  |
| ⟨জ⟩ | [z] |  |
| ⟨ঝ⟩ | [zʱ] |  |
| ⟨ঞ⟩ | [n] |  |
| ⟨ট⟩ | [t] |  |
| ⟨ঠ⟩ | [tʰ] |  |
| ⟨ড⟩ | [d] |  |
| ⟨ড়⟩ | [ɹ] |  |
| ⟨ঢ⟩ | [dʱ] |  |
| ⟨ঢ়⟩ | [ɹʱ] |  |
| ⟨ণ⟩ | [n] |  |
| ⟨ত⟩ | [t] |  |
| ⟨থ⟩ | [tʰ] |  |
| ⟨দ⟩ | [d] |  |
| ⟨ধ⟩ | [dʱ] |  |
| ⟨ন⟩ | [n] |  |
| ⟨প⟩ | [p] |  |
| ⟨ফ⟩ | [pʰ] [f] |  |
| ⟨ব⟩ | [b] [w] |  |
| ⟨ভ⟩ | [bʱ] [v] |  |
| ⟨ম⟩ | [m] |  |
| ⟨য⟩ | [z] [j] |  |
| ⟨য়⟩ | [j] |  |
| ⟨র⟩ | [ɹ] |  |
| ⟨ল⟩ | [l] |  |
| ⟨শ⟩ | [x] |  |
| ⟨ষ⟩ | [x] |  |
| ⟨স⟩ | [x] |  |
| ⟨হ⟩ | [h] |  |
| ⟨া⟩ | [a] |  |
| ⟨ি⟩ | [i] |  |
| ⟨ী⟩ | [i] |  |
| ⟨ু⟩ | [u] |  |
| ⟨ূ⟩ | [u] |  |
| ⟨ৃ⟩ | [ɹi] |  |
| ⟨ে⟩ | [ɛ] [e] |  |
| ⟨ৈ⟩ | [oi] |  |
| ⟨ো⟩ | [ʊ] [u] |  |
| ⟨ৌ⟩ | [ou] |  |
| ⟨্⟩ | ∅ |  |
| ⟨ৎ⟩ | [t] |  |
| ⟨ৰ⟩ | [ɹ] |  |
| ⟨ৱ⟩ | [w] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 1 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `AS_X_BEFORE_CONSONANT` | /x/ → [s], before a consonant | - | Roy & Mahanta 2018 |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="পাল|ভাল|শাল|ছাল|জাল|ৰাম|ছোৱালী|বোল|বেল|বেলি|বল|চকু|কলম|অসম|ক|অংক|ভক্ত|স্কুল" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "as")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| পাল | [pal] |
| ভাল | [bʱal] |
| শাল | [xal] |
| ছাল | [sal] |
| জাল | [zal] |
| ৰাম | [ɹam] |
| ছোৱালী | [sʊwali] |
| বোল | [bʊl] |
| বেল | [bɛl] |
| বেলি | [bɛli] |
| বল | [bɔl] |
| চকু | [sɔku] |
| কলম | [kɔlɔm] |
| অসম | [ɔxɔm] |
| ক | [kɔ] |
| অংক | [ɔŋkɔ] |
| ভক্ত | [bʱɔktɔ] |
| স্কুল | [skul] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Aromanian](rup.md) · [Home](../index.md) · [Assyrian Neo-Aramaic →](aii.md)
