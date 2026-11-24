# o2i IR v1: the compiled intermediate form of orthography2ipa

<!-- agent-hint
covers: the normative format of IR v1, the interpreter stages, the primitive set, versioning and the ruled output changes
source: orthography2ipa/ir/layout.py, orthography2ipa/ir/compiler.py, orthography2ipa/ir/interpreter.py, orthography2ipa/ir/interpreter.lua
generated: no
verify: python3 -I scripts/check_ir_version_doc.py --base origin/dev
see: docs/engine/ir.md, docs/contributing/behaviour_is_data.md, docs/guide/revisions.md
-->

This page is the format reference of the IR. [ir.md](../engine/ir.md) explains the design with a worked example.

## 1. Scope and principles

The IR is a JSON document that holds everything one language needs to turn text into IPA. The Python compiler makes it from a resolved `LanguageSpec`. The compiler reads the spec, its inheritance chain and the engine's phonetic knowledge, and writes plain tables, attribute bits, predicate expressions and ordered rule lists. Nothing in the IR is implied.

The interpreter is a small fixed program. It reads one IR document and one input text, and writes one IPA string. It knows a fixed set of general primitives (section 2.3). It never knows a language, a script, a phoneme class, a feature or a Unicode property. Every phonetic question that the legacy engine asks at runtime becomes, in the IR, a table lookup or an attribute bit that the compiler filled in.

The interpreter never loads a spec, resolves a language code, follows inheritance, reads a Unicode database, computes a logarithm or an exponential, or runs a host-language regular expression. Those steps are compile-time Python: spec loading (`json_loader.py`), the registry (`registry.py`), schema validation (`schema.py`), the inventory (`inventory.py`), the onset grammar and the distinctive features, which come from phonematcher (issue #2490).

The reference semantics are the semantics in this document, not the legacy engine's bytes. Where the legacy engine needs phonetics or a Unicode database at runtime, the IR changes the rule so that the interpreter stays small, and section 9 lists each change with the measurement that rules on it. Every interpreter matches the Python reference interpreter byte for byte. The Python reference interpreter matches the legacy engine except for the ruled changes of section 9.

Three interpreters implement IR v1. The Python reference interpreter is normative: `transcribe()` becomes `compile(spec)` (cached per process and per revision) followed by `interpret(ir, text)`. The Lua interpreter runs inside loom on LuaJIT 2.1 (section 10 gives its size). A C++ interpreter may follow.

Runtime plugins stay outside the IR. Section 3.1 names the point in the stage order where a host may call each one. The Lua interpreter in loom has no host hooks.

## 2. The IR document

### 2.1 Encoding

The document is one JSON object. Its runtime part holds only integers, arrays and objects with string keys from a fixed vocabulary. Every string the interpreter compares or emits is an array of codepoints, held once in the `strings` table and referred to by index. Every number is an integer in the exact range of an IEEE double, `±(2^53-1)`, so LuaJIT reads every value exactly. For loom, the exporter also writes the same structure as a Lua table literal. The JSON document stays the source of truth.

### 2.2 Top level

The canonical document has these top-level fields. `layout.LAYOUT` (`orthography2ipa/ir/layout.py`) is the schema of the runtime fields, and the block below is that schema written out. A test keeps the two equal.

```json
{
  "ir_version": 1, "lang": "pt-PT", "source": {},
  "strings": [], "chars": {"ranges": []},
  "entries": [], "fallback": [], "word": {}, "beam": {}, "allophone_map": [],
  "syllable": {}, "stress": {}, "atoms": {}, "allophony": {}, "sandhi": [],
  "dialect": [], "char_maps": {}, "rewrites": [], "consonant_nuclei": [], "tone": {}, "inherent": {}, "endings": {},
  "primitives": {}, "bits": {}, "debug": {}
}
```

| Field | Meaning and invariants |
|---|---|
| `ir_version` | The format major version. An interpreter refuses a value it does not support (8.3). |
| `lang` | The resolved code. Aliases resolve before compilation. |
| `source` | Provenance: package version, compiler commit, the data ref (8.2), `SPEC_FORMAT_VERSION`, Unicode version. No interpreter reads it, and it is outside the revision hash. |
| `strings` | Every string the runtime fields use, as codepoint arrays sorted by codepoint order. Index 0 is the empty string. |
| `chars` | `ranges`: a sorted list of `[lo, hi, bits]`, the char bits (2.4) of every codepoint from lo to hi. A codepoint outside every range has no bits. |
| `entries` | Grapheme entries: key, candidates, integer costs, entry bits, positional rules (3.3, 3.4). |
| `fallback` | The precomposed characters that are entries only through the decomposition fallback (3.3.2). |
| `word` | Word exceptions, apostrophe handling, geminate collapse, the context-beam flag, clitic and silent stress marks, the word-final virama vowel (3.3.3, 3.5, 3.9, 3.11). |
| `beam` | The tilde char of the nasal splice (3.3.6). |
| `allophone_map` | The `allophones` expansion of candidates (3.3.5). Absent when the expansion is off. |
| `syllable` | Splitter data (3.7). Present when the spec has stress rules or an aperture position. |
| `stress` | Decision and mark placement data (3.8). Absent when the spec has no stress rules. |
| `atoms` | The mark-placement atoms and `_AFFRICATES` (3.6.3, 3.7.3). |
| `allophony` | The allophone rules, their atoms and pass count (3.6). |
| `sandhi` | Cross-word rules (3.10.1). |
| `dialect` | The dialect program (3.10.2). |
| `char_maps` | Codepoint maps: `casefold`, `plain_lower`, `nfd`, `ccc`, `compose` and `presentation` (3.2, 4). |
| `rewrites` | Pattern rewrites of preparation (3.2). |
| `consonant_nuclei` | The consonant letters that spell a nucleus, with that reading, in spec order (3.3.2). |
| `tone` | The computed-tone system (3.9). |
| `inherent` | The abugida inherent vowel (3.3.2). |
| `endings` | Grammatical endings (3.5). |
| `primitives` | The manifest (8.1) as `{name: version}`. Outside the canonical bytes, because the revision hashes the manifest string itself. |
| `bits` | The bit names in bit order: `{"char": [...], "entry": [...]}`. The names are fixed (2.4). |
| `debug` | Readable notes. Interpreters ignore it. Outside the revision hash. |

An object field that a spec does not need is absent, and an interpreter reads an absent object as empty. In the schema below, `s` is a string index, `i` an integer, `sset` a sorted array of distinct string indices, `pat` a compiled pattern (5), `tpl` a template (5), `pred` a slot predicate (2.5), `gate` a spelling gate and `dpred` a dialect predicate (3.10.3), `eset` a sorted array of entry indices, and `opaque` a JSON value written as is. A pair is a two-element array.

<!-- layout-schema:begin -->
```
entries: list of object
entries[].key: s
entries[].cands: list of s
entries[].costs: list of i
entries[].bits: i
entries[].trie: i
entries[].onset: list of s
entries[].positional: list of pair of pred and list of s
fallback: sset
word: object
word.exceptions: list of list of s
word.internal_apostrophe: i
word.apostrophe_elision: i
word.collapse_geminates: i
word.context_beam: i
word.tone_dock: list of s
word.clitic_marks: sset
word.silent_stress_marks: sset
word.virama_final: s
beam: object
beam.tilde: s
allophone_map: list of pair of s and list of s
syllable: object
syllable.diphthongs: list of s
syllable.onset_graphemes: sset
syllable.semivowels: list of list of s
syllable.closed_hiatus: object
syllable.closed_hiatus.pairs: list of s
syllable.closed_hiatus.onsets: list of s
syllable.closed_hiatus.codas: list of s
syllable.closed_hiatus.multi_keys: list of s
syllable.final_diphthongs: object
syllable.final_diphthongs.diphthongs: list of s
syllable.final_diphthongs.finals: list of s
syllable.vowel_letters: sset
syllable.silent_tail: sset
syllable.onsets: object
syllable.onsets.max: i
syllable.onsets.units: list of s
syllable.onsets.velar: sset
syllable.onsets.table: list of list of s
stress: object
stress.mark: s
stress.secondary_mark: s
stress.alternating: i
stress.prefixes: list of s
stress.schwa_rimes: sset
stress.coda_liquid: i
stress.accent2: object
stress.accent2.mark: s
stress.accent2.finals: sset
stress.iambic: object
stress.iambic.max_onset: i
stress.marked: sset
stress.final: list of s
stress.penult: list of s
stress.antepenult: list of s
stress.default: i
stress.cliticless: sset
stress.compound_last: i
stress.mark_diphthongs: list of s
stress.tonic_after_diphthong: list of s
stress.stand_in: s
stress.apply: i
stress.contact_units: list of s
stress.silent_units: sset
stress.ipa_diphthongs: list of s
stress.ipa_count: i
stress.mark_onsets: object
stress.mark_onsets.max: i
stress.mark_onsets.velar: s
stress.mark_onsets.table: list of list of s
stress.weight: object
stress.weight.max_onset: i
stress.weight.superheavy_final: i
atoms: object
atoms.mark: list of s
atoms.affricates: list of s
allophony: object
allophony.passes: i
allophony.atoms: list of s
allophony.geminate: i
allophony.rules: list of object
allophony.rules[].phonemes: list of s
allophony.rules[].out: list of s
allophony.rules[].aware: list of i
allophony.rules[].when: pred
allophony.rules[].slot_when: pred
allophony.rules[].trig_next: i
allophony.rules[].trig_prev: i
allophony.rules[].mutate: s
allophony.rules[].mutate_at: i
allophony.rules[].seg: object
allophony.rules[].seg.initial: i
allophony.rules[].seg.final: i
allophony.rules[].seg.prev: sset
allophony.rules[].seg.next: sset
sandhi: list of object
sandhi[].left: pat
sandhi[].right: pat
sandhi[].obligatory: i
sandhi[].left_out: tpl
sandhi[].right_out: tpl
dialect: list of object
dialect[].gate: gate
dialect[].kind: opaque
dialect[].find: s
dialect[].rep: s
dialect[].pattern: pat
dialect[].template: tpl
dialect[].on: sset
dialect[].off: sset
dialect[].when_on: i
dialect[].map: list of list of s
dialect[].rules: list of list of s
dialect[].when: dpred
char_maps: object
char_maps.casefold: list of pair of i and s
char_maps.plain_lower: list of pair of i and s
char_maps.nfd: list of pair of i and s
char_maps.ccc: list of list of i
char_maps.compose: list of list of i
char_maps.presentation: list of pair of i and s
char_maps.fold: sset
rewrites: list of object
rewrites[].pattern: pat
rewrites[].template: tpl
consonant_nuclei: list of pair of s and s
tone: object
tone.classes: list of pair of s and s
tone.marks: list of pair of s and s
tone.no_mark: s
tone.dead_codas: list of s
tone.table: list of list of s
tone.atoms: list of s
inherent: object
inherent.vowel: s
inherent.final: s
inherent.coda_no: i
inherent.signs: list of pair of s and i
endings: object
endings.table: list of object
endings.table[].key: s
endings.table[].ipa: s
endings.table[].alts: list of s
endings.table[].costs: list of i
endings.suffix: sset
endings.vowels: list of object
endings.vowels[].key: s
endings.vowels[].reduced: sset
endings.vowels[].readings: sset
endings.sources: list of object
endings.sources[].surface: s
endings.sources[].vowels: sset
```
<!-- layout-schema:end -->

### 2.3 The primitive set

The interpreter implements these primitives and no others. A new spec field compiles to them (section 7).

| # | Primitive | What the interpreter does |
|---|---|---|
| 1 | Codepoint map | Replaces each codepoint found in a map with its sequence (3.2). |
| 2 | Pattern rewrite | Runs a compiled pattern (section 5) over a codepoint array, globally or once, and substitutes a template of literals and groups. Used by normalisation and sandhi. |
| 3 | Trie match | Longest match of entry keys at a position. |
| 4 | Attribute bits | Reads a named bit of a char or an entry (2.4). |
| 5 | Predicate expression | Evaluates a small expression tree over a slot context (2.5). Positional rules, allophone rules, tokenizer back-off and stress decisions use it. |
| 6 | Candidate list | Ordered `(string, cost)` pairs with a fixed sort and merge rule (3.3.5). |
| 7 | Beam | Expands slots with integer costs and a total tie order (3.3.6). |
| 8 | Syllable splitter | Splits a sequence by nucleus bits, a diphthong list, hiatus cuts and a licit-onset table (3.7). |
| 9 | Decision list | Returns the first index that a list of tests gives (3.8). |
| 10 | Stage sequencer | Runs the stages of 3.1 in order, skipping a stage whose table is empty. |
| 11 | IPA segmentation | Splits an IPA codepoint array into segments: the longest atom not followed by a modifier, else one base codepoint plus its trailing modifiers (3.6.3). |
| 12 | Word substring | Tests whether the lowercased word holds any string of a set as a substring (2.5). |
| 13 | Spelling gate | Evaluates a sentence-level condition on the joined spelling of the sentence: a pattern search, or the spelling being empty (3.10.3). |
| 14 | Positional literal rewrite | Scans a string left to right for a literal and replaces each match whose position predicate holds, reading the rule's input string (3.10.3). |
| 15 | Gated codepoint map | Maps codepoints left to right under a one-bit state that an on-set sets and an off-set clears (3.10.3). |
| 16 | Aligned word rewrite | Splits the IPA and the spelling into words and, when the counts are equal, rewrites each IPA word by rules keyed to its spelling word (3.10.3). |

### 2.4 Attribute bits

Each char and each entry carries an integer of attribute bits. The bit names and their meanings are a fixed contract of IR v1: an interpreter reads a bit by its name, and `bits` gives the bit number of each name in this IR. The compiler writes the names in the order below. A new bit name is a change of the format, with a new semantics version of the stages that read it (8.1). The compiler fills each bit from the legacy function named.

The compiler always writes every name of both tables below. An interpreter refuses an IR whose `bits.char` or `bits.entry` lacks a name that the interpreter reads, with an error that names the missing bits.

Char bits (`bits.char`):

| Bit | Name | Set when the char |
|---|---|---|
| 0 | `known` | the char is in the IR's char table at all |
| 1 | `space` | `_WS_RE` matches it (3.3.1) |
| 2 | `punct` | `_PUNCT_RE` matches it as one char (3.3.1) |
| 3 | `digit` | `_DIGIT_RE` matches it as one char (3.3.1) |
| 4 | `alpha` | `str.isalpha()` |
| 5 | `letter_or_mark` | Unicode category L* or M* |
| 6 | `combining` | `unicodedata.combining(c) != 0` |
| 7 | `mn_mc` | category Mn or Mc |
| 8 | `a_mark` | `_is_a_mark` |
| 9 | `modifier` | `_is_modifier`: combining, or category Lm or Sk |
| 10 | `orth_vowel` | `is_orthographic_vowel` |
| 11 | `ipa_vowel` | `is_ipa_vowel` |
| 12 | `basic_vowel` | `is_basic_vowel_letter` |
| 13 | `front_letter` | `is_front_vowel` |
| 14 | `length` | in `ːˑ` |
| 15 | `non_syllabic` | in `_NON_SYLLABIC` (inverted breves) |
| 16 | `glide` | in `_GLIDES` of `stress.py` |
| 17 | `offglide` | in `_OFFGLIDES` = `jwɥɰ` |
| 18 | `nasal_carrier` | in `_NASAL_CARRIERS` |
| 19 | `apostrophe` | in `_APOSTROPHES` of `g2p.py` |
| 20 | `hyphen` | in `_HYPHENS` of `g2p.py` |
| 21 | `pause` | in `PAUSE_PUNCTUATION` |
| 22 | `edge_punct` | `_EDGE_PUNCT_CHAR` matches it |
| 23 | `word_letter` | `[^\W\d_]` matches it |
| 24 | `elision_apostrophe` | in `'’`, and the spec elides at apostrophes (3.11) |
| 25 | `virama` | `unicodedata.combining(c) == 9` |
| 26 | `vowel_ipa_set` | in `_VOWEL_IPA` of `g2p.py` |
| 27 | `glide_head` | in `jw` |
| 28 | `elision_h` | in `hH` |
| 29 | `whitespace` | `str.isspace()` |
| 30 | `syllabic_mark` | in `SYLLABIC_MARKS`, set only for an abugida spec (`_is_nucleus`) |
| 31 | `mark_spells_nothing` | an abugida mark that reads as the empty string |
| 32 | `supplies_vowel` | a char of category Mn or Mc, or a char in `dependent_vowels`, whose first reading is not empty, does not start with a combining char, and holds a nucleus (`_supplies_vowel`) |
| 33 | `vowel_phone` | `is_vowel_phone` |
| 34 | `nucleus_base` | the first char of its NFD form is in `IPA_VOWEL_SYMBOLS` |
| 35 | `syllabic` | in `SYLLABIC_MARKS`, for every spec |
| 36 | `liquid` | in `_LIQUIDS` of `stress.py` |
| 37 | `tone_mark` | in `TONE_MARKS` of `tone.py` |

Entry bits (`bits.entry`):

| Bit | Name | Set when |
|---|---|---|
| 0 | `vowel` | `grapheme_is_vowel(key, readings, vowel_graphemes)` |
| 1 | `consonant` | a non-empty key without bit `vowel` |
| 2 | `front` | `grapheme_vowel_axis` is front |
| 3 | `back` | `grapheme_vowel_axis` is back |
| 4 | `palatal` | `is_palatal_consonant` of the first reading |
| 5 | `emphatic` | `is_pharyngealized_consonant` of the first reading |
| 6..11 | `base_a` .. `base_y` | `base_vowel_letter(key[0])` maps to `before_a`; `base_e` to `base_y` likewise |
| 12..16 | `after_a` .. `after_u` | the base letter of the key's first char (its last char for a `trailing_vowel_axis_digraphs` key) maps to `after_a`; `after_e` to `after_u` likewise |
| 17 | `after_front` | that tail char is a front vowel letter, or the key's axis is front |
| 18 | `after_back` | that tail char is a back vowel letter, or the key's axis is back |
| 19 | `silent_final` | the `word_final` positional readings hold the empty string |
| 20 | `transparent_final` | `silent_final` and the key is in `_TRANSPARENT_SUFFIX_GRAPHEMES` |
| 21 | `carries_nucleus` | the first reading holds a char with `is_ipa_vowel` |
| 22 | `spells_nothing` | every reading is empty and the key is a mark, or a letter plus marks |
| 23 | `multi_not_mute_digraph` | a key of 2+ chars outside `_MUTE_E_CONSONANT_DIGRAPHS` |
| 24 | `holds_vowel` | some reading holds an IPA vowel, or a positional reading of the key does |
| 25 | `readings_hold_vowel` | some flat or positional reading holds an IPA vowel |
| 26 | `orth_vowel_first` | the key's first char is an orthographic vowel |
| 27 | `glide_final_key` | a key of 2+ chars that ends in `u` or `i`, starts with a consonant letter, and whose head and tail are both keys |
| 28 | `fallback` | the entry exists only through the decomposition fallback |
| 29 | `cluster_next` | a consonant whose first reading is long or holds 2+ consonant segments |
| 30 | `cluster_prev` | same as `cluster_next` |
| 31 | `coda_nasal_reading` | the first reading starts with a nasal |
| 32 | `has_reading` | the entry has a reading |
| 33 | `glide_vowel_cons` | a `glide_final_key` whose reading before a consonant holds a vowel |
| 34 | `glide_vowel_final` | a `glide_final_key` whose word-final reading holds a vowel |
| 35 | `glide_marker` | a `glide_final_key` whose `before_a` or `before_back_vowel` reading holds `w` or `j` |
| 36 | `takes_inherent` | the key takes the inherent vowel (3.3.2) |
| 37 | `silent_before_consonant` | the `before_consonant` readings are exactly the empty string |
| 38 | `postvocalic` | the key has an `after_vowel` positional entry (3.3.2) |
| 39 | `vowel_inherent` | the readings plus the inherent vowel make a vowel entry |
| 40 | `vowel_inherent_final` | the readings plus the final inherent vowel make a vowel entry |
| 41 | `vowel_sign` | the key is in `dependent_vowels`, or its lowercase form is in `preposed_vowels` (3.3.2) |
| 42 | `preposed` | the lowercase key is in `preposed_vowels`. The compiler refuses a spec whose preposed key has a first reading with no `is_ipa_vowel` char |
| 43 | `preposed_host` | the key can carry a preposed vowel: its readings (its `onset` readings when present) are not empty, the first does not hold a nucleus, and the key is not a vowel sign (3.3.2) |
| 44 | `preposed_open` | a `preposed` key whose first reading ends in a vowel (`_ends_in_a_vowel`) |
| 45 | `silent_head` | a key of 2+ chars whose first char has a non-empty first reading and whose readings equal those of the key without its first char (`_silent_marker_head`) |
| 46 | `head_not_coda` | a `silent_head` key, the spec declares `codas`, and the first reading of the tail is not one of them |
| 47 | `audible` | some reading is not empty |
| 48 | `circumfix_tail` | the first char is category Mn or Mc, or the key is in `dependent_vowels`, and the first reading holds a nucleus |
| 49 | `vowel_nucleus` | the key is in `consonant_nuclei` and `grapheme_is_vowel` holds for the key with its nucleus reading |
| 50 | `prevocalic_backoff` | the key is in `prevocalic_glide_backoff`, and the key without its last char and that last char are both trie keys |

### 2.5 Predicate expressions

A predicate is a JSON array tree. The interpreter evaluates it over a slot context: the word's slots (grapheme tokens), the current slot index i, the written syllables and their stress indices, and during rescoring the current candidate lists.

| Node | Meaning |
|---|---|
| `["and", p...]`, `["or", p...]`, `["not", p]` | Logic. |
| `["exists", k]` | Slot i+k exists. k is any integer. |
| `["ebit", k, b]` | Slot i+k exists and its entry has bit b. |
| `["entry_in", k, set]` | Slot i+k's entry index is in a sorted set of entry indices. |
| `["top_in", k, set]` | The top candidate string of slot i+k is in a sorted set of string indices. |
| `["syll", rel]` | A relation between the written syllable of slot i and the stressed syllable: `has_stress` (the word has a stressed syllable and slot i has a syllable index), `idx_eq_stressed`, `idx_lt_stressed`, `idx_gt_stressed`, `idx_eq_stressed_minus_1`, `idx_in_secondary`, and the aperture relations `open` and `closed` (3.4), which read the open status of slot i and are false when it is absent. Every stress relation but `has_stress` is false when either index is absent. An unknown relation is an error. |
| `["syllpos", k, pos]` | Slot i+k exists and its position is `pos`, one of `onset`, `nucleus` and `coda`. A slot whose entry has bit `vowel` is the nucleus. Else, skip the later slots whose entry has bit `spells_nothing`: when the next slot after them has bit `vowel`, the slot is an onset, and else it is a coda. |
| `["reading_vowel", k]` | Slot i+k exists and the first reading of its token has a char with bit `ipa_vowel`. The reading includes an inherent vowel (3.3.2). An abugida spec lowers "after a consonant letter that carries its inherent vowel" to this node. |
| `["top_nucleus", scope]` | With scope `other`, some slot other than i, and with scope `later`, some slot after i, has a top candidate that holds a nucleus segment. Primitive 11 splits the candidate with no atoms. A segment is a nucleus when its first char has bit `nucleus_base` (the first char of its NFD form is in `IPA_VOWEL_SYMBOLS`) or one of its chars has bit `syllabic` (it is in `SYLLABIC_MARKS`), as `_is_nucleus_segment` does. |
| `["word_final"]` | Slot i is the last slot, or the top candidate of every later slot is the empty string or absent. A context with no candidate lists (S6) has no top candidates, so there the node holds only on the last slot. |
| `["word_in", set]` | The word, lowercased with `char_maps.plain_lower`, is in a sorted set of strings. |
| `["word_has_entry", set]` | Some slot of the word has an entry in the set. |
| `["word_has", set]` | The source word, lowercased with `char_maps.plain_lower`, contains some string of the set as a substring (primitive 12). |
| `["count", k1, k2, p, n]` | At least n slots in i+k1 .. i+k2 satisfy p, with p evaluated at each of those slots. `k1` and `k2` are integers or the words `"start"` and `"end"`, which mean the first and last slot of the word. Slot i itself is skipped when the range holds it and the node has the flag `"others"`. |
| `["top_seg_in", k, edge, set]` | The first (edge 0) or last (edge 1) segment of slot i+k's top candidate is in a set of strings. |
| `["true"]`, `["false"]` | Always, never. |

An unknown node is an error. `count` is the general neighbourhood quantifier. It expresses "the next vowel slot", "any later nucleus" and harmony over a distance without a new node.

### 2.6 Costs

A candidate cost is an integer in micro-nats: `cost = round(-ln(max(w / total, 1e-6)) * 1_000_000)`, from the spec weights by the arithmetic of `weights.py`. Unweighted lists get rank costs `r * 1_000_000`, which match `float(rank)`. The allophone step adds `500_000` per rank, which is exact. The largest weighted cost is 13,815,511. A word of 10,000 slots sums below `1.4e11`, so double addition in LuaJIT is exact.

Rounding moves each weighted term by up to 0.5 micro-nat, and the errors add along a path. Two paths whose float sums differ by less than about 0.5 micro-nat per weighted slot can therefore change order or become equal. Integer equality then sends the pair to the next sort key. This is ruled change 9.7. The n-best order is total: `(integer cost, IPA codepoint order, creation index)`. The first two keys match the legacy final sort. The third makes equal paths with equal IPA deterministic.

## 3. The interpreter

### 3.1 Stage order and host hooks

The order is the legacy order of `G2P.transcribe_detailed`, `_transcribe_word`, `_positional_beam` and `_finalize_word_ipa`.

```
interpret(ir, text, hooks):
  H0  host: <phoneme> markup splits text into plain runs and forced words (markup.py)
  H1  host: Pipeline.expand, per plain run
  H2  host: Pipeline.mark, whole sentence
  H3  host: declared normalize plugins, then the G2P normalizer callable 
  S1  prepared, offsets = prepare(text)                               3.2
  S2  words = group_words(tokenize(prepared), text, offsets)           3.11
  for each word w:
    if forced: ipa = forced IPA; go to S9 with forced = true
    S3  ipa = override(w)                                              3.5
    H4      host: Pipeline.lexicon, interleaved with S3 per key        3.5
    if ipa is none:
      S4  slots = tokenize(w) -> grapheme slots                        3.3
      S5  written syllables, stress index, secondary set of w          3.7, 3.8
      S6  cands = positional(slots)                                    3.4
      H5  host: Pipeline.rescore and declared rescorers, in order
      S7  cands = allophony(cands), allophone_passes times             3.6
      S8  constrain_nasal_carriers; beam; final sort                   3.3
      S8b grammatical ending rewrite of the paths                      3.5
      ipa = best path; if the word has no path, the word itself        9.3
    S9  word finalisation, in this order :
        a computed tone (needs the path)                               3.9
        b geminate collapse (not for overrides)                        3.12
        c virama_final_vowel                                           3.9
        d tone mark docking                                            3.9
        e iambic length                                                3.8
        f stress: weight branch or decision list, then mark placement  3.8
  S10 compound stress                                                  3.11
  H6  host: sentence rescorers 
  S11 sandhi rules                                                     3.10
  H7  host: Pipeline.sandhi or declared sandhi plugins
  S12 join non-empty words with U+0020                                 3.12
  S13 dialect program on the joined string (compile option)          3.10.2
  S14 NFC by table                                                     3.12
```

The steps S9e and S9f do not run for a forced word, for a cliticless word, or when `apply_stress` is false. S7 does not run when `apply_allophony` is false. S11 does not run when `apply_sandhi` is false. These three G2P options and `expand_allophones` are compile options: they change the IR, and so the revision. `on_unmapped` is host behaviour: the reference interpreter reports dropped characters (9.3), and the Python wrapper warns, logs or raises as `g2p.py` does.

### 3.2 Preparation (S1)

The legacy order is `prepare`: NFC, then `fold_diacritics`, then Arabic presentation forms, then gemination. When the spec sets `fold_diacritics`, `char_maps.fold` lists the marks to drop (semantics version `fold`). The fold step decomposes each char by `nfd`, drops every char in `char_maps.fold`, and composes the rest by NFC. Lowercasing happens per character inside the tokenizer and the trie (`_lower`). The interpreter keeps this order:

```
prepare(text):
  text = nfc(text)
  if char_maps.presentation: text = map each char through char_maps.presentation
  for rw in rewrites, in order: text = sub(rw.pattern, rw.template, text)   # primitive 2, global
  return text

nfc(text):                                         # NFC by table
  out = each char replaced by char_maps.nfd[c], else c       # full canonical decomposition
  sort each maximal run of chars with ccc > 0 by ccc, stably   # canonical order, char_maps.ccc
  result = []; starter = -1; last = -1
  for c in out:
    cc = ccc(c)                                                # 0 when absent
    if starter >= 0 and (last < cc or (last == 0 and starter == len(result) - 1)):
      if (result[starter], c) in char_maps.compose: result[starter] = that; continue
    if cc == 0: starter = len(result); last = -1 else: last = cc
    append c to result; if cc == 0: last = 0
  return result
```

`char_maps.nfd` maps a codepoint to its full canonical decomposition, `char_maps.ccc` gives the canonical combining class of each codepoint with a class above 0, and `char_maps.compose` lists the triples `[first, second, composite]` of the primary composites (section 4).

Casefolding stays in the tokenizer: the trie and every key test read `casefold(c)` through the `char_maps.casefold` map, as `_lower` does. The Turkish pairs `I → ı` and `İ → i` are entries of that map for Turkic specs.

**Rewrites.** Gemination is declared data. The compiler writes each declared mark rewrite as a pattern rewrite (primitive 2). The three Arabic shadda regexes and the Gurmukhi addak regex are already patterns of the section 5 subset, with the letter and harakat classes resolved to sets:

```
([LETTER])ّ([HARAKAT])  ->  \1\1\2        # shadda first
([LETTER])([HARAKAT])ّ  ->  \1\1\2        # harakat first
([LETTER])ّ             ->  \1\1          # bare
ੱ+([ਕ-ਹ]਼?)             ->  \1੍\1         # addak (nukta carried)
```

Arabic presentation forms are the codepoint map `char_maps.presentation`: each codepoint of U+FB50 to U+FDFF and U+FE70 to U+FEFF maps to its NFKC form when that form differs. Until the spec has a gemination field, the compiler emits the map and the rules under the legacy conditions: the map for an Arabic-script spec or a spec with a shadda key, the shadda rules for a spec with a shadda key, and the addak rule for a Gurmukhi spec. The top-level `rewrites` holds the rules in order as `{"pattern", "template"}`. The interpreter applies the map, then each rule with `sub` of primitive 2. The rewrite step has the semantics version `rewrite`.

**Positions.** A token's `position` and `length` index the prepared text, as in the legacy engine. Word grouping and the override lookup read the prepared text. An offset map into the caller's text is not in v1 (9.8).

### 3.3 Tokenisation, candidates and the beam (S4, S6, S8)

#### 3.3.1 Token classes

The legacy tokenizer tries, at each position: a whitespace run (`_WS_RE`), a punctuation run that no key claims (`_PUNCT_RE`), a digit run that no key claims (`_DIGIT_RE`), a grapheme key, the decomposition fallback, and else an UNKNOWN character. The IR keeps this order. The three classes are char bits, filled by the compiler from the legacy regexes over every character the spec knows plus ASCII, Latin-1, General Punctuation and the spec's script blocks. A character outside `chars` is UNKNOWN (ruled change 9.2).

#### 3.3.2 Grapheme keys

```
key = trie_longest_match(cps, pos)         # over casefold(c)
```

Then, in the legacy order, each branch whose IR data is present:

1. **Preposed vowel** (primitive `preposed`). The Tai vowels ⟨เ แ โ ใ ไ⟩ and ⟨ເ ແ ໂ ໃ ໄ⟩ are written before the consonant and read after it: Thai ⟨เก⟩ is /keː/. When the matched key has entry bit `preposed`, let `ckey` be the longest match after it. When there is none, the branch does not apply.
   - When `ckey` has bit `silent_head` and its head is the onset, `ckey` becomes its first char. The head is the onset when the vowel key has bit `preposed_open`, `ckey` lacks bit `head_not_coda`, and the keys after `ckey` up to the end of the text are all silent: each lacks bit `audible`, and the first one also lacks bit `spells_nothing`. A position where no key matches ends the walk, and the head is the onset when that char lacks bit `alpha`. So Thai ⟨โหม⟩ is /hoːm/ and ⟨โหมด⟩ is /moːt̚/.
   - When `ckey` lacks bit `preposed_host`, the branch does not apply, and the vowel key goes on to the steps below as an ordinary key.
   - The host readings are the entry's `onset` readings when present, else its `cands`. The compiler writes `onset` from the `word_initial` positional readings when they hold no nucleus and the flat first reading holds one: Lao ⟨ອ⟩ is /ʔ/ in ⟨ເອກ⟩ /ʔeːk̚/.
   - The circumfix tail is the longest match after `ckey` that steps over chars with bit `mark_spells_nothing` once the match has begun. When it has bit `circumfix_tail`, the tail supplies the nucleus (Lao ⟨ເ◌ືອ⟩ /ɯa/), and the host keeps its readings. Else the host readings become every host reading followed by every reading of the vowel key, in that order.
   - The tokenizer appends a token for the vowel key with no readings, then the host token. After a circumfix tail that stepped over a mark, it also appends a token for the raw span of the tail with the tail entry's readings, and goes on after the span. Else it goes on after the host.

   The tokens stay in text order. The silent vowel token is a slot with no candidates, and the positional rule `word_final` reads it (3.4).
2. **Hiatus prefix** (`_hiatus_prefix`), when `syllable` has `closed_hiatus` or `final_diphthongs` and the key has two or more chars and starts with a char with bit `orth_vowel`. The word is the maximal run of chars with bit `letter_or_mark` around the position. The key becomes its shortest prefix `key[:cut]` that is a trie key and whose cut point is a hiatus position of the word (3.7.4).
3. **Prevocalic glide back-off**, for an entry with bit `prevocalic_backoff`. When a char follows the key and has bit `orth_vowel`, drop the key's last char. Limburgish ⟨geweun⟩ reads as ⟨g·e·w·eu·n⟩.
4. **Final glide back-off**, for an entry with bit `glide_final_key`. Let `next` be the char after the key. When `next` has bit `elision_apostrophe` and the char after it has bit `alpha`, step over the apostrophe; then, when that char is a trie key whose `cands` are exactly `[""]` and the char after it has bit `alpha`, step over it too, and let `next` be the char reached. When `next` is absent or lacks bit `orth_vowel`: drop the key's last char unless the entry has bit `glide_vowel_cons` (when `next` exists) or `glide_vowel_final` (at the end). When `next` has bit `orth_vowel` and its casefold is not one char with bit `front_letter`: drop the key's last char when the previous grapheme token's first reading ends in a char with bit `ipa_vowel`, the entry has bit `glide_marker`, and the key's last char plus the casefold of `next` is a trie key.
5. **Consonant nuclei** (primitive `consonant_nuclei`). A letter of `consonant_nuclei` that stands between an onset with no vowel and a coda is the syllable's nucleus: Lao ⟨ພວກ⟩ is /pʰuːək̚/. The compiler writes the table with lowercase keys in spec order.
   - *The nucleus test* at a position p, after the tokens so far: it fails when the table is empty or the syllable already has a nucleus (item 6). Skip the chars with bit `mark_spells_nothing`. The longest match there must be a key of the table. Skip such chars again after it. The longest match there is the coda: it must exist, its first reading must be neither empty nor a nucleus, and the position after it must not supply a vowel (item 6). The test gives the offset of the letter, else -1.
   - *Back-off.* After the steps above, when the table is not empty and the key's first reading is not a nucleus, try each table key in order: when the key ends in it, the rest is a trie key, and the nucleus test at the end of that rest gives that very offset, the key becomes the rest. Thai ⟨ขว⟩ is a cluster in ⟨ขวา⟩ and backs off in ⟨ขวด⟩.
   - *Reading.* The tokenizer keeps the offset that the last inherent-vowel test computed. A table key that starts at that offset reads the table value, takes the vowel status of entry bit `vowel_nucleus`, and skips item 6.
   - Item 6 runs the nucleus test right after the letter, before the virama test. An offset of 0 or more stops the inherent vowel, as a vowel sign does.
6. **Inherent vowel**, when the top-level `inherent` object is present (`vowel`, the optional `final`, and `coda_no` for `coda_no_inherent_vowel`). The compiler decides per entry whether the key takes the vowel, as entry bit `takes_inherent`: its first reading is not empty and not a nucleus, and its key does not read as a mark. A key reads as a mark when its last char is category Mn or Mc, unless the key is a letter plus subjoined letters, medial consonant signs or register shifters, or a letter plus marks that are all in `consonant_marks`. The compiler tests these Unicode names, so the interpreter reads only the bit. At runtime, a following char with bit `virama` is consumed into the token. Else the vowel is appended to every reading unless the next position supplies a vowel, unless `coda_no` holds and the syllable already has a nucleus, or unless a next char exists and the entry has bit `silent_before_consonant`. A word-final consonant whose syllable already has a nucleus takes `final` when it is present. The syllable has a nucleus when, walking back over the tokens, the first token that is not a silent mark and not a non-nucleus reading of an entry with bit `postvocalic` has a nucleus reading. A token whose entry has bit `vowel_sign` also counts as a nucleus in this walk (`_prev_gives_nucleus`), whatever its reading. A nucleus reading holds a char with bit `ipa_vowel` or `syllabic_mark`. A token that takes the vowel also takes the vowel status of its new readings, from entry bit `vowel_inherent` or `vowel_inherent_final`, and every predicate and syllable test reads that status in place of entry bit `vowel`. The `script_type` field has no effect on the output.

   **Vowel signs** (`dependent_vowels`, primitive `vowel_signs`). The next position supplies a vowel when, after skipping the chars with bit `mark_spells_nothing`, one of these holds. First, the text at the position starts with a key of `inherent.signs`. The interpreter tries the signs in list order and the first match decides: it supplies the vowel when its flag is 1. Second, no sign matches and the char at the position has bit `supplies_vowel`. The compiler writes `inherent.signs` from the multi-char entries of `dependent_vowels`, longest first and then by codepoint order. A sign's flag is 1 when the first reading of the key holds a nucleus, and 0 when the key has no reading or its first reading holds no nucleus. A flag of 0 stops the search: the Burmese rhyme ⟨ကန်⟩ is one written unit, so the ⟨က⟩ before it takes no vowel and the output is [kàɴ], not *[ka̰nà]. The single-char entries of `dependent_vowels` reach the char bit: they name the Thai and Lao spacing vowel signs, which are category Lo.

**Decomposition fallback.** `entries` holds, for each precomposed char of the spec's scripts whose NFD pieces are all keys, the first `_MAX_DECOMPOSED_COMBOS = 4` products. Such an entry has entry bit `fallback`, and its char is in the top-level `fallback` list. It is not in the trie: the tokenizer tries it only when no grapheme key matches at the position. The interpreter needs no NFD table for this.

#### 3.3.3 Slot context and per-word tokenization

The legacy engine tokenizes the sentence to group words, then tokenizes each word's surface again (`g2p.py`, `grapheme_tokens`). Branches 1, 3 and 4 read the next character, which differs at a word edge between the two passes. The IR keeps two passes: S2 groups words, S4 tokenizes the word surface alone.

The slot context of a word depends on `word.context_beam`:

- **On.** All grapheme slots of the word form one run. When the IR has a `syllable` object, the interpreter divides the word into written syllables (3.7), and when it has `stress`, it decides the stressed index and the secondary set (3.8). Each slot gets a syllable index by the mapping below, and an aperture status when `syllable.silent_tail` is present (3.4).
- **Off.** The slots split into runs at every token that is not a grapheme token: a punctuation, digit, whitespace or unknown token closes the run before it. A run is the slot context of its slots, so `exists`, `ebit` and the other neighbour nodes do not reach across it. No slot has a syllable index or a stress index, so every `syll` relation is false.

The syllable index of a slot (`_map_tokens_to_syllables`, `g2p.py`) is found by a folded substring search. Fold a string by mapping each char through `char_maps.plain_lower` when its image is one char, and keeping it as is otherwise. Let `owner[k]` be the index of the syllable that holds char k of the joined syllables. With a cursor at 0, for each grapheme token in order: find the folded token text in the folded joined syllables at or after the cursor. When found at k, the index is `owner[k]` (the last syllable when k is past the end), and the cursor moves to k plus the token's length. When not found, or for an empty token, the index is the previous token's index, or 0 for the first token. With no syllables, every index is 0.

#### 3.3.4 Positional candidates (S6)

See 3.4. Its output for each slot is the candidate list of 3.3.5.

#### 3.3.5 Candidate lists

`build_branches` is kept:

```
build(cands, costs, allophone_map):
  out = []
  for rank r, s in cands:
    if allophone_map has s: for a_rank, a in allophone_map[s]: out += (a, costs[r] + 500_000 * a_rank)
    else: out += (s, costs[r])
  keep the lowest cost per string
  sort by (cost, string codepoint order)
```

`cands` start from the token's readings, which differ from the entry's candidates when the token took an inherent vowel (3.3.2). `costs` are the entry's precomputed integer costs (2.6) when the token's readings equal the entry's `cands`. They are rank costs `0, 1_000_000, ...` when a positional reading fired (`positional.py` drops weights then), and also when the token's readings differ from the entry's `cands`. `allophone_map` is the spec's `allophones` map, present only when the IR is compiled with `expand_allophones`. A positional reading puts its candidates first and appends the flat-table candidates it lacks.

After every rescoring step the list is re-sorted by `(cost, string)`.

#### 3.3.6 The beam (S8)

```
beam(slots, width):
  constrain_nasal_carriers(slots)
  B = [([], 0)]
  for slot in slots:
    if slot.cands empty: continue
    B = expand(B, slot.cands, width)             # phonetok.py _expand_beam
  sort B by (cost, ipa codepoints, creation index)
  return B
```

`constrain_nasal_carriers` scans each slot whose only reading is the standalone nasal tilde, walks back over earlier slots while they can be empty, and keeps in each only the empty reading and readings whose carrier tail is in the carrier set (the carrier tail is the char before the split point below; the carrier set is char bit `nasal_carrier`). `expand` (`_expand_beam`) appends each candidate to each path. For the tilde it splices onto the previous non-empty segment when its tail is a carrier: the tilde goes at the split point of the last non-empty segment: walk back from its end over chars with bit `length`, and over chars with bit `combining` that are not the tilde itself (`_splice_nasal_tilde`). The splice also appends an empty segment, and a path with no non-empty segment gets the tilde as a new segment, emits an empty segment when the tail is itself a tilde, and drops the extension otherwise. When no extension survives, it extends without the carrier test. Inside `expand`, paths sort by cost with a stable sort, then truncate to `width`. The creation index is the position of the path in the unsorted extension list: parent rank first, then candidate index. `width` is 1 for greedy search and the requested width for beam search (`G2P._width`).

### 3.4 Positional readings (S6)

The legacy engine computes, for each slot, a list of `GraphemePosition` values in a fixed emission order (`grapheme_positions`), then takes the first emitted position that the grapheme's positional entry declares (`positional_candidates`). So the priority is the emission order, not the spec's key order.

The compiler lowers this into, per entry, an ordered list `[(predicate, candidates)]`. It walks the emission order of `grapheme_positions` and, for each position the entry declares, writes the predicate that makes the legacy function emit it. The interpreter takes the first rule whose predicate holds:

```
positional(slot i):
  for (p, cands) in positional[entry(i)]:
    if eval(p, i): return build(cands ++ flat cands not in cands, rank costs)
  return build(flat cands, entry costs)
```

Lowering of the 40 emitted positions, in emission order:

| Position | Predicate |
|---|---|
| `before_final_vowel` | `["and", ["exists",1], ["ebit",1,vowel], ["ebit",1,silent_final], <slot i+1 is final or last audible>]` |
| `before_a` .. `before_y` | `["ebit",1,base_a]` .. `["ebit",1,base_y]` |
| `before_front_vowel` / `before_back_vowel` | `["ebit",1,front]` / `["and",["not",["ebit",1,front]],["ebit",1,back]]` |
| `before_palatal` | `["ebit",1,palatal]` |
| `word_initial` | `["not",["exists",-1]]` |
| `word_final` (first rule) | `["not",["exists",1]]`, and for a spec with `preposed_vowels` `["and",["not",["exists",1]],["not",["and",["ebit",-1,preposed],["not",["reading_vowel",-1]]]]]`. A slot after a silent preposed vowel token is an onset, so a coda reading does not reach it. |
| `intervocalic` | `["and",["ebit",-1,vowel],["ebit",1,vowel]]` |
| `nucleus_stressed_open` etc. (4) | `["and",<vowel or carries_nucleus>,["syll","open"\|"closed"],["syll","idx_eq_stressed"\|...]]` |
| `open_syllable` / `closed_syllable` | `["and",<vowel or carries_nucleus>,["syll","open"\|"closed"]]` |
| `nucleus_stressed`, `nucleus_secondary`, `nucleus_unstressed`, `first_pretonic`, `pretonic`, `posttonic` | `["syll",...]` relations, gated on `["syll","has_stress"]` |
| `before_mute_e` | `["and",["ebit",0,vowel],["entry_in",2,{e}],["count",3,3,<inflection entry>,0..],...]` written out from `_is_mute_e_slot` |
| `word_final` (second rule) | last audible slot and a previous slot |
| `after_a` .. `after_u`, `after_front_vowel`, `after_back_vowel`, `after_palatal`, `after_vowel`, `after_consonant` | bits of slot i-1, with the `trailing_vowel_axis_digraphs` case precomputed as entry bits |
| `before_vowel` / `before_consonant` | `["ebit",1,vowel]` / `["and",["exists",1],["not",["ebit",1,vowel]]]` |
| `nucleus` | `["ebit",0,vowel]` |
| `default` | `["true"]` |

`syll open/closed` is `_is_open_syllable`, with the semantics version `aperture`. A spec that uses an aperture position gets `syllable.silent_tail`: every lowercased grapheme key of at most `_MAX_SILENT_TAIL = 3` chars that `_silent_word_finally` calls silent. The interpreter then divides the word into written syllables even when the spec has no stress rules. It first folds a final syllable into the one before it when, after the trailing chars without bit `alpha` or `combining` come off and the silent tail is stripped, it holds no char with bit `orth_vowel` (`merge_nucleusless_final_syllable`). A slot index past the merged list maps to its last syllable. For each slot, the open status of its syllable is: strip the trailing chars without bit `alpha` or `combining`; strip the silent tail when a char came off or the syllable is the last; no status when nothing with bit `orth_vowel` is left; else open when the last char has bit `orth_vowel`. The silent tail is stripped longest first, and repeatedly, by lowercased suffix.

The five positions the legacy function never emits (`intervocalic_cross_word`, `onset`, `coda`, `consonantal`, `vocalic`) are inert: the compiler writes no rule for them, and lists them in `debug.inert_positions`. This is ruled change 9.4.

The stress context of S5 comes before this stage. The interpreter runs the decision list of 3.8 on the written syllables: one syllable gives index 0, a cliticless word gives the no-stress sentinel, and `secondary_stress_positions` gives the secondary set. When `stress.alternating` is 1 (spec `secondary_stress = "alternating"`, semantics version `secondary`), the set holds `stressed % 2, stressed % 2 + 2, …` below `stressed - 1`, and it is empty for a word of fewer than 3 syllables or with no stress.

### 3.5 Overrides and grammatical endings (S3, S8b)

The legacy precedence (`_whole_word_override`) is per key, not per source:

```
override(word):
  key = casefold(word without the chars of word.silent_stress_marks)
  keys = [key]; s = strip edge punctuation(key); if s and s != key: keys += [s]
  if word_internal_apostrophe: keys += [k with U+2019 -> ' for k in keys if it has U+2019]
  for k in keys:
    if k in word.exceptions: return it
    if host lexicon has NFC(k): return it                   # H4
  for (apostrophe, host) in elided_hosts(word):
    if override_whole(host) hits: return join(clitic_ipa(word, apostrophe), that)
  return none

elided_hosts(word):                                          # _elided_hosts
  none unless word.apostrophe_elision and word.internal_apostrophe
       and word holds a char with bit apostrophe
  for each i with bit apostrophe at word[i], 0 < i < len(word) - 1:
    host = word[i+1:]; before = the grapheme tokens of word that start before i
    keep (i, host) when word[i-1] has bit alpha, before is not empty,
         the first char of the last token of before lacks bit orth_vowel,
         and host[0] has bit orth_vowel or elision_h
```

The cliticless test (S5) uses the key `nfc(casefold(word))`: the word is cliticless when that key, or its edge-stripped form when that differs and is not empty, is in `stress.cliticless`. When neither holds, the word is cliticless when some host of `elided_hosts(word)` is, by the same key test without a further elided split. A word is never cliticless when the IR has no stress rules or an empty `stress.cliticless`.

So a host lexicon hit on the raw key beats an exception on the stripped key. The interpreter calls H4 inside the loop. Without a host, H4 never hits. Edge punctuation is the char bit `edge_punct` (`_EDGE_PUNCT_RE`).

The elided-clitic path transcribes the clitic with a width-1 beam and joins it to the host's override. The join segments the clitic's IPA with primitive 11 and reads the `ipa_vowel` bit of each segment.

`grammatical_endings` (`match_grammatical_ending`, `positional.py`, and `_apply_grammatical_ending`, `g2p.py`) compile to the top-level `endings` object, with the semantics version `endings`:

| Field | Content |
|---|---|
| `table` | One item per ending: `key`, the rank-1 reading `ipa` (absent when the ending defers rank 1 to the tables), the lower-ranked `alts`, and `costs`, the rank costs of the declared list. |
| `suffix` | The transparent suffix graphemes (`s`, `x`) that the spec silences word-finally. |
| `vowels` | Per grapheme key: the vowel runs of its readings in an unstressed position (`reduced`) and in any position (`readings`). Only keys with a reduced vowel are listed. |
| `sources` | Per allophone surface: the vowel runs of the phonemes that rules rewrite to it. |

`word.silent_stress_marks` holds the stress-mark graphemes that emit nothing. The interpreter matches on the word's grapheme tokens without those marks, then widens the span back over them. It lowercases the tokens and skips one last token when that token is in `suffix`. It then tries each letter cut from the left, so the first hit is the longest ending. It rounds the cut outward to a token start, and it requires at least one token before the span.

For each beam path longer than the span, it replaces the span's segments with one segment, the ending's reading, and joins the span's graphemes. Before that, each vowel run of the reading yields to the path's own vowel for that letter when the reading's vowel is in the letter's `reduced` set. When the path's vowel is not in the letter's `readings`, the one source vowel of `sources` that is in `readings` stands in for it. This happens only when the reading and the span have the same number of vowel runs, and each span segment has at most one. A vowel run is an `ipa_vowel` char plus the `ipa_vowel` and `combining` chars after it. The paths are de-duplicated by IPA. Each alternative is applied to the first unrewritten path at its rank cost, and the list is sorted by cost, keeping the order of equal costs.

### 3.6 Allophony (S7)

#### 3.6.1 Rules

Each allophone rule compiles to one object of `allophony.rules` (2.2):

| Field | Content |
|---|---|
| `phonemes` | The rule's target strings, in the spec's order. |
| `out` | For each target, `_applied(rule, ipa)`: the surface, or the target plus `append`. |
| `aware` | For each target, 1 when some `preceded_by_phoneme` or `followed_by_phoneme` entry equals it or starts with it. |
| `when` | The whole context: the word-level conditions (`word_initial`, `word_final`, `preceded_by_phoneme` as the last segment of slot i-1's top candidate, `followed_by_phoneme` as the first segment of slot i+1's) and then the slot conditions. |
| `slot_when` | The slot conditions alone: stress, syllable position, neighbour classes, graphemes, words, `requires_other_nucleus` and `followed_by_nucleus` (section 7.2). |
| `trig_next`, `trig_prev` | 1 when the rule has a following (`followed_by`, `followed_by_grapheme`, `followed_by_phoneme`) or preceding trigger. |
| `mutate`, `mutate_at` | Present when the rule has `mutates_neighbor`: the feature string, and 1 when it marks the preceding slot (`mutates_neighbor_side = "preceding"`, so the rule's own slot is at i+1 from the slot it marks) or -1 for the following slot. |
| `seg` | Present when the rule has `preceded_by_phoneme` or `followed_by_phoneme`: `initial` and `final` (-1 for no condition, else 0 or 1), and the `prev` and `next` segment sets. |

The class names `vowel`, `front_vowel`, `palatal`, `emphatic`, `coda_nasal` and `consonant_cluster` become bits or `count` expressions. No class name reaches the interpreter. `allophony.atoms` holds the spec's phoneme atoms. `allophony.geminate` is `doubled_letters_geminate`. 

#### 3.6.2 Algorithm

`AllophoneRescorer.rescore` and `_realize`. A pass runs over each run of slots (3.3.3), with a context whose candidate lists are the pass input, and the pass repeats `allophony.passes` times. The S7 context carries the syllable and stress indices and the secondary set, but no aperture status, so `syll open` and `syll closed` are false there. The compiler never writes them in an allophone rule, because no allophone rule field reads aperture:

```
rescore(slot i):
  new = none
  for each cand (ipa, cost), in order:
    s = realize(ipa, i)
    if s is not none and s != ipa: new = new or copy of cands; new[that index] = (s, cost)
  f = neighbor_mutation(i)semantics version mutate
  if f: in new (or a copy of cands), append f to every non-empty string that does not contain f
  if new: sort new by (cost, string)

neighbor_mutation(i):
  for step in (+1, -1):
    j = i + step; skip unless slot j exists and has candidates
    m = the context with slot j's syllable index replaced by slot i's    # the legacy approximation
    for rule in order: if rule.mutate_at == step and top(j) in rule.phonemes and eval(rule.when, m, j): return rule.mutate
  return none

realize(ipa, i):
  twin = geminate_twin_side(ipa, i)
  for rule in order:
    if ipa in rule.phonemes and eval(rule.when, i):
      k = index of ipa in rule.phonemes
      trig = rule.trig_next if twin > 0 else rule.trig_prev
      if twin and not rule.aware[k] and not (trig and heterosyllabic(i, twin)): continue
      return rule.out[k]
  segs = segment(ipa, allophony.atoms)
  if len(segs) <= 1: return none
  return realize_segments(segs, i)   # 3.6.3
```

`geminate_twin_side(ipa, i)` is none unless `allophony.geminate` is 1, `ipa` is not empty, and no segment of `segment(ipa)` (no atoms) starts with a char with bit `ipa_vowel`. Then it tries step +1, then -1: slot i+step exists, its top candidate equals `ipa`, its token text lowercased with `plain_lower` equals slot i's, and the two tokens' spans touch (one ends where the other starts). The first step that passes is the side.

`heterosyllabic(i, step)` holds when slot i-step and slot i+2·step exist and both are vowel slots, where a vowel slot reads the token's vowel status when the token took an inherent vowel and else entry bit `vowel` (3.3.2).

#### 3.6.3 The segment pass

`_realize_segments` runs the segment rules on each segment of a multi-segment candidate:

```
realize_segments(segs, i):
  for k, seg in segs:
    slot_ctx = inserted-vowel context when seg starts with an ipa_vowel char and slot i holds no vowel
    prev = segs[k-1]; or, for k = 0, the last segment of slot i-1's top candidate; or none
    next = segs[k+1]; or, for the last k, the first segment of slot i+1's top candidate; or none
    initial = (i == 0 and k == 0)
    final = word_final(i) and k is the last
    for rule in order, when rule.seg is present and seg is in rule.phonemes:
      skip unless rule.seg.initial is -1 or equals initial
      skip unless rule.seg.final is -1 or equals final
      skip when rule.seg.prev is not empty and prev is not in it
      skip when rule.seg.next is not empty and next is not in it
      if eval(rule.slot_when, slot_ctx, i): replace seg by rule.out[index of seg]; stop
  return the joined segments when one changed, else none
```

The neighbour segments come from `segment(top candidate, allophony.atoms)`. A slot holds a vowel when its entry has bit `holds_vowel` or one of its token's readings, which can carry an inherent vowel, has a char with bit `ipa_vowel`. The inserted-vowel context is the context itself when the slot has no syllable index or the word no stress index. Else slot i's syllable index becomes one more than the index of the nearest earlier slot that holds a vowel (-1 when none does), and the stressed index grows by one when it is above that earlier index.

The interpreter segments IPA with primitive 11, which is `segment_ipa` over compiled data:

```
segment(ipa, atoms):
  i = 0
  while i < len(ipa):
    a = longest atom that starts at i and is not followed by a modifier char
    if a: emit a; i += len(a); continue
    j = i + 1; while j < len(ipa) and modifier(ipa[j]): j += 1
    emit ipa[i:j]; i = j
```

The atom list differs per caller:

| Caller | Atoms |
|---|---|
| allophone rules, `top_seg_in`, the segment pass and its neighbour segments | `allophony.atoms` |
| geminate twin test, `top_nucleus`, the inherent-vowel and syllable tests on readings | none |
| clitic join (3.5), weight splitter and weight (3.7.3, 3.8.1) | `atoms.affricates` |
| mark-placement splitter and its onset table (3.7.2, 3.7.3) | `atoms.mark` |

`modifier` is a char bit. The compiler sets it on every codepoint, in any reading, rule output, allophone value or known char, for which `unicodedata.combining` is non-zero or the category is Lm or Sk. A reading can hold such a codepoint outside the known ranges: U+207F ⟨ⁿ⟩ occurs in the readings of 101 specs. The rule needs no phonetic fact beyond the `modifier` bit and the atom lists.

### 3.7 Syllabification (S5, S9f)

The legacy engine has three splitters. The IR keeps all three as one splitter primitive with three configurations, and replaces the runtime onset grammar with compiled tables.

#### 3.7.1 The written splitter

`_syllables_for` → `_bundled_syllables` → `syllabify`:

```
written_syllables(word):
  word = word without unknown chars                          # 9.2
  nucleus = nucleus_mask(word)
  if diphthongs: sylls = split_with_diphthongs(word, nucleus, diphthongs, onset_graphemes, hiatus)
  else: sylls = vowel-group split
  if constrain_onsets: sylls = rebalance(sylls, nucleus, written_onset_table)
```

The written splitter never captures coda liquids: no caller passes `coda_liquid_capture` to `syllabify`.

`nucleus_mask` reads char bits: `mark` is never a nucleus, `orth_vowel ∪ ipa_vowel` decide the rest, and the semivowel letters get their role (`nucleus`, `margin`, `contextual`) from `_semivowel_roles`, precomputed per IR. A contextual letter is a nucleus only when neither non-mark neighbour is.

When the spec declares `stress.vowel_letters`, the compiler writes the lowercased set as `syllable.vowel_letters` and an empty `syllable.semivowels`, with the semantics version `vowel_letters`. The written splitter then makes a char a nucleus when its lowercase form is in that set, and no other char is a nucleus. The IPA splitters do not read the set.

`split_with_diphthongs` and `_split_nuclei` are kept: longest diphthong first, no diphthong across a hiatus cut, marks and `ː` join the previous nucleus.

#### 3.7.2 The licit-onset tables

`_rebalance_onsets` keeps, for each syllable after the first, the longest suffix of its consonant run that the judge licenses, and moves the rest into the previous coda. The algorithm stays. The judge becomes a table (ruled change 9.1).

The compiler evaluates the legacy judge on unit sequences of 2 to 5 units. A key of the table is a sequence that primitive 11 segments back to itself, because the interpreter looks a run up by its own segmentation. The compiler evaluates every such sequence of 2 units. It evaluates a longer sequence only when it extends a licit sequence one unit shorter by one unit at the end, when it is a 3-unit sequence that extends a licit 2-unit sequence by one unit at the start, or when it is a declared cluster of that length.

This search finds every licit sequence of up to 5 units, because of the shape of the legacy judges. With no declared clusters, the judge licenses no run of more than 3 units, and a 3-unit run is licit only as a licit two-member core plus a palatal glide (so its 2-unit prefix is licit) or as an /s/ appendix on a licit two-member core (so its 2-unit suffix is licit). With declared clusters, a run of 3 or more units is licit only when its last unit is a glide and the run without it is licit, or when it is a declared cluster. The legacy judge also licenses a run of 6 or more units that stacks glides on a licit run. The table stops at 5 units, so such a run is not licit in the IR (ruled change 9.1). A change to a judge that breaks these shapes must change this rule. The units are:

- **Written table.** The compiler writes it when `constrain_onsets` holds, as the object `syllable.onsets` with the semantics version `written_onsets`: `units`, the lowercased grapheme keys, longest first; `velar`, the units whose first IPA segment opens with ŋ; `max`, the declared `max_onset` or -1; and `table`. The interpreter splits a run into units as `_OnsetJudge.graphemes_of` does: at each position the first unit equal to the lowercased slice, else one char, and then the chars with bit `combining` that follow. It splits each candidate suffix again before the lookup, as the legacy judge does, and looks up the lowercased units. The judge is `_OnsetJudge._licit` with `_declared`, `_two_member`, `_appendix_on` and the velar-nasal, glottal, geminate and three-member rules.
- **IPA table.** Units are the segments that primitive 11 can produce on joined candidates: the compiler segments every concatenation of two adjacent readings it can see, adds the atoms and `_AFFRICATES`, and uses that set. A run whose unit is outside the set is not licit unless it is a single unit, as for the written table. The judge is `_IpaOnsetJudge._licit`, with the extra rise onto a glide.

When the spec declares `onset_clusters`, the compiler uses that list as the judge, as the legacy code does. The table is a trie of licit unit sequences. The runtime test follows `_OnsetJudge._licit` in this order: the empty run is licit; a run that holds a char without bit `letter` or `mark` is not licit; a run of more units than `max_onset` is not licit; a run whose first unit opens with `ŋ` is not licit; a run of one unit is licit; a longer run is licit only when the table holds it. When `onset_clusters` makes `_declared` recurse on a glide-final run, the compiler builds the table up to the longest run the spec can produce, not only up to 3 units.

At runtime the splitter segments the consonant run into units by trie match, and a run is licit when its unit sequence is in the table. A run of two or more units that is not in the table is not licit. The interpreter has no sonority, place or voicing test.

#### 3.7.3 The IPA splitters

`syllabify_for_mark` splits the word's IPA for mark placement: nucleus bits from `ipa_vowel`, `ipa_diphthongs` when declared, else `diphthongs`, then rebalance with the IPA table when `constrain_mark_onsets` holds, then coda-liquid capture when `stress.coda_liquid` is 1 (`coda_liquid_capture`, semantics version `coda_liquid`). Capture (`_capture_coda_liquids`) walks the syllables after the first. For each, it takes the onset (the leading chars that are combining or not a nucleus) and its chars without bit `combining`. When there are two or more, the first has bit `liquid` (in `_LIQUIDS`), the second lacks bit `glide`, and the previous syllable is not empty, the first char and the combining chars after it move to the end of the previous syllable.

`syllabify_ipa` serves quantity-sensitive stress. It splits on IPA segments with `max_onset`, length marks and offglides (`_OFFGLIDES`). It segments the word's full IPA with primitive 11 and `atoms.affricates`. The first onset takes every leading consonant, the last coda every trailing one, and a medial cluster gives at most `stress.weight.max_onset` segments to the following onset.

#### 3.7.4 Hiatus

`hiatus_positions` has two steps. First it collects candidate cut points: `_closed_hiatus_candidates` tests letter pairs against `closed_hiatus.pairs`, then the rest of the word against `onsets` and `codas`, and `_final_diphthong_candidates` tests the word end against `final_diphthongs`. Second, it filters them by stress: it splits the word with the written splitter, using the candidates as hiatus cuts, runs the decision of 3.8.1 on that split, and keeps only the candidate that opens the stressed syllable.

So tokenization depends on the stress decision. The tokenizer calls the filter through `_hiatus_prefix` when it meets a multi-letter vowel key. In the stage order this is a nested call: S4 calls the S5 splitter and decision on the word for this one filter, before S5 runs for the word. The interpreter caches the result per word, as `hiatus_by_word` does in the legacy code. The tables are strings over the lowercased word, and the vowel tests read char bit `orth_vowel`.

#### 3.7.5 Host syllabifier

A host syllabifier (H5) replaces the written splitter. Its result is used only when it joins back to the word. `SilabificadorSyllabifier` is such a plugin. Its 25-code list says which codes it accepts, and it runs only when a caller passes it.

### 3.8 Stress (S5, S9e, S9f)

#### 3.8.1 The decision

`detect_stress`, kept as written:

```
decide(word, sylls):
  n = len(sylls); if n <= 1: return 0
  if marked_vowels: return first syllable index holding a marked char
  lw = plain_lower(word)                                   # str.lower()
  for e in final endings, longest first:    if lw ends with e: return n-1
  for e in penult endings, longest first:   if lw ends with e: return n-2
  for e in antepenult endings, longest first: if lw ends with e: return max(0, n-3)
  index = default_position resolved: pos>=1 -> min(pos-1, n-1); else max(0, n+pos)
  for p in stress.prefixes, longest first:                  # semantics version prefixes
    if lw starts with p:
      inside = number of syllables that end within len(p)
      final_open = last char of last syllable with bit alpha is orth_vowel
      final_schwa = rime(plain_lower(last syllable)) in schwa_rimes      # rime: from the first orth_vowel on, else empty
      if index < inside < n and not (inside == n-1 and (final_open or final_schwa)): return inside
      break
  return index
```

`stress.source == "plugin"` is deprecated, no spec sets it, and IR v1 does not carry it. `plain_lower` is a separate char map, `char_maps.plain_lower`, equal to Python `str.lower()` on the known chars. The Turkish pairs are not in it, as the legacy decision lowercases with `str.lower()`. `rime` is `_rime`, which strips the onset by char bit `orth_vowel`.

The weight branch replaces the decision when `quantity_sensitive` holds. The compiler writes the object `stress.weight` with `max_onset` and `superheavy_final` (from `superheavy_final_attracts`), with the semantics version `weight`. The interpreter splits the finished IPA with `syllabify_ipa` (3.7.3), weighs a syllable from its first vowel segment on, and decides an end-anchored index, as `detect_stress_by_weight` does:

```
weight(syl): nucleus = the run of segments whose first char has bit ipa_vowel; coda = the segments after it
  long = a nucleus segment holds "ː", or the run has 2+ segments, or a segment holds a diphthong
  superheavy if (long and coda) or len(coda) >= 2; heavy if long or coda; else light
index(sylls): n <= 1: -1
  superheavy_final and weight(last) is superheavy: -1
  weight(penult) is not light: -2
  default < 0: default if n >= -default else -n;  default >= 0: -n
```

A segment holds a diphthong when, over its chars without bit `combining`, a char with bit `ipa_vowel` or `vowel_phone` (`is_vowel_phone`) is followed by another such char, or by a char with bit `offglide` that no such char follows. The mark goes on with the same division as `ipa_syllables` and no written syllables (3.8.3). The written-syllable decision still sets the stressed syllable of the slot context (3.3.3) and the hiatus test (3.7.4), as in the legacy engine.

For an abugida, the decision at step S9f counts the syllables of the transcription, because the spelling writes no letter for the inherent vowel. The compiler writes `stress.ipa_count` = 1 for a spec whose `script_type` is `abugida`, with the semantics version `ipa_count`. When it is set, S9f takes the syllables from `syllabify_for_mark(ipa)` (3.7.3) in place of the written syllables, for the decision, the secondary set and mark placement, and no inserted nucleus folds (`_fold_inserted_nuclei` gives none). The written syllables of S5 still feed the positional and allophone contexts. Khmer stresses the last syllable: ⟨កករ⟩ is [kɑˈkrɔː], not *[ˈkɑkrɔː]. `accent2_mark` compiles to `stress.accent2` (`mark`, and `finals` from `accent2_final_letters`), with the semantics version `accent2`. When the word has two or more written syllables, the decision gives the penult (index n-2), and the word's last char lowercased with `plain_lower` is in `finals`, the mark placement writes `accent2.mark` in place of `stress.mark`. Placement then returns the IPA unchanged when it already holds either mark.

#### 3.8.2 Iambic length

Step S9e (semantics version `iambic`) runs when `stress.iambic` is present, the IPA is not empty and the word is not cliticless. It runs after tone docking and before S9f. It lengthens the vowel of each light syllable in a weak-strong pair. `weight_split(ipa, m)` is the weight splitter of 3.7.3 with `m` in place of `stress.weight.max_onset`, `segments(s)` are the segments that splitter reads, and `weight(s)` is the syllable weight of 3.8.1, with light = 0, heavy = 1 and superheavy = 2.

```
iambic(ipa):
  if ipa holds "ː": return ipa
  s = weight_split(ipa, stress.iambic.max_onset)
  if len(s) < 3: return ipa
  i = 0 if weight(s[0]) > 0 else 1
  while i < len(s) - 1:
    if weight(s[i]) == 0:
      segs = segments(s[i])
      k = index of the first seg whose first char has bit ipa_vowel
      if k exists: segs[k] += "ː"
      s[i] = concat(segs)
    i += 2
  return concat(s)
```

#### 3.8.3 Mark placement

Step S9f puts the stress mark into the finished IPA of a word. It runs when `stress` is present, `stress.apply` is 1, the IPA is not empty and the word is not cliticless. The path of a word is its best beam path: a list of IPA segments and the list of graphemes that they read. A word with no path, such as an override, has `path = none`.

In this section, a char is a vowel char when it lacks bit `combining` and has bit `orth_vowel` or `ipa_vowel`. `prefix(s, m)` writes the mark `m` into the syllable `s` after its leading chars that have bit `length` or `combining`. `lower` maps through `char_maps.plain_lower`, `casefold` through `char_maps.casefold`, and `nfc` is the NFC step of 3.2. `ipa_split(ipa)` is the IPA splitter `syllabify_for_mark` of 3.7.3, and `syllables(word)` is the written splitter of 3.7.1.

```
S9f(word, ipa, path):
  if stress.weight:
    sylls = weight_split(ipa)                                    # 3.7.3
    return place(ipa, weight_index(sylls), none, sylls, [], none)    # 3.8.1
  if stress.ipa_count: sylls = ipa_split(ipa) else: sylls = syllables(word)
  idx = decide(word, sylls)                                      # 3.8.1
  folded = none if stress.ipa_count else fold_inserted(word, ipa, path)
  division = cut_written(word, ipa, path, sylls, folded)
  mark = none
  if stress.accent2 and len(sylls) >= 2 and idx == len(sylls) - 2
     and word not empty and lower(last char of word) in stress.accent2.finals:
    mark = stress.accent2.mark
  return place(ipa, idx, sylls, division, sorted(secondary(len(sylls), idx)), mark)
```

`secondary` is the secondary set of 3.8.1. With `stress.ipa_count`, the decision, the secondary set and the placement all read the IPA syllables, because an abugida writes no letter for the inherent vowel.

**Placement.** `place` takes the IPA, the stressed index (negative counts from the end), the written syllables or none, an IPA division or none, the sorted secondary indices and the mark. A slot that already holds a mark gets no second one.

```
place(ipa, idx, written, division, secondary, mark):
  if stress.mark in ipa or (mark and mark in ipa): return ipa
  mark = mark or stress.mark; sec = stress.secondary_mark
  ipa_s = division if division not empty else ipa_split(ipa)
  if ipa_s empty: return ipa
  if written: ipa_s = glide_to_diphthong(written, ipa_s, idx)
  if written and len(ipa_s) < len(written) and -len(written) <= idx < len(written):
    aligned = align(written, ipa_s)
    if aligned:
      ipa_s, slots = aligned; main = slots[idx]; done = {main}
      for s in secondary: if 0 <= s < len(slots) and slots[s] not in done:
        done += slots[s]; ipa_s[slots[s]] = prefix(ipa_s[slots[s]], sec)
      ipa_s[main] = prefix(ipa_s[main], mark); return concat(ipa_s)
  if idx < 0: from_end = -idx
  else:
    n_orth = len(written) if written else len(ipa_s)
    over = len(ipa_s) - n_orth
    if over > 0:                         # merge epenthetic syllables into the one before
      merged = [ipa_s[0]]
      for i from 1: s = ipa_s[i]
        if over > 0 and epenthetic(s, i == len(ipa_s) - 1): merged[last] += s; over -= 1
        else: merged += s
      ipa_s = merged
    elif over < 0 and idx <= len(ipa_s) - 1:
      lost = lost_after_stress(ipa, written, ipa_s, idx)
      anchor = glide_anchored(written, ipa_s, idx)
      if lost or anchor is not none:
        target = idx if lost else anchor
        for s in secondary: if 0 <= s < len(ipa_s) and s != target: ipa_s[s] = prefix(ipa_s[s], sec)
        ipa_s[target] = prefix(ipa_s[target], mark); return concat(ipa_s)
    from_end = max(1, n_orth - idx)
  target = max(0, len(ipa_s) - from_end); done = {target}
  n = len(written) if written else len(ipa_s)
  for s in secondary:
    slot = max(0, len(ipa_s) + s) if s < 0 else max(0, len(ipa_s) - max(1, n - s))
    if slot not in done: done += slot; ipa_s[slot] = prefix(ipa_s[slot], sec)
  ipa_s[target] = prefix(ipa_s[target], mark); return concat(ipa_s)

epenthetic(s, final):
  the vowel chars of s are exactly [stress.stand_in], and not (final and s ends with stress.stand_in)
```

**Glide to diphthong.** When the stressed vowel follows a written diphthong, a glide that opens the stressed IPA syllable moves to the end of the syllable before it.

```
glide_to_diphthong(written, ipa_s, idx):
  if stress.tonic_after_diphthong empty or len(ipa_s) != len(written): return ipa_s
  i = idx if idx >= 0 else len(written) + idx
  if not 1 <= i < len(written): return ipa_s
  w = lower(nfc(written[i])); b = lower(nfc(written[i-1]))
  if w empty or w[0] not in tonic_after_diphthong: return ipa_s
  if no d in stress.mark_diphthongs with len(d) > 1 and b ends with lower(d): return ipa_s
  h = ipa_s[i]; p = ipa_s[i-1]
  if len(h) < 2 or h[0] lacks bit glide_head or h[1] is not a vowel char
     or p empty or p's last char is not a vowel char: return ipa_s
  ipa_s[i-1] = p + h[0]; ipa_s[i] = h[1:]; return ipa_s
```

**Alignment.** A vowel contact is a written syllable boundary where the syllable before ends in a char with bit `basic_vowel`. A "hiatus" contact splits one IPA syllable in two. A "merge" contact keeps the two written syllables in one IPA syllable.

```
contacts(written):
  for i in 1 .. len(written)-1:
    b = written[i-1]; a = written[i]
    if b empty or b's last char lacks basic_vowel: continue
    j = index of the first char of a with basic_vowel; if none: continue
    if j > 0 and some unit of contact_units(casefold(a[0:j])) is not in stress.silent_units: continue
    if lower(b's last char + a[j]) not in lower(stress.mark_diphthongs): kind[i] = hiatus
    elif j > 0: kind[i] = merge

contact_units(run): split run longest first over stress.contact_units, comparing casefold(run slice);
  a char that starts no unit is a unit; combining chars join the unit before them

split_first_nucleus(s):
  i = index of the first vowel char of s; if none: return none
  i += 1
  while i < len(s) and s[i] has bit combining or length:
    if s[i] has bit non_syllabic: return none
    i += 1
  if i == len(s) or s[i] is not a vowel char: return none
  if i + 1 < len(s) and s[i+1] has bit non_syllabic: return none
  return (s[0:i], s[i:])

align(written, ipa_s):
  kind = contacts(written); if kind empty: return none
  out = []; slots = [0]; pending = ipa_s[0]; j = 0
  for k in 1 .. len(written)-1:
    cut = split_first_nucleus(pending) if kind[k] else none
    if kind[k] == merge and cut: slots += len(out); continue
    if kind[k] == merge or cut is none:
      j += 1; if j == len(ipa_s): return none
      out += pending; pending = ipa_s[j]
    else: out += cut[0]; pending = cut[1]
    slots += len(out)
  if j != len(ipa_s) - 1: return none
  out += pending; return (out, slots)
```

**Lost and glide-anchored syllables.** A merge site is an index i ≥ 1 where `written[i-1]` and `written[i]` are not empty, the last char of `written[i-1]` has bit `basic_vowel`, and the first char of `written[i]` has bit `basic_vowel`.

```
lost_after_stress(ipa, written, ipa_s, idx):
  if the last char of ipa without bit combining is a vowel char: return false
  merged = []
  for site in merge sites of written:
    slot = site - len(merged)
    if slot >= len(ipa_s) or ipa_s[slot][0] is not a vowel char and lacks bit glide: merged += site
  return len(written) - len(merged) != len(ipa_s) or some site in merged > idx

glide_anchored(written, ipa_s, idx):
  if written is none or ipa_s empty or not 0 <= idx < len(written): return none
  if stress.marked empty or no char of written[idx] is in stress.marked: return none
  sites = merge sites of written
  if len(written) - len(sites) != len(ipa_s): return none
  shifted = idx - count of sites <= idx
  return shifted if 0 <= shifted < len(ipa_s) else none
```

**Inserted nuclei.** A vowel that no grapheme's readings hold, such as an epenthetic vowel, does not make a syllable of its own. `token_pairs(tokens, path)` walks the path's graphemes and segments in order, and pairs each with the next grapheme token of the word whose grapheme is equal. It gives none when a grapheme has no such token.

```
fold_inserted(word, ipa, path):
  if path is none or its graphemes are empty or concat(path segments) != ipa: return none
  tokens = grapheme tokens of word (S4); pairs = token_pairs(tokens, path); if none: return none
  inserted = {}; offset = 0
  for (t, seg) in pairs:
    if entry of tokens[t] lacks bit readings_hold_vowel:
      inserted += offset + each index of seg whose char has bit ipa_vowel
    offset += len(seg)
  if inserted empty: return none
  folded = []; offset = 0
  for s in ipa_split(ipa):
    nuclei = offset + each index of s whose char has bit ipa_vowel
    if folded not empty and nuclei not empty and every nucleus is in inserted: folded[last] += s
    else: folded += s
    offset += len(s)
  return folded if len(folded) < len(ipa_split(ipa)) else none
```

**Cuts from the written syllables.** When the IPA has fewer syllables than the written word, two vowels that the written word puts in two syllables are cut apart, and a dropped written vowel gets a stand-in for the split.

```
cut_written(word, ipa, path, written, division):
  if path is none or its graphemes are empty or concat(path segments) != ipa: return division
  s = division or ipa_split(ipa)
  if len(s) >= len(written) or concat(written) != word: return division
  tokens = grapheme tokens of word; tsyl = syllable index of each token (3.3.3)
  pairs = token_pairs(tokens, path); if none: return division
  owner = []; source = []
  for (t, seg) in pairs: repeat len(seg) times: owner += tsyl[t]; source += tokens[t].position
  if len(owner) != len(ipa): return division
  start[k] = total length of written[0:k]
  cuts = {}; last = none
  for o, ch in ipa:
    if ch lacks ipa_vowel:
      if ch lacks combining and lacks length: last = none
      continue
    if last is not none and owner[o] == owner[last] + 1 and not (o+1 < len(ipa) and ipa[o+1] has non_syllabic):
      b = written[owner[last]]; a = written[owner[o]]
      first = the first char of a with orth_vowel, else empty
      lead = a[0 : source[o] - start[owner[o]]]
      if some char of lead has alpha and lower(b's last char + first) not in lower(stress.mark_diphthongs):
        cuts += o
    last = o
  read = every text index covered by a token
  drops = []
  for k, syl in written:
    segs = the indices o with owner[o] == k
    dropped = text indices i of syl (from start[k]) whose char has orth_vowel and i not in read
    if segs and dropped and no ipa[o] for o in segs has ipa_vowel:
      drops += the first o in segs with source[o] > dropped[0], else last of segs + 1
  if drops:
    probe = ipa with stress.stand_in inserted before each index in drops
    at = [drops[i] + i for each i]                 # stand-in positions in probe
    ends = 0 and the running ends of ipa_split(probe)
    for p in at:
      lo = greatest end <= p; hi = least end > p
      lo -= count of q in at with q < lo; hi -= count of q in at with q < hi
      cuts += lo, hi
  bounds = running ends of s except the last, plus cuts
  edges = 0, sorted bounds strictly inside (0, len(ipa)), len(ipa)
  cut = the slices of ipa between consecutive edges
  return cut if len(cut) > len(s) else division
```

`stress.stand_in` is one codepoint, `ə`, so each stand-in is one position of the probe. End-relative placement is a later ruled change (11.2).

### 3.9 Tone and abugida word finalisation (S9a, S9c, S9d)

The compiler lowers all three: `tone_rules` to the top-level `tone` object, `virama_final_vowel` to `word.virama_final`, and `tone_marks_syllable_final` to `word.tone_dock`.

**Computed tone** (`assign_computed_tones`, `tone.py`, primitive `computed_tone`). Step S9a runs when `tone` is present, the word has a path with graphemes, and the IPA equals the path's joined segments; it runs before geminate collapse. The compiler writes `classes` (letter to class), `marks` (tone mark to mark name), `no_mark`, `dead_codas`, `atoms` (the spec's `phonemes`) and `table`, whose rows are `[class, shape, mark, tone]` with the tone name already replaced by its IPA (the empty string when `tones` lacks it).
   - *Syllables over slots.* A slot whose segment holds a char with bit `ipa_vowel` is a nucleus. With no nucleus, the IPA stays as it is. The first syllable takes every slot up to its nucleus. For each later nucleus: when its segment is not empty and its first char lacks `ipa_vowel`, the slot spells its own onset, and every slot since the previous nucleus closes the previous syllable. Else the onset is the last slot before the nucleus whose segment is not empty (the nucleus itself when there is none), the slots before the onset close the previous syllable, and the slots from the onset on open this one. The slots after the last nucleus close the last syllable.
   - *Tone of one syllable.* The class is that of the first char of the syllable's graphemes found in `classes`. With no class, or a class with no row, the tone is empty. The mark is `no_mark`, replaced by each char found in `marks`, so the last one wins. Segment the syllable's IPA with primitive 11 over `atoms`. The nucleus is the first run of segments whose first char has bit `ipa_vowel`, and the rest is the coda; with no nucleus the tone is empty. The vowel is long when the nucleus holds `ː`. The syllable is dead when the coda starts with a string of `dead_codas`, or when there is no coda and the vowel is short. The shape is `live`, `dead_short` or `dead_long`. The row `[class, shape, mark]` gives the tone, else the row `[class, any, mark]`, else the empty string.
   - The tone is appended to the syllable's IPA. Thai ⟨นก⟩ is /nok̚˦˥/: a low-class initial in a dead syllable with a short vowel.

**Virama final vowel** (primitive `virama_final`). When `word.virama_final` is present, step S9c appends it to the word's IPA when the IPA is not empty, the word's last char has char bit `virama`, and the IPA's last codepoint lacks char bit `ipa_vowel`. The step runs after geminate collapse, so the vowel of Malayalam ⟨റ്റ്⟩ follows the collapsed /tː/. It runs for an override too. The Malayalam spec sets the field to `ɨ`, the samvrutokaram.

**Tone docking** (semantics version `tone_dock`) runs when `word.tone_dock` is present, after geminate collapse and before stress. It moves each run of tone marks to the end of the syllable that follows it. A char is a tone mark when it has bit `tone_mark`. A segment is a nucleus when its first char has bit `ipa_vowel` or lacks bit `alpha`.

```
dock(ipa):
  if no char of ipa is a tone mark: return ipa
  out = ""; i = 0
  while i < len(ipa):
    if ipa[i] is not a tone mark: out += ipa[i]; i += 1; continue
    j = end of the run of tone marks that starts at i
    tone = ipa[i:j]
    t = index of the next tone mark at or after j, else len(ipa)
    segs = segment(ipa[j:t], word.tone_dock)        # primitive 11
    if segs not empty and t < len(ipa) and every seg is a nucleus:
      out += tone; i = j; continue                  # the tone stays
    k = count of leading nucleus segs
    c = k + count of non-nucleus segs that follow them
    if c < len(segs) and c > k: c -= 1              # leave one onset for the next nucleus
    coda = concat(segs[0:c])
    out += coda + tone; i = j + len(coda)
  return out
```

### 3.10 Sandhi (S11) and dialect profiles (S13)

#### 3.10.1 Sandhi

`SandhiEngine.apply`, kept:

```
sandhi(words, pausal):
  for i in 0 .. len(words)-2:
    if pausal[i]: continue
    L, R = words[i], words[i+1]
    left_done = right_done = false
    for rule in sandhi:
      if left_done and right_done: break
      mL = search(rule.left, L); mR = search(rule.right, R)
      if not (mL and mR): continue
      if rule.left_out and not left_done:  words[i]   = sub(rule.left, L, rule.left_out);   left_done = true
      if rule.right_out and not right_done: words[i+1] = sub(rule.right, R, rule.right_out); right_done = true
```

Each search reads the two words as they stood before this pair was rewritten. The compiler writes `obligatory`, and the v1 interpreter does not read it: `G2P` never passes `obligatory_only`, so every rule applies. `sub` is Python `re.sub` with count 0: it replaces every non-overlapping match from left to right. `left_out` and `right_out` are templates `[["lit", s], ["group", n], ...]`. An unmatched group is empty. 43 rules (46 fields) use a group in a template.

#### 3.10.2 Dialect profiles

`apply_transform` runs on the joined sentence after empty words drop, and only when the caller passes `dialect_profile`. `G2P` passes the spelling `" ".join(w.surface for w in words)`, with every word kept, and no allophone weights. A profile is a compile option. The compiler writes it into the IR as a dialect program, and the interpreter runs it at S13. So the dialect output is part of the IR and of its revision.

A dialect program is an ordered list of steps. Each step has a gate (primitive 13) and an action (primitives 2, 14, 15 or 16). The compiler emits the steps in the order of `apply_transform`:

1. Debiasing, when `requires_debiasing` holds: the steps of `debias_lisbon`, or of `debias_lisbon_preserve_spirants` when the IR is compiled with the option `dialect_spirants` (the `allophone_weights` branch of `apply_transform`, which `G2P` never takes).
2. Every `IPAChainShift` in rule order (primitive 15).
3. Every `IPALexicalRule` (primitive 16), in one step: for each word, the last matching rule wins, computed from the original word.
4. Every `IPARule` in rule order: a literal replace-all (primitive 2) when `context` is null, else primitive 14. A rule with `requires_ortho` gets the gate "spelling present".

#### 3.10.3 The dialect primitives

**Primitive 13, spelling gate.** A gate is a predicate over the joined spelling S:

| Node | Holds when |
|---|---|
| `["spell_search", pattern]` | the pattern (section 5) matches somewhere in S; a literal such as `ei` is a one-node pattern |
| `["spell_empty"]` | S is empty (Python's `not ortho`) |
| `and`, `or`, `not`, `true` | logic |

The test is case-sensitive on S as `G2P` builds it, as `"ei" in ortho` is.

**Primitive 14, positional literal rewrite.** `_apply_contextual`: scan the input string x from i = 0. Where x[i:i+len(find)] equals `find` and the position predicate holds at i, emit `replace` and skip len(find). Else emit x[i] and step one. Predicates read x, never the output. The nodes are general string-position tests:

| Node | Holds at position i, match length n |
|---|---|
| `["back_reach", target_set, stop_set]` | scanning x from i-1 down to 0, a char in `target_set` comes before a char in `stop_set` |
| `["at_in", k, set]` | x[i+k] exists and is in the set (k may be negative) |
| `["at_end_or_in", set]` | i+n is the end of x, or x[i+n] is in the set |
| `["ahead_match", k, pattern]` | the pattern matches x from i+k, anchored there |
| `["covered_by", strings]` | some string s of the set occurs at a start j with j ≤ i < j+len(s) |
| `["later_has", set]` | x[i:] holds a char of the set |
| `["spell", gate]` | a primitive 13 gate on the spelling |
| `and`, `or`, `not` | logic |

**Primitive 15, gated codepoint map.** `IPAChainShift.apply` as a generic scan:

```
state = off
for c in x:
  if c in on_set: state = on; emit c; continue
  if mode == "when_on" and state == off: emit c
  else: emit map.get(c, c)
  if c in off_set and state == on: state = off
```

The off test reads the input codepoint, not the mapped one, as the legacy code does.

**Primitive 16, aligned word rewrite.** `apply_transform`: split x and S as Python `str.split()` does, on runs of whitespace with empty pieces dropped. The whitespace set is every codepoint for which `str.isspace()` is true: U+0009 to U+000D, U+001C to U+001F, U+0020, U+0085, U+00A0, U+1680, U+2000 to U+200A, U+2028, U+2029, U+202F, U+205F and U+3000. When the counts are equal, for each word index w the step computes each matching rule's result from the ORIGINAL IPA word w, not from the result of an earlier rule: a rule matches when its key equals the lowercased spelling word, and its result is the original word with every occurrence of `find` replaced by `replace`. The result of the last matching rule in rule order becomes word w. Then the words join with U+0020. When the counts differ, the step does nothing. The rule keys are any strings, so the primitive serves any language.

The data of these primitives is plain IR. The sets `VOWEL_SET` and `PALATAL_SET` become char sets, the chain-shift mappings become codepoint maps, and the Cintra zone tables of `DIALECT_PROFILES` become step lists. Nothing in the primitives names Portuguese.

#### 3.10.4 Lowering of the legacy contexts

| `IPARule.context` | Predicate (primitive 14) |
|---|---|
| `stressed` | `back_reach({ˈ}, VOWEL)` |
| `unstressed` | `not back_reach({ˈ}, VOWEL)` |
| `word_final` | `at_end_or_in({space, tab, newline})` |
| `word_final_unstressed` | `and(word_final, unstressed)` |
| `coda` | `at_in(-1, VOWEL)` |
| `stressed_and_before_r_or_closed_syllable`, `stressed_before_r_C` | `and(stressed, ahead_match(1, [ɾr][C]))`, where C is the consonant class of `_before_r_or_closed` |
| `stressed_before_r_C_or_nasal_C` | `and(stressed, or(ahead_match(1, [ɾr][C]), ahead_match(1, [mn][C])))` |
| `stressed_and_adjacent_to_palatal` | `and(stressed, or(at_in(-1, PALATAL), at_in(1, PALATAL), covered_by({tʃ, dʒ})))` |
| `unstressed_pretonic` | `and(unstressed, later_has({ˈ}))` |
| `stressed_and_from_historical_ou` | `and(spell(spell_search(ou)), stressed)` |
| `ortho_has_ou`, `ortho_source_is_ch`, `ortho_source_is_z` | `spell(spell_search(ou))`, `spell(spell_search(ch))`, `spell(spell_search(z))` |
| `ortho_source_is_ss_or_s` | `spell(spell_search(s))`: the legacy `"ss" in S or "s" in S` equals `"s" in S` |
| `ortho_source_is_c_or_ç` | `spell(or(spell_search(ç), spell_search(c[ei])))` |
| `ortho_source_is_intervocalic_s` | `spell(spell_search([aeiouáéíóúâêôãõ]s[aeiouáéíóúâêôãõ]))` |
| `no_ortho_available` | `spell(spell_empty)` |

`ahead_match(1, ...)` reads from i+1, not from i+n, because `_before_r_or_closed` reads `ipa[pos + 1:]`. `at_in(1, PALATAL)` likewise reads x[i+1].

`debias_lisbon` lowers to four kinds of step:

- a literal rewrite `ɐj → ej`, gated on `spell_search(ei)`;
- a pattern rewrite `(?<=[^aeɛɐiɨoɔuɑæøœyãẽĩõũ\s])ɐj → ej`, gated on `spell_empty`, which is the `elif` branch and can only run when the first gate fails;
- a pattern rewrite `o(?=[tdszʃnlɾ]) → ow`, gated on `spell_search(ou)`;
- four literal rewrites `β → b`, `ð → d`, `ɣ → ɡ` and `ɫ → l`.

The spirant-preserving variant keeps only `ɫ → l` of the last four. The class lookbehind is the one-codepoint `behind set` node of 5.1, and `\s` lowers to the set of whitespace codepoints.

#### 3.10.5 Every profile

| Profile | Debias | `IPARule` | Chain shifts | Lexical rules | Primitives used |
|---|---|---|---|---|---|
| `estremenho` | yes | 0 | 0 | 0 | 2, 13 |
| `lisbon` | no | 4 | 0 | 0 | 2, 13, 14 |
| `ribatejano` | yes | 1 | 0 | 0 | 2, 13, 14 |
| `beira_baixa` | yes | 7 | 0 | 0 | 2, 13, 14 |
| `algarve_barlavento` | yes | 2 | 1 | 0 | 2, 13, 14, 15 |
| `northern` | yes | 2 | 0 | 0 | 2, 13, 14 |
| `transmontano` | yes | 9 | 0 | 0 | 2, 13, 14 |
| `baixo_minhoto` | yes | 4 | 0 | 0 | 2, 13, 14 |
| `porto` | yes | 7 | 0 | 0 | 2, 13, 14 |
| `beira_alta` | yes | 4 | 0 | 0 | 2, 13, 14 |
| `galician` | yes | 5 | 0 | 0 | 2, 13, 14 |
| `galician_west` | yes | 6 | 0 | 0 | 2, 13, 14 |
| `leonese` | yes | 12 | 0 | 0 | 2, 13, 14 |
| `rionorese` | yes | 12 | 0 | 2 | 2, 13, 14, 16 |
| `guadramilese` | yes | 13 | 0 | 2 | 2, 13, 14, 16 |

The counts come from `DIALECT_PROFILES` at `690611bb2`. Every context that a rule of a profile uses is in the table of 3.10.4, which covers every context `_check_context` knows. So every profile lowers to the primitives, and the compiler refuses a profile with an unknown context. `ALLOPHONE_GATED_RULES` and `load_clup_profile` are analysis helpers that `apply_transform` does not call, and the program does not hold them.

### 3.11 Words, punctuation and compounds (S2, S10)

Word grouping follows `G2P._group_words`. Whitespace ends a word. Punctuation ends a word, except an apostrophe between letters when `word_internal_apostrophe` holds, and a leading apostrophe that opens a word exception. A hyphen sets `hyphen_joined` on the next word. A punctuation run with a pause char marks the previous word pausal. The last word is pausal. Digit and UNKNOWN tokens stay inside the word surface, and the word path drops them (9.3).

Compound stress (S10, `compound_stress == "last"`): in each hyphen-joined run, every primary mark but the last becomes the secondary mark.

### 3.12 Output (S9b, S12, S14)

Geminate collapse (`_collapse_geminates`) merges equal adjacent codepoints except `ipa_vowel`, length marks and space. It does not run on overrides. Non-empty words join with U+0020. The result is NFC by `char_maps`. The output can join codepoints that no single key holds, such as a vowel from one reading and a nasal mark from the next. So `char_maps.compose` holds every primary composite whose two parts the IR can write, closed under composition: a composite joins the set and can be the first part of a further composite. The interpreter returns the IPA string, and the Python reference also returns per-word paths, integer costs, dropped characters and coverage. `confidence` uses `exp` and is computed by the Python wrapper from the costs.

### 3.13 Literal constants

The interpreter holds no phonetic literal. Each IPA string that a legacy stage writes as a constant is a field of the IR:

| Field | Value for pt-PT | Use |
|---|---|---|
| `stress.stand_in` | `ə` | The vowel that stands in for a dropped nucleus while the mark is placed (3.8.3). |
| `word.clitic_marks` | `ˈ`, `ˌ` | The marks that a clitic host's IPA must not open with before the clitic joins it (3.5). |
| `stress.mark_onsets.velar` | `ŋ` | A run whose first unit opens with this string is not a licit onset (3.7.2). |
| `beam.tilde` | U+0303 | The nasal mark that the beam tests on a nasal carrier (3.3.6). |
| `atoms.mark`, `atoms.affricates` | the legacy `_MARK_ATOMS`, `_AFFRICATES` | The atoms of primitive 11 (3.6.3). |

The length mark `ː` and the apostrophe fold U+2019 to `'` stay literals of the interpreter, as 3.6 and 3.2 state.

## 4. Unicode

The interpreter needs no Unicode database. Text crosses the loom bridge as codepoint arrays. Every Unicode fact is an IR table:

| Fact | IR table | Built from |
|---|---|---|
| NFC | `char_maps.nfd`, `char_maps.ccc`, `char_maps.compose` | `unicodedata.decomposition`, `combining` and `normalize("NFC")` over the known chars; `compose` is closed over every primary composite whose parts the IR can write |
| Casefold (tokenizer) | `char_maps.casefold` | `_lower`, with the Turkish pairs for Turkic specs |
| Plain lowercase | `char_maps.plain_lower` | `str.lower()`. Stress endings, hiatus, `word_in`, `word_has` and every other "lowercased" test of this spec read this map; only the tokenizer, the trie, the elided-clitic key, the override key and the cliticless key read `casefold`. |
| Decomposition fallback | `entries` | `unicodedata.normalize("NFD")` |
| Space, punctuation, digit, letter, mark, virama, edge punctuation | char bits | the legacy regexes and `unicodedata.category`, `combining` |
| Orthographic and IPA vowels | char bits | `vowels.py`, including the name tokens `VOWEL`, `VOCALIC` |
| Subjoined letters, medial signs | entry bits | `phonetok.py` name tests |
| Features (front, palatal, sonority) | bits and onset tables | phonematcher |

**Known chars.** The IR holds the known chars as a sorted list of codepoint ranges, `chars.ranges`, with a bit value per range or per codepoint. The compiler builds the list as the union of:

1. every codepoint of every entry key, positional key, word exception and grammatical ending, and the codepoints that casefold to them;
2. every codepoint whose Unicode Script property, in the compiler's Unicode version, equals the spec's `script` (`Latin`, `Arabic`, `Gurmukhi`, and so on), restricted to General Category L, M and N; for `script` values that name no Script property value (`Zyyy`, `Hebrew` for Judeo-Arabic), only item 1 applies;
3. the fixed ranges U+0020–U+007E, U+00A0–U+00BF, U+2000–U+206F (General Punctuation), U+0250–U+02FF (IPA Extensions and Spacing Modifier Letters), U+0300–U+036F (Combining Diacritical Marks) and U+1D00–U+1DBF (Phonetic Extensions);
4. every codepoint in a codepoint map or a rewrite pattern of the IR.

The Script property, not the block, decides item 2. So U+FB01 ⟨ﬁ⟩ is known for a Latin spec. A known char with no entry keeps its legacy bits (`letter`, `orth_vowel`, `mark`) and is dropped from the IPA as before. Section 9.2 gives the rule for unknown chars.

## 5. The pattern subset

### 5.1 Grammar

The compiler parses every pattern (sandhi contexts and normalisation rewrites) and stores the parse tree. No interpreter parses pattern text.

```
alt     := seq ('|' seq)*
seq     := item*
item    := atom ('?' | '*' | '+')?
atom    := literal | '.' | class | '^' | '$' | group | look
class   := '[' '^'? (cp | cp '-' cp)+ ']'
group   := '(' alt ')' | '(?:' alt ')'
look    := '(?=' alt ')' | '(?!' alt ')' | '(?<=' unit ')' | '(?<!' unit ')'
unit    := cp | class                          # lookbehind of exactly one codepoint
```

`^` and `$` are zero-width atoms allowed anywhere, so a pattern may have both anchors, and `$` may stand inside a lookahead (P33). IR nodes: `lit`, `any`, `set`, `bol`, `eol`, `seq`, `alt`, `group n`, `opt`, `star`, `plus`, `ahead neg`, `behind set neg` (a one-codepoint lookbehind over a literal or a class).

### 5.2 Semantics

Matching is on codepoints, with Python `re` semantics: `search` tries each start position from left to right, and the first match wins. Alternation is ordered, quantifiers are greedy, and the matcher backtracks. A class holds single codepoints. A combining mark inside a class is its own member. `.` matches any codepoint except U+000A, as Python does without `DOTALL`. Lookarounds consume nothing. A group captures its last iteration. `sub` replaces all non-overlapping matches from left to right. After an empty match, the next match can start at the same position only when it is not empty, as in Python 3.7 and later.

The compiler refuses a quantifier (`?`, `*`, `+`) whose body can match the empty string: a lookaround, an anchor, a starred or optional item, or an alternation with an empty branch. Python gives such repeats a special treatment of the empty iteration and of the groups inside it, and the subset leaves it out. No pattern in the data uses one.

### 5.3 Every pattern in the data

The data holds 145 sandhi rules in 36 spec files. After inheritance (`sandhi_rules` is `OVERLAY_BY_ID`), 202 loaded specs carry sandhi rules. The rules use 98 distinct context patterns. All 98 fit 5.1 as written, so each translates to its parse tree. No pattern uses a backreference or `{m,n}`. 9 patterns have both anchors (P15, P25, P35, P36, P37, P57, P77, P86, P87). P33 has `$` inside a lookahead. Tags: `^`, `$` anchors; `LA`, `NLA` lookahead; `LB` lookbehind; `NC` non-capturing group; `CAP` capturing group; `ALT`; `NEG` negated class; `STAR` `.*`; `INNER$` an anchor inside a group; `CMB` a combining mark inside a class.

| # | Pattern | Constructs | Specs |
|---|---|---|---|
| P1 | `^[ˈˌ]?[pbβm]` | ^ | 12 |
| P2 | `^[ˈˌ]?[tdðθszlɾrnɲʎʝʃʒf]` | ^ | 12 |
| P3 | `ŋ$` | $ | 9 |
| P4 | `^([ˈˌ]?)b` | ^ CAP | 6 |
| P5 | `^([ˈˌ]?)ɡ` | ^ CAP | 6 |
| P6 | `^[ˈˌ]?[bdɡvzʒmnɲlʎɾʁ]` | ^ | 6 |
| P7 | `ʃ$` | $ | 6 |
| P8 | `[aeiouəɛɔɐ]$` | $ | 5 |
| P9 | `[aeiouɛɔɐ]$` | $ | 5 |
| P10 | `^([ˈˌ]?)d` | ^ CAP | 5 |
| P11 | `^[aeoəɛɔɐ](?=.*[aeiouəɛɔɐ])` | ^ LA STAR | 5 |
| P12 | `^[ˈˌ]?s` | ^ | 5 |
| P13 | `^[ˈˌ]?ʃ` | ^ | 5 |
| P14 | `^i` | ^ | 5 |
| P15 | `^i$` | ^ $ | 5 |
| P16 | `^u(?=.)` | ^ LA | 5 |
| P17 | `[^mnŋɲ̃]$` | $ NEG CMB | 4 |
| P18 | `[^mnŋɲ̃lʎ]$` | $ NEG CMB | 4 |
| P19 | `[ʃ]$` | $ | 4 |
| P20 | `[ˈˌ]?s$` | $ | 4 |
| P21 | `[ˈˌ]?ʃ$` | $ | 4 |
| P22 | `^[ˈˌ]?[aeiouɛɔɐɨəãõẽĩũ]` | ^ | 4 |
| P23 | `^[ˈˌ]?[aeiouɛɔɐɪʊãẽĩõũ]` | ^ | 4 |
| P24 | `n$` | $ | 4 |
| P25 | `^(.*[aeiouəɛɔɐ].*[^ˈˌjw])ə$` | ^ $ CAP NEG STAR | 3 |
| P26 | `^(?:[ˈˌ][aeiouəɛɔɐ]\|[aeoəɛɔɐ])` | ^ NC ALT | 3 |
| P27 | `^[ˈˌ]?[aeiouəɛɔɐ]` | ^ | 3 |
| P28 | `^[ˈˌ]?[kɡɣxw]` | ^ | 3 |
| P29 | `s$` | $ | 3 |
| P30 | `([nŋ])$` | $ CAP | 2 |
| P31 | `[aeiouɛɔəɐ]$` | $ | 2 |
| P32 | `[aiueoɑæə]ː?$` | $ | 2 |
| P33 | `^(?!(?:[ˈˌ]?els?)$)[ˈˌ]?[aeiouəɛɔɐ]` | ^ NLA NC INNER$ | 2 |
| P34 | `^[ˈˌ]?(?:ʃ\|ʒ\|ʎ)` | ^ NC ALT | 2 |
| P35 | `^el$` | ^ $ | 2 |
| P36 | `^els$` | ^ $ | 2 |
| P37 | `^kə$` | ^ $ | 2 |
| P38 | `p$` | $ | 2 |
| P39 | `t$` | $ | 2 |
| P40 | `(?:[sz]̺?\|[lɫɾ]\|[aeiouɐɨɪʊəɛɔɵjw])$` | $ NC ALT | 1 |
| P41 | `(?:[sz]̺?\|ɾ\|[aeiouɐɨɪʊəɛɔɵjw])$` | $ NC ALT | 1 |
| P42 | `(?:[ãẽĩõũ]\|[ɐɨɪʊə]̃)$` | $ NC ALT | 1 |
| P43 | `(?:s̺\|[lɫɾ])$` | $ NC ALT | 1 |
| P44 | `(?<!t)s$` | $ LB | 1 |
| P45 | `([aeiouyɛɔəɨʉɯæɐʌɒœøɪʏʊɤɵɞɑɘɚɜɝɶãõẽĩũ].*)[ʃ]$` | $ CAP STAR | 1 |
| P46 | `([aeiouəɛɔɐ])[sʃ]$` | $ CAP | 1 |
| P47 | `([bdɡvzʒ])$` | $ CAP | 1 |
| P48 | `([nlɫ])t$` | $ CAP | 1 |
| P49 | `([nŋ])k$` | $ CAP | 1 |
| P50 | `([ˈˌ].*)[ɨ]$` | $ CAP STAR | 1 |
| P51 | `(m)p$` | $ CAP | 1 |
| P52 | `[aeiouəɛɔiuwjszʃʒfvβðɣɾr]$` | $ | 1 |
| P53 | `[aeiouəɛɔiuwjszʃʒfvβðɣɾrlɫ]$` | $ | 1 |
| P54 | `[nŋ]$` | $ | 1 |
| P55 | `[ptkbdɡ]$` | $ | 1 |
| P56 | `^([ˈˌ]?)d(?!ʒ)` | ^ NLA CAP | 1 |
| P57 | `^([ˈˌ]?)es̻$` | ^ $ CAP | 1 |
| P58 | `^([ˈˌ]?)s` | ^ CAP | 1 |
| P59 | `^([ˈˌ]?)s̻` | ^ CAP | 1 |
| P60 | `^([ˈˌ]?)ʃ` | ^ CAP | 1 |
| P61 | `^(ˈ?)(?=[aeiouɐɨɪʊəɵáéíóú])` | ^ LA CAP | 1 |
| P62 | `^(ˈ?)b` | ^ CAP | 1 |
| P63 | `^(ˈ?)d` | ^ CAP | 1 |
| P64 | `^(ˈ?)ɡ` | ^ CAP | 1 |
| P65 | `^.` | ^ | 1 |
| P66 | `^[aeiouɛɔ]` | ^ | 1 |
| P67 | `^[aeiouɛɔɑãɛ̃ɔ̃œ̃]` | ^ CMB | 1 |
| P68 | `^[aɑ](?=[^aeiouɑɐæɪʊəɛɔː])` | ^ LA NEG | 1 |
| P69 | `^[ˈˌ]?(?:ʃ\|ʒ\|tʃ\|dʒ\|ʎ)` | ^ NC ALT | 1 |
| P70 | `^[ˈˌ]?[aeiouəɛɔɐbdɡβðɣvzʒmnɲŋlʎɫɾrjw]` | ^ | 1 |
| P71 | `^[ˈˌ]?[bdɡvzmnɲɾʁlʎ]` | ^ | 1 |
| P72 | `^[ˈˌ]?[bdɡvzʒmnɲlʎɾʁr]` | ^ | 1 |
| P73 | `^[ˈˌ]?[bdɡβðɣvzʒmnɲŋlʎɫɾrjw]` | ^ | 1 |
| P74 | `^[ˈˌ]?[kɡ]` | ^ | 1 |
| P75 | `^[ˈˌ]?[pbmf]` | ^ | 1 |
| P76 | `^[ˈˌ]?[pbtdkɡfvszʃʒmnɲŋlʎɫɾrβðɣ]` | ^ | 1 |
| P77 | `^[ˈˌ]?es̻$` | ^ $ | 1 |
| P78 | `^[ˈˌ]?f` | ^ | 1 |
| P79 | `^[ˈˌ]?k` | ^ | 1 |
| P80 | `^[ˈˌ]?l` | ^ | 1 |
| P81 | `^[ˈˌ]?n` | ^ | 1 |
| P82 | `^[ˈˌ]?p` | ^ | 1 |
| P83 | `^[ˈˌ]?t` | ^ | 1 |
| P84 | `^[ˈˌ]?ʒ` | ^ | 1 |
| P85 | `^i(?=l)` | ^ LA | 1 |
| P86 | `^l$` | ^ $ | 1 |
| P87 | `^ˈ?([bβks])iɨ̃$` | ^ $ CAP | 1 |
| P88 | `^ˈ?[bdɡβðɣmnɲlɫʎɾrʒz]` | ^ | 1 |
| P89 | `^ˈ?[pbtdkɡfsʃʒzmnɲlʎɾrβðɣ]` | ^ | 1 |
| P90 | `f$` | $ | 1 |
| P91 | `k$` | $ | 1 |
| P92 | `ks$` | $ | 1 |
| P93 | `ps$` | $ | 1 |
| P94 | `s̺$` | $ | 1 |
| P95 | `ts$` | $ | 1 |
| P96 | `tʃ$` | $ | 1 |
| P97 | `z$` | $ | 1 |
| P98 | `ʁ$` | $ | 1 |

P17, P18 and P67 put a combining mark inside a class. The IR keeps Python's per-codepoint meaning. The specs probably mean a multi-codepoint member, which is a spec defect to report to their owners (decision 11.4).

## 6. Representing the engine and the spec fields

Each row says how IR v1 carries a behaviour or field. "IR" means a table or rule run by a primitive. "Compile" means the compiler resolves it and only the result reaches the IR. "Host" means a hook at a named point. "Inert" means the IR carries nothing because the legacy engine does nothing with it. "Change" means a ruled change in section 9.

| # | Behaviour or field | Source | IR v1 |
|---|---|---|---|
| 1 | Arabic shadda | `phonetok.py` | IR: pattern rewrites |
| 2 | Arabic presentation forms | `phonetok.py` | IR: codepoint map |
| 3 | Gurmukhi addak | `phonetok.py` | IR: pattern rewrite |
| 4 | Turkish casing | `phonetok.py` | IR: `casefold` map; `plain_lower` keeps stress endings untouched |
| 5 | `fold_diacritics` | `phonetok.py` | IR |
| 6 | pt syllabifier plugin | `syllabifiers.py` | Host H5 |
| 7 | English mute e | `positional.py` | IR: predicate over entry sets |
| 8 | Dialect profiles | `transforms.py`, `g2p.py` | IR: dialect program, primitives 13 to 16 (compile option) |
| 9 | Code resolution | `registry.py` | Compile |
| 10 | Vowel and glide sets | `vowels.py` | Compile: bits |
| 11 | Abugida syllables for stress | `g2p.py`, `inventory.py` | IR: flag in `stress` |
| 12 | Inherent vowel insertion | `phonetok.py` | IR: tokenizer branch with entry bits |
| 13 | Nukta in the schwa decision | `types.py` (`consonant_marks`) | IR: char bit `consonant_mark` |
| 14 | Preposed and circumfix vowels | `phonetok.py` | IR: tokenizer branch with entry bits |
| 15 | Consonant nuclei | `phonetok.py` | IR: entry table |
| 16 | Marker heads | `_silent_marker_head` | IR: entry table |
| 17 | Hiatus prefix | `_hiatus_prefix` | IR: hiatus tables |
| 18 | Glide back-off | `phonetok.py` | IR: precomputed entry bits |
| 19 | Decomposition fallback | `phonetok.py` | Compile |
| 20 | Positional keys emitted (40) | `positional.py` | IR: predicate lists in emission order |
| 21 | Positional keys never emitted (5) | `types.py` | Inert (9.4) |
| 22 | Allophone conditions | `schema.py` | IR: predicates |
| 23 | Allophone segment pass and `segment_ipa` | `allophony.py` | IR: primitive 11 |
| 24 | `mutates_neighbor` | `allophony.py` | IR |
| 25 | Geminate twins | `allophony.py` | IR |
| 26 | `allophone_passes` | `g2p.py` | IR |
| 27 | Onset judge | `stress.py` | Compile: licit-onset tables (9.1) |
| 28 | Written, mark and weight splitters | `stress.py` | IR: splitter configurations |
| 29 | `detect_stress` | `stress.py` | IR: decision list as in 3.8.1 |
| 30 | Weight stress | `stress.py` | IR: second decision list |
| 31 | Mark placement | `stress.py`, `g2p.py` | IR: algorithm with bits |
| 32 | `iambic_length` | `stress.py` | IR |
| 33 | Secondary stress | `stress.py` | IR |
| 34 | Compound stress | `g2p.py` | IR |
| 35 | `accent2_mark` | `g2p.py` | IR |
| 36 | Computed tone | `tone.py`, `g2p.py` | IR: tone table, stage S9a |
| 37 | Tone docking | `g2p.py` | IR: stage S9d |
| 38 | `virama_final_vowel` | `g2p.py` | IR: stage S9c, char bit `virama` |
| 39 | Geminate collapse | `_collapse_geminates` | IR |
| 40 | Overrides, per-key order | `g2p.py` | IR plus host H4 |
| 41 | Elided clitics | `g2p.py` | IR with primitive 11 |
| 42 | `grammatical_endings` | `positional.py`, `g2p.py` | IR |
| 43 | `expand_allophones` and the `allophones` map | `g2p.py`, `positional.py` | IR: compile option |
| 44 | `apply_stress`, `apply_allophony`, `apply_sandhi` | `g2p.py` | IR: compile options |
| 45 | `on_unmapped` | `g2p.py` | Host, over the dropped-char report |
| 46 | `normalizer`, normalize plugins | `g2p.py` | Host H3 |
| 47 | Pipeline expand, mark | `pipeline.py` | Host H1, H2 |
| 48 | Pipeline rescore, declared rescorers | `g2p.py` | Host H5 |
| 49 | Sentence rescorers | `g2p.py` | Host H6 |
| 50 | Pipeline sandhi | `g2p.py` | Host H7 |
| 51 | `<phoneme>` markup | `markup.py` | Host H0 |
| 52 | Sandhi contexts and templates | `sandhi.py` | IR: patterns |
| 53 | Beam: empty slots, nasal pre-pass, final sort | `g2p.py`, `phonetok.py` | IR |
| 54 | Costs and floor | `weights.py` | Compile: integers (9.7) |
| 55 | Confidence | `phonetok.py` | Host |
| 56 | Unknown chars and digits in a word | `g2p.py`, `stress.py` | Change 9.2 |
| 57 | Character name and category tests | `vowels.py`, `phonetok.py` | Compile: bits |
| 58 | Distinctive features | `feats.py` | Compile |
| 59 | Spec inheritance | `json_loader.py`, `FIELD_INHERITANCE` | Compile |
| 60 | Token positions | `phonetok.py` | IR: offsets (9.8) |
| 61 | `sentence_lattice`, `features` outputs | `g2p.py` | Host: Python over the reference interpreter's paths |
| 62 | Metadata fields (17) and `tone_inventory` | audit key scan | Inert: no effect on output |

Counts: 62 rows. IR 41, compile 8, host 10, inert 2, ruled change 1 (row 56). Rows 27, 54 and 60 also carry a ruled change of section 9.

## 7. Growth without interpreter changes

### 7.1 The rule

A new spec field compiles to the primitives of 2.3. It needs a compiler change and new conformance vectors, and no interpreter change. A field that needs a new primitive is a design decision: it adds a primitive with its own semantics version (section 8.1), changes every interpreter in one PR, and changes this spec in the same PR. The general primitives that make this rare are: attribute bits with compiler-defined meaning, the predicate tree with any slot offset and the `count` quantifier, pattern rewrites, and the codepoint maps.

### 7.2 Test: every field added since tag 7.30.0

`git diff 7.30.0 -- orthography2ipa/schema.py orthography2ipa/types.py` adds 10 positional keys and these output-relevant spec fields. Each row shows the lowering to existing primitives.

| Field | Lowering |
|---|---|
| `before_final_vowel` | `ebit +1 vowel`, `ebit +1 silent_final`, slot +1 final: predicate |
| `before_mute_e` | `entry_in`, `ebit`, `exists` at offsets 0..3: predicate |
| `before_y` | `ebit +1 base_y`: new bit, predicate |
| `open_syllable`, `closed_syllable` | `syll open`, `syll closed` with vowel or `carries_nucleus` |
| `nucleus_secondary` | `syll idx_in_secondary` |
| `nucleus_stressed_open`, `_closed`, `nucleus_unstressed_open`, `_closed` | `and` of the two syllable relations |
| `stress` allophone values `pretonic`, `posttonic` | `syll idx_lt_stressed`, `not` |
| `preceded_by_3`, `followed_by_3` | class predicate at offset ±3 |
| `preceded_by_surface_phoneme_2` | `top_seg_in -2 1 set`: the last segment of the top candidate two slots back, over the pass input |
| `preceded_by_grapheme`, `followed_by_grapheme`, `followed_by_grapheme_not` | `entry_in ±1`, `not` |
| `word_contains_grapheme`, `_not` | `word_has`, `not word_has`: a substring test over the lowercased source word. This needed the new primitive 12. |
| `requires_other_nucleus`, `followed_by_nucleus` | `["top_nucleus","other"]` and `["top_nucleus","later"]`, negated when the field is false. The test reads each slot's top candidate on the pass input, so a silent ⟨e⟩ (top candidate `""`) does not count. |
| `surface`, `append` | precomputed `out` strings |
| `mutates_neighbor`, `mutates_neighbor_side` | rule `mutate` field (exists in the rescoring primitive) |
| `accent2_mark`, `accent2_final_letters` | decision list entry: penult test and a char set on the last letter |
| `antepenult_stress_endings` | decision list entry |
| `unstressed_prefixes`, `schwa_rimes` | decision list prefix adjustment |
| `tonic_after_diphthong` | mark placement string set |
| `diphthongs`, `ipa_diphthongs`, `closed_hiatus`, `final_diphthongs` | splitter string tables |
| `vowel_letters` | `syllable.vowel_letters` |
| `max_onset` (declared), `onset_clusters`, `constrain_onsets`, `constrain_mark_onsets` | licit-onset tables, splitter flags |
| `coda_liquid_capture` | splitter flag with a liquid bit |
| `secondary_stress`, `compound_stress`, `iambic_length` | flags of existing stages |
| `apostrophe_elision`, `word_internal_apostrophe` | char bits and the grouping rule |
| `doubled_letters_geminate` | rescoring flag |
| `grammatical_endings` | ending table |
| `codas`, `coda_no_inherent_vowel`, `consonant_nuclei`, `dependent_vowels`, `preposed_vowels`, `inherent_vowel_final`, `virama_final_vowel` | tokenizer entry bits and tables |
| `prevocalic_glide_backoff`, `trailing_vowel_axis_digraphs`, `vowel_graphemes` | entry bits |
| `tone_rules` (`tones`, `classes`, `marks`, `table`, `dead_codas`, `no_mark`), `tone_marks_syllable_final` | tone table and bits |
| `stress: false` | compiler emits no `stress` object |
| `audit`, `valid_ceiling` | metadata: inert |

Result: one field in the diff did not fit the first draft of the primitive set. `word_contains_grapheme` is a substring test over the word, and no predicate over slots expresses it, because the data uses substrings that are not entries (pt-PT ⟨oicamente⟩, `ie` ⟨arch⟩). IR v1 adds primitive 12 for it. Every other field lowers to the primitives of 2.3. Four fields needed a mechanism the 7.30.0 engine did not have, and v1 carries each as a primitive: the tokenizer branches for preposed vowels and consonant nuclei, the tone stage and the neighbour mutation. The test shows that new fields mostly need only a compiler change, and that a field which reads a new kind of fact (here, the spelling as a string) still needs a new primitive.

### 7.3 Expected limits

These features need a new primitive or a host hook, and the spec names them now so that they are a decision, not a surprise: tone sandhi across syllables and words (Mandarin third tone, Bantu spreading), scripts without spaces (word segmentation is a host step before S2), morpheme boundaries beyond endings and prefixes, and unvocalised Arabic and Hebrew (a diacritizer is a host step at H3). Vowel harmony at any distance fits `count`.

## 8. Versioning

### 8.1 Versions and the revision

A dialect profile is a compile option, and its program is part of the IR. So the IR revision of an IR compiled with a profile covers the dialect output, and an IR compiled without one carries no dialect step.

`ir_version` is the format major. It changes only for a change that is not additive: a removed or restructured table. An additive change (a new optional table, a new bit, a new predicate node with a default) keeps `ir_version`.

Each primitive of 2.3 and each predicate node of 2.5 has its own semantics version, an integer in a table that every interpreter ships: `{"beam": 1, "segment": 1, "word_has": 1, ...}`. A primitive's version changes only when its behaviour on some input changes: a bug fix in that primitive. A compiler change never moves it. A new primitive starts at version 1.

The IR revision, `orthography2ipa.ir.layout.spec_revision(ir)`, is:

```
"sha256:" + sha256( "o2i-ir\n" + manifest(ir) + "\n" + canonical(ir) )
manifest(ir) = ";".join(sorted(name + "=" + str(version) for each primitive, node, syll relation and set field the IR uses))
```

Each `syll` relation has its own version, named `syll.<relation>`.

An optional field that changes output has its own version too. The manifest lists it when the field is set: a true flag, or a list, set or object that is not empty.

| Field | Version name |
|---|---|
| `word.internal_apostrophe` | `internal_apostrophe` |
| `word.apostrophe_elision` | `apostrophe_elision` |
| `word.collapse_geminates` | `collapse_geminates` |
| `word.context_beam` | `context_beam` |
| `word.clitic_marks` | `clitic_marks` |
| `word.silent_stress_marks` | `silent_stress_marks` |
| `word.exceptions` | `overrides` |
| `allophone_map` | `allophone_map` |
| `syllable.closed_hiatus`, `syllable.final_diphthongs` | `hiatus` |
| `syllable.semivowels` | `semivowels` |
| `stress.cliticless` | `cliticless` |
| `stress.compound_last` | `compound_last` |
| `stress.tonic_after_diphthong` | `tonic_after_diphthong` |
| `stress.ipa_diphthongs` | `ipa_diphthongs` |
| `stress.mark_onsets` | `mark_onsets` |
| `allophony.geminate` | `allophony_geminate` |

The other fields belong to a primitive that the manifest always lists when their table is present, such as `decision` for the stress endings and `mark_placement` for `mark_diphthongs`.

So a fix to the Thai tokenizer branch moves the revision of a Thai spec, whose IR uses that branch, and leaves pt-PT, whose IR does not, as it was.

`canonical(ir)` is the runtime part of the IR (everything except `source`, `debug`, `primitives` and `ir_version`; `bits` is inside) as JSON with sorted keys, no whitespace and integers only, after these normalisations:

- `strings` sorted by codepoint order, `entries` sorted by key codepoints, and every index renumbered to match.
- Every set sorted ascending.
- Every field equal to its documented default left out.
- Predicates in normal form: nested `and` and `or` flattened, their children sorted by canonical bytes with duplicates removed, `not not p` replaced by `p`, `true` removed from `and`, and an `and` or `or` of one child replaced by the child.

The normal form makes many equivalent predicates hash equal, but not all. A compiler change that replaces an `and`/`not` pair with a new attribute bit gives the same output and a new revision. The revision is conservative: it can move when output cannot change, and it never stays equal when output can change. The compiler keeps such rewrites rare, and the release notes list every compiler change that moves revisions.

**Lexicon and provenance.** The IR revision covers the IR only: the spec data, the compile options and the interpreter primitives. It does not cover a lexicon.

The package functions describe the rules engine that `transcribe` runs, and they are not the IR revision. `orthography2ipa.spec_revision(lang)` hashes the spec JSON, its parent chain and the engine fingerprint. `lexicon_revision(lang, patches=)` covers the packaged lexicon. `transcription_revision(lang, patches=False)` covers the default path, which reads both:

```
transcription_revision(lang, patches=False) = "sha256:" + sha256(spec_revision(lang) + "\n" + lexicon_revision(lang, patches=patches))
```

When no installed package supplies the lexicon files, the lexicon term is the string `none`.

The loom exporter writes the IR revision as `O2I_REVISION[lang]`, in `o2i.spec_revisions` and as the `revision` of `o2i.phonemizer_identity`. Its `expect_revisions` argument takes IR revisions. The Lua interpreter returns the IR revision from an `info` call and never computes it. loom carries no lexicon, so the IR revision alone covers its output.

### 8.2 Compiling older spec data

`compile(lang, data_ref=<tag or commit>)` reads `orthography2ipa/data/*.json` at that ref from the git checkout that holds the package, resolves inheritance with the current loader, and compiles with the current compiler. `source.data_ref` and `source.compiler_commit` record both.

It guarantees: when only spec data changed between the data ref and the compiler's commit, the output equals the old release's output. It does not guarantee equal output when the engine changed between the two: a bug fix, a new default, a ruled change of section 9 or a changed Unicode table can change the output of old data. The compiler does not imitate old engine behaviour.

Missing fields: a field that old data lacks takes the current default.

**Acceptance test: Kabyle 7.30.0.** Two Kabyle voices (`phoonnx_kab-DZ_miro_o2i`, `phoonnx_kab-DZ_dii_o2i`) were trained on orthography2ipa 7.30.0. A sample file holds 3,000 `[text, ipa]` rows from that release. The drift to later output comes from a data change (⟨ɣ⟩ from `ɣ` to `ʁ`, and the ⟨k⟩ and ⟨c⟩ readings). The legacy engine reproduces all 3,000 rows from the 7.30.0 data. The test compiles `kab` at data ref `7.30.0` and runs the 3,000 texts. Each row must give the file's IPA. A mismatch must trace to a ruled change of section 9 or a named engine change, listed in the test's expected-differences file. Any other mismatch is a compiler defect.

### 8.3 Compatibility

An interpreter declares the `ir_version` values and the primitive versions it supports. It refuses an IR whose `ir_version` or manifest holds anything else, with an error that names the primitive and both version numbers. It keeps every published `ir_version`. The compiler refuses to emit an IR for a target that lacks a primitive the spec needs, and names the primitive. That replaces the Lua PoC's `error("unported: ...")` checks.

### 8.4 Conformance vectors

A vector file is JSON Lines. The first line holds the IR. Each later line is one case with codepoint arrays:

```json
{"kind": "ir", "lang": "pt-PT", "revision": "sha256:...", "ir": {}}
{"kind": "case", "input": [111,115,32,106,111,103,111,115], "expect": [117,32,712,658,596,609,117,643]}
{"kind": "case", "input": [], "expect_error": "unsupported primitive version"}
```

The example is pt-PT ⟨os jogos⟩ → `u ˈʒɔɡuʃ`, the output of the engine at `690611bb2`. Every interpreter must give `expect` byte for byte. **Dialect corpus.** For each of the 15 profiles, the vector file holds every row of `tests/data/ep_dialect_sentences.csv` as `csv.DictReader` reads it: 235 rows, 228 distinct texts in the `text` column. The expected output is the legacy `G2P("pt-PT", dialect_profile=profile).transcribe(text)`. That gives 3,525 cases. The reference interpreter must match the legacy output byte for byte on all of them before the legacy `transforms.py` path is retired. Targeted cases add every context of 3.10.4, a sentence whose IPA and spelling word counts differ, an empty spelling, a lexical rule hit through a capitalised spelling word (the key test lowercases the spelling word), two lexical rules that match the same word (the last one wins), and a chain-shift mapping whose output is not a vowel (the off test reads the input codepoint).

The package generates vectors from the Python reference interpreter into `tests/conformance/ir-v1/`: for each spec a fixed sample of its gold or test data, plus targeted cases for every pattern, beam tie, normalisation rule, predicate node, tokenizer branch, ruled change and unknown version.

### 8.5 Stable Python API

These names keep their meaning, because outside code depends on them:

| Name | Notes |
|---|---|
| `transcribe(text, lang, ...)` | the rules engine |
| `G2P(lang, pipeline=Pipeline(lexicon=...))`, `transcribe`, `transcribe_detailed` | the rules engine plus host hooks |
| `Pipeline` with `lexicon`, `syllabifier`, `expand`, `mark`, `rescore`, `sandhi` | the hooks of 3.1 |
| `registry.get`, `resolve`, `available_codes` | compile-time Python |
| `phoneme_inventory(spec, lexicon=None)` | `inventory.py`, package root; phonematcher's coverage benchmark (`benchmarks/tasks/coverage.py`) reads it |
| `packaged_lexicon(lang, patches=)`, `packaged_lexicon_sources(patches=)` | lexicon data for H4 |
| `spec_revision(lang)` | unchanged: the spec JSON, its parent chain and the engine fingerprint (8.1) |
| `lexicon_revision(lang, patches=)` | unchanged |
| `transcription_revision(lang, patches=False)` | added: `spec_revision` plus the packaged lexicon (8.1) |
| `exceptions.EngineSourceUnavailable` | unchanged |
| `allophony.segment_ipa` | IPA utility; stays in Python, and interpreter primitive 11 implements the same rule |

Spec loading, the registry and the inventory stay compile-time Python.

## 9. Semantic changes from the legacy engine

Each change removes a runtime phonetic or Unicode test. Each one is measured before the switch on four corpora: the benchmark board (WikiPron gold, metric PER and changed-word count per language), the 336,234 recorded words (changed-output count per language), the pt-PT parity file of 4,569 lines, and the Kabyle 7.30.0 sample. A change that moves a language's PER up by more than the board's noise floor goes to a ruling before the switch, with the changed words listed.

### 9.1 Onsets from a compiled table

- Old: `_OnsetJudge` and `_IpaOnsetJudge` judge any consonant run at runtime from sonority, place, voicing, sibilance, glottality, laterality and glide features.
- New: the compiler runs the same judges on the unit sequences of 2 to 5 units that 3.7.2 searches, and writes the licit ones as a table (3.7.2). At runtime a run is licit only if its unit sequence is in the table.
- Why: the judges are a feature grammar. The table removes sonority and feature tests from every interpreter.
- Effect: none for runs built from the spec's own units. A run with a unit the spec does not produce (foreign input, an unseen IPA segment from a host hook) becomes unlicit instead of judged. Measure: changed-word count per language on the board and the recorded words. Expected: zero outside foreign-input words.
- Effect of the 5-unit cap: a run of 6 or more units that the legacy judge licenses by stacking glides on a declared onset is not licit. No gold word of the 346 languages with a gold set needs such a run: 0 of 242,822 words.

### 9.2 Unknown characters: boundaries, not letters

- Old: a character with no entry is dropped from the IPA, but the written syllabifier still tests it with `is_orthographic_vowel` and `isalpha`. A vowel from another script adds a syllable. pt-PT ⟨casa⟩ gives `ˈkazɐ`, and ⟨casa⟩ plus Cyrillic ⟨а⟩ gives `ˈkɐzɐ`.
- New: a character outside the known ranges (section 4) is unknown. In S4 it is an UNKNOWN token, as in the legacy tokenizer: it stops the longest match, so the letters on its two sides never join into one key, and it gives no slot. In S5 and every later stage that reads the written word, it is removed, so it adds no syllable and no positional context. It appears in the dropped-character report, which feeds `on_unmapped`. The written syllables map to tokens through the offsets of the removal.
- Why: one rule, no Unicode vowel or letter test at runtime.
- Effect: mixed-script words get the syllables and stress of their known letters. Letters on the two sides of an unknown char stay apart, as in the legacy engine: de-DE ⟨s😀chön⟩ keeps `ˈzçœn`, cy ⟨l😀lan⟩ keeps `llan`, and pl ⟨s⟩ + Cyrillic ⟨а⟩ + ⟨zum⟩ keeps its two letters. Measure: changed-word count per language on the board and recorded words, with three counts kept apart: syllable-count changes, stress moves and key changes. Expected: syllable and stress changes only in words with unknown chars, and zero key changes.

### 9.3 Digits

- Old: digit tokens inside a word are dropped by the context beam. `'a 12 b'` gives `'ɐ ˈb'`. The fallback `word if best is None` never fires, because `ipa_beam` always returns a path.
- New: the same. A digit that no key claims is an UNKNOWN-like boundary under 9.2. IR v1 keeps the fallback rule as written, with zero measured effect.
- Why: digits need a text normaliser, which is host step H3.
- Effect: none measured.

### 9.4 Inert positional keys

- Old: `intervocalic_cross_word` (14 specs), `onset` (16 specs), `coda`, `consonantal` and `vocalic` are declared in data, but `grapheme_positions` never emits them, so they have no effect.
- New: inert. The compiler writes no rule, and lists them in `debug.inert_positions` and in a compile lint.
- Why: implementing them would change the output of 30 specs with no reviewed source behind the change. Keeping them inert keeps output equal and the predicate set unchanged.
- Recommendation: inert in v1. File one issue per position with the specs that declare it. Each owner either deletes the entry or asks for the position in a ruled change. Measure: none needed, output equal.

### 9.5 Positional vowel tests read entry bits

- Old: `GraphemeContext.is_vowel`, `is_front`, `is_back`, `is_palatal` and `is_emphatic` are computed from the grapheme and the flat table each time.
- New: the same values as entry bits.
- Why: they are per-entry constants, and the compiler computes them once.
- Effect: none. Measure: the parity of every positional decision on the board corpus.

### 9.6 IPA segmentation as a primitive

- Old: `segment_ipa` uses `unicodedata.combining` and categories Lm, Sk at runtime.
- New: primitive 11 with the compiled `modifier` char bit and compiled atom lists (3.6.3). The rule is the legacy rule.
- Why: removes the Unicode category test. The output stays the same for every char in the `modifier` table.
- Effect: none for spec data. The compiler scans every reading and rule output, so every modifier the spec can emit has the bit, including U+207F ⟨ⁿ⟩, which lies outside the known ranges of section 4. Only a modifier that the spec never emits and that comes from a host hook lacks the bit. Measure: segmentation parity over every reading of every spec and the board's IPA output; the round-2 audit found 0 changed words in 5 specs that use ⟨ⁿ⟩.

### 9.7 Integer costs

- Old: float costs and float sums, final sort `(score, ipa)`.
- New: integer micro-nats, sort `(cost, ipa, creation index)` (2.6).
- Why: interpreters agree bit for bit on every platform.
- Effect: n-best order in beam mode can change where float sums differed in the last bits. In en-GB, the only weighted spec, such pairs do not change the 1-best output, because each slot's costs do not depend on the path. Measure: 1-best and n-best order over the en-GB board and recorded words, in beam mode at width 8.

### 9.8 Token positions and override keys in the caller's text

- Status: deferred. IR v1 keeps the legacy behaviour: `Token.position` indexes the prepared text, and the override lookup sees the prepared spelling.
- Planned change: offsets into the caller's text, so that a lexicon entry spelled with an addak or a shadda matches.
- Why deferred: the change alters output, and the IR v1 gate is byte parity with the legacy engine. It lands as a separate ruled change with its own measure: changed-word count for `pa`, `ar` and the Arabic-script specs, and the arbtok and tugaphone suites.

## 10. Lua interpreter size

The PoC driver `loom_driver.lua` has 3,416 lines, 3,130 of them code, for pt-PT only. The estimate takes each section's real size, removes what becomes a compiled table, and adds what the PoC refuses or v1 adds. The PoC refuses these 12 features, and the estimate includes all of them: secondary stress, `accent2_mark`, `vowel_letters`, `coda_liquid_capture`, `unstressed_prefixes`, prevocalic glide back-off, `trailing_vowel_axis_digraphs`, the aperture positions, silent stress marks, the emphatic class, the plain tokenizer beam and `_cut_written_syllables` with a dropped vowel letter. It also includes the features refused at spec load: grapheme weights, `constrain_onsets`, abugidas, tone, gemination rewrites, `mutates_neighbor`, grammatical endings and lookaround. The legacy runtime modules hold 5,076 Python code lines, and `stress.py` alone holds 869 code lines outside the onset judges.

| Stage | PoC lines (section span) | Moves to tables | Added for v1 | Estimate |
|---|---|---|---|---|
| Unicode, UTF-8, NFC | 326 (15-340) | all tables; NFC becomes a map | codepoint maps, offsets, known ranges | 90 |
| JSON | 82 (341-422) | all; loom reads a Lua literal | none | 0 |
| Vowels | 260 (423-682) | all; bits | none | 0 |
| Spec loading | 294 (683-976) | all | IR accessors, version manifest | 60 |
| IPA segmentation | 80 (977-1056) | category tests | primitive 11, two atom lists | 70 |
| Tokens, contexts, beam | 172 (1057-1228) | context bits | preposed, circumfix, inherent vowel, consonant nuclei, marker heads, decomposition, prevocalic back-off, plain beam | 520 |
| Stress | 668 (1229-1896) | onset judges (about 150) | weight stress, iambic length, hiatus filter, secondary stress, `accent2_mark`, `vowel_letters`, prefixes, coda liquids, silent marks, aperture | 1,000 |
| Allophony | 427 (1897-2323) | class tests | predicate evaluator with `count` and `word_has`, `mutates_neighbor`, emphatic | 450 |
| Rescorer driver | 30 (2324-2353) | none | none | 30 |
| Positional | 130 (2354-2483) | position lowering | predicate rules, trailing-axis bits | 80 |
| Pattern matcher, sandhi, rewrites | 205 (2484-2688) | the parser (about 70) | lookaround, both anchors, global sub | 180 |
| Engine | 710 (2689-3398) | glide back-off reading tests | tone, virama, tone docking, endings, elided clitics, dropped-vowel cut | 820 |
| Dialect program | 0 | none | primitives 13 to 16, class lookbehind | 150 |
| Entry point | 17 | none | `info` call | 20 |
| **Total** | 3,416 | | | **about 3,450** |

The Lua interpreter is about 3,300 lines for the core stages and about 150 lines for the dialect program, about 3,450 in total. Two cuts change output and are measured later as ruled changes: end-relative stress-mark placement in place of the alignment heuristics of 3.8.3 (about 300 lines), and the Thai and Lao preposed-vowel branch as a compile-time reordering rewrite (about 120 lines).

## 11. Decisions

**11.1 Positional keys that are never emitted.** They are inert (9.4). Each one has an issue that lists the specs that declare it. A position such as `cross_word_vowel`, or a syllable-position predicate, enters only as a ruled change.

**11.2 Mark placement.** `apply_stress_mark` and the cut and fold helpers stay in the interpreter. End-relative placement is measured on the board as a later ruled change.

**11.3 Mixed-script input.** Unknown characters follow 9.2. The legacy behaviour, which needs a vowel test over all of Unicode, is not kept.

**11.4 Combining marks inside sandhi classes.** P17, P18 and P67 keep Python semantics. The three patterns are reported to their specs as defects.

**11.5 Dialect profiles.** Dialect profiles export. They compile to the dialect program of 3.10.2, built on primitives 13 to 16. The dialect corpus of 8.4 checks byte parity with the legacy transforms.

**11.6 Two tokenization passes.** Both passes stay (3.3.3).

**11.7 Gemination and casefold fields.** The gemination rewrite field and a casefold override field enter the spec schema in one design PR that quotes the schema clause it extends. Until then, the compiler derives them from `script`, as the legacy code does.

**11.8 Size.** The Lua interpreter is about 3,300 lines plus about 150 lines of dialect primitives. The two output-changing cuts of section 10 are measured later as ruled changes.

---
[← Public API stability](../reference/api_stability.md) · [Home](../index.md) · [Architecture →](../engine/architecture.md)
