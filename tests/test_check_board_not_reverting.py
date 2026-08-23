"""Tests for scripts/check_board_not_reverting.py.

The defect under test is invisible to every other gate: a branch that
regenerated the board before other waves merged carries their pre-merge
values for rows it never touched, and the squash writes those values back
over dev. Both sides are internally consistent, so nothing else fails.

The classification tests drive the three-way comparison directly with
synthetic boards; the end-to-end tests build a real two-branch git
repository so the git plumbing, the ownership evidence and the exit code
are exercised the way CI runs them.
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
NO_DECLARATION = (set(), False, "")


class TestClassification:
    def test_carried_over_value_is_a_revert(self):
        """The branch's row is byte-identical to the merge base while the
        target has moved on: it cannot be a rescore, because the branch
        never produced that number."""
        old, new = row(per=0.4351), row(per=0.0535)
        reverts, undeclared, allowed = guard.classify(
            board(old), board(new), board(old), NOTHING_OWNED, NO_DECLARATION, False)
        assert [k for k, _, _ in reverts] == [("mr", "wikipron")]
        assert not undeclared and not allowed

    def test_declaration_cannot_excuse_a_revert(self):
        """Naming the row does not make a carried-over value a rescore."""
        old, new = row(per=0.4351), row(per=0.0535)
        declared = ({("mr", "wikipron")}, True, "harness rework")
        reverts, _, allowed = guard.classify(
            board(old), board(new), board(old), lambda lang: True, declared, True)
        assert [k for k, _, _ in reverts] == [("mr", "wikipron")]
        assert not allowed

    def test_row_the_branch_rescored_itself_passes(self):
        """The mirror case: the branch owns mr (it edited mr.json) and its
        value differs from both the target and the merge base."""
        reverts, undeclared, allowed = guard.classify(
            board(row(per=0.4351)), board(row(per=0.4351)), board(row(per=0.21)),
            lambda lang: lang == "mr", NO_DECLARATION, False)
        assert not reverts and not undeclared
        assert [k for k, _, _ in allowed] == [("mr", "wikipron")]

    def test_unchanged_rows_are_not_reported(self):
        same = board(row(), row("xh", "kaikki"))
        assert guard.classify(same, same, same, NOTHING_OWNED, NO_DECLARATION, False) \
            == ([], [], [])

    def test_new_row_is_owned(self):
        """A row on neither the target nor the merge base displaces nothing."""
        _, undeclared, allowed = guard.classify(
            {}, {}, board(row("tpw")), NOTHING_OWNED, NO_DECLARATION, False)
        assert not undeclared and len(allowed) == 1

    def test_move_without_ownership_or_declaration_fails(self):
        _, undeclared, allowed = guard.classify(
            board(row(per=0.4)), board(row(per=0.4)), board(row(per=0.2)),
            NOTHING_OWNED, NO_DECLARATION, False)
        assert [k for k, _, _ in undeclared] == [("mr", "wikipron")]
        assert not allowed

    def test_row_deleted_by_the_branch_needs_ownership(self):
        _, undeclared, _ = guard.classify(
            board(row()), board(row()), {}, NOTHING_OWNED, NO_DECLARATION, False)
        assert [k for k, _, _ in undeclared] == [("mr", "wikipron")]


class TestWideHarnessMovement:
    """A harness change SHOULD move every row — but only when declared."""

    def wide(self):
        mb = board(row("mr", per=0.4), row("xh", "kaikki", per=0.3), row("zu", per=0.2))
        head = board(row("mr", per=0.41), row("xh", "kaikki", per=0.31),
                     row("zu", per=0.21))
        return mb, mb, head

    def test_undeclared_wide_movement_fails_even_with_engine_touched(self):
        """Touching a harness file is not itself a licence — otherwise the
        guard is bypassed by editing one line of the engine."""
        mb, base, head = self.wide()
        _, undeclared, allowed = guard.classify(
            mb, base, head, NOTHING_OWNED, NO_DECLARATION, True)
        assert len(undeclared) == 3 and not allowed

    def test_declared_wide_movement_passes(self):
        mb, base, head = self.wide()
        declared = (set(), True, "stress placement reworked")
        reverts, undeclared, allowed = guard.classify(
            mb, base, head, NOTHING_OWNED, declared, True)
        assert not reverts and not undeclared and len(allowed) == 3

    def test_all_without_an_engine_change_is_not_a_licence(self):
        mb, base, head = self.wide()
        declared = (set(), True, "trust me")
        _, undeclared, _ = guard.classify(
            mb, base, head, NOTHING_OWNED, declared, False)
        assert len(undeclared) == 3

    def test_declared_wide_movement_still_catches_a_stale_row(self):
        """The honest wide-movement PR that is ALSO stale: it rescored two
        rows and carries the merge-base value for a third the target moved."""
        mb = board(row("mr", per=0.4), row("xh", "kaikki", per=0.3), row("zu", per=0.2))
        base = board(row("mr", per=0.4), row("xh", "kaikki", per=0.3),
                     row("zu", per=0.05))
        head = board(row("mr", per=0.41), row("xh", "kaikki", per=0.31),
                     row("zu", per=0.2))
        declared = (set(), True, "stress placement reworked")
        reverts, undeclared, allowed = guard.classify(
            mb, base, head, NOTHING_OWNED, declared, True)
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
            board(row(per=0.4)), board(row(per=0.4)), board(row(per=0.2)),
            NOTHING_OWNED, declared, True)
        assert [k for k, _, _ in undeclared] == [("mr", "wikipron")]


class TestMarkdownBoard:
    def test_table_rows_are_keyed_and_the_header_skipped(self):
        rows = guard._read_markdown(
            "# Scoreboard\n\n| Lang | Dataset | N | PER |\n|---|---|---:|---:|\n"
            "| mr | wikipron | 4267 | 0.0535 |\n")
        assert list(rows) == [("mr", "wikipron")]
        assert guard._per(rows[("mr", "wikipron")]) == "per=0.0535 n=4267"


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

    Regenerating the board on both sides always conflicts textually, which
    is the moment where the wrong resolution creates the defect.
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
    def test_stale_branch_reverting_dev_fails(self, repo, capsys):
        """The real incident: the branch rescores xh, regenerates the whole
        board from its pre-merge base, and so carries mr's old value."""
        write_board(repo, [row("mr", per=0.4351), row("xh", "kaikki", per=0.25)])
        write_spec(repo, "xh", "nasals")
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "fix(xh): nasals")

        assert guard.check("dev", "HEAD", repo=repo) == 1
        out = capsys.readouterr().out
        assert "would REVERT" in out
        assert "mr (wikipron): dev has per=0.0535" in out
        assert "the branch carries per=0.4351" in out
        assert "merge dev into the branch" in out

    def test_branch_that_merged_dev_first_passes(self, repo):
        """The fix the failure message asks for: keep dev's mr row."""
        write_board(repo, [row("mr", per=0.4351), row("xh", "kaikki", per=0.25)])
        write_spec(repo, "xh", "nasals")
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "fix(xh): nasals")
        merge_dev(repo, [row("mr", per=0.0535), row("xh", "kaikki", per=0.25)])

        assert guard.check("dev", "HEAD", repo=repo) == 0

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
        write_board(repo, [row("mr", per=0.4351), row("xh", "kaikki", per=0.25)])
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "chore: rescore xh")
        merge_dev(repo, [row("mr", per=0.0535), row("xh", "kaikki", per=0.25)])

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
