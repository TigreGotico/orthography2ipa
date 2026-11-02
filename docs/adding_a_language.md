# Adding a language

A language is one JSON file under `orthography2ipa/data/`, named by its code. The engine is language-agnostic, so you add a language by writing cited data, never code. This page is the procedure. The field reference is [`SCHEMA.md`](../orthography2ipa/data/SCHEMA.md), and the rules that a spec must keep are in [spec authoring rules](contributing/spec_authoring.md).

## What a spec declares

A spec must declare `graphemes`, `phonemes`, or both. It may not be silent about both. Some languages have a phonology and no grapheme rule to write. A logographic script has no letter-to-sound map, so `zh-Hani` ships an empty grapheme map and a declared inventory. An unwritten or reconstructed language has no orthography at all. The field `orthography_kind` says which kind of writing the graphemes are ([orthography kind](../orthography2ipa/data/SCHEMA.md#orthography-kind)).

A spec does not declare a `family` string. The family comes from the clade nodes above the spec in the ancestry graph (see [Classification](#classification-wire-it-into-the-clade-chain)). A spec also has no engine hooks. If a language needs behaviour that the shared engine cannot express, the engine or the spec vocabulary has a gap. Close the gap as [engine.md](contributing/engine.md) describes. Do not write code for one language.

## Procedure

1. Create `orthography2ipa/data/<code>.json`. Set `code`, `name`, `script` and an honest `quality`. Use `stub` when the spec is a stub ([quality tiers](quality_tiers.md)).

2. Declare `graphemes` or `phonemes`.

3. Keep `graphemes` to real orthographic units ([A grapheme key is an orthographic unit](contributing/spec_authoring.md#a-grapheme-key-is-an-orthographic-unit)).

4. Put each context in the rule layer, never in extra keys ([Express a context](contributing/spec_authoring.md#express-a-context)). The position keys are in [positional graphemes](positional_graphemes.md).

5. Cite every claim in `sources`, as [citation honesty](contributing/citations.md) describes.

6. Add `glottolog_code`, `wikidata_qid` and `iso639_3` where they exist. Make sure that each identifier resolves to this language. A null code is better than a wrong one.

7. Connect the ancestry with `parent` or `ancestors`. The ancestor roles and their typical weights are in [data model](data_model.md) and in [`SCHEMA.md`](../orthography2ipa/data/SCHEMA.md#ancestor-role-values).

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

The package layout and the loader functions (`load_json_spec`, `load_all_json_specs`, `available_json_codes`) are described in [architecture](architecture.md).

## Classification: wire it into the clade chain

A family is a clade node. A clade node is a spec whose JSON carries `"clade": true`, a `name` such as `"Ibero-Romance"`, and a `parent` that points at the next clade up. It holds classification only. It has no graphemes and no allophones, and no spec inherits data from it. `available_codes()` leaves clade nodes out unless you pass `include_clades=True`.

You classify a new language when you point its `parent` at the correct node. Then `family` and `family_path` derive themselves:

```python
import orthography2ipa

orthography2ipa.get("pt-BR").family_path   # ('Indo-European', 'Italic', 'Romance', 'Ibero-Romance')
orthography2ipa.get("pt-BR").family        # 'Indo-European > Italic > Romance > Ibero-Romance'
```

If the clade of the language has no node, add the node. Do not write a `family` string to go around the missing node. An explicit `family` string is correct only for a grouping that is not a genetic clade: creoles, constructed languages, isolates and unclassified languages. The full contract is in [`SCHEMA.md`](../orthography2ipa/data/SCHEMA.md#clade-nodes-and-the-derived-family).

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

The loader resolves the base spec first, then puts the dialect's own entries on top. Each `*_base` field can name a different base. A base can inherit from a base of its own, and the loader resolves the whole chain. When a spec states no `positional_graphemes_base`, its positional entries follow `graphemes_base`. The `allophones` layer follows only an explicit `allophones_base`.

The merge is one level deep, so a dialect that states one context for a letter replaces every context that the base gives that letter. Set a key to `null` to delete an inherited entry. Do not make a cycle of `*_base` references. The loader does not detect a cycle and fails with a `RecursionError`. The worked example, `es-ES-x-andalusia-w`, is in [`SCHEMA.md`](../orthography2ipa/data/SCHEMA.md#inheritance).

## Metadata worth filling in

A spec also records what the language is:

| Field | What it gives |
|---|---|
| `sources` | The citations, which trace every mapping of a `research` spec to a published description |
| `orthography_standard` | The official spelling norm, where one exists, and the primary authority for what a grapheme is |
| `location` | A representative point (latitude and longitude) that feeds `geographic_distance` |
| `timespan` | The attestation period, across which ancestry weights decay |
| `glottolog_code`, `wikidata_qid`, `phoible_id`, `wals_code`, `iso639_3` | Cross-references, of which `wikidata_qid` resolves the others |
| `wikipedia`, `urls` | References for a human reader |

## Looking for a source: what a phone inventory cannot tell you

A grapheme table maps a letter to the phones that it can take. A phone inventory lists the phones that a variety has. These are different facts, and the second never settles the first. A variety with both /q/ and /ɡ/ in its inventory still leaves ⟨ق⟩ undecided, and that reflex is the fact a spec records.

The sources that are easiest to reach are inventories. PHOIBLE is the obvious place to look, and the `phoible_id` field points to it. It covers Arabic only at the level of the macrolanguage and the standard variety. A search of the full database by ISO code returns zero segments for `ayh`, `acq`, `abv`, `ssh`, `aao`, `adf`, `aec`, `avl`, `ayp`, `bbz` and `sqr`. Where PHOIBLE has an inventory, it gives phones and no letter mappings.

A sound-definition list in a phonetic description has the same limit. Dawod's 1952 thesis on the Aden dialect lists "voiced velar plosive" and "voiceless uvular plosive" in readable English, so Aden has both. Its one table that maps letters to those sounds has a symbol column that is not legible on the scan. The inventory is legible, and the reflexes cannot be recovered.

So when a source is hard to get, first ask whether it answers the question. A spec needs a statement such as "⟨ق⟩ is realised as X in this variety", with a page number. Some evidence shows only that a phone or a letter occurs. Examples are an inventory, a phoneme count, a section on velar stops in a table of contents, and a corpus frequency count. None of them licenses a reading.

If no such statement is available, write a `stub` that says so and names where the description would be. Do not fill a `research` spec from the nearest inventory.

## Suffix morphology (`grammatical_endings`, optional)

Some endings take their sound from the grammatical ending and not from the letters that spell it. Examples are French mute ⟨-er⟩ and ⟨-ez⟩, and English ⟨-tion⟩ [ʃən]. Declare such an ending in `grammatical_endings`, never as a grapheme key, because a morpheme chunk is a forbidden key ([spec authoring rules](contributing/spec_authoring.md#a-grapheme-key-is-an-orthographic-unit)). The engine matches the ending only at the effective end of the word, so it does not touch letters inside the word. An entry in `word_exceptions` still wins over it. The contract is in [`SCHEMA.md`](../orthography2ipa/data/SCHEMA.md#grammatical-endings).

An ending can have more than one correct reading that the spelling does not choose between. French verbal ⟨-ent⟩ is mute, and nominal ⟨-ent⟩ is [ɑ̃]. Do not pick one, and do not write a word list. Declare an ordered candidate list, such as `"ent": [null, ""]`, so that both readings reach the lattice and a rescorer downstream can choose ([ambiguous endings](../orthography2ipa/data/SCHEMA.md#ambiguous-endings)). The review rules for such a list are in [Ambiguous grammatical endings](contributing/spec_authoring.md#ambiguous-grammatical-endings).

## Supply a lexicon (optional)

A deep orthography can need a word list on top of the rules. The caller registers that list at run time, and the package never bundles one. See [lexicon](lexicon.md).

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
| `tests/test_grammatical_endings.py` | Every list-valued ending is documented in `notes`, under a cap per spec |

---
[← Ancestry System](ancestry.md) · [Home](index.md) · [Allophony →](allophony.md)
