"""Ranking-error diagnosis: which slot choice does the beam get wrong?

See docs/ranking_error.md for the method and the resulting cluster tables.

For every word where oracle@k beats top-1, align the top-1 beam path
against the best-scoring top-k path slot by slot and record the
(grapheme, positional context, chosen IPA, better IPA) disagreement.

Usage: PYTHONPATH=. python scripts/rank_diag.py fr 2000
"""
from __future__ import annotations

import collections
import json
import sys
import unicodedata

sys.path.insert(0, "scripts")

from benchmark import (DATASETS, levenshtein, normalize,  # noqa: E402
                       _prosody_marks)

from orthography2ipa import G2P  # noqa: E402
from orthography2ipa.phonetok import flat_contexts  # noqa: E402
from orthography2ipa.positional import (grapheme_positions,  # noqa: E402
                                        positional_candidates)


def diagnose(lang: str, limit: int, k: int = 5, dataset: str = "wikipron"):
    import random
    loader = DATASETS[dataset][0]
    pairs = loader(lang, sys.maxsize)
    if limit and limit < len(pairs):
        random.Random(20260810).shuffle(pairs)
        pairs = pairs[:limit]
    engine = G2P(lang)
    extra = _prosody_marks(lang)
    strip_stress, broad = True, True

    refs = {}
    for w, g in pairs:
        refs.setdefault(w, []).append(g)

    clusters = collections.Counter()
    examples = collections.defaultdict(list)
    n_words = n_rank_fail = 0
    per_sum = orc_sum = 0.0

    for word, golds in refs.items():
        if " " in word:
            continue
        gn = [normalize(x, strip_stress, broad, extra_strip=extra)
              for x in golds]

        def score(h):
            return min(levenshtein(h, g) / max(len(g), 1) for g in gn)

        try:
            paths = engine._positional_beam(word, max(k, 8))
            paths = engine._apply_grammatical_ending(word, paths)
        except Exception:
            continue
        if not paths:
            continue
        fin = []
        for p in paths[:k]:
            s = normalize(
                unicodedata.normalize(
                    "NFC", engine._finalize_word_ipa(word, p.ipa)),
                strip_stress, broad, extra_strip=extra)
            fin.append(s)
        if not fin or not fin[0]:
            continue
        n_words += 1
        top = score(fin[0])
        per_sum += top
        best_i, best = 0, top
        for i, s in enumerate(fin):
            sc = score(s)
            if sc < best:
                best_i, best = i, sc
        orc_sum += best
        if best >= top:
            continue
        n_rank_fail += 1

        # slot-level attribution
        chosen = paths[0].segments
        better = paths[best_i].segments
        g_tokens = engine._tokenizer.grapheme_tokens(word)
        contexts = flat_contexts(g_tokens, engine.spec.vowel_graphemes)
        if len(chosen) != len(better) or len(chosen) != len(contexts):
            clusters["<unaligned>"] += 1
            examples["<unaligned>"].append(word)
            continue
        for idx, (a, b) in enumerate(zip(chosen, better)):
            if a == b:
                continue
            ctx = contexts[idx]
            try:
                positions = grapheme_positions(ctx, spec=engine.spec)
            except Exception:
                positions = ()
            pos_c = positional_candidates(engine.spec, ctx.grapheme, positions)
            src = "positional" if pos_c is not None else "flat"
            key = f"{ctx.grapheme}\t{a}->{b}\t{src}"
            clusters[key] += 1
            if len(examples[key]) < 6:
                examples[key].append(word)

    return {
        "lang": lang,
        "words": n_words,
        "rank_failures": n_rank_fail,
        "per_top1": per_sum / max(n_words, 1),
        "per_oracle": orc_sum / max(n_words, 1),
        "clusters": clusters.most_common(60),
        "examples": {k2: examples[k2] for k2, _ in clusters.most_common(60)},
    }


if __name__ == "__main__":
    lang = sys.argv[1]
    limit = int(sys.argv[2])
    out = diagnose(lang, limit)
    print(json.dumps(out, ensure_ascii=False, indent=1))
