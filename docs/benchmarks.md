# Benchmarks

How the G2P engine is evaluated: which gold pronunciation datasets are
used, where they come from, and the reference numbers the bundled
harness produces. Run any row yourself with
[`scripts/benchmark.py`](../scripts/benchmark.py):

```bash
python scripts/benchmark.py --dataset portuguese_lexicon --lang pt-PT
python scripts/benchmark.py --list
```

## Provenance discipline

A gold set is only usable for evaluation when its transcriptions come
from humans. Many public "G2P datasets" are generated with espeak-ng or
phonemizer wrappers — scoring against those measures agreement with
another rule engine, not correctness. Every dataset below is selected
for human or community provenance; anything tool-generated is excluded
on principle.

## Datasets

### Portal da Língua Portuguesa lexicon

Per-region IPA for ~617k Portuguese entries, scraped from the
INESC-ID [Portal da Língua Portuguesa](https://www.portaldalinguaportuguesa.org/)
and published as
[TigreGotico/portuguese_phonetic_lexicon](https://huggingface.co/datasets/TigreGotico/portuguese_phonetic_lexicon)
on Hugging Face. The harness loads it through
[tugalex](https://github.com/TigreGotico/tugalex), the lexicon library
that wraps this dataset; one region maps to each language tag (Lisbon →
`pt-PT`, Rio de Janeiro → `pt-BR`, Luanda → `pt-AO`, Maputo → `pt-MZ`,
Díli → `pt-TL`). Lexicographer-curated; the strongest gold available
for Portuguese and the only one with regional coverage.

### WikiPron

Word/IPA pairs mined from Wiktionary by
[CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)
(Lee et al. 2020, *WikiPron: Mining Wiktionary for Massively
Multilingual Pronunciation Data*, LREC). Community-curated by Wiktionary
editors — reliable where the editor community is large; the broad-
transcription TSVs are used. Note the gold carries **multiple valid
transcriptions per word** (dialect variants such as Galician
seseo/gheada); the harness scores against all of them and keeps the
best match.

### CMU Pronouncing Dictionary

[cmudict](https://github.com/cmusphinx/cmudict): ~134k American English
entries hand-curated by the CMU Speech Group. ARPABET, converted to IPA
via [scriptconv](https://github.com/TigreGotico/scriptconv). English
orthography is deeply irregular, so this row is a floor for a
rule-driven engine, reported for honesty rather than flattery.

### Mirandese gold set

[TigreGotico/mirandese_g2p](https://huggingface.co/datasets/TigreGotico/mirandese_g2p)
on Hugging Face: ~220 word/IPA rows with a dialect column (central,
raiano, sendinese), collected by a native Mirandese speaker
([MdMV](https://commons.wikimedia.org/wiki/User:MdMV_or_Emdy_idk)).
Native-speaker provenance makes it the reference gold for Mirandese;
its size keeps results indicative rather than statistical.

## Methodology

- **PER** — character-level Levenshtein distance over IPA, divided by
  reference length; mean over evaluated words. **WER** — fraction of
  words with any error.
- **Multi-reference**: rows are grouped by word and a hypothesis is
  scored against every gold variant, keeping the minimum PER.
- **Segmentation-free**: whitespace is removed before comparison (some
  gold sets space-separate phonemes).
- **Default normalization**: stress marks and narrow-transcription
  apparatus (raising/dentality diacritics, syllable separators, tie
  bars) are stripped from both sides — gold sets differ in
  transcription depth, and the engine should not be scored on notation
  conventions. `--keep-stress` / `--narrow` disable this.
- Runs are capped at 300 words by default — gold sets are alphabetical,
  so treat single-slice numbers as reference points, not leaderboard
  entries.

## Reference numbers

`python scripts/benchmark.py --dataset <d> --lang <l> --limit 300`:

| Dataset | Lang | N | PER | WER |
|---|---|---:|---:|---:|
| portuguese_lexicon | pt-PT | 300 | 0.167 | 0.73 |
| portuguese_lexicon | pt-MZ | 300 | 0.288 | 0.86 |
| portuguese_lexicon | pt-AO | 300 | 0.398 | 1.00 |
| portuguese_lexicon | pt-BR | 300 | 0.420 | 1.00 |
| portuguese_lexicon | pt-TL | 300 | 0.487 | 1.00 |
| wikipron | gl | 264 | 0.073 | 0.37 |
| wikipron | es | 298 | 0.100 | 0.52 |
| wikipron | pt | 243 | 0.190 | 0.71 |
| wikipron | pt-BR | 125 | 0.328 | 0.99 |
| mirandese | mwl | 205 | 0.230 | 0.76 |
| mirandese | mwl-x-sendim | 11 | 0.553 | 0.82 |
| cmudict | en-US | 300 | 0.612 | 0.98 |

Reading the table: languages whose specs carry positional grapheme
rules and stress blocks (gl, es, pt-PT, mwl) score far better than
those without — the engine consults
`positional_graphemes`/`stress` whenever a spec provides them, so the
per-language path to a better number is richer spec data, not engine
changes. The pt-BR/pt-AO/pt-TL rows lack positional vowel-reduction
blocks; the en-US row reflects English orthography itself.

## Agreement with espeak-ng

[`scripts/espeak_agreement.py`](../scripts/espeak_agreement.py) compares
this engine's output against espeak-ng on the same word lists. This is
**not an accuracy benchmark** — espeak is not a gold standard. It
answers a deployment question: a TTS model trained on espeak
phonemization maps phoneme symbols to embedding IDs, so replacing its
front-end requires symbol-level compatibility, not correctness.

Signals: **exact** (identical transcription), **exact-nostress**
(identical after stress-mark removal — espeak places stress inside the
syllable, this engine before it), **segmental** (mean character
similarity, stress-stripped), and **oov-rate** — the fraction of words
whose transcription contains a symbol espeak never emits for that
voice. Out-of-inventory symbols become unknown embedding IDs, so
oov-rate is the hard-failure signal; the offending symbols are listed
per run.

`python scripts/espeak_agreement.py --lang <l> --limit 300`:

| Lang | Voice | exact | exact-nostress | segmental | oov-rate | main OOV symbols |
|---|---|---:|---:|---:|---:|---|
| es | es | 0.05 | 0.55 | 0.92 | 0.00 | — |
| pt-PT | pt | 0.00 | 0.12 | 0.78 | 0.04 | s̺ apical mark, precomposed ã |
| pt-BR | pt-br | 0.00 | 0.02 | 0.71 | 0.37 | s̺, tie bar, ʎ, ʁ |
| en | en-gb | 0.00 | 0.04 | 0.51 | 0.84 | æ |

Reading the table: stress-mark placement alone rules out byte-exact
replacement everywhere; segmental similarity shows how close the phone
sequences are; the oov column decides deployability. A near-zero
oov-rate (Spanish) means a symbol-mapping shim suffices; a high one
(English — espeak-ng writes the TRAP vowel as ⟨a⟩ where this engine
emits ⟨æ⟩) means a per-symbol translation table must be built and
validated before any swap.

