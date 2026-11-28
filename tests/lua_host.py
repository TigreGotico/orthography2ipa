"""Run an exported loom file the way the loom host runs a ``lua`` phonemizer."""
import json
import subprocess
from pathlib import Path

from gguf import GGUFReader

_HOST = """
local dir = %r
local languages = {%s}
function phonemizer_data(lang)
  local f = io.open(dir .. "/" .. languages[lang + 1] .. ".json", "rb")
  if not f then return nil end
  local s = f:read("*a"); f:close(); return s
end
dofile(dir .. "/script.lua")
%s
local ipa, unmapped = phonemize({%s}, %d)
io.write(table.concat(ipa, " "), "|", table.concat(unmapped, " "))
"""


def field(reader: GGUFReader, key: str):
    return reader.fields[key].contents()


def phonemize(reader: GGUFReader, text: str, lang: int, tmp_path: Path, before: str = ""):
    """The IPA and the unmapped text that the file's script gives for *text*."""
    languages = field(reader, "loom.text.languages")
    (tmp_path / "script.lua").write_text(field(reader, "loom.phonemizer.script"), encoding="utf-8")
    for code in languages:
        (tmp_path / f"{code}.json").write_text(field(reader, f"loom.phonemizer.data.{code}"), encoding="utf-8")
    host = _HOST % (str(tmp_path), ", ".join(json.dumps(c) for c in languages), before,
                    ", ".join(str(ord(c)) for c in text), lang)
    proc = subprocess.run(["luajit", "-e", host], capture_output=True, text=True, check=True)
    ipa, unmapped = proc.stdout.split("|")
    return "".join(chr(int(x)) for x in ipa.split()), "".join(chr(int(x)) for x in unmapped.split())
