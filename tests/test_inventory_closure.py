"""Closure: no table may emit a symbol outside the spec's declared inventory.

A neural TTS frontend builds its embedding table from the phoneme inventory
*before* training. A symbol the phonemizer can put on a slot but nobody
enumerated has no embedding vector, and the word carrying it is mispronounced
permanently and silently. So the inventory a consumer reads
(:func:`~orthography2ipa.inventory.phoneme_inventory`) must be a true superset of
everything *every* emitting table can produce — not just the graphemes.

:mod:`tests.test_inventory` checks the grapheme and allophone-surface sources and
a handful of live transcriptions. This module states the invariant as a property
over **every** emission source of **every** spec: the grapheme table, the
positional table, the allophone map, the ``allophone_rules`` surfaces, and the
cross-word ``sandhi_rules`` surfaces. Each source is tokenised exactly as the
engine tokenises a real transcription — multi-character segments (``tʃ``, ``iː``,
``ɔ̃``, an affricate the spec declares) are held whole via the spec's own atoms,
never naively split — and every resulting token must be in the inventory.

The sandhi source is the one that historically escaped the derivation: sandhi
fires between words, after the tables, so French enchaînement's linking tie
``‿`` — a symbol in no grapheme, positional or allophone table — reached a real
transcription while sitting outside the enumerated inventory. Folding it into the
derivation is what closes the loop; this test is what keeps the derivation honest
as new emission sources are added.
"""
import pytest

from orthography2ipa import available_codes, get
from orthography2ipa.inventory import (
    _transform_literals,
    phoneme_inventory,
    tokenize,
)

#: Every spec, clade nodes included — a clade carries no phonology and so emits
#: nothing, but sweeping it costs nothing and proves the property is total.
ALL_CODES = sorted(available_codes(include_clades=True))


def _outside(surface: str, spec, inventory) -> list:
    """Tokens of *surface* that fall outside *inventory*, engine-segmented."""
    return [t for t in tokenize(surface, spec) if t not in inventory]


def _grapheme_surfaces(spec):
    for grapheme, readings in spec.graphemes.items():
        for reading in (readings or ()):
            yield f"graphemes[{grapheme!r}]", reading


def _positional_surfaces(spec):
    for grapheme, by_position in (spec.positional_graphemes or {}).items():
        for position, readings in by_position.items():
            for reading in (readings or ()):
                yield f"positional_graphemes[{grapheme!r}][{position}]", reading


def _allophone_surfaces(spec):
    for phoneme, surfaces in (spec.allophones or {}).items():
        for surface in (surfaces or ()):
            yield f"allophones[{phoneme!r}]", surface


def _allophone_rule_surfaces(spec):
    for rule in (spec.allophone_rules or ()):
        if rule.surface:
            yield f"allophone_rules[{rule.id}]", rule.surface


def _sandhi_surfaces(spec):
    for rule in (spec.sandhi_rules or ()):
        for attr in ("transform", "right_transform"):
            literal = _transform_literals(getattr(rule, attr, None))
            if literal:
                yield f"sandhi_rules[{rule.id}].{attr}", literal


_SOURCES = (
    ("grapheme", _grapheme_surfaces),
    ("positional_grapheme", _positional_surfaces),
    ("allophone", _allophone_surfaces),
    ("allophone_rule", _allophone_rule_surfaces),
    ("sandhi", _sandhi_surfaces),
)


@pytest.mark.parametrize("code", ALL_CODES)
def test_no_table_emits_outside_the_inventory(code):
    """Every symbol every table can emit is in the declared phoneme inventory.

    The closure invariant a downstream TTS relies on: the enumerable token set is
    the honest upper bound on what synthesis can be asked to say. A violation here
    is not cosmetic — it is an untrained embedding waiting to happen.
    """
    spec = get(code)
    inventory = phoneme_inventory(spec)

    violations = []
    for source_name, surfaces in _SOURCES:
        for where, surface in surfaces(spec):
            escaped = _outside(surface, spec, inventory)
            if escaped:
                violations.append(
                    f"  {source_name} {where} -> {surface!r} emits {escaped!r}"
                )

    assert not violations, (
        f"{code}: these tables emit tokens outside the declared inventory, so a "
        f"TTS frontend built from the inventory has no embedding for them:\n"
        + "\n".join(violations)
    )
