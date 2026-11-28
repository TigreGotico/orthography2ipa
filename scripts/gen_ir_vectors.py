"""Write the IR conformance vectors of section 8.4 into tests/conformance/ir-v1/.

For each target the tool compiles the IR with ``orthography2ipa.ir.compiler``,
runs its inputs through the Python reference interpreter, and writes
``<stem>.jsonl``: one ``ir`` line, then one ``case`` line per input. The
targets and their inputs:

* the 20 codes of ``tests/data/ir_golden_ci.json`` and kab: the first SAMPLE
  sorted distinct words of the golden rows, or of the shipped gold TSV for a
  code with no golden rows;
* the leader specs of LEADERS: the words of ``tests/data/ir_vector_inputs.json``
  for the language, then the inputs of ``tests/data/rules_outputs.json``;
* every lect of LECT_PREFIXES: the inputs whose output differs from the
  output of the parent spec, one for each new difference, at most LECT_CASES,
  plus AGREE inputs with the parent's output;
* ``pt-PT@<profile>`` for each dialect profile: the same choice against
  plain pt-PT, from the texts of ``tests/data/ep_dialect_sentences.csv``;
* targeted cases: for each IR feature of ``ir_features.feature_names()``, the
  first case whose output changes when the feature is ablated. When no
  sampled case does that, the tool adds the first input of the target's
  pool that does. ``features.json`` names the case of each feature.

* ``pt-PT-syllable``: the pt-PT IR with the fragment
  ``tests/data/ir_fragment_syllable.json``, and for each word of its list one
  ``case`` line and one ``syllables`` line, the written syllables of S5.

Every file also holds an empty input. ``unknown-version.jsonl`` holds the
cop IR with one primitive version raised, and one case that expects the
version error.

    python -I scripts/gen_ir_vectors.py          # write the files
    python -I scripts/gen_ir_vectors.py --check  # regenerate in memory and compare
"""
import argparse
import ast
import csv
import difflib
import json
import sys
import warnings
from pathlib import Path
from typing import Dict, List, Optional, Tuple

warnings.simplefilter("ignore")

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / "scripts"))

from ir_features import ablate, feature_names  # noqa: E402
from orthography2ipa import DIALECT_PROFILES, registry  # noqa: E402
from orthography2ipa.ir import layout  # noqa: E402
from orthography2ipa.ir.compiler import build_ir, contact_entries  # noqa: E402
from orthography2ipa.ir.interpreter import Interpreter, IRVersionError  # noqa: E402

OUT = REPO / "tests" / "conformance" / "ir-v1"
DATA = REPO / "tests" / "data"
GOLDEN = DATA / "ir_golden_ci.json"
FEATURES = "features.json"
#: The codes of ir_golden_ci.json and kab: the set that scripts/ir_parity_ci.py checks.
GOLDEN_SPECS = tuple(sorted([*json.loads(GOLDEN.read_text(encoding="utf-8")), "kab"]))
LEADERS = ("pt-PT", "pt-BR", "es-CO", "fr-FR", "it-IT", "de-DE", "nl-NL", "da", "kab", "hi", "bn")
LECT_PREFIXES = ("pt-PT-x-", "pt-BR-x-", "fr-", "es-")
#: Lects left out, with the reason. A vector file holds the whole IR.
EXCLUDED = {"es-PY": "its IR is 13 MB: stress.mark_onsets enumerates 16 MB of onset tuples (#2721)"}
#: Specs and compile options that carry IR features the sets above lack.
FEATURE_TARGETS = {
    "ar": ("ar", {}), "el": ("el", {}), "gv": ("gv", {}), "km": ("km", {}), "lo": ("lo", {}), "my": ("my", {}), "ml": ("ml", {}),
    "ru": ("ru", {}), "sv": ("sv", {}), "th": ("th", {}), "car": ("car", {}),
    "ar+arbtok": ("ar", {"fragments": (json.loads((DATA / "arbtok_sandhi_fragment.json").read_text(encoding="utf-8")),)}),
    "pt-PT+words": ("pt-PT", {"fragments": ({"ir_version": 1, "words": {"asa": "ˈwx"}},)}),
    "pt-PT+allophones": ("pt-PT", {"expand_allophones": True}),
}
#: Features that no case can show, with the reason (#2722).
UNREACHABLE = {
    "cut_pairs": "no pair of the syllable fragment is an onset, so the onset split already cuts each one",
    "node.count": "the compiler emits no such node",
    "node.false": "the compiler emits no such node",
    "node.top_in": "the compiler emits no such node",
    "node.word_has_entry": "the compiler emits no such node",
    "dnode.true": "the predicate normal form removes it from every dialect step",
    "gate.and": "its one node, and(not ⟨ei⟩, spell_empty), gates a rewrite of C+ɐj that only ⟨ei⟩ makes",
    "allophone_map": "its readings rank below the top reading, and every case runs with width 1",
}
SAMPLE = 200
LECT_CASES = 48
AGREE = 4
EXTRA = {"pt-PT": ["os jogos"]}
VERSION_ERROR = "unsupported primitive version"
#: Vector files of an IR with a fragment: stem -> (code, fragment, words).
FRAGMENT_VECTORS = {
    "pt-PT-syllable": ("pt-PT", DATA / "ir_fragment_syllable.json", (
        "carro", "nascer", "exceto", "desça", "bairro", "rainha", "juiz", "ainda", "ao", "aos", "aorta",
        "arruinar", "adleriano", "sublinhar", "sublocar", "sublime", "distribuidor", "construir",
        "cuidado", "ingenuidade", "contiguidade", "kubitschek", "gourmet", "facebookiano", "bureau",
        "boxeur", "marathon", "alzheimer", "pacto", "atleta", "abstrair", "neymar", "playground",
        "olho-d'água", "olá--bom", "bê-á-'bá")),
    "arz-EG-contact": ("arz-EG", DATA / "ir_fragment_contact.json", (
        "model", "Model", "computer", "jazz", "bank", "thinking", "the", "كتاب", "كتاب model", "Bank كبير")),
}
#: The size budget of one file: the IR line, and the case lines together.
IR_BUDGET = 1 << 20
CASE_BUDGET = 48 << 10


def _line(obj: dict) -> str:
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "\n"


def lects() -> Tuple[str, ...]:
    return tuple(sorted(c for c in registry.available_codes()
                        if c.startswith(LECT_PREFIXES) and c not in LEADERS and c not in EXCLUDED))


def stems() -> Tuple[str, ...]:
    """The stem of every vector file."""
    return tuple(sorted({*GOLDEN_SPECS, *LEADERS, *lects(), *(f"pt-PT@{p}" for p in DIALECT_PROFILES),
                         *FEATURE_TARGETS, *FRAGMENT_VECTORS,
                         "unknown-version"}))


def _rules_inputs() -> Dict[str, List[str]]:
    pool: Dict[str, List[str]] = {}
    for key in json.loads((DATA / "rules_outputs.json").read_text(encoding="utf-8")):
        _, lang, method, args, _ = json.loads(key)
        if method == "transcribe":
            text = ast.literal_eval(args)[0]
            pool.setdefault(lang, []).append(text)
    return {lang: sorted(set(texts)) for lang, texts in pool.items()}


def _dialect_texts() -> List[str]:
    with (DATA / "ep_dialect_sentences.csv").open(encoding="utf-8") as f:
        return sorted({row["text"] for row in csv.DictReader(f)})


def _gold(code: str) -> List[str]:
    tsv = next((REPO / "orthography2ipa" / "data" / "gold").glob(f"*/{code}.tsv"))
    with tsv.open(encoding="utf-8") as f:
        return sorted({row["sentence"] for row in csv.DictReader(f, delimiter="\t")})


def _unique(texts) -> List[str]:
    return list(dict.fromkeys(texts))


class Target:
    """One vector file: its IR and its inputs."""

    def __init__(self, stem: str, code: str, **options):
        self.stem, self.code = stem, code
        self.ir = build_ir(code, None, **options)
        self.doc = layout.encode(self.ir)
        del self.doc["source"]
        self.donors = {}
        for entry, (donor_ir, donor_words) in contact_entries(options.get("fragments", ()), code, self.ir):
            donor_doc = layout.encode(donor_ir)
            del donor_doc["source"]
            self.donors[entry["donor"]] = (donor_doc, donor_words)
        self.it = Interpreter(self.doc, donors={c: (Interpreter(d), w) for c, (d, w) in self.donors.items()})
        self.inputs: List[str] = []
        self.pool: List[str] = []
        self.syllable_words: List[str] = []
        self.uses = set(layout.manifest(self.ir).replace("=", ";").split(";")[::2])
        if self.ir.get("dialect"):
            self.uses |= {n for n in feature_names() if n.startswith(("gate.", "dnode."))}

    def out(self, text: str) -> str:
        return self.it.transcribe(text, width=1)

    def file(self) -> str:
        lines = [_line({"kind": "donor", "lang": c, "ir": d,
                        "words": [[[ord(x) for x in k], [ord(x) for x in v]] for k, v in sorted(w.items())]})
                 for c, (d, w) in sorted(self.donors.items())]
        lines.append(_line({"kind": "ir", "lang": self.code, "revision": layout.spec_revision(self.ir), "ir": self.doc}))
        for word in self.syllable_words:
            lines.append(_line({"kind": "syllables", "input": [ord(c) for c in word],
                                "expect": [[ord(c) for c in s] for s in self.it.syllables(word)]}))
        for text in self.inputs + [""]:
            lines.append(_line({"kind": "case", "input": [ord(c) for c in text],
                                "expect": [ord(c) for c in self.out(text)]}))
        return "".join(lines)


def _signature(a: str, b: str) -> frozenset:
    ops = difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes()
    return frozenset((a[i1:i2], b[j1:j2]) for tag, i1, i2, j1, j2 in ops if tag != "equal")


def differences(target: Target, parent: Target, pool: List[str]) -> Tuple[List[str], int, int]:
    """Inputs that show each new difference from *parent*, then AGREE inputs
    with the same output; also the number of differing inputs and of distinct
    differences in the pool."""
    seen: set = set()
    picked, agree, differing = [], [], 0
    for text in pool:
        a, b = parent.out(text), target.out(text)
        if a == b:
            agree.append(text)
            continue
        differing += 1
        sig = _signature(a, b)
        if sig - seen:
            if len(picked) < LECT_CASES:
                picked.append(text)
            seen |= sig
    return picked + agree[:AGREE], differing, len(seen)


def _synthetic(ir: dict) -> List[str]:
    """Pseudo-words around each grapheme key: one input for each entry."""
    vowel = next(iter(sorted(ir.get("syllable", {}).get("vowel_letters", ()))), "a")
    keys = sorted(e["key"] for e in ir["entries"] if e["key"].strip() and e.get("trie"))
    return [f"{vowel}{k}{vowel}" for k in keys] + [f"{k}{vowel}" for k in keys]


def _exception_words(ir: dict) -> List[str]:
    """The override words, and each one after an elided letter and an apostrophe."""
    listed = [w for w, _ in ir["word"]["exceptions"]] + [w for w, _ in ir["word"].get("words", ())]
    if not ir["word"]["apostrophe_elision"]:
        return listed
    letters = sorted(e["key"] for e in ir["entries"] if len(e["key"]) == 1 and e["key"].isalpha())[:4]
    return listed + [f"{c}'{w}" for w in listed[:40] for c in letters]


def build_targets(stems_wanted) -> Dict[str, Target]:
    golden = json.loads(GOLDEN.read_text(encoding="utf-8"))
    words = json.loads((DATA / "ir_vector_inputs.json").read_text(encoding="utf-8"))
    rules = _rules_inputs()
    dialect_texts = _dialect_texts()
    pt_golden = sorted({w for w, _ in golden["pt-PT"]})

    def family(code: str) -> List[str]:
        lang = code.split("-")[0]
        texts = list(words.get(lang, ()))
        if lang == "pt":
            texts += pt_golden + dialect_texts
        texts += [t for c in sorted(rules) if c.split("-")[0] == lang for t in rules[c]]
        return _unique(texts)

    targets: Dict[str, Target] = {}

    def get(stem: str) -> Target:
        if stem not in targets:
            code, _, profile = stem.partition("@")
            if stem in FRAGMENT_VECTORS:
                code, path, _ = FRAGMENT_VECTORS[stem]
                options = {"fragments": [json.loads(path.read_text(encoding="utf-8"))]}
            else:
                code, options = FEATURE_TARGETS.get(stem, (code, {"dialect_profile": profile} if profile else {}))
            targets[stem] = Target(stem, code, **options)
        return targets[stem]

    for stem in stems_wanted:
        if stem == "unknown-version":
            continue
        t = get(stem)
        code, _, profile = stem.partition("@")
        if stem in FRAGMENT_VECTORS:
            t.inputs = list(FRAGMENT_VECTORS[stem][2])
            if "syllable" in t.ir:
                t.syllable_words = list(t.inputs)
        elif stem in FEATURE_TARGETS:
            t.inputs = _unique(words.get(t.code, []) + rules.get(t.code, []))[:SAMPLE]
        elif profile:
            t.inputs, n, d = differences(t, get(code), dialect_texts)
            print(f"{stem}: pool {len(dialect_texts)}, differing {n}, differences {d}, picked {len(t.inputs)}",
                  flush=True)
        elif code in golden:
            t.inputs = sorted({w for w, _ in golden[code]})[:SAMPLE] + EXTRA.get(code, [])
        elif code == "kab":
            t.inputs = _gold(code)[:SAMPLE]
        elif code in LEADERS:
            t.inputs = family(code)[:SAMPLE]
        else:
            parent = get(registry.get(code).parent)
            pool = _unique(family(code) + _synthetic(t.ir))
            t.inputs, n, d = differences(t, parent, pool)
            print(f"{stem}: parent {parent.stem}, pool {len(pool)}, differing {n}, differences {d}, "
                  f"picked {len(t.inputs)}", flush=True)
        t.pool = _unique(t.inputs + (dialect_texts if profile else []) + family(t.code) + rules.get(t.code, []) + _exception_words(t.ir)
                         + _synthetic(t.ir))
    return {s: targets[s] for s in stems_wanted if s in targets}


def _changes(target: Target, ablated: dict, texts) -> Optional[int]:
    """The index of the first text whose output the ablated IR changes."""
    try:
        it = Interpreter(ablated)
    except Exception:
        return None
    for i, text in enumerate(texts):
        try:
            if it.transcribe(text, width=1) != target.out(text):
                return i
        except Exception:
            continue
    return None


def _syllables_change(target: Target, ablated: dict) -> Optional[int]:
    """The index of the first syllables line whose output the ablated IR changes."""
    it = Interpreter(ablated)
    for i, word in enumerate(target.syllable_words):
        if it.syllables(word) != target.it.syllables(word):
            return i
    return None


def cover(targets: Dict[str, Target]) -> Dict[str, list]:
    """The case of each feature. Adds a targeted input where no case shows a feature."""
    found: Dict[str, list] = {}
    order = sorted(targets.values(), key=lambda t: len(t.doc["strings"]))
    for name in feature_names():
        if name in UNREACHABLE:
            continue
        ablated = {}
        for t in order:
            if name not in t.uses:
                continue
            ablated[t.stem] = ablate(t.ir, name)
            if ablated[t.stem] is None:
                continue
            i = _changes(t, ablated[t.stem], t.inputs)
            if i is not None:
                found[name] = [f"{t.stem}.jsonl", len(t.syllable_words) + i]
                break
            i = _syllables_change(t, ablated[t.stem])
            if i is not None:
                found[name] = [f"{t.stem}.jsonl", i]
                break
        else:
            for t in order:
                if ablated.get(t.stem) is None:
                    continue
                extra = [x for x in t.pool if x not in t.inputs]
                i = _changes(t, ablated[t.stem], extra)
                if i is not None:
                    t.inputs.append(extra[i])
                    found[name] = [f"{t.stem}.jsonl", len(t.syllable_words) + len(t.inputs) - 1]
                    print(f"{name}: targeted {extra[i]!r} in {t.stem}", flush=True)
                    break
            else:
                print(f"{name}: UNCOVERED", flush=True)
    return found


def keep_targeted(targets: Dict[str, Target]) -> None:
    """For a run of some stems: append the targeted inputs that features.json names."""
    found = json.loads((OUT / FEATURES).read_text(encoding="utf-8"))
    for file, index in sorted(found.values(), key=lambda fi: fi[1]):
        t = targets.get(file[:-len(".jsonl")])
        if t is None or index < len(t.syllable_words) + len(t.inputs):
            continue
        with (OUT / file).open(encoding="utf-8") as f:
            lines = f.readlines()
        t.inputs.append("".join(map(chr, json.loads(lines[1 + index])["input"])))


def version_file(target: Target) -> str:
    doc = json.loads(json.dumps(target.doc))
    name = sorted(doc["primitives"])[0]
    doc["primitives"][name] += 1
    try:
        Interpreter(doc)
    except IRVersionError as exc:
        assert str(exc).startswith(VERSION_ERROR), exc
    else:
        raise AssertionError("the interpreter accepted a raised primitive version")
    return (_line({"kind": "ir", "lang": target.code, "revision": layout.spec_revision(target.ir), "ir": doc})
            + _line({"kind": "case", "input": [], "expect_error": VERSION_ERROR}))


def generate(wanted) -> Dict[str, str]:
    targets = build_targets(wanted)
    files = {}
    if len(wanted) == len(stems()):
        files[FEATURES] = json.dumps(cover(targets), ensure_ascii=False, indent=1, sort_keys=True) + "\n"
        files["unknown-version.jsonl"] = version_file(targets["cop"])
    else:
        keep_targeted(targets)
    for stem, t in targets.items():
        files[f"{stem}.jsonl"] = t.file()
        print(f"{stem}: N in {len(t.inputs) + 1}, N out {files[f'{stem}.jsonl'].count(chr(10)) - 1}", flush=True)
    return dict(sorted(files.items()))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="compare with the files on disk, write nothing")
    ap.add_argument("--lang", action="append", choices=stems(),
                    help="write only the file of this stem; its targeted cases need a full run")
    args = ap.parse_args()
    wanted = tuple(args.lang) if args.lang else stems()
    files = generate(wanted)
    vectors = [text for name, text in files.items() if name.endswith(".jsonl")]
    n_cases = sum(text.count("\n") - 1 for text in vectors)
    size = sum(len(text.encode()) for text in files.values())
    print(f"specs {len(vectors)}, files {len(files)}, cases {n_cases}, bytes {size}")
    if args.check:
        stale = sorted(name for name, text in files.items()
                       if not (OUT / name).exists() or (OUT / name).read_text(encoding="utf-8") != text)
        extra = [] if args.lang else sorted(p.name for p in OUT.iterdir() if p.name not in files)
        for name in stale + extra:
            print(f"STALE {name}")
        return 1 if stale or extra else 0
    OUT.mkdir(parents=True, exist_ok=True)
    for name, text in files.items():
        (OUT / name).write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
