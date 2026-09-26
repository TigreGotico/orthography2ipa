"""Tests for scripts/which_tests.py.

A Scottish Gaelic pre-aspiration fix passed ``tests/test_celtic.py`` and only
broke ``tests/test_cited_rules_germanic_celtic.py`` in CI, because nothing
told the author that file also asserts on ``gd``. The script's whole job is
to surface both files for a given code, so the regression test pins exactly
that pair, plus the short-code cases (``br``, ``an``) that a naive substring
match would flood with garbage.
"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import which_tests as wt  # noqa: E402

_REPO = os.path.join(os.path.dirname(__file__), "..")


def test_gd_reports_both_family_and_cited_rules_files():
    hits, _total = wt.matching_test_files("gd", include_children=False, repo=_REPO)
    assert "tests/test_celtic.py" in hits
    assert "tests/test_cited_rules_germanic_celtic.py" in hits


def test_short_codes_do_not_return_garbage():
    # every hit must genuinely reference the code as a quoted token, not
    # merely contain it as a substring of an unrelated word.
    for lang in ("br", "an"):
        hits, _total = wt.matching_test_files(lang, include_children=False, repo=_REPO)
        assert hits
        for rel in hits:
            with open(os.path.join(_REPO, rel), encoding="utf-8") as fh:
                text = fh.read()
            assert f'"{lang}"' in text or f"'{lang}'" in text


def test_include_children_only_adds_files():
    without, _total = wt.matching_test_files("pt-PT", include_children=False, repo=_REPO)
    with_children, _total = wt.matching_test_files("pt-PT", include_children=True, repo=_REPO)
    assert set(without) <= set(with_children)
    assert set(without) != set(with_children)


def test_unreferenced_code_returns_nothing():
    code = "po" + "x"  # split so this file's own source is not a false hit
    hits, total = wt.matching_test_files(code, include_children=False, repo=_REPO)
    assert hits == []
    assert total > 0  # it did search a real suite, this is a genuine negative


def test_missing_repo_raises_instead_of_reporting_a_false_all_clear():
    # An empty directory has neither tests/ nor orthography2ipa/data/. Silently
    # searching nothing and reporting "no references" would be indistinguishable
    # from a genuine all-clear on the one question this tool exists to answer.
    with tempfile.TemporaryDirectory() as empty:
        try:
            wt.matching_test_files("gd", include_children=False, repo=empty)
        except wt.RepoLayoutError as exc:
            assert empty in str(exc)
        else:
            assert False, "expected RepoLayoutError for a repo with no tests/"


def test_main_exits_nonzero_and_names_the_path_for_a_missing_repo(capsys):
    with tempfile.TemporaryDirectory() as empty:
        argv = sys.argv
        sys.argv = ["which_tests.py", "--lang", "gd", "--repo", empty]
        try:
            rc = wt.main()
        finally:
            sys.argv = argv
        assert rc != 0
        captured = capsys.readouterr()
        assert empty in captured.err


def test_spec_descendants_follows_parent_and_base_refs():
    descendants = wt.spec_descendants("pt-PT", repo=_REPO)
    assert "pt-PT" in descendants
    assert "pt-PT-x-lisbon" in descendants
