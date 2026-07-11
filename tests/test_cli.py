

def test_family_filter_matches_any_step_of_the_classification_path(capsys):
    """`family` is a Glottolog path ("Indo-European > Romance"). Filtering must
    accept the branch ("Romance") as well as the stock it sits in
    ("Indo-European", which selects every family beneath it), so normalising the
    field to a path does not break the short filter people actually type."""
    import pytest
    from orthography2ipa.cli import main

    for arg in ("Romance", "romance"):
        main(["list", "--family", arg])
        out = capsys.readouterr().out
        assert "Indo-European > Romance" in out
        assert "pt-PT" in out

    # The stock selects every family beneath it, not just an exact key.
    main(["list", "--family", "Indo-European"])
    out = capsys.readouterr().out
    assert "Indo-European > Romance" in out
    assert "Indo-European > Armenic" in out

    # An unknown family is still an error.
    with pytest.raises(SystemExit) as exc:
        main(["list", "--family", "Klingon"])
    assert exc.value.code == 1
