-- Check interpreter.lua against IR conformance vector files (section 8.4).
--
--   luajit scripts/ir_lua_conformance.lua tests/conformance/ir-v1/*.jsonl
--
-- A "donor" line holds the donor IR and donor words of a contact entry (3.5.1).
-- A "case" line is a transcription and a "syllables" line the written
-- syllables of S5. For each file it prints N in, N pass and every failed
-- case, then a total.
-- The exit status is 1 when a case fails.
local here = (arg[0]:match("^(.*)/[^/]*$") or ".")
package.path = here .. "/../orthography2ipa/ir/?.lua;" .. package.path
local M = require("interpreter")

local function same(a, b)
  if #a ~= #b then return false end
  for i = 1, #a do if a[i] ~= b[i] then return false end end
  return true
end

local function cps(t) return table.concat(t, " ") end

local total, passed = 0, 0
for i = 1, #arg do
  local f = assert(io.open(arg[i], "rb"))
  local it, err
  local donors = {}
  local n, ok = 0, 0
  for line in f:lines() do
    local rec = M.json_decode(line)
    if rec.kind == "donor" then
      local words = {}
      for _, p in ipairs(rec.words) do words[M.from_cps(p[1])] = M.from_cps(p[2]) end
      local lang = {}
      for k = 1, #rec.lang do lang[k] = rec.lang:byte(k) end
      donors[M.from_cps(lang)] = {M.new(rec.ir), words}
    elseif rec.kind == "ir" then
      local good, res = pcall(M.new, rec.ir, donors)
      if good then it, err = res, nil else it, err = nil, tostring(res) end
    else
      n = n + 1
      local good, res
      if not it then
        good, res = false, err
      elseif rec.kind == "syllables" then
        good, res = pcall(function()
          local out = {}
          for k, s in ipairs(it:syllables(M.from_cps(rec.input))) do out[k] = M.to_cps(s) end
          return out
        end)
      else
        good, res = pcall(it.transcribe_cps, it, rec.input, 1)
      end
      local pass
      if rec.expect_error then
        pass = not good and string.find(tostring(res), rec.expect_error, 1, true) ~= nil
      elseif rec.kind == "syllables" then
        pass = good and #res == #rec.expect
        for k = 1, pass and #res or 0 do pass = pass and same(res[k], rec.expect[k]) end
        if good then
          local parts = {}
          for k, s in ipairs(res) do parts[k] = cps(s) end
          res = {table.concat(parts, " | ")}
        end
      else
        pass = good and same(res, rec.expect)
      end
      if pass then
        ok = ok + 1
      else
        io.write(("  FAIL %s case %d: input [%s] got %s\n"):format(arg[i], n, cps(rec.input),
          good and ("[" .. cps(res) .. "]") or ("error " .. tostring(res))))
      end
    end
  end
  f:close()
  io.write(("%s: N in %d, N pass %d, N fail %d\n"):format(arg[i], n, ok, n - ok))
  total, passed = total + n, passed + ok
end
io.write(("total: files %d, N in %d, N pass %d, N fail %d\n"):format(#arg, total, passed, total - passed))
os.exit(passed == total and 0 or 1)
