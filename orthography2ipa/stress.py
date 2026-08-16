"""stress — Primary word-stress detection and IPA stress marking.

Consumes the declarative :class:`~orthography2ipa.types.StressRules` block
of a :class:`~orthography2ipa.types.LanguageSpec` to locate the stressed
syllable of an orthographic word and to insert the IPA stress mark into a
transcription.

The bundled syllabifier is a vowel-group splitter, good enough for end-anchored
stress systems (final / penultimate / antepenultimate). A spec that sets
``constrain_onsets`` has its onset maximisation constrained by the licit onsets
of the language (see :class:`_OnsetJudge`).
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
from collections import OrderedDict
from typing import List, Optional, Sequence

from orthography2ipa.allophony import segment_ipa
from orthography2ipa.phonetok import lower_str
from orthography2ipa.types import LanguageSpec, StressRules
from orthography2ipa.vowels import (
    SONORITY_FRICATIVE, SONORITY_GLIDE, SONORITY_LIQUID, SONORITY_NASAL,
    SONORITY_STOP,
    SONORITY_UNKNOWN, is_ipa_vowel, is_labial_approximant,
    is_orthographic_vowel, is_affricate, is_glottal, is_lateral,
    is_palatal_glide, is_sibilant, is_voiced, place_class,
    sonority_class)

__all__ = [
    "syllabify",
    "syllabify_ipa",
    "syllable_weight",
    "detect_stress",
    "detect_stress_by_weight",
    "apply_stress_mark",
    "secondary_stress_positions",
    "SECONDARY_ALTERNATING",
    "SECONDARY_MARK",
    "cliticless_keys",
    "is_cliticless",
    "LIGHT",
    "HEAVY",
    "SUPERHEAVY",
]


def cliticless_keys(spec: LanguageSpec) -> frozenset:
    """The spec's ``stress.cliticless_words`` as a normalized lookup set.

    A prosodic clitic — a definite article, a preposition, a vocative particle —
    leans on its host and lives inside the host's stress domain, so it carries no
    word stress of its own (Watson 2002, ch. 3). Which orthographic forms those
    are is a per-language fact declared in the spec; this turns that declaration
    into the set every stress consumer tests against.

    Keys are language-aware lowercased and NFC-normalized so a listed form
    matches the input word regardless of case or Unicode composition — the same
    normalization word-exception lookup uses, so the two never disagree.
    """
    forms = spec.stress.cliticless_words if spec.stress is not None else ()
    return frozenset(
        unicodedata.normalize("NFC", lower_str(f, spec.code)) for f in forms
    )


def is_cliticless(word: str, spec: LanguageSpec) -> bool:
    """Whether *word* is a declared prosodic clitic that takes no word stress.

    An orthographic-form test — it cannot tell a clitic homograph from a full-word
    one — matching the spec's ``stress.cliticless_words``. Any consumer that places
    stress per prosodic word (the engine, or a downstream assembler like arbtok)
    routes through this so a function word is left unstressed exactly once,
    identically, wherever the decision is made.
    """
    keys = cliticless_keys(spec)
    if not keys:
        return False
    return unicodedata.normalize("NFC", lower_str(word, spec.code)) in keys


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

#: Liquids (laterals + rhotics), orthographic ⟨l r⟩ and their IPA realisations.
#: A liquid that opens a medial cluster cannot be part of a complex onset —
#: onsets rise in sonority toward the nucleus, and nothing a Latin/Ibero-Romance
#: language writes after ⟨l r⟩ is *less* sonorous while still forming a legal
#: onset. So a medial ``liquid + consonant`` cluster syllabifies with the liquid
#: as the coda of the preceding syllable (bur-mei-lho, not bu-rmei-lho), which
#: is where a following stress mark must land. See :func:`_capture_coda_liquids`.
_LIQUIDS = frozenset("lɫʎɬrɾʁʀɽɭɺ")


def _capture_coda_liquids(
    syllables: List[str],
    is_vowel_char,
) -> List[str]:
    """Move a syllable-initial liquid that heads a consonant cluster back onto
    the preceding syllable as its coda.

    The naive splitter is onset-maximising: it hands a whole medial consonant
    run forward to the next nucleus. For a ``liquid + C`` cluster that is wrong
    on sonority grounds (a liquid cannot be the first member of a rising onset),
    so ``ɾm`` in ``buɾmejʎu`` is split ``buɾ | mejʎu``. Only the *leading*
    liquid of a ≥2-consonant onset is captured; a lone onset liquid (``ʎu``) or
    a rising cluster (``bɾ``, ``pl``) is left untouched. Opt-in per spec via
    :attr:`~orthography2ipa.types.StressRules.coda_liquid_capture`.
    """
    if len(syllables) < 2:
        return syllables
    out: List[str] = [syllables[0]]
    for syll in syllables[1:]:
        # onset = the leading consonant segments before the first nucleus char
        j = 0
        while j < len(syll) and (
                unicodedata.combining(syll[j]) or not is_vowel_char(syll[j])):
            j += 1
        onset = syll[:j]
        # the base consonant characters of the onset (combining marks ride along)
        cons = [c for c in onset if not unicodedata.combining(c)]
        # Capture only a FALLING cluster: liquid followed by an equal-or-lower
        # sonority consonant (nasal/obstruent/liquid). A liquid + glide
        # (⟨lh⟩+glide ʎj, lj, ɾw) RISES in sonority and is a legal complex
        # onset — mu-lhier stays muˈʎjeɾ, not muʎˈjeɾ — so it is left intact.
        if (len(cons) >= 2 and cons[0] in _LIQUIDS
                and cons[1] not in _GLIDES and out[-1]):
            # peel the leading liquid (plus any combining marks riding on it)
            k = 1
            while k < len(syll) and unicodedata.combining(syll[k]):
                k += 1
            out[-1] += syll[:k]
            out.append(syll[k:])
        else:
            out.append(syll)
    return out


# ═══════════════════════════════════════════════════════════════════════════
# Licit onsets — maximal onset CONSTRAINED by the language's phonotactics
# ═══════════════════════════════════════════════════════════════════════════
#
# Onset Maximisation says a medial consonant belongs to the following
# syllable. It is a *preference*, not a licence: it applies only as far as the
# language's own phonotactics allow (Blevins, "The Syllable in Phonological
# Theory", in Goldsmith ed., *The Handbook of Phonological Theory*, Blackwell
# 1995, § 3.1 — "maximise the onset subject to the language-particular
# constraints on onset well-formedness"; Vennemann, *Preference Laws for
# Syllable Structure*, Mouton de Gruyter 1988, ch. 1, Head Law and Syllable
# Contact Law). Handing a whole medial cluster forward unconditionally is what
# produced e·le·ktro·nisch (⟨ktr⟩ is no onset in any language), Mo·nsieur and
# wa·nde·len.
#
# The engine must not know which onsets *this* language licenses — that would
# be a hardcoded language list. It derives them:
#
#   (a) the spec's own ``stress.max_onset``, when the spec declares one. A
#       declared cap is the language owner speaking directly and outranks
#       everything below it: Arabic says one, so one it is. It is applied
#       FIRST, before any well-formedness reasoning, because a cap the spec
#       wrote cannot be argued out of by the engine.
#   (b) the universal shapes below, read off the spec's own grapheme→IPA
#       table through :mod:`orthography2ipa.vowels`.
#
# An earlier revision had a third tier between them: onsets harvested from
# the spec's own ``word_exceptions`` keys, as attested evidence. Measured, it
# was dead and unsound — Dutch harvested ONE cluster, most languages zero,
# and Arabic harvested 25 whole WORDS because the harvester's vowel test does
# not know the Arabic script. A dead tier is worse than no tier, so it is
# gone; ``lexicon``-driven attestation is the follow-up that would make it
# real, and it needs script-aware vowel detection first.
#
# With no spec in hand (the bare :func:`syllabify` call), or with a spec that
# has not set ``constrain_onsets``, there is nothing to read and the splitter
# keeps its historical unconstrained behaviour. The gate is not a formality:
# the shapes below are calibrated on the Germanic and Romance onset
# inventories, and Modern Greek ⟨σμ κτ πτ φτ χτ φθ γν μν βγ βδ⟩ — all
# word-initial in Greek, and so all tautosyllabic — is reachable from none of
# them. See :attr:`~orthography2ipa.types.LanguageSpec.constrain_onsets`.
#
# THE ONSET SHAPES
# ────────────────
# A single consonant is a licit onset everywhere. A two-member cluster is
# licit when it is one of four named shapes, and a three-member cluster when
# it is a sibilant appendix on a licit two-member core:
#
#   RISE      obstruent + liquid or glide — ⟨tr⟩ ⟨bl⟩ ⟨kʁ⟩ ⟨dj⟩. The core
#             rising onset of the Head Law (Vennemann 1988, ch. 1).
#   CW        obstruent + labial approximant — ⟨kv⟩ ⟨dv⟩ ⟨tv⟩ ⟨zw⟩ ⟨kw⟩.
#             Swedish *kvinna*, Russian *два*, Polish *kwiat*, German *zwei*
#             and *schwer*; see ``vowels._LABIAL_APPROXIMANTS``.
#   APPENDIX  sibilant + VOICELESS obstruent — ⟨st⟩ ⟨sp⟩ ⟨sk⟩, Dutch ⟨sch⟩
#             /sx/, Polish ⟨szcz⟩ /ʂt͡ʂ/, ⟨św⟩ /ɕf/. The extrasyllabic /s/ of
#             Vennemann 1988, ch. 1 and Blevins 1995, § 3.2. Voicing is not
#             decoration: German licenses ⟨st⟩ and not ⟨sd⟩, so *Ausdruck* is
#             Aus·druck and *Hausbau* is Haus·bau, both split.
#   STOP_N    stop + a NON-HOMORGANIC coronal nasal — ⟨kn⟩ ⟨gn⟩ ⟨pn⟩. The
#             restriction is what separates the onsets German and Dutch have
#             from the ones they do not: *Abmeldung* is Ab·mel·dung (⟨bm⟩ is
#             homorganic labial), *Aufnahme* is Auf·nah·me (⟨fn⟩ has a
#             fricative, not a stop), and Dutch *ritme* is rit·me (⟨tm⟩ has a
#             labial nasal). Wiese, *The Phonology of German*, OUP 1996,
#             ch. 2, on the German onset inventory.
#
# A three-member cluster is APPENDIX + a licit two-member core whose first
# member is a VOICELESS obstruent and not itself a sibilant — ⟨str⟩ ⟨spl⟩
# ⟨schr⟩ /sxr/ ⟨schw⟩ /sxv/ are onsets; ⟨sdr⟩ is not (voiced), and ⟨ssch⟩ is
# not (two sibilants), so Dutch *misschien* is mis·schien.
#
# ONE SEGMENT THAT IS STILL NO HEAD
# ────────────────────────────────
# A single consonant opens a syllable everywhere — with one exception, and it
# is the weakest possible head: the VELAR NASAL. In the inventories this judge
# is calibrated on it is a coda-only segment. Booij, *The Phonology of Dutch*,
# OUP 1995, ch. 2, states that Dutch /ŋ/ occurs only in syllable-final
# position; Wiese, *The Phonology of German*, OUP 1996, ch. 2, says the same
# for German. It is also what the Head Law predicts (Vennemann 1988, ch. 1):
# a head is preferred the greater its consonantal strength, and a nasal at the
# back of the mouth has the least of it.
#
# Without this, a spec whose grapheme table spells /ŋ/ with ONE grapheme —
# Dutch ⟨ng⟩, ⟨nk⟩ — has that grapheme maximised into the onset, and *angel*
# comes out a·ngel with an OPEN first syllable, which then feeds the
# open-syllable length rules the wrong answer ([aː] for [ɑ]). The judgement is
# made on the run's FIRST segment, so it covers both the bare nasal ⟨ng⟩ /ŋ/
# and a grapheme spelling a whole cluster that starts with it (⟨nk⟩ /ŋk/).


#: The velar nasal, by IPA. Coda-only in the inventories this judge is
#: calibrated on, so it heads no onset — see the module comment above.
_VELAR_NASAL = "ŋ"


class _OnsetJudge:
    """Decides whether an orthographic consonant run is a licit onset.

    Built once per spec. See the module comment above for the derivation and
    the citations; this class implements it.
    """

    #: More members than this is not an onset in any language this engine
    #: serves (Blevins 1995, § 3.2: three is the attested maximum outside the
    #: appendix, and the appendix is the third member here).
    MAX_MEMBERS = 3

    #: Bound on :attr:`_cache`; onset runs come from caller-supplied words.
    CACHE_MAX = 8192

    def __init__(self, spec: LanguageSpec, max_onset: Optional[int] = None):
        self.spec = spec
        self.code = spec.code
        self.max_onset = max_onset
        graphemes = spec.graphemes or {}
        self._graphemes = sorted(
            (g for g in graphemes if g), key=len, reverse=True)
        self._ipa_of = {g: (v[0] if v else "") for g, v in graphemes.items()}
        #: Verdicts, keyed by the consonant run asked about. The runs come
        #: from words the caller supplies, so the key space is unbounded and
        #: the cache is bounded to match.
        self._cache: dict = {}

    # ---- grapheme segmentation -------------------------------------------
    def graphemes_of(self, run: str) -> List[str]:
        """Split an orthographic consonant *run* into the spec's graphemes.

        Longest match first, so a multigraph the spec declares (German ⟨sch⟩,
        Dutch ⟨ch⟩, Polish ⟨sz⟩) is ONE unit and can never be cut in half by a
        syllable boundary. A spec that does not declare one is judged over the
        letters it does declare, which is the same answer for every shape
        above (Dutch ⟨sch⟩ is undeclared and comes out ⟨s⟩+⟨ch⟩ — a sibilant
        appendix on /x/, licit either way).

        Case folding goes through :func:`~orthography2ipa.phonetok.lower_str`,
        the same language-aware fold the rest of the engine uses. It can
        change a string's LENGTH (Turkish ⟨İ⟩), so the fold is done per
        candidate grapheme rather than by walking a lowered copy with indices
        into the original.
        """
        out: List[str] = []
        i = 0
        while i < len(run):
            for g in self._graphemes:
                size = len(g)
                if size <= len(run) - i and \
                        lower_str(run[i:i + size], self.code) == g:
                    out.append(run[i:i + size])
                    i += size
                    break
            else:
                out.append(run[i])
                i += 1
            while i < len(run) and unicodedata.combining(run[i]):
                out[-1] += run[i]
                i += 1
        return out

    # ---- one grapheme's phonology ----------------------------------------
    def ipa_of(self, grapheme: str) -> str:
        ipa = self._ipa_of.get(grapheme)
        if ipa is None:
            ipa = self._ipa_of.get(lower_str(grapheme, self.code), "")
        return ipa or ""

    def _segment(self, grapheme: str) -> Optional[str]:
        """The single IPA segment *grapheme* spells, or ``None``.

        A grapheme that spells a whole cluster (⟨x⟩ → /ks/) or spells nothing
        (a silent letter) has no single tier, and so can only ever stand alone
        in an onset.
        """
        ipa = self.ipa_of(grapheme)
        if not ipa:
            return None
        if is_affricate(ipa):
            return ipa      # one segment however the spec writes the tie bar
        segs = segment_ipa(ipa, _AFFRICATES)
        return segs[0] if len(segs) == 1 else None

    @staticmethod
    def _is_geminate(grapheme: str) -> bool:
        """Whether *grapheme* is a doubled letter — ⟨ss⟩ ⟨tt⟩ ⟨nn⟩.

        A geminate is heterosyllabic: its two halves belong to different
        syllables (Hayes 1989, "Compensatory Lengthening in Moraic Phonology";
        Ladefoged & Maddieson 1996, § 3.3). It can stand alone as an onset
        grapheme — which is what the spec declared it for, and what leaves
        *Wasser* where it was — but it can never join a COMPLEX one, or
        Icelandic *Skíris·skógur* comes out Skíri·sskógur.
        """
        letters = [c for c in grapheme if not unicodedata.combining(c)]
        return len(letters) == 2 and letters[0].lower() == letters[1].lower()

    def _opens_with_velar_nasal(self, grapheme: str) -> bool:
        """Whether *grapheme*'s first IPA segment is the velar nasal.

        A velar nasal is coda-only in the inventories this judge serves, so
        no onset may start with one — see the module comment for the
        citations (Booij 1995, ch. 2; Wiese 1996, ch. 2; Vennemann 1988,
        ch. 1). Read off the first segment rather than the whole IPA so a
        grapheme spelling a cluster (Dutch ⟨nk⟩ /ŋk/) is judged too.
        """
        ipa = self.ipa_of(grapheme)
        if not ipa:
            return False
        segs = segment_ipa(ipa, _AFFRICATES)
        return bool(segs) and segs[0].startswith(_VELAR_NASAL)

    def _tier(self, grapheme: str) -> int:
        seg = self._segment(grapheme)
        return sonority_class(seg) if seg else SONORITY_UNKNOWN

    # ---- the judgement ----------------------------------------------------
    def licit(self, run: str) -> bool:
        """Whether the orthographic consonant *run* may open a syllable."""
        cached = self._cache.get(run)
        if cached is None:
            if len(self._cache) >= self.CACHE_MAX:
                self._cache.clear()
            self._cache[run] = cached = self._licit(run)
        return cached

    def _licit(self, run: str) -> bool:
        if not run:
            return True                       # an onsetless syllable is fine
        if not all(ch.isalpha() or unicodedata.combining(ch) for ch in run):
            # A hyphen, an apostrophe, a space or a digit is not a segment. It
            # cannot be an onset and cannot be part of one, so it always ends
            # up in the coda of whatever precedes it — uniformly, whether or
            # not a consonant happens to stand before it. It is then
            # TRANSPARENT to weight: see ``positional._is_open_syllable``.
            return False
        units = self.graphemes_of(run)
        # (a) the spec's own cap, before any reasoning of ours
        if self.max_onset is not None and len(units) > self.max_onset:
            return False
        if self._opens_with_velar_nasal(units[0]):
            return False    # coda-only segment — see the module comment
        if len(units) == 1:
            return True   # every language licenses a simple onset
        if len(units) > self.MAX_MEMBERS:
            return False
        if any(self._is_geminate(u) for u in units):
            return False        # a geminate never joins a complex onset
        if len(units) == self.MAX_MEMBERS:
            if (self._two_member(units[0], units[1])
                    and self._is_palatal_glide_unit(units[2])):
                return True     # ⟨brj⟩ ⟨glj⟩ — Árnason 2011, ch. 5
            return self._appendix_on(units[0], units[1:])
        return self._two_member(units[0], units[1])

    # ---- the four shapes --------------------------------------------------
    def _two_member(self, first: str, second: str) -> bool:
        s1, s2 = self._segment(first), self._segment(second)
        if s1 is None or s2 is None:
            return False
        t1, t2 = sonority_class(s1), sonority_class(s2)
        if t1 == SONORITY_UNKNOWN or t2 == SONORITY_UNKNOWN:
            return False
        obstruent = t1 <= SONORITY_FRICATIVE
        if is_glottal(s1):
            # A glottal is placeless and cannot head a rising onset (the Head
            # Law wants a strong head — Vennemann 1988, ch. 1). ⟨h⟩ between a
            # vowel and a consonant closes the syllable it follows, which is
            # also where German orthography puts it: *jäh-rig*, not *jä-hrig*
            # (Duden, *Die deutsche Rechtschreibung*, 28. Aufl., § 107).
            # Icelandic ⟨hr- hl- hv-⟩ are word-INITIAL and never re-judged.
            return False
        # RISE — obstruent + liquid (a palatal glide is judged below: an
        # obstruent + /j/ sequence is heterosyllabic in the continental
        # Germanic inventories, kat·je and dag·je, not ka·tje — Booij 1995,
        # ch. 2–3, on the Dutch diminutive ⟨-je⟩ across a morpheme boundary;
        # Wiese 1996, ch. 2, for German).
        if obstruent and t2 >= SONORITY_LIQUID and not is_palatal_glide(s2):
            # …except a homorganic coronal stop + lateral. */tl dl/ is the
            # systematic gap in the Germanic and Romance onset inventories,
            # and without it every ``-land`` compound resyllabifies:
            # Icelandic *Bret·land* became *Bre·tland*.
            if (t1 == SONORITY_STOP and is_lateral(s2)
                    and place_class(s1) == place_class(s2) == "coronal"):
                return False
            return True
        # CJ — a SONORANT + /j/. Icelandic ⟨mj lj nj rj⟩ (*mjólk*, *ljós*,
        # *njóta*, *rjúpa*) are onsets over a sonorant head, which no rising
        # shape reaches (Árnason, *The Phonology of Icelandic and Faroese*,
        # OUP 2011, ch. 5). An OBSTRUENT head is excluded, per the RISE
        # comment above: continental Germanic cuts kat·je and dag·je. This is
        # the one place the two Germanic branches part company — Icelandic
        # ⟨bjór fjall sjá tjald⟩ ARE onsets — so an Icelandic-type spec must
        # not set ``constrain_onsets`` until this shape is made per-spec.
        if (t2 == SONORITY_GLIDE and is_palatal_glide(s2)
                and not obstruent):
            return True
        # CW — obstruent + labial approximant: ⟨kv⟩ ⟨dv⟩ ⟨tv⟩ ⟨kw⟩ ⟨zw⟩
        # /t͡sv/, German ⟨schw⟩ /ʃv/, Swedish and Icelandic ⟨sv⟩, Russian
        # ⟨св зв хв⟩, Polish ⟨sw zw chw św⟩, Greek ⟨σβ⟩ (*σβήνω* — so *Λέ·σβος*,
        # tautosyllabic, which is the Modern Greek rule). The head may be any
        # obstruent: an earlier revision required a stop or a non-anterior
        # sibilant on the false premise that no Germanic language has ⟨sw⟩ —
        # English *swim*, Swedish *svensk* and Icelandic *svartur* all do.
        if obstruent and is_labial_approximant(s2):
            return True
        # APPENDIX — VOICELESS sibilant + voiceless obstruent (⟨st⟩ ⟨sch⟩
        # ⟨szcz⟩). The appendix is /s/, voiceless: Polish ⟨zc⟩ is no onset.
        if (is_sibilant(s1) and is_voiced(s1) is False
                and t2 <= SONORITY_FRICATIVE
                and is_voiced(s2) is False and not is_sibilant(s2)):
            return True
        # STOP_N — stop + non-homorganic coronal nasal (⟨kn⟩ ⟨gn⟩ ⟨pn⟩)
        if (t1 == SONORITY_STOP and t2 == SONORITY_NASAL
                and place_class(s2) == "coronal"
                and place_class(s1) != place_class(s2)):
            return True
        return False

    def _is_palatal_glide_unit(self, grapheme: str) -> bool:
        seg = self._segment(grapheme)
        return seg is not None and is_palatal_glide(seg)

    def _appendix_on(self, first: str, rest: List[str]) -> bool:
        """A sibilant appendix on a licit two-member core — ⟨str⟩ ⟨schw⟩."""
        s1 = self._segment(first)
        core_head = self._segment(rest[0])
        if s1 is None or core_head is None or not is_sibilant(s1):
            return False
        if is_voiced(s1) is not False:
            return False        # the appendix is /s/, voiceless
        if is_sibilant(core_head):
            return False        # ⟨ssch⟩ is not an onset: mis·schien
        if sonority_class(core_head) > SONORITY_FRICATIVE:
            return False        # the appendix adjoins to an OBSTRUENT core
        if is_voiced(core_head) is not False:
            return False        # ⟨str⟩ yes, ⟨sdr⟩ no: Aus·druck
        return self._two_member(rest[0], rest[1])


#: Judges are cached per (language code, cap): building one walks the spec's
#: grapheme table, and syllabification is called once per word. Keyed by the
#: spec's CODE and not by ``id(spec)`` — an id is reused the moment its object
#: is collected, which would hand one language another's phonotactics — and
#: bounded, so a process that builds many ad-hoc specs cannot grow it forever.
_JUDGE_CACHE_MAX = 64
_judge_cache: "OrderedDict[tuple, _OnsetJudge]" = OrderedDict()


def _judge_for(
    spec: Optional[LanguageSpec],
    max_onset: Optional[int] = None,
) -> Optional["_OnsetJudge"]:
    """The cached :class:`_OnsetJudge` for *spec*, or ``None`` without one."""
    if spec is None:
        return None
    key = (spec.code, max_onset)
    judge = _judge_cache.get(key)
    if judge is None or judge.spec is not spec:
        judge = _OnsetJudge(spec, max_onset)
        _judge_cache[key] = judge
        while len(_judge_cache) > _JUDGE_CACHE_MAX:
            _judge_cache.popitem(last=False)
    else:
        _judge_cache.move_to_end(key)
    return judge


def _rebalance_onsets(
    syllables: List[str],
    is_vowel_char,
    judge: "_OnsetJudge",
) -> List[str]:
    """Move whatever the language cannot license as an onset into the coda.

    The splitters hand a whole medial consonant run forward to the next
    nucleus. This walks the result and, for each syllable after the first,
    keeps the LONGEST suffix of that run which *judge* licenses as an onset —
    maximal onset, constrained (Blevins 1995, § 3.1) — and leaves the rest
    behind to close the preceding syllable.

    The first syllable's onset is never re-judged: a cluster that begins a
    word of the language IS a licit onset of that language.
    """
    if len(syllables) < 2:
        return syllables
    out: List[str] = [syllables[0]]
    for syll in syllables[1:]:
        j = 0
        while j < len(syll) and (
                unicodedata.combining(syll[j]) or not is_vowel_char(syll[j])):
            j += 1
        onset = syll[:j]
        if not onset or not out[-1]:
            out.append(syll)
            continue
        units = judge.graphemes_of(onset)
        keep = 0
        for k in range(len(units), 0, -1):
            tail = "".join(units[len(units) - k:])
            if judge.licit(tail):
                keep = len(tail)
                break
        if keep >= len(onset):
            out.append(syll)
            continue
        out[-1] += onset[:len(onset) - keep]
        out.append(syll[len(onset) - keep:])
    return out


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
    coda_liquid_capture: bool = False,
    spec: Optional[LanguageSpec] = None,
    max_onset: Optional[int] = None,
) -> List[str]:
    """Split *word* into syllables by vowel groups.

    Each maximal run of vowel characters becomes a nucleus; consonants
    attach to the following nucleus as far as the language licenses
    (onset-maximising, constrained), trailing consonants to the last syllable.

    Onset maximisation is a *preference*, and it stops at what the language
    licenses. Pass *spec* and the medial cluster is divided so the following
    syllable keeps the longest suffix that is a licit onset of that language —
    ``elektronisch`` is e-lek-tro-nisch, not e-le-ktro-nisch, and ``Monsieur``
    is Mon-sieur, not Mo-nsieur (Blevins 1995, § 3.1). Where the licit onsets
    come from is documented on :class:`_OnsetJudge`. Without a *spec* there is
    no phonotactics to consult and the split stays unconstrained.

    *max_onset* caps the onset at that many graphemes — the spec's own
    :attr:`~orthography2ipa.types.StressRules.max_onset`, when it declares one.

    *diphthongs* (a spec's :attr:`~orthography2ipa.types.StressRules.diphthongs`)
    splits a vowel run into several nuclei wherever the orthography writes
    hiatus rather than a diphthong — Catalan ``tenia`` is te-ni-a, and the
    syllable count decides where stress (and the vowel reduction it
    conditions) lands. Empty = merge each run into one nucleus, unchanged.
    """
    is_vowel_char = (lambda c: c.lower() in vowels) if vowels is not None else _is_vowel_char
    if not word:
        return []
    judge = _judge_for(spec, max_onset)
    if diphthongs:
        sylls = _syllabify_with_diphthongs(word, is_vowel_char, diphthongs)
        if judge is not None:
            sylls = _rebalance_onsets(sylls, is_vowel_char, judge)
        if coda_liquid_capture:
            sylls = _capture_coda_liquids(sylls, is_vowel_char)
        return sylls
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
    if judge is not None:
        syllables = _rebalance_onsets(syllables, is_vowel_char, judge)
    if coda_liquid_capture:
        syllables = _capture_coda_liquids(syllables, is_vowel_char)
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
    spec: Optional[LanguageSpec] = None,
) -> List[str]:
    """Syllabify *word*: registered plugin for *lang* first, naive fallback.

    *diphthongs* reaches the bundled splitter only; a language that ships a
    real syllabifier plugin does not need it.

    *spec* is the language spec the bundled splitter reads its phonotactics
    from — which consonant clusters may open a syllable. When it is not passed
    but *lang* is, the spec is looked up. Without either, the split is
    unconstrained (the historical behaviour).
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
    if spec is None and lang:
        spec = _spec_for(lang)
    max_onset = None
    if spec is not None and not spec.constrain_onsets:
        # The spec has not opted in: its onset inventory has not been checked
        # against the shapes the judge knows, and a language whose onsets
        # exceed them would have every one of them split. Maximise the onset
        # unconstrained, exactly as before.
        spec = None
    if spec is not None and spec.stress is not None \
            and spec.stress.max_onset_declared:
        max_onset = spec.stress.max_onset
    return syllabify(word, diphthongs=diphthongs, spec=spec,
                     max_onset=max_onset)


def _spec_for(lang: str) -> Optional[LanguageSpec]:
    """The loaded spec for *lang*, or ``None`` if there is none to load."""
    try:
        from orthography2ipa.registry import get
        return get(lang)
    except Exception:
        return None


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
    ``antepenult_stress_endings`` → ``rules.default_position``.
    Monosyllables are inherently stressed.

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

    # 4. forced proparoxytone endings — the end-anchored twin of rule 3,
    #    for the two-syllable pre-stressed suffixes (English -ity, -ography).
    for ending in sorted(rules.antepenult_stress_endings, key=len, reverse=True):
        if lowered.endswith(ending):
            return max(0, n - 3)

    # 5. default position, clamped into the word.
    #    Positive values anchor from the start (1 = first syllable).
    #    Negative values anchor from the end (existing behaviour).
    pos = rules.default_position
    if pos >= 1:
        return min(pos - 1, n - 1)
    return max(0, n + pos)


# ═══════════════════════════════════════════════════════════════════════════
# Secondary stress — a second prominence level below the main word accent
# ═══════════════════════════════════════════════════════════════════════════
#
# Word prominence is not a stressed/unstressed switch. A metrical grid has
# levels: syllables are grouped into FEET, every foot has a head, and one of
# those heads is promoted to carry the word accent. The other heads are still
# metrically strong — that is secondary stress (Liberman & Prince 1977, "On
# Stress and Linguistic Rhythm", Linguistic Inquiry 8; Hayes 1995, *Metrical
# Stress Theory*, ch. 2-3).
#
# The engine models exactly one placement rule, the one a spelling can support:
# BINARY FEET BUILT LEFTWARD FROM THE MAIN STRESS (Hayes 1995 ch. 3, binary
# quantity-insensitive foot construction). Every second syllable to the left of
# the main stress is a foot head. Nothing is guessed from morphology, and no
# language is named here: a spec opts in with ``stress.secondary_stress``.

SECONDARY_ALTERNATING = "alternating"

#: IPA secondary-stress mark (U+02CC), written before a secondary foot head.
SECONDARY_MARK = "ˌ"

#: IPA length marks. They belong to the vowel BEFORE them, never to what
#: follows, so a syllable division that leaves one at the head of a syllable
#: has cut inside a long vowel.
_LENGTH_MARKS = "ːˑ"


def _prefix_mark(syll: str, mark: str) -> str:
    """*syll* with *mark* written before its first real segment.

    The naive splitter is a vowel-group splitter over the IPA, so a long
    vowel can be cut in half: ``sɜːkʌmləkjuːʃən`` divides as
    ``sɜ|ːkʌm|lə|kju|ːʃən``, and a mark prefixed blindly lands INSIDE the
    vowel — ``sɜˌːkʌm…``, which claims a syllable starts with half a
    nucleus. A length mark or a combining diacritic at the head of a
    syllable always belongs to the preceding vowel, so the stress mark goes
    after it and the audible syllable still gets marked at its true onset:
    ``sɜːˌkʌm…``.
    """
    i = 0
    while i < len(syll) and (syll[i] in _LENGTH_MARKS
                            or unicodedata.combining(syll[i])):
        i += 1
    return syll[:i] + mark + syll[i:]


def secondary_stress_positions(
    n_syllables: int,
    stress_index: int,
    rules: StressRules,
) -> frozenset:
    """The syllable indices that carry SECONDARY stress, as a 0-based set.

    Empty unless the spec declares ``stress.secondary_stress``. For the
    ``"alternating"`` mode the heads of the binary feet built leftward from
    *stress_index* are returned — ``stress_index - 2``, ``- 4``, … down to 0
    (Hayes 1995 ch. 3). A main stress on the first or second syllable leaves
    no room for a foot and yields the empty set, and so does a
    ``stress_index`` the engine could not place (a negative, end-anchored
    value, or a clitic sentinel): a level below the main accent is only
    definable relative to a known main accent.
    """
    if rules.secondary_stress != SECONDARY_ALTERNATING:
        return frozenset()
    if stress_index is None or stress_index < 0 or n_syllables < 3:
        return frozenset()
    return frozenset(range(stress_index % 2, stress_index - 1, 2))


def apply_stress_mark(
    ipa: str,
    rules: StressRules,
    stress_index: int,
    syllables: Optional[Sequence[str]] = None,
    ipa_syllables: Optional[Sequence[str]] = None,
    mark: Optional[str] = None,
    secondary_indices: Sequence[int] = (),
) -> str:
    """Insert ``rules.stress_mark`` before the stressed syllable of *ipa*.

    *mark*, when given, replaces ``rules.stress_mark`` as the inserted
    character (the pitch-accent-2 caller passes ``rules.accent2_mark``).

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
    secondary_indices : Sequence[int]
        Syllable indices carrying SECONDARY stress (from
        :func:`secondary_stress_positions`), counted the same way as
        *stress_index*. Each is prefixed with ``ˌ`` in the same pass. A
        secondary index that resolves onto the main-stress syllable is
        dropped — one syllable carries one level.
    ipa_syllables : Optional[Sequence[str]]
        Pre-computed syllables OF THE IPA, concatenating to *ipa*. A
        quantity-sensitive caller has already divided the transcription (that
        division is what its weights were read off), and must pass it back:
        the naive :func:`syllabify` used otherwise cuts ``saːliq`` as
        ``sa|ːliq``, so the mark would land *inside* the long vowel.

    Already-marked transcriptions are returned unchanged.
    """
    _mark = mark or rules.stress_mark
    if _mark in ipa or rules.stress_mark in ipa:
        return ipa
    # The spec's diphthongs split the IPA too, not just the spelling: without
    # them a vowel run is one nucleus, so a HIATUS merges and the mark lands a
    # syllable early (⟨coelho⟩ /kuɐʎu/ → ˈkuɐʎu instead of kuˈɐʎu). A language
    # whose diphthongs are written with glides (Portuguese /aj aw/) therefore
    # leaves only true hiatus as a two-vowel run, and it must split.
    ipa_sylls = (list(ipa_syllables) if ipa_syllables
                 else syllabify(ipa, diphthongs=rules.diphthongs,
                                coda_liquid_capture=rules.coda_liquid_capture))
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
            for sec in secondary_indices:
                if 0 <= sec < len(ipa_sylls) and sec != stress_index:
                    ipa_sylls[sec] = _prefix_mark(ipa_sylls[sec],
                                                  SECONDARY_MARK)
            ipa_sylls[stress_index] = _prefix_mark(
                ipa_sylls[stress_index], _mark)
            return "".join(ipa_sylls)
        offset_from_end = max(1, n_orth - stress_index)

    def _target(index: int) -> int:
        """The IPA-syllable slot *index* lands on, by the same anchoring the
        main stress used — so the two levels can never disagree about where a
        syllable is."""
        if index < 0:
            return max(0, len(ipa_sylls) + index)
        n = len(syllables) if syllables is not None else len(ipa_sylls)
        return max(0, len(ipa_sylls) - max(1, n - index))

    target = max(0, len(ipa_sylls) - offset_from_end)
    marked = {target}
    for sec in secondary_indices:
        sec_target = _target(sec)
        if sec_target not in marked:
            marked.add(sec_target)
            ipa_sylls[sec_target] = _prefix_mark(ipa_sylls[sec_target],
                                                 SECONDARY_MARK)
    ipa_sylls[target] = _prefix_mark(ipa_sylls[target], _mark)
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
# division has to be right. The bundled `syllabify` maximises the onset (as far
# as the language licenses one), which for a language whose onsets are legally
# complex still hands medial consonants forward and leaves the
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
