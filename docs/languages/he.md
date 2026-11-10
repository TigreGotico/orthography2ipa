# Hebrew (`he`)

<!-- atlas:summary begin -->
Hebrew is a Central Semitic language, written in the Hebrew script. Glottolog places it in 5 countries. The `he` spec is at the research tier. It cites 4 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `he` |
| ISO 639-3 | [heb](https://iso639-3.sil.org/code/heb), Hebrew |
| Glottolog | [hebr1245](https://glottolog.org/resource/languoid/id/hebr1245), Modern Hebrew |
| Wikidata | [Q9288](https://www.wikidata.org/wiki/Q9288) |
| Wikipedia | [Hebrew language](https://en.wikipedia.org/wiki/Hebrew_language) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Semitic > Central Semitic](by-family.md#afro-asiatic--semitic--central-semitic) |
| Region | [Eurasia](by-region.md#eurasia) > [Israel](by-region.md#israel), [Jordan](by-region.md#jordan), [Lebanon](by-region.md#lebanon), [Palestinian Territories](by-region.md#palestinian-territories), [Syria](by-region.md#syria) |
| Script | [Hebrew](by-script.md#hebrew) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1948, living |
| Ancestor | [Ancient Hebrew (Biblical Hebrew)](https://tigregotico.github.io/orthography2ipa/#hbo) `hbo` |
| Explorer | [`he` in the data explorer](https://tigregotico.github.io/orthography2ipa/#he) |
| Spec file | [`he.json`](../../orthography2ipa/data/he.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Modern Israeli Hebrew (Non-Oriental pronunciation, Laufer 1999).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1997 to 2021. [Sources](#sources) lists them. The spec file writes all 127 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/he.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `he` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-laufer1999"></a>Laufer, A. (1999). *Hebrew (Illustrations of the IPA)*. Handbook of the International Phonetic Association, Cambridge University Press, pp. 96-99, earlier version in Journal of the International Phonetic Association 20(2), 1990, 40-43. Cited: 96-99. [cambridge.org](https://www.cambridge.org/core/journals/journal-of-the-international-phonetic-association/article/hebrew/D23594A30B44604EFD3E88172BE58EB1)
2. <a id="src-bolozky1997"></a>Bolozky, S. (1997). *Israeli Hebrew Phonology*. In A.S. Kaye (ed.), Phonologies of Asia and Africa, Vol. 1, pp. 287-311. Winona Lake: Eisenbrauns. Cited: 287-311.
3. <a id="src-pariente2021"></a>Pariente, I. (2021). *Theoretical issues in Modern Hebrew phonology*. LOT Dissertation Series 599, Amsterdam: LOT (ISBN 978-94-6093-384-4). Cited: 6-9. [dx.medra.org](https://dx.medra.org/10.48273/LOT0599)
4. <a id="src-academy_ktiv_male"></a>Academy of the Hebrew Language (2017). *Kelalei ha-ktiv ha-male (Rules of Full Spelling)*. Ha-Akademya la-Lashon ha-Ivrit, Jerusalem, revised edition, Sivan 5777 / May 2017. [web.archive.org](https://web.archive.org/web/20170807214648/http://hebrew-academy.org.il/wp-content/uploads/Klaley-Ktiv-Male.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `primary_sources` | `he` | gold | expert-human | Apache-2.0 (this repository). Each row quotes and cites a published example. | 33 | 0.1929 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `he` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2872 | 0.3554 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 66 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  | ʔ |
| Affricate |  |  | ts | dʒ tʃ |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x | ʁ χ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [aχ] [ba] [be] [bi] [bo] [bu] [ja] [je] [ji] [jo] [ju] [ka] [ke] [ki] [ko] [ku] [pa] [pe] [pi] [po] [pu] [sa] [se] [si] [so] [su] [va] [ve] [vi] [ʃa] [ʃe] [ʃi] [ʃo] [ʃu] [ʔa] [χa].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨"⟩ | ∅ |  |
| ⟨'⟩ | ∅ |  |
| ⟨ְ⟩ | ∅ [e] |  |
| ⟨ֱ⟩ | [e] |  |
| ⟨ֲ⟩ | [a] |  |
| ⟨ֳ⟩ | [o] |  |
| ⟨ִ⟩ | [i] |  |
| ⟨ִי⟩ | [i] |  |
| ⟨ֵ⟩ | [e] |  |
| ⟨ֵי⟩ | [e] |  |
| ⟨ֶ⟩ | [e] |  |
| ⟨ַ⟩ | [a] |  |
| ⟨ָ⟩ | [a] [o] |  |
| ⟨ֹ⟩ | [o] |  |
| ⟨ֺ⟩ | [o] |  |
| ⟨ֻ⟩ | [u] |  |
| ⟨ּ⟩ | ∅ |  |
| ⟨ֽ⟩ | ∅ |  |
| ⟨־⟩ | ∅ |  |
| ⟨ֿ⟩ | ∅ |  |
| ⟨ׁ⟩ | ∅ |  |
| ⟨ׂ⟩ | ∅ |  |
| ⟨ׇ⟩ | [o] |  |
| ⟨א⟩ | [ʔ] ∅ |  |
| ⟨ב⟩ | [b] [v] | default [v] · intervocalic [v] · word initial [b] |
| ⟨בְּ⟩ | [b] [be] |  |
| ⟨בִּ⟩ | [bi] |  |
| ⟨בֵּ⟩ | [be] |  |
| ⟨בֶּ⟩ | [be] |  |
| ⟨בַּ⟩ | [ba] |  |
| ⟨בָּ⟩ | [ba] |  |
| ⟨בֹּ⟩ | [bo] |  |
| ⟨בֻּ⟩ | [bu] |  |
| ⟨בּ⟩ | [b] |  |
| ⟨ג⟩ | [ɡ] |  |
| ⟨ג'⟩ | [dʒ] |  |
| ⟨גּ⟩ | [ɡ] |  |
| ⟨ג׳⟩ | [dʒ] |  |
| ⟨ד⟩ | [d] |  |
| ⟨דּ⟩ | [d] |  |
| ⟨ה⟩ | [h] ∅ | default [h] · word final ∅ |
| ⟨הּ⟩ | [h] |  |
| ⟨ו⟩ | [v] [o] [u] | default [o] [u] [v] · word initial [v] |
| ⟨וִ⟩ | [vi] |  |
| ⟨וֵ⟩ | [ve] |  |
| ⟨וֶ⟩ | [ve] |  |
| ⟨וַ⟩ | [va] |  |
| ⟨וָ⟩ | [va] |  |
| ⟨וֹ⟩ | [o] |  |
| ⟨וּ⟩ | [u] |  |
| ⟨וו⟩ | [v] |  |
| ⟨ז⟩ | [z] |  |
| ⟨ז'⟩ | [ʒ] |  |
| ⟨ז׳⟩ | [ʒ] |  |
| ⟨ח⟩ | [χ] |  |
| ⟨ט⟩ | [t] |  |
| ⟨י⟩ | [j] [i] | default [i] [j] · word initial [j] |
| ⟨יִ⟩ | [ji] |  |
| ⟨יֵ⟩ | [je] |  |
| ⟨יֶ⟩ | [je] |  |
| ⟨יַ⟩ | [ja] |  |
| ⟨יָ⟩ | [ja] |  |
| ⟨יֹ⟩ | [jo] |  |
| ⟨יֻ⟩ | [ju] |  |
| ⟨יּ⟩ | [j] |  |
| ⟨יי⟩ | [j] |  |
| ⟨ך⟩ | [χ] |  |
| ⟨ךּ⟩ | [k] |  |
| ⟨כ⟩ | [k] [χ] | default [χ] · word initial [k] |
| ⟨כְּ⟩ | [k] [ke] |  |
| ⟨כִּ⟩ | [ki] |  |
| ⟨כֵּ⟩ | [ke] |  |
| ⟨כֶּ⟩ | [ke] |  |
| ⟨כַּ⟩ | [ka] |  |
| ⟨כָּ⟩ | [ka] |  |
| ⟨כֹּ⟩ | [ko] |  |
| ⟨כֻּ⟩ | [ku] |  |
| ⟨כּ⟩ | [k] |  |
| ⟨ל⟩ | [l] |  |
| ⟨ם⟩ | [m] |  |
| ⟨מ⟩ | [m] |  |
| ⟨ן⟩ | [n] |  |
| ⟨נ⟩ | [n] |  |
| ⟨ס⟩ | [s] |  |
| ⟨ע⟩ | [ʔ] ∅ |  |
| ⟨ף⟩ | [f] |  |
| ⟨פ⟩ | [p] [f] | default [f] · word initial [p] |
| ⟨פְּ⟩ | [p] [pe] |  |
| ⟨פִּ⟩ | [pi] |  |
| ⟨פֵּ⟩ | [pe] |  |
| ⟨פֶּ⟩ | [pe] |  |
| ⟨פַּ⟩ | [pa] |  |
| ⟨פָּ⟩ | [pa] |  |
| ⟨פֹּ⟩ | [po] |  |
| ⟨פֻּ⟩ | [pu] |  |
| ⟨פּ⟩ | [p] |  |
| ⟨ץ⟩ | [ts] |  |
| ⟨ץ'⟩ | [tʃ] |  |
| ⟨ץ׳⟩ | [tʃ] |  |
| ⟨צ⟩ | [ts] |  |
| ⟨צ'⟩ | [tʃ] |  |
| ⟨צ׳⟩ | [tʃ] |  |
| ⟨ק⟩ | [k] |  |
| ⟨ר⟩ | [ʁ] [r] |  |
| ⟨ש⟩ | [ʃ] [s] |  |
| ⟨שְׁ⟩ | [ʃ] [ʃe] |  |
| ⟨שְׂ⟩ | [s] [se] |  |
| ⟨שִׁ⟩ | [ʃi] |  |
| ⟨שִׂ⟩ | [si] |  |
| ⟨שֵׁ⟩ | [ʃe] |  |
| ⟨שֵׂ⟩ | [se] |  |
| ⟨שֶׁ⟩ | [ʃe] |  |
| ⟨שֶׂ⟩ | [se] |  |
| ⟨שַׁ⟩ | [ʃa] |  |
| ⟨שַׂ⟩ | [sa] |  |
| ⟨שָׁ⟩ | [ʃa] |  |
| ⟨שָׂ⟩ | [sa] |  |
| ⟨שֹׁ⟩ | [ʃo] |  |
| ⟨שֹׂ⟩ | [so] |  |
| ⟨שֻׁ⟩ | [ʃu] |  |
| ⟨שֻׂ⟩ | [su] |  |
| ⟨שׁ⟩ | [ʃ] |  |
| ⟨שׂ⟩ | [s] |  |
| ⟨ת⟩ | [t] |  |
| ⟨תּ⟩ | [t] |  |
| ⟨׳⟩ | ∅ |  |
| ⟨״⟩ | ∅ |  |

Stress falls on the last syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "he")`. They are engine output, not reference transcriptions.

The next table sets the engine output against worked examples printed in a cited source, from the [primary-source gold](../evaluation/datasets.md#primary-source-gold-primary_sources). The rows are spread evenly over that set. The last column says whether the two transcriptions are the same string.

| Spelling | Printed in the source | Engine output | Source, page | Same |
|:--|:--|:--|:--|:--|
| פַּר | /par/ | [ˈpaʁ] | Laufer 1999, p. 97 | no |
| תָּר | /tar/ | [ˈtaʁ] | Laufer 1999, p. 97 | no |
| גָּר | /gar/ | [ˈɡaʁ] | Laufer 1999, p. 97 | no |
| צַב | /tsav/ | [ˈtsav] | Laufer 1999, p. 97 | no |
| שַׂר | /sar/ | [ˈsaʁ] | Laufer 1999, p. 97 | no |
| גַּל | /gal/ | [ˈɡal] | Laufer 1999, p. 97 | no |
| שָׁר | /ʃar/ | [ˈʃaʁ] | Laufer 1999, p. 97 | no |
| יָם | /jam/ | [ˈjam] | Laufer 1999, p. 97 | no |
| צ׳יפְס | /tʃips/ | [ˈtʃifs] | Laufer 1999, p. 97 | no |
| חִיל | /χil/ | [ˈχil] | Laufer 1999, p. 98 | no |
| חוֹל | /χol/ | [ˈχol] | Laufer 1999, p. 98 | no |
| בֵּרֵךְ | /beˈreχ/ | [beˈʁeχ] | Laufer 1999, p. 98 | no |

Source: Laufer, A. (1999). *Hebrew*. Handbook of the International Phonetic Association: A Guide to the Use of the International Phonetic Alphabet, Cambridge University Press, pp. 96-99 (Illustrations of the IPA, earlier version: Journal of the International Phonetic Association 20(2), 1990, 40-43). [ia801006.us.archive.org](https://ia801006.us.archive.org/6/items/intonation-practice/Handbook_of_the_IPA.pdf)
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Hawaiian](haw.md) · [Home](../index.md) · [Hejazi Arabic →](acw-SA.md)
