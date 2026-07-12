"""stress — Primary word-stress detection and IPA stress marking.

Consumes the declarative :class:`~orthography2ipa.types.StressRules` block
of a :class:`~orthography2ipa.types.LanguageSpec` to locate the stressed
syllable of an orthographic word and to insert the IPA stress mark into a
transcription.

The bundled syllabifier is a naive vowel-group splitter, good enough for
end-anchored stress systems (final / penultimate / antepenultimate).
Languages with a real syllabifier ship it as an
``orthography2ipa.syllabify`` entry-point plugin (``silabificador`` for
Portuguese, ``pycotovia`` for Galician) — pass ``lang=`` and the plugin
is used automatically. Alternatively pass a pre-computed syllable list;
every function accepts one.

Usage
─────
    >>> from orthography2ipa import get
    >>> from orthography2ipa.stress import detect_stress, apply_stress_mark
    >>> rules = get("pt-PT").stress
    >>> detect_stress("falar", rules)     # oxytone: ends in -r
    1
    >>> detect_stress("casa", rules)      # paroxytone default
    0
    >>> apply_stress_mark("fɐlaɾ", rules, -1)
    'fɐˈlaɾ'
"""
from __future__ import annotations

import logging
from typing import List, Optional, Sequence

from orthography2ipa.types import StressRules
from orthography2ipa.vowels import is_ipa_vowel, is_orthographic_vowel

__all__ = [
    "syllabify",
    "detect_stress",
    "apply_stress_mark",
]


def _is_vowel_char(ch: str) -> bool:
    """Vowel test used by the naive syllabifier: orthographic vowels of
    Latin/Greek-script languages (with accented forms) plus IPA vocoids,
    so the same splitter works on spellings and on transcriptions."""
    return is_orthographic_vowel(ch) or is_ipa_vowel(ch)


_GLIDES = set("jw" "ʲʷ")


def _split_nuclei(run: str, diphthongs: Sequence[str]) -> List[str]:
    """Split a vowel *run* into nuclei using the spec's *diphthongs*.

    Greedy longest-first: a run position that starts a listed sequence
    consumes it as ONE nucleus, any other vowel letter is a nucleus of its
    own. With no diphthongs declared the whole run is one nucleus, which is
    the behaviour every spec had before :attr:`StressRules.diphthongs`
    existed.
    """
    if not diphthongs or len(run) < 2:
        return [run]
    ordered = sorted(diphthongs, key=len, reverse=True)
    lowered = run.lower()
    nuclei: List[str] = []
    i = 0
    while i < len(run):
        for diph in ordered:
            if lowered.startswith(diph, i):
                nuclei.append(run[i:i + len(diph)])
                i += len(diph)
                break
        else:
            nuclei.append(run[i])
            i += 1
    return nuclei


def syllabify(
    word: str,
    vowels: Optional[set] = None,
    diphthongs: Sequence[str] = (),
) -> List[str]:
    """Split *word* into syllables by vowel groups.

    Each maximal run of vowel characters becomes a nucleus; consonants
    attach to the following nucleus (onset-maximising), trailing
    consonants to the last syllable. This is intentionally naive — it
    exists to *count* end-anchored syllables, not to draw perfect
    boundaries.

    *diphthongs* (a spec's :attr:`~orthography2ipa.types.StressRules.diphthongs`)
    splits a vowel run into several nuclei wherever the orthography writes
    hiatus rather than a diphthong — Catalan ``tenia`` is te-ni-a, and the
    syllable count decides where stress (and the vowel reduction it
    conditions) lands. Empty = merge each run into one nucleus, unchanged.
    """
    is_vowel_char = (lambda c: c.lower() in vowels) if vowels is not None else _is_vowel_char
    if not word:
        return []
    if diphthongs:
        return _syllabify_with_diphthongs(word, is_vowel_char, diphthongs)
    # indices of nucleus starts
    syllables: List[str] = []
    current = ""
    in_nucleus = False
    for ch in word:
        is_vowel = is_vowel_char(ch)
        if is_vowel and not in_nucleus and current and any(
                is_vowel_char(c) for c in current):
            # a new nucleus after the previous syllable already has one:
            # close the syllable before this consonant-less transition
            syllables.append(current)
            current = ch
        elif not is_vowel and in_nucleus:
            # first consonant after a nucleus: close the syllable here so
            # the consonant opens the next one (onset-maximising)
            syllables.append(current)
            current = ch
        else:
            current += ch
        in_nucleus = is_vowel
    if current:
        if any(is_vowel_char(c) for c in current) or not syllables:
            syllables.append(current)
        else:
            # trailing consonant cluster joins the last syllable
            syllables[-1] += current
    return syllables


def _syllabify_with_diphthongs(
    word: str,
    is_vowel_char,
    diphthongs: Sequence[str],
) -> List[str]:
    """:func:`syllabify` with a vowel run split into nuclei by *diphthongs*.

    Onset-maximising exactly like the plain splitter: a whole consonant run
    opens the syllable of the nucleus that follows it, a trailing consonant
    run joins the last syllable, and only the run→nuclei step differs.
    """
    syllables: List[str] = []
    onset = ""
    i = 0
    while i < len(word):
        if not is_vowel_char(word[i]):
            onset += word[i]
            i += 1
            continue
        j = i
        while j < len(word) and is_vowel_char(word[j]):
            j += 1
        for k, nucleus in enumerate(_split_nuclei(word[i:j], diphthongs)):
            syllables.append((onset if k == 0 else "") + nucleus)
        onset = ""
        i = j
    if onset:
        if syllables:
            syllables[-1] += onset
        else:
            syllables.append(onset)
    return syllables


def _syllables_for(
    word: str,
    lang: Optional[str],
    diphthongs: Sequence[str] = (),
) -> List[str]:
    """Syllabify *word*: registered plugin for *lang* first, naive fallback.

    *diphthongs* reaches the bundled splitter only; a language that ships a
    real syllabifier plugin does not need it.
    """
    if lang:
        from orthography2ipa.registry import get_syllabifier
        plugin = get_syllabifier(lang)
        if plugin is not None:
            try:
                sylls = plugin.syllabify(word, lang)
                if sylls and "".join(sylls) == word:
                    return list(sylls)
            except Exception as exc:
                logging.getLogger(__name__).warning(
                    "syllabifier plugin %r failed on word %r: %s",
                    type(plugin).__name__, word, exc)
    return syllabify(word, diphthongs=diphthongs)


def detect_stress(
    word: str,
    rules: StressRules,
    syllables: Optional[Sequence[str]] = None,
    lang: Optional[str] = None,
) -> int:
    """Return the 0-based index of the stressed syllable of *word*.

    Precedence: written accents (``rules.marked_vowels``) →
    ``final_stress_endings`` → ``penult_stress_endings`` →
    ``rules.default_position``. Monosyllables are inherently stressed.

    Parameters
    ----------
    word : str
        Orthographic word (lowercased internally for ending checks).
    rules : StressRules
        The language's declarative stress system.
    syllables : Optional[Sequence[str]]
        Pre-computed syllables; takes precedence over plugin lookup.
    lang : Optional[str]
        Language code used to look up a registered
        ``orthography2ipa.syllabify`` plugin (``silabificador`` for
        Portuguese, ``pycotovia`` for Galician). The naive
        :func:`syllabify` is the fallback.
    """
    sylls = (list(syllables) if syllables is not None
             else _syllables_for(word, lang, rules.diphthongs))
    n = len(sylls)
    if n <= 1:
        return 0

    # 1. written accent overrides everything
    if rules.marked_vowels:
        marked = set(rules.marked_vowels)
        for idx, syllable in enumerate(sylls):
            if any(ch in marked for ch in syllable):
                return idx

    lowered = word.lower()

    # 2. oxytone endings — longest first so '-im' wins over '-m'
    for ending in sorted(rules.final_stress_endings, key=len, reverse=True):
        if lowered.endswith(ending):
            return n - 1

    # 3. forced paroxytone endings
    for ending in sorted(rules.penult_stress_endings, key=len, reverse=True):
        if lowered.endswith(ending):
            return n - 2

    # 4. default position, clamped into the word.
    #    Positive values anchor from the start (1 = first syllable).
    #    Negative values anchor from the end (existing behaviour).
    pos = rules.default_position
    if pos >= 1:
        return min(pos - 1, n - 1)
    return max(0, n + pos)


def apply_stress_mark(
    ipa: str,
    rules: StressRules,
    stress_index: int,
    syllables: Optional[Sequence[str]] = None,
) -> str:
    """Insert ``rules.stress_mark`` before the stressed syllable of *ipa*.

    Parameters
    ----------
    ipa : str
        A single word's IPA transcription (no spaces).
    rules : StressRules
        Supplies the mark character.
    stress_index : int
        Stressed syllable index. A non-negative value is interpreted
        over the *orthographic* syllable count and converted to an
        end-anchored offset, which is robust when the IPA syllable
        count differs (elided/silent vowels). A negative value is used
        as the end-anchored offset directly (``-1`` final syllable).
    syllables : Optional[Sequence[str]]
        Pre-computed orthographic syllables matching *stress_index*;
        needed only for non-negative ``stress_index`` conversion.

    Already-marked transcriptions are returned unchanged.
    """
    if rules.stress_mark in ipa:
        return ipa
    ipa_sylls = syllabify(ipa)
    if not ipa_sylls:
        return ipa

    if stress_index < 0:
        offset_from_end = -stress_index
    else:
        n_orth = len(syllables) if syllables is not None else len(ipa_sylls)
        offset_from_end = max(1, n_orth - stress_index)

    target = max(0, len(ipa_sylls) - offset_from_end)
    ipa_sylls[target] = rules.stress_mark + ipa_sylls[target]
    return "".join(ipa_sylls)
