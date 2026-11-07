from orthography2ipa import json_loader


def test_vi_vox_communis_fold_is_an_audit_not_a_ceiling():
    # Quoc ngu writes tone and the folded vowel letters. A ceiling is only
    # for a contrast the orthography does not write, so the notation
    # ladder lives in audit.vox_communis (T-2583).
    spec = json_loader.load_json_spec("vi")
    assert "vox_communis" not in (spec.valid_ceiling or {})
    assert spec.audit["vox_communis"].conclusion == "at_ceiling_documented"
    assert "0.0246" in spec.audit["vox_communis"].measured
