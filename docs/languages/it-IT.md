# Italian (`it-IT`)

<!-- atlas:summary begin -->
Italian is an Italo-Romance language, written in the Latin script. Its code names Italy. The `it-IT` spec is at the research tier. It cites 7 sources and has 3 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `it-IT` |
| Aliases | `ita` |
| ISO 639-3 | [ita](https://iso639-3.sil.org/code/ita), Italian |
| Glottolog | [ital1282](https://glottolog.org/resource/languoid/id/ital1282), Italian |
| Wikidata | [Q652](https://www.wikidata.org/wiki/Q652) |
| Wikipedia | [Italian language](https://en.wikipedia.org/wiki/Italian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Italo-Romance](by-family.md#indo-european--italic--romance--italo-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Italy](by-region.md#italy) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Parent | [Italo-Romance](https://tigregotico.github.io/orthography2ipa/#x-clade-italorom) `x-clade-italorom` |
| Child lects | 4, see [Related lects](#related-lects) |
| Explorer | [`it-IT` in the data explorer](https://tigregotico.github.io/orthography2ipa/#it-IT) |
| Spec file | [`it-IT.json`](../../orthography2ipa/data/it-IT.json) |
<!-- atlas:header end -->

## Overview

The `it-IT` spec describes Standard Italian, which rests on Florentine and Tuscan usage. Where the regional varieties disagree, it writes the Standard Northern value. The sources are Lepschy & Lepschy (1988), Maiden (1995), Rogers & d'Arcangeli (2004), Bertinetto & Loporcaro (2005), Krämer (2009) and Canepari (2009).

## C and G softening

The letters ⟨c⟩ and ⟨g⟩ are [tʃ] and [dʒ] before ⟨e⟩ and ⟨i⟩, and [k] and [ɡ] elsewhere. The digraphs ⟨ch⟩ and ⟨gh⟩ always keep the stop. The spec states the softening as `before_e` and `before_i` entries in `positional_graphemes`.

| Grapheme | Before ⟨e i⟩ | Elsewhere | Spec output |
|:---:|:---:|:---:|:---|
| c | tʃ | k | ⟨cena⟩ `ˈtʃena`, ⟨cosa⟩ `ˈkoza` |
| g | dʒ | ɡ | ⟨gente⟩ `ˈdʒente`, ⟨gatto⟩ `ˈɡatːo` |
| ch | k | k | ⟨chiaro⟩ `ˈkjaro` |
| sc | ʃ | sk | ⟨scena⟩ `ˈʃena`, ⟨scala⟩ `ˈskala` |

The ⟨i⟩ of ⟨ci⟩, ⟨gi⟩ and ⟨sci⟩ before another vowel is a spelling marker and has no sound of its own. The spec declares these sequences as graphemes with a `before_vowel` entry, so ⟨cielo⟩ gives `ˈtʃelo` and not a form with [i]. The doubled ⟨cc⟩ and ⟨gg⟩ take the value that the next vowel selects, as in ⟨leggo⟩ `ˈleɡːo` and ⟨legge⟩ `ˈledːʒe`. Only the stop part of the geminate affricate is long (Krämer 2009, §2.2 and §7.1). The sequences ⟨cci⟩ and ⟨ggi⟩ mute the ⟨i⟩ in the same way: ⟨faccia⟩ gives `ˈfatːʃa` and ⟨maggio⟩ gives `ˈmadːʒo`.

The digraph ⟨gu⟩ before a vowel is /ɡw/, the voiced partner of ⟨qu⟩. So ⟨guerra⟩ gives `ˈɡwerːa`. Before a consonant the ⟨u⟩ is an ordinary vowel, as in ⟨gustare⟩.

## GL and the palatal lateral

The digraph ⟨gl⟩ is [ʎ] before ⟨i⟩ and [ɡl] elsewhere. The spec gives ⟨figlio⟩ as `ˈfiʎʎo` and ⟨glottale⟩ as `ɡloˈtːale`. The palatal lateral is long between vowels, and the rule `IT_INHERENT_GEMINATE_GLI` writes it twice. The rules `IT_INHERENT_GEMINATE_GN`, `IT_INHERENT_GEMINATE_SC`, `IT_INHERENT_GEMINATE_TS` and `IT_INHERENT_GEMINATE_DZ` do the same for ⟨gn⟩, ⟨sc⟩ and ⟨z⟩.

## S and Z

A single ⟨s⟩ is [s] at the start of a word and [z] between vowels, as in ⟨casa⟩ `ˈkaza`. Intervocalic voicing is the northern and central norm, and southern varieties keep [s]. Before a consonant, Italian has no voicing contrast. The rule `IT_S_VOICING_BEFORE_VOICED_C` gives [z] before every voiced consonant, so ⟨svelto⟩ gives `ˈzvelto`. Before a voiceless consonant ⟨s⟩ stays [s], as in ⟨pasta⟩ (Bertinetto & Loporcaro 2005, Krämer 2009 §5.3).

The letter ⟨z⟩ is [dz] at the start of a word, so ⟨zero⟩ gives `ˈdzero`. After a consonant the spec ranks [ts] first and [dz] second, so ⟨marzo⟩ gives `ˈmartso`. Between vowels the default [ts] becomes long through `IT_INHERENT_GEMINATE_TS`: ⟨nazione⟩ gives `natˈtsjone`. The doubled ⟨zz⟩ is [tːs] first and [dːz] second, so ⟨pizza⟩ gives `ˈpitːsa`.

## Geminate consonants

Italian contrasts short and long consonants. The spec maps every doubled letter to a long consonant with the length mark ⟨ː⟩.

| Short | Long | Gloss |
|:---|:---|:---|
| ⟨fato⟩ `ˈfato` | ⟨fatto⟩ `ˈfatːo` | fate, done |
| ⟨caro⟩ `ˈkaro` | ⟨carro⟩ `ˈkarːo` | dear, cart |
| ⟨pala⟩ `ˈpala` | ⟨palla⟩ `ˈpalːa` | shovel, ball |

Raddoppiamento fonosintattico lengthens a consonant across a word boundary. It belongs to the sandhi layer, and the spec does not model it.

## Vowels

Italian has seven stressed vowels, /a e ɛ i o ɔ u/. In unstressed syllables the open-mid /ɛ ɔ/ do not occur, which leaves five vowels. In the reference grammars, a stressed vowel is long in an open syllable and short in a closed one, as in [ˈpaːdre] and [ˈfɔrte].

The spec writes only ⟨e⟩ /e/ and ⟨o⟩ /o/ for the mid vowels, and it does not write vowel length. The choice between the close-mid and the open-mid vowel depends on the word and its history, and the spelling does not mark it. So ⟨bello⟩ gives `ˈbelːo` and ⟨forte⟩ gives `ˈforte`.

The sequences ⟨ia ie io iu⟩ and ⟨ua ue uo⟩ are glide plus vowel. The spec gives ⟨pianta⟩ as `ˈpjanta`, ⟨buono⟩ as `ˈbwono` and ⟨quando⟩ as `ˈkwando`.

## Stress

The `stress` block puts stress on the penultimate syllable by default. A written accent (⟨à è é ì ò ó ù⟩) always marks the stressed vowel and overrides the default. Antepenultimate stress, as in ⟨tavola⟩, is lexical. Standard spelling does not require an accent on it, so the spec cannot predict it.

## Known limitations

The spec cannot recover these contrasts from the spelling, and a downstream lexicon must supply them:

| Contrast | Example |
|:---|:---|
| Close-mid against open-mid vowels | ⟨bello⟩ has [ɛ], the spec writes `e` |
| [ts] against [dz] for ⟨z⟩ and ⟨zz⟩ | ⟨azzurro⟩ [addzurro] against ⟨pizza⟩ [pittsa] |
| Glide against hiatus for ⟨i u⟩ before a vowel | ⟨Adriana⟩ [adriana] against ⟨piano⟩ [pjano] |
| Antepenultimate stress | ⟨tavola⟩ |
| Tuscan [s] against Northern [z] between vowels | ⟨casa⟩ |

The spec `notes` give the share of the remaining error that each contrast causes on the WikiPron gold. The scores are on the [scoreboard](../evaluation/generated/scoreboard.md).

<!-- atlas:lects begin -->
## Related lects

These specs name `it-IT` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Marchigiano](it-IT-x-marche.md) `it-IT-x-marche`: Italy, research tier
- [Romanesco](it-IT-x-roma.md) `it-IT-x-roma`: Italy, research tier
- [Tuscan](it-IT-x-toscana.md) `it-IT-x-toscana`: Italy, research tier
- [Umbrian dialect](it-IT-x-umbria.md) `it-IT-x-umbria`: Italy, research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 7 works. 1 of them have a DOI or a URL. The spec file holds a note on what 4 of them support.

1. <a id="src-lepschy_lepschy1988"></a>Lepschy, A.L. & Lepschy, G. (1988). *The Italian Language Today*. Hutchinson.
2. <a id="src-rogers_derosa2004"></a>Rogers, D. & d'Arcangeli, L. (2004). *Italian*. Journal of the International Phonetic Association. Cited: 117-121.
3. <a id="src-maiden_parry1997"></a>Maiden, M. & Parry, M. (eds.) (1997). *The Dialects of Italy*. Routledge.
4. <a id="src-kramer2009"></a>Krämer, M. (2009). *The Phonology of Italian*. Oxford University Press.
5. <a id="src-bertinetto_loporcaro2005"></a>Bertinetto, P.M. & Loporcaro, M. (2005). *The sound pattern of Standard Italian, as compared with the varieties spoken in Florence, Milan and Rome*. Journal of the International Phonetic Association. Cited: 131-151.
6. <a id="src-canepari2009"></a>Canepari, L. (2009). *Dizionario di pronuncia italiana (DiPI)*. Zanichelli.
7. <a id="src-romito2010"></a>Romito, L. (2010). *Elisione*. Enciclopedia dell'Italiano, Istituto della Enciclopedia Italiana Treccani. [treccani.it](https://www.treccani.it/enciclopedia/elisione_(Enciclopedia-dell'Italiano)/)
<!-- atlas:sources end -->

### Notes on the sources

The page also draws on two works that the spec does not cite:

- Maiden, M. (1995). *A Linguistic History of Italian*. Longman.
- Wikipedia: [Italian phonology](https://en.wikipedia.org/wiki/Italian_phonology)

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `it` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 82276 | 0.0441 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `it-IT` | generated | espeak-derived | CC BY 4.0 | 4583 | 0.2341 | no |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `it` | generated | epitran-derived | CC0 1.0 | 48570 | 0.1031 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 80 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bː p pː |  | d dː d̪ t tː t̪ |  |  | k kː ɡ ɡː |
| Affricate |  |  | dz dːz ts tːs | dʒ dːʒ tʃ tːʃ |  |  |
| Nasal | m mː | ɱ | n nː |  | ɲ | ŋ |
| Trill |  |  | r rː |  |  |  |
| Tap |  |  | ɾ |  |  |  |
| Fricative |  | f fː v | s sː z | ʃ |  |  |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l lː |  | ʎ |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [aj] [aw] [ddz] [dʒi] [dːʒi] [ej] [ew] [ja] [je] [jo] [ju] [ks] [kw] [oj] [sk] [tts] [tʃi] [tːʃi] [uj] [w] [wa] [we] [wo] [ɡl] [ɡw] [ɲɲ] [ʃi] [ʃʃ] [ʎi] [ʎʎ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [aj] |  |
| ⟨au⟩ | [aw] |  |
| ⟨b⟩ | [b] |  |
| ⟨bb⟩ | [bː] |  |
| ⟨c⟩ | [k] [tʃ] | before e [tʃ] · before i [tʃ] · default [k] |
| ⟨cc⟩ | [kː] [tːʃ] | before e [tːʃ] · before i [tːʃ] · default [kː] |
| ⟨cci⟩ | [tːʃ] [tːʃi] | before vowel [tːʃ] · default [tːʃi] |
| ⟨ch⟩ | [k] |  |
| ⟨ci⟩ | [tʃ] [tʃi] | before vowel [tʃ] · default [tʃi] |
| ⟨d⟩ | [d] |  |
| ⟨dd⟩ | [dː] |  |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨ei⟩ | [ej] |  |
| ⟨eu⟩ | [ew] |  |
| ⟨f⟩ | [f] |  |
| ⟨ff⟩ | [fː] |  |
| ⟨g⟩ | [ɡ] [dʒ] | before e [dʒ] · before i [dʒ] · default [ɡ] |
| ⟨gg⟩ | [ɡː] [dːʒ] | before e [dːʒ] · before i [dːʒ] · default [ɡː] |
| ⟨ggi⟩ | [dːʒ] [dːʒi] | before vowel [dːʒ] · default [dːʒi] |
| ⟨gh⟩ | [ɡ] |  |
| ⟨gi⟩ | [dʒ] [dʒi] | before vowel [dʒ] · default [dʒi] |
| ⟨gl⟩ | [ʎ] [ɡl] | before i [ʎ] · default [ɡl] |
| ⟨gli⟩ | [ʎ] [ʎi] | before vowel [ʎ] · default [ʎi] |
| ⟨gn⟩ | [ɲ] |  |
| ⟨gu⟩ | [ɡw] | before vowel [ɡw] |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨ia⟩ | [ja] |  |
| ⟨ie⟩ | [je] |  |
| ⟨io⟩ | [jo] |  |
| ⟨iu⟩ | [ju] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [lː] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [mː] |  |
| ⟨n⟩ | [n] |  |
| ⟨nn⟩ | [nː] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨oi⟩ | [oj] |  |
| ⟨p⟩ | [p] |  |
| ⟨pp⟩ | [pː] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [r] |  |
| ⟨rr⟩ | [rː] |  |
| ⟨s⟩ | [s] [z] | default [s] · intervocalic [z] · word initial [s] |
| ⟨sc⟩ | [ʃ] [sk] | before e [ʃ] · before i [ʃ] · default [sk] |
| ⟨sci⟩ | [ʃ] [ʃi] | before vowel [ʃ] · default [ʃi] |
| ⟨ss⟩ | [sː] |  |
| ⟨t⟩ | [t] |  |
| ⟨tt⟩ | [tː] |  |
| ⟨u⟩ | [u] |  |
| ⟨ua⟩ | [wa] |  |
| ⟨ue⟩ | [we] |  |
| ⟨ui⟩ | [uj] |  |
| ⟨uo⟩ | [wo] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [v] [w] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [i] [j] |  |
| ⟨z⟩ | [ts] [dz] | after consonant [ts] [dz] · default [ts] · word initial [dz] |
| ⟨zz⟩ | [tːs] [dːz] |  |
| ⟨à⟩ | [a] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [e] |  |
| ⟨ì⟩ | [i] |  |
| ⟨ò⟩ | [ɔ] |  |
| ⟨ó⟩ | [o] |  |
| ⟨ù⟩ | [u] |  |

Stress falls on the penult by default. A written ⟨à⟩ ⟨è⟩ ⟨é⟩ ⟨ì⟩ ⟨ò⟩ ⟨ó⟩ ⟨ù⟩ marks the stressed vowel.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 6 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `IT_INHERENT_GEMINATE_GN` | /ɲ/ → [ɲɲ], after a vowel, before a vowel | ⟨bagno⟩ [baɲɲo] | [Krämer 2009](#src-kramer2009) |
| `IT_INHERENT_GEMINATE_GLI` | /ʎ/ → [ʎʎ], after a vowel, before a vowel | ⟨aglio⟩ [aʎʎo] | [Krämer 2009](#src-kramer2009) |
| `IT_INHERENT_GEMINATE_SC` | /ʃ/ → [ʃʃ], after a vowel, before a vowel | ⟨pesce⟩ [peʃʃe] | [Krämer 2009](#src-kramer2009) |
| `IT_INHERENT_GEMINATE_TS` | /ts/ → [tts], after a vowel, before a vowel | ⟨vizio⟩ [vittsjo] | [Krämer 2009](#src-kramer2009) |
| `IT_INHERENT_GEMINATE_DZ` | /dz/ → [ddz], after a vowel, before a vowel | - | [Krämer 2009](#src-kramer2009) |
| `IT_S_VOICING_BEFORE_VOICED_C` | /s/ → [z], before [b] [d] [ɡ] [v] [m] [n] [ɲ] [l] and 4 more | ⟨sbagliare⟩ [zbaʎʎare] | [Krämer 2009](#src-kramer2009), [Bertinetto 2005](#src-bertinetto_loporcaro2005) |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="azzurro|pizza|Adriana|piano|bello|buono|cielo|figlio|gente|guerra|legge|nazione|scena|svelto" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "it-IT")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| azzurro | [aˈtːsurːo] |
| pizza | [ˈpitːsa] |
| Adriana | [aˈdrjana] |
| piano | [ˈpjano] |
| bello | [ˈbelːo] |
| buono | [ˈbwono] |
| cielo | [ˈtʃelo] |
| figlio | [ˈfiʎʎo] |
| gente | [ˈdʒente] |
| guerra | [ˈɡwerːa] |
| legge | [ˈledːʒe] |
| nazione | [natˈtsjone] |
| scena | [ˈʃena] |
| svelto | [ˈzvelto] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Isthmus-Mecayapan Nahuatl](nhx.md) · [Home](../index.md) · [Itelmen →](itl.md)
