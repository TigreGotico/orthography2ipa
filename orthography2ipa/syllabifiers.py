"""Syllabifier plugins that ship with orthography2ipa.

The bundled splitter counts nuclei; it does not draw boundaries a phonologist
would sign off on. That is enough for the end-anchored stress systems it exists
to serve, and it is not enough for everything.

So a caller may supply a real one. This module holds the plugins
orthography2ipa itself can offer when the underlying package is present —
installed via an extra, never a hard dependency, because a G2P library has no
business pulling a Portuguese syllabifier into an Arabic install::

    pip install orthography2ipa[portuguese]

Installing the extra changes no transcription. The caller builds the plugin and
passes it to one engine::

    G2P("pt-PT", pipeline=Pipeline(syllabifier=SilabificadorSyllabifier()))

## What a syllabifier supplies

A plugin supplies **syllables**. It does not supply stress.

Stress here is declarative — it comes from the spec's
:class:`~orthography2ipa.types.StressRules`, which is data a language owner wrote
and can be read, cited and diffed. The syllable count still reaches the stress
step, so a syllabifier can move the output of the engine it was passed to.

``silabificador`` *does* compute stress (2.x), and on its own 500-word held-out
gold its answer agrees with the spec's declarative rules on **every word**. So
nothing is lost by not asking it.
"""

from __future__ import annotations

from typing import List, Optional

from orthography2ipa.syllabifier_plugin import SyllabifierPlugin

__all__ = ["SilabificadorSyllabifier"]


class SilabificadorSyllabifier(SyllabifierPlugin):
    """Portuguese syllables from ``silabificador``, a rule-based phonotactic
    syllabifier.

    Optional: ``pip install orthography2ipa[portuguese]``. Building it raises
    :class:`ModuleNotFoundError` when the package is absent. An engine that gets
    no syllabifier uses the bundled splitter, which must be right on its own —
    see ``pt-PT``'s declared ``diphthongs``.
    """

    def __init__(self) -> None:
        from silabificador import Syllabifier  # raises if not installed
        self._syllabifier = Syllabifier()

    def syllabify(self, word: str, lang: Optional[str] = None) -> List[str]:
        return self._syllabifier.syllabify(word)

    @property
    def language_codes(self) -> List[str]:
        # The regional pt-BR specs read the pt-BR grapheme table
        # (graphemes_base), so they take the pt-BR syllables with it.
        return [
            "pt", "pt-PT", "pt-BR", "pt-AO", "pt-MZ", "pt-TL",
            "pt-CV", "pt-GW", "pt-ST", "pt-MO", "pt-UY",
            "pt-BR-x-bahia", "pt-BR-x-caipira", "pt-BR-x-ce",
            "pt-BR-x-cuiaba", "pt-BR-x-floripa", "pt-BR-x-fluminen",
            "pt-BR-x-mg", "pt-BR-x-norte", "pt-BR-x-pr", "pt-BR-x-recife",
            "pt-BR-x-rj", "pt-BR-x-sp", "pt-BR-x-sul",
        ]
