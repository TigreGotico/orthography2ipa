"""The ja/vox_communis row is logographic, like ja/ipadict.

65.9% of the snapshot's words carry a kanji, and a Kana spec transcribes a
kanji to nothing, so those words score 0.65 while pure-kana words score
0.0784. No rule change closes the kanji share.
"""
from orthography2ipa import json_loader


def test_vox_communis_is_audited_as_logographic():
    spec = json_loader.load_json_spec("ja")
    assert "vox_communis" not in (spec.valid_ceiling or {})
    entry = spec.audit["vox_communis"]
    assert entry.conclusion == "logographic"
    for number in ("32033", "0.65", "16574", "0.0784", "0.0385"):
        assert number in entry.measured, number


def test_the_two_audits_agree_on_the_method():
    audit = json_loader.load_json_spec("ja").audit
    assert audit["ipadict"].conclusion == audit["vox_communis"].conclusion
    assert "CJK Unified Ideograph" in audit["vox_communis"].measured
