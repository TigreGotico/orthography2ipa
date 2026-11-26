"""The o2i IR compiler: a resolved ``LanguageSpec`` in, an IR document out.

Every phonetic and Unicode question is asked here, once, and the answer is
written into the IR as a table, an attribute bit or a predicate
(docs/ir/o2i-ir-v1.md, sections 2 to 7). ``compile_spec(code)`` returns the
canonical JSON document (section 8.1); ``build_ir(code)`` returns the same IR
with plain Python strings.
"""
from __future__ import annotations

import hashlib
import io
import itertools
import json
import re
import subprocess
import tarfile
import tempfile
import unicodedata
from contextlib import contextmanager
from functools import lru_cache
from pathlib import Path
from typing import Callable, Dict, FrozenSet, Iterable, List, Optional, Sequence, Set, Tuple

import orthography2ipa.json_loader as json_loader
import orthography2ipa.registry as registry
from orthography2ipa.allophony import _applied, _is_modifier, _rule_atoms, segment_ipa
from orthography2ipa.g2p import _APOSTROPHES, _EDGE_PUNCT_CHAR, _HYPHENS, _VOWEL_IPA
from orthography2ipa.phonetok import (
    _DIGIT_RE, _ELISION_APOSTROPHES, _LENGTH_MARKS, _MAX_DECOMPOSED_COMBOS,
    _NASAL_CARRIERS, _NASAL_TILDE, _PUNCT_RE, _WS_RE, PAUSE_PUNCTUATION, PhonetokTokenizer,
    _AR_GEM_BARE, _AR_GEM_HARAKAT_FIRST, _AR_GEM_SHADDA_FIRST, _AR_SHADDA, _GURMUKHI_ADDAK,
    _GURMUKHI_VIRAMA, _ends_in_a_vowel, _is_a_mark, _is_nucleus, _is_subjoined_letter_cluster, _lower, lower_str)
from orthography2ipa.g2p import _UNSTRESSED_POSITIONS, _vowel_runs
from orthography2ipa.positional import _MAX_SILENT_TAIL, _silent_word_finally
from orthography2ipa.positional import (_AFTER_EXACT, _BEFORE_EXACT, _MUTE_E_CONSONANT_DIGRAPHS,
                                        _MUTE_E_INFLECTIONS, _TRANSPARENT_SUFFIX_GRAPHEMES,
                                        normalize_ending_value)
from orthography2ipa.stress import (
    _AFFRICATES, _GLIDES, _LIQUIDS, _MARK_ATOMS, _NON_SYLLABIC, _OFFGLIDES, SECONDARY_MARK, _IpaOnsetJudge, _ipa_judge,
    _judge_for, _semivowel_roles, cliticless_keys)
from orthography2ipa.transforms import (DIALECT_PROFILES, IPAChainShift, IPALexicalRule, IPARule,
                                        PALATAL_SET, VOWEL_SET)
from orthography2ipa.types import GraphemePosition as P
from orthography2ipa.types import LanguageSpec, ScriptType
from orthography2ipa.version import VERSION_STR
from orthography2ipa.vowels import (
    base_vowel_letter, grapheme_is_vowel, grapheme_vowel_axis, is_back_vowel,
    is_basic_vowel_letter, is_front_vowel, is_ipa_vowel, is_orthographic_vowel,
    IPA_VOWEL_SYMBOLS, SONORITY_GLIDE, SYLLABIC_MARKS, is_palatal_consonant, is_pharyngealized_consonant,
    sonority_class)
from orthography2ipa.weights import candidate_base_costs

from phonematcher import is_vowel_phone
from orthography2ipa.ir import layout, unidata
from orthography2ipa.tone import TONE_MARKS

__all__ = ["compile_spec", "build_ir", "IRUnsupportedFeature", "CHAR_BITS", "ENTRY_BITS"]

UNIDATA = unidata.VERSION


class IRUnsupportedFeature(NotImplementedError):
    """The spec uses a feature this compiler does not lower yet."""

    def __init__(self, code: str, feature: str):
        super().__init__(f"{code}: IR v1 compiler does not lower {feature}")
        self.code = code
        self.feature = feature


CHAR_BITS = (
    "known", "space", "punct", "digit", "alpha", "letter_or_mark", "combining", "mn_mc",
    "a_mark", "modifier", "orth_vowel", "ipa_vowel", "basic_vowel", "front_letter", "length",
    "non_syllabic", "glide", "offglide", "nasal_carrier", "apostrophe", "hyphen", "pause",
    "edge_punct", "word_letter", "elision_apostrophe", "virama", "vowel_ipa_set",
    "glide_head", "elision_h", "whitespace", "syllabic_mark", "mark_spells_nothing", "supplies_vowel",
    "vowel_phone", "nucleus_base", "syllabic", "liquid", "tone_mark",
)
ENTRY_BITS = (
    "vowel", "consonant", "front", "back", "palatal", "emphatic",
    "base_a", "base_e", "base_i", "base_o", "base_u", "base_y",
    "after_a", "after_e", "after_i", "after_o", "after_u", "after_front", "after_back",
    "silent_final", "transparent_final", "carries_nucleus", "spells_nothing",
    "multi_not_mute_digraph", "holds_vowel", "readings_hold_vowel", "orth_vowel_first",
    "glide_final_key", "fallback", "cluster_next", "cluster_prev", "coda_nasal_reading",
    "has_reading", "glide_vowel_cons", "glide_vowel_final", "glide_marker",
    "takes_inherent", "silent_before_consonant", "postvocalic", "vowel_inherent", "vowel_inherent_final",
    "vowel_sign", "preposed", "preposed_host", "preposed_open", "silent_head", "head_not_coda",
    "audible", "circumfix_tail", "vowel_nucleus",
    "prevocalic_backoff",
)
CB = {name: i for i, name in enumerate(CHAR_BITS)}
EB = {name: i for i, name in enumerate(ENTRY_BITS)}

_SCRIPT_NAMES = {"Latin": "LATIN", "Cyrillic": "CYRILLIC", "Greek": "GREEK"}
_FIXED_RANGES = ((0x20, 0x7E), (0xA0, 0xBF), (0x2000, 0x206F), (0x250, 0x2FF),
                 (0x300, 0x36F), (0x1D00, 0x1DBF))
_PUNCT_CHAR = re.compile(_PUNCT_RE.pattern[:-1])
_DIGIT_CHAR = re.compile(_DIGIT_RE.pattern[:-1])
_EDGE_CHAR = re.compile(_EDGE_PUNCT_CHAR)
_WORD_LETTER = re.compile(r"[^\W\d_]")
_NASALS = frozenset("mnɲŋɳɴ")

# The consonants that close a syllable in the "before r or closed syllable" context.
_DIALECT_C = "[bcdfɡhjklmnpqrstvwxzʃʒŋɲʎ]"


# ─── data_ref: older spec data through the current loader ────────────────
def _checkout() -> Optional[Path]:
    """The git checkout whose ``orthography2ipa/`` is this package, or ``None``."""
    package = Path(json_loader.__file__).resolve().parent
    try:
        top = subprocess.run(["git", "-C", str(package), "rev-parse", "--show-toplevel"],
                             check=True, capture_output=True, text=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None
    return Path(top) if (Path(top) / "orthography2ipa").resolve() == package else None


#: Extracted spec data per commit, kept for the life of the process.
_DATA_AT: Dict[str, tempfile.TemporaryDirectory] = {}


def _data_files(ref: str) -> Dict[str, Path]:
    """The spec files of *ref*, read with one ``git archive`` per commit."""
    repo = _checkout()
    if repo is None:
        raise RuntimeError(f"data_ref={ref!r} needs a git checkout of orthography2ipa; "
                           f"an installed package compiles only its own data")
    commit = subprocess.run(["git", "-C", str(repo), "rev-parse", f"{ref}^{{commit}}"],
                            check=True, capture_output=True, text=True).stdout.strip()
    if commit not in _DATA_AT:
        tar = subprocess.run(["git", "-C", str(repo), "archive", "--format=tar", commit,
                              "orthography2ipa/data/"], check=True, capture_output=True).stdout
        tmp = tempfile.TemporaryDirectory(prefix="o2i-ir-data-")
        with tarfile.open(fileobj=io.BytesIO(tar)) as archive:
            for member in archive.getmembers():
                name = Path(member.name).name
                if member.isfile() and name.endswith(".json"):
                    (Path(tmp.name) / name).write_bytes(archive.extractfile(member).read())
        _DATA_AT[commit] = tmp
    folder = Path(_DATA_AT[commit].name)
    return {path.name[:-5]: path for path in folder.iterdir()}


@contextmanager
def _data_at(ref: Optional[str]):
    if ref is None:
        yield
        return
    index = _data_files(ref)
    saved_index, saved_specs = dict(json_loader._index), dict(json_loader._specs)
    json_loader._index.clear()
    json_loader._index.update(index)
    json_loader._specs.clear()
    try:
        yield
    finally:
        json_loader._index.clear()
        json_loader._index.update(saved_index)
        json_loader._specs.clear()
        json_loader._specs.update(saved_specs)


def _git_head() -> str:
    repo = _checkout()
    if repo is None:
        return ""
    head = subprocess.run(["git", "-C", str(repo), "rev-parse", "--short=9", "HEAD"],
                          capture_output=True, text=True)
    return head.stdout.strip() if head.returncode == 0 else ""


# ─── characters ──────────────────────────────────────────────────────────
def _char_bits(c: str, elision: bool) -> int:
    cat = unidata.category(c)
    tests = {
        "known": True,
        "space": _WS_RE.match(c) is not None,
        "whitespace": c.isspace(),
        "punct": _PUNCT_CHAR.match(c) is not None,
        "digit": _DIGIT_CHAR.match(c) is not None,
        "alpha": cat[0] == "L",
        "letter_or_mark": cat[0] in "LM",
        "combining": unicodedata.combining(c) != 0,
        "mn_mc": cat in ("Mn", "Mc"),
        "a_mark": _is_a_mark(c),
        "modifier": _is_modifier(c),
        "orth_vowel": is_orthographic_vowel(c),
        "ipa_vowel": is_ipa_vowel(c),
        "basic_vowel": is_basic_vowel_letter(c),
        "front_letter": is_front_vowel(c),
        "length": c in _LENGTH_MARKS,
        "non_syllabic": c in _NON_SYLLABIC,
        "glide": c in _GLIDES,
        "offglide": c in _OFFGLIDES,
        "vowel_phone": is_vowel_phone(c),
        "nucleus_base": unicodedata.normalize("NFD", c)[0] in IPA_VOWEL_SYMBOLS,
        "syllabic": c in SYLLABIC_MARKS,
        "liquid": c in _LIQUIDS,
        "tone_mark": c in TONE_MARKS,
        "nasal_carrier": c in _NASAL_CARRIERS,
        "apostrophe": c in _APOSTROPHES,
        "hyphen": c in _HYPHENS,
        "pause": c in PAUSE_PUNCTUATION,
        "edge_punct": _EDGE_CHAR.match(c) is not None,
        "word_letter": _WORD_LETTER.match(c) is not None,
        "elision_apostrophe": elision and c in _ELISION_APOSTROPHES,
        "virama": unicodedata.combining(c) == 9,
        "vowel_ipa_set": c in _VOWEL_IPA,
        "glide_head": c in "jw",
        "elision_h": c in "hH",
    }
    return sum(1 << CB[name] for name, hit in tests.items() if hit)


@lru_cache(maxsize=None)
def _script_chars(script: str) -> FrozenSet[str]:
    return frozenset(chr(cp) for cp in range(0x110000)
                     if unidata.category(chr(cp))[0] in "LMNP"
                     and unicodedata.name(chr(cp), "").startswith(script + " "))


def _known_chars(spec: LanguageSpec, extra: Iterable[str]) -> Set[str]:
    chars: Set[str] = set()
    for text in extra:
        chars.update(text)
    for c in list(chars):
        chars.update(unicodedata.normalize("NFD", c))
        chars.update(x for x in c.upper() + c.lower() if unidata.assigned(x))
    script = _SCRIPT_NAMES.get(spec.script or "", (spec.script or "").upper())
    if script:
        chars |= _script_chars(script)
    for lo, hi in _FIXED_RANGES:
        chars.update(chr(cp) for cp in range(lo, hi + 1))
    chars.update(PAUSE_PUNCTUATION)
    return chars


# ─── entries ─────────────────────────────────────────────────────────────
def _micro(cost: float) -> int:
    return round(cost * 1_000_000)


def _entry_bits(key: str, readings: Tuple[str, ...], spec: LanguageSpec,
                positional_vowel_keys: Set[str], fallback: bool,
                table: Dict[str, Tuple[str, ...]]) -> int:
    vowel_overrides = spec.vowel_graphemes
    bits: Set[str] = set()
    is_vowel = grapheme_is_vowel(key, readings, vowel_overrides)
    if is_vowel:
        bits.add("vowel")
    elif key:
        bits.add("consonant")
    axis = grapheme_vowel_axis(key, readings, vowel_overrides)
    if axis == "front":
        bits.add("front")
    elif axis == "back":
        bits.add("back")
    if readings and is_palatal_consonant(readings[0]):
        bits.add("palatal")
    if readings and is_pharyngealized_consonant(readings[0]):
        bits.add("emphatic")
    if readings:
        bits.add("has_reading")
    exact = _BEFORE_EXACT.get(base_vowel_letter(key[0])) if key else None
    if exact is not None:
        bits.add("base_" + exact.value[len("before_"):])
    trailing = len(key) > 1 and key.lower() in {d.lower() for d in spec.trailing_vowel_axis_digraphs}
    tail = key[-1] if trailing else key[:1]
    after = _AFTER_EXACT.get(base_vowel_letter(tail)) if tail else None
    if after is not None:
        bits.add(after.value)
    if trailing and is_front_vowel(tail):
        bits.add("after_front")
    elif trailing and is_back_vowel(tail):
        bits.add("after_back")
    elif axis == "front":
        bits.add("after_front")
    elif axis == "back":
        bits.add("after_back")
    final = ((spec.positional_graphemes or {}).get(key) or {}).get(P.WORD_FINAL)
    silent_final = bool(final) and "" in final
    if silent_final:
        bits.add("silent_final")
    if silent_final and key in _TRANSPARENT_SUFFIX_GRAPHEMES:
        bits.add("transparent_final")
    primary = readings[0] if readings else ""
    if any(is_ipa_vowel(c) for c in primary):
        bits.add("carries_nucleus")
    if list(readings) == [""] and (
            _is_a_mark(key) if len(key) == 1 else
            (unidata.category(key[0]).startswith("L") or _is_a_mark(key[0]))
            and all(_is_a_mark(c) for c in key[1:])):
        bits.add("spells_nothing")
    if len(key) > 1 and key not in _MUTE_E_CONSONANT_DIGRAPHS:
        bits.add("multi_not_mute_digraph")
    if any(is_ipa_vowel(c) for r in readings for c in r) or key in positional_vowel_keys:
        bits.add("holds_vowel")
    positional = (spec.positional_graphemes or {}).get(key, {})
    if any(is_ipa_vowel(c) for r in (*readings, *(r for rs in positional.values() for r in rs or ()))
           for c in r):
        bits.add("readings_hold_vowel")
    if key and is_orthographic_vowel(key[0]):
        bits.add("orth_vowel_first")
    if fallback:
        bits.add("fallback")
    if not is_vowel and key:
        if "ː" in primary or len([s for s in segment_ipa(primary) if not is_ipa_vowel(s[0])]) >= 2:
            bits.add("cluster_next")
            bits.add("cluster_prev")
    if primary and primary[0] in _NASALS:
        bits.add("coda_nasal_reading")
    if (len(key) >= 2 and key[-1] in ("u", "i") and not is_orthographic_vowel(key[0])
            and key[:-1] in table and key[-1] in table):
        bits.add("glide_final_key")
        pg = (spec.positional_graphemes or {}).get(key) or {}
        for name, position in (("glide_vowel_cons", P.BEFORE_CONSONANT), ("glide_vowel_final", P.WORD_FINAL)):
            reading = pg.get(position)
            if reading is None:
                reading = pg.get(P.DEFAULT) or table.get(key)
            if reading and any(is_ipa_vowel(c) for c in reading[0]):
                bits.add(name)
        marker = pg.get(P.BEFORE_A) or pg.get(P.BEFORE_BACK_VOWEL)
        if marker and any(g in marker[0] for g in ("w", "j")):
            bits.add("glide_marker")
    if (key in {g.lower() for g in spec.prevocalic_glide_backoff}
            and key[:-1] in table and key[-1] in table):
        bits.add("prevocalic_backoff")
    return sum(1 << EB[name] for name in bits)


# ─── predicates ──────────────────────────────────────────────────────────
def _eb(k: int, name: str) -> list:
    return ["ebit", k, EB[name]]


def _not(p: list) -> list:
    return ["not", p]


def _and(*ps: list) -> list:
    return ["and", *ps]


def _or(*ps: list) -> list:
    return ["or", *ps]


def _EX(k):
    return ["exists", k]


def _V(k):
    return _eb(k, "vowel")


_N0 = _or(_V(0), _eb(0, "carries_nucleus"))


def _final_or_last_audible(k: int) -> list:
    """Slot i+k is the word's last slot, or the last before a silent suffix."""
    return _or(_and(_EX(k), _not(_EX(k + 1))),
               _and(_EX(k + 1), _not(_EX(k + 2)), _eb(k + 1, "transparent_final")))


def _positional_rules(spec: LanguageSpec, declared: Dict[P, List[str]]) -> List[list]:
    """The rules of one positional entry, in the order the positional pass applies them."""
    took_preposed = _and(_eb(-1, "preposed"), _not(["reading_vowel", -1]))
    has = _and(["syll", "has_stress"])
    eq = ["syll", "idx_eq_stressed"]
    sec = ["syll", "idx_in_secondary"]
    unstressed = _and(_not(eq), _not(sec))
    order: List[Tuple[P, list]] = [
        (P.BEFORE_FINAL_VOWEL, _and(_V(1), _eb(1, "silent_final"), _final_or_last_audible(1))),
    ]
    for letter in "aeiouy":
        order.append((P("before_" + letter), _eb(1, "base_" + letter)))
    order += [
        (P.BEFORE_FRONT_VOWEL, _eb(1, "front")),
        (P.BEFORE_BACK_VOWEL, _and(_not(_eb(1, "front")), _eb(1, "back"))),
        (P.BEFORE_PALATAL, _eb(1, "palatal")),
        (P.WORD_INITIAL, _not(_EX(-1))),
        (P.WORD_FINAL, _and(_not(_EX(1)), _not(took_preposed)) if spec.preposed_vowels else _not(_EX(1))),
        (P.INTERVOCALIC, _and(_V(-1), _V(1))),
        (P.NUCLEUS_STRESSED_OPEN, _and(_N0, ["syll", "open"], has, eq)),
        (P.NUCLEUS_STRESSED_CLOSED, _and(_N0, ["syll", "closed"], has, eq)),
        (P.NUCLEUS_UNSTRESSED_OPEN, _and(_N0, ["syll", "open"], has, unstressed)),
        (P.NUCLEUS_UNSTRESSED_CLOSED, _and(_N0, ["syll", "closed"], has, unstressed)),
        (P.OPEN_SYLLABLE, _and(_N0, ["syll", "open"])),
        (P.CLOSED_SYLLABLE, _and(_N0, ["syll", "closed"])),
        (P.NUCLEUS_STRESSED, _and(_N0, has, eq)),
        (P.NUCLEUS_SECONDARY, _and(_N0, has, _not(eq), sec)),
        (P.NUCLEUS_UNSTRESSED, _and(_N0, has, unstressed)),
        (P.FIRST_PRETONIC, _and(_N0, has, _not(eq), ["syll", "idx_eq_stressed_minus_1"])),
        (P.PRETONIC, _and(_N0, has, _not(eq), ["syll", "idx_lt_stressed"])),
        (P.POSTTONIC, _and(_N0, has, _not(eq), _not(["syll", "idx_lt_stressed"]))),
        (P.BEFORE_MUTE_E, _and(
            _V(0), ["entry_in", 2, ["e"]],
            _or(_not(_EX(3)), _and(_not(_EX(4)), ["entry_in", 3, sorted(_MUTE_E_INFLECTIONS)])),
            _EX(1), _not(_V(1)), _not(_eb(1, "multi_not_mute_digraph")))),
        (P.WORD_FINAL, _and(_EX(1), _not(_EX(2)), _eb(1, "transparent_final"), _EX(-1))),
    ]
    after_v = []
    for letter in "aeiou":
        after_v.append((P("after_" + letter), _and(_V(-1), _eb(-1, "after_" + letter))))
    after_v += [
        (P.AFTER_FRONT_VOWEL, _and(_V(-1), _eb(-1, "after_front"))),
        (P.AFTER_BACK_VOWEL, _and(_V(-1), _eb(-1, "after_back"))),
        (P.AFTER_PALATAL, _and(_V(-1), _eb(-1, "palatal"))),
        (P.AFTER_VOWEL, _V(-1)),
    ]
    order += after_v
    consonant = _and(_EX(-1), _not(_V(-1)))
    if spec.inherent_vowel:
        order.append((P.AFTER_VOWEL, _and(consonant, ["reading_vowel", -1])))
    order += [
        (P.AFTER_PALATAL, _and(consonant, _eb(-1, "palatal"))),
        (P.AFTER_CONSONANT, consonant),
        (P.BEFORE_VOWEL, _V(1)),
        (P.BEFORE_CONSONANT, _and(_EX(1), _not(_V(1)))),
        (P.NUCLEUS, _V(0)),
        (P.DEFAULT, ["true"]),
    ]
    return [[pred, list(declared[pos])] for pos, pred in order if pos in declared]


INERT_POSITIONS = (P.INTERVOCALIC_CROSS_WORD, P.ONSET, P.CODA, P.CONSONANTAL, P.VOCALIC)


# ─── allophony ───────────────────────────────────────────────────────────
def _neighbor(cls: str, k: int, code: str) -> list:
    step = 1 if k > 0 else -1
    if cls == "word_boundary":
        return _not(_EX(k))
    if cls == "any":
        return _EX(k)
    if cls in ("vowel", "consonant", "front_vowel", "back_vowel", "palatal", "emphatic"):
        name = {"front_vowel": "front", "back_vowel": "back"}.get(cls, cls)
        return _eb(k, name)
    if cls == "consonant_cluster":
        own = "cluster_next" if step > 0 else "cluster_prev"
        return _and(_eb(k, "consonant"), _or(_eb(k, own), _eb(k + step, "consonant")))
    if cls == "coda":
        return ["syllpos", k, "coda"]
    if cls == "coda_nasal":
        return _and(["syllpos", k, "coda"], _eb(k, "coda_nasal_reading"))
    raise IRUnsupportedFeature(code, f"allophone neighbour class {cls!r}")


def _allophone_rule(rule, spec: LanguageSpec, atoms: Sequence[str], keys: Dict[str, Tuple[str, ...]]) -> dict:
    code = spec.code
    slot: List[list] = []
    if rule.stress is not None:
        if rule.stress == "stressed":
            slot.append(_and(["syll", "has_stress"], ["syll", "idx_eq_stressed"]))
        elif rule.stress == "unstressed":
            slot.append(_and(["syll", "has_stress"], _not(["syll", "idx_eq_stressed"])))
        elif rule.stress == "pretonic":
            slot.append(_and(["syll", "has_stress"], ["syll", "idx_lt_stressed"]))
        else:
            slot.append(_and(["syll", "has_stress"], ["syll", "idx_gt_stressed"]))
    if rule.syllable_position is not None:
        slot.append(["syllpos", 0, rule.syllable_position])
    for name, k in (("preceded_by", -1), ("followed_by", 1), ("preceded_by_2", -2),
                    ("followed_by_2", 2), ("preceded_by_3", -3), ("followed_by_3", 3)):
        cls = getattr(rule, name)
        if cls is not None:
            slot.append(_neighbor(cls, k, code))
    for name, k, negate in (("preceded_by_grapheme", -1, False), ("followed_by_grapheme", 1, False),
                            ("followed_by_grapheme_not", 1, True)):
        wanted = getattr(rule, name)
        if wanted:
            hits = sorted(key for key in keys if key and key.lower() in wanted)
            test = _and(_EX(k), ["entry_in", k, hits])
            slot.append(_not(test) if negate else test)
    for name, k in (("preceded_by_phoneme_2", -2), ("followed_by_phoneme_2", 2)):
        wanted = getattr(rule, name)
        if wanted:
            hits = sorted(key for key, rs in keys.items()
                          if rs and rs[0] and segment_ipa(rs[0], atoms)[0] in wanted)
            slot.append(["entry_in", k, hits])
    if rule.preceded_by_surface_phoneme_2:
        slot.append(["top_seg_in", -2, 1, sorted(rule.preceded_by_surface_phoneme_2)])
    if rule.grapheme is not None:
        slot.append(["entry_in", 0, sorted(key for key in keys if key and key.lower() in rule.grapheme)])
    if rule.word_contains_grapheme:
        slot.append(["word_has", sorted(rule.word_contains_grapheme)])
    if rule.word_contains_grapheme_not:
        slot.append(_not(["word_has", sorted(rule.word_contains_grapheme_not)]))
    if rule.word is not None:
        slot.append(["word_in", sorted(rule.word)])
    for field, scope in (("requires_other_nucleus", "other"), ("followed_by_nucleus", "later")):
        wanted = getattr(rule, field)
        if wanted is not None:
            slot.append(["top_nucleus", scope] if wanted else _not(["top_nucleus", scope]))
    full: List[list] = []
    if rule.word_initial is not None:
        full.append(_not(_EX(-1)) if rule.word_initial else _EX(-1))
    if rule.word_final is not None:
        full.append(["word_final"] if rule.word_final else _not(["word_final"]))
    if rule.preceded_by_phoneme:
        full.append(["top_seg_in", -1, 1, sorted(rule.preceded_by_phoneme)])
    if rule.followed_by_phoneme:
        full.append(["top_seg_in", 1, 0, sorted(rule.followed_by_phoneme)])
    phonemes = list(rule.phonemes)
    aware = [any(n == p or n.startswith(p) for ctx in (rule.preceded_by_phoneme, rule.followed_by_phoneme)
                 for n in ctx) for p in phonemes]
    out = {
        "phonemes": phonemes,
        "out": [_applied(rule, p) for p in phonemes],
        "aware": [int(a) for a in aware],
        "when": _and(*full, *slot) if full or slot else ["true"],
        "slot_when": _and(*slot) if slot else ["true"],
        "trig_next": int(bool(rule.followed_by or rule.followed_by_grapheme or rule.followed_by_phoneme)),
        "trig_prev": int(bool(rule.preceded_by or rule.preceded_by_grapheme or rule.preceded_by_phoneme)),
    }
    if rule.mutates_neighbor:
        out["mutate"] = rule.mutates_neighbor
        out["mutate_at"] = 1 if rule.mutates_neighbor_side == "preceding" else -1
    if rule.preceded_by_phoneme or rule.followed_by_phoneme:
        out["seg"] = {
            "initial": -1 if rule.word_initial is None else int(rule.word_initial),
            "final": -1 if rule.word_final is None else int(rule.word_final),
            "prev": sorted(rule.preceded_by_phoneme or ()),
            "next": sorted(rule.followed_by_phoneme or ()),
        }
    return out


# ─── onset tables ────────────────────────────────────────────────────────
def _onset_table(judge, units: Sequence[str], declared: Sequence[str]) -> List[List[str]]:
    """Every unit sequence of two to five units that the judge licenses and that
    segments back to itself. Longer runs are searched only from licit shorter
    ones: a final glide, a palatal glide or /s/ appendix, or a declared cluster."""
    atoms = judge._atoms if isinstance(judge, _IpaOnsetJudge) else None
    reach = max(map(len, atoms), default=1) if atoms is not None else 0
    splits: Dict[Tuple[str, ...], bool] = {}

    def splits_into(c: Tuple[str, ...]) -> bool:
        """True if *c* joined segments back to *c*. For the IPA judge only the
        last *reach* characters are re-split."""
        if atoms is None or len(c) < 2:
            return judge.graphemes_of("".join(c)) == list(c)
        hit = splits.get(c)
        if hit is None:
            start, width = len(c) - 1, 0
            while start > 0 and width < reach:
                start -= 1
                width += len(c[start])
            hit = splits[c] = splits_into(c[:-1]) and segment_ipa("".join(c[start:]), atoms) == list(c[start:])
        return hit

    known: Dict[str, Tuple[str, ...]] = {}
    split = judge.graphemes_of

    def graphemes_of(run: str) -> List[str]:
        hit = known.get(run)
        return list(hit) if hit is not None else split(run)

    def keys(candidates: Iterable[Tuple[str, ...]]) -> Set[Tuple[str, ...]]:
        out = set()
        for c in candidates:
            if splits_into(c):
                run = "".join(c)
                known[run] = c
                if judge._licit(run):
                    out.add(c)
        return out

    if atoms is None:
        return _licit_onsets(judge, units, declared, atoms, keys)
    judge.graphemes_of = graphemes_of
    try:
        return _licit_onsets(judge, units, declared, atoms, keys)
    finally:
        judge.graphemes_of = split


def _licit_onsets(judge, units, declared, atoms, keys) -> List[List[str]]:
    licit = keys(itertools.product(units, repeat=2))
    layer = set(licit)
    unit_set = set(units)
    # The judge refuses a run longer than its cap, and without declared
    # clusters it refuses one of more than MAX_MEMBERS units.
    deepest = 5 if judge._onsets else judge.MAX_MEMBERS
    if judge.max_onset is not None:
        deepest = min(deepest, judge.max_onset)
    # The IPA judge with declared clusters licenses a longer run only when it
    # is declared, or when it ends in a glide on a licit run.
    glides_only = atoms is not None and bool(judge._onsets)
    tails = [u for u in units if (s := judge._segment(u)) is not None and sonority_class(s) == SONORITY_GLIDE] \
        if glides_only else units
    for depth in range(3, deepest + 1):
        candidates: Set[Tuple[str, ...]] = set()
        for seq in layer:
            for u in tails:
                candidates.add(seq + (u,))
            if depth == 3 and not glides_only:
                for u in units:
                    candidates.add((u,) + seq)
        for cluster in declared:
            parts = tuple(judge.graphemes_of(cluster))
            if len(parts) == depth and unit_set.issuperset(parts):
                candidates.add(parts)
        layer = keys(candidates)
        licit |= layer
    return sorted(list(t) for t in licit)


def _fast_split(judge) -> Callable[[str], List[str]]:
    """``judge.graphemes_of`` memoized, without a case fold: the onset candidates are lowercase."""
    split = judge.graphemes_of
    memo: Dict[str, List[str]] = {}

    def graphemes_of(run: str) -> List[str]:
        out = memo.get(run)
        if out is None:
            if lower_str(run, judge.code) != run:
                out = split(run)
            else:
                out, i = [], 0
                while i < len(run):
                    g = next((g for g in judge._graphemes if run.startswith(g, i)), run[i])
                    out.append(g)
                    i += len(g)
                    while i < len(run) and unicodedata.combining(run[i]):
                        out[-1] += run[i]
                        i += 1
            memo[run] = out
        return list(out)
    return graphemes_of


def _written_onsets(spec: LanguageSpec) -> dict:
    """The written onset judge of ``constrain_onsets`` as tables."""
    st = spec.stress
    judge = _judge_for(spec, st.max_onset if st is not None and st.max_onset_declared else None)
    units = sorted({g.lower() for g in spec.graphemes if g}, key=lambda g: (-len(g), g))
    judge.graphemes_of = _fast_split(judge)
    try:
        table = _onset_table(judge, units, st.onset_clusters if st is not None else ())
    finally:
        del judge.graphemes_of
    return {
        "max": -1 if judge.max_onset is None else judge.max_onset,
        "units": units,
        "velar": sorted(u for u in units if judge._opens_with_velar_nasal(u)),
        "table": table,
    }


# ─── dialect programs ────────────────────────────────────────────────────
def _dialect_program(name: str, spirants: bool) -> List[dict]:
    from orthography2ipa.ir.compile_patterns import compile_pattern
    profile = DIALECT_PROFILES[name]
    whitespace = sorted({" ", "\t", "\n"})
    stressed = ["back_reach", ["ˈ"], sorted(VOWEL_SET)]
    unstressed = _not(stressed)
    word_final = ["at_end_or_in", whitespace]
    r_c = ["ahead_match", 1, compile_pattern(f"[ɾr]{_DIALECT_C}")]
    contexts = {
        "stressed": stressed, "unstressed": unstressed, "word_final": word_final,
        "word_final_unstressed": _and(word_final, unstressed),
        "coda": ["at_in", -1, sorted(VOWEL_SET)],
        "stressed_and_before_r_or_closed_syllable": _and(stressed, r_c),
        "stressed_before_r_C": _and(stressed, r_c),
        "stressed_before_r_C_or_nasal_C": _and(stressed, _or(
            r_c, ["ahead_match", 1, compile_pattern(f"[mn]{_DIALECT_C}")])),
        "stressed_and_adjacent_to_palatal": _and(stressed, _or(
            ["at_in", -1, sorted(PALATAL_SET)], ["at_in", 1, sorted(PALATAL_SET)],
            ["covered_by", ["dʒ", "tʃ"]])),
        "unstressed_pretonic": _and(unstressed, ["later_has", ["ˈ"]]),
        "stressed_and_from_historical_ou": _and(["spell", ["spell_search", compile_pattern("ou")]], stressed),
        "ortho_has_ou": ["spell", ["spell_search", compile_pattern("ou")]],
        "ortho_source_is_ch": ["spell", ["spell_search", compile_pattern("ch")]],
        "ortho_source_is_z": ["spell", ["spell_search", compile_pattern("z")]],
        "ortho_source_is_ss_or_s": ["spell", ["spell_search", compile_pattern("s")]],
        "ortho_source_is_c_or_ç": ["spell", _or(["spell_search", compile_pattern("ç")],
                                                 ["spell_search", compile_pattern("c[ei]")])],
        "ortho_source_is_intervocalic_s": ["spell", ["spell_search", compile_pattern(
            "[aeiouáéíóúâêôãõ]s[aeiouáéíóúâêôãõ]")]],
        "no_ortho_available": ["spell", ["spell_empty"]],
    }
    def lit(find, rep, gate=("true",)):
        return {"gate": list(gate), "kind": "replace", "find": find, "rep": rep}

    steps: List[dict] = []
    if profile.requires_debiasing:
        ei = ["spell_search", compile_pattern("ei")]
        ou = ["spell_search", compile_pattern("ou")]
        if not spirants:
            steps.append(lit("ɐj", "ej", ei))
            steps.append({"gate": _and(_not(ei), ["spell_empty"]), "kind": "sub",
                          "pattern": compile_pattern(r"(?<=[^aeɛɐiɨoɔuɑæøœyãẽĩõũ\s])ɐj"),
                          "template": [["lit", "ej"]]})
            steps.append({"gate": ou, "kind": "sub", "pattern": compile_pattern("o(?=[tdszʃnlɾ])"),
                          "template": [["lit", "ow"]]})
            for a, b in (("β", "b"), ("ð", "d"), ("ɣ", "ɡ"), ("ɫ", "l")):
                steps.append(lit(a, b))
        else:
            raise IRUnsupportedFeature("pt-PT", "dialect_spirants")
    for rule in profile.rules:
        if isinstance(rule, IPAChainShift):
            if rule.context not in (None, "stressed"):
                raise IRUnsupportedFeature("pt-PT", f"chain shift context {rule.context!r}")
            steps.append({"gate": ["true"], "kind": "chain", "on": ["ˈ"], "off": sorted(VOWEL_SET),
                          "when_on": int(rule.context == "stressed"),
                          "map": sorted(rule.mapping.items())})
    lexical = [[r.word.lower(), r.find, r.replace] for r in profile.rules
               if isinstance(r, IPALexicalRule)]
    if lexical:
        steps.append({"gate": ["true"], "kind": "lexical", "rules": lexical})
    for rule in profile.rules:
        if not isinstance(rule, IPARule):
            continue
        gate = _not(["spell_empty"]) if rule.requires_ortho else ["true"]
        if rule.context is None:
            steps.append(lit(rule.find, rule.replace, gate))
        elif rule.context in contexts:
            steps.append({"gate": gate, "kind": "contextual", "find": rule.find,
                          "rep": rule.replace, "when": contexts[rule.context]})
        else:
            raise ValueError(f"dialect profile {name}: unknown context {rule.context!r}")
    return steps


# ─── the compiler ────────────────────────────────────────────────────────
def _check_supported(spec: LanguageSpec) -> None:
    if spec.plugins:
        raise IRUnsupportedFeature(spec.code, "declared plugins")
    st = spec.stress
    if st is not None and st.source == "plugin":
        raise IRUnsupportedFeature(spec.code, 'stress.source = "plugin"')


def _readings_of(spec: LanguageSpec, entries: Dict[str, Tuple[str, ...]]) -> Set[str]:
    out: Set[str] = set()
    for rs in entries.values():
        out.update(rs)
    for pos_map in (spec.positional_graphemes or {}).values():
        for rs in pos_map.values():
            out.update(rs or ())
    for rule in spec.allophone_rules:
        out.update(_applied(rule, p) for p in rule.phonemes)
    for values in (spec.allophones or {}).values():
        out.update(values)
    out.update((spec.word_exceptions or {}).values())
    return out


def build_ir(code: str, data_ref: Optional[str] = None, *, dialect_profile: Optional[str] = None,
             dialect_spirants: bool = False, apply_stress: bool = True,
             apply_allophony: bool = True, apply_sandhi: bool = True,
             expand_allophones: bool = False, expose_ambiguous_endings: bool = True,
             spec: Optional[LanguageSpec] = None, fragments: Sequence[dict] = ()) -> dict:
    """The IR of *code* with plain strings (the readable form).

    A caller *spec* replaces the registry spec of *code*, and its IR is not kept.
    *fragments* are plugin fragments (docs/ir/o2i-ir-v1.md, 3.5) merged into the document.
    """
    if spec is None:
        base, spec, elision = _base_ir(code, data_ref, apply_stress, apply_allophony, apply_sandhi,
                                       expand_allophones)
    else:
        base, elision = _build(spec, data_ref, apply_stress, apply_allophony, apply_sandhi,
                               expand_allophones)
    ir = dict(base)
    if dialect_profile:
        ir["dialect"] = _dialect_program(dialect_profile, dialect_spirants)
        extra: Set[str] = set()
        _collect_dialect_chars(ir["dialect"], extra)
        chars = dict(base["chars"])
        for c in extra - {chr(cp) for cp in chars}:
            chars[ord(c)] = _char_bits(c, elision) & ~(1 << CB["known"])
        ir["chars"] = chars
        ir["char_maps"] = _char_maps(spec, {chr(cp) for cp in chars})
    if not expose_ambiguous_endings and "endings" in ir:
        endings = dict(ir["endings"])
        endings["table"] = [{**e, "alts": [], "costs": e["costs"][:1]} for e in endings["table"]]
        ir["endings"] = endings
    words, sandhi = merge_fragments(fragments, ir["ir_version"])
    if words:
        ir["word"] = {**ir["word"], "words": sorted(words.items())}
    if sandhi:
        ir["sandhi"] = [*ir.get("sandhi", ()), *sandhi]
    return ir


def fragment_digest(fragment: dict) -> str:
    """sha256 of the canonical JSON of *fragment*."""
    return hashlib.sha256(json.dumps(fragment, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False).encode()).hexdigest()


_FRAGMENT_PARTS = {"ir_version", "words", "sandhi", "unsupported"}
_SANDHI_PAIR_KEYS = {"left", "right", "left_out", "right_out", "left_spelling", "right_spelling"}
_SANDHI_PAUSE_KEYS = {"left", "left_out", "left_spelling", "pause"}


def merge_fragments(fragments: Sequence[dict], ir_version: int) -> Tuple[Dict[str, str], List[dict]]:
    """The ``words`` of *fragments* as one table, and their ``sandhi`` rules as
    IR rules in fragment order. A later fragment wins on a duplicate word.

    Raises:
        ValueError: a fragment is malformed (an unknown key, a wrong ``ir_version``, a
            ``words`` key that is not lowercase NFC, a non-string entry) or has a
            ``sandhi`` rule that :func:`_sandhi_rule` refuses.
    """
    words: Dict[str, str] = {}
    sandhi: List[dict] = []
    for fragment in fragments:
        unknown = sorted(set(fragment) - _FRAGMENT_PARTS)
        if unknown:
            raise ValueError(f"fragment part {unknown[0]!r} is not supported; "
                             f"only 'words', 'sandhi' and 'unsupported' are")
        if fragment.get("ir_version") != ir_version:
            raise ValueError(f"fragment ir_version {fragment.get('ir_version')!r} is not {ir_version}")
        for key, ipa in fragment.get("words", {}).items():
            if not isinstance(key, str) or not isinstance(ipa, str):
                raise ValueError(f"fragment word {key!r}: the key and the value must be strings")
            if key != unicodedata.normalize("NFC", key).lower():
                raise ValueError(f"fragment word {key!r}: a key must be lowercase NFC")
            words[key] = ipa
        for name in fragment.get("unsupported", ()):
            if not isinstance(name, str):
                raise ValueError(f"fragment unsupported entry {name!r}: a name must be a string")
        sandhi += [_sandhi_rule(rule) for rule in fragment.get("sandhi", ())]
    return words, sandhi


def fragment_unsupported(fragments: Sequence[dict]) -> List[str]:
    """The sorted names the *fragments* list as rules they cannot express."""
    return sorted({name for fragment in fragments for name in fragment.get("unsupported", ())})


def _sandhi_rule(rule: dict) -> dict:
    """The IR sandhi rule of a fragment rule, with optional spelling conditions.

    A pair rule has ``left`` and ``right`` patterns (an absent one matches every word) and
    at least one of ``left_out`` and ``right_out``. A pause rule has ``"pause": true``, a
    ``left`` pattern and ``left_out``, and has no right word.

    Raises:
        ValueError: a key outside those of the rule kind, a text that is not a string, a
            pattern or template that the IR cannot compile, or a rule with no output.
    """
    from orthography2ipa.ir.compile_patterns import compile_pattern, compile_template
    pause = rule.get("pause", False)
    if pause is not False and pause is not True:
        raise ValueError(f"fragment sandhi rule {rule!r}: pause must be true or false")
    allowed = _SANDHI_PAUSE_KEYS if pause else _SANDHI_PAIR_KEYS
    unknown = sorted(set(rule) - allowed - {"pause"})
    if unknown:
        raise ValueError(f"fragment sandhi key {unknown[0]!r} is not allowed in {rule!r}")
    for key, text in rule.items():
        if key != "pause" and not isinstance(text, str):
            raise ValueError(f"fragment sandhi key {key!r} in {rule!r}: the value must be a string")
    if "left_out" not in rule and "right_out" not in rule:
        raise ValueError(f"fragment sandhi rule {rule!r} has no left_out or right_out")
    if pause and not rule.get("left"):
        raise ValueError(f"fragment sandhi rule {rule!r}: a pause rule needs a left pattern")
    try:
        item: dict = {"left": compile_pattern(rule.get("left", ""))}
        if not pause:
            item["right"] = compile_pattern(rule.get("right", ""))
        item["obligatory"] = 1
        for side in ("left", "right"):
            if side + "_out" in rule:
                item[side + "_out"] = compile_template(rule[side + "_out"])
            if side + "_spelling" in rule:
                item[side + "_spelling"] = compile_pattern(rule[side + "_spelling"])
    except (re.error, ValueError) as err:
        raise ValueError(f"fragment sandhi rule {rule!r}: {err}") from err
    if pause:
        item["pause"] = 1
    return item


@lru_cache(maxsize=32)
def _base_ir(code: str, data_ref: Optional[str], apply_stress: bool, apply_allophony: bool,
             apply_sandhi: bool, expand_allophones: bool):
    with _data_at(data_ref):
        resolved = registry.resolve(code)
        spec = registry.get(resolved) if data_ref is None else json_loader.load_json_spec(resolved)
        ir, elision = _build(spec, data_ref, apply_stress, apply_allophony, apply_sandhi, expand_allophones)
    return ir, spec, elision


def _build(spec: LanguageSpec, data_ref, apply_stress, apply_allophony, apply_sandhi,
           expand_allophones) -> Tuple[dict, bool]:
    from orthography2ipa.ir.compile_patterns import compile_pattern, compile_template
    _check_supported(spec)
    tok = PhonetokTokenizer(spec)
    table: Dict[str, Tuple[str, ...]] = dict(tok._grapheme_ipa)
    weights = tok._grapheme_weights
    positional_vowel_keys = {
        g for g, positions in (spec.positional_graphemes or {}).items()
        if any(is_ipa_vowel(c) for rs in positions.values() for r in rs or () for c in r)}

    known = _known_chars(spec, itertools.chain(
        table, (spec.positional_graphemes or {}), (spec.word_exceptions or {}),
        (spec.stress.cliticless_words if spec.stress else ())))
    readings = _readings_of(spec, table)
    fallback: Dict[str, Tuple[str, ...]] = {}
    for c in sorted(known):
        if c in table:
            continue
        decomposed = unicodedata.normalize("NFD", c)
        if decomposed == c:
            continue
        pieces = [table.get(p) for p in decomposed]
        if all(v is not None for v in pieces):
            combos = itertools.islice(itertools.product(*pieces), _MAX_DECOMPOSED_COMBOS)
            fallback[c] = tuple("".join(x) for x in combos)
    readings.update(r for rs in fallback.values() for r in rs)

    entries: List[dict] = []
    for key in sorted(set(table) | set(fallback), key=lambda s: [ord(c) for c in s]):
        is_fallback = key not in table
        rs = fallback[key] if is_fallback else table[key]
        w = None if is_fallback else weights.get(key)
        costs = [_micro(c) for c in candidate_base_costs(rs, w, grapheme=key)]
        entry = {"key": key, "cands": list(rs), "costs": costs,
                 "bits": _entry_bits(key, rs, spec, positional_vowel_keys, is_fallback, table)}
        if not is_fallback:
            entry["trie"] = 1
        if key in (spec.positional_graphemes or {}) and not is_fallback:
            declared = {p: v for p, v in spec.positional_graphemes[key].items()
                        if p not in INERT_POSITIONS}
            rules = _positional_rules(spec, declared)
            if rules:
                entry["positional"] = rules
        entries.append(entry)
    keys = {e["key"]: tuple(e["cands"]) for e in entries}

    all_chars = set(known)
    for s in readings:
        all_chars.update(s)
    ir: dict = {
        "ir_version": 1,
        "lang": spec.code,
        "source": {"o2i_version": VERSION_STR, "compiler_commit": _git_head(),
                   "data_ref": data_ref or _git_head(), "spec_format_version": 1,
                   "unidata": UNIDATA},
        "chars": {},
        "entries": entries,
        "fallback": sorted(fallback),
        "word": {
            "exceptions": sorted((spec.word_exceptions or {}).items()),
            "internal_apostrophe": int(spec.word_internal_apostrophe),
            "apostrophe_elision": int(spec.apostrophe_elision),
            "collapse_geminates": int(spec.collapse_geminates),
            "context_beam": int(spec.has_positional_data() or any(r.stress for r in spec.allophone_rules)),
            "clitic_marks": sorted({SECONDARY_MARK, spec.stress.stress_mark if spec.stress else "ˈ"}),
            "silent_stress_marks": sorted(ch for ch in (spec.stress.marked_vowels if spec.stress else ())
                                          if ch in spec.graphemes and not any(spec.graphemes[ch])),
            **({"tone_dock": sorted(spec.phonemes or ())} if spec.tone_marks_syllable_final else {}),
        },
        "beam": {"tilde": _NASAL_TILDE},
        "debug": {"inert_positions": sorted({p.value for pos in (spec.positional_graphemes or {}).values()
                                             for p in pos if p in INERT_POSITIONS})},
    }
    aperture = any(p in pos for pos in (spec.positional_graphemes or {}).values()
                   for p in (P.OPEN_SYLLABLE, P.CLOSED_SYLLABLE, P.NUCLEUS_STRESSED_OPEN,
                             P.NUCLEUS_STRESSED_CLOSED, P.NUCLEUS_UNSTRESSED_OPEN,
                             P.NUCLEUS_UNSTRESSED_CLOSED))
    if expand_allophones:
        ir["allophone_map"] = sorted((k, list(v)) for k, v in (spec.allophones or {}).items())

    st = spec.stress
    if st is not None or aperture:
        judge = _judge_for(spec)
        vowel_letters = st.vowel_letters if st is not None else ()
        ir["syllable"] = {
            "diphthongs": list(st.diphthongs) if st is not None else [],
            "onset_graphemes": sorted(judge.vowel_final_consonants),
            "semivowels": [] if vowel_letters else sorted(_semivowel_roles(spec).items()),
        }
        if vowel_letters:
            ir["syllable"]["vowel_letters"] = sorted({v.lower() for v in vowel_letters})
        if spec.constrain_onsets:
            ir["syllable"]["onsets"] = _written_onsets(spec)
        if aperture:
            tail_keys = {k.lower() for k in (*spec.graphemes, *(spec.positional_graphemes or {})) if k}
            ir["syllable"]["silent_tail"] = sorted(
                k for k in tail_keys if len(k) <= _MAX_SILENT_TAIL and _silent_word_finally(spec, k))
    if st is not None:
        if st.closed_hiatus is not None:
            ir["syllable"]["closed_hiatus"] = {
                "pairs": list(st.closed_hiatus.pairs), "onsets": list(st.closed_hiatus.onsets),
                "codas": list(st.closed_hiatus.codas),
                "atonic_onsets": list(st.closed_hiatus.atonic_onsets),
                "multi_keys": [g for g in spec.graphemes if len(g) > 1]}
        if st.final_diphthongs is not None:
            ir["syllable"]["final_diphthongs"] = {
                "diphthongs": list(st.final_diphthongs.diphthongs),
                "finals": list(st.final_diphthongs.finals)}
        stress = {
            "mark": st.stress_mark, "secondary_mark": SECONDARY_MARK,
            "alternating": int(st.secondary_stress == "alternating"),
            "prefixes": sorted(st.unstressed_prefixes, key=lambda a: (-len(a), a)),
            "coda_liquid": int(st.coda_liquid_capture),
            **({"iambic": {"max_onset": st.max_onset}} if st.iambic_length else {}),
            **({"accent2": {"mark": st.accent2_mark, "finals": sorted(st.accent2_final_letters)}}
               if st.accent2_mark else {}),
            "schwa_rimes": sorted(st.schwa_rimes),
            "marked": sorted(st.marked_vowels),
            "final": sorted(st.final_stress_endings, key=lambda a: (-len(a), a)),
            "penult": sorted(st.penult_stress_endings, key=lambda a: (-len(a), a)),
            "antepenult": sorted(st.antepenult_stress_endings, key=lambda a: (-len(a), a)),
            "default": st.default_position,
            "cliticless": sorted(cliticless_keys(spec)),
            "compound_last": int(st.compound_stress == "last"),
            "mark_diphthongs": list(st.diphthongs),
            "tonic_after_diphthong": list(st.tonic_after_diphthong),
            "stand_in": "ə",
            "apply": int(apply_stress),
            "contact_units": sorted((g for g in spec.graphemes if g), key=lambda a: (-len(a), a)),
            "silent_units": sorted(g for g, v in spec.graphemes.items() if g and not any(v)),
        }
        if st.quantity_sensitive:
            stress["weight"] = {"max_onset": st.max_onset,
                                "superheavy_final": int(st.superheavy_final_attracts)}
        if st.ipa_diphthongs is not None:
            stress["ipa_diphthongs"] = list(st.ipa_diphthongs)
        if st.constrain_mark_onsets:
            mo = st.max_onset if st.max_onset_declared else None
            ijudge = _ipa_judge(mo, st.onset_clusters)
            pieces: Set[str] = set()
            for a in readings:
                pieces.update(segment_ipa(a, _MARK_ATOMS))
            for a, b in itertools.product(readings, repeat=2):
                pieces.update(segment_ipa(a + b, _MARK_ATOMS))
            units = sorted(u for u in pieces if u and all(
                unidata.category(ch)[0] == "L" or unicodedata.combining(ch) for ch in u)
                and not any(is_ipa_vowel(ch) for ch in u))
            stress["mark_onsets"] = {
                "max": -1 if mo is None else mo,
                "velar": "ŋ",
                "table": _onset_table(ijudge, units, st.onset_clusters),
            }
        if spec.script_type == ScriptType.ABUGIDA:
            stress["ipa_count"] = 1
        ir["stress"] = stress
        all_chars.update(st.stress_mark + SECONDARY_MARK + "ə")
    ir["atoms"] = {"mark": sorted(_MARK_ATOMS, key=lambda a: (-len(a), a)), "affricates": list(_AFFRICATES)}

    if apply_allophony and spec.allophone_rules:
        atoms = sorted(_rule_atoms(spec.allophone_rules), key=lambda a: (-len(a), a))
        ir["allophony"] = {
            "passes": max(1, spec.allophone_passes),
            "atoms": atoms,
            "geminate": int(spec.doubled_letters_geminate),
            "rules": [_allophone_rule(r, spec, atoms, keys) for r in spec.allophone_rules],
        }
    if apply_sandhi and spec.sandhi_rules:
        sandhi = []
        for rule in spec.sandhi_rules:
            item = {"left": compile_pattern(rule.left_context), "right": compile_pattern(rule.right_context),
                    "obligatory": int(rule.obligatory)}
            if rule.transform is not None:
                item["left_out"] = compile_template(rule.transform)
            if rule.right_transform is not None:
                item["right_out"] = compile_template(rule.right_transform)
            sandhi.append(item)
            for part in (*item.get("left_out", ()), *item.get("right_out", ())):
                if part[0] == "lit":
                    all_chars.update(part[1])
        ir["sandhi"] = sandhi
    elision = bool(spec.apostrophe_elision and spec.word_internal_apostrophe
                   and not any(m in key for key in table for m in "'’"))
    if spec.grammatical_endings:
        ir["endings"] = _endings(spec)
        all_chars.update(c for e in ir["endings"]["table"] for r in (e.get("ipa", ""), *e["alts"]) for c in r)
    if spec.inherent_vowel:
        ir["inherent"] = {"vowel": spec.inherent_vowel, "coda_no": int(spec.coda_no_inherent_vowel)}
        if spec.inherent_vowel_final is not None:
            ir["inherent"]["final"] = spec.inherent_vowel_final
        signs = sorted((v for v in spec.dependent_vowels if len(v) > 1), key=lambda v: (-len(v), v))
        if signs:
            ir["inherent"]["signs"] = [[v, int(_is_nucleus((table.get(v) or ("",))[0]))] for v in signs]
            all_chars.update("".join(signs))
        all_chars.update(spec.inherent_vowel + (spec.inherent_vowel_final or ""))
        for entry in entries:
            entry["bits"] |= _inherent_entry_bits(entry["key"], tuple(table.get(entry["key"], ())), spec)
    if spec.preposed_vowels:
        for entry in entries:
            entry["bits"] |= _preposed_entry_bits(entry["key"], table, spec)
            onset = _onset_reading(entry["key"], tuple(table.get(entry["key"], ())), spec)
            if onset:
                entry["onset"] = list(onset)
                all_chars.update("".join(onset))
    if spec.consonant_nuclei:
        nuclei = {k.lower(): v for k, v in spec.consonant_nuclei.items()}
        ir["consonant_nuclei"] = [[k, v] for k, v in nuclei.items()]
        all_chars.update("".join(nuclei) + "".join(nuclei.values()))
        for entry in entries:
            reading = nuclei.get(entry["key"])
            if reading is not None and grapheme_is_vowel(entry["key"], (reading,), spec.vowel_graphemes):
                entry["bits"] |= 1 << EB["vowel_nucleus"]
    if spec.tone_rules is not None:
        ir["tone"] = _tone(spec)
        all_chars.update("".join(r[3] for r in ir["tone"]["table"]) + "".join(ir["tone"]["dead_codas"])
                         + "".join(ir["tone"]["atoms"]))
    if spec.virama_final_vowel is not None:
        ir["word"]["virama_final"] = spec.virama_final_vowel
        all_chars.update(spec.virama_final_vowel)
    all_chars.update(_whitespace())
    presentation, rewrites = _prepare_rewrites(spec, table)
    ir["rewrites"] = rewrites
    for _, out in presentation:
        all_chars.update(out)
    ir["chars"] = {ord(c): _char_bits(c, elision) | _abugida_char_bits(c, table, spec.dependent_vowels)
                   for c in sorted(all_chars)}
    for c in all_chars - known:
        ir["chars"][ord(c)] &= ~(1 << CB["known"])
    ir["char_maps"] = dict(_char_maps(spec, all_chars), presentation=presentation)
    ir["bits"] = {"char": list(CHAR_BITS), "entry": list(ENTRY_BITS)}
    return ir, elision


def _collect_dialect_chars(steps: List[dict], out: Set[str]) -> None:
    for step in steps:
        for field in ("find", "rep"):
            if field in step:
                out.update(step[field])
        for a, b in step.get("map", ()):
            out.update(a + b)
        for rule in step.get("rules", ()):
            out.update("".join(rule))


def _endings(spec: LanguageSpec) -> dict:
    """``grammatical_endings`` and the data its tail rewrite reads."""
    table = []
    for ending, value in sorted(spec.grammatical_endings.items()):
        rank1, alts = normalize_ending_value(value)
        item = {"key": ending, "alts": list(alts),
                "costs": [_micro(c) for c in candidate_base_costs(
                    (rank1 if rank1 is not None else "", *alts), grapheme=ending)]}
        if rank1 is not None:
            item["ipa"] = rank1
        table.append(item)
    positional = spec.positional_graphemes or {}
    vowels = []
    for key in sorted(set(positional) | set(spec.graphemes or {})):
        reduced, readings = set(), set()
        for position, values in (positional.get(key) or {}).items():
            for value in values or ():
                runs = {value[a:b] for a, b in _vowel_runs(value)}
                readings |= runs
                if position in _UNSTRESSED_POSITIONS:
                    reduced |= runs
        for value in (spec.graphemes or {}).get(key) or ():
            readings |= {value[a:b] for a, b in _vowel_runs(value)}
        if reduced:
            vowels.append({"key": key, "reduced": sorted(reduced), "readings": sorted(readings)})
    sources: Dict[str, Set[str]] = {}
    for rule in spec.allophone_rules:
        for phoneme in rule.phonemes:
            sources.setdefault(rule.surface, set()).update(phoneme[a:b] for a, b in _vowel_runs(phoneme))
    suffix = sorted(g for g in _TRANSPARENT_SUFFIX_GRAPHEMES
                    if "" in ((positional.get(g) or {}).get(P.WORD_FINAL) or ()))
    return {"table": table, "suffix": suffix, "vowels": vowels,
            "sources": [{"surface": k, "vowels": sorted(v)} for k, v in sorted(sources.items())]}


def _inherent_entry_bits(key: str, readings: Tuple[str, ...], spec: LanguageSpec) -> int:
    """The entry facts the inherent-vowel branch reads."""
    bits = 0
    first = readings[0] if readings else ""
    is_mark = (unidata.category(key[-1]) in ("Mn", "Mc") and not _is_subjoined_letter_cluster(key)
               and not (len(key) > 1 and set(key[1:]) <= set(spec.consonant_marks)))
    if first and not is_mark and not _is_nucleus(first):
        bits |= 1 << EB["takes_inherent"]
        for name, vowel in (("vowel_inherent", spec.inherent_vowel),
                            ("vowel_inherent_final", spec.inherent_vowel_final)):
            if vowel is not None and grapheme_is_vowel(key, tuple(r + vowel for r in readings),
                                                       spec.vowel_graphemes):
                bits |= 1 << EB[name]
    positional = (spec.positional_graphemes or {}).get(key) or {}
    if list(positional.get(P.BEFORE_CONSONANT) or ()) == [""] and P.BEFORE_CONSONANT in positional:
        bits |= 1 << EB["silent_before_consonant"]
    if P.AFTER_VOWEL in positional:
        bits |= 1 << EB["postvocalic"]
    if key in spec.dependent_vowels or key.lower() in {v.lower() for v in spec.preposed_vowels}:
        bits |= 1 << EB["vowel_sign"]
    return bits


def _tone(spec: LanguageSpec) -> dict:
    """``tone_rules`` with each tone name resolved to its IPA."""
    rules = spec.tone_rules
    table = [[cls, shape, mark, rules.tones.get(tone, "") if tone else ""]
             for cls, by_shape in sorted(rules.table.items())
             for shape, by_mark in sorted(by_shape.items())
             for mark, tone in sorted(by_mark.items())]
    return {"classes": sorted(rules.classes.items()), "marks": sorted(rules.marks.items()),
            "no_mark": rules.no_mark, "dead_codas": list(rules.dead_codas), "table": table,
            "atoms": list(spec.phonemes or ())}


def _preposed_entry_bits(key: str, table: Dict[str, Tuple[str, ...]], spec: LanguageSpec) -> int:
    """The entry facts of the preposed-vowel branch."""
    preposed = {v.lower() for v in spec.preposed_vowels}
    readings = table.get(key, ())
    bits = 0
    first = readings[0] if readings else ""
    if key.lower() in preposed:
        if not any(is_ipa_vowel(c) for c in first):
            raise IRUnsupportedFeature(spec.code, f"preposed vowel {key!r} without a vowel reading")
        bits |= 1 << EB["preposed"]
        if _ends_in_a_vowel(first):
            bits |= 1 << EB["preposed_open"]
    if any(readings):
        bits |= 1 << EB["audible"]
    head, tail = table.get(key[:1]), table.get(key[1:])
    if len(key) > 1 and head and head[0] and list(readings) == list(tail or (None,)):
        bits |= 1 << EB["silent_head"]
        if spec.codas and tail and tail[0] not in spec.codas:
            bits |= 1 << EB["head_not_coda"]
    initial = _onset_reading(key, readings, spec)
    effective = initial or readings
    is_sign = not initial and (
        (unidata.category(key[-1]) in ("Mn", "Mc") and not (first and not _is_nucleus(first)))
        or key in spec.dependent_vowels or key.lower() in preposed)
    if effective and not is_sign and not _is_nucleus(effective[0]):
        bits |= 1 << EB["preposed_host"]
    if (readings and (unidata.category(key[0]) in ("Mn", "Mc") or key in spec.dependent_vowels)
            and _is_nucleus(first)):
        bits |= 1 << EB["circumfix_tail"]
    return bits


def _onset_reading(key: str, readings: Tuple[str, ...], spec: LanguageSpec) -> Tuple[str, ...]:
    """The ``word_initial`` readings a preposed vowel's host takes when they
    are an onset and its flat reading is a nucleus (Lao ⟨ອ⟩), else ()."""
    initial = ((spec.positional_graphemes or {}).get(key) or {}).get(P.WORD_INITIAL)
    if initial and readings and _is_nucleus(readings[0]) and not _is_nucleus(initial[0]):
        return tuple(initial)
    return ()


def _abugida_char_bits(c: str, table: Dict[str, Tuple[str, ...]], vowel_signs: Sequence[str]) -> int:
    """The ``syllabic_mark``, ``mark_spells_nothing`` and ``supplies_vowel`` bits of one char."""
    bits = 0
    if c in SYLLABIC_MARKS:
        bits |= 1 << CB["syllabic_mark"]
    readings = table.get(c)
    if readings is not None and list(readings) == [""] and _is_a_mark(c):
        bits |= 1 << CB["mark_spells_nothing"]
    first = readings[0] if readings else ""
    if ((unidata.category(c) in ("Mn", "Mc") or c in vowel_signs) and first
            and not unicodedata.combining(first[0]) and _is_nucleus(first)):
        bits |= 1 << CB["supplies_vowel"]
    return bits


def _prepare_rewrites(spec: LanguageSpec, table) -> Tuple[List[Tuple[int, str]], List[dict]]:
    """The script rewrites of ``prepare``: the Arabic presentation forms as a
    codepoint map, and gemination as pattern rewrites."""
    from orthography2ipa.ir.compile_patterns import compile_pattern, compile_template
    presentation: List[Tuple[int, str]] = []
    rules: List[Tuple[str, str]] = []
    declares_shadda = _AR_SHADDA in table
    if spec.script == "Arabic" or declares_shadda:
        for lo, hi in ((0xFB50, 0xFDFF), (0xFE70, 0xFEFF)):
            for cp in range(lo, hi + 1):
                out = unicodedata.normalize("NFKC", chr(cp))
                if out != chr(cp) and unidata.assigned(chr(cp)):
                    presentation.append((cp, out))
        if declares_shadda:
            rules += [(_AR_GEM_SHADDA_FIRST.pattern, r"\1\1\2"), (_AR_GEM_HARAKAT_FIRST.pattern, r"\1\1\2"),
                      (_AR_GEM_BARE.pattern, r"\1\1")]
    elif spec.script == "Gurmukhi":
        rules.append((_GURMUKHI_ADDAK.pattern, "\\1" + _GURMUKHI_VIRAMA + "\\1"))
    rewrites = [{"pattern": compile_pattern(p), "template": compile_template(t)} for p, t in rules]
    return presentation, rewrites


@lru_cache(maxsize=None)
def _whitespace() -> FrozenSet[str]:
    """Every character the word split treats as a space."""
    return frozenset(c for c in map(chr, range(0x110000)) if _WS_RE.match(c))


@lru_cache(maxsize=None)
def _compositions() -> Tuple[Tuple[str, str, str], ...]:
    """Every primary composite of Unicode as (first, second, composite)."""
    out = []
    for cp in itertools.chain(range(0xAC00), range(0xAC00 + 11172, 0x110000)):
        c = chr(cp)
        raw = unicodedata.decomposition(c)
        if raw and not raw.startswith("<") and unidata.assigned(c):
            parts = [chr(int(x, 16)) for x in raw.split()]
            if len(parts) == 2 and unicodedata.normalize("NFC", c) == c:
                out.append((parts[0], parts[1], c))
    # Hangul syllables compose by arithmetic; Python 3.14 also lists them in the decomposition table.
    for s in range(11172):
        lv, t = divmod(s, 28)
        if t:
            out.append((chr(0xAC00 + lv * 28), chr(0x11A7 + t), chr(0xAC00 + s)))
        else:
            out.append((chr(0x1100 + lv // 21), chr(0x1161 + lv % 21), chr(0xAC00 + s)))
    return tuple(out)


def _char_maps(spec: LanguageSpec, chars: Set[str]) -> dict:
    casefold, lower, nfd, ccc = {}, {}, {}, {}
    for c in sorted(chars):
        cp = ord(c)
        if _lower(c, spec.code) != c:
            casefold[cp] = _lower(c, spec.code)
        if c.lower() != c:
            lower[cp] = c.lower()
        d = unicodedata.normalize("NFD", c)
        if d != c:
            nfd[cp] = d
        if unicodedata.combining(c):
            ccc[cp] = unicodedata.combining(c)
    reach = set(chars)
    while True:
        found = [t for t in _compositions() if t[0] in reach and t[1] in reach and t[2] not in reach]
        if not found:
            break
        reach.update(t[2] for t in found)
    compose = [[ord(a), ord(b), ord(c)] for a, b, c in _compositions() if a in reach and b in reach]
    for d in list(nfd.values()):
        for c in d:
            if unicodedata.combining(c):
                ccc[ord(c)] = unicodedata.combining(c)
    maps = {"casefold": sorted(casefold.items()), "plain_lower": sorted(lower.items()),
            "nfd": sorted(nfd.items()), "ccc": sorted(ccc.items()), "compose": sorted(compose)}
    if spec.fold_diacritics:
        maps["fold"] = sorted(spec.fold_diacritics)
    return maps


def compile_spec(code: str, data_ref: Optional[str] = None, **options) -> dict:
    """The canonical IR JSON document of *code* (docs/ir/o2i-ir-v1.md, 2.2)."""
    return layout.encode(build_ir(code, data_ref, **options))
