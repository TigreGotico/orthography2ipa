# Language JSON Schema

Each `.json` file in this directory defines one or more `LanguageSpec` entries.
Files are named `{code}.json` where `code` is the primary BCP-47 language code.

## Schema

```json
{
  "code": "es-ES",
  "name": "Spanish (Castilian)",
  "script": "Latin",
  "graphemes_base": null,
  "graphemes": {
    "a": [
      "a"
    ],
    "ch": [
      "tʃ"
    ],
    "th": {
      "ipa": ["θ", "ð"],
      "weights": [0.7, 0.3]
    }
  },
  "allophones_base": null,
  "allophones": {
    "b": [
      "b",
      "β"
    ]
  },
  "positional_graphemes_base": null,
  "positional_graphemes": {
    "b": {
      "intervocalic": [
        "β"
      ]
    }
  },
  "parent": "la-x-hispania",
  "ancestors": [
    {
      "code": "la-x-hispania",
      "role": "parent",
      "weight": 0.80,
      "notes": "Primary descent from Hispanic Vulgar Latin"
    }
  ],
  "notes": "Peninsular Castilian with distinción."
}
```

## Fields

| Field                       | Type   | Required | Description                                  |
|-----------------------------|--------|----------|----------------------------------------------|
| `code`                      | string | yes      | BCP-47 or ISO 639 language code              |
| `name`                      | string | yes      | Human-readable language name                 |
| `script`                    | string | yes      | Primary writing script                       |
| `family`                    | string | no       | **Do not author this.** `family` is DERIVED from the clade nodes on the ancestry chain (see [Clade nodes](#clade-nodes-and-the-derived-family)). It stays accepted as an override only for groupings that are not genetic clades — creoles, constructed languages, isolates, unclassified languages. |
| `clade`                     | bool   | no       | This spec is a classification-only node — a family, not a language (default: `false`). See [Clade nodes](#clade-nodes-and-the-derived-family). |
| `graphemes`                 | object | see note | Grapheme → IPA mapping. Each value is either a plain IPA list `[str]` **or** a weighted object `{"ipa": [str], "weights": [float]}` (candidate frequencies). Both normalise to the same internal shape; absent weights == rank ordering. See [candidate scoring](../../docs/candidate_scoring.md). |
| `allophones`                | object | see note | Phoneme → allophone mapping (`{str: [str]}`). Derived as an identity map from `graphemes` when absent. |
| `phonemes`                  | array  | see note | The phoneme inventory, stated directly and independently of `graphemes` (`["p", "t", "k", ...]`). **A spec must declare `graphemes` or `phonemes`; it may not be silent about both.** See [The inventory](#phonemes--the-inventory-stated-directly). |
| `orthography_kind`          | string | no       | What kind of writing the graphemes are: `"native"` (default), `"romanization"`, `"transliteration"`. See [Orthography kind](#orthography-kind). |
| `positional_graphemes`      | object | no       | Position-dependent grapheme mappings         |
| `parent`                    | string | no       | Primary parent language code                 |
| `ancestors`                 | array  | no       | Full ancestry specification                  |
| `notes`                     | string | no       | Free-form notes and sources                  |
| `graphemes_base`            | string | no       | Code to inherit graphemes from               |
| `allophones_base`           | string | no       | Code to inherit allophones from              |
| `positional_graphemes_base` | string | no       | Code to inherit positional graphemes from    |
| `word_exceptions_base`      | string | no       | Code to inherit whole-word overrides from    |
| `grammatical_endings_base`  | string | no       | Code to inherit grammatical endings from     |
| `quality`                   | string | no       | Data maturity: `"stub"`, `"skeleton"`, `"research"`, `"production"` (default: `"research"`) |
| `script_type`               | string | no       | Script typology: `"alphabet"`, `"abjad"`, `"abugida"`, `"syllabary"`, `"logographic"`, `"featural"`, `"mixed"`, `"reconstruction"` (default: `"alphabet"`) |
| `inherent_vowel`            | string | no       | For abugidas: vowel assumed when no vowel mark (e.g. `"ə"`) |
| `vowel_graphemes`           | array  | no       | Whole grapheme strings this spec declares vowel letters, overriding the closed Latin/Greek/harakat inventory (e.g. `["w"]` for Hmong RPA ⟨w⟩ = /ɨ/). Empty (default) keeps the closed-inventory answer. See [data_model.md](../../docs/data_model.md#vowel_graphemes-overriding-a-closed-inventory-consonant-letter). |
| `trailing_vowel_axis_digraphs` | array | no    | Multi-letter vowel graphemes (matched case-insensitively) for which the AFTER_FRONT_VOWEL/AFTER_BACK_VOWEL axis for a FOLLOWING grapheme is read off the digraph's trailing letter rather than its opening one, e.g. `["ía", "úa"]` for Old Irish, where quality under *caol le caol* is set by the digraph's closing letter. Empty (default) keeps the opening-letter (`grapheme[0]`) reading every other spec uses. |
| `iso639_3`                  | string | no       | ISO 639-3 three-letter code for cross-referencing |
| `sandhi_rules`              | array  | no       | Cross-word-boundary phonological rules       |
| `stress`                    | object | no       | Declarative stress placement (see [Stress Schema](#stress-schema)) |
| `word_exceptions`           | object | no       | Whole-word overrides for a closed irregular set (`{"one": "wʌn"}`); beats rules, beats a bundled lexicon |
| `grammatical_endings`       | object | no       | Suffix morphology: orthographic ending → IPA at the effective word end (`{"tion": "ʃən"}`), or an ordered candidate list for an ending that is genuinely ambiguous (`{"ent": [null, ""]}`); see [Grammatical endings](#grammatical-endings) |
| `allophone_rules`          | array  | no       | Post-lexical `phoneme → surface` rewrites (see [Allophone Rule Schema](#allophone-rule-schema) and [allophony](../../docs/allophony.md)) |
| `tone_inventory`            | object | no       | IPA tone mark → label (e.g. `{"˥": "high"}`) |
| `tone_marks_syllable_final` | bool   | no       | Dock every tone mark at the end of its syllable. Set it when the orthography writes tone on the nucleus letter, so that ⟨ōng⟩ comes out `oŋ³³` and not `o³³ŋ` |
| `sources`                   | array  | no       | Bibliographic references (see Sources Schema below) |
| `glottolog_code`            | string | no       | Glottolog languoid code (e.g. `"cast1244"`) — genealogical classification |
| `wikidata_qid`              | string | no       | Wikidata item id (e.g. `"Q1321"`) — the linked-data hub; one QID resolves this language's Glottolog, ISO 639-3, PHOIBLE, WALS and Wikipedia articles in every edition |
| `phoible_id`                | string | no       | PHOIBLE identifier — attested phoneme inventories, the reference a spec's emitted phoneme set can be validated against |
| `wals_code`                 | string | no       | WALS (World Atlas of Language Structures) code — typological cross-reference |
| `wikipedia`                 | array  | no       | Wikipedia article URLs (`https://<lang>.wikipedia.org/wiki/…`) |
| `urls`                      | array  | no       | Other reference URLs (Glottolog, Ethnologue, dialect articles, …) |
| `orthography_standard`      | object | no       | The official published spelling norm, when the language has one (see [Orthography Standard Schema](#orthography-standard-schema)) |
| `location`                  | object | no       | Representative point for where the variety is spoken (see [Location Schema](#location-schema)) |
| `timespan`                  | object | no       | Attestation period `{"start_year": int, "end_year": int\|null}` |
| *(lexicon)*                 | —      | —        | **Not a spec field, and never bundled.** A word lexicon is a corpus, not a description of a language. Supply one at runtime from a local file, a URL or a Hugging Face id: `orthography2ipa.register_lexicon("en-GB", "hf://TigreGotico/en-lexicon/en-GB.tsv")`, or point at a directory of `{code}.tsv` with `set_lexicon_dir()` / `$ORTHOGRAPHY2IPA_LEXICON_DIR`. |

## Clade Nodes and the Derived `family`

A language family is a **clade node**: a spec file whose JSON sets
`"clade": true` and carries classification and nothing else — a `name`, a
`parent` pointing at the next clade up, and (optionally) sources, identifiers and
a centroid `location`. It has no graphemes and no allophones, is never inherited
from, is never a data source, and is excluded from `available_codes()` unless
`include_clades=True` is passed.

```json
{
  "code": "x-clade-iberrom",
  "name": "Ibero-Romance",
  "clade": true,
  "script": "Zyyy",
  "quality": "stub",
  "graphemes": {},
  "allophones": {},
  "parent": "la-x-hispania",
  "notes": "Classification-only clade node for the Ibero-Romance branch."
}
```

Clade files are named `x-clade-{slug}.json`, use `Zyyy` (undetermined) as their
script, and sit at `quality: "stub"` with empty maps. A clade's `parent` is
whatever comes next up the chain — another clade, or the ancestral language the
branch descends from (`la-x-hispania` here).

The loader derives each spec's `family_path` by walking `parent` upwards and
collecting the clade names it passes, broadest first; `family` is that path joined
with `" > "`:

```python
get("pt-BR").family_path   # ('Indo-European', 'Italic', 'Romance', 'Ibero-Romance')
get("pt-BR").family        # 'Indo-European > Italic > Romance > Ibero-Romance'
```

So a language is classified by pointing its `parent` at the right node — never by
authoring a `family` string. If the clade does not exist yet, add the node. The
CLI filter matches any single step of the path, so `--family Romance` and
`--family Ibero-Romance` both return `pt-BR`.

## `phonemes` — the inventory, stated directly

A language's sounds are not a property of its writing system. Most of the world's
languages are unwritten or barely written (PHOIBLE catalogues inventories for
thousands of them), and a logographic script encodes no sound at all — so reading
the inventory out of the spelling cannot work for either.

```json
{
  "code": "zh-Hani",
  "name": "Chinese (Han script)",
  "script": "Han",
  "script_type": "logographic",
  "orthography_kind": "native",
  "graphemes": {},
  "allophones": {},
  "phonemes": ["p", "pʰ", "m", "f", "t", "tʰ", "n", "l", "..."]
}
```

When `phonemes` is absent the inventory is DERIVED from `graphemes` — every phoneme
any grapheme can produce — so a spec that declares nothing keeps the inventory it
always had. That derivation is a **fallback, not the definition**: it reads the
sounds out of the spelling, which is backwards, and it is why a reconstructed
language (Proto-Indo-European) once had to fake an identity orthography, `p` → [p],
merely to have an inventory at all. A reconstruction now declares its 30 phonemes.

**Integrity invariant:** a spec must declare `graphemes` **or** `phonemes`. It may
not be silent about both. "Every language has graphemes" is false — logographic
scripts and unwritten languages are the counterexamples — but a spec that has
neither sounds nor spelling describes nothing.

## Orthography kind

`orthography_kind` says what kind of writing a spec's `graphemes` encode, because
Han characters, Pinyin and Buckwalter ASCII are three different claims:

| Value | Meaning | Standards body |
|---|---|---|
| `native` (default) | The language's own writing system | Usually |
| `romanization` | An alternative orthography people READ AND WRITE — Pinyin (ISO 7098), Jyutping, Hepburn. A real orthography *of* the language, usually a plain alphabet, which is why it can be rule-transcribed when the native script cannot. | Yes |
| `transliteration` | A lossless machine re-encoding of ANOTHER script — Buckwalter, ITRANS, Harvard-Kyoto. Nobody reads it as a language, and it inherits every limit of the script it re-encodes. | No — that absence is the tell |

So `zh` is a **romanization** (it reads Pinyin, not Hanzi), `zh-Hani` is the
**native** spec with an empty grapheme map and a declared phonology, and
`ar-Latn-buckwalter` is a **transliteration**. See
[orthography kind](../../docs/orthography_kind.md).

## Inheritance

The `*_base` fields support data inheritance. When set, the loader:

1. Loads the referenced spec's data for that field
2. Deep-merges the current file's data on top (overrides only)

```json
{
  "code": "es-ES-x-andalusia-w",
  "graphemes_base": "es-ES",
  "graphemes": {
    "c": [
      "k",
      "s",
      "θ"
    ],
    "z": [
      "s",
      "θ"
    ],
    "s": [
      "s",
      "h"
    ],
    "ll": [
      "ʝ"
    ]
  }
}
```

The loader resolves `es-ES` first, copies its graphemes, then overlays
the four overridden entries.

> To mark a deletion, when a grapheme is no longer valid or an allophone no longer present, it can be set to None
> explicitly to avoid inheritance

## Sandhi Rule Schema

```json
{
  "sandhi_rules": [
    {
      "id": "FR_LIAISON_Z",
      "name": "z-liaison",
      "left_context": "z$",
      "right_context": "^[aeiouɛɔɑãɛ̃ɔ̃]",
      "transform": "z‿",
      "obligatory": true,
      "notes": "les amis → /lez‿ami/"
    }
  ]
}
```

| Sandhi Field   | Type   | Required | Description                          |
|----------------|--------|----------|--------------------------------------|
| `id`           | string | yes      | Unique rule identifier               |
| `name`         | string | yes      | Human-readable name                  |
| `left_context` | string | yes      | Regex on word-final IPA              |
| `right_context`| string | yes      | Regex on next-word-initial IPA       |
| `transform`    | string | yes      | Replacement pattern                  |
| `obligatory`   | bool   | no       | Whether rule is obligatory (default: true) |
| `notes`        | string | no       | Optional notes                       |

A sandhi rule applies only within its prosodic domain (Nespor & Vogel 1986,
*Prosodic Phonology*). Punctuation that writes a pause — a comma, a full stop,
and their equivalents in every script — closes the intonational phrase (IP),
and no rule of any language reaches across that break.

The engine blocks at IP boundaries only, and there is no field for it: it is a
property of the rule type, not a per-rule choice. This is a LOWER BOUND, not
the full story. Most cross-word rules take the smaller phonological phrase (φ)
as their domain, and φ boundaries also fall clause-internally where no
punctuation is written, so IP-only blocking UNDER-restricts. A per-rule
prosodic domain (`"domain": "phi"` blocking φ-internally too) is a possible
future refinement; it needs a φ-parser the engine does not have and evidence
per rule, so it is deliberately not added here.

## Allophone Rule Schema

`allophone_rules` is the POST-lexical half of the "two maps": an ordered
list of declarative, context-conditioned `phoneme → surface` rewrites (the
mirror of `positional_graphemes`, on the phoneme side). They compile into a
lattice rescorer the engine applies after phoneme selection and before
stress/sandhi. Empty by default → no-op: the rules alone decide the output. See
[allophony](../../docs/allophony.md).

```json
{
  "allophone_rules": [
    {
      "id": "CA_DEVOICE_D",
      "phonemes": ["d"],
      "surface": "t",
      "word_final": true,
      "notes": "Final-obstruent devoicing: word-final /d/ → [t]."
    },
    {
      "id": "CA_NASAL_VELAR",
      "phonemes": ["n"],
      "surface": "ŋ",
      "followed_by_phoneme": ["k", "ɡ"],
      "notes": "Nasal place assimilation: /n/ → [ŋ] before a velar."
    }
  ]
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Unique rule identifier (id-keyed inheritance overlay, like `sandhi_rules`) |
| `phonemes` | string \| array | yes | Target underlying phoneme(s); a bare string is accepted |
| `surface` | string | yes, unless `append` | Surface realisation the matched phoneme is rewritten to |
| `append` | string | no | IPA inserted AFTER the matched phoneme, which is otherwise left alone, so one rule states an insertion for a whole class of targets — what epenthesis needs, since a fixed `surface` can only name one target's output. Mutually exclusive with `surface`. See [allophony](../../docs/allophony.md#inserting-instead-of-rewriting-append) and the Egyptian (`egy`) reading convention |
| `word_initial` | bool | no | Require (or, if `false`, forbid) word-initial position |
| `word_final` | bool | no | Require (or forbid) word-final position |
| `stress` | string | no | `"stressed"` / `"unstressed"` — engine path only (needs stress context) |
| `syllable_position` | string | no | `"onset"` / `"coda"` / `"nucleus"` (maximal-onset heuristic) |
| `preceded_by` | string | no | Previous-grapheme class: `vowel`, `consonant`, `consonant_cluster`, `coda`, `coda_nasal`, `front_vowel`, `back_vowel`, `palatal`, `emphatic`, `word_boundary`. `consonant_cluster` = the neighbour begins two or more consonant segments counting away from this grapheme (a geminate, a multi-consonant grapheme such as ⟨x⟩ /ks/, or a consonant whose own neighbour is a consonant) — the context closed-syllable shortening and complementary quantity need. `coda` = the neighbour is in coda position; `coda_nasal` = a coda nasal — what a vowel nasalises before (⟨bon⟩ [bɔ̃] vs ⟨bonne⟩ [bɔn]). `emphatic` = a pharyngealized ("emphatic") consonant, decided by the neighbour's IPA carrying the `ˤ` diacritic (`orthography2ipa.vowels.is_pharyngealized_consonant`) — a generic feature class (not Arabic-specific) that backs emphasis-spread/tafkhim vowel backing (Watson 2002; Davis 1995). **Never enumerate clusters or nasal vowels as grapheme keys** (⟨an⟩ is not a digraph); see [allophony](../../docs/allophony.md#consonant_cluster) |
| `followed_by` | string | no | Next-grapheme class (same value set) |
| `preceded_by_phoneme` | array | no | Previous slot's chosen phoneme must be one of these |
| `followed_by_phoneme` | array | no | Next slot's chosen phoneme must be one of these |
| `followed_by_grapheme` | array | no | Next slot's source grapheme must be one of these (case-insensitive). For processes a letter group triggers while its phoneme hides the cluster (Swedish short vowel before ⟨ng⟩ ⟨nk⟩ ⟨sk⟩) |
| `followed_by_grapheme_not` | array | no | Next slot's source grapheme must NOT be one of these. For shortness-marking letter groups whose phonemes look like plain single consonants (German ⟨ss⟩ ⟨ck⟩ ⟨tz⟩ ⟨ng⟩) |
| `word_contains_grapheme` | array | no | At least one of these letters occurs ANYWHERE in the source word (case-insensitive). Word scope, not neighbour scope: some orthographies mark a property of the whole word on a single consonant letter standing any distance from the segment it conditions. Ottoman Turkish (`ota`) is the motivating case — the abjad leaves most vowels unwritten and signals which member of a vowel-harmony pair is meant by whether the word is spelt with a hard letter ⟨ح خ ص ض ط ظ ع غ ق⟩ or a soft one ⟨ت س ك گ ه⟩. The check is a raw substring test over the joined source word, so a multi-character grapheme key matches wherever that sequence occurs as a substring, not by slot-grapheme membership |
| `word_contains_grapheme_not` | array | no | None of these letters occurs anywhere in the source word. The negative twin of `word_contains_grapheme`, so an unmarked-harmony default can be stated as "no hard letter anywhere" instead of enumerated |
| `requires_other_nucleus` | bool | no | Require (or, if `false`, forbid) that some OTHER slot in the word carries a syllable nucleus. A vowel-deleting rule (`surface: ""`) must not empty the word of its only nucleus — every prosodic word contains at least one syllable (Hayes 2009; Blevins 1995). Romanian's asyllabic word-final ⟨i⟩ is the motivating case: ⟨lupi⟩ is [lupʲ], but the monosyllables ⟨și⟩ [ʃi], ⟨fi⟩ [fi], ⟨zi⟩ [zi] keep a full vowel (Chitoran 2002) |
| `followed_by_nucleus` | bool | no | Require (or, if `false`, forbid) that a syllable nucleus occurs LATER in the word than this slot — the final-syllable predicate. `false` selects the last nucleus of the word, `true` every earlier one. Unlike `requires_other_nucleus`, which is direction-blind, this one carries the direction that non-final reduction and final-syllable strengthening both need |
| `mutates_neighbor` | string | no | An IPA modifier (e.g. `"ʲ"`) this rule ADDS to an adjacent slot's candidate when it fires — paired with `surface: ""` this is the "marker grapheme" pattern: a letter that deletes itself while palatalising (or otherwise mutating) a neighbour, atomically. Requires `mutates_neighbor_side`. See [allophony](../../docs/allophony.md#marker-graphemes-delete-a-vowel-while-mutating-a-neighbour) and the Manx (`gv`) slender-marking rules. |
| `mutates_neighbor_side` | string | no | `"preceding"` / `"following"` — which adjacent slot, relative to THIS rule's own anchor grapheme, receives `mutates_neighbor`'s feature. Required together with `mutates_neighbor`. |
| `notes` | string | no | Provenance / convention notes |

All declared conditions are ANDed; an unset condition is "don't care". A rule
fires for a slot when the slot's chosen phoneme is in `phonemes` **and** every
condition holds, rewriting that candidate to `surface` at the same beam cost.
Inheritance is id-keyed overlay: a child spec setting `graphemes_base`
inherits the parent's rules and can override one by `id` or append new ones.

## Stress Schema

Declarative stress placement. The engine applies it after phoneme selection; a
spec with no `stress` block gets no stress marks.

```json
"stress": {
  "default_position": -2,
  "final_stress_endings": ["r", "l", "z"],
  "marked_vowels": ["á", "é", "í", "ó", "ú"],
  "stress_mark": "ˈ",
  "notes": "Paroxytone by default; oxytone before the listed final consonants."
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `default_position` | int | no | Default stressed syllable. Negative counts from the end (`-1` oxytone, `-2` paroxytone — the default, down to `-4`); positive counts from the start (`1` first syllable, `2` second). `0` is invalid. |
| `final_stress_endings` | array | no | Word endings that force final stress |
| `penult_stress_endings` | array | no | Word endings that force penultimate stress |
| `antepenult_stress_endings` | array | no | Word endings that force antepenultimate stress (the end-anchored twin of `penult_stress_endings`, for two-syllable pre-stressed suffixes such as English `-ity`, `-ography`) |
| `marked_vowels` | array | no | Orthographic vowels whose diacritic marks stress directly |
| `stress_mark` | string | no | IPA mark to insert (default `"ˈ"`) |
| `vowel_letters` | array | no | The letters this orthography uses as syllable NUCLEI, for the bundled syllabifier. Left undeclared, the splitter uses a cross-linguistic test that reads a letter's shape, and that test counts ⟨y⟩ and ⟨w⟩ as vowels because some orthographies use them so. Where a language does not — Xhosa ⟨y⟩ is /j/ and ⟨w⟩ is /w/, both onsets — the run ⟨oya⟩ collapses into one nucleus, the syllable count drops, and every position the count feeds (stress, and the `nucleus_stressed` entries hanging off it) lands on the wrong vowel or on two at once. Declaring the set states the language's own answer: the listed letters are nuclei, no other letter is. Inert for any spec that does not declare it |
| `accent2_mark` | string | no | Scandinavian pitch-accent 2 marker (e.g. `"²"`). When set, a penult-stressed word ending in one of `accent2_final_letters` takes this mark instead of `stress_mark` (Riad 2014); empty = no pitch accent |
| `accent2_final_letters` | array | no | Final orthographic letters selecting `accent2_mark` (e.g. `["a", "e"]`) |
| `secondary_stress` | string | no | Second prominence level below the main word accent. `""` (default) = the binary system, nothing changes. `"alternating"` = binary feet built leftward from the main stress, so every second syllable before it is a foot head (Liberman & Prince 1977; Hayes 1995 ch. 3): English ˌcombiˈnation, reˌsponsiˈbility. A foot head is NOT unstressed — it takes the `nucleus_secondary` position instead of `nucleus_unstressed`, so the spec's reduction entries no longer reach it, and `ˌ` is written before it |
| `notes` | string | no | Provenance / convention notes |

## Location Schema

Where the variety is spoken — a single representative point, consumed by
`geographic_distance`.

```json
"location": {
  "latitude": 41.453,
  "longitude": 1.569,
  "source": "glottolog",
  "notes": "Glottolog's representative point for Catalan."
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `latitude` | float | **yes** | −90.0 … 90.0 |
| `longitude` | float | **yes** | −180.0 … 180.0 |
| `source` | string | no | Where the point comes from (`glottolog`, `wikidata`, …) |
| `notes` | string | no | Why this point, and what it does *not* claim |

A point is a crude proxy for an AREA. It is a fair summary for a dialect anchored
to a region — which is where the geographic axis earns its keep — and close to
meaningless for a widespread macrolanguage, where the point is arbitrary. Prefer
a point that describes *this* variety (the centre of the norm, the heart of the
dialect region) over a generic national point, and say so in `notes`. Omit the
field entirely rather than guess: `geographic_distance` returns `None` for a spec
without a location, which is honest, whereas a made-up point is not.

## Sources Schema

The `sources` array contains bibliographic references for the phonological data in the spec.

```json
{
  "sources": [
    {
      "id": "wells1982_vol2",
      "author": "Wells, J.C.",
      "year": 1982,
      "title": "Accents of English, Vol. 2: The British Isles",
      "publisher": "Cambridge University Press",
      "url": null,
      "pages": null,
      "notes": null
    }
  ]
}
```

| Source Field  | Type    | Required | Description                                         |
|---------------|---------|----------|-----------------------------------------------------|
| `id`          | string  | yes      | Short cite key (e.g. `"wells1982"`)                 |
| `author`      | string  | yes      | Author(s), e.g. `"Wells, J.C."`                     |
| `year`        | integer | yes      | Publication year                                    |
| `title`       | string  | yes      | Full title of the work                              |
| `publisher`   | string  | no       | Publisher name                                      |
| `url`         | string  | no       | URL or DOI; use `null` for print-only works         |
| `wikipedia_url` | string | no       | Wikipedia article URL for quick human reference     |
| `pages`       | string  | no       | Specific page range, e.g. `"pp. 45-72"`            |
| `notes`       | string  | no       | Annotation about what this source supports          |

## Positional Grapheme Keys

Position keys in `positional_graphemes` use lowercase string values
matching the `GraphemePosition` enum:

| JSON key                    | Enum value                                 |
|-----------------------------|--------------------------------------------|
| `"default"`                 | `GraphemePosition.DEFAULT`                 |
| `"nucleus"`                 | `GraphemePosition.NUCLEUS`                 |
| `"pretonic"`                | `GraphemePosition.PRETONIC`                |
| `"posttonic"`               | `GraphemePosition.POSTTONIC`               |
| `"onset"`                   | `GraphemePosition.ONSET`                   |
| `"nucleus_stressed"`        | `GraphemePosition.NUCLEUS_STRESSED`        |
| `"nucleus_unstressed"`      | `GraphemePosition.NUCLEUS_UNSTRESSED`      |
| `"nucleus_secondary"`       | `GraphemePosition.NUCLEUS_SECONDARY`       |
| `"coda"`                    | `GraphemePosition.CODA`                    |
| `"word_initial"`            | `GraphemePosition.WORD_INITIAL`            |
| `"word_final"`              | `GraphemePosition.WORD_FINAL`              |
| `"intervocalic"`            | `GraphemePosition.INTERVOCALIC`            |
| `"intervocalic_cross_word"` | `GraphemePosition.INTERVOCALIC_CROSS_WORD` |
| `"before_vowel"`            | `GraphemePosition.BEFORE_VOWEL`            |
| `"after_vowel"`             | `GraphemePosition.AFTER_VOWEL`             |
| `"before_consonant"`        | `GraphemePosition.BEFORE_CONSONANT`        |
| `"after_consonant"`         | `GraphemePosition.AFTER_CONSONANT`         |
| `"before_a"`                | `GraphemePosition.BEFORE_A`                |
| `"before_e"`                | `GraphemePosition.BEFORE_E`                |
| `"before_i"`                | `GraphemePosition.BEFORE_I`                |
| `"before_o"`                | `GraphemePosition.BEFORE_O`                |
| `"before_u"`                | `GraphemePosition.BEFORE_U`                |
| `"before_front_vowel"`      | `GraphemePosition.BEFORE_FRONT_VOWEL`      |
| `"before_back_vowel"`       | `GraphemePosition.BEFORE_BACK_VOWEL`       |
| `"after_front_vowel"`       | `GraphemePosition.AFTER_FRONT_VOWEL`       |
| `"after_back_vowel"`        | `GraphemePosition.AFTER_BACK_VOWEL`        |
| `"before_palatal"`          | `GraphemePosition.BEFORE_PALATAL`          |
| `"after_palatal"`           | `GraphemePosition.AFTER_PALATAL`           |
| `"consonantal"`             | `GraphemePosition.CONSONANTAL`             |
| `"vocalic"`                 | `GraphemePosition.VOCALIC`                 |

The `*_front_vowel` / `*_back_vowel` positions condition on the whole vowel
**class** of the neighbouring grapheme rather than a single letter — e.g. one
`"before_front_vowel"` entry replaces `"before_e"` + `"before_i"` plus every
accented ⟨e⟩/⟨i⟩ variant (Romance c/g softening). Membership is owned by
`orthography2ipa.vowels.is_front_vowel` / `is_back_vowel`, which classify a
letter by NFD-decomposing it to its base and reading the base — `e i y` are
front, `a o u` are back — whenever every diacritic preserves the front/back
axis (acute, grave, circumflex, caron, macron, breve, ogonek, dot, tilde), so
`é ě ī į ý` are front and `á â ã ā ą` are back without hand-listing. Diaeresis
changes the axis, so `ä ö ü ë ï ÿ` are front by explicit rule, as are dotless
`ı` and non-decomposing `ø œ æ`; ring `å` straddles the axis and is in neither
class. Resolution order is **exact-letter position > vowel-class
position > default `graphemes` mapping**: an exact `"before_e"` entry declared
for the same grapheme wins over `"before_front_vowel"`, and the class positions
are inert (change nothing) for any spec that does not declare them.

The `"before_palatal"` / `"after_palatal"` positions are the consonant-side
mirror: they condition on the neighbouring grapheme being a **palatal /
palato-alveolar consonant** (`ʎ ɲ ʃ ʒ j c ɟ ç ʝ ɕ ʑ` and the affricates
`tʃ dʒ tɕ dʑ`, tie-bar `t͡ʃ` too). Membership is owned by
`orthography2ipa.vowels.is_palatal_consonant`, which reads the **IPA the
neighbour maps to** (its `ipa[0]`), not its spelling — so one `"before_palatal"`
entry covers every digraph producing a palatal (⟨lh⟩→ʎ, ⟨nh⟩→ɲ, ⟨ch⟩→ʃ, ⟨x⟩,
⟨j⟩), e.g. European-Portuguese stressed ⟨e⟩ → [ɐ] before ⟨lh⟩. They sit at the
class tier (below exact-letter positions, so `"before_i"` wins over
`"before_palatal"` when the neighbour ⟨i⟩ realises the palatal glide /j/) and are
likewise inert for any spec that does not declare them.

`"after_vowel"` reads the neighbour's **nucleus**, not its spelling, so in an
abugida it also matches after a consonant LETTER whose inherent vowel still
stands: Tibetan ⟨ལག⟩ is [lak], where ⟨ག⟩ closes the syllable ⟨ལ⟩ opened
rather than opening one of its own, and no vowel letter is written between
them. Only a spec that declares `inherent_vowel` matches this way, and a
letter whose inherent vowel was suppressed — one inside a subjoined stack, or
one the spec silences with `"before_consonant": [""]` — does not carry a
nucleus and does not trigger it. Such a neighbour is a consonant letter as
well, so `"after_consonant"` is still offered for the same slot, one tier
below `"after_vowel"`.

Declaring `"after_vowel"` for a grapheme is also what tells the engine the
letter can **close** a syllable. `coda_no_inherent_vowel` uses that
declaration to bound its search for the syllable's nucleus: it looks back
past letters the spec describes post-vocalically — which for Tibetan is the
suffix set ⟨ག ང ད ན བ མ འ ར ལ ས⟩, so the post-suffix ⟨ས⟩ of ⟨ཁམས⟩ finds the
nucleus two letters behind it — and stops at any other letter. A spec that
declares no post-vocalic reading at all (Thai, Lao) keeps the one-token
behaviour, which is what stops the search from deleting the unwritten vowel
of a following syllable's onset.

## Grammatical endings

`grammatical_endings` maps an orthographic **word ending** to the IPA it
realises, for cases where the realisation belongs to the grammatical ending
rather than to the letter sequence that spells it — suffix morphology.

```json
"grammatical_endings": {
  "er": "e",
  "ez": "e"
}
```

Three phenomena it exists for:

- **French mute ⟨-er⟩ / ⟨-ez⟩.** The infinitive and agent-noun ⟨-er⟩ is [e]
  (`parler`, `boulanger`, `boulangers`) and the 2pl ⟨-ez⟩ is [e] (`mangez`,
  and the frozen `nez`, `chez`, `assez`): final-consonant elision in the
  grammatical ending (Fouché 1959, *Traité de prononciation française*;
  Tranel 1987 §3).
- **English suffix palatalization.** ⟨-tion⟩ → /ʃən/, ⟨-cious⟩ → /ʃəs/,
  ⟨-tial⟩ → /ʃəl/: palatalization of the stem-final coronal before the `-ion`
  suffix (Chomsky & Halle 1968, *The Sound Pattern of English*; surface values
  per Wells 2008, *Longman Pronunciation Dictionary*).
- **A morphologically ambiguous ending, exposed for downstream rescoring.**
  See [Ambiguous endings](#ambiguous-endings) below.

**Every ending is a cited linguistic claim about a suffix's realisation, never
a PER-chasing pattern.** This applies to every key, single-valued and
list-valued alike, and it is the same prohibition that keeps n-grams out of
`graphemes`: an ending earns its place from a published source — a paper or a
reference grammar — that states how that suffix is realised. Corpus frequency
supports the *ordering* of a list value, but a frequency count on its own is
not a citation and never licenses a key. An ending added because it moved the
score, with the source found afterwards or not at all, is rejected.

Two mechanical gates enforce this (`tests/test_grammatical_endings.py`): every
declared ending must be named in its spec's `notes`, and that passage must
carry a citation traceable to the spec's `sources` array.

Rules of the match:

- **Effective word end only.** The ending must occupy the word's last grapheme
  tokens, or its last tokens before a *transparent grammatical suffix* the spec
  already silences word-finally (French plural ⟨-s⟩/⟨-x⟩) — the same question
  `effective_word_end` answers for positional graphemes. So `boulangers`
  matches, and the word-internal ⟨er⟩ of `personne`, `version` or `terre`
  never does.
- **Token-aligned.** The ending must start where a grapheme token starts. The
  word is tokenized exactly as it would be without the table, and only the
  emitted IPA of the trailing tokens is replaced — this is why a morpheme is
  **not** written as a grapheme key (forbidden, see `AGENTS.md`): a morpheme
  key would change how the word's interior is cut.
- **A head is required.** At least one token must precede the ending.
- **Longest match wins.** English ⟨-stion⟩ → /stʃən/ overrides the ⟨-tion⟩ it
  contains, so `question` keeps its /t/.

Precedence: `word_exceptions` **>** `grammatical_endings` **>**
`graphemes` / `positional_graphemes`. The closed set of French nouns that keep
/ɛʁ/ (`mer`, `hiver`, `super`, and their plurals) therefore stays in
`word_exceptions` and is unaffected.

Inheritance is `base_merge`, opt-in through `grammatical_endings_base`: a
dialect that shares its parent's graphemes shares its suffix morphology
(en-US palatalizes ⟨-tion⟩ exactly as en-GB does) and overrides per ending.

### Ambiguous endings

Some endings have more than one licit reading and orthography does not say
which. French verbal ⟨-ent⟩ is the reference case: the 3PL inflection is mute
(*ils parlent* [paʁl]) while the noun or adjective is [ɑ̃] (*vent*, *cent*,
*moment*). The two are separated by part of speech and by nothing spelled.

**o2i does not decide, and does not accept a POS tag as an input.** That
decision belongs to a downstream rescorer. What this layer owes is that the
reading it cannot choose still **exists in the lattice**, because a ranking
error is downstream-fixable and a missing candidate is not. Before this, [paʁl]
was in no French beam at any width.

An ambiguous ending is therefore declared as an **ordered candidate list** —
the same discipline `graphemes` and `positional_graphemes` already use:

```json
"grammatical_endings": {
  "ent": [null, ""]
}
```

- **Element 0 is rank 1.** A string there rewrites the matched tail exactly as
  the plain-string form does, so `["ʃən"]` is exactly `"ʃən"`.
- **`null` at element 0 means "defer".** Rank 1 stays whatever the grapheme
  tables already produced, and the entry contributes only the alternatives.
  French uses this shape because the nasal reading of ⟨-ent⟩ is already what
  nasal ⟨en⟩ + silent ⟨t⟩ yields — deferring keeps every 1-best *and* every
  existing candidate ordering byte-identical.
- **Elements 1..n are lower-ranked licit readings.** Each becomes an extra
  costed path, ranked by declaration order with the same rank cost an ordered
  grapheme list gets, so it reaches `word_candidates`, oracle@k and any
  rescorer plugin — and can never displace rank 1.
- **`null` is only valid at element 0.** As an alternative it would have to
  mean "this ending may also be silent", which is written `""`. An empty list
  is rejected.

`[null]` alone declares an ending that is *not* ambiguous: it rewrites nothing
and adds nothing, and its only effect is longest-match shielding — a way to keep
a longer, unambiguous ending off a shorter ambiguous one.

Ordering the list is a claim, and it should be made on what the consumer pays
for. French keeps the nasal reading at rank 1 even though gold *types* run
3873 mute to 287 nasal, because this library feeds TTS, where type counts do
not price a mispronounced *vent*. The consequence is deliberate: oracle@k
improves and 1-best does not move. That is the intended shape of the change,
not a disappointing result — and the oracle movement it causes is kept OUT of
the published scoreboard entirely, because that board defines `PER − Oracle@k`
as ranking error. See [benchmarks.md](../../docs/benchmarks.md#injected-alternatives-do-not-count-as-ranking-error).

#### Admissibility: a proven lattice hole, never a guess

**A list-valued ending is admissible only where the missing reading is a
demonstrated lattice hole, shown with gold evidence.** The bar is the
**0-in-top-k test**: take a sample of the gold types that carry the missing
reading, run `word_candidates` at a generous *k* and beam width, and show the
gold reading appears **0 times anywhere in the top k**. That is what separates
a *coverage* hole — which nothing downstream can repair, and which this
mechanism exists for — from a *ranking* error, which any downstream rescorer
already fixes without a spec change. French ⟨-ent⟩ cleared it at 0/300 in the
top 10.

Declaring a list because a reading "also exists", or "might help", or to raise
an oracle column, is **forbidden**. An unproven alternative costs beam width and
inflates our own diagnostic while fixing nothing (see
[benchmarks.md](../../docs/benchmarks.md#injected-alternatives-do-not-count-as-ranking-error)). If the reading is already
reachable at any *k*, the fix belongs in weights or in a downstream rescorer,
not here.

Record the evidence where the data lives: the sample size, the measured
0-in-top-k result, and the source of the gold, in the spec's `notes` beside the
ending.

#### Not a paradigm table

A list value states the **attested realisations of one spelled ending**, ordered
by frequency and cited. It is not a place to enumerate a paradigm.

**Adding ending keys shaped like a conjugation or declension table is
forbidden**, and it is forbidden by the same clause that forbids morpheme
chunks as grapheme keys (see `AGENTS.md`: morphology belongs to a downstream
consumer, and the package ships no word lists, stem lists or vocabularies).
Concretely, a key earns its place only if it is a *spelling* that a reader can
see at the end of a word and that has its own attested realisation. Enumerating
`ons`, `ez`, `ent`, `ais`, `ait`, `aient`, `èrent`, `assions`… because they are
the cells of a verb paradigm is a lexicon of morphology written in the schema's
notation, and it is rejected on sight — even though each individual key would
match orthographically.

The two tests to apply, both of which must pass:

1. **Is it a spelling fact?** State the entry without naming a part of speech,
   a tense, a person, a number, a gender or a case. If the justification cannot
   survive that, it is morphology and it does not belong here.
2. **Is the ordering cited?** Each list must carry a frequency claim traceable
   to a source or a measurement on gold — not an intuition about which reading
   "feels" more common.

## Ancestor Role Values

| JSON value         | Enum value                    |
|--------------------|-------------------------------|
| `"parent"`         | `AncestorRole.PARENT`         |
| `"parent_dialect"` | `AncestorRole.PARENT_DIALECT` |
| `"proto_language"` | `AncestorRole.PROTO_LANGUAGE` |
| `"ancestor"`       | `AncestorRole.ANCESTOR`       |
| `"substrate"`      | `AncestorRole.SUBSTRATE`      |
| `"superstrate"`    | `AncestorRole.SUPERSTRATE`    |
| `"adstrate"`       | `AncestorRole.ADSTRATE`       |
| `"lexifier"`       | `AncestorRole.LEXIFIER`       |
| `"creole_base"`    | `AncestorRole.CREOLE_BASE`    |
| `"related"`        | `AncestorRole.RELATED`        |

## Guidelines:

- under `"graphemes"` mark ONLY canonical phonemes, ordered from most common to less common phoneme
- if a grapheme value is exactly the same as their parent, don't redefine it, set `"graphemes_base"` instead
- when a parent grapheme is no longer valid or no longer present, set it explicitly to None to avoid inheritance
- under `"allophones"` map ALL canonical phonemes to their possible allophones, ordered from most common to less common
  phoneme realization
- if an allophone value is exactly the same as their parent, don't redefine it, set `"allophones_base"` instead
- when a parent allophone is no longer valid or no longer present, set it explicitly to None to avoid inheritance
- under `"positional_graphemes"` mark ALL context around ambiguous graphemes, ordered from most common to less common
  phoneme
- if a grapheme is unambiguous skip defining it in `"positional_graphemes"`
- if an allophone is predictable, use it in  `"positional_graphemes"`

## File Organisation

```
data/
├── SCHEMA.md  (this file)
├── es-ES.json
├── es-ES-x-andalusia-w.json
├── fr-FR.json
├── pt-PT.json
├── en-GB.json
├── de-DE.json
├── ru.json
├── eu.json
└── ...
```

## Orthography Standard Schema

Many languages are governed by a named spelling norm issued by a language academy
or state body. Where such a norm exists **and is public**, it is the primary
authority for what a grapheme *is* in that language — so it is recorded as a
first-class field rather than buried among `urls`.

| Key         | Type   | Required | Description                                        |
|-------------|--------|----------|----------------------------------------------------|
| `name`      | string | **yes**  | Title of the standard, in the language's own naming |
| `authority` | string | no       | The academy or body that issues it                  |
| `year`      | int    | no       | Year of the edition referenced                      |
| `url`       | string | no       | Public link to the standard itself                  |
| `notes`     | string | no       | Caveats — a variety that does not follow it, a competing norm |

```json
"orthography_standard": {
  "name": "Normas ortográficas e morfolóxicas do idioma galego",
  "authority": "Real Academia Galega / Instituto da Lingua Galega",
  "year": 2012,
  "url": "https://academia.gal/documents/10157/704901/Normas...pdf",
  "notes": "Defines the standard spelling; seseo and gheada are dialectal, not normative."
}
```

A standard is a property of the *language*, not of every dialect of it: a dialect
that spells by its standard language's norm simply omits the field, and consumers
walk the ancestry chain. Omit it entirely for varieties with no official norm and
for reconstructions.
