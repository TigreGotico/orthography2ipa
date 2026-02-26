"""Type definitions for orthography2ipa.

The core data model supports:
- Single-parent inheritance (simple dialect trees)
- Multi-ancestor relationships (contact languages, creoles, transitional dialects)
- Weighted ancestry for distance calculations
- Positional grapheme-to-IPA mappings for context-sensitive G2P
- Glottolog classification codes for interoperability
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, FrozenSet, List, Optional, Tuple

# ═══════════════════════════════════════════════════════════════════════════
# Type aliases
# ═══════════════════════════════════════════════════════════════════════════

Grapheme2IPA = Dict[str, List[str]]
"""Orthographic grapheme → list of IPA phoneme candidates."""

AllophoneMap = Dict[str, List[str]]
"""Underlying phoneme → list of surface realisations."""

PositionalGrapheme2IPA = Dict[str, Dict["GraphemePosition", List[str]]]
"""Grapheme → {position: IPA candidates} for context-sensitive mappings."""


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

    CONSONANTAL = "consonantal"
    VOCALIC = "vocalic"


# ═══════════════════════════════════════════════════════════════════════════
# AncestorRole
# ═══════════════════════════════════════════════════════════════════════════

class AncestorRole(str, Enum):
    """How an ancestor language relates to its descendant."""

    PARENT = "parent"
    """Primary genetic descent.  The main lineage: Latin -> Spanish.
    Every language has at most one PARENT.  Weight typically 0.7-1.0."""

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
    """Language family."""

    script: str
    """Primary script."""

    graphemes: Grapheme2IPA
    """Orthographic grapheme -> canonical IPA phoneme(s).
    This is the context-free DEFAULT mapping, used when no positional
    override is available."""

    allophones: AllophoneMap
    """Phoneme -> contextual surface realisations."""

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

    glottolog_code: str | None = None
    """Optional Glottolog languoid code (e.g. 'cast1244' for Castilian,
    'west2813' for West Iberian). Enables cross-referencing with
    Glottolog's genealogical classification database.
    See https://glottolog.org for the full catalogue."""

    notes: str = ""
    """Free-form notes."""

    def __post_init__(self) -> None:
        # Normalise None to empty dict
        if self.positional_graphemes is None:
            object.__setattr__(self, "positional_graphemes", {})
        if self.graphemes is None:
            object.__setattr__(self, "graphemes", {})
        if self.allophones is None:
            object.__setattr__(self, "allophones", {})

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

        # Normalise list to str
        if isinstance(self.notes, list):
            object.__setattr__(self, "notes", "\n".join(self.notes))

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
            position: GraphemePosition | None = None,
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

    def get_ancestors(self, role: AncestorRole | None = None) -> Tuple[Ancestor, ...]:
        """Return ancestors, optionally filtered by role.
        Synthesises from parent field if ancestors tuple is empty."""
        anc = self.ancestors
        if not anc and self.parent:
            anc = (Ancestor(self.parent, AncestorRole.PARENT, 1.0),)
        if role is not None:
            anc = tuple(a for a in anc if a.role == role)
        return anc

    @property
    def primary_parent(self) -> str | None:
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
