"""Forcing a pronunciation: ``<phoneme>`` in the input text.

Some words are not transcribable from their spelling, and no rule will ever make
them so. A brand name, a proper noun, an acronym, a loanword a speaker pronounces
in a way the orthography does not predict — for these the caller *already knows*
the answer and needs a way to say it.

That way is SSML's ``<phoneme>`` element, which is what every TTS frontend already
speaks::

    <phoneme alphabet="ipa" ph="ˈmiːtinɡ">meeting</phoneme>

Two things are given, and both are load-bearing:

* **``ph``** — the IPA to use. It replaces the rules entirely; nothing is derived.
* **the element's text** — the *spelling*. It is not decoration. Cross-word rules
  read the orthography, because whether a word carries a case ending is a fact
  about the page and cannot be recovered from its IPA (the ``-in`` of قَاضٍ is an
  ending; the ``-in`` of مُؤْمِن is the word). A bare bracket escape that carried
  only the IPA would throw the spelling away and break sandhi.

## Where it sits

A forced pronunciation is the top of a ladder the engine already had:

    <phoneme ph="…">  >  spec word_exceptions  >  caller's lexicon  >  the rules

Every tier answers the same question — *what is this word's IPA?* — and everything
downstream (cross-word sandhi, ``confidence == 1.0``) is indifferent to which tier
answered. So this adds a tier; it does not add a pipeline.

The one thing it does *not* do is re-stress. ``ph`` is the pronunciation, mark and
all: a caller who writes ``ˈmiːtinɡ`` has placed the stress, and a caller who
writes no mark has said this word carries none. Re-deriving stress from the
spelling would overrule the very thing being forced.

## The inventory is still the law

``ph`` is checked against the spec's declared phoneme inventory, and an undeclared
symbol is an error. This is the constraint that makes the feature safe rather than
a hole in it: a TTS frontend builds its embedding table from the declared inventory
*before* training, so a symbol that appears only at inference has no vector, and
every word carrying it is mispronounced permanently and silently.

This is precisely the case that matters for a loanword. English *meeting* is not
[ˈmiːtɪŋ] in Saudi Arabic — it is nativised, and /ɪ/ and /ŋ/ are not Arabic
phonemes. Forcing the donor's phonology would emit two symbols the ``ar`` spec
never declares. The check turns that from a silent, permanent mispronunciation
into an error at the call site, which names the offending symbols.

A caller who genuinely means to emit a phoneme outside the inventory is making a
claim about the phonology, and a claim about the phonology belongs in the spec —
where it can be read, cited and diffed.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List, Optional

__all__ = ["Chunk", "parse_markup", "MarkupError"]


class MarkupError(ValueError):
    """The markup is malformed. The message says what, and where."""


#: ``<phoneme ph="…">text</phoneme>``. ``alphabet`` is optional and, when given,
#: must be ``ipa`` — this library has no other alphabet to offer, and silently
#: accepting ``x-sampa`` would mean reading it as IPA.
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


def _attrs(raw: str) -> dict:
    return {m["name"].lower(): m["value"] for m in _ATTR.finditer(raw)}


def parse_markup(text: str) -> List[Chunk]:
    """Split *text* into plain runs and forced-pronunciation words.

    Text with no markup yields a single plain chunk, so a caller who has never
    heard of ``<phoneme>`` pays nothing.

    Raises:
        MarkupError: on a ``<phoneme>`` with no ``ph``, an empty ``ph``, an
            ``alphabet`` other than ``ipa``, or an unclosed tag.
    """
    chunks: List[Chunk] = []
    pos = 0

    for match in _PHONEME.finditer(text):
        attrs = _attrs(match["attrs"])

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

    _reject_stray_tag("".join(c.text for c in chunks if not c.is_forced))
    return chunks or [Chunk("")]


def _reject_stray_tag(remainder: str) -> None:
    """A ``<phoneme`` left in the plain text never closed, and would be read as
    letters — silently, which is the failure this whole module exists to avoid."""
    if re.search(r"</?phoneme(?=[\s>])", remainder, re.IGNORECASE):
        raise MarkupError(
            "unclosed <phoneme> tag: every <phoneme …> needs a matching </phoneme>. "
            "Left as it is, the tag would be tokenised as ordinary letters and read "
            "aloud."
        )
