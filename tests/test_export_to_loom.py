"""The loom export: one compiled IR per requested language, run by interpreter.lua."""
import json
import re
import subprocess

import pytest
from gguf import GGUFReader

from orthography2ipa.export_to_loom import export_to_loom
from orthography2ipa.ir import layout
from orthography2ipa.ir.compiler import build_ir
from orthography2ipa.ir.interpreter import Interpreter


def _field(reader: GGUFReader, key: str):
    return reader.fields[key].contents()


@pytest.fixture(scope="module")
def exported(tmp_path_factory):
    out = tmp_path_factory.mktemp("loom") / "kab.gguf"
    export_to_loom(["kab", "pt-PT"], out)
    return GGUFReader(str(out))


def test_only_the_requested_languages_are_carried(exported):
    driver = _field(exported, "model.driver_script")
    irs = driver.split("O2I_IRS = {", 1)[1]
    carried = re.findall(r'^  \["([^"]+)"\] = \[=*\[', irs, flags=re.M)
    assert carried == ["kab", "pt-PT"]
    assert _field(exported, "loom.text.languages") == ["kab", "pt-PT"]


def test_ruleset_names_each_spec_revision(exported):
    revs = [layout.spec_revision(build_ir(code)) for code in ("kab", "pt-PT")]
    assert _field(exported, "o2i.spec_revisions") == revs
    ruleset = _field(exported, "loom.phonemizer.ruleset")
    assert ruleset.endswith(f"; kab={revs[0]}; pt-PT={revs[1]}")


def test_driver_runs_and_matches_the_reference(exported, tmp_path):
    driver = tmp_path / "driver.lua"
    text = "os jogos"
    driver.write_text(_field(exported, "model.driver_script"), encoding="utf-8")
    call = "dofile(%r); io.write(table.concat(infer{text = {%s}, lang = 1}, ' '))" % (
        str(driver), ", ".join(str(ord(c)) for c in text))
    proc = subprocess.run(["luajit", "-e", call], capture_output=True, text=True, check=True)
    got = "".join(chr(int(x)) for x in proc.stdout.split())
    assert got == "u ˈʒɔɡuʃ"
    assert got == Interpreter(json.loads(json.dumps(layout.encode(build_ir("pt-PT"))))).transcribe(text)


IDENTITY_KEYS = {"backend", "distribution", "version", "lang", "revision", "frontend"}


def test_export_to_loom_returns_the_metadata_it_writes(tmp_path):
    from orthography2ipa.version import VERSION_STR
    out = tmp_path / "kab.gguf"
    meta = export_to_loom(["kab"], out)
    reader = GGUFReader(str(out))
    rev = layout.spec_revision(build_ir("kab"))
    assert meta["ruleset"] == _field(reader, "loom.phonemizer.ruleset")
    assert meta["spec_revisions"] == {"kab": rev}
    assert meta["o2i_version"] == VERSION_STR == _field(reader, "o2i.version")
    identity = meta["phonemizer_identity"]["kab"]
    assert set(identity) == IDENTITY_KEYS
    assert identity == {"backend": "orthography2ipa", "distribution": "orthography2ipa",
                        "version": VERSION_STR, "lang": "kab", "revision": rev, "frontend": None}
    assert json.loads(_field(reader, "o2i.phonemizer_identity")) == meta["phonemizer_identity"]


def test_expected_revision_mismatch_is_refused(tmp_path):
    out = tmp_path / "kab.gguf"
    with pytest.raises(ValueError, match=r"kab.*sha256:0+.*sha256:[0-9a-f]{64}"):
        export_to_loom(["kab"], out, expect_revisions={"kab": "sha256:" + "0" * 64})
    assert not out.exists()


def test_expected_revision_match_exports(tmp_path):
    rev = layout.spec_revision(build_ir("kab"))
    meta = export_to_loom(["kab"], tmp_path / "kab.gguf", expect_revisions={"kab": rev})
    assert meta["spec_revisions"] == {"kab": rev}


def test_expected_revision_for_a_language_not_exported_is_refused(tmp_path):
    with pytest.raises(ValueError, match="pt-PT"):
        export_to_loom(["kab"], tmp_path / "kab.gguf", expect_revisions={"pt-PT": "sha256:x"})


def test_data_ref_without_a_checkout_is_refused(tmp_path, monkeypatch):
    from orthography2ipa import export_to_loom as module
    from orthography2ipa.ir import compiler
    monkeypatch.setattr(compiler, "_checkout", lambda: None)
    with pytest.raises(RuntimeError, match="git checkout"):
        module.export_to_loom(["kab"], tmp_path / "kab.gguf", data_ref="7.30.0")


def test_wheel_mode_exports_the_installed_data(tmp_path, monkeypatch):
    from orthography2ipa import export_to_loom as module
    from orthography2ipa.ir import compiler
    checkout_rev = layout.spec_revision(build_ir("kab"))
    monkeypatch.setattr(compiler, "_checkout", lambda: None)
    meta = module.export_to_loom(["kab"], tmp_path / "kab.gguf")
    assert meta["spec_revisions"]["kab"] == checkout_rev
