"""IPA dialect transform system for Portuguese and Ibero-Romance varieties.

Converts a standard PT-PT IPA phoneme string (from eSpeak-NG or similar) into
any of the dialect profiles identified in Cintra (1971) and extended to cover
Galician and Astur-Leonese enclave varieties.

Usage::

    from orthography2ipa.transforms import apply_transform, debias_lisbon

    ipa = "u ˈvɛʎu ˈveɾdɨ foj ˈveɾ ɐ ˈvakɐ"
    ortho = "O velho verde foi ver a vaca"

    # De-bias eSpeak output to neutral standard
    neutral = debias_lisbon(ipa, ortho)

    # Apply a dialect transform
    rionorese = apply_transform(neutral, "rionorese", ortho)

Source: Cintra, L.F.L. (1971), "Nova proposta de classificação dos dialectos
galego-portugueses", Boletim de Filologia 22:81–116.

T-13: Core types (IPARule, IPAChainShift, IPALexicalRule, DialectTransform)
T-14: debias_lisbon() — 7 de-biasing rules (DB1–DB7)
T-15: Northern PT transforms (NORTHERN_COMMON, TRANSMONTANO, BAIXO_MINHOTO,
       PORTO, BEIRA_ALTA)
T-16: Central-Southern, Galician, Leonese transforms
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union


# ---------------------------------------------------------------------------
# Vowel / consonant reference sets
# ---------------------------------------------------------------------------

#: All IPA vowel characters used in Ibero-Romance transcription.
VOWEL_SET: frozenset = frozenset(
    "aeɛɐiɨoɔuɑæøœyãẽĩõũ"
)

#: Palatal consonants — used to detect "adjacent to palatal" context.
PALATAL_SET: frozenset = frozenset(["ɲ", "ʎ", "ʃ", "ʒ", "j"])

#: The IPA primary-stress diacritic.
STRESS = "ˈ"


# ---------------------------------------------------------------------------
# T-13: Core dataclasses
# ---------------------------------------------------------------------------

@dataclass
class IPARule:
    """A single phoneme-level IPA transformation rule.

    Attributes:
        id: Short identifier (e.g. "N1", "DB1").
        name: Human-readable name.
        find: IPA substring to match.
        replace: IPA replacement string (empty string = deletion).
        context: Named context condition string, or None for unconditional.
        requires_ortho: If True the rule only fires when the source
            orthographic word is supplied to apply_transform().
        description: Free-text explanation.
    """
    id: str
    name: str
    find: str
    replace: str
    context: Optional[str] = None
    requires_ortho: bool = False
    description: str = ""


@dataclass
class IPAChainShift:
    """A simultaneous multi-vowel mapping (chain shift).

    Mappings are applied in a single left-to-right pass so that the output
    of one mapping does not become the input of the next.

    Attributes:
        id: Short identifier (e.g. "ALG_CHAIN").
        name: Human-readable name.
        mapping: Dict mapping source IPA char → target IPA char.
        context: "stressed" to limit to the first vowel of each stressed
            syllable, or None for all vowels.
        description: Free-text explanation.
    """
    id: str
    name: str
    mapping: Dict[str, str]
    context: Optional[str] = None
    description: str = ""

    def apply(self, ipa: str) -> str:
        """Apply all mappings simultaneously in a single pass."""
        result: List[str] = []
        in_stressed_syllable = False
        for ch in ipa:
            if ch == STRESS:
                in_stressed_syllable = True
                result.append(ch)
                continue
            if self.context == "stressed" and not in_stressed_syllable:
                result.append(ch)
            else:
                result.append(self.mapping.get(ch, ch))
            # Reset after first vowel in stressed syllable
            if ch in VOWEL_SET and in_stressed_syllable:
                in_stressed_syllable = False
        return "".join(result)


@dataclass
class IPALexicalRule:
    """A word-specific lexical substitution (requires orthographic word).

    Used for article paradigm replacements and pronoun forms that cannot
    be derived by phonological rule.

    Attributes:
        id: Short identifier.
        word: Orthographic word that triggers this rule (case-insensitive).
        find: IPA substring to replace.
        replace: Replacement IPA string.
    """
    id: str
    word: str
    find: str
    replace: str

    def applies(self, ortho_word: str) -> bool:
        return ortho_word is not None and ortho_word.lower() == self.word.lower()


#: Union type for all rule kinds.
AnyRule = Union[IPARule, IPAChainShift, IPALexicalRule]


@dataclass
class DialectTransform:
    """A named dialect profile containing an ordered list of transform rules.

    Attributes:
        profile_code: Machine-readable identifier matching keys in
            DIALECT_PROFILES (e.g. "transmontano").
        name: Human-readable name.
        cintra_zone: Cintra (1971) classification zone.
        rules: Ordered list of rules to apply.
        requires_debiasing: If True, debias_lisbon() should be called
            before applying these rules when the input comes from eSpeak.
    """
    profile_code: str
    name: str
    cintra_zone: str
    rules: List[AnyRule] = field(default_factory=list)
    requires_debiasing: bool = True


# ---------------------------------------------------------------------------
# T-14: Lisbon de-biasing module
# ---------------------------------------------------------------------------

def debias_lisbon(ipa: str, ortho: Optional[str] = None) -> str:
    """Convert Lisbon-biased phonemizer output to neutral standard PT-PT.

    eSpeak-NG and most PT phonemizers target the Lisbon prestige norm.
    This function corrects the most common systematic biases before
    dialectal transforms are applied.

    Rules applied:

    - DB1: ɐj → ej  (Lisbon lowers /ej/ to [ɐj] — restore)
    - DB2: o → ow   (Lisbon monophthongizes /ow/ → [o] — restore when
                     ortho contains ‹ou›)
    - DB3: ɨ over-reduction — flagged but NOT applied by default (too
                     context-sensitive to apply blindly)
    - DB4: β → b    (normalize allophonic spirantization)
    - DB5: ð → d    (normalize allophonic spirantization)
    - DB6: ɣ → ɡ   (normalize allophonic spirantization)
    - DB6b: ɫ → l  (normalize coda-l velarization)
    - DB7: ʁ kept   (Lisbon uvular is also standard — no change)

    Args:
        ipa: IPA string from a phonemizer (e.g., eSpeak-NG ``-v pt``).
        ortho: Optional source orthographic word or phrase for disambiguation.

    Returns:
        Neutral standard IPA string.
    """
    # DB1: ɐj → ej
    # With ortho: apply wherever word contains ‹ei›
    # Without ortho: heuristic — ɐj after a consonant in stressed position
    if ortho and "ei" in ortho:
        ipa = ipa.replace("ɐj", "ej")
    elif not ortho:
        # ɐj preceded by a non-vowel → likely from ‹ei›
        ipa = re.sub(r"(?<=[^aeɛɐiɨoɔuɑæøœyãẽĩõũ\s])ɐj", "ej", ipa)

    # DB2: Restore /ow/ diphthong where Lisbon monophthongizes
    if ortho and "ou" in ortho:
        # Heuristic: o before certain consonants that match the ‹ou› pattern
        ipa = re.sub(r"o(?=[tdszʃnlɾ])", "ow", ipa)

    # DB4: β → b  (allophonic spirantization)
    ipa = ipa.replace("β", "b")
    # DB5: ð → d
    ipa = ipa.replace("ð", "d")
    # DB6: ɣ → ɡ
    ipa = ipa.replace("ɣ", "ɡ")
    # DB6b: ɫ → l  (velarized lateral)
    ipa = ipa.replace("ɫ", "l")

    # DB7: ʁ preserved — no change

    return ipa


def debias_lisbon_preserve_spirants(ipa: str, ortho: Optional[str] = None) -> str:
    """Like :func:`debias_lisbon` but preserves spirants (β, ð, ɣ).

    Used when CLUP allophone weights indicate the region genuinely
    spirantizes — normalizing β→b would discard real dialectal information.
    DB1, DB2, DB6b still apply; DB4, DB5, DB6 are skipped.
    """
    # DB1
    if ortho and "ei" in ortho:
        ipa = ipa.replace("ɐj", "ej")
    elif not ortho:
        ipa = re.sub(r"(?<=[^aeɛɐiɨoɔuɑæøœyãẽĩõũ\s])ɐj", "ej", ipa)

    # DB2
    if ortho and "ou" in ortho:
        ipa = re.sub(r"o(?=[tdszʃnlɾ])", "ow", ipa)

    # DB4–DB6 SKIPPED (spirants preserved)

    # DB6b: ɫ → l (velarized lateral — still normalize)
    ipa = ipa.replace("ɫ", "l")

    return ipa


# ---------------------------------------------------------------------------
# T-15: Northern PT rule lists
# ---------------------------------------------------------------------------

#: Rules shared by ALL Northern Portuguese varieties.
NORTHERN_COMMON: List[AnyRule] = [
    IPARule(
        id="N1",
        name="betacism",
        find="v",
        replace="b",
        context=None,
        description="/v/ → /b/ merger — complete in all Northern varieties",
    ),
    IPARule(
        id="N2",
        name="ou_diphthong_preservation",
        find="o",
        replace="ow",
        context="ortho_has_ou",
        requires_ortho=True,
        description="Restore /ow/ diphthong (without de-biasing pre-step)",
    ),
]

#: Transmontano / Alto-Minhoto — 4-sibilant system + ch affrication.
TRANSMONTANO: List[AnyRule] = NORTHERN_COMMON + [
    IPARule(
        id="TM1a",
        name="apicoalveolar_s",
        find="s",
        replace="s̺",
        context="ortho_source_is_ss_or_s",
        requires_ortho=True,
        description="‹ss/s› → apicoalveolar [s̺]",
    ),
    IPARule(
        id="TM1b",
        name="predorsodental_s",
        find="s",
        replace="s̻",
        context="ortho_source_is_c_or_ç",
        requires_ortho=True,
        description="‹ç/c(e,i)› → predorsodental [s̻]",
    ),
    IPARule(
        id="TM1c",
        name="apicoalveolar_z",
        find="z",
        replace="z̺",
        context="ortho_source_is_intervocalic_s",
        requires_ortho=True,
        description="intervocalic ‹s› → apicoalveolar [z̺]",
    ),
    IPARule(
        id="TM1d",
        name="predorsodental_z",
        find="z",
        replace="z̻",
        context="ortho_source_is_z",
        requires_ortho=True,
        description="‹z› → predorsodental [z̻]",
    ),
    IPARule(
        id="TM1_fallback",
        name="apicoalveolar_sibilants_all",
        find="s",
        replace="s̺",
        context="no_ortho_available",
        requires_ortho=False,
        description="Fallback (no ortho): all /s/ → [s̺] apicoalveolar",
    ),
    IPARule(
        id="TM2",
        name="ch_affrication",
        find="ʃ",
        replace="tʃ",
        context="ortho_source_is_ch",
        requires_ortho=True,
        description="/ʃ/ → /tʃ/ affricate (where ortho is ‹ch›)",
    ),
    IPARule(
        id="TM3",
        name="nasal_diphthong_reduction",
        find="ɐ̃w̃",
        replace="õ",
        context="word_final",
        description="Final /-ɐ̃w̃/ → [-õ] (Transmontano variant)",
    ),
]

#: Baixo-Minhoto / Duriense / Beirão — 2-sibilant (apicoalveolar) system.
BAIXO_MINHOTO_DURIENSE: List[AnyRule] = NORTHERN_COMMON + [
    IPARule(
        id="BMD1a",
        name="apicoalveolar_s_merged",
        find="s",
        replace="s̺",
        context=None,
        description="All /s/ → [s̺] (apicoalveolar, merged)",
    ),
    IPARule(
        id="BMD1b",
        name="apicoalveolar_z_merged",
        find="z",
        replace="z̺",
        context=None,
        description="All /z/ → [z̺] (apicoalveolar, merged)",
    ),
]

#: Porto / Baixo-Minho / Douro Litoral — 2-sibilant + e/o diphthongization.
PORTO: List[AnyRule] = BAIXO_MINHOTO_DURIENSE + [
    IPARule(
        id="PT1",
        name="porto_e_diphthong",
        find="e",
        replace="je",
        context="stressed_and_before_r_or_closed_syllable",
        description="Stressed /e/ → [je] (Porto diphthongization)",
    ),
    IPARule(
        id="PT2",
        name="porto_o_diphthong",
        find="o",
        replace="wo",
        context="stressed_and_before_r_or_closed_syllable",
        description="Stressed /o/ → [wo] (Porto diphthongization)",
    ),
    IPARule(
        id="PT3",
        name="porto_nasal_a_velarization",
        find="ɐ̃",
        replace="ɑ̃",
        context="stressed",
        description="Tonic /ɐ̃/ → [ɑ̃] (more open, velarized)",
    ),
]

#: Beira-Alta — 2-sibilant; no Porto-style diphthongization.
BEIRA_ALTA: List[AnyRule] = BAIXO_MINHOTO_DURIENSE + []


# ---------------------------------------------------------------------------
# T-16: Central-Southern PT rule lists
# ---------------------------------------------------------------------------

#: Standard PT-PT *is* Central-Southern (Cintra). No additional transforms.
CENTRAL_SOUTHERN_COMMON: List[AnyRule] = []

#: Centro-Litoral / Estremenho — the neutral dialect; closest to orthographic
#: standard. After de-biasing, no further transforms needed.
ESTREMENHO: List[AnyRule] = CENTRAL_SOUTHERN_COMMON + []

#: Lisbon — when explicitly targeting the Lisbon accent (NOT the neutral
#: de-biased form). Skip de-biasing; apply Lisbon-specific features.
LISBON: List[AnyRule] = [
    IPARule(id="LX1", name="lisbon_ei_lowering",
            find="ej", replace="ɐj",
            description="/ej/ → [ɐj] (Lisbon diphthong lowering)"),
    IPARule(id="LX2", name="lisbon_ou_monophthong",
            find="ow", replace="o",
            description="/ow/ → [o] (Lisbon monophthongization)"),
    IPARule(id="LX3", name="lisbon_unstressed_reduction",
            find="e", replace="ɨ",
            context="unstressed_pretonic",
            description="Unstressed /e/ → [ɨ] (heavy reduction)"),
    IPARule(id="LX4", name="lisbon_coda_l_velarization",
            find="l", replace="ɫ",
            context="coda",
            description="Coda /l/ → [ɫ] (velarized)"),
]

#: Ribatejano / Baixo-Beirão / Alentejano — ei monophthongization.
RIBATEJANO_ALENTEJANO: List[AnyRule] = CENTRAL_SOUTHERN_COMMON + [
    IPARule(id="RA1", name="ei_monophthong",
            find="ej", replace="e",
            description="/ej/ → [e] (monophthongization)"),
]

#: Beira-Baixa / Alto-Alentejo — u→y palatalization + vowel shifts.
BEIRA_BAIXA: List[AnyRule] = CENTRAL_SOUTHERN_COMMON + [
    IPARule(id="RA1", name="ei_monophthong",
            find="ej", replace="e",
            description="/ej/ → [e]"),
    IPARule(id="BB1", name="u_palatalization",
            find="u", replace="y",
            context="stressed",
            description="Tonic /u/ → [y] (palatalized)"),
    IPARule(id="BB2a", name="a_palatalization_palatal_context",
            find="a", replace="æ",
            context="stressed_and_adjacent_to_palatal",
            description="Tonic /a/ → [æ] before/after palatal C"),
    IPARule(id="BB3", name="o_fronting",
            find="o", replace="ø",
            context="stressed_and_from_historical_ou",
            requires_ortho=True,
            description="Tonic /o/ (< /ow/) → [ø]"),
    IPARule(id="BB4", name="open_e_labialization",
            find="ɛ", replace="œ",
            context="stressed",
            description="Tonic /ɛ/ → [œ] (labialized)"),
    IPARule(id="BB5a", name="final_u_deletion",
            find="u", replace="",
            context="word_final_unstressed",
            description="Final unstressed /u/ → Ø"),
    IPARule(id="BB5b", name="final_schwa_deletion",
            find="ɨ", replace="",
            context="word_final",
            description="Final /ɨ/ → Ø"),
]

#: Barlavento Algarvio — simultaneous chain vowel shift.
BARLAVENTO_ALGARVE: List[AnyRule] = CENTRAL_SOUTHERN_COMMON + [
    IPARule(id="RA1", name="ei_monophthong",
            find="ej", replace="e",
            description="/ej/ → [e]"),
    IPAChainShift(
        id="ALG_CHAIN",
        name="barlavento_chain_shift",
        mapping={
            "a": "ɔ",
            "ɔ": "o",
            "o": "u",
            "u": "y",
            "ɛ": "æ",
            "e": "ɛ",
        },
        context="stressed",
        description="Barlavento Algarvio simultaneous chain vowel shift",
    ),
    IPARule(id="ALG2a", name="final_u_deletion_alg",
            find="u", replace="",
            context="word_final_unstressed",
            description="Final unstressed /u/ → Ø"),
]


# ---------------------------------------------------------------------------
# T-16: Galician rule lists
# ---------------------------------------------------------------------------

#: Rules common to all Galician varieties.
GALICIAN_COMMON: List[AnyRule] = [
    IPARule(id="G1", name="betacism",
            find="v", replace="b",
            description="/v/ → /b/"),
    IPARule(id="G2a", name="palatal_devoicing",
            find="ʒ", replace="ʃ",
            description="/ʒ/ → /ʃ/ (sibilant devoicing)"),
    IPARule(id="G2b", name="alveolar_devoicing",
            find="z", replace="s",
            description="/z/ → /s/ (sibilant devoicing)"),
    IPARule(id="G3a", name="galician_unstressed_e",
            find="ɨ", replace="e",
            context="unstressed",
            description="Unstressed [ɨ] → [e] (less reduction)"),
    IPARule(id="G3c", name="galician_unstressed_a",
            find="ɐ", replace="a",
            context="unstressed",
            description="Unstressed [ɐ] → [a] (less reduction)"),
]

#: Western Galician — includes geada (/ɡ/ → [x]).
GALICIAN_WEST: List[AnyRule] = GALICIAN_COMMON + [
    IPARule(id="GW1", name="geada",
            find="ɡ", replace="x",
            description="/ɡ/ → [x] (velar fricativization — geada)"),
]

#: Eastern Galician — no geada; all other Galician features apply.
GALICIAN_EAST: List[AnyRule] = GALICIAN_COMMON + []


# ---------------------------------------------------------------------------
# T-16: Astur-Leonese enclave rule lists
# ---------------------------------------------------------------------------

#: Rules common to all Leonese enclave varieties.
#: Includes Northern Common + 4-sibilant TM1 rules + Leonese-specific rules.
_TM1_RULES = [r for r in TRANSMONTANO if r.id.startswith("TM1")]

LEONESE_COMMON: List[AnyRule] = list(NORTHERN_COMMON) + _TM1_RULES + [
    IPARule(id="LEO1", name="leonese_e_diphthong",
            find="ɛ", replace="je",
            context="stressed_before_r_C_or_nasal_C",
            description="Stressed /ɛ/ → [je] (Leonese diphthongization)"),
    IPARule(id="LEO2", name="leonese_o_diphthong",
            find="ɔ", replace="wɔ",
            context="stressed_before_r_C",
            description="Stressed /ɔ/ → [wɔ] (Leonese diphthongization)"),
    IPARule(id="LEO3", name="lh_yodization",
            find="ʎ", replace="j",
            description="/ʎ/ → [j] (yodization)"),
    IPARule(id="LEO4", name="leonese_palatal_devoicing",
            find="ʒ", replace="ʃ",
            description="/ʒ/ → /ʃ/ (shared with Galician)"),
    IPARule(id="LEO5", name="participle_d_syncope",
            find="adu", replace="aw",
            context="word_final",
            description="/-adu/ → [-aw] (intervocalic /d/ syncope in participles)"),
]

#: Rionorese — Leonese base + article o → al.
RIONORESE_RULES: List[AnyRule] = LEONESE_COMMON + [
    IPALexicalRule(id="RIO_ART", word="o", find="u", replace="al"),
    IPALexicalRule(id="RIO_PRON", word="eu", find="ew", replace="jew"),
]

#: Guadramilese — Leonese base + article o → o (no change) + pronoun eu → you.
GUADRAMILESE_RULES: List[AnyRule] = LEONESE_COMMON + [
    IPALexicalRule(id="GUA_PRON", word="eu", find="ew", replace="jow"),
    IPARule(id="GUA_IMPF", name="guadramilese_3pl_imperfect",
            find="iɐ̃w̃", replace="jẽ",
            context="word_final",
            description="3pl imperfect -iam → -ien"),
    IPALexicalRule(id="GUA_IR", word="ia", find="iɐ", replace="dibɐ"),
]


# ---------------------------------------------------------------------------
# T-13: DIALECT_PROFILES registry
# ---------------------------------------------------------------------------

DIALECT_PROFILES: Dict[str, DialectTransform] = {
    # Central-Southern (standard / neutral)
    "estremenho": DialectTransform(
        profile_code="estremenho",
        name="Centro-Litoral / Estremenho",
        cintra_zone="Central-Meridional",
        rules=ESTREMENHO,
        requires_debiasing=True,
    ),
    "lisbon": DialectTransform(
        profile_code="lisbon",
        name="Lisbon / Lisboa",
        cintra_zone="Central-Meridional (Lisbon)",
        rules=LISBON,
        requires_debiasing=False,  # raw phonemizer output IS Lisbon
    ),
    "ribatejano": DialectTransform(
        profile_code="ribatejano",
        name="Ribatejano / Baixo-Beirão / Alentejano",
        cintra_zone="Central-Meridional",
        rules=RIBATEJANO_ALENTEJANO,
        requires_debiasing=True,
    ),
    "beira_baixa": DialectTransform(
        profile_code="beira_baixa",
        name="Beira-Baixa / Alto-Alentejo",
        cintra_zone="Central-Meridional",
        rules=BEIRA_BAIXA,
        requires_debiasing=True,
    ),
    "algarve_barlavento": DialectTransform(
        profile_code="algarve_barlavento",
        name="Barlavento Algarvio",
        cintra_zone="Meridional",
        rules=BARLAVENTO_ALGARVE,
        requires_debiasing=True,
    ),
    # Northern
    "northern": DialectTransform(
        profile_code="northern",
        name="Northern Portuguese (common)",
        cintra_zone="Setentrional",
        rules=NORTHERN_COMMON,
        requires_debiasing=True,
    ),
    "transmontano": DialectTransform(
        profile_code="transmontano",
        name="Transmontano / Alto-Minhoto",
        cintra_zone="Setentrional",
        rules=TRANSMONTANO,
        requires_debiasing=True,
    ),
    "baixo_minhoto": DialectTransform(
        profile_code="baixo_minhoto",
        name="Baixo-Minhoto / Duriense / Beirão",
        cintra_zone="Setentrional",
        rules=BAIXO_MINHOTO_DURIENSE,
        requires_debiasing=True,
    ),
    "porto": DialectTransform(
        profile_code="porto",
        name="Porto / Baixo-Minho / Douro Litoral",
        cintra_zone="Setentrional",
        rules=PORTO,
        requires_debiasing=True,
    ),
    "beira_alta": DialectTransform(
        profile_code="beira_alta",
        name="Beira-Alta (General Beirão)",
        cintra_zone="Setentrional",
        rules=BEIRA_ALTA,
        requires_debiasing=True,
    ),
    # Galician
    "galician": DialectTransform(
        profile_code="galician",
        name="Galician / Galego (Eastern)",
        cintra_zone="Galician",
        rules=GALICIAN_EAST,
        requires_debiasing=True,
    ),
    "galician_west": DialectTransform(
        profile_code="galician_west",
        name="Western Galician (with geada)",
        cintra_zone="Galician",
        rules=GALICIAN_WEST,
        requires_debiasing=True,
    ),
    # Leonese enclaves
    "leonese": DialectTransform(
        profile_code="leonese",
        name="Leonese enclave (common)",
        cintra_zone="Astur-Leonese",
        rules=LEONESE_COMMON,
        requires_debiasing=True,
    ),
    "rionorese": DialectTransform(
        profile_code="rionorese",
        name="Rionorese (Rionor de Castela)",
        cintra_zone="Astur-Leonese",
        rules=RIONORESE_RULES,
        requires_debiasing=True,
    ),
    "guadramilese": DialectTransform(
        profile_code="guadramilese",
        name="Guadramilese (Guadramil)",
        cintra_zone="Astur-Leonese",
        rules=GUADRAMILESE_RULES,
        requires_debiasing=True,
    ),
}


# ---------------------------------------------------------------------------
# Context checking helpers
# ---------------------------------------------------------------------------

def _is_stressed_position(ipa: str, pos: int) -> bool:
    """Return True if character at ``pos`` is in a stressed syllable.

    A position is stressed if the stress marker (ˈ) appears somewhere
    to its left, with no intervening vowel between the stress marker
    and this position.
    """
    # Look back for ˈ without crossing a vowel boundary
    i = pos - 1
    while i >= 0:
        ch = ipa[i]
        if ch == STRESS:
            return True
        if ch in VOWEL_SET:
            break
        i -= 1
    return False


def _is_word_final(ipa: str, pos: int, length: int) -> bool:
    """Return True if the substring at pos..pos+length is at a word boundary."""
    end = pos + length
    if end >= len(ipa):
        return True
    return ipa[end] in (" ", "\t", "\n", "")


def _is_unstressed(ipa: str, pos: int) -> bool:
    return not _is_stressed_position(ipa, pos)


def _adjacent_to_palatal(ipa: str, pos: int) -> bool:
    """Return True if the character at pos is immediately adjacent to a palatal."""
    if pos > 0 and ipa[pos - 1] in PALATAL_SET:
        return True
    if pos < len(ipa) - 1 and ipa[pos + 1] in PALATAL_SET:
        return True
    # Also handle two-char palatal 'tʃ'
    for palatal in ("tʃ", "dʒ"):
        for offset in range(len(palatal)):
            start = pos - offset
            if start >= 0 and ipa[start:start + len(palatal)] == palatal:
                return True
    return False


def _before_r_or_closed(ipa: str, pos: int) -> bool:
    """Return True if the character at pos is before a rhotic + consonant cluster."""
    rest = ipa[pos + 1:]
    return bool(re.match(r"[ɾr][bcdfɡhjklmnpqrstvwxzʃʒŋɲʎ]", rest))


def _check_context(
    context: str,
    ipa: str,
    pos: int,
    length: int,
    ortho: Optional[str],
    find: str,
) -> bool:
    """Evaluate a named context condition.

    Returns True if the rule should apply at this position.
    """
    if context is None:
        return True

    if context == "stressed":
        return _is_stressed_position(ipa, pos)

    if context == "unstressed":
        return _is_unstressed(ipa, pos)

    if context == "word_final":
        return _is_word_final(ipa, pos, length)

    if context == "word_final_unstressed":
        return _is_word_final(ipa, pos, length) and _is_unstressed(ipa, pos)

    if context == "coda":
        # Simplified: after the main vowel of a syllable, before consonant/boundary
        if pos > 0 and ipa[pos - 1] in VOWEL_SET:
            return True
        return False

    if context == "stressed_and_before_r_or_closed_syllable":
        return _is_stressed_position(ipa, pos) and _before_r_or_closed(ipa, pos)

    if context == "stressed_and_adjacent_to_palatal":
        return _is_stressed_position(ipa, pos) and _adjacent_to_palatal(ipa, pos)

    if context == "stressed_before_r_C":
        return _is_stressed_position(ipa, pos) and _before_r_or_closed(ipa, pos)

    if context == "stressed_before_r_C_or_nasal_C":
        rest = ipa[pos + 1:]
        before_nasal_c = bool(re.match(r"[mn][bcdfɡhjklmnpqrstvwxzʃʒŋɲʎ]", rest))
        return _is_stressed_position(ipa, pos) and (
            _before_r_or_closed(ipa, pos) or before_nasal_c
        )

    if context == "unstressed_pretonic":
        # Unstressed position that is before the stressed syllable
        return _is_unstressed(ipa, pos) and STRESS in ipa[pos:]

    if context == "stressed_and_from_historical_ou":
        return (
            ortho is not None
            and "ou" in ortho
            and _is_stressed_position(ipa, pos)
        )

    if context == "ortho_has_ou":
        return ortho is not None and "ou" in ortho

    if context == "ortho_source_is_ch":
        return ortho is not None and "ch" in ortho

    if context == "ortho_source_is_ss_or_s":
        return ortho is not None and ("ss" in ortho or "s" in ortho)

    if context == "ortho_source_is_c_or_ç":
        return ortho is not None and (
            "ç" in ortho
            or re.search(r"c[ei]", ortho) is not None
        )

    if context == "ortho_source_is_intervocalic_s":
        return ortho is not None and re.search(r"[aeiouáéíóúâêôãõ]s[aeiouáéíóúâêôãõ]", ortho) is not None

    if context == "ortho_source_is_z":
        return ortho is not None and "z" in ortho

    if context == "no_ortho_available":
        return ortho is None

    # Unknown context — skip the rule to be safe
    return False


def _apply_contextual(ipa: str, rule: IPARule, ortho: Optional[str]) -> str:
    """Apply a context-sensitive IPARule to an IPA string.

    Scans left-to-right for occurrences of rule.find and checks the
    context condition at each position.
    """
    find = rule.find
    replace = rule.replace
    flen = len(find)
    result: List[str] = []
    i = 0
    while i < len(ipa):
        if ipa[i:i + flen] == find:
            if _check_context(rule.context, ipa, i, flen, ortho, find):
                result.append(replace)
                i += flen
                continue
        result.append(ipa[i])
        i += 1
    return "".join(result)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def apply_transform(
    ipa: str,
    profile: str,
    ortho: Optional[str] = None,
    debias: bool = True,
    allophone_weights: Optional[Dict[str, float]] = None,
) -> str:
    """Apply a dialect transform to an IPA string.

    Args:
        ipa: Phonemized IPA string (e.g., from eSpeak-NG or
            ``PhonetokTokenizer.ipa_best()``).
        profile: Dialect profile key from ``DIALECT_PROFILES``
            (e.g., ``"transmontano"``, ``"rionorese"``).
        ortho: Optional source orthographic text for disambiguation of
            context-sensitive rules (e.g., sibilant origin, ‹ou› diphthong).
        debias: If True and the profile has ``requires_debiasing=True``,
            apply :func:`debias_lisbon` before the dialect rules.
            Set to False if your input is already de-biased or comes from
            a neutral phonemizer.
        allophone_weights: Optional dict of allophone weight keys (from
            :func:`load_clup_profile`) for continuous parameterization.
            When provided, de-biasing of spirants (DB4–DB6) is skipped if
            ``spirantization_rate > 0.02`` (the region genuinely spirantizes).

    Returns:
        Dialectally transformed IPA string.

    Raises:
        KeyError: If ``profile`` is not in :data:`DIALECT_PROFILES`.

    Example::

        >>> apply_transform("ˈvakɐ", "northern")
        'ˈbakɐ'
        >>> apply_transform("ˈkazɐ", "algarve_barlavento")
        'ˈkɔzɐ'
    """
    dt = DIALECT_PROFILES[profile]

    # Step 0: De-bias Lisbon phonemizer output → neutral standard
    # When allophone_weights indicate the region genuinely spirantizes,
    # preserve spirants (skip β→b, ð→d, ɣ→ɡ normalization).
    if debias and dt.requires_debiasing:
        if (
            allophone_weights
            and allophone_weights.get("spirantization_rate", 0.0) > 0.02
        ):
            ipa = debias_lisbon_preserve_spirants(ipa, ortho)
        else:
            ipa = debias_lisbon(ipa, ortho)

    # Step 1: Apply chain shifts (simultaneous — must run before sequential rules)
    for rule in dt.rules:
        if isinstance(rule, IPAChainShift):
            ipa = rule.apply(ipa)

    # Step 2: Apply lexical rules (word-level, require ortho)
    if ortho:
        words_ipa = ipa.split()
        words_ortho = ortho.split()
        if len(words_ipa) == len(words_ortho):
            for i, (w_ipa, w_ortho) in enumerate(zip(words_ipa, words_ortho)):
                for rule in dt.rules:
                    if isinstance(rule, IPALexicalRule) and rule.applies(w_ortho):
                        words_ipa[i] = w_ipa.replace(rule.find, rule.replace)
            ipa = " ".join(words_ipa)

    # Step 3: Apply phonological rules (ordered)
    for rule in dt.rules:
        if not isinstance(rule, IPARule):
            continue
        if rule.requires_ortho and ortho is None:
            continue
        if rule.context is None:
            # Simple unconditional substitution
            ipa = ipa.replace(rule.find, rule.replace)
        else:
            ipa = _apply_contextual(ipa, rule, ortho)

    return ipa


def available_profiles() -> List[str]:
    """Return sorted list of available dialect profile codes."""
    return sorted(DIALECT_PROFILES.keys())


# ---------------------------------------------------------------------------
# T-17: CLUP allophone continuous parameterization
# ---------------------------------------------------------------------------

#: Mapping from CLUP CSV allophone flag columns to normalized weight keys.
#: Boolean columns (YES/empty) become 1.0/0.0; numeric columns are normalized
#: by dividing by ``ipa_chars`` to produce a per-character rate.
_CLUP_BOOL_COLUMNS = {
    "retroflex_sibilant": "retroflex_sibilant",
    "uvular_trill_ʀ": "uvular_trill",
    "voiceless_uvular_χ": "voiceless_uvular",
    "retroflex_tap_ɽ": "retroflex_tap",
    "retroflex_lateral_ɭ": "retroflex_lateral",
    "aspiration": "aspiration",
    "insular_vowel_shift": "insular_vowel_shift",
}

_CLUP_RATE_COLUMNS = {
    "vowel_reduction_ratio": "vowel_reduction_ratio",
}

_CLUP_COUNT_COLUMNS = {
    "spirant_count": "spirantization_rate",
    "devoicing_count": "devoicing_rate",
    "retroflex_sib_count": "retroflex_sibilant_rate",
    "aspiration_count": "aspiration_rate",
}


def load_clup_profile(
    region: str,
    clup_csv: str,
) -> Optional[Dict[str, float]]:
    """Load a CLUP allophone profile for a region from the analysis CSV.

    The CLUP analysis CSV (produced by ``ipa_research/clup/analyze_clup_ipa.py``)
    contains per-region allophone presence flags and counts.  This function
    normalizes them into a ``Dict[str, float]`` of weight keys suitable for
    passing to ``apply_transform(..., allophone_weights=...)``.

    Weight keys returned:

    - ``retroflex_sibilant`` — 1.0 if region shows retroflex sibilants, else 0.0
    - ``uvular_trill`` — 1.0 if ʀ present
    - ``voiceless_uvular`` — 1.0 if χ present
    - ``retroflex_tap`` — 1.0 if ɽ present
    - ``retroflex_lateral`` — 1.0 if ɭ present
    - ``aspiration`` — 1.0 if aspirated tokens present
    - ``insular_vowel_shift`` — 1.0 if front-rounded/open-back vowels present
    - ``vowel_reduction_ratio`` — float (ratio of [ɨ] to total vowels)
    - ``spirantization_rate`` — float (spirant tokens / total IPA chars)
    - ``devoicing_rate`` — float (devoicing tokens / total IPA chars)
    - ``retroflex_sibilant_rate`` — float
    - ``aspiration_rate`` — float

    Args:
        region: Region string to match (substring match, case-insensitive).
        clup_csv: Path to the ``clup_analysis_allophone_flags.csv`` file.

    Returns:
        Dict of weight keys → float values, or ``None`` if the region is
        not found in the CSV.
    """
    import csv as _csv
    from pathlib import Path

    csv_path = Path(clup_csv)
    if not csv_path.exists():
        return None

    region_lower = region.lower()
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = _csv.DictReader(f)
        for row in reader:
            if region_lower not in row.get("region", "").lower():
                continue

            ipa_chars = int(row.get("ipa_chars", "1") or "1")
            weights: Dict[str, float] = {}

            # Boolean flags: YES → 1.0, else 0.0
            for csv_col, key in _CLUP_BOOL_COLUMNS.items():
                val = row.get(csv_col, "").strip().upper()
                weights[key] = 1.0 if val == "YES" else 0.0

            # Direct rate columns (already float in CSV)
            for csv_col, key in _CLUP_RATE_COLUMNS.items():
                try:
                    weights[key] = float(row.get(csv_col, "0") or "0")
                except ValueError:
                    weights[key] = 0.0

            # Count columns → normalize by ipa_chars
            for csv_col, key in _CLUP_COUNT_COLUMNS.items():
                try:
                    count = int(row.get(csv_col, "0") or "0")
                except ValueError:
                    count = 0
                weights[key] = round(count / ipa_chars, 6) if ipa_chars > 0 else 0.0

            return weights

    return None


#: Rule IDs that are gated by allophone weight keys.
#: When ``allophone_weights`` is provided to ``apply_transform``, rules whose
#: ID appears here will only fire if the corresponding weight exceeds the
#: threshold.
ALLOPHONE_GATED_RULES: Dict[str, tuple] = {
    # rule_id: (weight_key, threshold)
    # Spirantization-related de-biasing: if the region HAS spirants,
    # keep them (skip DB4/DB5/DB6 normalization)
    "N1": ("spirantization_rate", 0.0),  # betacism — always allow if in profile
    "BMD1a": ("retroflex_sibilant", 0.0),  # retroflex sibilants gate apico rules
}
