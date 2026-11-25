"""Refuse language knowledge in the IR interpreters.

The interpreters run one compiled IR document and nothing else. Behaviour
lives in the data, so an interpreter never tests a language code, a script
or a family name, never asks Unicode for a character name, never imports
phonematcher, and never compares a codepoint against a range to guess a
script. This check parses
the runtime files (``ast`` for Python, a token scan for Lua) and lists every
violation with its file and line.

The forbidden names come from the spec data, not from a hand-typed list:
every ``orthography2ipa/data/*.json`` file name and ``code`` value is a
language code, and every ``script``, ``script_type`` and ``family`` value is
a script or family name. A bare code that is also an IR vocabulary word (a
field, node or primitive name of ``orthography2ipa/ir/layout.py``) is not a
violation: ``and``, ``set`` and ``end`` are ISO 639-3 codes as well as IR
words. A code with a subtag, such as ``pt-PT``, is always a violation.

The check reads literals only: a code built by string concatenation or a
script found by codepoint arithmetic passes it, so review still applies.

    python -I scripts/check_engine_agnostic.py [FILE ...]

Exit status 1 means at least one violation.
"""
import argparse
import ast
import json
import re
import sys
from pathlib import Path
from typing import Iterator, List, NamedTuple, Optional, Set, Tuple

REPO = Path(__file__).resolve().parent.parent
IR = REPO / "orthography2ipa" / "ir"
RUNTIME = [IR / "interpreter.py", IR / "pattern.py", IR / "dialect.py", IR / "layout.py",
           IR / "interpreter.lua"]

# UTF-8 and UTF-16 encoding boundaries. A codec compares against these to
# encode or decode a codepoint, which is not a test on a script.
CODEC_BOUNDARIES = {0x80, 0x800, 0x10000, 0x110000, 0xD800, 0xDBFF, 0xDC00, 0xDFFF}

UNICODE_NAME_CALLS = {"name", "lookup"}

# The interpreters read the compiled IR only. The vowel and place tables are
# compile-time knowledge, so phonematcher is never a runtime import.
FORBIDDEN_IMPORTS = {"unicodedata", "phonematcher"}

# IR words that are also ISO 639-3 codes and that layout.py does not name,
# because they are values of opaque fields. Each one is defined in
# docs/ir/o2i-ir-v1.md, and tests/test_engine_agnostic.py holds it to that.
IR_OPAQUE_WORDS = {
    "any", "set", "bol", "seq", "alt",  # pattern nodes (primitive 2)
    "end",  # the open upper bound of a node.count window
    "sub",  # the pattern rewrite kind of a dialect step
}


class Violation(NamedTuple):
    path: str
    line: int
    message: str

    def __str__(self) -> str:
        return f"{self.path}:{self.line}: {self.message}"


class Vocab(NamedTuple):
    codes: Set[str]
    names: Set[str]
    ir_words: Set[str]


def load_vocab(data_dir: Path = REPO / "orthography2ipa" / "data") -> Vocab:
    codes: Set[str] = set()
    names: Set[str] = set()
    for path in data_dir.glob("*.json"):
        spec = json.loads(path.read_text(encoding="utf-8"))
        codes.update({path.stem, spec.get("code") or path.stem})
        for key in ("script", "script_type", "family"):
            if spec.get(key):
                names.add(spec[key].casefold())
    sys.path.insert(0, str(REPO))
    from orthography2ipa.ir import layout
    ir_words: Set[str] = set()

    def walk(t) -> None:
        if isinstance(t, str):
            ir_words.add(t)
        elif isinstance(t, tuple):
            for part in t:
                walk(part)
        elif isinstance(t, dict):
            for key, value in t.items():
                ir_words.add(key)
                walk(value)

    walk(layout.LAYOUT)
    for name in layout.SEMANTICS:
        ir_words.update(name.split("."))
    for table in layout._PRED_TABLES.values():
        ir_words.update(table)
    return Vocab(codes, names, ir_words | IR_OPAQUE_WORDS)


def judge_literal(value: str, vocab: Vocab) -> Optional[str]:
    if value in vocab.codes and ("-" in value or value not in vocab.ir_words):
        return f"language code literal {value!r}"
    if value.casefold() in vocab.names and value not in vocab.ir_words:
        return f"script or family name literal {value!r}"
    return None


def is_script_codepoint(value) -> bool:
    if isinstance(value, str) and len(value) == 1:
        value = ord(value)
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0x80 \
        and value not in CODEC_BOUNDARIES


def check_python(path: Path, vocab: Vocab) -> List[Violation]:
    src = path.read_text(encoding="utf-8")
    found: List[Violation] = []
    for match in re.finditer(r"\\N\{", src):
        found.append(Violation(str(path), src.count("\n", 0, match.start()) + 1,
                               "Unicode character name escape \\N{...}"))
    tree = ast.parse(src)
    doc_nodes = {id(node.body[0].value) for node in ast.walk(tree)
                 if isinstance(node, (ast.Module, ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef))
                 and node.body and isinstance(node.body[0], ast.Expr)
                 and isinstance(node.body[0].value, ast.Constant)}
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and id(node) not in doc_nodes:
            message = judge_literal(node.value, vocab)
            if message:
                found.append(Violation(str(path), node.lineno, message))
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            modules = [getattr(node, "module", None) or ""] if isinstance(node, ast.ImportFrom) \
                else [alias.name for alias in node.names]
            for module in modules:
                if module.split(".")[0] in FORBIDDEN_IMPORTS:
                    found.append(Violation(str(path), node.lineno, f"imports {module} at runtime"))
        elif isinstance(node, ast.Attribute) and node.attr in UNICODE_NAME_CALLS \
                and isinstance(node.value, ast.Name) and node.value.id == "unicodedata":
            found.append(Violation(str(path), node.lineno, f"Unicode name lookup unicodedata.{node.attr}"))
        elif isinstance(node, ast.Compare):
            ordering = any(isinstance(op, (ast.Lt, ast.LtE, ast.Gt, ast.GtE)) for op in node.ops)
            operands = [node.left, *node.comparators]
            if ordering and any(isinstance(o, ast.Constant) and is_script_codepoint(o.value) for o in operands):
                found.append(Violation(str(path), node.lineno, "codepoint range comparison"))
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "range" \
                and any(isinstance(a, ast.Constant) and is_script_codepoint(a.value) for a in node.args):
            found.append(Violation(str(path), node.lineno, "codepoint range literal"))
    return found


LONG_COMMENT = re.compile(r"--\[(=*)\[")
LONG_STRING = re.compile(r"\[(=*)\[")
LUA_TOKEN = re.compile(r"0[xX][0-9a-fA-F]+|\d+|[<>]=?|==|~=|[A-Za-z_]\w*(?:\.\w+)*|\S")


def lua_tokens(src: str) -> Iterator[Tuple[str, str, int]]:
    """Yield (kind, text, line) for strings, numbers and operators; skip comments."""
    i, line, n = 0, 1, len(src)
    while i < n:
        c = src[i]
        if c.isspace():
            line += c == "\n"
            i += 1
        elif src.startswith("--", i):
            long = LONG_COMMENT.match(src, i)
            end = src.find("]" + long.group(1) + "]", i) + len(long.group(1)) + 2 if long else src.find("\n", i)
            end = n if end < 2 else end
            line += src.count("\n", i, end)
            i = end
        elif c in "\"'":
            j = i + 1
            while j < n and src[j] != c:
                j += 2 if src[j] == "\\" else 1
            yield "str", src[i + 1:j], line
            line += src.count("\n", i, j)
            i = j + 1
        elif LONG_STRING.match(src, i):
            eq = LONG_STRING.match(src, i).group(1)
            end = src.find("]" + eq + "]", i)
            yield "str", src[i + len(eq) + 2:end], line
            line += src.count("\n", i, end)
            i = end + len(eq) + 2
        else:
            m = LUA_TOKEN.match(src, i)
            text = m.group(0)
            kind = "num" if text[0].isdigit() else "op" if text in ("<", "<=", ">", ">=") else "word"
            yield kind, text, line
            i += len(text)


def lua_unescape(text: str) -> str:
    def code(m: re.Match) -> str:
        if m.group(1):
            return chr(int(m.group(1), 16))
        if m.group(2):
            return chr(int(m.group(2)))
        return m.group(0)
    return re.sub(r"\\u\{([0-9a-fA-F]+)\}|\\(\d{1,3})", code, text)


def check_lua(path: Path, vocab: Vocab) -> List[Violation]:
    found: List[Violation] = []
    tokens = list(lua_tokens(path.read_text(encoding="utf-8")))
    for k, (kind, text, line) in enumerate(tokens):
        if kind == "str":
            if text.split(".")[0] == "phonematcher":
                found.append(Violation(str(path), line, f"requires {text} at runtime"))
            message = judge_literal(text, vocab)
            if message:
                found.append(Violation(str(path), line, message))
            value = lua_unescape(text)
            if len(value) == 1 and is_script_codepoint(value) and any(
                    t[0] == "op" for t in tokens[max(k - 1, 0):k + 2]):
                found.append(Violation(str(path), line, "codepoint range comparison"))
        elif kind == "num" and is_script_codepoint(int(text, 0)) and any(
                t[0] == "op" for t in tokens[max(k - 1, 0):k + 2] if t is not tokens[k]):
            found.append(Violation(str(path), line, "codepoint range comparison"))
        elif kind == "word" and re.search(r"(^|\.)(charname|unicode_name|utf8\.name)$", text):
            found.append(Violation(str(path), line, f"Unicode name lookup {text}"))
    return found


def check(paths: List[Path], vocab: Optional[Vocab] = None) -> List[Violation]:
    vocab = vocab or load_vocab()
    found: List[Violation] = []
    for path in paths:
        found += check_lua(path, vocab) if path.suffix == ".lua" else check_python(path, vocab)
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("files", nargs="*", type=Path)
    args = ap.parse_args()
    paths = args.files or [p for p in RUNTIME if p.exists()]
    vocab = load_vocab()
    found = check(paths, vocab)
    print(f"checked {len(paths)} files against {len(vocab.codes)} language codes and "
          f"{len(vocab.names)} script and family names: {len(found)} violations")
    for violation in found:
        print(violation)
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
