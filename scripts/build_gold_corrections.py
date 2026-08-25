#!/usr/bin/env python3
"""Regenerate the committed gold-correction overlays.

An OVERLAY is a small, separately committed file that repairs a defect in an
upstream gold set without touching the upstream file: one row per corrected
gold entry, recording the spelling, the reading the upstream gold shipped, the
reading the overlay substitutes, the reason, and the authority the correction
rests on. ``scripts/benchmark.py`` registers the overlaid gold as its OWN
dataset, so the original row and the corrected row both stay on the board and
the correction's effect is visible as the difference between them.

THE RULE THAT MAKES AN OVERLAY HONEST: a correction may be derived ONLY from
the orthography of the word or from a fetched citation. It may NEVER be derived
from what orthography2ipa itself outputs. A gold repaired with this project's
own answers would score beautifully and measure nothing. Nothing in this file
imports orthography2ipa, and nothing in it may start.

Currently one overlay:

``vox_communis`` / ``vi`` — the upstream phone tier merges two contrastive
Vietnamese tones. It writes the identical Chao tone letter ˨˨ for both *ngang*
(A1, the unmarked tone) and *huyền* (A2). Kirby (2011: 386) tabulates them as
separate categories on the minimal pair ⟨ma⟩ 'ghost' (ngang, "level") versus
⟨mà⟩ 'but, yet' (huyền, "mid falling"); the two are the classic Vietnamese
tone minimal pair, so a gold that spells them alike has lost a phonemic
contrast, not chosen a notation.

The repair is derivable from spelling alone because Vietnamese orthography
writes huyền with a COMBINING GRAVE ACCENT (U+0300) over the syllable nucleus —
à è ì ò ù ỳ and their circumflex/breve/horn variants — and writes ngang with no
tone mark at all. Which of the two merged tones a syllable carries is therefore
recoverable from the Unicode combining marks of the spelling, with no
phonological model in the loop. ``vi_tone_from_spelling`` below reads exactly
those marks.

The substituted value is ˧˩. Kirby prints tone letters rather than Chao
digits, and labels huyền "mid falling" against hỏi's "low falling"
(2011: 386), so huyền must start above hỏi's register: ˧ (mid) falling to ˩.
The upstream gold's own ngang is ˨˨ and its hỏi is ˨˩˨, so ˧˩ is distinct from
every tone-letter sequence already in the file.

    Kirby, James P. (2011). Vietnamese (Hanoi Vietnamese). Journal of the
    International Phonetic Association 41(3): 381-392.
    https://doi.org/10.1017/S0025100311000181

Usage::

    PYTHONPATH=. python scripts/build_gold_corrections.py

Rewrites every file under ``orthography2ipa/data/gold/corrections/``. The build
is deterministic: rerunning it on an unchanged upstream cache reproduces the
committed bytes.
"""
import json
import os
import re
import sys
import unicodedata
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

CORRECTIONS_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..",
    "orthography2ipa", "data", "gold", "corrections",
)

#: The five Vietnamese tone marks, as Unicode combining characters, mapped to
#: the traditional tone names. An unmarked syllable is *ngang*. These are the
#: ONLY diacritics that carry tone: the circumflex (U+0302), breve (U+0306) and
#: horn (U+031B) of ⟨â ê ô ă ơ ư⟩ are vowel-quality marks and are ignored here.
VI_TONE_MARKS = {
    "̀": "huyen",   # grave       à
    "̉": "hoi",     # hook above  ả
    "̃": "nga",     # tilde       ã
    "́": "sac",     # acute       á
    "̣": "nang",    # dot below   ạ
}

#: Chao tone letters and the glottalisation/creak marks that ride with them,
#: as used by the VoxCommunis Vietnamese phone tier.
TONE_LETTERS = re.compile("[˥-˩̰̃ˀʼ]+")

VI_NGANG_READING = "˨˨"     # ˨˨ — what the upstream gold writes
VI_HUYEN_READING = "˧˩"     # ˧˩ — Kirby 2011:386, "mid falling"

VI_TONE_REASON = (
    "upstream phone tier writes the ngang tone letter ˨˨ on a "
    "syllable spelled with the huyen grave accent, merging two contrastive "
    "tones; replaced with the huyen tone letters ˧˩"
)
VI_TONE_AUTHORITY = (
    "Vietnamese orthography (huyen is written U+0300 COMBINING GRAVE ACCENT) "
    "+ Kirby, James P. (2011), Vietnamese (Hanoi Vietnamese), JIPA 41(3): "
    "381-392, tone table p. 386 (ngang A1 'level' ma vs huyen A2 "
    "'mid falling' mà), https://doi.org/10.1017/S0025100311000181"
)


def vi_tone_from_spelling(word: str) -> Optional[str]:
    """The tone of a Vietnamese syllable, read off its combining marks.

    Returns a name from :data:`VI_TONE_MARKS`, ``"ngang"`` for an unmarked
    syllable, or ``None`` when the spelling carries more than one tone mark —
    a multi-syllable token, where no single tone can be assigned and the row
    must be left uncorrected.

    Orthography only. No phonology, no lexicon, and above all no o2i.
    """
    marks = [VI_TONE_MARKS[c] for c in unicodedata.normalize("NFD", word)
             if c in VI_TONE_MARKS]
    if not marks:
        return "ngang"
    if len(marks) == 1:
        return marks[0]
    return None


def build_vi_tone_rows(pairs: List[Tuple[str, str]]) -> Tuple[List[Dict], Dict[str, int]]:
    """Overlay rows for the VoxCommunis Vietnamese tone merge, plus the counts
    of everything deliberately left alone.

    A row is corrected only when BOTH of these hold, and skipped and counted
    otherwise:

    * the spelling carries exactly one tone mark and it is the huyen grave;
    * the gold reading's tone-letter sequence is exactly ˨˨, i.e. it is a
      single-syllable reading that actually shows the merge.

    A grave-accented spelling whose reading is NOT ˨˨ is not evidence of the
    merge and gets no correction, whatever it is. This is the negative-result
    bucket and it is reported, never silently dropped.
    """
    rows: List[Dict] = []
    stats = {
        "corrected": 0,
        "huyen_reading_not_ngang": 0,
        "tone_undeterminable": 0,
        "not_huyen": 0,
    }
    for word, reading in pairs:
        tone = vi_tone_from_spelling(word)
        if tone is None:
            stats["tone_undeterminable"] += 1
            continue
        if tone != "huyen":
            stats["not_huyen"] += 1
            continue
        if "".join(TONE_LETTERS.findall(reading)) != VI_NGANG_READING:
            stats["huyen_reading_not_ngang"] += 1
            continue
        rows.append({
            "dataset": "vox_communis",
            "lang": "vi",
            "spelling": word,
            "original_reading": reading,
            "corrected_reading": reading.replace(
                VI_NGANG_READING, VI_HUYEN_READING),
            "reason": VI_TONE_REASON,
            "authority": VI_TONE_AUTHORITY,
        })
        stats["corrected"] += 1
    rows.sort(key=lambda r: (r["spelling"], r["original_reading"]))
    return rows, stats


def write_overlay(name: str, rows: List[Dict]) -> str:
    os.makedirs(CORRECTIONS_DIR, exist_ok=True)
    path = os.path.join(CORRECTIONS_DIR, f"{name}.jsonl")
    with open(path, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    return path


def main() -> None:
    import benchmark  # the BASE gold loader only; never the o2i engine

    pairs = benchmark.load_vox_communis("vi", sys.maxsize)
    rows, stats = build_vi_tone_rows(pairs)
    path = write_overlay("vox_communis_vi", rows)
    print(f"read {len(pairs)} upstream pairs")
    for key, value in sorted(stats.items()):
        print(f"  {key}: {value}")
    print(f"wrote {len(rows)} rows to {os.path.relpath(path, os.getcwd())}")


if __name__ == "__main__":
    main()
