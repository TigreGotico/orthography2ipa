# Known limitations

Language specs carry notes about what they do not do. The wording is uniform: "not modelled", "left unencoded", "known miss", "DECLARED GAP". The wording hides four different situations, and only one of them is a defect worth fixing. This page separates them, shows how to tell them apart, and records the limits of the ranker that measurement has confirmed.

A note that says "not modelled" because the language has a second script that nobody gives the engine costs nothing. A note that says "left unencoded" about a contrast the spelling plainly marks is a bug with a measurable price.

## The four classes

| Class | What the note describes | What to do |
|---|---|---|
| Deliberate scope limit | a design boundary: a second script, a neighbouring dialect, a morphological process that belongs downstream | Nothing. It needs no issue and no fix. |
| Engine limitation | something that the rule layer cannot express, where the author named the obstacle correctly | Change the engine, or refuse with a stated reason. A spec edit does not help. |
| Unwritten contrast | something that the orthography does not encode at all, so the spec behaves correctly and the note describes an error floor | Measure it against gold. Do not try to fix it. |
| Parked defect | a trigger visible in the spelling, a rule that the engine can express, and a gold that shows the engine getting it wrong | Fix it. These are the only notes that describe a bug. |

Tone and stress exemptions make up most of the unwritten contrasts.

## Reading a note in a spec

Ask one question: is the trigger visible in the input string? If it is a letter, a digraph, a diacritic or a position in the word, then "left unencoded" claims a defect. Such a note should carry a measured size. If the trigger is not visible, the note describes a scope decision or an error floor. The honest form of that note is a number, not a promise.

To size a note, count the gold words that contain the trigger. Transcribe them, and count how many the engine gets wrong on account of the note. [benchmarks.md](benchmarks.md#diagnosing-a-language) describes `scripts/error_analysis.py`, which ranks the confusion pairs and the worst words of a gold row. A note that misdescribes the engine is worse than no note. It sends a maintainer to look for a defect that is not there.

A spec without a gold dataset cannot be sized. Its notes may be right or wrong, and nothing in the repository can tell which. Getting gold for the language comes before any action on such a note.

## Notes measured against gold

| Language | What the note says | What the gold shows | Class |
|---|---|---|---|
| Lashi (`lsi`) | "Also left unencoded is the fronting of ⟨a⟩ to [æ] before a labial coda that the Waingmaw transcriptions show." | Some gold words with ⟨a⟩ before a labial have [æ], and the engine gives none of them. The trigger is a window of two graphemes. | parked defect |
| Passamaquoddy-Maliseet (`pqm`) | Stops and ⟨s⟩ voice between vowels, and the spec leaves this unencoded. | The note carries its own measurement. Almost every intervocalic stop or ⟨s⟩ in the gold is voiceless. | true, cost near nil |
| Plains Cree (`crk`) | The same voicing claim as the sibling spec. | The same result: the gold almost never shows the voicing. | true, cost near nil |
| Bouyei (`pcc`) | Chinese loans have an apical vowel after ⟨s⟩ and ⟨z⟩, which the spec does not model. | One gold word is in the environment. The engine gives `siyzij` as `si˧tsi˥˧`, with [i]. | true, cost of one word |
| Zulu (`zu`) | The gold writes a long vowel on the ⟨i-⟩ augment of many nouns in isolation, and nothing separates the two groups. | The engine already writes the penultimate length: `ihhashi` gives `iɦaːʃi`, and the gold has [îːɦáːʃi]. The residue is the extra length on the augment, which the note classes as an effect of citation form. | unwritten contrast |
| Classical Syriac (`syc`) | Spirantization is left unencoded, because the quššaya and rukkakha dots never appear in the input. | The gold writes a small number of spirantized tokens, and the note counts them by phoneme. | unwritten contrast, measured ceiling |
| Turoyo (`tru`) | The same alternation, from unpointed Serto text. | A larger share of the gold carries a spirantized reflex that the consonant spelling cannot predict. | unwritten contrast, measured ceiling |

The Syriac and Turoyo ceilings are not defects and should not become issues. They are the honest floor of what the orthography allows.

## Notes that cannot be measured

Some specs have no gold dataset on the board, and their notes describe triggers that the spelling plainly shows. Each would be a parked defect if a gold existed to size it:

| Language | What the note says is not modelled |
|---|---|
| Fon (`fon`) | some nasal vowels, which the spec under-generates |
| Ga (`gaa`) | vowel length, written by doubling or tripling the vowel letter |
| Bislama (`bi`) | labialized consonants, written with a following ⟨w⟩ |
| Tyap (`kcg`) | the fortis consonants, written by doubling the letter |
| Kokborok (`trp`) | the central vowel /ə/, which has no dedicated letter in the promoted orthography |

Two more notes cannot be measured for another reason. The labiovelarized `kʷ gʷ` of Kabyle and the ⟨ř⟩ of Riffian never occur in their gold orthographies. The graphemes that the notes discuss are absent from the data.

## Ranking errors

The [scoreboard](scoreboard.md) reports a 1-best PER and an oracle PER@k, the per-word minimum over the top k readings of the engine. The difference is ranking error: the beam already holds a better reading and ranks it lower. What remains at the oracle is model error, where no reading in the beam is better. [benchmarks.md](benchmarks.md#finding-where-the-beam-ranks-a-better-reading-wrong) describes the scripts that attribute ranking error to single decisions, and how to reproduce a sweep. Every rejection below is the result of such a sweep.

### Measured and rejected

#### Verbal ⟨-ent⟩

A `grammatical_endings` entry `"ent": ""` makes the third person plural ending mute, as in *ils parlent* [paʁl]. On the French `wikipron` row it wins 3,844 types and loses 254, and it lowers the PER of the row a long way. It does not ship.

The 254 losses are the nouns and adjectives in ⟨-ent⟩: *vent, dent, cent, argent, accent, talent, absent, serpent, Occident, Vincent*. Type PER counts each of them once, like each rare verb form. Running text does not. This library feeds TTS, and saying "v" for *vent* is not paid for by thousands of rare verb forms.

The entry also fails the precondition that `grammatical_endings` states in `types.py`. The words that keep the ending must be a closed set in `word_exceptions`, the way French ⟨-er⟩ keeps *mer* and *hiver*. The French nouns and adjectives in ⟨-ent⟩ are not a closed set, and the proper nouns (*Laurent*, *Florent*, *Clément*) are open-ended. Verb against noun cannot be decided from spelling. It needs part of speech, and o2i takes no part-of-speech input.

A rescorer downstream can supply part of speech, but it can only choose among readings that the beam contains. Without help, the beam never contains [paʁl] at any width. That is a gap in coverage, not a ranking error. French therefore declares the ending as a deferring candidate list:

```json
"ent": [null, ""]
```

`null` at element 0 keeps rank 1 where it was, and the mute reading joins the beam below it. With the alternatives exposed, the mute reading is in the top five, and the 1-best does not move:

```python
from orthography2ipa import G2P

for expose in (False, True):
    g = G2P("fr-FR", expose_ambiguous_endings=expose)
    print(expose, g.word_candidates("parlent", k=5))
```

```text
False ['paʁlɑ̃', 'paʁle', 'paʁlɑ̃t', 'paʁlet', 'paʁlɛ']
True ['paʁlɑ̃', 'paʁle', 'paʁlɑ̃t', 'paʁl', 'paʁlet']
```

On a 300-word sample of the ⟨-ent⟩ words that the gold makes mute, the gold reading is in the top 10 for 192 of them. Exact match at rank 1 stays at zero, as it must, because o2i is not the layer that decides. That movement is reachability, not ranking improvement. [benchmarks.md](benchmarks.md#injected-alternatives-do-not-count-as-ranking-error) explains why the scoreboard measures its oracle without injected alternatives. [SCHEMA.md](../orthography2ipa/data/SCHEMA.md#ambiguous-endings) describes the list form.

The spec declares no ⟨-ment⟩ entry beside it. ⟨-ment⟩ has the same ambiguity: *dorment* and *ferment* are mute, *moment* and *comment* are not. A longer entry would shield exactly the verbs that the list form reaches. Without `"ent"`, the nasal ⟨en⟩ and a silent ⟨t⟩ already give *rapidement* [ʁapidəmɑ̃]. A `"ment": "mɑ̃"` entry also fails in the adverbs in ⟨-amment⟩ and ⟨-emment⟩. ⟨mm⟩ is one token there, so ⟨-ment⟩ cannot match. The entry turned *comment* into [kɔm] and *apparemment* into [apaʁəm], with 131 losses against 7 wins in that bucket.

#### ⟨o⟩ under the loi de position

The aperture positions let a spec choose a vowel by whether its syllable is open or closed. That is the environment of the Romance *loi de position*. French ⟨eu⟩ uses them. Declared for ⟨o⟩ and measured on the French `wikipron` row, they make the PER worse. French ⟨o⟩ is [ɔ] in most open syllables too (*moto*, *protoplasme*), so the law is much weaker for ⟨o⟩ than for ⟨eu⟩. The spec declares nothing for ⟨o⟩ rather than half a rule.

### Gaps that remain open

| Gap | Why the engine cannot close it | What could |
|---|---|---|
| French loanwords in ⟨-er⟩ | 138 of the 6,211 types that end in ⟨-er⟩ keep a pronounced /ʁ/: *Jupiter, laser, cancer, Esther, Asperger*, and many English and German loans and place names. The ⟨-er⟩ grammatical ending makes the whole ending mute, so the engine gives *Jupiter* as `ʒypite`. | `word_exceptions`, which already lists some (*revolvers*, *leaders*, *pokers*, *laser*), or a layer that knows loanwords |
| French verbal ⟨-ent⟩ | Verb against noun needs part of speech. o2i exposes both readings and ranks neither well. | a downstream rescorer with part of speech |
| Boundaries inside compounds | The word-level rules cannot see a boundary inside a compound. French intervocalic ⟨s⟩ in learned compounds (*pléonasme*, *œcuménisme*) goes wrong in both directions. Dutch devoicing at the boundary does not fire: *opvanghuis* gives `ˈoːpvɑŋɦœys` with [v]. | compound segmentation |

---
[← Gold defects](gold_defects.md) · [Home](index.md) · [Spec diagnostics →](spec_diagnostics.md)
