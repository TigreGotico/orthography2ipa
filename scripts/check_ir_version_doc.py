"""Refuse an IR version or semantics change that leaves the spec unchanged.

A new IR mechanism is an IR version bump or a semantics version bump, and
docs/ir/o2i-ir-v1.md defines each one. This check reads the versions at the
base ref and at HEAD and compares their values:

- ``IR_VERSION`` and ``SEMANTICS`` in orthography2ipa/ir/layout.py,
- ``SUPPORTED_IR_VERSIONS`` in orthography2ipa/ir/interpreter.py and in
  orthography2ipa/ir/interpreter.lua,
- the ``"ir_version"`` value that orthography2ipa/ir/compiler.py writes.

When one of them differs and ``git diff BASE...HEAD`` does not touch the
spec, the check fails.

    python -I scripts/check_ir_version_doc.py --base origin/dev
"""
import argparse
import ast
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, Optional

REPO = Path(__file__).resolve().parent.parent
SPEC = "docs/ir/o2i-ir-v1.md"


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(REPO), *args], check=True, capture_output=True,
                          text=True).stdout


def read(ref: Optional[str], path: str) -> Optional[str]:
    if ref is None:
        file = REPO / path
        return file.read_text(encoding="utf-8") if file.exists() else None
    try:
        return git("show", f"{ref}:{path}")
    except subprocess.CalledProcessError:
        return None


def python_assignments(src: Optional[str], names: set) -> Dict[str, object]:
    found: Dict[str, object] = {}
    if src is None:
        return found
    for node in ast.parse(src).body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in names:
                    found[target.id] = ast.literal_eval(node.value)
    return found


def versions(ref: Optional[str]) -> Dict[str, object]:
    """Every version value at *ref* (None means the working tree)."""
    out: Dict[str, object] = {}
    for name, value in python_assignments(read(ref, "orthography2ipa/ir/layout.py"),
                                          {"IR_VERSION", "SEMANTICS"}).items():
        out[f"layout.{name}"] = value
    for name, value in python_assignments(read(ref, "orthography2ipa/ir/interpreter.py"),
                                          {"SUPPORTED_IR_VERSIONS"}).items():
        out[f"interpreter.py {name}"] = value
    compiler = read(ref, "orthography2ipa/ir/compiler.py")
    if compiler is not None:
        out["compiler ir_version"] = sorted(set(re.findall(r'"ir_version":\s*(\d+)', compiler)))
    lua = read(ref, "orthography2ipa/ir/interpreter.lua")
    if lua is not None:
        match = re.search(r"SUPPORTED_IR_VERSIONS\s*=\s*(\{[^}]*\})", lua)
        out["interpreter.lua SUPPORTED_IR_VERSIONS"] = match and re.sub(r"\s+", "", match.group(1))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--base", required=True, help="the base branch ref, such as origin/dev")
    args = ap.parse_args()
    merge_base = git("merge-base", args.base, "HEAD").strip()
    before, after = versions(merge_base), versions(None)
    changed = sorted(k for k in before.keys() | after.keys() if before.get(k) != after.get(k))
    spec_changed = SPEC in git("diff", "--name-only", merge_base).split()
    print(f"base {merge_base[:12]}: {len(before)} version values before, {len(after)} after, "
          f"{len(changed)} changed; {SPEC} changed: {spec_changed}")
    for key in changed:
        old, new = before.get(key), after.get(key)
        if isinstance(old, dict) and isinstance(new, dict):
            for name in sorted(old.keys() | new.keys()):
                if old.get(name) != new.get(name):
                    print(f"  {key}[{name!r}]: {old.get(name)!r} -> {new.get(name)!r}")
        else:
            print(f"  {key}: {old!r} -> {new!r}")
    if changed and not spec_changed:
        print(f"error: an IR version or semantics version changed, and {SPEC} did not. "
              "Define the change in the spec in the same pull request.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
