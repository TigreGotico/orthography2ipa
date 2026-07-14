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

from typing import Dict, FrozenSet, List, Sequence, Tuple

from orthography2ipa.allophony import segment_ipa
from orthography2ipa.lexicon import get_lexicon
from orthography2ipa.types import LanguageSpec

__all__ = [
    "emission_inventory",
    "phoneme_inventory",
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


def emission_inventory(spec: LanguageSpec) -> FrozenSet[str]:
    """Every IPA string *spec* can place on a slot.

    The union of **every** source the engine can take IPA from:

    * the grapheme table and the positional grapheme table;
    * the allophone map's surfaces, and the ``allophone_rules`` surfaces — a
      rule is a *new* source of IPA, so an inventory read off the graphemes
      alone would miss Najdi's ``ts`` entirely;
    * the word-level overrides — inline ``word_exceptions`` and the sidecar
      lexicon (caller-registered, never bundled) — which carry arbitrary IPA per
      word and bypass the tables completely;
    * the stress marks, when the spec declares stress rules.

    The empty string is excluded: a deleted slot emits nothing, which is the
    absence of a symbol rather than a symbol.
    """
    emissions: set = set()

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
    return frozenset(emissions)


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
