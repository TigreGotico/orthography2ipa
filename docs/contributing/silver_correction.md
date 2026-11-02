# Silver IPA correction

`scripts/correct_silver_ipa.py` writes a corrected IPA for each row of the
LLM-generated gold sets. It asks Claude for each sentence, under rules that
keep the engine output out of the first two readings. The result stays a
silver label. Its tier is `llm-corrected`, and it gates no quality decision.

## The sets it reads

The tool reads these sets:

| Set | Where the rows come from |
| :--- | :--- |
| `spain_romance_tts` | `orthography2ipa/data/gold/spain_romance_tts/<lect>.tsv` |
| `portuguese_tts` | `orthography2ipa/data/gold/portuguese_tts/<lect>.tsv` |
| `arabic_tts` | `orthography2ipa/data/gold/arabic_tts/<lect>.tsv` |
| `kabyle_tts` | `orthography2ipa/data/gold/kabyle_tts/<lect>.tsv` |
| `iberian_creole_tts` | `orthography2ipa/data/gold/iberian_creole_tts/<lect>.tsv` |
| `gold20_arabic` | the `scripts/benchmark.py` loader of the same name |
| `mirandese_dict` | the `scripts/benchmark.py` loader of the same name |
| `barranquenho_dict` | the `scripts/benchmark.py` loader of the same name |

The three remote sets carry no row id. The tool uses the position of the row
in the loader output as its id.

## Convention sheets

Published descriptions of a lect do not always agree. For example, they give
different stress rules for Modern Standard Arabic, and different pausal
forms. If each row makes its own choice, the set is not consistent. Thus each
lect gets one convention sheet, and every pass of every row reads it.

The `conventions` subcommand writes the sheets. It sends one request for each
lect. The request gets the notes and the cited sources of the lect spec. It
does not get a row or the engine output. The tool writes the answer to
`orthography2ipa/data/gold/conventions/<lect>.md`. The sheet has one section
for each of these topics, and each section names its source:

- the stress rule and the tradition that it follows
- the function words that carry stress and the words that do not
- the pausal forms: where they apply, and what tanwīn and the final vowels do
- the connected-speech processes across word boundaries
- the notation of glides and diphthongs
- the other choices where published descriptions disagree

The last section, word segmentation, comes from the tool and not from the
model. Refer to [Word segmentation](#word-segmentation).

Without `--lect`, the subcommand writes a sheet for each lect of the sets
that `--dataset` names, and by default of all eight sets. It sends up to
`--concurrency` requests at the same time (8 by default), with the keys in
turn.

Read each sheet and correct it before the run. The sheet is plain Markdown.
If a sheet file exists, the subcommand keeps it. To write it again, give
`--force`. A run refuses a lect that has no sheet. A change to a sheet changes
the cache key, so the rows of that lect run again.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at
punctuation. An apostrophe between two letters stays in its word only if the
spec sets `word_internal_apostrophe`. Thus `liga-me` is two words, `ˈliɡɐ mɨ`.

Each pass gets the list of words of its text, in this split. It must write
one IPA word for each word in the list. The comparison of the passes ignores
spaces, so a pass that joins two words can still agree. Thus the tool counts
the words of each output row and compares the count with the engine output.
If the counts are different, the `word_count` field of the row shows it and
the run report names the row. The tool does not change the IPA of the row.

## How the tool decides a row

Each row gets up to three passes. Every pass returns JSON that matches a
schema. Every pass gets the convention sheet of the lect after the notes,
and the word list of the text.

1. Pass A transcribes the sentence. It gets the sentence, the lect code, and
   the notes and cited sources of the lect spec. It does not get the engine
   output or the existing `ipa`. The notes give the transcription conventions
   and context. For the pronunciation, the prompt tells the model to follow
   the published phonological descriptions of the lect, also where a note
   disagrees.
2. Pass B does the same task with a different framing. It writes each word in
   its citation form, then applies the connected-speech rules of the lect. It
   does not get the engine output or the existing `ipa` either.
3. The tool compares A, B and the engine output. It uses the broad
   normalisation of the scorer: no spaces and no narrow marks. It keeps the
   primary stress. It moves each stress mark to the vowel after it, so
   `esˈta` and `eˈsta` are equal, but `ˈesta` and `esˈta` are not. It removes
   the secondary stress marks, because the board does not score them.
4. If all three agree, the tool keeps A and sets the flag `agreed`.
5. If they do not agree, pass C decides. It sees A, B, the engine output and
   the cited rules of the lect. It returns one IPA, a flag (`agreed`,
   `adjudicated` or `uncertain`) and a reason of one line. It also returns
   `note_conflict`: the spec note that its reading disagrees with, or an
   empty string. A conflict is a lead for a fix to the spec.

## The output

The tool writes one file for each set,
`orthography2ipa/data/gold/<set>.llm-corrected.jsonl`. It does not change
the original files. A new run merges its rows into the file, sorted by lect
and id. Each line holds one row:

| Field | Value |
| :--- | :--- |
| `dataset`, `lect`, `id`, `sentence` | the source row |
| `ipa` | the corrected IPA, with the IPA letter ɡ (U+0261) for the voiced velar stop where a pass wrote ASCII g (U+0067) |
| `ipa_llm_original` | the `ipa` of the source row |
| `ipa_engine` | the engine output for the sentence |
| `model` | the model that wrote the passes |
| `passes` | the IPA of pass A and pass B, and the full answer of pass C or `null`, as the model wrote them |
| `flag`, `reason` | the decision |
| `note_conflict` | the spec note that pass C disagrees with, or an empty string |
| `word_count` | the number of words in `ipa` and in the engine output, and `ok`, which is false when they are different |
| `tier` | `llm-corrected` |
| `source_row` | the other columns of the source row |

## Spend

Before it sends a request, the tool prints an estimate and compares it with
`--max-usd`. If the estimate is more than the cap, the tool sends no new
request. The cap applies only to new requests: in batch mode, the tool always
collects the batches that it sent before, because they are already paid for.
It collects the batches that have ended before it makes the estimate.
The estimate is an upper bound:

- It counts one input token for each UTF-8 byte of the prompt, plus 1000
  tokens for each request.
- It counts `--max-tokens` output tokens for each request.
- It counts pass C for each row whose A and B are not known yet.

`--count-tokens` replaces the byte count with the token-counting endpoint of
the API. In `--sync` mode, the tool also stops before a request that can take
the spend of the run past the cap. At the end, the tool prints the tokens and
the cost that the API reported.

The Message Batches API costs half the price of the synchronous API. The tool
uses it unless you give `--sync`.

## Resume

The tool keeps each response in `.silver_correction_cache/`. The key of a
response is the set, the row id, the model and a hash of the request. It also
keeps the ids of the batches that it sent and did not collect. If a run
stops, run the same command again. The tool collects the open batches, uses
the kept responses, and sends only the requests that have no response. Each
kept response also records the file name of the key that served it.

In batch mode, the tool sends pass C for a row when the cache has the A and
B of that row. It does not wait for the batches of other rows, for example a
batch that sends again an A or B that came back unusable. The tool sends each
request at most once in a run. A response that is unusable again waits for
the next run.

## Credentials

Put each API key in its own file. Set `O2I_ANTHROPIC_KEY_FILE` to the paths
of the files, with `:` between them. The file names must be different. If
you have one key, you can set `ANTHROPIC_API_KEY` instead.

The tool divides the work between the keys:

- In `--sync` mode, it sends each request with the next key in the list.
- In batch mode, it divides the rows equally between the keys and sends one
  batch for each key. It collects each batch with the key that sent it.

A key can fail with HTTP 401, 402 or 403, a `billing_error`, or an HTTP 400
about the credit balance. Then the tool does not use that key again in the
run, and it gives the work of that key to the other keys. If no key is left,
the tool stops with exit status 4. The cache keeps each response, so run the
same command again with a key that works.

The tool names a key only by its file name. It does not write the key to the
screen, the log, the cache or the output. A dry run needs no key.

## Run a pilot

Install the extra for the API client:

```bash
uv pip install -e '.[silver-correction]'
```

Write the convention sheets first. Read the estimate with `--dry-run`, then
write the sheets:

```bash
python scripts/correct_silver_ipa.py conventions \
    --lect es-ES pt-PT ar --dry-run
O2I_ANTHROPIC_KEY_FILE=/path/to/first.key:/path/to/second.key \
python scripts/correct_silver_ipa.py conventions \
    --lect es-ES pt-PT ar --max-usd 5
```

Read and correct the three sheets. Then read the estimate of the run. This
command sends no request:

```bash
python scripts/correct_silver_ipa.py \
    --dataset spain_romance_tts portuguese_tts arabic_tts \
    --lect es-ES pt-PT ar --limit 20 --sync --dry-run
```

Then run the pilot with 20 rows for each lect:

```bash
O2I_ANTHROPIC_KEY_FILE=/path/to/first.key:/path/to/second.key \
python scripts/correct_silver_ipa.py \
    --dataset spain_romance_tts portuguese_tts arabic_tts \
    --lect es-ES pt-PT ar --limit 20 --sync --max-usd 50
```

For a full set, remove `--limit` and `--sync`. Add `--no-wait` to send the
batches and exit, then run the same command again to collect them.

---

---
[← The pinned WikiPron mirror](../wikipron_mirror.md) · [Home](../index.md) · [Arabic TTS gold set →](../arabic-tts-gold.md)
