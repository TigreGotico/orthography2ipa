"""stress — Primary word-stress detection and IPA stress marking.

Consumes the declarative :class:`~orthography2ipa.types.StressRules` block
of a :class:`~orthography2ipa.types.LanguageSpec` to locate the stressed
syllable of an orthographic word and to insert the IPA stress mark into a
transcription.

The bundled syllabifier is a naive vowel-group splitter, good enough for
end-anchored stress systems (final / penultimate / antepenultimate).
Consumers with a real syllabifier (e.g. ``silabificador`` for Portuguese)
should pass their own syllable list — every function accepts one.

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

from typing import List, Optional, Sequence

from orthography2ipa.types import StressRules

__all__ = [
    "syllabify",
    "detect_stress",
    "apply_stress_mark",
]

# Vowel characters recognised by the naive syllabifier: orthographic vowels
# of Latin-script languages (with their accented forms) plus IPA vocoids,
# so the same splitter works on spellings and on transcriptions.
_VOWELS = set(
    "aeiou"
    "áéíóúàèìòùâêîôûãõäëïöüåæø"
    "ɐɑɒɔəɘɚɛɜɝɞɪɨɵøœɶʊʉʌyɤeiou̯ãẽĩõũɐ̃"
)
_GLIDES = set("jw" "ʲʷ")


def syllabify(word: str, vowels: Optional[set] = None) -> List[str]:
    """Split *word* into syllables by vowel groups.

    Each maximal run of vowel characters becomes a nucleus; consonants
    attach to the following nucleus (onset-maximising), trailing
    consonants to the last syllable. This is intentionally naive — it
    exists to *count* end-anchored syllables, not to draw perfect
    boundaries.
    """
    vowels = vowels if vowels is not None else _VOWELS
    if not word:
        return []
    # indices of nucleus starts
    syllables: List[str] = []
    current = ""
    in_nucleus = False
    for ch in word:
        is_vowel = ch.lower() in vowels
        if is_vowel and not in_nucleus and current and any(
                c.lower() in vowels for c in current):
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
        if any(c.lower() in vowels for c in current) or not syllables:
            syllables.append(current)
        else:
            # trailing consonant cluster joins the last syllable
            syllables[-1] += current
    return syllables


def detect_stress(
    word: str,
    rules: StressRules,
    syllables: Optional[Sequence[str]] = None,
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
        Pre-computed syllables; the naive :func:`syllabify` is used
        when omitted.
    """
    sylls = list(syllables) if syllables is not None else syllabify(word)
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

    # 4. default position, clamped into the word
    return max(0, n + rules.default_position)


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
