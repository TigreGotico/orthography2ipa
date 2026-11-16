from orthography2ipa import json_loader


def test_yo_vox_communis_fold_is_an_audit_not_a_ceiling():
    # Yoruba spelling writes tone; the epitran gold omits it. A ceiling is
    # only for a contrast the orthography does not write, so the fold
    # lives in audit.vox_communis (T-2583).
    spec = json_loader.load_json_spec("yo")
    assert "vox_communis" not in (spec.valid_ceiling or {})
    assert spec.audit["vox_communis"].conclusion == "at_ceiling_documented"
    assert "0.0798" in spec.audit["vox_communis"].measured
