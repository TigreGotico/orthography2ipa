"""Lattice plugins: an external tool contributing phonology to one language.

A syllabifier answers a question the engine already asks, and answers it better.
A **rescorer** does something categorically different: it changes what the engine
*says*. That is its entire purpose — a rescorer exists to make ⟨ِي⟩ read as a
consonant before a vowel, to back /a/ next to an emphatic, to assimilate the lām
of the article into a sun letter.

So the two cannot share a contract. "Installing this must not change the output"
is the whole point of a syllabifier plugin and the exact opposite of the point of
a rescorer plugin, and pretending both are just "plugins" is how the extension
system stopped making sense.

## The contract for phonology

A rescorer plugin may change the transcription. What it may **not** do:

1. **Speak for a language it did not claim.** A Portuguese rescorer must be
   invisible to Arabic. This is not politeness; a rescorer is a rule about a
   phonology, and a phonology belongs to a language.
2. **Emit a symbol outside the spec's inventory.** This is the hard one, and it
   is why :mod:`orthography2ipa.inventory` exists. A TTS frontend builds its
   embedding table from the declared phoneme inventory *before* training; a
   rescorer that invents a symbol at inference time produces a token with no
   embedding, and the word carrying it is mispronounced permanently and silently.
   A plugin that needs a new symbol must say so **in the spec**, where it can be
   read, cited and diffed — not smuggle it in at runtime.
3. **Be non-deterministic.** Same input, same output, every time. A transcription
   that varies run to run is not a transcription.

Those three are checkable, and :func:`~orthography2ipa.conformance.assert_rescorer_conforms`
checks them.

## Why this is the right extension point

The engine already has one — :class:`~orthography2ipa.rescorer.LatticeRescorer` —
and it is already how the hard languages get done: arbtok layers sun-letter
assimilation, hamzat al-waṣl and the accusative alif onto the shared lattice as
rescorers, because those are Arabic morpho-phonology that no grapheme table can
express.

But arbtok has to *construct* that chain itself, because there is no way to
*register* one. So the knowledge lives in a downstream package that o2i cannot
see, and a language expert who is not writing a whole engine has nowhere to put a
single rule. This closes that gap: contribute the rule, claim the language, pass
the conformance kit.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Sequence

from orthography2ipa.rescorer import LatticeRescorer

__all__ = ["RescorerPlugin"]


class RescorerPlugin(ABC):
    """Contributes lattice rescorers — phonology — for one or more languages."""

    @abstractmethod
    def rescorers(self, lang: str) -> Sequence[LatticeRescorer]:
        """The rescorers this plugin contributes for *lang*, in application order.

        Called only for a code in :attr:`language_codes`. Return an empty sequence
        to contribute nothing for a particular variety.
        """

    @property
    @abstractmethod
    def language_codes(self) -> List[str]:
        """BCP-47 codes this plugin speaks for, and only these."""

    @property
    def priority(self) -> int:
        """Order among plugins claiming the same code. Higher runs later, so a
        higher-priority plugin sees the lower one's work — realization is a
        cascade, not a competition, and the last word wins."""
        return 50
