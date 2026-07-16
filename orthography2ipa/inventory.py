"""The closed set of symbols a spec can emit — the TTS token vocabulary.

A neural TTS frontend needs a **fixed, enumerable symbol set**: the model's
embedding table is built from it before training, and a symbol that shows up at
inference time but never at training time has no embedding — the word carrying
it is mispronounced, permanently and silently. So a phonemizer that can emit a
symbol nobody enumerated is not safe to train on.

This module answers two questions a consumer must be able to ask:

* :func:`emission_inventory` — every IPA string this spec's tables can put on a
  slot. This is the honest upper bound: the grapheme readings, the positional
  readings, the allophone surfaces, and the surfaces of the ``allophone_rules``.
* :func:`phoneme_inventory` — those emissions cut into **segments**, which is the
  token set proper. ``ja`` is one *emission* but two tokens; ``aː`` is one of
  each.

and one a maintainer should:

* :func:`dead_allophone_rules` — rules whose target phoneme no grapheme in this
  spec can produce. A rule that cannot fire is not a subtle bug, it is a rule
  written against the wrong symbol, and it is invisible without this check.

## The closure invariant

:func:`emission_inventory` is derived from the same tables that do the emitting,
so it is closed *by construction* — the point of stating it as an invariant (and
testing it) is that the derivation must keep pace with the engine. Every place
the engine can put IPA on a slot has to be a place this function reads. When
someone adds a new source of IPA and forgets, the closure test is what catches
it, and a TTS consumer downstream is what would otherwise pay.
"""

from __future__ import annotations

import re
from typing import Dict, FrozenSet, List, Sequence, Set, Tuple

from orthography2ipa.allophony import segment_ipa
from orthography2ipa.lexicon import get_lexicon
from orthography2ipa.types import LanguageSpec

__all__ = [
    "emission_inventory",
    "phoneme_inventory",
    "phoneme_atoms",
    "tokenize",
    "dead_allophone_rules",
    "STRESS_MARKS",
]


def _positional_readings(spec: LanguageSpec) -> List[str]:
    """Every IPA reading in the positional table, across all positions."""
    out: List[str] = []
    for by_position in (spec.positional_graphemes or {}).values():
        for readings in by_position.values():
            out.extend(readings or ())
    return out


#: Primary and secondary stress, inserted by ``stress.apply_stress_mark``.
STRESS_MARKS = ("ˈ", "ˌ")

#: A regex-substitution backreference — ``\1`` or ``\g<name>`` — inside a sandhi
#: ``transform``. It re-emits text the input already carried, so it introduces no
#: *new* symbol; only the literal characters around it do.
_BACKREF = re.compile(r"\\g<[^>]*>|\\\d+")


def _transform_literals(transform: str) -> str:
    """The literal text a sandhi ``transform`` inserts, stripped of backrefs.

    A sandhi rule's ``transform`` is a ``re.sub`` replacement string: parts of it
    are backreferences that copy the matched input (already in the inventory by
    construction), and the rest is literal IPA the rule *adds* — French liaison's
    linking tie ``‿`` is added exactly this way. Only the literal remainder is a
    new source of symbols, so that is what the inventory must read.
    """
    if not transform:
        return ""
    return _BACKREF.sub("", transform).replace("\\", "")


def _base_emissions(spec: LanguageSpec) -> Set[str]:
    """Every IPA string the *within-word* tables can place on a slot."""
    emissions: Set[str] = set()

    for readings in spec.graphemes.values():
        emissions.update(readings or ())

    emissions.update(_positional_readings(spec))

    for surfaces in (spec.allophones or {}).values():
        emissions.update(surfaces or ())

    for rule in (spec.allophone_rules or ()):
        if rule.surface:
            emissions.add(rule.surface)

    # Word-level overrides hand the engine whole transcriptions, so their IPA
    # never passes through the grapheme table at all.
    emissions.update((spec.word_exceptions or {}).values())
    emissions.update(get_lexicon(spec.code).values())

    if spec.stress:
        emissions.update(STRESS_MARKS)

    emissions.discard("")
    return emissions


def _sandhi_emissions(spec: LanguageSpec, base: Set[str]) -> Set[str]:
    """The segments cross-word ``sandhi_rules`` can insert into the stream.

    Sandhi fires *after* the word tables, between words, so anything its
    ``transform``/``right_transform`` adds is a symbol source the base tables
    never saw — and French enchaînement inserts a linking tie ``‿`` that lives in
    no grapheme, positional or allophone table. The literal inserted text is cut
    with :func:`~allophony.segment_ipa` against the base atoms (so a re-emitted
    affricate stays whole and the tie stands as its own segment), exactly as
    :func:`tokenize` will cut a real transcription.
    """
    rules = spec.sandhi_rules or ()
    if not rules:
        return set()
    atoms = sorted(
        {p for p in (spec.phonemes or ()) if p}
        | {e for e in base if len(e) > 1 and e not in STRESS_MARKS},
        key=len,
        reverse=True,
    )
    out: Set[str] = set()
    for rule in rules:
        for transform in (rule.transform, rule.right_transform):
            literal = _transform_literals(transform)
            for seg in segment_ipa(literal, atoms):
                if seg and not seg.isspace():
                    out.add(seg)
    out.discard("")
    return out


def emission_inventory(spec: LanguageSpec) -> FrozenSet[str]:
    """Every IPA string *spec* can place on a slot.

    The union of **every** source the engine can take IPA from:

    * the grapheme table and the positional grapheme table;
    * the allophone map's surfaces, and the ``allophone_rules`` surfaces — a
      rule is a *new* source of IPA, so an inventory read off the graphemes
      alone would miss Najdi's ``ts`` entirely;
    * the cross-word ``sandhi_rules`` surfaces — sandhi fires between words,
      after the tables, so a linking tie or an assimilated segment it inserts is
      a source the within-word tables never carried;
    * the word-level overrides — inline ``word_exceptions`` and the sidecar
      lexicon (caller-registered, never bundled) — which carry arbitrary IPA per
      word and bypass the tables completely;
    * the stress marks, when the spec declares stress rules.

    The empty string is excluded: a deleted slot emits nothing, which is the
    absence of a symbol rather than a symbol.
    """
    base = _base_emissions(spec)
    return frozenset(base | _sandhi_emissions(spec, base))


def phoneme_inventory(spec: LanguageSpec) -> FrozenSet[str]:
    """The **token set**: :func:`emission_inventory`, cut into segments.

    An emission is what one slot carries, and it is not always one phoneme —
    ``ja`` is a glide plus a vowel, ``ʔa`` a stop plus a vowel. A TTS vocabulary
    wants the segments, so each emission is cut with :func:`~allophony.segment_ipa`.

    Multi-character segments are held together when the spec declares them:
    the declared ``phonemes`` inventory (and any multi-character emission, such
    as an affricate surface like Najdi ``ts``) is passed as the atom list, so
    ``ts`` stays one token rather than becoming ``t`` + ``s``. This is the
    narrow-vs-broad choice, and it is made by the *data*: a spec that declares an
    affricate gets it as a token, and one that does not, does not.
    """
    tokens: set = set()
    for emission in emission_inventory(spec):
        tokens.update(tokenize(emission, spec))
    return frozenset(tokens)


def phoneme_atoms(spec: LanguageSpec) -> List[str]:
    """The multi-character segments *this spec declares*, longest first.

    Public because segmentation is not only a tokenizer concern: syllable
    weight has to know that a spec's ``ts`` is one consonant, or it counts the
    coda of ``lidz`` as two and calls the syllable superheavy. The list is
    derived from the spec's own tables, so what counts as a segment is decided
    by the *data*, exactly as in :func:`phoneme_inventory`.
    """
    return _atoms(spec)


def _atoms(spec: LanguageSpec) -> List[str]:
    """The segments that must never be split, longest first."""
    emissions = emission_inventory(spec)
    return sorted(
        {p for p in (spec.phonemes or ()) if p}
        | {e for e in emissions if len(e) > 1 and e not in STRESS_MARKS},
        key=len,
        reverse=True,
    )


def tokenize(ipa: str, spec: LanguageSpec) -> List[str]:
    """Cut a transcription into the tokens a TTS model consumes.

    The counterpart to :func:`phoneme_inventory`: that function says what the
    vocabulary *is*, this one produces the sequence drawn from it. Every token
    this returns is in the inventory — that is the closure invariant, and it is
    the whole contract a TTS frontend depends on.

    **Stress marks are their own tokens.** They are prosodic, not segmental:
    ``ˈ`` modifies a syllable, not the vowel it happens to precede, and the
    generic IPA segmenter — which treats a spacing modifier as belonging to the
    character before it — would otherwise hand back ``ɐˈ``, a "phoneme" that is
    in no inventory and that a model would have to learn separately from ``ɐ``.
    Whitespace is dropped; a word boundary is the caller's concern.
    """
    atoms = _atoms(spec)
    tokens: List[str] = []
    for chunk in _split_on_stress(ipa):
        if chunk in STRESS_MARKS:
            tokens.append(chunk)
            continue
        tokens.extend(seg for seg in segment_ipa(chunk, atoms) if seg and not seg.isspace())
    return tokens


def _split_on_stress(ipa: str) -> List[str]:
    """Split *ipa* so each stress mark stands alone."""
    out: List[str] = []
    buf: List[str] = []
    for ch in ipa:
        if ch in STRESS_MARKS:
            if buf:
                out.append("".join(buf))
                buf = []
            out.append(ch)
        else:
            buf.append(ch)
    if buf:
        out.append("".join(buf))
    return out


def dead_allophone_rules(spec: LanguageSpec) -> Tuple[str, ...]:
    """Ids of ``allophone_rules`` whose target phoneme this spec cannot produce.

    An allophone rule rewrites a phoneme it finds on a slot. If no grapheme,
    positional reading or other rule can ever *put* that phoneme on a slot, the
    rule is unreachable — which almost always means it was written against a
    symbol the spec does not actually use (a plain ``g`` where the table emits
    ``ɡ``, say). Silent, and invisible without this check.

    Reachability is checked against **both** inventories, because the rescorer
    matches both ways: it compares a rule's target against a slot's whole IPA
    *and*, for segmental rules, against the segments within it. So a rule on
    ``a`` is live in a spec whose only source of ``a`` is the emission ``ja``,
    and a rule on ``dʒa`` is live only if some slot emits exactly that.
    """
    producible = phoneme_inventory(spec) | emission_inventory(spec)
    dead: List[str] = []
    for rule in (spec.allophone_rules or ()):
        targets: Sequence[str] = rule.phonemes or ()
        if targets and not any(t in producible for t in targets):
            dead.append(rule.id)
    return tuple(dead)
