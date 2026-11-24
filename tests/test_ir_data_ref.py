"""Compiling older spec data: aliases, the checkout guard and the git reads."""
import subprocess
from pathlib import Path

import pytest

from orthography2ipa import json_loader
from orthography2ipa.ir import compiler, layout
from orthography2ipa.ir.compiler import build_ir


def test_an_alias_resolves_at_a_data_ref():
    assert layout.spec_revision(build_ir("pt", "HEAD")) == layout.spec_revision(build_ir("pt-PT", "HEAD"))


def test_a_data_ref_reads_the_spec_files_with_one_git_process(monkeypatch):
    compiler._DATA_AT.clear()
    calls = []
    real_run = subprocess.run

    def run(args, *a, **k):
        calls.append(args)
        return real_run(args, *a, **k)

    monkeypatch.setattr(compiler.subprocess, "run", run)
    build_ir("kab", "HEAD")
    build_ir("kab", "HEAD")
    reads = [c for c in calls if "archive" in c or "show" in c or "cat-file" in c]
    assert len(reads) == 1


def test_an_unrelated_git_repository_is_not_a_checkout(tmp_path, monkeypatch):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    subprocess.run(["git", "-C", str(tmp_path), "-c", "user.name=t", "-c", "user.email=t@t",
                    "commit", "-q", "--allow-empty", "-m", "outer"], check=True)
    package = tmp_path / ".venv" / "site-packages" / "orthography2ipa"
    package.mkdir(parents=True)
    monkeypatch.setattr(json_loader, "__file__", str(package / "json_loader.py"))
    assert compiler._checkout() is None
    assert compiler._git_head() == ""
    from orthography2ipa.export_to_loom import export_to_loom
    with pytest.raises(RuntimeError, match="git checkout"):
        export_to_loom(["kab"], tmp_path / "kab.gguf", data_ref="HEAD")


def test_this_package_is_its_own_checkout():
    assert compiler._checkout() == Path(json_loader.__file__).resolve().parent.parent


def test_a_moved_ref_reads_the_new_commit(tmp_path, monkeypatch):
    data = tmp_path / "orthography2ipa" / "data"
    data.mkdir(parents=True)
    git = ["git", "-C", str(tmp_path), "-c", "user.name=t", "-c", "user.email=t@t"]
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    for content in ("old", "new"):
        (data / "xx.json").write_text(content, encoding="utf-8")
        subprocess.run(git + ["add", "-A"], check=True)
        subprocess.run(git + ["commit", "-q", "-m", content], check=True)
        subprocess.run(git + ["tag", "-f", "ref", "HEAD"], check=True, capture_output=True)
        monkeypatch.setattr(compiler, "_checkout", lambda: tmp_path)
        assert compiler._data_files("ref")["xx"].read_text(encoding="utf-8") == content
