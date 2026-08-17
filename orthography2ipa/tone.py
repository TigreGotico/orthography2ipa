"""Tone-mark placement.

A tone mark is a property of the whole syllable, and IPA writes it at the
syllable edge — after the rime, not in the middle of it. Orthographies
that mark tone with a diacritic on the nucleus letter therefore produce
tone in the wrong slot when a grapheme table is read left to right: the
Khiamniungan spelling ⟨ōng⟩ maps ⟨ō⟩ to a mid-tone vowel and ⟨ng⟩ to a
coda nasal, which concatenates to ``o³³ŋ`` where the transcription is
``oŋ³³``.

:func:`dock_tone_marks` moves each tone mark to the end of its syllable.
It is stated over the universal IPA tone symbols and a maximal-onset
syllable division, so it consults no language, script or code, and specs
whose orthography puts the mark where it is pronounced (Yi, Zhuang) leave
it off.
"""

from __future__ import annotations

from typing import List, Sequence

from .allophony import segment_ipa
from .vowels import is_ipa_vowel

__all__ = ["TONE_MARKS", "dock_tone_marks"]

#: The IPA tone symbols: Chao pitch numerals and Chao tone letters.
TONE_MARKS = frozenset("¹²³⁴⁵˥˦˧˨˩")


def _is_nucleus(seg: str) -> bool:
    """Whether *seg* can continue a nucleus: a vocoid, or a mark on one."""
    return is_ipa_vowel(seg[0]) or not seg[0].isalpha()


def dock_tone_marks(ipa: str, atoms: Sequence[str] = ()) -> str:
    """Move every tone mark in *ipa* to the end of the syllable it belongs to.

    The syllable a mark belongs to is the one whose nucleus it follows.
    Its end is found by maximal onset: the offglides that continue the
    nucleus stay with it, and of the consonants that follow, the last one
    is the next syllable's onset whenever another vowel comes after it.
    *atoms* are the multi-character phonemes of the language (affricates,
    aspirates), so that ``ts`` is one onset and not a coda ``t`` plus an
    onset ``s``.

    A mark already at a syllable end is left where it is, so the function
    is idempotent.
    """
    if not ipa or not any(ch in TONE_MARKS for ch in ipa):
        return ipa
    atoms = sorted(atoms, key=len, reverse=True)
    out: List[str] = []
    i, n = 0, len(ipa)
    while i < n:
        if ipa[i] not in TONE_MARKS:
            out.append(ipa[i])
            i += 1
            continue
        j = i
        while j < n and ipa[j] in TONE_MARKS:
            j += 1
        tone = ipa[i:j]
        # Window up to the next tone mark: everything the current
        # syllable could still claim.
        t = j
        while t < n and ipa[t] not in TONE_MARKS:
            t += 1
        segs = segment_ipa(ipa[j:t], atoms)
        if segs and t < n and all(_is_nucleus(s) for s in segs):
            # Nothing but another tone-bearing nucleus follows: this
            # syllable ended at the mark (hiatus).
            out.append(tone)
            i = j
            continue
        k = 0
        while k < len(segs) and _is_nucleus(segs[k]):
            k += 1                      # offglides finish the nucleus
        c = k
        while c < len(segs) and not _is_nucleus(segs[c]):
            c += 1                      # the consonants after the rime
        if c < len(segs) and c > k:
            c -= 1                      # the last one is the next onset
        coda = "".join(segs[:c])
        out.append(coda)
        out.append(tone)
        i = j + len(coda)
    return "".join(out)
