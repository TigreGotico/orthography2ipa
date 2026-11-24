"""scripts/check_ir_version_doc.py ties IR version bumps to the spec."""
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
FILES = ["scripts/check_ir_version_doc.py", "docs/ir/o2i-ir-v1.md", "orthography2ipa/ir/layout.py",
         "orthography2ipa/ir/interpreter.py", "orthography2ipa/ir/compiler.py"]


def git(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@t", *args],
                   check=True, capture_output=True)


@pytest.fixture()
def repo(tmp_path: Path) -> Path:
    for name in FILES:
        (tmp_path / name).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(REPO / name, tmp_path / name)
    git(tmp_path, "init", "-q", "-b", "dev")
    git(tmp_path, "add", ".")
    git(tmp_path, "commit", "-qm", "base")
    git(tmp_path, "checkout", "-qb", "feature")
    return tmp_path


def edit(repo: Path, name: str, old: str, new: str) -> None:
    path = repo / name
    src = path.read_text(encoding="utf-8")
    assert old in src
    path.write_text(src.replace(old, new, 1), encoding="utf-8")
    git(repo, "commit", "-qam", "change")


def run(repo: Path) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-I", str(repo / FILES[0]), "--base", "dev"],
                          capture_output=True, text=True)


def test_no_change_passes(repo):
    edit(repo, "orthography2ipa/ir/interpreter.py", "from __future__", "# a comment\nfrom __future__")
    result = run(repo)
    assert result.returncode == 0, result.stdout
    assert "0 changed" in result.stdout


@pytest.mark.parametrize("name, old, new, key", [
    ("orthography2ipa/ir/layout.py", '"beam": 1,', '"beam": 2,', "layout.SEMANTICS"),
    ("orthography2ipa/ir/interpreter.py", "SUPPORTED_IR_VERSIONS = (1,)",
     "SUPPORTED_IR_VERSIONS = (1, 2)", "interpreter.py SUPPORTED_IR_VERSIONS"),
    ("orthography2ipa/ir/compiler.py", '"ir_version": 1,', '"ir_version": 2,', "compiler ir_version"),
    ("orthography2ipa/ir/layout.py", "SSET = ", "IR_VERSION = 2\nSSET = ", "layout.IR_VERSION"),
])
def test_version_change_needs_the_spec(repo, name, old, new, key):
    edit(repo, name, old, new)
    result = run(repo)
    assert result.returncode == 1, result.stdout
    assert key in result.stdout
    spec = repo / "docs/ir/o2i-ir-v1.md"
    spec.write_text(spec.read_text(encoding="utf-8") + "\nThe new version.\n", encoding="utf-8")
    git(repo, "commit", "-qam", "spec")
    result = run(repo)
    assert result.returncode == 0, result.stdout
    assert "1 changed" in result.stdout
