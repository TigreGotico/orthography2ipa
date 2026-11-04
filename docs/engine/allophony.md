# Allophony: the second map

The library models pronunciation as two maps. The pre-lexical map takes orthography to phonemes. `positional_graphemes`, the vowel-class positions and the candidate weights condition it. The post-lexical map takes a phoneme to its surface allophone. `allophone_rules` make this second map conditional on context.

A spec declares an ordered list of `allophone_rules`. Each rule is a declarative `phoneme → surface` rewrite with context conditions. The list compiles into a [lattice rescorer](lattice.md), `orthography2ipa.allophony.AllophoneRescorer`. The rescorer replaces a chosen phoneme with its one context-correct surface form at the same beam cost. It realises the phoneme and does not add beam branches.

The flat `spec.allophones` table is a different thing. It lists the variants of each phoneme with no context. Only `expand_allophones` reads it, and that option puts every variant into the beam at a flat `+0.5` cost.

## Where it runs in the pipeline

```
normalize → tokenize → select (positional + weights)
                          │
                          ▼
                 rescore  ├─ user rescorer(s)
                          └─ allophony  ← allophone_rules compile to here
                          │
                          ▼
                 beam path selection → stress marks → sandhi → dialect
```

The allophony stage runs after phoneme selection, so it sees the chosen phoneme and its resolved neighbours. It runs after any user rescorer and before beam path selection. So it runs before stress-mark insertion and before cross-word sandhi, which act on the whole utterance. In the structured lattice, it turns the phoneme lattice into the allophone lattice.

Stress and syllable context come only from the engine path (`G2P.transcribe` and `G2P.ipa_lattice`). The standalone tokenizer path (`PhonetokTokenizer.ipa_beam`) has no stress context, so a stress-conditioned rule does not fire there. The stress-conditioned positional entries behave the same way. Word-position and neighbour conditions work on both paths.

## The condition vocabulary

Each rule names one or more underlying `phonemes` and a `surface` realisation. Its conditions are all ANDed, and a condition left unset matches anything. For each slot, the first rule in the list whose phoneme and conditions match is the one that fires. A rule with an empty `phonemes` list never fires, which is how a child spec disables a rule it inherits.

The conditions on the slot itself:

| Condition | Values | Fires when |
|---|---|---|
| `word_initial`, `word_final` | `true` or `false` | the grapheme is, or is not, at that word edge |
| `stress` | `"stressed"`, `"unstressed"`, `"pretonic"`, `"posttonic"` | the syllable has, or lacks, primary stress, or stands before or after it (engine path only) |
| `syllable_position` | `"onset"`, `"coda"`, `"nucleus"` | a vowel is a nucleus, a consonant before a vowel is an onset, and any other consonant is a coda |
| `grapheme` | list of graphemes | the slot's own source grapheme is one of them |
| `word` | list of words | the whole source word is one of them |
| `word_contains_grapheme` | list of strings | one of them occurs anywhere in the source word |
| `word_contains_grapheme_not` | list of strings | none of them occurs in the source word |
| `requires_other_nucleus` | `true` or `false` | another slot of the word carries a nucleus |
| `followed_by_nucleus` | `true` or `false` | a nucleus occurs later in the word |

The conditions on the neighbours:

| Condition | Values | Fires when |
|---|---|---|
| `preceded_by`, `followed_by` | a neighbour class | the previous or next grapheme belongs to the class |
| `preceded_by_2`, `followed_by_2` | a neighbour class | the grapheme two away belongs to the class |
| `preceded_by_3`, `followed_by_3` | a neighbour class | the grapheme three away belongs to the class |
| `preceded_by_phoneme`, `followed_by_phoneme` | list of IPA strings | the chosen phoneme of the previous or next slot is one of them |
| `preceded_by_phoneme_2`, `followed_by_phoneme_2` | list of IPA strings | the first declared candidate of the grapheme two away is one of them |
| `preceded_by_surface_phoneme_2` | list of IPA strings | the resolved candidate of the slot two back is one of them |
| `preceded_by_grapheme`, `followed_by_grapheme` | list of graphemes | the previous or next source grapheme is one of them |
| `followed_by_grapheme_not` | list of graphemes | the next source grapheme is none of them |

The neighbour classes are `vowel`, `consonant`, `consonant_cluster`, `coda`, `coda_nasal`, `front_vowel`, `back_vowel`, `palatal`, `emphatic`, `word_boundary` and `any`. `orthography2ipa.vowels` holds the predicates. `palatal` and `emphatic` read the neighbour's IPA. `word_boundary` matches when no grapheme stands there, and `any` matches when one does.

The offset conditions look past a mute letter. Russian final devoicing reaches the ⟨в⟩ of ⟨любовь⟩ because the silent ⟨ь⟩ after it is word-final (`followed_by_2: "word_boundary"`). English ⟨-ed⟩ uses `preceded_by_3: "any"` to tell a real stem (⟨used⟩) from a monosyllable whose ⟨ed⟩ is the stem (⟨fed⟩). Portuguese plural ⟨-ens⟩ uses `followed_by_3: "word_boundary"` from the ⟨e⟩.

`preceded_by_phoneme_2` reads the underlying phoneme, which is known before any rule runs. `preceded_by_surface_phoneme_2` reads what the slot resolved to. English ⟨-ed⟩ devoicing needs the second one. The stem of ⟨used⟩ resolves its ⟨s⟩ to [z], but the first declared candidate of ⟨s⟩ is [s].

`word` is the lexeme-level hook. Portuguese ⟨sopa⟩ has close [o] and ⟨sova⟩ has open [ɔ], and only the lexeme decides. A `word` rule pins that one vowel and lets every other process run, so it inherits cleanly to the dialects. A `word_exceptions` entry freezes the whole word instead.

`requires_other_nucleus: true` keeps a vowel-deleting rule from emptying a word of its only nucleus (Hayes 2009, ch. 13). Romanian word-final ⟨i⟩ is asyllabic in ⟨lupi⟩ [lupʲ] but full in the monosyllables ⟨și⟩, ⟨fi⟩ and ⟨zi⟩ (Chitoran 2002, ch. 5). A syllabic consonant counts as a nucleus, so Czech ⟨vlk⟩ has one.

The vocabulary covers the common post-lexical processes:

| Process | Conditions |
|---|---|
| Final-obstruent devoicing | `word_final: true` |
| Unstressed vowel reduction | `stress: "unstressed"` |
| Intervocalic flapping | `preceded_by: "vowel"`, `followed_by: "vowel"` |
| Nasal place assimilation | `followed_by_phoneme: ["k", "ɡ"]` for velar, `["p", "b", "m"]` for labial |
| Closed-syllable shortening, complementary quantity | `followed_by: "consonant_cluster"` |

### `consonant_cluster`

The neighbour begins two or more consonant segments, counted away from the anchor grapheme. The engine decides this on the phonemes, in one of three ways. The neighbour realises a long consonant (`tː`), which is moraic on its own. The neighbour is one grapheme that spells several consonants, such as ⟨x⟩ for /ks/. Or the grapheme beyond the neighbour is also a consonant, as in ⟨s⟩⟨t⟩.

Mainland Scandinavian complementary quantity needs this context (Riad 2014, Kristoffersen 2000, Basbøll 2005). A stressed vowel is long in an open syllable and short before a cluster:

```python
from orthography2ipa import G2P

sv = G2P("sv-SE")
sv.transcribe_word("vit")    # 'ˈviːt'
sv.transcribe_word("vitt")   # 'ˈvɪtː'
```

State the context as a class. Do not list the clusters as grapheme keys (`bl`, `bf`, `st`). Such keys assert spellings the orthography does not have, and their number grows with every pair. The tokenizer also reads the longest key first, so a cluster key changes how the neighbouring rules see the word.

Some letter groups hide a cluster behind one phoneme. Swedish vowels are short before ⟨ng⟩, ⟨nk⟩ and ⟨sk⟩, but ⟨ng⟩ maps to the single [ŋ]. `followed_by_grapheme` states these by spelling.

### `coda` and `coda_nasal`

`coda` matches a neighbour in coda position, with the same heuristic as `syllable_position`. `coda_nasal` matches a coda neighbour whose IPA is a nasal consonant.

Nasal vowels need `coda_nasal`. A vowel nasalises before a nasal that closes the syllable and stays oral before one that opens the next. Pair the vowel rule with an absorb rule that deletes the coda nasal:

```json
{"id": "FR_NASAL_a", "phonemes": ["a"], "surface": "ɑ̃",
 "followed_by": "coda_nasal"},
{"id": "FR_NASAL_ABSORB", "phonemes": ["n", "m"], "surface": "",
 "syllable_position": "coda", "preceded_by": "vowel"}
```

```python
G2P("fr-FR").transcribe_word("bon")     # 'bɔ̃'
G2P("fr-FR").transcribe_word("bonne")   # 'bɔn'
G2P("mwl").transcribe_word("pan")       # 'ˈpɐ̃'
G2P("mwl").transcribe_word("cana")      # 'ˈkanɐ'
```

⟨an⟩ is not a digraph in any orthography. It is a vowel letter and a nasal letter, and a rule supplies the nasality. A table of pseudo-digraphs such as `{"an": ["ɑ̃"], "am": ["ɑ̃"], "en": ["ɑ̃"]}` cannot express the onset contrast. It also forces more pseudo-graphemes (⟨anh⟩) to undo the first ones. Follow the official orthography of the language for what a digraph is. Mirandese has ⟨nh⟩ and ⟨lh⟩, and it has no ⟨an⟩.

Neighbour lookups read the original slots, so one rule cannot feed another within a pass. That is why the vowel rule keys on `coda_nasal`, a grapheme-level class that the emptied nasal slot does not change. The absorb rule keys on the slot. If the absorb rule fed the vowel rule, it would bleed the nasalisation. The vowel rule would then see an empty next slot.

### `emphatic`

`emphatic` matches a neighbour whose IPA carries the pharyngealisation diacritic ⟨ˤ⟩ (U+02E4). `orthography2ipa.vowels.is_pharyngealized_consonant` decides it, as the mirror of `is_palatal_consonant`. The class names no language. Any spec that writes a pharyngealised consonant with ⟨ˤ⟩ gets it, including the lateral emphatics ⟨ɬˤ ɮˤ⟩.

## Inserting instead of rewriting: `append`

A rule normally names the `surface` that its target becomes. Epenthesis does not fit that shape. The inserted segment is the same wherever it goes, while the segment it attaches to is any member of a class. A fixed `surface` string can name only one of them. `append` states the insertion. The realisation is `phoneme + append`, so one rule covers the whole class:

```json
{"id": "EGY_EPEN_INITIAL",
 "phonemes": ["b", "d", "d͡ʒ", "f", "h", "k", "m", "n", "p", "r", "s", "t", "t͡ʃ", "x", "z", "ç", "ɡ", "ʃ", "w"],
 "append": "ɛ", "word_initial": true, "followed_by": "consonant"}
```

This is the Egyptological reading of Egyptian. The script writes no vowels, and the convention supplies one to break the consonant string (see [languages/egy.md](../languages/egy.md)):

```python
G2P("egy").transcribe_word("nfr")   # 'nɛfɛr'
```

`append` and `surface` are mutually exclusive. A rule either rewrites its target or inserts next to it.

## Doubled letters that are not geminates

The pass protects a geminate from being split. A rule that material outside the geminate triggers may not rewrite one half and leave a heterorganic cluster. This protection assumes that the orthography writes gemination by doubling the letter, and most orthographies do. A consonantal skeleton does not. Egyptological ⟨bbr⟩ is the root b-b-r, and the reading convention puts a vowel between the two ⟨b⟩. The `egy` spec sets `doubled_letters_geminate: false`, which turns the protection off:

```python
G2P("egy").transcribe_word("bbr")   # 'bɛbɛr'
```

The protection also covers only doubling that is one segment. A doubled consonant between two nuclei spans a syllable boundary (Hayes 1989, Ladefoged & Maddieson 1996:92). Its halves are a coda and an onset. So a rule whose neighbour condition points at the twin may realise the half it applies to, because the boundary triggered it. Lashi ⟨yuggi⟩ shows this. The coda rule reads the consonant after the first ⟨g⟩ and finds the second one:

```python
G2P("lsi").transcribe_word("yuggi")   # 'juk̚ɡi'
```

`followed_by`, `followed_by_grapheme` and `followed_by_phoneme` point at the twin from the first half. The `preceded_by` family points at it from the second half.

Everything else stays blocked. Word-finally, or before another consonant, no nucleus follows to license an onset. The pair is then one long coda that nothing may divide. Najdi ⟨بَخّ⟩ keeps both halves and takes no gahawa epenthesis between them:

```python
G2P("ars-SA").transcribe_word("بَخّ")   # 'ˈbaxx'
```

A rule that points anywhere but at the twin is blocked too. This covers a rule with no condition, a `word_final` rule, a two-step condition such as `followed_by_2` that reads past the twin, and a negative condition such as `followed_by_grapheme_not`.

Rules are pure data, and specs hold no code. [`data/SCHEMA.md`](../../orthography2ipa/data/SCHEMA.md#allophone-rule-schema) gives the JSON shape.

## Toggles

`G2P(lang, apply_allophony=True)` is the default, and it applies the spec's `allophone_rules`. It does nothing for a spec that declares none. Set `apply_allophony=False` to get the broad, phonemic output for a spec that declares rules.

`expand_allophones` is independent. It puts every `spec.allophones` variant into the beam, which shows all surface possibilities. It does not pick the variant that fits the context.

## Inheritance

`allophone_rules` inherit by id-keyed overlay (`InheritanceMode.OVERLAY_BY_ID`), as `sandhi_rules` do. A child spec that sets `graphemes_base` inherits the whole rule list of its base, in order. An own rule with a matching `id` replaces the inherited rule in place. An own rule with a new `id` goes to the end of the list.

A post-lexical process is usually a property of the whole language. Catalan final devoicing and nasal assimilation hold in every Catalan variety, so the dialects inherit them and can still override one rule by `id`. A child that lacks a process redeclares the rule `id` with an empty `phonemes` list. Afrikaans (`af`) does this for the Dutch open-syllable lengthening rules it would otherwise inherit.

## Worked example: Catalan

The `ca` spec declares rules for four processes, each cited to a reference grammar.

### Final-obstruent devoicing

Word-final voiced obstruents devoice: `/b d ɡ z ʒ v/ → [p t k s ʃ f] / _#` (Wheeler 2005, *The Phonology of Catalan*, §5.3).

```python
ca = G2P("ca")
ca.transcribe_word("fred")                                  # 'ˈfɾɛt'
ca.transcribe_word("llarg")                                 # 'ˈʎark'
G2P("ca", apply_allophony=False).transcribe_word("fred")    # 'ˈfɾɛd'
```

Central Catalan also deletes a word-final stop after a homorganic nasal or lateral (Wheeler 2005 §10.4). The `CA_CLUSTER_*_FINAL` rules state this, so ⟨sang⟩ is [ˈsaŋ] and ⟨camp⟩ is [ˈkam]. Valencian and Balearic keep the stop.

### Nasal place assimilation

/n/ takes the place of a following consonant (Recasens 1993, *Fonètica i fonologia*). It becomes [m] before a labial, [ɱ] before /f v/, [ŋ] before a velar and [ɲ] before a palatal.

```python
ca.transcribe_word("banca")   # 'ˈbaŋkə'
ca.transcribe_word("canvi")   # 'ˈkambi'
ca.transcribe_word("àngel")   # 'ˈaɲʒəl'
```

### Spirantisation

The voiced stops lenite to approximants after a vowel: `/b d ɡ/ → [β ð ɣ]` (Wheeler 2005, §5.2). The `CA_SPIRANT_*` rules key on `preceded_by: "vowel"`, and the `CA_SPIRANT_*_CONT` rules extend them to a preceding continuant. A word-final stop takes the devoicing rule instead, because that rule comes first in the list. The `CA_GEMINATE_BL` and `CA_GEMINATE_GL` rules keep /b ɡ/ a stop before a lateral, where Catalan geminates them.

```python
ca.transcribe_word("cada")    # 'ˈkaðə'
ca.transcribe_word("pagar")   # 'pəˈɣa'
ca.transcribe_word("roba")    # 'ˈrɔβə'
ca.transcribe_word("poble")   # 'ˈpɔblə'
```

### Unstressed vowel reduction

The Eastern block (Central and Balearic) reduces vowels only in unstressed syllables. Unstressed /a e ɛ/ become [ə] and /o ɔ/ become [u], and stressed vowels keep full quality (Wheeler 2005, §2.3). The spec states this in the pre-lexical map, with the `nucleus_unstressed` position of [positional_graphemes.md](positional_graphemes.md), and not as an allophone rule. Like a stress-conditioned rule, the position fires on the engine path only.

```python
ca.transcribe_word("casa")   # 'ˈkazə'
ca.transcribe_word("dona")   # 'ˈdɔnə'
```

The Western block does not reduce in this way (Recasens 1996, Veny 1982). Valencian (`ca-x-valencia`) keeps full ⟨a⟩ in unstressed syllables. Northwestern Catalan (`ca-x-occident`) has its own word-final [ɛ] for ⟨a⟩.

```python
G2P("ca-x-valencia").transcribe_word("casa")     # 'ˈkaza'
G2P("ca-x-occident").transcribe_word("casa")   # 'ˈkazɛ'
```

## Worked example: Brazilian Portuguese

The `pt-BR` spec is the base of the Brazilian dialect specs. Its rules raise the final unstressed vowels (Barbosa & Albano 2004, Câmara Jr. 1970). Word-final /e o/ become the close vowels [i u]:

```json
{"id": "BR_RAISE_FINAL_E", "phonemes": ["ɪ"], "surface": "i", "word_final": true}
```

```python
br = G2P("pt-BR")
br.transcribe_word("gato")                                    # 'ˈɡatu'
br.transcribe_word("leite")                                   # 'ˈlejt͡ʃi'
G2P("pt-BR", apply_allophony=False).transcribe_word("gato")   # 'ˈɡatʊ'
G2P("pt-BR", apply_allophony=False).transcribe_word("leite")  # 'ˈlejtɪ'
```

The rules show two ways to write a base rule that inherits well:

1. Target the reduced vowel, not the underlying phoneme. The rule fires on the near-close [ɪ ʊ] that the pre-lexical map already selects word-finally. A conservative dialect that keeps a final [e o] inherits the rule, and the rule never fires there.
2. Leave a process pre-lexical when a position already states it. The `pt-BR` positional table affricates ⟨t d⟩ before the letter ⟨i⟩ (⟨tia⟩ [ˈt͡ʃiɐ]). The `BR_AFFRIC_T_RAISED` and `BR_AFFRIC_D_RAISED` rules cover only the [i ɪ] that a raised ⟨e⟩ supplies, as in ⟨leite⟩.

[languages/pt-BR.md](../languages/pt-BR.md) gives the full description.

## Worked example: European Portuguese

The `pt-PT` rules use the `syllable_position` condition for the coda consonants.

### Dark coda /l/

/l/ becomes [ɫ] in the coda, both word-finally and before a consonant. An onset /l/ stays clear (Mateus & d'Andrade 2000, ch. 2, Cruz-Ferreira 1995, *JIPA* 25(2): 91).

```python
pt = G2P("pt-PT")
pt.transcribe("sol")    # 'ˈsɔɫ'
pt.transcribe("alto")   # 'ˈɐɫtu'
pt.transcribe("bola")   # 'ˈbɔlɐ'
```

### Coda sibilants

The standard realisation of a coda sibilant is the *chiado*: /s/ becomes [ʃ] and /z/ becomes [ʒ] (Mateus & d'Andrade 2000, ch. 2). The `PT_CODA_S_HUSH` and `PT_CODA_Z_HUSH` rules state it. The sandhi rule `PT_CODA_S_VOICING` voices [ʃ] to [ʒ] before a voiced consonant in the next word.

```python
pt.transcribe("pasta")      # 'ˈpaʃtɐ'
pt.transcribe("casa")       # 'ˈkazɐ'
pt.transcribe("os dedos")   # 'oʒ ˈdɛduʃ'
```

The `pt-PT-x-*` dialect specs inherit these rules by id. The varieties that keep an alveolar coda /s/ (`pt-AO`, `pt-CV`, `pt-GW`, `pt-MZ`, `pt-ST`, `pt-TL`) override `PT_CODA_S_HUSH` and `PT_CODA_Z_HUSH` by id with [s] and [z].

### Processes outside the rule list

European Portuguese unstressed vowel reduction (/a/ to [ɐ], /e/ to [ɨ], /o/ to [u]) lives in the pre-lexical map. The `nucleus_stressed`, `nucleus_unstressed`, `pretonic` and `word_final` positions state it, so no allophone rule repeats it. Intervocalic spirantisation of /b d ɡ/ is a real process (Mateus & d'Andrade 2000), and the spec does not encode it. Every `pt` gold set is broad and transcribes the stops. Dialect features such as the northern apico-alveolar coda [s̺] belong in the `pt-PT-x-*` specs.

## Multi-pass feeding (`allophone_passes`)

One pass reads the neighbours of every rule from the state before the pass. So two rules in one pass cannot feed each other, and a rule that needs another rule's output never sees it. Brazilian Portuguese shows the problem. The unstressed final ⟨-es⟩ and ⟨-os⟩ raise to [i] and [u] (`BR_RAISE_FINAL_ES`, `BR_RAISE_FINAL_OS`). Then /t d/ must affricate before the raised [i]. In one pass, the affrication rule reads the vowel before raising and does not fire.

A spec sets `allophone_passes: N` to run the compiled pass N times. The default is 1. Each pass rebuilds the segment context from the output of the pass before it, so in pass 2 the raised vowel feeds the affrication:

```python
br.transcribe_word("estes")                                     # 'ˈest͡ʃis'
br.transcribe_word("dentes")                                    # 'ˈdẽt͡ʃis'
br.transcribe_word("gatos")                                     # 'ˈɡatus'
G2P("pt-BR", apply_allophony=False).transcribe_word("estes")    # 'ˈestes'
```

The count is fixed, so a rule set cannot loop. The field is `NOT_INHERITED`. A second pass can fire a rule that is not idempotent again, so each spec states its own count and checks it against its own gold. `pt-BR` and each regional `pt-BR-x-*` spec declare 2.

## Worked example: Arabic emphasis spread

Emphasis spread, or *tafkhim*, is pharyngealisation that radiates from an emphatic consonant onto the adjacent vowels. It backs /a i u/ to [ɑ ɪ ʊ] (Watson 2002, *The Phonology and Morphology of Arabic*, ch. "Emphasis", Davis 1995, *Linguistic Inquiry* 26(3)).

The `arb` spec (Classical and Modern Standard Arabic) is the root of the `graphemes_base` chain of the Arabic family. It declares the `AR_EMPHASIS_SPREAD_*` rules over the `emphatic` class, for /a aː i iː u uː/ before and after an emphatic. Every descendant inherits them.

```python
ar = G2P("arb")
ar.transcribe_word("صَبَرَ")   # 'ˈsˤɑbara'
ar.transcribe_word("طَالِب")   # 'ˈtˤɑːlib'
ar.transcribe_word("صُوف")    # 'ˈsˤʊːf'
ar.transcribe_word("كَتَبَ")   # 'ˈkataba'
```

The spread is local and reaches only the adjacent vowel. Watson also reports spread across several segments, and in some dialects an intervening high front vocoid /i j/ blocks it (Watson 2002 §2.4.2). That word-domain spread needs context beyond one grapheme.

The `ar` spec and its descendants also carry the `AR_EMPH_BACK_A_*` and `AR_EMPH_BACK_AA_*` rules, which key on a listed set of emphatic phonemes. They are not redundant with the class rules. Only they reach the fused nisba and gemination grapheme ⟨َيي⟩ [ajj], a single token with several phonemes that the grapheme class cannot see inside.

## Marker graphemes: delete a vowel while mutating a neighbour

Some orthographies use a vowel letter as a diacritic on an adjacent consonant. The letter adds a feature to its neighbour and is otherwise silent. Goidelic slender and broad marking (*caol* and *leathan*) is the main case. A written ⟨i⟩ or ⟨e⟩ beside a consonant marks that consonant as palatalised (Broderick 1984-86, *A Handbook of Late Spoken Manx*, vol. 3, Thomson 1992, "The Manx Language", in MacAulay (ed.), *The Celtic Languages*, ch. 3). The Cyrillic soft sign ⟨ь⟩ and similar Slavic and Uralic letters have the same shape.

An ordinary rule cannot express this, because `surface` rewrites only the rule's own phoneme. The two-rule technique of the nasal vowels does not transfer. The consonant's rule would need to know whether its neighbouring vowel is about to delete itself. The grapheme-class lookups read the slots before the rescorer runs, so no class answers that question. The consonant rule would have to copy the vowel rule's conditions and keep the two in step.

`mutates_neighbor` holds an IPA modifier such as `"ʲ"`, and `mutates_neighbor_side` is `"preceding"` or `"following"`. One rule on the marker vowel rewrites its own slot and adds the feature to the named neighbour. One firing produces both effects, so they cannot go out of step. The two fields go together, and the schema refuses one without the other.

The `gv` spec declares two such rules. The rule `GV_SLENDER_ONSET_CONSONANT` deletes an ⟨i⟩ or ⟨e⟩ between an onset consonant and a vowel. It palatalises the consonant before it. The rule `GV_SLENDER_FINAL_N` palatalises a word-final ⟨n⟩. It keeps the marker as [ə], because most Manx transcriptions show a schwa there:

```json
{
  "id": "GV_SLENDER_FINAL_N",
  "phonemes": ["i", "e"],
  "surface": "ə",
  "followed_by_phoneme": ["n"],
  "followed_by_2": "word_boundary",
  "mutates_neighbor": "ʲ",
  "mutates_neighbor_side": "following"
}
```

```python
gv = G2P("gv")
gv.transcribe_word("giare")                                   # 'ɡʲare'
gv.transcribe_word("dowin")                                   # 'dowənʲ'
G2P("gv", apply_allophony=False).transcribe_word("giare")     # 'ɡiare'
```

The rescorer evaluates `mutates_neighbor` from the affected slot. It runs the marker rule's match against a rebuilt context of the marker slot, and it reads the shared slot state from before the pass. So the result does not depend on which slot the pass reaches first. A stress condition on such a rule reads the stress context of the affected slot, because this layer has no stress array for the marker itself. The Goidelic and Slavic marker cases do not condition on stress.

The mechanism names no language, and `allophony.py` does not mention Goidelic or Manx. It applies wherever a marker grapheme deletes itself and adds a feature to a neighbour.

---
[← Lattice PER](lattice_per.md) · [Home](../index.md) · [Positional Graphemes →](positional_graphemes.md)
