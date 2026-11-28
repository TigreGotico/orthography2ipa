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
    _split_leading_marks,
    _tokenize,
    _transform_literals,
    emission_inventory,
    phoneme_atoms,
    phoneme_inventory,
)
from orthography2ipa.vowels import SONORITY_LIQUID, SONORITY_STOP, sonority_class

#: Every spec, clade nodes included — a clade carries no phonology and so emits
#: nothing, but sweeping it costs nothing and proves the property is total.
ALL_CODES = sorted(available_codes(include_clades=True))


def _segments_written(spec, atoms) -> set:
    """The segments the tables of *spec* write, before any mark joins them."""
    return {token for emission in emission_inventory(spec)
            if not _split_leading_marks(emission)[0]
            for token in _tokenize(emission, atoms)}


def _hosts(spec, atoms, inventory) -> list:
    """The segments a bare ``ʲ`` or ``ʷ`` can land on: each stop, fricative,
    nasal and liquid a table writes that carries no secondary mark and no
    length mark, and that is not the cut-off half of a tied segment."""
    return [t for t in _segments_written(spec, atoms) & inventory
            if SONORITY_STOP <= sonority_class(t) <= SONORITY_LIQUID
            and not any(m in t for m in "ʲʷː") and t[-1] not in "\u0361\u035c"]


def _outside(surface: str, atoms, inventory, hosts) -> list:
    """Tokens of *surface* that fall outside *inventory*, cut as
    :func:`tokenize` cuts it with the spec's *atoms*.

    A surface that starts with a mark (the coda tilde of Portuguese, ``ʲ``,
    ``ʷ``) or that is a bare ``ː`` writes the mark on the segment before it, so
    the surface is checked joined to that segment, as whole tokens. ``ʲ`` and
    ``ʷ`` must give inventory tokens after every host in *hosts*. The other
    marks must give inventory tokens after at least one segment.
    """
    mark, _ = _split_leading_marks(surface)
    if not mark and surface != "ː":
        return [t for t in _tokenize(surface, atoms) if t not in inventory]

    def escaped(host):
        return [t for t in _tokenize(host + surface, atoms) if t not in inventory]

    if mark[:1] in ("ʲ", "ʷ"):
        return sorted({t for host in hosts for t in escaped(host)})
    if any(not escaped(host) for host in inventory):
        return []
    return [surface]


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


#: ycl writes a mark below plus tone letters with no base (⟨x⟩ is ``̠˦˦``), and
#: the engine joins both to the vowel before: ⟨sax⟩ is [sa̠˦˦]. The inventory
#: carries the mark but lists the tone letters as a token of their own, so
#: ``a̠˦˦`` is outside it.
_KNOWN_GAPS = {"ycl": "#2503: a mark below plus tone letters joins the vowel before as one token"}


@pytest.mark.parametrize("code", [
    pytest.param(code, marks=pytest.mark.xfail(strict=True, reason=_KNOWN_GAPS[code], raises=AssertionError))
    if code in _KNOWN_GAPS else code
    for code in ALL_CODES
])
def test_no_table_emits_outside_the_inventory(code):
    """Every symbol every table can emit is in the declared phoneme inventory.

    The closure invariant a downstream TTS relies on: the enumerable token set is
    the honest upper bound on what synthesis can be asked to say. A violation here
    is not cosmetic — it is an untrained embedding waiting to happen.
    """
    spec = get(code)
    inventory = phoneme_inventory(spec)
    # tokenize() derives the atoms on every call; derive them once per spec.
    atoms = phoneme_atoms(spec)
    hosts = _hosts(spec, atoms, inventory)

    violations = []
    for source_name, surfaces in _SOURCES:
        for where, surface in surfaces(spec):
            escaped = _outside(surface, atoms, inventory, hosts)
            if escaped:
                violations.append(
                    f"  {source_name} {where} -> {surface!r} emits {escaped!r}"
                )

    assert not violations, (
        f"{code}: these tables emit tokens outside the declared inventory, so a "
        f"TTS frontend built from the inventory has no embedding for them:\n"
        + "\n".join(violations)
    )


def test_a_mark_led_surface_needs_its_joined_token():
    """The check joins a bare ``ʲ`` to each host and asks for the joined token
    itself. An inventory with ``sʲ`` and ``nʲ`` but no ``tʲ`` does not close
    over the Russian soft sign, because ⟨ть⟩ writes [tʲ]."""
    spec = get("ru")
    atoms = phoneme_atoms(spec)
    inventory = phoneme_inventory(spec) - {"tʲ"}
    assert _outside("ʲ", atoms, inventory, _hosts(spec, atoms, inventory)) == ["tʲ"]
