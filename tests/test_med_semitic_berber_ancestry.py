"""Ancestry-chain tests for the med-semitic-berber batch: xpu, uga, hbo, jrb,
ajt, aju, yhd, rif, gnc, plus the he -> hbo ancestry rewire.

Chains exercised:
    xpu -> phn -> x-clade-semi1276
    uga -> x-clade-semi1276
    hbo -> sem-x-central          he -> hbo -> sem-x-central
    jrb -> arb                    (macrolanguage collective, not a clade)
    ajt -> jrb / ar-TN            aju -> jrb / ar-MA           yhd -> jrb / ar-IQ
    rif -> ber                    gnc -> ber
"""
import pytest

import orthography2ipa
from orthography2ipa.types import QualityTier, AncestorRole


@pytest.mark.parametrize("code", [
    "xpu", "uga", "hbo", "jrb", "ajt", "yhd", "rif", "gnc",
])
def test_new_specs_resolve(code):
    spec = orthography2ipa.get(code)
    assert spec is not None
    assert spec.code == code


@pytest.mark.xfail(
    reason=(
        "KNOWN ENGINE LIMITATION (not fixed here: data-only constraint on this "
        "campaign): langcodes.standardize_tag('aju', macro=True) collapses "
        "'aju' to its ISO macrolanguage 'jrb' before orthography2ipa.registry "
        "checks for an exact spec match, same class of collision documented "
        "in registry.py for bxr/diq. The upstream fix is a one-line pin in "
        "registry.py's _ALIASES table ('aju': 'aju'), matching the existing "
        "bxr/diq precedent; out of scope for a DATA-ONLY spec-adding pass."
    ),
    strict=True,
)
def test_aju_resolve_blocked_by_langcodes_macro_collapse():
    spec = orthography2ipa.get("aju")
    assert spec.code == "aju"


class TestPunicUnderPhoenician:
    def test_parent(self):
        assert orthography2ipa.get("xpu").parent == "phn"

    def test_stub_tier(self):
        assert orthography2ipa.get("xpu").quality is QualityTier.STUB

    def test_chain_reaches_semitic_clade(self):
        assert orthography2ipa.get("phn").parent == "x-clade-semi1276"


class TestUgaritic:
    def test_parent(self):
        assert orthography2ipa.get("uga").parent == "x-clade-semi1276"

    def test_has_grapheme_table(self):
        # Ugaritic is research-quality: the 30-sign transliteration table is
        # sourced, unlike the sibling ancient-language stubs in this batch.
        uga = orthography2ipa.get("uga")
        assert uga.quality is QualityTier.RESEARCH
        assert len(uga.graphemes) > 20


class TestHebrewLineage:
    def test_hbo_parent(self):
        assert orthography2ipa.get("hbo").parent == "sem-x-central"

    def test_hbo_is_stub(self):
        assert orthography2ipa.get("hbo").quality is QualityTier.STUB

    def test_he_now_descends_from_hbo(self):
        he = orthography2ipa.get("he")
        assert he.parent == "hbo"
        parents = he.get_ancestors(AncestorRole.PARENT)
        assert [a.code for a in parents] == ["hbo"]


class TestJudeoArabicMacronode:
    def test_jrb_parent(self):
        assert orthography2ipa.get("jrb").parent == "arb"

    def test_jrb_is_stub_not_clade(self):
        jrb = orthography2ipa.get("jrb")
        assert jrb.quality is QualityTier.STUB
        assert jrb.clade is False

    @pytest.mark.parametrize("code,regional_parent", [
        ("ajt", "ar-TN"),
        ("yhd", "ar-IQ"),
        # "aju" excluded: blocked by the langcodes macro-collapse xfail above.
    ])
    def test_dual_parentage(self, code, regional_parent):
        spec = orthography2ipa.get(code)
        codes = {a.code for a in spec.get_ancestors(AncestorRole.PARENT)}
        assert "jrb" in codes
        assert regional_parent in codes

    @pytest.mark.parametrize("code", ["ajt", "yhd"])
    def test_hebrew_is_adstrate(self, code):
        spec = orthography2ipa.get(code)
        adstrates = {a.code for a in spec.get_ancestors(AncestorRole.ADSTRATE)}
        assert "he" in adstrates


class TestBerberBranch:
    def test_rif_parent(self):
        assert orthography2ipa.get("rif").parent == "ber"

    def test_rif_research_quality_with_inventory(self):
        rif = orthography2ipa.get("rif")
        assert rif.quality is QualityTier.RESEARCH
        assert len(rif.graphemes) > 10

    def test_rif_adstrates(self):
        rif = orthography2ipa.get("rif")
        adstrates = {a.code for a in rif.get_ancestors(AncestorRole.ADSTRATE)}
        assert "es-ES" in adstrates
        assert "ar" in adstrates

    def test_gnc_parent_and_stub(self):
        gnc = orthography2ipa.get("gnc")
        assert gnc.parent == "ber"
        assert gnc.quality is QualityTier.STUB
        assert gnc.graphemes == {}
