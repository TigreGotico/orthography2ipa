# French (`fr-FR`)

<!-- atlas:summary begin -->
French is a Gallo-Romance language, written in the Latin script. Its code names France. The `fr-FR` spec is at the research tier. It cites 7 sources and has 3 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `fr-FR` |
| Aliases | `fra` |
| ISO 639-3 | [fra](https://iso639-3.sil.org/code/fra), French |
| Glottolog | [stan1290](https://glottolog.org/resource/languoid/id/stan1290), French |
| Wikidata | [Q150](https://www.wikidata.org/wiki/Q150) |
| Wikipedia | [French language](https://en.wikipedia.org/wiki/French_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Gallo-Romance](by-family.md#indo-european--italic--romance--gallo-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [France](by-region.md#france) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Parent | [Gallo-Romance](https://tigregotico.github.io/orthography2ipa/#x-clade-gallorom) `x-clade-gallorom` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`fr-FR` in the data explorer](https://tigregotico.github.io/orthography2ipa/#fr-FR) |
| Spec file | [`fr-FR.json`](../../orthography2ipa/data/fr-FR.json) |
<!-- atlas:header end -->

## Overview

The `fr-FR` spec describes Standard Metropolitan French, as spoken in Paris and the north. That is the variety the WikiPron gold transcribes. The registry resolves the bare tag `fr` to this spec. French has a deep orthography, so the 0.25 PER threshold applies to a promotion (see [quality tiers](../specs/quality_tiers.md#the-per-threshold)).

The sources are Fouché (1959), Tranel (1987), Fougeron & Smith (1993), Tranel (1995), Ladefoged & Maddieson (1996), Divay & Vitale (1997) and Walker (2001).

## Benchmark

The `wikipron` row under the tag `fr` is crowd-scraped, and the `ipadict` row under `fr-FR` is machine-generated. Both can gate a promotion. The `ipa_childes` row is espeak-derived, so it measures agreement with espeak and cannot gate. The scores are on the [scoreboard](../evaluation/generated/scoreboard.md).

## Consonants

### C and G softening

The letter ⟨c⟩ is [s] before ⟨e i y⟩ and [k] elsewhere. The letter ⟨g⟩ is [ʒ] before the same vowels and [ɡ] elsewhere. The letter ⟨ç⟩ is always [s], and ⟨gu⟩ is a grapheme of its own that keeps [ɡ].

| Grapheme | Before ⟨e i y⟩ | Elsewhere | Spec output |
|:---:|:---:|:---:|:---|
| c | s | k | ⟨ceci⟩ `səsi`, ⟨cœur⟩ `kœʁ` |
| g | ʒ | ɡ | ⟨général⟩ `ʒeneʁal`, ⟨gâteau⟩ `ɡɑto` |
| ç | s | s | ⟨ça⟩ `sa` |

### Silent final consonants

Most written word-final consonants are silent when a word stands alone. The spec gives ⟨t d p s x⟩ an empty `word_final` entry in `positional_graphemes`. For ⟨r⟩ the `word_final` entry ranks [ʁ] first and the empty reading second. Monosyllables and loanwords that keep a final consonant, such as ⟨fils⟩ and ⟨bus⟩, are in `word_exceptions`.

Within a word, a single ⟨s⟩ between vowels is [z], so ⟨maison⟩ gives `mɛzɔ̃` and ⟨rose⟩ gives `ʁoz`. The digraph ⟨ss⟩ is always [s], as in ⟨passer⟩ `pase`.

### Doubled consonants

The doubled letters ⟨bb dd ff gg ll mm nn pp rr tt⟩ are graphemes that map to one consonant, the modern French default (Fouché 1959, Tranel 1987). So ⟨Allier⟩ gives `alje`. The grapheme ⟨ill⟩ is longer than ⟨ll⟩, so longest-match tokenisation reads it first. Its default is [ij], as in ⟨fille⟩ `fij`.

A closed set of words keeps ⟨ill⟩ as [il]: ⟨ville⟩, ⟨mille⟩, ⟨tranquille⟩, ⟨tranquillement⟩ and the place name ⟨Lille⟩. These words are in `word_exceptions` (Tranel 1987, §4.3), so ⟨ville⟩ gives `vil`.

### The endings ⟨-er⟩ and ⟨-ez⟩

The word-final ⟨-er⟩ of infinitives and agent nouns is [e], and so is the second-person plural ⟨-ez⟩ (Fouché 1959, Tranel 1987 §3). The spec states both in `grammatical_endings`, not as graphemes. So ⟨parler⟩ gives `paʁle`, ⟨boulanger⟩ gives `bulɑ̃ʒe` and ⟨chez⟩ gives `ʃe`. The same letters inside a word are ordinary graphemes, as in ⟨personne⟩ `pɛʁsɔn` and ⟨version⟩ `vɛʁsjɔ̃`. The ending still matches behind the plural ⟨-s⟩, so ⟨boulangers⟩ gives `bulɑ̃ʒe`.

A closed set of words keeps /ɛʁ/. It holds ⟨mer fer cher ver hier hiver enfer cancer amer super⟩ and the loanwords in ⟨-er⟩, such as ⟨leader⟩ and ⟨poker⟩. These words and their plurals are in `word_exceptions`, which outranks the endings. So ⟨hiver⟩ gives `ivɛʁ`.

### The ambiguous ending ⟨-ent⟩

The third-person plural ⟨-ent⟩ is silent, as in ⟨parlent⟩ [paʁl]. The ⟨-ent⟩ of nouns and adjectives is [ɑ̃], as in ⟨vent⟩, ⟨dent⟩ and ⟨moment⟩. The spelling does not separate the two. The difference is one of part of speech (Fouché 1959, Tranel 1987 §3, Divay & Vitale 1997), and this library takes no part-of-speech input.

The spec therefore declares the ending as a list of candidates, `"ent": [null, ""]`. The `null` in the first place keeps the rank-1 reading from the grapheme tables, a nasal vowel plus a silent ⟨t⟩. So ⟨vent⟩ gives `vɑ̃`, ⟨moment⟩ gives `mɔmɑ̃` and ⟨parlent⟩ gives `paʁlɑ̃`. The silent reading comes second. There `word_candidates`, an oracle@k score or a downstream rescorer that knows the part of speech can reach it. The spec does not declare ⟨-ment⟩ on its own, because it has the same ambiguity: ⟨dorment⟩ is silent and ⟨moment⟩ is not.

### Glide formation

Inside a word, an ⟨i⟩ before another vowel letter becomes the glide [j] through the `before_vowel` entry (Tranel 1987, §5 and §6). So ⟨fiacre⟩ gives `fjakʁ`. The digraphs ⟨y⟩, ⟨ien⟩ and ⟨oui⟩ carry [j] or [w] on their own.

Some learned and prefixed words keep the hiatus [iV] in careful speech and in the WikiPron gold. Examples are compounds in ⟨anti-⟩, ⟨bi-⟩ and ⟨archi-⟩, and nouns such as ⟨lion⟩, ⟨ion⟩ and ⟨chiite⟩. Tranel (1987, §5) describes this variation. The rule glides these words too, so ⟨lion⟩ gives `ljɔ̃`. A finer split needs syllable-count or morpheme-boundary knowledge that the spelling does not hold.

The glide does not apply when the next vowel is the last audible slot of the word. The engine marks that slot with the `before_final_vowel` position. So a word-final unmarked ⟨ie⟩ stays [i]: ⟨vie⟩ gives `vi`, ⟨folie⟩ gives `fɔli` and ⟨Algérie⟩ gives `alʒeʁi`. The plural ⟨vies⟩ also gives `vi`, because the silent suffix ⟨s⟩ does not count as more of the word (Tranel 1987, §3).

## Oral vowels

| Grapheme | IPA | Spec output |
|:---:|:---:|:---|
| a | a | ⟨chat⟩ `ʃa` |
| â | ɑ | ⟨pâte⟩ `pɑt` |
| é | e | ⟨été⟩ `ete` |
| è, ê, ë | ɛ | ⟨mère⟩ `mɛʁ` |
| e, word-final | silent | ⟨Adèle⟩ `adɛl` |
| i, î, ï | i | ⟨île⟩ `il` |
| o, word-final | o | ⟨pot⟩ `po` |
| o, elsewhere | ɔ | ⟨sort⟩ `sɔʁ` |
| ô | o | ⟨côte⟩ `kot` |
| u, û | y | ⟨lune⟩ `lyn` |
| ou | u | ⟨tour⟩ `tuʁ` |
| eu, open syllable | ø | ⟨feu⟩ `fø` |
| eu, closed syllable | œ | ⟨peur⟩ `pœʁ` |

The word-final unstressed ⟨e⟩ (e caduc) is silent by default through the `word_final` entry of ⟨e⟩. This matches the modern elision of the mute e. The monosyllabic function words whose only vowel is that ⟨e⟩ keep their schwa through `word_exceptions`: ⟨le de que ce ne se je me te⟩. So ⟨le⟩ gives `lə`.

### Mid-vowel aperture: the loi de position

The three mid-vowel pairs /e ɛ/, /ø œ/ and /o ɔ/ follow the syllable. The close-mid vowel occurs in an open syllable (syllabe libre, no coda) and the open-mid vowel in a closed one (syllabe entravée). Fougeron & Smith (1993) state the law in these terms. Tranel (1987, ch. 3 and 4) and Walker (2001, ch. 3) give it with its limits.

| Pair | Open syllable | Closed syllable |
|:---|:---|:---|
| /ø œ/ | ⟨heureux⟩ `øʁø`, ⟨jeudi⟩ `ʒødi` | ⟨jeune⟩ `ʒœn`, ⟨heure⟩ `œʁ`, ⟨seule⟩ `sœl` |
| /o ɔ/ | ⟨mot⟩ `mo`, ⟨numéro⟩ `nymeʁo` | ⟨bord⟩ `bɔʁ`, ⟨botte⟩ `bɔt` |
| /e ɛ/ | ⟨été⟩ `ete`, ⟨numéro⟩ `nymeʁo` | ⟨sel⟩ `sɛl`, ⟨Abel⟩ `abɛl` |

The law is about a pronounced coda, but the engine has only letters. So it asks a spelling question instead. It removes the graphemes that this spec declares silent at the end of a word, and then looks at how the syllable ends. Two consequences follow, and a reader must know them before trusting an aperture value.

First, a final syllable whose only vowel letter is a mute ⟨e⟩ has no nucleus. The function `positional.merge_nucleusless_final_syllable` joins it to the syllable before it. So ⟨jeune⟩ becomes one syllable, which ends in ⟨n⟩ and is closed, and it gives `ʒœn`. The same applies to ⟨heure⟩, ⟨veuve⟩ `vœv` and ⟨seule⟩.

Second, the strip then runs a second time on the merged string, on letters that are not final in speech. That is why ⟨meute⟩ gives `møt` and ⟨heureuse⟩ gives `øʁøz`. Both strip back to an open syllable because the spec calls final ⟨t⟩ and ⟨s⟩ silent, yet the /t/ and the /z/ are pronounced. The close-mid vowel is right in both words, but for another reason: /z/ keeps the vowel close (see below).

The proxy fails in two places. An obstruent plus liquid coda does not close the syllable for the law, but the engine treats it as closed: ⟨neutre⟩ gives `nœtʁ` and ⟨feutre⟩ gives `fœtʁ`, where the gold has [ø]. A /z/ spelled ⟨z⟩ cannot be stripped, and the `FR_EU_BEFORE_Z` rule exists for that case.

Two rules state the standard exceptions to the law:

| Rule | Effect | Spec output | Source |
|:---|:---|:---|:---|
| `FR_O_BEFORE_Z`, `FR_EU_BEFORE_Z` | /z/ keeps the vowel close in a closed syllable | ⟨chose⟩ `ʃoz`, ⟨Deleuze⟩ `dəløz` | Fouché 1959, Tranel 1987 §3, Walker 2001 ch. 3 |
| `FR_AU_BEFORE_R` | /ʁ/ opens ⟨au⟩, the one systematic exception to ⟨au⟩ = [o] | ⟨Laure⟩ `lɔʁ`, ⟨aurore⟩ `ɔʁɔʁ`, ⟨dinosaure⟩ `dinozɔʁ` | Fouché 1959, Tranel 1987 ch. 3, Walker 2001 ch. 3 |

The ⟨eu⟩ half of the /z/ rule is needed only where ⟨z⟩ spells the /z/. The common ⟨euse⟩ words, such as ⟨heureuse⟩ and ⟨chanteuse⟩, already reach [ø] through the strip. Learned and foreign spellings resist the ⟨au⟩ rule, so ⟨Saurat⟩ and ⟨vaurien⟩ keep [o] in the gold.

### What the spec does not model

The spec does not read ⟨o⟩ from syllable aperture. Open [o] in every open syllable is the southern French pattern (Walker 2001, ch. 3). Standard French keeps [ɔ] in a non-final open syllable, as in ⟨homophone⟩ `ɔmɔfɔn` and ⟨obole⟩ `ɔbɔl`. So ⟨o⟩ keeps the `FR_O_FINAL_OPEN` and `FR_O_BEFORE_Z` rules. A test of the aperture reading raised the PER on the WikiPron gold.

The spec does not read ⟨e⟩ from syllable aperture either. French ⟨e⟩ is [ɛ] in a syllable that the spelling closes, whether or not the coda is pronounced. So ⟨met⟩ and ⟨mets⟩ both give `mɛ`. The rules `FR_E_CLOSED_CLUSTER` and `FR_E_CLOSED_FINAL` state this from the spelling.

The spec does not open ⟨eu⟩ before /ʁ/, as it opens ⟨au⟩. In an open syllable the quality is lexical: ⟨heureux⟩ and ⟨euro⟩ have [ø], but ⟨fleurette⟩ has [œ]. Walker (2001, ch. 3) says the same of non-final syllables.

## Nasal vowels

| Spelling | IPA | Spec output |
|:---:|:---:|:---|
| an, am, en, em | ɑ̃ | ⟨plan⟩ `plɑ̃`, ⟨temps⟩ `tɑ̃` |
| in, im, ain, ein | ɛ̃ | ⟨vin⟩ `vɛ̃`, ⟨pain⟩ `pɛ̃` |
| on, om | ɔ̃ | ⟨bon⟩ `bɔ̃`, ⟨ombre⟩ `ɔ̃bʁ` |
| un, um | œ̃ | ⟨lundi⟩ `lœ̃di`, ⟨brun⟩ `bʁœ̃` |

Most nasal spellings are not graphemes. The rules `FR_NASAL_a`, `FR_NASAL_ə`, `FR_NASAL_i`, `FR_NASAL_ɔ` and `FR_NASAL_y` nasalise a vowel before a nasal consonant in the coda. Then `FR_NASAL_ABSORB` deletes that coda nasal. The digraphs ⟨ain⟩ and ⟨ein⟩ are graphemes with the value [ɛ̃].

Before a vowel in the same word, the nasal consonant is an onset, so no nasal vowel forms. So ⟨amateur⟩ gives `amatœʁ`, ⟨inutile⟩ gives `inytil` and ⟨unanime⟩ gives `ynanim`. For the nasal graphemes ⟨ain aim ein ien oin⟩, the `FR_NASAL_BLOCK_PREVOCALIC_*` rules remove the nasal vowel before a vowel. The `FR_NASAL_BLOCK_GEMINATE_*` rules remove it before ⟨n m nn mm⟩, so ⟨plaine⟩ gives `plɛn` and ⟨chienne⟩ gives `ʃjɛn`.

Many speakers in and around Paris merge /œ̃/ into /ɛ̃/, so ⟨brun⟩ and ⟨brin⟩ sound the same (Fougeron & Smith 1993). Conservative Standard French keeps the contrast. The spec keeps both values as allophones of `œ̃` and does not reduce the inventory, because Fougeron & Smith still treat /œ̃/ as a phoneme for their reference speaker.

## Liaison and elision

Liaison is a cross-word process. A final consonant that is silent elsewhere is pronounced before a word that starts with a vowel. It is obligatory after a determiner and between a subject pronoun and its verb, as in [le.z‿ami] ⟨les amis⟩ and [nu.z‿avɔ̃] ⟨nous avons⟩. It is blocked after the conjunction ⟨et⟩, before an aspirate-h word, and between a singular noun and its adjective.

Tranel (1995) treats liaison and elision in Optimality Theory, with both driven by ONSET: a syllable prefers an onset consonant. A linking consonant and an eliding vowel are floating segments that surface only when the next syllable gains an onset from them. Aspirate-h words, such as ⟨hibou⟩, start with a vowel but block both liaison and elision. They require the word boundary and the syllable boundary to align at the left edge (ALIGN-LEFT outranks ONSET).

Elision needs no rule. Standard spelling already writes the elided form with an apostrophe, as in ⟨l'homme⟩, so the input carries it.

The spec declares liaison in `sandhi_rules` as `FR_LIAISON_Z`, `FR_LIAISON_T`, `FR_LIAISON_N`, `FR_LIAISON_R`, `FR_LIAISON_P` and `FR_ENCHAÎNEMENT`. These rules match the final IPA of the left word, and the spec has already silenced that consonant. So the liaison rules do not fire, and `transcribe("les amis", "fr-FR")` gives `l ami`.

## Digraphs

| Grapheme | IPA | Spec output |
|:---:|:---:|:---|
| ch | ʃ | ⟨chat⟩ `ʃa` |
| gn | ɲ | ⟨vigne⟩ `viɲ` |
| ph | f | ⟨photo⟩ `fɔto` |
| ill | ij | ⟨fille⟩ `fij` |
| oi | wa | ⟨moi⟩ `mwa` |
| ui | ɥi | ⟨nuit⟩ `nɥi` |
| eu | ø or œ | ⟨feu⟩ `fø`, ⟨peur⟩ `pœʁ` |
| bb, dd, ff, gg, ll, mm, nn, pp, rr, tt | one consonant | ⟨Allier⟩ `alje` |

## Known limitations

| Limitation | Spec output | Cause |
|:---|:---|:---|
| Liaison does not surface | ⟨les amis⟩ `l ami` | The sandhi rules match a final consonant that the spec has already silenced |
| `FR_ENCHAÎNEMENT` deletes the consonant it should link | ⟨des amis⟩ `‿ ami`, ⟨j'aime⟩ `‿ ɛm` | Its `transform` replaces the final voiced consonant with the link mark |
| Plural determiners lose their vowel | ⟨les⟩ `l`, ⟨des⟩ `d`, ⟨mes⟩ `m` | Only the singular function words are in `word_exceptions` |
| Aspirate-h does not block liaison or elision | ⟨le héros⟩ `lə eʁo` | ⟨h⟩ maps to nothing for both mute and aspirate h, and the spec has no aspirate-h word list |
| ⟨e⟩ before a doubled nasal letter reads as schwa | ⟨femme⟩ `fəm`, ⟨ennemi⟩ `ənəmi` | The `FR_NASAL_BLOCK_GEMINATE_*` rules cover only ⟨ain aim ein ien oin⟩ |

Foreign names, such as ⟨Amsterdam⟩, and acronyms that are read letter by letter are lexical exceptions. A grapheme rule cannot encode them.

<!-- atlas:lects begin -->
## Related lects

These specs name `fr-FR` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Seychellois Creole](crs.md) `crs`: Seychelles, research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 7 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-fouche1959"></a>Fouché, P. (1959). *Traité de prononciation française*. Klincksieck.
2. <a id="src-divay_vitale1997"></a>Divay, M. & Vitale, A.J. (1997). *Algorithms for grapheme-phoneme translation for English and French: applications for database searches and speech synthesis*. Computational Linguistics 23(4), 495-523. Cited: 495-523.
3. <a id="src-tranel1987"></a>Tranel, B. (1987). *The Sounds of French*. Cambridge University Press.
4. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
5. <a id="src-fougeron_smith1993"></a>Fougeron, C. & Smith, C.L. (1993). *Illustrations of the IPA: French*. Journal of the International Phonetic Association, 23(2). Cited: 73-76. [cambridge.org](https://www.cambridge.org/core/journals/journal-of-the-international-phonetic-association/article/french/E2BC8B1DD975FE4B272B088B8345B933)
6. <a id="src-tranel1995"></a>Tranel, B. (1995). *French liaison and elision revisited: A unified account within Optimality Theory*. Rutgers Optimality Archive (ROA-15). [roa.rutgers.edu](https://roa.rutgers.edu/files/15-0594/15-0594-TRANEL-0-0.PDF)
7. <a id="src-walker2001"></a>Walker, D.C. (2001). *French Sound Structure*. University of Calgary Press.
<!-- atlas:sources end -->

### Notes on the sources

The page also draws on the Wikipedia article [French phonology](https://en.wikipedia.org/wiki/French_phonology), which the spec does not cite.

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `fr` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 85500 | 0.0667 | yes |
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `fr-FR` | generated | machine-generated | MIT, each file its own | 245718 | 0.0763 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `fr-FR` | generated | espeak-derived | CC BY 4.0 | 9446 | 0.0917 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 75 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  | ʀ |
| Fricative |  | f v | s z | ʃ ʒ |  | ɣ | ʁ χ |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i y |  | u |
| Close-mid | e ø |  | o |
| Mid |  | ə |  |
| Open-mid | œ œ̃ ɛ ɛ̃ |  | ɔ ɔ̃ |
| Near-open | æ̃ |  |  |
| Open | a |  | ɑ ɑ̃ |

Sequences that the spec writes as one unit: [aj] [ej] [ij] [il] [jɛ] [jɛn] [jɛ̃] [ks] [nj] [sjal] [sjɑ̃s] [sjɔ̃] [sjɛl] [sk] [stjɔ̃] [uj] [ul] [w] [wa] [waj] [wi] [wɛ] [wɛn] [wɛ̃] [œj] [œl] [ɛj] [ɛl] [ɛm] [ɛn] [ɡz] [ɥ] [ɥi] [ɥij] [‿].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [ɛ] [e] |  |
| ⟨ail⟩ | [aj] | before vowel [ɛl] · default [aj] · word final [aj] |
| ⟨aill⟩ | [aj] |  |
| ⟨aim⟩ | [ɛ̃] |  |
| ⟨ain⟩ | [ɛ̃] |  |
| ⟨au⟩ | [o] |  |
| ⟨aî⟩ | [ɛ] [e] |  |
| ⟨b⟩ | [b] |  |
| ⟨bb⟩ | [b] |  |
| ⟨c⟩ | [k] [s] | before front vowel [s] · default [k] |
| ⟨cc⟩ | [k] [ks] | before front vowel [ks] · default [k] |
| ⟨ch⟩ | [ʃ] |  |
| ⟨ck⟩ | [k] |  |
| ⟨cqu⟩ | [k] |  |
| ⟨d⟩ | [d] | default [d] · intervocalic cross word [t] · word final ∅ |
| ⟨dd⟩ | [d] |  |
| ⟨e⟩ | [ə] [e] [ɛ] | default [ə] [e] [ɛ] · word final ∅ [ə] |
| ⟨eau⟩ | [o] |  |
| ⟨ei⟩ | [ɛ] |  |
| ⟨eil⟩ | [ɛj] | before vowel [ɛl] · default [ɛj] · word final [ɛj] |
| ⟨eill⟩ | [ɛj] |  |
| ⟨ein⟩ | [ɛ̃] |  |
| ⟨eu⟩ | [ø] [œ] | closed syllable [œ] [ø] · default [ø] [œ] · open syllable [ø] [œ] |
| ⟨euil⟩ | [œj] | before vowel [œl] · default [œj] · word final [œj] |
| ⟨euill⟩ | [œj] |  |
| ⟨eû⟩ | [ø] [œ] |  |
| ⟨f⟩ | [f] |  |
| ⟨ff⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [ʒ] | before front vowel [ʒ] · default [ɡ] |
| ⟨gg⟩ | [ɡ] |  |
| ⟨gn⟩ | [ɲ] |  |
| ⟨gu⟩ | [ɡ] |  |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] | before final vowel [i] · before vowel [j] [i] · default [i] |
| ⟨ien⟩ | [jɛ̃] |  |
| ⟨ill⟩ | [ij] [il] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kk⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨nn⟩ | [n] |  |
| ⟨o⟩ | [ɔ] [o] |  |
| ⟨oi⟩ | [wa] |  |
| ⟨oin⟩ | [wɛ̃] |  |
| ⟨ou⟩ | [u] |  |
| ⟨oui⟩ | [wi] |  |
| ⟨ouil⟩ | [uj] | before vowel [ul] · default [uj] · word final [uj] |
| ⟨ouill⟩ | [uj] |  |
| ⟨oî⟩ | [wa] |  |
| ⟨où⟩ | [u] |  |
| ⟨oû⟩ | [u] |  |
| ⟨p⟩ | [p] | default [p] · word final ∅ |
| ⟨ph⟩ | [f] |  |
| ⟨pp⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [k] |  |
| ⟨r⟩ | [ʁ] | default [ʁ] · word final [ʁ] ∅ |
| ⟨rr⟩ | [ʁ] |  |
| ⟨s⟩ | [s] [z] | default [s] · intervocalic [z] · intervocalic cross word [z] · word final ∅ |
| ⟨sc⟩ | [sk] [s] | before front vowel [s] · default [sk] |
| ⟨sch⟩ | [ʃ] |  |
| ⟨ss⟩ | [s] |  |
| ⟨t⟩ | [t] | default [t] · word final ∅ |
| ⟨th⟩ | [t] |  |
| ⟨tt⟩ | [t] |  |
| ⟨u⟩ | [y] |  |
| ⟨ueil⟩ | [œj] | before vowel [œl] · default [œj] · word final [œj] |
| ⟨ueill⟩ | [œj] |  |
| ⟨ui⟩ | [ɥi] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] [v] |  |
| ⟨x⟩ | [ks] [ɡz] | default [ks] · intervocalic cross word [z] · word final ∅ |
| ⟨y⟩ | [i] [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨à⟩ | [a] |  |
| ⟨â⟩ | [ɑ] |  |
| ⟨æ⟩ | [e] |  |
| ⟨ç⟩ | [s] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [e] |  |
| ⟨ê⟩ | [ɛ] |  |
| ⟨ë⟩ | [ɛ] |  |
| ⟨î⟩ | [i] |  |
| ⟨ï⟩ | [i] |  |
| ⟨ô⟩ | [o] |  |
| ⟨ù⟩ | [y] |  |
| ⟨û⟩ | [y] |  |
| ⟨ü⟩ | [y] |  |
| ⟨ÿ⟩ | [i] |  |
| ⟨œ⟩ | [e] [ø] |  |
| ⟨œil⟩ | [œj] |  |
| ⟨œill⟩ | [œj] |  |
| ⟨œu⟩ | [ø] [œ] | closed syllable [œ] [ø] · default [ø] [œ] · open syllable [ø] [œ] |

The spec declares no stress rule.

Whole-word exceptions (121): ⟨affenpinscher⟩ [afənpinʃəʁ], ⟨afrikander⟩ [afʁikɑ̃dɛʁ], ⟨afrikaner⟩ [afʁikanɛʁ], ⟨amer⟩ [amɛʁ], ⟨amers⟩ [amɛʁ], ⟨angledozer⟩ [ɑ̃ɡlədozœʁ], ⟨aster⟩ [astɛʁ], ⟨atlas⟩ [atlas], ⟨autobus⟩ [otobys], ⟨blazer⟩ [blazœʁ], ⟨bloomer⟩ [blumœʁ], ⟨boomer⟩ [bumœʁ], ⟨bus⟩ [bys], ⟨bécher⟩ [beʃɛʁ], ⟨cactus⟩ [kaktys], ⟨campus⟩ [kɑ̃pys], ⟨cancer⟩ [kɑ̃sɛʁ], ⟨cancers⟩ [kɑ̃sɛʁ], ⟨casher⟩ [kaʃɛʁ], ⟨cathéter⟩ [katetɛʁ], ⟨ce⟩ [sə], ⟨charter⟩ [ʃaʁtɛʁ], ⟨cher⟩ [ʃɛʁ], ⟨chers⟩ [ʃɛʁ], ⟨container⟩ [kɔ̃tɛnɛʁ], ⟨containers⟩ [kɔ̃tɛnɛʁ], ⟨cover⟩ [kɔvœʁ], ⟨cracker⟩ [kʁakœʁ], ⟨crackers⟩ [kʁakœʁ], ⟨cuiller⟩ [kɥijɛʁ], and 91 more in the spec file.

Grammatical endings: ⟨-ent⟩ ∅ ∅, ⟨-er⟩ [e], ⟨-ez⟩ [e], ⟨-stion⟩ [stjɔ̃], ⟨-tial⟩ [sjal], ⟨-tiel⟩ [sjɛl], ⟨-tience⟩ [sjɑ̃s], ⟨-tion⟩ [sjɔ̃].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 25 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `FR_NASAL_BLOCK_PREVOCALIC_AIN` | /ɛ̃/ → [ɛn], before a vowel, spelled ⟨ain⟩ | - | [Fouché 1959](#src-fouche1959), [Tranel 1987](#src-tranel1987), [Walker 2001](#src-walker2001) |
| `FR_NASAL_BLOCK_GEMINATE_AIN` | /ɛ̃/ → [ɛ], spelled ⟨ain⟩, before ⟨n⟩ ⟨m⟩ ⟨nn⟩ ⟨mm⟩ | - | [Fouché 1959](#src-fouche1959), [Tranel 1987](#src-tranel1987), [Walker 2001](#src-walker2001) |
| `FR_NASAL_BLOCK_PREVOCALIC_AIM` | /ɛ̃/ → [ɛm], before a vowel, spelled ⟨aim⟩ | - | [Fouché 1959](#src-fouche1959), [Tranel 1987](#src-tranel1987), [Walker 2001](#src-walker2001) |
| `FR_NASAL_BLOCK_GEMINATE_AIM` | /ɛ̃/ → [ɛ], spelled ⟨aim⟩, before ⟨n⟩ ⟨m⟩ ⟨nn⟩ ⟨mm⟩ | - | [Fouché 1959](#src-fouche1959), [Tranel 1987](#src-tranel1987), [Walker 2001](#src-walker2001) |
| `FR_NASAL_BLOCK_PREVOCALIC_EIN` | /ɛ̃/ → [ɛn], before a vowel, spelled ⟨ein⟩ | - | [Fouché 1959](#src-fouche1959), [Tranel 1987](#src-tranel1987), [Walker 2001](#src-walker2001) |
| `FR_NASAL_BLOCK_GEMINATE_EIN` | /ɛ̃/ → [ɛ], spelled ⟨ein⟩, before ⟨n⟩ ⟨m⟩ ⟨nn⟩ ⟨mm⟩ | - | [Fouché 1959](#src-fouche1959), [Tranel 1987](#src-tranel1987), [Walker 2001](#src-walker2001) |
| `FR_NASAL_BLOCK_PREVOCALIC_IEN` | /jɛ̃/ → [jɛn], before a vowel, spelled ⟨ien⟩ | - | [Fouché 1959](#src-fouche1959), [Tranel 1987](#src-tranel1987), [Walker 2001](#src-walker2001) |
| `FR_NASAL_BLOCK_GEMINATE_IEN` | /jɛ̃/ → [jɛ], spelled ⟨ien⟩, before ⟨n⟩ ⟨m⟩ ⟨nn⟩ ⟨mm⟩ | - | [Fouché 1959](#src-fouche1959), [Tranel 1987](#src-tranel1987), [Walker 2001](#src-walker2001) |
| `FR_NASAL_BLOCK_PREVOCALIC_OIN` | /wɛ̃/ → [wɛn], before a vowel, spelled ⟨oin⟩ | - | [Fouché 1959](#src-fouche1959), [Tranel 1987](#src-tranel1987), [Walker 2001](#src-walker2001) |
| `FR_NASAL_BLOCK_GEMINATE_OIN` | /wɛ̃/ → [wɛ], spelled ⟨oin⟩, before ⟨n⟩ ⟨m⟩ ⟨nn⟩ ⟨mm⟩ | - | [Fouché 1959](#src-fouche1959), [Tranel 1987](#src-tranel1987), [Walker 2001](#src-walker2001) |
| `FR_NASAL_a` | /a/ → [ɑ̃], before a coda nasal | - | - |
| `FR_NASAL_ə` | /ə/ → [ɑ̃], before a coda nasal | - | - |
| `FR_NASAL_i` | /i/ → [ɛ̃], before a coda nasal | - | - |
| `FR_NASAL_ɔ` | /ɔ/ → [ɔ̃], before a coda nasal | - | - |
| `FR_NASAL_y` | /y/ → [œ̃], before a coda nasal | - | - |
| `FR_NASAL_ABSORB` | /n m/ → ∅, in the coda, after a vowel | - | - |
| `FR_E_CLOSED_MULTIGRAPH` | /ə/ → [ɛ], before a consonant cluster, spelled ⟨e⟩ | ⟨Abel⟩ [abɛl] | [Tranel 1987](#src-tranel1987), [Walker 2001](#src-walker2001) |
| `FR_E_CLOSED_CLUSTER` | /ə/ → [ɛ], before a consonant, spelled ⟨e⟩, with more context in the spec | ⟨Abel⟩ [abɛl] | [Tranel 1987](#src-tranel1987) |
| `FR_E_CLOSED_FINAL` | /ə/ → [ɛ], before a consonant, spelled ⟨e⟩, with more context in the spec | ⟨Abel⟩ [abɛl] | [Tranel 1987](#src-tranel1987) |
| `FR_O_FINAL_OPEN` | /ɔ/ → [o], word-finally, spelled ⟨o⟩ | ⟨mot⟩ [mo] | [Tranel 1987](#src-tranel1987) |
| `FR_O_BEFORE_Z` | /ɔ/ → [o], before [z], spelled ⟨o⟩ | ⟨mot⟩ [mo] | [Tranel 1987](#src-tranel1987) |
| `FR_AU_BEFORE_R` | /o/ → [ɔ], before [ʁ], spelled ⟨au⟩ | ⟨Laure⟩ [lɔʁ] | [Fouché 1959](#src-fouche1959), [Tranel 1987](#src-tranel1987), [Walker 2001](#src-walker2001) |
| `FR_EU_BEFORE_Z` | /œ/ → [ø], before [z], spelled ⟨eu⟩ | ⟨Deleuze⟩ [dəløz] | [Fouché 1959](#src-fouche1959), [Tranel 1987](#src-tranel1987), [Walker 2001](#src-walker2001) |
| `FR_C_HARD_BEFORE_OEU` | /s/ → [k], spelled ⟨c⟩, before ⟨œu⟩ | ⟨cœur⟩ [kœʁ] | - |
| `FR_AI_FINAL_CLOSE_MID` | /ɛ/ → [e], before a word boundary, spelled ⟨ai⟩ | ⟨j'ai⟩ [ʒe] | [Fouché 1959](#src-fouche1959), [Walker 2001](#src-walker2001) |

The spec applies 6 rules across a word boundary. The contexts are regular expressions on the IPA of the two words.

| Rule | End of word | Start of next word | Change | Example | Cited |
|:--|:--|:--|:--|:--|:--|
| `FR_LIAISON_Z` | `z$` | `^[aeiouɛɔɑãɛ̃ɔ̃œ̃]` | left [z‿] | - | - |
| `FR_LIAISON_T` | `t$` | `^[aeiouɛɔɑãɛ̃ɔ̃œ̃]` | left [t‿] | - | - |
| `FR_LIAISON_N` | `n$` | `^[aeiouɛɔɑãɛ̃ɔ̃œ̃]` | left [n‿] | - | - |
| `FR_LIAISON_R` | `ʁ$` | `^[aeiouɛɔɑãɛ̃ɔ̃œ̃]` | left [ʁ‿] | - | - |
| `FR_LIAISON_P` | `p$` | `^[aeiouɛɔɑãɛ̃ɔ̃œ̃]` | left [p‿] | - | - |
| `FR_ENCHAÎNEMENT` | `[bdgvzʒ]$` | `^[aeiouɛɔɑãɛ̃ɔ̃œ̃]` | left [‿] | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="Abel|Algérie|amateur|bon|botte|boulanger|brun|chienne|Deleuze|dinosaure|été|parlent|ennemi|cœur" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "fr-FR")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| Abel | [abɛl] |
| Algérie | [alʒeʁi] |
| amateur | [amatœʁ] |
| bon | [bɔ̃] |
| botte | [bɔt] |
| boulanger | [bulɑ̃ʒe] |
| brun | [bʁœ̃] |
| chienne | [ʃjɛn] |
| Deleuze | [dəløz] |
| dinosaure | [dinozɔʁ] |
| été | [ete] |
| parlent | [paʁlɑ̃] |
| ennemi | [ənəmi] |
| cœur | [kœʁ] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Franco-Provençal](frp.md) · [Home](../index.md) · [Friulian →](fur.md)
