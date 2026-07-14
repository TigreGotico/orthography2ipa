"""The pluggable steps, and the one declaration that makes them safe.

The pipeline has clearly-defined steps, and each is a place a language expert
could plausibly beat the built-in answer:

===============  ===================================================  ===========
stage            the question it answers                              contract
===============  ===================================================  ===========
``normalize``    what IS the input, canonically?                      declared
``syllabify``    where are the syllable boundaries?                   **neutral**
``stress``       which syllable carries it?                           declared
``rescore``      which allophone surfaces here?                       declared
``sandhi``       what happens between words?                          declared
===============  ===================================================  ===========

Four of them change the transcription. One does not. That difference is the whole
design, and it comes from a single rule:

    **The transcription is a function of the SPEC and the INPUT.
    Never of the environment.**

So:

* **``syllabify`` is neutral.** A better syllabifier draws better boundaries and
  reaches the *same answer*; nothing downstream can tell it was installed. It
  needs no declaration, and it is checked by
  :func:`~orthography2ipa.conformance.assert_syllabifier_conforms`, which fails if
  installing it moves the output. (If it does move the output, the built-in answer
  is wrong — that is how ``coelho`` was found.)

* **The other four are declared.** They change what the engine says, so the spec
  must *name* the plugin it wants. Then the output still depends only on the spec
  and the input, and installing a package is no longer a silent switch::

      "plugins": {
        "normalize": "text2tashkeel",
        "sandhi": "arbtok-sandhi"
      }

* **A declared plugin that is missing is an ERROR.** Never a quiet fallback to
  some other answer. A quiet fallback is how you get two transcriptions for one
  word and no way to know which one you got.

## Who selects a plugin — the spec, or the caller?

Both, and the difference matters.

The danger was never *"a plugin changed the output"*. It was ***"pip install*
changed the output"** — a transcription that silently depends on what happened to
be in the environment. An **explicit** choice by the caller is not that. It is a
declaration, made in code, that anyone reading the call site can see.

So there are exactly two ways an output-changing plugin gets selected, and
discovery alone is never one of them:

1. **The spec names it** — for a plugin that is intrinsic to how the language is
   defined, shipped with the data, the default for everyone::

       "plugins": {"sandhi": "arbtok"}

2. **The caller names it** — which overrides the spec::

       G2P("ar", plugins={"normalize": "text2tashkeel"})

The second is how a downstream engine works, and it is the normal case. **arbtok**
is not editing orthography2ipa's shipped ``ar.json`` to announce that it wants a
diacritizer; it passes one, at construction, because *it* is the thing that
decided. Likewise a lexicon, a POS tagger, a diacritizer — a rich engine composes
the steps it wants and says so in code.

And note what that means for orthography2ipa's own contract: the ``ar`` spec must
**not** name a diacritizer, because this library's input contract *is* diacritized
text and it ships no weights. The spec describes the language; the engine decides
the pipeline. A spec should only name a plugin when the language is not
transcribable without it.

A plugin is identified by its **entry-point name**, which is what the spec or the
caller names. That makes the declaration readable and greppable, and it means two
packages cannot fight over a language — something already said which one it
wanted.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Sequence

__all__ = [
    "NormalizePlugin",
    "SandhiPlugin",
    "STAGES",
    "OUTPUT_CHANGING_STAGES",
    "ENTRY_POINT_GROUPS",
]

#: Every pluggable stage.
STAGES = ("normalize", "syllabify", "stress", "rescore", "sandhi")

#: The stages that change the transcription — and must therefore be named by the
#: spec. ``syllabify`` is absent on purpose: it is a refinement, not a decision.
OUTPUT_CHANGING_STAGES = ("normalize", "stress", "rescore", "sandhi")

#: entry-point group per stage.
ENTRY_POINT_GROUPS: Dict[str, str] = {
    stage: f"orthography2ipa.{stage}" for stage in STAGES
}


class NormalizePlugin(ABC):
    """Decides what the input *is*, canonically, before anything reads it.

    The step that runs before the engine sees a single grapheme, and the one with
    the most leverage: diacritic restoration for an abjad, number and date
    expansion, orthographic normalisation. Arabic is the motivating case — the
    engine's contract is diacritized text and real text is not diacritized, so
    something has to put the vowels back, and that something is a model.

    It changes the transcription completely (it changes the *word*), so the spec
    must name it. A library that quietly diacritized your text differently
    depending on what you had installed would be unusable.
    """

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
        lang: str,
    ) -> List[str]:
        """Rewrite the IPA of each word, given its neighbours.

        Args:
            words: each word's IPA, in order.
            surfaces: each word's orthographic form, aligned with *words*. The
                spelling is not redundant: whether a word ends in a case ending is
                a fact about the page, and guessing it from the last characters of
                the IPA confuses an ending with a stem.
            lang: the resolved code.

        Returns a list of the same length. A plugin that returns a different
        length has rewritten the sentence, not its sandhi.
        """

    @property
    @abstractmethod
    def language_codes(self) -> List[str]:
        """BCP-47 codes this plugin speaks for, and only these."""
