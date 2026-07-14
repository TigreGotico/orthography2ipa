# orthography2ipa — Task Playbooks

How to carry out the recurring jobs in this repo. The **rules** live in
[AGENTS.md](AGENTS.md); read its *Design constraints* section before any task that
touches `orthography2ipa/data/*.json`. Reference docs live in [`docs/`](docs/).

| I want to… | Playbook |
|---|---|
| add or extend a language spec | [Add a language](#add-a-language) |
| express a context-dependent sound | [Express a context](#express-a-context) |
| check data for design violations | [Audit the data](#audit-the-data) |
| use a word lexicon | [Supply a lexicon](#supply-a-lexicon) |
| measure accuracy | [Benchmark](#benchmark) |
| find out *why* a word is wrong | [Error analysis](#error-analysis) |
| give the engine a new capability | [Extend the engine](#extend-the-engine) |

---

## Add a language

Full walkthrough: [`docs/adding_a_language.md`](docs/adding_a_language.md); field
reference: [`orthography2ipa/data/SCHEMA.md`](orthography2ipa/data/SCHEMA.md).

1. Create `orthography2ipa/data/<code>.json`. Set `code`, `name`, `script`, and an
   honest `quality` (`stub` if that is what it is).
2. Declare `graphemes` **or** `phonemes` — a spec may not be silent about both.
3. Keep `graphemes` to real orthographic units. A multigraph earns its key only if
   its IPA is *not* the concatenation of its parts (AGENTS.md §2).
4. Put context-dependence in the rule layer, never in extra keys
   ([Express a context](#express-a-context)).
5. Cite: `sources`, `wikipedia`, `urls`, plus `glottolog_code` / `wikidata_qid` /
   `iso639_3` where they exist. Verify an identifier resolves to *this* language —
   a null code beats a wrong one.
6. Wire ancestry (`parent` / `ancestors`, `graphemes_base` for dialects) and add
   cited stubs for any ancestor that has no file (AGENTS.md §7).
7. Run the suite:

```bash
uv run pytest tests
```

`tests/test_all_languages.py` and `tests/test_language_integrity.py` sweep every
spec; add family-level cases to the matching `tests/test_<family>.py`.

## Express a context

A sound that depends on its surroundings is a **rule**, not a spelling. Pick the
mechanism, do not enumerate keys:

- **neighbouring class** → `allophone_rules` with `preceded_by` / `followed_by`
  (`vowel`, `consonant`, `front_vowel`, `back_vowel`, `palatal`, `word_boundary`).
  See [`docs/allophony.md`](docs/allophony.md).
- **word/syllable position** → `positional_graphemes`, `word_initial`,
  `word_final`. See [`docs/positional_graphemes.md`](docs/positional_graphemes.md).
- **stress** → the `stress` schema, `nucleus_stressed`.
- **across a word boundary** → `sandhi_rules`. See
  [`docs/sentence_context.md`](docs/sentence_context.md).
- **a closed irregular set** → `word_exceptions`.
- **competing readings** → give the grapheme several candidates with `weights`;
  the lattice keeps them all. See
  [`docs/candidate_scoring.md`](docs/candidate_scoring.md).

If none of these can say what the language does, the engine is missing a
predicate — [extend it](#extend-the-engine). Do **not** enumerate spellings to
simulate the context.

## Audit the data

Before committing spec changes, check you have not introduced derivable keys —
keys whose IPA is just the concatenation of parts the spec already maps. These are
the signature of enumeration.

Resolve inheritance before checking: a spec with `graphemes_base` keeps only its
*own* keys in the file, so a file-local check misses derivable keys whose parts
live in the parent.

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

Every hit is either a key to delete or a genuine unit that needs a `notes` line
saying why the orthography treats it as one symbol. Also eyeball the key list for
blocks that look loop-generated (every C×C or C×V pair) and for morpheme chunks
(`tion`, `cious`) — both are forbidden (AGENTS.md §2).

A cluster is **never** a grapheme: use `followed_by: "consonant_cluster"`
(AGENTS.md §3). Watch for the same enumeration hiding in the *rule* layer — a
`followed_by_phoneme` list of 170 cluster strings is the same violation wearing
a different hat. A closed natural class (`["p","t","k"]`) is fine; a cartesian
product is not.

## Supply a lexicon

Deep orthographies (English, Danish, Irish) cannot reach production accuracy from
grapheme rules alone. The answer is a word lexicon — **and it is never bundled**
(AGENTS.md §6). Do not try to buy the accuracy back inside a spec by adding
suffix pseudo-graphemes (⟨tion⟩) or fattening `word_exceptions`.

The caller registers one, from a local file, a URL, or a Hugging Face id:

```python
import orthography2ipa as o2i

o2i.register_lexicon("en-GB", "/data/en-GB.tsv")
o2i.register_lexicon("en-GB", "https://example.org/en-GB.tsv")
o2i.register_lexicon("en-GB", "hf://TigreGotico/en-lexicon/en-GB.tsv")   # needs .[hf]

o2i.set_lexicon_dir("~/lexicons")        # or $ORTHOGRAPHY2IPA_LEXICON_DIR
```

Format is `word<TAB>ipa`, UTF-8, NFC, lowercase keys, first entry wins. Validate
before registering:

```python
problems = o2i.validate_lexicon_text(open("en-GB.tsv").read())
```

Precedence is `word_exceptions` > lexicon > rules. Resolution is lazy (nothing is
read or fetched until the first transcription for that language) and remote
sources are cached under `$XDG_CACHE_HOME/orthography2ipa`.
`scripts/build_en_lexicon.py` builds a CMUdict-derived English one.

## Benchmark

Reference: [`docs/benchmarks.md`](docs/benchmarks.md).

```bash
python scripts/benchmark.py --list                          # datasets
python scripts/benchmark.py --dataset wikipron --lang fi    # one language
python scripts/benchmark.py --lexicon-report                # bundled lexicons
```

Rules of engagement:

- Benchmarks are **full-dataset** — never cap or sample to make a number look
  better, and say so in the report if coverage was limited.
- Gold sets are not trusted. A cited disagreement with gold is a win; report
  losses honestly alongside wins.
- A score never justifies a design violation (AGENTS.md §4). If a cleanup lowers
  the score, the score was wrong.
- The full scoreboard (`--scoreboard`) is slow: run it only from the main agent,
  and only when a change can actually alter transcription. Never delegate it.

## Error analysis

To find out *why* a word came out wrong rather than just that it did:

```bash
PYTHONPATH=$PWD python scripts/error_analysis.py pt-PT --dataset portuguese_unified --limit 300
```

Diagnose the cause before touching data — a wrong output is usually a missing
*rule*, not a missing *spelling*.

## Extend the engine

When a language needs something the rule layer cannot express, the fix goes in the
engine — generically.

1. Add the capability as a **language-neutral** predicate or rule field (e.g. a new
   `followed_by` class in `vowels.py` / `allophony.py`). No language code, name, or
   script may appear in a branch condition.
2. Document it in `data/SCHEMA.md` and the relevant `docs/` page.
3. Adopt it from the specs that needed it, and delete whatever enumeration was
   standing in for it.
4. Add engine-level tests plus a case in the family test file.

This is the only sanctioned path around a limitation. Enumerating data to fake a
missing predicate is a design violation, however good the resulting score.
