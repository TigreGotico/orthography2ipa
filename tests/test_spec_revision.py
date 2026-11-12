"""spec_revision and lexicon_revision: equal for equal inputs, different otherwise.

No test pins a hash the code produced. A test compares two revisions, or
recomputes a lexicon revision with hashlib over the same bytes. The parent
chain comes from ``ancestry_chain``, which walks ``parent`` on its own.
"""
from __future__ import annotations

import ast
import hashlib
import json
import os
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

from orthography2ipa import (
    ancestry_chain,
    lexicon_revision,
    packaged_lexicon,
    resolve,
    spec_revision,
)
from orthography2ipa import json_loader, revision
from orthography2ipa import lexicon as lexmod

GROUP = "orthography2ipa.lexicons"
PATCH_GROUP = "orthography2ipa.lexicon_patches"

# Modules that ``import orthography2ipa`` loads but that are not on the
# transcription path. The runtime guard needs this list, because the package
# imports these for tools. Each entry says why it stays out of
# revision.ENGINE_MODULES.
NOT_ENGINE = {
    "distance": "distance metrics between languages; the package imports it, "
                "transcription never calls it",
    "script_distance": "distance between writing systems; not called by transcription",
    "underspecification": "reports where a reading is underdetermined; changes no output",
    "revision": "computes the revisions themselves",
    "version": "the release number; an alpha bumps it with no engine change",
}

# The only module outside revision.ENGINE_MODULES that an engine module may
# import. lexicon.py and registry.py read VERSION_MAJOR only to write a removal
# version into a deprecation message, and an alpha bumps it every day.
ENGINE_MAY_IMPORT = {"version"}

# One spec per script family that reaches different engine code.
TRANSCRIPTIONS = [
    ("pt-PT", "o gato comeu a sopa"),   # Latin, stress, sandhi, allophone rules
    ("en-US", "the cat ate the soup"),  # Latin, graphemes_base edge
    ("ar", "كتب الولد"),                 # abjad, positional graphemes
    ("zh", "ni3 hao3"),                 # tone marks
    ("fr-FR", "les amis"),              # sandhi rules
    ("hi", "नमस्ते"),                    # abugida
    ("th", "สวัสดี"),                    # tone rules, preposed vowels
]


@pytest.fixture(autouse=True)
def fresh_caches():
    """Each test reads the spec files and module sources it sets up."""
    def clear():
        revision._canonical_spec.cache_clear()
        revision._spec_revision.cache_clear()
        revision.engine_fingerprint.cache_clear()
    clear()
    yield
    clear()


def edit_spec(monkeypatch, tmp_path, code, edit):
    """Point the loader index for *code* at a copy changed by *edit*."""
    raw = json.loads(json_loader._index[code].read_text(encoding="utf-8"))
    edit(raw)
    copy = tmp_path / f"{code}.json"
    copy.write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8")
    monkeypatch.setitem(json_loader._index, code, copy)
    revision._canonical_spec.cache_clear()
    revision._spec_revision.cache_clear()


def add_grapheme(raw):
    raw.setdefault("graphemes", {})["ʘʘ"] = ["ʘ"]


# ── spec_revision: stable ─────────────────────────────────────────────────

def test_format():
    rev = spec_revision("pt-PT")
    assert rev.startswith("sha256:")
    assert len(rev) == len("sha256:") + 64
    int(rev[len("sha256:"):], 16)


def test_equal_across_calls():
    first = spec_revision("pt-PT")
    revision._spec_revision.cache_clear()
    revision._canonical_spec.cache_clear()
    assert spec_revision("pt-PT") == first


def test_equal_in_a_fresh_process():
    script = "import orthography2ipa as o; print(o.spec_revision('pt-PT'))"
    out = subprocess.run([sys.executable, "-c", script], capture_output=True,
                         text=True, check=True,
                         env={**os.environ, "PYTHONHASHSEED": "random"})
    assert out.stdout.strip() == spec_revision("pt-PT")


@pytest.mark.parametrize("alias, canonical", [("pt", "pt-PT"), ("por", "pt-PT"),
                                              ("eng", "en-GB")])
def test_alias_gives_the_canonical_revision(alias, canonical):
    assert resolve(alias) == canonical
    assert spec_revision(alias) == spec_revision(canonical)


def test_unknown_code_raises_key_error():
    with pytest.raises(KeyError):
        spec_revision("qqq-x-nothing-here")


def test_child_and_parent_differ():
    parent = ancestry_chain("pt-BR")[0]
    assert spec_revision("pt-BR") != spec_revision(parent)


def test_every_registered_code_has_its_own_revision(all_codes):
    revisions = {spec_revision(code) for code in all_codes}
    assert len(revisions) == len(all_codes)


# ── spec_revision: what changes it ────────────────────────────────────────

def test_changes_with_its_own_spec(monkeypatch, tmp_path):
    before = spec_revision("pt-BR")
    edit_spec(monkeypatch, tmp_path, "pt-BR", add_grapheme)
    assert spec_revision("pt-BR") != before


def test_changes_with_every_spec_on_its_parent_chain(monkeypatch, tmp_path):
    chain = ancestry_chain("en-US")
    assert len(chain) > 3
    before = spec_revision("en-US")
    for parent in chain:
        with monkeypatch.context() as m:
            edit_spec(m, tmp_path, parent, lambda raw: raw.update(notes="edited"))
            assert spec_revision("en-US") != before, parent
        revision._canonical_spec.cache_clear()
        revision._spec_revision.cache_clear()
    assert spec_revision("en-US") == before


def test_changes_with_a_graphemes_base_off_the_parent_chain(monkeypatch, tmp_path):
    raw = json.loads(json_loader._index["aae"].read_text(encoding="utf-8"))
    base = raw["graphemes_base"]
    assert base not in ancestry_chain("aae")
    before = spec_revision("aae")
    edit_spec(monkeypatch, tmp_path, base, add_grapheme)
    assert spec_revision("aae") != before


def test_unchanged_by_an_unrelated_spec(monkeypatch, tmp_path):
    assert "fi" not in ["en-US", *ancestry_chain("en-US")]
    before = spec_revision("en-US")
    edit_spec(monkeypatch, tmp_path, "fi", add_grapheme)
    assert spec_revision("fi") != spec_revision("en-US")
    assert spec_revision("en-US") == before


def test_unchanged_by_reformatting(monkeypatch, tmp_path):
    before = spec_revision("pt-BR")
    reformatted = tmp_path / "pt-BR.json"
    raw = json.loads(json_loader._index["pt-BR"].read_text(encoding="utf-8"))
    reordered = dict(reversed(list(raw.items())))
    reformatted.write_text(json.dumps(reordered, ensure_ascii=True, indent=7) + "\n\n",
                           encoding="utf-8")
    assert reformatted.read_bytes() != json_loader._index["pt-BR"].read_bytes()
    monkeypatch.setitem(json_loader._index, "pt-BR", reformatted)
    revision._canonical_spec.cache_clear()
    revision._spec_revision.cache_clear()
    assert spec_revision("pt-BR") == before


def test_changes_with_the_engine_source(monkeypatch):
    before = spec_revision("pt-PT")
    real = revision._module_source

    def edited(name):
        source = real(name)
        return source.replace(b"def ", b"def x_", 1) if name == "g2p" else source

    monkeypatch.setattr(revision, "_module_source", edited)
    revision._spec_revision.cache_clear()
    revision.engine_fingerprint.cache_clear()
    assert spec_revision("pt-PT") != before


def test_changes_with_the_spec_format_version(monkeypatch):
    before = spec_revision("pt-PT")
    monkeypatch.setattr(revision, "SPEC_FORMAT_VERSION", revision.SPEC_FORMAT_VERSION + 1)
    revision._spec_revision.cache_clear()
    assert spec_revision("pt-PT") != before


# ── engine fingerprint ────────────────────────────────────────────────────

def fingerprint(source: str) -> str:
    return revision._fingerprint([("orthography2ipa/m.py", source.encode())])


def test_comments_leave_the_fingerprint_equal():
    real = revision._module_source("g2p").decode()
    commented = "# a comment\n" + real.replace("\ndef ", "\n# another comment\ndef ")
    assert commented != real
    assert fingerprint(commented) == fingerprint(real)
    assert (fingerprint("def f(a, b):\n    return a + b\n")
            == fingerprint("def f(a, b):  # adds\n    return a + b  # sum\n"))


def test_reformatting_leaves_the_fingerprint_equal():
    compact = "def f(a,b):\n  return a+b\n"
    spread = "\n\ndef f(a, b):\n\n\n        return a + b\n\n"
    assert fingerprint(compact) == fingerprint(spread)
    real = revision._module_source("stress").decode()
    spaced = "\n\n" + real.replace("\ndef ", "\n\n\n\ndef ")
    assert spaced != real
    assert fingerprint(spaced) == fingerprint(real)


def test_a_token_edit_changes_the_fingerprint():
    assert fingerprint("def f(a, b):\n    return a + b\n") != fingerprint(
        "def f(a, b):\n    return a - b\n")
    real = revision._module_source("g2p").decode()
    assert fingerprint(real.replace("def ", "def x_", 1)) != fingerprint(real)


def test_docstrings_count():
    assert fingerprint('def f():\n    """One."""\n') != fingerprint(
        'def f():\n    """Two."""\n')


def test_an_fstring_is_one_string_token():
    """Python 3.12 splits an f-string into parts. The fingerprint does not."""
    source = 'x = f"a{b!r}{f\'{c}\'}d"\ny = 1\n'
    assert list(revision._source_tokens(source.encode())) == [
        ("NAME", "x"), ("OP", "="), ("STRING", 'f"a{b!r}{f\'{c}\'}d"'), ("NEWLINE", ""),
        ("NAME", "y"), ("OP", "="), ("NUMBER", "1"), ("NEWLINE", ""),
    ]


def test_a_multiline_fstring_is_one_string_token():
    source = 'x = f"""a\n{b}\nc"""\n'
    assert list(revision._source_tokens(source.encode())) == [
        ("NAME", "x"), ("OP", "="), ("STRING", 'f"""a\n{b}\nc"""'), ("NEWLINE", ""),
    ]


def test_the_engine_fingerprint_reads_the_package_source(monkeypatch):
    before = revision.engine_fingerprint()
    real = revision._module_source
    monkeypatch.setattr(revision, "_module_source",
                        lambda name: real(name) + (b"\nZ = 1\n" if name == "weights" else b""))
    revision.engine_fingerprint.cache_clear()
    assert revision.engine_fingerprint() != before


def test_engine_modules_name_real_files():
    package = Path(revision.__file__).parent
    assert len(set(revision.ENGINE_MODULES)) == len(revision.ENGINE_MODULES)
    for name in revision.ENGINE_MODULES:
        assert (package / f"{name}.py").is_file(), name
    assert not set(revision.ENGINE_MODULES) & set(NOT_ENGINE)


def test_every_module_a_transcription_loads_is_listed():
    script = textwrap.dedent(f"""
        import json, sys, warnings
        warnings.simplefilter("ignore")
        from orthography2ipa import G2P
        for code, text in {TRANSCRIPTIONS!r}:
            assert G2P(code).transcribe(text), code
        print(json.dumps(sorted(m.split(".", 1)[1] for m in sys.modules
                                if m.startswith("orthography2ipa."))))
    """)
    out = subprocess.run([sys.executable, "-c", script], capture_output=True,
                         text=True, check=True)
    loaded = set(json.loads(out.stdout))
    assert "g2p" in loaded and "phonetok" in loaded
    unlisted = loaded - set(revision.ENGINE_MODULES) - set(NOT_ENGINE)
    assert not unlisted, f"add to revision.ENGINE_MODULES or NOT_ENGINE: {sorted(unlisted)}"


def test_block_structure_changes_the_fingerprint():
    """A line moved in or out of a block changes behaviour, so it changes the fingerprint."""
    inside = "def f(xs):\n    out = []\n    for x in xs:\n        out.append(x)\n        return out\n"
    after = "def f(xs):\n    out = []\n    for x in xs:\n        out.append(x)\n    return out\n"
    assert fingerprint(inside) != fingerprint(after)
    assert fingerprint("x = 1\n-1\n") != fingerprint("x = 1 -1\n")


def test_a_dedent_in_an_engine_module_changes_the_fingerprint():
    real = revision._module_source("stress").decode()
    # stress.py, the for-else of the nucleus count: moving ``i += 1`` out of
    # the else block changes the Italian reading of "ciao".
    tail = "\n        # a combining mark, or the length mark"
    block = "            nuclei.append(run[i])\n            i += 1" + tail
    assert real.count(block) == 1
    dedented = real.replace(block, "            nuclei.append(run[i])\n        i += 1" + tail)
    assert fingerprint(dedented) != fingerprint(real)


def test_reindenting_leaves_the_fingerprint_equal():
    four = "def f(x):\n    if x:\n        return 1\n    return 2\n"
    two = "def f(x):\n  if x:\n    return 1\n  return 2\n"
    assert fingerprint(four) == fingerprint(two)


def test_a_missing_source_file_raises_engine_source_unavailable(monkeypatch, tmp_path):
    from orthography2ipa.exceptions import EngineSourceUnavailable

    monkeypatch.setattr(revision, "files", lambda package: tmp_path)
    with pytest.raises(EngineSourceUnavailable):
        revision.engine_fingerprint()
    revision._spec_revision.cache_clear()
    with pytest.raises(EngineSourceUnavailable):
        spec_revision("pt-PT")


def static_imports(source: str) -> set:
    """The ``orthography2ipa`` modules that *source* imports, in any scope."""
    found = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.ImportFrom):
            if node.level:
                found.add((node.module or "").split(".")[0] or "__init__")
            elif node.module and node.module.startswith("orthography2ipa."):
                found.add(node.module.split(".")[1])
            elif node.module == "orthography2ipa":
                package = Path(revision.__file__).parent
                found |= {a.name for a in node.names if (package / f"{a.name}.py").is_file()}
                found.add("__init__")
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.startswith("orthography2ipa."):
                    found.add(alias.name.split(".")[1])
                elif alias.name == "orthography2ipa":
                    found.add("__init__")
    return found


def import_closure(read) -> set:
    """Every module that the engine modules import, followed to the end.

    The walk also reads the modules in ENGINE_MAY_IMPORT, so a module that one of
    them imports is in the closure.
    """
    walked = set(revision.ENGINE_MODULES) | ENGINE_MAY_IMPORT
    seen, stack = set(), list(revision.ENGINE_MODULES)
    while stack:
        name = stack.pop()
        if name in seen:
            continue
        seen.add(name)
        if name in walked:
            stack.extend(static_imports(read(name)))
    return seen


def unlisted_engine_imports(read) -> set:
    """The modules that the engine reaches and the fingerprint does not hash.

    NOT_ENGINE does not count here. A module that the package imports for tools
    is on the transcription path as soon as an engine module imports it.
    """
    return import_closure(read) - set(revision.ENGINE_MODULES) - ENGINE_MAY_IMPORT


def test_every_module_the_engine_imports_is_listed():
    """A static walk reaches imports that no test sentence runs, such as one behind a spec flag."""
    unlisted = unlisted_engine_imports(lambda name: revision._module_source(name).decode())
    assert not unlisted, f"add to revision.ENGINE_MODULES: {sorted(unlisted)}"


def test_an_engine_import_of_a_tool_module_is_unlisted():
    """``distance`` is in NOT_ENGINE, and an engine import of it still fails the guard."""
    real = revision._module_source("g2p").decode()
    anchor = "\nclass G2P:"
    assert real.count(anchor) == 1
    planted = real.replace(anchor, (
        "\ndef _planted(ipa):\n"
        "    from orthography2ipa.distance import segment_distance\n"
        "    return segment_distance(ipa[0], ipa[0])\n" + anchor), 1)

    def read(name):
        return planted if name == "g2p" else revision._module_source(name).decode()

    assert "distance" in NOT_ENGINE
    assert "distance" in unlisted_engine_imports(read)
    assert "distance" not in unlisted_engine_imports(
        lambda name: revision._module_source(name).decode())


def test_the_static_walk_finds_an_import_behind_a_spec_flag():
    real = revision._module_source("g2p").decode()
    anchor = "\nclass G2P:"
    assert real.count(anchor) == 1
    planted = real.replace(anchor, (
        "\ndef _planted(spec):\n"
        "    if spec.tone_marks_syllable_final:\n"
        "        from orthography2ipa.planted_rare import nudge\n"
        "        return nudge\n" + anchor), 1)

    def read(name):
        return planted if name == "g2p" else revision._module_source(name).decode()

    assert "planted_rare" in import_closure(read)
    assert "planted_rare" not in import_closure(lambda name: revision._module_source(name).decode())


def test_an_import_in_a_module_the_engine_may_import_is_unlisted():
    """``version`` is outside the fingerprint, so a module it imports is unlisted too."""
    real = revision._module_source("version").decode()
    planted = real + "\nfrom orthography2ipa.distance import segment_distance  # noqa: F401\n"

    def read(name):
        return planted if name == "version" else revision._module_source(name).decode()

    assert "distance" in unlisted_engine_imports(read)
    assert not unlisted_engine_imports(lambda name: revision._module_source(name).decode())


def test_a_clade_with_no_parent_follows_its_parent_role_ancestor(monkeypatch, tmp_path):
    """The spec gives ``parent`` from its first parent-role ancestor, and the loader walks through a clade by it."""
    raw = json.loads(json_loader._index["mni"].read_text(encoding="utf-8"))
    assert "parent" not in raw or raw["parent"] is None
    ancestor = next(a["code"] for a in raw["ancestors"] if a["role"] == "parent")
    edit_spec(monkeypatch, tmp_path, "mni", lambda r: r.update(clade=True))
    before = spec_revision("mni-Mtei")
    edit_spec(monkeypatch, tmp_path, ancestor, add_grapheme)
    assert spec_revision("mni-Mtei") != before


def test_a_clade_whose_parent_has_no_file_follows_its_parent_role_ancestor(
        monkeypatch, tmp_path):
    """The loader drops a ``parent`` with no file, and the spec takes its first parent-role ancestor."""
    specs = {
        "qqa": {"code": "qqa", "name": "Data ancestor", "script": "Latin",
                "graphemes": {"a": ["a"]}, "stress": {"default_position": -1}},
        "qqb": {"code": "qqb", "name": "Clade", "script": "Latin", "clade": True,
                "parent": "qqz",
                "ancestors": [{"code": "qqa", "role": "parent", "weight": 1.0}],
                "graphemes": {}},
        "qqc": {"code": "qqc", "name": "Child", "script": "Latin", "parent": "qqb",
                "graphemes": {"a": ["a"]}},
    }

    def register():
        for code, raw in specs.items():
            path = tmp_path / f"{code}.json"
            path.write_text(json.dumps(raw), encoding="utf-8")
            monkeypatch.setitem(json_loader._index, code, path)
        monkeypatch.setattr(json_loader, "_specs", {})
        revision._canonical_spec.cache_clear()
        revision._spec_revision.cache_clear()

    register()
    assert "qqz" not in json_loader._index
    assert json_loader.load_json_spec("qqb").parent == "qqa"
    assert json_loader.load_json_spec("qqc").stress.default_position == -1
    before = spec_revision("qqc")

    specs["qqa"]["stress"]["default_position"] = -2
    register()
    assert json_loader.load_json_spec("qqc").stress.default_position == -2
    assert spec_revision("qqc") != before


# ── lexicon_revision ──────────────────────────────────────────────────────

class _EntryPoint:
    class dist:
        name = "fake-lexicons"

    def __init__(self, group, name, path):
        self.group = group
        self.name = name
        self.value = f"fake-lexicons:{name}"
        self.path = path

    def load(self):
        return lambda name: self.path


@pytest.fixture
def installed(monkeypatch, tmp_path):
    """A pt-PT provider of one exception file and one patch file, and nothing else."""
    lexicon = tmp_path / "pt-PT.tsv"
    lexicon.write_text("gato\tˈɡaʃtɐ\n", encoding="utf-8")
    patch = tmp_path / "pt-PT.patch.tsv"
    patch.write_text("rato\tˈʁɔtu\n", encoding="utf-8")
    points = {GROUP: [_EntryPoint(GROUP, "pt-PT", lexicon)],
              PATCH_GROUP: [_EntryPoint(PATCH_GROUP, "pt-PT", patch)]}
    monkeypatch.setattr(lexmod, "entry_points", lambda group=None: list(points.get(group, [])))
    lexmod._PACKAGED.clear()
    yield lexicon, patch
    lexmod._PACKAGED.clear()


def expected(patches, *files):
    digest = hashlib.sha256(f"patches:{int(patches)}\n".encode())
    for kind, path in zip(("lexicon", "patch"), files):
        data = path.read_bytes()
        digest.update(f"{kind}:{len(data)}\n".encode() + data)
    return "sha256:" + digest.hexdigest()


def test_lexicon_revision_hashes_the_file_packaged_lexicon_reads(installed):
    lexicon, patch = installed
    assert packaged_lexicon("pt-PT") == {"gato": "ˈɡaʃtɐ"}
    assert lexicon_revision("pt-PT") == expected(False, lexicon)
    assert lexicon_revision("pt") == lexicon_revision("pt-PT")
    assert lexicon_revision("pt-PT", patches=True) == expected(True, lexicon, patch)


def test_lexicon_revision_is_stable(installed):
    assert lexicon_revision("pt-PT") == lexicon_revision("pt-PT")
    assert lexicon_revision("pt-PT", patches=True) == lexicon_revision("pt-PT", patches=True)


def test_lexicon_revision_changes_with_the_file(installed):
    lexicon, patch = installed
    before = lexicon_revision("pt-PT")
    before_patched = lexicon_revision("pt-PT", patches=True)
    lexicon.write_text("gato\tˈɡatu\n", encoding="utf-8")
    assert lexicon_revision("pt-PT") != before
    after_patched = lexicon_revision("pt-PT", patches=True)
    assert after_patched != before_patched
    patch.write_text("rato\tˈʁatu\n", encoding="utf-8")
    assert lexicon_revision("pt-PT", patches=True) != after_patched


def test_patches_flag_changes_the_revision(installed):
    lexicon, patch = installed
    assert lexicon_revision("pt-PT", patches=True) != lexicon_revision("pt-PT")
    patch.write_text("", encoding="utf-8")
    assert lexicon_revision("pt-PT", patches=True) != lexicon_revision("pt-PT")


def test_lexicon_revision_without_a_provider_raises(installed):
    with pytest.raises(LookupError):
        lexicon_revision("fi")
    with pytest.raises(LookupError):
        packaged_lexicon("fi")


def test_lexicon_revision_without_a_patch_file_raises(installed, monkeypatch):
    monkeypatch.setattr(lexmod, "entry_points", lambda group=None: [
        _EntryPoint(GROUP, "pt-PT", installed[0])] if group == GROUP else [])
    lexmod._PACKAGED.clear()
    assert lexicon_revision("pt-PT").startswith("sha256:")
    with pytest.raises(LookupError):
        lexicon_revision("pt-PT", patches=True)
    with pytest.raises(LookupError):
        packaged_lexicon("pt-PT", patches=True)
