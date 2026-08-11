"""positional — Shared positional grapheme→IPA resolution.

The engine (:mod:`orthography2ipa.g2p`) and the standalone tokenizer
beam (:mod:`orthography2ipa.phonetok`) must agree, per word, on which
IPA candidate a grapheme takes in context. Both consult a spec's
``positional_graphemes`` overrides (context-sensitive grapheme→IPA
mappings, including the vowel-class positions from the
``GraphemePosition`` redesign). This module is the **single** home for
that resolution so the two beams cannot drift apart.

Three concerns live here:

1. :func:`grapheme_positions` — given a grapheme's context (a
   :class:`~orthography2ipa.phonetok.GraphemeContext`, duck-typed: it
   only needs ``grapheme``/``prev``/``next``/``is_vowel``/``is_front``/
   ``is_back``/``is_palatal``), return the ordered list of :class:`GraphemePosition`
   values to try, **most specific first**. Exact-letter positions
   (``BEFORE_E``) precede their vowel *class* (``BEFORE_FRONT_VOWEL``),
   which precede the generic (``BEFORE_VOWEL``) and finally
   ``DEFAULT`` — this ordering is the exact>class>default precedence.
   :func:`effective_word_end` answers, once, the "is this slot
   effectively word-final?" question that several of those positions
   depend on.

2. :func:`positional_candidates` — consult ``spec.positional_graphemes``
   for a grapheme with a pre-computed position list, returning the first
   matching position's candidates (or ``None`` when the grapheme has no
   positional override at all, so the caller falls back to the flat
   ``graphemes`` table where per-candidate weights apply).

3. :func:`build_branches` / :func:`resolve_branches` — turn candidates
   into ``(ipa, cost)`` beam branches (weights → ``-log p`` cost,
   allophone expansion, dedup), and the top-level
   :func:`resolve_branches` that wires 1→2→3 together for one grapheme
   context. Both beams call :func:`resolve_branches`.

Stress/syllable-conditioned positions (``NUCLEUS_STRESSED`` etc.) need
sentence-level stress detection that only the engine computes; callers
pass ``syll_idx``/``stressed_syll_idx`` when they have them and ``None``
otherwise. With ``stressed_syll_idx is None`` the stress-conditioned
positions are simply omitted — which is why the standalone tokenizer
(no stress context) still agrees with the engine on every
non-stress-conditioned position.
"""
from __future__ import annotations

import bisect
import unicodedata

from typing import (Callable, Dict, List, NamedTuple, Optional, Sequence,
                    Tuple)

from orthography2ipa.types import GraphemePosition, LanguageSpec
from orthography2ipa.vowels import (
    base_vowel_letter,
    is_back_vowel,
    is_front_vowel,
    is_ipa_vowel,
    is_orthographic_vowel,
)
from orthography2ipa.weights import candidate_base_costs

__all__ = [
    "WordEnd",
    "effective_word_end",
    "GrammaticalEnding",
    "normalize_ending_value",
    "match_grammatical_ending",
    "grapheme_positions",
    "positional_candidates",
    "build_branches",
    "resolve_branches",
]


def _carries_nucleus(ctx) -> bool:
    """True when a non-vowel grapheme's primary IPA candidate contains a
    vowel — a CV unit (Cyrillic ⟨дя⟩ → dʲa, soft-consonant + nucleus)
    whose realisation is stress-conditioned like a plain vowel letter's.
    Reads the flat-table candidates (``ctx.ipa``), never a positional
    result, so the answer cannot be circular."""
    primary = next(iter(getattr(ctx, "ipa", ()) or ()), "")
    return any(is_ipa_vowel(ch) for ch in primary)

# Map an exact next/prev vowel letter to its BEFORE_*/AFTER_* position.
_BEFORE_EXACT: Dict[str, GraphemePosition] = {
    "a": GraphemePosition.BEFORE_A,
    "e": GraphemePosition.BEFORE_E,
    "i": GraphemePosition.BEFORE_I,
    "o": GraphemePosition.BEFORE_O,
    "u": GraphemePosition.BEFORE_U,
    # Cyrillic plain vowel letters map onto the same exact-letter axes so
    # positional keys like before_o work for Cyrillic-script specs
    # (Ukrainian ⟨в⟩ → [w] before rounded vowels). The iotated letters
    # (е ё ю я) are deliberately absent: they open with a glide, which is
    # the neighbour that matters.
    "а": GraphemePosition.BEFORE_A,
    "э": GraphemePosition.BEFORE_E,
    "и": GraphemePosition.BEFORE_I,
    "і": GraphemePosition.BEFORE_I,
    "о": GraphemePosition.BEFORE_O,
    "у": GraphemePosition.BEFORE_U,
}
_AFTER_EXACT: Dict[str, GraphemePosition] = {
    "a": GraphemePosition.AFTER_A,
    "e": GraphemePosition.AFTER_E,
    "i": GraphemePosition.AFTER_I,
    "o": GraphemePosition.AFTER_O,
    "u": GraphemePosition.AFTER_U,
}


#: Graphemes that, when word-final and independently silenced by the
#: spec, are TRANSPARENT grammatical markers rather than a root-final
#: consonant: adding them never changes how the preceding syllable is
#: built (French plural/verbal-agreement ``-s``, and its ``-x`` allomorph
#: — choux, genoux — Tranel 1987 §3, standard French orthography). A
#: root-final silenced consonant (pied's ``-d``, chat's ``-t``…) is NOT
#: transparent in this sense: the syllable's nucleus was fixed by the
#: root before that consonant ever dropped out, so a preceding glide is
#: still licensed and a following vowel is still needed as the nucleus.
#: This set is deliberately narrow rather than "any silenced consonant"
#: to avoid conflating the two (see positional_graphemes rule review for
#: the ``pied``/``vies`` minimal pair that motivated the distinction).
_TRANSPARENT_SUFFIX_GRAPHEMES = frozenset({"s", "x"})


class WordEnd(NamedTuple):
    """Where the word effectively ends, as seen from one grapheme slot.

    The three flags are the named cases of the single question "is this
    slot effectively word-final?", and they form a small lattice rather
    than three independent booleans: ``final_slot`` and
    ``last_audible_slot`` are mutually exclusive by construction (the
    first means nothing follows, the second means exactly one transparent
    suffix follows), and ``silent_final_vowel`` implies one of them (it is
    the e-caduc reading OF an effectively-final vowel slot, so
    ``(False, False, True)`` is unreachable). A caller reads the case it
    needs instead of composing predicates.
    """

    #: Nothing at all follows: the slot holds the word's last grapheme.
    final_slot: bool
    #: The only thing that follows is a transparent grammatical suffix the
    #: spec already silences (see
    #: :data:`_TRANSPARENT_SUFFIX_GRAPHEMES`) — French plural ⟨vies⟩. The
    #: syllable is built as if the word ended at this slot.
    last_audible_slot: bool
    #: The slot itself is a vowel the spec silences word-finally — the
    #: e-caduc class — sitting in the word's last audible slot. Only such
    #: a vowel can cause nucleus loss under glide formation (French ⟨vie⟩:
    #: gliding the ⟨i⟩ would leave the silent e-caduc as the only
    #: nucleus). A *pronounced* terminal vowel (⟨alicia⟩'s ⟨a⟩) carries
    #: the nucleus itself, so this case must NOT fire for it.
    silent_final_vowel: bool


_NO_WORD_END = WordEnd(final_slot=False, last_audible_slot=False,
                       silent_final_vowel=False)


def effective_word_end(ctx, spec: Optional[LanguageSpec]) -> WordEnd:
    """Classify how the word ends at the slot *ctx*, under *spec*.

    This is the one place that answers "is this slot effectively
    word-final?"; the linguistic distinctions live inside it as the named
    cases of :class:`WordEnd`:

    * a **transparent grammatical suffix** (⟨s⟩/⟨x⟩, Tranel 1987 §3) that
      the spec silences word-finally leaves the preceding slot audibly
      final — ``last_audible_slot``. A root-final silenced consonant
      (⟨pied⟩'s ⟨d⟩) is NOT transparent: the nucleus was fixed by the root
      before that consonant dropped out, which is the ⟨pied⟩/⟨vies⟩
      minimal pair the narrow suffix set exists for.
    * a spec-silenced final **vowel** (e-caduc) is the nucleus-loss case —
      ``silent_final_vowel`` — as opposed to a pronounced terminal vowel,
      which carries the nucleus itself.

    Only ``spec``'s declared ``word_final`` overrides are read, never a
    resolved positional result, so there is no recursion and no ordering
    dependency on the caller.
    """
    if ctx is None:
        return _NO_WORD_END

    positional = spec.positional_graphemes if spec else None

    def silenced_word_finally(grapheme: str) -> bool:
        """Spec declares an empty candidate for *grapheme* at word_final."""
        if not positional:
            return False
        entry = positional.get(grapheme)
        if not entry:
            return False
        final_candidates = entry.get(GraphemePosition.WORD_FINAL)
        return bool(final_candidates) and "" in final_candidates

    tail = ctx.next
    final_slot = tail is None
    last_audible_slot = (
        tail is not None
        and tail.next is None
        and tail.grapheme in _TRANSPARENT_SUFFIX_GRAPHEMES
        and silenced_word_finally(tail.grapheme)
    )
    silent_final_vowel = (
        (final_slot or last_audible_slot)
        and ctx.is_vowel
        and silenced_word_finally(ctx.grapheme)
    )
    return WordEnd(final_slot=final_slot,
                   last_audible_slot=last_audible_slot,
                   silent_final_vowel=silent_final_vowel)


class GrammaticalEnding(NamedTuple):
    """A matched ``grammatical_endings`` entry, in token terms.

    ``tokens`` counts the trailing grapheme tokens the match covers —
    the ending itself plus the transparent grammatical suffix behind it,
    if any — so the caller replaces exactly that many emitted segments
    with :attr:`ipa` and never touches the word's interior.

    :attr:`ipa` is ``None`` for a **deferring** ending: rank 1 is
    whatever the grapheme tables already produced, and only the
    :attr:`alternatives` are contributed. See
    :func:`normalize_ending_value`.
    """

    #: The orthographic ending as declared in the spec (lowercase).
    ending: str
    #: Its rank-1 IPA realisation, replacing the whole matched tail, or
    #: ``None`` when the ending defers rank 1 to the grapheme tables.
    ipa: Optional[str]
    #: How many trailing grapheme tokens the tail spans.
    tokens: int
    #: Lower-ranked licit realisations of the same tail, in declared
    #: order. Each enters the beam as a costed alternative reading; it
    #: never displaces rank 1.
    alternatives: Tuple[str, ...] = ()


def normalize_ending_value(
    value: object,
) -> Tuple[Optional[str], Tuple[str, ...]]:
    """Normalise one ``grammatical_endings`` value to ``(rank1, alts)``.

    Three accepted JSON shapes, in increasing order of what they claim:

    * ``"tion": "ʃən"`` — a **string**: one realisation, which rewrites
      the matched tail. Today's shape, and the only shape that existed
      before ambiguous endings; unchanged in every respect.
    * ``"tion": ["ʃən"]`` — a **one-element list**, exactly equivalent
      to the string. This is the identity that makes the list form a
      pure superset.
    * ``"ent": [null, ""]`` — a list whose FIRST element is ``null``:
      the ending **defers** rank 1 to the grapheme tables and only adds
      the remaining elements as lower-ranked candidates.

    ``rank1`` is ``None`` exactly for the deferring shape. ``alts`` is
    everything after element 0, in declared order.

    Only element 0 may be ``null`` — a null alternative would mean "and
    also this ending may be silent", which is spelled ``""``.
    """
    if isinstance(value, str):
        return value, ()
    if isinstance(value, (list, tuple)):
        if not value:
            raise ValueError("grammatical_endings value must not be an empty list")
        head = value[0]
        if head is not None and not isinstance(head, str):
            raise ValueError(
                f"grammatical_endings rank-1 value must be a string or null, "
                f"got {head!r}")
        for alt in value[1:]:
            if not isinstance(alt, str):
                raise ValueError(
                    f"grammatical_endings alternative must be a string "
                    f"(use \"\" for a mute reading), got {alt!r}")
        return head, tuple(value[1:])
    raise ValueError(
        f"grammatical_endings value must be a string or a list, got {value!r}")


class _EndSlot(NamedTuple):
    """Minimal duck-typed grapheme context for :func:`effective_word_end`.

    The ending matcher works on grapheme *keys*, not on the tokenizer's
    context objects, but the "is this slot effectively word-final?"
    question must be answered by the one function that owns it. Two of
    these slots reproduce exactly the fields it reads."""

    grapheme: str
    next: Optional["_EndSlot"]
    is_vowel: bool = False


def match_grammatical_ending(
    graphemes: Sequence[str], spec: Optional[LanguageSpec]
) -> Optional[GrammaticalEnding]:
    """Longest ``spec.grammatical_endings`` entry sitting at the word end.

    *graphemes* are the word's grapheme-token keys, in order. A match
    requires all three of:

    1. **Effectively word-final.** The ending occupies the word's last
       tokens, or its last tokens before a *transparent grammatical
       suffix* — the ⟨s⟩/⟨x⟩ the spec already silences word-finally, per
       :func:`effective_word_end`, which is the single owner of that
       question. French ``boulangers`` therefore matches ⟨-er⟩ — and so
       does ``vers``, purely orthographically: this matcher never looks
       at the lexicon, only at grapheme tokens. ``vers`` keeps /vɛʁ/
       anyway because ``spec.word_exceptions`` outranks
       ``grammatical_endings`` and lists ``vers`` explicitly; the matcher
       itself has no notion of "root" versus "suffix" for a given word.
    2. **Matched on surface letters, replaced by whole tokens.** The
       ending is looked for in the word's trailing *letters*, then the
       span it occupies is rounded OUTWARD to whole grapheme tokens.
       Matching on tokens alone silently missed every ending that starts
       inside a digraph: French ⟨mm⟩ is one token, so ``comment`` and the
       whole ⟨-amment⟩/⟨-emment⟩ adverb class could never match ⟨-ment⟩
       even though the letters are plainly there. Rounding outward keeps
       the invariant that matters — a match still replaces whole tokens,
       still never re-tokenizes, and the word's interior is tokenized
       exactly as it was without this table. It also means a straddling
       ending's declared IPA stands for the ROUNDED span, i.e. for the
       straddled token as well; declare such an ending only when that is
       what you mean (French ⟨-ment⟩ over a degeminating ⟨mm⟩:
       ``comment`` → [kɔ] + [mɑ̃], not [kɔm] + [mɑ̃]).
    3. **Leaving a head.** At least one token must precede the rounded
       span; a word that *is* its ending is a word, not a suffix.

    Longest match wins, which is how a more specific ending (English
    ⟨-stion⟩) overrides the general one (⟨-tion⟩) it contains — and how
    a longer *deferring* ending (French ⟨-ment⟩, declared ``[null]``)
    shields its class from a shorter ambiguous one (⟨-ent⟩).

    The matched entry's value is normalised by
    :func:`normalize_ending_value`, so the returned
    :class:`GrammaticalEnding` carries a rank-1 realisation (possibly
    ``None``, meaning "defer to the grapheme tables") plus any
    lower-ranked alternatives the spec declares.
    """
    endings = spec.grammatical_endings if spec else None
    if not endings or len(graphemes) < 2:
        return None

    # Trailing transparent grammatical suffix, if the spec declares one.
    suffix_tokens = 0
    last = _EndSlot(graphemes[-1].lower(), None)
    if effective_word_end(_EndSlot(graphemes[-2].lower(), last),
                          spec).last_audible_slot:
        suffix_tokens = 1

    end = len(graphemes) - suffix_tokens
    # Letter offset at which each candidate token span starts, so a
    # surface-letter ending can be rounded outward to whole tokens.
    stem = [g.lower() for g in graphemes[:end]]
    surface = "".join(stem)
    starts = []
    offset = 0
    for token in stem:
        starts.append(offset)
        offset += len(token)
    if not surface:
        return None
    # Ascending letter cut => the first hit is the longest ending. A cut
    # inside a token rounds OUTWARD to that token's start, and the span
    # is admissible only while at least one whole token still precedes
    # it (a word that IS its ending is a word, not a suffix).
    for cut in range(1, len(surface)):
        if surface[cut:] not in endings:
            continue
        rank1, alternatives = normalize_ending_value(endings[surface[cut:]])
        first = bisect.bisect_right(starts, cut) - 1
        if first < 1:
            # This ending's outward-rounded span leaves no head token; a
            # SHORTER ending later in the scan may still fit, so keep
            # looking rather than aborting the search.
            continue
        return GrammaticalEnding(
            ending=surface[cut:], ipa=rank1,
            tokens=end - first + suffix_tokens,
            alternatives=alternatives)
    return None


def _silent_word_finally(spec: Optional[LanguageSpec], letters: str) -> bool:
    """Does *spec* emit nothing for the grapheme *letters* at a word end?

    Two ways a spec can say "mute here", and the engine honours both, so
    this must too:

    * a ``positional_graphemes`` ``word_final`` entry whose FIRST
      (canonical) candidate is the empty string — French ⟨s⟩, ⟨t⟩, ⟨x⟩;
    * a flat ``graphemes`` entry whose first candidate is empty, i.e. the
      letter is mute *unconditionally* — French ⟨h⟩. Reading only the
      positional table missed these and made ``beuh``/``chleuh`` look
      like closed syllables ([bœ] for [bø]).

    A grapheme whose word-final reading is merely *optionally* silent (the
    empty string ranked second, French ⟨r⟩ since it is pronounced by
    default) is pronounced by the engine, so it is not silent here either
    — the two answers cannot drift apart.
    """
    if not spec:
        return False
    entry = (spec.positional_graphemes or {}).get(letters)
    if entry:
        candidates = entry.get(GraphemePosition.WORD_FINAL)
        if candidates:
            return candidates[0] == ""
        default = entry.get(GraphemePosition.DEFAULT)
        if default:
            return default[0] == ""
    flat = (spec.graphemes or {}).get(letters)
    return bool(flat) and flat[0] == ""


#: Longest silent-tail grapheme :func:`_strip_silent_tail` will consider.
#: Mute word-final graphemes are one or two letters in every spec that has
#: any (⟨h⟩, ⟨s⟩, ⟨x⟩, ⟨gh⟩); the bound keeps the strip loop O(1) per
#: syllable instead of scanning the whole grapheme table.
_MAX_SILENT_TAIL = 3


def _strip_silent_tail(syllable: str, spec: Optional[LanguageSpec]) -> str:
    """Remove the trailing graphemes *spec* emits nothing for.

    Longest grapheme first, so a two-letter mute digraph is not mistaken
    for its last letter, and repeated so a stack of mute finals (French
    plural ⟨-s⟩ over a mute ⟨-h⟩) is fully removed.
    """
    changed = True
    while changed and syllable:
        changed = False
        for size in range(min(_MAX_SILENT_TAIL, len(syllable)), 0, -1):
            if _silent_word_finally(spec, syllable[-size:].lower()):
                syllable = syllable[:-size]
                changed = True
                break
    return syllable


def merge_nucleusless_final_syllable(
    syllables: Sequence[str],
    spec: Optional[LanguageSpec] = None,
) -> List[str]:
    """Fold a final syllable with no audible nucleus into the one before.

    A syllabifier works on LETTERS, so it happily emits a final syllable
    whose only vowel letter the spec itself silences — French *jeu·ne*,
    *eu·re*, *ho·no·re*, where the ⟨e⟩ is mute. That string is not a
    syllable: with no nucleus to carry, its consonants are the CODA of the
    syllable before it, which is therefore CLOSED. Left unmerged it looks
    open, and the mid-vowel alternations keyed on
    :attr:`~orthography2ipa.types.GraphemePosition.OPEN_SYLLABLE` read it
    the wrong way round — *jeune* came out [ʒøn] for [ʒœn], *heure* [øʁ]
    for [œʁ] (the *loi de position*: Fougeron & Smith 1993; Tranel 1987
    ch. 3-4, which state the alternation over PHONETIC syllable shape).

    Silence is asked of the spec (:func:`_strip_silent_tail`), so a
    language that pronounces its final vowels is never touched and no
    language is named here.

    THE APPROXIMATION, stated plainly: this is orthographic bookkeeping,
    not a phonetic coda test. What comes off is what the spec calls mute
    WORD-FINALLY, and :func:`_is_open_syllable` then applies that same
    strip a second time to the merged string — to letters that are no
    longer word-final once the syllables are joined. French *meute* [møt]
    and *heureuse* [øʁøz] therefore strip back to an open *meu*/*reu* and
    get the right vowel for the wrong reason, since /t/ and /z/ are both
    pronounced there. A pronounced coda that the spec does not silence
    still closes (*neutre* → *neutr*), which is right for *jeune* and
    wrong for the obstruent+liquid class the *loi de position* exempts.

    Returns a new list; the input is not modified.
    """
    result = list(syllables)
    if len(result) < 2:
        return result
    core = result[-1]
    while core and not (core[-1].isalpha() or unicodedata.combining(core[-1])):
        core = core[:-1]
    core = _strip_silent_tail(core, spec)
    if core and any(is_orthographic_vowel(ch) for ch in core):
        return result
    return result[:-2] + [result[-2] + result[-1]]


def _is_open_syllable(
    syllable: Optional[str],
    *,
    spec: Optional[LanguageSpec] = None,
    word_final: bool = False,
) -> Optional[bool]:
    """Is *syllable* open (no coda)? ``None`` when it cannot be decided.

    Decided orthographically, on the syllable the spec's own syllabifier
    produced: a syllable is OPEN when its last character is a vowel
    letter, CLOSED when it is not. This is the same level of description
    the rest of ``positional_graphemes`` works at (grapheme tokens and
    their neighbours), and it needs no phonological analysis of the
    output. A syllable with no vowel letter at all (a syllabified
    consonant run, or a token the syllabifier could not place) is
    undecidable and returns ``None`` so no aperture position is emitted.

    Aperture is about a PRONOUNCED coda, and the closest this can get to
    one without a phonological analysis is to drop what the spec itself
    calls mute: in the word's last syllable the trailing graphemes the
    spec emits nothing for are stripped before the question is asked
    (:func:`_strip_silent_tail`). It is an approximation of the coda, not
    the coda — see :func:`merge_nucleusless_final_syllable` for where it
    is known to give the right answer for the wrong reason. French
    *heureux*
    is heu·reux with a mute ⟨x⟩, an OPEN final syllable ([øʁø], not
    *[øʁœ]); *beuh* is open too, over a mute ⟨h⟩; and *chanteurs* is
    chan·teurs with a mute ⟨s⟩ over a pronounced ⟨r⟩, still CLOSED. Only
    the last syllable is treated this way — that is the only place a
    spec's ``word_final`` entry applies.
    """
    if not syllable:
        return None
    while syllable and not (syllable[-1].isalpha()
                            or unicodedata.combining(syllable[-1])):
        # A hyphen, an apostrophe or a space is NOT a segment, so it is no
        # coda: it cannot make an open syllable closed. It is also an
        # orthographic word boundary, so what stands before it is word-final
        # and its silent tail comes off with the same rule a true word-final
        # syllable gets — French *peut-être* is peu(t-)·ê·tre, an OPEN first
        # syllable, /pø/ and not *[pœ]. Weight never sees the punctuation.
        syllable = syllable[:-1]
        word_final = True
    if word_final:
        syllable = _strip_silent_tail(syllable, spec)
    if not syllable or not any(is_orthographic_vowel(ch) for ch in syllable):
        return None
    return is_orthographic_vowel(syllable[-1])


def grapheme_positions(
    ctx,
    *,
    spec: Optional[LanguageSpec] = None,
    syll_idx: Optional[int] = None,
    stressed_syll_idx: Optional[int] = None,
    syllable: Optional[str] = None,
    syllable_final: Optional[bool] = None,
) -> List[GraphemePosition]:
    """Ordered positions to try for the grapheme wrapped by *ctx*.

    Most-specific first, so a caller consulting ``positional_graphemes``
    in this order gets exact>class>default precedence for free.

    *ctx* is any object exposing ``grapheme``, ``prev``/``next`` (each a
    context or ``None``) and ``is_vowel``/``is_front``/``is_back``/
    ``is_palatal`` predicates — i.e. a
    :class:`~orthography2ipa.phonetok.GraphemeContext`. Neighbours are
    word-local for the standalone tokenizer and word-flat for the engine
    (which strips punctuation before this stage); either way ``prev is
    None`` marks the word-initial grapheme and ``next is None`` the
    word-final one.

    ``syll_idx``/``stressed_syll_idx`` add the stress-conditioned
    nucleus positions; when ``stressed_syll_idx is None`` (no stress
    context, e.g. the standalone tokenizer) those are omitted.

    ``syllable``/``syllable_final`` are the aperture context, and the
    caller owns both: ``syllable`` is the string this grapheme's syllable
    contributes a nucleus to, ``syllable_final`` says whether that string
    ends the word (so its silent tail comes off — see
    :func:`_is_open_syllable`). ``syllable=None`` means "no
    syllabification", and no aperture position is emitted. Callers that
    merge syllables for aperture (:func:`merge_nucleusless_final_syllable`)
    must report finality in the MERGED list, which is why this is a flag
    and not an index comparison the callee could do itself.

    When ``syllable`` is given, the aperture positions
    (:attr:`~orthography2ipa.types.GraphemePosition.OPEN_SYLLABLE` /
    ``CLOSED_SYLLABLE`` and their stress-crossed variants) are emitted
    too; without it they are omitted, exactly like the stress positions.
    """
    pos: List[GraphemePosition] = []
    grapheme = ctx.grapheme
    is_vowel = ctx.is_vowel
    prev_ctx = ctx.prev
    next_ctx = ctx.next
    prev_is_v = prev_ctx is not None and prev_ctx.is_vowel
    next_is_v = next_ctx is not None and next_ctx.is_vowel

    # 0. before a vowel that is itself the word's last audible slot and is
    # silenced there (the e-caduc case of effective_word_end) — most
    # specific, checked before the exact per-letter/class positions below so
    # a spec that declares it can block e.g. glide formation only when there
    # is nothing left to carry the syllable's nucleus.
    word_end = effective_word_end(ctx, spec)
    next_word_end = effective_word_end(next_ctx, spec)
    if next_word_end.silent_final_vowel:
        pos.append(GraphemePosition.BEFORE_FINAL_VOWEL)

    # 1. before_X (exact letter) then the front/back vowel *class*.
    if next_ctx is not None:
        nc = base_vowel_letter(next_ctx.grapheme[0])
        exact = _BEFORE_EXACT.get(nc)
        if exact is not None:
            pos.append(exact)
        if next_ctx.is_front:
            pos.append(GraphemePosition.BEFORE_FRONT_VOWEL)
        elif next_ctx.is_back:
            pos.append(GraphemePosition.BEFORE_BACK_VOWEL)
        # Palatal is a consonant class (decided by the neighbour's IPA), so it
        # never collides with the front/back vowel classes above; it sits at
        # the same class tier — after any exact-letter position, before the
        # generic BEFORE_CONSONANT and DEFAULT.
        if next_ctx.is_palatal:
            pos.append(GraphemePosition.BEFORE_PALATAL)

    # 2. word boundary
    if prev_ctx is None:
        pos.append(GraphemePosition.WORD_INITIAL)
    if word_end.final_slot:
        pos.append(GraphemePosition.WORD_FINAL)
    effectively_word_final_vowel = is_vowel and word_end.last_audible_slot
    # NOTE: the WORD_FINAL entry for this "effectively final" case (a vowel
    # followed only by a transparent suffix grapheme the spec already
    # silences — French plural -s/-x: "vies") is appended in section 4
    # below, AFTER nucleus_stressed/nucleus_unstressed, not here. A TRUE
    # word-final vowel outranks stress (section 2 fires unconditionally
    # before section 4), but this is a heuristic proxy for finality, not
    # the real thing — giving it the same priority caused a cross-language
    # regression (Barranquenho Portuguese clitic "les" [lɛ], stressed, lost
    # its stress-conditioned vowel quality to the language's word_final
    # reduction rule). Ranking it below NUCLEUS_STRESSED means a spec's
    # stress-aware rule wins whenever one is defined, and this only
    # supplies an answer when nothing more specific does.

    # 3. intervocalic (consonants between two vowels)
    if prev_is_v and next_is_v:
        pos.append(GraphemePosition.INTERVOCALIC)

    # 4. nucleus_stressed / nucleus_unstressed for graphemes carrying a
    # nucleus. Besides plain vowel letters this covers CV units whose IPA
    # contains a vowel — e.g. the Cyrillic iotated-vowel digraphs (⟨дя⟩ →
    # dʲa) — whose reduction is conditioned on the same stress geometry.
    # Emitting the extra positions is inert unless the spec defines them
    # for that grapheme, so vowel-less digraphs are unaffected.
    # 4a. syllable aperture (open/closed), on its own and crossed with
    # stress. The mid-vowel alternations of Romance (loi de position) and
    # the Germanic open-syllable length alternation key on APERTURE, not on
    # stress alone, so the crossed positions are emitted first (most
    # specific), then the aperture-only pair, and only then the
    # stress-only positions kept below. Aperture is unknown without a
    # syllabification, so nothing is emitted when *syllable* is None.
    open_syllable = _is_open_syllable(
        syllable, spec=spec, word_final=bool(syllable_final))
    if open_syllable is not None and (is_vowel or _carries_nucleus(ctx)):
        if stressed_syll_idx is not None and syll_idx is not None:
            if syll_idx == stressed_syll_idx:
                pos.append(GraphemePosition.NUCLEUS_STRESSED_OPEN
                           if open_syllable
                           else GraphemePosition.NUCLEUS_STRESSED_CLOSED)
            else:
                pos.append(GraphemePosition.NUCLEUS_UNSTRESSED_OPEN
                           if open_syllable
                           else GraphemePosition.NUCLEUS_UNSTRESSED_CLOSED)
        pos.append(GraphemePosition.OPEN_SYLLABLE if open_syllable
                   else GraphemePosition.CLOSED_SYLLABLE)

    if stressed_syll_idx is not None and syll_idx is not None and (
            is_vowel or _carries_nucleus(ctx)):
        if syll_idx == stressed_syll_idx:
            pos.append(GraphemePosition.NUCLEUS_STRESSED)
        else:
            pos.append(GraphemePosition.NUCLEUS_UNSTRESSED)
            if syll_idx < stressed_syll_idx:
                if syll_idx == stressed_syll_idx - 1:
                    pos.append(GraphemePosition.FIRST_PRETONIC)
                pos.append(GraphemePosition.PRETONIC)
            else:
                pos.append(GraphemePosition.POSTTONIC)

    if effectively_word_final_vowel:
        pos.append(GraphemePosition.WORD_FINAL)

    # 5. after/before vowel / consonant context
    if prev_is_v:
        pc = base_vowel_letter(prev_ctx.grapheme[0])
        exact = _AFTER_EXACT.get(pc)
        if exact is not None:
            pos.append(exact)
        if prev_ctx.is_front:
            pos.append(GraphemePosition.AFTER_FRONT_VOWEL)
        elif prev_ctx.is_back:
            pos.append(GraphemePosition.AFTER_BACK_VOWEL)
        # Palatal is decided by the neighbour's IPA, so a vowel *letter*
        # realised as a palatal glide (⟨i⟩/⟨y⟩ → /j/) is palatal too — mirror
        # the unconditional BEFORE_PALATAL emission so the two sides agree.
        if prev_ctx.is_palatal:
            pos.append(GraphemePosition.AFTER_PALATAL)
        pos.append(GraphemePosition.AFTER_VOWEL)
    elif prev_ctx is not None:
        # Preceding grapheme is a consonant: the palatal class (decided by
        # its IPA) is more specific than the generic AFTER_CONSONANT.
        if prev_ctx.is_palatal:
            pos.append(GraphemePosition.AFTER_PALATAL)
        pos.append(GraphemePosition.AFTER_CONSONANT)
    if next_is_v:
        pos.append(GraphemePosition.BEFORE_VOWEL)
    elif next_ctx is not None:
        pos.append(GraphemePosition.BEFORE_CONSONANT)

    # 6. nucleus fallback for vowels
    if is_vowel:
        pos.append(GraphemePosition.NUCLEUS)

    pos.append(GraphemePosition.DEFAULT)
    return pos


def positional_candidates(
    spec: LanguageSpec,
    grapheme: str,
    positions: Sequence[GraphemePosition],
) -> Optional[List[str]]:
    """First positional override matching *grapheme* over *positions*.

    Returns ``None`` when the grapheme has no ``positional_graphemes``
    entry at all (caller falls back to the flat table), or when it has an
    entry but none of *positions* is declared for it.
    """
    pg = spec.positional_graphemes.get(grapheme)
    if not pg:
        return None
    for position in positions:
        if position in pg:
            return pg[position]
    return None


def build_branches(
    candidates: Sequence[str],
    weights: Optional[Sequence[float]],
    allophone_map: Optional[Dict[str, List[str]]],
    grapheme: str,
) -> List[Tuple[str, float]]:
    """Turn ordered *candidates* into deduped ``(ipa, cost)`` beam branches.

    ``weights`` (or ``None``) feed
    :func:`~orthography2ipa.weights.candidate_base_costs` — ``None`` gives
    the uniform-descending rank cost, byte-identical to the pre-weights
    behaviour. When *allophone_map* is given each phoneme further branches
    into its allophonic variants at ``+0.5`` per rank beyond the first.
    Duplicate IPA strings collapse to their lowest cost; the result is
    sorted ``(cost, ipa)``.
    """
    costs = candidate_base_costs(candidates, weights, grapheme=grapheme)
    branches: List[Tuple[str, float]] = []
    for rank, phoneme in enumerate(candidates):
        base_cost = costs[rank]
        if allophone_map and phoneme in allophone_map:
            for a_rank, allophone in enumerate(allophone_map[phoneme]):
                branches.append((allophone, base_cost + 0.5 * a_rank))
        else:
            branches.append((phoneme, base_cost))
    seen: Dict[str, float] = {}
    for ipa, cost in branches:
        if ipa not in seen or cost < seen[ipa]:
            seen[ipa] = cost
    return sorted(seen.items(), key=lambda x: (x[1], x[0]))


def resolve_branches(
    spec: LanguageSpec,
    ctx,
    *,
    weights_for: Callable[[str], Optional[Sequence[float]]],
    allophone_map: Optional[Dict[str, List[str]]] = None,
    syll_idx: Optional[int] = None,
    stressed_syll_idx: Optional[int] = None,
    syllable: Optional[str] = None,
    syllable_final: Optional[bool] = None,
) -> List[Tuple[str, float]]:
    """The full per-grapheme branch resolution both beams share.

    Consults ``positional_graphemes`` in most-specific-first order; when a
    positional override fires its candidates are ranked first and the flat
    table's remaining candidates are appended (so the beam space is
    preserved). When no override fires the flat table is used with its
    per-candidate weights.

    Parameters
    ----------
    spec
        The language spec.
    ctx
        The grapheme's :class:`~orthography2ipa.phonetok.GraphemeContext`.
        Its ``ipa`` tuple is the flat-table base candidate list.
    weights_for
        Callable mapping a grapheme string to its per-candidate weights or
        ``None`` (typically ``PhonetokTokenizer.weights_for``).
    allophone_map
        Optional phoneme→allophones map for allophone expansion.
    syll_idx, stressed_syll_idx
        Stress context for nucleus positions; ``None`` when unavailable.
    syllable, syllable_final
        Aperture context, both owned by the caller: the syllable string
        this grapheme sits in, and whether that string ends the word.
        ``syllable=None`` means "no syllabification" and emits no aperture
        position. See :func:`grapheme_positions`.
    """
    grapheme = ctx.grapheme
    base_candidates = list(ctx.ipa)

    positions = grapheme_positions(
        ctx, spec=spec, syll_idx=syll_idx,
        stressed_syll_idx=stressed_syll_idx, syllable=syllable,
        syllable_final=syllable_final)
    pos_candidates = positional_candidates(spec, grapheme, positions)

    if pos_candidates is None:
        # Flat table: per-candidate weights (if any) apply.
        candidates = base_candidates
        weights = weights_for(grapheme)
    else:
        # Positional winner first, then flat alternatives not already
        # covered. Positional overrides carry their own ordering; flat
        # weights do not apply to them.
        seen = set(pos_candidates)
        extra = [c for c in base_candidates if c not in seen]
        candidates = list(pos_candidates) + extra
        weights = None

    return build_branches(candidates, weights, allophone_map, grapheme)
