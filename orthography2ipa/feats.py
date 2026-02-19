import math
from collections import defaultdict, Counter

import numpy as np
from phonematcher.distance import vectorize_phones

from orthography2ipa import get
from orthography2ipa.phonetok import PhonetokTokenizer


def phoneme_embeddings(lang_code: str) -> dict[str, np.ndarray]:
    spec = get(lang_code)
    phonemes = {p for ipa_list in spec.graphemes.values() for p in ipa_list}
    embeddings = {}
    for p in phonemes:
        try:
            vec = vectorize_phones(p)
            embeddings[p] = np.array([0.5 if v is None else float(v) for v in vec])
        except ValueError:
            pass
    return embeddings


def build_ngram_lm(words: list[str], lang_code: str, n=3):
    spec = get(lang_code)
    tok = PhonetokTokenizer(spec)

    counts = defaultdict(Counter)
    for word in words:
        paths = tok.ipa_beam(word, beam_width=1)
        if not paths: continue
        phones = ["<s>"] + list(paths[0].ipa) + ["</s>"]
        for i in range(len(phones) - n + 1):
            ctx = tuple(phones[i:i + n - 1])
            counts[ctx][phones[i + n - 1]] += 1
    return counts


def perplexity(lm, test_words, lang_code, n=3):
    spec = get(lang_code)
    tok = PhonetokTokenizer(spec)
    log_prob, total = 0.0, 0
    for word in test_words:
        paths = tok.ipa_beam(word, beam_width=1)
        if not paths: continue
        phones = ["<s>"] + list(paths[0].ipa) + ["</s>"]
        for i in range(n - 1, len(phones)):
            ctx = tuple(phones[i - n + 1:i])
            next_p = phones[i]
            dist = lm.get(ctx, Counter())
            total_ct = sum(dist.values()) + len(dist) + 1  # add-1 smoothing
            p = (dist.get(next_p, 0) + 1) / total_ct
            log_prob += math.log2(p)
            total += 1
    return 2 ** (-log_prob / total) if total > 0 else float('inf')
