# Spec authoring rules

A spec is a JSON file in `orthography2ipa/data/` that describes one language.
These rules keep a spec a linguistic description and not a lookup table. A
violation degrades every consumer of the data, even when a score goes up.
The field reference is [`SCHEMA.md`](../../orthography2ipa/data/SCHEMA.md),
and the walkthrough is [adding_a_language.md](../adding_a_language.md).

## Add a language

1. Create `orthography2ipa/data/<code>.json`. Set `code`, `name`, `script` and
   an honest `quality`. Use `stub` when the spec is a stub.
2. Declare `graphemes` or `phonemes`. A spec may not be silent about both.
3. Keep `graphemes` to real orthographic units (see the next section).
4. Put context in the rule layer, never in extra keys (see
   [Express a context](#express-a-context)).
5. Cite every claim in `sources`, as [citations.md](citations.md) describes.
   Add `glottolog_code`, `wikidata_qid` and `iso639_3` where they exist.
   Make sure each identifier resolves to this language. A null code is
   better than a wrong one.
6. Connect the ancestry with `parent` or `ancestors`. A dialect uses
   `graphemes_base` to inherit its parent's tables.
7. If an ancestor or a related lect has no file, add a cited stub. Leave no
   dangling reference. A grouping node (`"clade": true`) is allowed only
   when the literature recognises the group.
8. Run the tests that name the language:

```bash
PYTHONPATH=$PWD python scripts/which_tests.py --lang fi
PYTHONPATH=$PWD python -m pytest $(PYTHONPATH=$PWD python scripts/which_tests.py --lang fi)
```

`scripts/which_tests.py` writes one test file per line to stdout and a
summary line to stderr. With no `--lang`, it reads the specs that changed
against `origin/dev`. A family test file that passes does not prove that a
`test_cited_rules_*.py` file for the same language passes.

## A grapheme key is an orthographic unit

A key in `graphemes` must be a unit that the writing system treats as one
symbol. That is a letter (`b`, `ä`, `ц`) or a multigraph the orthography
reads as one unit (⟨sch⟩ /ʃ/, ⟨szcz⟩ /ʂtʂ/, ⟨ng⟩ /ŋ/, a pinyin final
⟨iang⟩). A multigraph earns its key when one of these three tests passes:

1. Its IPA is not the concatenation of the IPA of its parts. ⟨sch⟩ is /ʃ/,
   and s+c+h gives /sx/.
2. It spells one phonological unit: one segment or one syllable nucleus.
   This covers diphthongs (Finnish ⟨ai⟩), affricates (⟨dž⟩), prenasalized
   stops (Bantu ⟨mb⟩), clicks (⟨gc⟩), aspirates (Urdu ⟨پھ⟩), geminates (⟨tt⟩
   /tː/) and the letter-plus-diacritic units of an abjad or an abugida.
3. It blocks a wrong maximal-munch match. The tokenizer is greedy, so a key
   can earn its place by defeating a wrong neighbour. Mirandese ⟨anh⟩ /aɲ/
   exists because without it the nasal-vowel digraph ⟨an⟩ wins, and
   ⟨danho⟩ reads /dɐ̃u/. Say so in `notes`.

A key that fails all three tests is noise. ⟨bl⟩→/bl/ fails because b+l
already gives /bl/. Russian ⟨бь⟩→/bʲ/ fails because the engine already reads ь
as /ʲ/.

These keys are forbidden:

- Cartesian products: every consonant pair (`bd`, `bf`, `bk`) or every
  consonant-vowel pair (`дзе`, `дзё`, `дзю`). A block of keys that looks like
  the output of a nested loop is wrong.
- Morpheme and suffix chunks such as `tion` or `cious`. A closed irregular
  set goes in `word_exceptions`. A cited suffix rule goes in
  `grammatical_endings`.
- Statistical substrings, that is, keys that exist because a sequence is
  frequent.

Before you delete a key that an audit flags, apply all three tests. Then
delete it and run the tests. If a test fails, the key encodes a fact. Find the
fact and state it as a rule, or keep the key and write in `notes` which test it
passes.

## Express a context

A sound that depends on its neighbours, its position or the stress is a rule,
not a spelling. Pick the mechanism from this table.

| The context | The mechanism |
|---|---|
| A neighbouring sound or letter class | `allophone_rules` with `preceded_by` or `followed_by` (`vowel`, `consonant`, `front_vowel`, `back_vowel`, `palatal`, `word_boundary` and more) |
| A neighbour two or three slots away | `preceded_by_2`, `followed_by_2`, `preceded_by_3`, `followed_by_3`, `preceded_by_phoneme_2`, `followed_by_phoneme_2` |
| The position in the word or syllable | `positional_graphemes`, `word_initial`, `word_final`, `syllable_position` |
| The stress | The `stress` block and the `nucleus_stressed` position |
| A word boundary | `sandhi_rules` |
| A closed irregular set | `word_exceptions` |
| Competing readings | Several candidates with `weights` (see [candidate_scoring.md](../candidate_scoring.md)) |

Each mechanism has its own page: [allophony.md](../allophony.md),
[positional_graphemes.md](../positional_graphemes.md) and
[sentence_context.md](../sentence_context.md). A context spelled out as extra
keys asserts spellings the language does not have. The tokenizer is
maximal-munch, so the extra keys also change how neighbouring rules see the
word.

If no mechanism can say what the language does, the engine lacks a
predicate. Add the predicate as [engine.md](engine.md) describes. Do not
enumerate spellings to simulate it.

A cluster is never a grapheme. Use `followed_by: "consonant_cluster"`. The
same violation can hide in the rule layer: a `followed_by_phoneme` list of
many cluster strings is an enumeration. A closed natural class such as
`["p", "t", "k"]` is correct.

## Audit the data

A derivable key has an IPA value that is the concatenation of parts the spec
already maps. It is the signature of enumeration. This script resolves
inheritance first, because a spec with `graphemes_base` keeps only its own
keys in the file:

```bash
python3 - <<'EOF'
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

Each hit is a key to delete or a real unit that needs a `notes` line. Many
hits are diphthongs and affricates that pass test 2. The script reads only
the value, so it cannot see the shape of a cartesian block. A key such as
Russian ⟨ки⟩ /kʲɪ/ is not к+и, because it bundles palatalisation and vowel
reduction. A block of every consonant-vowel pair is still a cartesian product,
whatever its values say.

`positional_graphemes` can hide the same block. This script lists every
multi-character positional key:

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

Judge each key with the three tests. A real multigraph (⟨ch⟩, ⟨sch⟩, ⟨mb⟩)
belongs there. A consonant-vowel pair does not.

## A shared alphabet is not a shared phonology

Do not generate one language's rules from another language's template. Derive
each inventory from the language's own sources, and check every generated
rule against a cited form in that language. Ukrainian is the warning case. It
writes the Cyrillic alphabet of Russian, but uk ⟨и⟩ is a hard /ɪ/, so a Russian
softening rule on ⟨и⟩ palatalises the wrong consonants. Ukrainian ⟨л⟩ is
velarised /ɫ/, so its geminate is /ɫː/.

## Supply a lexicon, never bundle one

The package ships descriptions: grapheme maps, rules, inventories and
ancestry. It ships no word lists, lexicons, gold sets or weights. A lexicon is
a corpus. Bundling one makes the wheel larger and freezes a corpus into a
release. Deep orthographies such as English and Danish cannot reach
production accuracy from rules alone. The answer is a lexicon that the caller
supplies:

```python
import orthography2ipa as o2i

o2i.register_lexicon("en-GB", "en-GB.tsv")               # a local file
o2i.register_lexicon("en-GB", "https://example.org/en-GB.tsv")
o2i.register_lexicon("en-GB", "hf://<repo_id>/<path>")   # needs the hf extra
o2i.set_lexicon_dir("~/lexicons")    # or $ORTHOGRAPHY2IPA_LEXICON_DIR

problems = o2i.validate_lexicon_text(open("en-GB.tsv").read())
```

The format is `word<TAB>ipa` in UTF-8 NFC, with lowercase keys. The first
entry for a word wins. The precedence is `word_exceptions`, then the lexicon,
then the rules. Nothing is read or fetched until the first transcription in
that language. Remote sources are cached under
`$XDG_CACHE_HOME/orthography2ipa`. `scripts/build_en_lexicon.py` builds an
English lexicon from CMUdict.

Do not buy accuracy back inside a spec with suffix pseudo-graphemes or a
growing `word_exceptions`. Text normalisation, diacritic restoration, script
conversion and morphology belong downstream, in a consumer of the lattice
such as [arbtok](https://github.com/TigreGotico/arbtok),
[tugaphone](https://github.com/TigreGotico/tugaphone) or
[scriptconv](https://github.com/TigreGotico/scriptconv). The specs assume
normalised input.

## Ambiguous grammatical endings

A list-valued `grammatical_endings` entry injects a reading into the beam
that the spec cannot choose between. It is the one way morphological
ambiguity reaches the lattice. Every ending is a cited claim about how a
suffix is realised. Corpus frequency can support the order of a list, but a
frequency count alone is not a citation. A review of a change that adds or
widens a list-valued ending verifies three things in writing:

1. The lattice hole is proven. The change shows that the missing reading is
   absent from `word_candidates` at a generous *k* and beam width over a named
   gold sample, and it shows the reachability after the change. A reading
   that some *k* already reaches is a ranking problem, so the entry is
   rejected.
2. The order is cited. The reading at rank 1 carries a source or a
   measurement on gold, in the spec's `notes` beside the ending.
3. The oracle change is reported apart. It is not counted as ranking-error
   headroom or as a cross-system win (see
   [benchmark_methodology.md](../benchmark_methodology.md#injected-alternatives-do-not-count-as-ranking-error)).

`tests/test_grammatical_endings.py` checks that every list-valued ending is
documented in its spec's `notes`. It also caps how many one spec may declare.
Raising the cap is a change to [`AGENTS.md`](../../AGENTS.md), argued there
first.

---
[← Sourcing a claim](../sourcing.md) · [Home](../index.md) · [Citation honesty →](citations.md)
