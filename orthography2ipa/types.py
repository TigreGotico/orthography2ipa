"""Type definitions for orthography2ipa.

The core data model supports:
- Single-parent inheritance (simple dialect trees)
- Multi-ancestor relationships (contact languages, creoles, transitional dialects)
- Weighted ancestry for distance calculations
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Tuple

# Grapheme key → list of IPA transcription strings.
Grapheme2IPA = Dict[str, List[str]]

# Phoneme key → list of allophonic surface realisations.
AllophoneMap = Dict[str, List[str]]


class AncestorRole(Enum):
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

    def __repr__(self) -> str:
        return f"Ancestor({self.code!r}, {self.role.value}, w={self.weight:.2f})"


@dataclass(frozen=True)
class LanguageSpec:
    """Complete phonological specification for one language / variety."""

    code: str
    """BCP-47 or ISO 639 code."""

    name: str
    """Human-readable name."""

    family: str
    """Language family."""

    script: str
    """Primary script."""

    graphemes: Grapheme2IPA
    """Orthographic grapheme -> canonical IPA phoneme(s)."""

    allophones: AllophoneMap
    """Phoneme -> contextual surface realisations."""

    parent: str | None = None
    """Primary parent code (backward-compatible shorthand).
    If ancestors is also set, should match the PARENT-role ancestor."""

    ancestors: Tuple[Ancestor, ...] = ()
    """Full ancestry specification.  Encodes multiple parents,
    substrates, superstrates, contact languages, creole origins.
    If empty but parent is set, a default PARENT ancestor is inferred."""

    notes: str = ""
    """Free-form notes."""

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
