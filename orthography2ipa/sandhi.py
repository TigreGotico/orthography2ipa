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

Spelling conditions
───────────────────
A rule may also name ``left_spelling`` and ``right_spelling``, regexes on the
written form of each word, for words whose IPA is the same and whose sandhi
differs: French ⟨cent⟩ and ⟨sang⟩ are both [sɑ̃], and only ⟨cent ans⟩ links
with [t]. The caller passes the spellings to :meth:`SandhiEngine.apply`:

    >>> rule = SandhiRule(id="FR_CENT_T", name="cent ans", left_context=r"$",
    ...                   right_context=r"^ɑ̃$", transform="t‿", left_spelling=r"^cent$")
    >>> SandhiEngine((rule,)).apply(["sɑ̃", "ɑ̃"], spellings=["cent", "ans"])
    ['sɑ̃t‿', 'ɑ̃']
    >>> SandhiEngine((rule,)).apply(["sɑ̃", "ɑ̃"], spellings=["sang", "ans"])
    ['sɑ̃', 'ɑ̃']

``left_joined_spelling`` and ``right_joined_spelling`` read the joined
spelling, which adds the word before and a hyphen when a hyphen joins the two
(``quatre-vingt`` for the ⟨vingt⟩ of ⟨quatre-vingt-deux⟩). A rule with a
spelling condition does not fire when the caller passes no spellings.

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
        self._compiled: List[Tuple[SandhiRule, re.Pattern, re.Pattern, Tuple[Optional[re.Pattern], ...]]] = []
        for rule in rules:
            left_re = re.compile(rule.left_context)
            right_re = re.compile(rule.right_context)
            spelled = tuple(None if text is None else re.compile(text) for text in (
                rule.left_spelling, rule.left_joined_spelling,
                rule.right_spelling, rule.right_joined_spelling))
            self._compiled.append((rule, left_re, right_re, spelled))

    def apply(
        self,
        words_ipa: List[str],
        *,
        obligatory_only: bool = False,
        pausal: Optional[Sequence[bool]] = None,
        spellings: Optional[Sequence[str]] = None,
        joined_spellings: Optional[Sequence[str]] = None,
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
        spellings : sequence of str, optional
            ``spellings[i]`` is the casefolded spelling of word *i*, which the
            ``left_spelling`` and ``right_spelling`` conditions read.
        joined_spellings : sequence of str, optional
            ``joined_spellings[i]`` is the joined spelling of word *i*, which
            the ``*_joined_spelling`` conditions read: the word before, ``-``
            and the word, when a hyphen joins them, else the spelling alone.
            Omitted, it is *spellings*, as for a text with no hyphen.

            A rule with a spelling condition never fires when the spelling it
            reads is not passed. A spec whose spelling-free rules must still
            run then keeps its spelling conditions in rules of their own, as
            fr-FR keeps its enchaînement rules spelling-free and states the
            h aspiré block in one rule ordered before them.

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
        for name, values in (("spellings", spellings), ("joined_spellings", joined_spellings)):
            if values is not None and len(values) != len(words_ipa):
                raise ValueError(
                    f"{name} has {len(values)} entries for {len(words_ipa)} words"
                )
        if joined_spellings is None:
            joined_spellings = spellings
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
            for rule, left_re, right_re, spelled in self._compiled:
                if left_done and right_done:
                    break
                if obligatory_only and not rule.obligatory:
                    continue
                if not (left_re.search(left) and right_re.search(right)):
                    continue
                left_sp, left_joined, right_sp, right_joined = spelled
                if not (_spelled(left_sp, spellings, i) and _spelled(left_joined, joined_spellings, i)
                        and _spelled(right_sp, spellings, i + 1)
                        and _spelled(right_joined, joined_spellings, i + 1)):
                    continue
                if rule.transform is not None and not left_done:
                    result[i] = left_re.sub(rule.transform, left)
                    left_done = True
                if rule.right_transform is not None and not right_done:
                    result[i + 1] = right_re.sub(rule.right_transform, right)
                    right_done = True
        return result


def _spelled(pattern: Optional[re.Pattern], spellings: Optional[Sequence[str]], i: int) -> bool:
    """A rule's spelling condition on word *i* holds: it has none, or the
    pattern finds a match in the spelling of the word."""
    if pattern is None:
        return True
    return spellings is not None and pattern.search(spellings[i]) is not None
