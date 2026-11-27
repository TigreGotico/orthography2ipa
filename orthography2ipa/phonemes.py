"""The phoneme set of a language: every segment its compiled IR can emit.

A voice checks at load time that its symbol table holds every segment of
:func:`phoneme_set`. The compiler computes the set from the runtime fields of
the IR (docs/ir/o2i-ir-v1.md, 2.2, field ``phonemes``), so the set changes only
when the IR changes. :func:`segments` cuts IPA by the segment rule of the PER
board, and the set holds segments in that form.
"""
from __future__ import annotations

import unicodedata
from typing import FrozenSet, Iterator, List, Set

__all__ = ["phoneme_set", "segments", "ir_phonemes"]

_LIGATURES = (("ʧ", "t͡ʃ"), ("ʤ", "d͡ʒ"), ("ʦ", "t͡s"), ("ʣ", "d͡z"))
_TIES = "͜͡"
_MODIFIERS = "ʰʲʷˠˤːˑ"
_DROP = "ˈˌ.·|‿'"
#: The length mark is a literal of the interpreter (docs/ir/o2i-ir-v1.md, 3.13).
_LENGTH = "ː"


def segments(ipa: str) -> List[str]:
    """The phone segments of *ipa*, by the segment rule of the PER board.

    The text is NFD. ʧ ʤ ʦ ʣ become their tied forms. Stress marks, syllable
    dots, joiners and spaces drop. A segment is one base symbol with its
    combining marks and modifier letters, and a tie bar joins the next base
    into the same segment. ``scripts/benchmark.py`` holds the same rule.
    """
    s = unicodedata.normalize("NFD", ipa)
    for lig, tied in _LIGATURES:
        s = s.replace(lig, tied)
    out: List[str] = []
    join = False
    for ch in s:
        if ch in _DROP or ch.isspace():
            continue
        if ch in _TIES:
            join = bool(out)
            if out:
                out[-1] += "͡"
        elif out and (join or unicodedata.combining(ch) or ch in _MODIFIERS):
            out[-1] += ch
            join = False
        else:
            out.append(ch)
    return out


def _attaches(ch: str) -> bool:
    return bool(unicodedata.combining(ch)) or ch in _MODIFIERS or ch in _TIES


def _template_lits(template) -> Iterator[str]:
    for part in template or ():
        if part[0] == "lit":
            yield part[1]


def _outputs(ir: dict) -> Iterator[str]:
    """Every IPA string that a runtime field of the readable *ir* can write."""
    for entry in ir.get("entries", ()):
        yield from entry["cands"]
        yield from entry.get("onset", ())
        for _, readings in entry.get("positional", ()):
            yield from readings
    for _, surfaces in ir.get("allophone_map", ()):
        yield from surfaces
    word = ir.get("word", {})
    for table in ("exceptions", "words"):
        for row in word.get(table, ()):
            yield from row[1:]
    if "virama_final" in word:
        yield word["virama_final"]
    for rule in ir.get("allophony", {}).get("rules", ()):
        yield from rule["out"]
    for rule in ir.get("sandhi", ()):
        yield from _template_lits(rule.get("left_out"))
        yield from _template_lits(rule.get("right_out"))
    for step in ir.get("dialect", ()):
        if "rep" in step:
            yield step["rep"]
        yield from _template_lits(step.get("template"))
        for _, b in step.get("map", ()):
            yield b
        for rule in step.get("rules", ()):
            yield rule[2]
    endings = ir.get("endings", {})
    for row in endings.get("table", ()):
        yield row.get("ipa", "")
        yield from row["alts"]
    for _, reading in ir.get("consonant_nuclei", ()):
        yield reading
    for row in ir.get("tone", {}).get("table", ()):
        yield row[3]
    inherent = ir.get("inherent", {})
    for field in ("vowel", "final"):
        if field in inherent:
            yield inherent[field]


def _char_test(ir: dict):
    names = ir["bits"]["char"]
    chars = ir["chars"]
    return lambda ch, name: bool(chars.get(ord(ch), 0) >> names.index(name) & 1)


def _carrier_split(text: str, tilde: str, has) -> int:
    j = len(text)
    while j > 0 and (has(text[j - 1], "length")
                     or (text[j - 1] != tilde and has(text[j - 1], "combining"))):
        j -= 1
    return j


def ir_phonemes(ir: dict) -> List[str]:
    """The sorted phoneme set of the readable *ir*.

    It holds the segments of every string of :func:`_outputs`, and of the
    strings that the interpreter builds from them: the nasal splice (3.3.6),
    the neighbour mutation (3.6) and the iambic length mark (3.8.2). A string
    that opens with a mark joins the last segment of the string before it. A
    mark other than the nasal mark joins every segment of the set. The nasal
    mark joins a segment that ends in a nasal carrier. It joins every segment
    only when an entry reads as the nasal mark alone, because then the beam
    splices it onto a segment that is not a carrier (3.3.6). A positional
    reading of the nasal mark alone does not count: its predicate places it
    after a vowel, and the exactness test holds this.

    The set is exact for well-formed words with the default options: no
    dialect profile, no lexicon and no host hooks.
    """
    has = _char_test(ir)
    texts = {t for t in _outputs(ir) if t}
    tilde = ir.get("beam", {}).get("tilde")

    def carrier(text: str) -> bool:
        j = _carrier_split(text, tilde, has)
        return j > 0 and text[j - 1] != tilde and has(text[j - 1], "nasal_carrier")

    alone = any(e["cands"] == [tilde] for e in ir.get("entries", ()))
    built: Set[str] = set()
    if tilde in texts:
        for t in texts:
            j = _carrier_split(t, tilde, has)
            if t != tilde and (carrier(t) or alone and t[j - 1:j] != tilde):
                built.add(t[:j] + tilde + t[j:])
    for rule in ir.get("allophony", {}).get("rules", ()):
        feature = rule.get("mutate")
        if feature:
            built.update(t + feature for t in texts if feature not in t)
    texts |= built
    found: Set[str] = set()
    marks: Set[str] = set()
    nasal: Set[str] = set()
    for text in texts:
        if text == tilde and not alone:
            continue
        segs = segments(text)
        if segs and _attaches(segs[0][0]) and text != tilde:
            if tilde and segs[0].startswith(tilde):
                nasal.add(segs[0])
                if not alone:
                    segs.pop(0)
            else:
                marks.add(segs[0])
        found.update(segs)
    if "iambic" in ir.get("stress", {}):
        found.update([seg + _LENGTH for seg in found if has(seg[0], "ipa_vowel")])
    base = list(found)
    for mark in marks:
        found.update(segments(seg + mark)[-1] for seg in base)
    for mark in nasal:
        found.update(segments(seg + mark)[-1] for seg in base if alone or carrier(seg))
    return sorted(found)


def phoneme_set(lang: str) -> FrozenSet[str]:
    """Every segment that ``G2P(lang)`` can emit, from the compiled IR.

    The segments follow :func:`segments`: NFD, without stress marks or
    syllable dots, so a consumer cuts a transcription with :func:`segments`
    and checks each piece against this set. A lexicon is outside the IR, so
    the set does not cover a lexicon or a host hook. The set is exact for
    well-formed words with the default options: no dialect profile, no
    lexicon and no host hooks. Any code that ``resolve`` accepts works,
    lect codes included.

    >>> "ʎ" in phoneme_set("pt-PT")
    True
    """
    from orthography2ipa.ir import cache
    from orthography2ipa.registry import resolve
    doc = cache.document(resolve(lang), **cache.DEFAULT_OPTIONS)
    strings = doc["strings"]
    return frozenset("".join(map(chr, strings[i])) for i in doc.get("phonemes", ()))
