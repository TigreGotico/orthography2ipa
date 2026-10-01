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
