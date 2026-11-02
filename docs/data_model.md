# Data Model

The package rests on a small set of types in `orthography2ipa/types.py`. Each type is a frozen dataclass or an enum. The loader also deep-freezes the dict and list fields of a `LanguageSpec`. So `registry.get()` hands out one shared, cached object that no caller can change. An attempt to change a grapheme list raises `TypeError`.

Every authored string in a spec is NFC-normalised. That covers graphemes, allophones, `word_exceptions`, notes and source titles, and `tests/test_data_nfc.py` checks each data file. The engine also normalises its own output to NFC.

`orthography2ipa/data/SCHEMA.md` names every JSON key the loader reads. This page describes the Python objects that the loader builds from those keys.

## `Grapheme2IPA`

```python
Grapheme2IPA = Dict[str, List[str]]
```

A `Grapheme2IPA` maps an orthographic string to a list of IPA phoneme strings. A key is a grapheme as the orthography of the language writes it. It can be a single letter (`"a"`, `"ñ"`, `"ü"`) or a digraph (`"ch"`, `"ll"`, `"lh"`, `"nh"`, `"rr"`). It can also be a trigraph, such as German ⟨sch⟩, English ⟨tch⟩ or French ⟨eau⟩. Some languages also key a vowel sequence (`"ai"`, `"ie"`, `"ua"`) where it needs its own reading.

A value lists the phonemes the grapheme can stand for, the most common first:

```python
import orthography2ipa
orthography2ipa.get("en-GB").graphemes["c"]    # ['k', 's']: cat, city
orthography2ipa.get("en-GB").graphemes["th"]   # ['θ', 'ð']: think, this
orthography2ipa.get("es-ES").graphemes["c"]    # ['k', 'θ']: /k/ before a, o, u and /θ/ before e, i
orthography2ipa.get("es-ES").graphemes["ll"]   # ['ʝ']: yeísmo
orthography2ipa.get("pt-PT").graphemes["lh"]   # ['ʎ']: one reading only
orthography2ipa.get("pt-PT").graphemes["x"]    # ['ʃ', 'ks', 'z', 's', 'ɡz']
```

The order matters. The beam search of `PhonetokTokenizer` gives the first value the lowest cost, so it is the reading the engine picks when nothing else decides. [candidate_scoring.md](candidate_scoring.md) describes how weights and positional overrides change the cost.

## `AllophoneMap`

```python
AllophoneMap = Dict[str, List[str]]
```

An `AllophoneMap` maps an underlying phoneme to the surface forms it takes in context. A key is an IPA phoneme, and a value lists its attested allophones:

```python
import orthography2ipa
orthography2ipa.get("en-GB").allophones["t"]   # ['t', 'tʰ', 'ʔ', 'ɾ']
orthography2ipa.get("es-ES").allophones["b"]   # ['b', 'β']: β between vowels
orthography2ipa.get("es-ES").allophones["n"]   # ['n', 'ŋ', 'm']: place assimilation
```

The map records which allophones exist. The distance metrics and the inventory functions read it. It does not say which allophone occurs where. The spec's `allophone_rules` make that choice, and the engine applies them after it selects the phonemes ([allophony.md](allophony.md)). A spec that declares graphemes and no allophones gets an identity map: each phoneme a grapheme can produce is its own allophone.

### How the two maps relate

The two maps are two layers of description:

```
orthography → graphemes → underlying phonemes → allophones → surface forms
  "butter"     b,u,tt,e,r     /b ʌ t ə r/       [b ʌ ɾ ə r]
```

The grapheme map goes from orthography to phonology. The allophone map goes from phonology to phonetics. In American English, *butter* passes through both. The grapheme step maps ⟨tt⟩ to /t/, and the allophone step realises /t/ as the flap [ɾ] between vowels.

## `LanguageSpec`

A `LanguageSpec` holds all the data for one language, dialect, historical stage or clade node. The fields fall into these groups. `SCHEMA.md` documents the JSON key behind each one.

| Group | Fields | What they hold |
| :--- | :--- | :--- |
| Identity | `code`, `name`, `script`, `script_type`, `orthography_kind` | The BCP-47 code, the display name, the script and its type, and what kind of writing the graphemes are |
| Cross-references | `iso639_3`, `glottolog_code`, `wikidata_qid`, `phoible_id`, `wals_code` | Identifiers in other catalogues |
| Classification | `family`, `family_path`, `clade`, `parent`, `ancestors` | The derived family path, the clade flag and the typed ancestry |
| Sound and spelling | `graphemes`, `allophones`, `phonemes`, `positional_graphemes`, `grapheme_weights` | The two maps, the declared inventory, the context-sensitive overrides and the candidate weights |
| Whole words and endings | `word_exceptions`, `grammatical_endings` | Overrides for an irregular set of words, and suffix readings at the word end |
| Script behaviour | `inherent_vowel`, `inherent_vowel_final`, `virama_final_vowel`, `dependent_vowels`, `preposed_vowels`, `coda_no_inherent_vowel`, `codas`, `consonant_nuclei`, `vowel_graphemes`, `fold_diacritics`, `optional_marks`, `word_internal_apostrophe`, `doubled_letters_geminate`, `collapse_geminates`, `trailing_vowel_axis_digraphs`, `constrain_onsets` | How the tokenizer and the syllabifier read the script |
| Rules | `stress`, `allophone_rules`, `allophone_passes`, `sandhi_rules`, `tone_rules`, `tone_inventory`, `tone_marks_syllable_final`, `plugins` | Stress placement, post-lexical rewrites, cross-word rules, tone and the plugins a stage must use |
| Provenance | `quality`, `sources`, `wikipedia`, `urls`, `notes`, `audit`, `valid_ceiling` | The quality tier, the citations, the notes and the recorded audit results |
| Place and time | `location`, `timespan`, `orthography_standard` | A representative point, the attestation period and the official spelling norm |

`positional_graphemes` defaults to `None` in the dataclass, and `__post_init__` turns it into `{}`. `quality` defaults to `RESEARCH` and `script_type` to `ALPHABET`. [positional_graphemes.md](positional_graphemes.md) covers the positional overrides.

### `phonemes`: the inventory, stated directly

`phonemes` is the phoneme inventory of the language: the sounds it has, declared apart from `graphemes`. The sounds of a language are not a property of its writing system. Most languages of the world have little or no writing, and PHOIBLE catalogues inventories for thousands of them. A logographic script encodes no sound at all. So a reading of the inventory out of the spelling fails in both cases.

```python
import orthography2ipa
ine = orthography2ipa.get("ine")        # Proto-Indo-European, never written
len(ine.phonemes)                       # 30 reconstructed phonemes, declared
han = orthography2ipa.get("zh-Hani")    # Chinese in Han script
dict(han.graphemes)                     # {}: no grapheme-to-IPA rule exists to write
len(han.phonemes)                       # 60: the phonology is known regardless
```

When `phonemes` is empty, the inventory comes from `graphemes`: each phoneme that any grapheme can produce. A spec that says nothing keeps the inventory its grapheme map implies. That derivation is a fallback, not the definition, because it reads the sounds out of the spelling. `distance._extract_phonemes` applies the rule, so the declared inventory wins and the grapheme map is the fallback. Every phonological metric builds on it.

A spec must declare `graphemes` or `phonemes`, and it may not leave both empty. Logographic scripts and unwritten languages show that a language can lack graphemes. No language lacks both sounds and spelling. `tests/test_language_integrity.py` checks this rule.

### `orthography_kind`: native scripts, romanizations and transliterations

The `graphemes` map says that some writing produces some sounds, and `orthography_kind` says which writing. Han characters, Pinyin and Buckwalter ASCII make three different claims, and a consumer must be able to tell them apart.

| `orthography_kind` | What the graphemes are | Standards body | Example |
| :--- | :--- | :--- | :--- |
| `native` | The writing system of the language | Usually | `zh-Hani` (Han), `ar` (Arabic), `en-GB` (Latin) |
| `romanization` | An alternative orthography that people read and write | Yes | `zh` (Pinyin, ISO 7098) |
| `transliteration` | A lossless machine re-encoding of another script | No, and that absence is the tell | `ar-Latn-buckwalter` |

```python
import orthography2ipa
orthography2ipa.get("zh").orthography_kind                   # OrthographyKind.ROMANIZATION
orthography2ipa.get("zh-Hani").orthography_kind              # OrthographyKind.NATIVE
orthography2ipa.get("ar-Latn-buckwalter").orthography_kind   # OrthographyKind.TRANSLITERATION
```

`native` is the default. A spec that says nothing claims to read the own script of the language.

#### A romanization is an orthography, a transliteration is an encoding

A romanization is a real orthography of the language. Schools teach Pinyin, the law sets it, and ISO 7098 standardises it. A Chinese primary-school child writes it. It is also a plain alphabet, which is why rules can transcribe it where they cannot transcribe the native script:

```python
from orthography2ipa import G2P
G2P("zh").transcribe("beijing")   # 'peitɕiŋ': Pinyin in, IPA out
```

So `zh` reads Pinyin, not Hanzi, and says so. The conversion of Han text to Pinyin is a dictionary lookup (CC-CEDICT and similar), and this library does not do it.

A transliteration re-encodes another script for machines. Nobody reads Buckwalter as a language. It takes every property of the script it re-encodes, and the limits come with it.

#### Buckwalter cannot recover the vowels

A transliteration that changed the pronunciation would not be a transliteration. `ar` and `ar-Latn-buckwalter` write the same word in two encodings and give one IPA:

```python
from orthography2ipa import G2P
G2P("ar").transcribe("كَتَبَ")                    # 'ˈkataba': vocalised Arabic
G2P("ar-Latn-buckwalter").transcribe("kataba")   # 'ˈkataba': the same IPA
```

A re-encoding cannot recover what the script never wrote. Unvocalised Buckwalter is as hard to read as unvocalised Arabic. Both omit the short vowels, and nothing puts them back:

```python
from orthography2ipa import G2P
g = G2P("ar-Latn-buckwalter")
g.transcribe("kataba")   # 'ˈkataba'
g.transcribe("ktb")      # 'ˈktb': the bare form has no vowels
```

#### The native Han spec has no grapheme map

A Han character does not encode sound. Its reading depends on the word it sits in. So `zh-Hani` has no grapheme map at all, and that empty map is the answer, not a gap:

```python
import orthography2ipa
han = orthography2ipa.get("zh-Hani")
dict(han.graphemes)   # {}: there is no grapheme-to-IPA rule to write
len(han.phonemes)     # 60: the phonology is declared
```

The input contract for Han text is a dictionary, which is a lexical lookup and not a phonological rule. That is a fact about the writing system, not a defect of the engine. The romanization avoids the problem, because Pinyin is an alphabet that rules can read. `zh-Hani` also shows why the [phoneme inventory](#phonemes-the-inventory-stated-directly) is declared apart from the graphemes. It has no orthography the rules can read, and its phonology is complete.

### `vowel_graphemes`: overriding a closed-inventory consonant letter

`orthography2ipa.vowels.grapheme_is_vowel` treats the Latin, Greek and Arabic-harakat letter sets as closed inventories. A Latin letter outside them, such as ⟨w⟩, ⟨y⟩ or ⟨r⟩, is a consonant letter by construction, whatever IPA a spec maps it to. This is deliberate. Czech syllabic ⟨r⟩ and English ⟨y⟩ must not become vowels because their IPA output is a vowel somewhere else.

Some orthographies do use one of those consonant letters to spell a vowel: Hmong RPA ⟨w⟩ is /ɨ/, and Welsh ⟨w⟩ is /ʊ, w/. `vowel_graphemes` is the exception for one spec. It is a tuple of whole grapheme strings, matched in full and not by the first character, that the spec declares vowel letters. The check reads it before the closed inventories:

```python
import orthography2ipa
orthography2ipa.get("mww").vowel_graphemes   # ('w',)
```

An empty tuple, the default, gives the closed-inventory answer. The field is `OWN_ONLY`, like `script_type` and `optional_marks`. A dialect that shares the grapheme table of a parent does not get the script exceptions of that parent.

### Derived classification: `family`, `family_path`, `clade`

No spec author writes `family`. Families are clade nodes in the ancestry graph: specs with `clade=True`, which carry classification and nothing else. The loader walks the `parent` chain upwards and collects the names of the clades it passes, broadest first, into `family_path`. `family` is that path joined with `" > "`:

```python
import orthography2ipa
orthography2ipa.get("pt-BR").family_path   # ('Indo-European', 'Italic', 'Romance', 'Ibero-Romance')
orthography2ipa.get("pt-BR").family        # 'Indo-European > Italic > Romance > Ibero-Romance'
orthography2ipa.get("pt-BR").clade         # False
```

A spec can still carry an explicit `family` string, and that string wins over the derived one. The exception exists for groupings that are not genetic clades: creoles, constructed languages, isolates and unclassified languages. `available_codes()` leaves out the clade nodes unless you pass `include_clades=True`. [ancestry.md](ancestry.md#clade-nodes-and-the-derived-family) describes the clade graph.

### `Location`, `OrthographyStandard`, `TimeSpan`

| Type | Fields | Purpose |
| :--- | :--- | :--- |
| `Location` | `latitude`, `longitude`, `source`, `notes` | A representative point for the variety. It feeds `geographic_distance`. The point of a clade is a centroid of its range. |
| `OrthographyStandard` | `name`, `authority`, `year`, `url`, `notes` | The official published spelling norm, when one exists. It belongs to the language, not to each dialect. A dialect that spells by the norm of its standard language omits the field, and consumers walk the ancestry chain. |
| `TimeSpan` | `start_year`, `end_year` | The attestation period. It decays ancestry weights across time and drives `temporal_distance`. |

```python
import orthography2ipa
orthography2ipa.get("gl-ES").orthography_standard.authority
# 'Real Academia Galega / Instituto da Lingua Galega'
orthography2ipa.get("ca").location.latitude   # 41.453
```

### The `parent` and `ancestors` fields

A spec can state its parent in two ways. `parent` is a string shorthand, and `ancestors` is the full typed tuple of `Ancestor` objects. If `ancestors` is empty and `parent` is set, `__post_init__` makes a `PARENT` ancestor with weight 1.0. If `parent` is empty and `ancestors` holds a `PARENT` entry, `__post_init__` sets `parent` from it.

Give a new language or dialect the full `ancestors` tuple, because it carries the most data. A dialect that differs little from its parent can use `parent` alone.

### Accessor methods and properties

```python
import orthography2ipa
from orthography2ipa.types import AncestorRole, GraphemePosition
spec = orthography2ipa.get("es-ES")
spec.primary_parent                         # 'es-ES-x-medieval'
spec.get_ancestors()                        # every ancestor
spec.get_ancestors(AncestorRole.SUBSTRATE)  # the substrate ancestors only
spec.substrate_codes                        # ('xaq',)
spec.superstrate_codes                      # ('got',)
spec.contact_codes                          # every non-parent ancestor: ('xaq', 'got', 'xaa')
spec.resolve_grapheme("b", GraphemePosition.INTERVOCALIC)   # ['β']
spec.has_positional_data()                  # True
spec.positional_grapheme_keys()             # frozenset of the graphemes with overrides
spec.positions_for_grapheme("b")            # (GraphemePosition.INTERVOCALIC,)
```

## Inheritance between specs

A dialect often shares most of its data with a base variety. The JSON of the dialect names that base with a `*_base` key, such as `graphemes_base` or `allophones_base`, and states only what differs. The loader in `json_loader.py` resolves the base first and then applies the own values of the dialect. `FIELD_INHERITANCE` in `types.py` sets the mode for each field:

| Mode | Behaviour | Fields |
| :--- | :--- | :--- |
| `BASE_MERGE` | The own values overlay the values of the base key by key | `graphemes`, `allophones`, `positional_graphemes`, `word_exceptions`, `grammatical_endings` |
| `OVERLAY_BY_ID` | The rules of the base come first, in order. An own rule with the same `id` replaces one, and an own rule with a new `id` goes at the end | `sandhi_rules`, `allophone_rules` |
| `BASE_SCALAR` | The value follows the `graphemes_base` edge unless the spec states it | `constrain_onsets`, `word_internal_apostrophe` |
| `BASE_BLOCK` | A spec that states the block keeps it whole. A spec that does not takes the block of its `graphemes_base`, else of a `parent` that is the same language (same or no `iso639_3`). `false` takes no block | `stress` |
| `NOT_INHERITED` | Each file states its own value on purpose | `grapheme_weights`, `allophone_passes` |
| `OWN_ONLY` | The field never takes part in inheritance | Identity, classification, bibliography and script fields, such as `code`, `name`, `sources`, `timespan`, `vowel_graphemes` |

Each `*_base` key can name a different base, and the loader resolves a chain of bases recursively. A field added to `LanguageSpec` must have an entry in `FIELD_INHERITANCE`. [adding_a_language.md](adding_a_language.md) shows a dialect file that uses these keys.

## `AncestorRole`

```python
class AncestorRole(Enum):
    PARENT          = "parent"
    PARENT_DIALECT  = "parent_dialect"
    PROTO_LANGUAGE  = "proto_language"
    ANCESTOR        = "ancestor"
    SUBSTRATE       = "substrate"
    SUPERSTRATE     = "superstrate"
    ADSTRATE        = "adstrate"
    LEXIFIER        = "lexifier"
    CREOLE_BASE     = "creole_base"
    RELATED         = "related"
```

`AncestorRole` names the kind of historical relation between a language and an ancestor.

| Role | Definition | Example | Typical weight |
| :--- | :--- | :--- | :--- |
| `PARENT` | Primary genetic descent | Latin to Spanish | 0.70 to 1.00 |
| `PARENT_DIALECT` | Direct dialectal ancestor in the same language | A regional variety that descends from a broader standard | |
| `PROTO_LANGUAGE` | Reconstructed common ancestor at the top of a lineage | Proto-Indo-European, Proto-Germanic, Proto-Semitic | |
| `ANCESTOR` | Earlier stage of the same lineage that is not the immediate parent | Old Spanish in the ancestry of modern Spanish | |
| `SUBSTRATE` | Language of the population that was there first | Basque substrate in Castilian | 0.05 to 0.30 |
| `SUPERSTRATE` | Language of a dominant group, later absorbed | Frankish superstrate in French | 0.10 to 0.40 |
| `ADSTRATE` | Contact influence from a neighbouring language of equal status | Arabic adstrate on Ibero-Romance | 0.05 to 0.20 |
| `LEXIFIER` | Vocabulary source in creole or pidgin formation | Portuguese lexifier of Papiamento | 0.50 to 0.80 |
| `CREOLE_BASE` | Grammatical source in creole formation | West African languages as a creole base | 0.20 to 0.50 |
| `RELATED` | Sister language with shared features and no direct descent | Typological comparison, not inheritance | |

A language has at most one `PARENT`, which is its primary line of descent. A reconstructed proto-language has none.

A substrate is the language of the original population that took up the incoming language. Its effects show as phonological features that depart from the parent. The Basque substrate in Castilian is the classic explanation for the change of *f-* to *h-* (Latin *filium*, Spanish *hijo*).

A superstrate is a prestige language whose speakers shift to the local language in the end, but leave phonological and lexical traces. Frankish gave vocabulary, and possibly phonological features, to Old French.

An adstrate is a neighbouring language of about equal social status that keeps up its influence. Arabic was an adstrate on medieval Ibero-Romance and gave more than 4,000 loanwords to Spanish and Portuguese.

## `Ancestor`

```python
@dataclass(frozen=True)
class Ancestor:
    code: str            # language code of the ancestor
    role: AncestorRole   # kind of relation
    weight: float = 0.5  # contribution weight in [0.0, 1.0]
    notes: str = ""      # optional notes
```

The weights in the role table are guidelines from the `Ancestor` docstring. They need not sum to 1.0. A weight is an approximate phonological contribution, not a share of heritage.

```python
from orthography2ipa.types import Ancestor, AncestorRole
Ancestor(code="la-x-hispania", role=AncestorRole.PARENT, weight=0.80,
         notes="Primary descent from Hispanic Vulgar Latin")
# Ancestor('la-x-hispania', parent, w=0.80)
```

## `QualityTier`

| Value | Meaning |
| :--- | :--- |
| `STUB` | Code, name, script and a parent for the clade chain, with no phoneme data |
| `SKELETON` | Graphemes and allophones from auto-generation, not validated |
| `RESEARCH` | Validated against published phonology, with positional rules |
| `PRODUCTION` | Full coverage, regression tests and cited sources |

[quality_tiers.md](quality_tiers.md) sets the bar a spec must clear for each tier.

## `ScriptType`

| Value | Scripts |
| :--- | :--- |
| `ALPHABET` | Latin, Cyrillic, Greek, Armenian, Georgian |
| `ABJAD` | Arabic, Hebrew: the consonants come first and the vowels are optional |
| `ABUGIDA` | Devanagari, Bengali, Tamil, Thai: each consonant carries an inherent vowel |
| `SYLLABARY` | Kana, Cherokee |
| `LOGOGRAPHIC` | Hanzi and other CJK ideographs |
| `FEATURAL` | Hangul |
| `MIXED` | Japanese, which mixes logographs and a syllabary |
| `RECONSTRUCTION` | An IPA-based reconstruction for an extinct language |

## `LinguisticSource`

A `LinguisticSource` is one bibliographic reference. Its fields are `id`, `author`, `year`, `title`, `publisher`, `url`, `doi`, `wikipedia_url`, `pages` and `notes`.

## `SandhiRule`

A `SandhiRule` is one cross-word rule. Its fields are `id`, `name`, `left_context`, `right_context`, `transform`, `right_transform`, `obligatory` and `notes`.

A word boundary has two sides, and a rule can rewrite either side or both. `transform` replaces the `left_context` match in the left word. A process that the right side conditions (regressive) needs this shape, such as the voicing of coda /s/ in European Portuguese. A `None` value leaves the left word as it is.

`right_transform` replaces the `right_context` match in the right word. A process that the left side conditions (progressive) needs this shape. Catalan phrase-level spirantization is one example: the initial /b d ɡ/ of the next word lenites after a continuant, so *de decidir* gives `də ðəsiˈði`. Spanish and Galician have the same shape. `None`, the default, leaves the right word as it is.

The side that a rule rewrites is its target, which is not the same as its direction of conditioning. A rule must declare at least one of the two transforms, and the schema rejects a rule that declares neither. Such a rule would match a boundary and change nothing.

The two sides resolve apart from each other, and the first matching rule wins on each side. So one boundary can voice the coda of the left word and lenite the onset of the right word: *els dos* gives `əlz ˈðos`. The contexts always match against the original words, so the side that fires first cannot hide the trigger of the other.

## `StressRules.diphthongs`

The bundled syllabifier counts each maximal run of vowel letters as one nucleus. That works for a language whose vowel runs are all diphthongs. It fails where the orthography also writes hiatus. The `diphthongs` list names the vowel sequences that form one nucleus, and every other vowel letter in a run becomes a nucleus of its own. So Catalan *ciutat* has the diphthong ⟨iu⟩ (`siwˈtat`), while *tenia* splits into te-ni-a (`təˈniə`). An empty list, the default, merges the whole run.

The syllable count matters for more than the stress mark. In a language with vowel reduction that depends on stress, a wrong count reduces the wrong vowel and the whole word is wrong. Without its `diphthongs` list, Catalan *tenia* comes out `ˈtɛniə`.

## `StressRules.ipa_diphthongs`

The engine writes the stress mark into the transcription, so it also divides the IPA into syllables. By default it splits the IPA with `diphthongs`, the orthographic list. That fails for a language whose transcription writes a diphthong with a glide. Portuguese ⟨ui⟩ is [uj], so an IPA [ui] comes only from a hiatus such as ⟨uí⟩. With the orthographic ⟨ui⟩ entry, ⟨proíbe⟩ /pɾuibɨ/ falls into two syllables and the mark lands on the first: `ˈpɾuibɨ`.

`ipa_diphthongs` lists the IPA vowel sequences that form one nucleus. When a spec declares it, the engine splits the transcription with this list and not with `diphthongs`. An empty list makes each IPA vowel its own nucleus, which gives `pɾuˈibɨ`, and `pt-PT` declares that empty list. Leave the field out to keep the orthographic list.

## Lexicon overlay (sidecar `word_exceptions` at scale)

A caller-registered lexicon extends `word_exceptions` to thousands of words, and [lexicon.md](lexicon.md) describes its contract.

---
[← Architecture](architecture.md) · [Home](index.md) · [Language Registry →](registry.md)
