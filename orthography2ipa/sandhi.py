"""sandhi — Cross-word-boundary phonological rule engine.

Applies sandhi and liaison rules across word boundaries in an IPA
token stream.  Rules are defined per-language as ``SandhiRule`` objects
on the ``LanguageSpec.sandhi_rules`` field and loaded from JSON.

Usage
─────
    >>> from orthography2ipa.sandhi import SandhiEngine
    >>> from orthography2ipa.types import SandhiRule
    >>> rules = (SandhiRule(
    ...     id="FR_LIAISON_Z", name="z-liaison",
    ...     left_context=r"z$", right_context=r"^[aeiou]",
    ...     transform="z‿",
    ... ),)
    >>> engine = SandhiEngine(rules)
    >>> engine.apply(["lez", "ami"])
    ['lez‿', 'ami']
"""
from __future__ import annotations

import re
from typing import List, Tuple

from orthography2ipa.types import SandhiRule

__all__ = [
    "SandhiEngine",
]


class SandhiEngine:
    """Applies sandhi rules across word boundaries in a token stream."""

    def __init__(self, rules: Tuple[SandhiRule, ...]) -> None:
        self.rules = rules
        # Pre-compile regexes
        self._compiled: List[Tuple[SandhiRule, re.Pattern, re.Pattern]] = []
        for rule in rules:
            left_re = re.compile(rule.left_context)
            right_re = re.compile(rule.right_context)
            self._compiled.append((rule, left_re, right_re))

    def apply(
        self,
        words_ipa: List[str],
        *,
        obligatory_only: bool = False,
    ) -> List[str]:
        """Apply sandhi rules between adjacent words.

        Parameters
        ----------
        words_ipa : list of str
            IPA transcription of each word.
        obligatory_only : bool
            If True, only apply rules marked as obligatory.

        Returns
        -------
        list of str
            Modified IPA word list with sandhi applied.
        """
        if len(words_ipa) <= 1:
            return list(words_ipa)

        result = list(words_ipa)
        for i in range(len(result) - 1):
            left = result[i]
            right = result[i + 1]
            for rule, left_re, right_re in self._compiled:
                if obligatory_only and not rule.obligatory:
                    continue
                if left_re.search(left) and right_re.search(right):
                    result[i] = left_re.sub(rule.transform, left)
                    break  # first matching rule wins per boundary
        return result
