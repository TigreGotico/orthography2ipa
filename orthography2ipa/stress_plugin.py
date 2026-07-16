"""Stress plugins — and the rule that makes any output-changing plugin safe.

A stress plugin breaks the tidy story. A syllabifier must not change the
transcription; a rescorer exists to change it. Where does stress go? It *changes*
the transcription — it adds a mark, and it moves the vowel reduction that stress
conditions — so by that split it looks like a rescorer. But letting an installed
package decide where the stress falls is **exactly** the bug this library just
had: `coelho` was ˈkuɐʎu with a plugin installed and ˈkoɐʎu without.

So "does it change the output?" is the wrong axis. The right one is:

    **The transcription is a function of the SPEC and the INPUT.
    Never of the environment.**

That single rule subsumes both cases and settles this one:

* A plugin that **does not** change the transcription may be installed freely.
  It is a pure refinement — better syllable boundaries, same answer. (Nothing
  needs to declare it, because nothing downstream can tell.)
* A plugin that **does** change the transcription must be **named by the spec**.
  Then the output is still determined by the spec plus the input, and *installing
  something* is no longer a silent switch.
* And if the spec names a plugin that is not installed, that is an **error** — not
  a silent fallback to some other answer. A silent fallback is how you get two
  transcriptions for one word and no way to know which you got.

## So: how a stress plugin fits

The spec opts in. ``StressRules.source`` is ``"rules"`` by default — stress comes
from the declarative block, which is data a language owner wrote and anyone can
read, cite and diff. A spec that sets ``source: "plugin"`` is saying *this
language's stress is not expressible as end-anchored endings or syllable weight,
and here is the tool that knows*. o2i then requires one, and says so loudly if it
is missing.

Nothing installs its way into changing a transcription.

## Worth knowing before reaching for one

``silabificador`` computes Portuguese stress (2.x), and on its own 500-word
held-out gold it agrees with o2i's declarative rules on **every word**. So for
Portuguese a stress plugin would be a no-op, which is the best possible reason to
have built the mechanism: the first thing it proves is that it changes nothing.

Reach for it where the declarative model genuinely cannot reach — lexical stress
that is not predictable from the orthography at all (Russian), or stress that
needs morphology.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional, Sequence

__all__ = ["StressPlugin"]


class StressPlugin(ABC):
    """Decides which syllable carries primary stress, for the languages it claims.

    Only consulted when the spec asks for it (``StressRules.source == "plugin"``).
    """

    @abstractmethod
    def stressed_index(
        self,
        word: str,
        syllables: Sequence[str],
        lang: str,
    ) -> Optional[int]:
        """Index of the stressed syllable in *syllables*, or ``None`` if unsure.

        ``None`` means *I do not know*, and the engine falls back to the spec's
        declarative rules. It does not mean *unstressed*. A plugin that guesses
        rather than abstaining is worse than no plugin, because a wrong stress
        moves every reduction the stress conditions.
        """

    @property
    @abstractmethod
    def language_codes(self) -> List[str]:
        """BCP-47 codes this plugin speaks for, and only these."""

    @property
    def priority(self) -> int:
        """Highest wins, for a code claimed by several plugins."""
        return 50
