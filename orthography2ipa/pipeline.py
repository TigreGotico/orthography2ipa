"""The configuration one engine runs with, named by the caller.

The transcription is a function of the spec, the input and the caller's explicit
configuration. A :class:`Pipeline` holds that configuration. The caller builds it
and passes it to one engine, so two engines in one process can run different
pipelines side by side, and an engine that gets no pipeline does not see them::

    from orthography2ipa import G2P, Pipeline, load_lexicon

    engine = G2P("en-GB", pipeline=Pipeline(lexicon=load_lexicon("/data/en-GB.tsv")))
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Optional

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
    """

    lexicon: Optional[Mapping[str, str]] = None
    syllabifier: Optional[SyllabifierPlugin] = None
