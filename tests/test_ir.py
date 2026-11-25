"""Tests for the o2i IR v1: compiler, canonical form, revision and the
reference interpreter (docs/ir/o2i-ir-v1.md)."""
import ast
import csv
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

from tests.frozen_rules import FrozenRules
from orthography2ipa.ir import layout, pattern
from orthography2ipa.ir.compile_patterns import compile_pattern, compile_template
from orthography2ipa.ir.compiler import build_ir
from orthography2ipa.ir.interpreter import Interpreter, IRVersionError
from orthography2ipa.registry import available_codes, get
from orthography2ipa.transforms import DIALECT_PROFILES

IR_DIR = Path(__file__).resolve().parent.parent / "orthography2ipa" / "ir"
DIALECT_CSV = Path(__file__).resolve().parent / "data" / "ep_dialect_sentences.csv"
RUNTIME_MODULES = ("interpreter.py", "pattern.py", "dialect.py", "layout.py")
ALLOWED_IMPORTS = {"__future__", "dataclasses", "itertools", "typing", "hashlib", "json",
                   "orthography2ipa.ir", "orthography2ipa.ir.dialect"}


@pytest.fixture(scope="module")
def pt_ir():
    return build_ir("pt-PT")


@pytest.fixture(scope="module")
def pt_doc(pt_ir):
    return layout.encode(pt_ir)


def _imports(path: Path):
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Import):
            yield from (a.name for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            yield node.module


class TestImportIsolation:
    @pytest.mark.parametrize("module", RUNTIME_MODULES)
    def test_runtime_imports_no_engine_module_and_no_unicode_or_regex(self, module):
        imported = set(_imports(IR_DIR / module))
        assert imported <= ALLOWED_IMPORTS, imported - ALLOWED_IMPORTS

    def test_the_check_sees_a_forbidden_import(self, tmp_path):
        probe = tmp_path / "probe.py"
        probe.write_text("import unicodedata\nfrom orthography2ipa.stress import detect_stress\n")
        assert set(_imports(probe)) - ALLOWED_IMPORTS == {"unicodedata", "orthography2ipa.stress"}


class TestCanonicalForm:
    def test_strings_are_sorted_codepoint_arrays_with_the_empty_string_first(self, pt_doc):
        strings = pt_doc["strings"]
        assert strings[0] == []
        assert strings == sorted(strings)
        assert len({tuple(s) for s in strings}) == len(strings)

    def test_entries_sorted_by_key_codepoints(self, pt_doc):
        keys = [pt_doc["strings"][e["key"]] for e in pt_doc["entries"]]
        assert keys == sorted(keys)

    def test_runtime_part_holds_no_data_string(self, pt_doc):
        vocabulary = set()
        for table in (layout._SLOT_ARGS, layout._GATE_ARGS, layout._DPRED_ARGS):
            vocabulary |= set(table)
        vocabulary |= {"has_stress", "idx_eq_stressed", "idx_lt_stressed", "idx_gt_stressed",
                       "idx_eq_stressed_minus_1", "idx_in_secondary", "coda", "onset", "nucleus",
                       "lit", "group", "any", "set", "bol", "eol", "seq", "alt", "opt", "star",
                       "plus", "ahead", "behind"}
        found = set()

        def walk(v):
            if isinstance(v, str):
                found.add(v)
            elif isinstance(v, list):
                for x in v:
                    walk(x)
            elif isinstance(v, dict):
                for x in v.values():
                    walk(x)
        walk({k: v for k, v in pt_doc.items() if k in layout.RUNTIME_FIELDS})
        assert found <= vocabulary, found - vocabulary

    def test_json_round_trip_gives_the_same_transcriptions(self, pt_ir, pt_doc):
        doc = json.loads(json.dumps(pt_doc))
        readable, loaded = Interpreter(pt_ir), Interpreter(doc)
        for text in ("os jogos", "Disse-lhe que não, obrigado!", "guarda-chuva", "rainha"):
            assert loaded.transcribe(text) == readable.transcribe(text)

    def test_predicate_normal_form(self):
        p = ["and", ["true"], ["and", ["exists", 1], ["exists", -1]], ["not", ["not", ["exists", 1]]]]
        assert layout._normal(p, layout._SLOT_ARGS) == ["and", ["exists", -1], ["exists", 1]]


class TestRevision:
    def test_equal_irs_hash_equal(self, pt_ir):
        assert layout.spec_revision(pt_ir) == layout.spec_revision(build_ir("pt-PT"))

    def test_an_output_relevant_change_moves_the_revision(self, pt_ir):
        changed = json.loads(json.dumps(layout.encode(pt_ir)))
        strings = changed["strings"]
        z = next(e for e in changed["entries"] if strings[e["key"]] == [ord("z")])
        changed["strings"].append([ord("ð")])
        z["cands"] = [len(strings) - 1]
        before, after = Interpreter(pt_ir).transcribe("zebra"), Interpreter(changed).transcribe("zebra")
        assert before != after
        moved = layout.decode(changed)
        assert layout.spec_revision(moved) != layout.spec_revision(pt_ir)

    def test_a_primitive_version_moves_the_revision(self, pt_ir, monkeypatch):
        before = layout.spec_revision(pt_ir)
        monkeypatch.setitem(layout.SEMANTICS, "beam", 2)
        assert layout.spec_revision(pt_ir) != before

    def test_a_dialect_profile_is_part_of_the_revision(self, pt_ir):
        porto = build_ir("pt-PT", dialect_profile="porto")
        assert layout.spec_revision(porto) != layout.spec_revision(pt_ir)


    def test_the_bit_name_table_is_part_of_the_revision(self, pt_ir):
        swapped = dict(pt_ir, bits=dict(pt_ir["bits"]))
        names = list(swapped["bits"]["char"])
        names[0], names[1] = names[1], names[0]
        swapped["bits"]["char"] = names
        text = "o rapaz comeu as maçãs"
        assert Interpreter(swapped).transcribe(text) != Interpreter(pt_ir).transcribe(text)
        assert layout.spec_revision(swapped) != layout.spec_revision(pt_ir)

    def test_bit_names_are_unique(self, pt_ir):
        for kind, names in pt_ir["bits"].items():
            assert len(names) == len(set(names)), kind

    def test_syll_relations_are_versioned_in_the_manifest(self, pt_ir):
        relations = {n for n in layout.manifest(pt_ir).split(";") if n.startswith("syll.")}
        runtime = json.dumps({k: v for k, v in pt_ir.items() if k != "debug"}, ensure_ascii=False)
        used = set(re.findall(r'\["syll", "(\w+)"\]', runtime))
        assert len(used) >= 3
        assert relations == {f"syll.{r}=1" for r in used}

    def test_an_unknown_syll_relation_is_refused(self, pt_ir):
        interp = Interpreter(pt_ir)
        ctx = type("Ctx", (), {"syll_idx": [0], "stressed": 0, "secondary": ()})()
        with pytest.raises(ValueError, match="unknown syll relation 'idx_typo_stressed'"):
            interp._syll("idx_typo_stressed", ctx, 0)


class TestPatterns:
    def _sandhi_patterns(self):
        seen = set()
        for code in available_codes():
            try:
                spec = get(code)
            except Exception:
                continue
            for rule in spec.sandhi_rules:
                seen.update((rule.left_context, rule.right_context))
        return sorted(seen)

    def test_every_sandhi_pattern_matches_like_re(self):
        patterns = self._sandhi_patterns()
        assert len(patterns) >= 90
        alphabet = sorted({c for p in patterns for c in p if c.isalpha() or ord(c) > 0x2B0} | set("ˈˌaeiouə"))
        samples = ["", "ʃ", "ˈʒɔɡuʃ", "els", "el", "kə", "mbi", "ˈbiɨ̃", "pɐ̃w̃"]
        samples += [alphabet[i:i + 4] for i in range(0, len(alphabet), 3)]
        samples = ["".join(s) for s in samples]
        for text in patterns:
            node = compile_pattern(text)
            rx = re.compile(text)
            for s in samples:
                m = rx.search(s)
                got = pattern.search(node, [ord(c) for c in s], 0, pattern.group_count(node))
                assert (m is None) == (got is None), (text, s)
                if m:
                    assert (m.start(), m.end()) == got[:2], (text, s)

    def test_sub_with_groups_like_re(self):
        text, template = r"([aeiouəɛɔɐ])[sʃ]$", r"\1z"
        node, tpl = compile_pattern(text), compile_template(template)
        strings = [[ord(c) for c in p[1]] for p in tpl if p[0] == "lit"]
        parts = [["lit", 0] if p[0] == "lit" else p for p in tpl]
        for s in ("ˈkazɐʃ", "uʃ", "ʃ", "ɐs"):
            got = "".join(map(chr, pattern.sub(node, parts, [ord(c) for c in s], strings)))
            assert got == re.sub(text, template, s)


class TestConformance:
    def test_os_jogos(self, pt_ir):
        assert [ord(c) for c in Interpreter(pt_ir).transcribe("os jogos")] == \
            [117, 32, 712, 658, 596, 609, 117, 643]

    def test_unknown_primitive_version_is_refused(self, pt_doc):
        doc = dict(pt_doc, primitives=dict(pt_doc["primitives"], beam=99))
        with pytest.raises(IRVersionError, match="unsupported primitive version: beam"):
            Interpreter(doc)

    def test_unknown_ir_version_is_refused(self, pt_doc):
        with pytest.raises(IRVersionError):
            Interpreter(dict(pt_doc, ir_version=2))


def _dialect_rows():
    with DIALECT_CSV.open(encoding="utf-8") as f:
        return [row["text"] for row in csv.DictReader(f)]


@pytest.mark.parametrize("profile", sorted(DIALECT_PROFILES))
def test_dialect_profile_byte_parity(profile):
    texts = _dialect_rows()
    assert len(texts) == 235
    legacy = FrozenRules("pt-PT", dialect_profile=profile)
    it = Interpreter(build_ir("pt-PT", dialect_profile=profile))
    diffs = [(t, legacy.transcribe(t), it.transcribe(t)) for t in texts
             if legacy.transcribe(t) != it.transcribe(t)]
    assert diffs == []


class TestDialectTargeted:
    """Targeted cases of section 8.4, each checked against the legacy transform."""

    @pytest.fixture(scope="class")
    def runner(self):
        from orthography2ipa.ir.dialect import run_program
        from orthography2ipa.ir.compiler import _dialect_program
        from orthography2ipa.transforms import apply_transform
        base = Interpreter(build_ir("pt-PT"))

        def run(profile, ipa, ortho):
            got = run_program(base, _dialect_program(profile, False), ipa, ortho)
            return got, apply_transform(ipa, profile, ortho=ortho)
        return run

    @pytest.mark.parametrize("profile,ipa,ortho", [
        ("rionorese", "u ˈʒɔɡu", "O jogo"),           # lexical rule through a capitalised word
        ("rionorese", "u ˈʒɔɡu ˈmaɪ", "o jogo"),      # word counts differ
        ("guadramilese", "ˈew ˈvow", "eu vou"),        # lexical rule
        ("lisbon", "ˈɐj ɐj", ""),                     # empty spelling
        ("algarve_barlavento", "ˈkazɐ ˈpɔtu", "casa pôto"),  # chain shift
        ("porto", "ˈpɛɾtu ˈeɾɐ", "perto era"),
        ("transmontano", "ˈsaʃ ˈpɔʃ", "sás pós"),
    ])
    def test_matches_legacy(self, runner, profile, ipa, ortho):
        got, legacy = runner(profile, ipa, ortho)
        assert got == legacy


def _random_pattern(rng, depth=0):
    atoms = ["a", "b", ".", "[ab]", "[^a]", "\\n", "^", "$"]
    kind = rng.randrange(7 if depth < 3 else 1)
    if kind == 0:
        return rng.choice(atoms)
    if kind == 1:
        return _random_pattern(rng, depth + 1) + _random_pattern(rng, depth + 1)
    if kind == 2:
        return _random_pattern(rng, depth + 1) + "|" + rng.choice(["", _random_pattern(rng, depth + 1)])
    if kind == 3:
        return "(" + _random_pattern(rng, depth + 1) + ")"
    if kind == 4:
        return "(?:" + _random_pattern(rng, depth + 1) + ")" + rng.choice("*+?")
    if kind == 5:
        return "(" + _random_pattern(rng, depth + 1) + ")" + rng.choice("*+?")
    return rng.choice(["(?=", "(?!"]) + _random_pattern(rng, depth + 1) + ")" + rng.choice(["", "+", "*"])


class TestPatternFuzz:
    """Every pattern the compiler accepts behaves exactly as ``re``."""

    def test_accepted_patterns_match_and_sub_like_re(self):
        import random
        from orthography2ipa.ir.compile_patterns import PatternOutsideSubset
        rng = random.Random(2482)
        texts = ["".join(rng.choice("ab\n") for _ in range(rng.randrange(7))) for _ in range(40)]
        accepted = diffs = 0
        for _ in range(4000):
            text = _random_pattern(rng)
            try:
                rx = re.compile(text)
            except re.error:
                continue
            try:
                node = compile_pattern(text)
            except PatternOutsideSubset:
                continue
            accepted += 1
            ngroups = rx.groups
            template = "<" + "".join(f"\\{g}" for g in range(1, ngroups + 1)) + ">"
            tpl = compile_template(template)
            strings = [[ord(c) for c in p[1]] for p in tpl if p[0] == "lit"]
            parts, n = [], 0
            for p in tpl:
                if p[0] == "lit":
                    parts.append(["lit", n])
                    n += 1
                else:
                    parts.append(p)
            for s in texts:
                cps = [ord(c) for c in s]
                m = rx.search(s)
                got = pattern.search(node, cps, 0, pattern.group_count(node))
                want = None if m is None else (m.start(), m.end(), tuple(m.span(g) if m.group(g) is not None else None
                                                                          for g in range(1, ngroups + 1)))
                have = None if got is None else (got[0], got[1], tuple(got[2][1:ngroups + 1]))
                subbed = "".join(map(chr, pattern.sub(node, parts, cps, strings)))
                if want != have or subbed != rx.sub(template, s):
                    diffs += 1
                    assert (text, s, want, subbed) == (text, s, have, rx.sub(template, s))
        assert accepted >= 1000
        assert diffs == 0


class TestNeighbourhoodNodes:
    """``count`` and ``word_has_entry`` of section 2.5, on "casa"."""

    @pytest.fixture(scope="class")
    def run(self, pt_ir):
        interp = Interpreter(pt_ir)
        ctx = type("Ctx", (), {})()
        ctx.entries = [interp._key_index[k] for k in ("c", "a", "s", "a")]
        ctx.cands = [[("k", 0)], [("a", 0)], [("z", 0)], [("ɐ", 0)]]
        ctx.source = "casa"
        return lambda p, i: interp._eval(p, ctx, i)

    def test_count_over_a_range(self, run):
        vowel_a = ["entry_in", 0, ["a"]]
        assert run(["count", "start", "end", vowel_a, 2], 0) is True
        assert run(["count", "start", "end", vowel_a, 3], 0) is False
        assert run(["count", 1, "end", vowel_a, 2], 1) is False
        assert run(["count", 1, "end", vowel_a, 1], 1) is True
        assert run(["count", -5, 5, vowel_a, 2], 2) is True

    def test_count_others_skips_slot_i(self, run):
        vowel_a = ["entry_in", 0, ["a"]]
        assert run(["count", "start", "end", vowel_a, 2, "others"], 1) is False
        assert run(["count", "start", "end", vowel_a, 1, "others"], 1) is True

    def test_word_has_entry(self, run):
        assert run(["word_has_entry", ["s"]], 0) is True
        assert run(["word_has_entry", ["ç"]], 0) is False


class TestCompileTime:
    def test_atom_match_is_the_longest_unfollowed_atom(self):
        import random
        from orthography2ipa.allophony import _is_modifier, _match_atom
        from orthography2ipa.stress import _MARK_ATOMS

        def reference(ipa, start, atoms):
            longest = None
            for atom in atoms:
                end = start + len(atom)
                if ipa.startswith(atom, start) and not (end < len(ipa) and _is_modifier(ipa[end])):
                    if longest is None or len(atom) > len(longest):
                        longest = atom
            return longest

        atoms = ("t", "tʃ", "tʃʰ", "d", "dʒ", "ʃ", "k", "kʰ", "ts", "s") + tuple(_MARK_ATOMS)
        alphabet = sorted({c for a in atoms for c in a} | {"ʰ", "ʲ", "ː", "a", "̃"})
        rng = random.Random(7)
        checked = 0
        for _ in range(3000):
            s = "".join(rng.choice(alphabet) for _ in range(rng.randrange(1, 7)))
            for i in range(len(s)):
                assert _match_atom(s, i, atoms) == reference(s, i, atoms), (s, i)
                checked += 1
        assert checked > 9000

    def test_uk_compiles_within_three_cpu_minutes(self):
        # CPU time, not wall time, so a loaded machine does not fail the test.
        # The compile takes about one CPU minute; the bound leaves three times that.
        import time
        from orthography2ipa.ir import compiler
        t0 = time.process_time()
        compiler._base_ir.__wrapped__("uk", None, True, True, True, False)
        assert time.process_time() - t0 < 180


class TestOnsetTable:
    def test_a_declared_cluster_longer_than_every_licit_shorter_run_is_kept(self):
        from orthography2ipa.ir.compiler import _onset_table

        class Judge:
            MAX_MEMBERS = 3
            max_onset = None
            _onsets = frozenset({"stra"})

            def graphemes_of(self, run):
                return list(run)

            def _licit(self, run):
                return run == "stra"

        assert _onset_table(Judge(), "astr", ["stra"]) == [["s", "t", "r", "a"]]


class TestPrepareRewrites:
    @pytest.mark.parametrize("code,text", [
        ("ayl", "عَمَّ رَبٌّ"), ("ayl", "مُدَّرِّس"), ("fa", "\ufef7\ufe8e"),
    ])
    def test_prepare_like_legacy(self, code, text):
        from orthography2ipa.phonetok import PhonetokTokenizer
        legacy = PhonetokTokenizer(get(code)).prepare(text)
        assert Interpreter(build_ir(code)).prepare(text) == legacy
        assert legacy != text

    def test_the_addak_rewrite_like_legacy(self):
        from orthography2ipa.ir.compiler import _prepare_rewrites
        from orthography2ipa.phonetok import PhonetokTokenizer
        tok = PhonetokTokenizer(get("pa"))
        _, rewrites = _prepare_rewrites(get("pa"), tok._grapheme_ipa)
        text = "ਪੱਗ ਸੱਚ ਅੱਖ਼"
        out = text
        for rw in rewrites:
            out = Interpreter._sub(rw["pattern"], rw["template"], [ord(c) for c in out])
        assert out == tok.prepare(text) != text


class TestOutputNFC:
    def test_a_nasal_vowel_built_from_two_readings_is_composed(self):
        out = Interpreter(build_ir("ur")).transcribe("باں")
        assert [ord(c) for c in out] == [0x62, 0xE3, 0x2D0]


class TestScriptPause:
    def test_the_arabic_comma_blocks_sandhi_like_the_ascii_one(self):
        """The Arabic comma is a pause, so the article keeps its hamzat wasl."""
        interp = Interpreter(build_ir("arb"))
        assert interp.transcribe("\u0641\u0650\u064a \u0627\u0644\u0628\u064e\u064a\u0652\u062a\u0650") == "fi\u02d0 l\u02c8bajti"
        assert interp.transcribe("\u0641\u0650\u064a\u060c \u0627\u0644\u0628\u064e\u064a\u0652\u062a\u0650") == "fi\u02d0 al\u02c8bajti"
        assert interp.transcribe("\u0641\u0650\u064a, \u0627\u0644\u0628\u064e\u064a\u0652\u062a\u0650") == "fi\u02d0 al\u02c8bajti"


class TestGrammaticalEndings:
    @pytest.mark.parametrize("code,words", [
        ("ru", ["большого", "самого", "красного", "моего"]),
        ("ru-x-pskov", ["ничего", "чего", "большого"]),
    ])
    def test_ending_words_like_legacy(self, code, words):
        interp, g = Interpreter(build_ir(code)), FrozenRules(code)
        assert [interp.transcribe(w) for w in words] == [g.transcribe(w) for w in words]


class TestInherentVowel:
    @pytest.mark.parametrize("code,words", [
        ("hi", ["कमल", "क़लम", "प्यार", "चिन्ह"]),
        ("bo", ["ཁ་འདབ", "ཀྲ", "གསུམ", "ཁམས"]),
        ("ta", ["அகங்காரம்", "அகத்தமிழ்"]),
        ("pa", ["ਪੱਗ", "ਸੱਚ"]),
    ])
    def test_abugida_words_like_legacy(self, code, words):
        interp, g = Interpreter(build_ir(code)), FrozenRules(code)
        assert [interp.transcribe(w) for w in words] == [g.transcribe(w) for w in words]


class TestPreposedVowels:
    # Thai and Lao write ⟨เ แ โ ใ ไ⟩ before the consonant they follow: ⟨เก⟩ is /keː/ (Smyth 2002).
    @pytest.mark.parametrize("code,words", [
        ("th", ["เก", "ไหม", "โหม", "โหมด", "แหล่", "เหลือ", "เอกชน", "คลอโรฟอร์ม"]),
        ("lo", ["ເອກ", "ເຫຼົ້າ", "ໂຫລ", "ເມືອງ"]),
    ])
    def test_tokens_like_legacy(self, code, words):
        from orthography2ipa import registry
        from orthography2ipa.phonetok import PhonetokTokenizer
        interp, legacy = Interpreter(build_ir(code, apply_stress=False)), PhonetokTokenizer(registry.get(code))
        for w in words:
            assert [(t.grapheme, t.readings) for t in interp.grapheme_tokens(w)] == \
                [(t.grapheme, tuple(t.ipa)) for t in legacy.tokenize(w) if t.kind.name == "GRAPHEME"]

    def test_host_is_no_coda(self):
        interp = Interpreter(build_ir("th", apply_stress=False))
        assert interp._word_paths("เก", 1)[0][0] == ("keː",)


class TestComputedTone:
    # Thai tone follows the initial's class, the rime's shape and the mark (Slayden 2009 § 6).
    def test_thai_words_like_legacy(self):
        words = ["เป็นต้อง", "ก่อน", "ขวด", "ไหม", "นก"]
        interp, g = Interpreter(build_ir("th")), FrozenRules("th")
        assert [interp.transcribe(w) for w in words] == [g.transcribe(w) for w in words]
        assert interp.transcribe("นก") == "nok̚˦˥"


class TestConsonantNuclei:
    # Lao ⟨ວ⟩ between an onset and a coda is the nucleus /uːə/: ⟨ພວກ⟩ is /pʰuːək̚/ (Enfield 2007).
    def test_lao_words_like_legacy(self):
        words = ["ໜ່ວຍ", "ຊວງ", "ພວກ", "ດວງຈິດ", "ຂອງພວກເຮົາ"]
        interp, g = Interpreter(build_ir("lo")), FrozenRules("lo")
        assert [interp.transcribe(w) for w in words] == [g.transcribe(w) for w in words]

    def test_thai_cluster_backs_off(self):
        # ⟨ขว⟩ is a cluster in ⟨ขวา⟩, but ⟨ว⟩ is the nucleus of ⟨ขวด⟩.
        from orthography2ipa import registry
        from orthography2ipa.phonetok import PhonetokTokenizer
        interp, legacy = Interpreter(build_ir("th", apply_stress=False)), PhonetokTokenizer(registry.get("th"))
        for w in ["ขวด", "ขวา", "สวน"]:
            assert [(t.grapheme, t.readings) for t in interp.grapheme_tokens(w)] == \
                [(t.grapheme, tuple(t.ipa)) for t in legacy.tokenize(w) if t.kind.name == "GRAPHEME"]


class TestDependentVowels:
    # A Burmese rhyme is one written unit that carries the nucleus: ⟨ကန်⟩ is [kàɴ] (Okell 1969).
    @pytest.mark.parametrize("code,words", [
        ("my", ["ကန်", "မြန်မာ", "ကောင်း", "သိုး"]),
        ("new", ["नेपाय्", "कँय्", "तँय्", "गंल्वय्"]),
    ])
    def test_words_like_legacy(self, code, words):
        interp, g = Interpreter(build_ir(code)), FrozenRules(code)
        assert [interp.transcribe(w) for w in words] == [g.transcribe(w) for w in words]


class TestViramaFinalVowel:
    # Malayalam samvrutokaram: a word-final virama reads /ɨ/ (Asher & Kumari 1997 § 3.1.1.2).
    def test_malayalam_words_like_legacy(self):
        words = ["അവന്", "കണ്ണ്", "ആറ്റ്", "പാല്", "മലയാളം"]
        interp, g = Interpreter(build_ir("ml")), FrozenRules("ml")
        assert [interp.transcribe(w) for w in words] == [g.transcribe(w) for w in words]
        assert interp.transcribe("പാല്") == "paːlɨ"


class TestWeightStress:
    # Ryding 2005 § 2.3: superheavy final, heavy penult, else the antepenult.
    @pytest.mark.parametrize("word,ipa", [
        ("كِتَاب", "kiˈtaːb"), ("مُدَرِّس", "muˈdarris"),
        ("مَدْرَسَة", "ˈmadrasa"), ("كَتَبَ", "ˈkataba"),
    ])
    def test_arabic_cascade(self, word, ipa):
        assert Interpreter(build_ir("ar")).transcribe(word) == ipa

    @pytest.mark.parametrize("code,words", [
        ("arz-EG", ["مدرسة", "كتاب", "بيت"]),
        ("ary-MA", ["مدرسة", "كتاب"]),
    ])
    def test_weight_words_like_legacy(self, code, words):
        interp, g = Interpreter(build_ir(code)), FrozenRules(code)
        assert [interp.transcribe(w) for w in words] == [g.transcribe(w) for w in words]


class TestWrittenOnsets:
    # The homorganic /tl/ gap keeps Bret|land (stress.py _two_member).
    def test_tl_gap(self):
        assert Interpreter(build_ir("de-DE")).syllables("Bretland") == ["Bret", "land"]

    @pytest.mark.parametrize("code,words", [
        ("de-DE", ["Fenster", "Abstand", "Monster", "Erdbeere", "Wasser"]),
        ("de-x-alemanni", ["Fenster", "Abstand", "Kinder"]),
    ])
    def test_syllables_like_legacy(self, code, words):
        interp, g = Interpreter(build_ir(code)), FrozenRules(code)
        assert [interp.syllables(w) for w in words] == [g._syllables_cached(w) for w in words]
        assert [interp.transcribe(w) for w in words] == [g.transcribe(w) for w in words]


class TestVowelLetters:
    # Yiddish writes its vowels with letters a Hebrew-script test reads as consonants.
    @pytest.mark.parametrize("word,sylls", [
        ("שולע", ["שו", "לע"]), ("מאַמע", ["מאַ", "מע"]), ("בוך", ["בוך"]),
    ])
    def test_yiddish_nuclei(self, word, sylls):
        assert Interpreter(build_ir("yi")).syllables(word) == sylls

    @pytest.mark.parametrize("code,words", [("ast", ["fíu", "muyer", "güeyu"]), ("zu", ["umuntu", "inkomo"])])
    def test_words_like_legacy(self, code, words):
        interp, g = Interpreter(build_ir(code)), FrozenRules(code)
        assert [interp.transcribe(w) for w in words] == [g.transcribe(w) for w in words]


class TestSecondaryStress:
    # Alternating feet leftward from the main stress (Hayes 1995 ch. 3).
    @pytest.mark.parametrize("word,ipa", [("information", "ˌɪnfəˈmæʃən"), ("examination", "ɛkˌsæmɪˈnæʃən")])
    def test_english_feet(self, word, ipa):
        assert Interpreter(build_ir("en-GB")).transcribe(word) == ipa


class TestAperture:
    # Loi de position: a closed syllable opens the mid vowel, after the mute final e merges.
    @pytest.mark.parametrize("word,ipa", [("jeune", "ʒœn"), ("jeu", "ʒø"), ("heure", "œʁ"), ("peu", "pø")])
    def test_french_mid_vowels(self, word, ipa):
        assert Interpreter(build_ir("fr-FR")).transcribe(word) == ipa


class TestNucleusConditions:
    # A silent final e of a word with no other nucleus reads /iː/.
    @pytest.mark.parametrize("word,ipa", [("be", "ˈbiː"), ("me", "ˈmiː")])
    def test_english_lone_e(self, word, ipa):
        assert Interpreter(build_ir("en-GB")).transcribe(word) == ipa

    @pytest.mark.parametrize("code,words", [
        ("pt-BR", ["cidade", "leite", "também", "cantam"]), ("fr-FR", ["le", "je", "premier"]),
    ])
    def test_words_like_legacy(self, code, words):
        interp, g = Interpreter(build_ir(code)), FrozenRules(code)
        assert [interp.transcribe(w) for w in words] == [g.transcribe(w) for w in words]


@pytest.mark.parametrize("code,entries", [
    ("ar", {"weight=1"}), ("de-DE", {"written_onsets=1"}), ("yi", {"vowel_letters=1"}),
    ("en-GB", {"secondary=1", "node.top_nucleus=1", "syll.closed=1"}),
    ("fr-FR", {"aperture=1", "syll.closed=1", "node.top_nucleus=1"}),
])
def test_lifted_manifest_entries(code, entries):
    assert entries <= set(layout.manifest(build_ir(code)).split(";"))


def _schema_lines(t, path=""):
    kind = t[0] if isinstance(t, tuple) else None
    if kind == "obj":
        out = [f"{path}: object"] if path else []
        for k, v in t[1].items():
            out += _schema_lines(v, f"{path}.{k}" if path else k)
        return out
    if kind == "list":
        inner = _schema_lines(t[1], path + "[]")
        head = inner[0].split(": ", 1)[1]
        return [f"{path}: list of {head}"] + inner[1:]
    if kind == "pair":
        a, b = (_schema_lines(x, "x")[0].split(": ", 1)[1] for x in t[1:])
        return [f"{path}: pair of {a} and {b}"]
    return [f"{path}: {t}"]


def test_spec_schema_is_the_layout():
    doc = (Path(__file__).parent.parent / "docs/ir/o2i-ir-v1.md").read_text(encoding="utf-8")
    block = doc.split("<!-- layout-schema:begin -->\n```\n")[1].split("\n```\n<!-- layout-schema:end -->")[0]
    assert block.split("\n") == _schema_lines(layout.LAYOUT)


def test_spec_bit_tables_are_the_compiler_bits():
    from orthography2ipa.ir.compiler import CHAR_BITS, ENTRY_BITS
    doc = (Path(__file__).parent.parent / "docs/ir/o2i-ir-v1.md").read_text(encoding="utf-8")
    section = doc.split("### 2.4 Attribute bits")[1].split("### 2.5")[0]
    chars, entries = section.split("Entry bits")

    def names(text, order):
        out = []
        for row in re.findall(r"^\| [\d.]+ \| (.+?) \|", text, re.M):
            first, *last = re.findall(r"`(\w+)`", row)
            out += order[order.index(first):order.index(last[0]) + 1] if last else [first]
        return out
    assert names(chars, list(CHAR_BITS)) == list(CHAR_BITS)
    assert names(entries, list(ENTRY_BITS)) == list(ENTRY_BITS)


class TestPortGaps:
    def test_word_final_without_candidate_lists(self):
        from orthography2ipa.ir.interpreter import _Ctx
        interp = Interpreter(build_ir("pt-PT"))
        ctx = _Ctx(entries=[0, 0], tokens=[])
        assert [interp._eval(["word_final"], ctx, i) for i in (0, 1)] == [False, True]

    def test_dialect_sub_template_with_group(self):
        from orthography2ipa.ir.dialect import run_program
        step = {"gate": ["true"], "kind": "sub", "pattern": compile_pattern("(a)b"),
                "template": [["group", 1], ["lit", "x"]]}
        assert run_program(Interpreter(build_ir("pt-PT")), [step], "abab", "s") == "axax"

    def test_abugida_stress_counts_transcribed_syllables(self):
        # Khmer stress falls on the last syllable (Huffman 1970); the inherent vowels count.
        words = ["កករ", "កកិត", "កងយោធពល"]
        interp, g = Interpreter(build_ir("km")), FrozenRules("km")
        assert interp.ir["stress"]["ipa_count"] == 1
        assert [interp.transcribe(w) for w in words] == [g.transcribe(w) for w in words]


class TestUnstressedPrefixes:
    # Dutch be-, ver-, ge- never take the stress: be'talen, ver'kopen.
    @pytest.mark.parametrize("word,ipa", [("betalen", "bəˈtaːlən"), ("verkopen", "vəɹˈkoupən")])
    def test_dutch_prefix(self, word, ipa):
        assert Interpreter(build_ir("nl-NL")).transcribe(word) == ipa


class TestCodaLiquids:
    # A liquid before a consonant closes the syllable before it: buɾ|mejʎu.
    @pytest.mark.parametrize("word,ipa", [("burmeilho", "buɾˈmejʎu"), ("carga", "ˈkaɾɣɐ")])
    def test_mirandese_liquid(self, word, ipa):
        assert Interpreter(build_ir("mwl")).transcribe(word) == ipa

    def test_manifest(self):
        assert {"coda_liquid=1", "prefixes=1"} <= (
            set(layout.manifest(build_ir("mwl")).split(";")) | set(layout.manifest(build_ir("nl-NL")).split(";")))


class TestNeighbourMutation:
    # Romanian plural -i is non-syllabic and palatalizes the consonant before it.
    @pytest.mark.parametrize("word,ipa", [("lupi", "ˈlupʲ"), ("pomi", "ˈpomʲ")])
    def test_romanian_plural_i(self, word, ipa):
        assert Interpreter(build_ir("ro-RO")).transcribe(word) == ipa

    def test_manx_like_legacy(self):
        words = ["ben", "keeill", "thie", "ushtey"]
        assert [Interpreter(build_ir("gv")).transcribe(w) for w in words] == [FrozenRules("gv").transcribe(w) for w in words]


class TestAccent2:
    # Swedish disyllables in -a or -e stressed on the penult take accent 2.
    @pytest.mark.parametrize("word,ipa", [("flicka", "²flɪkːa"), ("gata", "²ɡɑːta"), ("bil", "ˈbiːl")])
    def test_swedish_accent2(self, word, ipa):
        assert Interpreter(build_ir("sv")).transcribe(word) == ipa


class TestFoldToneIambic:
    # Ancient Greek folds the written accents away before reading.
    def test_greek_fold(self):
        assert Interpreter(build_ir("grc")).transcribe("Άρτα") == "arta"

    # Kim Mun writes the tone after the vowel; it docks at the syllable end.
    def test_tone_docks_syllable_final(self):
        assert Interpreter(build_ir("kix")).transcribe("Chāmtāmōng") == "tʃʰam˧˧ta˧˧moŋ˧˧"

    # Carib lengthens the stressed vowel of each even iamb.
    def test_iambic_length(self):
        assert Interpreter(build_ir("car")).transcribe("ainapatoro") == "ainapaːtoˈɾo"


class TestGlideBackoffTurkic:
    # Limburgish ⟨ew⟩ gives its glide letter to the next syllable before a vowel.
    def test_prevocalic_glide_backoff(self):
        it = Interpreter(build_ir("li"))
        assert [t.grapheme for t in it.grapheme_tokens("geweun")] == ["g", "e", "w", "eu", "n"]

    # Turkish capital I is dotless ı, and capital İ is dotted i.
    @pytest.mark.parametrize("word,ipa", [("IRMAK", "ɯɾˈmak"), ("İSTANBUL", "istanˈbul")])
    def test_turkish_capitals(self, word, ipa):
        assert Interpreter(build_ir("tr")).transcribe(word) == ipa


@pytest.mark.parametrize("table,name", [("char", "virama"), ("entry", "glide_marker")])
def test_ir_lacking_a_bit_is_refused(table, name):
    ir = build_ir("ml")
    ir["bits"][table] = [n if n != name else name + "_renamed" for n in ir["bits"][table]]
    with pytest.raises(IRVersionError, match=name):
        Interpreter(ir)


def test_interpreter_bit_names_are_the_compiler_bits():
    from orthography2ipa.ir import compiler, interpreter
    assert interpreter._CHAR_NAMES == tuple(compiler.CHAR_BITS)
    assert interpreter._ENTRY_NAMES == tuple(compiler.ENTRY_BITS)


def test_revision_does_not_depend_on_hash_seed():
    script = ("import sys\nfrom orthography2ipa.ir.compiler import build_ir\nfrom orthography2ipa.ir import layout\n"
              "print(' '.join(layout.spec_revision(build_ir(c)) for c in sys.argv[1:]))")
    codes = ["pt-PT", "es-ES", "sv", "el", "ar", "kix", "ro"]
    revisions = {
        subprocess.run([sys.executable, "-I", "-c", script, *codes], capture_output=True, text=True, check=True,
                       env={**os.environ, "PYTHONHASHSEED": seed}).stdout
        for seed in ("1", "2", "3")}
    assert len(revisions) == 1


def test_transcription_revision(monkeypatch):
    from orthography2ipa import revision
    spec = revision.spec_revision("pt-PT")
    expected = lambda lexicon: "sha256:" + hashlib.sha256(f"{spec}\n{lexicon}".encode()).hexdigest()  # noqa: E731
    monkeypatch.setattr(revision, "lexicon_revision", lambda code, patches=False: f"sha256:lex{int(patches)}")
    assert revision.transcription_revision("pt-PT", patches=True) == expected("sha256:lex1")

    def missing(code, patches=False):
        raise LookupError(code)
    monkeypatch.setattr(revision, "lexicon_revision", missing)
    assert revision.transcription_revision("pt-PT") == expected("none")


def test_output_changing_fields_have_semantics_versions():
    names = set(layout.manifest(build_ir("pt-PT")).split(";"))
    assert {"collapse_geminates=1", "apostrophe_elision=1", "clitic_marks=1", "compound_last=1",
            "allophony_geminate=1", "tonic_after_diphthong=1", "hiatus=1", "overrides=1"} <= names
    assert "ipa_diphthongs=1" in layout.manifest(build_ir("it-IT")).split(";")
    assert "ipa_diphthongs=1" not in names
