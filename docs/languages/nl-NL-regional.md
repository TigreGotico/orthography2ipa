# Regional Standard Dutch of the Netherlands (nl-NL-x-*)

The `nl-NL-x-*` specs model the regional accents of Standard Dutch in the Netherlands. They describe the standard language as educated speakers from one region speak it. They do not describe the traditional dialects, which have specs of their own, such as `li` for Limburgish. Each regional spec is a delta spec over `nl-NL`: it inherits the whole standard and declares only what its region changes. This page first explains how the inheritance works. One table then compares the defining features of every regional spec. Each spec then has its own section, with its sources, its rules and their conditions, and its known gaps.

Every transcription on this page is real output of `orthography2ipa.transcribe(text, code)`.

## How the regional specs inherit from nl-NL

Every spec on this page sets `parent` to `nl-NL`. It also sets the four base keys `graphemes_base`, `allophones_base`, `positional_graphemes_base` and `word_exceptions_base` to `nl-NL`. So each regional spec starts from the full standard. It gets the open-syllable vowel length, the final devoicing, the stress block, the allophone rules and the word exceptions of `nl-NL`. The engine does not inherit `collapse_geminates`, so each spec sets it to `true` again, as `nl-NL` does.

The dictionary fields `graphemes`, `allophones`, `positional_graphemes` and `word_exceptions` merge key by key. An own entry replaces the `nl-NL` entry with the same key, and every other key is inherited. In `positional_graphemes` the key is the grapheme. So an own map for ⟨g⟩ replaces the whole ⟨g⟩ map of `nl-NL`, and the spec must state every position it needs.

A regional spec states a value itself when `nl-NL` could change that value later. The Limburg spec gives ⟨g⟩ the velar [x] and ⟨v⟩ the voiced [v] in its own positional maps. So a change to the dorsal fricative or to the initial ⟨v⟩ of `nl-NL` does not reach Limburg through the inheritance.

The rule list `allophone_rules` merges by id (see [../engine/allophony.md](../engine/allophony.md#inheritance)). The `nl-NL` rules keep their order. An own rule with the same id replaces the inherited rule in place. An own rule with a new id goes to the end of the list.

The data for these specs come from the teacher corpus of Van Hout et al. (1999). It holds 160 teachers of Dutch from four regions of the Netherlands and four regions of Flanders. The teachers read word lists and carrier sentences. van der Harst (2011, p. 53) states the reason for the choice: teachers "are professional language users who are assumed to speak the standard language on a daily basis". The Netherlands regions are the Randstad, the Middle (south Gelderland), the North (Groningen and north Drenthe) and the South (Dutch Limburg).

## Defining features

| Spec | Region | Features that set it apart from `nl-NL` | Example |
|:---|:---|:---|:---|
| [`nl-NL-x-limburg`](#limburg-nl-nl-x-limburg) | Dutch Limburg: Sittard, Geleen, Roermond | /ɣ/ as the voiceless velar [x], the soft g<br>word-initial ⟨v⟩ stays [v] | `guize` [ˈxœyzə], `liegen` [ˈlixən], `vier` [ˈviːr] |

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

---
[← German](de-DE.md) · [Home](../index.md) · [Faroese →](fo.md)
