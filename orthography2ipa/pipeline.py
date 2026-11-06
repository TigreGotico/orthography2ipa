"""The configuration one engine runs with, named by the caller.

The transcription is a function of the spec, the input and the caller's explicit
configuration. A :class:`Pipeline` holds that configuration. The caller builds it
and passes it to one engine, so two engines in one process can run different
pipelines side by side, and an engine that gets no pipeline does not see them::

    from orthography2ipa import G2P, Pipeline, load_lexicon

    engine = G2P("en-GB", pipeline=Pipeline(lexicon=load_lexicon("/data/en-GB.tsv")))
"""
from __future__ import annotations

import unicodedata
from dataclasses import dataclass, replace
from itertools import zip_longest
from typing import Callable, List, Mapping, Optional, Tuple

from orthography2ipa.markup import Chunk
from orthography2ipa.plugins import SandhiPlugin
from orthography2ipa.rescorer import LatticeRescorer
from orthography2ipa.syllabifier_plugin import SyllabifierPlugin

__all__ = ["Pipeline"]


@dataclass(frozen=True)
class Pipeline:
    """What one :class:`~orthography2ipa.g2p.G2P` engine uses in place of the defaults.

    Attributes:
        lexicon: ``{word: ipa}`` entries for this engine, with lowercase NFC
            keys, as :func:`~orthography2ipa.lexicon.load_lexicon` and
            :func:`~orthography2ipa.lexicon.packaged_lexicon` return them. The
            precedence is ``spec.word_exceptions``, then this mapping, then the
            rules. An empty mapping is a lexicon with no entries. ``None``
            leaves the choice to the process-wide lexicon API, which is
            deprecated.
        syllabifier: the syllabifier for this engine. ``None`` uses the
            bundled splitter. A word this syllabifier cannot split goes to the
            bundled splitter too.
        expand: writes out one plain run of the input. It takes a string and
            returns a string, and the words may change. It runs once per plain
            run, so it never sees a ``<phoneme>`` tag or a forced word. The
            caller binds the language and composes several jobs into one
            callable.
        mark: adds marks to the whole sentence after ``expand``. It takes a
            string and returns a string with the same words, and it sees a
            forced word as spelled. It runs once per call. Removing the
            combining marks from its output must give its input back, or the
            engine raises :class:`ValueError`. A marked forced word keeps its
            written surface. The engine runs ``expand`` and ``mark`` for
            ``transcribe``, ``transcribe_detailed``, ``sentence_lattice`` and
            ``features``. A word method takes a prepared word and runs neither.
        rescore: the rescorers of this engine, in order. They run in every word
            path, before the spec's allophone rules. A single rescorer or a list
            also works, as for ``rescorer=``.
        sandhi: what happens between the words of a sentence. ``apply`` runs in
            ``transcribe`` and ``transcribe_detailed``, after the spec's
            ``sandhi_rules``, and it returns one IPA string per word.
            ``apply_sandhi=False`` turns off the spec's rules, not this field.

    A pipeline makes no promise to be hashable: a dict lexicon is not, and a
    callable compares by identity. Key a cache on what builds the pipeline.
    """

    lexicon: Optional[Mapping[str, str]] = None
    syllabifier: Optional[SyllabifierPlugin] = None
    expand: Optional[Callable[[str], str]] = None
    mark: Optional[Callable[[str], str]] = None
    rescore: Tuple[LatticeRescorer, ...] = ()
    sandhi: Optional[SandhiPlugin] = None


def _letters(text: str) -> str:
    """*text* in NFD, without its combining marks."""
    return "".join(ch for ch in unicodedata.normalize("NFD", text)
                   if unicodedata.category(ch) != "Mn")


def _check_mark(before: str, after: str) -> None:
    """Raise :class:`ValueError` unless *after* holds the words of *before*."""
    if _letters(before) == _letters(after):
        return
    was, got = next(
        ((old, new) for old, new
         in zip_longest(before.split(), after.split(), fillvalue="")
         if _letters(old) != _letters(new)),
        (before, after))
    raise ValueError(
        f"the mark stage changed {was!r} to {got!r}. A mark stage keeps the "
        f"words: removing its marks must give the input back")


def _cut_marked(marked: str, chunks: List[Chunk]) -> List[Chunk]:
    """Put *marked*, the marked text of *chunks* joined, back into *chunks*.

    A cut counts letters, and it takes the combining marks that follow them. A
    forced chunk keeps its text, so a mark on a forced word goes.
    """
    out: List[Chunk] = []
    pos = 0
    for chunk in chunks:
        start = pos
        remaining = len(_letters(chunk.text))
        while pos < len(marked) and (remaining > 0 or not _letters(marked[pos])):
            remaining -= len(_letters(marked[pos]))
            pos += 1
        out.append(chunk if chunk.is_forced
                   else replace(chunk, text=marked[start:pos]))
    return out
