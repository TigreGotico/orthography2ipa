# Regional Standard Dutch of the Netherlands (nl-NL-x-*)

The `nl-NL-x-*` specs model the regional and social accents of Standard Dutch in the Netherlands. A regional spec describes the standard language as educated speakers from one region speak it. Polder Dutch (`nl-NL-x-polder`) is a sociolect, not a region: it describes the standard language of a social group. The specs do not describe the traditional dialects, which have specs of their own, such as `li` for Limburgish and `gos` for Gronings. Each spec is a delta spec over `nl-NL`: it inherits the whole standard and declares only what its region or group changes. This page first explains how the inheritance works. One table then compares the defining features of every regional spec. Each spec then has its own section, with its sources, its rules and their conditions, and its known gaps.

Every transcription on this page is real output of `orthography2ipa.transcribe(text, code)`.

## How the regional specs inherit from nl-NL

Every spec on this page sets `parent` to `nl-NL`. It also sets the four base keys `graphemes_base`, `allophones_base`, `positional_graphemes_base` and `word_exceptions_base` to `nl-NL`. So each regional spec starts from the full standard. It gets the open-syllable vowel length, the final devoicing, the stress block, the allophone rules and the word exceptions of `nl-NL`. The engine does not inherit `collapse_geminates`, so each spec sets it to `true` again, as `nl-NL` does.

The dictionary fields `graphemes`, `allophones`, `positional_graphemes` and `word_exceptions` merge key by key. An own entry replaces the `nl-NL` entry with the same key, and every other key is inherited. In `positional_graphemes` the key is the grapheme. So an own map for ⟨g⟩ replaces the whole ⟨g⟩ map of `nl-NL`, and the spec must state every position it needs.

A spec states a value itself when `nl-NL` could change that value later. The Limburg spec gives ⟨g⟩ and ⟨sch⟩ the velar [x] and ⟨v⟩ the voiced [v] in its own positional maps, and ⟨ch⟩ the velar [x] in its own `graphemes` map. So a change to the dorsal fricative or to the initial ⟨v⟩ of `nl-NL` does not reach Limburg through the inheritance. A word exception bypasses the grapheme map and the allophone rules. So the Limburg spec also restates the `nl-NL` exception `tjerkgaast` with the velar [x]. The `nl-NL` keys ⟨berg⟩ and ⟨kerk⟩ and the exceptions `tietjerk`, `tjerkgaast` and `tjerkwerd` write the coda approximant [ɹ] in their own values. A child that switches the approximant rule off still inherits those values, so the Limburg spec restates them with [r]. The Groningen spec states its voiceless initial ⟨v⟩ in the same way. The Polder spec gives its eight diphthong graphemes their values in its own `graphemes` map for the same reason.

The rule list `allophone_rules` merges by id (see [../engine/allophony.md](../engine/allophony.md#inheritance)). The `nl-NL` rules keep their order. An own rule with the same id replaces the inherited rule in place. An own rule with a new id goes to the end of the list.

The data for the Limburg and Groningen specs come from the teacher corpus of Van Hout et al. (1999). It holds 160 teachers of Dutch from four regions of the Netherlands and four regions of Flanders. The teachers read word lists and carrier sentences. van der Harst (2011, p. 53) states the reason for the choice: teachers "are professional language users who are assumed to speak the standard language on a daily basis". The Netherlands regions are the Randstad, the Middle (south Gelderland), the North (Groningen and north Drenthe) and the South (Dutch Limburg).

## Defining features

| Spec | Region or group | Features that set it apart from `nl-NL` | Example |
|:---|:---|:---|:---|
| [`nl-NL-x-limburg`](#limburg-nl-nl-x-limburg) | Dutch Limburg: Sittard, Geleen, Roermond | /ɣ/ as the voiceless velar [x], the soft g<br>⟨ch⟩ as the same velar [x]<br>word-initial ⟨v⟩ stays [v]<br>coda /r/ as the consonantal [r] | `guize` [ˈxœyzə], `lachen` [ˈlaːxən], `vier` [ˈviːr], `door` [ˈdoᵊr] |
| [`nl-NL-x-groninge`](#groningen-nl-nl-x-groninge) | Groningen and north Drenthe: Assen, Veendam, Winschoten | word-initial ⟨v⟩ as [f] | `vier` [ˈfiːɹ], `vader` [ˈfaːdəɹ] |
| [`nl-NL-x-polder`](#polder-dutch-nl-nl-x-polder) | A sociolect, not a region: younger women in public speech | ⟨ei ij⟩ as [aːi]<br>⟨ui⟩ as [ɑy]<br>⟨ou au⟩ as [aːu] | `tijd` [ˈtaːit], `huis` [ˈɦɑys], `vrouw` [ˈvraːu] |

## Limburg (nl-NL-x-limburg)

`nl-NL-x-limburg` models the Standard Dutch of the province of Limburg. The teacher-corpus towns are Sittard, Geleen and Roermond (van der Harst 2011, p. 55). van der Harst (2011, p. 200) finds that in the vowels "N-S differs more from the other Dutch regions than it does from the Flemish regions". Sources: van der Harst & Van de Velde (2007), Verhoeven (2005), Gussenhoven & Aarts (1999), Van de Velde (2016), van der Harst (2011), Voeten (2021), Van Bezooijen & van den Berg (2004).

### The soft g

van der Harst & Van de Velde (2007) transcribe the word-initial /ɣ/ of the carrier sentence *in de guize horen we g*. In Dutch Limburg they find mostly velar and palato-velar realisations (p. 184):

> *"In Nederlands Limburg (N-Z) vinden we zoals verwacht vooral velairen (52.5%) en palato-velairen (42.5%). De uvulair komt er maar zelden voor (5%) in dit type taalgebruik."*

Their Table 4 (p. 184) gives 77.5% voiceless tokens for the region, against 17.5% voiced ones. The speakers almost never scrape the uvula (p. 185). The paper names the voiceless velar as the norm of the region (p. 189):

> *"in de regio's onder de rivieren (N-Z en de vier Vlaamse regio's) is de stemloze velair de norm"*

The spec gives ⟨g⟩ the velar [x] in every position. The word-final [x] combines the velar place of /ɣ/ with the final devoicing of `nl-NL`. The source does not measure the coda. The spec also gives the velar [x] to the ⟨g⟩ inside the `nl-NL` grapheme ⟨berg⟩.

| Word | `nl-NL` | `nl-NL-x-limburg` |
|:---|:---|:---|
| `guize` (the carrier word) | [ˈχœyzə] | [ˈxœyzə] |
| `gaan` | [ˈχaːn] | [ˈxaːn] |
| `gras` | [ˈχrɑs] | [ˈxrɑs] |
| `liegen` | [ˈliχən] | [ˈlixən] |
| `dagen` | [ˈdaːχən] | [ˈdaːxən] |
| `dag` (word-final) | [ˈdɑχ] | [ˈdɑx] |
| `bergen` (⟨berg⟩) | [ˈbɛɹχən] | [ˈbɛrxən] |

The inherited rules of `nl-NL` apply to the new [x]. The regressive devoicing rules `NL_CODA_DEVOICE_*` make a coda obstruent voiceless before it: `zandgrond` [ˈzɑntxrɔnt], where `nl-NL` gives [ˈzɑntχrɔnt]. Where ⟨g⟩ meets ⟨ch⟩, the two velars merge in one [x], as the two uvulars of `nl-NL` merge in one [χ]: `lachgas` [ˈlɑxɑs], where `nl-NL` gives [ˈlɑχɑs].

### ⟨ch⟩ as the velar [x]

No opened source measures /x/ in Dutch Limburg. The value of ⟨ch⟩ rests on the regional norm that van der Harst & Van de Velde (2007, p. 192) name:

> *"Limburg onttrekt zich echter volledig aan dit patroon en heeft een eigen uitspraaknorm. Daar komen vooral stemloze velairen en palato-velairen voor. Nederlands-Limburg deelt die uitspraaknorm voor /γ/ met Vlaanderen"*

In the Flemish standard that shares this norm, ⟨ch⟩ is the voiceless velar. Verhoeven (2005, p. 244) writes: *"Belgian Dutch has a voiced and voiceless velar fricative: these are absent in the Netherlands. The Netherlands has a voiceless uvular fricative which does not occur in Belgian Dutch"*. His word list gives x for ⟨ch⟩ in *chijl*. The dialect of Maastricht has the same velar pair and no uvular fricative (Gussenhoven & Aarts 1999, pp. 155-156). That is dialect data, and the spec cites it as background only.

So the spec gives ⟨ch⟩ the voiceless velar [x] of ⟨g⟩. It also restates the `nl-NL` entries that spell ⟨ch⟩ inside one key: ⟨sch⟩, ⟨brecht⟩ and the word exception `tjerkgaast`.

| Word | `nl-NL` | `nl-NL-x-limburg` |
|:---|:---|:---|
| `lachen` | [ˈlaːχən] | [ˈlaːxən] |
| `acht` | [ˈɑχt] | [ˈɑxt] |
| `school` (⟨sch⟩) | [ˈsχoul] | [ˈsxoul] |
| `logisch` (word-final ⟨sch⟩) | [ˈlouχis] | [ˈlouxis] |
| `Albrecht` (⟨brecht⟩) | [ˈɑlbrɛχt] | [ˈɑlbrɛxt] |
| `Egchel` (⟨g⟩ + ⟨ch⟩) | [ˈɛχəl] | [ˈɛxəl] |
| `tjerkgaast` (word exception) | [ˈtʃɛɹkχaːst] | [ˈtʃɛrkxaːst] |

### Word-initial ⟨v⟩

Van de Velde (2016, p. 10) gives the rate of voiced word-initial v in the same corpus:

> *"In de Randstad gebruikt 41% die v aan het begin van een woord, in de middenregio 53% en in het zuiden 65%."*

So the voiced [v] is the majority value in Limburg. The spec states ⟨v⟩ as [v], and as [f] at the end of a word, in its own positional map: `vier` [ˈviːr] against `fier` [ˈfiːr]. Apart from the coda [r], the output is the same as `nl-NL` gives. The map keeps the voiced value if `nl-NL` devoices the initial ⟨v⟩ in its positional map. If `nl-NL` uses an allophone rule for that instead, the Limburg spec must switch the rule off by its id.

### Coda /r/

`nl-NL` gives a coda /r/ the approximant [ɹ] (Gussenhoven 1992, p. 46) through the allophone rule `NL_CODA_R_APPROXIMANT`. Van Bezooijen & van den Berg (2004) call that approximant the Gooise r: *"the approximant realisation of postvocalic r, the so-called Gooise r"* (p. 86) and *"Het is, zoals gezegd, een approximant"* (p. 91). They describe the region of one listener group as follows (p. 94):

> *"Het zuiden van Limburg, met een concentratie in Geleen. Dit is een gebied met vrijwel uitsluitend huig-r. De Gooise r komt hier nauwelijks of niet voor, evenmin als de tongpunt-r."*

So the spec switches the rule off by its id, and a coda /r/ keeps the [r] of the onset. Gussenhoven (1992, p. 46) adds that *"the majority of speakers have a uvular, rather than alveolar, realization of /r/"*. The `nl-NL` notes declare the symbol: *"the [r] of the onset stands for the uvular of most speakers as well"*. So the Limburg [r] stands for the uvular that the source names, in the onset and in the coda. The spec also restates the `nl-NL` entries that write [ɹ] in their own values.

| Word | `nl-NL` | `nl-NL-x-limburg` |
|:---|:---|:---|
| `door` | [ˈdoᵊɹ] | [ˈdoᵊr] |
| `vaart` | [ˈvaːɹt] | [ˈvaːrt] |
| `water` | [ˈʋaːtəɹ] | [ˈʋaːtər] |
| `kerk` (⟨kerk⟩) | [ˈkɛɹk] | [ˈkɛrk] |
| `rood` (onset) | [ˈrout] | [ˈrout] |

### Known gaps

- The palato-velar realisation of /ɣ/ (42.5%) has no rule. The paper scores it as a category, but it gives no conditioning context.
- The value of ⟨ch⟩ is an inference from the shared norm for /ɣ/. No opened source measures /x/ in Dutch Limburg.
- The ⟨berg⟩, ⟨sch⟩ and ⟨brecht⟩ entries and the `tjerkgaast` exception copy the other segments of the `nl-NL` entries. A change to one of those entries in `nl-NL` must be copied here. The tests fail when `nl-NL` adds a key or an exception with the uvular [χ] that the Limburg spec does not restate.
- The `nl-NL` grapheme ⟨veld⟩ blocks the regressive devoicing before the new [x]: `veldgrijs` [ˈvɛldxrɛis].
- The coda [r] rests on a background remark about where a group of listeners lives, with no measurement. It names South Limburg and Geleen; the teacher towns also include Sittard and Roermond. Sebregts (2014) measures /r/ in ten cities, and none is in Dutch Limburg (pp. 49-50). The uvular place of /r/ has no symbol of its own, in the onset or in the coda.
- The long mid vowels and the diphthongs take the `nl-NL` values. Voeten (2021, p. 166) finds that the non-Randstad regions "diphthongize less strongly" for /eː/, and that for /øː oː œy/ "Netherlands-Limburg goes along with the Flemish regions". He adds (p. 171) that "there are no regions which categorically do not diphthongize their vowels". These are gradient differences, with no change of category.
- Tone and pitch accent belong to the Limburgish dialects. No opened source measures them in regional Standard Dutch.

---

## Groningen (nl-NL-x-groninge)

`nl-NL-x-groninge` models the Standard Dutch of the province of Groningen and the north of Drenthe. It is not Gronings. Gronings is a Low Saxon dialect group with its own ISO 639-3 code, and the spec for it is `gos`. The data come from the teachers of the region N-N in the teacher corpus. van der Harst (2011, p. 54) defines the region as "the Groningen province and the north of the Drenthe province", and its towns are Assen, Veendam and Winschoten (p. 55). Sources: Van de Velde (2016), van der Harst & Van de Velde (2007), van der Harst (2011), Taeldeman (2006), Van de Velde & van Hout (2001), Voeten (2021).

The code follows the rule for private-use lect codes in `orthography2ipa/data/SCHEMA.md`. The slug names the place, and "A name with no short form is cut to its first 8 characters". So *Groningen* becomes `groninge`. The slug is not `gronings`, because that word names the dialect, and the dialect is keyed by its own code.

### Word-initial ⟨v⟩

Van de Velde (2016, p. 10) gives the rate of voiced word-initial v in the north:

> *"Op die manier ontdekten we dat in het noorden van Nederland de v aan het begin van een woord in slechts 9% van de gevallen als een v wordt uitgesproken. Ze zeggen in het noorden dus meestal 'fier' als het cijfer vier is bedoeld."*

So the voiceless [f] is the majority value, with 91% of the tokens. The spec gives ⟨v⟩ the value [f] at the start and at the end of a word in its own positional map. The source measures the start of the word only, so a ⟨v⟩ inside a word keeps the `nl-NL` value: `over` [ˈouvəɹ].

| Word | `nl-NL` | `nl-NL-x-groninge` |
|:---|:---|:---|
| `vier` (the source's example) | [ˈviːɹ] | [ˈfiːɹ] |
| `fier` | [ˈfiːɹ] | [ˈfiːɹ] |
| `vader` | [ˈvaːdəɹ] | [ˈfaːdəɹ] |
| `voorvader` | [ˈvoᵊɹvaːdəɹ] | [ˈfoᵊɹvaːdəɹ] |
| `over` | [ˈouvəɹ] | [ˈouvəɹ] |

### The uvular g

van der Harst & Van de Velde (2007, p. 184) find only uvular realisations of /ɣ/ in the north:

> *"Uit tabel 3 blijkt dat in de Randstad (N-R) en in het noorden (N-N) enkel uvulaire realisaties voorkomen."*

Their Table 4 (p. 184) gives 90.0% voiceless tokens for the region. The paper names the norm of the regions north of the rivers (p. 189):

> *"In de regio's boven de rivieren (N-M, N-N en N-R) is de sterk geschraapte stemloze uvulair de norm"*

`nl-NL` gives ⟨g⟩ and ⟨ch⟩ the voiceless uvular [χ] in every position (Gussenhoven 1992, p. 45). That is the norm the paper names, so the spec takes ⟨g⟩, ⟨berg⟩ and the regressive devoicing rules `NL_CODA_DEVOICE_*` from `nl-NL` and states no delta for them: `gaan` [ˈχaːn], `dag` [ˈdɑχ], `zandgrond` [ˈzɑntχrɔnt], `ogen` [ˈouχən]. The scraping is a voice quality, and the IPA value does not show it.

### Known gaps

- ⟨ch⟩ keeps the `nl-NL` value: `lachen` [ˈlaːχən], `school` [ˈsχoul]. The source measures /ɣ/ only.
- Initial ⟨z⟩ keeps the `nl-NL` value. No opened source measures it in the regional standard of the north. In the dialects, Taeldeman (2006, p. 185) finds *"enkel z-"* in Westerwolde and *"alleen s-vormen"* in the Westerkwartier.
- Final ⟨-en⟩ needs no delta. The north keeps the [n] most often: Van de Velde & van Hout (2001, Table 3, p. 96) count 347 tokens with [n] against 130 without. `nl-NL` already gives `lopen` [ˈloupən].
- Coda ⟨r⟩ takes the `nl-NL` approximant [ɹ] (Gussenhoven 1992, p. 46), as in `door` [ˈdoᵊɹ]. No opened source measures /r/ in the north. Sebregts (2014) measures no northern city (pp. 49-50). The listener regions of Van Bezooijen & van den Berg (2004, pp. 94-95) do not include Groningen.
- The diphthongs take the `nl-NL` values. Voeten (2021, p. 166) finds that /œy/ "diphthongizes significantly more than in the Randstad" and that /εi/ has "a significantly lower F1". These are gradient differences, with no change of category.

---

## Polder Dutch (nl-NL-x-polder)

`nl-NL-x-polder` models Polder Dutch (*Poldernederlands*). Polder Dutch is a sociolect, not a region. Stroop (1998) names it and defines its speakers by age, sex and job, not by place. He estimates that about half of the guests of one radio programme are younger women, and that these women speak the variety (p. 16):

> *"Ongeveer de helft van hen zijn - naar mijn schatting - jongere vrouwen en het zijn juist deze vrouwen die dat aparte soort Nederlands spreken. Ze zijn doorgaans zo tussen de 25 en 40 jaar oud."*

Most of his speakers did not grow up in the Randstad (p. 51):

> *"De anderen komen uit Utrecht, Groningen, Heerlen, Zwolle, Den Bosch, enzovoort. De meesten zijn pas na hun middelbare school naar de Randstad gekomen."*

So the spec has no `location`. The data are the observations of the author, which colleagues checked (p. 25), and the book gives no frequencies. Sources: Stroop (1998), Sebregts (2014).

### The lowered diphthongs

Stroop calls the lowering of the diphthongs "hét kenmerk van het Poldernederlands" (p. 29). He describes three changes. The spec states each one in its own `graphemes` map.

⟨ei ij⟩ becomes [aːi] (p. 25):

> *"Het opvallendste kenmerk van het Poldernederlands is - zoals gezegd - de uitspraak van de tweeklank (diftong) die als ei of ij gespeld wordt, namelijk: aai [a:i]."*

⟨ui⟩ becomes [ɑy] (p. 26):

> *"De uitspraak die in het Poldernederlands terrein wint, is die van een lage, geronde achterdiftong: in fonetisch schrift [ɑy] of gewoon gespeld: au."*

⟨ou au⟩ becomes [aːu] (p. 27). Stroop separates it from the new ui: it is "meer midden, lager en (dus) niet gerond".

> *"De oorspronkelijke ou wordt opvallend wijder en lager en klinkt nu als aau [a:u]."*

The spec gives [aːu] to the five `nl-NL` graphemes of this diphthong: ⟨ou au ouw auw aauw⟩. Stroop's examples *jaauw* (jou), *vraauw* (vrouw) and *Paaul* (Paul) spell ⟨ou ouw au⟩. The rest of each word is inherited from `nl-NL`.

| Word | `nl-NL` | `nl-NL-x-polder` |
|:---|:---|:---|
| `tijd` (taaid, p. 25) | [ˈtɛit] | [ˈtaːit] |
| `twijfelen` (twaaifelen, p. 25) | [ˈtʋɛifələn] | [ˈtʋaːifələn] |
| `huis` (haus, p. 26) | [ˈɦœys] | [ˈɦɑys] |
| `buiten` (bauten, p. 26) | [ˈbœytən] | [ˈbɑytən] |
| `Muiden` (Mauden, p. 26) | [ˈmœydən] | [ˈmɑydən] |
| `jou` (jaauw, p. 27) | [ˈjɑu] | [ˈjaːu] |
| `vrouw` (vraauw, p. 27) | [ˈvrɑu] | [ˈvraːu] |
| `Paul` (Paaul, p. 27) | [ˈpɑul] | [ˈpaːul] |

The new [aːi] is the `nl-NL` value of ⟨aai⟩, so `kraai` [ˈkraːi] and the ⟨ij⟩ of `tijd` [ˈtaːit] have the same diphthong. Stroop's spelling *aai* states the same merger.

### Known gaps

- Coda ⟨r⟩ takes the `nl-NL` approximant [ɹ] (Gussenhoven 1992, p. 46), as in `vaart` [ˈvaːɹt]. Stroop (p. 34) finds the Gooise r in Polder Dutch *"ook weer niet bij alle spreeksters van het Poldernederlands"*. Sebregts (2014) samples city accents, not this group. In his corpus the retroflex or bunched approximant is 31.8% of all coda tokens (Table 3-9, p. 75), "well over 80%" of the coda /r/ in Leiden (p. 114) and "just under 75%" in The Hague (p. 119). No source gives a share for the speakers of Polder Dutch.
- ⟨ee eu oo⟩ take the `nl-NL` closing diphthongs: `fee` [ˈfei], `beuk` [ˈbøyk], `boot` [ˈbout]. Stroop (pp. 30, 33) describes a drift beyond them, towards *aai* and *au*, with no endpoint for the sociolect.
- ⟨e⟩ before ⟨l⟩ keeps the `nl-NL` value. Stroop (p. 32) finds the raising to *opbillen* and *vertillen* *"uitsluitend bij jongere vrouwen"*.
- The fricatives keep the `nl-NL` voicing. Stroop (p. 34) finds the devoicing *"meestal afwezig"* with Polder speakers from outside the Randstad.
- The suffix ⟨-lijk⟩ takes the full diphthong of `nl-NL`: `eigenlijk` [ˈaːiχənlaːik], where `nl-NL` gives [ˈɛiχənlɛik]. The Wikipron Dutch data give [lək] for 342 of their 350 ⟨-lijk⟩ rows. That is an `nl-NL` limit, and the spec does not correct it.

---

---
[← German](de-DE.md) · [Home](../index.md) · [Faroese →](fo.md)
