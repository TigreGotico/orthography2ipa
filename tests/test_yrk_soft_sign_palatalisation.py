"""Regression test for the Tundra Nenets (yrk) Cyrillic soft sign ⟨ь⟩.

``yrk.json`` used to map the bare soft sign to an empty candidate, deleting it
outright and dropping palatalisation everywhere it occurs: ``ванесь`` (gold,
wikipron, ``w ʌ nʲ e sʲ``) came out with no ``ʲ`` at all. The soft sign is a
palatalisation mark, not a silent letter -- the ru and uk specs already map it
to /ʲ/ and compose it onto the preceding consonant.

Unlike the analogous Ket fix, the wikipron gold for the consonants that
actually precede ⟨ь⟩ in this dataset (с, з, н, л; ц is handled by its own
affricate mapping) shows plain C+ʲ concatenation, not a fused single segment:
``-сь`` -> ``sʲ``, ``-зь`` -> ``zʲ``, ``-нь`` -> ``nʲ``, ``-ль`` -> ``lʲ``. So
no Cyrillic+ь multigraph keys are needed here; the bare soft sign composing
/ʲ/ generically is already correct.
"""
from orthography2ipa.json_loader import load_json_spec

import orthography2ipa


def test_yrk_spec_maps_bare_soft_sign_to_palatalisation():
    spec = load_json_spec("yrk")
    assert list(spec.graphemes["ь"]) == ["ʲ"]


def test_yrk_spec_has_no_soft_sign_multigraph_keys():
    # The wikipron gold shows plain C+ʲ concatenation for every consonant
    # attested before ⟨ь⟩ (с, з, н, л), so nothing needs its own fused key.
    spec = load_json_spec("yrk")
    assert not any(k.endswith("ь") and len(k) > 1 for k in spec.graphemes)


def test_yrk_soft_sign_palatalises_the_preceding_consonant():
    # ванесь: gold w ʌ nʲ e sʲ (wikipron). Was missing both ʲ when ь deleted.
    result = orthography2ipa.transcribe("ванесь", "yrk")
    assert "nʲ" in result
    assert result.endswith("sʲ")


def test_yrk_soft_sign_palatalises_final_consonants():
    # мань: gold m ʌ nʲ (wikipron).
    assert orthography2ipa.transcribe("мань", "yrk").endswith("nʲ")
    # манзь: gold m ʌ n zʲ (wikipron).
    assert orthography2ipa.transcribe("манзь", "yrk").endswith("zʲ")
