"""Type definitions for orthography2ipa.

The core data model supports:
- Single-parent inheritance (simple dialect trees)
- Multi-ancestor relationships (contact languages, creoles, transitional dialects)
- Weighted ancestry for distance calculations
- Positional grapheme-to-IPA mappings for context-sensitive G2P
- Glottolog classification codes for interoperability
- Attestation time spans for diachronic distance metrics
"""
from __future__ import annotations

from dataclasses import dataclass, field, fields
from enum import Enum
from typing import Dict, FrozenSet, List, Optional, Tuple

# ═══════════════════════════════════════════════════════════════════════════
# Type aliases
# ═══════════════════════════════════════════════════════════════════════════

Grapheme2IPA = Dict[str, List[str]]
"""Orthographic grapheme → list of IPA phoneme candidates."""

GraphemeWeights = Dict[str, List[float]]
"""Orthographic grapheme → per-candidate weights (candidate frequencies),
aligned index-for-index with the grapheme's :data:`Grapheme2IPA` list.
Sparse: only graphemes whose spec used the weighted-object JSON form have
an entry. See :mod:`orthography2ipa.weights`."""

AllophoneMap = Dict[str, List[str]]
"""Underlying phoneme → list of surface realisations."""

PositionalGrapheme2IPA = Dict[str, Dict["GraphemePosition", List[str]]]
"""Grapheme → {position: IPA candidates} for context-sensitive mappings."""


# ═══════════════════════════════════════════════════════════════════════════
# OrthographyStandard — the official published spelling norm, when one exists
# ═══════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class OrthographyStandard:
    """The official, publicly published orthography of a language.

    Many languages are governed by a named spelling norm issued by a language
    academy or state body — the *Acordo Ortográfico da Língua Portuguesa*
    (1990), the Real Academia Galega's *Normas ortográficas*, the RAE's
    *Ortografía de la lengua española*. Where such a norm exists and is public,
    it is the primary authority for what a grapheme *is* in that language, so
    it is recorded as a first-class reference rather than as one link among
    many in :attr:`LanguageSpec.urls`.

    Parameters
    ----------
    name : str
        Title of the standard, in the language's own naming where sensible.
    authority : Optional[str]
        The academy or body that issues it.
    year : Optional[int]
        Year of the edition referenced.
    url : Optional[str]
        Public link to the standard itself.
    notes : str
        Anything a consumer needs to know (e.g. a variety that does not follow
        it, or a competing norm).
    """

    name: str
    authority: Optional[str] = None
    year: Optional[int] = None
    url: Optional[str] = None
    notes: str = ""


# ═══════════════════════════════════════════════════════════════════════════
# TimeSpan — attestation period for a language
# ═══════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class TimeSpan:
    """The attestation period during which a language was spoken.

    Parameters
    ----------
    start_year : int
        Year the language variety is first attested or conventionally begins.
        Use negative values for BCE (e.g. ``-200`` = 200 BCE).
    end_year : Optional[int]
        Year the language variety ceased being spoken / merged into a successor.
        ``None`` indicates a living language (ongoing).

    Examples
    --------
    Old English: ``TimeSpan(450, 1150)``
    Modern Spanish: ``TimeSpan(1500, None)``
    """
    start_year: int
    end_year: Optional[int]  # None = living / ongoing


# ═══════════════════════════════════════════════════════════════════════════
# StressRules — declarative word-stress placement
# ═══════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class StressRules:
    """Declarative rules for primary word-stress placement.

    Captures the semi-predictable, orthography-driven stress systems of
    languages like Portuguese, Spanish or Italian: a default syllable
    position, ending patterns that shift it, and accented vowels that
    override everything.

    Detection precedence (see :func:`orthography2ipa.stress.detect_stress`):

    1. A syllable containing a ``marked_vowels`` character is stressed.
    2. A word ending in one of ``final_stress_endings`` is oxytone.
    3. A word ending in one of ``penult_stress_endings`` is paroxytone.
    4. Otherwise ``default_position`` applies.

    Parameters
    ----------
    default_position : int
        Stressed syllable position. Negative values count from the end:
        ``-1`` final (oxytone), ``-2`` penultimate (paroxytone),
        ``-3`` antepenultimate. Positive values count from the start:
        ``1`` = first syllable (initial stress), ``2`` = second syllable.
        ``0`` is not valid. Range: ``-4`` to ``2`` (excluding ``0``).
    final_stress_endings : Tuple[str, ...]
        Orthographic word endings that attract final stress
        (Portuguese ``-r``, ``-l``, ``-z``, ``-im``, ``-ão`` …).
    penult_stress_endings : Tuple[str, ...]
        Endings that force penultimate stress when the default differs.
    marked_vowels : Tuple[str, ...]
        Vowel characters whose written accent marks the stressed
        syllable (``á é í ó ú â ê ô ã õ``).
    stress_mark : str
        IPA symbol inserted before the stressed syllable (``ˈ``).
    notes : str
        Free-form provenance / convention notes.
    """
    default_position: int = -2
    final_stress_endings: Tuple[str, ...] = ()
    penult_stress_endings: Tuple[str, ...] = ()
    marked_vowels: Tuple[str, ...] = ()
    stress_mark: str = "ˈ"
    notes: str = ""


# ═══════════════════════════════════════════════════════════════════════════
# GraphemePosition — positional contexts for grapheme→IPA disambiguation
# ═══════════════════════════════════════════════════════════════════════════

class GraphemePosition(str, Enum):
    """Positional context in which a grapheme occurs.

    These positions are standard in phonological descriptions and cover
    the major environments where grapheme-to-phoneme mappings diverge.
    They correspond to well-established concepts in phonology:

    - **Word boundaries** (WORD_INITIAL, WORD_FINAL): Documented in
      virtually every phonology textbook. E.g., German Auslautverhärtung
      (final devoicing), English aspiration of word-initial stops.

    - **Intervocalic** (INTERVOCALIC): The V_V environment is the most
      important single context for lenition processes cross-linguistically.
      E.g., Spanish /b d ɡ/ → [β ð ɣ] between vowels; Portuguese
      intervocalic /s/ → [z]; Latin intervocalic voicing > Romance.

    - **Cross-word intervocalic** (INTERVOCALIC_CROSS_WORD): Sandhi
      environments where a consonant at a word boundary is flanked by
      vowels across words. E.g., French liaison, Portuguese resyllabification
      of final /s/ before a vowel-initial word.

    - **Syllable positions** (ONSET, NUCLEUS, CODA): The three structural
      positions of a syllable. E.g., English /l/ is clear [l] in onset
      but dark [ɫ] in coda; Korean obstruent neutralisation in coda.

    - **DEFAULT**: Fallback when no specific positional context applies.
      Equivalent to the existing context-free ``graphemes`` mapping.

    References
    ----------
    - Kenstowicz, M. (1994). *Phonology in Generative Grammar*. Blackwell.
    - Hayes, B. (2009). *Introductory Phonology*. Wiley-Blackwell.
    - Zsiga, E. (2013). *The Sounds of Language*. Wiley-Blackwell.
    """
    WORD_INITIAL = "word_initial"
    """Absolute word-initial position (#_).
    E.g., English ⟨k⟩ → [kʰ] word-initially (aspiration);
    German ⟨s⟩ → [z] word-initially before vowels."""

    WORD_FINAL = "word_final"
    """Absolute word-final position (_#).
    E.g., German ⟨d⟩ → [t] word-finally (Auslautverhärtung);
    Portuguese ⟨s⟩ → [ʃ] word-finally (Lisbon)."""

    INTERVOCALIC = "intervocalic"
    """Between two vowels within the same word (V_V).
    E.g., Spanish ⟨b⟩ → [β] intervocalically (lenition);
    Portuguese ⟨s⟩ → [z] between vowels; American English ⟨t⟩ → [ɾ]."""

    INTERVOCALIC_CROSS_WORD = "intervocalic_cross_word"
    """Between vowels across a word boundary (V#_V or V_#V).
    E.g., French liaison ⟨s⟩ → [z] before vowel-initial word;
    Portuguese coda ⟨s⟩ → [z] before vowel-initial next word."""

    ONSET = "onset"
    """Syllable onset position (beginning of syllable).
    E.g., English ⟨l⟩ → [l] (clear l) in onset;
    Korean aspirated stops in onset."""

    NUCLEUS_STRESSED = "nucleus_stressed"
    """Syllable nucleus position (typically a vowel).
    This is the defining sound of the syllable."""

    NUCLEUS_UNSTRESSED = "nucleus_unstressed"
    """Syllable nucleus position (typically a vowel).
    E.g., reduced vowels in unstressed nuclei — Portuguese ⟨e⟩ → [ɨ]
    vs. [ɛ] in stressed nucleus; English ⟨a⟩ → [ə] in unstressed."""

    CODA = "coda"
    """Syllable coda position (end of syllable).
    E.g., English ⟨l⟩ → [ɫ] (dark l) in coda;
    Korean obstruent neutralisation in coda;
    Portuguese ⟨l⟩ → [w] in coda (Brazilian)."""

    PRETONIC = "pretonic"
    """default value when before the stressed/tonic syllable."""

    POSTTONIC = "posttonic"
    """default value when after the stressed/tonic syllable."""

    BEFORE_VOWEL = "before_vowel"

    AFTER_VOWEL = "after_vowel"

    BEFORE_CONSONANT = "before_consonant"

    AFTER_CONSONANT = "after_consonant"

    BEFORE_A = "before_a"
    BEFORE_E = "before_e"
    BEFORE_I = "before_i"
    BEFORE_O = "before_o"
    BEFORE_U = "before_u"

    BEFORE_FRONT_VOWEL = "before_front_vowel"
    """Before a *front* vowel letter (``e i y`` + accented/rounded variants,
    membership decided by :func:`orthography2ipa.vowels.is_front_vowel`).
    The class-level condition for Romance c/g softening: a single
    ``BEFORE_FRONT_VOWEL`` entry replaces enumerating ``BEFORE_E`` +
    ``BEFORE_I`` + every accented ⟨e⟩/⟨i⟩. An exact per-letter position
    (e.g. ``BEFORE_E``) declared for the same grapheme still wins over
    this class position."""

    BEFORE_BACK_VOWEL = "before_back_vowel"
    """Before a *back* vowel letter (``a o u`` + accented variants,
    membership decided by :func:`orthography2ipa.vowels.is_back_vowel`).
    The class-level condition for the "hard" realisation in Romance
    c/g softening. Exact per-letter positions win over it."""

    AFTER_FRONT_VOWEL = "after_front_vowel"
    """After a *front* vowel letter (mirrors :attr:`BEFORE_FRONT_VOWEL`).
    E.g. German ⟨ch⟩ → [ç] (Ich-Laut) after front vowels. Exact per-letter
    positions (``AFTER_E`` …) win over it."""

    AFTER_BACK_VOWEL = "after_back_vowel"
    """After a *back* vowel letter (mirrors :attr:`BEFORE_BACK_VOWEL`).
    E.g. German ⟨ch⟩ → [x] (Ach-Laut) after back vowels. Exact per-letter
    positions (``AFTER_A`` …) win over it."""

    BEFORE_PALATAL = "before_palatal"
    """Before a *palatal / palato-alveolar consonant* — the consonant-side
    mirror of :attr:`BEFORE_FRONT_VOWEL`. Membership is decided by the IPA the
    following grapheme maps to (:func:`orthography2ipa.vowels.is_palatal_consonant`
    — ``ʎ ɲ ʃ ʒ j`` and the affricates ``tʃ``/``dʒ`` …), not by its written
    letter, so a single ``BEFORE_PALATAL`` entry covers every digraph that
    produces a palatal (⟨lh⟩→ʎ, ⟨nh⟩→ɲ, ⟨ch⟩→ʃ, ⟨x⟩, ⟨j⟩). The class-level
    condition for e.g. European Portuguese stressed ⟨e⟩ → [ɐ] before ⟨lh⟩. An
    exact per-letter position declared for the same grapheme still wins over
    this class position."""

    AFTER_PALATAL = "after_palatal"
    """After a *palatal / palato-alveolar consonant* (mirrors
    :attr:`BEFORE_PALATAL`; membership via
    :func:`orthography2ipa.vowels.is_palatal_consonant` on the preceding
    grapheme's IPA). Exact per-letter positions win over it."""

    AFTER_A = "after_a"
    """Preceding token's grapheme starts with ``a`` (mirrors BEFORE_A).
    E.g., German ⟨ch⟩ after back vowels ``a/o/u`` → [x] (Ach-Laut)."""

    AFTER_E = "after_e"
    """Preceding token's grapheme starts with ``e`` (mirrors BEFORE_E).
    E.g., German ⟨ch⟩ after front vowels ``e/i`` → [ç] (Ich-Laut)."""

    AFTER_I = "after_i"
    """Preceding token's grapheme starts with ``i`` (mirrors BEFORE_I)."""

    AFTER_O = "after_o"
    """Preceding token's grapheme starts with ``o`` (mirrors BEFORE_O)."""

    AFTER_U = "after_u"
    """Preceding token's grapheme starts with ``u`` (mirrors BEFORE_U)."""

    CONSONANTAL = "consonantal"
    VOCALIC = "vocalic"

    DEFAULT = "default"
    """Fallback when no specific positional context applies."""

    NUCLEUS = "nucleus"
    """Generic syllable nucleus (when stress is not distinguished)."""


# ═══════════════════════════════════════════════════════════════════════════
# AncestorRole
# ═══════════════════════════════════════════════════════════════════════════

class AncestorRole(str, Enum):
    """How an ancestor language relates to its descendant."""

    PARENT = "parent"
    """Primary genetic descent.  The main lineage: Latin -> Spanish.
    Every language has at most one PARENT.  Weight typically 0.7-1.0."""

    PARENT_DIALECT = "parent_dialect"
    """Direct dialectal ancestor within the same language.
    E.g. a regional variety descending from a broader standard."""

    PROTO_LANGUAGE = "proto_language"
    """Reconstructed common ancestor at the top of a lineage.
    E.g. Proto-Indo-European, Proto-Germanic, Proto-Semitic."""

    ANCESTOR = "ancestor"
    """Earlier historical stage of the same lineage that is not the
    immediate parent.  E.g. Old Spanish in the ancestry of modern Spanish."""

    SUBSTRATE = "substrate"
    """Language of population BEFORE adopting current language.
    E.g. Basque substrate in Castilian (f->h), Gaulish in French."""

    SUPERSTRATE = "superstrate"
    """Language of dominant group eventually ABSORBED into local language.
    E.g. Frankish in French, Norse in English, Arabic in Mozarabic."""

    ADSTRATE = "adstrate"
    """Ongoing contact influence from neighboring language at equal status.
    E.g. Arabic adstrate on Ibero-Romance (4000+ loanwords)."""

    LEXIFIER = "lexifier"
    """Language providing most vocabulary in a creole/pidgin.
    E.g. Portuguese lexifier of Papiamento, English of Tok Pisin."""

    CREOLE_BASE = "creole_base"
    """Substrate language contributing to creole formation.
    E.g. West African languages as base for Atlantic creoles."""

    RELATED = "related"
    """Sister language with shared features but no direct descent.
    Used for typological comparison rather than inheritance."""


# ═══════════════════════════════════════════════════════════════════════════
# QualityTier — data maturity classification
# ═══════════════════════════════════════════════════════════════════════════

class QualityTier(str, Enum):
    """Classification of data quality and completeness for a language spec."""

    STUB = "stub"
    """Code + name + family + script only."""

    SKELETON = "skeleton"
    """Graphemes + allophones from auto-generation (unvalidated)."""

    RESEARCH = "research"
    """Validated against published phonology; positional rules present."""

    PRODUCTION = "production"
    """Full coverage, regression-tested, cited sources."""


# ═══════════════════════════════════════════════════════════════════════════
# ScriptType — typological classification of writing systems
# ═══════════════════════════════════════════════════════════════════════════

class ScriptType(str, Enum):
    """Typological classification of a writing system."""

    ALPHABET = "alphabet"
    """Latin, Cyrillic, Greek, Armenian, Georgian."""

    ABJAD = "abjad"
    """Arabic, Hebrew — consonants primary, vowels optional."""

    ABUGIDA = "abugida"
    """Devanagari, Bengali, Tamil, Thai — inherent vowel."""

    SYLLABARY = "syllabary"
    """Kana, Cherokee."""

    LOGOGRAPHIC = "logographic"
    """Hanzi / CJK ideographs."""

    FEATURAL = "featural"
    """Hangul."""

    MIXED = "mixed"
    """Japanese (logographic + syllabary)."""

    RECONSTRUCTION = "reconstruction"
    """IPA-based phonological reconstruction for unwritten/extinct languages
    (PIE, Proto-Germanic, Proto-Semitic, etc.). Grapheme keys ARE the IPA
    transcription convention. Enables phonetic distance calculations without
    implying any historical script existed."""


# ═══════════════════════════════════════════════════════════════════════════
# LinguisticSource — bibliographic reference for phonological decisions
# ═══════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class WeightedDistance:
    """Result of ``weighted_full_distance()`` with all component scores visible.

    Attributes
    ----------
    inventory : float
        Feature-mean inventory distance in [0, 1].
    grapheme : float
        Mean IPA distance for shared graphemes in [0, 1].
    allophone : float
        Jaccard allophone *similarity* in [0, 1] (higher = more overlap).
    ancestry : float
        Ancestry *similarity* in [0, 1] (higher = more related).
    combined : float
        Weighted combined *distance* in [0, 1].
    weights : Tuple[float, float, float, float]
        The component weights used: ``(w_inventory, w_grapheme, w_allophone, w_ancestry)``.
    """

    inventory: float
    grapheme: float
    allophone: float
    ancestry: float
    temporal: Optional[float]
    """Temporal distance in [0, 1], or ``None`` if timespan data is unavailable."""
    combined: float
    weights: Tuple[float, float, float, float, float]
    """Component weights: ``(w_inventory, w_grapheme, w_allophone, w_ancestry, w_temporal)``."""


@dataclass(frozen=True)
class LinguisticSource:
    """A bibliographic reference for a phonological decision.

    Parameters
    ----------
    id : str
        Short cite key, e.g. ``"wells1982"``.
    author : str
        Author(s), e.g. ``"Wells, J.C."``.
    year : int
        Publication year.
    title : str
        Full title of the work.
    publisher : Optional[str]
        Publisher name, if applicable.
    url : Optional[str]
        URL or DOI for online resources; ``None`` for print-only works.
    wikipedia_url : Optional[str]
        Wikipedia article URL for this source or the phenomenon it describes;
        intended as a quick human reference, not a citable source.
    pages : Optional[str]
        Specific page range referenced, e.g. ``"pp. 45-72"``.
    notes : Optional[str]
        Optional annotation about what this source supports.
    """

    id: str
    author: str
    year: int
    title: str
    publisher: Optional[str] = None
    url: Optional[str] = None
    wikipedia_url: Optional[str] = None
    pages: Optional[str] = None
    notes: Optional[str] = None


# ═══════════════════════════════════════════════════════════════════════════
# SandhiRule — cross-word-boundary phonological rule
# ═══════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class SandhiRule:
    """A single sandhi / liaison rule applied across word boundaries.

    Parameters
    ----------
    id : str
        Unique identifier (e.g. ``"FR_LIAISON_Z"``).
    name : str
        Human-readable description.
    left_context : str
        Regex on IPA of word-final segment(s).
    right_context : str
        Regex on IPA of next-word-initial segment(s).
    transform : str
        Replacement pattern applied to the left boundary.
    obligatory : bool
        Whether this rule applies unconditionally.
    notes : str
        Optional notes.
    """
    id: str
    name: str
    left_context: str
    right_context: str
    transform: str
    obligatory: bool = True
    notes: str = ""


# ═══════════════════════════════════════════════════════════════════════════
# AllophoneRule — post-lexical, context-conditioned phoneme→surface rewrite
# ═══════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class AllophoneRule:
    """One declarative, context-conditioned ``phoneme → surface`` rewrite.

    This is the mirror of ``positional_graphemes`` on the *phoneme* side: it
    is the POST-lexical half of the library's "two maps" (orthography →
    phoneme → surface allophone). Where ``positional_graphemes`` conditions
    a grapheme's IPA on orthographic context, an ``AllophoneRule`` conditions
    a selected phoneme's *surface* realisation on phonological context —
    syllable position, stress, word position and neighbouring segments.

    Rules are **pure data** (no code in specs). They compile into a
    :class:`~orthography2ipa.rescorer.LatticeRescorer`
    (:class:`orthography2ipa.allophony.AllophoneRescorer`) that runs as the
    engine's post-lexical pass — after positional/weight phoneme selection,
    before stress-mark insertion and cross-word sandhi.

    A rule fires for a lattice slot when the slot's chosen phoneme is one of
    :attr:`phonemes` **and every declared condition holds** (all conditions
    are ANDed; a condition left ``None`` / empty is "don't care"). When it
    fires the slot's matching candidate is rewritten to :attr:`surface` at
    the same beam cost — a deterministic realisation, not a new beam branch.

    The condition vocabulary is deliberately small but expressive enough to
    state the cross-linguistically common post-lexical processes:

    - **Final-obstruent devoicing** — ``word_final=True``.
    - **Unstressed vowel reduction** — ``stress="unstressed"`` (engine path
      only; stress is unavailable to the standalone tokenizer, so a
      stress-conditioned rule is inert there, exactly like the
      stress-conditioned positional rules).
    - **Intervocalic flapping** — ``preceded_by="vowel"`` +
      ``followed_by="vowel"``.
    - **Nasal place assimilation** — ``followed_by_phoneme=("k", "ɡ")`` (→
      velar) or ``("p", "b", "m")`` (→ labial), matching the *next slot's*
      chosen phoneme rather than its grapheme.

    Parameters
    ----------
    id : str
        Unique identifier (e.g. ``"CA_DEVOICE_D"``). Used for id-keyed
        inheritance overlay (:class:`InheritanceMode.OVERLAY_BY_ID`), exactly
        like :class:`SandhiRule`: a child spec redeclaring this ``id``
        replaces the inherited rule in place; a new ``id`` is appended.
    phonemes : Tuple[str, ...]
        The underlying phoneme(s) this rule targets. A bare string is
        accepted and normalised to a 1-tuple.
    surface : str
        The surface realisation the matched phoneme is rewritten to.
    word_initial, word_final : Optional[bool]
        Require the grapheme to be word-initial / word-final (or, when
        ``False``, require it *not* to be). ``None`` = don't care.
    stress : Optional[str]
        ``"stressed"`` or ``"unstressed"`` — require the grapheme's syllable
        to carry (or not carry) primary stress. Needs engine-supplied stress
        context; inert on the standalone tokenizer path.
    syllable_position : Optional[str]
        ``"onset"``, ``"coda"`` or ``"nucleus"``. A vowel is a nucleus; a
        consonant followed by a vowel (same word) is an onset, otherwise a
        coda (maximal-onset heuristic).
    preceded_by, followed_by : Optional[str]
        A neighbouring-*grapheme* class the previous / next grapheme must
        match: ``"vowel"``, ``"consonant"``, ``"front_vowel"``,
        ``"back_vowel"``, ``"palatal"`` (a palatal / palato-alveolar
        consonant, decided by the neighbour's IPA — the mirror of the
        ``BEFORE_PALATAL`` position) or ``"word_boundary"`` (no neighbour).
        Predicates delegate to :mod:`orthography2ipa.vowels`.
    preceded_by_phoneme, followed_by_phoneme : Tuple[str, ...]
        The chosen phoneme of the previous / next lattice slot must be one of
        these — the *phoneme*-level neighbour condition (for e.g. nasal place
        assimilation, which conditions on the following consonant's place).
        Empty = don't care.
    grapheme : Optional[Tuple[str, ...]]
        Require the slot's own *source grapheme* to be one of these (matched
        case-insensitively). This lets a rule target a surface shift that
        depends on where the phoneme came from — e.g. Portuguese unstressed
        ⟨o⟩ reduces to [u], but before a coda nasal that reduced [u] lowers
        back to [o] ([õ]) whereas a lexical ⟨u⟩ stays [ũ]; both are the same
        phoneme [u], so only the source grapheme distinguishes them. ``None``
        / empty = don't care.
    notes : str
        Free-form provenance / convention notes.
    """
    id: str
    phonemes: Tuple[str, ...]
    surface: str
    word_initial: Optional[bool] = None
    word_final: Optional[bool] = None
    stress: Optional[str] = None
    syllable_position: Optional[str] = None
    preceded_by: Optional[str] = None
    followed_by: Optional[str] = None
    preceded_by_phoneme: Tuple[str, ...] = ()
    followed_by_phoneme: Tuple[str, ...] = ()
    grapheme: Optional[Tuple[str, ...]] = None
    notes: str = ""

    def __post_init__(self) -> None:
        if isinstance(self.phonemes, str):
            object.__setattr__(self, "phonemes", (self.phonemes,))
        else:
            object.__setattr__(self, "phonemes", tuple(self.phonemes))
        object.__setattr__(
            self, "preceded_by_phoneme", tuple(self.preceded_by_phoneme))
        object.__setattr__(
            self, "followed_by_phoneme", tuple(self.followed_by_phoneme))
        if self.grapheme is not None:
            object.__setattr__(
                self, "grapheme",
                tuple(g.lower() for g in self.grapheme))
        if self.stress is not None and self.stress not in (
                "stressed", "unstressed"):
            raise ValueError(
                f"AllophoneRule {self.id!r}: stress must be 'stressed', "
                f"'unstressed' or None, got {self.stress!r}")
        if self.syllable_position is not None and self.syllable_position not in (
                "onset", "coda", "nucleus"):
            raise ValueError(
                f"AllophoneRule {self.id!r}: syllable_position must be "
                f"'onset', 'coda', 'nucleus' or None, "
                f"got {self.syllable_position!r}")
        _classes = ("vowel", "consonant", "front_vowel", "back_vowel",
                    "palatal", "word_boundary")
        for attr in ("preceded_by", "followed_by"):
            val = getattr(self, attr)
            if val is not None and val not in _classes:
                raise ValueError(
                    f"AllophoneRule {self.id!r}: {attr} must be one of "
                    f"{_classes} or None, got {val!r}")


# ═══════════════════════════════════════════════════════════════════════════
# Ancestor
# ═══════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class Ancestor:
    """A single ancestry link from a language to one of its ancestors.

    Parameters
    ----------
    code : str
        Language code of the ancestor (must exist in registry).
    role : AncestorRole
        Type of historical relationship.
    weight : float
        Approximate contribution to descendant's phonological system
        [0.0, 1.0].  Guidelines:
        - PARENT: 0.7-1.0 (dominant genetic lineage)
        - SUBSTRATE: 0.05-0.30 (phonological/structural traces)
        - SUPERSTRATE: 0.10-0.40 (heavy lexical / some structural)
        - ADSTRATE: 0.05-0.20 (ongoing contact)
        - LEXIFIER: 0.50-0.80 (vocabulary source for creoles)
        - CREOLE_BASE: 0.20-0.50 (grammar source for creoles)
    notes : str
        Optional notes about this specific relationship.
    """
    code: str
    role: AncestorRole
    weight: float = 0.5
    notes: str = ""

    def __post_init__(self):

        # Normalise str to AncestorRole
        if not isinstance(self.role, AncestorRole):
            object.__setattr__(self, "role", AncestorRole(self.role))

        # Normalise list to str
        if isinstance(self.notes, list):
            object.__setattr__(self, "notes", "\n".join(self.notes))

    def __repr__(self) -> str:
        return f"Ancestor({self.code!r}, {self.role.value}, w={self.weight:.2f})"


# ═══════════════════════════════════════════════════════════════════════════
# InheritanceMode — explicit, enforced manifest of how each LanguageSpec
# field participates (or doesn't) in the ``*_base`` / ancestry inheritance
# chain resolved by :mod:`orthography2ipa.json_loader`.
# ═══════════════════════════════════════════════════════════════════════════

class InheritanceMode(str, Enum):
    """How a ``LanguageSpec`` field is resolved when a spec declares a base
    (``graphemes_base`` / ``allophones_base`` / ``positional_graphemes_base``)
    or an ancestry ``parent``.
    """

    BASE_MERGE = "base_merge"
    """Dict-valued field. Own values overlay the resolved base's values key
    by key (``{**base, **own}``). Used by ``graphemes``, ``allophones`` and
    ``positional_graphemes``."""

    OVERLAY_BY_ID = "overlay_by_id"
    """Sequence of id-keyed rule objects. The base's rules are inherited in
    order; own rules with a matching ``id`` replace the inherited rule
    in-place, own rules with a new ``id`` are appended. Used by
    ``sandhi_rules`` and ``allophone_rules`` — a blind dict-splat is wrong
    here because rules are identified by ``id``, not by a single dict key.

    ``allophone_rules`` inherits this way because a post-lexical process is
    typically a property of a whole language: Catalan final-obstruent
    devoicing and nasal place assimilation hold in every Catalan variety, so
    a dialect that sets ``graphemes_base`` to the standard should inherit the
    realisation rules for free while still being able to override a single
    rule by ``id`` (e.g. a dialect that resists a specific devoicing) or
    append its own — exactly the id-keyed overlay ``sandhi_rules`` needs."""

    NOT_INHERITED = "not_inherited"
    """Own-file-only by design. The field never propagates through
    inheritance even though a base/parent is set — this is a deliberate
    modeling choice (documented per-field), not an oversight. Used by
    ``stress``, ``word_exceptions`` and ``grapheme_weights``.

    ``grapheme_weights`` is own-only for two reasons. First, candidate
    weights are *corpus-frequency* data specific to one variety — the
    relative frequency of ⟨ou⟩ → /aʊ/ vs /uː/ in en-GB is not the same
    statistic as in en-US, so a child variety must cite its own weights
    rather than silently inherit its parent's. Second, keeping weights
    off the inheritance edge means a child that pulls its ``graphemes``
    from a weighted parent via ``graphemes_base`` still gets the plain
    IPA lists and *rank* ordering — its transcription is byte-identical
    to before weights existed. Within one spec the weights ride inside
    the grapheme's own weighted-object JSON value, so a grapheme's IPA
    list and its weights are always authored (and overridden) together;
    the ``graphemes``/``grapheme_weights`` split is purely an internal
    representation that keeps ``spec.graphemes`` a plain ``list[str]``
    map for every existing consumer."""

    OWN_ONLY = "own_only"
    """Identity / bibliographic / classification field that never
    participates in inheritance resolution at all (e.g. ``code``, ``name``,
    ``family``, ``sources``, ``timespan``)."""


FIELD_INHERITANCE: Dict[str, InheritanceMode] = {
    "code": InheritanceMode.OWN_ONLY,
    "name": InheritanceMode.OWN_ONLY,
    "family": InheritanceMode.OWN_ONLY,
    "script": InheritanceMode.OWN_ONLY,
    "graphemes": InheritanceMode.BASE_MERGE,
    "allophones": InheritanceMode.BASE_MERGE,
    "parent": InheritanceMode.OWN_ONLY,
    "ancestors": InheritanceMode.OWN_ONLY,
    "positional_graphemes": InheritanceMode.BASE_MERGE,
    "glottolog_code": InheritanceMode.OWN_ONLY,
    "notes": InheritanceMode.OWN_ONLY,
    "quality": InheritanceMode.OWN_ONLY,
    "script_type": InheritanceMode.OWN_ONLY,
    "inherent_vowel": InheritanceMode.OWN_ONLY,
    "phonemes": InheritanceMode.OWN_ONLY,
    "iso639_3": InheritanceMode.OWN_ONLY,
    "wikidata_qid": InheritanceMode.OWN_ONLY,
    "phoible_id": InheritanceMode.OWN_ONLY,
    "wals_code": InheritanceMode.OWN_ONLY,
    "sandhi_rules": InheritanceMode.OVERLAY_BY_ID,
    "allophone_rules": InheritanceMode.OVERLAY_BY_ID,
    "tone_inventory": InheritanceMode.OWN_ONLY,
    "sources": InheritanceMode.OWN_ONLY,
    "wikipedia": InheritanceMode.OWN_ONLY,
    "urls": InheritanceMode.OWN_ONLY,
    "orthography_standard": InheritanceMode.OWN_ONLY,
    "timespan": InheritanceMode.OWN_ONLY,
    "stress": InheritanceMode.NOT_INHERITED,
    "word_exceptions": InheritanceMode.NOT_INHERITED,
    "grapheme_weights": InheritanceMode.NOT_INHERITED,
    "clade": InheritanceMode.OWN_ONLY,
    "family_path": InheritanceMode.OWN_ONLY,
}
"""Explicit, enforced registry of every ``LanguageSpec`` field's inheritance
behavior. ``tests/test_types.py`` asserts this covers every field returned by
``dataclasses.fields(LanguageSpec)`` — a field added to the dataclass without
a registered decision here fails that test, which is the forcing function:
no field can silently skip inheritance resolution again the way
``sandhi_rules`` and ``word_exceptions`` did before this registry existed.
"""


def fields_missing_inheritance_decision() -> FrozenSet[str]:
    """Return the set of ``LanguageSpec`` field names absent from
    :data:`FIELD_INHERITANCE`. Empty when the manifest is complete."""
    declared = {f.name for f in fields(LanguageSpec)}
    return frozenset(declared - set(FIELD_INHERITANCE.keys()))


# ═══════════════════════════════════════════════════════════════════════════
# LanguageSpec
# ═══════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class LanguageSpec:
    """Complete phonological specification for one language / variety.

    The ``positional_graphemes`` field provides optional context-sensitive
    IPA mappings that override the base ``graphemes`` for specific
    phonological positions.  When absent or empty, the base ``graphemes``
    mapping is used for all positions (backward-compatible).

    The ``glottolog_code`` field provides an optional Glottolog languoid
    identifier for cross-referencing with the Glottolog classification
    (e.g. ``'cast1244'`` for Castilian). This enables interoperability
    with Glottolog's genealogical database while keeping our own BCP-47
    codes as primary identifiers.
    """

    code: str
    """BCP-47 or ISO 639 code."""

    name: str
    """Human-readable name."""

    family: str
    """Language family, as a classification path (``"Indo-European > Italic >
    Romance > Ibero-Romance"``).

    Derived, not hand-maintained: the loader joins :attr:`family_path`, which
    it reads off the clade nodes on the ancestry chain. A JSON spec may still
    carry an explicit ``family`` string, which then wins — that escape hatch
    is for groupings that are not genetic clades (creoles, constructed
    languages, isolates, unclassified languages)."""

    script: str
    """Primary script."""

    graphemes: Grapheme2IPA
    """Orthographic grapheme -> canonical IPA phoneme(s).
    This is the context-free DEFAULT mapping, used when no positional
    override is available."""

    allophones: AllophoneMap
    """Phoneme -> contextual surface realisations."""

    phonemes: Tuple[str, ...] = ()
    """The language's phoneme inventory — the sounds it HAS, stated directly.

    Deliberately independent of :attr:`graphemes`. A language's sounds are not a
    property of its writing system: most of the world's languages have a
    documented phonology and NO orthography at all (PHOIBLE catalogues inventories
    for thousands of them), and a logographic script encodes no sound, so reading
    the inventory out of the spelling cannot work for either.

    When empty, the inventory is DERIVED from ``graphemes`` — which is what every
    spec did before this field existed, and what leaves them unchanged. That
    derivation is a fallback, not the definition: it reads the sounds out of the
    spelling, which is backwards, and it is why a reconstructed language had to
    fake an identity orthography (Proto-Indo-European declaring ``p`` -> [p])
    merely to have an inventory at all.
    """

    parent: Optional[str] = None
    """Primary parent code (backward-compatible shorthand).
    If ancestors is also set, should match the PARENT-role ancestor."""

    ancestors: Tuple[Ancestor, ...] = ()
    """Full ancestry specification.  Encodes multiple parents,
    substrates, superstrates, contact languages, creole origins.
    If empty but parent is set, a default PARENT ancestor is inferred."""

    positional_graphemes: PositionalGrapheme2IPA = None  # type: ignore[assignment]
    """Optional positional grapheme→IPA overrides.

    Maps grapheme keys to dicts of ``{GraphemePosition: [IPA candidates]}``.
    Only graphemes whose IPA mapping changes by position need entries here.
    For any grapheme+position combination not present, the base ``graphemes``
    mapping is used as fallback.

    Example::

        positional_graphemes = {
            "s": {
                GraphemePosition.WORD_INITIAL: ["s"],
                GraphemePosition.INTERVOCALIC: ["z"],
                GraphemePosition.WORD_FINAL: ["ʃ"],
            },
            "l": {
                GraphemePosition.ONSET: ["l"],
                GraphemePosition.CODA: ["w"],
            },
        }
    """

    glottolog_code: Optional[str] = None
    """Optional Glottolog languoid code (e.g. 'cast1244' for Castilian,
    'west2813' for West Iberian). Enables cross-referencing with
    Glottolog's genealogical classification database.
    See https://glottolog.org for the full catalogue."""

    notes: str = ""
    """Free-form notes."""

    quality: QualityTier = QualityTier.RESEARCH
    """Data maturity tier.  Existing production specs default to RESEARCH."""

    script_type: ScriptType = ScriptType.ALPHABET
    """Typological classification of the primary writing system."""

    inherent_vowel: Optional[str] = None
    """For abugidas — the vowel assumed when no vowel mark is present
    (e.g. ``"ə"`` for Hindi, ``"a"`` for Sanskrit)."""

    iso639_3: Optional[str] = None
    """ISO 639-3 three-letter code for PHOIBLE/Glottolog cross-referencing."""

    wikidata_qid: Optional[str] = None
    """Optional Wikidata item id (e.g. ``"Q1321"`` for Spanish). The hub of the
    linked-data graph: one QID resolves to this language's Glottolog code,
    ISO 639-3 code, PHOIBLE inventories, WALS entry and Wikipedia articles in
    every edition. See https://www.wikidata.org."""

    phoible_id: Optional[str] = None
    """Optional PHOIBLE identifier for the language's attested phoneme
    inventories. PHOIBLE catalogues cross-linguistic phoneme inventories and is
    the reference against which a spec's emitted phoneme set can be validated.
    See https://phoible.org."""

    wals_code: Optional[str] = None
    """Optional WALS (World Atlas of Language Structures) code, for typological
    cross-referencing. See https://wals.info."""

    sandhi_rules: Tuple[SandhiRule, ...] = ()
    """Cross-word-boundary phonological rules (liaison, sandhi)."""

    allophone_rules: Tuple["AllophoneRule", ...] = ()
    """Post-lexical, context-conditioned ``phoneme → surface`` rewrites.

    The POST-lexical half of the "two maps": where ``positional_graphemes``
    conditions orthography→phoneme, these condition phoneme→surface allophone
    on syllable position, stress, word position and neighbouring segments.
    They compile into a
    :class:`~orthography2ipa.rescorer.LatticeRescorer`
    (:class:`orthography2ipa.allophony.AllophoneRescorer`) applied by
    :class:`~orthography2ipa.g2p.G2P` after phoneme selection and before
    stress/sandhi. Empty (the default) for every spec that has not opted in,
    so the field is a no-op — the engine behaves byte-identically. Inherited
    by id-keyed overlay (:class:`InheritanceMode.OVERLAY_BY_ID`), like
    ``sandhi_rules``. See :mod:`orthography2ipa.allophony` and
    ``docs/allophony.md``."""

    tone_inventory: Optional[Dict[str, str]] = None
    """Optional tone inventory: IPA tone mark → label
    (e.g. ``{"˥": "high", "˧˥": "rising"}``)."""

    sources: Tuple["LinguisticSource", ...] = field(default_factory=tuple)
    """Bibliographic references supporting the phonological decisions in this spec."""

    wikipedia: Tuple[str, ...] = ()
    """Wikipedia article URLs for this language or dialect.

    Multiple URLs are encouraged — link articles in different languages or
    covering distinct aspects (phonology, history, dialectology) to give a
    complete cross-reference picture.  Order: English article first, then
    by relevance."""

    urls: Tuple[str, ...] = ()
    """Other reference URLs — Glottolog, Ethnologue, dialect articles.
    Wikipedia articles belong in :attr:`wikipedia`; the official spelling norm
    belongs in :attr:`orthography_standard`."""

    orthography_standard: Optional["OrthographyStandard"] = None
    """The official published orthography, where the language has one.

    ``None`` means either that no official norm exists (many varieties and all
    reconstructions) or that this spec follows its parent's — a dialect that
    spells by its standard language's norm simply omits the field, since a
    standard is a property of the language, not of every dialect of it."""

    timespan: Optional["TimeSpan"] = None
    """Attestation period.  ``None`` if unknown.

    For living languages, set ``end_year=None``.  For historical/extinct
    languages, set both ``start_year`` and ``end_year``.  Enables
    :func:`~orthography2ipa.distance.temporal_distance` and
    ancestor weight decay in
    :func:`~orthography2ipa.distance.ancestry_similarity`."""

    stress: Optional["StressRules"] = None
    """Declarative primary-stress placement rules.  ``None`` when the
    language has no (encoded) predictable stress system.

    Not inherited through ancestry — each spec declares its own block;
    consumed by :func:`orthography2ipa.stress.detect_stress`."""

    grapheme_weights: Optional[GraphemeWeights] = None
    """Optional per-candidate weights for :attr:`graphemes`.

    Sparse map: an entry exists only for graphemes whose spec JSON used
    the weighted-object form ``{"ipa": [...], "weights": [...]}``. Each
    value is aligned index-for-index with that grapheme's IPA list and
    represents candidate frequency (from cited corpora). When a grapheme
    has no entry here the beam uses uniform-descending *rank* cost, which
    is byte-identical to the behaviour that predates weights.

    Not inherited through ancestry — see :data:`FIELD_INHERITANCE` /
    :class:`InheritanceMode.NOT_INHERITED`. The beam turns a weight into
    a ``-log(p)`` cost via :func:`orthography2ipa.weights.candidate_base_costs`."""

    clade: bool = False
    """True for a classification-only node (``Romance``, ``West Germanic``).

    A clade carries no phonology — empty ``graphemes`` / ``allophones`` — and
    is never a data-inheritance source: the loader walks *through* clade nodes
    when it looks for the nearest data-bearing ancestor. Clades exist purely
    as steps in the ancestry chain, which is where :attr:`family_path` (and
    therefore :attr:`family`) is read from.

    A reconstructed PROTO-LANGUAGE (Proto-Bantu, Hispanic Vulgar Latin) is
    *not* a clade: it is a language, it carries graphemes, and it legitimately
    acts as a data ancestor."""

    family_path: Tuple[str, ...] = ()
    """Derived classification path — the names of the clade nodes on this
    spec's ancestry chain, broadest first (``("Indo-European", "Italic",
    "Romance", "Ibero-Romance")``). Computed by the loader by walking
    ``parent``; never hand-written in JSON."""

    word_exceptions: Optional[Dict[str, str]] = None
    """Whole-word IPA overrides for a closed set of irregular words that
    the rule system (flat graphemes / positional_graphemes) cannot
    express cleanly — e.g. monosyllabic function words whose sole vowel
    is a positionally-conditioned e caduc (French ``le`` → ``lə``) that
    would otherwise be silenced by a ``word_final`` rule tuned for
    polysyllables. Keys are lowercase orthographic word forms; matched
    case-insensitively before positional-beam search. Not inherited
    through ancestry — each spec declares its own block."""

    def __post_init__(self) -> None:
        # Normalise None to empty dict
        if self.positional_graphemes is None:
            object.__setattr__(self, "positional_graphemes", {})
        if self.graphemes is None:
            object.__setattr__(self, "graphemes", {})
        if self.allophones is None:
            object.__setattr__(self, "allophones", {})
        if self.grapheme_weights is None:
            object.__setattr__(self, "grapheme_weights", {})

        # filter values explicitly nulled during inheritance
        for graph in set(self.graphemes.keys()):
            if self.graphemes[graph] is None:
                self.graphemes.pop(graph)
        for graph in set(self.positional_graphemes.keys()):
            if self.positional_graphemes[graph] is None:
                self.positional_graphemes.pop(graph)
        for graph in set(self.allophones.keys()):
            if self.allophones[graph] is None:
                self.allophones.pop(graph)

        # Derive a baseline identity allophone map when none is provided.
        # Every phoneme a grapheme can produce is, at minimum, its own
        # surface realisation; this keeps the allophone map well-defined
        # for specs that only declare graphemes.
        if not self.allophones and self.graphemes:
            derived: AllophoneMap = {}
            for ipa_candidates in self.graphemes.values():
                if not ipa_candidates:
                    continue
                for phoneme in ipa_candidates:
                    if phoneme and phoneme not in derived:
                        derived[phoneme] = [phoneme]
            object.__setattr__(self, "allophones", derived)

        # Normalise list to str
        if isinstance(self.notes, list):
            object.__setattr__(self, "notes", "\n".join(self.notes))

        # Normalise str to enums for new fields
        if isinstance(self.quality, str):
            object.__setattr__(self, "quality", QualityTier(self.quality))
        if isinstance(self.script_type, str):
            object.__setattr__(self, "script_type", ScriptType(self.script_type))

        # Normalize positional_graphemes to use Enum
        for grapheme, pos_map in self.positional_graphemes.items():
            for pos in set(pos_map.keys()):
                if not isinstance(pos, GraphemePosition):
                    new_pos = GraphemePosition(pos)
                    self.positional_graphemes[grapheme][new_pos] = self.positional_graphemes[grapheme].pop(pos)

        # ensure main parent is set
        if not self.ancestors and self.parent:
            object.__setattr__(self, "ancestors", [Ancestor(code=self.parent, role=AncestorRole.PARENT, weight=1.0,
                                                            notes="primary parent")])
        # if "parent" is not set, check if it is defined in "ancestors"
        #  this is technically incomplete json, but handle it
        elif not self.parent and self.ancestors:
            for a in self.ancestors:
                if a.role == AncestorRole.PARENT:
                    object.__setattr__(self, "parent", a.code)
                    break

    # ─── Positional grapheme resolution ─────────────────────────────
    def resolve_grapheme(
            self,
            grapheme: str,
            position: Optional[GraphemePosition] = None,
    ) -> List[str]:
        """Resolve a grapheme to its IPA candidates for a given position.

        Lookup order:
        1. ``positional_graphemes[grapheme][position]`` — exact match
        2. ``positional_graphemes[grapheme][DEFAULT]`` — positional default
        3. ``graphemes[grapheme]`` — base mapping fallback

        Parameters
        ----------
        grapheme : str
            The orthographic grapheme key.
        position : GraphemePosition
            The phonological position to resolve for.

        Returns
        -------
        List[str]
            IPA candidates, ordered from most to least common.

        Raises
        ------
        KeyError
            If the grapheme is not found in any mapping.
        """
        # Check positional overrides first
        if position is not None:
            if self.positional_graphemes and grapheme in self.positional_graphemes:
                pos_map = self.positional_graphemes[grapheme]
                if position in pos_map:
                    return pos_map[position]

        # Fallback to base graphemes
        if grapheme in self.graphemes:
            return self.graphemes[grapheme]

        raise KeyError(
            f"Grapheme {grapheme!r} not found in {self.code} mappings"
        )

    def has_positional_data(self) -> bool:
        """Return True if this spec has any positional grapheme overrides."""
        return bool(self.positional_graphemes)

    def positional_grapheme_keys(self) -> FrozenSet[str]:
        """Return the set of graphemes that have positional overrides."""
        if not self.positional_graphemes:
            return frozenset()
        return frozenset(self.positional_graphemes.keys())

    def positions_for_grapheme(self, grapheme: str) -> Tuple[GraphemePosition, ...]:
        """Return the positions defined for a grapheme in positional data.

        Returns empty tuple if the grapheme has no positional overrides.
        """
        if not self.positional_graphemes or grapheme not in self.positional_graphemes:
            return ()
        return tuple(self.positional_graphemes[grapheme].keys())

    # ─── Ancestry accessors ─────────────────────────────────────────

    def get_ancestors(self, role: Optional[AncestorRole] = None) -> Tuple[Ancestor, ...]:
        """Return ancestors, optionally filtered by role.
        Synthesises from parent field if ancestors tuple is empty."""
        anc = self.ancestors
        if not anc and self.parent:
            anc = (Ancestor(self.parent, AncestorRole.PARENT, 1.0),)
        if role is not None:
            anc = tuple(a for a in anc if a.role == role)
        return anc

    @property
    def primary_parent(self) -> Optional[str]:
        """The primary parent code."""
        if self.parent:
            return self.parent
        parents = self.get_ancestors(AncestorRole.PARENT)
        return parents[0].code if parents else None

    @property
    def substrate_codes(self) -> Tuple[str, ...]:
        return tuple(a.code for a in self.get_ancestors(AncestorRole.SUBSTRATE))

    @property
    def superstrate_codes(self) -> Tuple[str, ...]:
        return tuple(a.code for a in self.get_ancestors(AncestorRole.SUPERSTRATE))

    @property
    def contact_codes(self) -> Tuple[str, ...]:
        """All non-parent ancestor codes."""
        return tuple(
            a.code for a in self.get_ancestors()
            if a.role != AncestorRole.PARENT
        )
