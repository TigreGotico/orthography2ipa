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

Scope: both sides, and one rule per side
────────────────────────────────────────
A rule sees the IPA of BOTH words at the boundary and may rewrite either
side (``transform`` for the left word, ``right_transform`` for the right);
:meth:`SandhiEngine.apply` resolves the two sides independently, so at most
one rule fires per side per boundary. Nothing restricts a rule to consonant
edges: VOWEL CONTACT — the deletion or gliding of one of two vowels meeting
across a boundary (Wheeler 2005, *The Phonology of Catalan*, §10.1;
Bonet & Lloret 1998 ch. 5) — is expressed with the same two fields, and the
declared rules of the Catalan branch are the worked example.

Two rules that must never BOTH fire at one boundary are made mutually
exclusive **in their contexts**, not by any precedence the engine knows: if
one deletes a left-word final schwa and the other a right-word initial
vowel, the second declares a left context that excludes schwa, so only one
vowel is ever lost. Likewise a rule guards against emptying a word by
requiring a neighbouring segment in its own pattern (a capture group, or a
lookahead). Contexts are matched against the ORIGINAL words, so a rewrite
cannot feed another rule at the same boundary.

Domain: the prosodic constituent, not the word pair
───────────────────────────────────────────────────
A sandhi rule is defined on a prosodic domain, and no rule reaches outside it
(Nespor & Vogel 1986, *Prosodic Phonology*, for the hierarchy: phonological
word < clitic group < phonological phrase φ < intonational phrase IP <
phonological utterance).

What punctuation writes is the INTONATIONAL PHRASE (IP) break, and that is what
:meth:`SandhiEngine.apply` blocks at, from the pause flags the tokenizer already
computes. Most cross-word rules actually take the smaller φ as their domain, and
φ boundaries also fall clause-internally where nothing is written — so blocking
at IP boundaries is a LOWER BOUND. It is under-restrictive, never
over-restrictive: every IP boundary is also a φ boundary, so no rule that should
fire is blocked here.
"""
from __future__ import annotations

import re
from typing import List, Optional, Sequence, Tuple

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
        pausal: Optional[Sequence[bool]] = None,
    ) -> List[str]:
        """Apply sandhi rules between adjacent words.

        Parameters
        ----------
        words_ipa : list of str
            IPA transcription of each word.
        obligatory_only : bool
            If True, only apply rules marked as obligatory.
        pausal : sequence of bool, optional
            ``pausal[i]`` is True when word *i* stands before a pause — the
            phrase break the tokenizer already read off the punctuation. No
            rule fires at such a boundary. Omitting it treats the word list
            as a single phrase.

        Returns
        -------
        list of str
            Modified IPA word list with sandhi applied.
        """
        # Validate BEFORE the early return: a caller that mismatched the two
        # lists has a bug whether or not the utterance happens to be one word.
        if pausal is not None and len(pausal) != len(words_ipa):
            raise ValueError(
                f"pausal has {len(pausal)} flags for {len(words_ipa)} words"
            )
        if len(words_ipa) <= 1:
            return list(words_ipa)

        result = list(words_ipa)
        for i in range(len(result) - 1):
            # A sandhi rule applies within its prosodic domain; the
            # intonational phrase that punctuation marks is that domain's outer
            # edge (Nespor & Vogel 1986, *Prosodic Phonology*), and nothing
            # joins the two words a pause separates.
            if pausal is not None and pausal[i]:
                continue
            left = result[i]
            right = result[i + 1]
            # The two sides of a boundary are resolved independently: the
            # first matching rule wins *per side*. A left-only rule set (every
            # rule declaring `transform` and no `right_transform` — the shape
            # every spec had before ``right_transform`` existed) therefore still
            # applies exactly one rule per boundary, to the left word.
            # Contexts are always matched against the ORIGINAL words, so the
            # side that fires first cannot mask the other's trigger.
            left_done = right_done = False
            for rule, left_re, right_re in self._compiled:
                if left_done and right_done:
                    break
                if obligatory_only and not rule.obligatory:
                    continue
                if not (left_re.search(left) and right_re.search(right)):
                    continue
                if rule.transform is not None and not left_done:
                    result[i] = left_re.sub(rule.transform, left)
                    left_done = True
                if rule.right_transform is not None and not right_done:
                    result[i + 1] = right_re.sub(rule.right_transform, right)
                    right_done = True
        return result
