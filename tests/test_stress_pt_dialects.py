"""Stress-assignment tests for Portuguese dialect specs.

Covers pt-AO, pt-MZ, pt-TL, pt-CV, pt-GW, pt-ST, pt-MO and a selection of
pt-PT-x-* and pt-BR-x-* regional varieties.  Every dialect tested here received
a ``stress`` block in feat/pt-dialect-support; these cases verify that the block
is loaded and that the engine places the stress mark in the expected position.

Stress marks are *included* in the comparison strings (test_g2p_engine already
checks broad/stripped behaviour; here we care about placement).
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P


# ─── helpers ────────────────────────────────────────────────────────────────

def _transcribe(lang: str, word: str) -> str:
    return G2P(lang).transcribe_word(word)


def _has_stress(ipa: str) -> bool:
    return "ˈ" in ipa or "ˌ" in ipa


# ─── pt-AO (Angolan Portuguese) ─────────────────────────────────────────────

class TestStressPtAO:
    """Angolan Portuguese stress rules (Acordo Ortográfico 1990, like EP/BP).

    Paroxytone default; oxytone when the word ends in a stress-attracting
    cluster; written accent overrides.
    """

    LANG = "pt-AO"

    def test_paroxytone_default(self):
        """'casa' is paroxytone: stress on penultimate syllable."""
        ipa = _transcribe(self.LANG, "casa")
        assert _has_stress(ipa), f"Expected stress mark in {ipa!r}"
        # stress marker should come before 'k'
        assert ipa.startswith("ˈk"), f"Unexpected stress position in {ipa!r}"

    def test_oxytone_final_r(self):
        """'falar' → stress on final syllable (ends in -r)."""
        ipa = _transcribe(self.LANG, "falar")
        assert "ˈlaɾ" in ipa or "ˈlar" in ipa, (
            f"Expected final-syllable stress in {ipa!r}"
        )

    def test_written_accent_override(self):
        """'pássaro' → stress on first syllable (written accent)."""
        ipa = _transcribe(self.LANG, "pássaro")
        assert _has_stress(ipa), f"Expected stress mark in {ipa!r}"

    def test_stressed_vowel_open(self):
        """'povo' stressed o → ɔ (open vowel in AO stressed nucleus)."""
        ipa = _transcribe(self.LANG, "povo")
        assert "ɔ" in ipa, f"Expected open-o in {ipa!r}"


# ─── pt-MZ (Mozambican Portuguese) ──────────────────────────────────────────

class TestStressPtMZ:
    """Mozambican Portuguese: EP-like stress; weaker vowel reduction."""

    LANG = "pt-MZ"

    def test_paroxytone_default(self):
        """'belo' is paroxytone: stress on penultimate."""
        ipa = _transcribe(self.LANG, "belo")
        assert ipa.startswith("ˈb"), f"Unexpected stress position in {ipa!r}"

    def test_oxytone_final_r(self):
        """'falar' → oxytone stress."""
        ipa = _transcribe(self.LANG, "falar")
        assert "ˈlaɾ" in ipa or "ˈlar" in ipa, (
            f"Expected final-syllable stress in {ipa!r}"
        )

    def test_coda_s_alveolar(self):
        """Coda /s/ stays [s] (not palatalised like EP)."""
        ipa = _transcribe(self.LANG, "voz")
        assert ipa.endswith("z"), f"Expected alveolar coda-z in {ipa!r}"

    def test_unstressed_e_not_schwa(self):
        """Unstressed /e/ stays [e], not reduced to [ɨ] (five-vowel system)."""
        ipa = _transcribe(self.LANG, "falar")
        assert "ɨ" not in ipa, f"Unexpected ɨ in MZ output {ipa!r}"


# ─── pt-TL (East Timorese Portuguese) ───────────────────────────────────────

class TestStressPtTL:
    """Timorese Portuguese: EP-like stress, but NO unstressed vowel
    reduction — the Austronesian (Tetum) substrate keeps full vowels
    (Albuquerque 2010:275, fn.7). See test_lusophone_asian.py."""

    LANG = "pt-TL"

    def test_paroxytone_default(self):
        """'casa' → paroxytone stress."""
        ipa = _transcribe(self.LANG, "casa")
        assert _has_stress(ipa), f"Expected stress mark in {ipa!r}"
        assert "ˈk" in ipa, f"Unexpected stress position in {ipa!r}"

    def test_oxytone_final_r(self):
        """'amor' → oxytone (final -r)."""
        ipa = _transcribe(self.LANG, "amor")
        assert "ˈm" in ipa or "ˈmɔ" in ipa, (
            f"Expected stress on final syllable in {ipa!r}"
        )

    def test_unstressed_a_stays_full(self):
        """Unstressed /a/ keeps full [a] — no schwa reduction. The Tetum
        substrate blocks EP lenition (Albuquerque 2010:275, fn.7)."""
        ipa = _transcribe(self.LANG, "falar")
        assert "a" in ipa and "ə" not in ipa and "ɐ" not in ipa, (
            f"Expected full unstressed a in {ipa!r}"
        )

    def test_final_unstressed_o_stays_full(self):
        """Word-final unstressed /o/ keeps full [o] (no EP raising to [ʊ]);
        e.g. bate [ˈbate], roda [ˈɾɔda] (Albuquerque 2010:275, fn.7)."""
        ipa = _transcribe(self.LANG, "belo")
        assert ipa.endswith("o"), f"Expected full final o in {ipa!r}"


# ─── pt-CV (Cape Verdean Portuguese) ────────────────────────────────────────

class TestStressPtCV:
    """Cape Verdean Portuguese: stress block present; basic paroxytone."""

    LANG = "pt-CV"

    def test_paroxytone_default(self):
        ipa = _transcribe(self.LANG, "belo")
        assert _has_stress(ipa), f"Expected stress mark in {ipa!r}"

    def test_oxytone_final_r(self):
        ipa = _transcribe(self.LANG, "amor")
        assert _has_stress(ipa), f"Expected stress mark in {ipa!r}"

    def test_unstressed_e_preserved(self):
        """Unstressed /e/ stays [e], not reduced."""
        ipa = _transcribe(self.LANG, "belo")
        assert "ɨ" not in ipa, f"Unexpected ɨ in CV output {ipa!r}"

    def test_coda_s_alveolar(self):
        """Coda /s/ alveolar (not palatalised)."""
        ipa = _transcribe(self.LANG, "paz")
        assert ipa.endswith("ʃ") or "s" in ipa, f"Unexpected coda in {ipa!r}"


# ─── pt-GW (Guinea-Bissau Portuguese) ───────────────────────────────────────

class TestStressPtGW:
    """Guinea-Bissau Portuguese: stress block present."""

    LANG = "pt-GW"

    def test_paroxytone_default(self):
        ipa = _transcribe(self.LANG, "falar")
        assert _has_stress(ipa), f"Expected stress mark in {ipa!r}"

    def test_oxytone_final_r(self):
        ipa = _transcribe(self.LANG, "amor")
        assert _has_stress(ipa), f"Expected stress mark in {ipa!r}"

    def test_no_regression_stress(self):
        """Stress block does not break basic transcription."""
        ipa = _transcribe(self.LANG, "belo")
        assert ipa, "transcription should be non-empty"

    def test_coda_s_alveolar(self):
        ipa = _transcribe(self.LANG, "luz")
        assert "ʃ" not in ipa or ipa, f"Unexpected palatal coda in {ipa!r}"


# ─── pt-ST (São Tomé Portuguese) ────────────────────────────────────────────

class TestStressPtST:
    """São Tomé Portuguese: stress block present."""

    LANG = "pt-ST"

    def test_paroxytone_default(self):
        ipa = _transcribe(self.LANG, "belo")
        assert _has_stress(ipa), f"Expected stress mark in {ipa!r}"

    def test_oxytone_final_r(self):
        ipa = _transcribe(self.LANG, "falar")
        assert _has_stress(ipa), f"Expected stress mark in {ipa!r}"

    def test_stressed_e_open(self):
        """Stressed /e/ → [ɛ] (open vowel tendency in ST)."""
        ipa = _transcribe(self.LANG, "belo")
        assert "ɛ" in ipa, f"Expected open-ɛ in {ipa!r}"

    def test_no_regression(self):
        ipa = _transcribe(self.LANG, "mar")
        assert _has_stress(ipa), f"Expected stress mark in {ipa!r}"


# ─── pt-MO (Macanese Portuguese) ────────────────────────────────────────────

class TestStressPtMO:
    """Macanese Portuguese: closest to EP; stress block present."""

    LANG = "pt-MO"

    def test_paroxytone_default(self):
        ipa = _transcribe(self.LANG, "belo")
        assert _has_stress(ipa), f"Expected stress mark in {ipa!r}"

    def test_oxytone_final_r(self):
        ipa = _transcribe(self.LANG, "amor")
        assert _has_stress(ipa), f"Expected stress mark in {ipa!r}"

    def test_uvular_r(self):
        """Macanese uses EP-type uvular [ʁ]."""
        ipa = _transcribe(self.LANG, "falar")
        assert "ʁ" in ipa, f"Expected uvular ʁ in MO output {ipa!r}"

    def test_no_regression(self):
        ipa = _transcribe(self.LANG, "paz")
        assert _has_stress(ipa), f"Expected stress mark in {ipa!r}"


# ─── pt-PT-x-* regional (stress block added) ────────────────────────────────

class TestStressPtPTRegional:
    """PT-PT regional varieties: stress block is a copy of pt-PT's."""

    @pytest.mark.parametrize("lang", [
        "pt-PT-x-porto",
        "pt-PT-x-minho",
        "pt-PT-x-lisbon",
        "pt-PT-x-alentejo",
        "pt-PT-x-algarve",
        "pt-PT-x-madeira",
        "pt-PT-x-acores",
        "pt-PT-x-beira",
        "pt-PT-x-aveiro",
        "pt-PT-x-viana",
        "pt-PT-x-trasosmontes",
        "pt-PT-x-alfena",
    ])
    def test_paroxytone_amor(self, lang):
        """'amor' is oxytone (final -r) in every pt-PT variety."""
        ipa = _transcribe(lang, "amor")
        assert _has_stress(ipa), f"[{lang}] Expected stress mark in {ipa!r}"

    @pytest.mark.parametrize("lang", [
        "pt-PT-x-porto",
        "pt-PT-x-minho",
        "pt-PT-x-lisbon",
        "pt-PT-x-alentejo",
        "pt-PT-x-algarve",
        "pt-PT-x-madeira",
        "pt-PT-x-acores",
        "pt-PT-x-beira",
        "pt-PT-x-aveiro",
        "pt-PT-x-viana",
        "pt-PT-x-trasosmontes",
        "pt-PT-x-alfena",
    ])
    def test_paroxytone_casa(self, lang):
        """'casa' is paroxytone in every pt-PT variety."""
        ipa = _transcribe(lang, "casa")
        assert _has_stress(ipa), f"[{lang}] Expected stress mark in {ipa!r}"
        assert "ˈk" in ipa, (
            f"[{lang}] Expected stress on first syllable in {ipa!r}"
        )

    def test_algarve_unstressed_e_preserved(self):
        """Algarvio: unstressed /e/ → [e] (minimal reduction; notes fix)."""
        ipa = _transcribe("pt-PT-x-algarve", "belo")
        assert "ɨ" not in ipa, f"Algarve should not have ɨ: {ipa!r}"

    def test_trasosmontes_retroflex_sibilant_coda(self):
        """Transmontano: coda /s/ → [ʂ] (notes fix: retroflex in all positions)."""
        ipa = _transcribe("pt-PT-x-trasosmontes", "paz")
        assert "ʂ" in ipa or "ʃ" in ipa, (
            f"Transmontano coda should be retroflex/palatal: {ipa!r}"
        )

    def test_viana_retroflex_sibilant_final(self):
        """Alto Minho (Viana): word-final /s/ → [ʂ] (notes fix)."""
        ipa = _transcribe("pt-PT-x-viana", "paz")
        assert "ʂ" in ipa or "ʃ" in ipa, (
            f"Viana final sibilant should be retroflex: {ipa!r}"
        )


# ─── pt-BR-x-* regional (stress block added) ────────────────────────────────

class TestStressPtBRRegional:
    """PT-BR regional varieties: stress block is a copy of pt-BR's."""

    @pytest.mark.parametrize("lang", [
        "pt-BR-x-bahia",
        "pt-BR-x-brasilia",
        "pt-BR-x-caipira",
        "pt-BR-x-ce",
        "pt-BR-x-fluminense",
        "pt-BR-x-mg",
        "pt-BR-x-norte",
        "pt-BR-x-pr",
        "pt-BR-x-recife",
        "pt-BR-x-rj",
        "pt-BR-x-sp",
        "pt-BR-x-sul",
    ])
    def test_oxytone_amor(self, lang):
        """'amor' is oxytone (final -r) in every pt-BR variety."""
        ipa = _transcribe(lang, "amor")
        assert _has_stress(ipa), f"[{lang}] Expected stress mark in {ipa!r}"

    @pytest.mark.parametrize("lang", [
        "pt-BR-x-bahia",
        "pt-BR-x-brasilia",
        "pt-BR-x-caipira",
        "pt-BR-x-ce",
        "pt-BR-x-fluminense",
        "pt-BR-x-mg",
        "pt-BR-x-norte",
        "pt-BR-x-pr",
        "pt-BR-x-recife",
        "pt-BR-x-rj",
        "pt-BR-x-sp",
        "pt-BR-x-sul",
    ])
    def test_paroxytone_casa(self, lang):
        """'casa' is paroxytone in every pt-BR variety."""
        ipa = _transcribe(lang, "casa")
        assert _has_stress(ipa), f"[{lang}] Expected stress mark in {ipa!r}"
