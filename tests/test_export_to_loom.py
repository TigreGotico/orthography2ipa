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
from tests.lua_host import field, phonemize


@pytest.fixture(scope="module")
def exported(tmp_path_factory):
    out = tmp_path_factory.mktemp("loom") / "kab.gguf"
    export_to_loom(["kab", "pt-PT"], out)
    return GGUFReader(str(out))


def test_only_the_requested_languages_are_carried(exported):
    data = sorted(k for k in exported.fields if k.startswith("loom.phonemizer.data."))
    assert data == ["loom.phonemizer.data.kab", "loom.phonemizer.data.pt-PT"]
    assert field(exported, "loom.text.languages") == ["kab", "pt-PT"]
    assert field(exported, "loom.phonemizer.kind") == "lua"


def test_the_file_has_no_o2i_keys(exported):
    assert [k for k in exported.fields if k.startswith("o2i.")] == []
    assert "model.driver_script" not in exported.fields


def test_each_language_carries_its_ir(exported):
    for code in ("kab", "pt-PT"):
        doc = json.loads(field(exported, f"loom.phonemizer.data.{code}"))
        assert doc == json.loads(json.dumps(layout.encode(build_ir(code)), ensure_ascii=False))


def test_ruleset_names_each_spec_revision(exported):
    revs = [layout.spec_revision(build_ir(code)) for code in ("kab", "pt-PT")]
    ruleset = field(exported, "loom.phonemizer.ruleset")
    assert ruleset.endswith(f"; kab={revs[0]}; pt-PT={revs[1]}")


def test_the_script_matches_the_reference(exported, tmp_path):
    ipa, unmapped = phonemize(exported, "os jogos", 1, tmp_path)
    assert ipa == "u ˈʒɔɡuʃ"
    assert ipa == Interpreter(json.loads(json.dumps(layout.encode(build_ir("pt-PT"))))).transcribe("os jogos")
    assert unmapped == ""


def test_the_script_reports_what_it_drops(exported, tmp_path):
    # The kab spec maps no digit and no ⟨ε⟩; Python warns for each, and the script returns them.
    text = "Azul 2024! ε"
    ipa, unmapped = phonemize(exported, text, 0, tmp_path)
    reference = Interpreter(json.loads(json.dumps(layout.encode(build_ir("kab")))))
    assert ipa == reference.transcribe(text)
    assert unmapped == "2024ε" == "".join(reference.unmapped(text))


def test_set_lexicon_overrides_the_rules(exported, tmp_path):
    before = "set_lexicon(1, {{{%s}, {%s}}})" % (", ".join(str(ord(c)) for c in "jogos"),
                                               ", ".join(str(ord(c)) for c in "ʒOʒO"))
    ipa, _ = phonemize(exported, "os jogos", 1, tmp_path, before)
    assert "ʒOʒO" in ipa
    reference = Interpreter(json.loads(json.dumps(layout.encode(build_ir("pt-PT")))))
    assert ipa == reference.transcribe("os jogos", lexicon={"jogos": "ʒOʒO"})


def test_the_script_leaves_only_its_entry_points(exported, tmp_path):
    (tmp_path / "script.lua").write_text(field(exported, "loom.phonemizer.script"), encoding="utf-8")
    probe = ("local before = {}; for k in pairs(_G) do before[k] = true end; dofile(%r); "
             "local new = {}; for k in pairs(_G) do if not before[k] then new[#new + 1] = k end end; "
             "table.sort(new); io.write(table.concat(new, ' '))") % str(tmp_path / "script.lua")
    proc = subprocess.run(["luajit", "-e", probe], capture_output=True, text=True, check=True)
    assert proc.stdout == "phonemize set_lexicon"


def test_the_script_uses_no_io_or_os(exported):
    script = field(exported, "loom.phonemizer.script")
    assert not re.search(r"\b(io|os)\.", script)


IDENTITY_KEYS = {"backend", "distribution", "version", "lang", "revision", "frontend"}


def test_export_to_loom_returns_the_metadata_it_writes(tmp_path):
    from orthography2ipa.version import VERSION_STR
    out = tmp_path / "kab.gguf"
    meta = export_to_loom(["kab"], out)
    reader = GGUFReader(str(out))
    rev = layout.spec_revision(build_ir("kab"))
    assert meta["ruleset"] == field(reader, "loom.phonemizer.ruleset")
    assert meta["spec_revisions"] == {"kab": rev}
    assert meta["o2i_version"] == VERSION_STR
    identity = meta["phonemizer_identity"]["kab"]
    assert set(identity) == IDENTITY_KEYS
    assert identity == {"backend": "orthography2ipa", "distribution": "orthography2ipa",
                        "version": VERSION_STR, "lang": "kab", "revision": rev, "frontend": None}
    assert json.loads(field(reader, "loom.phonemizer.identity")) == meta["phonemizer_identity"]


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


def test_phoneme_set_of_each_language_is_in_the_metadata(exported):
    from orthography2ipa import phoneme_set
    for code in ("kab", "pt-PT"):
        got = field(exported, f"loom.phonemizer.phonemes.{code}")
        assert got == sorted(phoneme_set(code))
    assert "ʎ" in field(exported, "loom.phonemizer.phonemes.pt-PT")
