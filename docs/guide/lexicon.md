# Lexicons and forced pronunciations

Some words cannot be transcribed from their spelling, and no rule can change that. Brand names, proper nouns, acronyms and loanwords are the usual cases. For these words the caller already knows the answer and needs a way to give it. The engine has three tiers that override the rules, and this page describes each one.

## The precedence ladder

```
<phoneme ph="…">  >  spec word_exceptions  >  the engine's lexicon  >  the rules
```

| Tier | Scope | Who supplies it |
| :--- | :--- | :--- |
| `<phoneme>` markup | One occurrence of a word in the input text | The caller, in the text |
| `word_exceptions` | A small, closed set of irregular words | The spec author, in the JSON |
| Lexicon | Thousands of words in a `word<TAB>ipa` file, for one engine | The caller, in `Pipeline(lexicon=...)`, from a file, a URL, a dataset or an installed package such as `o2i-lexicons` |
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

The engine checks `ph` against the phoneme inventory of the spec. That inventory is `phoneme_inventory(spec, lexicon)`: each segment the spec and the lexicon of the engine can emit. A symbol outside it raises `MarkupError`. The check makes the feature safe. A TTS frontend builds its embedding table from the inventory before it trains. A symbol that appears only at inference has no vector, so each word that carries it is mispronounced, permanently and without a sign.

A loanword is the case that matters. In Arabic, English *meeting* is nativised and does not keep its English sounds. Modern Standard Arabic has /q/ and /dʒ/ and no /ɡ/, so the `ar` spec refuses a reading with [ɡ]:

```python
>>> G2P("ar").transcribe('<phoneme ph="ˈmiːtinɡ">meeting</phoneme>')
Traceback (most recent call last):
    ...
orthography2ipa.markup.MarkupError: <phoneme ph='ˈmiːtinɡ'> uses ['ɡ'], which the ar spec does not declare.
...
```

In Najdi Arabic, /ɡ/ is the Gulf reflex of qāf, and the `ars-SA` spec has it. The same reading then passes:

```python
>>> G2P("ars-SA").transcribe(
...     'عِنْدِي <phoneme ph="ˈmiːtinɡ">meeting</phoneme> السَّاعَة')
'ˈʕindiː ˈmiːtinɡ asˈsaːʕa'
```

The inventory is a claim about the phonology, so it separates varieties that really differ. A refusal for `ar` and an acceptance for `ars-SA` show the check at work.

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

The package ships no lexicon. A lexicon is a word list, not a description of a language, so it is not part of the payload. The wheel holds only `data/*.json` and `data/SCHEMA.md`. The caller reads a lexicon into a mapping and gives it to one engine through a `Pipeline`:

```python
from orthography2ipa import G2P, Pipeline, load_lexicon

lexicon = load_lexicon("/data/en-GB.tsv")                  # a local file
lexicon = load_lexicon("https://example.org/en-GB.tsv")    # a URL
lexicon = load_lexicon("hf://<owner>/<repo>/<file>.tsv")   # needs the hf extra
engine = G2P("en-GB", pipeline=Pipeline(lexicon=lexicon))
```

The lexicon belongs to that engine. `load_lexicon` sets no state, so another engine in the process keeps its own output, and two engines with different lexicons run side by side. A mapping that you build in code works too. Its keys are lowercase and NFC, the same as the keys of a file:

```python
engine = G2P("en-GB", pipeline=Pipeline(lexicon={"colonel": "ˈkɜːnəl"}))
```

`Pipeline(lexicon={})` is a lexicon with no entries, so that engine takes the rules. With `Pipeline()` or with no pipeline, the engine reads the [process-wide lexicon](#the-process-wide-api), which is deprecated.

A Hugging Face id has the form `hf://<owner>/<repo>/<path>`, with an optional `@<revision>`. The library fetches it from a dataset repository with `huggingface_hub`. A URL or a Hugging Face file downloads once into `$XDG_CACHE_HOME/orthography2ipa/lexicons`, which is `~/.cache/orthography2ipa/lexicons` by default.

### Packaged lexicons

A package can supply a lexicon for a language. [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) is such a package. It holds only the words that the rules get wrong, and each entry records the gold it came from. Install it through the extra:

```bash
uv pip install 'orthography2ipa[lexicons]'
```

The install changes no output. The transcription is a function of the spec, the input and the explicit configuration of the caller, never of the environment. So the caller reads a packaged lexicon in code and gives it to the engine that wants it:

```python
from orthography2ipa import G2P, Pipeline, packaged_lexicon, packaged_lexicon_sources

packaged_lexicon_sources()       # {'en-GB': PosixPath('…/wikipron.tsv')}: lists, reads nothing
engine = G2P("en-GB", pipeline=Pipeline(lexicon=packaged_lexicon("en-GB")))
```

`packaged_lexicon()` raises `LookupError` when no installed package supplies a file for the code. A request for an absent lexicon is an error, not a quiet fall back to the rules. The same error comes from a provider that raises or that returns a path that is not a file, and the library logs the reason as a warning.

A provider declares one entry point per language code in the group `orthography2ipa.lexicons`. The entry point loads a callable. The library calls it with the name of the entry point, and the callable returns the path of a local `word<TAB>ipa` file:

```toml
[project.entry-points."orthography2ipa.lexicons"]
"en-GB" = "o2i_lexicons:tsv_path"
```

Only `packaged_lexicon()`, `packaged_lexicon_sources()` and `use_packaged_lexicons()` read the entry points, once per process. Import, `get()` and transcription never read them. The name of the entry point must name a registered spec exactly. The library skips an entry point that only a nearest-language guess would place, and it logs a warning. When two packages serve one spec, the entry point named for the exact resolved code wins. Then the first by distribution name wins, and the library logs a warning.

The benchmark never enables a packaged lexicon, so the board stays rules-only whatever is installed.

### The file format

A lexicon is a UTF-8 TSV with one `word<TAB>ipa` pair per line. The words are lowercase, and both columns are NFC-normalised. Sort the file, because the first entry for a word wins. The parser skips blank lines and lines that do not have exactly two fields.

### Reading a lexicon

Import of the package reads no lexicon and does not use the network. A call to `get()` does not read one either. `load_lexicon` and `packaged_lexicon` read the file when you call them, and return a new mapping each time. Build the mapping once and share it between the engines that want it.

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
| `Pipeline(lexicon=None, syllabifier=None)` | yes | The lexicon and the syllabifier of one engine |
| `load_lexicon(source)` | yes | The `{word: ipa}` map at a file, a URL or a dataset id |
| `packaged_lexicon(code)` | yes | The `{word: ipa}` map an installed package supplies for a code |
| `packaged_lexicon_sources()` | yes | The installed packaged lexicons, as `{code: path}`. Reads no entry |
| `available_lexicon_codes()` | yes | The registered codes, the file stems in the directory, and the enabled packaged codes |
| `resolve_lexicon_source(source)` | yes | The local file for a source, fetched if remote |
| `validate_lexicon_text(text)` | yes | The list of problems in a lexicon body |
| `is_ipa_string(ipa)` | yes | True for an NFC string of IPA characters |
| `lexicon_path(code)` | `orthography2ipa.lexicon` only | The local file behind the lexicon of a code, or `None` |
| `parse_lexicon_text(text)` | `orthography2ipa.lexicon` only | Parse a TSV body, first entry winning |

`examples/08_lexicon_overlay.py` gives an engine a two-word lexicon and shows the overlay win over the rules:

```
colonel -> 'ˈkɒlənəl'                     # rules only
colonel -> 'ˈkɜːnəl'   confidence=1.0     # with the lexicon
choir   -> 'ˈkwaɪə'    confidence=1.0
```

### The process-wide API

These names act on the whole process: each engine with no lexicon in its pipeline reads them. A call made for one engine therefore changes the output of every other engine in the process. They are deprecated. They keep working for one stable cycle, and each one raises a `DeprecationWarning` that names the release that removes it.

| Deprecated name | Purpose | Use in its place |
| :--- | :--- | :--- |
| `register_lexicon(code, source)` | Use `source` as the lexicon for `code` | `Pipeline(lexicon=load_lexicon(source))` |
| `set_lexicon_dir(path)` | Use a directory of `{code}.tsv` files, or `None` to unset it | `Pipeline(lexicon=load_lexicon(path))` with the file of the language |
| `$ORTHOGRAPHY2IPA_LEXICON_DIR` | The same directory, from the environment. `set_lexicon_dir()` overrides it | `Pipeline(lexicon=load_lexicon(path))` with the file of the language |
| `use_packaged_lexicons(codes=None)` | Enable the installed packaged lexicons, for every code or for `codes` | `Pipeline(lexicon=packaged_lexicon(code))` |
| `clear_lexicons()` | Forget every registration and the directory, and disable the packaged lexicons | Nothing: the lexicon of an engine ends with the engine |
| `get_lexicon(code)` | The `{word: ipa}` map for a resolved code, or `{}` | `Pipeline.lexicon` |

Their precedence is `register_lexicon()`, then the directory, then an enabled packaged lexicon, and the sources do not merge. `register_lexicon()` resolves `code` to the spec that `get()` returns for it, so two tags that resolve to the same spec share one slot. A file in the directory belongs to the spec that its name resolves to, and a file named for the exact resolved code wins over the others. The engine reads a process-wide lexicon on the first transcription for that language, and caches it for the life of the process.

## Building an English lexicon from CMUdict

`scripts/build_en_lexicon.py` builds an English lexicon that you can load. Run it from a checkout:

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
