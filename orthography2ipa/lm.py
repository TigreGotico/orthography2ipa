"""Language-model utilities for IPA phoneme sequences.

Separated from feats.py to keep the distinctive-feature module focused
on phonetic feature vectors and segment-level distance computation.

Functions
---------
build_ngram_lm   Build an n-gram language model over IPA phone sequences.
perplexity       Evaluate perplexity of a test word list under a phone LM.
phoneme_embeddings  Return feature-vector embeddings for a language's phonemes.
"""
from __future__ import annotations

import math
from collections import defaultdict, Counter

import numpy as np

from orthography2ipa.feats import vectorize_phones
from orthography2ipa.phonetok import PhonetokTokenizer
from orthography2ipa.types import LanguageSpec


def phoneme_embeddings(spec: LanguageSpec) -> dict[str, np.ndarray]:
    """Return a dict mapping each phoneme in *spec* to its 21-feature vector.

    Unknown phonemes (those not in the feature table) are silently skipped.

    Parameters
    ----------
    spec : LanguageSpec
        The language specification whose grapheme→IPA mapping is used
        to collect the phoneme set.

    Returns
    -------
    dict[str, np.ndarray]
        Phoneme string → 21-dim float array (None features become 0.5).
    """
    phonemes = {p for ipa_list in spec.graphemes.values() for p in ipa_list}
    embeddings = {}
    for p in phonemes:
        try:
            vec = vectorize_phones(p)
            embeddings[p] = np.array([0.5 if v is None else float(v) for v in vec])
        except ValueError:
            pass
    return embeddings


def build_ngram_lm(words: list[str], spec: LanguageSpec, n: int = 3) -> dict:
    """Build an n-gram count table over IPA phone sequences.

    Parameters
    ----------
    words : list[str]
        Orthographic word list to phonemize and index.
    spec : LanguageSpec
        Language specification used for tokenization.
    n : int
        N-gram order (default 3 = trigram).

    Returns
    -------
    dict[tuple[str, ...], Counter]
        Mapping from (n-1)-gram context to a Counter of next phones.
    """
    tok = PhonetokTokenizer(spec)
    counts: dict = defaultdict(Counter)
    for word in words:
        paths = tok.ipa_beam(word, beam_width=1)
        if not paths:
            continue
        phones = ["<s>"] + list(paths[0].ipa) + ["</s>"]
        for i in range(len(phones) - n + 1):
            ctx = tuple(phones[i:i + n - 1])
            counts[ctx][phones[i + n - 1]] += 1
    return counts


def perplexity(lm: dict, test_words: list[str], spec: LanguageSpec, n: int = 3) -> float:
    """Compute perplexity of *test_words* under the phone n-gram *lm*.

    Uses add-1 (Laplace) smoothing.

    Parameters
    ----------
    lm : dict
        N-gram count table from :func:`build_ngram_lm`.
    test_words : list[str]
        Orthographic words to evaluate.
    spec : LanguageSpec
        Language specification used for tokenization.
    n : int
        N-gram order matching *lm* (default 3).

    Returns
    -------
    float
        Perplexity score (lower = better fit). Returns ``inf`` if no
        tokens were found.
    """
    tok = PhonetokTokenizer(spec)
    log_prob, total = 0.0, 0
    for word in test_words:
        paths = tok.ipa_beam(word, beam_width=1)
        if not paths:
            continue
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
