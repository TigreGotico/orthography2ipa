"""What the writing does not say — and admitting it.

An abjad does not write its short vowels. Standard Arabic spells ⟨كتب⟩ and
leaves the reader to decide between *kataba*, *kutiba*, *kutub* and *kattaba* —
the choice is morphological and syntactic, and the letters carry none of it.

The engine has always had to produce *something* for such a word, so it falls
back on a default reading. That is the only sensible thing to do, and it is also
a **guess dressed as an answer**: the output is a confident IPA string with no
signal that the vowels in it were invented. A caller cannot tell a transcription
the orthography determined from one the engine made up.

This module closes that gap. It does not change any transcription and it does
not restore the missing marks — diacritic restoration is a statistical,
morphosyntactic problem that no grapheme table can express, and it belongs to a
diacritizer, not here. What it does is make the *silence* visible:

* :func:`is_underdetermined` — is this word's reading a guess?
* :func:`underdetermined_positions` — exactly which letters the reading invented
  a vowel for;
* :func:`mark_density` — how much of the word the writing actually determines.

:attr:`~orthography2ipa.types.LanguageSpec.script_type` already recorded that an
orthography *is* an abjad, but the fact sat there as inert metadata. Paired with
:attr:`~orthography2ipa.types.LanguageSpec.optional_marks` it becomes
operational.

## Why this is the substrate for diacritization

Restoring the marks is a search: for each underdetermined position, which vowel?
Framed that way it is a **free generation** problem over the whole space of
readings. But the spec already knows which readings a bare letter *licenses* —
that is what the grapheme table is — so the search is really a **path selection**
over a constrained candidate set, which is a far smaller and far safer problem.
A diacritizer that scores licensed candidates cannot invent a reading the
orthography forbids; a diacritizer that generates freely can, and does.

That integration belongs downstream, in the library that knows about both the
diacritizer and the lattice. What belongs *here* is the honest report of where
the ambiguity is.
"""

from __future__ import annotations

from typing import Tuple

from orthography2ipa.types import LanguageSpec, ScriptType

__all__ = [
    "is_underdetermined",
    "underdetermined_positions",
    "mark_density",
]

#: Script types whose orthography habitually omits marks the reading needs.
_UNDERSPECIFYING_SCRIPTS = (ScriptType.ABJAD,)


def _is_letter(ch: str, spec: LanguageSpec) -> bool:
    """True for a base letter — not one of the omissible marks, not punctuation."""
    if ch in spec.optional_marks:
        return False
    return ch.isalpha()


def underdetermined_positions(word: str, spec: LanguageSpec) -> Tuple[int, ...]:
    """Indices of the letters in *word* whose reading the writing does not fix.

    A letter is underdetermined when it carries **none** of the spec's
    :attr:`~orthography2ipa.types.LanguageSpec.optional_marks`: the mark that
    would say which vowel follows it is simply absent, so whatever the engine
    reads there it inferred rather than read.

    Returns an empty tuple for an orthography that writes its vowels, and for a
    fully-marked word — a diacritized Arabic word is *not* underdetermined,
    which is exactly why the Arabic engine's input contract demands one.
    """
    if not spec.optional_marks or spec.script_type not in _UNDERSPECIFYING_SCRIPTS:
        return ()

    marks = set(spec.optional_marks)
    letters = [i for i, ch in enumerate(word) if _is_letter(ch, spec)]
    if not letters:
        return ()
    last_letter = letters[-1]

    positions = []
    for i in letters:
        # The marks that belong to a letter follow it, so look ahead over the
        # run of marks sitting on this letter.
        j = i + 1
        carries_mark = False
        while j < len(word) and word[j] in marks:
            carries_mark = True
            j += 1
        if carries_mark:
            continue

        # A **mater lectionis** needs no mark of its own: ⟨ا⟩ after a fatḥa is
        # the long vowel that fatḥa opened, not a consonant waiting for a vowel.
        # The mark before it is what licenses it, so the reading is determined.
        if i > 0 and word[i - 1] in marks:
            continue

        # The **last letter** needs no mark either: in the pausal form that is
        # actually spoken, a word-final consonant carries no ending. Demanding a
        # mark there would report every correctly-written word as a guess.
        if i == last_letter:
            continue

        positions.append(i)
    return tuple(positions)


def is_underdetermined(word: str, spec: LanguageSpec) -> bool:
    """True when *word*'s reading is, in part, a guess.

    ``True`` for a bare Arabic skeleton and ``False`` for the same word fully
    diacritized — the transcription of the first is inferred, the second read.
    """
    return bool(underdetermined_positions(word, spec))


def mark_density(word: str, spec: LanguageSpec) -> float:
    """The fraction of *word*'s letters the writing actually determines, in
    ``[0, 1]``.

    ``1.0`` for a fully-marked word (and for any orthography that writes its
    vowels — there is nothing left unsaid); ``0.0`` for a bare skeleton.
    Partial marking is common in the wild — a text will mark only the words it
    thinks are ambiguous — so this is a spectrum, not a flag, and it is the
    right thing to threshold on when deciding whether to run a diacritizer.
    """
    if not spec.optional_marks or spec.script_type not in _UNDERSPECIFYING_SCRIPTS:
        return 1.0

    letters = sum(1 for ch in word if _is_letter(ch, spec))
    if not letters:
        return 1.0
    unmarked = len(underdetermined_positions(word, spec))
    return (letters - unmarked) / letters
