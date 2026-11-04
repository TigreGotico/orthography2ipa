# Regional Standard Dutch of the Netherlands (nl-NL-x-*)

The `nl-NL-x-*` specs model the regional and social accents of Standard Dutch in the Netherlands. A regional spec describes the standard language as educated speakers from one region speak it. Polder Dutch (`nl-NL-x-polder`) is a sociolect, not a region: it describes the standard language of a social group. The specs do not describe the traditional dialects, which have specs of their own, such as `li` for Limburgish. Each spec is a delta spec over `nl-NL`: it inherits the whole standard and declares only what its region or group changes. This page first explains how the inheritance works. One table then compares the defining features of every regional spec. Each spec then has its own section, with its sources, its rules and their conditions, and its known gaps.

Every transcription on this page is real output of `orthography2ipa.transcribe(text, code)`.

## How the regional specs inherit from nl-NL

Every spec on this page sets `parent` to `nl-NL`. It also sets the four base keys `graphemes_base`, `allophones_base`, `positional_graphemes_base` and `word_exceptions_base` to `nl-NL`. So each regional spec starts from the full standard. It gets the open-syllable vowel length, the final devoicing, the stress block, the allophone rules and the word exceptions of `nl-NL`. The engine does not inherit `collapse_geminates`, so each spec sets it to `true` again, as `nl-NL` does.

The dictionary fields `graphemes`, `allophones`, `positional_graphemes` and `word_exceptions` merge key by key. An own entry replaces the `nl-NL` entry with the same key, and every other key is inherited. In `positional_graphemes` the key is the grapheme. So an own map for ⟨g⟩ replaces the whole ⟨g⟩ map of `nl-NL`, and the spec must state every position it needs.

A spec states a value itself when `nl-NL` could change that value later. The Limburg spec gives ⟨g⟩ the velar [x] and ⟨v⟩ the voiced [v] in its own positional maps. So a change to the dorsal fricative or to the initial ⟨v⟩ of `nl-NL` does not reach Limburg through the inheritance. The Polder spec gives its eight diphthong graphemes their values in its own `graphemes` map for the same reason.

The rule list `allophone_rules` merges by id (see [../engine/allophony.md](../engine/allophony.md#inheritance)). The `nl-NL` rules keep their order. An own rule with the same id replaces the inherited rule in place. An own rule with a new id goes to the end of the list.

The data for the Limburg spec come from the teacher corpus of Van Hout et al. (1999). It holds 160 teachers of Dutch from four regions of the Netherlands and four regions of Flanders. The teachers read word lists and carrier sentences. van der Harst (2011, p. 53) states the reason for the choice: teachers "are professional language users who are assumed to speak the standard language on a daily basis". The Netherlands regions are the Randstad, the Middle (south Gelderland), the North (Groningen and north Drenthe) and the South (Dutch Limburg).

## Defining features

| Spec | Region or group | Features that set it apart from `nl-NL` | Example |
|:---|:---|:---|:---|
| [`nl-NL-x-limburg`](#limburg-nl-nl-x-limburg) | Dutch Limburg: Sittard, Geleen, Roermond | /ɣ/ as the voiceless velar [x], the soft g<br>word-initial ⟨v⟩ stays [v] | `guize` [ˈxœyzə], `liegen` [ˈlixən], `vier` [ˈviːr] |
| [`nl-NL-x-polder`](#polder-dutch-nl-nl-x-polder) | A sociolect, not a region: younger women in public speech | ⟨ei ij⟩ as [aːi]<br>⟨ui⟩ as [ɑy]<br>⟨ou au⟩ as [aːu] | `tijd` [ˈtaːit], `huis` [ˈɦɑys], `vrouw` [ˈvraːu] |

## Limburg (nl-NL-x-limburg)

`nl-NL-x-limburg` models the Standard Dutch of the province of Limburg. The teacher-corpus towns are Sittard, Geleen and Roermond (van der Harst 2011, p. 55). van der Harst (2011, p. 200) finds that in the vowels "N-S differs more from the other Dutch regions than it does from the Flemish regions". Sources: van der Harst & Van de Velde (2007), Van de Velde (2016), van der Harst (2011), Voeten (2021), Van Bezooijen & van den Berg (2004).

### The soft g

van der Harst & Van de Velde (2007) transcribe the word-initial /ɣ/ of the carrier sentence *in de guize horen we g*. In Dutch Limburg they find mostly velar and palato-velar realisations (p. 184):

> *"In Nederlands Limburg (N-Z) vinden we zoals verwacht vooral velairen (52.5%) en palato-velairen (42.5%). De uvulair komt er maar zelden voor (5%) in dit type taalgebruik."*

Their Table 4 (p. 184) gives 77.5% voiceless tokens for the region, against 17.5% voiced ones. The speakers almost never scrape the uvula (p. 185). The paper names the voiceless velar as the norm of the region (p. 189):

> *"in de regio's onder de rivieren (N-Z en de vier Vlaamse regio's) is de stemloze velair de norm"*

The spec gives ⟨g⟩ the velar [x] in every position. The word-final [x] combines the velar place of /ɣ/ with the final devoicing of `nl-NL`. The source does not measure the coda. The spec also gives the velar [x] to the ⟨g⟩ inside the `nl-NL` grapheme ⟨berg⟩.

| Word | `nl-NL` | `nl-NL-x-limburg` |
|:---|:---|:---|
| `guize` (the carrier word) | [ˈɣœyzə] | [ˈxœyzə] |
| `gaan` | [ˈɣaːn] | [ˈxaːn] |
| `gras` | [ˈɣrɑs] | [ˈxrɑs] |
| `liegen` | [ˈliɣən] | [ˈlixən] |
| `dagen` | [ˈdaːɣən] | [ˈdaːxən] |
| `dag` (word-final) | [ˈdɑx] | [ˈdɑx] |
| `bergen` (⟨berg⟩) | [ˈbɛrɣən] | [ˈbɛrxən] |

The inherited rules of `nl-NL` apply to the new [x]. The regressive devoicing rules `NL_CODA_DEVOICE_*` make a coda obstruent voiceless before it: `zandgrond` [ˈzɑntxrɔnt], where `nl-NL` gives [ˈzɑndɣrɔnt]. The degemination of `collapse_geminates` merges it with an [x] before it: `lachgas` [ˈlɑxɑs], where `nl-NL` gives [ˈlɑxɣɑs].

### Word-initial ⟨v⟩

Van de Velde (2016, p. 10) gives the rate of voiced word-initial v in the same corpus:

> *"In de Randstad gebruikt 41% die v aan het begin van een woord, in de middenregio 53% en in het zuiden 65%."*

So the voiced [v] is the majority value in Limburg. The spec states ⟨v⟩ as [v], and as [f] at the end of a word, in its own positional map: `vier` [ˈviːr] against `fier` [ˈfiːr]. The output is the same as `nl-NL` gives. The map keeps the voiced value if `nl-NL` devoices the initial ⟨v⟩ in its positional map. If `nl-NL` uses an allophone rule for that instead, the Limburg spec must switch the rule off by its id.

### Known gaps

- The palato-velar realisation of /ɣ/ (42.5%) has no rule. The paper scores it as a category, but it gives no conditioning context.
- ⟨ch⟩ keeps the `nl-NL` value: `lachen` [ˈlaːxən], `school` [ˈsxoːl]. The source measures /ɣ/ only, and no opened source measures /x/ in Dutch Limburg.
- The ⟨berg⟩ entry of the spec copies the [r] of the `nl-NL` entry. A change to that entry in `nl-NL` must be copied here.
- The `nl-NL` grapheme ⟨veld⟩ blocks the regressive devoicing before the new [x]: `veldgrijs` [ˈvɛldxrɛis].
- /r/ takes the `nl-NL` value. Van Bezooijen & van den Berg (2004, p. 94) call South Limburg *"een gebied met vrijwel uitsluitend huig-r"*. That is a background remark about where a group of listeners lives, with no measurement.
- The long mid vowels and the diphthongs take the `nl-NL` values. Voeten (2021, p. 166) finds that the non-Randstad regions "diphthongize less strongly" for /eː/, and that for /øː oː œy/ "Netherlands-Limburg goes along with the Flemish regions". He adds (p. 171) that "there are no regions which categorically do not diphthongize their vowels". These are gradient differences, with no change of category.
- Tone and pitch accent belong to the Limburgish dialects. No opened source measures them in regional Standard Dutch.

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

- Coda ⟨r⟩ takes the `nl-NL` value. Stroop (p. 34) finds the Gooise r in Polder Dutch *"ook weer niet bij alle spreeksters van het Poldernederlands"*. Sebregts (2014) samples city accents, not this group. In his corpus the retroflex or bunched approximant is 31.8% of all coda tokens (Table 3-9, p. 75), "well over 80%" of the coda /r/ in Leiden (p. 114) and "just under 75%" in The Hague (p. 119). No source gives a share for the speakers of Polder Dutch.
- ⟨ee eu oo⟩ take the `nl-NL` values: `fee` [ˈfeː], `beuk` [ˈbøːk], `boot` [ˈboːt]. Stroop (pp. 30, 33) describes a drift towards *ei*, *ui* and *ou*, with no endpoint for the sociolect.
- ⟨e⟩ before ⟨l⟩ keeps the `nl-NL` value. Stroop (p. 32) finds the raising to *opbillen* and *vertillen* *"uitsluitend bij jongere vrouwen"*.
- The fricatives keep the `nl-NL` voicing. Stroop (p. 34) finds the devoicing *"meestal afwezig"* with Polder speakers from outside the Randstad.
- The suffix ⟨-lijk⟩ takes the full diphthong of `nl-NL`: `eigenlijk` [ˈaːiɣənlaːik], where `nl-NL` gives [ˈɛiɣənlɛik]. The Wikipron Dutch data give [lək] for 342 of their 350 ⟨-lijk⟩ rows. That is an `nl-NL` limit, and the spec does not correct it.

---

---
[← German](de-DE.md) · [Home](../index.md) · [Faroese →](fo.md)
