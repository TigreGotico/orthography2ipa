"""Tests for scripts/check_board_not_reverting.py.

The defect under test is invisible to every other gate: a branch merges dev,
resolves the conflicted board file by keeping its own copy, and so puts back
the numbers dev measured after the branch was cut. Both sides are internally
consistent, so nothing else fails.

The classification tests drive the verdict logic directly with synthetic
boards; the end-to-end tests build a real two-branch git repository so the
merge, the ownership evidence and the exit code are exercised the way CI runs
them.
"""
import json
import os
import subprocess
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import check_board_not_reverting as guard  # noqa: E402


def row(lang="mr", dataset="wikipron", per=0.4351, n=4267):
    return {"lang": lang, "dataset": dataset, "n": n, "per": per,
            "exact_match": 0.1, "quality_tier": "research", "harness_version": "1.1"}


def board(*rows):
    return {(r["lang"], r["dataset"]): r for r in rows}


NOTHING_OWNED = lambda lang: False  # noqa: E731
NEVER_SUPERSEDED = lambda key, value: False  # noqa: E731
NO_DECLARATION = (set(), False, "")


def superseding(*rows):
    """A ``superseded`` callable recognising *rows* as values dev moved past."""
    old = {(r["lang"], r["dataset"]): guard.scored(r) for r in rows}
    return lambda key, value: old.get(key) == guard.scored(value)


class TestClassification:
    def test_old_value_for_an_unowned_row_is_a_revert(self):
        """The merge would install a number dev already moved past, for a
        language this branch never touched."""
        old, new = row(per=0.4351), row(per=0.0535)
        reverts, undeclared, allowed = guard.classify(
            board(new), board(old), NOTHING_OWNED, superseding(old),
            NO_DECLARATION, False)
        assert [k for k, _, _ in reverts] == [("mr", "wikipron")]
        assert not undeclared and not allowed

    def test_declaration_cannot_excuse_a_revert(self):
        """Naming the row is prose; a stale copy can produce prose."""
        old, new = row(per=0.4351), row(per=0.0535)
        declared = ({("mr", "wikipron")}, True, "harness rework")
        reverts, _, allowed = guard.classify(
            board(new), board(old), NOTHING_OWNED, superseding(old),
            declared, True)
        assert [k for k, _, _ in reverts] == [("mr", "wikipron")]
        assert not allowed

    def test_owning_the_spec_does_excuse_an_old_value(self):
        """Reverting a spec change genuinely reproduces the old numbers, and a
        spec edit is evidence a stale copy cannot fake."""
        old, new = row(per=0.4351), row(per=0.0535)
        reverts, undeclared, allowed = guard.classify(
            board(new), board(old), lambda lang: lang == "mr", superseding(old),
            NO_DECLARATION, False)
        assert not reverts and not undeclared
        assert [k for k, _, _ in allowed] == [("mr", "wikipron")]

    def test_row_the_branch_rescored_itself_passes(self):
        reverts, undeclared, allowed = guard.classify(
            board(row(per=0.4351)), board(row(per=0.21)),
            lambda lang: lang == "mr", NEVER_SUPERSEDED, NO_DECLARATION, False)
        assert not reverts and not undeclared
        assert [k for k, _, _ in allowed] == [("mr", "wikipron")]

    def test_unchanged_rows_are_not_reported(self):
        same = board(row(), row("xh", "kaikki"))
        assert guard.classify(same, same, NOTHING_OWNED, NEVER_SUPERSEDED,
                              NO_DECLARATION, False) == ([], [], [])

    def test_provenance_only_movement_is_not_a_finding(self):
        """Only measurements are compared; a tier relabel moves no number."""
        before = row()
        after = dict(before, quality_tier="verified")
        assert guard.classify(board(before), board(after), NOTHING_OWNED,
                              NEVER_SUPERSEDED, NO_DECLARATION, False) \
            == ([], [], [])

    def test_new_row_is_allowed(self):
        _, undeclared, allowed = guard.classify(
            {}, board(row("tpw")), NOTHING_OWNED, NEVER_SUPERSEDED,
            NO_DECLARATION, False)
        assert not undeclared and len(allowed) == 1

    def test_restoring_a_row_dev_deleted_is_a_revert(self):
        gone = row("qu", "ipa_childes")
        reverts, _, allowed = guard.classify(
            {}, board(gone), NOTHING_OWNED, superseding(gone),
            NO_DECLARATION, False)
        assert [k for k, _, _ in reverts] == [("qu", "ipa_childes")]
        assert not allowed

    def test_move_without_ownership_or_declaration_fails(self):
        _, undeclared, allowed = guard.classify(
            board(row(per=0.4)), board(row(per=0.2)), NOTHING_OWNED,
            NEVER_SUPERSEDED, NO_DECLARATION, False)
        assert [k for k, _, _ in undeclared] == [("mr", "wikipron")]
        assert not allowed

    def test_row_deleted_by_the_branch_needs_ownership(self):
        _, undeclared, _ = guard.classify(
            board(row()), {}, NOTHING_OWNED, NEVER_SUPERSEDED,
            NO_DECLARATION, False)
        assert [k for k, _, _ in undeclared] == [("mr", "wikipron")]

    def test_rekeying_a_dataset_owns_both_sides(self):
        """Scoring a dataset against a better-fitting spec drops one row and
        adds another; the branch edits the spec it moved to."""
        _, undeclared, allowed = guard.classify(
            board(row("qu", "ipa_childes")), board(row("quz", "ipa_childes")),
            lambda lang: lang == "quz", NEVER_SUPERSEDED, NO_DECLARATION, False)
        assert not undeclared and len(allowed) == 2

    def test_dropping_a_row_is_not_licensed_by_an_unrelated_addition(self):
        _, undeclared, _ = guard.classify(
            board(row("qu", "ipa_childes")), board(row("quz", "wikipron")),
            lambda lang: lang == "quz", NEVER_SUPERSEDED, NO_DECLARATION, False)
        assert [k for k, _, _ in undeclared] == [("qu", "ipa_childes")]


class TestWideHarnessMovement:
    """A harness change SHOULD move every row — but only when declared."""

    def wide(self):
        base = board(row("mr", per=0.4), row("xh", "kaikki", per=0.3),
                     row("zu", per=0.2))
        merged = board(row("mr", per=0.41), row("xh", "kaikki", per=0.31),
                       row("zu", per=0.21))
        return base, merged

    def test_undeclared_wide_movement_fails_even_with_engine_touched(self):
        """Touching a harness file is not itself a licence — otherwise the
        guard is bypassed by editing one line of the engine."""
        base, merged = self.wide()
        _, undeclared, allowed = guard.classify(
            base, merged, NOTHING_OWNED, NEVER_SUPERSEDED, NO_DECLARATION, True)
        assert len(undeclared) == 3 and not allowed

    def test_declared_wide_movement_passes(self):
        base, merged = self.wide()
        declared = (set(), True, "stress placement reworked")
        reverts, undeclared, allowed = guard.classify(
            base, merged, NOTHING_OWNED, NEVER_SUPERSEDED, declared, True)
        assert not reverts and not undeclared and len(allowed) == 3

    def test_all_without_an_engine_change_is_not_a_licence(self):
        base, merged = self.wide()
        declared = (set(), True, "trust me")
        _, undeclared, _ = guard.classify(
            base, merged, NOTHING_OWNED, NEVER_SUPERSEDED, declared, False)
        assert len(undeclared) == 3

    def test_declared_wide_movement_still_catches_an_old_value(self):
        """The honest wide-movement PR that also puts one row back."""
        stale = row("zu", per=0.2)
        base = board(row("mr", per=0.4), row("xh", "kaikki", per=0.3),
                     row("zu", per=0.05))
        merged = board(row("mr", per=0.41), row("xh", "kaikki", per=0.31), stale)
        declared = (set(), True, "stress placement reworked")
        reverts, undeclared, allowed = guard.classify(
            base, merged, NOTHING_OWNED, superseding(stale), declared, True)
        assert [k for k, _, _ in reverts] == [("zu", "wikipron")]
        assert not undeclared and len(allowed) == 2


class TestDeclarationParsing:
    def test_named_rows(self):
        rows, all_, _ = guard.parse_declaration(
            "body\nBoard-Rows: mr/wikipron, mr/vox_communis\nmore")
        assert rows == {("mr", "wikipron"), ("mr", "vox_communis")}
        assert not all_

    def test_all_with_a_reason(self):
        rows, all_, reason = guard.parse_declaration(
            "Board-Rows: all - stress placement reworked")
        assert all_ and reason == "stress placement reworked" and not rows

    def test_all_without_a_reason_carries_none(self):
        _, all_, reason = guard.parse_declaration("Board-Rows: all")
        assert all_ and reason == ""

    def test_a_body_without_a_declaration_licenses_nothing(self):
        declared = guard.parse_declaration("just a normal PR body", None)
        assert declared == (set(), False, "")
        _, undeclared, _ = guard.classify(
            board(row(per=0.4)), board(row(per=0.2)), NOTHING_OWNED,
            NEVER_SUPERSEDED, declared, True)
        assert [k for k, _, _ in undeclared] == [("mr", "wikipron")]


class TestMarkdownBoard:
    def test_cells_are_read_under_their_headers(self):
        rows = guard._read_markdown(
            "# Scoreboard\n\n| Lang | Dataset | N | PER |\n|---|---|---:|---:|\n"
            "| mr | wikipron | 4267 | 0.0535 |\n")
        assert rows == {("mr", "wikipron"): {"Lang": "mr", "Dataset": "wikipron",
                                             "N": "4267", "PER": "0.0535"}}

    def test_the_differing_column_is_named(self):
        before = {"Lang": "es", "Dataset": "wikipron", "PER": "0.0797",
                  "PER CI low": "0.0790"}
        after = dict(before, **{"PER CI low": "0.0801"})
        assert guard._delta(before, after, "dev") == "PER CI low 0.0790 -> 0.0801"


class TestSpecResolution:
    """Board tags without a spec file of their own resolve like the harness."""

    @pytest.mark.parametrize("lang, code", [
        ("de", "de-DE"), ("en", "en-GB"), ("es", "es-ES"), ("fr", "fr-FR"),
        ("it", "it-IT"), ("ro", "ro-RO"), ("pt-BR-x-carioca", "pt-BR"),
    ])
    def test_bare_tag_resolves_to_its_spec(self, lang, code):
        repo = os.path.join(os.path.dirname(__file__), "..")
        assert guard.spec_code(lang, repo=repo) == code
        assert code in guard.spec_ancestors(lang, repo=repo)

    def test_a_tag_with_its_own_spec_is_its_own_spec(self):
        repo = os.path.join(os.path.dirname(__file__), "..")
        assert guard.spec_code("pt-PT", repo=repo) == "pt-PT"

    def test_a_swallowed_import_does_not_pass_the_tag_off_as_its_own_spec(self,
                                                                          monkeypatch):
        """de has no de.json; if the package cannot be imported, spec_code
        must not fall back to treating 'de' as its own spec, since that
        blocks a legitimate wave on de-DE.json blaming the author for a row
        it never had evidence to judge."""
        monkeypatch.setitem(sys.modules, "orthography2ipa", None)
        repo = os.path.join(os.path.dirname(__file__), "..")
        with pytest.raises(guard.PackageUnavailable):
            guard.spec_code("de", repo=repo)


def git(repo, *args):
    subprocess.run(("git", *args), cwd=repo, check=True, capture_output=True)


def write_board(repo, rows):
    os.makedirs(os.path.join(repo, "benchmarks"), exist_ok=True)
    for name, indent in (("results.json", 1), ("results_ci_sample.json", 2)):
        with open(os.path.join(repo, "benchmarks", name), "w", encoding="utf-8") as fh:
            json.dump(rows, fh, indent=indent)
    os.makedirs(os.path.join(repo, "docs"), exist_ok=True)
    with open(os.path.join(repo, "docs", "scoreboard.md"), "w", encoding="utf-8") as fh:
        fh.write("| Lang | Dataset | N | PER |\n|---|---|---:|---:|\n")
        for r in rows:
            fh.write(f"| {r['lang']} | {r['dataset']} | {r['n']} | {r['per']} |\n")


def merge_dev(repo, rows):
    """Merge dev into the branch and resolve the board to *rows*.

    Regenerating the board on both sides always conflicts textually, and the
    resolution is where the wrong value gets carried forward.
    """
    subprocess.run(("git", "merge", "--no-commit", "dev"), cwd=repo, capture_output=True)
    write_board(repo, rows)
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "merge dev")


def write_spec(repo, lang, note):
    os.makedirs(os.path.join(repo, "orthography2ipa", "data"), exist_ok=True)
    path = os.path.join(repo, "orthography2ipa", "data", f"{lang}.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"code": lang, "graphemes": {"a": "a"}, "notes": note}, fh)


@pytest.fixture
def repo(tmp_path):
    """Two-branch repository: dev rescored mr, the branch was cut before."""
    path = str(tmp_path / "repo")
    os.makedirs(path)
    git(path, "init", "-q", "-b", "dev")
    git(path, "config", "user.email", "t@example.com")
    git(path, "config", "user.name", "t")
    write_board(path, [row("mr", per=0.4351), row("xh", "kaikki", per=0.3)])
    write_spec(path, "mr", "base")
    write_spec(path, "xh", "base")
    git(path, "add", "-A")
    git(path, "commit", "-qm", "base")
    git(path, "branch", "wave")
    write_board(path, [row("mr", per=0.0535), row("xh", "kaikki", per=0.3)])
    write_spec(path, "mr", "schwa rule")
    git(path, "add", "-A")
    git(path, "commit", "-qm", "fix(mr): schwa")
    git(path, "checkout", "-q", "wave")
    return path


class TestEndToEnd:
    def test_merging_dev_and_keeping_the_stale_row_fails(self, repo, capsys):
        """The real defect: the branch merges dev, resolves the conflicted
        board by keeping its own file, and puts mr's old value back."""
        write_board(repo, [row("mr", per=0.4351), row("xh", "kaikki", per=0.25)])
        write_spec(repo, "xh", "nasals")
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "fix(xh): nasals")
        merge_dev(repo, [row("mr", per=0.4351), row("xh", "kaikki", per=0.25)])

        assert guard.check("dev", "HEAD", repo=repo) == 1
        out = capsys.readouterr().out
        assert "backwards" in out
        assert "mr (wikipron): per 0.0535 -> 0.4351" in out
        assert "already carried and moved past" in out

    def test_a_declaration_does_not_buy_off_the_stale_row(self, repo):
        write_board(repo, [row("mr", per=0.4351), row("xh", "kaikki", per=0.25)])
        write_spec(repo, "xh", "nasals")
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "fix(xh): nasals")
        merge_dev(repo, [row("mr", per=0.4351), row("xh", "kaikki", per=0.25)])

        assert guard.check("dev", "HEAD", repo=repo,
                           body="Board-Rows: mr/wikipron, xh/kaikki") == 1

    def test_merging_dev_and_keeping_its_rows_passes(self, repo):
        write_board(repo, [row("mr", per=0.4351), row("xh", "kaikki", per=0.25)])
        write_spec(repo, "xh", "nasals")
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "fix(xh): nasals")
        merge_dev(repo, [row("mr", per=0.0535), row("xh", "kaikki", per=0.25)])

        assert guard.check("dev", "HEAD", repo=repo) == 0

    def test_a_merely_stale_branch_passes(self, repo, capsys):
        """The branch never merged dev, so git's three-way merge keeps dev's
        mr row: the staleness never reaches dev and is not a finding."""
        write_board(repo, [row("mr", per=0.4351), row("xh", "kaikki", per=0.25)])
        write_spec(repo, "xh", "nasals")
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "fix(xh): nasals")

        assert guard.check("dev", "HEAD", repo=repo) == 0
        assert "backwards" not in capsys.readouterr().out.replace(
            "does not carry dev backwards", "")

    def test_a_board_that_does_not_merge_asks_for_a_resolution(self, repo, capsys):
        """Both sides rewrote the same row, so there is no merge result to
        judge and GitHub will not merge it either. The guard re-runs on the
        resolution, which is where a wrong value would appear."""
        write_board(repo, [row("mr", per=0.30), row("xh", "kaikki", per=0.3)])
        write_spec(repo, "mr", "different schwa rule")
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "fix(mr): other schwa")

        assert guard.check("dev", "HEAD", repo=repo) == 0
        assert "conflicted" in capsys.readouterr().out

    def test_a_branch_that_does_not_touch_the_board_passes(self, repo, capsys):
        """An engine, harness or test PR is not the guard's business, however
        far dev has moved since the branch was cut."""
        with open(os.path.join(repo, "orthography2ipa", "stress.py"), "w") as fh:
            fh.write("RULE = 1\n")
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "chore: stress")

        assert guard.check("dev", "HEAD", repo=repo) == 0
        assert "does not touch the board" in capsys.readouterr().out

    def test_undeclared_wide_movement_fails(self, repo):
        write_board(repo, [row("mr", per=0.44), row("xh", "kaikki", per=0.25)])
        with open(os.path.join(repo, "orthography2ipa", "stress.py"), "w") as fh:
            fh.write("RULE = 1\n")
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "fix: stress placement")
        merge_dev(repo, [row("mr", per=0.054), row("xh", "kaikki", per=0.25)])

        assert guard.check("dev", "HEAD", repo=repo) == 1

    def test_declared_wide_movement_passes(self, repo, capsys):
        write_board(repo, [row("mr", per=0.44), row("xh", "kaikki", per=0.25)])
        with open(os.path.join(repo, "orthography2ipa", "stress.py"), "w") as fh:
            fh.write("RULE = 1\n")
        git(repo, "add", "-A")
        git(repo, "commit", "-qm",
            "fix: stress placement\n\nBoard-Rows: all - every row rescored")
        merge_dev(repo, [row("mr", per=0.054), row("xh", "kaikki", per=0.25)])

        assert guard.check("dev", "HEAD", repo=repo) == 0
        assert "accounted for" in capsys.readouterr().out

    def test_declaration_read_from_the_pull_request_body(self, repo):
        write_board(repo, [row("mr", per=0.4351), row("xh", "kaikki", per=0.22)])
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "chore: rescore xh")
        merge_dev(repo, [row("mr", per=0.0535), row("xh", "kaikki", per=0.22)])

        assert guard.check("dev", "HEAD", repo=repo) == 1
        assert guard.check("dev", "HEAD", repo=repo,
                           body="Board-Rows: xh/kaikki") == 0

    def test_inherited_spec_owns_the_dialect_row(self, repo):
        """Editing pt-PT.json accounts for pt-PT-x-lisbon's row moving."""
        write_spec(repo, "pt-PT", "base")
        with open(os.path.join(repo, "orthography2ipa", "data",
                               "pt-PT-x-lisbon.json"), "w") as fh:
            json.dump({"code": "pt-PT-x-lisbon", "parent": "pt-PT"}, fh)
        write_board(repo, [row("mr", per=0.4351), row("xh", "kaikki", per=0.3),
                           row("pt-PT-x-lisbon", per=0.2)])
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "seed dialect")
        git(repo, "checkout", "-q", "dev")
        git(repo, "merge", "-q", "wave", "-m", "merge wave")
        git(repo, "checkout", "-q", "wave")

        write_board(repo, [row("mr", per=0.0535), row("xh", "kaikki", per=0.3),
                           row("pt-PT-x-lisbon", per=0.15)])
        write_spec(repo, "pt-PT", "vowel reduction")
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "fix(pt-PT): vowel reduction")

        assert guard.check("dev", "HEAD", repo=repo) == 0

    def test_branch_already_merged_is_a_no_op(self, repo):
        assert guard.check("dev", "dev", repo=repo) == 0

    def test_declaring_all_without_touching_engine_or_harness_code_fails(self, repo):
        """A pure data wave that declares 'Board-Rows: all' is not believed:
        the docstring's claim that the declaration requires the diff to
        actually touch harness or engine code is proven here rather than
        only by the classification-level tests, which can be satisfied by
        forcing engine_touched=True by hand."""
        write_board(repo, [row("mr", per=0.44), row("xh", "kaikki", per=0.25)])
        write_spec(repo, "mr", "unrelated data-only touch")
        git(repo, "add", "-A")
        git(repo, "commit", "-qm",
            "data: mr wave\n\nBoard-Rows: all - trust me, everything moved")
        merge_dev(repo, [row("mr", per=0.054), row("xh", "kaikki", per=0.25)])

        assert guard.check("dev", "HEAD", repo=repo) == 1

    def test_cannot_import_the_package_reports_a_verdict_the_guard_could_not_reach(
            self, repo, monkeypatch):
        """When orthography2ipa cannot be imported, the guard must not guess
        that a bare board tag like de is its own spec; it must say it cannot
        judge ownership, not blame the branch. de has no de.json of its own
        in this fixture, so resolving it requires the import spec_code falls
        back to when a tag has no spec file of its own."""
        write_board(repo, [row("mr", per=0.4351), row("xh", "kaikki", per=0.3),
                           row("de", "wikipron", per=0.2)])
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "chore: seed de")
        merge_dev(repo, [row("mr", per=0.4351), row("xh", "kaikki", per=0.3),
                          row("de", "wikipron", per=0.15)])

        monkeypatch.setitem(sys.modules, "orthography2ipa", None)
        assert guard.check("dev", "HEAD", repo=repo) == 2
