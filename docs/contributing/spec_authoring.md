# Writing a language spec

A language is one JSON file under `orthography2ipa/data/`, named by its code. The engine is language-agnostic, so you add a language by writing cited data, never code. This page gives the procedure first. Then it gives the rules that keep a spec a linguistic description and not a lookup table. A violation of a rule degrades every consumer of the data, even when a score goes up. The field reference is [`SCHEMA.md`](../../orthography2ipa/data/SCHEMA.md), and the Python view of a loaded spec is in [data model](../specs/data_model.md).

## What a spec declares

A spec must declare `graphemes`, `phonemes`, or both ([the inventory](../../orthography2ipa/data/SCHEMA.md#phonemes-the-inventory-stated-directly)). The field `orthography_kind` says which kind of writing the graphemes are ([orthography kind](../specs/data_model.md#orthography_kind-native-scripts-romanizations-and-transliterations)).

A spec does not declare a `family` string. The family comes from the clade nodes above the spec in the ancestry graph (see [Classification](#classification-wire-it-into-the-clade-chain)). A spec also has no engine hooks. If a language needs behaviour that the shared engine cannot express, the engine or the spec vocabulary has a gap. Close the gap as [engine.md](engine.md) describes. Do not write code for one language.

## Procedure

1. Create `orthography2ipa/data/<code>.json`. Set `code`, `name`, `script` and an honest `quality`. Use `stub` when the spec is a stub ([quality tiers](../specs/quality_tiers.md)). A variety with no ISO 639-3 code takes a private-use code ([minting a lect code](../../orthography2ipa/data/SCHEMA.md#minting-a-private-use-lect-code)).

2. Declare `graphemes` or `phonemes`.

3. Keep `graphemes` to real orthographic units ([A grapheme key is an orthographic unit](#a-grapheme-key-is-an-orthographic-unit)).

4. Put each context in the rule layer, never in extra keys ([Express a context](#express-a-context)). The position keys are in [positional graphemes](../engine/positional_graphemes.md).

5. Cite every claim in `sources`, as [citation honesty](citations.md) describes.

6. Add `glottolog_code`, `wikidata_qid` and `iso639_3` where they exist. Make sure that each identifier resolves to this language. A null code is better than a wrong one.

7. Connect the ancestry with `parent` or `ancestors`. Give a new language or dialect the full `ancestors` list, because it carries the most data. A dialect that differs little from its parent can use `parent` alone. The ancestor roles and their typical weights are in [data model](../specs/data_model.md#ancestorrole) and in [`SCHEMA.md`](../../orthography2ipa/data/SCHEMA.md#ancestor-role-values).

8. Make sure that the parent has its own file. A dialect needs its standard variety. A historical language needs an ancestor chain that reaches a proto-language.

9. If an ancestor or a related lect has no file, add a cited stub. Leave no dangling reference. Add a grouping node (`"clade": true`) only when the literature recognises the group.

10. For a dialect, inherit the parent's tables with `graphemes_base` and the related fields (see [Inherit a parent's tables](#inherit-a-parents-tables)).

11. Run the tests that name the language (see [Run the tests](#run-the-tests)).

## A minimal spec

This file has one plain grapheme, one digraph, one positional rule and one parent link. The field `notes` holds the citation in prose, and `sources` holds it as data.

```json
{
  "code": "xx-YY",
  "name": "Language Name",
  "script": "Latin",
  "quality": "stub",
  "graphemes": {
    "a": ["a"],
    "ch": ["tʃ"]
  },
  "allophones": {
    "a": ["a"],
    "tʃ": ["tʃ"]
  },
  "positional_graphemes": {
    "b": {
      "default": ["b"],
      "intervocalic": ["β"]
    }
  },
  "parent": "parent-code",
  "ancestors": [
    {"code": "parent-code", "role": "parent", "weight": 0.85, "notes": "Primary descent"}
  ],
  "notes": "Source: Author (year). Title."
}
```

The package layout and the loader functions (`load_json_spec`, `load_all_json_specs`, `available_json_codes`) are described in [architecture](../engine/architecture.md).

## Classification: wire it into the clade chain

A family is a clade node, and a clade node holds classification only. You classify a new language when you point its `parent` at the correct node. Then `family` and `family_path` derive themselves ([data model](../specs/data_model.md#derived-classification-family-family_path-clade)).

If the clade of the language has no node, add the node. Do not write a `family` string to go around the missing node. An explicit `family` string is correct only for a grouping that is not a genetic clade. The node format and the full contract are in [`SCHEMA.md`](../../orthography2ipa/data/SCHEMA.md#clade-nodes-and-the-derived-family).

## Inherit a parent's tables

A dialect shares most of its data with a parent variety. It inherits that data through the `*_base` fields and states only the entries that differ:

```json
{
  "code": "xx-YY-x-dialect",
  "graphemes_base": "xx-YY",
  "graphemes": {
    "only": ["overrides"]
  },
  "allophones_base": "xx-YY",
  "allophones": {
    "only": ["overrides"]
  }
}
```

The merge is one level deep, and `null` deletes an inherited entry ([`SCHEMA.md`](../../orthography2ipa/data/SCHEMA.md#inheritance)). So when a dialect states one context for a letter, write again each base context that the dialect keeps. Do not make a cycle of `*_base` references. The base edge that each field follows, and how the loader resolves a chain, are in [data model](../specs/data_model.md#inheritance-between-specs).

## Metadata worth filling in

A spec also records what the language is. Fill in `sources`, `orthography_standard`, `location` and `timespan`. Add the cross-references `glottolog_code`, `wikidata_qid`, `phoible_id`, `wals_code` and `iso639_3`, and the reader links `wikipedia` and `urls`. [`SCHEMA.md`](../../orthography2ipa/data/SCHEMA.md#fields) defines each field and what reads it.

## Looking for a source: what a phone inventory cannot tell you

A grapheme table maps a letter to the phones that it can take. A phone inventory lists the phones that a variety has. These are different facts, and the second never settles the first. A variety with both /q/ and /ɡ/ in its inventory still leaves ⟨ق⟩ undecided, and that reflex is the fact a spec records.

The sources that are easiest to reach are inventories. PHOIBLE is the obvious place to look, and the `phoible_id` field points to it. It covers Arabic only at the level of the macrolanguage and the standard variety. A search of the full database by ISO code returns zero segments for `ayh`, `acq`, `abv`, `ssh`, `aao`, `adf`, `aec`, `avl`, `ayp`, `bbz` and `sqr`. Where PHOIBLE has an inventory, it gives phones and no letter mappings.

A sound-definition list in a phonetic description has the same limit. Dawod's 1952 thesis on the Aden dialect lists "voiced velar plosive" and "voiceless uvular plosive" in readable English, so Aden has both. Its one table that maps letters to those sounds has a symbol column that is not legible on the scan. The inventory is legible, and the reflexes cannot be recovered.

So when a source is hard to get, first ask whether it answers the question. A spec needs a statement such as "⟨ق⟩ is realised as X in this variety", with a page number. Some evidence shows only that a phone or a letter occurs. Examples are an inventory, a phoneme count, a section on velar stops in a table of contents, and a corpus frequency count. None of them licenses a reading.

If no such statement is available, write a `stub` that says so and names where the description would be. Do not fill a `research` spec from the nearest inventory.

## Run the tests

`scripts/which_tests.py` lists the test files that assert on a language. Run those files:

```bash
PYTHONPATH=$PWD python scripts/which_tests.py --lang fi
PYTHONPATH=$PWD python -m pytest $(PYTHONPATH=$PWD python scripts/which_tests.py --lang fi)
```

The script writes one test file per line to stdout and a summary line to stderr. With no `--lang`, it reads the specs that changed against `origin/dev`. With `--no-children`, it matches the exact code only and leaves out the specs that inherit from it. A family test file that passes does not prove that a `test_cited_rules_*.py` file for the same language passes.

The checks over every spec run in the full suite. These files hold them:

| Test file | What it checks |
|---|---|
| `tests/test_language_integrity.py` | Required fields, `graphemes` or a declared inventory, existing `parent` and ancestor codes, weights in range, no parent cycles, and facts for key languages |
| `tests/test_data_quality.py` | An explicit `quality` tier, content above `stub`, no own table on a stub, and the `production` benchmark bar |
| `tests/test_sources.py` | At least one real source on every spec above `stub`, with well-formed fields |
| `tests/test_grammatical_endings.py` | A cited `notes` sentence for every ending, the evidence for every list-valued ending, and a cap per spec |

## The rules a spec keeps

A spec describes how a language is written and pronounced. It is not a list of words or of frequent substrings. These rules keep it a description.

### A grapheme key is an orthographic unit

A key in `graphemes` must be a unit that the writing system treats as one symbol. That is a letter (`b`, `ä`, `ц`) or a multigraph that the orthography reads as one unit. Examples are Spanish ⟨ch⟩ /tʃ/, Portuguese ⟨lh⟩ /ʎ/, English ⟨sh⟩ /ʃ/, German ⟨sch⟩ /ʃ/, Polish ⟨szcz⟩ /ʂtʂ/ and a pinyin final such as ⟨iang⟩. A multigraph earns its key when one of these three tests passes:

1. Its IPA is not the concatenation of the IPA of its parts. ⟨sch⟩ is /ʃ/, and s+c+h gives /sx/.

2. It spells one phonological unit: one segment or one syllable nucleus. This covers diphthongs (Finnish ⟨ai⟩), affricates (⟨dž⟩), prenasalized stops (Bantu ⟨mb⟩), clicks (⟨gc⟩) and aspirates (Urdu ⟨پھ⟩). It also covers geminates (⟨tt⟩ /tː/) and the letter-plus-diacritic units of an abjad or an abugida. A vowel sequence earns a key only when the language treats it as one unit for prosody or phonology.

3. It blocks a wrong maximal-munch match. The tokenizer is greedy, so a key can earn its place when it defeats a wrong neighbour. Mirandese ⟨anh⟩ /aɲ/ exists because without it the nasal-vowel digraph ⟨an⟩ wins, and ⟨danho⟩ reads /dɐ̃u/. Say so in `notes`.

A key that fails all three tests is noise. ⟨bl⟩→/bl/ fails because b+l already gives /bl/. Russian ⟨бь⟩→/bʲ/ fails because the engine already reads ь as /ʲ/. The tokenizer always takes the longest key that matches, so the order of the keys in the file has no effect on the match.

These keys are forbidden:

- Cartesian products: every consonant pair (`bd`, `bf`, `bk`) or every consonant-vowel pair (`дзе`, `дзё`, `дзю`). A block of keys that looks like the output of a nested loop is wrong.

- Morpheme and suffix chunks such as `tion` or `cious`. A closed irregular set goes in `word_exceptions`. A cited suffix rule goes in `grammatical_endings` ([Declare a grammatical ending](#declare-a-grammatical-ending)).

- Statistical substrings, that is, keys that exist because a sequence is frequent.

- Positional spellings of one letter. Spanish ⟨c⟩ before ⟨e⟩ or ⟨i⟩ is a context of ⟨c⟩, so it goes in `positional_graphemes` and gets no key of its own.

- Rare or archaic spellings, unless the spec describes a historical variety.

Before you delete a key that an audit flags, apply all three tests. Then delete it and run the tests. If a test fails, the key encodes a fact. Find the fact and state it as a rule, or keep the key and write in `notes` which test it passes.

### Order the IPA values

The order of a grapheme's IPA list is data. When the spec gives no `weights`, the first value is the cheapest path through the beam and each later value costs one step more. Put the most frequent reading first. If the frequency is not known, put the citation form of the dictionary first. Put regular readings before irregular or lexicalised ones. `tests/test_language_integrity.py` checks that the first value of every list is a string.

A grapheme that is always silent maps to an empty string. Spanish ⟨h⟩ is `"h": [""]`.

### Fill the allophone map

The allophone map lists the phonetically distinct surface forms of each phoneme. These forms belong in it:

- Allophones that the context predicts, such as place assimilation, lenition and aspiration.

- Stylistic or register variants that a source documents.

- The variants of each dialect, when the spec is a standard variety that covers several dialects.

These forms do not belong in it:

- Free variants with no conditioning. List only the dominant one.

- Variants of one speaker, or very marginal variants.

- Sounds that the literature describes as separate phonemes.

Put the citation form first: the form of slow, careful speech or of a dictionary recording. The contextual variants follow it. The English /t/ of `en-US` is `"t": ["t", "tʰ", "ɾ", "ʔ", "t̚"]`. A list that starts with `tʰ` has no citation form at its head.

An allophone list marks a deletion with an empty string, as `es-ES-x-andalusia-w` does for coda /s/ (`"s": ["s", "h", ""]`). The distance code also reads `∅` as no phone.

### Express a context

A sound that depends on its neighbours, its position or the stress is a rule, not a spelling. Pick the mechanism from this table.

| The context | The mechanism |
|---|---|
| A neighbouring sound or letter class | `allophone_rules` with `preceded_by` or `followed_by` (`vowel`, `consonant`, `front_vowel`, `back_vowel`, `palatal`, `word_boundary` and more) |
| A neighbour two or three slots away | `preceded_by_2`, `followed_by_2`, `preceded_by_3`, `followed_by_3`, `preceded_by_phoneme_2`, `followed_by_phoneme_2` |
| The position in the word or syllable | `positional_graphemes`, `word_initial`, `word_final`, `syllable_position` |
| The stress | The `stress` block and the `nucleus_stressed` position |
| A word boundary | `sandhi_rules` |
| A closed irregular set | `word_exceptions` |
| Competing readings | Several candidates with `weights` (see [how cost works](../engine/lattice.md#how-cost-works)) |

Each mechanism has its own page: [allophony](../engine/allophony.md), [positional graphemes](../engine/positional_graphemes.md) and [the sentence-context seam](../engine/lattice.md#the-sentence-context-seam). A context written as extra keys asserts spellings that the language does not have. The tokenizer is maximal-munch, so the extra keys also change how neighbouring rules see the word.

If no mechanism can say what the language does, the engine lacks a predicate. Add the predicate as [engine.md](engine.md) describes. Do not enumerate spellings to simulate it.

A cluster is never a grapheme. Use `followed_by: "consonant_cluster"`. The same violation can hide in the rule layer: a `followed_by_phoneme` list of many cluster strings is an enumeration. A closed natural class such as `["p", "t", "k"]` is correct.

### Audit the data

A derivable key has an IPA value that is the concatenation of parts that the spec already maps. It is the signature of enumeration. This script resolves inheritance first, because a spec with `graphemes_base` keeps only its own keys in the file. Run it from the repository root:

```bash
PYTHONPATH=$PWD python3 - <<'EOF'
import json, glob, os
import orthography2ipa

def ipas(v):
    v = v.get('ipa', []) if isinstance(v, dict) else v
    return [x for x in (v if isinstance(v, list) else [v]) if isinstance(x, str)]

for f in sorted(glob.glob('orthography2ipa/data/*.json')):
    own = json.load(open(f)).get('graphemes')
    if not isinstance(own, dict):
        continue
    code = os.path.basename(f)[:-5]
    try:                                    # resolved = inheritance applied
        res = {k: ipas(v) for k, v in orthography2ipa.get(code).graphemes.items()}
    except Exception:
        continue
    for k in own:
        for i in range(1, len(k)):
            a, b = k[:i], k[i:]
            if a in res and b in res:
                cat = {x + y for x in res[a] for y in res[b]}
                if set(ipas(own[k])) and set(ipas(own[k])) <= cat:
                    print(f"{code}: {k!r} -> {ipas(own[k])} == {a!r}+{b!r}")
                    break
EOF
```

Each hit is a key to delete or a real unit that needs a `notes` line. Many hits are diphthongs and affricates that pass test 2. The script reads only the value, so it cannot see the shape of a cartesian block. A key such as Russian ⟨ки⟩ /kʲɪ/ is not к+и, because it bundles palatalisation and vowel reduction. A block of every consonant-vowel pair is still a cartesian product, whatever its values say.

`positional_graphemes` can hide the same block. This script lists every multi-character positional key:

```bash
python3 - <<'EOF'
import json, glob, os
for f in sorted(glob.glob('orthography2ipa/data/*.json')):
    pg = json.load(open(f)).get('positional_graphemes')
    if not isinstance(pg, dict):
        continue
    multi = [k for k in pg if len(k) > 1]
    if multi:
        print(f"{os.path.basename(f)[:-5]:24s} {multi}")
EOF
```

Judge each key with the three tests. A real multigraph (⟨ch⟩, ⟨sch⟩, ⟨mb⟩) belongs there. A consonant-vowel pair does not.

### A shared alphabet is not a shared phonology

Do not generate the rules of one language from the template of another language. Derive each inventory from the language's own sources, and check every generated rule against a cited form in that language. Ukrainian is the warning case. It writes the Cyrillic alphabet of Russian, but uk ⟨и⟩ is a hard /ɪ/, so a Russian softening rule on ⟨и⟩ palatalises the wrong consonants. Ukrainian ⟨л⟩ is velarised /ɫ/, so its geminate is /ɫː/.

### Declare a grammatical ending

Some endings take their sound from the grammatical ending and not from the letters that spell it. Examples are French mute ⟨-er⟩ and ⟨-ez⟩, and English ⟨-tion⟩ [ʃən]. Declare such an ending in `grammatical_endings`, never as a grapheme key, because a morpheme chunk is a forbidden key. The match rules and the precedence are in [`SCHEMA.md`](../../orthography2ipa/data/SCHEMA.md#grammatical-endings).

An ending can have more than one correct reading that the spelling does not choose between. French verbal ⟨-ent⟩ is mute, and nominal ⟨-ent⟩ is [ɑ̃]. Do not pick one, and do not write a word list. Declare an ordered candidate list, so that both readings reach the lattice and a rescorer downstream can choose ([ambiguous endings](../../orthography2ipa/data/SCHEMA.md#ambiguous-endings)).

Each ending needs a sentence in the spec's `notes` that starts with `ENDING "<ending>"`. The same sentence cites an author and a year from the spec's `sources`. `tests/test_grammatical_endings.py` fails a spec that leaves out the sentence or the citation.

### Ambiguous grammatical endings

A list-valued `grammatical_endings` entry puts a reading into the beam that the spec cannot choose. It is the one way that morphological ambiguity reaches the lattice. A review of a change that adds or widens a list-valued ending verifies three things in writing:

1. The lattice hole is proven. The change shows that the missing reading is absent from `word_candidates` at a generous *k* and beam width over a named gold sample. It also shows the reachability after the change. A reading that some *k* already reaches is a ranking problem, so the entry is rejected.

2. The order is cited. The reading at rank 1 carries a source or a measurement on gold, in the spec's `notes` beside the ending.

3. The oracle change is reported apart. It does not count as ranking-error headroom or as a win over another system (see [benchmarks](../evaluation/benchmarks.md#injected-alternatives-do-not-count-as-ranking-error)).

`tests/test_grammatical_endings.py` checks that the notes hold the evidence for the first two. A list-valued ending needs a `lattice-hole evidence for "<ending>"` passage and an `ordering basis for "<ending>"` passage. The test also caps the list-valued endings of one spec at `MAX_AMBIGUOUS_ENDINGS_PER_SPEC`. A change to the cap is a change to [`AGENTS.md`](../../AGENTS.md), argued there first.

### Supply a lexicon, never bundle one

The package ships descriptions: grapheme maps, rules, inventories and ancestry. It ships no word lists, lexicons, gold sets or weights. A lexicon is a corpus. A bundled lexicon makes the wheel larger and freezes a corpus into a release.

Deep orthographies such as English and Danish cannot reach production accuracy from rules alone. The answer is a lexicon that the caller registers at run time, or a separate package that supplies one through the `orthography2ipa.lexicons` entry points. The API, the file format and the precedence are in [lexicon](../guide/lexicon.md#supplying-a-lexicon).

Do not buy accuracy back inside a spec with suffix pseudo-graphemes or a growing `word_exceptions`. Text normalisation, diacritic restoration, script conversion and morphology belong downstream, in a consumer of the lattice. Examples of such consumers are [arbtok](https://github.com/TigreGotico/arbtok), [tugaphone](https://github.com/TigreGotico/tugaphone) and [scriptconv](https://github.com/TigreGotico/scriptconv).

The specs assume normalised input.

---
[← Bibliography](../specs/bibliography.md) · [Home](../index.md) · [Citation honesty →](citations.md)
