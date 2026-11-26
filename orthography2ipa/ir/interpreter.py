"""The o2i IR reference interpreter (docs/ir/o2i-ir-v1.md, section 3).

It reads one IR document and one text and writes one IPA string. Every fact
it tests is a table, an attribute bit or a predicate that the compiler wrote;
it imports no engine module. A host may run its own steps through :class:`Hooks`.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import accumulate
from typing import Callable, Dict, FrozenSet, List, Mapping, Optional, Sequence, Set, Tuple

from orthography2ipa.ir import layout, pattern
from orthography2ipa.ir.dialect import run_program

__all__ = ["Interpreter", "IRVersionError", "WordResult", "Result", "Hooks"]

SUPPORTED_IR_VERSIONS = (1,)

# Bit numbers: the compiler writes their names into ``bits``; the
# interpreter resolves names to numbers once, at load.
_CHAR_NAMES = (
    "known", "space", "punct", "digit", "alpha", "letter_or_mark", "combining", "mn_mc",
    "a_mark", "modifier", "orth_vowel", "ipa_vowel", "basic_vowel", "front_letter", "length",
    "non_syllabic", "glide", "offglide", "nasal_carrier", "apostrophe", "hyphen", "pause",
    "edge_punct", "word_letter", "elision_apostrophe", "virama", "vowel_ipa_set",
    "glide_head", "elision_h", "whitespace", "syllabic_mark", "mark_spells_nothing", "supplies_vowel",
    "vowel_phone", "nucleus_base", "syllabic", "liquid", "tone_mark",
)
_ENTRY_NAMES = (
    "vowel", "consonant", "front", "back", "palatal", "emphatic",
    "base_a", "base_e", "base_i", "base_o", "base_u", "base_y",
    "after_a", "after_e", "after_i", "after_o", "after_u", "after_front", "after_back",
    "silent_final", "transparent_final", "carries_nucleus", "spells_nothing",
    "multi_not_mute_digraph", "holds_vowel", "readings_hold_vowel", "orth_vowel_first",
    "glide_final_key", "fallback", "cluster_next", "cluster_prev", "coda_nasal_reading",
    "has_reading", "glide_vowel_cons", "glide_vowel_final", "glide_marker",
    "takes_inherent", "silent_before_consonant", "postvocalic", "vowel_inherent", "vowel_inherent_final",
    "vowel_sign", "preposed", "preposed_host", "preposed_open", "silent_head", "head_not_coda",
    "audible", "circumfix_tail", "vowel_nucleus", "prevocalic_backoff",
)
_NO_STRESS = -1

WORD, WS, PUNCT, DIGIT, UNKNOWN = "grapheme", "whitespace", "punctuation", "digit", "unknown"


class IRVersionError(ValueError):
    pass


@dataclass(frozen=True)
class Token:
    kind: str
    grapheme: str
    entry: int
    readings: Tuple[str, ...]
    position: int
    length: int
    vowel: Optional[bool] = None


@dataclass(frozen=True)
class WordResult:
    word: str
    ipa: str
    dropped: Tuple[str, ...] = ()
    paths: Tuple[Tuple[Tuple[str, ...], int], ...] = ()
    forced: bool = False
    override: bool = False


@dataclass
class Result:
    ipa: str
    words: Tuple[WordResult, ...] = ()


@dataclass
class _Word:
    surface: str
    hyphen_joined: bool = False
    pausal: bool = False
    forced: Optional[str] = None
    #: The spelling before the caller's mark stage, when it differs: the lexicon key.
    key: Optional[str] = None


#: One slot of the word beam: ``[(ipa, cost)]``, best first. A cost is an
#: integer in micro-units, as the IR writes it.
Slot = List[Tuple[str, int]]


@dataclass(frozen=True)
class Hooks:
    """The host callbacks the interpreter runs. Every field is optional, and a
    hook is never part of the IR."""
    # text(run): rewrites one plain run of the input before it is prepared.
    text: Optional[Callable[[str], str]] = None
    # rescore(word, tokens, slots, syllables, stressed): returns new beam slots, before the
    # allophony pass. syllables is the syllable index of each token (None without syllable
    # context); stressed is the stressed syllable. A slot with no candidates deletes its grapheme.
    rescore: Optional[Callable[[str, Sequence["Token"], List[Slot], Optional[List[Optional[int]]],
                                Optional[int]], List[Slot]]] = None
    # syllables(word): the written syllables of *word*, or None to let the IR split it.
    syllables: Optional[Callable[[str], Optional[List[str]]]] = None
    # sandhi(words, surfaces, pausal): one IPA string per word; the dialect program and NFC run after.
    sandhi: Optional[Callable[[List[str], List[str], List[bool]], List[str]]] = None


@dataclass
class _Ctx:
    """The slot context of a predicate: one run of grapheme slots."""
    entries: List[int]
    tokens: List[Token]
    syll_idx: Optional[List[Optional[int]]] = None
    stressed: Optional[int] = None
    secondary: FrozenSet[int] = frozenset()
    aperture: Optional[List[Optional[bool]]] = None
    cands: Optional[List[List[Tuple[str, int]]]] = None
    source: str = ""


class Interpreter:
    """Runs one IR (readable or canonical form)."""

    def __init__(self, ir: dict):
        if ir.get("ir_version") not in SUPPORTED_IR_VERSIONS:
            raise IRVersionError(f"unsupported ir_version {ir.get('ir_version')!r}")
        for name, version in ir.get("primitives", {}).items():
            if layout.SEMANTICS.get(name) != version:
                raise IRVersionError(f"unsupported primitive version: {name} needs {version}, "
                                     f"this interpreter has {layout.SEMANTICS.get(name)}")
        if "strings" in ir:
            ir = layout.decode(ir)
        self.ir = ir
        names, enames = ir["bits"]["char"], ir["bits"]["entry"]
        missing = sorted(set(_CHAR_NAMES) - set(names)) + sorted(set(_ENTRY_NAMES) - set(enames))
        if missing:
            raise IRVersionError(f"the IR's bit table lacks {', '.join(missing)}")
        self._cbit = {n: 1 << names.index(n) for n in _CHAR_NAMES}
        self._ebit = {n: 1 << enames.index(n) for n in _ENTRY_NAMES}
        self._chars: Dict[int, int] = ir["chars"]
        maps = ir["char_maps"]
        self._casefold = {chr(cp): s for cp, s in maps["casefold"]}
        self._lower = {chr(cp): s for cp, s in maps["plain_lower"]}
        self._nfd = {chr(cp): s for cp, s in maps["nfd"]}
        self._ccc = {chr(cp): v for cp, v in maps["ccc"]}
        self._compose = {(chr(a), chr(b)): chr(c) for a, b, c in maps["compose"]}
        self._fold = frozenset(maps.get("fold", ()))
        self._presentation = {chr(cp): out for cp, out in maps.get("presentation", ())}
        self._rewrites = ir.get("rewrites", ())
        self._inherent = ir.get("inherent")
        self._nuclei = dict(ir.get("consonant_nuclei", ()))
        self._tone = ir.get("tone")
        if self._tone:
            self._tone_classes = dict(self._tone["classes"])
            self._tone_marks = dict(self._tone["marks"])
            self._tone_table = {(c, s, m): t for c, s, m, t in self._tone["table"]}
            self._tone_class_names = {c for c, _, _, _ in self._tone["table"]}
        endings = ir.get("endings")
        if endings:
            self._endings = {e["key"]: e for e in endings["table"]}
            self._ending_suffix = set(endings["suffix"])
            self._ending_vowels = {v["key"]: (set(v["reduced"]), set(v["readings"])) for v in endings["vowels"]}
            self._ending_sources = {v["surface"]: set(v["vowels"]) for v in endings["sources"]}
        self.entries = ir["entries"]
        self._key_index = {e["key"]: i for i, e in enumerate(self.entries)}
        self._trie_keys = {e["key"] for e in self.entries if e.get("trie")}
        self._max_key = max((len(k) for k in self._trie_keys), default=0)
        self._trie: dict = {}
        for k in self._trie_keys:
            node = self._trie
            for c in k:
                node = node.setdefault(c, {})
            node[""] = k
        self._fallback = set(ir.get("fallback", ()))
        self._bits = [e["bits"] for e in self.entries]
        self.word = ir["word"]
        self._exceptions = dict(self.word["exceptions"])
        self._fragment_words = dict(self.word.get("words", ()))
        self._tokens: Dict[str, Tuple[Token, ...]] = {}
        self._words: Dict[Tuple[str, int], "WordResult"] = {}
        self._segments: Dict[Tuple[str, int], Tuple[Sequence[str], Tuple[str, ...]]] = {}
        self.stress = ir.get("stress")
        self.syll = ir.get("syllable") or {}
        self._allo = ir.get("allophony")
        self._allophone_map = dict(ir["allophone_map"]) if "allophone_map" in ir else None
        self._mark_atoms = tuple(ir["atoms"]["mark"])
        self._affricates = tuple(ir["atoms"]["affricates"])
        self._tilde = ir["beam"]["tilde"]
        self._hiatus_cache: Dict[str, FrozenSet[int]] = {}
        self._syll_cache: Dict[str, List[str]] = {}
        self.hooks = Hooks()
        if self.stress:
            self._cliticless = frozenset(self.stress["cliticless"])
            onsets = self.stress.get("mark_onsets")
            self._mark_table = {tuple(t) for t in onsets["table"]} if onsets else None
        self._hiatus_on = bool(self.syll.get("closed_hiatus") or self.syll.get("final_diphthongs"))
        self._semivowels = dict(self.syll.get("semivowels", ()))
        self._vowel_letters = frozenset(self.syll.get("vowel_letters", ())) or None
        self._onsets = self.syll.get("onsets")
        if self._onsets:
            self._onset_table = {tuple(t) for t in self._onsets["table"]}
            self._onset_velar = frozenset(self._onsets["velar"])

    def with_hooks(self, hooks: Hooks) -> "Interpreter":
        """A copy of this interpreter that runs *hooks*. It shares the
        loaded tables and keeps its own syllable cache."""
        it = object.__new__(Interpreter)
        it.__dict__.update(self.__dict__)
        it.hooks = hooks
        it._syll_cache = {}
        it._words = {}
        return it

    # ─── characters ──────────────────────────────────────────────────
    def _c(self, ch: str, name: str) -> bool:
        return bool(self._chars.get(ord(ch), 0) & self._cbit[name])

    def _e(self, entry: int, name: str) -> bool:
        return bool(self._bits[entry] & self._ebit[name])

    def _slot_bits(self, ctx: "_Ctx", j: int) -> int:
        """The entry bits of slot j, with ``vowel`` as the token's inherent
        vowel leaves it (3.3.2 item 6)."""
        bits = self._bits[ctx.entries[j]]
        vowel = ctx.tokens[j].vowel
        if vowel is None:
            return bits
        return bits | self._ebit["vowel"] if vowel else bits & ~self._ebit["vowel"]

    def _comb(self, ch: str) -> bool:
        return self._c(ch, "combining")

    def _vowel_char(self, ch: str) -> bool:
        return not self._comb(ch) and (self._c(ch, "orth_vowel") or self._c(ch, "ipa_vowel"))

    def lower(self, text: str) -> str:
        return "".join(self._lower.get(c, c) for c in text)

    def casefold(self, text: str) -> str:
        return "".join(self._casefold.get(c, c) for c in text)

    def prepare(self, text: str) -> str:
        """S1: NFC, the presentation-form map, then the rewrites in order."""
        text = self.nfc(text)
        if self._fold:
            text = self.nfc("".join(c for ch in text for c in self._nfd.get(ch, ch) if c not in self._fold))
        if self._presentation:
            text = "".join(self._presentation.get(c, c) for c in text)
        for rw in self._rewrites:
            text = self._sub(rw["pattern"], rw["template"], [ord(c) for c in text])
        return text

    def nfc(self, text: str) -> str:
        """NFC by table: full decomposition, canonical order, composition."""
        out: List[str] = []
        for c in text:
            out.extend(self._nfd.get(c, c))
        i = 0
        while i < len(out):
            if self._ccc.get(out[i], 0):
                j = i
                while j < len(out) and self._ccc.get(out[j], 0):
                    j += 1
                out[i:j] = sorted(out[i:j], key=lambda c: self._ccc[c])
                i = j
            else:
                i += 1
        result: List[str] = []
        starter = -1
        last_ccc = -1
        for c in out:
            cc = self._ccc.get(c, 0)
            if starter >= 0 and (last_ccc < cc or (last_ccc == 0 and len(result) - 1 == starter)):
                composed = self._compose.get((result[starter], c))
                if composed is not None:
                    result[starter] = composed
                    continue
            if cc == 0:
                starter = len(result)
                last_ccc = -1
            else:
                last_ccc = cc
            result.append(c)
            if cc == 0:
                last_ccc = 0
        return "".join(result)

    # ─── segmentation (primitive 11) ─────────────────────────────────
    def segment(self, ipa: str, atoms: Sequence[str] = ()) -> List[str]:
        key = (ipa, id(atoms))
        hit = self._segments.get(key)
        if hit is not None and hit[0] is atoms:
            return list(hit[1])
        segments = self._segment(ipa, atoms)
        if len(self._segments) >= 65536:
            self._segments.clear()
        self._segments[key] = (atoms, tuple(segments))
        return segments

    def _segment(self, ipa: str, atoms: Sequence[str]) -> List[str]:
        segments: List[str] = []
        i, n = 0, len(ipa)
        while i < n:
            seg = None
            for atom in atoms:
                end = i + len(atom)
                if ipa.startswith(atom, i) and not (end < n and self._c(ipa[end], "modifier")):
                    if seg is None or len(atom) > len(seg):
                        seg = atom
            if seg is None:
                j = i + 1
                while j < n and self._c(ipa[j], "modifier"):
                    j += 1
                seg = ipa[i:j]
            segments.append(seg)
            i += len(seg)
        return segments

    # ─── S1, S4: preparation and tokenization ────────────────────────
    def _longest_match(self, text: str, start: int) -> Optional[str]:
        node = self._trie
        best = None
        for i in range(start, min(start + self._max_key, len(text))):
            ch = text[i]
            ch = self._casefold.get(ch, ch)
            node = node.get(ch) if len(ch) == 1 else None
            if node is None:
                break
            best = node.get("", best)
        return best

    def _run(self, text: str, pos: int, bit: str) -> int:
        end = pos
        while end < len(text) and self._c(text[end], bit):
            end += 1
        return end

    def tokenize(self, text: str) -> List[Token]:
        hit = self._tokens.get(text)
        if hit is None:
            if len(self._tokens) >= 65536:
                self._tokens.clear()
            hit = self._tokens[text] = tuple(self._tokenize(text))
        return list(hit)

    def _tokenize(self, text: str) -> List[Token]:
        tokens: List[Token] = []
        n = len(text)
        pos = 0
        nucleus_at = -1
        while pos < n:
            end = self._run(text, pos, "space")
            if end > pos:
                tokens.append(Token(WS, " ", -1, (), pos, end - pos))
                pos = end
                continue
            for bit, kind in (("punct", PUNCT), ("digit", DIGIT)):
                end = self._run(text, pos, bit)
                if end > pos:
                    span = text[pos:end]
                    if not (span in self._trie_keys or self._longest_match(text, pos) is not None):
                        tokens.append(Token(kind, span, -1, (), pos, end - pos))
                        pos = end
                        break
            else:
                gkey = self._longest_match(text, pos)
                if gkey is not None and self._e(self._key_index[gkey], "preposed"):
                    end = self._preposed(text, pos, gkey, tokens)
                    if end is not None:
                        pos = end
                        continue
                if gkey is not None:
                    gkey = self._backoff(text, pos, gkey, tokens)
                    if self._nuclei:
                        gkey = self._unfuse_nucleus(text, pos, gkey, tokens)
                    e = self._key_index[gkey]
                    readings, length, vowel = tuple(self.entries[e]["cands"]), len(gkey), None
                    if pos == nucleus_at and gkey in self._nuclei:
                        readings, vowel = (self._nuclei[gkey],), self._e(e, "vowel_nucleus")
                    elif self._inherent and self._e(e, "takes_inherent"):
                        readings, length, vowel, nucleus_at = self._inherent_vowel(text, pos, e, readings, tokens)
                    tokens.append(Token(WORD, gkey, e, readings, pos, length, vowel))
                    pos += length
                    continue
                ch = text[pos]
                if ch in self._fallback:
                    e = self._key_index[ch]
                    tokens.append(Token(WORD, ch, e, tuple(self.entries[e]["cands"]), pos, 1))
                else:
                    tokens.append(Token(UNKNOWN, ch, -1, (), pos, 1))
                pos += 1
                continue
        return tokens

    def _inherent_vowel(self, text: str, pos: int, e: int, readings: Tuple[str, ...],
                        tokens: List[Token]) -> Tuple[Tuple[str, ...], int, Optional[bool], int]:
        """3.3.2 item 6: the inherent vowel of an abugida consonant letter.
        The last value is the offset of a consonant nucleus after the letter, or -1."""
        length = len(self.entries[e]["key"])
        after = pos + length
        next_ch = text[after] if after < len(text) else ""
        nucleus_at = self._consonant_nucleus_at(text, after, tokens)
        if next_ch and self._c(next_ch, "virama"):
            return readings, length + 1, None, nucleus_at
        if nucleus_at >= 0 or self._supplies_vowel_at(text, after):
            return readings, length, None, nucleus_at
        inherent = self._inherent
        if inherent["coda_no"] and self._syllable_has_nucleus(tokens):
            return readings, length, None, nucleus_at
        if next_ch and self._e(e, "silent_before_consonant"):
            return readings, length, None, nucleus_at
        vowel, bit = inherent["vowel"], "vowel_inherent"
        if not next_ch and "final" in inherent and self._syllable_has_nucleus(tokens):
            vowel, bit = inherent["final"], "vowel_inherent_final"
        return tuple(r + vowel for r in readings), length, self._e(e, bit), nucleus_at

    def _consonant_nucleus_at(self, text: str, pos: int, tokens: List[Token]) -> int:
        """3.3.2 item 5: the offset of a consonant letter at *pos* that is the
        nucleus between an onset with no vowel and a coda, or -1."""
        if not self._nuclei or self._syllable_has_nucleus(tokens):
            return -1
        pos = self._skip_silent_marks(text, pos)
        letter = self._longest_match(text, pos)
        if letter not in self._nuclei:
            return -1
        close = self._skip_silent_marks(text, pos + len(letter))
        coda = self._longest_match(text, close)
        coda_ipa = self.entries[self._key_index[coda]]["cands"] if coda else None
        if (not coda_ipa or not coda_ipa[0] or self._is_nucleus(coda_ipa[0])
                or self._supplies_vowel_at(text, close + len(coda))):
            return -1
        return pos

    def _skip_silent_marks(self, text: str, pos: int) -> int:
        while pos < len(text) and self._c(text[pos], "mark_spells_nothing"):
            pos += 1
        return pos

    def _unfuse_nucleus(self, text: str, pos: int, gkey: str, tokens: List[Token]) -> str:
        """A cluster key that ends in a consonant nucleus backs off to its head
        when the letter is the nucleus."""
        cands = self.entries[self._key_index[gkey]]["cands"]
        if not cands or self._is_nucleus(cands[0]):
            return gkey
        for letter in self._nuclei:
            head = gkey[:-len(letter)]
            if (head and gkey.endswith(letter) and head in self._trie_keys
                    and self._consonant_nucleus_at(text, pos + len(head), tokens) == pos + len(head)):
                return head
        return gkey

    def _preposed(self, text: str, pos: int, gkey: str, tokens: List[Token]) -> Optional[int]:
        """3.3.2 item 1: a vowel written before its consonant and read after it.
        Appends the silent vowel token and the consonant token, and returns
        the position after them, or None when no consonant can host the vowel."""
        after = pos + len(gkey)
        ckey = self._longest_match(text, after)
        if ckey is None:
            return None
        c = self._key_index[ckey]
        if self._e(c, "silent_head") and self._head_is_the_onset(gkey, c, text, after):
            ckey = ckey[0]
            c = self._key_index[ckey]
        if not self._e(c, "preposed_host"):
            return None
        e = self._key_index[gkey]
        host = tuple(self.entries[c].get("onset") or self.entries[c]["cands"])
        post = after + len(ckey)
        pkey, pend = self._match_transparent(text, post)
        tail = pkey is not None and self._e(self._key_index[pkey], "circumfix_tail")
        readings = host if tail else tuple(r + v for r in host for v in self.entries[e]["cands"])
        tokens.append(Token(WORD, gkey, e, (), pos, len(gkey)))
        tokens.append(Token(WORD, ckey, c, readings, after, len(ckey)))
        if not tail:
            return post
        if pend > post:
            p = self._key_index[pkey]
            tokens.append(Token(WORD, text[post:pend], p, tuple(self.entries[p]["cands"]), post, pend - post))
            return pend
        return post

    def _head_is_the_onset(self, gkey: str, c: int, text: str, after: int) -> bool:
        """The silent head of the host is the onset when the vowel ends open and
        nothing audible follows the tail."""
        if not self._e(self._key_index[gkey], "preposed_open") or self._e(c, "head_not_coda"):
            return False
        pos = after + len(self.entries[c]["key"])
        first = True
        while pos < len(text):
            nkey = self._longest_match(text, pos)
            if nkey is None:
                return not self._c(text[pos], "alpha")
            n = self._key_index[nkey]
            if self._e(n, "audible") or first and self._e(n, "spells_nothing"):
                return False
            first = False
            pos += len(nkey)
        return True

    def _match_transparent(self, text: str, start: int) -> Tuple[Optional[str], int]:
        """Longest trie match at *start* that steps over chars with bit
        ``mark_spells_nothing`` once the match has begun."""
        node = self._trie
        best, best_end, i = None, start, start
        while i < len(text):
            ch = text[i]
            ch = self._casefold.get(ch, ch)
            if len(ch) == 1 and ch in node:
                node = node[ch]
                i += 1
                if "" in node:
                    best, best_end = node[""], i
            elif i > start and self._c(text[i], "mark_spells_nothing"):
                i += 1
            else:
                break
        return best, best_end

    def _supplies_vowel_at(self, text: str, pos: int) -> bool:
        while pos < len(text) and self._c(text[pos], "mark_spells_nothing"):
            pos += 1
        for sign, supplies in (self._inherent or {}).get("signs", ()):
            if text.startswith(sign, pos):
                return bool(supplies)
        return pos < len(text) and self._c(text[pos], "supplies_vowel")

    def _is_nucleus(self, ipa: str) -> bool:
        return any(self._c(c, "ipa_vowel") or self._c(c, "syllabic_mark") for c in ipa)

    def _syllable_has_nucleus(self, tokens: List[Token]) -> bool:
        for tok in reversed(tokens):
            if tok.kind != WORD:
                return False
            first = tok.readings[0] if tok.readings else ""
            if list(tok.readings) == [""] and self._e(tok.entry, "spells_nothing"):
                continue
            if self._e(tok.entry, "vowel_sign") or first and self._is_nucleus(first):
                return True
            if first and self._e(tok.entry, "postvocalic"):
                continue
            return False
        return False

    def _backoff(self, text: str, pos: int, gkey: str, tokens: List[Token]) -> str:
        n = len(text)
        if self._hiatus_on and len(gkey) > 1 and self._c(gkey[0], "orth_vowel"):
            gkey = self._hiatus_prefix(text, pos, gkey)
        e = self._key_index[gkey]
        if self._e(e, "prevocalic_backoff") and pos + len(gkey) < n and self._c(text[pos + len(gkey)], "orth_vowel"):
            gkey = gkey[:-1]
            e = self._key_index[gkey]
        if self._e(e, "glide_final_key"):
            after = pos + len(gkey)
            next_ch = text[after] if after < n else ""
            if (next_ch and self._c(next_ch, "elision_apostrophe") and after + 1 < n
                    and self._c(text[after + 1], "alpha")):
                after += 1
                low = text[after]
                low = self._casefold.get(low, low)
                silent = low in self._trie_keys and self.entries[self._key_index[low]]["cands"] == [""]
                if silent and after + 1 < n and self._c(text[after + 1], "alpha"):
                    after += 1
                next_ch = text[after]
            nlow = self._casefold.get(next_ch, next_ch) if next_ch else ""
            if not (next_ch and self._c(next_ch, "orth_vowel")):
                bit = "glide_vowel_cons" if next_ch else "glide_vowel_final"
                if not self._e(e, bit):
                    gkey = gkey[:-1]
            elif not (len(nlow) == 1 and self._c(nlow, "front_letter")):
                prev = next((t for t in reversed(tokens) if t.kind == WORD), None)
                prev_ipa = prev.readings[0] if prev and prev.readings else ""
                prev_is_vowel = bool(prev_ipa) and self._c(prev_ipa[-1], "ipa_vowel")
                if prev_is_vowel and self._e(e, "glide_marker") and gkey[-1] + nlow in self._trie_keys:
                    gkey = gkey[:-1]
        return gkey

    def _hiatus_prefix(self, text: str, pos: int, gkey: str) -> str:
        start = pos
        while start and self._c(text[start - 1], "letter_or_mark"):
            start -= 1
        end = pos
        while end < len(text) and self._c(text[end], "letter_or_mark"):
            end += 1
        word = text[start:end]
        hiatus = self._hiatus_cache.get(word)
        if hiatus is None:
            hiatus = self._hiatus_cache[word] = self.hiatus_positions(word)
        for cut in range(1, len(gkey)):
            if pos - start + cut in hiatus and gkey[:cut] in self._trie_keys:
                return gkey[:cut]
        return gkey

    def grapheme_tokens(self, word: str) -> List[Token]:
        return [t for t in self.tokenize(word) if t.kind == WORD]

    # ─── S2: words ───────────────────────────────────────────────────
    def _group_words(self, text: str, words: List[_Word], lexicon) -> None:
        tokens = self.tokenize(text)
        current: List[str] = []
        joined = after_hyphen = False

        def flush():
            if current:
                words.append(_Word("".join(current), joined))
                current.clear()

        for token in tokens:
            if token.kind == WS:
                flush()
                after_hyphen = False
            elif token.kind == PUNCT and self._internal_apostrophe(text, token):
                current.append(token.grapheme)
            elif token.kind == PUNCT and self._opens_listed_word(text, token, lexicon):
                flush()
                joined, after_hyphen = after_hyphen, False
                current.append(token.grapheme)
            elif token.kind == PUNCT:
                after_hyphen = bool(current) and len(token.grapheme) == 1 and self._c(token.grapheme, "hyphen")
                flush()
                if words and any(self._c(c, "pause") for c in token.grapheme):
                    words[-1].pausal = True
            else:
                tail = text[token.position:token.position + token.length][len(token.grapheme):]
                if not current:
                    joined, after_hyphen = after_hyphen, False
                current.append(token.grapheme + tail)
        flush()

    def _apostrophe_token(self, token: Token) -> bool:
        return len(token.grapheme) == 1 and self._c(token.grapheme, "apostrophe")

    def _internal_apostrophe(self, text: str, token: Token) -> bool:
        start, end = token.position, token.position + token.length
        return (bool(self.word["internal_apostrophe"]) and self._apostrophe_token(token)
                and 0 < start and end < len(text)
                and self._c(text[start - 1], "alpha") and self._c(text[end], "alpha"))

    def _opens_listed_word(self, text: str, token: Token, lexicon) -> bool:
        start, end = token.position, token.position + token.length
        if not (self.word["internal_apostrophe"] and self._apostrophe_token(token)
                and (start == 0 or self._c(text[start - 1], "whitespace"))):
            return False
        stop = self._run(text, end, "word_letter")
        if stop == end:
            return False
        key = self.casefold("'" + text[end:stop])
        return (key in self._exceptions or (lexicon is not None and self.nfc(key) in lexicon)
                or self.nfc(key) in self._fragment_words)

    # ─── S3: overrides ───────────────────────────────────────────────
    def _strip_edges(self, key: str) -> str:
        i, j = 0, len(key)
        while i < j and self._c(key[i], "edge_punct"):
            i += 1
        if i == j:
            return ""
        while j > i and self._c(key[j - 1], "edge_punct"):
            j -= 1
        return key[i:j]

    def _whole_word_override(self, word: str, lexicon) -> Optional[str]:
        marks = self.word["silent_stress_marks"]
        key = self.casefold("".join(c for c in word if c not in marks))
        keys = [key]
        stripped = self._strip_edges(key)
        if stripped and stripped != key:
            keys.append(stripped)
        if self.word["internal_apostrophe"]:
            keys += [k.replace("’", "'") for k in keys if "’" in k]
        for k in keys:
            hit = self._exceptions.get(k)
            if hit is not None:
                return hit
            if lexicon:
                hit = lexicon.get(self.nfc(k))
                if hit is not None:
                    return hit
            hit = self._fragment_words.get(self.nfc(k))
            if hit is not None:
                return hit
        return None

    def _elided_hosts(self, word: str) -> List[Tuple[int, str]]:
        if not (self.word["apostrophe_elision"] and self.word["internal_apostrophe"]) \
                or not any(self._c(c, "apostrophe") for c in word):
            return []
        tokens = self.grapheme_tokens(word)
        splits = []
        for i, mark in enumerate(word):
            if not self._c(mark, "apostrophe") or not 0 < i < len(word) - 1:
                continue
            host = word[i + 1:]
            before = [t.grapheme for t in tokens if t.position < i]
            if (self._c(word[i - 1], "alpha") and before
                    and not self._c(before[-1][0], "orth_vowel")
                    and (self._c(host[0], "orth_vowel") or self._c(host[0], "elision_h"))):
                splits.append((i, host))
        return splits

    def _override_for(self, word: str, lexicon) -> Optional[str]:
        override = self._whole_word_override(word, lexicon)
        if override is not None:
            return override
        for apostrophe, host in self._elided_hosts(word):
            host_ipa = self._whole_word_override(host, lexicon)
            if host_ipa is not None:
                return self._join_clitic(self._clitic_ipa(word, apostrophe), host_ipa)
        return None

    def _join_clitic(self, clitic: str, host_ipa: str) -> str:
        if host_ipa[:1] not in self.word["clitic_marks"]:
            return clitic + host_ipa
        if not any(self._c(c, "ipa_vowel") for c in clitic):
            return host_ipa[0] + clitic + host_ipa[1:]
        segments = self.segment(clitic, self._affricates)
        if self._c(segments[-1][0], "ipa_vowel"):
            return clitic + host_ipa
        return "".join(segments[:-1]) + host_ipa[0] + segments[-1] + host_ipa[1:]

    def _clitic_ipa(self, word: str, apostrophe: int) -> str:
        paths = self._word_paths(word, 1)
        if not paths:
            return ""
        count = sum(1 for t in self.grapheme_tokens(word) if t.position < apostrophe)
        return "".join(paths[0][0][:count])

    def _is_cliticless(self, word: str, elided: bool = True) -> bool:
        if not self.stress or not self._cliticless:
            return False
        key = self.nfc(self.casefold(word))
        if key in self._cliticless:
            return True
        stripped = self._strip_edges(key)
        if stripped and stripped != key and stripped in self._cliticless:
            return True
        return elided and any(self._is_cliticless(host, elided=False)
                              for _, host in self._elided_hosts(word))

    # ─── predicates (primitive 5) ────────────────────────────────────
    def _eval(self, p: list, ctx: _Ctx, i: int) -> bool:
        op = p[0]
        if op == "and":
            return all(self._eval(q, ctx, i) for q in p[1:])
        if op == "or":
            return any(self._eval(q, ctx, i) for q in p[1:])
        if op == "not":
            return not self._eval(p[1], ctx, i)
        if op == "true":
            return True
        if op == "false":
            return False
        n = len(ctx.entries)
        if op == "exists":
            return 0 <= i + p[1] < n
        if op == "ebit":
            j = i + p[1]
            return 0 <= j < n and bool(self._slot_bits(ctx, j) & (1 << p[2]))
        if op == "entry_in":
            j = i + p[1]
            return 0 <= j < n and self.entries[ctx.entries[j]]["key"] in p[2]
        if op == "syll":
            return self._syll(p[1], ctx, i)
        if op == "syllpos":
            j = i + p[1]
            return 0 <= j < n and self._syllable_position(ctx, j) == p[2]
        if op == "word_in":
            return self.lower(ctx.source) in p[1]
        if op == "word_has":
            word = self.lower(ctx.source)
            return any(g in word for g in p[1])
        if op == "word_final":
            if i + 1 >= n:
                return True
            if ctx.cands is None:
                return False
            return all(not ctx.cands[j] or ctx.cands[j][0][0] == "" for j in range(i + 1, n))
        if op == "top_seg_in":
            j = i + p[1]
            if not 0 <= j < n or not ctx.cands[j] or not ctx.cands[j][0][0]:
                return False
            segs = self.segment(ctx.cands[j][0][0], self._allo["atoms"])
            return segs[-1 if p[2] else 0] in p[3]
        if op == "top_nucleus":
            js = range(i + 1, n) if p[1] == "later" else (j for j in range(n) if j != i)
            return any(ctx.cands[j] and any(
                self._c(seg[0], "nucleus_base") or any(self._c(c, "syllabic") for c in seg)
                for seg in self.segment(ctx.cands[j][0][0])) for j in js)
        if op == "top_in":
            j = i + p[1]
            return 0 <= j < n and bool(ctx.cands[j]) and ctx.cands[j][0][0] in p[2]
        if op == "count":
            lo = 0 if p[1] == "start" else max(0, i + p[1])
            hi = n - 1 if p[2] == "end" else min(n - 1, i + p[2])
            skip = i if p[5:] == ["others"] else -1
            hits = sum(1 for j in range(lo, hi + 1) if j != skip and self._eval(p[3], ctx, j))
            return hits >= p[4]
        if op == "reading_vowel":
            j = i + p[1]
            if not 0 <= j < n:
                return False
            readings = ctx.tokens[j].readings
            return bool(readings) and any(self._c(c, "ipa_vowel") for c in readings[0])
        if op == "word_has_entry":
            return any(self.entries[e]["key"] in p[1] for e in ctx.entries)
        raise ValueError(f"unknown predicate node {op!r}")

    def _syll(self, rel: str, ctx: _Ctx, i: int) -> bool:
        if rel in ("open", "closed"):
            status = ctx.aperture[i] if ctx.aperture is not None else None
            return status is not None and status == (rel == "open")
        idx = ctx.syll_idx[i] if ctx.syll_idx is not None else None
        st = ctx.stressed
        if rel == "has_stress":
            return st is not None and idx is not None
        if st is None or idx is None:
            return False
        if rel == "idx_eq_stressed":
            return idx == st
        if rel == "idx_lt_stressed":
            return idx < st
        if rel == "idx_gt_stressed":
            return idx > st
        if rel == "idx_eq_stressed_minus_1":
            return idx == st - 1
        if rel == "idx_in_secondary":
            return idx in ctx.secondary
        raise ValueError(f"unknown syll relation {rel!r}")

    def _syllable_position(self, ctx: _Ctx, j: int) -> str:
        if self._slot_bits(ctx, j) & self._ebit["vowel"]:
            return "nucleus"
        k = j + 1
        while k < len(ctx.entries) and self._e(ctx.entries[k], "spells_nothing"):
            k += 1
        if k < len(ctx.entries) and self._slot_bits(ctx, k) & self._ebit["vowel"]:
            return "onset"
        return "coda"

    # ─── S6: positional candidates; 3.3.5 candidate lists ────────────
    def _branches(self, ctx: _Ctx, i: int, token: Token) -> List[Tuple[str, int]]:
        entry = self.entries[ctx.entries[i]]
        base = list(token.readings)
        for pred, cands in entry.get("positional", ()):
            if self._eval(pred, ctx, i):
                seen = set(cands)
                candidates = list(cands) + [c for c in base if c not in seen]
                costs = [r * 1_000_000 for r in range(len(candidates))]
                break
        else:
            candidates = base
            costs = entry["costs"] if token.readings == tuple(entry["cands"]) else \
                [r * 1_000_000 for r in range(len(candidates))]
        branches: List[Tuple[str, int]] = []
        amap = self._allophone_map
        for rank, ipa in enumerate(candidates):
            if amap and ipa in amap:
                for a_rank, allophone in enumerate(amap[ipa]):
                    branches.append((allophone, costs[rank] + 500_000 * a_rank))
            else:
                branches.append((ipa, costs[rank]))
        best: Dict[str, int] = {}
        for ipa, cost in branches:
            if ipa not in best or cost < best[ipa]:
                best[ipa] = cost
        return sorted(best.items(), key=lambda x: (x[1], x[0]))

    # ─── S7: allophony ───────────────────────────────────────────────
    def _rescore_pass(self, runs: List[Tuple[int, int]], tokens: List[Token], entries: List[int],
                      cands: List[List[Tuple[str, int]]], syll_idx, stressed, secondary) -> List[list]:
        out = list(cands)
        for start, end in runs:
            ctx = _Ctx(entries[start:end], tokens[start:end],
                       syll_idx[start:end] if syll_idx is not None else None, stressed, secondary,
                       cands=cands[start:end], source="".join(t.grapheme for t in tokens[start:end]))
            for local in range(end - start):
                new = self._rescore_slot(ctx, local)
                if new is not None:
                    out[start + local] = sorted(new, key=lambda c: (c[1], c[0]))
        return out

    def _rescore_slot(self, ctx: _Ctx, i: int) -> Optional[List[Tuple[str, int]]]:
        new = None
        for idx, (ipa, cost) in enumerate(ctx.cands[i]):
            surface = self._realize(ipa, ctx, i)
            if surface is not None and surface != ipa:
                if new is None:
                    new = list(ctx.cands[i])
                new[idx] = (surface, cost)
        feature = self._neighbor_mutation(ctx, i)
        if feature:
            base = new if new is not None else list(ctx.cands[i])
            mutated = [(ipa + feature, cost) if ipa and feature not in ipa else (ipa, cost)
                       for ipa, cost in base]
            if mutated != base:
                new = mutated
        return new

    def _neighbor_mutation(self, ctx: _Ctx, i: int) -> Optional[str]:
        for step in (1, -1):
            j = i + step
            if not 0 <= j < len(ctx.entries) or not ctx.cands[j]:
                continue
            ipa = ctx.cands[j][0][0]
            marker = None
            for rule in self._allo["rules"]:
                if rule.get("mutate_at") != step or ipa not in rule["phonemes"]:
                    continue
                if marker is None:
                    marker = ctx
                    if ctx.syll_idx is not None:
                        syll_idx = list(ctx.syll_idx)
                        syll_idx[j] = ctx.syll_idx[i]
                        marker = replace(ctx, syll_idx=syll_idx)
                if self._eval(rule["when"], marker, j):
                    return rule["mutate"]
        return None

    def _twin_side(self, ipa: str, ctx: _Ctx, i: int) -> Optional[int]:
        if not self._allo["geminate"]:
            return None
        if not ipa or any(self._c(seg[0], "ipa_vowel") for seg in self.segment(ipa)):
            return None
        own = self.lower(ctx.tokens[i].grapheme)
        for step in (1, -1):
            j = i + step
            if not 0 <= j < len(ctx.entries):
                continue
            if not ctx.cands[j] or ctx.cands[j][0][0] != ipa:
                continue
            if own != self.lower(ctx.tokens[j].grapheme):
                continue
            a, b = ctx.tokens[i], ctx.tokens[j]
            near = (a.position, a.position + a.length)
            far = (b.position, b.position + b.length)
            if near[1] == far[0] or far[1] == near[0]:
                return step
        return None

    def _heterosyllabic(self, ctx: _Ctx, i: int, step: int) -> bool:
        before, after = i - step, i + 2 * step
        n = len(ctx.entries)
        vowel = self._ebit["vowel"]
        return bool(0 <= before < n and self._slot_bits(ctx, before) & vowel
                    and 0 <= after < n and self._slot_bits(ctx, after) & vowel)

    def _realize(self, ipa: str, ctx: _Ctx, i: int) -> Optional[str]:
        twin = self._twin_side(ipa, ctx, i)
        for rule in self._allo["rules"]:
            if ipa in rule["phonemes"] and self._eval(rule["when"], ctx, i):
                k = rule["phonemes"].index(ipa)
                if twin is not None and not rule["aware"][k] and not (
                        rule["trig_next" if twin > 0 else "trig_prev"]
                        and self._heterosyllabic(ctx, i, twin)):
                    continue
                return rule["out"][k]
        segments = self.segment(ipa, self._allo["atoms"])
        if len(segments) <= 1:
            return None
        return self._realize_segments(segments, ctx, i)

    def _realize_segments(self, segments: List[str], ctx: _Ctx, i: int) -> Optional[str]:
        changed = False
        out: List[str] = []
        inserted: Optional[_Ctx] = None
        for k, seg in enumerate(segments):
            slot_ctx = ctx
            if self._c(seg[0], "ipa_vowel") and not self._holds_vowel(ctx, i):
                if inserted is None:
                    inserted = self._inserted_vowel_context(ctx, i)
                slot_ctx = inserted
            surface = self._realize_one_segment(seg, segments, k, ctx, i, slot_ctx)
            if surface is not None and surface != seg:
                changed = True
                out.append(surface)
            else:
                out.append(seg)
        return "".join(out) if changed else None

    def _holds_vowel(self, ctx: _Ctx, i: int) -> bool:
        return self._e(ctx.entries[i], "holds_vowel") or any(
            self._c(c, "ipa_vowel") for r in ctx.tokens[i].readings for c in r)

    def _inserted_vowel_context(self, ctx: _Ctx, i: int) -> _Ctx:
        """The slot context of a vowel a rule inserted: its own unstressed
        syllable after the nearest earlier slot that holds a vowel."""
        if ctx.syll_idx is None or ctx.stressed is None:
            return ctx
        before = -1
        for step in range(1, i + 1):
            if self._holds_vowel(ctx, i - step):
                before = ctx.syll_idx[i - step]
                break
        syll_idx = list(ctx.syll_idx)
        syll_idx[i] = before + 1
        stressed = ctx.stressed + 1 if ctx.stressed > before else ctx.stressed
        return replace(ctx, syll_idx=syll_idx, stressed=stressed)

    def _realize_one_segment(self, seg: str, segments: List[str], k: int, ctx: _Ctx, i: int,
                             slot_ctx: _Ctx) -> Optional[str]:
        atoms = self._allo["atoms"]
        n = len(ctx.entries)
        if k > 0:
            prev = segments[k - 1]
        elif i > 0 and ctx.cands[i - 1]:
            prev_segs = self.segment(ctx.cands[i - 1][0][0], atoms)
            prev = prev_segs[-1] if prev_segs else None
        else:
            prev = None
        if k < len(segments) - 1:
            nxt = segments[k + 1]
        elif i + 1 < n and ctx.cands[i + 1]:
            next_segs = self.segment(ctx.cands[i + 1][0][0], atoms)
            nxt = next_segs[0] if next_segs else None
        else:
            nxt = None
        initial = i == 0 and k == 0
        final = self._eval(["word_final"], ctx, i) and k == len(segments) - 1
        for rule in self._allo["rules"]:
            seg_rule = rule.get("seg")
            if seg_rule is None or seg not in rule["phonemes"]:
                continue
            if seg_rule["initial"] >= 0 and bool(seg_rule["initial"]) != initial:
                continue
            if seg_rule["final"] >= 0 and bool(seg_rule["final"]) != final:
                continue
            if seg_rule["prev"] and (prev is None or prev not in seg_rule["prev"]):
                continue
            if seg_rule["next"] and (nxt is None or nxt not in seg_rule["next"]):
                continue
            if self._eval(rule["slot_when"], slot_ctx, i):
                return rule["out"][rule["phonemes"].index(seg)]
        return None

    # ─── S8: the beam ────────────────────────────────────────────────
    def _carrier_split(self, seg: str) -> int:
        j = len(seg)
        while j > 0 and (self._c(seg[j - 1], "length")
                         or (seg[j - 1] != self._tilde and self._comb(seg[j - 1]))):
            j -= 1
        return j

    def _carrier_tail(self, seg: str) -> str:
        j = self._carrier_split(seg)
        return seg[j - 1] if j > 0 else ""

    def _is_carrier(self, ch: str) -> bool:
        return ch != "" and self._c(ch, "nasal_carrier")

    def _splice(self, segs: List[str]) -> List[str]:
        new = list(segs)
        for i in range(len(new) - 1, -1, -1):
            if new[i]:
                j = self._carrier_split(new[i])
                new[i] = new[i][:j] + self._tilde + new[i][j:]
                new.append("")
                return new
        new.append(self._tilde)
        return new

    def _constrain_nasal_carriers(self, slots: List[List[Tuple[str, int]]]) -> None:
        for idx in range(1, len(slots)):
            branches = slots[idx]
            if not branches or any(ipa != self._tilde for ipa, _ in branches):
                continue
            j = idx - 1
            while j >= 0:
                prev = slots[j]
                if not prev:
                    break
                has_empty = any(not ipa for ipa, _ in prev)
                kept = [(ipa, c) for ipa, c in prev if not ipa or self._is_carrier(self._carrier_tail(ipa))]
                if kept and len(kept) != len(prev):
                    slots[j] = kept
                if not has_empty:
                    break
                j -= 1

    def _expand(self, beam, branches, width: int):
        new = []
        for segs, sc in beam:
            for ipa, cost in branches:
                if ipa == self._tilde:
                    tail = ""
                    for seg in reversed(segs):
                        if seg:
                            tail = self._carrier_tail(seg)
                            break
                    if tail == self._tilde:
                        new.append((segs + [""], sc + cost))
                        continue
                    if not self._is_carrier(tail):
                        continue
                    new.append((self._splice(segs), sc + cost))
                    continue
                new.append((segs + [ipa], sc + cost))
        if not new:
            for segs, sc in beam:
                for ipa, cost in branches:
                    if ipa == self._tilde:
                        new.append((self._splice(segs), sc + cost))
                    else:
                        new.append((segs + [ipa], sc + cost))
        new.sort(key=lambda x: x[1])
        return new[:width]

    def _slots(self, word: str, context: bool, allophony: bool = True):
        """The grapheme tokens of *word* and each one's S6 candidates, after
        S7 when *allophony* holds. *context* gives the slots the word's stress
        and syllable context; without it the slots read their runs alone."""
        tokens = self.tokenize(word)
        g_tokens = [t for t in tokens if t.kind == WORD]
        entries = [t.entry for t in g_tokens]
        syll_idx = None
        stressed: Optional[int] = None
        secondary: FrozenSet[int] = frozenset()
        aperture = None
        if context and g_tokens:
            runs = [(0, len(g_tokens))]
            sylls: List[str] = []
            if self.stress is not None or "silent_tail" in self.syll:
                sylls = self.syllables(word)
            if self.stress is not None:
                stressed = self.detect_stress(word, sylls) if len(sylls) > 1 else 0
                if self._is_cliticless(word):
                    stressed = _NO_STRESS
                secondary = self.secondary_positions(len(sylls), stressed)
            syll_idx = self._map_tokens_to_syllables(g_tokens, sylls)
            if "silent_tail" in self.syll:
                aperture = self._aperture(sylls, syll_idx)
        else:
            runs = []
            start = 0
            g = 0
            for t in tokens:
                if t.kind == WORD:
                    g += 1
                elif g > start:
                    runs.append((start, g))
                    start = g
            if g > start:
                runs.append((start, g))
        cands: List[List[Tuple[str, int]]] = [[] for _ in g_tokens]
        for start, end in runs:
            ctx = _Ctx(entries[start:end], g_tokens[start:end],
                       syll_idx[start:end] if syll_idx is not None else None, stressed, secondary,
                       aperture[start:end] if aperture is not None else None)
            for local in range(end - start):
                cands[start + local] = self._branches(ctx, local, g_tokens[start + local])
        if self.hooks.rescore is not None and g_tokens:
            cands = [sorted(slot, key=lambda c: (c[1], c[0]))
                     for slot in self.hooks.rescore(word, g_tokens, cands, syll_idx, stressed)]
        if self._allo and allophony:
            for _ in range(self._allo["passes"]):
                cands = self._rescore_pass(runs, g_tokens, entries, cands, syll_idx, stressed, secondary)
        return g_tokens, cands

    def lattice(self, word: str) -> List[Tuple[Token, List[Tuple[str, int]]]]:
        """Each grapheme slot of *word* that sounds, with its ranked candidates,
        in the word's stress and syllable context."""
        g_tokens, cands = self._slots(word, context=True)
        return [(t, c) for t, c in zip(g_tokens, cands) if c]

    def _word_paths(self, word: str, width: int, context: Optional[bool] = None,
                    allophony: bool = True):
        """Beam paths of *word*: [(segments, cost, graphemes)], best first."""
        if context is None:
            context = bool(self.word["context_beam"])
        g_tokens, cands = self._slots(word, context, allophony)
        self._constrain_nasal_carriers(cands)
        beam = [([], 0)]
        spelled = []
        for i, branches in enumerate(cands):
            if not branches:
                continue
            spelled.append(g_tokens[i].grapheme)
            beam = self._expand(beam, branches, width)
        paths = [(tuple(segs), sc, tuple(spelled)) for segs, sc in beam]
        paths.sort(key=lambda p: (p[1], "".join(p[0])))
        return paths

    # ─── S5: written syllables, hiatus, the stress decision ──────────
    def _strip_silent_tail(self, syllable: str) -> str:
        tail = self.syll["silent_tail"]
        changed = True
        while changed and syllable:
            changed = False
            for size in range(min(3, len(syllable)), 0, -1):
                if self.lower(syllable[-size:]) in tail:
                    syllable = syllable[:-size]
                    changed = True
                    break
        return syllable

    def _trim_edge(self, syllable: str) -> Tuple[str, bool]:
        trimmed = False
        while syllable and not (self._c(syllable[-1], "alpha") or self._comb(syllable[-1])):
            syllable = syllable[:-1]
            trimmed = True
        return syllable, trimmed

    def _aperture(self, sylls: List[str], syll_idx: List[Optional[int]]) -> List[Optional[bool]]:
        merged = list(sylls)
        if len(merged) >= 2:
            core = self._strip_silent_tail(self._trim_edge(merged[-1])[0])
            if not (core and any(self._c(ch, "orth_vowel") for ch in core)):
                merged = merged[:-2] + [merged[-2] + merged[-1]]
        out: List[Optional[bool]] = []
        for idx in syll_idx:
            if idx is not None and len(merged) < len(sylls):
                idx = min(idx, len(merged) - 1)
            if idx is None or not 0 <= idx < len(merged):
                out.append(None)
                continue
            syllable, final = self._trim_edge(merged[idx])
            if final or idx == len(merged) - 1:
                syllable = self._strip_silent_tail(syllable)
            if not syllable or not any(self._c(ch, "orth_vowel") for ch in syllable):
                out.append(None)
            else:
                out.append(self._c(syllable[-1], "orth_vowel"))
        return out

    def _map_tokens_to_syllables(self, tokens: List[Token], sylls: List[str]) -> List[int]:
        if not sylls:
            return [0] * len(tokens)
        owner: List[int] = []
        for idx, syll in enumerate(sylls):
            owner.extend([idx] * len(syll))
        fold = lambda text: "".join(self._lower.get(c, c) if len(self._lower.get(c, c)) == 1 else c  # noqa: E731
                                    for c in text)
        folded = fold("".join(sylls))
        result: List[int] = []
        cursor = 0
        for token in tokens:
            at = folded.find(fold(token.grapheme), cursor) if token.grapheme else -1
            if at < 0:
                result.append(result[-1] if result else 0)
                continue
            result.append(owner[at] if at < len(owner) else len(sylls) - 1)
            cursor = at + len(token.grapheme)
        return result

    def _known_only(self, word: str) -> str:
        return "".join(c for c in word if self._c(c, "known"))

    def syllables(self, word: str) -> List[str]:
        sylls = self._syll_cache.get(word)
        if sylls is None:
            if self.hooks.syllables is not None:
                sylls = self.hooks.syllables(word)
            if not sylls:
                written = self._known_only(word)
                sylls = self._bundled(written, self.hiatus_positions(written))
            self._syll_cache[word] = sylls
        return list(sylls)

    def _nucleus_mask(self, word: str, semivowels: Mapping[str, str],
                      vowels: Optional[FrozenSet[str]] = None) -> List[bool]:
        fixed: List[Optional[bool]] = []
        for ch in word:
            role = semivowels.get(self.lower(ch))
            if self._comb(ch):
                fixed.append(False)
            elif role is None:
                fixed.append(self.lower(ch) in vowels if vowels is not None else self._vowel_char(ch))
            elif role == "contextual":
                fixed.append(None)
            else:
                fixed.append(role == "nucleus")
        mask: List[bool] = []
        for i, status in enumerate(fixed):
            if status is None:
                before = next((fixed[k] for k in range(i - 1, -1, -1) if not self._comb(word[k])), False)
                after = next((fixed[k] for k in range(i + 1, len(word)) if not self._comb(word[k])), False)
                status = not (before or after)
            mask.append(status)
        return mask

    def _split_nuclei(self, run: str, diphthongs: Sequence[str], hiatus: FrozenSet[int] = frozenset()) -> List[str]:
        if len(run) < 2:
            return [run]
        ordered = sorted(diphthongs, key=len, reverse=True)
        lowered = self.lower(run)
        nuclei: List[str] = []
        i = 0
        while i < len(run):
            for diph in ordered:
                if lowered.startswith(diph, i) and not any(i < h < i + len(diph) for h in hiatus):
                    nuclei.append(run[i:i + len(diph)])
                    i += len(diph)
                    break
            else:
                nuclei.append(run[i])
                i += 1
            while i < len(run) and (self._comb(run[i]) or run[i] == "ː"):
                if nuclei:
                    nuclei[-1] += run[i]
                else:
                    nuclei.append(run[i])
                i += 1
        return nuclei

    def _with_diphthongs(self, word: str, nucleus: Sequence[bool], diphthongs: Sequence[str],
                         onset_graphemes: Sequence[str] = (), hiatus: FrozenSet[int] = frozenset()) -> List[str]:
        syllables: List[str] = []
        onset = ""
        i = 0
        while i < len(word):
            if onset and i + 1 < len(word) and nucleus[i + 1] and any(
                    g[-1] == self.lower(word[i]) and self.lower(onset[len(onset) - len(g) + 1:]) == g[:-1]
                    for g in onset_graphemes):
                onset += word[i]
                i += 1
                continue
            if not nucleus[i]:
                onset += word[i]
                i += 1
                while i < len(word) and self._comb(word[i]):
                    onset += word[i]
                    i += 1
                continue
            j = i
            while j < len(word) and (nucleus[j] or self._comb(word[j]) or word[j] == "ː"):
                j += 1
            run_hiatus = frozenset(h - i for h in hiatus if i < h < j)
            for k, piece in enumerate(self._split_nuclei(word[i:j], diphthongs, run_hiatus)):
                syllables.append((onset if k == 0 else "") + piece)
            onset = ""
            i = j
        if onset:
            if syllables:
                syllables[-1] += onset
            else:
                syllables.append(onset)
        return syllables

    def _vowel_groups(self, word: str, nucleus: Sequence[bool]) -> List[str]:
        syllables: List[str] = []
        current = ""
        current_start = 0
        in_nucleus = False
        for i, ch in enumerate(word):
            if self._comb(ch) or ch == "ː":
                current += ch
                continue
            is_vowel = nucleus[i]
            if is_vowel and not in_nucleus and current and any(nucleus[current_start:i]):
                syllables.append(current)
                current, current_start = ch, i
            elif not is_vowel and in_nucleus:
                syllables.append(current)
                current, current_start = ch, i
            else:
                current += ch
            in_nucleus = is_vowel
        if current:
            if any(nucleus[current_start:]) or not syllables:
                syllables.append(current)
            else:
                syllables[-1] += current
        return syllables

    def _bundled(self, word: str, hiatus: FrozenSet[int]) -> List[str]:
        if not word:
            return []
        nucleus = self._nucleus_mask(word, self._semivowels, self._vowel_letters)
        diphthongs = self.syll.get("diphthongs", ())
        if diphthongs:
            sylls = self._with_diphthongs(word, nucleus, diphthongs,
                                          self.syll.get("onset_graphemes", ()), hiatus)
        else:
            sylls = self._vowel_groups(word, nucleus)
        if self._onsets:
            return self._rebalance(sylls, nucleus, self._written_units, self._licit_written_onset)
        return sylls

    def _written_units(self, run: str) -> List[str]:
        out: List[str] = []
        i = 0
        while i < len(run):
            for g in self._onsets["units"]:
                if len(g) <= len(run) - i and self.lower(run[i:i + len(g)]) == g:
                    out.append(run[i:i + len(g)])
                    i += len(g)
                    break
            else:
                out.append(run[i])
                i += 1
            while i < len(run) and self._comb(run[i]):
                out[-1] += run[i]
                i += 1
        return out

    def _licit_written_onset(self, run: str) -> bool:
        if not run:
            return True
        if not all(self._c(ch, "alpha") or self._comb(ch) for ch in run):
            return False
        units = self._written_units(run)
        cap = self._onsets["max"]
        if cap >= 0 and len(units) > cap:
            return False
        if self.lower(units[0]) in self._onset_velar:
            return False
        return len(units) == 1 or tuple(self.lower(u) for u in units) in self._onset_table

    def hiatus_positions(self, word: str) -> FrozenSet[int]:
        if self.stress is None:
            return frozenset()
        found: List[int] = []
        lowered = self.lower(word)
        rule = self.syll.get("closed_hiatus")
        if rule:
            for k in range(1, len(lowered)):
                if lowered[k - 1:k + 1] not in rule["pairs"]:
                    continue
                rest = lowered[k + 1:]
                if any(rest.startswith(o) for o in rule["onsets"]) or (
                        rest[:1] in rule["codas"]
                        and not (len(rest) > 1 and self._c(rest[1], "orth_vowel"))
                        and not any(rest.startswith(g) for g in rule["multi_keys"])):
                    found.append(k)
        rule = self.syll.get("final_diphthongs")
        if rule:
            for diphthong in rule["diphthongs"]:
                for final in ("", *rule["finals"]):
                    k = len(lowered) - len(diphthong) - len(final)
                    if k >= 1 and lowered.endswith(diphthong + final) and self._c(lowered[k - 1], "orth_vowel"):
                        found.append(k)
        if not found:
            return frozenset()
        sylls = self._bundled(word, frozenset(found))
        stressed = self.detect_stress(word, sylls)
        start = sum(len(s) for s in sylls[:stressed])
        return frozenset(k for k in found if k == start)

    def secondary_positions(self, n: int, stressed: Optional[int]) -> FrozenSet[int]:
        if not self.stress["alternating"] or stressed is None or stressed < 0 or n < 3:
            return frozenset()
        return frozenset(range(stressed % 2, stressed - 1, 2))

    def detect_stress(self, word: str, sylls: Sequence[str]) -> int:
        n = len(sylls)
        if n <= 1:
            return 0
        st = self.stress
        if st["marked"]:
            marked = set(st["marked"])
            for idx, syllable in enumerate(sylls):
                if any(ch in marked for ch in syllable):
                    return idx
        lowered = self.lower(word)
        for ending in st["final"]:
            if lowered.endswith(ending):
                return n - 1
        for ending in st["penult"]:
            if lowered.endswith(ending):
                return n - 2
        for ending in st["antepenult"]:
            if lowered.endswith(ending):
                return max(0, n - 3)
        pos = st["default"]
        index = min(pos - 1, n - 1) if pos >= 1 else max(0, n + pos)
        for prefix in st.get("prefixes", ()):
            if lowered.startswith(prefix):
                inside = end = 0
                for syll in sylls:
                    end += len(syll)
                    if end > len(prefix):
                        break
                    inside += 1
                letters = [ch for ch in sylls[-1] if self._c(ch, "alpha")]
                final_open = bool(letters) and self._c(letters[-1], "orth_vowel")
                final_schwa = self._rime(self.lower(sylls[-1])) in st["schwa_rimes"]
                if index < inside < n and not (inside == n - 1 and (final_open or final_schwa)):
                    return inside
                break
        return index

    def _rime(self, syllable: str) -> str:
        for i, ch in enumerate(syllable):
            if self._c(ch, "orth_vowel"):
                return syllable[i:]
        return ""

    def _vowel_segment(self, seg: str) -> bool:
        return bool(seg) and self._c(seg[0], "ipa_vowel")

    def dock_tone_marks(self, ipa: str) -> str:
        if not any(self._c(ch, "tone_mark") for ch in ipa):
            return ipa
        nucleus = lambda seg: self._c(seg[0], "ipa_vowel") or not self._c(seg[0], "alpha")  # noqa: E731
        out: List[str] = []
        i, n = 0, len(ipa)
        while i < n:
            if not self._c(ipa[i], "tone_mark"):
                out.append(ipa[i])
                i += 1
                continue
            j = i
            while j < n and self._c(ipa[j], "tone_mark"):
                j += 1
            tone = ipa[i:j]
            t = j
            while t < n and not self._c(ipa[t], "tone_mark"):
                t += 1
            segs = self.segment(ipa[j:t], self.word["tone_dock"])
            if segs and t < n and all(nucleus(s) for s in segs):
                out.append(tone)
                i = j
                continue
            k = 0
            while k < len(segs) and nucleus(segs[k]):
                k += 1
            c = k
            while c < len(segs) and not nucleus(segs[c]):
                c += 1
            if c < len(segs) and c > k:
                c -= 1
            coda = "".join(segs[:c])
            out.append(coda)
            out.append(tone)
            i = j + len(coda)
        return "".join(out)

    def apply_iambic_length(self, ipa: str) -> str:
        if "ː" in ipa:
            return ipa
        sylls = self.syllabify_by_weight(ipa, self.stress["iambic"]["max_onset"])
        n = len(sylls)
        if n < 3:
            return ipa
        start = 0 if self.syllable_weight(sylls[0]) else 1
        for i in range(start, n - 1, 2):
            if self.syllable_weight(sylls[i]) == 0:
                segs = self.segment(sylls[i], self._affricates)
                k = next((k for k, seg in enumerate(segs) if self._vowel_segment(seg)), None)
                if k is not None:
                    segs[k] += "ː"
                sylls[i] = "".join(segs)
        return "".join(sylls)

    def syllabify_by_weight(self, ipa: str, max_onset: Optional[int] = None) -> List[str]:
        if not ipa:
            return []
        segs = self.segment(ipa, self._affricates)
        nuclei: List[Tuple[int, int]] = []
        i = 0
        while i < len(segs):
            if self._vowel_segment(segs[i]):
                start = i
                while i < len(segs) and self._vowel_segment(segs[i]):
                    i += 1
                nuclei.append((start, i))
            else:
                i += 1
        if not nuclei:
            return [ipa]
        if max_onset is None:
            max_onset = self.stress["weight"]["max_onset"]
        out = []
        for n, (start, end) in enumerate(nuclei):
            onset = 0 if n == 0 else start - min(max_onset, start - nuclei[n - 1][1])
            if n + 1 < len(nuclei):
                nxt = nuclei[n + 1][0]
                coda = nxt - min(max_onset, nxt - end)
            else:
                coda = len(segs)
            out.append("".join(segs[onset:coda]))
        return out

    def _holds_diphthong(self, seg: str) -> bool:
        letters = [c for c in seg if not self._comb(c)]
        vowel = [self._c(c, "ipa_vowel") or self._c(c, "vowel_phone") for c in letters]
        vowel.append(False)
        return any(vowel[i] and (vowel[i + 1] or (self._c(c, "offglide") and not vowel[i + 2]))
                   for i, c in enumerate(letters[1:]))

    def syllable_weight(self, syllable: str) -> int:
        """0 light, 1 heavy, 2 superheavy."""
        segs = self.segment(syllable, self._affricates)
        start = next((i for i, s in enumerate(segs) if self._vowel_segment(s)), None)
        if start is None:
            return 0
        end = start
        while end < len(segs) and self._vowel_segment(segs[end]):
            end += 1
        nucleus, coda = segs[start:end], segs[end:]
        long_vowel = (any("ː" in s for s in nucleus) or len(nucleus) > 1
                      or any(self._holds_diphthong(s) for s in nucleus))
        if (long_vowel and coda) or len(coda) >= 2:
            return 2
        return int(long_vowel or bool(coda))

    def stress_by_weight(self, sylls: Sequence[str]) -> int:
        n = len(sylls)
        if n <= 1:
            return -1
        if self.stress["weight"]["superheavy_final"] and self.syllable_weight(sylls[-1]) == 2:
            return -1
        if self.syllable_weight(sylls[-2]) >= 1:
            return -2
        default = self.stress["default"]
        return (default if n >= -default else -n) if default < 0 else -n

    # ─── S9f: mark placement ─────────────────────────────────────────
    def _licit_onset(self, run: str) -> bool:
        if not run:
            return True
        if not all(self._c(ch, "alpha") or self._comb(ch) for ch in run):
            return False
        units = self.segment(run, self._mark_atoms)
        onsets = self.stress["mark_onsets"]
        if onsets["max"] >= 0 and len(units) > onsets["max"]:
            return False
        if units[0].startswith(onsets["velar"]):
            return False
        if len(units) == 1:
            return True
        return tuple(units) in self._mark_table

    def _rebalance(self, syllables: List[str], nucleus: Sequence[bool], split, licit) -> List[str]:
        if len(syllables) < 2:
            return syllables
        out = [syllables[0]]
        start = len(syllables[0])
        for syll in syllables[1:]:
            j = 0
            while j < len(syll) and (self._comb(syll[j]) or not nucleus[start + j]):
                j += 1
            start += len(syll)
            onset = syll[:j]
            if not onset or not out[-1]:
                out.append(syll)
                continue
            units = split(onset)
            keep = 0
            for k in range(len(units), 0, -1):
                tail = "".join(units[len(units) - k:])
                if licit(tail):
                    keep = len(tail)
                    break
            if keep >= len(onset):
                out.append(syll)
                continue
            out[-1] += onset[:len(onset) - keep]
            out.append(syll[len(onset) - keep:])
        return out

    def syllabify_for_mark(self, ipa: str) -> List[str]:
        st = self.stress
        nucleus = self._nucleus_mask(ipa, {})
        if "ipa_diphthongs" not in st:
            if st["mark_diphthongs"]:
                sylls = self._with_diphthongs(ipa, nucleus, st["mark_diphthongs"])
            else:
                sylls = self._vowel_groups(ipa, nucleus) if ipa else []
        else:
            sylls = self._with_diphthongs(ipa, nucleus, st["ipa_diphthongs"])
        if st.get("mark_onsets") is not None:
            sylls = self._rebalance(sylls, nucleus, lambda run: self.segment(run, self._mark_atoms),
                                    self._licit_onset)
        if st.get("coda_liquid"):
            sylls = self._capture_coda_liquids(sylls, nucleus)
        return sylls

    def _capture_coda_liquids(self, syllables: List[str], nucleus: Sequence[bool]) -> List[str]:
        if len(syllables) < 2:
            return syllables
        out = [syllables[0]]
        start = len(syllables[0])
        for syll in syllables[1:]:
            j = 0
            while j < len(syll) and (self._comb(syll[j]) or not nucleus[start + j]):
                j += 1
            start += len(syll)
            cons = [c for c in syll[:j] if not self._comb(c)]
            if len(cons) >= 2 and self._c(cons[0], "liquid") and not self._c(cons[1], "glide") and out[-1]:
                k = 1
                while k < len(syll) and self._comb(syll[k]):
                    k += 1
                out[-1] += syll[:k]
                out.append(syll[k:])
            else:
                out.append(syll)
        return out

    def _prefix_mark(self, syll: str, mark: str) -> str:
        i = 0
        while i < len(syll) and (self._c(syll[i], "length") or self._comb(syll[i])):
            i += 1
        return syll[:i] + mark + syll[i:]

    def _merge_sites(self, syllables: Sequence[str]) -> List[int]:
        return [i for i in range(1, len(syllables))
                if syllables[i - 1] and syllables[i]
                and self._c(syllables[i - 1][-1], "basic_vowel") and self._c(syllables[i][0], "basic_vowel")]

    def _contact_units(self, run: str) -> List[str]:
        units = self.stress["contact_units"]
        out: List[str] = []
        i = 0
        while i < len(run):
            for g in units:
                if len(g) <= len(run) - i and self.casefold(run[i:i + len(g)]) == g:
                    out.append(run[i:i + len(g)])
                    i += len(g)
                    break
            else:
                out.append(run[i])
                i += 1
            while i < len(run) and self._comb(run[i]):
                out[-1] += run[i]
                i += 1
        return out

    def _vowel_contacts(self, syllables: Sequence[str]) -> Dict[int, str]:
        diphthongs = {self.lower(d) for d in self.stress["mark_diphthongs"]}
        silent = set(self.stress["silent_units"])
        contacts: Dict[int, str] = {}
        for i in range(1, len(syllables)):
            before, after = syllables[i - 1], syllables[i]
            if not before or not self._c(before[-1], "basic_vowel"):
                continue
            j = 0
            while j < len(after) and not self._c(after[j], "basic_vowel"):
                j += 1
            if j == len(after):
                continue
            if j and not all(g in silent for g in self._contact_units(self.casefold(after[:j]))):
                continue
            if self.lower(before[-1] + after[j]) not in diphthongs:
                contacts[i] = "hiatus"
            elif j:
                contacts[i] = "merge"
        return contacts

    def _split_first_nucleus(self, syll: str) -> Optional[Tuple[str, str]]:
        i = 0
        while i < len(syll) and not self._vowel_char(syll[i]):
            i += 1
        if i == len(syll):
            return None
        i += 1
        while i < len(syll) and (self._comb(syll[i]) or self._c(syll[i], "length")):
            if self._c(syll[i], "non_syllabic"):
                return None
            i += 1
        if i == len(syll) or not self._vowel_char(syll[i]):
            return None
        if i + 1 < len(syll) and self._c(syll[i + 1], "non_syllabic"):
            return None
        return syll[:i], syll[i:]

    def _align(self, syllables: Sequence[str], ipa_sylls: Sequence[str]):
        contacts = self._vowel_contacts(syllables)
        if not contacts:
            return None
        out: List[str] = []
        slots = [0]
        pending = ipa_sylls[0]
        j = 0
        for k in range(1, len(syllables)):
            kind = contacts.get(k)
            cut = self._split_first_nucleus(pending) if kind else None
            if kind == "merge" and cut is not None:
                slots.append(len(out))
                continue
            if kind == "merge" or cut is None:
                j += 1
                if j == len(ipa_sylls):
                    return None
                out.append(pending)
                pending = ipa_sylls[j]
            else:
                out.append(cut[0])
                pending = cut[1]
            slots.append(len(out))
        if j != len(ipa_sylls) - 1:
            return None
        out.append(pending)
        return out, slots

    def _glide_anchored(self, syllables, ipa_sylls, stress_index: int) -> Optional[int]:
        if syllables is None or not ipa_sylls or not 0 <= stress_index < len(syllables):
            return None
        marked = set(self.stress["marked"])
        if not marked or not any(ch in marked for ch in syllables[stress_index]):
            return None
        sites = self._merge_sites(syllables)
        if len(syllables) - len(sites) != len(ipa_sylls):
            return None
        shifted = stress_index - sum(1 for site in sites if site <= stress_index)
        return shifted if 0 <= shifted < len(ipa_sylls) else None

    def _ends_in_vowel(self, ipa: str) -> bool:
        for ch in reversed(ipa):
            if self._comb(ch):
                continue
            return self._vowel_char(ch)
        return False

    def _lost_after_stress(self, ipa: str, syllables, ipa_sylls, stress_index: int) -> bool:
        if self._ends_in_vowel(ipa):
            return False
        merged: List[int] = []
        for site in self._merge_sites(syllables):
            slot = site - len(merged)
            if slot >= len(ipa_sylls) or not (self._vowel_char(ipa_sylls[slot][0])
                                              or self._c(ipa_sylls[slot][0], "glide")):
                merged.append(site)
        return len(syllables) - len(merged) != len(ipa_sylls) or any(s > stress_index for s in merged)

    def _glide_to_diphthong(self, syllables, ipa_sylls: List[str], stress_index: int) -> List[str]:
        letters = self.stress["tonic_after_diphthong"]
        if not letters or len(ipa_sylls) != len(syllables):
            return ipa_sylls
        i = stress_index if stress_index >= 0 else len(syllables) + stress_index
        if not 1 <= i < len(syllables):
            return ipa_sylls
        stressed = self.lower(self.nfc(syllables[i]))
        before = self.lower(self.nfc(syllables[i - 1]))
        if not stressed or stressed[0] not in letters:
            return ipa_sylls
        if not any(len(d) > 1 and before.endswith(self.lower(d)) for d in self.stress["mark_diphthongs"]):
            return ipa_sylls
        head, prev = ipa_sylls[i], ipa_sylls[i - 1]
        if (len(head) < 2 or not self._c(head[0], "glide_head") or not self._vowel_char(head[1])
                or not prev or not self._vowel_char(prev[-1])):
            return ipa_sylls
        out = list(ipa_sylls)
        out[i - 1] = prev + head[0]
        out[i] = head[1:]
        return out

    def apply_stress_mark(self, ipa: str, stress_index: int, syllables: Optional[Sequence[str]],
                          ipa_syllables: Optional[Sequence[str]], secondary: Sequence[int] = (),
                          mark: Optional[str] = None) -> str:
        if self.stress["mark"] in ipa or (mark is not None and mark in ipa):
            return ipa
        mark = mark or self.stress["mark"]
        ipa_sylls = list(ipa_syllables) if ipa_syllables else self.syllabify_for_mark(ipa)
        if not ipa_sylls:
            return ipa
        if syllables is not None:
            ipa_sylls = self._glide_to_diphthong(syllables, ipa_sylls, stress_index)
        aligned = (self._align(syllables, ipa_sylls)
                   if syllables is not None and len(ipa_sylls) < len(syllables)
                   and -len(syllables) <= stress_index < len(syllables) else None)
        if aligned is not None:
            ipa_sylls, slots = aligned
            main = slots[stress_index]
            marked = {main}
            for sec in secondary:
                if 0 <= sec < len(slots) and slots[sec] not in marked:
                    marked.add(slots[sec])
                    ipa_sylls[slots[sec]] = self._prefix_mark(ipa_sylls[slots[sec]], self.stress["secondary_mark"])
            ipa_sylls[main] = self._prefix_mark(ipa_sylls[main], mark)
            return "".join(ipa_sylls)
        if stress_index < 0:
            offset_from_end = -stress_index
        else:
            n_orth = len(syllables) if syllables is not None else len(ipa_sylls)
            overflow = len(ipa_sylls) - n_orth
            if overflow > 0:
                stand_in = self.stress["stand_in"]

                def epenthetic(syll: str, final: bool) -> bool:
                    if [c for c in syll if self._vowel_char(c)] != [stand_in]:
                        return False
                    return not (final and syll.endswith(stand_in))
                merged = [ipa_sylls[0]]
                for i, syll in enumerate(ipa_sylls[1:], start=1):
                    if overflow > 0 and epenthetic(syll, final=i == len(ipa_sylls) - 1):
                        merged[-1] += syll
                        overflow -= 1
                    else:
                        merged.append(syll)
                ipa_sylls = merged
            elif overflow < 0 and stress_index <= len(ipa_sylls) - 1 and (
                    self._lost_after_stress(ipa, syllables, ipa_sylls, stress_index)
                    or self._glide_anchored(syllables, ipa_sylls, stress_index) is not None):
                lost = self._lost_after_stress(ipa, syllables, ipa_sylls, stress_index)
                target = stress_index if lost else self._glide_anchored(syllables, ipa_sylls, stress_index)
                for sec in secondary:
                    if 0 <= sec < len(ipa_sylls) and sec != target:
                        ipa_sylls[sec] = self._prefix_mark(ipa_sylls[sec], self.stress["secondary_mark"])
                ipa_sylls[target] = self._prefix_mark(ipa_sylls[target], mark)
                return "".join(ipa_sylls)
            offset_from_end = max(1, n_orth - stress_index)
        target = max(0, len(ipa_sylls) - offset_from_end)
        marked = {target}
        n = len(syllables) if syllables is not None else len(ipa_sylls)
        for sec in secondary:
            slot = max(0, len(ipa_sylls) + sec) if sec < 0 else max(0, len(ipa_sylls) - max(1, n - sec))
            if slot not in marked:
                marked.add(slot)
                ipa_sylls[slot] = self._prefix_mark(ipa_sylls[slot], self.stress["secondary_mark"])
        ipa_sylls[target] = self._prefix_mark(ipa_sylls[target], mark)
        return "".join(ipa_sylls)

    def _token_index(self, tokens: List[Token], graphemes, segments):
        t = 0
        for grapheme, segment in zip(graphemes, segments):
            while t < len(tokens) and tokens[t].grapheme != grapheme:
                t += 1
            if t == len(tokens):
                return
            yield t, segment
            t += 1

    def _vowel_offsets(self, ipa: str) -> List[int]:
        return [i for i, c in enumerate(ipa) if self._c(c, "ipa_vowel")]

    def _fold_inserted_nuclei(self, word: str, ipa: str, path) -> Optional[List[str]]:
        if path is None or not path[2] or "".join(path[0]) != ipa:
            return None
        tokens = self.grapheme_tokens(word)
        inserted: Set[int] = set()
        offset = 0
        pairs = list(self._token_index(tokens, path[2], path[0]))
        if len(pairs) != len(path[2]):
            return None
        for t, segment in pairs:
            if not self._e(tokens[t].entry, "readings_hold_vowel"):
                inserted.update(offset + i for i in self._vowel_offsets(segment))
            offset += len(segment)
        if not inserted:
            return None
        syllables = self.syllabify_for_mark(ipa)
        folded: List[str] = []
        offset = 0
        for syllable in syllables:
            nuclei = [offset + i for i in self._vowel_offsets(syllable)]
            if folded and nuclei and inserted.issuperset(nuclei):
                folded[-1] += syllable
            else:
                folded.append(syllable)
            offset += len(syllable)
        return folded if len(folded) < len(syllables) else None

    def _cut_written_syllables(self, word: str, ipa: str, path, syllables: List[str],
                               division: Optional[List[str]]) -> Optional[List[str]]:
        if path is None or not path[2] or "".join(path[0]) != ipa:
            return division
        sylls = division or self.syllabify_for_mark(ipa)
        if len(sylls) >= len(syllables) or "".join(syllables) != word:
            return division
        tokens = self.grapheme_tokens(word)
        token_syllable = self._map_tokens_to_syllables(tokens, syllables)
        owner: List[int] = []
        source: List[int] = []
        pairs = list(self._token_index(tokens, path[2], path[0]))
        if len(pairs) != len(path[2]):
            return division
        for t, segment in pairs:
            owner += [token_syllable[t]] * len(segment)
            source += [tokens[t].position] * len(segment)
        if len(owner) != len(ipa):
            return division
        starts = [sum(map(len, syllables[:k])) for k in range(len(syllables))]
        diphthongs = {self.lower(d) for d in self.stress["mark_diphthongs"]}
        cuts: Set[int] = set()
        last: Optional[int] = None
        for o, ch in enumerate(ipa):
            if not self._c(ch, "ipa_vowel"):
                if not (self._comb(ch) or self._c(ch, "length")):
                    last = None
                continue
            following = ipa[o + 1:o + 2]
            if (last is not None and owner[o] == owner[last] + 1
                    and not (following and self._c(following, "non_syllabic"))):
                before, after = syllables[owner[last]], syllables[owner[o]]
                first = next((c for c in after if self._c(c, "orth_vowel")), "")
                lead = after[:source[o] - starts[owner[o]]]
                if any(self._c(c, "alpha") for c in lead) and self.lower(before[-1:] + first) not in diphthongs:
                    cuts.add(o)
            last = o
        read = {i for token in tokens for i in range(token.position, token.position + token.length)}
        drops: List[int] = []
        for k, syllable in enumerate(syllables):
            segments = [o for o, w in enumerate(owner) if w == k]
            dropped = [i for i, c in enumerate(syllable, start=starts[k])
                       if self._c(c, "orth_vowel") and i not in read]
            if segments and dropped and not any(self._c(ipa[o], "ipa_vowel") for o in segments):
                drops.append(next((o for o in segments if source[o] > dropped[0]), segments[-1] + 1))
        if drops:
            stand_in = self.stress["stand_in"]
            probe = stand_in.join(ipa[a:b] for a, b in zip([0, *drops], [*drops, len(ipa)]))
            stand_ins = [at + i for i, at in enumerate(drops)]
            ends = [0, *accumulate(map(len, self.syllabify_for_mark(probe)))]
            for p in stand_ins:
                start = max(e for e in ends if e <= p)
                end = min(e for e in ends if e > p)
                start -= sum(q < start for q in stand_ins)
                end -= sum(q < end for q in stand_ins)
                cuts |= {start, end}
        bounds = set(accumulate(map(len, sylls[:-1]))) | cuts
        edges = [0, *sorted(b for b in bounds if 0 < b < len(ipa)), len(ipa)]
        cut = [ipa[a:b] for a, b in zip(edges, edges[1:])]
        return cut if len(cut) > len(sylls) else division

    # ─── S9: word finalisation ───────────────────────────────────────
    def _collapse_geminates(self, ipa: str) -> str:
        out: List[str] = []
        for ch in ipa:
            if (out and ch == out[-1] and not self._c(ch, "vowel_ipa_set")
                    and not self._c(ch, "length") and not self._c(ch, "whitespace")):
                continue
            out.append(ch)
        return "".join(out)

    def _finalize(self, word: str, ipa: str, path, collapse: bool, forced: bool = False) -> str:
        if self._tone and path is not None and path[2] and ipa == "".join(path[0]):
            ipa = self._computed_tones(path[2], path[0])
        if collapse and self.word["collapse_geminates"] and ipa:
            ipa = self._collapse_geminates(ipa)
        virama_final = self.word.get("virama_final")
        if (virama_final is not None and word and ipa and self._c(word[-1], "virama")
                and not self._c(ipa[-1], "ipa_vowel")):
            ipa += virama_final
        if "tone_dock" in self.word and ipa:
            ipa = self.dock_tone_marks(ipa)
        if forced:
            return ipa
        if self.stress is not None and self.stress.get("iambic") and ipa and not self._is_cliticless(word):
            ipa = self.apply_iambic_length(ipa)
        if self.stress is not None and self.stress["apply"] and ipa and not self._is_cliticless(word):
            if self.stress.get("weight"):
                ipa_sylls = self.syllabify_by_weight(ipa)
                return self.apply_stress_mark(ipa, self.stress_by_weight(ipa_sylls), None, ipa_sylls)
            ipa_count = self.stress.get("ipa_count")
            sylls = self.syllabify_for_mark(ipa) if ipa_count else self.syllables(word)
            idx = self.detect_stress(word, sylls)
            folded = None if ipa_count else self._fold_inserted_nuclei(word, ipa, path)
            division = self._cut_written_syllables(word, ipa, path, sylls, folded)
            accent2 = self.stress.get("accent2")
            mark = (accent2["mark"] if accent2 and len(sylls) >= 2 and idx == len(sylls) - 2
                    and word and self.lower(word[-1]) in accent2["finals"] else None)
            ipa = self.apply_stress_mark(ipa, idx, sylls, division,
                                         sorted(self.secondary_positions(len(sylls), idx)), mark)
        return ipa

    # ─── S9a: computed tone ──────────────────────────────────────────
    def _computed_tones(self, graphemes: Sequence[str], segments: Sequence[str]) -> str:
        """3.9: append each syllable's tone, from its initial's class, its
        rime's shape and its tone mark."""
        sylls = self._tone_syllables(segments)
        if not sylls:
            return "".join(segments)
        out: List[str] = []
        for syl in sylls:
            ipa = "".join(segments[i] for i in syl)
            out.append(ipa + self._syllable_tone([graphemes[i] for i in syl], ipa))
        return "".join(out)

    def _tone_syllables(self, segments: Sequence[str]) -> List[List[int]]:
        """Slot indices grouped by maximal onset."""
        nuclei = [i for i, seg in enumerate(segments) if any(self._c(ch, "ipa_vowel") for ch in seg)]
        if not nuclei:
            return []
        sylls: List[List[int]] = [[] for _ in nuclei]
        prev = 0
        for n, idx in enumerate(nuclei):
            between = list(range(prev, idx))
            if n == 0:
                sylls[0] = between + [idx]
            elif segments[idx] and not self._c(segments[idx][0], "ipa_vowel"):
                sylls[n - 1] += between
                sylls[n] = [idx]
            else:
                spelling = [i for i in between if segments[i]]
                cut = spelling[-1] if spelling else idx
                sylls[n - 1] += [i for i in between if i < cut]
                sylls[n] = [i for i in between if i >= cut] + [idx]
            prev = idx + 1
        sylls[-1] += list(range(prev, len(segments)))
        return sylls

    def _syllable_tone(self, graphemes: Sequence[str], ipa: str) -> str:
        cls = next((self._tone_classes[ch] for g in graphemes for ch in g if ch in self._tone_classes), None)
        if cls is None or cls not in self._tone_class_names:
            return ""
        mark = self._tone["no_mark"]
        for g in graphemes:
            for ch in g:
                if ch in self._tone_marks:
                    mark = self._tone_marks[ch]
        segs = self.segment(ipa, self._tone["atoms"])
        i = 0
        while i < len(segs) and not self._c(segs[i][0], "ipa_vowel"):
            i += 1
        if i == len(segs):
            return ""
        j = i
        while j < len(segs) and self._c(segs[j][0], "ipa_vowel"):
            j += 1
        long_vowel = "ː" in "".join(segs[i:j])
        coda = "".join(segs[j:])
        dead = any(coda.startswith(c) for c in self._tone["dead_codas"]) if coda else not long_vowel
        shape = ("dead_long" if long_vowel else "dead_short") if dead else "live"
        tone = self._tone_table.get((cls, shape, mark))
        if tone is None:
            tone = self._tone_table.get((cls, "any", mark))
        return tone or ""

    def _dropped(self, word: str) -> Tuple[str, ...]:
        out: List[str] = []
        for tok in self.tokenize(word):
            if tok.kind == UNKNOWN:
                out.append(tok.grapheme)
            elif tok.kind == DIGIT:
                out.extend(tok.grapheme)
        return tuple(out)

    # ─── S8b: grammatical endings ───────────────────────────────────
    def _match_ending(self, graphemes: List[str]) -> Optional[Tuple[dict, int]]:
        if len(graphemes) < 2:
            return None
        suffix = int(self.lower(graphemes[-1]) in self._ending_suffix)
        end = len(graphemes) - suffix
        stem = [self.lower(g) for g in graphemes[:end]]
        surface = "".join(stem)
        starts = []
        offset = 0
        for token in stem:
            starts.append(offset)
            offset += len(token)
        for cut in range(1, len(surface)):
            entry = self._endings.get(surface[cut:])
            if entry is None:
                continue
            first = max(i for i, at in enumerate(starts) if at <= cut)
            if first < 1:
                continue
            return entry, end - first + suffix
        return None

    def _apply_ending(self, word: str, paths: list) -> list:
        if not paths or not self.ir.get("endings"):
            return paths
        tokens = [t.grapheme for t in self.tokenize(word) if t.kind == WORD]
        marks = self.word["silent_stress_marks"]
        kept = [i for i, g in enumerate(tokens) if not (len(g) == 1 and g in marks)]
        match = self._match_ending([tokens[i] for i in kept])
        if match is None:
            return paths
        entry, n = match
        if marks and n:
            n = len(tokens) - kept[-n]

        def rewrite(path, ipa: str, extra: int):
            segs, cost, graphemes = path
            if len(segs) <= n:
                return path
            ipa = self._ending_vowels_follow_stress(path, n, ipa)
            return (segs[:-n] + (ipa,), cost + extra,
                    graphemes[:-n] + ("".join(graphemes[-n:]),) if graphemes else ())

        out, seen = [], set()
        for path in paths:
            new = path if "ipa" not in entry else rewrite(path, entry["ipa"], 0)
            if "".join(new[0]) not in seen:
                seen.add("".join(new[0]))
                out.append(new)
        if entry["alts"] and out:
            for alt, cost in zip(entry["alts"], entry["costs"][1:]):
                new = rewrite(paths[0], alt, cost)
                if "".join(new[0]) not in seen:
                    seen.add("".join(new[0]))
                    out.append(new)
            out.sort(key=lambda p: p[1])
        return out

    def _vowel_runs(self, ipa: str) -> List[Tuple[int, int]]:
        runs: List[Tuple[int, int]] = []
        for i, c in enumerate(ipa):
            if self._c(c, "ipa_vowel"):
                if runs and runs[-1][1] == i:
                    runs[-1] = (runs[-1][0], i + 1)
                else:
                    runs.append((i, i + 1))
            elif runs and runs[-1][1] == i and self._c(c, "combining"):
                runs[-1] = (runs[-1][0], i + 1)
        return runs

    def _ending_vowels_follow_stress(self, path, tail: int, ipa: str) -> str:
        segs, _, graphemes = path
        if not graphemes:
            return ipa
        letters = []
        for grapheme, segment in zip(graphemes[-tail:], segs[-tail:]):
            runs = self._vowel_runs(segment)
            if len(runs) > 1:
                return ipa
            if runs:
                letters.append((self.lower(grapheme), segment[runs[0][0]:runs[0][1]]))
        declared = self._vowel_runs(ipa)
        if len(declared) != len(letters):
            return ipa
        out = []
        last = 0
        for (start, end), (grapheme, actual) in zip(declared, letters):
            written = ipa[start:end]
            if written == actual:
                continue
            reduced, readings = self._ending_vowels.get(grapheme, ((), ()))
            if written not in reduced:
                continue
            if actual not in readings:
                sources = self._ending_sources.get(actual, set()) & readings
                actual = next(iter(sources)) if len(sources) == 1 else None
            if actual is not None and actual != written:
                out.append(ipa[last:start])
                out.append(actual)
                last = end
        out.append(ipa[last:])
        return "".join(out)

    def transcribe_word(self, word: str, width: int, lexicon=None, forced: Optional[str] = None,
                        key: Optional[str] = None) -> WordResult:
        """*word* to IPA. A *forced* reading takes the place of a lexicon hit
        and is not stressed. *key* is the spelling to look up in place of
        *word*. Without a lexicon, a forced reading or a key the result
        depends on *word* and *width* alone, so it is cached."""
        if lexicon is None and forced is None and key is None:
            hit = self._words.get((word, width))
            if hit is None:
                if len(self._words) >= 65536:
                    self._words.clear()
                hit = self._words[(word, width)] = self._transcribe_word(word, width, None, None)
            return hit
        return self._transcribe_word(word, width, lexicon, forced, key)

    def _transcribe_word(self, word: str, width: int, lexicon, forced: Optional[str],
                         key: Optional[str] = None) -> WordResult:
        override = forced if forced is not None else self._override_for(key or word, lexicon)
        paths = []
        if override is not None:
            ipa = self._finalize(word, override, None, collapse=False, forced=forced is not None)
        else:
            paths = self._apply_ending(word, self._word_paths(word, width))
            best = paths[0] if paths else None
            ipa = self._finalize(word, word if best is None else "".join(best[0]), best, collapse=True)
        return WordResult(word, ipa, self._dropped(word), tuple((p[0], p[1]) for p in paths),
                          forced is not None, override is not None)

    # ─── S10 to S14: the sentence ────────────────────────────────────
    def _mark_compounds(self, words: List[_Word], ipa_words: List[str]) -> List[str]:
        mark, secondary = self.stress["mark"], self.stress["secondary_mark"]
        out = list(ipa_words)
        start = 0
        for end in range(1, len(words) + 1):
            if end < len(words) and words[end].hyphen_joined:
                continue
            marked = [i for i in range(start, end) if mark in out[i]]
            for i in marked[:-1]:
                out[i] = out[i].replace(mark, secondary)
            start = end
        return out

    def _sandhi(self, words: List[str], surfaces: List[str], pausal: List[bool]) -> List[str]:
        result = list(words)
        for i in range(len(result)):
            if pausal[i]:
                left = [ord(c) for c in result[i]]
                for rule in self.ir["sandhi"]:
                    if "pause" in rule and self._side_holds(rule, "left", left, surfaces[i]):
                        result[i] = self._sub(rule["left"], rule["left_out"], left)
                        break
                continue
            left, right = [ord(c) for c in result[i]], [ord(c) for c in result[i + 1]]
            left_done = right_done = False
            for rule in self.ir["sandhi"]:
                if left_done and right_done:
                    break
                if "pause" in rule:
                    continue
                if not (self._side_holds(rule, "left", left, surfaces[i])
                        and self._side_holds(rule, "right", right, surfaces[i + 1])):
                    continue
                if "left_out" in rule and not left_done:
                    result[i] = self._sub(rule["left"], rule["left_out"], left)
                    left_done = True
                if "right_out" in rule and not right_done:
                    result[i + 1] = self._sub(rule["right"], rule["right_out"], right)
                    right_done = True
        return result

    @staticmethod
    def _side_holds(rule: dict, side: str, ipa: List[int], surface: str) -> bool:
        """The *side* pattern finds a match in the IPA and, when the rule has one, the
        spelling pattern finds a match in the surface of the word."""
        if pattern.search(rule[side], ipa, 0, pattern.group_count(rule[side])) is None:
            return False
        spelling = rule.get(side + "_spelling")
        return spelling is None or pattern.search(
            spelling, [ord(c) for c in surface], 0, pattern.group_count(spelling)) is not None

    @staticmethod
    def _sub(node: list, template: list, s: List[int]) -> str:
        strings = []
        tpl = []
        for part in template:
            if part[0] == "lit":
                tpl.append(["lit", len(strings)])
                strings.append([ord(c) for c in part[1]])
            else:
                tpl.append(part)
        return "".join(map(chr, pattern.sub(node, tpl, s, strings)))

    def words(self, runs: Sequence[Tuple], lexicon=None) -> List[_Word]:
        """The words of *runs*, as :meth:`transcribe_runs` reads them, the
        last one pausal."""
        words: List[_Word] = []
        for text, forced, *unmarked in runs:
            if forced is not None:
                words.append(_Word(text.strip(), forced=forced))
                continue
            start = len(words)
            self._group_words(self._run_text(text), words, lexicon)
            if unmarked and unmarked[0] != text:
                self._key_words(words[start:], unmarked[0], lexicon)
        if words:
            words[-1].pausal = True
        return words

    def _run_text(self, text: str) -> str:
        return self.prepare(text if self.hooks.text is None else self.hooks.text(text))

    def _key_words(self, words: List[_Word], unmarked: str, lexicon) -> None:
        keys: List[_Word] = []
        self._group_words(self._run_text(unmarked), keys, lexicon)
        if len(keys) != len(words):
            raise ValueError(
                f"the mark stage made {len(words)} words of the {len(keys)} words in "
                f"{unmarked!r}. A mark stage keeps the words")
        for word, key in zip(words, keys):
            if key.surface != word.surface:
                word.key = key.surface

    def transcribe_runs(self, runs: Sequence[Tuple], *, width: int = 1,
                        lexicon=None) -> Result:
        """Transcribe a text given as runs. A run ``(text, None)`` is plain
        text; a run ``(surface, ipa)`` is one word with a forced reading. A
        plain run ``(text, None, unmarked)`` is *text* after a mark stage: the
        lexicon is looked up by the words of *unmarked*, and the rules read *text*."""
        words = self.words(runs, lexicon)
        if not words:
            return Result("")
        results = [self.transcribe_word(w.surface, width, lexicon, w.forced, w.key) for w in words]
        ipa_words = [r.ipa for r in results]
        if self.stress is not None and self.stress["compound_last"]:
            ipa_words = self._mark_compounds(words, ipa_words)
        if self.ir.get("sandhi"):
            ipa_words = self._sandhi(ipa_words, [w.surface for w in words], [w.pausal for w in words])
        if self.hooks.sandhi is not None:
            rewritten = self.hooks.sandhi(list(ipa_words), [w.surface for w in words],
                                          [w.pausal for w in words])
            if len(rewritten) != len(ipa_words):
                raise ValueError(f"the sandhi hook returned {len(rewritten)} words for {len(ipa_words)}")
            ipa_words = list(rewritten)
        ipa = " ".join(w for w in ipa_words if w)
        if self.ir.get("dialect"):
            ipa = run_program(self, self.ir["dialect"], ipa, " ".join(w.surface for w in words))
        if ipa:
            ipa = self.nfc(ipa)
        return Result(ipa, tuple(WordResult(r.word, self.nfc(iw) if iw else iw, r.dropped, r.paths, r.forced,
                                            r.override)
                                 for r, iw in zip(results, ipa_words)))

    def transcribe(self, text: str, *, width: int = 1, lexicon=None) -> str:
        return self.transcribe_runs([(text, None)], width=width, lexicon=lexicon).ipa
