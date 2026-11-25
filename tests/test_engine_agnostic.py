"""scripts/check_engine_agnostic.py refuses language knowledge in the interpreters."""
import importlib.util
import re
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("check_engine_agnostic", REPO / "scripts" / "check_engine_agnostic.py")
check_engine_agnostic = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_engine_agnostic)

INTERPRETER = REPO / "orthography2ipa" / "ir" / "interpreter.py"
ANCHOR = "    def transcribe("


@pytest.fixture(scope="module")
def vocab():
    return check_engine_agnostic.load_vocab()


def injected(tmp_path: Path, body: str) -> Path:
    """A copy of interpreter.py with *body* as the first lines of a new method."""
    src = INTERPRETER.read_text(encoding="utf-8")
    assert ANCHOR in src
    method = "    def _injected(self, lang, cp, ch):\n" + "".join(f"        {line}\n" for line in body.split("\n"))
    path = tmp_path / "interpreter.py"
    path.write_text(src.replace(ANCHOR, method + "\n" + ANCHOR, 1), encoding="utf-8")
    return path


def test_runtime_files_are_clean(vocab):
    paths = [p for p in check_engine_agnostic.RUNTIME if p.exists()]
    assert INTERPRETER in paths
    assert check_engine_agnostic.check(paths, vocab) == []


def test_vocab_comes_from_the_spec_data(vocab):
    data = REPO / "orthography2ipa" / "data"
    assert len(vocab.codes) == len(list(data.glob("*.json")))
    assert {"pt-PT", "kab", "en-US"} <= vocab.codes
    assert {"latin", "arabic", "cyrillic", "abjad", "creole"} <= vocab.names


@pytest.mark.parametrize("body, message", [
    ('if lang == "pt-PT":\n    return 1', "language code literal 'pt-PT'"),
    ('if lang in ("kab", "fr"):\n    return 1', "language code literal 'kab'"),
    ('return {"tr": 1}.get(lang)', "language code literal 'tr'"),
    ('if self.ir.get("script") == "Arabic":\n    return 1', "script or family name literal 'Arabic'"),
    ('return lang == "Creole"', "script or family name literal 'Creole'"),
    ('import unicodedata\nreturn unicodedata.name(ch)', "Unicode name lookup unicodedata.name"),
    ('import phonematcher\nreturn 1', "imports phonematcher at runtime"),
    ('from phonematcher import is_vowel_phone\nreturn 1', "imports phonematcher at runtime"),
    ('from phonematcher.features import vectorize_phones\nreturn 1', "imports phonematcher.features at runtime"),
    ('return "\\N{ARABIC LETTER ALEF}" == ch', "Unicode character name escape"),
    ('return 0x0600 <= cp <= 0x06FF', "codepoint range comparison"),
    ('return "\\u0590" < ch', "codepoint range comparison"),
    ('return cp in range(0x0900, 0x097F)', "codepoint range literal"),
])
def test_python_violation_fails(tmp_path, vocab, body, message):
    found = check_engine_agnostic.check([injected(tmp_path, body)], vocab)
    assert [v.message for v in found if message in v.message], found


def test_python_violation_fails_the_command(tmp_path, capsys):
    path = injected(tmp_path, 'if lang == "pt-PT":\n    return 1')
    import sys
    argv, sys.argv = sys.argv, ["check_engine_agnostic.py", str(path)]
    try:
        assert check_engine_agnostic.main() == 1
    finally:
        sys.argv = argv
    out = capsys.readouterr().out
    assert re.search(r"interpreter\.py:\d+: language code literal 'pt-PT'", out)


def test_docstrings_and_ir_words_pass(tmp_path, vocab):
    body = '"""Text about pt-PT and Arabic in a docstring."""\nreturn lang == "and" or cp < 0x80'
    assert check_engine_agnostic.check([injected(tmp_path, body)], vocab) == []


LUA_CLEAN = '''
-- a comment may name pt-PT and Arabic
local function enc(cp)
  if cp < 0x80 then return string.char(cp) end
  if cp >= 0xD800 and cp <= 0xDBFF then return nil end
  return op == "and" or op == "seq"
end
'''


@pytest.mark.parametrize("snippet, message", [
    ('if lang == "pt-PT" then return 1 end', "language code literal 'pt-PT'"),
    ("local t = {['kab'] = true}", "language code literal 'kab'"),
    ('local pm = require("phonematcher")', "requires phonematcher at runtime"),
    ('if script == "Cyrillic" then return 1 end', "script or family name literal 'Cyrillic'"),
    ("if cp >= 0x0600 and cp <= 0x06FF then return 1 end", "codepoint range comparison"),
    ('if ch > "\\u{0590}" then return 1 end', "codepoint range comparison"),
])
def test_lua_violation_fails(tmp_path, vocab, snippet, message):
    path = tmp_path / "interpreter.lua"
    path.write_text(LUA_CLEAN, encoding="utf-8")
    assert check_engine_agnostic.check([path], vocab) == []
    path.write_text(LUA_CLEAN + snippet + "\n", encoding="utf-8")
    found = check_engine_agnostic.check([path], vocab)
    assert [v for v in found if message in v.message and v.line == LUA_CLEAN.count("\n") + 1], found


def test_ir_opaque_words_are_defined_in_the_spec():
    spec = (REPO / "docs" / "ir" / "o2i-ir-v1.md").read_text(encoding="utf-8")
    for word in check_engine_agnostic.IR_OPAQUE_WORDS:
        assert re.search(rf'`"?{word}"?`', spec), word
