"""Spelling divergence — how differently two orthographies WRITE the same sounds.

The inverse of `grapheme_divergence`. Orthography and phonology are orthogonal,
and Galician is the proof: reintegrationist and RAG Galician are the same
language with the same phonology, spelled by different conventions.
"""
import orthography2ipa as o2i
from orthography2ipa import (
    grapheme_divergence,
    phonological_distance,
    spelling_divergence,
)


def test_spelling_divergence_sees_what_reading_divergence_cannot():
    """The two metrics answer different questions.

    Reading: given the same TEXT, do these sound alike?
    Spelling: given the same SOUND, do these write it alike?
    """
    rag = o2i.get("gl")
    reint = o2i.get("gl-x-reintegrado")
    pt = o2i.get("pt-PT")

    # /ɲ/ is written <ñ> by the RAG norm (a Castilian convention) and <nh> by the
    # reintegrationist norm (as Portuguese writes it). The graphemes are not even
    # shared, so reading divergence cannot compare them at all.
    assert "ɲ" in {i for v in rag.graphemes.values() if v for i in v}
    assert rag.graphemes["ñ"] == ["ɲ"]
    assert reint.graphemes["nh"] == ["ɲ"]
    assert pt.graphemes["nh"] == ["ɲ"]

    # Spelling divergence is what notices that reintegrationist writes Galician
    # the way Portuguese writes it.
    assert (spelling_divergence(reint, pt).mean_distance
            < spelling_divergence(rag, pt).mean_distance)


def test_reintegrationist_galician_spells_more_like_portuguese_than_rag_does():
    """The reintegrationist claim, made measurable."""
    to_pt_reint = spelling_divergence(
        o2i.get("gl-x-reintegrado"), o2i.get("pt-PT")).mean_distance
    to_pt_rag = spelling_divergence(
        o2i.get("gl"), o2i.get("pt-PT")).mean_distance
    assert to_pt_reint < to_pt_rag


def test_rag_galician_spells_more_like_spanish_than_like_portuguese():
    """The other half of the same claim: the official norm follows Castilian
    convention. This is the reintegrationist critique, and it is measurable."""
    rag = o2i.get("gl")
    to_es = spelling_divergence(rag, o2i.get("es-ES")).mean_distance
    to_pt = spelling_divergence(rag, o2i.get("pt-PT")).mean_distance
    assert to_es < to_pt


def test_the_two_norms_are_phonologically_the_same_language():
    """A norm is an orthography, not a variety. Both specs inherit their
    phonology from the same source, so their phoneme inventories and allophony
    are identical — only the spelling differs."""
    rag = o2i.get("gl")
    reint = o2i.get("gl-x-reintegrado")
    pt = o2i.get("pt-PT")

    assert reint.allophones == rag.allophones

    # The genuinely phonological components are identical against a third
    # language, as they must be for the same phonology.
    assert (phonological_distance(reint, pt).allophone_sim
            == phonological_distance(rag, pt).allophone_sim)


def test_spelling_divergence_is_zero_for_a_spec_against_itself():
    pt = o2i.get("pt-PT")
    result = spelling_divergence(pt, pt)
    assert result.mean_distance == 0.0
    assert result.disjoint_spellings == 0
    assert result.shared_phonemes == result.total_phonemes


def test_same_orthography_different_pronunciation_has_low_spelling_divergence():
    """pt-PT and pt-BR share one orthography (the same Agreement) but differ
    phonologically — spelling divergence should be near nil even though the two
    sound quite different."""
    assert spelling_divergence(
        o2i.get("pt-PT"), o2i.get("pt-BR")).mean_distance < 0.10
