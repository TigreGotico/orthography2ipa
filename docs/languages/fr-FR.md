# French (fr-FR): Phonology Reference

**Code**: `fr-FR` | **Family**: Indo-European > Romance > Gallo-Romance | **Script**: Latin (alphabet) | **Quality tier**: research

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

## References

- Fouché, P. (1959). *Traité de prononciation française*. Klincksieck.
- Tranel, B. (1987). *The Sounds of French*. Cambridge University Press.
- Fougeron, C. & Smith, C.L. (1993). Illustrations of the IPA: French. *Journal of the International Phonetic Association*, 23(2), 73-76.
- Tranel, B. (1995). French liaison and elision revisited: A unified account within Optimality Theory. Rutgers Optimality Archive, ROA-15.
- Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
- Divay, M. & Vitale, A.J. (1997). Algorithms for grapheme-phoneme translation for English and French: applications for database searches and speech synthesis. *Computational Linguistics*, 23(4), 495-523.
- Walker, D.C. (2001). *French Sound Structure*. University of Calgary Press.
- Wikipedia: [French phonology](https://en.wikipedia.org/wiki/French_phonology)

---
[← Romanian](ro-RO.md) · [Home](../index.md) · [Italian →](it-IT.md)
