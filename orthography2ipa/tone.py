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

from typing import List, Optional, Sequence

from .allophony import segment_ipa
from .vowels import is_ipa_vowel

__all__ = ["TONE_MARKS", "dock_tone_marks", "assign_computed_tones"]

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


# ═══════════════════════════════════════════════════════════════════════════
# Computed tone — tone spelled by the syllable's SHAPE, not by a diacritic
# ═══════════════════════════════════════════════════════════════════════════


def _syllable_slots(segments: Sequence[str]) -> List[List[int]]:
    """Group slot indices into syllables by maximal onset over SLOTS.

    A slot whose IPA holds a vocoid is a nucleus. Of the consonant slots
    between two nuclei the last one opens the following syllable and the
    rest close the preceding one — maximal onset counted in slots, so a
    slot that already spells a cluster (⟨กร⟩ ``kr``) stays one onset.
    Slots that spell nothing (a tone mark, a cancellation sign) carry no
    segment; they ride the syllable of the slot they are written on,
    which is the nearest one to their left.
    """
    nuclei = [i for i, seg in enumerate(segments)
              if any(is_ipa_vowel(ch) for ch in seg)]
    if not nuclei:
        return []
    sylls: List[List[int]] = [[] for _ in nuclei]
    prev = 0
    for n, idx in enumerate(nuclei):
        between = list(range(prev, idx))
        if n == 0:
            sylls[0] = between + [idx]
        elif segments[idx] and not is_ipa_vowel(segments[idx][0]):
            # This slot spells its own onset — a consonant read with its
            # inherent vowel, or one that absorbed a preposed vowel sign.
            # It takes nothing from the consonants before it, and they
            # all close the syllable before.
            sylls[n - 1] += between
            sylls[n] = [idx]
        else:
            spelling = [i for i in between if segments[i]]
            # The onset is the last slot before the nucleus that spells
            # something. Everything from the onset onward opens this
            # syllable, INCLUDING the slots after it that spell nothing:
            # a tone mark is written on the initial consonant, so it sits
            # between that consonant and the vowel sign that follows it,
            # and it names the tone of the syllable that consonant opens.
            # Handing it to the syllable before instead put ⟨เป็นต้อง⟩'s
            # mai tho on ⟨เป็น⟩ and read the pair /peːn˥˩tɔːŋ˧/ with the
            # two tones swapped.
            cut = spelling[-1] if spelling else idx
            sylls[n - 1] += [i for i in between if i < cut]
            sylls[n] = [i for i in between if i >= cut] + [idx]
        prev = idx + 1
    sylls[-1] += list(range(prev, len(segments)))
    return sylls


def _rime(ipa: str, atoms: Sequence[str], dead_codas: Sequence[str]
          ) -> Optional[tuple]:
    """``(nucleus_end_offset, long_vowel, dead)`` for one syllable's IPA.

    The nucleus is the first maximal run of vocoids; everything after it
    is the coda. A syllable is *dead* when its coda opens with one of the
    spec's ``dead_codas`` (the obstruents that check a syllable), or when
    it has no coda and its nucleus is short. Length is read off the IPA
    length mark, so it is a property of the transcription rather than of
    the spelling.
    """
    segs = segment_ipa(ipa, tuple(atoms))
    i = 0
    while i < len(segs) and not is_ipa_vowel(segs[i][0]):
        i += 1
    if i == len(segs):
        return None
    j = i
    while j < len(segs) and is_ipa_vowel(segs[j][0]):
        j += 1
    nucleus = "".join(segs[i:j])
    coda = "".join(segs[j:])
    long_vowel = "ː" in nucleus
    if coda:
        dead = any(coda.startswith(c) for c in dead_codas)
    else:
        dead = not long_vowel
    return len("".join(segs[:j])), long_vowel, dead


def assign_computed_tones(graphemes: Sequence[str], segments: Sequence[str],
                          rules, atoms: Sequence[str] = ()) -> str:
    """Write each syllable's tone into *segments*, per the spec's tone rules.

    Some orthographies do not spell tone with a tone letter at all: they
    spell it with the SHAPE of the syllable — the class its initial
    consonant belongs to, whether the rime is checked, how long the vowel
    is, and which of the tone marks (if any) rides the initial. Thai and
    the other Tai orthographies are the clear case. The tone of such a
    syllable is not in any one grapheme, so no grapheme table can carry
    it and :func:`dock_tone_marks` has nothing to move; it has to be
    computed from the syllable once the syllable exists.

    *graphemes* and *segments* are the parallel per-slot arrays of one
    reading: the grapheme key each slot matched, and the IPA it produced
    (``""`` for a slot that spells no segment). The tone letter is
    appended at the end of its syllable, where IPA writes it; a spec
    whose transcription convention puts it on the nucleus instead reads
    it back with :func:`dock_tone_marks`.

    Every fact consulted — which letters belong to which class, which
    marks exist, which codas check a syllable, and the class × shape ×
    mark table itself — comes from *rules*, so this function names no
    language and no script.
    """
    sylls = _syllable_slots(segments)
    if not sylls:
        # Nothing with a nucleus to carry a tone — a bare consonant
        # letter, a spelling the tables read as silent. The reading is
        # returned untouched rather than rebuilt from no syllables.
        return "".join(segments)
    out: List[str] = []
    for syl in sylls:
        ipa = "".join(segments[i] for i in syl)
        tone = _syllable_tone([graphemes[i] for i in syl], ipa, rules, atoms)
        out.append(ipa + tone if tone else ipa)
    return "".join(out)


def _syllable_tone(graphemes: Sequence[str], ipa: str, rules,
                   atoms: Sequence[str]) -> str:
    """The tone letter one syllable's spelling calls for, or ``""``."""
    cls = None
    for grapheme in graphemes:
        for ch in grapheme:
            if ch in rules.classes:
                cls = rules.classes[ch]
                break
        if cls is not None:
            break
    if cls is None or cls not in rules.table:
        return ""
    mark = rules.no_mark
    for grapheme in graphemes:
        for ch in grapheme:
            if ch in rules.marks:
                mark = rules.marks[ch]
    rime = _rime(ipa, atoms, rules.dead_codas)
    if rime is None:
        return ""
    _end, long_vowel, dead = rime
    shape = ("dead_long" if long_vowel else "dead_short") if dead else "live"
    by_shape = rules.table[cls]
    tone = by_shape.get(shape, {}).get(mark)
    if tone is None:
        tone = by_shape.get("any", {}).get(mark)
    return rules.tones.get(tone, "") if tone else ""
