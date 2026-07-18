#!/usr/bin/env python
"""Per-utterance latency benchmark for the TTS front-end path.

o2i runs on ONE utterance at a time before synthesis, so the number that
matters is per-sentence wall time (and its tail), not batch throughput.
This times ``G2P.transcribe`` over realistic, function-word-heavy sentences
of mixed length and reports p50/p95/p99 plus per-word cost.

Run::

    python benchmarks/latency.py            # summary table
    python benchmarks/latency.py --profile  # cProfile the hot language
"""
import argparse
import cProfile
import gc
import pstats
import statistics
import sys
import time

from orthography2ipa import G2P

# Realistic utterances: short commands, mid clauses, long sentences — the
# spread a TTS front-end actually sees, deliberately heavy on repeated
# function words (the, a, de, o, que, and, of...).
CORPUS = {
    "en-GB": [
        "yes",
        "turn off the light",
        "what time is it in London",
        "set a timer for five minutes and remind me later",
        "the quick brown fox jumps over the lazy dog by the river",
        "could you please tell me what the weather is going to be like tomorrow "
        "afternoon in the city and whether i should take an umbrella with me",
    ],
    "pt-PT": [
        "sim",
        "liga a luz da sala",
        "que horas sao agora em Lisboa",
        "marca um alarme para as sete e meia da manha por favor",
        "o gato preto atravessou a rua devagar enquanto o carro passava",
        "podes dizer me como vai estar o tempo amanha de tarde na cidade e se "
        "devo levar um casaco comigo quando sair de casa",
    ],
    "es-ES": [
        "si",
        "apaga la luz de la cocina",
        "que hora es ahora en Madrid",
        "pon una alarma para las siete y media de la manana por favor",
        "el perro corrio por el parque mientras los ninos jugaban con la pelota",
    ],
    "ar": [
        "نعم",
        "أطفئ الضوء من فضلك",
        "كم الساعة الآن في الرياض",
        "اضبط منبها في السابعة والنصف صباحا من فضلك",
        "خرج الولد من البيت ومشى في الشارع الطويل نحو المدرسة في الصباح الباكر",
    ],
}


def _wordcount(sentences):
    return sum(len(s.split()) for s in sentences)


def bench_lang(code, sentences, reps):
    g = G2P(code)
    # warm any lazy spec/tokenizer construction so we time steady state
    for s in sentences:
        g.transcribe(s)

    per_sentence_ms = []
    gc.disable()
    for _ in range(reps):
        for s in sentences:
            t0 = time.perf_counter()
            g.transcribe(s)
            per_sentence_ms.append((time.perf_counter() - t0) * 1e3)
    gc.enable()

    words = _wordcount(sentences) * reps
    total_ms = sum(per_sentence_ms)
    per_sentence_ms.sort()

    def pct(p):
        i = min(len(per_sentence_ms) - 1, int(p * len(per_sentence_ms)))
        return per_sentence_ms[i]

    return {
        "code": code,
        "n": len(per_sentence_ms),
        "p50": statistics.median(per_sentence_ms),
        "p95": pct(0.95),
        "p99": pct(0.99),
        "mean": total_ms / len(per_sentence_ms),
        "per_word_ms": total_ms / words,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reps", type=int, default=30)
    ap.add_argument("--profile", action="store_true")
    ap.add_argument("--lang", default="pt-PT")
    args = ap.parse_args()

    if args.profile:
        g = G2P(args.lang)
        sents = CORPUS[args.lang]
        for s in sents:
            g.transcribe(s)
        pr = cProfile.Profile()
        pr.enable()
        for _ in range(args.reps * 5):
            for s in sents:
                g.transcribe(s)
        pr.disable()
        st = pstats.Stats(pr).sort_stats("cumulative")
        st.print_stats(30)
        return

    rows = [bench_lang(c, s, args.reps) for c, s in CORPUS.items()]
    hdr = f"{'lang':7} {'p50':>8} {'p95':>8} {'p99':>8} {'mean':>8} {'ms/word':>8}"
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        print(f"{r['code']:7} {r['p50']:8.2f} {r['p95']:8.2f} {r['p99']:8.2f} "
              f"{r['mean']:8.2f} {r['per_word_ms']:8.2f}")
    print("\n(ms per utterance; TTS synthesis is typically 50-200ms for reference)")


if __name__ == "__main__":
    sys.exit(main())
