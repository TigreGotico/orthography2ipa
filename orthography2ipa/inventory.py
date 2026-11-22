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
import unicodedata
from typing import Dict, FrozenSet, List, Mapping, Optional, Sequence, Set, Tuple

from orthography2ipa.allophony import _is_modifier, segment_ipa
from orthography2ipa.lexicon import _process_lexicon, _warn_deprecated
from orthography2ipa.phonetok import (
    _AR_SHADDA, _NASAL_CARRIERS, _carrier_split_index, _carrier_tail,
)
from orthography2ipa.positional import normalize_ending_value
from orthography2ipa.types import LanguageSpec
from orthography2ipa.vowels import (
    SONORITY_LIQUID, SONORITY_NASAL, SONORITY_STOP, SONORITY_UNKNOWN,
    is_affricate, place_class, sonority_class,
)

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


def _slot_emissions(spec: LanguageSpec) -> Set[str]:
    """Every IPA string the grapheme, positional and allophone tables can place
    on one slot. These are the only emissions that can be a segment."""
    emissions: Set[str] = set()

    for readings in spec.graphemes.values():
        emissions.update(readings or ())

    emissions.update(_positional_readings(spec))

    for surfaces in (spec.allophones or {}).values():
        emissions.update(surfaces or ())

    for rule in (spec.allophone_rules or ()):
        if rule.surface:
            emissions.add(rule.surface)
        if rule.append:
            # An inserting rule emits the inserted segment; the phoneme it
            # attaches to is already an emission of the grapheme table.
            emissions.add(rule.append)

    if spec.stress:
        emissions.update(STRESS_MARKS)

    emissions.discard("")
    return emissions


def _word_emissions(
    spec: LanguageSpec,
    lexicon: Optional[Mapping[str, str]] = None,
) -> Set[str]:
    """Every whole transcription, or whole word tail, that bypasses the tables.

    These are emissions, but never segments: a word is cut into the segments
    the slot tables declare, as :func:`tokenize` cuts any transcription."""
    # Word-level overrides hand the engine whole transcriptions, so their IPA
    # never passes through the grapheme table at all.
    emissions: Set[str] = set((spec.word_exceptions or {}).values())
    # Suffix morphology replaces the word's tail wholesale, so its IPA also
    # bypasses the grapheme table (see LanguageSpec.grammatical_endings).
    # An ambiguous ending declares an ordered candidate LIST, and every
    # element of it can surface — the lower-ranked ones through
    # ``word_candidates``/a rescorer rather than through 1-best — so the
    # whole list is an emission source. A deferring rank 1 (``None``)
    # emits nothing of its own: rank 1 comes from the grapheme table,
    # which is already counted.
    for value in (spec.grammatical_endings or {}).values():
        rank1, alternatives = normalize_ending_value(value)
        if rank1 is not None:
            emissions.add(rank1)
        emissions.update(alternatives)
    emissions.update(
        (_process_lexicon(spec.code) if lexicon is None else lexicon).values())
    emissions.discard("")
    return emissions


def _sandhi_emissions(spec: LanguageSpec, atoms: Sequence[str]) -> Set[str]:
    """The segments cross-word ``sandhi_rules`` can insert into the stream.

    Sandhi fires *after* the word tables, between words, so anything its
    ``transform``/``right_transform`` adds is a symbol source the base tables
    never saw — and French enchaînement inserts a linking tie ``‿`` that lives in
    no grapheme, positional or allophone table. The literal inserted text is cut
    with :func:`~allophony.segment_ipa` against the slot *atoms* (so a re-emitted
    affricate stays whole and the tie stands as its own segment), exactly as
    :func:`tokenize` will cut a real transcription.
    """
    rules = spec.sandhi_rules or ()
    if not rules:
        return set()
    out: Set[str] = set()
    for rule in rules:
        for transform in (rule.transform, rule.right_transform):
            literal = _transform_literals(transform)
            for seg in segment_ipa(literal, atoms):
                if seg and not seg.isspace():
                    out.add(seg)
    out.discard("")
    return out


def emission_inventory(
    spec: LanguageSpec,
    lexicon: Optional[Mapping[str, str]] = None,
) -> FrozenSet[str]:
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
      lexicon (never bundled) — which carry arbitrary IPA per word and bypass
      the tables completely. The sidecar is *lexicon*, the mapping an engine
      holds in :attr:`~orthography2ipa.pipeline.Pipeline.lexicon`, and the
      process-wide lexicon when *lexicon* is ``None``;
    * the stress marks, when the spec declares stress rules.

    The empty string is excluded: a deleted slot emits nothing, which is the
    absence of a symbol rather than a symbol.
    """
    slots = _slot_emissions(spec)
    sandhi = _sandhi_emissions(spec, _atoms_of(spec, slots))
    return frozenset(slots | sandhi | _word_emissions(spec, lexicon))


def phoneme_inventory(
    spec: LanguageSpec,
    lexicon: Optional[Mapping[str, str]] = None,
) -> FrozenSet[str]:
    """The **token set**: :func:`emission_inventory`, cut into segments.

    An emission is what one slot carries, and it is not always one phoneme —
    ``ja`` is a glide plus a vowel, ``ʔa`` a stop plus a vowel. A TTS vocabulary
    wants the segments, so each emission is cut with :func:`~allophony.segment_ipa`.

    Multi-character segments are held together when the spec declares them:
    the declared ``phonemes`` inventory, and every segment of a slot emission
    that is written with more than one base letter (an affricate surface like
    Najdi ``ts``, a tie-bar ``k͡p``, a prenasalised ``ᵐb``), is passed as the
    atom list, so ``ts`` stays one token rather than becoming ``t`` + ``s``. A
    cluster, a diphthong or a syllable a slot emits (``ks``, ``aj``, ``me``) is
    cut into its segments. This is the narrow-vs-broad choice, and it is made by
    the *data*: a spec that declares a diphthong gets it as a token, and one
    that does not, does not. A whole-word reading (a word exception, an ending,
    a lexicon entry) is an emission but never a segment: it is cut like any
    other transcription. A combining mark that a slot emits before any base
    letter (the coda tilde of Portuguese) lands on the segment before it, so it
    joins each vowel and glide that can carry it and is never a token alone. So
    does a bare palatalization mark ``ʲ`` (the Cyrillic soft sign), which joins
    each consonant from stop to liquid, and a bare length mark ``ː``, which joins
    each segment that is not a mark or a tie. Each joined token is cut like any
    transcription, so the inventory holds only tokens :func:`tokenize` returns.
    A spec whose engine doubles the letter before a shadda gets no ``ː`` joins.
    """
    atoms = _atoms(spec)
    tokens: set = set()
    marks: Set[str] = set()
    bare: Set[str] = set()
    for emission in emission_inventory(spec, lexicon):
        mark, rest = _split_leading_marks(emission)
        if mark:
            marks.add(mark)
        if rest in _BARE_MODIFIERS:
            bare.add(rest)
        else:
            tokens.update(_tokenize(rest, atoms))
    if _PALATALIZATION in bare:
        for token in tuple(tokens):
            if SONORITY_STOP <= sonority_class(token) <= SONORITY_LIQUID:
                tokens.update(_tokenize(_palatalize(token), atoms))
    if _LENGTH in bare and not _expands_shadda(spec):
        for token in tuple(tokens):
            if _LENGTH not in token and sonority_class(token) != SONORITY_UNKNOWN:
                tokens.update(_tokenize(token + _LENGTH, atoms))
    for mark in marks:
        tokens.update(_carry(token, mark) for token in tuple(tokens)
                      if _carrier_tail(token) in _NASAL_CARRIERS)
    return frozenset(tokens)


_PALATALIZATION = "ʲ"
_LENGTH = "ː"
_BARE_MODIFIERS = frozenset({_PALATALIZATION, _LENGTH})


def _expands_shadda(spec: LanguageSpec) -> bool:
    """Whether the engine doubles the letter before a shadda, so that no ``ː``
    from the shadda reading ever follows a letter."""
    return spec.script == "Arabic" and _AR_SHADDA in spec.graphemes


def _palatalize(token: str) -> str:
    """*token* with the palatalization mark before its trailing length mark."""
    base = token.rstrip("ːˑ")
    if _PALATALIZATION in base:
        return token
    return base + _PALATALIZATION + token[len(base):]


def _split_leading_marks(emission: str) -> Tuple[str, str]:
    """Split *emission* into its leading combining marks and the rest.

    A slot can emit a combining mark with no base: the coda ⟨m n⟩ of
    Portuguese emits the tilde alone, and PT_FINAL_EM_GLIDE emits ``̃j̃``. The
    mark lands on the segment the slot before it wrote, so it is never a token
    of its own.
    """
    i = 0
    while i < len(emission) and unicodedata.combining(emission[i]):
        i += 1
    return emission[:i], emission[i:]


def _carry(token: str, mark: str) -> str:
    """*token* with *mark* after its base letter, where the engine splices the
    nasal tilde (``aː`` takes it as ``ãː``), in NFC as the engine writes it.
    A token that already carries *mark* is returned as it is."""
    if mark in token:
        return token
    j = _carrier_split_index(token)
    return unicodedata.normalize("NFC", token[:j] + mark + token[j:])


def phoneme_atoms(
    spec: LanguageSpec,
    lexicon: Optional[Mapping[str, str]] = None,
) -> List[str]:
    """The multi-character segments *this spec declares*, longest first.

    Public because segmentation is not only a tokenizer concern: syllable
    weight has to know that a spec's ``ts`` is one consonant, or it counts the
    coda of ``lidz`` as two and calls the syllable superheavy. The list is
    derived from the spec's own tables, so what counts as a segment is decided
    by the *data*, exactly as in :func:`phoneme_inventory`. A lexicon holds
    words, not segments, so *lexicon* has no effect and is deprecated.
    """
    if lexicon is not None:
        _warn_deprecated("the lexicon argument of phoneme_atoms()", "phoneme_atoms(spec)")
    return _atoms(spec)


def _atoms(spec: LanguageSpec) -> List[str]:
    """The segments that must never be split, longest first."""
    slots = _slot_emissions(spec)
    return _atoms_of(spec, slots | _sandhi_emissions(spec, _atoms_of(spec, slots)))


def _atoms_of(spec: LanguageSpec, emissions: Set[str]) -> List[str]:
    """The declared phonemes and the multi-character segments of *emissions*,
    longest first."""
    return sorted(
        {p for p in (spec.phonemes or ()) if p}
        | {seg for e in emissions if e not in STRESS_MARKS
           for seg in _segments(_split_leading_marks(e)[1]) if len(seg) > 1},
        key=len,
        reverse=True,
    )


#: The tie bars. A tie joins the symbols on either side into one segment.
_TIES = "\u0361\u035c"


def _segments(emission: str) -> List[str]:
    """Cut one slot emission into its segments.

    A base letter takes its trailing marks, as in :func:`~allophony.segment_ipa`.
    Three spellings write one segment with two base letters: a tie bar
    (``t͡s``, ``k͡p``), a modifier letter before its base (prenasalised ``ᵐb``,
    preaspirated ``ʰt``), and two plain letters that make an affricate
    (``ts``, ``tʃ``, ``d̠ʒ``) or a labial-velar stop (``kp``, ``ɡb``, ``ŋm``).
    Everything else is more than one segment: a cluster (``ks``, ``kw``), a
    diphthong (``aj``) or a syllable (``me``).
    """
    segments: List[str] = []
    pairable = False
    for seg in segment_ipa(emission):
        if segments and (segments[-1][-1] in _TIES
                         or all(_is_modifier(ch) for ch in segments[-1])):
            segments[-1] += seg
        elif segments and pairable and _one_segment_pair(segments[-1], seg):
            segments[-1] += seg
            pairable = False
        else:
            segments.append(seg)
            pairable = True
    return segments


def _one_segment_pair(first: str, second: str) -> bool:
    """Whether the segments *first* and *second* write one affricate or one
    labial-velar stop."""
    a, b = ("".join(ch for ch in seg if not _is_modifier(ch)) for seg in (first, second))
    if len(a) != 1 or len(b) != 1:
        return False
    if is_affricate(a + b):
        return True
    return (sonority_class(a) == sonority_class(b) in (SONORITY_STOP, SONORITY_NASAL)
            and place_class(a) == "dorsal" and place_class(b) == "labial")


def tokenize(
    ipa: str,
    spec: LanguageSpec,
    lexicon: Optional[Mapping[str, str]] = None,
) -> List[str]:
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
    Whitespace is dropped; a word boundary is the caller's concern. The segments
    come from the spec alone, so *lexicon* has no effect and is deprecated.
    """
    if lexicon is not None:
        _warn_deprecated("the lexicon argument of tokenize()", "tokenize(ipa, spec)")
    return _tokenize(ipa, _atoms(spec))


def _tokenize(ipa: str, atoms: Sequence[str]) -> List[str]:
    """:func:`tokenize` with the spec's atoms already computed."""
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

    An abugida adds one more source the tables do not show. A consonant letter
    carries its inherent vowel unless a matra or a virama cancels it, so a slot
    can hold ``kə`` in a spec whose grapheme table only ever writes ``k`` — and
    the inherent vowel is exactly what the schwa-deletion rules of every
    Devanagari language target. Those rules are reachable, so the check adds
    reading + inherent vowel to the producible set for an abugida.
    """
    producible = set(phoneme_inventory(spec) | emission_inventory(spec))
    # A silent reading is no symbol, so both inventories leave it out, but a
    # rule can target it: a slot the tables leave empty gets a vowel back
    # (English word-final ⟨e⟩ when it is the word's only vowel).
    if any("" in (readings or ()) for readings in spec.graphemes.values()) \
            or "" in _positional_readings(spec):
        producible.add("")
    if spec.script_type == "abugida" and spec.inherent_vowel:
        producible.update(p + spec.inherent_vowel for p in tuple(producible))
    dead: List[str] = []
    for rule in (spec.allophone_rules or ()):
        targets: Sequence[str] = rule.phonemes or ()
        if targets and not any(t in producible for t in targets):
            dead.append(rule.id)
    return tuple(dead)
