"""Forcing a pronunciation: SSML ``<phoneme>`` in the input text::

    <phoneme alphabet="ipa" ph="ˈmiːtinɡ">meeting</phoneme>

``ph`` replaces the rules, stress marks included. The element text is the
spelling, which cross-word rules read. The precedence is::

    <phoneme ph="…">  >  spec word_exceptions  >  caller's lexicon  >  the rules

The engine checks ``ph`` against
:func:`~orthography2ipa.inventory.phoneme_inventory`, because a TTS frontend
has no embedding for a symbol outside the declared inventory.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List, Optional

__all__ = ["Chunk", "parse_markup", "MarkupError"]


class MarkupError(ValueError):
    """The markup is malformed. The message says what, and where."""


#: ``<phoneme ph="…">text</phoneme>``; ``alphabet``, when given, must be ``ipa``.
_PHONEME = re.compile(
    r"""<phoneme
        (?=[\s>])                                  # a tag, not <phonemes…>
        (?P<attrs>(?:\s+[\w-]+\s*=\s*(?:"[^"]*"|'[^']*'))*)
        \s*>
        (?P<text>.*?)
        </phoneme\s*>""",
    re.VERBOSE | re.DOTALL | re.IGNORECASE,
)

_ATTR = re.compile(r"""(?P<name>[\w-]+)\s*=\s*(?P<quote>["'])(?P<value>.*?)(?P=quote)""")


@dataclass(frozen=True)
class Chunk:
    """A run of the input: either plain text, or a word with a forced reading."""

    text: str
    #: The IPA to use verbatim, or ``None`` to transcribe *text* by the rules.
    forced_ipa: Optional[str] = None

    @property
    def is_forced(self) -> bool:
        return self.forced_ipa is not None


def parse_markup(text: str) -> List[Chunk]:
    """Split *text* into plain runs and forced-pronunciation words.

    Raises:
        MarkupError: on a ``<phoneme>`` with no ``ph``, an empty ``ph``, an
            ``alphabet`` other than ``ipa``, or an unclosed tag.
    """
    chunks: List[Chunk] = []
    pos = 0

    for match in _PHONEME.finditer(text):
        attrs = {m["name"].lower(): m["value"] for m in _ATTR.finditer(match["attrs"])}

        alphabet = attrs.get("alphabet")
        if alphabet is not None and alphabet.lower() != "ipa":
            raise MarkupError(
                f"<phoneme alphabet={alphabet!r}>: the only alphabet this library "
                f"reads is 'ipa'. Reading {alphabet!r} as if it were IPA would "
                f"mispronounce the word silently, so it is refused."
            )

        ph = attrs.get("ph")
        if ph is None:
            raise MarkupError(
                "<phoneme> with no `ph`: the element exists to give the "
                'pronunciation, so it must carry one — <phoneme ph="…">word</phoneme>.'
            )
        if not ph.strip():
            raise MarkupError(
                '<phoneme ph=""> is empty. To make a word silent, omit it from the '
                "text; an empty pronunciation is more likely a mistake than an intent."
            )

        surface = match["text"]
        if not surface.strip():
            raise MarkupError(
                f"<phoneme ph={ph!r}> wraps no text. The spelling is not decoration: "
                f"cross-word rules read the orthography, and a word with none cannot "
                f"take part in them."
            )

        if match.start() > pos:
            chunks.append(Chunk(text[pos:match.start()]))
        chunks.append(Chunk(surface, forced_ipa=ph))
        pos = match.end()

    if pos < len(text):
        chunks.append(Chunk(text[pos:]))

    remainder = "".join(c.text for c in chunks if not c.is_forced)
    if re.search(r"</?phoneme(?=[\s>])", remainder, re.IGNORECASE):
        raise MarkupError(
            "unclosed <phoneme> tag: every <phoneme …> needs a matching </phoneme>. "
            "Left as it is, the tag would be tokenised as ordinary letters and read "
            "aloud."
        )
    return chunks or [Chunk("")]
