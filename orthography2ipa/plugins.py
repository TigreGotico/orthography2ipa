"""The sandhi contract, and the stage names that discovery used.

The transcription is a function of the spec, the input and the caller's explicit
configuration. It is never a function of what is installed. So a caller passes
each step to one engine as an object, in a :class:`~orthography2ipa.pipeline.Pipeline`::

    G2P("ar", pipeline=Pipeline(mark=diacritize, sandhi=MySandhi()))

Another engine in the process does not see these steps.

:class:`SandhiPlugin` is the contract for ``Pipeline(sandhi=...)``. It gets the IPA,
the spelling and the pause flag of each word, which a cross-word rule needs, and it
returns one IPA string per word.

The other names here served discovery by entry point. The spec field ``plugins``
and the deprecated ``G2P(plugins=...)`` name a plugin by its entry-point name, and
the engine finds it in the group of its stage. A named plugin that is not installed
raises :class:`~orthography2ipa.registry.MissingPlugin`, and the engine never falls
back to the built-in answer.

:class:`NormalizePlugin`, ``STAGES``, ``OUTPUT_CHANGING_STAGES`` and
``ENTRY_POINT_GROUPS`` are deprecated, and go in the next major release together
with that discovery. Each one warns when a caller reads it, and a subclass of
``NormalizePlugin`` warns when it is defined.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Sequence

from orthography2ipa.lexicon import _warn_deprecated

__all__ = [
    "NormalizePlugin",
    "SandhiPlugin",
    "STAGES",
    "OUTPUT_CHANGING_STAGES",
    "ENTRY_POINT_GROUPS",
]

_STAGES = ("normalize", "syllabify", "stress", "rescore", "sandhi")

#: entry-point group per stage. ``syllabify`` has none: the caller passes a
#: syllabifier as an object.
_ENTRY_POINT_GROUPS: Dict[str, str] = {
    stage: f"orthography2ipa.{stage}" for stage in _STAGES if stage != "syllabify"
}

#: Deprecated module constants, each with what replaces it.
_DEPRECATED_CONSTANTS = {
    "STAGES": (_STAGES, "the fields of Pipeline"),
    "OUTPUT_CHANGING_STAGES": (_STAGES, "the fields of Pipeline"),
    "ENTRY_POINT_GROUPS": (_ENTRY_POINT_GROUPS, "the fields of Pipeline"),
}


def __getattr__(name: str):
    if name in _DEPRECATED_CONSTANTS:
        value, replacement = _DEPRECATED_CONSTANTS[name]
        _warn_deprecated(name, replacement)
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


class NormalizePlugin(ABC):
    """Deprecated: decides what the input *is*, canonically, before anything reads it.

    A subclass warns when it is defined. Pass the step in
    ``Pipeline(expand=...)`` or ``Pipeline(mark=...)``.

    The step that runs before the engine sees a single grapheme, and the one with
    the most leverage: diacritic restoration for an abjad, number and date
    expansion, orthographic normalisation. Arabic is the motivating case — the
    engine's contract is diacritized text and real text is not diacritized, so
    something has to put the vowels back, and that something is a model.

    It changes the transcription completely (it changes the *word*), so the spec
    must name it. A library that quietly diacritized your text differently
    depending on what you had installed would be unusable.
    """

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        # The frames are this method, ABCMeta.__new__ and the class statement.
        _warn_deprecated("NormalizePlugin", "Pipeline(expand=...) or Pipeline(mark=...)",
                         stacklevel=4)

    @abstractmethod
    def normalize(self, text: str, lang: str) -> str:
        """Return *text* in the form the engine's spec expects."""

    @property
    @abstractmethod
    def language_codes(self) -> List[str]:
        """BCP-47 codes this plugin speaks for, and only these."""


class SandhiPlugin(ABC):
    """What happens between words.

    Some of the most audible phonology is not a property of a word at all, but of
    a word *next to another word*, and no word-level engine can see it: a final
    /n/ that assimilates to the next onset (Arabic مِنْ رَبِّهِمْ is *mir
    rabbihim*), a case ending that a pause removes, a French liaison, an elided
    article vowel.

    The spec's own ``sandhi_rules`` cover the regular cases. This is for the ones
    that need code — arbtok's cross-word layer is the worked example, and it
    currently lives downstream where this library cannot see it.
    """

    @abstractmethod
    def apply(
        self,
        words: Sequence[str],
        surfaces: Sequence[str],
        pausal: Sequence[bool],
        lang: str,
    ) -> List[str]:
        """Rewrite the IPA of each word, given its neighbours.

        Args:
            words: each word's IPA, in order.
            surfaces: each word's orthographic form, aligned with *words*. The
                spelling is not redundant: whether a word ends in a case ending is
                a fact about the page, and guessing it from the last characters of
                the IPA confuses an ending with a stem — the ``-in`` of قَاضٍ is an
                ending and the ``-in`` of مُؤْمِن is the word.
            pausal: whether each word stands before a pause — punctuation, or the
                end of the utterance. This has to be given, not inferred: the
                engine strips punctuation during word splitting, so by the time a
                plugin sees the words the pause is *gone from the input*, and a
                pause is precisely what removes a case ending.
            lang: the resolved code.

        The IPA may already carry a stress mark: stress is placed per word, before
        this runs. A plugin matching on the shape of a word must account for that
        — ``ˈmin`` is still *min*.

        Returns a list of the same length. A plugin that returns a different
        length has rewritten the sentence, not its sandhi.
        """

    @property
    def language_codes(self) -> List[str]:
        """BCP-47 codes this plugin speaks for. The engine does not read them."""
        return []
