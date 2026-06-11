"""Signature-word tests for the seven European-Portuguese regional dialect specs.

Each test asserts one or more phonemically diagnostic words per dialect as
documented in DIALECT_PATTERNS.md and whitepaper5 (TigreGotico internal
dialect research). The words are drawn from the research sources and cross-
checked against the ep_dialect_sentences.csv gold set.

Dialect specs under test:
    pt-PT-x-lisbon   — Lisbon prestige
    pt-PT-x-porto    — Porto/Northern EP
    pt-PT            — Conservative standard (Coimbra-type)
    pt-PT-x-alentejo — Alentejo
    pt-PT-x-algarve  — Algarve
    pt-PT-x-madeira  — Madeira
    pt-PT-x-acores   — Azores (São Miguel class for u→y)
"""
from __future__ import annotations


import pytest
from orthography2ipa import G2P


def _t(lang: str) -> G2P:
    return G2P(lang)


def bare(s: str) -> str:
    """Strip stress marks for bare phoneme comparison."""
    return s.replace("ˈ", "").replace("ˌ", "")


# ─── pt-PT-x-lisbon ─────────────────────────────────────────────────────────


class TestLisbon:
    """Lisbon: ei→ɐj, ou→o are the categorical grapheme-level features."""

    def test_ei_lowering_leite(self):
        """‹ei› → [ɐj] — Lisbon diphthong lowering (DIALECT_PATTERNS §Diphthongs)."""
        eng = _t("pt-PT-x-lisbon")
        assert "ɐj" in bare(eng.transcribe_word("leite"))

    def test_ei_lowering_primeiro(self):
        eng = _t("pt-PT-x-lisbon")
        assert "ɐj" in bare(eng.transcribe_word("primeiro"))

    def test_ou_monophthong_ouro(self):
        """‹ou› → [o] — monophthongization (no diphthong in Lisbon)."""
        eng = _t("pt-PT-x-lisbon")
        result = bare(eng.transcribe_word("ouro"))
        assert "o" in result
        assert "ow" not in result

    def test_no_betacism(self):
        """Lisbon preserves /v/ ≠ /b/."""
        eng = _t("pt-PT-x-lisbon")
        assert bare(eng.transcribe_word("vinho")).startswith("v")


# ─── pt-PT-x-porto ──────────────────────────────────────────────────────────


class TestPorto:
    """Porto/Northern EP: betacism (v→b), ou→ow, ei→ej."""

    def test_betacism_vinho(self):
        """/v/ → [b] — categorical merger (DIALECT_PATTERNS §Betacism)."""
        eng = _t("pt-PT-x-porto")
        assert bare(eng.transcribe_word("vinho")).startswith("b")

    def test_betacism_vaca(self):
        eng = _t("pt-PT-x-porto")
        assert bare(eng.transcribe_word("vaca")).startswith("b")

    def test_ou_preserved_ouro(self):
        """‹ou› → [ow] — diphthong preserved in Northern EP."""
        eng = _t("pt-PT-x-porto")
        assert "ow" in bare(eng.transcribe_word("ouro"))

    def test_ei_preserved(self):
        """‹ei› → [ej] — not lowered to [ɐj] as in Lisbon."""
        eng = _t("pt-PT-x-porto")
        result = bare(eng.transcribe_word("leite"))
        assert "ej" in result
        assert "ɐj" not in result


# ─── pt-PT (Coimbra-type standard) ──────────────────────────────────────────


class TestStandard:
    """Conservative EP standard: ou→o, /v/ ≠ /b/, ei→ɐj/ej variable."""

    def test_ou_monophthong(self):
        """‹ou› → [o] as primary output (conservative standard)."""
        eng = _t("pt-PT")
        result = bare(eng.transcribe_word("ouro"))
        assert "ow" not in result

    def test_no_betacism(self):
        eng = _t("pt-PT")
        assert bare(eng.transcribe_word("vinho")).startswith("v")


# ─── pt-PT-x-alentejo ───────────────────────────────────────────────────────


class TestAlentejo:
    """Alentejo: intervocalic d-deletion, ei→e monophthong."""

    def test_d_deletion_nada(self):
        """Intervocalic /d/ → ∅ — nada→[naɐ] (DIALECT_PATTERNS §Intervocalic d)."""
        eng = _t("pt-PT-x-alentejo")
        result = bare(eng.transcribe_word("nada"))
        # intervocalic d deleted: naɐ or naa (no d between vowels)
        assert "d" not in result

    def test_d_deletion_vida(self):
        eng = _t("pt-PT-x-alentejo")
        assert "d" not in bare(eng.transcribe_word("vida"))

    def test_ei_monophthong_leite(self):
        """‹ei› → [e] — monophthongization (not [ɐj] as in Lisbon)."""
        eng = _t("pt-PT-x-alentejo")
        result = bare(eng.transcribe_word("leite"))
        assert "ej" not in result
        assert "ɐj" not in result

    def test_no_betacism(self):
        eng = _t("pt-PT-x-alentejo")
        assert bare(eng.transcribe_word("vinho")).startswith("v")


# ─── pt-PT-x-algarve ────────────────────────────────────────────────────────


class TestAlgarve:
    """Algarve: ei→e, word-final s→ʒ (sibilant voicing)."""

    def test_ei_monophthong(self):
        eng = _t("pt-PT-x-algarve")
        result = bare(eng.transcribe_word("leite"))
        assert "ej" not in result
        assert "ɐj" not in result

    def test_final_s_voicing_vamos(self):
        """Word-final /s/ → [ʒ] in Algarve (DIALECT_PATTERNS §Sibilant Voicing)."""
        eng = _t("pt-PT-x-algarve")
        assert bare(eng.transcribe_word("vamos")).endswith("ʒ")

    def test_final_s_voicing_turistas(self):
        eng = _t("pt-PT-x-algarve")
        assert bare(eng.transcribe_word("turistas")).endswith("ʒ")

    def test_no_betacism(self):
        eng = _t("pt-PT-x-algarve")
        assert bare(eng.transcribe_word("vinho")).startswith("v")


# ─── pt-PT-x-madeira ────────────────────────────────────────────────────────


class TestMadeira:
    """Madeira: nasal diphthong → nasal+n (ões→õns)."""

    def test_nasal_plus_n_veroes(self):
        """‹ões› → [õns] — nasal diphthong simplification (DIALECT_PATTERNS §Nasal Patterns)."""
        eng = _t("pt-PT-x-madeira")
        assert "õns" in bare(eng.transcribe_word("verões"))

    def test_nasal_plus_n_caes(self):
        """‹ães› → [ɐ̃ns]."""
        eng = _t("pt-PT-x-madeira")
        assert "ɐ̃ns" in bare(eng.transcribe_word("cães"))

    def test_no_betacism(self):
        eng = _t("pt-PT-x-madeira")
        assert bare(eng.transcribe_word("vinho")).startswith("v")


# ─── pt-PT-x-acores ─────────────────────────────────────────────────────────


class TestAcores:
    """Azores (São Miguel class): u→y, ou→ow, ões→õns."""

    def test_u_fronting_tu(self):
        """/u/ → [y] — São Miguel fronted-u feature (DIALECT_PATTERNS §Açores Fronted u)."""
        eng = _t("pt-PT-x-acores")
        assert bare(eng.transcribe_word("tu")) == "ty"

    def test_u_fronting_numero(self):
        eng = _t("pt-PT-x-acores")
        assert "y" in bare(eng.transcribe_word("número"))

    def test_ou_preserved(self):
        """‹ou› → [ow] — diphthong preserved in Azores."""
        eng = _t("pt-PT-x-acores")
        assert "ow" in bare(eng.transcribe_word("ouro"))

    def test_nasal_plus_n_veroes(self):
        """‹ões› → [õns] (shared with Madeira)."""
        eng = _t("pt-PT-x-acores")
        assert "õns" in bare(eng.transcribe_word("verões"))
