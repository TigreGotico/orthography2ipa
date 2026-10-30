"""The da/ipa_childes row is documented notation, not a ceiling (T-2702).

Danish orthography does not write stød, but folding it moves this row by only
0.0342. Every larger mover is a convention of the espeak-derived gold, so no
`valid_ceiling` is recorded (T-2583).
"""
from orthography2ipa import json_loader


def test_ipa_childes_is_an_audit_not_a_ceiling():
    spec = json_loader.load_json_spec("da")
    assert "ipa_childes" not in (spec.valid_ceiling or {})
    entry = spec.audit["ipa_childes"]
    assert entry.conclusion == "at_ceiling_documented"
    for number in ("0.4476", "0.4134", "0.2841", "0.2108"):
        assert number in entry.measured, number


def test_the_fold_script_is_named():
    spec = json_loader.load_json_spec("da")
    assert "fold_da_notation.py" in spec.audit["ipa_childes"].measured
