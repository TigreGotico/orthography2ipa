"""stress — Primary word-stress detection and IPA stress marking.

Consumes the declarative :class:`~orthography2ipa.types.StressRules` block
of a :class:`~orthography2ipa.types.LanguageSpec` to locate the stressed
syllable of an orthographic word and to insert the IPA stress mark into a
transcription.

The bundled syllabifier is a naive vowel-group splitter, good enough for
end-anchored stress systems (final / penultimate / antepenultimate).
Languages with a real syllabifier ship it as an
``orthography2ipa.syllabify`` entry-point plugin (``silabificador`` for
Portuguese, ``pycotovia`` for Galician) — pass ``lang=`` and the plugin
is used automatically. Alternatively pass a pre-computed syllable list;
every function accepts one.

Usage
─────
    >>> from orthography2ipa import get
    >>> from orthography2ipa.stress import detect_stress, apply_stress_mark
    >>> rules = get("pt-PT").stress
    >>> detect_stress("falar", rules)     # oxytone: ends in -r
    1
    >>> detect_stress("casa", rules)      # paroxytone default
    0
    >>> apply_stress_mark("fɐlaɾ", rules, -1)
    'fɐˈlaɾ'
"""
from __future__ import annotations

import logging
import unicodedata
from typing import List, Optional, Sequence

from orthography2ipa.allophony import segment_ipa
from orthography2ipa.types import StressRules
from orthography2ipa.vowels import is_ipa_vowel, is_orthographic_vowel

__all__ = [
    "syllabify",
    "syllabify_ipa",
    "syllable_weight",
    "detect_stress",
    "detect_stress_by_weight",
    "apply_stress_mark",
    "LIGHT",
    "HEAVY",
    "SUPERHEAVY",
]


def _is_vowel_char(ch: str) -> bool:
    """Vowel test used by the naive syllabifier: orthographic vowels of
    Latin/Greek-script languages (with accented forms) plus IPA vocoids,
    so the same splitter works on spellings and on transcriptions.

    A combining mark is never a nucleus: it modifies the character it sits
    on. Counting one as a vowel splits a nasal diphthong down the middle —
    ⟨pão⟩ /pɐ̃w̃/ becomes pɐ̃-w̃, and the stress mark lands on the offglide.
    """
    if unicodedata.combining(ch):
        return False
    return is_orthographic_vowel(ch) or is_ipa_vowel(ch)


def _ends_in_vowel(ipa: str) -> bool:
    """Whether *ipa*'s final phonetic segment is a vowel (ignoring trailing
    combining marks such as nasality/length). Used to tell a word-final vowel
    deletion (consonant-final result) from an orthographic syllable over-count
    (still vowel-final) when the IPA has fewer syllables than the spelling."""
    for ch in reversed(ipa):
        if unicodedata.combining(ch):
            continue
        return _is_vowel_char(ch)
    return False


_GLIDES = set("jw" "ʲʷ")


def _split_nuclei(run: str, diphthongs: Sequence[str]) -> List[str]:
    """Split a vowel *run* into nuclei using the spec's *diphthongs*.

    Greedy longest-first: a run position that starts a listed sequence
    consumes it as ONE nucleus, any other vowel letter is a nucleus of its
    own. With no diphthongs declared the whole run is one nucleus, which is
    the behaviour every spec had before :attr:`StressRules.diphthongs`
    existed.
    """
    if not diphthongs or len(run) < 2:
        return [run]
    ordered = sorted(diphthongs, key=len, reverse=True)
    lowered = run.lower()
    nuclei: List[str] = []
    i = 0
    while i < len(run):
        for diph in ordered:
            if lowered.startswith(diph, i):
                nuclei.append(run[i:i + len(diph)])
                i += len(diph)
                break
        else:
            nuclei.append(run[i])
            i += 1
        # a combining mark is not a nucleus of its own: it rides on the vowel
        # it was written over (⟨ão⟩ /ɐ̃w̃/ — the tilde belongs to the ɐ)
        while i < len(run) and unicodedata.combining(run[i]):
            if nuclei:
                nuclei[-1] += run[i]
            else:                       # a run cannot start with a mark today
                nuclei.append(run[i])
            i += 1
    return nuclei


def syllabify(
    word: str,
    vowels: Optional[set] = None,
    diphthongs: Sequence[str] = (),
) -> List[str]:
    """Split *word* into syllables by vowel groups.

    Each maximal run of vowel characters becomes a nucleus; consonants
    attach to the following nucleus (onset-maximising), trailing
    consonants to the last syllable. This is intentionally naive — it
    exists to *count* end-anchored syllables, not to draw perfect
    boundaries.

    *diphthongs* (a spec's :attr:`~orthography2ipa.types.StressRules.diphthongs`)
    splits a vowel run into several nuclei wherever the orthography writes
    hiatus rather than a diphthong — Catalan ``tenia`` is te-ni-a, and the
    syllable count decides where stress (and the vowel reduction it
    conditions) lands. Empty = merge each run into one nucleus, unchanged.
    """
    is_vowel_char = (lambda c: c.lower() in vowels) if vowels is not None else _is_vowel_char
    if not word:
        return []
    if diphthongs:
        return _syllabify_with_diphthongs(word, is_vowel_char, diphthongs)
    # indices of nucleus starts
    syllables: List[str] = []
    current = ""
    in_nucleus = False
    for ch in word:
        if unicodedata.combining(ch):
            # a combining mark belongs to the character it sits on: it never
            # opens or closes a syllable, and never counts as a nucleus
            current += ch
            continue
        is_vowel = is_vowel_char(ch)
        if is_vowel and not in_nucleus and current and any(
                is_vowel_char(c) for c in current):
            # a new nucleus after the previous syllable already has one:
            # close the syllable before this consonant-less transition
            syllables.append(current)
            current = ch
        elif not is_vowel and in_nucleus:
            # first consonant after a nucleus: close the syllable here so
            # the consonant opens the next one (onset-maximising)
            syllables.append(current)
            current = ch
        else:
            current += ch
        in_nucleus = is_vowel
    if current:
        if any(is_vowel_char(c) for c in current) or not syllables:
            syllables.append(current)
        else:
            # trailing consonant cluster joins the last syllable
            syllables[-1] += current
    return syllables


def _syllabify_with_diphthongs(
    word: str,
    is_vowel_char,
    diphthongs: Sequence[str],
) -> List[str]:
    """:func:`syllabify` with a vowel run split into nuclei by *diphthongs*.

    Onset-maximising exactly like the plain splitter: a whole consonant run
    opens the syllable of the nucleus that follows it, a trailing consonant
    run joins the last syllable, and only the run→nuclei step differs.
    """
    syllables: List[str] = []
    onset = ""
    i = 0
    while i < len(word):
        if not is_vowel_char(word[i]):
            onset += word[i]
            i += 1
            # a combining mark rides along with whatever it sits on
            while i < len(word) and unicodedata.combining(word[i]):
                onset += word[i]
                i += 1
            continue
        j = i
        while j < len(word) and (
                is_vowel_char(word[j]) or unicodedata.combining(word[j])):
            j += 1
        for k, nucleus in enumerate(_split_nuclei(word[i:j], diphthongs)):
            syllables.append((onset if k == 0 else "") + nucleus)
        onset = ""
        i = j
    if onset:
        if syllables:
            syllables[-1] += onset
        else:
            syllables.append(onset)
    return syllables


def _syllables_for(
    word: str,
    lang: Optional[str],
    diphthongs: Sequence[str] = (),
) -> List[str]:
    """Syllabify *word*: registered plugin for *lang* first, naive fallback.

    *diphthongs* reaches the bundled splitter only; a language that ships a
    real syllabifier plugin does not need it.
    """
    if lang:
        from orthography2ipa.registry import get_syllabifier
        plugin = get_syllabifier(lang)
        if plugin is not None:
            try:
                sylls = plugin.syllabify(word, lang)
                if sylls and "".join(sylls) == word:
                    return list(sylls)
            except Exception as exc:
                logging.getLogger(__name__).warning(
                    "syllabifier plugin %r failed on word %r: %s",
                    type(plugin).__name__, word, exc)
    return syllabify(word, diphthongs=diphthongs)


def _plugin_stress(word, syllables, lang):
    """Ask the registered stress plugin, or fail loudly if the spec expects one."""
    from orthography2ipa.registry import MissingStressPlugin, get_stress_plugin

    plugin = get_stress_plugin(lang) if lang else None
    if plugin is None:
        raise MissingStressPlugin(
            f"the {lang!r} spec sets stress.source = 'plugin', but no stress plugin "
            f"is registered for it.\n\n"
            f"This is fatal on purpose. The spec is saying its stress cannot be "
            f"expressed by the declarative rules, so falling back to them would not "
            f"be a graceful degradation — it would be a DIFFERENT ANSWER, silently. "
            f"Install the plugin the spec expects, or change the spec."
        )
    return plugin.stressed_index(word, list(syllables), lang)


def detect_stress(
    word: str,
    rules: StressRules,
    syllables: Optional[Sequence[str]] = None,
    lang: Optional[str] = None,
) -> int:
    """Return the 0-based index of the stressed syllable of *word*.

    Precedence: written accents (``rules.marked_vowels``) →
    ``final_stress_endings`` → ``penult_stress_endings`` →
    ``rules.default_position``. Monosyllables are inherently stressed.

    Parameters
    ----------
    word : str
        Orthographic word (lowercased internally for ending checks).
    rules : StressRules
        The language's declarative stress system.
    syllables : Optional[Sequence[str]]
        Pre-computed syllables; takes precedence over plugin lookup.
    lang : Optional[str]
        Language code used to look up a registered
        ``orthography2ipa.syllabify`` plugin (``silabificador`` for
        Portuguese, ``pycotovia`` for Galician). The naive
        :func:`syllabify` is the fallback.
    """
    sylls = (list(syllables) if syllables is not None
             else _syllables_for(word, lang, rules.diphthongs))
    n = len(sylls)
    if n <= 1:
        return 0

    # 0. The spec may say its stress is not expressible here at all, and name a
    #    plugin instead. It has to SAY so: a plugin that places the stress changes
    #    the transcription, and the transcription must be a function of the spec
    #    and the input — never of what happens to be installed. A plugin that is
    #    unsure returns None and the declarative rules take over from here.
    if rules.source == "plugin":
        index = _plugin_stress(word, sylls, lang)
        if index is not None:
            return max(0, min(index, n - 1))


    # 1. written accent overrides everything
    if rules.marked_vowels:
        marked = set(rules.marked_vowels)
        for idx, syllable in enumerate(sylls):
            if any(ch in marked for ch in syllable):
                return idx

    lowered = word.lower()

    # 2. oxytone endings — longest first so '-im' wins over '-m'
    for ending in sorted(rules.final_stress_endings, key=len, reverse=True):
        if lowered.endswith(ending):
            return n - 1

    # 3. forced paroxytone endings
    for ending in sorted(rules.penult_stress_endings, key=len, reverse=True):
        if lowered.endswith(ending):
            return n - 2

    # 4. default position, clamped into the word.
    #    Positive values anchor from the start (1 = first syllable).
    #    Negative values anchor from the end (existing behaviour).
    pos = rules.default_position
    if pos >= 1:
        return min(pos - 1, n - 1)
    return max(0, n + pos)


def apply_stress_mark(
    ipa: str,
    rules: StressRules,
    stress_index: int,
    syllables: Optional[Sequence[str]] = None,
    ipa_syllables: Optional[Sequence[str]] = None,
) -> str:
    """Insert ``rules.stress_mark`` before the stressed syllable of *ipa*.

    Parameters
    ----------
    ipa : str
        A single word's IPA transcription (no spaces).
    rules : StressRules
        Supplies the mark character.
    stress_index : int
        Stressed syllable index. A non-negative value is interpreted
        over the *orthographic* syllable count and converted to an
        end-anchored offset, which is robust when the IPA syllable
        count differs (elided/silent vowels). A negative value is used
        as the end-anchored offset directly (``-1`` final syllable).
    syllables : Optional[Sequence[str]]
        Pre-computed orthographic syllables matching *stress_index*;
        needed only for non-negative ``stress_index`` conversion.
    ipa_syllables : Optional[Sequence[str]]
        Pre-computed syllables OF THE IPA, concatenating to *ipa*. A
        quantity-sensitive caller has already divided the transcription (that
        division is what its weights were read off), and must pass it back:
        the naive :func:`syllabify` used otherwise cuts ``saːliq`` as
        ``sa|ːliq``, so the mark would land *inside* the long vowel.

    Already-marked transcriptions are returned unchanged.
    """
    if rules.stress_mark in ipa:
        return ipa
    # The spec's diphthongs split the IPA too, not just the spelling: without
    # them a vowel run is one nucleus, so a HIATUS merges and the mark lands a
    # syllable early (⟨coelho⟩ /kuɐʎu/ → ˈkuɐʎu instead of kuˈɐʎu). A language
    # whose diphthongs are written with glides (Portuguese /aj aw/) therefore
    # leaves only true hiatus as a two-vowel run, and it must split.
    ipa_sylls = (list(ipa_syllables) if ipa_syllables
                 else syllabify(ipa, diphthongs=rules.diphthongs))
    if not ipa_sylls:
        return ipa

    if stress_index < 0:
        offset_from_end = -stress_index
    else:
        n_orth = len(syllables) if syllables is not None else len(ipa_sylls)
        overflow = len(ipa_sylls) - n_orth
        if overflow > 0:
            # The IPA has MORE syllables than the orthography. Two very
            # different causes share these counts:
            #
            # * the orthographic syllabifier UNDERCOUNTED a vowel
            #   sequence (Spanish ``ayer`` → 1 orth syllable, IPA
            #   a-ʝeɾ) — end-anchoring below still lands right, because
            #   ``detect_stress`` computed its index over the same
            #   undercounted syllables;
            # * an allophone rule EPENTHESIZED a nucleus (Irish
            #   svarabhakti, ``gorm`` → ɡɔ-ɾˠəmˠ) — end-anchoring now
            #   lands one syllable LATE, on the epenthetic vowel.
            #
            # The discriminator is the nucleus itself: anaptyctic vowels
            # are reduced (ə — the cross-linguistic epenthesis default),
            # while an undercounted written sequence splits into FULL
            # vowels. Fold excess non-initial ə-nucleus syllables back
            # into the preceding syllable for COUNTING, then end-anchor
            # as before. A word-final OPEN ə syllable is normally a real
            # written vowel (Catalan ``casa`` → ka-zə, Irish ``-cha`` →
            # xə) and is left alone; a word-final CLOSED one is the
            # classic anaptyxis site (Irish ``gorm`` → ɡɔ-ɾˠəmˠ) and
            # merges. When there is no overflow this is dead code, so
            # languages whose ə is a real written vowel are untouched.
            def _epenthetic(syll: str, final: bool) -> bool:
                if [c for c in syll if _is_vowel_char(c)] != ["ə"]:
                    return False
                return not (final and syll.endswith("ə"))

            merged: List[str] = [ipa_sylls[0]]
            for i, syll in enumerate(ipa_sylls[1:], start=1):
                if overflow > 0 and _epenthetic(
                        syll, final=i == len(ipa_sylls) - 1):
                    merged[-1] += syll
                    overflow -= 1
                else:
                    merged.append(syll)
            ipa_sylls = merged
        elif (overflow < 0 and stress_index <= len(ipa_sylls) - 1
              and not _ends_in_vowel(ipa)):
            # The IPA has FEWER syllables than the orthography, the
            # start-anchored stress index still points inside it, AND the
            # transcription ends in a consonant while the spelling ended in a
            # vowel — the signature of word-final vowel APOCOPE (Alentejo
            # ⟨fazendo⟩ → [fɐˈzẽd]). The apocope rule only ever deletes
            # UNSTRESSED final vowels, so the stressed nucleus is untouched and
            # keeps its start-anchored index; end-anchoring would drag the mark
            # forward onto an earlier syllable (ˈfɐzẽd). The consonant-final
            # guard is what separates a real trailing deletion from an
            # orthographic OVER-count of a digraph (⟨linya⟩ → [ˈliɲa], IPA
            # still vowel-final): the latter falls through to end-anchoring,
            # which lands correctly. A loss BEFORE the stress (initial/medial
            # syncope) overshoots the end and also falls through.
            ipa_sylls[stress_index] = rules.stress_mark + ipa_sylls[stress_index]
            return "".join(ipa_sylls)
        offset_from_end = max(1, n_orth - stress_index)

    target = max(0, len(ipa_sylls) - offset_from_end)
    ipa_sylls[target] = rules.stress_mark + ipa_sylls[target]
    return "".join(ipa_sylls)


# ═══════════════════════════════════════════════════════════════════════════
# Quantity-sensitive stress — placement by syllable weight
# ═══════════════════════════════════════════════════════════════════════════
#
# The systems above are end-anchored: an orthographic ending picks the
# stressed syllable. Arabic and Latin do not work that way. Their stress is
# *quantity-sensitive* — it falls on a syllable because that syllable is
# HEAVY, and weight is a property of the transcription (a long vowel, a coda),
# not of the spelling. No ending table can express it.
#
# The catch is that weight depends on where a syllable ends, so the syllable
# division has to be right. The bundled `syllabify` is onset-maximising, which
# hands every medial consonant forward to the next onset and leaves the
# previous syllable with no coda: `mudarris` comes out `mu-da-rris`, its penult
# is light, and the stress lands on the antepenult. The correct division obeys
# the language's onset limit — Arabic takes exactly one consonant as an onset,
# so it is `mu-dar-ris`, the penult is heavy, and the stress lands there:
# `muˈdarris`. Weight-based stress therefore ships its own syllabifier.

#: Length mark; a nucleus carrying it is long.
_LENGTH = "ː"

LIGHT, HEAVY, SUPERHEAVY = "light", "heavy", "superheavy"


#: Affricates written as two symbols. An affricate is ONE consonant — it is a
#: single stop-fricative contour, not a cluster — so a coda ``dz``/``dʒ`` must
#: count once when weighing a syllable, and must never be split across a
#: syllable boundary. This is a closed, cross-linguistic list (the IPA's
#: affricate series), not a per-language table: no language weighs ``t͡ʃ`` as
#: two consonants. Both spellings are listed: the tie bar is a combining mark
#: and binds only to the ``t``, so ``t͡ʃ`` needs its own entry to be one segment.
_BARE_AFFRICATES = (
    "tʃ", "dʒ", "tɕ", "dʑ", "ts", "dz", "ʈʂ", "ɖʐ", "pf", "tɬ", "dɮ", "kx",
)
_TIE = "\u0361"
_AFFRICATES: Sequence[str] = tuple(
    a[0] + _TIE + a[1:] for a in _BARE_AFFRICATES
) + _BARE_AFFRICATES


def _is_vowel_segment(seg: str) -> bool:
    """Whether a segment is a vocoid — decided by its BASE character.

    ``segment_ipa`` glues a base to its trailing modifiers, so the length mark
    of ``aː`` and the pharyngealization of ``tˤ`` never stand alone.
    """
    return bool(seg) and is_ipa_vowel(seg[0])


def syllabify_ipa(
    ipa: str,
    max_onset: int = 1,
    atoms: Sequence[str] = (),
) -> List[str]:
    """Split an IPA word into syllables, dividing clusters by *max_onset*.

    Each maximal vowel run is a nucleus. A consonant cluster between two
    nuclei is divided so the following syllable takes at most *max_onset*
    consonants as its onset and the rest close the preceding syllable. Leading
    consonants are the first onset; trailing consonants are the last coda.

    Unlike :func:`syllabify`, this draws boundaries that are *phonologically*
    meaningful rather than merely countable, because weight depends on them.

    The division is over **segments**, not characters: a base plus its trailing
    modifiers (``tˤ``, ``aː``, ``kʰ``) is one consonant, and so is any declared
    multi-character *atom* (an affricate such as ``ts``/``dʒ``). Counting a
    two-character affricate as a two-consonant cluster would split it across a
    syllable boundary, which no language does.
    """
    if not ipa:
        return []

    segs = segment_ipa(ipa, tuple(atoms) + tuple(_AFFRICATES))

    # Nucleus spans (in SEGMENTS): maximal runs of vocoids. A length mark rides
    # on the vowel it lengthens, so it is already inside its segment.
    nuclei: List[List[int]] = []
    i = 0
    while i < len(segs):
        if _is_vowel_segment(segs[i]):
            start = i
            while i < len(segs) and _is_vowel_segment(segs[i]):
                i += 1
            nuclei.append([start, i])
        else:
            i += 1

    if not nuclei:
        return [ipa]

    syllables: List[str] = []
    for n, (start, end) in enumerate(nuclei):
        if n == 0:
            onset_start = 0  # everything before the first nucleus is its onset
        else:
            prev_end = nuclei[n - 1][1]
            cluster = start - prev_end
            # The following syllable takes at most max_onset consonants; the
            # rest stay behind as the previous syllable's coda.
            onset_start = start - min(max_onset, cluster)

        if n + 1 < len(nuclei):
            nxt_start = nuclei[n + 1][0]
            cluster = nxt_start - end
            coda_end = nxt_start - min(max_onset, cluster)
        else:
            coda_end = len(segs)  # trailing consonants close the last syllable

        syllables.append("".join(segs[onset_start:coda_end]))

    return syllables


def syllable_weight(syllable: str, atoms: Sequence[str] = ()) -> str:
    """Classify one IPA syllable as ``light``, ``heavy`` or ``superheavy``.

    Weight is the nucleus plus what follows it:

    ===============  =========================  ==================
    weight           shape                      example
    ===============  =========================  ==================
    ``light``        short vowel, open (CV)     ``ki``
    ``heavy``        long vowel (CVː)           ``taː``
    ``heavy``        short vowel + 1 coda (CVC) ``dar``
    ``superheavy``   long vowel + coda (CVːC)   ``taːb``
    ``superheavy``   short vowel + 2 codas      ``bint``
    ===============  =========================  ==================

    The coda is counted in **segments**, not characters. ``latˤ`` is CVC and so
    merely heavy — ``tˤ`` is one pharyngealized consonant, not /t/ + /ˤ/ — and
    ``lidz`` is CVC too when ``dz`` is a declared affricate *atom*. Counting
    characters made both superheavy and pulled the stress onto them.
    """
    segs = segment_ipa(syllable, tuple(atoms) + tuple(_AFFRICATES))
    start = next((i for i, s in enumerate(segs) if _is_vowel_segment(s)), None)
    if start is None:
        return LIGHT  # no nucleus — nothing to weigh

    end = start
    while end < len(segs) and _is_vowel_segment(segs[end]):
        end += 1

    nucleus = segs[start:end]
    coda = segs[end:]

    # A long vowel or a diphthong is a branching (heavy) nucleus.
    long_vowel = any(_LENGTH in s for s in nucleus) or len(nucleus) > 1

    if long_vowel and coda:
        return SUPERHEAVY
    if len(coda) >= 2:
        return SUPERHEAVY
    if long_vowel or coda:
        return HEAVY
    return LIGHT


def detect_stress_by_weight(
    ipa: str,
    rules: StressRules,
    atoms: Sequence[str] = (),
) -> int:
    """Locate the stressed syllable of *ipa* by weight. Returns an end-anchored
    index (``-1`` final, ``-2`` penult, …), ready for :func:`apply_stress_mark`.

    The cascade (Ryding, *A Reference Grammar of MSA*, CUP 2005, § 2.3; Watson,
    *The Phonology and Morphology of Arabic*, OUP 2002, ch. 3):

    1. a **superheavy final** syllable takes the stress — ``kiˈtaːb`` — unless
       the language never stresses a final syllable
       (:attr:`~StressRules.superheavy_final_attracts`);
    2. otherwise a **heavy penult** takes it — ``muˈdarris``;
    3. otherwise the default position — the antepenult for Arabic —
       ``ˈmadrasa``.

    A word with fewer syllables than the default position reaches for falls
    back to its first syllable.
    """
    syllables = syllabify_ipa(ipa, rules.max_onset, atoms)
    n = len(syllables)
    if n <= 1:
        return -1

    if (rules.superheavy_final_attracts
            and syllable_weight(syllables[-1], atoms) == SUPERHEAVY):
        return -1

    if n >= 2 and syllable_weight(syllables[-2], atoms) in (HEAVY, SUPERHEAVY):
        return -2

    default = rules.default_position
    if default < 0:
        return default if n >= -default else -n
    return -n  # a positive default counts from the start: the first syllable
