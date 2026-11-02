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

## How the tool decides a row

Each row gets up to three passes. Every pass returns JSON that matches a
schema.

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
| `ipa` | the corrected IPA |
| `ipa_llm_original` | the `ipa` of the source row |
| `ipa_engine` | the engine output for the sentence |
| `model` | the model that wrote the passes |
| `passes` | the IPA of pass A and pass B, and the full answer of pass C or `null` |
| `flag`, `reason` | the decision |
| `note_conflict` | the spec note that pass C disagrees with, or an empty string |
| `tier` | `llm-corrected` |
| `source_row` | the other columns of the source row |

## Spend

Before it sends a request, the tool prints an estimate and compares it with
`--max-usd`. If the estimate is more than the cap, the tool does not start.
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

Read the estimate first. This command sends no request:

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
    --lect es-ES pt-PT ar --limit 20 --sync --max-usd 40
```

For a full set, remove `--limit` and `--sync`. Add `--no-wait` to send the
batches and exit, then run the same command again to collect them.

---

---
[← The pinned WikiPron mirror](../wikipron_mirror.md) · [Home](../index.md) · [Arabic TTS gold set →](../arabic-tts-gold.md)
