"""Independent recompute of the th.json tone-accuracy note.

Fetches the full WikiPron th gold TSV directly (the same source
``scripts/benchmark.py`` uses), transcribes every headword with the
current th spec, and restricts to the rows whose tone-stripped
transcription matches the tone-stripped gold exactly (a whole-word
metric would blame a single wrong syllable's tone for every OTHER
syllable in the word too). Within that subset it walks the two IPA
strings syllable by syllable — a syllable being everything up to and
including its trailing Chao tone letter, which is where both WikiPron
and the docked engine output write it — and counts how many syllables
carry the same tone letter in both.

Usage: python3 scripts/recompute_th_tone_accuracy.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, "scripts")
from benchmark import load_wikipron  # noqa: E402

from orthography2ipa import transcribe  # noqa: E402
from orthography2ipa.tone import TONE_MARKS  # noqa: E402

_TONE_RUN = "[" + "".join(TONE_MARKS) + "]+"
_SYLLABLE = re.compile(r".+?" + _TONE_RUN)


def strip_tone(ipa: str) -> str:
    return "".join(ch for ch in ipa if ch not in TONE_MARKS)


def syllables(ipa: str):
    """Split *ipa* into (segment, tone) chunks at each trailing tone run."""
    out = []
    for m in _SYLLABLE.finditer(ipa):
        chunk = m.group()
        tone = "".join(ch for ch in chunk if ch in TONE_MARKS)
        out.append((chunk[:len(chunk) - len(tone)], tone))
    return out


def main() -> None:
    pairs = load_wikipron("th", sys.maxsize)

    syllables_compared = 0
    tone_matches = 0
    for word, gold in pairs:
        gold = unicodedata.normalize("NFC", gold.replace(" ", ""))
        try:
            pred = transcribe(word, "th")
        except Exception:
            continue
        pred = unicodedata.normalize("NFC", pred)
        if strip_tone(pred) != strip_tone(gold):
            continue
        gold_sylls = syllables(gold)
        pred_sylls = syllables(pred)
        if len(gold_sylls) != len(pred_sylls):
            # Same segmentals, different tone-mark COUNT (a tone landed
            # on the wrong side of a syllable boundary): every syllable
            # in this word is uncertain, so skip the row rather than
            # zip mismatched syllables together.
            continue
        if [g for g, _ in gold_sylls] != [p for p, _ in pred_sylls]:
            continue
        for (gseg, gtone), (pseg, ptone) in zip(gold_sylls, pred_sylls):
            syllables_compared += 1
            if gtone == ptone:
                tone_matches += 1

    print(f"WikiPron th rows fetched: {len(pairs)}")
    print(f"syllables compared (segmentally exact rows only): "
          f"{syllables_compared}")
    print(f"of those, tone also matches gold: {tone_matches}")
    pct = (100.0 * tone_matches / syllables_compared
           if syllables_compared else 0.0)
    print(f"{tone_matches} of {syllables_compared} = {pct:.1f}%")


if __name__ == "__main__":
    main()
