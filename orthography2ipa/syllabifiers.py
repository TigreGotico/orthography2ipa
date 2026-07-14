"""Syllabifier plugins that ship with orthography2ipa.

The bundled splitter counts nuclei; it does not draw boundaries a phonologist
would sign off on. That is enough for the end-anchored stress systems it exists
to serve, and it is not enough for everything.

So a language may supply a real one. This module holds the plugins
orthography2ipa itself can offer when the underlying package is present —
installed via an extra, never a hard dependency, because a G2P library has no
business pulling a Portuguese syllabifier into an Arabic install::

    pip install orthography2ipa[portuguese]

## What a syllabifier is allowed to change, and what it is not

A plugin supplies **syllables**. It does not supply stress.

That distinction matters more than it looks. Stress here is declarative — it
comes from the spec's :class:`~orthography2ipa.types.StressRules`, which is data
a language owner wrote and can be read, cited and diffed. If a plugin could also
place the stress, then installing an optional package would change the
transcription, and the same word would have two answers depending on what
happened to be in the environment. That is not hypothetical: it is the bug this
library just had, and the syllable count was how it got in.

``silabificador`` *does* compute stress (2.x), and on its own 500-word held-out
gold its answer agrees with the spec's declarative rules on **every word**. So
nothing is lost by not asking it — and what is gained is that the answer does not
depend on whether it is installed.
"""

from __future__ import annotations

from typing import List, Optional

from orthography2ipa.syllabifier_plugin import SyllabifierPlugin

__all__ = ["SilabificadorSyllabifier"]


class SilabificadorSyllabifier(SyllabifierPlugin):
    """Portuguese syllables from ``silabificador``, a rule-based phonotactic
    syllabifier.

    Optional: ``pip install orthography2ipa[portuguese]``. When the package is
    absent this plugin fails to load and discovery simply carries on without it,
    which is why the bundled splitter must still be right on its own — see
    ``pt-PT``'s declared ``diphthongs``.
    """

    def __init__(self) -> None:
        from silabificador import Syllabifier  # raises if not installed
        self._syllabifier = Syllabifier()

    def syllabify(self, word: str, lang: Optional[str] = None) -> List[str]:
        return self._syllabifier.syllabify(word)

    @property
    def language_codes(self) -> List[str]:
        return [
            "pt", "pt-PT", "pt-BR", "pt-AO", "pt-MZ", "pt-TL",
            "pt-CV", "pt-GW", "pt-ST", "pt-MO", "pt-UY",
        ]

    @property
    def priority(self) -> int:
        # Neutral. A downstream plugin that knows better should win by saying so.
        return 50
