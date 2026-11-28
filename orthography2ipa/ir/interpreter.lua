-- The o2i IR interpreter for LuaJIT 2.1 (docs/ir/o2i-ir-v1.md, section 3).
--
-- It reads one canonical IR document (the JSON that compile_spec writes)
-- and turns codepoint arrays into codepoint arrays. It knows the primitives
-- of section 2.3 and nothing about any language, script or phoneme class.
-- Every function follows the Python reference interpreter
-- (orthography2ipa/ir/interpreter.py, layout.py, pattern.py, dialect.py)
-- and must give the same bytes.
--
-- Strings are held in a fixed-width form: three bytes per codepoint, the
-- first byte with the high bit set and the other two without. Byte order is
-- codepoint order, a plain substring search can only match at a codepoint
-- boundary, and every Python string index i is byte 3*i + 1.
--
-- Use:
--   local ir = require("interpreter")   -- or dofile
--   local it = ir.new(ir.json_decode(text))
--   it:transcribe_cps({codepoints}, width) -> {codepoints}
--   luajit interpreter.lua IR.json [width] < lines of codepoints
-- loom: define O2I_LANGUAGES (codes) and O2I_IRS (code -> IR JSON text)
-- before this chunk; it then defines infer{text = {...}, lang = index}.

local floor, max, min = math.floor, math.max, math.min
local unpack = unpack or table.unpack
local concat, sort = table.concat, table.sort
local sbyte, schar, ssub, sfind = string.byte, string.char, string.sub, string.find

local M = {}

M.SUPPORTED_IR_VERSIONS = {[1] = true}
-- The semantics version of every primitive and predicate node (8.1).
M.SEMANTICS = {
  codepoint_map = 1, pattern = 1, trie = 1, bits = 1, predicate = 1, candidates = 1,
  beam = 1, splitter = 1, decision = 1, sequencer = 1, segment = 1, word_has = 1,
  spell_gate = 1, positional_rewrite = 1, gated_map = 1, aligned_rewrite = 1,
  allophony = 1, mark_placement = 1, sandhi = 1, sandhi_spelling = 1, sandhi_joined = 1, sandhi_pause = 1, rewrite = 1, endings = 1, inherent = 1,
  written_onsets = 1, vowel_letters = 1, secondary = 1, aperture = 1, prefixes = 1, coda_liquid = 1, mutate = 1, accent2 = 1,
  fold = 1, tone_dock = 1, iambic = 1, prevocalic_backoff = 1,
  ipa_count = 1, consonant_nuclei = 1, computed_tone = 1,
  internal_apostrophe = 1, apostrophe_elision = 1, collapse_geminates = 1, context_beam = 1,
  clitic_marks = 1, silent_stress_marks = 1, overrides = 1, words = 1, allophone_map = 1, hiatus = 2,
  semivowels = 1, cliticless = 1, compound_last = 1, noncohering = 1, tonic_after_diphthong = 1,
  ipa_diphthongs = 1, mark_onsets = 1, allophony_geminate = 1,
  cut_pairs = 1, glide_hiatus = 1, stem_cuts = 1, prefix_cuts = 1, seams = 1, foreign_nuclei = 1,
  weight = 1, virama_final = 1, vowel_signs = 1, preposed = 1,
  ["node.and"] = 1, ["node.or"] = 1, ["node.not"] = 1, ["node.true"] = 1, ["node.false"] = 1,
  ["node.exists"] = 1, ["node.ebit"] = 1, ["node.entry_in"] = 1, ["node.top_in"] = 1,
  ["node.top_seg_in"] = 1, ["node.syll"] = 1, ["node.word_in"] = 1, ["node.word_has"] = 1,
  ["node.syllpos"] = 1, ["node.word_final"] = 1, ["node.count"] = 1, ["node.word_has_entry"] = 1,
  ["node.reading_vowel"] = 1,
  ["syll.has_stress"] = 1, ["syll.idx_eq_stressed"] = 1, ["syll.idx_lt_stressed"] = 1,
  ["syll.idx_gt_stressed"] = 1, ["syll.idx_eq_stressed_minus_1"] = 1, ["syll.idx_in_secondary"] = 1,
  ["syll.open"] = 1, ["syll.closed"] = 1, ["node.top_nucleus"] = 1,
}

local CHAR_NAMES = {
  "known", "space", "punct", "digit", "alpha", "letter_or_mark", "combining", "mn_mc",
  "a_mark", "modifier", "orth_vowel", "ipa_vowel", "basic_vowel", "front_letter", "length",
  "non_syllabic", "glide", "offglide", "nasal_carrier", "apostrophe", "hyphen", "pause",
  "edge_punct", "word_letter", "elision_apostrophe", "virama", "vowel_ipa_set",
  "glide_head", "elision_h", "whitespace", "syllabic_mark", "mark_spells_nothing", "supplies_vowel",
  "vowel_phone", "nucleus_base", "syllabic", "liquid", "tone_mark",
}
local ENTRY_NAMES = {
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
}
local NO_STRESS = -1
local NONE = "none"
local WORD, WS, PUNCT, DIGIT, UNKNOWN = "grapheme", "whitespace", "punctuation", "digit", "unknown"

-- ═══ general helpers ═══════════════════════════════════════════════════════

-- Python truth value of IR data.
local function T(x)
  if x == nil or x == false or x == 0 or x == "" then return false end
  if type(x) == "table" then return next(x) ~= nil end
  return true
end

local function hasbit(x, pw) return floor(x / pw) % 2 == 1 end

-- Stable sort with a strict "less" on the elements.
local function ssort(t, lt)
  local w = {}
  for i = 1, #t do w[i] = {t[i], i} end
  sort(w, function(a, b)
    if lt(a[1], b[1]) then return true end
    if lt(b[1], a[1]) then return false end
    return a[2] < b[2]
  end)
  for i = 1, #t do t[i] = w[i][1] end
  return t
end

-- Python list slice t[i:j] of a 1-based array, with Python index rules.
local function lsl(t, i, j)
  local n = #t
  i = i or 0; j = j or n
  if i < 0 then i = max(0, i + n) elseif i > n then i = n end
  if j < 0 then j = max(0, j + n) elseif j > n then j = n end
  local out = {}
  for k = i + 1, j do out[#out + 1] = t[k] end
  return out
end

local function lappend(a, b)
  local out = {}
  for k = 1, #a do out[k] = a[k] end
  for k = 1, #b do out[#out + 1] = b[k] end
  return out
end

-- A hash view of a set or list, cached by table identity.
local SETS = setmetatable({}, {__mode = "k"})
local function setof(list)
  local h = SETS[list]
  if not h then
    h = {}
    for _, v in ipairs(list) do h[v] = true end
    SETS[list] = h
  end
  return h
end
local function inset(list, x) return setof(list)[x] == true end

-- ═══ fixed-width strings ═══════════════════════════════════════════════════

local CH = {}
local function C(cp)
  local s = CH[cp]
  if not s then
    s = schar(0x80 + floor(cp / 16384), floor(cp / 128) % 128, cp % 128)
    CH[cp] = s
  end
  return s
end
local function cp_of(ch)
  local a, b, c = sbyte(ch, 1, 3)
  return (a - 0x80) * 16384 + b * 128 + c
end
local function slen(s) return #s / 3 end
local function at(s, i)
  if i < 0 then i = i + #s / 3 end
  return ssub(s, 3 * i + 1, 3 * i + 3)
end
local function sl(s, i, j)
  local n = #s / 3
  i = i or 0; j = j or n
  if i < 0 then i = max(0, i + n) elseif i > n then i = n end
  if j < 0 then j = max(0, j + n) elseif j > n then j = n end
  if j <= i then return "" end
  return ssub(s, 3 * i + 1, 3 * j)
end
local function startswith(s, p, i)
  i = i or 0
  if i > #s / 3 then return false end
  return ssub(s, 3 * i + 1, 3 * i + #p) == p
end
local function endswith(s, p)
  return #p == 0 or (#p <= #s and ssub(s, -#p) == p)
end
local function contains(s, p) return sfind(s, p, 1, true) ~= nil end
local function sfind_from(s, p, i)
  local b = sfind(s, p, 3 * (i or 0) + 1, true)
  return b and (b - 1) / 3 or -1
end
local function sreplace(s, a, b)
  if a == "" then
    local out = {b}
    for i = 0, slen(s) - 1 do out[#out + 1] = at(s, i); out[#out + 1] = b end
    return concat(out)
  end
  local out, pos = {}, 1
  while true do
    local x = sfind(s, a, pos, true)
    if not x then break end
    out[#out + 1] = ssub(s, pos, x - 1)
    out[#out + 1] = b
    pos = x + #a
  end
  out[#out + 1] = ssub(s, pos)
  return concat(out)
end
local function from_cps(cps)
  local out = {}
  for i = 1, #cps do out[i] = C(cps[i]) end
  return concat(out)
end
local function to_cps(s)
  local out = {}
  for i = 0, #s / 3 - 1 do out[i + 1] = cp_of(ssub(s, 3 * i + 1, 3 * i + 3)) end
  return out
end
local function chars(s)
  local out = {}
  for i = 0, #s / 3 - 1 do out[i + 1] = ssub(s, 3 * i + 1, 3 * i + 3) end
  return out
end
local SPACE, APOS, RSQUO, LENGTH, HYPHEN = C(32), C(39), C(0x2019), C(0x2D0), C(0x2D)
M.C, M.from_cps, M.to_cps = C, from_cps, to_cps

-- ═══ JSON ══════════════════════════════════════════════════════════════════

local function utf8_char(cp)
  if cp < 0x80 then return schar(cp) end
  if cp < 0x800 then return schar(0xC0 + floor(cp / 64), 0x80 + cp % 64) end
  if cp < 0x10000 then
    return schar(0xE0 + floor(cp / 4096), 0x80 + floor(cp / 64) % 64, 0x80 + cp % 64)
  end
  return schar(0xF0 + floor(cp / 262144), 0x80 + floor(cp / 4096) % 64,
               0x80 + floor(cp / 64) % 64, 0x80 + cp % 64)
end

local ESCAPES = {b = "\b", f = "\f", n = "\n", r = "\r", t = "\t"}

function M.json_decode(str)
  local pos = 1
  local value
  local function ws() pos = sfind(str, "[^ \t\r\n]", pos) or #str + 1 end
  local function parse_string()
    pos = pos + 1
    local parts = {}
    while true do
      local s = sfind(str, '["\\]', pos)
      if not s then error("json: unterminated string") end
      parts[#parts + 1] = ssub(str, pos, s - 1)
      if ssub(str, s, s) == '"' then pos = s + 1; break end
      local esc = ssub(str, s + 1, s + 1)
      if esc == "u" then
        local cp = tonumber(ssub(str, s + 2, s + 5), 16)
        pos = s + 6
        if cp >= 0xD800 and cp <= 0xDBFF and ssub(str, pos, pos + 1) == "\\u" then
          local lo = tonumber(ssub(str, pos + 2, pos + 5), 16)
          cp = 0x10000 + (cp - 0xD800) * 1024 + (lo - 0xDC00)
          pos = pos + 6
        end
        parts[#parts + 1] = utf8_char(cp)
      else
        parts[#parts + 1] = ESCAPES[esc] or esc
        pos = s + 2
      end
    end
    return concat(parts)
  end
  function value()
    ws()
    local c = ssub(str, pos, pos)
    if c == "{" then
      pos = pos + 1
      local obj = {}
      ws()
      if ssub(str, pos, pos) == "}" then pos = pos + 1; return obj end
      while true do
        ws()
        local key = parse_string()
        ws(); pos = pos + 1 -- ':'
        obj[key] = value()
        ws()
        local d = ssub(str, pos, pos); pos = pos + 1
        if d == "}" then return obj end
      end
    elseif c == "[" then
      pos = pos + 1
      local arr = {}
      ws()
      if ssub(str, pos, pos) == "]" then pos = pos + 1; return arr end
      while true do
        arr[#arr + 1] = value()
        ws()
        local d = ssub(str, pos, pos); pos = pos + 1
        if d == "]" then return arr end
      end
    elseif c == '"' then
      return parse_string()
    elseif ssub(str, pos, pos + 3) == "true" then pos = pos + 4; return true
    elseif ssub(str, pos, pos + 4) == "false" then pos = pos + 5; return false
    elseif ssub(str, pos, pos + 3) == "null" then pos = pos + 4; return nil
    end
    local s, e = sfind(str, "^-?%d+%.?%d*[eE]?[-+]?%d*", pos)
    if not s then error("json: bad value at " .. pos) end
    pos = e + 1
    return tonumber(ssub(str, s, e))
  end
  return value()
end

-- ═══ the IR layout (layout.py) ═════════════════════════════════════════════

local S_, I_, PAT, OPAQUE, SSET, PRED, GATE, DPRED, TPL, ESET =
  "s", "i", "pat", "opaque", "sset", "pred", "gate", "dpred", "tpl", "eset"
local function Lt(t) return {"list", t} end
local function Ob(f) return {"obj", f} end
local function Pr(a, b) return {"pair", a, b} end

local RULE = Ob{phonemes = Lt(S_), out = Lt(S_), aware = Lt(I_), when = PRED, slot_when = PRED,
                trig_next = I_, trig_prev = I_, mutate = S_, mutate_at = I_,
                seg = Ob{initial = I_, final = I_, prev = SSET, next = SSET}}
local STEP = Ob{gate = GATE, kind = OPAQUE, find = S_, rep = S_, pattern = PAT, template = TPL,
                on = SSET, off = SSET, when_on = I_, map = Lt(Lt(S_)), rules = Lt(Lt(S_)), when = DPRED}
local LAYOUT = Ob{
  entries = Lt(Ob{key = S_, cands = Lt(S_), costs = Lt(I_), bits = I_, trie = I_, onset = Lt(S_),
                  positional = Lt(Pr(PRED, Lt(S_)))}),
  fallback = SSET,
  word = Ob{exceptions = Lt(Lt(S_)), words = Lt(Lt(S_)), internal_apostrophe = I_, apostrophe_elision = I_,
            collapse_geminates = I_, context_beam = I_, tone_dock = Lt(S_), clitic_marks = SSET, silent_stress_marks = SSET,
            virama_final = S_},
  beam = Ob{tilde = S_},
  allophone_map = Lt(Pr(S_, Lt(S_))),
  syllable = Ob{diphthongs = Lt(S_), onset_graphemes = SSET, semivowels = Lt(Lt(S_)),
                closed_hiatus = Ob{pairs = Lt(S_), onsets = Lt(S_), codas = Lt(S_), atonic_onsets = Lt(S_), multi_keys = Lt(S_)},
                final_diphthongs = Ob{diphthongs = Lt(S_), finals = Lt(S_)}, vowel_letters = SSET, silent_tail = SSET,
                onsets = Ob{max = I_, units = Lt(S_), velar = SSET, table = Lt(Lt(S_))},
                cut_pairs = SSET, glide_hiatus = Ob{glides = SSET, before = Lt(S_), codas = SSET, diphthong_words = SSET},
                stem_cuts = Lt(Pr(S_, Lt(I_))), prefix_cuts = Lt(Ob{prefix = S_, onset = SSET, stems = Lt(S_)}),
                seams = Ob{suffixes = Lt(Ob{pattern = PAT, cut = I_}), stems = Lt(S_), next = SSET},
                foreign = Ob{pattern = PAT, nuclei = Lt(S_), finals = Lt(Pr(S_, Lt(S_)))}},
  stress = Ob{mark = S_, secondary_mark = S_, alternating = I_, prefixes = Lt(S_),
              schwa_rimes = SSET, coda_liquid = I_, accent2 = Ob{mark = S_, finals = SSET},
              iambic = Ob{max_onset = I_}, marked = SSET, final = Lt(S_), penult = Lt(S_),
              antepenult = Lt(S_), default = I_, cliticless = SSET, compound_last = I_,
              mark_diphthongs = Lt(S_), tonic_after_diphthong = Lt(S_), stand_in = S_, apply = I_,
              contact_units = Lt(S_), silent_units = SSET, ipa_diphthongs = Lt(S_), ipa_count = I_,
              mark_onsets = Ob{max = I_, velar = S_, table = Lt(Lt(S_))},
              weight = Ob{max_onset = I_, superheavy_final = I_},
              noncohering = Ob{suffixes = Lt(S_), exceptions = SSET}},
  atoms = Ob{mark = Lt(S_), affricates = Lt(S_)},
  allophony = Ob{passes = I_, atoms = Lt(S_), geminate = I_, rules = Lt(RULE)},
  sandhi = Lt(Ob{left = PAT, right = PAT, obligatory = I_, left_out = TPL, right_out = TPL,
                 left_spelling = PAT, right_spelling = PAT,
                 left_joined_spelling = PAT, right_joined_spelling = PAT, pause = I_}),
  dialect = Lt(STEP),
  char_maps = Ob{casefold = Lt(Pr(I_, S_)), plain_lower = Lt(Pr(I_, S_)), nfd = Lt(Pr(I_, S_)),
                 ccc = Lt(Lt(I_)), compose = Lt(Lt(I_)), presentation = Lt(Pr(I_, S_)), fold = SSET},
  consonant_nuclei = Lt(Pr(S_, S_)),
  tone = Ob{classes = Lt(Pr(S_, S_)), marks = Lt(Pr(S_, S_)), no_mark = S_, dead_codas = Lt(S_),
           table = Lt(Lt(S_)), atoms = Lt(S_)},
  rewrites = Lt(Ob{pattern = PAT, template = TPL}),
  inherent = Ob{vowel = S_, final = S_, coda_no = I_, signs = Lt(Pr(S_, I_))},
  endings = Ob{table = Lt(Ob{key = S_, ipa = S_, alts = Lt(S_), costs = Lt(I_)}), suffix = SSET,
               vowels = Lt(Ob{key = S_, reduced = SSET, readings = SSET}),
               sources = Lt(Ob{surface = S_, vowels = SSET})},
  phonemes = SSET,
}

local SLOT_ARGS = {
  ["and"] = "preds", ["or"] = "preds", ["not"] = {PRED}, ["true"] = {}, ["false"] = {},
  exists = {I_}, ebit = {I_, I_}, entry_in = {I_, ESET}, top_in = {I_, SSET},
  top_seg_in = {I_, I_, SSET}, syll = {OPAQUE}, word_in = {SSET}, word_has = {SSET},
  syllpos = {I_, OPAQUE}, word_final = {},
  count = {OPAQUE, OPAQUE, PRED, I_, OPAQUE}, word_has_entry = {ESET}, reading_vowel = {I_}, top_nucleus = {OPAQUE},
}
local GATE_ARGS = {["and"] = "preds", ["or"] = "preds", ["not"] = {GATE}, ["true"] = {},
                   spell_search = {PAT}, spell_empty = {}}
local DPRED_ARGS = {["and"] = "preds", ["or"] = "preds", ["not"] = {DPRED}, ["true"] = {},
                    back_reach = {SSET, SSET}, at_in = {I_, SSET}, at_end_or_in = {SSET},
                    ahead_match = {I_, PAT}, covered_by = {SSET}, later_has = {SSET},
                    spell = {GATE}}
local PRED_TABLES = {[PRED] = SLOT_ARGS, [GATE] = GATE_ARGS, [DPRED] = DPRED_ARGS}

local function walk(t, v, fs, fe)
  if t == S_ then return fs(v) end
  if t == SSET then
    local out = {}
    for k, x in ipairs(v) do out[k] = fs(x) end
    return out
  end
  if t == ESET then
    local out = {}
    for k, x in ipairs(v) do out[k] = fe(x) end
    return out
  end
  if t == I_ or t == PAT or t == OPAQUE then return v end
  if t == TPL then
    local out = {}
    for k, p in ipairs(v) do
      if p[1] == "lit" then out[k] = {"lit", fs(p[2])} else out[k] = {p[1], p[2]} end
    end
    return out
  end
  if type(t) == "string" then
    local tab = PRED_TABLES[t]
    local op = v[1]
    local args = tab[op]
    if args == nil then error("unknown predicate node " .. tostring(op)) end
    local out = {op}
    if args == "preds" then
      for k = 2, #v do out[k] = walk(t, v[k], fs, fe) end
    else
      for k = 1, min(#args, #v - 1) do out[k + 1] = walk(args[k], v[k + 1], fs, fe) end
    end
    return out
  end
  local kind = t[1]
  if kind == "list" then
    local out = {}
    for k, x in ipairs(v) do out[k] = walk(t[2], x, fs, fe) end
    return out
  end
  if kind == "pair" then return {walk(t[2], v[1], fs, fe), walk(t[3], v[2], fs, fe)} end
  local out = {}
  for k, x in pairs(v) do
    local sub = t[2][k]
    if sub == nil then error("unknown IR field " .. k) end
    out[k] = walk(sub, x, fs, fe)
  end
  return out
end

-- The readable form of a canonical IR document (layout.decode).
local function decode(doc)
  local strings = {}
  for k, s in ipairs(doc.strings) do strings[k] = from_cps(s) end
  local fs = function(i) return strings[i + 1] end
  local keys = {}
  for k, e in ipairs(doc.entries or {}) do keys[k] = strings[e.key + 1] end
  local fe = function(i) return keys[i + 1] end
  local body = {}
  for k, v in pairs(doc) do if LAYOUT[2][k] then body[k] = v end end
  local ir = walk(LAYOUT, body, fs, fe)
  ir.ir_version, ir.lang = doc.ir_version, doc.lang
  ir.ranges = doc.chars.ranges
  ir.bits = doc.bits or {}
  return ir
end

-- ═══ the pattern matcher (pattern.py, primitive 2) ═════════════════════════

local function in_set(node, c)
  local hit = false
  for _, r in ipairs(node[3]) do
    if r[1] <= c and c <= r[2] then hit = true; break end
  end
  return hit ~= T(node[2])
end

local function one(node, s, i)
  if i >= #s then return false end
  local op = node[1]
  if op == "lit" then return s[i + 1] == node[2] end
  if op == "any" then return s[i + 1] ~= 10 end
  return in_set(node, s[i + 1])
end

local pmatch

local function pseq(node, a, s, i, groups, k)
  if a > #node then return k(i, groups) end
  return pmatch(node[a], s, i, groups, function(j, g) return pseq(node, a + 1, s, j, g, k) end)
end

local function prepeat(node, s, i, groups, k, count)
  local op = node[1]
  local limit = op == "opt" and 1 or -1
  if limit < 0 or count < limit then
    local r = pmatch(node[2], s, i, groups, function(j, g)
      if j == i then return nil end -- an empty iteration ends the loop, as in re
      return prepeat(node, s, j, g, k, count + 1)
    end)
    if r ~= nil then return r end
  end
  if op == "plus" and count == 0 then return nil end
  return k(i, groups)
end

local function capture(j, g) return {j, g} end

function pmatch(node, s, i, groups, k)
  local op = node[1]
  if op == "lit" or op == "any" or op == "set" then
    if one(node, s, i) then return k(i + 1, groups) end
    return nil
  end
  if op == "seq" then return pseq(node, 2, s, i, groups, k) end
  if op == "alt" then
    for a = 2, #node do
      local r = pmatch(node[a], s, i, groups, k)
      if r ~= nil then return r end
    end
    return nil
  end
  if op == "bol" then
    if i == 0 then return k(i, groups) end
    return nil
  end
  if op == "eol" then
    local n = #s
    if i == n or (i == n - 1 and s[i + 1] == 10) then return k(i, groups) end
    return nil
  end
  if op == "group" then
    local n = node[2]
    return pmatch(node[3], s, i, groups, function(j, g)
      local g2 = {}
      for x = 1, #g do g2[x] = g[x] end
      g2[n + 1] = {i, j}
      return k(j, g2)
    end)
  end
  if op == "star" or op == "plus" or op == "opt" then return prepeat(node, s, i, groups, k, 0) end
  if op == "ahead" then
    local found = pmatch(node[3], s, i, groups, capture)
    if T(node[2]) then
      if found == nil then return k(i, groups) end
      return nil
    end
    if found ~= nil then return k(i, found[2]) end
    return nil
  end
  if op == "behind" then
    local ok = i > 0 and one(node[3], s, i - 1)
    if ok ~= T(node[2]) then return k(i, groups) end
    return nil
  end
  error("unknown pattern node " .. tostring(op))
end

local function group_count(node)
  local op = node[1]
  if op == "group" then return max(node[2], group_count(node[3])) end
  if op == "lit" or op == "any" or op == "set" or op == "bol" or op == "eol" then return 0 end
  local first = (op == "ahead" or op == "behind") and 3 or 2
  local best = 0
  for x = first, #node do
    if type(node[x]) == "table" then best = max(best, group_count(node[x])) end
  end
  return best
end

-- The leftmost match at or after start: start, end, groups.
local function psearch(node, s, start, ngroups, no_empty_at)
  no_empty_at = no_empty_at or -1
  local empty = {}
  for x = 1, (ngroups or 0) + 1 do empty[x] = false end
  for i = start or 0, #s do
    local r
    if i == no_empty_at then
      r = pmatch(node, s, i, empty, function(j, g)
        if j == i then return nil end
        return {j, g}
      end)
    else
      r = pmatch(node, s, i, empty, capture)
    end
    if r ~= nil then return i, r[1], r[2] end
  end
  return nil
end

local function match_at(node, s, i)
  local empty = {}
  for x = 1, group_count(node) + 1 do empty[x] = false end
  return pmatch(node, s, i, empty, capture) ~= nil
end

-- re.sub: replace every non-overlapping match, left to right.
local function psub(node, template, s, strings, count)
  count = count or 0
  local ngroups = group_count(node)
  local out = {}
  local pos, done, made = 0, 0, 0
  local no_empty_at = -1
  while pos <= #s and not (count ~= 0 and made == count) do
    local start, e, groups = psearch(node, s, pos, ngroups, no_empty_at)
    if start == nil then break end
    for x = done + 1, start do out[#out + 1] = s[x] end
    for _, part in ipairs(template) do
      if part[1] == "lit" then
        for _, c in ipairs(strings[part[2] + 1]) do out[#out + 1] = c end
      else
        local span = groups[part[2] + 1]
        if span then
          for x = span[1] + 1, span[2] do out[#out + 1] = s[x] end
        end
      end
    end
    done, pos = e, e
    no_empty_at = (e == start) and e or -1
    made = made + 1
  end
  for x = done + 1, #s do out[#out + 1] = s[x] end
  return out
end

M.pattern = {search = psearch, sub = psub, match_at = match_at, group_count = group_count}

-- ═══ the interpreter ═══════════════════════════════════════════════════════

local P = {}
local MT = {__index = P}

function M.new(doc)
  if not M.SUPPORTED_IR_VERSIONS[doc.ir_version] then
    error("unsupported ir_version " .. tostring(doc.ir_version))
  end
  local names = {}
  for name in pairs(doc.primitives or {}) do names[#names + 1] = name end
  sort(names)
  for _, name in ipairs(names) do
    local version = doc.primitives[name]
    if M.SEMANTICS[name] ~= version then
      error(("unsupported primitive version: %s needs %s, this interpreter has %s")
        :format(name, tostring(version), tostring(M.SEMANTICS[name])))
    end
  end
  local ir = decode(doc)
  local self = setmetatable({ir = ir}, MT)
  local function first_index(names)
    local idx = {}
    for i = #names, 1, -1 do idx[names[i]] = i end
    return idx
  end
  local cidx, eidx = first_index(ir.bits.char or {}), first_index(ir.bits.entry or {})
  local missing = {}
  for _, n in ipairs(CHAR_NAMES) do if not cidx[n] then missing[#missing + 1] = n end end
  sort(missing)
  local emissing = {}
  for _, n in ipairs(ENTRY_NAMES) do if not eidx[n] then emissing[#emissing + 1] = n end end
  sort(emissing)
  for _, n in ipairs(emissing) do missing[#missing + 1] = n end
  if #missing > 0 then
    error("the IR's bit table lacks " .. concat(missing, ", "))
  end
  self._cbit, self._ebit = {}, {}
  for _, n in ipairs(CHAR_NAMES) do self._cbit[n] = 2 ^ (cidx[n] - 1) end
  for _, n in ipairs(ENTRY_NAMES) do self._ebit[n] = 2 ^ (eidx[n] - 1) end
  self._ranges = ir.ranges
  self._cc = {}
  local maps = ir.char_maps
  local function cmap(list)
    local m = {}
    for _, p in ipairs(list or {}) do m[C(p[1])] = p[2] end
    return m
  end
  self._casefold = cmap(maps.casefold)
  self._lower = cmap(maps.plain_lower)
  self._nfd = cmap(maps.nfd)
  self._ccc = {}
  for _, p in ipairs(maps.ccc) do self._ccc[C(p[1])] = p[2] end
  self._compose = {}
  for _, p in ipairs(maps.compose) do self._compose[C(p[1]) .. C(p[2])] = C(p[3]) end
  self._presentation = cmap(maps.presentation)
  self._fold = setof(maps.fold or {})
  self._nuclei, self._nuclei_order = {}, {}
  for _, pr in ipairs(ir.consonant_nuclei or {}) do
    if self._nuclei[pr[1]] == nil then self._nuclei_order[#self._nuclei_order + 1] = pr[1] end
    self._nuclei[pr[1]] = pr[2]
  end
  self._tone = ir.tone
  if T(self._tone) then
    self._tone_classes, self._tone_marks = {}, {}
    for _, pr in ipairs(self._tone.classes) do self._tone_classes[pr[1]] = pr[2] end
    for _, pr in ipairs(self._tone.marks) do self._tone_marks[pr[1]] = pr[2] end
    self._tone_table, self._tone_class_names = {}, {}
    for _, row in ipairs(self._tone.table) do
      local key = row[1] .. "|" .. row[2] .. "|" .. row[3]
      if self._tone_table[key] == nil then self._tone_table[key] = row[4] end
      self._tone_class_names[row[1]] = true
    end
  end
  self._rewrites = ir.rewrites or {}
  self._inherent = ir.inherent
  local endings = ir.endings
  if T(endings) then
    self._endings = {}
    for _, e in ipairs(endings.table) do self._endings[e.key] = e end
    self._ending_suffix = setof(endings.suffix)
    self._ending_vowels = {}
    for _, v in ipairs(endings.vowels) do
      self._ending_vowels[v.key] = {setof(v.reduced), setof(v.readings)}
    end
    self._ending_sources = {}
    for _, v in ipairs(endings.sources) do self._ending_sources[v.surface] = v.vowels end
  end
  self.entries = ir.entries or {}
  self._key_index = {}
  self._trie_keys = {}
  self._max_key = 0
  self._trie = {}
  self._bits = {}
  for i, e in ipairs(self.entries) do
    self._key_index[e.key] = i - 1
    self._bits[i] = e.bits
    if T(e.trie) then
      self._trie_keys[e.key] = true
      self._max_key = max(self._max_key, slen(e.key))
      local node = self._trie
      for _, c in ipairs(chars(e.key)) do
        local nxt = node[c]
        if not nxt then nxt = {}; node[c] = nxt end
        node = nxt
      end
      node[1] = e.key
    end
  end
  self._fallback = setof(ir.fallback or {})
  self.word = ir.word
  self._exceptions = {}
  for _, p in ipairs(self.word.exceptions) do self._exceptions[p[1]] = p[2] end
  self._fragment_words = {}
  for _, p in ipairs(self.word.words or {}) do self._fragment_words[p[1]] = p[2] end
  self.stress = ir.stress
  self.syll = ir.syllable or {}
  self._allo = ir.allophony
  if ir.allophone_map ~= nil then
    self._allophone_map = {}
    for _, p in ipairs(ir.allophone_map) do self._allophone_map[p[1]] = p[2] end
  end
  self._mark_atoms = ir.atoms.mark
  self._affricates = ir.atoms.affricates
  self._no_atoms = {}
  self._tilde = ir.beam.tilde
  self._hiatus_cache = {}
  self._syll_cache = {}
  self._seg_cache = setmetatable({}, {__mode = "k"})
  if T(self.stress) then
    self._cliticless = setof(self.stress.cliticless)
    local onsets = self.stress.mark_onsets
    if T(onsets) then
      self._mark_table = {}
      for _, t in ipairs(onsets.table) do self._mark_table[concat(t, "\1")] = true end
    end
  end
  self._hiatus_on = T(self.syll.closed_hiatus) or T(self.syll.final_diphthongs)
  self._semivowels = {}
  for _, p in ipairs(self.syll.semivowels or {}) do -- the role is a data string: read it as ASCII
    self._semivowels[p[1]] = schar(unpack(to_cps(p[2])))
  end
  local letters = self.syll.vowel_letters
  self._vowel_letters = T(letters) and setof(letters) or nil
  self._onsets = self.syll.onsets
  if T(self._onsets) then
    self._onset_table = {}
    for _, t in ipairs(self._onsets.table) do self._onset_table[concat(t, "\1")] = true end
    self._onset_velar = setof(self._onsets.velar)
  end
  local sy = self.syll
  self._cuts_on = T(sy.cut_pairs) or T(sy.glide_hiatus) or T(sy.stem_cuts) or T(sy.prefix_cuts)
    or T(sy.seams) or T(sy.foreign)
  if self._allo then
    for _, rule in ipairs(self._allo.rules) do
      rule._index = {}
      for k = #rule.phonemes, 1, -1 do rule._index[rule.phonemes[k]] = k end
    end
  end
  return self
end

-- ─── characters ────────────────────────────────────────────────────────────

function P:_char_bits(ch)
  local bits = self._cc[ch]
  if bits then return bits end
  local cp = cp_of(ch)
  local r = self._ranges
  local lo, hi = 1, #r
  bits = 0
  while lo <= hi do
    local mid = floor((lo + hi) / 2)
    local x = r[mid]
    if cp < x[1] then hi = mid - 1
    elseif cp > x[2] then lo = mid + 1
    else bits = x[3]; break end
  end
  self._cc[ch] = bits
  return bits
end

function P:_c(ch, name)
  return floor(self:_char_bits(ch) / self._cbit[name]) % 2 == 1
end

function P:_e(entry, name)
  return hasbit(self._bits[entry + 1], self._ebit[name])
end

-- The entry bits of slot j, with vowel as the token's inherent vowel leaves it.
function P:_slot_bits(ctx, j)
  local bits = self._bits[ctx.entries[j + 1] + 1]
  local vowel = ctx.tokens[j + 1].vowel
  if vowel == nil then return bits end
  local vb = self._ebit.vowel
  local has = hasbit(bits, vb)
  if vowel then return has and bits or bits + vb end
  return has and bits - vb or bits
end

function P:_comb(ch) return self:_c(ch, "combining") end
function P:_vowel_char(ch)
  return not self:_comb(ch) and (self:_c(ch, "orth_vowel") or self:_c(ch, "ipa_vowel"))
end

local function map_chars(map, text)
  local out = {}
  for i = 0, #text / 3 - 1 do
    local c = ssub(text, 3 * i + 1, 3 * i + 3)
    out[i + 1] = map[c] or c
  end
  return concat(out)
end
function P:lower(text) return map_chars(self._lower, text) end
function P:casefold(text) return map_chars(self._casefold, text) end

-- S1: NFC, the presentation-form map, then the rewrites in order.
function P:prepare(text)
  text = self:nfc(text)
  if T(self._fold) then
    local out = {}
    for _, ch in ipairs(chars(text)) do
      for _, c in ipairs(chars(self._nfd[ch] or ch)) do
        if not self._fold[c] then out[#out + 1] = c end
      end
    end
    text = self:nfc(concat(out))
  end
  if T(self._presentation) then text = map_chars(self._presentation, text) end
  for _, rw in ipairs(self._rewrites) do
    text = self:_sub(rw.pattern, rw.template, to_cps(text))
  end
  return text
end

-- NFC by table: full decomposition, canonical order, composition.
function P:nfc(text)
  local ccc, nfd = self._ccc, self._nfd
  local out = {}
  for i = 0, #text / 3 - 1 do
    local c = ssub(text, 3 * i + 1, 3 * i + 3)
    local d = nfd[c]
    if d then
      for j = 0, #d / 3 - 1 do out[#out + 1] = ssub(d, 3 * j + 1, 3 * j + 3) end
    else
      out[#out + 1] = c
    end
  end
  local i = 1
  while i <= #out do
    if (ccc[out[i]] or 0) ~= 0 then
      local j = i
      while j <= #out and (ccc[out[j]] or 0) ~= 0 do j = j + 1 end
      for a = i + 1, j - 1 do -- stable insertion sort by combining class
        local c, b = out[a], a - 1
        while b >= i and ccc[out[b]] > ccc[c] do out[b + 1] = out[b]; b = b - 1 end
        out[b + 1] = c
      end
      i = j
    else
      i = i + 1
    end
  end
  local result = {}
  local starter, last_ccc = 0, -1
  for _, c in ipairs(out) do
    local cc = ccc[c] or 0
    local skip = false
    if starter > 0 and (last_ccc < cc or (last_ccc == 0 and #result == starter)) then
      local composed = self._compose[result[starter] .. c]
      if composed then result[starter] = composed; skip = true end
    end
    if not skip then
      if cc == 0 then starter = #result + 1; last_ccc = -1 else last_ccc = cc end
      result[#result + 1] = c
      if cc == 0 then last_ccc = 0 end
    end
  end
  return concat(result)
end

-- ─── segmentation (primitive 11) ───────────────────────────────────────────

function P:segment(ipa, atoms)
  atoms = atoms or self._no_atoms
  local cache = self._seg_cache[atoms]
  if not cache then cache = {}; self._seg_cache[atoms] = cache end
  local hit = cache[ipa]
  if hit then return lsl(hit) end
  local segments = {}
  local i, n = 0, slen(ipa)
  while i < n do
    local seg
    for _, atom in ipairs(atoms) do
      local e = i + slen(atom)
      if startswith(ipa, atom, i) and not (e < n and self:_c(at(ipa, e), "modifier")) then
        if seg == nil or #atom > #seg then seg = atom end
      end
    end
    if seg == nil then
      local j = i + 1
      while j < n and self:_c(at(ipa, j), "modifier") do j = j + 1 end
      seg = sl(ipa, i, j)
    end
    segments[#segments + 1] = seg
    i = i + slen(seg)
  end
  cache[ipa] = segments
  return lsl(segments)
end

-- ─── S1, S4: tokenization ──────────────────────────────────────────────────

function P:_longest_match(text, start)
  local node = self._trie
  local best
  for i = start, min(start + self._max_key, slen(text)) - 1 do
    local ch = at(text, i)
    ch = self._casefold[ch] or ch
    node = (#ch == 3) and node[ch] or nil
    if node == nil then break end
    if node[1] ~= nil then best = node[1] end
  end
  return best
end

function P:_run(text, pos, bit)
  local e, n = pos, slen(text)
  while e < n and self:_c(at(text, e), bit) do e = e + 1 end
  return e
end

local function Token(kind, grapheme, entry, readings, position, length, vowel)
  return {kind = kind, grapheme = grapheme, entry = entry, readings = readings,
          position = position, length = length, vowel = vowel}
end

local function copy(t)
  local out = {}
  for k = 1, #t do out[k] = t[k] end
  return out
end

function P:tokenize(text)
  local tokens = {}
  local n = slen(text)
  local pos = 0
  local nucleus_at = -1
  while pos < n do
    local e = self:_run(text, pos, "space")
    if e > pos then
      tokens[#tokens + 1] = Token(WS, SPACE, -1, {}, pos, e - pos)
      pos = e
    else
      local done = false
      for _, bk in ipairs({{"punct", PUNCT}, {"digit", DIGIT}}) do
        e = self:_run(text, pos, bk[1])
        if e > pos then
          local span = sl(text, pos, e)
          if not (self._trie_keys[span] or self:_longest_match(text, pos) ~= nil) then
            tokens[#tokens + 1] = Token(bk[2], span, -1, {}, pos, e - pos)
            pos = e
            done = true
            break
          end
        end
      end
      if not done then
        local gkey = self:_longest_match(text, pos)
        local stop
        if gkey ~= nil and self:_e(self._key_index[gkey], "preposed") then
          stop = self:_preposed(text, pos, gkey, tokens)
        end
        if stop ~= nil then
          pos = stop
        elseif gkey ~= nil then
          gkey = self:_backoff(text, pos, gkey, tokens)
          if T(self._nuclei_order) then gkey = self:_unfuse_nucleus(text, pos, gkey, tokens) end
          local ei = self._key_index[gkey]
          local readings, length, vowel = copy(self.entries[ei + 1].cands), slen(gkey), nil
          if pos == nucleus_at and self._nuclei[gkey] ~= nil then
            readings, vowel = {self._nuclei[gkey]}, self:_e(ei, "vowel_nucleus")
          elseif T(self._inherent) and self:_e(ei, "takes_inherent") then
            readings, length, vowel, nucleus_at = self:_inherent_vowel(text, pos, ei, readings, tokens)
          end
          tokens[#tokens + 1] = Token(WORD, gkey, ei, readings, pos, length, vowel)
          pos = pos + length
        else
          local ch = at(text, pos)
          if self._fallback[ch] then
            local ei = self._key_index[ch]
            tokens[#tokens + 1] = Token(WORD, ch, ei, copy(self.entries[ei + 1].cands), pos, 1)
          else
            tokens[#tokens + 1] = Token(UNKNOWN, ch, -1, {}, pos, 1)
          end
          pos = pos + 1
        end
      end
    end
  end
  return tokens
end

-- 3.3.2 item 6: the inherent vowel of an abugida consonant letter.
function P:_inherent_vowel(text, pos, e, readings, tokens)
  local length = slen(self.entries[e + 1].key)
  local after = pos + length
  local nucleus_at = self:_consonant_nucleus_at(text, after, tokens)
  local next_ch = after < slen(text) and at(text, after) or ""
  if next_ch ~= "" and self:_c(next_ch, "virama") then return readings, length + 1, nil, nucleus_at end
  if nucleus_at >= 0 or self:_supplies_vowel_at(text, after) then return readings, length, nil, nucleus_at end
  local inherent = self._inherent
  if T(inherent.coda_no) and self:_syllable_has_nucleus(tokens) then return readings, length, nil, nucleus_at end
  if next_ch ~= "" and self:_e(e, "silent_before_consonant") then return readings, length, nil, nucleus_at end
  local vowel, bit = inherent.vowel, "vowel_inherent"
  if next_ch == "" and inherent.final ~= nil and self:_syllable_has_nucleus(tokens) then
    vowel, bit = inherent.final, "vowel_inherent_final"
  end
  local out = {}
  for k, r in ipairs(readings) do out[k] = r .. vowel end
  return out, length, self:_e(e, bit), nucleus_at
end

-- 3.3.2 item 5: the offset of a consonant letter at pos that is the nucleus
-- between an onset with no vowel and a coda, or -1.
function P:_consonant_nucleus_at(text, pos, tokens)
  if not T(self._nuclei_order) or self:_syllable_has_nucleus(tokens) then return -1 end
  pos = self:_skip_silent_marks(text, pos)
  local letter = self:_longest_match(text, pos)
  if letter == nil or self._nuclei[letter] == nil then return -1 end
  local close = self:_skip_silent_marks(text, pos + slen(letter))
  local coda = self:_longest_match(text, close)
  local coda_ipa = coda ~= nil and coda ~= "" and self.entries[self._key_index[coda] + 1].cands or nil
  if not T(coda_ipa) or coda_ipa[1] == "" or self:_is_nucleus(coda_ipa[1])
      or self:_supplies_vowel_at(text, close + slen(coda)) then
    return -1
  end
  return pos
end

function P:_skip_silent_marks(text, pos)
  while pos < slen(text) and self:_c(at(text, pos), "mark_spells_nothing") do pos = pos + 1 end
  return pos
end

-- A cluster key that ends in a consonant nucleus backs off to its head when
-- the letter is the nucleus.
function P:_unfuse_nucleus(text, pos, gkey, tokens)
  local cands = self.entries[self._key_index[gkey] + 1].cands
  if not T(cands) or self:_is_nucleus(cands[1]) then return gkey end
  for _, letter in ipairs(self._nuclei_order) do
    local head = sl(gkey, 0, slen(gkey) - slen(letter))
    if head ~= "" and endswith(gkey, letter) and self._trie_keys[head]
        and self:_consonant_nucleus_at(text, pos + slen(head), tokens) == pos + slen(head) then
      return head
    end
  end
  return gkey
end

-- 3.3.2 item 1: a vowel written before its consonant and read after it.
-- Appends the silent vowel token and the consonant token, and returns the
-- position after them, or nil when no consonant can host the vowel.
function P:_preposed(text, pos, gkey, tokens)
  local after = pos + slen(gkey)
  local ckey = self:_longest_match(text, after)
  if ckey == nil then return nil end
  local c = self._key_index[ckey]
  if self:_e(c, "silent_head") and self:_head_is_the_onset(gkey, c, text, after) then
    ckey = at(ckey, 0)
    c = self._key_index[ckey]
  end
  if not self:_e(c, "preposed_host") then return nil end
  local e = self._key_index[gkey]
  local ce = self.entries[c + 1]
  local host = T(ce.onset) and ce.onset or ce.cands
  local post = after + slen(ckey)
  local pkey, pend = self:_match_transparent(text, post)
  local tail = pkey ~= nil and self:_e(self._key_index[pkey], "circumfix_tail")
  local readings = {}
  if tail then
    readings = copy(host)
  else
    for _, r in ipairs(host) do
      for _, v in ipairs(self.entries[e + 1].cands) do readings[#readings + 1] = r .. v end
    end
  end
  tokens[#tokens + 1] = Token(WORD, gkey, e, {}, pos, slen(gkey))
  tokens[#tokens + 1] = Token(WORD, ckey, c, readings, after, slen(ckey))
  if not tail then return post end
  if pend > post then
    local p = self._key_index[pkey]
    tokens[#tokens + 1] = Token(WORD, sl(text, post, pend), p, copy(self.entries[p + 1].cands), post, pend - post)
    return pend
  end
  return post
end

-- The silent head of the host is the onset when the vowel ends open and
-- nothing audible follows the tail.
function P:_head_is_the_onset(gkey, c, text, after)
  if not self:_e(self._key_index[gkey], "preposed_open") or self:_e(c, "head_not_coda") then return false end
  local pos = after + slen(self.entries[c + 1].key)
  local first = true
  while pos < slen(text) do
    local nkey = self:_longest_match(text, pos)
    if nkey == nil then return not self:_c(at(text, pos), "alpha") end
    local n = self._key_index[nkey]
    if self:_e(n, "audible") or (first and self:_e(n, "spells_nothing")) then return false end
    first = false
    pos = pos + slen(nkey)
  end
  return true
end

-- The longest trie match at start that steps over chars with bit
-- mark_spells_nothing once the match has begun.
function P:_match_transparent(text, start)
  local node = self._trie
  local best, best_end, i = nil, start, start
  while i < slen(text) do
    local ch = at(text, i)
    ch = self._casefold[ch] or ch
    if #ch == 3 and node[ch] then
      node = node[ch]
      i = i + 1
      if node[1] ~= nil then best, best_end = node[1], i end
    elseif i > start and self:_c(at(text, i), "mark_spells_nothing") then
      i = i + 1
    else
      break
    end
  end
  return best, best_end
end

function P:_supplies_vowel_at(text, pos)
  local n = slen(text)
  while pos < n and self:_c(at(text, pos), "mark_spells_nothing") do pos = pos + 1 end
  for _, sign in ipairs(self._inherent.signs or {}) do
    if startswith(text, sign[1], pos) then return T(sign[2]) end
  end
  return pos < n and self:_c(at(text, pos), "supplies_vowel")
end

function P:_is_nucleus(ipa)
  for _, c in ipairs(chars(ipa)) do
    if self:_c(c, "ipa_vowel") or self:_c(c, "syllabic_mark") then return true end
  end
  return false
end

function P:_syllable_has_nucleus(tokens)
  for k = #tokens, 1, -1 do
    local tok = tokens[k]
    if tok.kind ~= WORD then return false end
    local first = tok.readings[1] or ""
    if not (#tok.readings == 1 and tok.readings[1] == "" and self:_e(tok.entry, "spells_nothing")) then
      if self:_e(tok.entry, "vowel_sign") or (first ~= "" and self:_is_nucleus(first)) then return true end
      if not (first ~= "" and self:_e(tok.entry, "postvocalic")) then return false end
    end
  end
  return false
end

function P:_backoff(text, pos, gkey, tokens)
  local n = slen(text)
  if self._hiatus_on and slen(gkey) > 1 and self:_c(at(gkey, 0), "orth_vowel") then
    gkey = self:_hiatus_prefix(text, pos, gkey)
  end
  local e = self._key_index[gkey]
  local after = pos + slen(gkey)
  if self:_e(e, "prevocalic_backoff") and after < n and self:_c(at(text, after), "orth_vowel") then
    gkey = sl(gkey, 0, slen(gkey) - 1)
    e = self._key_index[gkey]
  end
  if self:_e(e, "glide_final_key") then
    local after = pos + slen(gkey)
    local next_ch = after < n and at(text, after) or ""
    if next_ch ~= "" and self:_c(next_ch, "elision_apostrophe") and after + 1 < n
        and self:_c(at(text, after + 1), "alpha") then
      after = after + 1
      local low = at(text, after)
      low = self._casefold[low] or low
      local cands = self._trie_keys[low] and self.entries[self._key_index[low] + 1].cands
      local silent = cands and #cands == 1 and cands[1] == ""
      if silent and after + 1 < n and self:_c(at(text, after + 1), "alpha") then after = after + 1 end
      next_ch = at(text, after)
    end
    local nlow = next_ch ~= "" and (self._casefold[next_ch] or next_ch) or ""
    if not (next_ch ~= "" and self:_c(next_ch, "orth_vowel")) then
      local bit = next_ch ~= "" and "glide_vowel_cons" or "glide_vowel_final"
      if not self:_e(e, bit) then gkey = sl(gkey, 0, -1) end
    elseif not (slen(nlow) == 1 and self:_c(nlow, "front_letter")) then
      local prev
      for k = #tokens, 1, -1 do
        if tokens[k].kind == WORD then prev = tokens[k]; break end
      end
      local prev_ipa = (prev and #prev.readings > 0) and prev.readings[1] or ""
      local prev_is_vowel = prev_ipa ~= "" and self:_c(at(prev_ipa, -1), "ipa_vowel")
      if prev_is_vowel and self:_e(e, "glide_marker") and self._trie_keys[at(gkey, -1) .. nlow] then
        gkey = sl(gkey, 0, -1)
      end
    end
  end
  return gkey
end

function P:_hiatus_prefix(text, pos, gkey)
  local start = pos
  while start > 0 and self:_c(at(text, start - 1), "letter_or_mark") do start = start - 1 end
  local e = pos
  while e < slen(text) and self:_c(at(text, e), "letter_or_mark") do e = e + 1 end
  local word = sl(text, start, e)
  local hiatus = self._hiatus_cache[word]
  if hiatus == nil then
    hiatus = self:hiatus_positions(word)
    self._hiatus_cache[word] = hiatus
  end
  for cut = 1, slen(gkey) - 1 do
    if hiatus[pos - start + cut] and self._trie_keys[sl(gkey, 0, cut)] then return sl(gkey, 0, cut) end
  end
  return gkey
end

function P:grapheme_tokens(word)
  local out = {}
  for _, t in ipairs(self:tokenize(word)) do
    if t.kind == WORD then out[#out + 1] = t end
  end
  return out
end

-- ─── S2: words ─────────────────────────────────────────────────────────────

function P:_group_words(text, words)
  local tokens = self:tokenize(text)
  local current = {}
  local joined, after_hyphen = false, false
  local function flush()
    if #current > 0 then
      words[#words + 1] = {surface = concat(current), hyphen_joined = joined, pausal = false}
      current = {}
    end
  end
  for _, token in ipairs(tokens) do
    if token.kind == WS then
      flush()
      after_hyphen = false
    elseif token.kind == PUNCT and self:_internal_apostrophe(text, token) then
      current[#current + 1] = token.grapheme
    elseif token.kind == PUNCT and self:_opens_listed_word(text, token) then
      flush()
      joined, after_hyphen = after_hyphen, false
      current[#current + 1] = token.grapheme
    elseif token.kind == PUNCT then
      after_hyphen = #current > 0 and slen(token.grapheme) == 1 and self:_c(token.grapheme, "hyphen")
      flush()
      if #words > 0 then
        for _, c in ipairs(chars(token.grapheme)) do
          if self:_c(c, "pause") then words[#words].pausal = true; break end
        end
      end
    else
      local tail = sl(sl(text, token.position, token.position + token.length), slen(token.grapheme))
      if #current == 0 then joined, after_hyphen = after_hyphen, false end
      current[#current + 1] = token.grapheme .. tail
    end
  end
  flush()
end

function P:_apostrophe_token(token)
  return slen(token.grapheme) == 1 and self:_c(token.grapheme, "apostrophe")
end

function P:_internal_apostrophe(text, token)
  local start, e = token.position, token.position + token.length
  return T(self.word.internal_apostrophe) and self:_apostrophe_token(token)
    and 0 < start and e < slen(text)
    and self:_c(at(text, start - 1), "alpha") and self:_c(at(text, e), "alpha")
end

function P:_opens_listed_word(text, token)
  local start, e = token.position, token.position + token.length
  if not (T(self.word.internal_apostrophe) and self:_apostrophe_token(token)
          and (start == 0 or self:_c(at(text, start - 1), "whitespace"))) then
    return false
  end
  local stop = self:_run(text, e, "word_letter")
  if stop == e then return false end
  local key = self:casefold(APOS .. sl(text, e, stop))
  return self._exceptions[key] ~= nil or self._fragment_words[self:nfc(key)] ~= nil
end

-- ─── S3: overrides ─────────────────────────────────────────────────────────

function P:_strip_edges(key)
  local i, j = 0, slen(key)
  while i < j and self:_c(at(key, i), "edge_punct") do i = i + 1 end
  if i == j then return "" end
  while j > i and self:_c(at(key, j - 1), "edge_punct") do j = j - 1 end
  return sl(key, i, j)
end

function P:_whole_word_override(word)
  local marks = setof(self.word.silent_stress_marks)
  local kept = {}
  for _, c in ipairs(chars(word)) do
    if not marks[c] then kept[#kept + 1] = c end
  end
  local key = self:casefold(concat(kept))
  local keys = {key}
  local stripped = self:_strip_edges(key)
  if stripped ~= "" and stripped ~= key then keys[#keys + 1] = stripped end
  if T(self.word.internal_apostrophe) then
    for k = 1, #keys do
      if contains(keys[k], RSQUO) then keys[#keys + 1] = sreplace(keys[k], RSQUO, APOS) end
    end
  end
  for _, k in ipairs(keys) do
    local hit = self._exceptions[k]
    if hit == nil then hit = self._fragment_words[self:nfc(k)] end
    if hit ~= nil then return hit end
  end
  return nil
end

function P:_elided_hosts(word)
  if not (T(self.word.apostrophe_elision) and T(self.word.internal_apostrophe)) then return {} end
  local wc = chars(word)
  local any = false
  for _, c in ipairs(wc) do if self:_c(c, "apostrophe") then any = true; break end end
  if not any then return {} end
  local tokens = self:grapheme_tokens(word)
  local splits = {}
  for i0, mark in ipairs(wc) do
    local i = i0 - 1
    if self:_c(mark, "apostrophe") and 0 < i and i < #wc - 1 then
      local host = sl(word, i + 1)
      local before
      for _, t in ipairs(tokens) do
        if t.position < i then before = t.grapheme end
      end
      if self:_c(wc[i], "alpha") and before ~= nil
          and not self:_c(at(before, 0), "orth_vowel")
          and (self:_c(at(host, 0), "orth_vowel") or self:_c(at(host, 0), "elision_h")) then
        splits[#splits + 1] = {i, host}
      end
    end
  end
  return splits
end

function P:_override_for(word)
  local override = self:_whole_word_override(word)
  if override ~= nil then return override end
  for _, split in ipairs(self:_elided_hosts(word)) do
    local host_ipa = self:_whole_word_override(split[2])
    if host_ipa ~= nil then
      return self:_join_clitic(self:_clitic_ipa(word, split[1]), host_ipa)
    end
  end
  return nil
end

function P:_join_clitic(clitic, host_ipa)
  if not inset(self.word.clitic_marks, sl(host_ipa, 0, 1)) then return clitic .. host_ipa end
  local vowel = false
  for _, c in ipairs(chars(clitic)) do if self:_c(c, "ipa_vowel") then vowel = true; break end end
  if not vowel then return at(host_ipa, 0) .. clitic .. sl(host_ipa, 1) end
  local segments = self:segment(clitic, self._affricates)
  if self:_c(at(segments[#segments], 0), "ipa_vowel") then return clitic .. host_ipa end
  return concat(segments, "", 1, #segments - 1) .. at(host_ipa, 0) .. segments[#segments] .. sl(host_ipa, 1)
end

function P:_clitic_ipa(word, apostrophe)
  local paths = self:_word_paths(word, 1)
  if #paths == 0 then return "" end
  local count = 0
  for _, t in ipairs(self:grapheme_tokens(word)) do
    if t.position < apostrophe then count = count + 1 end
  end
  return concat(lsl(paths[1][1], 0, count))
end

function P:_is_cliticless(word, elided)
  if elided == nil then elided = true end
  if not T(self.stress) or not T(self._cliticless) then return false end
  local key = self:nfc(self:casefold(word))
  if self._cliticless[key] then return true end
  local stripped = self:_strip_edges(key)
  if stripped ~= "" and stripped ~= key and self._cliticless[stripped] then return true end
  if elided then
    for _, split in ipairs(self:_elided_hosts(word)) do
      if self:_is_cliticless(split[2], false) then return true end
    end
  end
  return false
end

-- ─── predicates (primitive 5) ──────────────────────────────────────────────

function P:_eval(p, ctx, i)
  local op = p[1]
  if op == "and" then
    for k = 2, #p do if not self:_eval(p[k], ctx, i) then return false end end
    return true
  end
  if op == "or" then
    for k = 2, #p do if self:_eval(p[k], ctx, i) then return true end end
    return false
  end
  if op == "not" then return not self:_eval(p[2], ctx, i) end
  if op == "true" then return true end
  if op == "false" then return false end
  local n = #ctx.entries
  if op == "exists" then
    local j = i + p[2]
    return 0 <= j and j < n
  end
  if op == "ebit" then
    local j = i + p[2]
    return 0 <= j and j < n and hasbit(self:_slot_bits(ctx, j), 2 ^ p[3])
  end
  if op == "entry_in" then
    local j = i + p[2]
    return 0 <= j and j < n and inset(p[3], self.entries[ctx.entries[j + 1] + 1].key)
  end
  if op == "syll" then return self:_syll(p[2], ctx, i) end
  if op == "syllpos" then
    local j = i + p[2]
    return 0 <= j and j < n and self:_syllable_position(ctx, j) == p[3]
  end
  if op == "word_in" then return inset(p[2], self:lower(ctx.source)) end
  if op == "word_has" then
    local word = self:lower(ctx.source)
    for _, g in ipairs(p[2]) do if contains(word, g) then return true end end
    return false
  end
  if op == "word_final" then
    if i + 1 >= n then return true end
    if ctx.cands == nil then return false end
    for j = i + 1, n - 1 do
      local c = ctx.cands[j + 1]
      if not (#c == 0 or c[1][1] == "") then return false end
    end
    return true
  end
  if op == "top_seg_in" then
    local j = i + p[2]
    if not (0 <= j and j < n) then return false end
    local c = ctx.cands[j + 1]
    if #c == 0 or c[1][1] == "" then return false end
    local segs = self:segment(c[1][1], self._allo.atoms)
    return inset(p[4], T(p[3]) and segs[#segs] or segs[1])
  end
  if op == "top_nucleus" then
    for j = p[2] == "later" and i + 1 or 0, n - 1 do
      local c = ctx.cands[j + 1]
      if j ~= i and #c > 0 then
        for _, seg in ipairs(self:segment(c[1][1])) do
          if self:_c(at(seg, 0), "nucleus_base") then return true end
          for _, ch in ipairs(chars(seg)) do if self:_c(ch, "syllabic") then return true end end
        end
      end
    end
    return false
  end
  if op == "top_in" then
    local j = i + p[2]
    if not (0 <= j and j < n) then return false end
    local c = ctx.cands[j + 1]
    return #c > 0 and inset(p[3], c[1][1])
  end
  if op == "count" then
    local lo = p[2] == "start" and 0 or max(0, i + p[2])
    local hi = p[3] == "end" and n - 1 or min(n - 1, i + p[3])
    local skip = (#p == 6 and p[6] == "others") and i or -1
    local hits = 0
    for j = lo, hi do
      if j ~= skip and self:_eval(p[4], ctx, j) then hits = hits + 1 end
    end
    return hits >= p[5]
  end
  if op == "reading_vowel" then
    local j = i + p[2]
    if not (0 <= j and j < n) then return false end
    local readings = ctx.tokens[j + 1].readings
    if #readings == 0 then return false end
    for _, c in ipairs(chars(readings[1])) do if self:_c(c, "ipa_vowel") then return true end end
    return false
  end
  if op == "word_has_entry" then
    for _, e in ipairs(ctx.entries) do
      if inset(p[2], self.entries[e + 1].key) then return true end
    end
    return false
  end
  error("unknown predicate node " .. tostring(op))
end

function P:_syll(rel, ctx, i)
  if rel == "open" or rel == "closed" then
    local status = ctx.aperture and ctx.aperture[i + 1]
    return status ~= nil and status ~= NONE and status == (rel == "open")
  end
  local idx = ctx.syll_idx and ctx.syll_idx[i + 1] or nil
  local st = ctx.stressed
  if rel == "has_stress" then return st ~= nil and idx ~= nil end
  if st == nil or idx == nil then return false end
  if rel == "idx_eq_stressed" then return idx == st end
  if rel == "idx_lt_stressed" then return idx < st end
  if rel == "idx_gt_stressed" then return idx > st end
  if rel == "idx_eq_stressed_minus_1" then return idx == st - 1 end
  if rel == "idx_in_secondary" then return ctx.secondary[idx] == true end
  error("unknown syll relation " .. tostring(rel))
end

function P:_syllable_position(ctx, j)
  if hasbit(self:_slot_bits(ctx, j), self._ebit.vowel) then return "nucleus" end
  local k = j + 1
  while k < #ctx.entries and self:_e(ctx.entries[k + 1], "spells_nothing") do k = k + 1 end
  if k < #ctx.entries and hasbit(self:_slot_bits(ctx, k), self._ebit.vowel) then return "onset" end
  return "coda"
end

-- ─── S6: positional candidates; 3.3.5 candidate lists ──────────────────────

local function by_cost_then_ipa(a, b)
  if a[2] ~= b[2] then return a[2] < b[2] end
  return a[1] < b[1]
end

local function rank_costs(n)
  local costs = {}
  for r = 1, n do costs[r] = (r - 1) * 1000000 end
  return costs
end

local function same_list(a, b)
  if #a ~= #b then return false end
  for k = 1, #a do if a[k] ~= b[k] then return false end end
  return true
end

function P:_branches(ctx, i, token)
  local entry = self.entries[ctx.entries[i + 1] + 1]
  local base = token.readings
  local candidates, costs
  for _, rule in ipairs(entry.positional or {}) do
    if self:_eval(rule[1], ctx, i) then
      local seen = setof(rule[2])
      candidates = copy(rule[2])
      for _, c in ipairs(base) do
        if not seen[c] then candidates[#candidates + 1] = c end
      end
      costs = rank_costs(#candidates)
      break
    end
  end
  if candidates == nil then
    candidates = base
    costs = same_list(token.readings, entry.cands) and entry.costs or rank_costs(#candidates)
  end
  local branches = {}
  local amap = self._allophone_map
  for rank, ipa in ipairs(candidates) do
    if T(amap) and amap[ipa] then
      for a_rank, allophone in ipairs(amap[ipa]) do
        branches[#branches + 1] = {allophone, costs[rank] + 500000 * (a_rank - 1)}
      end
    else
      branches[#branches + 1] = {ipa, costs[rank]}
    end
  end
  local best, order = {}, {}
  for _, b in ipairs(branches) do
    local old = best[b[1]]
    if old == nil then order[#order + 1] = b[1] end
    if old == nil or b[2] < old then best[b[1]] = b[2] end
  end
  local out = {}
  for k, ipa in ipairs(order) do out[k] = {ipa, best[ipa]} end
  sort(out, by_cost_then_ipa)
  return out
end

-- ─── S7: allophony ─────────────────────────────────────────────────────────

local function Ctx(entries, tokens, syll_idx, stressed, secondary, cands, source, aperture)
  return {entries = entries, tokens = tokens, syll_idx = syll_idx, stressed = stressed,
          secondary = secondary or {}, cands = cands, source = source or "", aperture = aperture}
end

local function join_graphemes(tokens)
  local out = {}
  for k, t in ipairs(tokens) do out[k] = t.grapheme end
  return concat(out)
end

function P:_rescore_pass(runs, tokens, entries, cands, syll_idx, stressed, secondary)
  local out = copy(cands)
  for _, run in ipairs(runs) do
    local start, e = run[1], run[2]
    local toks = lsl(tokens, start, e)
    local ctx = Ctx(lsl(entries, start, e), toks, syll_idx and lsl(syll_idx, start, e) or nil,
                    stressed, secondary, lsl(cands, start, e), join_graphemes(toks))
    for loc = 0, e - start - 1 do
      local new = self:_rescore_slot(ctx, loc)
      if new ~= nil then out[start + loc + 1] = ssort(new, by_cost_then_ipa) end
    end
  end
  return out
end

function P:_rescore_slot(ctx, i)
  local new
  for idx, cand in ipairs(ctx.cands[i + 1]) do
    local surface = self:_realize(cand[1], ctx, i)
    if surface ~= nil and surface ~= cand[1] then
      if new == nil then new = copy(ctx.cands[i + 1]) end
      new[idx] = {surface, cand[2]}
    end
  end
  local feature = self:_neighbor_mutation(ctx, i)
  if feature ~= nil and feature ~= "" then
    local base = new or ctx.cands[i + 1]
    local mutated, changed = {}, false
    for k, cand in ipairs(base) do
      if cand[1] ~= "" and not contains(cand[1], feature) then
        mutated[k] = {cand[1] .. feature, cand[2]}
        changed = true
      else
        mutated[k] = cand
      end
    end
    if changed then new = mutated end
  end
  return new
end

function P:_neighbor_mutation(ctx, i)
  for _, step in ipairs({1, -1}) do
    local j = i + step
    if 0 <= j and j < #ctx.entries and #ctx.cands[j + 1] > 0 then
      local ipa = ctx.cands[j + 1][1][1]
      local marker = ctx
      if ctx.syll_idx ~= nil then
        marker = {}
        for k, v in pairs(ctx) do marker[k] = v end
        marker.syll_idx = copy(ctx.syll_idx)
        marker.syll_idx[j + 1] = ctx.syll_idx[i + 1]
      end
      for _, rule in ipairs(self._allo.rules) do
        if rule.mutate_at == step and rule._index[ipa] and self:_eval(rule.when, marker, j) then
          return rule.mutate
        end
      end
    end
  end
  return nil
end

function P:_twin_side(ipa, ctx, i)
  if not T(self._allo.geminate) then return nil end
  if ipa == "" then return nil end
  for _, seg in ipairs(self:segment(ipa)) do
    if self:_c(at(seg, 0), "ipa_vowel") then return nil end
  end
  local own = self:lower(ctx.tokens[i + 1].grapheme)
  for _, step in ipairs({1, -1}) do
    local j = i + step
    if 0 <= j and j < #ctx.entries then
      local c = ctx.cands[j + 1]
      if #c > 0 and c[1][1] == ipa and own == self:lower(ctx.tokens[j + 1].grapheme) then
        local a, b = ctx.tokens[i + 1], ctx.tokens[j + 1]
        if a.position + a.length == b.position or b.position + b.length == a.position then
          return step
        end
      end
    end
  end
  return nil
end

function P:_heterosyllabic(ctx, i, step)
  local before, after = i - step, i + 2 * step
  local n = #ctx.entries
  return 0 <= before and before < n and hasbit(self:_slot_bits(ctx, before), self._ebit.vowel)
    and 0 <= after and after < n and hasbit(self:_slot_bits(ctx, after), self._ebit.vowel)
end

function P:_realize(ipa, ctx, i)
  local twin = self:_twin_side(ipa, ctx, i)
  for _, rule in ipairs(self._allo.rules) do
    local k = rule._index[ipa]
    if k and self:_eval(rule.when, ctx, i) then
      local skip = false
      if twin ~= nil and not T(rule.aware[k]) then
        local trig = twin > 0 and rule.trig_next or rule.trig_prev
        skip = not (T(trig) and self:_heterosyllabic(ctx, i, twin))
      end
      if not skip then return rule.out[k] end
    end
  end
  local segments = self:segment(ipa, self._allo.atoms)
  if #segments <= 1 then return nil end
  return self:_realize_segments(segments, ctx, i)
end

function P:_realize_segments(segments, ctx, i)
  local changed = false
  local out = {}
  local inserted
  for k0, seg in ipairs(segments) do
    local slot_ctx = ctx
    if self:_c(at(seg, 0), "ipa_vowel") and not self:_holds_vowel(ctx, i) then
      if inserted == nil then inserted = self:_inserted_vowel_context(ctx, i) end
      slot_ctx = inserted
    end
    local surface = self:_realize_one_segment(seg, segments, k0 - 1, ctx, i, slot_ctx)
    if surface ~= nil and surface ~= seg then
      changed = true
      out[#out + 1] = surface
    else
      out[#out + 1] = seg
    end
  end
  return changed and concat(out) or nil
end

function P:_holds_vowel(ctx, i)
  if self:_e(ctx.entries[i + 1], "holds_vowel") then return true end
  for _, r in ipairs(ctx.tokens[i + 1].readings) do
    for _, c in ipairs(chars(r)) do if self:_c(c, "ipa_vowel") then return true end end
  end
  return false
end

-- The slot context of a vowel a rule inserted: its own unstressed syllable
-- after the nearest earlier slot that holds a vowel.
function P:_inserted_vowel_context(ctx, i)
  if ctx.syll_idx == nil or ctx.stressed == nil then return ctx end
  local before = -1
  for step = 1, i do
    if self:_holds_vowel(ctx, i - step) then
      before = ctx.syll_idx[i - step + 1]
      break
    end
  end
  local syll_idx = copy(ctx.syll_idx)
  syll_idx[i + 1] = before + 1
  local stressed = ctx.stressed > before and ctx.stressed + 1 or ctx.stressed
  local new = {}
  for k, v in pairs(ctx) do new[k] = v end
  new.syll_idx, new.stressed = syll_idx, stressed
  return new
end

local WORD_FINAL = {"word_final"}

function P:_realize_one_segment(seg, segments, k, ctx, i, slot_ctx)
  local atoms = self._allo.atoms
  local n = #ctx.entries
  local prev, nxt
  if k > 0 then
    prev = segments[k]
  elseif i > 0 and #ctx.cands[i] > 0 then
    local prev_segs = self:segment(ctx.cands[i][1][1], atoms)
    prev = prev_segs[#prev_segs]
  end
  if k < #segments - 1 then
    nxt = segments[k + 2]
  elseif i + 1 < n and #ctx.cands[i + 2] > 0 then
    local next_segs = self:segment(ctx.cands[i + 2][1][1], atoms)
    nxt = next_segs[1]
  end
  local initial = i == 0 and k == 0
  local final = self:_eval(WORD_FINAL, ctx, i) and k == #segments - 1
  for _, rule in ipairs(self._allo.rules) do
    local seg_rule = rule.seg
    if seg_rule ~= nil and rule._index[seg] then
      local ok = true
      if seg_rule.initial >= 0 and (seg_rule.initial ~= 0) ~= initial then ok = false end
      if ok and seg_rule.final >= 0 and (seg_rule.final ~= 0) ~= final then ok = false end
      if ok and T(seg_rule.prev) and (prev == nil or not inset(seg_rule.prev, prev)) then ok = false end
      if ok and T(seg_rule.next) and (nxt == nil or not inset(seg_rule.next, nxt)) then ok = false end
      if ok and self:_eval(rule.slot_when, slot_ctx, i) then return rule.out[rule._index[seg]] end
    end
  end
  return nil
end

-- ─── S8: the beam ──────────────────────────────────────────────────────────

function P:_carrier_split(seg)
  local j = slen(seg)
  while j > 0 do
    local c = at(seg, j - 1)
    if not (self:_c(c, "length") or (c ~= self._tilde and self:_comb(c))) then break end
    j = j - 1
  end
  return j
end

function P:_carrier_tail(seg)
  local j = self:_carrier_split(seg)
  return j > 0 and at(seg, j - 1) or ""
end

function P:_is_carrier(ch) return ch ~= "" and self:_c(ch, "nasal_carrier") end

function P:_splice(segs)
  local new = copy(segs)
  for i = #new, 1, -1 do
    if new[i] ~= "" then
      local j = self:_carrier_split(new[i])
      new[i] = sl(new[i], 0, j) .. self._tilde .. sl(new[i], j)
      new[#new + 1] = ""
      return new
    end
  end
  new[#new + 1] = self._tilde
  return new
end

function P:_constrain_nasal_carriers(slots)
  for idx = 2, #slots do
    local branches = slots[idx]
    local only_tilde = #branches > 0
    for _, b in ipairs(branches) do if b[1] ~= self._tilde then only_tilde = false; break end end
    if only_tilde then
      local j = idx - 1
      while j >= 1 do
        local prev = slots[j]
        if #prev == 0 then break end
        local has_empty = false
        local kept = {}
        for _, b in ipairs(prev) do
          if b[1] == "" then has_empty = true end
          if b[1] == "" or self:_is_carrier(self:_carrier_tail(b[1])) then kept[#kept + 1] = b end
        end
        if #kept > 0 and #kept ~= #prev then slots[j] = kept end
        if not has_empty then break end
        j = j - 1
      end
    end
  end
end

local function by_cost(a, b) return a[2] < b[2] end

function P:_expand(beam, branches, width)
  local new = {}
  local tilde = self._tilde
  for _, path in ipairs(beam) do
    local segs, sc = path[1], path[2]
    for _, br in ipairs(branches) do
      local ipa, cost = br[1], br[2]
      if ipa == tilde then
        local tail = ""
        for k = #segs, 1, -1 do
          if segs[k] ~= "" then tail = self:_carrier_tail(segs[k]); break end
        end
        if tail == tilde then
          local s2 = copy(segs); s2[#s2 + 1] = ""
          new[#new + 1] = {s2, sc + cost}
        elseif self:_is_carrier(tail) then
          new[#new + 1] = {self:_splice(segs), sc + cost}
        end
      else
        local s2 = copy(segs); s2[#s2 + 1] = ipa
        new[#new + 1] = {s2, sc + cost}
      end
    end
  end
  if #new == 0 then
    for _, path in ipairs(beam) do
      local segs, sc = path[1], path[2]
      for _, br in ipairs(branches) do
        if br[1] == tilde then
          new[#new + 1] = {self:_splice(segs), sc + br[2]}
        else
          local s2 = copy(segs); s2[#s2 + 1] = br[1]
          new[#new + 1] = {s2, sc + br[2]}
        end
      end
    end
  end
  ssort(new, by_cost)
  return lsl(new, 0, width)
end

-- Beam paths of word: {segments, cost, graphemes}, best first.
function P:_word_paths(word, width)
  local tokens = self:tokenize(word)
  local g_tokens, entries = {}, {}
  for _, t in ipairs(tokens) do
    if t.kind == WORD then g_tokens[#g_tokens + 1] = t; entries[#entries + 1] = t.entry end
  end
  local syll_idx, stressed, runs, aperture
  local secondary = {}
  if T(self.word.context_beam) and #g_tokens > 0 then
    runs = {{0, #g_tokens}}
    local sylls = {}
    if self.stress ~= nil or self.syll.silent_tail ~= nil then sylls = self:syllables(word) end
    if self.stress ~= nil then
      stressed = #sylls > 1 and self:detect_stress(word, sylls) or 0
      if self:_is_cliticless(word) then stressed = NO_STRESS end
      secondary = self:secondary_positions(#sylls, stressed)
    end
    syll_idx = self:_map_tokens_to_syllables(g_tokens, sylls)
    if self.syll.silent_tail ~= nil then aperture = self:_aperture(sylls, syll_idx) end
  else
    runs = {}
    local start, g = 0, 0
    for _, t in ipairs(tokens) do
      if t.kind == WORD then
        g = g + 1
      elseif g > start then
        runs[#runs + 1] = {start, g}
        start = g
      end
    end
    if g > start then runs[#runs + 1] = {start, g} end
  end
  local cands = {}
  for k = 1, #g_tokens do cands[k] = {} end
  for _, run in ipairs(runs) do
    local start, e = run[1], run[2]
    local ctx = Ctx(lsl(entries, start, e), lsl(g_tokens, start, e),
                    syll_idx and lsl(syll_idx, start, e) or nil, stressed, secondary, nil, nil,
                    aperture and lsl(aperture, start, e) or nil)
    for loc = 0, e - start - 1 do
      cands[start + loc + 1] = self:_branches(ctx, loc, g_tokens[start + loc + 1])
    end
  end
  if T(self._allo) then
    for _ = 1, self._allo.passes do
      cands = self:_rescore_pass(runs, g_tokens, entries, cands, syll_idx, stressed, secondary)
    end
  end
  self:_constrain_nasal_carriers(cands)
  local beam = {{{}, 0}}
  local spelled = {}
  for i, branches in ipairs(cands) do
    if #branches > 0 then
      spelled[#spelled + 1] = g_tokens[i].grapheme
      beam = self:_expand(beam, branches, width)
    end
  end
  local paths = {}
  for k, b in ipairs(beam) do paths[k] = {b[1], b[2], spelled, concat(b[1])} end
  ssort(paths, function(a, b)
    if a[2] ~= b[2] then return a[2] < b[2] end
    return a[4] < b[4]
  end)
  return paths
end

-- ─── S5: written syllables, hiatus, the stress decision ────────────────────

function P:_strip_silent_tail(syllable)
  local tail = setof(self.syll.silent_tail)
  local changed = true
  while changed and syllable ~= "" do
    changed = false
    for size = min(3, slen(syllable)), 1, -1 do
      if tail[self:lower(sl(syllable, -size))] then
        syllable = sl(syllable, 0, -size)
        changed = true
        break
      end
    end
  end
  return syllable
end

function P:_trim_edge(syllable)
  local trimmed = false
  while syllable ~= "" and not (self:_c(at(syllable, -1), "alpha") or self:_comb(at(syllable, -1))) do
    syllable = sl(syllable, 0, -1)
    trimmed = true
  end
  return syllable, trimmed
end

function P:_has_orth_vowel(s)
  for _, ch in ipairs(chars(s)) do if self:_c(ch, "orth_vowel") then return true end end
  return false
end

-- Per slot: true for an open written syllable, false for a closed one, nil
-- when the slot has no syllable with a vowel.
function P:_aperture(sylls, syll_idx)
  local merged = copy(sylls)
  if #merged >= 2 then
    local core = self:_strip_silent_tail((self:_trim_edge(merged[#merged])))
    if not (core ~= "" and self:_has_orth_vowel(core)) then
      local last = table.remove(merged)
      merged[#merged] = merged[#merged] .. last
    end
  end
  local out = {}
  for k, idx in ipairs(syll_idx) do
    if idx ~= nil and #merged < #sylls then idx = min(idx, #merged - 1) end
    local status
    if idx ~= nil and 0 <= idx and idx < #merged then
      local syllable, final = self:_trim_edge(merged[idx + 1])
      if final or idx == #merged - 1 then syllable = self:_strip_silent_tail(syllable) end
      if syllable ~= "" and self:_has_orth_vowel(syllable) then status = self:_c(at(syllable, -1), "orth_vowel") end
    end
    if status == nil then status = NONE end -- keeps the array free of holes
    out[k] = status
  end
  return out
end

function P:secondary_positions(n, stressed)
  local out = {}
  if not T(self.stress.alternating) or stressed == nil or stressed < 0 or n < 3 then return out end
  for k = stressed % 2, stressed - 2, 2 do out[k] = true end
  return out
end

function P:_map_tokens_to_syllables(tokens, sylls)
  if #sylls == 0 then
    local out = {}
    for k = 1, #tokens do out[k] = 0 end
    return out
  end
  local owner = {}
  for idx, syll in ipairs(sylls) do
    for _ = 1, slen(syll) do owner[#owner + 1] = idx - 1 end
  end
  local lower = self._lower
  local function fold(text)
    local out = {}
    for k, c in ipairs(chars(text)) do
      local l = lower[c] or c
      out[k] = #l == 3 and l or c
    end
    return concat(out)
  end
  local folded = fold(concat(sylls))
  local result = {}
  local cursor = 0
  for _, token in ipairs(tokens) do
    local pos = token.grapheme ~= "" and sfind_from(folded, fold(token.grapheme), cursor) or -1
    if pos < 0 then
      result[#result + 1] = result[#result] or 0
    else
      result[#result + 1] = pos < #owner and owner[pos + 1] or #sylls - 1
      cursor = pos + slen(token.grapheme)
    end
  end
  return result
end

function P:_known_only(word)
  local out = {}
  for _, c in ipairs(chars(word)) do
    if self:_c(c, "known") then out[#out + 1] = c end
  end
  return concat(out)
end

function P:syllables(word)
  local sylls = self._syll_cache[word]
  if sylls == nil then
    local written = self:_known_only(word)
    sylls = self:_bundled(written, self:hiatus_positions(written))
    self._syll_cache[word] = sylls
  end
  return copy(sylls)
end

local CONTEXTUAL = "contextual"

function P:_nucleus_mask(word, semivowels, vowels)
  local wc = chars(word)
  local fixed = {}
  for k, ch in ipairs(wc) do
    local role = semivowels[self:lower(ch)]
    if self:_comb(ch) then fixed[k] = false
    elseif role == nil and vowels then fixed[k] = vowels[self:lower(ch)] == true
    elseif role == nil then fixed[k] = self:_vowel_char(ch)
    elseif role == "contextual" then fixed[k] = CONTEXTUAL
    else fixed[k] = role == "nucleus" end
  end
  local mask = {}
  for i, status in ipairs(fixed) do
    if status == CONTEXTUAL then
      local before, after = false, false
      for k = i - 1, 1, -1 do
        if not self:_comb(wc[k]) then before = fixed[k]; break end
      end
      for k = i + 1, #wc do
        if not self:_comb(wc[k]) then after = fixed[k]; break end
      end
      status = not ((before == true) or (after == true))
    end
    mask[i] = status
  end
  return mask
end

local function by_len_desc(a, b) return #a > #b end

function P:_split_nuclei(run, diphthongs, hiatus, joins)
  hiatus = hiatus or {}
  joins = joins or {}
  if slen(run) < 2 then return {run} end
  local ordered = ssort(copy(diphthongs), by_len_desc)
  local lowered = self:lower(run)
  local nuclei = {}
  local i, n = 0, slen(run)
  while i < n do
    local matched = false
    if joins[i] then
      nuclei[#nuclei + 1] = sl(run, i, i + joins[i])
      i = i + joins[i]
      matched = true
    end
    for _, diph in ipairs(matched and {} or ordered) do
      if startswith(lowered, diph, i) then
        local cut = false
        local dl = slen(diph)
        for h in pairs(hiatus) do
          if i < h and h < i + dl then cut = true; break end
        end
        if not cut then
          nuclei[#nuclei + 1] = sl(run, i, i + dl)
          i = i + dl
          matched = true
          break
        end
      end
    end
    if not matched then
      nuclei[#nuclei + 1] = at(run, i)
      i = i + 1
    end
    while i < n and (self:_comb(at(run, i)) or at(run, i) == LENGTH) do
      if #nuclei > 0 then
        nuclei[#nuclei] = nuclei[#nuclei] .. at(run, i)
      else
        nuclei[#nuclei + 1] = at(run, i)
      end
      i = i + 1
    end
  end
  return nuclei
end

function P:_with_diphthongs(word, nucleus, diphthongs, onset_graphemes, hiatus, joins)
  onset_graphemes = onset_graphemes or {}
  hiatus = hiatus or {}
  joins = joins or {}
  local syllables = {}
  local onset = ""
  local i, n = 0, slen(word)
  while i < n do
    local glued = false
    if onset ~= "" and i + 1 < n and nucleus[i + 2] then
      local low = self:lower(at(word, i))
      for _, g in ipairs(onset_graphemes) do
        if at(g, -1) == low
            and self:lower(sl(onset, slen(onset) - slen(g) + 1)) == sl(g, 0, -1) then
          glued = true
          break
        end
      end
    end
    if glued then
      onset = onset .. at(word, i)
      i = i + 1
    elseif not nucleus[i + 1] then
      onset = onset .. at(word, i)
      i = i + 1
      while i < n and self:_comb(at(word, i)) do
        onset = onset .. at(word, i)
        i = i + 1
      end
    else
      local j = i
      while j < n and (nucleus[j + 1] or self:_comb(at(word, j)) or at(word, j) == LENGTH) do j = j + 1 end
      local run_hiatus = {}
      for h in pairs(hiatus) do
        if i < h and h < j then run_hiatus[h - i] = true end
      end
      local run_joins = {}
      for h, w in pairs(joins) do
        if i <= h and h + w <= j then run_joins[h - i] = w end
      end
      for k, piece in ipairs(self:_split_nuclei(sl(word, i, j), diphthongs, run_hiatus, run_joins)) do
        syllables[#syllables + 1] = (k == 1 and onset or "") .. piece
      end
      onset = ""
      i = j
    end
  end
  if onset ~= "" then
    if #syllables > 0 then
      syllables[#syllables] = syllables[#syllables] .. onset
    else
      syllables[#syllables + 1] = onset
    end
  end
  return syllables
end

local function any_true(mask, i, j) -- any(mask[i:j]), 0-based
  for k = i + 1, min(j, #mask) do if mask[k] then return true end end
  return false
end

function P:_vowel_groups(word, nucleus)
  local syllables = {}
  local current, current_start = "", 0
  local in_nucleus = false
  for i0, ch in ipairs(chars(word)) do
    local i = i0 - 1
    if self:_comb(ch) or ch == LENGTH then
      current = current .. ch
    else
      local is_vowel = nucleus[i + 1]
      if is_vowel and not in_nucleus and current ~= "" and any_true(nucleus, current_start, i) then
        syllables[#syllables + 1] = current
        current, current_start = ch, i
      elseif not is_vowel and in_nucleus then
        syllables[#syllables + 1] = current
        current, current_start = ch, i
      else
        current = current .. ch
      end
      in_nucleus = is_vowel
    end
  end
  if current ~= "" then
    if any_true(nucleus, current_start, #nucleus) or #syllables == 0 then
      syllables[#syllables + 1] = current
    else
      syllables[#syllables] = syllables[#syllables] .. current
    end
  end
  return syllables
end

function P:_bundled(word, hiatus)
  if word == "" then return {} end
  local nucleus = self:_nucleus_mask(word, self._semivowels, self._vowel_letters)
  local cuts, joins = {}, {}
  if self._cuts_on then cuts, joins = self:_fragment_cuts(word) end
  local diphthongs = self.syll.diphthongs or {}
  local sylls
  if T(diphthongs) then
    local both = {}
    for h in pairs(hiatus) do both[h] = true end
    for h in pairs(cuts) do both[h] = true end
    sylls = self:_with_diphthongs(word, nucleus, diphthongs, self.syll.onset_graphemes or {}, both, joins)
  else
    sylls = self:_vowel_groups(word, nucleus)
  end
  if T(self._onsets) then
    return self:_rebalance(sylls, nucleus,
      function(run) return self:_written_units(run) end,
      function(run) return self:_licit_written_onset(run) end, cuts)
  end
  if next(cuts) ~= nil then
    return self:_rebalance(sylls, nucleus, chars, function() return true end, cuts)
  end
  return sylls
end

-- 3.7.6: the offsets where the fragment tables start a syllable, and the
-- spans they join into one nucleus, as {start = length}.
function P:_fragment_cuts(word)
  local sy = self.syll
  local low = self:lower(word)
  local n = slen(low)
  local vowel = {}
  for k = 0, n - 1 do vowel[k] = self:_c(at(low, k), "orth_vowel") end
  local cuts, joins = {}, {}
  local multi = {}
  for _, u in ipairs(T(self._onsets) and self._onsets.units or {}) do
    if slen(u) > 1 then multi[#multi + 1] = u end
  end
  local inside = {}
  local k = 0
  while k < n do
    local width = 1
    for _, u in ipairs(multi) do
      if startswith(low, u, k) then width = slen(u); break end
    end
    for x = k + 1, k + width - 1 do inside[x] = true end
    k = k + width
  end
  for _, pair in ipairs(sy.cut_pairs or {}) do
    k = sfind_from(low, pair, 0)
    while k >= 0 do
      if not inside[k + 1] then cuts[k + 1] = true end
      k = sfind_from(low, pair, k + 1)
    end
  end
  local rule = sy.glide_hiatus
  if T(rule) then
    if inset(rule.diphthong_words, low) then
      k = 0
      while k < n do
        local j = k
        while j < n and vowel[j] do j = j + 1 end
        if j - k > 1 then joins[k] = j - k end
        k = j + 1
      end
    end
    for x = 1, n - 1 do
      local g = at(low, x)
      if inset(rule.glides, g) and vowel[x - 1] and g ~= at(low, x - 1)
          and not (x + 1 < n and vowel[x + 1]) then
        local rest = sl(low, x + 1)
        local hit = false
        for _, b in ipairs(rule.before) do
          if startswith(rest, b) then hit = true; break end
        end
        if not hit and inset(rule.codas, sl(rest, 0, 1)) then
          hit = not (slen(rest) > 1 and (vowel[x + 2] or at(rest, 1) == at(rest, 0)))
          for _, u in ipairs(multi) do
            if startswith(rest, u) then hit = false; break end
          end
        end
        if hit then cuts[x] = true end
      end
    end
  end
  for _, sc in ipairs(sy.stem_cuts or {}) do
    k = sfind_from(low, sc[1], 0)
    if k >= 0 then
      for _, o in ipairs(sc[2]) do cuts[k + o] = true end
    end
  end
  for _, r in ipairs(sy.prefix_cuts or {}) do
    if startswith(low, r.prefix) then
      local stem = sl(low, slen(r.prefix))
      if inset(r.onset, sl(stem, 0, 1)) then
        for _, t in ipairs(r.stems) do
          if startswith(stem, t) then cuts[slen(r.prefix)] = true; break end
        end
      end
      break
    end
  end
  local seams = sy.seams
  if T(seams) then
    local cps = to_cps(low)
    local done = false
    for _, r in ipairs(seams.suffixes) do
      local start = psearch(r.pattern, cps, 0, group_count(r.pattern))
      if start ~= nil then cuts[start + r.cut] = true; done = true; break end
    end
    if not done then
      for _, stem in ipairs(seams.stems) do
        k = sfind_from(low, stem, 0)
        local e = k + slen(stem)
        if k >= 0 and inset(seams.next, sl(low, e, e + 1)) and n > e + 1 then
          cuts[e] = true
          break
        end
      end
    end
  end
  local foreign = sy.foreign
  if T(foreign) then
    for _, f in ipairs(foreign.finals) do
      for _, tail in ipairs(f[2]) do
        if endswith(low, f[1] .. tail) then joins[n - slen(f[1] .. tail)] = slen(f[1]) end
      end
    end
    if T(foreign.nuclei) and psearch(foreign.pattern, to_cps(low), 0, group_count(foreign.pattern)) ~= nil then
      for _, nuc in ipairs(foreign.nuclei) do
        k = sfind_from(low, nuc, 0)
        while k >= 0 do
          local covered = false
          for h, w in pairs(joins) do
            if h <= k and k < h + w then covered = true; break end
          end
          if not covered then joins[k] = slen(nuc) end
          k = sfind_from(low, nuc, k + slen(nuc))
        end
      end
    end
  end
  return cuts, joins
end

function P:_units_by(run, units, norm)
  local out = {}
  local i, n = 0, slen(run)
  while i < n do
    local matched = false
    for _, g in ipairs(units) do
      local gl = slen(g)
      if gl <= n - i and norm(self, sl(run, i, i + gl)) == g then
        out[#out + 1] = sl(run, i, i + gl)
        i = i + gl
        matched = true
        break
      end
    end
    if not matched then
      out[#out + 1] = at(run, i)
      i = i + 1
    end
    while i < n and self:_comb(at(run, i)) do
      out[#out] = out[#out] .. at(run, i)
      i = i + 1
    end
  end
  return out
end

function P:_written_units(run) return self:_units_by(run, self._onsets.units, P.lower) end

function P:_letters_or_marks(run)
  for _, ch in ipairs(chars(run)) do
    if not (self:_c(ch, "alpha") or self:_comb(ch)) then return false end
  end
  return true
end

function P:_licit_written_onset(run)
  if run == "" then return true end
  if not self:_letters_or_marks(run) then return false end
  local units = self:_written_units(run)
  local cap = self._onsets.max
  if cap >= 0 and #units > cap then return false end
  if self._onset_velar[self:lower(units[1])] then return false end
  if #units == 1 then return true end
  local low = {}
  for k, u in ipairs(units) do low[k] = self:lower(u) end
  return self._onset_table[concat(low, "\1")] == true
end

function P:hiatus_positions(word)
  if self.stress == nil then return {} end
  local found = {}
  local lowered = self:lower(word)
  local ln = slen(lowered)
  local atonic = {}
  local rule = self.syll.closed_hiatus
  if T(rule) then
    for k = 1, ln - 1 do
      if inset(rule.pairs, sl(lowered, k - 1, k + 1)) then
        local rest = sl(lowered, k + 1)
        local hit = false
        for _, o in ipairs(rule.onsets) do
          if startswith(rest, o) then hit = true; break end
        end
        if not hit and inset(rule.codas, sl(rest, 0, 1))
            and not (slen(rest) > 1 and (self:_c(at(rest, 1), "orth_vowel")
                                         or at(rest, 1) == at(rest, 0))) then
          hit = true
          for _, g in ipairs(rule.multi_keys) do
            if startswith(rest, g) then hit = false; break end
          end
        end
        if not hit then
          for _, o in ipairs(rule.atonic_onsets or {}) do
            if startswith(rest, o) then hit = true; atonic[k] = true; break end
          end
        end
        if hit then found[#found + 1] = k end
      end
    end
  end
  rule = self.syll.final_diphthongs
  if T(rule) then
    for _, diphthong in ipairs(rule.diphthongs) do
      local finals = {""}
      for _, f in ipairs(rule.finals) do finals[#finals + 1] = f end
      for _, final in ipairs(finals) do
        local k = ln - slen(diphthong) - slen(final)
        if k >= 1 and endswith(lowered, diphthong .. final) and self:_c(at(lowered, k - 1), "orth_vowel") then
          found[#found + 1] = k
        end
      end
    end
  end
  if #found == 0 then return {} end
  local set = {}
  for _, k in ipairs(found) do set[k] = true end
  local sylls = self:_bundled(word, set)
  local stressed = self:detect_stress(word, sylls)
  local start = 0
  for k = 1, min(stressed, #sylls) do start = start + slen(sylls[k]) end
  local out = {}
  for _, k in ipairs(found) do if k == start or atonic[k] then out[k] = true end end
  return out
end

function P:detect_stress(word, sylls)
  local n = #sylls
  if n <= 1 then return 0 end
  local st = self.stress
  if T(st.marked) then
    local marked = setof(st.marked)
    for idx, syllable in ipairs(sylls) do
      for _, ch in ipairs(chars(syllable)) do
        if marked[ch] then return idx - 1 end
      end
    end
  end
  local lowered = self:lower(word)
  for _, ending in ipairs(st.final) do if endswith(lowered, ending) then return n - 1 end end
  for _, ending in ipairs(st.penult) do if endswith(lowered, ending) then return n - 2 end end
  for _, ending in ipairs(st.antepenult) do if endswith(lowered, ending) then return max(0, n - 3) end end
  local pos = st.default
  local index = pos >= 1 and min(pos - 1, n - 1) or max(0, n + pos)
  for _, prefix in ipairs(st.prefixes or {}) do
    if startswith(lowered, prefix) then
      local inside, e = 0, 0
      for _, syll in ipairs(sylls) do
        e = e + slen(syll)
        if e > slen(prefix) then break end
        inside = inside + 1
      end
      local last
      for _, ch in ipairs(chars(sylls[n])) do if self:_c(ch, "alpha") then last = ch end end
      local final_open = last ~= nil and self:_c(last, "orth_vowel")
      local final_schwa = inset(st.schwa_rimes, self:_rime(self:lower(sylls[n])))
      if index < inside and inside < n and not (inside == n - 1 and (final_open or final_schwa)) then
        return inside
      end
      break
    end
  end
  return index
end

function P:_rime(syllable)
  for i, ch in ipairs(chars(syllable)) do
    if self:_c(ch, "orth_vowel") then return sl(syllable, i - 1) end
  end
  return ""
end

function P:_vowel_segment(seg) return seg ~= "" and self:_c(at(seg, 0), "ipa_vowel") end

function P:dock_tone_marks(ipa)
  local ic = chars(ipa)
  local any = false
  for _, ch in ipairs(ic) do if self:_c(ch, "tone_mark") then any = true; break end end
  if not any then return ipa end
  local function nucleus(seg) return self:_c(at(seg, 0), "ipa_vowel") or not self:_c(at(seg, 0), "alpha") end
  local out = {}
  local i, n = 0, #ic
  while i < n do
    if not self:_c(ic[i + 1], "tone_mark") then
      out[#out + 1] = ic[i + 1]
      i = i + 1
    else
      local j = i
      while j < n and self:_c(ic[j + 1], "tone_mark") do j = j + 1 end
      local tone = sl(ipa, i, j)
      local t = j
      while t < n and not self:_c(ic[t + 1], "tone_mark") do t = t + 1 end
      local segs = self:segment(sl(ipa, j, t), self.word.tone_dock)
      local all = #segs > 0
      for _, sg in ipairs(segs) do if not nucleus(sg) then all = false; break end end
      if all and t < n then
        out[#out + 1] = tone
        i = j
      else
        local k = 0
        while k < #segs and nucleus(segs[k + 1]) do k = k + 1 end
        local c = k
        while c < #segs and not nucleus(segs[c + 1]) do c = c + 1 end
        if c < #segs and c > k then c = c - 1 end
        local coda = concat(segs, "", 1, c)
        out[#out + 1] = coda
        out[#out + 1] = tone
        i = j + slen(coda)
      end
    end
  end
  return concat(out)
end

function P:apply_iambic_length(ipa)
  if contains(ipa, LENGTH) then return ipa end
  local sylls = self:syllabify_by_weight(ipa, self.stress.iambic.max_onset)
  local n = #sylls
  if n < 3 then return ipa end
  local start = self:syllable_weight(sylls[1]) ~= 0 and 0 or 1
  for i = start, n - 2, 2 do
    if self:syllable_weight(sylls[i + 1]) == 0 then
      local segs = self:segment(sylls[i + 1], self._affricates)
      for k, seg in ipairs(segs) do
        if self:_vowel_segment(seg) then segs[k] = seg .. LENGTH; break end
      end
      sylls[i + 1] = concat(segs)
    end
  end
  return concat(sylls)
end

function P:syllabify_by_weight(ipa, max_onset)
  if ipa == "" then return {} end
  local segs = self:segment(ipa, self._affricates)
  local nuclei = {}
  local i = 0
  while i < #segs do
    if self:_vowel_segment(segs[i + 1]) then
      local start = i
      while i < #segs and self:_vowel_segment(segs[i + 1]) do i = i + 1 end
      nuclei[#nuclei + 1] = {start, i}
    else
      i = i + 1
    end
  end
  if #nuclei == 0 then return {ipa} end
  if max_onset == nil then max_onset = self.stress.weight.max_onset end
  local out = {}
  for n, nu in ipairs(nuclei) do
    local start, e = nu[1], nu[2]
    local onset = n == 1 and 0 or start - min(max_onset, start - nuclei[n - 1][2])
    local coda
    if n < #nuclei then
      local nxt = nuclei[n + 1][1]
      coda = nxt - min(max_onset, nxt - e)
    else
      coda = #segs
    end
    out[#out + 1] = concat(lsl(segs, onset, coda))
  end
  return out
end

function P:_holds_diphthong(seg)
  local letters = {}
  for _, c in ipairs(chars(seg)) do
    if not self:_comb(c) then letters[#letters + 1] = c end
  end
  local vowel = {}
  for k, c in ipairs(letters) do vowel[k] = self:_c(c, "ipa_vowel") or self:_c(c, "vowel_phone") end
  vowel[#letters + 1] = false
  for i = 0, #letters - 2 do
    local c = letters[i + 2]
    if vowel[i + 1] and (vowel[i + 2] or (self:_c(c, "offglide") and not vowel[i + 3])) then return true end
  end
  return false
end

-- 0 light, 1 heavy, 2 superheavy.
function P:syllable_weight(syllable)
  local segs = self:segment(syllable, self._affricates)
  local start
  for k, s in ipairs(segs) do
    if self:_vowel_segment(s) then start = k - 1; break end
  end
  if start == nil then return 0 end
  local e = start
  while e < #segs and self:_vowel_segment(segs[e + 1]) do e = e + 1 end
  local coda = #segs - e
  local long_vowel = e - start > 1
  for k = start + 1, e do
    if contains(segs[k], LENGTH) or self:_holds_diphthong(segs[k]) then long_vowel = true end
  end
  if (long_vowel and coda > 0) or coda >= 2 then return 2 end
  return (long_vowel or coda > 0) and 1 or 0
end

function P:stress_by_weight(sylls)
  local n = #sylls
  if n <= 1 then return -1 end
  if T(self.stress.weight.superheavy_final) and self:syllable_weight(sylls[n]) == 2 then return -1 end
  if self:syllable_weight(sylls[n - 1]) >= 1 then return -2 end
  local default = self.stress.default
  if default < 0 then return n >= -default and default or -n end
  return -n
end

-- ─── S9f: mark placement ───────────────────────────────────────────────────

function P:_licit_onset(run)
  if run == "" then return true end
  if not self:_letters_or_marks(run) then return false end
  local units = self:segment(run, self._mark_atoms)
  local onsets = self.stress.mark_onsets
  if onsets.max >= 0 and #units > onsets.max then return false end
  if startswith(units[1], onsets.velar) then return false end
  if #units == 1 then return true end
  return self._mark_table[concat(units, "\1")] == true
end

function P:_rebalance(syllables, nucleus, split, licit, cuts)
  cuts = cuts or {}
  if #syllables < 2 then return syllables end
  local out = {syllables[1]}
  local start = slen(syllables[1])
  for k = 2, #syllables do
    local syll = syllables[k]
    local j, n = 0, slen(syll)
    while j < n and (self:_comb(at(syll, j)) or not nucleus[start + j + 1]) do j = j + 1 end
    local cut
    for c in pairs(cuts) do
      if start <= c and c <= start + j and (cut == nil or c - start < cut) then cut = c - start end
    end
    start = start + n
    local onset = sl(syll, 0, j)
    if onset == "" or out[#out] == "" then
      out[#out + 1] = syll
    else
      local keep = 0
      if cut ~= nil then
        keep = slen(onset) - cut
      else
        local units = split(onset)
        for kk = #units, 1, -1 do
          local tail = concat(units, "", #units - kk + 1, #units)
          if licit(tail) then keep = slen(tail); break end
        end
      end
      local on = slen(onset)
      if keep >= on then
        out[#out + 1] = syll
      else
        out[#out] = out[#out] .. sl(onset, 0, on - keep)
        out[#out + 1] = sl(syll, on - keep)
      end
    end
  end
  return out
end

function P:syllabify_for_mark(ipa)
  local st = self.stress
  local nucleus = self:_nucleus_mask(ipa, {})
  local sylls
  if st.ipa_diphthongs == nil then
    if T(st.mark_diphthongs) then
      sylls = self:_with_diphthongs(ipa, nucleus, st.mark_diphthongs)
    else
      sylls = ipa ~= "" and self:_vowel_groups(ipa, nucleus) or {}
    end
  else
    sylls = self:_with_diphthongs(ipa, nucleus, st.ipa_diphthongs)
  end
  if st.mark_onsets ~= nil then
    sylls = self:_rebalance(sylls, nucleus,
      function(run) return self:segment(run, self._mark_atoms) end,
      function(run) return self:_licit_onset(run) end)
  end
  if T(st.coda_liquid) then sylls = self:_capture_coda_liquids(sylls, nucleus) end
  return sylls
end

function P:_capture_coda_liquids(syllables, nucleus)
  if #syllables < 2 then return syllables end
  local out = {syllables[1]}
  local start = slen(syllables[1])
  for k = 2, #syllables do
    local syll = syllables[k]
    local j, n = 0, slen(syll)
    while j < n and (self:_comb(at(syll, j)) or not nucleus[start + j + 1]) do j = j + 1 end
    start = start + n
    local cons = {}
    for _, c in ipairs(chars(sl(syll, 0, j))) do if not self:_comb(c) then cons[#cons + 1] = c end end
    if #cons >= 2 and self:_c(cons[1], "liquid") and not self:_c(cons[2], "glide") and out[#out] ~= "" then
      local kk = 1
      while kk < n and self:_comb(at(syll, kk)) do kk = kk + 1 end
      out[#out] = out[#out] .. sl(syll, 0, kk)
      out[#out + 1] = sl(syll, kk)
    else
      out[#out + 1] = syll
    end
  end
  return out
end

function P:_prefix_mark(syll, mark)
  local i, n = 0, slen(syll)
  while i < n and (self:_c(at(syll, i), "length") or self:_comb(at(syll, i))) do i = i + 1 end
  return sl(syll, 0, i) .. mark .. sl(syll, i)
end


function P:_merge_sites(syllables)
  local out = {}
  for i = 1, #syllables - 1 do
    local a, b = syllables[i], syllables[i + 1]
    if a ~= "" and b ~= "" and self:_c(at(a, -1), "basic_vowel") and self:_c(at(b, 0), "basic_vowel") then out[#out + 1] = i end
  end
  return out
end

function P:_contact_units(run) return self:_units_by(run, self.stress.contact_units, P.casefold) end

function P:_vowel_contacts(syllables)
  local diphthongs = {}
  for _, d in ipairs(self.stress.mark_diphthongs) do diphthongs[self:lower(d)] = true end
  local silent = setof(self.stress.silent_units)
  local contacts = {}
  for i = 1, #syllables - 1 do
    local before, after = syllables[i], syllables[i + 1]
    if before ~= "" and self:_c(at(before, -1), "basic_vowel") then
      local j, n = 0, slen(after)
      while j < n and not self:_c(at(after, j), "basic_vowel") do j = j + 1 end
      if j ~= n then
        local ok = true
        if j > 0 then
          for _, g in ipairs(self:_contact_units(self:casefold(sl(after, 0, j)))) do
            if not silent[g] then ok = false; break end
          end
        end
        if ok then
          if not diphthongs[self:lower(at(before, -1) .. at(after, j))] then
            contacts[i] = "hiatus"
          elseif j > 0 then
            contacts[i] = "merge"
          end
        end
      end
    end
  end
  return contacts
end

function P:_split_first_nucleus(syll)
  local i, n = 0, slen(syll)
  while i < n and not self:_vowel_char(at(syll, i)) do i = i + 1 end
  if i == n then return nil end
  i = i + 1
  while i < n and (self:_comb(at(syll, i)) or self:_c(at(syll, i), "length")) do
    if self:_c(at(syll, i), "non_syllabic") then return nil end
    i = i + 1
  end
  if i == n or not self:_vowel_char(at(syll, i)) then return nil end
  if i + 1 < n and self:_c(at(syll, i + 1), "non_syllabic") then return nil end
  return {sl(syll, 0, i), sl(syll, i)}
end

function P:_align(syllables, ipa_sylls)
  local contacts = self:_vowel_contacts(syllables)
  if next(contacts) == nil then return nil end
  local out = {}
  local slots = {0}
  local pending = ipa_sylls[1]
  local j = 0
  for k = 1, #syllables - 1 do
    local kind = contacts[k]
    local cut = kind and self:_split_first_nucleus(pending) or nil
    if kind == "merge" and cut ~= nil then
      slots[#slots + 1] = #out
    else
      if kind == "merge" or cut == nil then
        j = j + 1
        if j == #ipa_sylls then return nil end
        out[#out + 1] = pending
        pending = ipa_sylls[j + 1]
      else
        out[#out + 1] = cut[1]
        pending = cut[2]
      end
      slots[#slots + 1] = #out
    end
  end
  if j ~= #ipa_sylls - 1 then return nil end
  out[#out + 1] = pending
  return out, slots
end

function P:_any_marked(syllable)
  local marked = setof(self.stress.marked)
  for _, ch in ipairs(chars(syllable)) do if marked[ch] then return true end end
  return false
end

function P:_glide_anchored(syllables, ipa_sylls, stress_index)
  if syllables == nil or #ipa_sylls == 0 or not (0 <= stress_index and stress_index < #syllables) then
    return nil
  end
  if not T(self.stress.marked) or not self:_any_marked(syllables[stress_index + 1]) then return nil end
  local sites = self:_merge_sites(syllables)
  if #syllables - #sites ~= #ipa_sylls then return nil end
  local shifted = stress_index
  for _, site in ipairs(sites) do if site <= stress_index then shifted = shifted - 1 end end
  if 0 <= shifted and shifted < #ipa_sylls then return shifted end
  return nil
end

function P:_ends_in_vowel(ipa)
  for i = slen(ipa) - 1, 0, -1 do
    local ch = at(ipa, i)
    if not self:_comb(ch) then return self:_vowel_char(ch) end
  end
  return false
end

function P:_lost_after_stress(ipa, syllables, ipa_sylls, stress_index)
  if self:_ends_in_vowel(ipa) then return false end
  local merged = {}
  for _, site in ipairs(self:_merge_sites(syllables)) do
    local slot = site - #merged
    if slot >= #ipa_sylls or not (self:_vowel_char(at(ipa_sylls[slot + 1], 0))
                                  or self:_c(at(ipa_sylls[slot + 1], 0), "glide")) then
      merged[#merged + 1] = site
    end
  end
  if #syllables - #merged ~= #ipa_sylls then return true end
  for _, s in ipairs(merged) do if s > stress_index then return true end end
  return false
end

function P:_glide_to_diphthong(syllables, ipa_sylls, stress_index)
  local letters = self.stress.tonic_after_diphthong
  if not T(letters) or #ipa_sylls ~= #syllables then return ipa_sylls end
  local i = stress_index >= 0 and stress_index or #syllables + stress_index
  if not (1 <= i and i < #syllables) then return ipa_sylls end
  local stressed = self:lower(self:nfc(syllables[i + 1]))
  local before = self:lower(self:nfc(syllables[i]))
  if stressed == "" or not inset(letters, at(stressed, 0)) then return ipa_sylls end
  local hit = false
  for _, d in ipairs(self.stress.mark_diphthongs) do
    if slen(d) > 1 and endswith(before, self:lower(d)) then hit = true; break end
  end
  if not hit then return ipa_sylls end
  local head, prev = ipa_sylls[i + 1], ipa_sylls[i]
  if slen(head) < 2 or not self:_c(at(head, 0), "glide_head") or not self:_vowel_char(at(head, 1))
      or prev == "" or not self:_vowel_char(at(prev, -1)) then
    return ipa_sylls
  end
  local out = copy(ipa_sylls)
  out[i] = prev .. at(head, 0)
  out[i + 1] = sl(head, 1)
  return out
end

function P:apply_stress_mark(ipa, stress_index, syllables, ipa_syllables, secondary, mark)
  secondary = secondary or {}
  local smark = self.stress.secondary_mark
  if contains(ipa, self.stress.mark) or (mark ~= nil and contains(ipa, mark)) then return ipa end
  if mark == nil or mark == "" then mark = self.stress.mark end
  local ipa_sylls = (ipa_syllables and #ipa_syllables > 0) and copy(ipa_syllables) or self:syllabify_for_mark(ipa)
  if #ipa_sylls == 0 then return ipa end
  if syllables ~= nil then ipa_sylls = self:_glide_to_diphthong(syllables, ipa_sylls, stress_index) end
  local aligned, slots
  if syllables ~= nil and #ipa_sylls < #syllables
      and -#syllables <= stress_index and stress_index < #syllables then
    aligned, slots = self:_align(syllables, ipa_sylls)
  end
  if aligned ~= nil then
    local si = stress_index < 0 and stress_index + #slots or stress_index
    local main = slots[si + 1]
    local marked = {[main] = true}
    for _, sec in ipairs(secondary) do
      if 0 <= sec and sec < #slots and not marked[slots[sec + 1]] then
        marked[slots[sec + 1]] = true
        aligned[slots[sec + 1] + 1] = self:_prefix_mark(aligned[slots[sec + 1] + 1], smark)
      end
    end
    aligned[main + 1] = self:_prefix_mark(aligned[main + 1], mark)
    return concat(aligned)
  end
  local offset_from_end
  if stress_index < 0 then
    offset_from_end = -stress_index
  else
    local n_orth = syllables ~= nil and #syllables or #ipa_sylls
    local overflow = #ipa_sylls - n_orth
    if overflow > 0 then
      local stand_in = self.stress.stand_in
      local function epenthetic(syll, final)
        local vowels = {}
        for _, c in ipairs(chars(syll)) do if self:_vowel_char(c) then vowels[#vowels + 1] = c end end
        if not (#vowels == 1 and vowels[1] == stand_in) then return false end
        return not (final and endswith(syll, stand_in))
      end
      local merged = {ipa_sylls[1]}
      for i = 2, #ipa_sylls do
        local syll = ipa_sylls[i]
        if overflow > 0 and epenthetic(syll, i == #ipa_sylls) then
          merged[#merged] = merged[#merged] .. syll
          overflow = overflow - 1
        else
          merged[#merged + 1] = syll
        end
      end
      ipa_sylls = merged
    elseif overflow < 0 and stress_index <= #ipa_sylls - 1 and (
        self:_lost_after_stress(ipa, syllables, ipa_sylls, stress_index)
        or self:_glide_anchored(syllables, ipa_sylls, stress_index) ~= nil) then
      local lost = self:_lost_after_stress(ipa, syllables, ipa_sylls, stress_index)
      local target = lost and stress_index or self:_glide_anchored(syllables, ipa_sylls, stress_index)
      for _, sec in ipairs(secondary) do
        if 0 <= sec and sec < #ipa_sylls and sec ~= target then
          ipa_sylls[sec + 1] = self:_prefix_mark(ipa_sylls[sec + 1], smark)
        end
      end
      ipa_sylls[target + 1] = self:_prefix_mark(ipa_sylls[target + 1], mark)
      return concat(ipa_sylls)
    end
    offset_from_end = max(1, n_orth - stress_index)
  end
  local target = max(0, #ipa_sylls - offset_from_end)
  local marked = {[target] = true}
  local n = syllables ~= nil and #syllables or #ipa_sylls
  for _, sec in ipairs(secondary) do
    local slot = sec < 0 and max(0, #ipa_sylls + sec) or max(0, #ipa_sylls - max(1, n - sec))
    if not marked[slot] then
      marked[slot] = true
      ipa_sylls[slot + 1] = self:_prefix_mark(ipa_sylls[slot + 1], smark)
    end
  end
  ipa_sylls[target + 1] = self:_prefix_mark(ipa_sylls[target + 1], mark)
  return concat(ipa_sylls)
end

-- Pairs (token index, segment) of a path's graphemes on the word's tokens.
function P:_token_index(tokens, graphemes, segments)
  local out = {}
  local t = 0
  for k = 1, min(#graphemes, #segments) do
    while t < #tokens and tokens[t + 1].grapheme ~= graphemes[k] do t = t + 1 end
    if t == #tokens then return out end
    out[#out + 1] = {t, segments[k]}
    t = t + 1
  end
  return out
end

function P:_vowel_offsets(ipa)
  local out = {}
  for i, c in ipairs(chars(ipa)) do
    if self:_c(c, "ipa_vowel") then out[#out + 1] = i - 1 end
  end
  return out
end

function P:_fold_inserted_nuclei(word, ipa, path)
  if path == nil or #path[3] == 0 or concat(path[1]) ~= ipa then return nil end
  local tokens = self:grapheme_tokens(word)
  local inserted = {}
  local any = false
  local offset = 0
  local pairs_ = self:_token_index(tokens, path[3], path[1])
  if #pairs_ ~= #path[3] then return nil end
  for _, pr in ipairs(pairs_) do
    local t, segment = pr[1], pr[2]
    if not self:_e(tokens[t + 1].entry, "readings_hold_vowel") then
      for _, i in ipairs(self:_vowel_offsets(segment)) do inserted[offset + i] = true; any = true end
    end
    offset = offset + slen(segment)
  end
  if not any then return nil end
  local syllables = self:syllabify_for_mark(ipa)
  local folded = {}
  offset = 0
  for _, syllable in ipairs(syllables) do
    local nuclei = self:_vowel_offsets(syllable)
    local all = #nuclei > 0
    for _, i in ipairs(nuclei) do if not inserted[offset + i] then all = false; break end end
    if #folded > 0 and all then
      folded[#folded] = folded[#folded] .. syllable
    else
      folded[#folded + 1] = syllable
    end
    offset = offset + slen(syllable)
  end
  if #folded < #syllables then return folded end
  return nil
end

function P:_cut_written_syllables(word, ipa, path, syllables, division)
  if path == nil or #path[3] == 0 or concat(path[1]) ~= ipa then return division end
  local sylls = (division and #division > 0) and division or self:syllabify_for_mark(ipa)
  if #sylls >= #syllables or concat(syllables) ~= word then return division end
  local tokens = self:grapheme_tokens(word)
  local token_syllable = self:_map_tokens_to_syllables(tokens, syllables)
  local owner, source = {}, {}
  local pairs_ = self:_token_index(tokens, path[3], path[1])
  if #pairs_ ~= #path[3] then return division end
  for _, pr in ipairs(pairs_) do
    local t, segment = pr[1], pr[2]
    for _ = 1, slen(segment) do
      owner[#owner + 1] = token_syllable[t + 1]
      source[#source + 1] = tokens[t + 1].position
    end
  end
  local ln = slen(ipa)
  if #owner ~= ln then return division end
  local starts = {}
  local acc = 0
  for k = 1, #syllables do starts[k] = acc; acc = acc + slen(syllables[k]) end
  local diphthongs = {}
  for _, d in ipairs(self.stress.mark_diphthongs) do diphthongs[self:lower(d)] = true end
  local cuts = {}
  local last
  local ic = chars(ipa)
  for o0, ch in ipairs(ic) do
    local o = o0 - 1
    if not self:_c(ch, "ipa_vowel") then
      if not (self:_comb(ch) or self:_c(ch, "length")) then last = nil end
    else
      local following = ic[o0 + 1]
      if last ~= nil and owner[o + 1] == owner[last + 1] + 1
          and not (following and self:_c(following, "non_syllabic")) then
        local before, after = syllables[owner[last + 1] + 1], syllables[owner[o + 1] + 1]
        local first = ""
        for _, c in ipairs(chars(after)) do
          if self:_c(c, "orth_vowel") then first = c; break end
        end
        local lead = sl(after, 0, source[o + 1] - starts[owner[o + 1] + 1])
        local alpha = false
        for _, c in ipairs(chars(lead)) do if self:_c(c, "alpha") then alpha = true; break end end
        if alpha and not diphthongs[self:lower(sl(before, -1) .. first)] then cuts[o] = true end
      end
      last = o
    end
  end
  local read = {}
  for _, token in ipairs(tokens) do
    for i = token.position, token.position + token.length - 1 do read[i] = true end
  end
  local drops = {}
  for k, syllable in ipairs(syllables) do
    local segments = {}
    for o, w in ipairs(owner) do if w == k - 1 then segments[#segments + 1] = o - 1 end end
    local dropped = {}
    for i0, c in ipairs(chars(syllable)) do
      local i = starts[k] + i0 - 1
      if self:_c(c, "orth_vowel") and not read[i] then dropped[#dropped + 1] = i end
    end
    if #segments > 0 and #dropped > 0 then
      local vowel = false
      for _, o in ipairs(segments) do if self:_c(ic[o + 1], "ipa_vowel") then vowel = true; break end end
      if not vowel then
        local pick = segments[#segments] + 1
        for _, o in ipairs(segments) do
          if source[o + 1] > dropped[1] then pick = o; break end
        end
        drops[#drops + 1] = pick
      end
    end
  end
  if #drops > 0 then
    local stand_in = self.stress.stand_in
    local bounds_a = {0}
    for _, d in ipairs(drops) do bounds_a[#bounds_a + 1] = d end
    local pieces = {}
    for k = 1, #bounds_a do
      local a = bounds_a[k]
      local b = drops[k] or ln
      pieces[k] = sl(ipa, a, b)
    end
    local probe = concat(pieces, stand_in)
    local stand_ins = {}
    for i, d in ipairs(drops) do stand_ins[i] = d + i - 1 end
    local ends = {0}
    local e = 0
    for _, s in ipairs(self:syllabify_for_mark(probe)) do e = e + slen(s); ends[#ends + 1] = e end
    for _, p in ipairs(stand_ins) do
      local start, stop
      for _, x in ipairs(ends) do
        if x <= p and (start == nil or x > start) then start = x end
        if x > p and (stop == nil or x < stop) then stop = x end
      end
      if stop == nil then error("min() arg is an empty sequence") end
      local ds, de = 0, 0
      for _, q in ipairs(stand_ins) do
        if q < start then ds = ds + 1 end
        if q < stop then de = de + 1 end
      end
      cuts[start - ds] = true
      cuts[stop - de] = true
    end
  end
  local bounds = {}
  acc = 0
  for k = 1, #sylls - 1 do acc = acc + slen(sylls[k]); bounds[acc] = true end
  for b in pairs(cuts) do bounds[b] = true end
  local edges = {}
  for b in pairs(bounds) do if 0 < b and b < ln then edges[#edges + 1] = b end end
  sort(edges)
  table.insert(edges, 1, 0)
  edges[#edges + 1] = ln
  local cut = {}
  for k = 1, #edges - 1 do cut[k] = sl(ipa, edges[k], edges[k + 1]) end
  if #cut > #sylls then return cut end
  return division
end

-- ─── S9: word finalisation ─────────────────────────────────────────────────

function P:_collapse_geminates(ipa)
  local out = {}
  for _, ch in ipairs(chars(ipa)) do
    if not (#out > 0 and ch == out[#out] and not self:_c(ch, "vowel_ipa_set")
            and not self:_c(ch, "length") and not self:_c(ch, "whitespace")) then
      out[#out + 1] = ch
    end
  end
  return concat(out)
end

function P:_finalize(word, ipa, path, collapse)
  if T(self._tone) and path ~= nil and #path[3] > 0 and ipa == concat(path[1]) then
    ipa = self:_computed_tones(path[3], path[1])
  end
  if collapse and T(self.word.collapse_geminates) and ipa ~= "" then
    ipa = self:_collapse_geminates(ipa)
  end
  local virama_final = self.word.virama_final
  if virama_final ~= nil and word ~= "" and ipa ~= "" and self:_c(at(word, -1), "virama")
      and not self:_c(at(ipa, -1), "ipa_vowel") then
    ipa = ipa .. virama_final
  end
  if self.word.tone_dock ~= nil and ipa ~= "" then ipa = self:dock_tone_marks(ipa) end
  if self.stress ~= nil and T(self.stress.iambic) and ipa ~= "" and not self:_is_cliticless(word) then
    ipa = self:apply_iambic_length(ipa)
  end
  if self.stress ~= nil and T(self.stress.apply) and ipa ~= "" and not self:_is_cliticless(word) then
    if T(self.stress.weight) then
      local ipa_sylls = self:syllabify_by_weight(ipa)
      return self:apply_stress_mark(ipa, self:stress_by_weight(ipa_sylls), nil, ipa_sylls)
    end
    local ipa_count = T(self.stress.ipa_count)
    local sylls = ipa_count and self:syllabify_for_mark(ipa) or self:syllables(word)
    local idx = self:detect_stress(word, sylls)
    local folded = nil
    if not ipa_count then folded = self:_fold_inserted_nuclei(word, ipa, path) end
    local division = self:_cut_written_syllables(word, ipa, path, sylls, folded)
    local sec = {}
    for k in pairs(self:secondary_positions(#sylls, idx)) do sec[#sec + 1] = k end
    sort(sec)
    local accent2 = self.stress.accent2
    local mark
    if T(accent2) and #sylls >= 2 and idx == #sylls - 2 and word ~= ""
        and inset(accent2.finals, self:lower(at(word, -1))) then
      mark = accent2.mark
    end
    ipa = self:apply_stress_mark(ipa, idx, sylls, division, sec, mark)
  end
  return ipa
end

-- ─── S9a: computed tone ────────────────────────────────────────────────────

local function enc(ascii)
  local out = {}
  for k = 1, #ascii do out[k] = C(sbyte(ascii, k)) end
  return concat(out)
end
local DEAD_LONG, DEAD_SHORT, LIVE, ANY = enc("dead_long"), enc("dead_short"), enc("live"), enc("any")

-- 3.9: append each syllable's tone, from its initial's class, its rime's
-- shape and its tone mark.
function P:_computed_tones(graphemes, segments)
  local sylls = self:_tone_syllables(segments)
  if #sylls == 0 then return concat(segments) end
  local out = {}
  for _, syl in ipairs(sylls) do
    local parts, gs = {}, {}
    for _, i in ipairs(syl) do
      parts[#parts + 1] = segments[i + 1]
      gs[#gs + 1] = graphemes[i + 1]
    end
    local ipa = concat(parts)
    out[#out + 1] = ipa .. self:_syllable_tone(gs, ipa)
  end
  return concat(out)
end

-- Slot indices grouped by maximal onset over slots.
function P:_tone_syllables(segments)
  local nuclei = {}
  for i, seg in ipairs(segments) do
    for _, ch in ipairs(chars(seg)) do
      if self:_c(ch, "ipa_vowel") then nuclei[#nuclei + 1] = i - 1; break end
    end
  end
  if #nuclei == 0 then return {} end
  local sylls = {}
  for n = 1, #nuclei do sylls[n] = {} end
  local function add(t, i) t[#t + 1] = i end
  local prev = 0
  for n, idx in ipairs(nuclei) do
    if n == 1 then
      for i = prev, idx - 1 do add(sylls[1], i) end
      add(sylls[1], idx)
    elseif segments[idx + 1] ~= "" and not self:_c(at(segments[idx + 1], 0), "ipa_vowel") then
      for i = prev, idx - 1 do add(sylls[n - 1], i) end
      sylls[n] = {idx}
    else
      local cut = idx
      for i = prev, idx - 1 do if segments[i + 1] ~= "" then cut = i end end
      for i = prev, idx - 1 do if i < cut then add(sylls[n - 1], i) end end
      for i = prev, idx - 1 do if i >= cut then add(sylls[n], i) end end
      add(sylls[n], idx)
    end
    prev = idx + 1
  end
  for i = prev, #segments - 1 do add(sylls[#sylls], i) end
  return sylls
end

function P:_syllable_tone(graphemes, ipa)
  local cls
  for _, g in ipairs(graphemes) do
    for _, ch in ipairs(chars(g)) do
      if self._tone_classes[ch] ~= nil then cls = self._tone_classes[ch]; break end
    end
    if cls ~= nil then break end
  end
  if cls == nil or not self._tone_class_names[cls] then return "" end
  local mark = self._tone.no_mark
  for _, g in ipairs(graphemes) do
    for _, ch in ipairs(chars(g)) do
      if self._tone_marks[ch] ~= nil then mark = self._tone_marks[ch] end
    end
  end
  local segs = self:segment(ipa, self._tone.atoms)
  local i = 0
  while i < #segs and not self:_c(at(segs[i + 1], 0), "ipa_vowel") do i = i + 1 end
  if i == #segs then return "" end
  local j = i
  while j < #segs and self:_c(at(segs[j + 1], 0), "ipa_vowel") do j = j + 1 end
  local long_vowel = contains(concat(segs, "", i + 1, j), LENGTH)
  local coda = concat(segs, "", j + 1, #segs)
  local dead
  if coda ~= "" then
    dead = false
    for _, c in ipairs(self._tone.dead_codas) do
      if startswith(coda, c) then dead = true; break end
    end
  else
    dead = not long_vowel
  end
  local shape = dead and (long_vowel and DEAD_LONG or DEAD_SHORT) or LIVE
  local tone = self._tone_table[cls .. "|" .. shape .. "|" .. mark]
  if tone == nil then tone = self._tone_table[cls .. "|" .. ANY .. "|" .. mark] end
  return tone or ""
end

-- ─── S8b: grammatical endings ──────────────────────────────────────────────

function P:_match_ending(graphemes)
  if #graphemes < 2 then return nil end
  local suffix = self._ending_suffix[self:lower(graphemes[#graphemes])] and 1 or 0
  local e = #graphemes - suffix
  local stem = {}
  for k = 1, e do stem[k] = self:lower(graphemes[k]) end
  local surface = concat(stem)
  local starts = {}
  local offset = 0
  for k, token in ipairs(stem) do starts[k] = offset; offset = offset + slen(token) end
  for cut = 1, slen(surface) - 1 do
    local entry = self._endings[sl(surface, cut)]
    if entry ~= nil then
      local first
      for k, s in ipairs(starts) do if s <= cut then first = k - 1 end end
      if first >= 1 then return entry, e - first + suffix end
    end
  end
  return nil
end

local function path_ipa(path) return concat(path[1]) end

function P:_apply_ending(word, paths)
  if #paths == 0 or not T(self.ir.endings) then return paths end
  local tokens = {}
  for _, t in ipairs(self:tokenize(word)) do
    if t.kind == WORD then tokens[#tokens + 1] = t.grapheme end
  end
  local marks = self.word.silent_stress_marks
  local kept, kept_g = {}, {}
  for i, g in ipairs(tokens) do
    if not (slen(g) == 1 and inset(marks, g)) then kept[#kept + 1] = i - 1; kept_g[#kept_g + 1] = g end
  end
  local entry, n = self:_match_ending(kept_g)
  if entry == nil then return paths end
  if T(marks) and n ~= 0 then n = #tokens - kept[#kept - n + 1] end
  local function rewrite(path, ipa, extra)
    local segs, cost, graphemes = path[1], path[2], path[3]
    if #segs <= n then return path end
    ipa = self:_ending_vowels_follow_stress(path, n, ipa)
    local new_segs = lsl(segs, 0, -n)
    new_segs[#new_segs + 1] = ipa
    local new_g = {}
    if #graphemes > 0 then
      new_g = lsl(graphemes, 0, -n)
      new_g[#new_g + 1] = concat(lsl(graphemes, -n))
    end
    return {new_segs, cost + extra, new_g}
  end
  local out, seen = {}, {}
  for _, path in ipairs(paths) do
    local new = entry.ipa == nil and path or rewrite(path, entry.ipa, 0)
    local key = path_ipa(new)
    if not seen[key] then seen[key] = true; out[#out + 1] = new end
  end
  if T(entry.alts) and #out > 0 then
    for k, alt in ipairs(entry.alts) do
      local cost = entry.costs[k + 1]
      if cost == nil then break end
      local new = rewrite(paths[1], alt, cost)
      local key = path_ipa(new)
      if not seen[key] then seen[key] = true; out[#out + 1] = new end
    end
    ssort(out, by_cost)
  end
  return out
end

function P:_vowel_runs(ipa)
  local runs = {}
  for i0, c in ipairs(chars(ipa)) do
    local i = i0 - 1
    local last = runs[#runs]
    if self:_c(c, "ipa_vowel") then
      if last and last[2] == i then last[2] = i + 1 else runs[#runs + 1] = {i, i + 1} end
    elseif last and last[2] == i and self:_c(c, "combining") then
      last[2] = i + 1
    end
  end
  return runs
end

function P:_ending_vowels_follow_stress(path, tail, ipa)
  local segs, graphemes = path[1], path[3]
  if #graphemes == 0 then return ipa end
  local letters = {}
  local gs, ss = lsl(graphemes, -tail), lsl(segs, -tail)
  for k = 1, min(#gs, #ss) do
    local runs = self:_vowel_runs(ss[k])
    if #runs > 1 then return ipa end
    if #runs == 1 then letters[#letters + 1] = {self:lower(gs[k]), sl(ss[k], runs[1][1], runs[1][2])} end
  end
  local declared = self:_vowel_runs(ipa)
  if #declared ~= #letters then return ipa end
  local out = {}
  local last = 0
  for k, run in ipairs(declared) do
    local start, e = run[1], run[2]
    local grapheme, actual = letters[k][1], letters[k][2]
    local written = sl(ipa, start, e)
    if written ~= actual then
      local v = self._ending_vowels[grapheme]
      local reduced, readings = v and v[1] or {}, v and v[2] or {}
      if reduced[written] then
        if not readings[actual] then
          local sources = self._ending_sources[actual] or {}
          local hits = {}
          for _, s in ipairs(sources) do
            if readings[s] and not hits[s] then hits[s] = true; hits[#hits + 1] = s end
          end
          actual = #hits == 1 and hits[1] or nil
        end
        if actual ~= nil and actual ~= written then
          out[#out + 1] = sl(ipa, last, start)
          out[#out + 1] = actual
          last = e
        end
      end
    end
  end
  out[#out + 1] = sl(ipa, last)
  return concat(out)
end

function P:noncohering_split(word)
  local nc = T(self.stress) and self.stress.noncohering or nil
  if not T(nc) then return nil end
  local key = self:nfc(self:casefold(word))
  if setof(nc.exceptions)[key] then return nil end
  for _, suffix in ipairs(nc.suffixes) do
    local n = slen(suffix)
    if slen(key) > n and endswith(key, suffix) and self:_c(at(key, -n - 1), "orth_vowel") then
      local cut = slen(word) - n
      return sl(word, 0, cut), sl(word, cut)
    end
  end
  return nil
end

function P:transcribe_word(word, width)
  local override = self:_override_for(word)
  if override ~= nil then return self:_finalize(word, override, nil, false) end
  local base, suffix = self:noncohering_split(word)
  if base ~= nil then
    return sreplace(self:transcribe_word(base, width), self.stress.mark, self.stress.secondary_mark)
      .. self:transcribe_word(suffix, width)
  end
  local paths = self:_apply_ending(word, self:_word_paths(word, width))
  local best = paths[1]
  return self:_finalize(word, best == nil and word or concat(best[1]), best, true)
end

-- ─── S10 to S14: the sentence ──────────────────────────────────────────────

function P:_mark_compounds(words, ipa_words)
  local mark, secondary = self.stress.mark, self.stress.secondary_mark
  local out = copy(ipa_words)
  local start = 0
  for e = 1, #words do
    if not (e < #words and words[e + 1].hyphen_joined) then
      local marked = {}
      for i = start, e - 1 do
        if contains(out[i + 1], mark) then marked[#marked + 1] = i end
      end
      for k = 1, #marked - 1 do out[marked[k] + 1] = sreplace(out[marked[k] + 1], mark, secondary) end
      start = e
    end
  end
  return out
end

function P:_sandhi(words, surfaces, pausal, joined)
  local result = copy(words)
  for i = 1, #result do
    if pausal[i] then
      local left = to_cps(result[i])
      for _, rule in ipairs(self.ir.sandhi) do
        if T(rule.pause) and self:_side_holds(rule, "left", left, surfaces[i], joined[i]) then
          result[i] = self:_sub(rule.left, rule.left_out, left)
          break
        end
      end
    else
      local left, right = to_cps(result[i]), to_cps(result[i + 1])
      local left_done, right_done = false, false
      for _, rule in ipairs(self.ir.sandhi) do
        if left_done and right_done then break end
        if not T(rule.pause) and self:_side_holds(rule, "left", left, surfaces[i], joined[i])
            and self:_side_holds(rule, "right", right, surfaces[i + 1], joined[i + 1]) then
          if rule.left_out ~= nil and not left_done then
            result[i] = self:_sub(rule.left, rule.left_out, left)
            left_done = true
          end
          if rule.right_out ~= nil and not right_done then
            result[i + 1] = self:_sub(rule.right, rule.right_out, right)
            right_done = true
          end
        end
      end
    end
  end
  return result
end

-- The side pattern finds a match in the IPA and, when the rule has them, the
-- spelling pattern finds a match in the surface of the word and the joined
-- spelling pattern in its joined spelling.
function P:_side_holds(rule, side, ipa, surface, joined)
  local node = rule[side]
  if psearch(node, ipa, 0, group_count(node)) == nil then return false end
  local spelling = rule[side .. "_spelling"]
  if spelling ~= nil and psearch(spelling, to_cps(surface), 0, group_count(spelling)) == nil then
    return false
  end
  local pair = rule[side .. "_joined_spelling"]
  return pair == nil or psearch(pair, to_cps(joined), 0, group_count(pair)) ~= nil
end

function P:_sub(node, template, s)
  local strings, tpl = {}, {}
  for k, part in ipairs(template) do
    if part[1] == "lit" then
      tpl[k] = {"lit", #strings}
      strings[#strings + 1] = to_cps(part[2])
    else
      tpl[k] = part
    end
  end
  return from_cps(psub(node, tpl, s, strings))
end

function P:transcribe(text, width)
  width = width or 1
  local prepared = self:prepare(text)
  local words = {}
  self:_group_words(prepared, words)
  if #words == 0 then return "" end
  words[#words].pausal = true
  local ipa_words = {}
  for k, w in ipairs(words) do ipa_words[k] = self:transcribe_word(w.surface, width) end
  if self.stress ~= nil and T(self.stress.compound_last) then
    ipa_words = self:_mark_compounds(words, ipa_words)
  end
  if T(self.ir.sandhi) then
    local surfaces, pausal, joined = {}, {}, {}
    for k, w in ipairs(words) do
      surfaces[k], pausal[k] = w.surface, w.pausal
      -- A word joined to the one before by a hyphen: that word, "-" and its own
      -- surface (docs/ir/o2i-ir-v1.md, 3.10.1).
      if k > 1 and w.hyphen_joined then
        joined[k] = words[k - 1].surface .. HYPHEN .. w.surface
      else
        joined[k] = w.surface
      end
    end
    ipa_words = self:_sandhi(ipa_words, surfaces, pausal, joined)
  end
  local kept = {}
  for _, w in ipairs(ipa_words) do if w ~= "" then kept[#kept + 1] = w end end
  local ipa = concat(kept, SPACE)
  if T(self.ir.dialect) then
    local surfaces = {}
    for k, w in ipairs(words) do surfaces[k] = w.surface end
    ipa = self:run_program(self.ir.dialect, ipa, concat(surfaces, SPACE))
  end
  if ipa ~= "" then ipa = self:nfc(ipa) end
  return ipa
end

function P:transcribe_cps(cps, width)
  return to_cps(self:transcribe(from_cps(cps), width))
end

-- ═══ the dialect program (dialect.py, primitives 13 to 16) ═════════════════

local function gate(g, spelling)
  local op = g[1]
  if op == "true" then return true end
  if op == "spell_search" then return psearch(g[2], spelling, 0, group_count(g[2])) ~= nil end
  if op == "spell_empty" then return #spelling == 0 end
  if op == "and" then
    for k = 2, #g do if not gate(g[k], spelling) then return false end end
    return true
  end
  if op == "or" then
    for k = 2, #g do if gate(g[k], spelling) then return true end end
    return false
  end
  if op == "not" then return not gate(g[2], spelling) end
  error("unknown gate node " .. tostring(op))
end

local function dpred(p, x, i, n, spelling)
  local op = p[1]
  local xl = slen(x)
  if op == "back_reach" then
    for j = i - 1, 0, -1 do
      local c = at(x, j)
      if inset(p[2], c) then return true end
      if inset(p[3], c) then return false end
    end
    return false
  end
  if op == "at_in" then
    local j = i + p[2]
    return 0 <= j and j < xl and inset(p[3], at(x, j))
  end
  if op == "at_end_or_in" then return i + n >= xl or inset(p[2], at(x, i + n)) end
  if op == "ahead_match" then
    if i + p[2] <= xl then return match_at(p[3], to_cps(x), i + p[2]) end
    return false
  end
  if op == "covered_by" then
    for _, s in ipairs(p[2]) do
      for j = max(0, i - slen(s) + 1), i do
        if startswith(x, s, j) then return true end
      end
    end
    return false
  end
  if op == "later_has" then
    for j = i, xl - 1 do if inset(p[2], at(x, j)) then return true end end
    return false
  end
  if op == "spell" then return gate(p[2], spelling) end
  if op == "true" then return true end
  if op == "and" then
    for k = 2, #p do if not dpred(p[k], x, i, n, spelling) then return false end end
    return true
  end
  if op == "or" then
    for k = 2, #p do if dpred(p[k], x, i, n, spelling) then return true end end
    return false
  end
  if op == "not" then return not dpred(p[2], x, i, n, spelling) end
  error("unknown dialect predicate node " .. tostring(op))
end

local function contextual(x, find, rep, when, spelling)
  local out = {}
  local i, n, xl = 0, slen(find), slen(x)
  while i < xl do
    if sl(x, i, i + n) == find and dpred(when, x, i, n, spelling) then
      out[#out + 1] = rep
      i = i + n
    else
      out[#out + 1] = at(x, i)
      i = i + 1
    end
  end
  return concat(out)
end

local function chain(x, on, off, when_on, mapping)
  local state = false
  local out = {}
  for _, c in ipairs(chars(x)) do
    if on[c] then
      state = true
      out[#out + 1] = c
    else
      if when_on and not state then out[#out + 1] = c else out[#out + 1] = mapping[c] or c end
      if off[c] and state then state = false end
    end
  end
  return concat(out)
end

function P:_split_ws(text)
  local words, current = {}, {}
  for _, c in ipairs(chars(text)) do
    if self:_c(c, "whitespace") then
      if #current > 0 then words[#words + 1] = concat(current); current = {} end
    else
      current[#current + 1] = c
    end
  end
  if #current > 0 then words[#words + 1] = concat(current) end
  return words
end

function P:_lexical(x, spelling, rules)
  local xw, sw = self:_split_ws(x), self:_split_ws(spelling)
  if #xw ~= #sw then return x end
  for w = 1, #xw do
    local original = xw[w]
    local key = self:lower(sw[w])
    for _, r in ipairs(rules) do
      if key == r[1] then xw[w] = sreplace(original, r[2], r[3]) end
    end
  end
  return concat(xw, SPACE)
end

function P:run_program(steps, ipa, spelling)
  local cps = to_cps(spelling)
  for _, step in ipairs(steps) do
    if gate(step.gate, cps) then
      local kind = step.kind
      if kind == "replace" then
        ipa = sreplace(ipa, step.find, step.rep)
      elseif kind == "sub" then
        ipa = self:_sub(step.pattern, step.template, to_cps(ipa))
      elseif kind == "contextual" then
        ipa = contextual(ipa, step.find, step.rep, step.when, cps)
      elseif kind == "chain" then
        local mapping = {}
        for _, m in ipairs(step.map) do mapping[m[1]] = m[2] end
        ipa = chain(ipa, setof(step.on), setof(step.off), T(step.when_on), mapping)
      elseif kind == "lexical" then
        ipa = self:_lexical(ipa, spelling, step.rules)
      else
        error("unknown dialect step " .. tostring(kind))
      end
    end
  end
  return ipa
end

-- ═══ entry points ══════════════════════════════════════════════════════════

-- loom: O2I_LANGUAGES = {codes}, O2I_IRS = {code = IR JSON text},
-- optional O2I_REVISION = {code = spec_revision}.
if rawget(_G, "O2I_LANGUAGES") then
  local engines = {}
  local function engine(index)
    local code = O2I_LANGUAGES[(index or 0) + 1]
    local it = engines[code]
    if not it then
      it = M.new(M.json_decode(O2I_IRS[code]))
      engines[code] = it
    end
    return it, code
  end
  function _G.infer(args)
    return engine(args.lang):transcribe_cps(args.text, args.width or 1)
  end
  -- The spec_revision the exporter recorded, as codepoints; never computed here.
  function _G.info(args)
    local code = O2I_LANGUAGES[(args.lang or 0) + 1]
    local rev = rawget(_G, "O2I_REVISION")
    return rev and rev[code] and {sbyte(rev[code], 1, -1)} or {}
  end
end

-- CLI: luajit interpreter.lua IR.json [width]. Each stdin line holds the
-- decimal codepoints of one text; each stdout line holds those of its IPA,
-- or "E " and an error message. A wall-clock line goes to stderr.
local function main(path, width)
  local f = assert(io.open(path, "rb"))
  local text = f:read("*a")
  f:close()
  local ok, it = pcall(M.new, M.json_decode(text))
  if not ok then
    io.stdout:write("E ", tostring(it):gsub("\n", " "), "\n")
    return
  end
  width = tonumber(width) or 1
  local out = {}
  local n = 0
  local t0 = os.clock()
  for line in io.stdin:lines() do
    local cps = {}
    for d in line:gmatch("%d+") do cps[#cps + 1] = tonumber(d) end
    local good, res = pcall(it.transcribe_cps, it, cps, width)
    if good then
      out[#out + 1] = concat(res, " ")
    else
      out[#out + 1] = "E " .. tostring(res):gsub("\n", " ")
    end
    n = n + 1
  end
  local dt = os.clock() - t0
  io.stdout:write(concat(out, "\n"), n > 0 and "\n" or "")
  io.stderr:write(("lua: %d texts in %.3f s cpu\n"):format(n, dt))
end

if arg and arg[0] and arg[0]:match("interpreter%.lua$") and arg[1] then
  main(arg[1], arg[2])
end

return M
