# Gold corrections overlays

Each file here repairs a defect in an upstream gold set without touching the
upstream file, which stays byte-identical. One JSONL row per corrected gold
entry:

| field | meaning |
|---|---|
| `dataset` | the upstream gold set the correction applies to |
| `lang` | the language tag of the upstream row |
| `spelling` | the orthographic word, matched exactly against upstream |
| `original_reading` | the reading upstream shipped, matched exactly |
| `corrected_reading` | the reading the overlay substitutes |
| `reason` | what is wrong with the original reading |
| `authority` | the orthographic fact or the citation the correction rests on |

A correction may be derived only from the orthography of the word or from a
fetched citation, never from what orthography2ipa outputs. The overlaid gold is
registered as its own benchmark dataset so the uncorrected row stays on the
board beside it, and it can never gate a quality promotion. See
"Corrections overlays" in `docs/benchmarks.md` for the full rules.

Regenerate with:

    PYTHONPATH=. python scripts/build_gold_corrections.py

## `vox_communis_vi.jsonl`

The VoxCommunis Vietnamese phone tier writes the same Chao tone letter ˨˨ for
*ngang* and *huyền*, merging two contrastive tones. Vietnamese orthography
writes huyền with a combining grave accent, so the merged rows are separable
from the spelling alone; the substituted ˧˩ follows Kirby (2011: 386), who
labels huyền "mid falling" against hỏi's "low falling". 401 rows corrected,
7 left uncorrected and reported by the build.

## `portuguese_unified_pt.jsonl`

This overlay corrects rows of the Portuguese unified pronunciation lexicon
(`TigreGotico/portuguese-unified-pronunciation-lexicon`). The file is keyed on
the source row of the dataset, not on an o2i language tag, so any consumer of
the dataset can apply the same rows. Its fields differ from the table above:

| field | meaning |
|---|---|
| `dataset` | always `portuguese_unified` |
| `source` | `infopedia`, `wiktionary`, `infopedia+wiktionary` or `portal`, read from the row's fields |
| `region` | the dataset's region tag, for example `pt-PT-x-lisboa` |
| `word`, `pos` | the headword and the part of speech of the row |
| `field` | `ipa_narrow` or `ipa_broad` |
| `original_reading` | the reading the row ships, matched exactly |
| `corrected_reading` | the reading to use; `null` drops the row |
| `kind` | `accent_contradiction`, `unaccented_stress`, `missing_mark`, `wrong_headword` or `mojibake` |
| `reason`, `authority` | what is wrong, and the orthographic fact or the fetched citation |

A correction moves or adds the primary stress mark, drops a variant, or drops
a row. It changes no segment. The written accent, or the accent rules of the
Acordo Ortográfico 1990, settles each stressed syllable. A row is dropped when
its reading transcribes another headword (*tração* rows that read *seleto*),
or when it ends in mis-encoded text. A mark goes only on a vowel that the
stressed letter can spell. A row that also needs a segment fix stays
uncorrected.

The narrow field has 539 corrections: 79 accent contradictions, 24 unaccented
words stressed against the accent rules, 337 missing marks, 48 rows or
variants of another headword, and 51 rows with mis-encoded text. The broad
field has 441 corrections that follow the narrow ones.
