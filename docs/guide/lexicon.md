# Lexicons and forced pronunciations

Some words cannot be transcribed from their spelling, and no rule can change that. Brand names, proper nouns, acronyms and loanwords are the usual cases. For these words the caller already knows the answer and needs a way to give it. The engine has three tiers that override the rules, and this page describes each one.

## The precedence ladder

```
<phoneme ph="…">  >  spec word_exceptions  >  caller's lexicon  >  enabled packaged lexicon  >  the rules
```

| Tier | Scope | Who supplies it |
| :--- | :--- | :--- |
| `<phoneme>` markup | One occurrence of a word in the input text | The caller, in the text |
| `word_exceptions` | A small, closed set of irregular words | The spec author, in the JSON |
| Lexicon | Thousands of words in a `word<TAB>ipa` file | The caller, by registration |
| Packaged lexicon | The words the rules get wrong, in a `word<TAB>ipa` file | An installed package, such as `o2i-lexicons`, that the caller enables in code |
| Rules | Every other word | The spec: graphemes, positional overrides, allophone and stress rules |

Each tier answers the same question: what is the IPA of this word? The stages after it do not depend on which tier answered. Cross-word sandhi still applies, and the word reports `confidence == 1.0`. An entry from `word_exceptions` or from a lexicon also gets the stress mark of the spec. A forced `<phoneme>` reading does not, as the next section explains.

`G2P._override_for` looks up `word_exceptions` and the lexicon with the same key. The key is the word in lowercase, with the casing rules of the language (Turkish dotted and dotless i, for example). If the raw word misses, the lookup tries again without the punctuation at its edges, so ⟨I,⟩ finds the entry for ⟨I⟩. For a spec that sets `word_internal_apostrophe`, a typographic apostrophe (U+2019) also matches an entry written with U+0027.

## Forcing one occurrence: `<phoneme>`

SSML's `<phoneme>` element sets the IPA of one word in the input text. TTS frontends already use it:

```python
>>> from orthography2ipa import G2P
>>> G2P("pt-PT").transcribe('olá <phoneme ph="ˈɡuɡɫ">Google</phoneme> mundo')
'oˈla ˈɡuɡɫ ˈmũdu'
```

The `alphabet` attribute is optional. If you give it, it must be `ipa`, and any other value raises `MarkupError`. This library reads no other alphabet, and a reading of X-SAMPA as IPA would mispronounce the word without a sign. An unclosed tag also raises `MarkupError`. Text with no markup passes through unchanged, so a caller that never writes `<phoneme>` sees no difference.

### Both halves carry information

The `ph` attribute is the IPA. It replaces the rules for that word, and the engine derives nothing from the spelling.

The text of the element is the spelling, and it is not decoration. Cross-word rules read the orthography, because a case ending is a fact about the written word that its IPA does not show. The ⟨-in⟩ of قَاضٍ is an ending, and the ⟨-in⟩ of مُؤْمِن is part of the stem. A bare bracket escape that held only the IPA would lose the spelling and break sandhi.

### The engine does not re-stress a forced reading

`ph` is the pronunciation, with its stress marks. A caller who writes `ˈɡuɡɫ` has placed the stress. A caller who writes `ɡuɡɫ` with no mark says that the word has no stress, and the output is `ɡuɡɫ`. A stress mark derived from the spelling would overrule the reading that the caller forced.

### Markup comes before normalization

The engine reads the markup before the normalize step. A normalize plugin, such as a diacritizer or a number expander, never sees a tag. It gets the plain runs of text between the tags, which is the only text it must rewrite.

### The inventory check

The engine checks `ph` against the phoneme inventory of the spec. That inventory is `phoneme_inventory(spec)`: each segment the spec can emit. A symbol outside it raises `MarkupError`. The check makes the feature safe. A TTS frontend builds its embedding table from the inventory before it trains. A symbol that appears only at inference has no vector, so each word that carries it is mispronounced, permanently and without a sign.

A loanword is the case that matters. In Arabic, English *meeting* is nativised and does not keep its English sounds. Modern Standard Arabic has /q/ and /dʒ/ and no /ɡ/, so the `ar` spec refuses a reading with [ɡ]:

```python
>>> G2P("ar").transcribe('<phoneme ph="ˈmiːtinɡ">meeting</phoneme>')
Traceback (most recent call last):
    ...
orthography2ipa.markup.MarkupError: <phoneme ph='ˈmiːtinɡ'> uses ['ɡ'], which the ar spec does not declare.
...
```

In Najdi Arabic, /ɡ/ is the Gulf reflex of qāf, and the `ar-SA-x-najd` spec has it. The same reading then passes:

```python
>>> G2P("ar-SA-x-najd").transcribe(
...     'عِنْدِي <phoneme ph="ˈmiːtinɡ">meeting</phoneme> السَّاعَة')
'ˈʕindiː ˈmiːtinɡ asˈsaːʕa'
```

The inventory is a claim about the phonology, so it separates varieties that really differ. A refusal for `ar` and an acceptance for `ar-SA-x-najd` show the check at work.

A caller who means to emit a phoneme outside the inventory says so in code:

```python
>>> G2P("ar", allow_undeclared_phonemes=True).transcribe(
...     '<phoneme ph="ˈmiːtinɡ">meeting</phoneme>')
'ˈmiːtinɡ'
```

That choice is explicit, and anyone who reads the call site can see it. A lasting claim about the phonology belongs in the spec, where people can read it, cite it and diff it.

## Whole-word overrides in the spec: `word_exceptions`

`word_exceptions` maps a word to its IPA in the JSON of the spec. It suits a small, closed set of irregular words, such as English `{"one": "wʌn"}`. An inline exception beats a lexicon and the rules. The field is `BASE_MERGE`, so a dialect inherits the exceptions of its base through the `word_exceptions_base` key. The own entries of the dialect win word by word ([data_model.md](../specs/data_model.md#inheritance-between-specs)).

The field does not scale to thousands of entries. Deep orthographies such as English, Danish and Irish cannot reach production accuracy from grapheme rules alone, because too many words are irregular. A lexicon covers that case.

## Supplying a lexicon

The package ships no lexicon. A lexicon is a word list, not a description of a language, so it is not part of the payload. The wheel holds only `data/*.json` and `data/SCHEMA.md`, and `available_lexicon_codes()` returns an empty list on a fresh install, with or without a lexicon package. The caller supplies a lexicon from a local file, a URL or a Hugging Face dataset:

```python
import orthography2ipa as o2i
o2i.register_lexicon("en-GB", "/data/en-GB.tsv")                  # a local file
o2i.register_lexicon("en-GB", "https://example.org/en-GB.tsv")    # a URL
o2i.register_lexicon("en-GB", "hf://<owner>/<repo>/<file>.tsv")   # needs the hf extra
o2i.set_lexicon_dir("~/lexicons")   # a directory of {code}.tsv files
```

The environment variable `ORTHOGRAPHY2IPA_LEXICON_DIR` sets the directory too, and `set_lexicon_dir()` overrides it. A Hugging Face id has the form `hf://<owner>/<repo>/<path>`, with an optional `@<revision>`. The library fetches it from a dataset repository with `huggingface_hub`. A URL or a Hugging Face file downloads once into `$XDG_CACHE_HOME/orthography2ipa/lexicons`, which is `~/.cache/orthography2ipa/lexicons` by default.

`register_lexicon(code, source)` resolves `code` to the spec that `get()` returns for it. So two tags that resolve to the same spec share one slot, and the later registration replaces the earlier one. A file in the lexicon directory belongs to the spec that its name resolves to, so `en.tsv` serves `en-GB`. A file named for the exact resolved code wins over the others. A registered lexicon wins over a file in the directory.

### Packaged lexicons

A package can supply a lexicon for a language. [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) is such a package. It holds only the words that the rules get wrong, and each entry records the gold it came from. Install it through the extra:

```bash
uv pip install 'orthography2ipa[lexicons]'
```

The install changes no output. The transcription is a function of the spec and the input, never of the environment, so the caller enables a packaged lexicon in code:

```python
import orthography2ipa as o2i
o2i.packaged_lexicon_sources()          # {'en-GB': PosixPath('…/wikipron.tsv')}: lists, enables nothing
o2i.use_packaged_lexicons()             # enable every installed packaged lexicon
o2i.use_packaged_lexicons(["en-GB"])    # enable only these
o2i.clear_lexicons()                    # disable them again, with every registration
```

`use_packaged_lexicons()` raises `LookupError` for a code that no installed package serves. A request for an absent lexicon is an error, not a quiet fall back to the rules.

A provider declares one entry point per language code in the group `orthography2ipa.lexicons`. The entry point loads a callable. The library calls it with the name of the entry point, and the callable returns the path of a local `word<TAB>ipa` file:

```toml
[project.entry-points."orthography2ipa.lexicons"]
"en-GB" = "o2i_lexicons:tsv_path"
```

Only `use_packaged_lexicons()` and `packaged_lexicon_sources()` read the entry points, once per process. Import, `get()` and transcription never read them. The library loads a provider only on the first transcription for its language after the caller enabled it. The name of the entry point must name a registered spec exactly. The library skips an entry point that only a nearest-language guess would place, and it logs a warning. It also logs a warning and uses the rules when a provider raises or returns a path that is not a file.

An enabled packaged lexicon has the lowest rank of the lexicon sources. A lexicon from `register_lexicon()` or from the lexicon directory replaces it for that language. The two lexicons do not merge. When two packages serve one spec, the entry point named for the exact resolved code wins. Then the first by distribution name wins, and the library logs a warning.

The benchmark never enables a packaged lexicon, so the board stays rules-only whatever is installed.

### The file format

A lexicon is a UTF-8 TSV with one `word<TAB>ipa` pair per line. The words are lowercase, and both columns are NFC-normalised. Sort the file, because the first entry for a word wins. The parser skips blank lines and lines that do not have exactly two fields.

### Loading is lazy

Import of the package reads no lexicon and does not use the network. A call to `get()` does not read one either. The engine reads a lexicon, and fetches it if it is remote, on the first transcription for that language through `get_lexicon(code)`. It then caches the result for the life of the process. `register_lexicon`, `set_lexicon_dir` and `clear_lexicons` clear that cache. A language with no lexicon gets an empty mapping, and its output is the same as with no lexicon module at all.

### Checking a lexicon before you use it

`validate_lexicon_text` returns a list of `(line_no, reason)` pairs, and an empty list means that the file is clean:

```python
import orthography2ipa as o2i
o2i.validate_lexicon_text("cat\tkæt\nnature\tˈneɪtʃə\n")
# []
o2i.validate_lexicon_text("Cat\tkæt\nnoipa\ncat\tk at\n")
# [(1, "word not lowercase: 'Cat'"),
#  (2, "expected 'word<TAB>ipa', got 1 fields"),
#  (3, "IPA not NFC / not IPA-only: 'k at'")]
```

The function checks that each line has one TAB and that neither column is empty. It checks that the word is NFC and lowercase, and that the IPA holds IPA characters only. It also flags a word that repeats an earlier line. `is_ipa_string` holds the IPA rule: phonetic letters, combining diacritics, and the length, stress, tie and tone marks. It rejects whitespace, digits and ASCII punctuation, except the prosodic boundaries `.`, `|` and `‖`.

Write the lexicon in the same broad IPA that the `graphemes` of the spec use. Then the output of the lexicon and the output of the rules are comparable.

### The lexicon API

| Function | Top-level | Purpose |
| :--- | :--- | :--- |
| `register_lexicon(code, source)` | yes | Use `source` as the lexicon for `code` |
| `set_lexicon_dir(path)` | yes | Use a directory of `{code}.tsv` files, or `None` to unset it |
| `clear_lexicons()` | yes | Forget every registration and the directory, and disable the packaged lexicons |
| `use_packaged_lexicons(codes=None)` | yes | Enable the installed packaged lexicons, for every code or for `codes` |
| `packaged_lexicon_sources()` | yes | The installed packaged lexicons, as `{code: path}`. Enables nothing |
| `get_lexicon(code)` | yes | The `{word: ipa}` map for a resolved code, or `{}` |
| `available_lexicon_codes()` | yes | The registered codes, the file stems in the directory, and the enabled packaged codes |
| `resolve_lexicon_source(source)` | yes | The local file for a source, fetched if remote |
| `validate_lexicon_text(text)` | yes | The list of problems in a lexicon body |
| `is_ipa_string(ipa)` | yes | True for an NFC string of IPA characters |
| `lexicon_path(code)` | `orthography2ipa.lexicon` only | The local file behind the lexicon of a code, or `None` |
| `parse_lexicon_text(text)` | `orthography2ipa.lexicon` only | Parse a TSV body, first entry winning |

`examples/08_lexicon_overlay.py` registers a two-word lexicon and shows the overlay win over the rules:

```
colonel -> 'ˈkɒlənəl'                     # rules only
colonel -> 'ˈkɜːnəl'   confidence=1.0     # with the lexicon
choir   -> 'ˈkwaɪə'    confidence=1.0
```

## Building an English lexicon from CMUdict

`scripts/build_en_lexicon.py` builds an English lexicon that you can register. Run it from a checkout:

```bash
O2I_LEXICON_OUT=/data/en-GB.tsv python scripts/build_en_lexicon.py
```

The script downloads its two sources, keeps the 5,000 most frequent words that CMUdict covers, and writes a sorted NFC file. With no `O2I_LEXICON_OUT`, it writes `en-GB.tsv` at the root of the checkout, outside the package. The same sources give the same file on each run.

| Source | Licence | Use |
| :--- | :--- | :--- |
| [CMU Pronouncing Dictionary](https://github.com/cmusphinx/cmudict), Carnegie Mellon University Speech Group | BSD-style, free for any use | The pronunciations. The script converts each hand-curated ARPABET entry to broad, non-rhotic IPA that leans to RP, with ⟨ɡ⟩ as U+0261 to match the `en-GB` inventory. |
| [google-10000-english](https://github.com/first20hours/google-10000-english), Josh Kaufman, from the Google Web Trillion Word Corpus | MIT | The frequency order only, to select the words. None of its content goes into the file. |

CMUdict describes General American, so this file helps most on the General American evaluation. A full RP or `en-GB` lexicon belongs in a downstream package or a dataset of its own, not in this library.

## Measuring the effect of a lexicon

`scripts/benchmark.py --lexicon-report` scores each language that has a lexicon twice on the same WikiPron gold: once with the rules only and once with the lexicon. It writes `docs/evaluation/generated/lexicon_scoreboard.md` and `benchmarks/lexicon_results.json`. The benchmark runs in its own process, so give it the lexicon through the directory variable:

```bash
ORTHOGRAPHY2IPA_LEXICON_DIR=/data/lexicons PYTHONPATH=$PWD python scripts/benchmark.py --lexicon-report
```

The report has two sets of columns. The full columns score every gold word, so each gold word outside the lexicon dilutes the gain. The covered columns score only the gold words that the lexicon contains, where the overlay can act. The delta on the covered subset compares the lexicon with the rules on the same words. The report also keeps the rules honest: a lexicon must lower PER without hiding a regression in the grapheme rules behind it. [lexicon_scoreboard.md](../evaluation/generated/lexicon_scoreboard.md) holds the last report.

[spec_authoring.md](../contributing/spec_authoring.md#supply-a-lexicon-never-bundle-one) gives the rule for contributors: supply a lexicon, never bundle one.

---
[← Getting Started](getting_started.md) · [Home](../index.md) · [Distance Metrics →](distance.md)
